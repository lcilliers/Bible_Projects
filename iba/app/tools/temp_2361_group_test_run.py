"""temp_2361_group_test_run.py -- tests for escalation #2361 stage 2: the group repoint (lib/surfacegroup.py, handlers/surfacegroup.py,
Surface-Group.ps1). The reproduction puts a copy of iba.db back to the state before the recorded repoint of 2026-11-04 (the 56 corrections
reverted from their own events) and checks that the rule finds the same changes and the same held pairs as the recorded workbook; it then
checks the writer, idempotence, the refusals, and that no file is read by the handlers.

Usage: python iba/app/tools/temp_2361_group_test_run.py <scratch dir>
"""
import builtins
import pathlib
import shutil
import subprocess
import sys
import types

import openpyxl

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import surfacegroup as H  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

WF = ROOT / "_analytics" / "surfaces" / "working_files"
results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


wb = openpyxl.load_workbook(WF / "group" / "import" / "surface-repoint-m1-v1-20261104.xlsx", read_only=True)
APP = {r[0]: (r[1], r[2]) for r in list(wb["Applied changes"].iter_rows(values_only=True))[1:] if r[0]}
HELD = {(r[0], r[2]) for r in list(wb["Held for decision"].iter_rows(values_only=True))[1:] if r[0]}
HELD_BASES = {b for b, _ in HELD}

S = pathlib.Path(sys.argv[1]) / "t2361g"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
mig = ROOT / "iba/app/migration/surface_group_2361_v1_20261106.py"
mig = mig if mig.exists() else ROOT / "iba/app/migration/archive" / mig.name
o = [subprocess.run([sys.executable, str(mig), "--db", str(DB), "--no-snapshot"], capture_output=True, text=True).stdout.strip() for _ in range(2)]
case("B0", "migration: applied (or already), then nothing to do", ("applied" in o[0] or "already" in o[0]) and "already" in o[1], o)
cfg = Cfg(DB)
conn = cfg.conn
ctx = lambda **p: types.SimpleNamespace(cfg=cfg, params=p, run_id="TEST-RUN")  # noqa: E731
count = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731
grp = lambda s: conn.execute("SELECT surface_group FROM surface_term WHERE surface=? AND deleted=0", (s,)).fetchone()[0]  # noqa: E731

# ---- the live state: the recorded corrections are in the tables, so the rule proposes nothing to change --------------------------
o = H.status(ctx())
case("B1", "the recorded corrections are in the tables: nothing to correct, nothing proposed", o.condition == "ok" and o.counts["to_correct"] == 0 and o.counts["proposed"] == 0, o.counts)

# ---- put the copy back to the state before the repoint ---------------------------------------------------------------------------
ev = conn.execute("SELECT id, subject_id, value_before FROM surface_event WHERE action='correct' AND field='surface_group' AND by LIKE '%2359 repoint%'").fetchall()
for _id, sid, vb in ev:
    conn.execute("UPDATE surface_term SET surface_group=?, group_state='judged', group_reason=NULL WHERE id=?", (vb, sid))
    conn.execute("DELETE FROM surface_event WHERE id=?", (_id,))
conn.commit()
case("B2", "the copy is put back: the 56 recorded corrections reverted from their events", len(ev) == 56 and all(grp(b) == v[0] for b, v in APP.items()), len(ev))

_real_open = builtins.open


def _no_files(path, *a, **k):
    if any(x in str(path).replace("\\", "/") for x in ("_analytics/", "outputs/")):
        raise AssertionError(f"a file was read: {path}")
    return _real_open(path, *a, **k)


builtins.open = _no_files
try:
    vals, plan, pairs = H._plan(ctx())
    auto = set(plan["apply"])
    rev = set(plan["review"])
    want_other = {b for b, v in APP.items() if v[0] == "other"}
    case("B3", "the bases the rule corrects by itself are exactly the recorded changes of bases judged other (53)",
         auto == want_other and len(auto) == 53, (len(auto), sorted(auto ^ want_other)[:5]))
    case("B4", "the proposed bases (judged being) are exactly the 3 the researcher applied: build, circumcise, redeem",
         rev == {b for b, v in APP.items() if v[0] == "being"} and len(rev) == 3, sorted(rev))
    bad = [b for b in auto | rev if (plan["apply"].get(b) or plan["review"].get(b))[0] != APP[b][1]]
    case("B5", "each new group equals the recorded group_after", not bad, bad[:5])
    found = {(b, p[0]) for b, ps in pairs.items() for p in ps}
    case("B6", "all 52 recorded held pairs are found by the rule, and none is new (each is named by a held_pair flag already)",
         HELD <= found and not plan["held"], (len(HELD), len(HELD & found), len(plan["held"]), len(plan["skipped"])))
    o = H.repoint(ctx(Check="true"))
    case("B7", "Repoint -Check previews and writes nothing", o.condition == "ok" and "PREVIEW" in o.message and grp("abandon") == "other"
         and count("SELECT count(*) FROM surface_event WHERE action='correct' AND by='surface-group'") == 0, o.counts)
    o = H.repoint(ctx())
    case("B8", "Repoint corrects the 53 by rule and flags the 3 proposed ones", o.condition == "ok" and o.counts["corrected"] == 53 and o.counts["flagged"] == 3, o.counts)
    case("B9", "the corrections: group, state corrected, one event each naming the derived words",
         grp("abandon") == "inner_being_state" and count("SELECT count(*) FROM surface_event WHERE action='correct' AND by='surface-group' AND reason LIKE '%because of:%'") == 53
         and count("SELECT count(*) FROM surface_term WHERE group_state='corrected' AND run_id='TEST-RUN'") == 53, grp("abandon"))
    o = H.repoint(ctx())
    case("B10", "a second Repoint changes nothing (the 3 proposals are flagged, left to the reading)", o.counts["corrected"] == 0 and o.counts["flagged"] == 0, o.counts)
    o = H.repoint(ctx(Base="nosuchword"))
    case("B11", "-Base naming a base the rule does not propose is refused", o.condition == "refused", o.message[:80])
    conn.execute("DELETE FROM surface_flag WHERE kind='held_pair' AND load_ref IS NULL AND created_by='surface-group'")
    conn.commit()
    o = H.repoint(ctx(Base="build,circumcise,redeem"))
    case("B12", "-Base names the 3 proposed bases: they are corrected to the recorded group_after",
         o.condition == "ok" and o.counts["corrected"] == 3 and all(grp(b) == APP[b][1] for b in APP), o.message[:200])
    case("B13", "all 56 recorded changes are reproduced", all(grp(b) == v[1] for b, v in APP.items()), len(APP))
    conn.execute("DELETE FROM cfg_setting WHERE key='group.repoint_apply_kinds'")
    conn.commit()
    before = count("SELECT count(*) FROM surface_event")
    o1, o2 = H.status(ctx()), H.repoint(ctx())
    case("B14", "a missing setting is refused by Status and Repoint and writes nothing", o1.condition == "refused" and o2.condition == "refused"
         and count("SELECT count(*) FROM surface_event") == before, o2.message[:80])
finally:
    builtins.open = _real_open
case("B15", "no file under _analytics or outputs was read by any handler call above", True, "open() was patched to raise, and none did")

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res_, evd in results:
    print(f"{cid:<{width}}  {res_}  {desc}  [{evd}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
