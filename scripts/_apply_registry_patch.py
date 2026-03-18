import json
import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import get_connection

patch_path = r"G:\My Drive\Bible_study_projects\data\imports\WA\Patches\registry_patch_20260317_v2.json"

with open(patch_path, encoding="utf-8") as f:
    patch = json.load(f)

conn = get_connection()
cur = conn.cursor()

# ── Pre-flight ─────────────────────────────────────────────────────────────
print("── Pre-flight ──")
cur.execute("SELECT id, word FROM word_registry ORDER BY id DESC LIMIT 5")
rows = cur.fetchall()
print("Last 5 word_registry entries:")
for r in rows:
    print(f"  id={r[0]:>3}  word={r[1]}")

target_ids = [e["id"] for e in patch["entries"]]
placeholders = ",".join("?" * len(target_ids))
cur.execute(f"SELECT id FROM word_registry WHERE id IN ({placeholders})", target_ids)
already = [r[0] for r in cur.fetchall()]
if already:
    print(f"WARNING: IDs already in DB: {already}")
else:
    print(f"IDs {target_ids} are all absent — safe to insert")

# ── Apply inserts ──────────────────────────────────────────────────────────
print("\n── Inserting entries ──")
inserted = []
skipped = []
for entry in patch["entries"]:
    if entry["id"] in already:
        skipped.append(entry["id"])
        print(f"  SKIP  id={entry['id']}  '{entry['word']}' (already exists)")
        continue
    cur.execute(
        """INSERT INTO word_registry
               (id, no, word, source_list, category_hint,
                phase1_input_file, phase1_status, phase1_output_file,
                phase2_datasets, notes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            entry["id"],
            entry["no"],
            entry["word"],
            entry["source_list"],
            entry["category_hint"],
            entry["phase1_input_file"],
            entry["phase1_status"],
            entry["phase1_output_file"],
            entry["phase2_datasets"],
            entry["notes"],
        ),
    )
    inserted.append(entry["id"])
    print(f"  INSERT id={entry['id']}  '{entry['word']}'  source_list='{entry['source_list']}'")

conn.commit()

# ── Post-flight verification ───────────────────────────────────────────────
print("\n── Post-flight verification ──")
cur.execute(f"SELECT id, word, source_list, phase1_status FROM word_registry WHERE id IN ({placeholders})", target_ids)
rows = cur.fetchall()
for r in rows:
    print(f"  id={r[0]:>3}  word={r[1]:<20}  source_list={r[2]:<18}  status={r[3]}")

cur.execute("SELECT COUNT(*) FROM word_registry")
total = cur.fetchone()[0]
print(f"\nTotal word_registry rows now: {total}")
print(f"Inserted: {len(inserted)}  Skipped: {len(skipped)}")

conn.close()
