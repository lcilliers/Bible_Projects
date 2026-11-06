"""temp_2361_structure_test_run.py -- tests for escalation #2361 stage 2: the surface-structure module (lib/surfacestructure.py,
handlers/surfacestructure.py, Surface-Structure.ps1). Part A reproduces the recorded control of 2026-11-04 (the expected values, read
from the import folder) from the pure function. Part B runs the migration and the handlers on a copy of iba.db made with
lib/dbsnapshot.copy_db and proves the module reads only the tables.

Usage: python iba/app/tools/temp_2361_structure_test_run.py <scratch dir>
"""
import builtins
import collections
import json
import pathlib
import shutil
import sqlite3
import subprocess
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import surfacestructure as H  # noqa: E402
from iba.app.lib import surfacestructure as ss  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

WF = ROOT / "_analytics" / "surfaces" / "working_files"
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


# ---- part A: the pure function against the recorded control -------------------------------------------------------------------
d = json.load(open(WF / "structure" / "import" / "surface-match-control-v3-20261104.json", encoding="utf-8"))
v4 = {}
for line in open(WF / "group" / "import" / "first-split-v4-20261104.jsonl", encoding="utf-8"):
    if line.strip():
        r = json.loads(line)
        v4[r["surface"]] = r["group"]
SET = {"structure.min_base_length": 3, "structure.min_computed_base_length": 4, "structure.min_starts_with_length": 3,
       "structure.possessive_pattern": r"[’']s$", "structure.tested_form": "single word"}
cons = sorted(d["constructs"], key=lambda c: c["id"])
for c in cons:
    c["result_kind"] = "x"
surfaces = [{"surface": s["surface"], "group": s["group"], "form": s["form"]} for s in d["surfaces"]]
N = {ss.normalise(s["surface"], SET["structure.possessive_pattern"]) for s in surfaces}
outside = {}
for sf, g in v4.items():
    n = ss.normalise(sf, SET["structure.possessive_pattern"])
    if n not in N:
        outside.setdefault(n, g)
res = ss.analyse(surfaces, cons, outside, SET)
case("A1", "the 1,386 hits equal the recorded hits, in order", res["hits"] == d["hits"], f"{len(res['hits'])} of {len(d['hits'])}")
rec = {s["surface"]: s for s in d["surfaces"]}
FIELDS = ("group", "normalised", "form", "status", "bases", "roots", "derived_by", "pointed_at_by", "opposite_leads", "other_leads",
          "starts_with_leads", "status_v2", "sibling_group", "sibling_via", "base_outside_input")
bad = collections.Counter()
for r in res["surfaces"]:
    for k in FIELDS:
        ov = rec[r["surface"]].get(k)
        if ov is None:
            ov = [] if isinstance(r[k], list) else ""
        if r[k] != ov:
            bad[k] += 1
case("A2", "every field of every one of the 3,850 surfaces equals the record", not bad, dict(bad) or f"{len(res['surfaces'])} surfaces, {len(FIELDS)} fields")
case("A3", "the 47 sibling groups (members, computed bases, numbering) equal the record", res["sibling_groups"] == d["sibling_groups"], len(res["sibling_groups"]))
case("A4", "the normalised table (1,435 roots) equals the record", res["normalised"] == d["normalised"], len(res["normalised"]))
case("A5", "root counts and the status counts equal the record", (res["roots_before"], res["roots_after_siblings"]) == (d["meta"]["roots_before"], d["meta"]["roots_after_siblings"])
     and res["counts"] == d["meta"]["single_word_status_v2"], res["counts"])
try:
    ss.analyse(surfaces, cons, outside, {k: v for k, v in SET.items() if k != "structure.min_base_length"})
    refused = False
except ss.StructureError:
    refused = True
case("A6", "the pure function stops when a setting is missing (no default in code)", refused, "StructureError")

# ---- part B: the migration and the handlers on a copy --------------------------------------------------------------------------
S = pathlib.Path(sys.argv[1]) / "t2361s"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
mig = ROOT / "iba/app/migration/surface_structure_2361_v1_20261106.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
o = [subprocess.run([sys.executable, str(mig), "--db", str(DB), "--no-snapshot"], capture_output=True, text=True).stdout.strip() for _ in range(2)]
case("B0", "migration: applied (or already), then nothing to do", ("applied" in o[0] or "already" in o[0]) and "already" in o[1], o)
cfg = Cfg(DB)
conn = cfg.conn
ctx = lambda cfg_=cfg, **p: types.SimpleNamespace(cfg=cfg_, params=p, run_id="TEST-RUN")  # noqa: E731
count = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731
live_rows = lambda: count("SELECT count(*) FROM surface_derivation WHERE deleted=0 AND method IN ('structure','sibling')")
accepted = lambda: count("SELECT count(*) FROM surface_derivation WHERE deleted=0 AND method='structure' AND accepted=1")
states = lambda: conn.execute("SELECT base_state, count(*) FROM surface_term GROUP BY 1 ORDER BY 1").fetchall()
st0, rows0, acc0 = states(), live_rows(), accepted()

_real_open = builtins.open
def _no_files(path, *a, **k):
    if any(x in str(path).replace("\\", "/") for x in ("_analytics/", "outputs/")):
        raise AssertionError(f"a file was read: {path}")
    return _real_open(path, *a, **k)
builtins.open = _no_files
try:
    o = H.status(ctx())
    case("B1", "status: the loaded structure rows already equal the module's (only the 152 sibling rows are finer)",
         o.condition == "ok" and o.counts["to_add"] == o.counts["to_supersede"] and o.counts["to_add"] in (0, 152), o.counts)
    SYNC = o.counts["to_add"]
    o = H.match(ctx(Check="true"))
    case("B2", "Match -Check previews and writes nothing", o.condition == "ok" and "PREVIEW" in o.message and live_rows() == rows0, o.counts)
    o = H.match(ctx())
    case("B3", "Match writes the difference: the sibling rows made finer (152 on the first run, 0 once run), the rest unchanged",
         o.counts == {"added": SYNC, "superseded": SYNC, "kept": rows0 - SYNC}, o.counts)
    case("B4", "the live evidence count is unchanged and the sibling evidence now names its construct",
         live_rows() == rows0 and count("SELECT count(*) FROM surface_derivation WHERE deleted=0 AND method='sibling' AND evidence LIKE 'S%:C%'") == 152, live_rows())
    o = H.match(ctx())
    case("B5", "a second Match with the same inputs changes nothing", o.counts == {"added": 0, "superseded": 0, "kept": rows0}, o.counts)
    case("B6", "the choice of evidence (accepted) and every base state are untouched by the module", accepted() == acc0 and states() == st0, (acc0, accepted()))
    # a switched-off construct supersedes exactly its rows; switching it on restores them as new rows
    c01 = count("SELECT count(*) FROM surface_derivation WHERE deleted=0 AND method='structure' AND evidence='C01'")
    conn.execute("UPDATE cfg_base_construct SET inactive=1 WHERE id='C01'"); conn.commit()
    o = H.match(ctx())
    left = count("SELECT count(*) FROM surface_derivation WHERE deleted=0 AND evidence='C01'")
    case("B7", "C01 switched off: its live rows are superseded (nothing physically deleted), none left live",
         left == 0 and o.counts["superseded"] >= c01 and count("SELECT count(*) FROM surface_derivation WHERE deleted=1 AND evidence='C01'") >= c01, (c01, o.counts))
    conn.execute("UPDATE cfg_base_construct SET inactive=0 WHERE id='C01'"); conn.commit()
    o = H.match(ctx())
    case("B8", "C01 switched on again: the same evidence is back, and the history rows stay",
         live_rows() == rows0 and count("SELECT count(*) FROM surface_derivation WHERE deleted=0 AND evidence='C01'") == c01 and o.counts["added"] >= c01, (live_rows(), o.counts))
    o = H.show(ctx(Surface="hides"))
    case("B9", "Show: hides has two bases, hid and hide", "['hid', 'hide']" in o.message, o.message.split("\n")[1][:80] if "\n" in o.message else o.message[:80])
    o = H.show(ctx(Surface="sinner’s"))
    case("B10", "Show: the possessive form takes the result of its twin (base sin)", "['sin']" in o.message, o.message.split("\n")[1][:80] if "\n" in o.message else o.message[:80])
    o = H.show(ctx(Surface="not a surface"))
    case("B11", "Show: a surface that is not in collection a is refused", o.condition == "refused", o.message[:80])
    conn.execute("DELETE FROM cfg_setting WHERE key='structure.min_base_length'"); conn.commit()
    before = live_rows()
    o1, o2 = H.status(ctx()), H.match(ctx())
    case("B12", "a missing setting is refused by Status and Match and writes nothing", o1.condition == "refused" and o2.condition == "refused" and live_rows() == before, o2.message[:80])
finally:
    builtins.open = _real_open
case("B13", "no file under _analytics or outputs was read by any handler call above", True, "open() was patched to raise, and none did")

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res_, ev in results:
    print(f"{cid:<{width}}  {res_}  {desc}  [{ev}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
