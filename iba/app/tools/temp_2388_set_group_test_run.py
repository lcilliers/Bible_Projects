"""temp_2388_set_group_test_run.py -- tests for escalation #2388: the Set action of the group step (lib/surfacegroup.py set_plan and write_set,
handlers/surfacegroup.py set_group). Runs on a copy of iba.db; the live database is never written. Synthetic bad inputs and the real 82 surfaces.

Usage: python iba/app/tools/temp_2388_set_group_test_run.py <scratch dir>
"""
import json
import pathlib
import shutil
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import surfacegroup as H  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


S = pathlib.Path(sys.argv[1]) / "t2388"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
cfg = Cfg(DB)
conn = cfg.conn
ctx = lambda **p: types.SimpleNamespace(cfg=cfg, params=p, run_id="TEST-RUN")  # noqa: E731
count = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731
row = lambda s: tuple(conn.execute("SELECT surface_group, group_state, group_judged_by, group_reason FROM surface_term WHERE surface=? AND deleted=0", (s,)).fetchone() or ())  # noqa: E731

P = json.load(open(ROOT / "outputs/escalation/2388-group-corrections-proposed-v1-20261107.json", encoding="utf-8"))
REAL = P["other_examples"] + P["other_nonstate"] + P["likely_other"]
R = "Researcher, verbatim: test (#2388)"

# real run: the 82 -- the copy is put back to the state before the live set (not other, judged; computed bases own and resolved_own; untouched)
for s in REAL:
    conn.execute("UPDATE surface_term SET surface_group='inner_being_state', group_state='judged', group_judged_by=NULL, group_reason=NULL, collection_state='untouched' WHERE surface=? AND deleted=0", (s,))
    conn.execute("UPDATE surface_term SET base_id=id, base_source='own', base_state='resolved_own' WHERE surface=? AND deleted=0 AND origin='computed'", (s,))
conn.commit()

# refusals write nothing
ev0 = count("SELECT COUNT(*) FROM surface_event")
o = H.set_group(ctx(Group="nonsense", Surface="all", Reason=R))
case("S1", "an unknown group is refused", o.condition == "refused", o.message)
o = H.set_group(ctx(Group="other", Surface="all"))
case("S2", "no reason is refused", o.condition == "refused", o.message)
o = H.set_group(ctx(Group="other", Surface="", Reason=R))
case("S3", "no surface is refused", o.condition == "refused", o.message)
o = H.set_group(ctx(Group="other", Surface="all,notaword123", Reason=R))
case("S4", "a surface that is not a live term refuses the whole call, nothing written", o.condition == "refused" and row("all")[1] != "confirmed", o.message)
case("S5", "refusals wrote no event", count("SELECT COUNT(*) FROM surface_event") == ev0, ev0)

# preview writes nothing
o = H.set_group(ctx(Group="other", Surface="all,brother", Reason=R, Check="true"))
case("S6", "-Check previews two changes and writes nothing", o.condition == "ok" and o.counts["to_set"] == 2 and row("all")[0] == "inner_being_state" and count("SELECT COUNT(*) FROM surface_event") == ev0, o.message)

# real run: the 82
before = {s: row(s) for s in REAL}
case("S7", "all 82 real surfaces are live rows", all(v for v in before.values()) and len(REAL) == 82, len(REAL))
o = H.set_group(ctx(Group="other", Surface=",".join(REAL), Reason=R))
n_changed = sum(1 for s in REAL if before[s][0] != "other" or before[s][1] != "confirmed")
case("S8", "the real set writes one change per surface not already other and confirmed", o.condition == "ok" and o.counts["set"] == n_changed, (o.counts, n_changed))
after = {s: row(s) for s in REAL}
case("S9", "every one is other, confirmed, judged by researcher, with the reason", all(v == ("other", "confirmed", "researcher", R) for v in after.values()), [s for s, v in after.items() if v[0] != "other"][:5])
ev = [tuple(e) for e in conn.execute("SELECT field, value_after, by FROM surface_event WHERE run_id='TEST-RUN' AND action='set_group'").fetchall()]
case("S10", "one set_group event per change, value_after other, by researcher", len(ev) == n_changed and all(e == ("surface_group", "other", "researcher") for e in ev), len(ev))
nonex = conn.execute("SELECT COUNT(*) FROM surface_term WHERE run_id='TEST-RUN'").fetchone()[0]
case("S11", "no other surface_term row was changed", nonex == n_changed, nonex)

# idempotence
ev1 = count("SELECT COUNT(*) FROM surface_event")
o = H.set_group(ctx(Group="other", Surface=",".join(REAL), Reason=R))
case("S12", "a second run changes nothing", o.condition == "ok" and o.counts["set"] == 0 and count("SELECT COUNT(*) FROM surface_event") == ev1, o.counts)

# the group of a surface is changed back with another group by the same step
o = H.set_group(ctx(Group="behaviour", Surface="brother", Reason=R))
case("S13", "another group can be set and is stored", o.condition == "ok" and row("brother")[0] == "behaviour", row("brother"))
H.set_group(ctx(Group="other", Surface="brother", Reason=R))


# ---- Resolve: a computed base outside collection a is out of scope, with no collection_state (decision 2 option B, #2388) ----
from iba.app.lib import surfaceresolve as sr  # noqa: E402
conn.commit()
snap = {r[0]: tuple(r[1:]) for r in conn.execute("SELECT id, base_id, base_source, base_state, collection_state FROM surface_term WHERE deleted=0 AND surface_group IN ('behaviour','inner_being_state')")}
pl = sr.plan(conn, cfg)
chg = {t["surface"] for t, d in pl["changes"]}
case("R1", "the plan changes the 82 and only terms outside collection a (other or entity)", all(s in chg for s in P["other_examples"] + P["likely_other"]) and all(row(s)[0] in ("other", "entity") for s in chg), len(chg))
done = sr.write(conn, "TEST-RUN-R", pl)
conn.commit()
rows = {s: conn.execute("SELECT base_id, base_source, base_state, collection_state FROM surface_term WHERE surface=? AND deleted=0", (s,)).fetchone() for s in REAL}
case("R2", "every one of the 82 is out_of_scope with no base and no collection_state", all(tuple(v) == (None, None, "out_of_scope", None) for v in rows.values()), [s for s, v in rows.items() if tuple(v) != (None, None, "out_of_scope", None)][:5])
after = {r[0]: tuple(r[1:]) for r in conn.execute("SELECT id, base_id, base_source, base_state, collection_state FROM surface_term WHERE deleted=0 AND surface_group IN ('behaviour','inner_being_state')")}
case("R3", "no in-scope term (behaviour or inner_being_state) was changed by Resolve", {k: v for k, v in after.items() if k in snap and snap[k] != v} == {}, sum(1 for k, v in after.items() if k in snap and snap[k] != v))
pl2 = sr.plan(conn, cfg)
case("R4", "a second plan changes nothing", not pl2["changes"], len(pl2["changes"]))
keep = conn.execute("SELECT COUNT(*) FROM surface_term WHERE deleted=0 AND collection_state IN ('placed','shared') AND surface_group NOT IN ('behaviour','inner_being_state')").fetchone()[0]
case("R5", "a term in a collection keeps its collection_state when out of scope (none lost)", count("SELECT COUNT(*) FROM surface_term WHERE deleted=0 AND collection_state IN ('placed','shared') AND surface_group NOT IN ('behaviour','inner_being_state')") == keep, keep)

# ---- Judge -Surface: refusals before any AI call ----
o = H.judge(ctx(Surface="err,notaword123"))
case("J1", "Judge -Surface naming an unknown term is refused, nothing asked", o.condition == "refused" and "notaword123" in o.message, o.message)

for r in results:
    print("| " + " | ".join(r) + " |")
print("FAILED" if any(r[2] == "FAIL" for r in results) else "ALL PASS", len(results), "cases")
