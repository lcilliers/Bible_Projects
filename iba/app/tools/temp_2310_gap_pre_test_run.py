"""temp_2310_gap_pre_test_run.py -- escalation #2310 test on a COPY of iba.db (never the live DB): the migration
(dry run, apply, second run refused), reading.gap_types after it, and _item_subgroups on real and synthetic items.
Usage: python iba/app/tools/temp_2310_gap_pre_test_run.py <copy-path>"""
import pathlib
import sqlite3
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib import reading as rd  # noqa: E402

DB = pathlib.Path(sys.argv[1])
copy_db(DB)
MIG = str(ROOT / "iba/app/migration/archive/gap_pre_2310_v1_20261026.py")
res = []


def case(name, ok, detail=""):
    res.append(ok)
    print(("PASS " if ok else "FAIL ") + name + (f" -- {detail}" if detail else ""))


def mig(*a):
    return subprocess.run([sys.executable, MIG, "--db", str(DB), *a], capture_output=True, text=True).stdout.strip()


cfg0 = Cfg(DB)
case("before: read_in_files_only is a gap type", "read_in_files_only" in rd.gap_types(cfg0))
out = mig("--dry-run")
case("dry run writes nothing", out.startswith("DRY RUN -- 3 write(s)") and "read_in_files_only" in rd.gap_types(Cfg(DB)), out)
out = mig()
case("apply", "3 write(s) applied" in out, out)
gt = rd.gap_types(Cfg(DB))
case("after: read_in_files_only gone, enum and setting agree", "read_in_files_only" not in gt and "open_item" in gt)
case("pre types unchanged otherwise", [t for t, x in gt.items() if x["phase"] == "pre"] ==
     ["term_cluster", "meaning_missing", "base_missing", "term_reading_missing", "face_not_gathered", "open_item"],
     str([t for t, x in gt.items() if x["phase"] == "pre"]))
case("open_item guide mentions subgroups", "subgroups" in gt["open_item"]["guide"])
case("detector gone", "read_in_files_only" not in rd.PRE and not hasattr(rd, "_pre_read_in_files_only"))
case("second run refused", mig().startswith("already applied"))

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
items = conn.execute("SELECT * FROM escalation_thread_item WHERE status='open' AND target_cluster<>'' ORDER BY id").fetchall()
got = [(i["id"], rd._item_subgroups(conn, i)) for i in items]
with_sg = [g for g in got if g[1]]
case("real: items with a target reach subgroups", len(items) == 204 and len(with_sg) == 202, f"{len(items)} items, {len(with_sg)} reach one")
print("   sample:", with_sg[0], with_sg[-1])
print("   no subgroup:", [g[0] for g in got if not g[1]])
nine = conn.execute("SELECT * FROM escalation_thread_item WHERE id IN (27,420,500,632)").fetchall()
case("synthetic: items with no target terms give []", all(rd._item_subgroups(conn, i) == [] for i in nine))
fake = {"target_cluster": "M39", "target_terms": "H9999X"}
case("synthetic: a strong in no subgroup gives []", rd._item_subgroups(conn, fake) == [])
fake2 = {"target_cluster": "M39", "target_terms": "H2580,H2896A"}
print("   two-term item:", rd._item_subgroups(conn, fake2))
print("ALL PASS" if all(res) else "FAILURES")
