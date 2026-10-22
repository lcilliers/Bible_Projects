"""catchup_october_ledgers_2172_v1_20261022.py -- escalation #2172 catch-up B
(outputs/escalation/2172-catch-up-plan-v1-20261022.md section 2 B; decisions in
outputs/escalation/2172-catch-up-answers-v1-20261022.md and #2172 v26-v29).

The October row ledgers (1 to 5 October) moved into the tables as they were approved, through the
reading process's own steps (lib/strandreading.py): no verse is read anew and no narrative is written.

1. One strand per October strand (Define): its words are the Strong's codes of its unit pulls, its
   home cluster, its October escalation. Context writes its hits and records the open items that
   match it (#2219).
2. Each ledger row becomes one observation (Record): the head is the text, the ledger's parts go to
   their columns (setting, meaning, implication, chain, parties), S/R becomes stated/read (a row
   marked both is 'read': it carries a reading), each verse is grounded on the strand words in it.
   The ledger ID is kept as stable_key '<strand>:<ID>'; the October disposition, and the row's
   touches, placement or 'also appears', in revisit_note. Status stays draft until step C.
3. A face from a unit pull (with the faces file's parties for anger) goes onto its hit.
4. Left out and listed, never guessed: a row that does not parse; a row with no basis; a verse with
   no strand word in it (#2216; a row left with no verse is not imported); a hit with no face (#2217);
   a quotation not in its verse.

Run on a dbsnapshot copy first (--db <copy>): the report is the dry run. Live only when the report
is accepted. Also restates the use of ib_observation.stable_key and revisit_note (cfg_column) and
registers itself in cfg_utility (inactive), through configmaint.apply_logged. One transaction.

Usage:
    python iba/app/migration/catchup_october_ledgers_2172_v1_20261022.py --db PATH --report PATH [--strand CODE]
"""
import argparse
import collections
import csv
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
if not (ROOT / "iba").is_dir():
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import narrativeregister as nr  # noqa: E402
from iba.app.lib import strandreading as sr  # noqa: E402

MODULE = "catchup_october_ledgers_2172_v1_20261022"
RUN = "CATCHUP-2172-B-20261022"
A = ROOT / "_analytics"
FEAR, ANGER, LD = A / "Clusters/M01 - fear-awe", A / "Clusters/M02 - anger-wrath", A / "Clusters/M25 - life-death"
OT = A / "cross-cluster-web/origin-of-thought"

STRANDS = [
    {"code": "fear", "title": "Fear", "cluster": "M01", "escalation": 1962,
     "pulls": sorted(FEAR.glob("fear-unit*pull*.csv")), "faces": [],
     "ledgers": sorted(FEAR.glob("fear-observation-ledger-*.md"))},
    {"code": "anger", "title": "Anger", "cluster": "M02", "escalation": 1963,
     "pulls": sorted(ANGER.glob("anger-unit*pull*.csv")), "faces": sorted(ANGER.glob("anger-unit*-faces-*.csv")),
     "ledgers": [ANGER / "anger-strand-observation-ledger-v1-20261001.md"] +
                sorted(ANGER.glob("anger-observation-ledger-unit*.md")) + [ANGER / "anger-m47-seat-ledger-v1-20261005.md"]},
    {"code": "life-death", "title": "Life and death", "cluster": "M25", "escalation": 1932,
     "pulls": sorted(LD.glob("life-death-unit*pull*.csv")), "faces": [],
     "ledgers": sorted(LD.glob("life-death-observation-ledger-unit*.md")) +
                [LD / "life-death-q2-q3-soul-spirit-heart-ledger-v1-20261004.md",
                 LD / "life-death-q4-body-resurrection-ledger-v1-20261002.md"]},
    {"code": "origin-of-thought", "title": "Origin of thought", "cluster": "M64", "escalation": 1918,
     "pulls": [OT / "change-of-character-thought-words-pull-v1-20261001.csv"], "faces": [],
     "ledgers": [OT / "origin-of-thought-observation-ledger-v2-20261001.md"]},
]
ID_RE = re.compile(r"^[A-Z][A-Za-z0-9]*-\d+[a-z]?$")
CFG_USE = {"stable_key": "the generating JSON file's own name; for a strand-reading observation imported from a "
                         "ledger (#2172 catch-up), '<strand>:<ledger ID>'",
           "revisit_note": "synthesis stage; for a strand-reading observation, its disposition note (#2172): the "
                           "October disposition and the row's touches until step C sets the status, then the claim, "
                           "item or reason"}


def rel(p: pathlib.Path) -> str:
    return p.relative_to(ROOT).as_posix()


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def role(h: str) -> str | None:
    h = h.lower().strip()
    for key, r in (("verses", "verses"), ("basis", "basis"), ("chain", "chain"), ("parties", "parties"),
                   ("also appears", "also"), ("disp", "disposition"), ("touches", "touches"), ("from", "from"),
                   ("placement", "placement"), ("setting · meaning", "smi"), ("meaning in setting", "meaning"),
                   ("observation", "text"), ("what the verse", "text")):
        if h.startswith(key):
            return r
    return None


def parse_ledger(path: pathlib.Path) -> tuple[list[dict], list[str]]:
    """Every row of every observation table (an id column, a verses column)."""
    rows, problems, lines = [], [], path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines) - 1:
        head, sep = lines[i], lines[i + 1]
        if head.startswith("|") and re.match(r"^\|\s*:?-{3}", sep):
            hs = cells(head)
            roles = [role(h) for h in hs[1:]]
            i += 2
            if hs[0].lower() not in ("id", "#") or "verses" not in roles:
                continue
            while i < len(lines) and lines[i].startswith("|"):
                cs = cells(lines[i])
                i += 1
                if not ID_RE.match(cs[0].strip("*")):
                    continue
                if len(cs) != len(hs):
                    problems.append(f"{rel(path)} {cs[0]}: {len(cs)} cells for {len(hs)} columns")
                    continue
                rows.append({"id": cs[0].strip("*"), "file": rel(path),
                             **{r: c for r, c in zip(roles, cs[1:]) if r}})
            continue
        i += 1
    return rows, problems


def clean(s: str | None) -> str | None:
    s = re.sub(r"\*+", "", s or "").strip()
    return None if s in ("", "—", "-", "–") else s


def head_and_rest(cell: str) -> tuple[str, str]:
    m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", cell.strip(), re.S)
    if m:
        return clean(m.group(1)), clean(m.group(2)) or ""
    text = cell.strip()
    for m in re.finditer(r"[.!?]\s+", text):        # the first sentence end outside a quotation
        head = text[:m.start() + 1]
        if head.count('"') % 2 == 0 and head.count("“") == head.count("”"):
            return clean(head), clean(text[m.end():]) or ""
    return clean(text), ""


def split_smi(cell: str) -> dict:
    parts, cur = {}, None
    for tok in re.split(r"(\*\*(?:Setting|Meaning|Implies|Implication)s?:\*\*)", cell):
        m = re.match(r"\*\*(Setting|Meaning|Impl\w*)s?:\*\*", tok)
        if m:
            cur = {"Setting": "setting", "Meaning": "meaning"}.get(m.group(1), "implication")
        elif cur and tok.strip():
            parts[cur] = clean(tok)
    return parts or {"meaning": clean(cell)}


def basis_of(cell: str | None) -> str | None:
    marks = set(re.findall(r"\b([SR])\b", cell or ""))
    return {frozenset("S"): "stated", frozenset("R"): "read", frozenset("SR"): "read"}.get(frozenset(marks))


def to_observation(code: str, r: dict) -> dict:
    head, rest = head_and_rest(r.get("text") or "")
    o = {"key": r["id"], "stable_key": f"{code}:{r['id']}", "text": head, "basis": basis_of(r.get("basis")),
         "chain": clean(r.get("chain")), "parties": clean(r.get("parties"))}
    if r.get("smi"):
        o.update(split_smi(r["smi"]))
    elif r.get("meaning"):
        o["meaning"] = clean(r["meaning"])
    if not o.get("meaning"):                     # a one-cell ledger: the cell itself is what it means
        o["meaning"] = clean(r.get("text"))
    note =[f"October disposition: {clean(r.get('disposition'))}" if clean(r.get("disposition")) else
            "October disposition: none in the ledger"]
    note += [f"{lab}: {clean(r[k])}" for k, lab in (("touches", "touches"), ("also", "also appears"),
                                                    ("from", "from"), ("placement", "placement")) if clean(r.get(k))]
    o["note"] = f"{'; '.join(note)} ({r['file']})"
    return o


def strand_words(pulls: list[pathlib.Path]) -> list[str]:
    out = set()
    for f in pulls:
        for x in csv.DictReader(open(f, encoding="utf-8-sig")):
            out.add(x.get("strong") or x.get("variant"))
    return sorted(s for s in out if s)


def faces(conn, vx, s: dict) -> tuple[dict, list[str]]:
    """{(verse_id, strong): (face, parties)} from the unit pulls (faces files add parties)."""
    parties = {}
    for f in s["faces"]:
        for x in csv.DictReader(open(f, encoding="utf-8-sig")):
            if x.get("angry_one") or x.get("toward"):
                p = f"{x.get('angry_one') or '?'} toward {x.get('toward') or '?'}"
                parties[(x["reference"], x["position"])] = p + (f"; also {x['other_parties']}" if x.get("other_parties") else "")
    got, problems = collections.defaultdict(lambda: [set(), set()]), []
    for f in s["pulls"]:
        for x in csv.DictReader(open(f, encoding="utf-8-sig")):
            if not (x.get("face") or "").strip():
                continue
            refs = nr.parse_refs(x["reference"], vx)
            if len(refs) != 1 or refs[0].verse_id is None:
                problems.append(f"{rel(f)}: {x['reference']} is not one verse")
                continue
            k = (refs[0].verse_id, x["strong"])
            got[k][0].add(f"{x['face']}. {x['face_name']}".strip())
            if (x["reference"], x["position"]) in parties:
                got[k][1].add(parties[(x["reference"], x["position"])])
    return {k: ("; ".join(sorted(v[0])), "; ".join(sorted(v[1])) or None) for k, v in got.items()}, problems


def build(cfg, s: dict, report: list) -> dict:
    """The strand's Record file, and what is left out."""
    conn = cfg.conn
    vx = nr.VerseIndex(cfg)
    st = sr.strand(conn, s["code"])
    words = set(sr._strongs(conn, st["id"]))
    rows, problems = [], []
    for f in s["ledgers"]:
        r, p = parse_ledger(f)
        rows += r
        problems += p
    out = {"observations": [], "hits": []}
    no_word, no_basis, no_verse, chapters, seen = [], [], [], [], set()
    for r in rows:
        if r["id"] in seen:
            problems.append(f"{r['file']} {r['id']}: the ID is used twice in the strand's ledgers; the second left out")
            continue
        seen.add(r["id"])
        o = to_observation(s["code"], r)
        if not o["basis"]:
            no_basis.append(f"{r['id']} ({r['file']}): basis {r.get('basis')!r}")
            continue
        verses = []
        for ref in nr.parse_refs(r.get("verses") or "", vx):
            if ref.verse_id is None:
                chapters.append(f"{r['id']}: {ref.normalised} ({ref.kind})")
                continue
            osis = conn.execute("SELECT osisId FROM verse WHERE id=?", (ref.verse_id,)).fetchone()[0]
            here = [x[0] for x in conn.execute("SELECT DISTINCT strong FROM verse_lexical WHERE verse_id=? AND "
                                               "deleted=0", (ref.verse_id,)) if x[0] in words]
            if not here:
                no_word.append(f"{r['id']}: {ref.normalised}")
            verses += [{"verse": osis, "strong": w} for w in sorted(here)]
        if not verses:
            no_verse.append(f"{r['id']} ({r['file']}): {r.get('verses')}")
            continue
        out["observations"].append({**{k: v for k, v in o.items() if v is not None}, "verses": verses})
    fc, fprob = faces(conn, vx, s)
    problems += fprob
    hits = conn.execute("SELECT h.verse_id, h.strong, v.osisId FROM reading_strand_hit h JOIN verse v ON "
                        "v.id=h.verse_id WHERE h.strand_id=?", (st["id"],)).fetchall()
    have = {(h["verse_id"], h["strong"]): h["osisId"] for h in hits}
    for (vid, strong), (face, parties) in sorted(fc.items()):
        if (vid, strong) not in have:
            problems.append(f"face {face!r} on {strong} at verse {vid}: not a hit of the strand")
            continue
        out["hits"].append({"verse": have[(vid, strong)], "strong": strong, "face": face,
                            **({"parties": parties} if parties else {})})
    report += [f"## {s['code']} ({sr._cluster_name(conn, s['cluster'])}, #{s['escalation']})", "",
               f"- words: {len(words)}; hits: {len(hits)}; with a face from the pulls: {len(out['hits'])}; "
               f"left with no face (#2217): {len(hits) - len(out['hits'])}",
               f"- ledger rows: {len(rows)}; observations to record: {len(out['observations'])}",
               f"- rows with no basis, left out: {len(no_basis)}",
               f"- verses with no strand word, left out of the grounding (#2216): {len(no_word)}",
               f"- rows left with no grounded verse, not imported (#2216): {len(no_verse)}",
               f"- references that name no verse (a whole chapter, or no such verse), not groundable: {len(chapters)}",
               f"- rows or faces that did not parse: {len(problems)}", ""]
    for title, lst in (("Rows with no basis", no_basis), ("Rows with no grounded verse", no_verse),
                       ("Verses with no strand word", no_word), ("References that name no verse", chapters),
                       ("Did not parse", problems)):
        if lst:
            report += [f"### {title} ({len(lst)})", ""] + [f"- {x}" for x in lst] + [""]
    return out


def record_clean(cfg, s: dict, data: dict, folder: pathlib.Path, report: list) -> int:
    """Record; what Record refuses is listed and left out, and the rest recorded."""
    path = folder / f"{s['code']}-import.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    w = nr.Writer(cfg.conn, "strand_reading.record", "Claude")
    try:
        msg = sr.record(cfg, w, {"Strand": s["code"], "File": str(path)}, f"{RUN}-{s['code']}")
        report += [f"Recorded: {msg}", ""]
        return len(data["observations"])
    except nr.Refused as exc:
        errs = [x.strip() for x in str(exc).split("\n") if x.strip()]
    bad_obs, bad_hits, other = set(), set(), []
    for e in errs:
        m = re.match(r"observations\[\d+\] \(([^)]+)\)", e)
        h = re.match(r"hits\[(\d+)\]", e)
        if m:
            bad_obs.add(m.group(1))
        elif h:
            bad_hits.add(int(h.group(1)))
        elif not e.startswith(("the reading is not recorded", "quotation(s) not found")):
            other.append(e)
    report += [f"### Refused by Record and left out ({len(errs) - 2 if len(errs) > 2 else len(errs)})", ""] + \
              [f"- {e}" for e in errs if not e.startswith(("the reading is not recorded", "quotation(s) not found"))] + [""]
    if other:
        raise SystemExit(f"{s['code']}: Record refused for a reason not tied to a row: {other}")
    data = {"observations": [o for o in data["observations"] if o["key"] not in bad_obs],
            "hits": [h for i, h in enumerate(data["hits"]) if i not in bad_hits]}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    msg = sr.record(cfg, w, {"Strand": s["code"], "File": str(path)}, f"{RUN}-{s['code']}")
    report += [f"Recorded: {msg}", ""]
    return len(data["observations"])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--report", required=True)
    ap.add_argument("--strand")
    a = ap.parse_args()
    cfg = Cfg(pathlib.Path(a.db))
    conn = cfg.conn
    folder = pathlib.Path(a.report).with_suffix("")
    folder.mkdir(parents=True, exist_ok=True)
    report = ["# 2172 catch-up B: the October ledgers into the tables", "",
              f"Database: `{a.db}`. Script: `iba/app/migration/{MODULE}.py`. Import files: `{folder.name}/`.", ""]
    total = 0
    conn.execute("SAVEPOINT catchup")
    try:
        for name, use in CFG_USE.items():
            if not conn.execute("SELECT 1 FROM cfg_column WHERE table_name='ib_observation' AND name=? AND use=?",
                                (name, use)).fetchone():
                apply_logged(conn, RUN, "cfg_column", "update", {"database": "iba", "table_name": "ib_observation",
                                                                 "name": name}, {"use": use})
        if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (MODULE,)).fetchone():
            apply_logged(conn, RUN, "cfg_utility", "insert", {}, {
                "module": MODULE, "file_path": f"iba/app/migration/archive/{MODULE}.py", "inactive": 1,
                "config_exempt": 1, "config_exempt_reason": "one-off catch-up script (#2172 catch-up B), run once",
                "purpose": f"ONE-OFF -- escalation #2172 catch-up B: the October row ledgers into ib_observation "
                           f"through Strand-Reading Define, Context and Record; run_id {RUN}. inactive once run."})
        for s in STRANDS:
            if a.strand and s["code"] != a.strand:
                continue
            words = strand_words(s["pulls"])
            if not conn.execute("SELECT 1 FROM reading_strand WHERE code=?", (s["code"],)).fetchone():
                sr.define(cfg, nr.Writer(conn, "strand_reading.define", "Claude"), {
                    "Strand": s["code"], "Title": s["title"], "Cluster": s["cluster"],
                    "Escalation": str(s["escalation"]), "Strongs": ",".join(words),
                    "Note": "October words: the unit pulls (#2172 catch-up B)"})
            lines, console = sr.context(cfg, nr.Writer(conn, "strand_reading.context", "Claude"), {"Strand": s["code"]})
            (folder / f"{s['code']}-context.md").write_text("\n".join(lines), encoding="utf-8")
            report += [f"Context: {console}", ""]
            data = build(cfg, s, report)
            total += record_clean(cfg, s, data, folder, report)
        conn.execute("RELEASE catchup")
        conn.commit()
    except BaseException:
        conn.execute("ROLLBACK TO catchup")
        conn.execute("RELEASE catchup")
        raise
    report.insert(4, f"**{total} observations recorded.**\n")
    pathlib.Path(a.report).write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"{total} observation(s) recorded -> {a.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
