"""M09 Phases 8 + 8.5 + 8.7 — batched application.

Phase 8: dissolve 23 inherited VCGs (legacy registry-id codes)
Phase 8.5: set-aside 12 verses (11 diatassō + 1 tapeinoō Luk 3:5) with evidence-grounded reasons;
           soft-delete M09-D-VCG-05 (the dedicated PHASE_8_5_FLAG VCG, now empty);
           record cluster_observation noting M23 future-pickup candidacy for diatassō
Phase 8.7: load 6 characteristics + 8 characteristic_subgroup links + cluster_observations

Per v2_8 §11, §11A, §11B.
"""
import sys, io, sqlite3
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
CLUSTER = 'M09'

# Phase 8.5 set-aside vc_ids
DIATASSO_VC_REASON = ('non-M09 content — G1299 diatassō verse evidences practical command-giving / '
                      'narrative direction with no inner-disposition register; Pass A explicitly noted '
                      '"does not evidence inner-being content for this term." M23 (authority/directive) '
                      'is the primary register; future pickup candidate when M23 opens.')
LUK35_VC_REASON = ('non-M09 content — G5013 tapeinoō at Luk 3:5 evidences physical-prophetic landscape '
                   'imagery (Isaiah\'s mountains-made-low); no inner-being content for this term. '
                   'Single outlier in tapeinoō\'s otherwise-clean humility corpus.')

# Phase 8.7 characteristic definitions
CHARACTERISTICS = [
    (1, 'Humility', 'The inner disposition of voluntary self-lowering before God and others. The settled posture of the heart that does not assert standing, claim merit, or insist on its own way. Volume-split into M09-A (willed self-lowering — voluntary/dispositional) and M09-B (experienced/imposed lowliness — state). Vocabulary: tapeinos / tapeinōsis / tapeinofrosunē / tapeinoō family; ka.na voluntary-humbling verses; tsa.na / tsa.nu.a (walking humbly with God).'),
    (2, 'Submission', 'The inner disposition of willing yielding to legitimate authority — heart-located submission of will, not merely external compliance. Cross-register flag: M30 (Obedience). Volume-split into M09-C (heart/conscience-located inner disposition) and M09-D (lived relational pattern of obedience-in-context). Vocabulary: hupakoē / hupakouō / hupotagē / yiq.qe.hah; plus Luk 17:10 (single diatassō verse evidencing self-assessing servant posture).'),
    (3, 'Contrition', 'The acute form of humility produced by genuine confrontation with one\'s failure or with the holiness of God — crushed/broken spirit. Located in spirit and heart. dak.ka pairs structurally with lowliness — the inner posture that opens the person to divine encounter (Psa 34:18; Isa 57:15).'),
    (4, 'Meekness and gentleness', 'The inner quality of calibrated restraint and gentleness — controlled strength, capacity to hold force in measured response. metriopatheō (Heb 5:2 — gentleness grounded in shared creaturely weakness); okneō (Act 9:38 — absence of resistant hesitation, immediate volitional responsiveness).'),
    (5, 'Dignity', 'Grounded moral gravity and seriousness of character — inner-grounded worth that does NOT require self-promotion or status-seeking. Cross-register flag: M08 (structural opposite of proud self-display). semnotēs — the inner quality of peaceable godly life (1Ti 2:2), orderly household character (1Ti 3:4), gravitas authenticating teaching (Tit 2:7).'),
    (6, 'Willing-heartedness', 'The freely-moved willing disposition of the heart/spirit. Cross-register flags: M04 (joy/delight — spontaneous-generosity dimension); M29 (desire/will — volitional dimension). na.div — willing-hearted contributions (Exo 35:5, 35:22), willing-hearted skilled craftsmen (1Ch 28:21), willing-hearted offerings (2Ch 29:31), willing spirit upheld with the joy of salvation (Psa 51:12).'),
]

LINKS = [
    (1, 'M09-A', 'Voluntary/dispositional partition of CHAR-1 (willed self-lowering — heart-disposition vocabulary).', 0, None),
    (1, 'M09-B', 'Condition/state/imposed partition of CHAR-1 (lowliness as experienced state — social, suffering, creaturely, divine-imposed).', 0, None),
    (2, 'M09-C', 'Heart/conscience-located partition of CHAR-2 (inner disposition of will yielding to authority). Cross-register flag M30.', 0, None),
    (2, 'M09-D', 'Lived expression/relational partition of CHAR-2 (relational pattern of obedience-in-context). Cross-register flag M30. (Post-Phase-8.5: 11 diatassō verses set-aside; M09-D-VCG-05 soft-deleted.)', 0, None),
    (3, 'M09-E', 'Single-sub-group representation.', 0, None),
    (4, 'M09-F', 'Single-sub-group representation. Multi-faceted note: Mat 11:29 tapeinos (Christ "gentle and lowly in heart") is primary-placed in M09-A but contributes secondary to M09-F gentleness dimension.', 0, None),
    (5, 'M09-G', 'Single-sub-group representation. Cross-register flag M08 (structural opposite of proud self-display).', 0, None),
    (6, 'M09-H', 'Single-sub-group representation. Cross-register flags M04 (joy/delight) + M29 (desire/will).', 0, None),
]

OBSERVATIONS = [
    (1, 'M09-A', 'INTEGRATION_NOTE', 'phase_9_findings',
     'CHAR-1 volume-split across M09-A / M09-B',
     'CHAR-1 (Humility) was volume-split per v2_8 §8.6: M09-A (37V willed/voluntary self-lowering) + M09-B (13V state/imposed lowliness). The characteristic identity persists across the split; Phase 9 evaluates CHAR-1 as a single inner-being faculty manifesting in two registers (the voluntary disposition vs the experienced state). The split-axis is voluntary-vs-imposed.'),
    (2, 'M09-C', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M09 submission ↔ M30 (Obedience) register-adjacency',
     'CHAR-2 (Submission) is register-adjacent with the future M30 (Obedience/Disobedience) cluster. M09-C/D hupakoē/hupakouō/hupotagē/yiq.qe.hah carry the submission-of-will register; M30 will carry the broader obedience-as-action register. When M30 opens, M09-C/D evidence will inform M30\'s T6 relational findings. Cross-register flag carried forward.'),
    (5, 'M09-G', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M09 dignity ↔ M08 pride as structural opposites',
     'CHAR-5 (Dignity, semnotēs) functions as the structural opposite of M08 (Pride) — grounded moral gravity vs proud self-display. The 3 semnotēs verses (1Ti 2:2, 1Ti 3:4, Tit 2:7) name the inner-grounded worth that does not require self-promotion. Phase 9 T6 should articulate the M09-G ↔ M08 polarity.'),
    (6, 'M09-H', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M09 willing-heartedness ↔ M04 joy + M29 desire/will',
     'CHAR-6 (Willing-heartedness, na.div) overlaps with M04 (joy/delight — spontaneous generosity dimension) and M29 (desire/will — volitional readiness dimension). Psa 51:12 in particular pairs willing spirit with joy of salvation. When M04 / M29 open, the na.div corpus will inform their cross-cluster T6 findings.'),
    (None, None, 'CROSS_CLUSTER_HANDOFF', 'session_d',
     'M23 pickup note: G1299 diatassō (11 verses set-aside at Phase 8.5)',
     'At Phase 8.5 (2026-05-22), 11 G1299 diatassō verses (Mat 11:1, Luk 3:13, Luk 17:9, Act 7:44, Act 18:2, 1Cor 7:17, 1Cor 9:14, 1Cor 11:34, 1Cor 16:1, Gal 3:19, Tit 1:5) were set_aside from M09 because the verses evidence practical command-giving / narrative direction — no M09 inner-disposition content. Pass A meanings explicitly note "does not evidence inner-being content for this term." The term\'s primary register is M23 (authority/directive). One diatassō verse (Luk 17:10) carried M09-relational content and was kept in M09-C. WHEN M23 OPENS: the 11 set-aside verses are candidates for adoption as M23 evidence (the term mti_id stays in M09 because Luk 17:10 evidences M09; M23 picks up the verses via cross-cluster co-reference).'),
    (None, None, 'INTEGRATION_NOTE', 'phase_9_findings',
     'Phase 8.5 set-aside: 12 non-M09-content verses',
     'At Phase 8.5 (2026-05-22), 12 verses were set-aside from M09 substantive corpus: 11 G1299 diatassō verses (see CROSS_CLUSTER_HANDOFF for M23 future-pickup) + 1 G5013 tapeinoō Luk 3:5 ("mountains made low" Isaiah landscape imagery — no inner-being content). M09-D-VCG-05 (the dedicated PHASE_8_5_FLAG VCG holding the 11 diatassō verses) was soft-deleted post-set-aside. Substantive corpus: 109 → 97 is_relevant verses; M09-D 30 → 19 verses.'),
]

# Diatassō verses (vc_ids) — fetch from DB
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

diatasso_vcs = [r[0] for r in cur.execute("""
    SELECT vc.id FROM verse_context vc
    JOIN verse_context_group vcg ON vcg.id=vc.group_id
    WHERE vcg.group_code='M09-D-VCG-05' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchall()]
print(f'PHASE_8_5_FLAG diatassō vc_ids (M09-D-VCG-05): {len(diatasso_vcs)}')
assert len(diatasso_vcs) == 11

luk35_vc = cur.execute("""
    SELECT vc.id FROM verse_context vc
    JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
    JOIN mti_terms mt ON mt.id=vc.mti_term_id
    WHERE mt.cluster_code='M09' AND mt.strongs_number='G5013' AND vr.reference='Luk 3:5'
      AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
print(f'Luk 3:5 tapeinoō vc_id: {luk35_vc}')

m09_d_vcg05_id = cur.execute("SELECT id FROM verse_context_group WHERE group_code='M09-D-VCG-05' AND COALESCE(delete_flagged,0)=0").fetchone()[0]

# Resolve sub-group ids for Phase 8.7
sg_id = {r['subgroup_code']: r['id'] for r in cur.execute(
    "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
    (CLUSTER,)
).fetchall()}

# Source attribution
SOURCE = ('wa-cluster-M09-constitution-debate-v1-20260521.md + wa-cluster-M09-subgroup-design-v1-20260521.md + '
          'wa-cluster-M09-dir-002-phase6-subgroup-assign-v1-20260521.md (Phase 5/6 design); '
          'wa-cluster-M09-vcg-creation-v1-20260522.json (Phase 7 VCG design)')

print()
print('=== APPLYING (Phase 8 + 8.5 + 8.7) ===')
cur.execute('BEGIN')
try:
    # ============================================================
    # Phase 8: Dissolve 23 inherited VCGs
    # ============================================================
    inherited_ids = [r[0] for r in cur.execute("""
        SELECT DISTINCT vcg.id FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vt.delete_flagged,0)=0
          AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(vcg.delete_flagged,0)=0
          AND NOT (vcg.group_code LIKE 'M09-%-VCG-%')
    """, (CLUSTER,)).fetchall()]
    assert len(inherited_ids) == 23, f'Expected 23 inherited VCGs, got {len(inherited_ids)}'

    n_active_orphans = cur.execute(
        f"""SELECT COUNT(*) FROM verse_context WHERE group_id IN ({','.join('?'*len(inherited_ids))})
            AND is_relevant=1 AND COALESCE(delete_flagged,0)=0""",
        inherited_ids,
    ).fetchone()[0]
    assert n_active_orphans == 0, f'{n_active_orphans} is_relevant verses still on inherited VCGs'

    cur.execute(
        f"""UPDATE verse_context_group SET delete_flagged=1,
            notes='Dissolved at M09 Phase 8 ' || ? || ' (replaced by M09-*-VCG-NN; per dir-004)'
            WHERE id IN ({','.join('?'*len(inherited_ids))}) AND COALESCE(delete_flagged,0)=0""",
        [NOW] + inherited_ids,
    )
    assert cur.rowcount == 23
    print(f'  Phase 8 Op A: 23 inherited VCGs soft-deleted')

    cur.execute(
        f"""UPDATE vcg_term SET delete_flagged=1, last_updated_date=?
            WHERE vcg_id IN ({','.join('?'*len(inherited_ids))}) AND COALESCE(delete_flagged,0)=0""",
        [NOW] + inherited_ids,
    )
    n_vt_dis = cur.rowcount
    print(f'  Phase 8 Op B: {n_vt_dis} vcg_term links soft-deleted')

    # ============================================================
    # Phase 8.5: set-aside 12 verses + soft-delete M09-D-VCG-05
    # ============================================================
    # Diatassō verses (11) → is_relevant=0 + set_aside_reason
    qm = ','.join('?'*len(diatasso_vcs))
    cur.execute(
        f"UPDATE verse_context SET is_relevant=0, set_aside_reason=? WHERE id IN ({qm}) AND is_relevant=1",
        (DIATASSO_VC_REASON, *diatasso_vcs),
    )
    assert cur.rowcount == 11
    print(f'  Phase 8.5: 11 diatassō verses set_aside')

    # Luk 3:5 tapeinoō → is_relevant=0 + set_aside_reason
    cur.execute(
        "UPDATE verse_context SET is_relevant=0, set_aside_reason=? WHERE id=? AND is_relevant=1",
        (LUK35_VC_REASON, luk35_vc),
    )
    assert cur.rowcount == 1
    print(f'  Phase 8.5: Luk 3:5 tapeinoō set_aside')

    # Soft-delete M09-D-VCG-05 (now empty after diatassō set-aside)
    cur.execute(
        "UPDATE verse_context_group SET delete_flagged=1, notes=? WHERE id=? AND COALESCE(delete_flagged,0)=0",
        (f'Dissolved at M09 Phase 8.5 {NOW} (PHASE_8_5_FLAG verses set_aside; VCG empty)', m09_d_vcg05_id),
    )
    assert cur.rowcount == 1
    cur.execute(
        "UPDATE vcg_term SET delete_flagged=1, last_updated_date=? WHERE vcg_id=? AND COALESCE(delete_flagged,0)=0",
        (NOW, m09_d_vcg05_id),
    )
    print(f'  Phase 8.5: M09-D-VCG-05 soft-deleted (now empty)')

    # ============================================================
    # Phase 8.7: load 6 characteristics + 8 links + observations
    # ============================================================
    char_id_by_seq = {}
    for seq, name, definition in CHARACTERISTICS:
        cur.execute(
            "INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, 'v1', ?, ?)",
            (CLUSTER, seq, name, definition, SOURCE, NOW, NOW),
        )
        char_id_by_seq[seq] = cur.lastrowid
    print(f'  Phase 8.7 Op A: {len(CHARACTERISTICS)} characteristic rows')

    for seq, sg_code, qualifier, is_partial, partial_note in LINKS:
        cur.execute(
            "INSERT INTO characteristic_subgroup (characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, partial_register_note, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (char_id_by_seq[seq], sg_id[sg_code], qualifier, is_partial, partial_note, NOW, NOW),
        )
    print(f'  Phase 8.7 Op B: {len(LINKS)} characteristic_subgroup links')

    for seq, sg_code, obs_type, target_phase, title, description in OBSERVATIONS:
        char_id = char_id_by_seq[seq] if seq else None
        sg_id_val = sg_id[sg_code] if sg_code else None
        cur.execute(
            "INSERT INTO cluster_observation (cluster_code, characteristic_id, cluster_subgroup_id, source_phase, observation_type, target_phase, title, description, status, raised_date, source_file, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'open', ?, ?, ?, ?)",
            (CLUSTER, char_id, sg_id_val, 'phase_8_7', obs_type, target_phase, title, description, NOW, SOURCE, NOW, NOW),
        )
    print(f'  Phase 8.7 Op C: {len(OBSERVATIONS)} cluster_observation rows')

    conn.commit()
    print(f'Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

# Post-state
print()
print('=== POST-STATE ===')
n_substantive = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
    WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""", (CLUSTER,)).fetchone()[0]
print(f'  M09 substantive verses (post): {n_substantive} (was 109, -12 set_aside = 97)')

n_vcgs = cur.execute("""
    SELECT COUNT(*) FROM verse_context_group WHERE group_code LIKE 'M09-%-VCG-%' AND COALESCE(delete_flagged,0)=0
""").fetchone()[0]
print(f'  Active M09 VCGs (post): {n_vcgs} (was 22, -1 M09-D-VCG-05 = 21)')

n_chars = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)).fetchone()[0]
print(f'  M09 characteristics: {n_chars} (expected 6)')

print()
print('=== M09 PHASES 8 + 8.5 + 8.7 COMPLETE ===')
conn.close()
