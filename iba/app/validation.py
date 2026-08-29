"""validation.py — the raw-layer validation report. Read-only.

Computes, for a word, whether the raw build is correct and complete, whether the store is
sound, and whether the run succeeded, and writes a markdown report. It does NOT change the
gate (raw.validate stays the authoritative stop) — it REPORTS.

    python -m iba.app.validation --word malice        # -> iba/app/reports/validation-malice.md

Checks are config-driven where they can be: integrity (notnull, dedup keys) and references
(fk columns) are generated from cfg_column, so a new column is checked automatically. Only
the semantic expectations are stated explicitly.
"""

from __future__ import annotations

import argparse
import datetime
import pathlib
import sys

from .lib.cfg import Cfg
from .lib.db import Db
from .lib import reportkit, valuequality as vq

_SECTION_KEY = {
    "1. App & DB": "app_db", "2. Pre/post": "pre_post", "3. Integrity": "integrity",
    "4. References": "references", "5. Expectations": "expectations",
    "6. Value quality": "value_quality", "3. Candidate (L4b)": "candidate",
    "4. Passages": "passages",
}

CONTROL = {"run", "validation_result", "escalation"}   # not raw study tables


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Check:
    __slots__ = ("section", "name", "expected", "actual", "verdict", "detail")

    def __init__(self, section, name, expected, actual, verdict, detail=""):
        self.section, self.name = section, name
        self.expected, self.actual, self.verdict, self.detail = expected, actual, verdict, detail


def _raw_tables(cfg: Cfg) -> list[str]:
    return [t for t in cfg.tables() if t not in CONTROL]


# ── section 1: app & DB running success ──────────────────────────────────────
def _health(cfg: Cfg, db: Db, word: str) -> list[Check]:
    out = []
    ver = cfg.config_version()
    out.append(Check("1. App & DB", "config loaded", "a config_version", ver,
                     "PASS" if ver and ver != "?" else "FAIL"))
    have = {r[0] for r in db.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    missing = [t for t in cfg.tables() if t not in have]
    out.append(Check("1. App & DB", "data tables present", f"{len(cfg.tables())} tables",
                     f"{len(cfg.tables()) - len(missing)} present",
                     "PASS" if not missing else "FAIL", ", ".join(missing)))
    try:
        from .lib.stepapi import Step, StepUnavailable
        try:
            ev = Step(cfg).up()
            out.append(Check("1. App & DB", "STEP known-answer", "expected answer",
                             f"{ev['resolved']} {ev['gloss']!r}, {ev['verses']} verses", "PASS"))
        except StepUnavailable as e:
            out.append(Check("1. App & DB", "STEP known-answer", "up + tagged", "not ready", "FAIL", str(e)))
    except Exception as e:  # never let the report die on STEP
        out.append(Check("1. App & DB", "STEP known-answer", "up + tagged", "error", "WARN", str(e)))
    run = db.rows("SELECT run_id, state FROM run WHERE lower(runs_over)=lower(?) "
                  "ORDER BY id DESC LIMIT 1", (word,))
    st = run[0]["state"] if run else "(no run)"
    out.append(Check("1. App & DB", "latest run complete", "done", st,
                     "PASS" if st == "done" else "FAIL",
                     run[0]["run_id"] if run else ""))
    return out, (run[0]["run_id"] if run else None)


# ── section 2: pre/post delta (from the run's snapshots) ─────────────────────
def _delta(db: Db, run_id: str | None) -> list[list]:
    if not run_id:
        return []
    def snap(phase):
        return {r["check_name"].split(":", 1)[1]: int(r["detail"]) for r in db.rows(
            "SELECT check_name, detail FROM validation_result "
            "WHERE run_id=? AND step='snapshot' AND check_name LIKE ?", (run_id, f"{phase}:%"))}
    pre, post = snap("pre"), snap("post")
    rows = []
    for t in sorted(set(pre) | set(post)):
        a, b = pre.get(t, 0), post.get(t, 0)
        rows.append([t, a, b, b - a])
    return rows


# ── section 3: integrity (config-derived) ────────────────────────────────────
def _integrity(cfg: Cfg, db: Db) -> list[Check]:
    out = []
    for t in _raw_tables(cfg):
        for c in cfg.columns(t):
            if c["notnull"]:
                n = db.rows(f'SELECT COUNT(*) n FROM "{t}" WHERE "{c["name"]}" IS NULL')[0]["n"]
                out.append(Check("3. Integrity", f"{t}.{c['name']} not-null", "0 NULL", f"{n} NULL",
                                 "PASS" if n == 0 else "FAIL"))
        key = cfg.unique_key(t)
        if key:
            cols = ", ".join(f'"{k}"' for k in key)
            d = db.rows(f'SELECT COUNT(*) n FROM (SELECT {cols} FROM "{t}" WHERE deleted=0 '
                        f'GROUP BY {cols} HAVING COUNT(*)>1)')[0]["n"] if "deleted" in cfg.column_names(t) \
                else db.rows(f'SELECT COUNT(*) n FROM (SELECT {cols} FROM "{t}" '
                             f'GROUP BY {cols} HAVING COUNT(*)>1)')[0]["n"]
            out.append(Check("3. Integrity", f"{t} dedup key ({', '.join(key)})", "0 dup", f"{d} dup",
                             "PASS" if d == 0 else "FAIL"))
    return out


# ── section 4: references (fk resolvability) ─────────────────────────────────
def _references(cfg: Cfg, db: Db) -> list[Check]:
    out = []
    for t in _raw_tables(cfg):
        for c in cfg.columns(t):
            if not c["fk"]:
                continue
            rt, rc = c["fk"].split(".")
            orphans = db.rows(
                f'SELECT COUNT(*) n FROM "{t}" a WHERE a."{c["name"]}" IS NOT NULL '
                f'AND NOT EXISTS (SELECT 1 FROM "{rt}" b WHERE b."{rc}"=a."{c["name"]}")')[0]["n"]
            # FK -> strong may orphan by design (the raw model names strongs it need not hold)
            soft = rt == "strong"
            verdict = "PASS" if orphans == 0 else ("WARN" if soft else "FAIL")
            out.append(Check("4. References", f"{t}.{c['name']} -> {rt}.{rc}", "0 orphan",
                             f"{orphans} orphan", verdict,
                             "expected for the raw model" if soft and orphans else ""))
    return out


# ── section 5: expectations vs actual ────────────────────────────────────────
def _expectations(cfg: Cfg, db: Db, word: str) -> list[Check]:
    out = []
    reg = db.rows("SELECT * FROM word_registry WHERE lower(word)=lower(?) AND deleted=0", (word,))
    if not reg:
        return [Check("5. Expectations", "registry entry", "1 row", "0", "FAIL", "word not registered")]
    r = reg[0]
    wid = r["id"]
    out.append(Check("5. Expectations", "registry built", "raw-complete", r["status"],
                     "PASS" if r["status"] == "raw-complete" else "FAIL"))
    out.append(Check("5. Expectations", "registry source set", "non-empty",
                     "set" if r["source"] else "empty", "PASS" if r["source"] else "WARN"))

    ws = db.rows("SELECT strong FROM word_strong WHERE word_id=? AND deleted=0", (wid,))
    import re
    pat = re.compile(cfg.setting("discovery.particle_pattern", r"^[HG]9\d{3}$"))
    parts = [x["strong"] for x in ws if pat.match(x["strong"])]
    out.append(Check("5. Expectations", "word_strong present", ">=1", str(len(ws)),
                     "PASS" if ws else "FAIL"))
    out.append(Check("5. Expectations", "word_strong non-particle", "0 particles", f"{len(parts)}",
                     "PASS" if not parts else "FAIL", ", ".join(parts)))

    no_sense = db.rows("SELECT COUNT(*) n FROM strong s WHERE s.deleted=0 AND NOT EXISTS "
                       "(SELECT 1 FROM strong_sense ss WHERE ss.strong=s.strongNumber)")[0]["n"]
    out.append(Check("5. Expectations", "every strong has a sense", "0 missing", f"{no_sense} missing",
                     "PASS" if no_sense == 0 else "FAIL"))

    # parse-check: span recovers every strong_verse, per this word's strongs
    missed = []
    for x in ws:
        code = x["strong"]
        asserted = {v["verse_id"] for v in db.rows(
            "SELECT verse_id FROM strong_verse WHERE strong=? AND deleted=0", (code,))}
        parsed = {v["verse_id"] for v in db.rows(
            "SELECT DISTINCT verse_id FROM span WHERE strong_variant=? AND deleted=0", (code,))}
        if asserted - parsed:
            missed.append(f"{code}:{len(asserted - parsed)}")
    out.append(Check("5. Expectations", "span recovers strong_verse", "0 missed",
                     f"{len(missed)} strong(s) missed", "PASS" if not missed else "FAIL",
                     "; ".join(missed)))

    dup_osis = db.rows("SELECT COUNT(*) n FROM (SELECT osisId FROM verse GROUP BY osisId "
                       "HAVING COUNT(*)>1)")[0]["n"]
    out.append(Check("5. Expectations", "verse.osisId unique", "0 dup", f"{dup_osis} dup",
                     "PASS" if dup_osis == 0 else "FAIL"))
    return out


# ── section 6: value quality (config-derived — cfg_column.expectation, scoped to this word) ──
def _value_quality_word(cfg: Cfg, word_id: int, word: str) -> list[Check]:
    """Per-word value-quality — the same generic engine candidate.validate uses (lib/
    valuequality), scoped to just this word's strongs/spans/registry row, so a word reviewer sees
    it here without running the standalone candidate-quality check over the whole programme."""
    out = []
    scoped = (
        ("strong_sense", "head",
         "strong IN (SELECT strong FROM word_strong WHERE word_id=?)"),
        ("span", "surface",
         "verse_id IN (SELECT verse_id FROM strong_verse WHERE strong IN "
         "(SELECT strong FROM word_strong WHERE word_id=?))"),
    )
    for table, column, where in scoped:
        exp = cfg.conn.execute("SELECT expectation FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
                               (table, column)).fetchone()
        if not exp or not exp["expectation"]:
            continue
        f = vq.scan_column(cfg, table, column, exp["expectation"], where, (word_id,))
        if not f:
            continue
        out.append(Check("6. Value quality", f"{table}.{column} ({f.rule})", "0 violations",
                         f"{f.violations}/{f.total}", "PASS" if not f.violations else "WARN",
                         "; ".join(repr(v) for v, _ in f.samples[:3]) if f.violations else ""))
    exp = cfg.conn.execute(
        "SELECT expectation FROM cfg_column WHERE database='iba' AND table_name='word_registry' "
        "AND name='word'").fetchone()
    if exp and exp["expectation"]:
        f = vq.scan_column(cfg, "word_registry", "word", exp["expectation"], "id=?", (word_id,))
        if f:
            out.append(Check("6. Value quality", f"word_registry.word ({f.rule})", "0 violations",
                             f"{f.violations}/{f.total}", "PASS" if not f.violations else "FAIL",
                             word if f.violations else ""))
    return out


def _value_quality_book(cfg: Cfg, book: str) -> list[Check]:
    """Book-scoped span.surface (this book's verses) + programme-wide candidate_seed.tag/
    lemma_inventory.gloss context (those tables aren't book-local — informational, full detail in
    candidate-quality.md)."""
    out = []
    like = f"{book}.%"
    exp = cfg.conn.execute(
        "SELECT expectation FROM cfg_column WHERE database='iba' AND table_name='span' "
        "AND name='surface'").fetchone()
    if exp and exp["expectation"]:
        f = vq.scan_column(cfg, "span", "surface", exp["expectation"],
                           "verse_id IN (SELECT id FROM verse WHERE osisId LIKE ?)", (like,))
        if f:
            out.append(Check("6. Value quality", f"span.surface ({f.rule}, this book)",
                             "0 violations", f"{f.violations}/{f.total}",
                             "PASS" if not f.violations else "WARN"))
    for table, column in (("candidate_seed", "tag"), ("lemma_inventory", "gloss")):
        exp = cfg.conn.execute("SELECT expectation FROM cfg_column WHERE database='iba' AND table_name=? AND name=?",
                               (table, column)).fetchone()
        if exp and exp["expectation"]:
            f = vq.scan_column(cfg, table, column, exp["expectation"])
            if f:
                out.append(Check("6. Value quality", f"{table}.{column} ({f.rule}, programme-wide)",
                                 "0 violations", f"{f.violations}/{f.total}",
                                 "PASS" if not f.violations else "WARN",
                                 "see candidate-quality.md for detail"))
    return out


def _tbl(headers, rows):
    L = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        L.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return L


def _mark(v):
    return {"PASS": "✓ PASS", "FAIL": "✗ FAIL", "WARN": "⚠ WARN"}.get(v, v)


_WORD_SECTIONS = {                          # section label -> the cfg_setting toggle that shows it
    "1. App & DB": "validation.show_health",
    "2. Pre/post": "validation.show_delta",
    "3. Integrity": "validation.show_integrity",
    "4. References": "validation.show_references",
    "5. Expectations": "validation.show_expectations",
    "6. Value quality": "validation.show_value_quality",
}


def generate(word: str) -> pathlib.Path:
    cfg = Cfg()
    db = Db(cfg)
    output_dir = pathlib.Path(cfg.required_setting("validation.output_dir"))
    shown = {sec: bool(cfg.setting(key, True)) for sec, key in _WORD_SECTIONS.items()}

    reg = db.rows("SELECT id FROM word_registry WHERE lower(word)=lower(?) AND deleted=0", (word,))
    health, run_id = _health(cfg, db, word)
    checks = health + _integrity(cfg, db) + _references(cfg, db) + _expectations(cfg, db, word)
    if reg:
        checks += _value_quality_word(cfg, reg[0]["id"], word)
    delta = _delta(db, run_id)

    fails = sum(1 for c in checks if c.verdict == "FAIL")
    warns = sum(1 for c in checks if c.verdict == "WARN")
    passes = sum(1 for c in checks if c.verdict == "PASS")
    overall = "FAIL" if fails else ("WARN" if warns else "PASS")

    intro = [
        f"> Generated {_now()} · run `{run_id or '(none)'}`. Read-only; the authoritative gate is "
        f"`raw.validate`. Sections shown are config-governed (`cfg_setting validation.show_*`).", "",
        f"## Verdict: {_mark(overall)}   ({passes} pass · {warns} warn · {fails} fail)",
    ]

    sections: dict[str, list[str]] = {}
    for sec in ("1. App & DB", "2. Pre/post", "3. Integrity", "4. References", "5. Expectations",
               "6. Value quality"):
        if not shown[sec]:
            continue
        if sec == "2. Pre/post":
            S = (_tbl(["table", "pre", "post", "delta"], delta) if delta else
                 ["_no snapshots for this run (run predates snapshotting, or no run)._"])
        else:
            rows = [[_mark(c.verdict), c.name, c.expected, c.actual, c.detail]
                    for c in checks if c.section == sec]
            S = _tbl(["verdict", "check", "expected", "actual", "detail"], rows)
        sections[_SECTION_KEY[sec]] = S

    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"validation-{word}.md"
    L = reportkit.render_scaffold(db.conn, "validation.word", sections, intro=intro, word=word)
    if reg:
        word_strong_rows = db.rows("SELECT * FROM word_strong WHERE word_id=?", (reg[0]["id"],))
        strongs = [r["strong"] for r in word_strong_rows]
        ph = ",".join("?" * len(strongs)) or "''"
        span_rows = db.rows(
            f"SELECT DISTINCT sp.* FROM span sp JOIN strong_verse sv ON sv.verse_id=sp.verse_id "
            f"WHERE sv.strong IN ({ph})", strongs)
    else:
        word_strong_rows, span_rows = [], []
    reportkit.write_csv_pairing(db.conn, "validation.word", output_dir / "export",
                                row_filter={"span": span_rows, "word_strong": word_strong_rows})
    out = reportkit.write_report(db.conn, "validation.word", out, L)
    db.close()
    return out, overall, (passes, warns, fails)


def _base_checks(cfg: Cfg, db: Db, book: str) -> list[Check]:
    """Base-layer checks (candidate L4b + passages) for a book. Config-derived where it can be."""
    out = []
    like = f"{book}.%"
    S = "3. Candidate (L4b)"
    P = "4. Passages"
    q1 = lambda sql, pr=(): db.rows(sql, pr)[0]["n"]

    # candidate integrity
    orphan = q1("SELECT COUNT(*) n FROM span_candidate sc WHERE sc.deleted=0 AND NOT EXISTS "
                "(SELECT 1 FROM span sp WHERE sp.id=sc.span_id)")
    out.append(Check(S, "span_candidate -> span resolves", "0 orphan", f"{orphan} orphan",
                     "PASS" if orphan == 0 else "FAIL"))
    badinv = q1("SELECT COUNT(*) n FROM candidate_seed cs WHERE cs.deleted=0 AND NOT EXISTS "
                "(SELECT 1 FROM lemma_inventory li WHERE li.lemma_key=cs.lemma_key)")
    out.append(Check(S, "candidate_seed -> lemma_inventory", "0 orphan", f"{badinv} orphan",
                     "PASS" if badinv == 0 else "FAIL"))
    stamped = q1("SELECT COUNT(*) n FROM span_candidate sc JOIN span sp ON sp.id=sc.span_id "
                 "JOIN verse v ON v.id=sp.verse_id WHERE v.osisId LIKE ? AND sc.deleted=0", (like,))
    out.append(Check(S, "candidate spans stamped (book)", ">=0", str(stamped), "PASS"))
    missing = q1("SELECT COUNT(*) n FROM candidate_seed WHERE decision='candidate' "
                 "AND registry_match IS NULL AND deleted=0")
    out.append(Check(S, "candidate missing registry words (double control)", "informational",
                     f"{missing} lemma(s)", "WARN" if missing else "PASS",
                     "candidate lemmas no registry word carries — grow the registry"))

    # passages
    pc = q1("SELECT COUNT(*) n FROM passage WHERE book=? AND deleted=0", (book,))
    unpass = q1("SELECT COUNT(DISTINCT sp.verse_id) n FROM span_candidate sc "
                "JOIN span sp ON sp.id=sc.span_id JOIN verse v ON v.id=sp.verse_id "
                "WHERE v.osisId LIKE ? AND sc.deleted=0 AND NOT EXISTS "
                "(SELECT 1 FROM verse_passage vp WHERE vp.verse_id=sp.verse_id)", (like,))
    out.append(Check(P, "candidate-bearing verses unpassaged", "0", f"{unpass}",
                     "PASS" if unpass == 0 else "FAIL", "completeness gate"))
    dup = q1("SELECT COUNT(*) n FROM (SELECT vp.verse_id FROM verse_passage vp JOIN verse v "
             "ON v.id=vp.verse_id WHERE v.osisId LIKE ? GROUP BY vp.verse_id HAVING COUNT(*)>1)", (like,))
    out.append(Check(P, "verse in at most one passage", "0 dup", f"{dup} dup",
                     "PASS" if dup == 0 else "FAIL"))
    anc = q1("SELECT COUNT(*) n FROM verse_passage vp JOIN passage p ON p.id=vp.passage_id "
             "WHERE p.book=? AND vp.is_anchor=1", (book,))
    out.append(Check(P, "anchors = passage count", str(pc), str(anc), "PASS" if anc == pc else "FAIL"))
    cross = q1("SELECT COUNT(*) n FROM passage WHERE book=? AND start_chapter<>end_chapter", (book,))
    out.append(Check(P, "passages do not cross chapters", "0", f"{cross}",
                     "PASS" if cross == 0 else "FAIL"))
    nr = q1("SELECT COUNT(*) n FROM passage WHERE book=? AND needs_review=1", (book,))
    out.append(Check(P, f"passages needing review (> review_over verses)", "reviewed", f"{nr} flagged",
                     "WARN" if nr else "PASS", "a long run may be several passages — confirm the rule"))
    return out


_BOOK_SECTIONS = {
    "1. App & DB": "validation.show_health",
    "3. Candidate (L4b)": "validation.show_candidate",
    "4. Passages": "validation.show_passages",
    "6. Value quality": "validation.show_value_quality",
}


def generate_book(book: str) -> tuple:
    cfg = Cfg()
    db = Db(cfg)
    output_dir = pathlib.Path(cfg.required_setting("validation.output_dir"))
    shown = {sec: bool(cfg.setting(key, True)) for sec, key in _BOOK_SECTIONS.items()}

    health, _ = _health(cfg, db, book)
    # keep only the app/DB rows from health (drop the word-run row, which is word-scoped)
    health = [c for c in health if c.name != "latest run complete"]
    checks = health + _base_checks(cfg, db, book) + _value_quality_book(cfg, book)
    fails = sum(1 for c in checks if c.verdict == "FAIL")
    warns = sum(1 for c in checks if c.verdict == "WARN")
    passes = sum(1 for c in checks if c.verdict == "PASS")
    overall = "FAIL" if fails else ("WARN" if warns else "PASS")

    intro = [
        f"> Generated {_now()}. Read-only. Candidate (L4b) + passages. Sections shown are "
        f"config-governed (`cfg_setting validation.show_*`).", "",
        f"## Verdict: {_mark(overall)}   ({passes} pass · {warns} warn · {fails} fail)",
    ]
    sections: dict[str, list[str]] = {}
    for sec in ("1. App & DB", "3. Candidate (L4b)", "4. Passages", "6. Value quality"):
        if not shown[sec]:
            continue
        rows = [[_mark(c.verdict), c.name, c.expected, c.actual, c.detail]
                for c in checks if c.section == sec]
        if not rows:
            continue
        sections[_SECTION_KEY[sec]] = _tbl(
            ["verdict", "check", "expected", "actual", "detail"], rows)

    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"validation-book-{book}.md"
    L = reportkit.render_scaffold(db.conn, "validation.book", sections, intro=intro, book=book)
    like = f"{book}.%"
    candidate_seed_rows = db.rows(
        "SELECT cs.* FROM candidate_seed cs WHERE cs.deleted=0 AND EXISTS (SELECT 1 FROM "
        "span sp JOIN verse v ON v.id=sp.verse_id WHERE v.osisId LIKE ? AND sp.strong_variant="
        "cs.strong_variant)", (like,))
    passage_rows = db.rows("SELECT * FROM passage WHERE book=? AND deleted=0", (book,))
    verse_passage_rows = db.rows(
        "SELECT vp.* FROM verse_passage vp JOIN passage p ON p.id=vp.passage_id WHERE p.book=?",
        (book,))
    reportkit.write_csv_pairing(db.conn, "validation.book", output_dir / "export",
                                row_filter={"candidate_seed": candidate_seed_rows,
                                           "passage": passage_rows,
                                           "verse_passage": verse_passage_rows})
    out = reportkit.write_report(db.conn, "validation.book", out, L)
    db.close()
    return out, overall, (passes, warns, fails)


def main() -> int:
    ap = argparse.ArgumentParser(description="Validation report — raw layer (--word) or base layer (--book).")
    ap.add_argument("--word")
    ap.add_argument("--book")
    a = ap.parse_args()
    if not a.word and not a.book:
        ap.error("give --word or --book")
    out, overall, (p, w, f) = generate_book(a.book) if a.book else generate(a.word)
    print(f"{overall}  ({p} pass · {w} warn · {f} fail)  -> {out}")
    return 0 if overall != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
