"""temp_2393_export_test_run.py -- escalation #2393 test: the two export views against the recorded files of 2026-11-07 (v3 and v4 of #2379).
Read-only on a COPY of iba.db (lib/dbsnapshot.copy_db), never the live one. Usage: python iba/app/tools/temp_2393_export_test_run.py <scratch dir>."""
import collections
import csv
import pathlib
import sqlite3
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib import collectionexport as ce  # noqa: E402
from iba.app.lib import dbsnapshot  # noqa: E402

scratch = pathlib.Path(sys.argv[1])
scratch.mkdir(parents=True, exist_ok=True)
copy = scratch / "iba-copy.db"
copy.exists() or dbsnapshot.copy_db(copy)
conn = sqlite3.connect(copy)
TIERS, GROUPS = ["core", "synonym", "opposite"], ["behaviour", "inner_being_state"]
E1 = ROOT / "outputs/escalation"
for view, old_name in (("members-verses", "2379-surface-collections-members-verses-v4-20261107.csv"), ("surfaces", "2379-behaviour-and-inner-state-surfaces-v3-20261107.csv")):
    t0 = time.time()
    head, rows = ce.build(conn, view, TIERS, GROUPS)
    head2, rows2 = ce.build(conn, view, TIERS, GROUPS)
    print(view, "rows", len(rows), "secs", round(time.time() - t0, 1), "deterministic", rows == rows2)
    old = list(csv.reader(open(E1 / old_name, encoding="utf-8-sig", newline="")))
    print("  header same:", old[0] == head)
    # the files are of 17:40 UTC on 2026-11-07; later changes to the tables are not a defect of the view: rows of surfaces touched by a surface_event since,
    # of collections whose links changed since, and (members-verses) of collections made since are left out of both sides.
    since = "2026-11-07T17:40:27Z"
    touched = {r[0] for r in conn.execute("SELECT subject_id FROM surface_event WHERE subject_kind='surface_term' AND created_at>=?", (since,))}
    names = {r[0] for r in conn.execute(f"SELECT surface FROM surface_term WHERE id IN ({','.join(map(str, touched or [0]))}) OR base_id IN ({','.join(map(str, touched or [0]))})")}
    changed = {str(r[0]) for r in conn.execute("SELECT collection_id FROM collection_link WHERE created_at>=? OR updated_at>=?", (since, since))}
    old_ids = {r[0] for r in old[1:]} if view == "members-verses" else None
    si, ci = head.index("surface"), head.index("collection_id")
    names |= {str(r[si]) for r in rows if str(r[ci]) in changed}
    def keep(r):
        if r[si] in names or r[ci] in changed:
            return False
        return old_ids is None or r[ci] in old_ids
    a = collections.Counter(tuple(r) for r in old[1:] if keep(r))
    b = collections.Counter(tuple(str(x) for x in r) for r in rows if keep([str(x) for x in r]))
    print("  compared old", sum(a.values()), "new", sum(b.values()), "only old", sum((a - b).values()), "only new", sum((b - a).values()))
    for k in list((a - b))[:3]:
        print("   only old:", k[:10])
    for k in list((b - a))[:3]:
        print("   only new:", k[:10])

# ---- handler cases, on the copy (migration applied to it first, exports_root pointed at the scratch folder) ----
from types import SimpleNamespace  # noqa: E402
from iba.app.handlers import collectionbuild as hb  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

conn.close()
cn = sqlite3.connect(copy)
cn.execute("UPDATE cfg_setting SET value=? WHERE key='surfaces.exports_root'", ('"' + (scratch / "exports").as_posix() + '"',))
cn.commit()
cn.close()
cfg = Cfg(copy)
res = []


def case(name, what, okk, detail=""):
    res.append(bool(okk))
    print(f"{name} {'PASS' if okk else 'FAIL'} {what}" + ("" if okk else f"  -- {detail}"), flush=True)


def call(fn, name):
    return fn(SimpleNamespace(cfg=cfg, params={"Name": name}))


exp = scratch / "exports"
r = call(hb.export_members, "Bad_Name")
case("H1", "a name with an underscore is refused, nothing written", r.condition == "refused" and not exp.exists(), r.message)
r = call(hb.export_members, "")
case("H2", "no -Name is refused", r.condition == "refused", r.message)
r1 = call(hb.export_members, "t-members-v1-20261108")
case("H3", "members-verses is written", r1.condition == "ok" and (exp / "t-members-v1-20261108.csv").exists(), r1.message)
r = call(hb.export_members, "t-members-v1-20261108")
case("H4", "the same name is refused, the file is not overwritten", r.condition == "refused" and "already exists" in r.message, r.message)
r2 = call(hb.export_members, "t-members-v2-20261108")
case("H5", "a second run on the same tables gives the same bytes", (exp / "t-members-v1-20261108.csv").read_bytes() == (exp / "t-members-v2-20261108.csv").read_bytes())
r3 = call(hb.export_surfaces, "t-surfaces-v1-20261108")
case("H6", "surfaces is written", r3.condition == "ok" and (exp / "t-surfaces-v1-20261108.csv").exists(), r3.message)
n4 = sum(1 for _ in open(exp / "t-members-v1-20261108.csv", encoding="utf-8-sig", newline="")) 
case("H7", "the row count in the message is the file's data lines + the header (no embedded newline broke a record)", r1.counts["rows"] > 0 and len(list(csv.reader(open(exp / "t-members-v1-20261108.csv", encoding="utf-8-sig", newline="")))) == r1.counts["rows"] + 1)
cn = sqlite3.connect(copy)
cn.execute("UPDATE cfg_setting SET inactive=1 WHERE key='surfaces.export_groups'")
cn.commit()
cn.close()
r = call(hb.export_surfaces, "t-surfaces-v2-20261108")
case("H8", "a missing setting is refused naming it, nothing written", r.condition == "refused" and "surfaces.export_groups" in r.message and not (exp / "t-surfaces-v2-20261108.csv").exists(), r.message)
print("ALL PASS" if all(res) else "SOME FAILED")
