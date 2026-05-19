"""M07 Phase 8 — dissolve 40 inherited VCGs.

Per directive WA-M07-dir-004-vcg-dissolve-v1-20260519.
Operations:
- Op A: UPDATE verse_context_group SET delete_flagged=1 + notes
- Op B: UPDATE vcg_term SET delete_flagged=1 for links to those VCGs
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
DIRECTIVE = 'wa-cluster-M07-dir-004-vcg-dissolve-v1-20260519'

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Identify inherited VCGs
inherited_ids = [r[0] for r in cur.execute("""
    SELECT DISTINCT vcg.id FROM verse_context_group vcg
    JOIN vcg_term vt ON vt.vcg_id = vcg.id
    JOIN mti_terms mt ON mt.id = vt.mti_term_id
    WHERE mt.cluster_code='M07'
      AND COALESCE(vt.delete_flagged,0)=0
      AND COALESCE(mt.delete_flagged,0)=0
      AND COALESCE(vcg.delete_flagged,0)=0
      AND NOT (vcg.group_code LIKE 'M07%-VCG-%')
""").fetchall()]
print(f"Inherited VCGs to dissolve: {len(inherited_ids)}")
assert len(inherited_ids) == 40, f"Expected 40, got {len(inherited_ids)}"

# Pre-check: ensure all are empty of is_relevant references
ph = ','.join('?' * len(inherited_ids))
n_active = cur.execute(
    f"""SELECT COUNT(*) FROM verse_context
        WHERE group_id IN ({ph}) AND is_relevant=1 AND COALESCE(delete_flagged,0)=0""",
    inherited_ids,
).fetchone()[0]
print(f"is_relevant verses still pointing at inherited VCGs (pre): {n_active}")
assert n_active == 0, "FAIL: some is_relevant verses still reference inherited VCGs"

# Apply
print()
print("=== APPLYING ===")
cur.execute('BEGIN')
try:
    # Op A — soft-delete VCG rows
    note = f"Dissolved at M07 Phase 8 {NOW} (replaced by M07-*-VCG-NN; per {DIRECTIVE})"
    cur.execute(
        f"""UPDATE verse_context_group
            SET delete_flagged=1, notes=?
            WHERE id IN ({ph}) AND COALESCE(delete_flagged,0)=0""",
        [note] + inherited_ids,
    )
    n_a = cur.rowcount
    print(f"  Op A: {n_a} verse_context_group rows soft-deleted")
    assert n_a == len(inherited_ids)

    # Op B — soft-delete vcg_term links
    cur.execute(
        f"""UPDATE vcg_term
            SET delete_flagged=1, last_updated_date=?
            WHERE vcg_id IN ({ph}) AND COALESCE(delete_flagged,0)=0""",
        [NOW] + inherited_ids,
    )
    n_b = cur.rowcount
    print(f"  Op B: {n_b} vcg_term rows soft-deleted")

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Post-checks
print()
print("=== POST-CHECKS ===")
n_old_active = cur.execute(f"""
    SELECT COUNT(*) FROM verse_context_group vcg
    JOIN vcg_term vt ON vt.vcg_id = vcg.id
    JOIN mti_terms mt ON mt.id = vt.mti_term_id
    WHERE mt.cluster_code='M07'
      AND COALESCE(vcg.delete_flagged,0)=0
      AND COALESCE(vt.delete_flagged,0)=0
      AND NOT (vcg.group_code LIKE 'M07%-VCG-%')
""").fetchone()[0]
print(f"  Inherited VCGs still active for M07: {n_old_active} (expected 0)")
assert n_old_active == 0

n_new_active = cur.execute(f"""
    SELECT COUNT(DISTINCT vcg.id) FROM verse_context_group vcg
    JOIN vcg_term vt ON vt.vcg_id = vcg.id
    JOIN mti_terms mt ON mt.id = vt.mti_term_id
    WHERE mt.cluster_code='M07'
      AND COALESCE(vcg.delete_flagged,0)=0
      AND COALESCE(vt.delete_flagged,0)=0
      AND vcg.group_code LIKE 'M07%-VCG-%'
""").fetchone()[0]
print(f"  New (Phase 7) VCGs active for M07: {n_new_active} (expected 29)")
assert n_new_active == 29

# H5: orphan VCG with no active vc references (across the dissolved set, all are now soft-deleted so excluded)
h5 = cur.execute(f"""
    SELECT COUNT(*) FROM verse_context_group vcg
    JOIN vcg_term vt ON vt.vcg_id = vcg.id
    JOIN mti_terms mt ON mt.id = vt.mti_term_id
    LEFT JOIN verse_context vc ON vc.group_id = vcg.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    WHERE mt.cluster_code='M07'
      AND COALESCE(vcg.delete_flagged,0)=0
      AND COALESCE(vt.delete_flagged,0)=0
      AND vc.id IS NULL
    GROUP BY vcg.id
""").fetchall()
print(f"  H5 (active VCGs with 0 is_relevant references): {len(h5)} (expected 0)")

print()
print("=== M07 PHASE 8 COMPLETE ===")
print(f"- 40 inherited VCGs soft-deleted")
print(f"- {n_b} vcg_term links soft-deleted")
print(f"- 29 Phase 7 VCGs remain active for M07")
print("Ready for Phase 8.5 — BOUNDARY resolution (v2_8 §11A).")
conn.close()
