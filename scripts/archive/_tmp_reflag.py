#!/usr/bin/env python3
"""Re-run flag engine for soul (file_id=36) and verify WR-19."""
import sqlite3, os, sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _ROOT)

from engine.flag_engine import run_flag_engine
from engine.audit import run_audit

DB = os.path.join(_ROOT, "data", "bible_research.db")
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

FILE_ID     = 36
REGISTRY_ID = 182

print("=== Re-running flag engine for soul (file_id=36) ===\n")
result = run_flag_engine(conn, FILE_ID, REGISTRY_ID)
print(f"flags_written : {result['flags_written']}")
print(f"errors        : {result['errors']}")

prose_flags = conn.execute(
    """SELECT COUNT(*) FROM wa_data_quality_flags dqf
       JOIN wa_quality_flag_types qt ON qt.id = dqf.flag_id
       WHERE dqf.file_id=? AND qt.flag_code='PROSE_ONLY_MEANING'""",
    (FILE_ID,)
).fetchone()[0]
print(f"PROSE_ONLY_MEANING flags written: {prose_flags}")

print("\n=== Running WR-19 check ===\n")
audit_result = run_audit(conn, FILE_ID, REGISTRY_ID)
checks = audit_result.get("checks", [])
for c in checks:
    if c.get("check") == "WR-19":
        print(f"WR-19: {c['result']}  {c.get('detail','')}")
        break
print("\nAll REVIEW items:")
for c in checks:
    if c.get("result") == "REVIEW":
        print(f"  {c['check']}: {c.get('detail','')}")

conn.close()
