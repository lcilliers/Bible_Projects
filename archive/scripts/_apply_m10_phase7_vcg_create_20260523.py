"""M10 Phase 7 — apply VCG design.

Per v2_8 §10.5. Per directive wa-cluster-M10-dir-003-phase7-vcg-create-v1-20260523.md.

Source: Sessions/Session_Clusters/M10/files phase 7/wa-cluster-M10-vcg-creation-v1-20260523.json
        (validated; 23 sub-groups, 69 VCGs, 1,325 verses; 2 anchor errors corrected by CC)

Operations:
- Op A: INSERT 69 verse_context_group rows (one per VCG). group_code = JSON's
        provisional_code; context_description = JSON's description.
- Op B: INSERT vcg_term links — per VCG, one row per (vcg_id, mti_term_id) where
        the VCG covers any of the term's verses.
- Op C: UPDATE verse_context.group_id for every is_relevant verse in the cluster
        to point at its new VCG (1,325 updates).
- Op D: Clear any prior is_anchor=1 on M10 verses, then set is_anchor=1 on the
        69 new anchor verses.

Modelled on scripts/_apply_m09_phase7_vcg_create_20260522.py.
"""
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
JSON_PATH = REPO / 'Sessions' / 'Session_Clusters' / 'M10' / 'files phase 7' / 'wa-cluster-M10-vcg-creation-v1-20260523.json'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
CLUSTER = 'M10'


def main() -> int:
    dry = '--dry-run' in sys.argv
    data = json.loads(JSON_PATH.read_text(encoding='utf-8'))

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Flatten VCG specs in sub-group sort order, then VCG order from JSON
    sg_rows = cur.execute(
        "SELECT subgroup_code FROM cluster_subgroup "
        "WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0 "
        "ORDER BY sort_order"
    ).fetchall()
    sg_order = [r['subgroup_code'] for r in sg_rows]
    print(f"Sub-group order ({len(sg_order)}): {sg_order}")

    specs: list[dict] = []
    for sg_code in sg_order:
        if sg_code not in data['subgroups']:
            print(f"WARN: {sg_code} not in JSON")
            continue
        for vcg in data['subgroups'][sg_code]['vcgs']:
            specs.append({
                'subgroup_code': sg_code,
                'group_code': vcg['provisional_code'],
                'description': vcg.get('description') or '',
                'verses': vcg.get('verses') or [],
                'anchor_vc_id': vcg['anchor_vc_id'],
            })
    print(f"Loaded {len(specs)} VCG specs from JSON")

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
    print('  No existing VCGs with our codes (clean to insert)')

    prior_anchors = cur.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    print(f'  Prior is_anchor=1 rows on M10 verses: {prior_anchors} (will be cleared by Op D)')

    # vc → mti_term_id map (for is_relevant=1 rows)
    vc_to_term: dict[int, int] = {}
    for r in cur.execute("""
        SELECT vc.id, vc.mti_term_id FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchall():
        vc_to_term[r['id']] = r['mti_term_id']

    # Validate every JSON vc_id is in the cluster's is_relevant set
    all_json_vc = [v for s in specs for v in s['verses']]
    bad = [v for v in all_json_vc if v not in vc_to_term]
    assert not bad, f"{len(bad)} JSON vc_ids not in M10 is_relevant set (first 5: {bad[:5]})"
    print(f'  All {len(all_json_vc)} JSON vc_ids are M10 is_relevant rows')
    assert len(all_json_vc) == len(set(all_json_vc)), \
        f"JSON has {len(all_json_vc) - len(set(all_json_vc))} duplicate vc_id entries"
    print('  No global duplicates in JSON')
    # Anchors in members
    for spec in specs:
        assert spec['anchor_vc_id'] in spec['verses'], \
            f"{spec['group_code']}: anchor {spec['anchor_vc_id']} not in members"
    print(f'  All {len(specs)} anchors are in their VCG members')

    if dry:
        print('\n[DRY-RUN — no writes]')
        conn.close()
        return 0

    # Apply
    print()
    print('=== APPLYING ===')
    cur.execute('BEGIN')
    try:
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
        vcg_term_pairs: set[tuple[int, int]] = set()
        for spec in specs:
            vcg_id = code_to_id[spec['group_code']]
            for vc_id in spec['verses']:
                mti_id = vc_to_term.get(vc_id)
                if mti_id is None:
                    raise RuntimeError(f'vc_id={vc_id} not in M10 is_relevant set (unexpected)')
                vcg_term_pairs.add((vcg_id, mti_id))
        for vcg_id, mti_id in sorted(vcg_term_pairs):
            cur.execute(
                "INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, "
                "delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, 'Phase 7 routing', 0, ?, ?)",
                (vcg_id, mti_id, NOW, NOW),
            )
        print(f'  Op B: inserted {len(vcg_term_pairs)} vcg_term rows')

        # Op C — UPDATE verse_context.group_id
        n_updated = 0
        for spec in specs:
            vcg_id = code_to_id[spec['group_code']]
            for vc_id in spec['verses']:
                cur.execute(
                    "UPDATE verse_context SET group_id=? "
                    "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                    (vcg_id, vc_id),
                )
                n_updated += cur.rowcount
        print(f'  Op C: routed {n_updated} verses to VCGs (expected 1325)')
        assert n_updated == 1325

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
        "SELECT COUNT(*) FROM verse_context_group "
        "WHERE group_code LIKE 'M10-%-VCG-%' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f'  New M10 VCGs in DB: {n_new_vcgs}')

    n_routed = cur.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
          AND vcg.group_code LIKE 'M10-%-VCG-%'
    """, (CLUSTER,)).fetchone()[0]
    print(f'  is_relevant verses routed to new M10 VCGs: {n_routed} (expected 1325)')

    n_a = cur.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    print(f'  is_anchor=1 on M10 verses: {n_a} (expected {len(specs)})')

    # Per-VCG verse counts
    print()
    print('  Per-VCG verse counts (alphabetical):')
    rows = cur.execute("""
        SELECT vcg.group_code, COUNT(vc.id) AS n
        FROM verse_context_group vcg
        LEFT JOIN verse_context vc ON vc.group_id = vcg.id
            AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        WHERE vcg.group_code LIKE 'M10-%-VCG-%' AND COALESCE(vcg.delete_flagged,0)=0
        GROUP BY vcg.group_code ORDER BY vcg.group_code
    """).fetchall()
    for r in rows:
        print(f'    {r["group_code"]:<22s} {r["n"]:>4d}')

    conn.close()
    print()
    print('=== M10 PHASE 7 COMPLETE ===')
    return 0


if __name__ == '__main__':
    sys.exit(main())
