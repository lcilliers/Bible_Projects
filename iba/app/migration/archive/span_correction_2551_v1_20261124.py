"""span_correction_2551_v1_20261124.py -- escalation #2551 (the correction table for stored span errors; design adopted 2026-11-24).

Creates the table span_correction (one row per corrected field of one span code), its unique index on the live rows, and the cfg_utility rows of spancorrection and this migration.
The table holds no row yet: the corrections themselves are added through configmaint.apply_logged from #2541 (items 2.1, 2.2, 2.4), each with its reason and escalation.
Idempotent. A named rollback snapshot is taken before a live apply.

Usage:
    python iba/app/migration/span_correction_2551_v1_20261124.py [--db PATH] [--dry-run] [--no-snapshot]
"""
import argparse
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers.configmaint import apply_logged  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DEFAULT_DB = ROOT / "iba" / "app" / "db" / "iba.db"
RUN_ID = "DEVMODE-SPAN-CORRECTION-2551-20261124"
DDL = [
    """CREATE TABLE IF NOT EXISTS "span_correction" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "span_id" INTEGER NOT NULL,
  "code_ordinal" INTEGER NOT NULL,
  "field" TEXT NOT NULL,
  "stored_value" TEXT,
  "corrected_value" TEXT,
  "reason" TEXT NOT NULL CHECK (length(reason) >= 20),
  "escalation_id" INTEGER NOT NULL,
  "applied_at" TEXT,
  "applied_count" INTEGER NOT NULL DEFAULT 0,
  "deleted" INTEGER NOT NULL DEFAULT 0,
  "created_at" TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now')),
  "run_id" TEXT,
  FOREIGN KEY ("span_id") REFERENCES "span"("id")
)""",
    'CREATE UNIQUE INDEX IF NOT EXISTS "uq_span_correction_live" ON "span_correction" ("span_id","code_ordinal","field") WHERE deleted=0',
]
UTILITIES = [("iba.app.lib.spancorrection", "iba/app/lib/spancorrection.py", "the corrections of stored span errors, applied by lexical.write_readings_for_span (#2551)"),
             ("iba.app.migration.span_correction_2551_v1_20261124", "iba/app/migration/span_correction_2551_v1_20261124.py", "creates span_correction (#2551)")]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DEFAULT_DB))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-snapshot", action="store_true")
    a = ap.parse_args()
    conn = Cfg(pathlib.Path(a.db)).conn
    have = conn.execute("SELECT 1 FROM sqlite_master WHERE name='span_correction'").fetchone() is not None
    ops = [("cfg_utility", "insert", {}, {"module": m, "file_path": f, "purpose": pu, "inactive": 0, "config_exempt": 1, "config_exempt_reason": "a table definition and its reader; no setting",
                                          "crash_escalation_reviewed": 0, "crash_escalation_note": None})
           for m, f, pu in UTILITIES if not conn.execute("SELECT 1 FROM cfg_utility WHERE module=?", (m,)).fetchone()]
    print(f"span_correction exists: {have}; cfg writes: {len(ops)}; dry run: {a.dry_run}")
    if a.dry_run or (have and not ops):
        return 0
    if not a.no_snapshot:
        from iba.app.lib import dbsnapshot
        print(f"named rollback snapshot: {dbsnapshot.snapshot('pre-span-correction-2551-apply', named=True)}")
    for s in DDL:
        conn.execute(s)
    for t_, op, where, set_ in ops:
        apply_logged(conn, RUN_ID, t_, op, where, set_)
    conn.commit()
    print(f"applied (run {RUN_ID})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
