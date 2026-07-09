"""Apply the T7.1.8 catalogue rewording (v2.1, 2026-05-13).

Source: Workflow/Catalogue/wa-obs-catalogue-tiered-v2_1-20260513.md (change note §)

Backup → update → verify → report. Run with --live to commit; default is dry-run.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
QUESTION_CODE = "T7.1.8"
NEW_TEXT = (
    "What does the relationship between the OT Hebrew vocabulary and the NT Greek vocabulary "
    "reveal about continuity or development of this characteristic across the Testaments?"
)

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true", help="Commit changes (default: dry-run)")
args = ap.parse_args()

backup_dir = "backups/row_backups"
os.makedirs(backup_dir, exist_ok=True)
backup_path = os.path.join(
    backup_dir,
    f"wa_obs_question_catalogue_{QUESTION_CODE.replace('.','_')}_pre-rewording_"
    f"{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

rows = list(conn.execute(
    "SELECT * FROM wa_obs_question_catalogue WHERE question_code = ?",
    (QUESTION_CODE,)
))
if not rows:
    raise SystemExit(f"No row found for {QUESTION_CODE}")
if len(rows) > 1:
    raise SystemExit(f"Multiple rows found for {QUESTION_CODE} ({len(rows)}); aborting")

before = dict(rows[0])
print("BEFORE:")
for k in ("obs_id", "question_code", "question_text", "tier", "component_code",
          "component_title", "status", "deleted", "catalogue_version", "date_added"):
    v = before.get(k)
    show = (v[:100] + "…") if isinstance(v, str) and len(v) > 100 else v
    print(f"  {k:25s} = {show!r}")

with open(backup_path, "w", encoding="utf-8") as f:
    json.dump(before, f, indent=2, ensure_ascii=False)
print(f"\nBackup → {backup_path}")

print(f"\nProposed update on wa_obs_question_catalogue obs_id={before['obs_id']}:")
print(f"  question_text:")
print(f"    OLD: {before['question_text']!r}")
print(f"    NEW: {NEW_TEXT!r}")

if not args.live:
    print("\n[DRY-RUN] no changes committed. Re-run with --live to apply.")
    conn.close()
    sys.exit(0)

conn.execute(
    "UPDATE wa_obs_question_catalogue SET question_text = ?, catalogue_version = ? "
    "WHERE question_code = ?",
    (NEW_TEXT, "v2.1-2026-05-13", QUESTION_CODE)
)
conn.commit()

after = dict(conn.execute(
    "SELECT * FROM wa_obs_question_catalogue WHERE question_code = ?",
    (QUESTION_CODE,)
).fetchone())
print("\nAFTER:")
for k in ("obs_id", "question_code", "question_text", "catalogue_version"):
    print(f"  {k:25s} = {after[k]!r}")
print("\n[LIVE] update committed.")
conn.close()
