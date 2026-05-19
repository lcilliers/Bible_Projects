"""M07 Phase 7 — apply VCG design.

Per v2_8 §10.5. Per directive WA-M07-dir-003-vcg-create-v1-20260519.md.

Operations:
- Op A: INSERT verse_context_group rows (29 VCGs).
       group_code = provisional code from JSON (e.g. M07-A-VCG-01).
- Op B: INSERT vcg_term links — per VCG, one row per (vcg_id, mti_term_id)
       where the VCG covers any of the term's verses.
- Op C: UPDATE verse_context.group_id for every is_relevant verse to
       its new VCG id. WHERE delete_flagged=0.
- Op D: UPDATE verse_context.is_anchor=1 for every Phase 7 anchor;
       reset prior is_anchor=1 on M07 verses to 0 first (clear slate).
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
import json
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

DB = Path('database/bible_research.db')
JSON_PATH = Path('Sessions/Session_Clusters/M07/files phase 7/WA-M07-vcg-creation-v1-20260519.json')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
CLUSTER = 'M07'

# Load JSON
with open(JSON_PATH, encoding='utf-8') as f:
    data = json.load(f)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Flatten: list of vcg specs in deterministic order (sub-group code, then VCG seq)
specs = []
for sg_code in sorted(data['subgroups'].keys()):
    for vcg in data['subgroups'][sg_code]['vcgs']:
        specs.append({
            'subgroup_code': sg_code,
            'group_code': vcg['provisional_code'],
            'description': vcg['description'],
            'verses': vcg['verses'],
            'anchor_vc_id': vcg['anchor_vc_id'],
        })
print(f"Loaded {len(specs)} VCG specs from JSON")

# Pre-checks
print()
print('=== PRE-CHECKS ===')
# No existing VCGs with these codes
existing_codes = [r[0] for r in cur.execute(
    f"SELECT group_code FROM verse_context_group WHERE group_code IN ({','.join('?' * len(specs))}) "
    f"AND COALESCE(delete_flagged,0)=0",
    [s['group_code'] for s in specs],
).fetchall()]
assert not existing_codes, f"VCG codes already in DB: {existing_codes}"
print(f"  No existing VCGs with our codes (clean to insert)")

# Pre-state: prior anchors on M07 verses
prior_anchors = cur.execute(
    """
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
    """,
    (CLUSTER,),
).fetchone()[0]
print(f"  Prior is_anchor=1 rows on M07 verses: {prior_anchors} (will be cleared by Op D)")

# Apply
print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    # Op A — INSERT verse_context_group
    code_to_id = {}
    for spec in specs:
        cur.execute(
            "INSERT INTO verse_context_group (group_code, context_description, vertical_pass_flag) "
            "VALUES (?, ?, ?)",
            (spec['group_code'], spec['description'], 0),
        )
        code_to_id[spec['group_code']] = cur.lastrowid
    print(f"  Op A: inserted {len(specs)} verse_context_group rows")

    # Op B — INSERT vcg_term links (per VCG, per term covered)
    # Build (vcg_id, mti_term_id) pairs
    vc_to_term = {}
    for r in cur.execute(
        """
        SELECT vc.id, vc.mti_term_id FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        """,
        (CLUSTER,),
    ).fetchall():
        vc_to_term[r['id']] = r['mti_term_id']

    vcg_term_pairs = set()
    for spec in specs:
        vcg_id = code_to_id[spec['group_code']]
        for vc_id in spec['verses']:
            mti_id = vc_to_term.get(vc_id)
            if mti_id is None:
                raise RuntimeError(f"vc_id={vc_id} not in M07 is_relevant set (unexpected)")
            vcg_term_pairs.add((vcg_id, mti_id))

    for vcg_id, mti_id in sorted(vcg_term_pairs):
        cur.execute(
            "INSERT INTO vcg_term (vcg_id, mti_term_id, placement_note, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?)",
            (vcg_id, mti_id, 'Phase 7 routing', NOW, NOW),
        )
    print(f"  Op B: inserted {len(vcg_term_pairs)} vcg_term rows")

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
    print(f"  Op C: routed {n_updated} verses to VCGs")
    assert n_updated == 363

    # Op D — clear prior anchors on M07, then set new
    cur.execute(
        """
        UPDATE verse_context SET is_anchor=0
        WHERE id IN (
            SELECT vc.id FROM verse_context vc
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.cluster_code=? AND vc.is_anchor=1
              AND COALESCE(vc.delete_flagged,0)=0
        )
        """,
        (CLUSTER,),
    )
    cleared = cur.rowcount
    print(f"  Op D (clear): cleared {cleared} prior anchors")

    n_anchors = 0
    for spec in specs:
        cur.execute(
            "UPDATE verse_context SET is_anchor=1 "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (spec['anchor_vc_id'],),
        )
        n_anchors += cur.rowcount
    print(f"  Op D (set): set is_anchor=1 on {n_anchors} verses (expected {len(specs)})")
    assert n_anchors == len(specs)

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Post-checks
print()
print('=== POST-CHECKS ===')

# H3 — every M07 mti_term has a vcg_term link
h3 = cur.execute(
    """
    SELECT COUNT(*) FROM mti_terms mt
    WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
      AND NOT EXISTS (
        SELECT 1 FROM vcg_term vt
        JOIN verse_context_group vcg ON vcg.id = vt.vcg_id
        WHERE vt.mti_term_id = mt.id AND COALESCE(vt.delete_flagged,0)=0
          AND vcg.group_code LIKE 'M07%'
      )
    """,
    (CLUSTER,),
).fetchone()[0]
print(f"  H3 (M07 mti_terms without vcg_term link to a new M07 VCG): {h3}")

# Every is_relevant vc has group_id pointing at a new M07 VCG
n_routed = cur.execute(
    """
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN verse_context_group vcg ON vcg.id = vc.group_id
    WHERE mt.cluster_code=? AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0
      AND vcg.group_code LIKE 'M07%-VCG-%'
    """,
    (CLUSTER,),
).fetchone()[0]
print(f"  is_relevant verses routed to new M07 VCGs: {n_routed} (expected 363)")

# Anchors
n_a = cur.execute(
    """
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0
    """,
    (CLUSTER,),
).fetchone()[0]
print(f"  is_anchor=1 on M07 verses: {n_a} (expected {len(specs)})")

# R4 — every M07 OWNER mti_term has at least one anchor
mt_no_anchor = cur.execute(
    """
    SELECT mt.id, mt.strongs_number, mt.transliteration FROM mti_terms mt
    JOIN wa_term_inventory wti ON wti.strongs_number = mt.strongs_number
    WHERE mt.cluster_code=? AND wti.term_owner_type='OWNER'
      AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(wti.delete_flagged,0)=0
      AND NOT EXISTS (
        SELECT 1 FROM verse_context vc
        WHERE vc.mti_term_id=mt.id AND vc.is_anchor=1
          AND COALESCE(vc.delete_flagged,0)=0
      )
    """,
    (CLUSTER,),
).fetchall()
print(f"  R4 (M07 OWNER mti_terms without active anchor): {len(mt_no_anchor)}")
if mt_no_anchor:
    print("    (informational — these terms have no Phase 7 anchor; usually because all their verses are in a sub-group whose anchor is on a different term)")
    for r in mt_no_anchor[:10]:
        print(f"    {r['strongs_number']} {r['transliteration']}")

print()
print('=== M07 PHASE 7 COMPLETE ===')
print(f"- {len(specs)} VCGs created")
print(f"- {len(vcg_term_pairs)} vcg_term links")
print(f"- {n_routed} verses routed to new VCGs")
print(f"- {n_a} anchors set")
print(f"- Old (inherited) VCGs still present in DB — Phase 8 dissolves them")
print("Ready for Phase 8 — Dissolve old VCGs (v2_8 §11).")
conn.close()
