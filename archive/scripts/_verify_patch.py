import json, sys, collections

path = r"G:\My Drive\Bible_study_projects\data\imports\WA\Patches\WA-phase2-flags-patch-v2-2026-03-16.json"

# ── 1. Parse JSON ──────────────────────────────────────────────────────────
with open(path, encoding="utf-8") as f:
    data = json.load(f)
print("✓ JSON is valid and parses successfully")

# ── 2. Top-level sections ──────────────────────────────────────────────────
sections = list(data.keys())
print(f"\nTop-level keys: {sections}")

# ── 3. phase2_flag_types_insert ────────────────────────────────────────────
ft = data["phase2_flag_types_insert"]
print(f"\n── phase2_flag_types_insert ──")
print(f"  target_table   : {ft['target_table']}")
print(f"  operation      : {ft['operation']}")
print(f"  conflict_action: {ft['conflict_action']}")
print(f"  columns        : {ft['columns']}")
ft_rows = ft["rows"]
print(f"  row count      : {len(ft_rows)}")

ft_ids = []
ft_codes = []
for i, row in enumerate(ft_rows):
    for col in ft["columns"]:
        if col not in row:
            print(f"  ✗ Row {i}: missing column '{col}'")
    ft_ids.append(row["id"])
    ft_codes.append(row["flag_code"])

dup_ids = [k for k, v in collections.Counter(ft_ids).items() if v > 1]
dup_codes = [k for k, v in collections.Counter(ft_codes).items() if v > 1]
print(f"  id range       : {min(ft_ids)} – {max(ft_ids)}")
print(f"  duplicate ids  : {dup_ids if dup_ids else 'none'}")
print(f"  duplicate codes: {dup_codes if dup_codes else 'none'}")
for row in ft_rows:
    print(f"    id={row['id']:>3}  {row['flag_code']}")

# ── 4. wa_term_phase2_flags_insert ─────────────────────────────────────────
wf = data["wa_term_phase2_flags_insert"]
print(f"\n── wa_term_phase2_flags_insert ──")
print(f"  target_table   : {wf['target_table']}")
print(f"  operation      : {wf['operation']}")
print(f"  conflict_action: {wf['conflict_action']}")
print(f"  columns        : {wf['columns']}")
wf_rows = wf["rows"]
declared_counts = wf.get("row_counts", {})
print(f"  declared total : {declared_counts.get('total_rows')}")
print(f"  actual row count: {len(wf_rows)}")

flag_dist = collections.Counter(r["flag_id"] for r in wf_rows)
print(f"  rows by flag_id: {dict(sorted(flag_dist.items()))}")
print(f"  declared flag_id=1 (god_as_subject gap): {declared_counts.get('god_as_subject_gap_flag_id_1')},  actual: {flag_dist[1]}")
print(f"  declared flag_id=3 (somatic_link gap)  : {declared_counts.get('somatic_link_gap_flag_id_3')},  actual: {flag_dist[3]}")
print(f"  declared flag_id=2 (causative gap)     : {declared_counts.get('causative_gap_flag_id_2')},  actual: {flag_dist[2]}")

missing_cols = []
for i, row in enumerate(wf_rows):
    for col in wf["columns"]:
        if col not in row:
            missing_cols.append(f"row {i}: missing '{col}'")
if missing_cols:
    for m in missing_cols:
        print(f"  ✗ {m}")
else:
    print(f"  ✓ All rows have required columns")

pairs = [(r["term_inv_id"], r["flag_id"]) for r in wf_rows]
dup_pairs = [k for k, v in collections.Counter(pairs).items() if v > 1]
if dup_pairs:
    print(f"  ✗ Duplicate (term_inv_id, flag_id) pairs in patch: {dup_pairs}")
else:
    print(f"  ✓ No duplicate (term_inv_id, flag_id) pairs within patch")

flag_ids_used = set(flag_dist.keys())
print(f"  flag_ids referenced: {sorted(flag_ids_used)}")
term_ids_used = sorted(set(r["term_inv_id"] for r in wf_rows))
print(f"  term_inv_id range  : {min(term_ids_used)} – {max(term_ids_used)}  ({len(term_ids_used)} distinct)")

# ── 5. Cross-check against DB ──────────────────────────────────────────────
import sys
sys.path.insert(0, r"G:\My Drive\Bible_study_projects")
from analytics.db_client import get_connection

print("\n── DB cross-check ──")
conn = get_connection()
cur = conn.cursor()

# 5a. phase2_flag_types: check existing IDs, no collision unless IGNORE is safe
cur.execute("SELECT id, flag_code FROM phase2_flag_types ORDER BY id")
existing_flags = {row[0]: row[1] for row in cur.fetchall()}
print(f"  Existing phase2_flag_types rows: ids {sorted(existing_flags.keys())}")

collisions = []
for row in ft_rows:
    if row["id"] in existing_flags:
        collisions.append(f"id={row['id']} code={row['flag_code']} (existing: {existing_flags[row['id']]})")
if collisions:
    print(f"  ⚠ Already-existing ids (IGNORE will skip): {collisions}")
else:
    print(f"  ✓ All 11 new flag ids (15-25) are absent from DB – clean inserts")

# 5b. wa_term_phase2_flags: check flag_ids 1,2,3 exist
for fid in sorted(flag_ids_used):
    cur.execute("SELECT flag_code FROM phase2_flag_types WHERE id=?", (fid,))
    row = cur.fetchone()
    if row:
        print(f"  ✓ flag_id={fid} ({row[0]}) exists in phase2_flag_types")
    else:
        print(f"  ✗ flag_id={fid} NOT found in phase2_flag_types")

# 5c. Check term_inv_ids exist in wa_term_inventory
placeholders = ",".join("?" * len(term_ids_used))
cur.execute(f"SELECT id FROM wa_term_inventory WHERE id IN ({placeholders})", term_ids_used)
found_inv = {row[0] for row in cur.fetchall()}
missing_inv = sorted(set(term_ids_used) - found_inv)
if missing_inv:
    print(f"  ✗ term_inv_ids NOT in wa_term_inventory: {missing_inv}")
else:
    print(f"  ✓ All {len(term_ids_used)} distinct term_inv_ids exist in wa_term_inventory")

# 5d. Check (term_inv_id, flag_id) pairs already in DB
cur.execute("SELECT term_inv_id, flag_id FROM wa_term_phase2_flags")
existing_pairs = set(cur.fetchall())
already_there = [p for p in pairs if p in existing_pairs]
if already_there:
    print(f"  ⚠ {len(already_there)} pairs already exist in DB (IGNORE will skip them):")
    for p in already_there:
        print(f"      term_inv_id={p[0]}, flag_id={p[1]}")
else:
    print(f"  ✓ None of the 200 (term_inv_id, flag_id) pairs are already in DB – all will insert")

conn.close()
print("\n── Summary ──")
print("  Patch targets 2 tables: phase2_flag_types (INSERT 11 rows, ids 15-25)")
print("                          wa_term_phase2_flags (INSERT 200 rows)")
print("  conflict_action=IGNORE on both: safe to re-run without duplicating data")
