"""Apply M15-H core_description and notes (researcher-authored 2026-05-12).

Backup → update → verify → report. Run with --live to commit; default is dry-run.
"""
import sqlite3, sys, os, json, argparse
from datetime import datetime, timezone
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB = "database/bible_research.db"
SG_CODE = "M15-H"
NEW_CORE = "the Living Word indwelling the inner being, the embodiment of Christ as the Word of God"
NEW_NOTES = "word, spoken or written, often with a focus on the content of a communication; matter, thing"

ap = argparse.ArgumentParser()
ap.add_argument("--live", action="store_true", help="Commit changes (default: dry-run)")
args = ap.parse_args()

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
backup_dir = "backups/row_backups"
os.makedirs(backup_dir, exist_ok=True)
backup_path = os.path.join(backup_dir, f"cluster_subgroup_M15-H_pre-description-fill_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json")

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

before = conn.execute("SELECT * FROM cluster_subgroup WHERE subgroup_code=?", (SG_CODE,)).fetchone()
if not before:
    raise SystemExit(f"{SG_CODE} not found")
before_d = dict(before)
print("BEFORE:")
for k, v in before_d.items():
    show = (v[:80] + "…") if isinstance(v, str) and len(v) > 80 else v
    print(f"  {k:25s} = {show!r}")

# Write backup (always, even dry-run, so it's available if --live follows)
with open(backup_path, "w", encoding="utf-8") as f:
    json.dump(before_d, f, indent=2, ensure_ascii=False)
print(f"\nBackup → {backup_path}")

print(f"\nProposed update on cluster_subgroup row id={before_d['id']}:")
print(f"  core_description : {before_d['core_description']!r}")
print(f"                  → {NEW_CORE!r}")
print(f"  notes            : {before_d['notes']!r}")
print(f"                  → {NEW_NOTES!r}")
print(f"  last_updated_date: {before_d['last_updated_date']!r}")
print(f"                  → {now_utc!r}")

if not args.live:
    print("\n[DRY-RUN] no changes committed. Re-run with --live to apply.")
    conn.close()
    sys.exit(0)

conn.execute("""
    UPDATE cluster_subgroup
       SET core_description = ?, notes = ?, last_updated_date = ?
     WHERE subgroup_code = ?
""", (NEW_CORE, NEW_NOTES, now_utc, SG_CODE))
conn.commit()

after = dict(conn.execute("SELECT * FROM cluster_subgroup WHERE subgroup_code=?", (SG_CODE,)).fetchone())
print("\nAFTER:")
for k in ("subgroup_code", "core_description", "notes", "last_updated_date"):
    print(f"  {k:25s} = {after[k]!r}")
print("\n[LIVE] update committed.")
conn.close()
