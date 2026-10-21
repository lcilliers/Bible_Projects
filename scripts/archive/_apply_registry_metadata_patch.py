"""
_apply_registry_metadata_patch.py
Apply registry-metadata-patch-20260320-v1.json to bible_research.db.

Sequence (per patch import_order):
  1. DDL  — add 4 new columns to word_registry (skip if already present)
  2. UPDATE — update all 211 rows with source_list, origin, source_category,
               inference_note, anchor_verses; verify word match before each UPDATE
"""

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "bible_research.db"
PATCH_PATH = ROOT / "data" / "imports" / "WA" / "Patches" / "registry-metadata-patch-20260320-v1.json"


def get_existing_columns(conn, table):
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return {row[1] for row in rows}


def apply_ddl(conn, schema_block):
    table = schema_block["target_table"]
    existing = get_existing_columns(conn, table)
    added = []
    skipped = []
    for col in schema_block["columns_to_add"]:
        name = col["name"]
        col_type = col["type"]
        if name in existing:
            skipped.append(name)
        else:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {name} {col_type}")
            added.append(name)
    conn.commit()
    return added, skipped


def apply_updates(conn, update_block):
    table = update_block["target_table"]
    pk = update_block["pk_column"]
    columns = update_block["columns"]
    rows = update_block["rows"]

    updated = 0
    mismatches = []
    skipped = []

    for row in rows:
        row_id = row[pk]
        ref_word = row.get("_ref", {}).get("word")

        # Verify word match
        if ref_word:
            db_row = conn.execute(
                f"SELECT word FROM {table} WHERE {pk} = ?", (row_id,)
            ).fetchone()
            if db_row is None:
                skipped.append({"id": row_id, "reason": "id not found in DB"})
                continue
            if db_row[0].lower() != ref_word.lower():
                mismatches.append({
                    "id": row_id,
                    "db_word": db_row[0],
                    "patch_word": ref_word,
                })
                continue

        # Build SET clause from columns present in patch row (excluding _ref and pk)
        set_parts = []
        values = []
        for col in columns:
            if col in row:
                set_parts.append(f"{col} = ?")
                values.append(row[col])

        if not set_parts:
            skipped.append({"id": row_id, "reason": "no column values in patch row"})
            continue

        values.append(row_id)
        sql = f"UPDATE {table} SET {', '.join(set_parts)} WHERE {pk} = ?"
        conn.execute(sql, values)
        updated += 1

    conn.commit()
    return updated, mismatches, skipped


def main():
    print(f"Patch : {PATCH_PATH.name}")
    print(f"DB    : {DB_PATH}")
    print()

    with open(PATCH_PATH, encoding="utf-8") as f:
        patch = json.load(f)

    meta = patch["_meta"]
    print(f"Patch ID   : {meta['patch_id']}")
    print(f"Description: {meta['description']}")
    print()

    conn = sqlite3.connect(DB_PATH)

    # ── STEP 1: DDL ──────────────────────────────────────────────────────────
    print("=== STEP 1: DDL — adding columns ===")
    added, skipped_ddl = apply_ddl(conn, patch["schema_changes"])
    if added:
        print(f"  Added   : {added}")
    if skipped_ddl:
        print(f"  Skipped (already exist): {skipped_ddl}")
    if not added and not skipped_ddl:
        print("  (nothing to do)")
    print()

    # Verify columns now present
    existing = get_existing_columns(conn, patch["schema_changes"]["target_table"])
    expected_new = [c["name"] for c in patch["schema_changes"]["columns_to_add"]]
    missing = [c for c in expected_new if c not in existing]
    if missing:
        print(f"ERROR: columns still missing after DDL: {missing}")
        conn.close()
        return

    # ── STEP 2: UPDATE ───────────────────────────────────────────────────────
    print("=== STEP 2: UPDATE — populating 211 rows ===")
    updated, mismatches, skipped_upd = apply_updates(conn, patch["word_registry_update"])
    print(f"  Updated  : {updated}")
    print(f"  Skipped  : {len(skipped_upd)}")
    print(f"  Mismatches: {len(mismatches)}")

    if mismatches:
        print("\n  MISMATCH DETAILS:")
        for m in mismatches:
            print(f"    id={m['id']}  db='{m['db_word']}'  patch='{m['patch_word']}'")

    if skipped_upd:
        print("\n  SKIPPED DETAILS:")
        for s in skipped_upd:
            print(f"    id={s['id']}  reason={s['reason']}")

    # ── VERIFICATION ─────────────────────────────────────────────────────────
    print()
    print("=== VERIFICATION ===")
    table = patch["word_registry_update"]["target_table"]
    rc = patch["word_registry_update"]["row_counts"]

    total = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    orig = conn.execute(f"SELECT COUNT(*) FROM {table} WHERE origin = 'original_list'").fetchone()[0]
    prog = conn.execute(f"SELECT COUNT(*) FROM {table} WHERE origin = 'programme_addition'").fetchone()[0]
    high = conn.execute(f"SELECT COUNT(*) FROM {table} WHERE source_list = 'High Confidence'").fetchone()[0]
    low  = conn.execute(f"SELECT COUNT(*) FROM {table} WHERE source_list = 'Low Confidence / Inferred'").fetchone()[0]
    mib  = conn.execute(f"SELECT COUNT(*) FROM {table} WHERE source_list = 'Missing Inner Being Words'").fetchone()[0]
    paddn= conn.execute(f"SELECT COUNT(*) FROM {table} WHERE source_list = 'Programme Addition'").fetchone()[0]
    infer= conn.execute(f"SELECT COUNT(*) FROM {table} WHERE inference_note IS NOT NULL").fetchone()[0]
    anch = conn.execute(f"SELECT COUNT(*) FROM {table} WHERE anchor_verses IS NOT NULL").fetchone()[0]

    def chk(label, actual, expected):
        status = "OK" if actual == expected else f"MISMATCH (expected {expected})"
        print(f"  {label:<35} {actual:>4}  {status}")

    chk("total rows",               total, rc["total_rows"])
    chk("origin=original_list",     orig,  rc["origin_original_list"])
    chk("origin=programme_addition",prog,  rc["origin_programme_addition"])
    chk("source_list=High Confidence", high, rc["source_high_confidence"])
    chk("source_list=Low Confidence/Inferred", low, rc["source_low_confidence"])
    chk("source_list=Missing Inner Being", mib, rc["source_missing_inner_being"])
    chk("source_list=Programme Addition", paddn, rc["source_programme_addition"])
    chk("rows_with_inference_note", infer, rc["rows_with_inference_note"])
    chk("rows_with_anchor_verses",  anch,  rc["rows_with_anchor_verses"])

    conn.close()
    print()
    print("Done.")


if __name__ == "__main__":
    main()
