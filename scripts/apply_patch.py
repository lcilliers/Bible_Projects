"""
apply_patch.py  —  Generic patch processor for bible-projects-patch-spec-v1.1 files.

Usage:
    python scripts/apply_patch.py <patch_file.json> [--dry-run]

Supports:
    - INSERT (conflict_action: IGNORE | REPLACE | FAIL)
    - UPDATE (pk_column based WHERE clause)
    - id_baseline verification
    - import_order respected
    - _ref fields stripped automatically
"""

import json
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from analytics.db_client import get_connection


def strip_ref(row, columns):
    """Return only the values for declared columns, ignoring _ref and extras."""
    return [row[col] for col in columns]


def check_baseline(cur, baseline: dict, patch_id: str):
    """Verify id_baseline values against actual DB MAX(id). Warn on mismatch."""
    ok = True
    for table, expected_max in baseline.items():
        cur.execute(f"SELECT COALESCE(MAX(id), 0) FROM {table}")
        actual_max = cur.fetchone()[0]
        if actual_max != expected_max:
            print(f"  ⚠  BASELINE MISMATCH [{patch_id}] {table}: "
                  f"expected MAX(id)={expected_max}, actual MAX(id)={actual_max}")
            ok = False
        else:
            print(f"  ✓  baseline {table}: MAX(id)={actual_max}")
    return ok


def apply_insert(cur, block: dict, dry_run: bool):
    table = block["target_table"]
    conflict = block.get("conflict_action", "IGNORE").upper()
    columns = block["columns"]
    rows = block["rows"]
    declared_total = block.get("row_counts", {}).get("total_rows")

    if declared_total is not None and declared_total != len(rows):
        print(f"  ✗  {table}: declared total_rows={declared_total} "
              f"but actual row count={len(rows)}")

    col_str = ", ".join(columns)
    placeholders = ", ".join("?" * len(columns))

    if conflict == "IGNORE":
        sql = f"INSERT OR IGNORE INTO {table} ({col_str}) VALUES ({placeholders})"
    elif conflict == "REPLACE":
        sql = f"INSERT OR REPLACE INTO {table} ({col_str}) VALUES ({placeholders})"
    else:  # FAIL
        sql = f"INSERT INTO {table} ({col_str}) VALUES ({placeholders})"

    inserted = 0
    for row in rows:
        values = strip_ref(row, columns)
        if not dry_run:
            cur.execute(sql, values)
            if cur.rowcount > 0:
                inserted += 1
        else:
            inserted += 1

    label = "would insert" if dry_run else "inserted"
    print(f"  ✓  {table}: {label} {inserted}/{len(rows)} rows "
          f"(conflict_action={conflict})")
    return inserted


def apply_update(cur, block: dict, dry_run: bool):
    table = block["target_table"]
    pk_col = block["pk_column"]
    columns = block["columns"]
    rows = block["rows"]
    declared_total = block.get("row_counts", {}).get("total_rows")

    if declared_total is not None and declared_total != len(rows):
        print(f"  ✗  {table}: declared total_rows={declared_total} "
              f"but actual row count={len(rows)}")

    set_clause = ", ".join(f"{col} = ?" for col in columns)
    sql = f"UPDATE {table} SET {set_clause} WHERE {pk_col} = ?"

    updated = 0
    for row in rows:
        values = [row[col] for col in columns] + [row[pk_col]]
        if not dry_run:
            cur.execute(sql, values)
            if cur.rowcount > 0:
                updated += 1
        else:
            updated += 1

    label = "would update" if dry_run else "updated"
    print(f"  ✓  {table}: {label} {updated}/{len(rows)} rows")
    return updated


def apply_patch(patch_path: str, dry_run: bool = False):
    with open(patch_path, encoding="utf-8") as f:
        patch = json.load(f)

    meta = patch.get("_meta", {})
    patch_id = meta.get("patch_id", os.path.basename(patch_path))
    print(f"\n{'='*60}")
    print(f"PATCH: {patch_id}")
    print(f"  {meta.get('description', '')}")
    if dry_run:
        print("  [DRY RUN — no changes will be written]")
    print(f"{'='*60}")

    conn = get_connection()
    cur = conn.cursor()

    # ── Baseline check ────────────────────────────────────────────────────
    baseline = meta.get("id_baseline", {})
    if baseline:
        print("\n── Baseline verification ──")
        check_baseline(cur, baseline, patch_id)

    # ── Determine block execution order ───────────────────────────────────
    import_order_raw = meta.get("import_order", [])
    # Parse "1. block_name_here" → "block_name_here"
    ordered_keys = []
    for item in import_order_raw:
        # strip leading "N. " prefix
        parts = item.split(". ", 1)
        key = parts[1].strip() if len(parts) == 2 else parts[0].strip()
        ordered_keys.append(key)

    # Fall back to dict insertion order for any blocks not listed
    all_block_keys = [k for k in patch.keys() if k != "_meta"]
    if ordered_keys:
        remaining = [k for k in all_block_keys if k not in ordered_keys]
        execution_order = ordered_keys + remaining
    else:
        execution_order = all_block_keys

    # ── Apply blocks ──────────────────────────────────────────────────────
    print("\n── Applying blocks ──")
    for key in execution_order:
        block = patch.get(key)
        if block is None:
            continue
        op = block.get("operation", "").upper()
        print(f"\n  [{key}]  operation={op}")
        if op == "INSERT":
            apply_insert(cur, block, dry_run)
        elif op == "UPDATE":
            apply_update(cur, block, dry_run)
        else:
            print(f"  ⚠  Unknown operation '{op}' — skipped")

    if not dry_run:
        conn.commit()
        print(f"\n✓ Patch {patch_id} committed.")
    else:
        print(f"\n[DRY RUN] Patch {patch_id} — no changes committed.")

    conn.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    dry = "--dry-run" in args
    paths = [a for a in args if not a.startswith("--")]

    if not paths:
        print("Usage: python scripts/apply_patch.py <patch.json> [<patch2.json> ...] [--dry-run]")
        sys.exit(1)

    for p in paths:
        apply_patch(p, dry_run=dry)
