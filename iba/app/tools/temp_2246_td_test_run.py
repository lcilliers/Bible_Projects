"""temp_2246_td_test_run.py -- tests for escalation #2246 option A: thread audit T-d flags an open
cluster:/strong: item only when it was opened before its strand was worked
(outputs/escalation/2246-thread-audit-td-review-v1-20261023.md). Run on a copy of iba.db made with
lib/dbsnapshot.copy_db; the live database is not written.

Usage: python iba/app/tools/temp_2246_td_test_run.py <scratch dir>
"""
import pathlib
import shutil
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.lib import threadaudit  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t2246"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
FIVE = {"OT-108.3", "OT-108.4", "OT-108.5", "OT-108.6", "OT-108.8"}
results = []


def td() -> dict[str, str]:
    cfg = Cfg(DB)
    F = threadaudit.audit(cfg, Db(cfg, DB))
    return {f["ref"]: f["reason"] for f in F if f["check"] == "T-d"}


def case(name, got, want):
    results.append((name, got == want, got, want))


# 1 real data: the five catch-up items, opened 2026-10-22 after their strands, are no finding
got = td()
case("1 real: the five OT-108 items are not T-d", sorted(FIVE & set(got)), [])

c = sqlite3.connect(DB)
tid = c.execute("SELECT id FROM escalation WHERE alias='OT-108'").fetchone()[0]
m18_strong = c.execute("SELECT strong FROM cluster_strong WHERE cluster_code='M18' AND deleted=0 "
                       "ORDER BY strong LIMIT 1").fetchone()[0]
# 2 synthetic: OT-108.4 (M72, #1998 completed 2026-10-12) opened before the strand was worked
c.execute("UPDATE escalation_thread_item SET opened_at='2026-10-01T00:00:00Z' "
          "WHERE escalation_id=? AND item_no=4", (tid,))
# 3, 4 synthetic strong items on M18 (#1993 completed 2026-10-14): one before, one after
# 5 synthetic cluster item on M09 (#2148 completed 2026-10-15) opened the day before
for no, kind, val, at in ((901, "strong", m18_strong, "2026-10-01T00:00:00Z"),
                          (902, "strong", m18_strong, "2026-10-20T00:00:00Z"),
                          (903, "cluster", "M09", "2026-10-14T00:00:00Z")):
    c.execute("INSERT INTO escalation_thread_item (escalation_id, item_no, kind, value, status, "
              "note, opened_at, opened_by) VALUES (?,?,?,?, 'open', 'test #2246', ?, 'Claude')",
              (tid, no, kind, val, at))
c.commit()
c.close()
got = td()
case("2 synthetic: cluster item opened before the strand is T-d", "OT-108.4" in got, True)
case("3 synthetic: strong item opened before the strand is T-d", "OT-108.901" in got, True)
case("4 synthetic: strong item opened after the strand is not T-d", "OT-108.902" in got, False)
case("5 synthetic: cluster item opened a day before the strand is T-d", "OT-108.903" in got, True)
case("6 the other four real items stay clear", sorted((FIVE - {"OT-108.4"}) & set(got)), [])

L = ["# #2246 T-d date rule -- test results", "",
     f"Run on a copy of iba.db ({DB}); strong used for cases 3 and 4: {m18_strong}.", "",
     "| case | result | got | expected |", "|---|---|---|---|"]
L += [f"| {n} | {'pass' if ok else 'FAIL'} | {g} | {w} |" for n, ok, g, w in results]
L += ["", f"{sum(ok for _, ok, _, _ in results)}/{len(results)} pass"]
print("\n".join(L))
