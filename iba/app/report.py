"""report.py — the word-raw output. CONFIG-GOVERNED.

What the report shows is read from config (cfg_setting report.*): how many sample
verses, whether the verse text appears, which columns per section. This module only
knows HOW to render a section (a markdown table) — a report shape, not a choice.

    python -m iba.app.report --word hypocrisy
"""

from __future__ import annotations

import argparse
import pathlib

from .lib import reportkit
from .lib.cfg import Cfg, DB_PATH
from .lib.db import Db
from .lib.stepapi import strip_html

B = "http://localhost:8989"


def esc(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def clip(s, n) -> str:
    s = esc(s)
    return s if len(s) <= n else s[: n - 1] + "…"


# how to fetch a field's value — the only per-field code; the LIST of fields is config
def _strong_val(db, code, field):
    s = db.get("strong", strongNumber=code) or {}
    if field in ("stepGloss", "accentedUnicode", "stepTransliteration", "count"):
        return s[field] if field in s.keys() else ""
    if field == "head":
        se = db.get("strong_sense", strong=code)
        return f"**{clip(se['head'], 34)}**" if se else ""
    if field == "verses":
        return db.count("strong_verse", strong=code)
    return ""


def _span_val(db, sp, field, held):
    if field in ("position", "surface", "strong_variant", "morph_code"):
        v = sp[field] if field in sp.keys() else ""
        return f"`{esc(v)}`" if field in ("strong_variant", "morph_code") else esc(v)
    if field == "is_particle":
        return "·" if sp["is_particle"] else ""
    if field == "sense":
        se = db.get("strong_sense", strong=sp["strong_variant"])
        return f"**{clip(se['head'], 24)}**" if (sp["strong_variant"] in held and se) else ""
    return ""


def generate(word: str, cfg: Cfg | None = None) -> pathlib.Path | None:
    """Build the word-raw report and write it to config-governed output_dir/output_pattern.
    Returns the path, or None if the word isn't in the DB. Split out from main() 2026-07-21 so
    this can be called as a dispatcher step (handlers/reports.py), not only as a standalone CLI."""
    own_cfg = cfg is None
    cfg = cfg or Cfg()
    db = Db(cfg)

    # ── config: what to show ──
    sample_n = int(cfg.setting("report.sample_verses", 3))
    show_text = bool(cfg.setting("report.show_verse_text", True))
    show_val = bool(cfg.setting("report.show_validation", True))
    strong_fields = cfg.setting("report.strong_fields", ["stepGloss", "head", "count", "verses"])
    span_fields = cfg.setting("report.span_fields",
                              ["position", "surface", "strong_variant", "morph_code", "is_particle", "sense"])
    output_dir = cfg.setting("report.output_dir", "iba/app")
    output_pattern = cfg.setting("report.output_pattern", "report-{word}.md")

    w = db.get("word_registry", word=word)
    if not w:
        if own_cfg:
            db.close(); cfg.close()
        return None
    wid = w["id"]
    strongs = [r["strong"] for r in db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? ORDER BY strong", (wid,))]
    ph = ",".join("?" * len(strongs))
    held = set(strongs)

    intro = [
        f"> Built by the IBA app into `{DB_PATH.relative_to(pathlib.Path.cwd())}`. "
        f"What this report shows is config (`cfg_setting report.*`). Every row is checkable "
        f"against STEP.", "",
        f"**word_registry** — id {wid} · status `{w['status']}` · source {esc(w['source'])}",
    ]

    sections: dict[str, list[str]] = {}

    # ── validation (util.validation) — show_val OWNS inclusion, not cfg_report_section ──
    if show_val:
        vr = db.rows("SELECT check_name, result, detail, ran_at FROM validation_result "
                     "WHERE word=? ORDER BY id", (word,))
        if vr:
            S = ["| check | result | detail |", "|---|---|---|"]
            for r in vr:
                mark = "✓ pass" if r["result"] == "pass" else "✗ **FAIL**"
                S.append(f"| {r['check_name']} | {mark} | {clip(r['detail'], 70)} |")
        else:
            S = ["_No validation recorded — raw.validate has not run for this word._"]
        sections["validation"] = S

    # ── strongs and their meaning ──
    S = ["| strong | " + " | ".join(strong_fields) + " |",
         "|---|" + "---|" * len(strong_fields)]
    for code in strongs:
        S.append("| `" + code + "` | " +
                 " | ".join(str(_strong_val(db, code, f)) for f in strong_fields) + " |")
    sections["strongs"] = S

    # ── sample verses — the span layer, with verse text if config says so ──
    sample = db.rows(
        f"SELECT v.* FROM verse v JOIN strong_verse sv ON sv.verse_id=v.id "
        f"WHERE sv.strong IN ({ph}) GROUP BY v.id "
        f"ORDER BY (SELECT COUNT(*) FROM span s WHERE s.verse_id=v.id) DESC LIMIT ?",
        strongs + [sample_n])
    S = []
    all_spans = []
    for v in sample:
        S += [f"### {v['reference']} — `{v['osisId']}`", ""]
        if show_text:                                     # <- config toggle
            S += [f"> {clip(strip_html(v['preview']), 400)}", ""]
        spans = db.rows("SELECT * FROM span WHERE verse_id=? ORDER BY position", (v["id"],))
        all_spans += spans
        S += ["| " + " | ".join(span_fields) + " |", "|" + "---|" * len(span_fields)]
        for sp in spans:
            S.append("| " + " | ".join(str(_span_val(db, sp, f, held)) for f in span_fields) + " |")
        S += [""]
    sections["sample_verses"] = S

    out_dir = pathlib.Path(output_dir)
    out = out_dir / output_pattern.format(word=word)
    L = reportkit.render_scaffold(db.conn, "report.word", sections, intro=intro, word=word)
    word_strong_rows = db.rows("SELECT * FROM word_strong WHERE word_id=?", (wid,))
    reportkit.write_csv_pairing(db.conn, "report.word", out_dir / "export",
                                row_filter={"span": all_spans, "word_strong": word_strong_rows})
    text = "\n".join(L).rstrip() + "\n"
    reportkit.write_report(db.conn, "report.word", out, text.splitlines())
    if own_cfg:
        db.close(); cfg.close()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--word", required=True)
    a = ap.parse_args()
    out = generate(a.word)
    if out is None:
        print(f"{a.word!r} not in the DB.")
        return 1
    print(f"wrote {out.relative_to(pathlib.Path.cwd()) if out.is_absolute() else out}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
