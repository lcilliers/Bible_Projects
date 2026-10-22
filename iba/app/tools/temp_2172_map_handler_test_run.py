"""TEMPORARY (#2172 test plan, iba/docs/2172-strand-reading-test-plan-v1-20261022.md). Run:
    python iba/app/tools/temp_2172_map_handler_test_run.py <scratch folder>
against a dbsnapshot copy of iba.db in the scratch folder; live iba.db and live files are never written.
Map through its handler on the t4 copy (after test_strand.py): held statements land on the strand's escalation."""
import json
import pathlib
import sys

ROOT = pathlib.Path(r"C:\Bible_study_projects")
sys.path.insert(0, str(ROOT))
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.db import Db  # noqa: E402
from iba.app.handlers import strandreading as hs  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402

S = pathlib.Path(sys.argv[1]) / "t4"
cfg = Cfg(S / "iba.db")
db = Db(cfg)
m = json.loads((S / "m3.json").read_text(encoding="utf-8"))
for b in m["blocks"]:
    b["statements"] = [st for st in b["statements"] if "new_claim" not in st]
    for st in b["statements"]:
        if "claims" in st:
            st["claims"] = [c for c in st["claims"] if c["claim"] not in ("C-331",)]
    b["statements"] = [st for st in b["statements"] if st.get("claims") or st.get("item")]
(S / "m4.json").write_text(json.dumps(m), encoding="utf-8")
v0 = cfg.conn.execute("SELECT MAX(version) FROM escalation WHERE id=2172").fetchone()[0]
out = hs.map_blocks(Ctx(db=db, cfg=cfg, step=None, run_id="RUN-TEST-MAPH", word="", word_id=None,
                        params={"Strand": "test-strand", "By": "Claude", "File": str(S / "m4.json")},
                        step_id="strand_reading.map"))
row = cfg.conn.execute("SELECT version, comment FROM escalation WHERE id=2172 ORDER BY version DESC LIMIT 1").fetchone()
ok = out.condition == "ok" and row[0] == v0 + 1 and "held, no claim yet" in (row[1] or "")
print("map handler: held statements on #2172 |", "PASS" if ok else "FAIL", "|", out.condition, out.message[:300].replace("\n", " "))
print("comment:", (row[1] or "")[-300:].replace("\n", " "))
