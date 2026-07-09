"""M08 Phase 5.5 — Set-aside patch for non-M08-content verses.

Per researcher Option 2 decision (2026-05-20): 174 verses whose terms STAY in M08
(via v2_8 §6.3.2 cross-register verses) but whose individual verse-meanings carry
no M08-relational content are set_aside before Phase 6 fires. This keeps Phase 5
sub-groups characteristic-only (clean §8.0 compliance).

Operations:
  Op A: UPDATE verse_context SET is_relevant=0, set_aside_reason=?
        for 122 vc_ids with reason M22_REGISTER
  Op B: UPDATE verse_context SET is_relevant=0, set_aside_reason=?
        for 52 vc_ids with reason NO_INNER_BEING

Source: WA-M08-subgroup-mapping-resolved-v2-20260520.json (set_aside_vc_ids block)
"""
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
SRC = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-subgroup-mapping-resolved-v2-20260520.json'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

REASONS = {
    'M22_REGISTER': 'non-M08 content — M22-register (divine majesty / God-directed exaltation); term STAYS in M08 via other verses (v2_8 §6.3.2)',
    'NO_INNER_BEING': 'non-M08 content — narrative marker / neutral assertiveness; no inner-being state evidenced in this verse as an individual unit of analysis',
}

spec = json.loads(SRC.read_text(encoding='utf-8'))
m22_ids = list(spec['set_aside_vc_ids']['M22_REGISTER'])
nib_ids = list(spec['set_aside_vc_ids']['NO_INNER_BEING'])

assert len(m22_ids) == 122, f'Expected 122 M22 vc_ids, got {len(m22_ids)}'
assert len(nib_ids) == 52, f'Expected 52 NIB vc_ids, got {len(nib_ids)}'
assert set(m22_ids).isdisjoint(set(nib_ids)), 'vc_id overlap between M22 and NIB lists'

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Pre-checks: confirm all 174 vc_ids exist, belong to M08 terms, are currently is_relevant=1 with no set_aside_reason
print('=== PRE-CHECKS ===')
all_ids = m22_ids + nib_ids
qmarks = ','.join('?' * len(all_ids))
rows = cur.execute(f"""
    SELECT vc.id, vc.is_relevant, vc.set_aside_reason, mt.cluster_code, COALESCE(vc.delete_flagged,0) AS df
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE vc.id IN ({qmarks})
""", all_ids).fetchall()
print(f'  Loaded {len(rows)}/{len(all_ids)} vc rows')
assert len(rows) == len(all_ids), 'Some vc_ids not found in DB'
mismatches = 0
for r in rows:
    if r['cluster_code'] != 'M08':
        print(f'  WARN: vc_id={r["id"]} not in M08 (cluster={r["cluster_code"]})')
        mismatches += 1
    if r['is_relevant'] != 1:
        print(f'  WARN: vc_id={r["id"]} already is_relevant={r["is_relevant"]}')
        mismatches += 1
    if r['set_aside_reason']:
        print(f'  WARN: vc_id={r["id"]} already has set_aside_reason={r["set_aside_reason"]!r}')
        mismatches += 1
    if r['df']:
        print(f'  WARN: vc_id={r["id"]} delete_flagged=1')
        mismatches += 1
if mismatches:
    raise SystemExit(f'Pre-check failures: {mismatches}')
print(f'  All 174 vc_ids in M08, is_relevant=1, no prior set_aside_reason, delete_flagged=0 OK')

# Pre counts
n_rel_pre = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id=vc.mti_term_id
    WHERE mt.cluster_code='M08' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
print(f'  M08 is_relevant=1 vc count (pre): {n_rel_pre}')

# Apply
print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    # Op A: M22_REGISTER
    qm = ','.join('?' * len(m22_ids))
    cur.execute(
        f"UPDATE verse_context SET is_relevant=0, set_aside_reason=? "
        f"WHERE id IN ({qm}) AND is_relevant=1",
        (REASONS['M22_REGISTER'], *m22_ids)
    )
    n_a = cur.rowcount
    if n_a != 122:
        raise RuntimeError(f'Op A: expected 122 rows, got {n_a}')
    print(f'  Op A (M22_REGISTER): {n_a} rows updated')

    # Op B: NO_INNER_BEING
    qm = ','.join('?' * len(nib_ids))
    cur.execute(
        f"UPDATE verse_context SET is_relevant=0, set_aside_reason=? "
        f"WHERE id IN ({qm}) AND is_relevant=1",
        (REASONS['NO_INNER_BEING'], *nib_ids)
    )
    n_b = cur.rowcount
    if n_b != 52:
        raise RuntimeError(f'Op B: expected 52 rows, got {n_b}')
    print(f'  Op B (NO_INNER_BEING): {n_b} rows updated')

    conn.commit()
    print(f'  Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

# Post-checks
print()
print('=== POST-CHECKS ===')
n_rel_post = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id=vc.mti_term_id
    WHERE mt.cluster_code='M08' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
print(f'  M08 is_relevant=1 vc count (post): {n_rel_post}  (expected {n_rel_pre - 174})')
assert n_rel_post == n_rel_pre - 174

# Spot-check a few rows
print()
print('  Spot check (first 3 of each reason):')
for vid in m22_ids[:3]:
    r = cur.execute("SELECT id, is_relevant, set_aside_reason FROM verse_context WHERE id=?", (vid,)).fetchone()
    print(f'    [M22] vc_id={r["id"]} is_relevant={r["is_relevant"]} reason={r["set_aside_reason"][:60]!r}...')
for vid in nib_ids[:3]:
    r = cur.execute("SELECT id, is_relevant, set_aside_reason FROM verse_context WHERE id=?", (vid,)).fetchone()
    print(f'    [NIB] vc_id={r["id"]} is_relevant={r["is_relevant"]} reason={r["set_aside_reason"][:60]!r}...')

# Verify all 174 are now is_relevant=0 with reason set
print()
all_set = cur.execute(f"""
    SELECT COUNT(*) FROM verse_context
    WHERE id IN ({','.join('?'*len(all_ids))})
      AND is_relevant=0 AND set_aside_reason IS NOT NULL
""", all_ids).fetchone()[0]
print(f'  All 174 rows confirmed is_relevant=0 with set_aside_reason: {all_set}/174')
assert all_set == 174

print()
print('=== M08 PHASE 5.5 SET-ASIDE COMPLETE ===')
print(f'  122 vc_ids: M22_REGISTER reason applied')
print(f'   52 vc_ids: NO_INNER_BEING reason applied')
print(f'  M08 substantive corpus: {n_rel_pre} -> {n_rel_post}')
print()
print('Ready for Phase 6: route 296 remaining is_relevant=1 vc_ids')
print('to verse_context_group rows under their respective sub-group codes.')
conn.close()
