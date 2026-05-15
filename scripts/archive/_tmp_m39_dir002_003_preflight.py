"""Pre-flight verifier for M39 dir-002 (A) and dir-003 (B) mapping directives."""
import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
c = sqlite3.connect('database/bible_research.db')
c.row_factory = sqlite3.Row

# Directive 002 — M39-A
DIR_A_VCG_UPDATES = [
    # (vcg_id, expected_group_code)
    (340,  '2330-001'),
    (561,  '795-003'),
    (1119, '5470-001'),
    (1121, '888-001'),
    (1123, '888-003'),
    (1126, '889-001'),
    (1127, '889-002'),
    (1641, '984-001'),
    (3087, '1301-001'),
]
DIR_A_VC_ASSIGNS = [
    # (vr_id, mti_term_id, target_group_id, target_group_code)
    (117146, 795,  560,  '795-002'),
    (92213,  984,  1641, '984-001'),
    (167037, 889,  1128, '889-003'),
    (167044, 889,  1128, '889-003'),
    (167048, 889,  1128, '889-003'),
    (167049, 889,  1127, '889-002'),
    (167022, 889,  1127, '889-002'),
    (24847,  889,  1128, '889-003'),
    (167001, 5470, 1119, '5470-001'),
    (166982, 888,  1123, '888-003'),
    (166996, 5470, 1119, '5470-001'),
    (166971, 888,  1123, '888-003'),
    (166972, 888,  1123, '888-003'),
    (166973, 888,  1123, '888-003'),
    (166993, 5470, 1119, '5470-001'),
    (166994, 5470, 1119, '5470-001'),
]

# Directive 003 — M39-B
DIR_B_VCG_UPDATES = [
    (1587, '542-001'),
    (2837, '632-001'),
    (2838, '632-002'),
    (2839, '632-003'),
]
DIR_B_VC_ASSIGNS = [
    (4188,  542, 1587, '542-001'),
    (4189,  542, 1587, '542-001'),
    (4190,  542, 1587, '542-001'),
    (59830, 632, 2839, '632-003'),
    (59831, 632, 2839, '632-003'),
    (59832, 632, 2839, '632-003'),
    (59833, 632, 2838, '632-002'),
    (4197,  542, 1587, '542-001'),
    (59838, 632, 2839, '632-003'),
    (4198,  542, 1587, '542-001'),
    (59836, 632, 2838, '632-002'),
    (12533, 632, 2838, '632-002'),
    (12542, 632, 2838, '632-002'),
    (12560, 632, 2838, '632-002'),
]


def verify_vcg_updates(label, items):
    print(f"\n{label} — verse_context_group rows ({len(items)} expected):")
    errs = 0
    for vcg_id, expected_code in items:
        r = c.execute("""SELECT id, group_code, COALESCE(delete_flagged,0) deleted
                         FROM verse_context_group WHERE id=?""", (vcg_id,)).fetchone()
        if not r:
            print(f"  ❌ vcg_id={vcg_id}  NOT FOUND")
            errs += 1
            continue
        if r['group_code'] != expected_code:
            print(f"  ❌ vcg_id={vcg_id}  DB code={r['group_code']!r} expected={expected_code!r}")
            errs += 1
            continue
        if r['deleted']:
            print(f"  ❌ vcg_id={vcg_id} {expected_code:<10}  delete_flagged=1")
            errs += 1
            continue
        print(f"  ✓ vcg_id={vcg_id:<5} group_code={expected_code}")
    return errs


def verify_vc_assigns(label, items, expected_subgroup):
    print(f"\n{label} — verse_context UPDATE targets ({len(items)} expected):")
    errs = 0
    for vr_id, mti_id, target_gid, target_code in items:
        # vc row exists, is_relevant=1, group_id IS NULL
        vc = c.execute("""SELECT id, group_id, is_relevant, set_aside_reason,
                                  COALESCE(delete_flagged,0) deleted
                          FROM verse_context
                          WHERE verse_record_id=? AND mti_term_id=?""",
                       (vr_id, mti_id)).fetchone()
        if not vc:
            print(f"  ❌ vr={vr_id} mti={mti_id}  NO verse_context row")
            errs += 1
            continue
        if vc['deleted']:
            print(f"  ❌ vr={vr_id} mti={mti_id}  delete_flagged=1")
            errs += 1
            continue
        if vc['is_relevant'] != 1:
            print(f"  ⚠  vr={vr_id} mti={mti_id}  is_relevant={vc['is_relevant']}")
        if vc['group_id'] is not None:
            print(f"  ⚠  vr={vr_id} mti={mti_id}  group_id ALREADY={vc['group_id']} (will overwrite)")
        # Target group exists and matches code
        tg = c.execute("SELECT group_code FROM verse_context_group WHERE id=?",
                       (target_gid,)).fetchone()
        if not tg:
            print(f"  ❌ vr={vr_id} mti={mti_id}  target group_id={target_gid} NOT FOUND")
            errs += 1
            continue
        if tg['group_code'] != target_code:
            print(f"  ❌ vr={vr_id} mti={mti_id}  target gid={target_gid} code={tg['group_code']!r} expected={target_code!r}")
            errs += 1
            continue
        # mti_term sub-group placement matches expected segment
        sg = c.execute("""SELECT cs.subgroup_code
                          FROM mti_term_subgroup mts
                          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
                          WHERE mts.mti_term_id=? AND COALESCE(mts.delete_flagged,0)=0""",
                       (mti_id,)).fetchone()
        if not sg:
            print(f"  ❌ vr={vr_id} mti={mti_id}  no mti_term_subgroup placement")
            errs += 1
            continue
        if sg['subgroup_code'] != expected_subgroup:
            print(f"  ❌ vr={vr_id} mti={mti_id}  in sub-group {sg['subgroup_code']!r} (expected {expected_subgroup!r})")
            errs += 1
            continue
        print(f"  ✓ vr={vr_id:<7} mti={mti_id:<5} → group_id={target_gid} ({target_code})")
    return errs


total = 0
total += verify_vcg_updates("DIR-002 (M39-A) VCG REFINE", DIR_A_VCG_UPDATES)
total += verify_vc_assigns("DIR-002 (M39-A) VC group_id assigns", DIR_A_VC_ASSIGNS, 'M39-A')
total += verify_vcg_updates("DIR-003 (M39-B) VCG REFINE", DIR_B_VCG_UPDATES)
total += verify_vc_assigns("DIR-003 (M39-B) VC group_id assigns", DIR_B_VC_ASSIGNS, 'M39-B')

print(f"\n{'=' * 60}")
print(f"Total errors: {total}")

# Also: count remaining P-status (group_id IS NULL, is_relevant=1) for M39-A and M39-B before
print("\n=== Pre-state: P-status (is_relevant=1 AND group_id IS NULL) per sub-group ===")
for sg in ('M39-A', 'M39-B', 'M39-BOUNDARY'):
    n = c.execute("""
        SELECT COUNT(*) c
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id AND COALESCE(mts.delete_flagged,0)=0
        JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
        WHERE cs.cluster_code='M39' AND cs.group_code=?
          AND vc.is_relevant=1 AND vc.group_id IS NULL
    """, (sg,)).fetchone()['c']
    print(f"  {sg}: {n} P-status verses")
