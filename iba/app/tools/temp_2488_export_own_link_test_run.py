"""temp_2488_export_own_link_test_run.py -- escalation #2488 test: the `surfaces` export reads a link on a derived surface's own row, as `members-verses`,
engagement and the evidence report do. Read-only on a COPY of iba.db (lib/dbsnapshot.copy_db), never the live one.
Usage: python iba/app/tools/temp_2488_export_own_link_test_run.py <scratch dir>"""
import collections
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionexport as ce  # noqa: E402
from iba.app.lib import dbsnapshot  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
scratch.mkdir(parents=True, exist_ok=True)
copy = scratch / "iba-copy-2488.db"
copy.exists() or dbsnapshot.copy_db(copy)
conn = sqlite3.connect(copy)
TIERS = [r[0] for r in conn.execute("SELECT 1 WHERE 0")] or ["core", "synonym", "opposite", "gathered", "phrase"]
GROUPS = ["behaviour", "inner_being_state"]
results = []
def case(name, ok, note=""):
    results.append(ok); print(("PASS " if ok else "FAIL ") + name, note)

terms = {r[0]: r for r in conn.execute("SELECT id, surface, origin, surface_group, group_state, base_id FROM surface_term WHERE deleted=0")}
old = ce._memberships(conn, terms, TIERS, own_link=False)
new = ce._memberships(conn, terms, TIERS, own_link=True)
missed = sorted(set(new) - set(old))
case("T1 the base-only rule misses terms that own-row links reach", len(missed) > 0, "%d terms" % len(missed))
case("T2 own-row links only add, never remove a membership", all(old[s] <= new[s] for s in old))

head, rows = ce.build(conn, "surfaces", TIERS, GROUPS)
head2, rows2 = ce.build(conn, "surfaces", TIERS, GROUPS)
case("T3 the surfaces view is the same on a second run", rows == rows2, "%d rows" % len(rows))
si, ci, ti = head.index("surface"), head.index("collection"), head.index("tier")
by_surface = collections.defaultdict(set)
for r in rows:
    if r[ci]:
        by_surface[r[si]].add((r[ci], r[ti]))
tr = [r for r in rows if r[si] == "troubled" and r[ci]]
case("T4 'troubled' shows its collections in the surfaces view, fear among them", any(r[ci] == "fear" for r in tr), str(sorted({(r[ci], r[ti]) for r in tr})))
# every in-scope term the old rule missed now has its collections in the view
scope_missed = [s for s in missed if terms[s][3] in GROUPS or terms[s][3] is None]
bad = [terms[s][1] for s in scope_missed if not by_surface.get(terms[s][1])]
case("T5 every in-scope surface the old rule missed has a collection row now", not bad, "%d surfaces, %d without" % (len(scope_missed), len(bad)))
# the two views agree on the collections of every in-scope surface
mhead, mrows = ce.build(conn, "members-verses", TIERS, GROUPS)
msi, mci = mhead.index("surface"), mhead.index("collection")
mv = collections.defaultdict(set)
for r in mrows:
    mv[r[msi]].add(r[mci])
diff = [s for s, cs in by_surface.items() if s in mv and {c for c, _ in cs} != mv[s]]
case("T6 surfaces view and members-verses give a surface the same collections", not diff, "%d differ" % len(diff))
# engagement's member set equals the export's membership for one collection
from iba.app.lib import engagement as eng  # noqa: E402
cid = {r[1]: r[0] for r in conn.execute("SELECT id, name FROM collection WHERE deleted=0")}
m = eng.member_terms(conn, cid["fear"], TIERS)
exp = {s for s, mems in new.items() if any(x[0] == cid["fear"] for x in mems)}
case("T7 engagement's members of 'fear' equal the export's", set(m) == exp, "%d" % len(m))
case("T8 the live database was not read or written", copy.exists() and "iba-copy" in copy.name)
print("%d of %d cases pass" % (sum(results), len(results)))
sys.exit(0 if all(results) else 1)
