"""M08 Phase 7 — apply VCG design.

Per v2_8 §10.5. Per directive WA-M08-dir-003-vcg-create-v1-20260520.md.

Operations:
- Op 0: Soft-delete 3 duplicate rum vc rows (same vr+mti+css; would violate
        UNIQUE constraint on Op C when both get the same new group_id).
        Pairs: (34234,34306 Dan 11:12) (34235,34295 Dan 11:36) (34230,34263 Psa 75:7).
        Keep lower vc_id of each pair; soft-delete higher. None are anchors.
- Op A: INSERT verse_context_group rows (25 VCGs).
       group_code = provisional code from JSON (e.g. M08-A1-VCG-01).
- Op B: INSERT vcg_term links — per VCG, one row per (vcg_id, mti_term_id)
       where the VCG covers any of the term's verses.
- Op C: UPDATE verse_context.group_id for every is_relevant verse to its new VCG id.
       Skips the 3 soft-deleted duplicates → 293 updates instead of 296.
- Op D: Clear prior M08 is_anchor=1, then set is_anchor=1 on the 25 new anchors.
"""
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
JSON_PATH = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-vcg-creation-v1-20260520.json'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
CLUSTER = 'M08'

data = json.loads(JSON_PATH.read_text(encoding='utf-8'))

# Op 0: duplicate rum vc_ids to soft-delete (keep lower of each pair)
DUPLICATES_TO_SOFTDELETE = [34306, 34295, 34263]  # higher vc_id of each pair

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Flatten VCG specs in deterministic order (sub-group code, then VCG order from JSON)
sg_order = ['M08-A1','M08-A2','M08-A3','M08-A4','M08-B','M08-C','M08-D','M08-E','M08-BOUNDARY']
specs = []
for sg_code in sg_order:
    if sg_code not in data['subgroups']:
        continue
    for vcg in data['subgroups'][sg_code]['vcgs']:
        specs.append({
            'subgroup_code': sg_code,
            'group_code': vcg['provisional_code'],
            'description': vcg['description'],
            'verses': vcg['verses'],
            'anchor_vc_id': vcg['anchor_vc_id'],
        })
print(f'Loaded {len(specs)} VCG specs from JSON')

# Pre-checks
print()
print('=== PRE-CHECKS ===')

# No existing VCGs with these codes
qmarks = ','.join('?' * len(specs))
existing = [r[0] for r in cur.execute(
    f"SELECT group_code FROM verse_context_group WHERE group_code IN ({qmarks}) "
    f"AND COALESCE(delete_flagged,0)=0",
    [s['group_code'] for s in specs],
).fetchall()]
assert not existing, f'VCG codes already in DB: {existing}'
print(f'  No existing VCGs with our codes (clean to insert)')

prior_anchors = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
""", (CLUSTER,)).fetchone()[0]
print(f'  Prior is_anchor=1 rows on M08 verses: {prior_anchors} (will be cleared by Op D)')

# Op 0 pre-check: confirm the 3 duplicates are present, is_relevant=1, not anchors
for vid in DUPLICATES_TO_SOFTDELETE:
    r = cur.execute(
        "SELECT id, is_relevant, is_anchor, COALESCE(delete_flagged,0) AS df FROM verse_context WHERE id=?",
        (vid,)
    ).fetchone()
    assert r, f'Duplicate vc_id={vid} not found'
    assert r['is_relevant'] == 1, f'vc_id={vid} not is_relevant=1'
    assert r['is_anchor'] == 0, f'vc_id={vid} is an anchor — would break apply'
    assert r['df'] == 0, f'vc_id={vid} already soft-deleted'
print(f'  Op 0 pre-check: 3 duplicate vc rows verified (34306, 34295, 34263 all is_relevant=1, not anchors)')

# Build the route set excluding soft-deletes
softdelete_set = set(DUPLICATES_TO_SOFTDELETE)

# Apply
print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    # Op 0 — soft-delete the 3 duplicates
    for vid in DUPLICATES_TO_SOFTDELETE:
        cur.execute(
            "UPDATE verse_context SET delete_flagged=1, is_relevant=0 WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (vid,)
        )
        assert cur.rowcount == 1, f'Op 0: vc_id={vid} not soft-deleted'
    print(f'  Op 0: soft-deleted {len(DUPLICATES_TO_SOFTDELETE)} duplicate rum vc rows')

    # Op A — INSERT verse_context_group
    code_to_id: dict[str, int] = {}
    for spec in specs:
        cur.execute(
            "INSERT INTO verse_context_group (group_code, context_description, vertical_pass_flag) "
            "VALUES (?, ?, 0)",
            (spec['group_code'], spec['description']),
        )
        code_to_id[spec['group_code']] = cur.lastrowid
    print(f'  Op A: inserted {len(specs)} verse_context_group rows')

    # Op B — vcg_term links
    vc_to_term: dict[int, int] = {}
    for r in cur.execute("""
        SELECT vc.id, vc.mti_term_id FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchall():
        vc_to_term[r['id']] = r['mti_term_id']

    vcg_term_pairs = set()
    for spec in specs:
        vcg_id = code_to_id[spec['group_code']]
        for vc_id in spec['verses']:
            if vc_id in softdelete_set:
                continue  # duplicate; its kept-pair sibling carries the term-VCG link
            mti_id = vc_to_term.get(vc_id)
            if mti_id is None:
                raise RuntimeError(f'vc_id={vc_id} not in M08 is_relevant set (unexpected)')
            vcg_term_pairs.add((vcg_id, mti_id))

    for vcg_id, mti_id in sorted(vcg_term_pairs):
        cur.execute(
            "INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, delete_flagged, created_at, last_updated_date) "
            "VALUES (?, ?, 'Phase 7 routing', 0, ?, ?)",
            (vcg_id, mti_id, NOW, NOW),
        )
    print(f'  Op B: inserted {len(vcg_term_pairs)} vcg_term rows')

    # Op C — UPDATE verse_context.group_id (skip soft-deleted duplicates)
    n_updated = 0
    n_skipped = 0
    for spec in specs:
        vcg_id = code_to_id[spec['group_code']]
        for vc_id in spec['verses']:
            if vc_id in softdelete_set:
                n_skipped += 1
                continue
            cur.execute(
                "UPDATE verse_context SET group_id=? "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (vcg_id, vc_id),
            )
            n_updated += cur.rowcount
    expected_updates = 296 - len(softdelete_set)
    print(f'  Op C: routed {n_updated} verses to VCGs (expected {expected_updates}, skipped {n_skipped} soft-deleted duplicates)')
    assert n_updated == expected_updates

    # Op D — clear prior anchors, then set new
    cur.execute("""
        UPDATE verse_context SET is_anchor=0
        WHERE id IN (
            SELECT vc.id FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
        )
    """, (CLUSTER,))
    cleared = cur.rowcount
    print(f'  Op D (clear): cleared {cleared} prior anchors')

    n_anchors = 0
    for spec in specs:
        cur.execute(
            "UPDATE verse_context SET is_anchor=1 "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (spec['anchor_vc_id'],),
        )
        n_anchors += cur.rowcount
    print(f'  Op D (set): set is_anchor=1 on {n_anchors} verses (expected {len(specs)})')
    assert n_anchors == len(specs)

    conn.commit()
    print(f'  Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

# Post-checks
print()
print('=== POST-CHECKS ===')

n_new_vcgs = cur.execute(
    "SELECT COUNT(*) FROM verse_context_group WHERE group_code LIKE 'M08-%-VCG-%' AND COALESCE(delete_flagged,0)=0"
).fetchone()[0]
print(f'  New M08 VCGs in DB: {n_new_vcgs}')

expected_routed = 296 - len(softdelete_set)
n_routed = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN verse_context_group vcg ON vcg.id = vc.group_id
    WHERE mt.cluster_code=? AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0
      AND vcg.group_code LIKE 'M08-%-VCG-%'
""", (CLUSTER,)).fetchone()[0]
print(f'  is_relevant verses routed to new M08 VCGs: {n_routed} (expected {expected_routed})')

n_a = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
""", (CLUSTER,)).fetchone()[0]
print(f'  is_anchor=1 on M08 verses: {n_a} (expected {len(specs)})')

# Per-VCG verse counts
print()
print('  Per-VCG verse counts:')
rows = cur.execute("""
    SELECT vcg.group_code, COUNT(vc.id) AS n
    FROM verse_context_group vcg
    LEFT JOIN verse_context vc ON vc.group_id = vcg.id AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    WHERE vcg.group_code LIKE 'M08-%-VCG-%' AND COALESCE(vcg.delete_flagged,0)=0
    GROUP BY vcg.group_code ORDER BY vcg.group_code
""").fetchall()
for r in rows:
    print(f'    {r["group_code"]:24s} {r["n"]}')

print()
print('=== M08 PHASE 7 COMPLETE ===')
print(f'- {len(specs)} VCGs created (Op A)')
print(f'- {len(vcg_term_pairs)} vcg_term links (Op B)')
print(f'- {n_routed} verses routed to new VCGs (Op C)')
print(f'- {n_a} anchors set (Op D); {cleared} prior anchors cleared')
print(f'- Old (inherited) VCGs still present — Phase 8 dissolves them')
print('Ready for Phase 8 — Dissolve old VCGs (v2_8 §11).')
conn.close()
