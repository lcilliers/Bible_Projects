"""M10 Phases 8 + 8.5 + 8.7 — batched application.

Phase 8 (§11): dissolve 77 inherited VCGs (legacy registry-id codes like '1024-001');
   their vcg_term links are also soft-deleted. All have 0 active verses already
   (Phase 7 routed everything to M10-*-VCG-NN).
Phase 8.5 (§11A): resolve the 6 BOUNDARY-verdict terms:
   - H0205H a.ven (4 active relevant verses) — SET-ASIDE all 4
     (the term's residual corpus is genuinely mixed between moral-trouble,
      grief, and circumstantial-suffering; no coherent M10 register survives)
   - H2256D che.vel (1 verse Mic 2:10) — SET-ASIDE with CROSS_CLUSTER_HANDOFF to M10c
     (uncleanness-as-cause-of-destruction; primary register is the defilement
      sibling cluster, not M10's moral-failure track)
   - H2475 cha.loph, H4889 mash.chit, H4892 mash.chet, H4893B ma.she.chat — 0 relevant
     each (already set_aside at Phase 1); recorded as closed via cluster_observation
   - Pro 12:21 a.ven (Phase 1 borderline, never inserted into DB) — recorded as set-
     aside by parent-term verdict (BOUNDARY); no DB action on the verse
   - Soft-delete M10-BND-VCG-01 (now empty after the 5-verse set-aside)
Phase 8.7 (§11B): load 22 characteristics + 22 characteristic_subgroup links + the
   key cluster_observations for cross-register flags. M10-BND is excluded
   (BOUNDARY isn't a characteristic).

Per v2_8 §11 / §11A / §11B.
"""
import sys, io, sqlite3
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
CLUSTER = 'M10'

# Phase 8.5 set-aside reasons
A_VEN_REASON = (
    'Phase 3 BOUNDARY verdict. The 4 a.ven (H0205H) active verses (Deu 26:14, '
    'Job 5:6, Psa 90:10, Pro 22:8) plus the Phase 1 parked borderline Pro 12:21 '
    'are semantically mixed between moral-trouble-as-iniquity-consequence and '
    'general circumstantial suffering / grief / mortal burden. No coherent M10 '
    '(sin-as-act/state) register survives. Set aside from M10. The term mti_id '
    'stays in M10 with no relevant verses. If M03 (grief) or M20 (distress) '
    "later opens these verses, they may be picked up via cross-cluster co-reference."
)
CHE_VEL_REASON = (
    'Phase 3 BOUNDARY verdict. The single che.vel (H2256D) verse Mic 2:10 names '
    'uncleanness-as-cause-of-destruction. Primary register is M10c (Defilement/'
    'Impurity), the sibling cluster carved out at the 2026-05-22 3-way split. '
    'M10c picks this verse up via cross-cluster co-reference (CROSS_CLUSTER_HANDOFF '
    'observation recorded).'
)

# Phase 8.7 characteristic definitions per sub-group (22 substantive sub-groups; M10-BND excluded)
CHARACTERISTICS = [
    # (subgroup_code, char_seq, short_name, definition)
    ('M10-J', 1, 'Wilful sinning',
     'The will committing a known wrong — sinning as a deliberate relational act directed against '
     'God, another person, or the self, where the person knows what they are doing and does it.'),
    ('M10-K', 2, 'Unintentional sinning',
     'Sin committed without deliberate intent — real and morally consequential even though the '
     'inner person did not consciously defy God\'s command; conscience engages once the act '
     'surfaces to awareness.'),
    ('M10-L', 3, 'Confession',
     'The moment the inner person names a committed sin as sin — first-person confession, corporate '
     'declaration, or the conscience voicing an act already done. Conscience in confessional mode.'),
    ('M10-M', 4, 'Conscience suppression',
     'The inner person who does not recognize, denies, or suppresses awareness of their own '
     'sinful state — conscience absent, self-blinded, or actively claiming innocence where guilt '
     'is real.'),
    ('M10-N', 5, 'Refusal to repent',
     'The will that persistently refuses to turn from a sinful course when departure is available '
     'and known to be required — turning actively withheld.'),
    ('M10-O', 6, 'Habitual defection',
     'Sin as a recurring, established pattern of the will over time — the will\'s settled '
     'direction toward sin, distinct from the specific moment of refusal.'),
    ('M10-P', 7, 'Contagious sin',
     'Sin as a moral direction set by a leader whose inner commitment to wrongdoing is transmitted '
     'to those under their authority — sin propagated through authority relationships.'),
    ('M10-Q', 8, 'Political revolt',
     'Breaking submission to established authority — wilful political defection carrying the '
     'moral weight of sinful transgression. Pa.sha political-revolt register.'),
    ('M10-R', 9, 'Sinful speech',
     'Sin committed through the mouth: blasphemy and slander originating in inner moral '
     'corruption, directed against God or persons. Cross-register flag: M06 (Hate/Contempt).'),
    ('M10-S', 10, 'Specialised sinful mechanisms',
     'Sin operating through a specific inner mechanism — desire exploited by enticement '
     '(deleazō; M14 cross-register), identity falsified through hypocrisy (sunupokrinomai; M08 '
     'cross-register), covenantal identity abandoned through apostasy (apostasia; M31 cross-register).'),
    ('M10-T', 11, 'Sin as universal condition',
     'Sin as a structural condition of the inner person — not primarily an act but a state under '
     'which every person stands. Universal human condition, fall-short-of-glory register.'),
    ('M10-U', 12, 'Sin as enslaving power',
     'Sin as an active force or power that masters the inner person, governing the will so it '
     'cannot freely choose otherwise. The will captive under sin\'s dominion.'),
    ('M10-V', 13, 'Sin as divine record',
     'Sin as an objective moral weight existing before God — recorded, accumulated, named, not '
     'hidden from divine memory even if hidden from others. The person carries this record '
     'whether they feel it or not.'),
    ('M10-W', 14, 'Forgiveness sought and received',
     'The inner movement toward God in search of forgiveness — the will that turns and asks for '
     'sin\'s removal; and the divine response of granting, withholding, or declaring forgiveness. '
     'Cross-register flag: M11 (Repentance, Forgiveness, Restoration).'),
    ('M10-X', 15, 'Generational sin',
     'Sin as a moral condition that enters through lineage — inherited from ancestors, transmitted '
     'through family or national belonging. The inner person carries a guilt or moral liability '
     'not only for their own acts but for the accumulated sinful history of those before them.'),
    # Pre-revision unchanged sub-groups (designed at original Phase 5)
    ('M10-C', 16, 'The sinner as moral character',
     'The constitutive inner moral identity of the person defined by sin — not the act or the '
     'condition but what kind of person they are at their moral core. Hamartōlos and chat.ta '
     'register: sinner as recognisable moral category.'),
    ('M10-D', 17, 'Guilt as inner-being state',
     'The conscience\'s recognition of moral liability before God — the subjective inner '
     'experience of being guilty, of bearing a wrong that cannot be hidden. Conscience in its '
     'guilt-awareness mode. Cross-register flag (pu.qah): M03 (Grief).'),
    ('M10-E', 18, 'Iniquity as accumulated moral crime',
     'The inner dimension of accumulated moral wrongdoing — crime in its moral-spiritual sense, '
     'iniquity as measured, generational, heart-seated accumulation. A.von H5771G crime sub-entry.'),
    ('M10-F', 19, 'Transgression as deliberate boundary-crossing',
     'The wilful defiance of known moral or covenantal order — the will that knowingly crosses a '
     'boundary or breaches a covenant. Pe.sha / pa.sha / parabasis-family register.'),
    ('M10-G', 20, 'Faithlessness as covenant-breaking sin',
     'The inner disposition of deliberate unfaithfulness — the will that breaks covenantal loyalty, '
     'betrays a trust, acts treacherously against God or persons. Cross-register flag: M13 '
     '(Truth/Faithfulness) + M31 (Faith/Unbelief).'),
    ('M10-H', 21, 'Perversion as inner inversion',
     'The inner state or disposition of moral distortion — twisting what is right, corrupting '
     'what was good, inverting the moral order from within. Sexual-perversion and moral-'
     'corruption registers. Cross-register flags (specific terms): M03, M07, M23/M35.'),
    ('M10-I', 22, 'Injustice as moral failure of right conduct',
     'The inner state/disposition of doing wrong toward persons — unjust conduct, unjust '
     'character, the moral faculty bent toward wrongdoing against others. Cross-register flag: '
     'M26 (Righteousness/Justice).'),
]

# Cross-register observations (one per cross-register flag — for downstream T6)
CROSS_REGISTER_OBS = [
    # (char_seq, sg_code, obs_type, target_phase, title, description)
    (9, 'M10-R', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M10 sinful-speech ↔ M06 contempt cross-register',
     'CHAR-9 (Sinful speech, blasfēmia/blasfēmos) is register-adjacent with M06 (Hate, Contempt '
     'and Hostility). Slander/blasphemy originates in inner moral corruption (Mat 15:19 — "from '
     'the heart"; Mar 7:22) but also expresses contempt and hostility (Rev 13:5/6; Col 3:8). '
     'When M06 opens or is re-examined, these verses inform its T6 cross-cluster findings.'),
    (10, 'M10-S', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M10 specialised-mechanisms ↔ M14 / M08 / M31',
     'CHAR-10 covers three small-corpus mechanisms with distinct cross-registers: deleazō '
     '(enticement → M14 Deceit), sunupokrinomai (hypocrisy → M08 Pride/performed self-elevation), '
     'apostasia (apostasy → M31 Faith/Unbelief covenantal defection). Downstream T6 findings '
     'should articulate each cross-register polarity.'),
    (14, 'M10-W', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M10 forgiveness-sought ↔ M11 Repentance/Forgiveness/Restoration',
     'CHAR-14 (Forgiveness sought and received) carries 34 verses with kip.pu.rim (8V) and '
     'chat.tat sin-offering (4V). These terms\' primary register is M11 (Repentance, Forgiveness '
     'and Restoration) — atonement as the remedy of sin. M10 owns these verses as sin-response; '
     'M11 will own them as forgiveness-mechanism when the cluster opens.'),
    (17, 'M10-D', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M10 guilt ↔ M03 grief (pu.qah)',
     'Pu.qah (H6330, 1V — 1Sa 25:31) names a staggering of conscience that touches both M10 '
     '(guilt-as-inner-state) and M03 (grief). The verse stays in M10 as the conscience-faculty '
     'in pre-emptive guilt; M03 may pick it up via cross-cluster co-reference for the '
     'grief-of-conscience register.'),
    (20, 'M10-G', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M10 faithlessness ↔ M13 truth/faithfulness + M31 faith/unbelief',
     'CHAR-20 (Faithlessness as covenant-breaking sin) — all 3 terms (ba.gad, ma.al verb, ma.al '
     'noun = 101V) carry the M13/M31 cross-register. Faithlessness is the negative of '
     'covenant-faithfulness (M13) and of faith (M31). Phase 9 T6 should articulate the polarity.'),
    (22, 'M10-I', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M10 injustice ↔ M26 righteousness/justice',
     'CHAR-22 (Injustice as moral failure of right conduct) — all 4 main injustice terms '
     '(a.vel, av.lah, adikos, av.val) carry M26 cross-register. Injustice is the structural '
     'opposite of righteousness. Phase 9 T6 should articulate the polarity.'),
    (21, 'M10-H', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M10 perversion: nested cross-registers (M03, M07, M23/M35)',
     'CHAR-21 (Perversion) carries multiple term-specific cross-registers: cha.val (M03 grief — '
     'spirit-breaking destruction), a.vah-twist (M03), nav.lut (M07 shame — lewdness with '
     'exposure register), fthora (M23 strength / M35 testing — bodily-decay register). Phase 9 '
     'T6 should note each.'),
]

# Phase 8.5 closure observations (one per BOUNDARY term)
BOUNDARY_CLOSURE_OBS = [
    (None, 'M10-BND', 'INTEGRATION_NOTE', 'phase_9_findings',
     'Phase 8.5 closure — H0205H a.ven (4 verses + 1 parked borderline) SET-ASIDE',
     'At Phase 8.5 (2026-05-23), the 4 active relevant a.ven (H0205H) verses (Deu 26:14, Job 5:6, '
     'Psa 90:10, Pro 22:8) and the Phase 1 parked borderline Pro 12:21 were set aside from M10. '
     'The residual corpus is semantically mixed between moral-trouble-as-iniquity-consequence and '
     'general circumstantial suffering / grief / mortal burden. No coherent M10 (sin-as-act/state) '
     'register survives. The term mti_id stays in M10 with no relevant verses. If M03 (grief) or '
     'M20 (distress) later opens, candidates for cross-cluster co-reference.'),
    (None, 'M10-BND', 'CROSS_CLUSTER_HANDOFF', 'session_d',
     'M10c pickup note: H2256D che.vel Mic 2:10 (Phase 8.5 set-aside)',
     'At Phase 8.5 (2026-05-23), the single che.vel (H2256D) verse Mic 2:10 was set aside from '
     'M10 because the verse evidences uncleanness-as-cause-of-destruction — primary register is '
     'M10c (Defilement/Impurity), the sibling cluster carved out at the 2026-05-22 3-way split. '
     'When M10c is processed, Mic 2:10 is a candidate for inclusion as evidence of the '
     'defilement→destruction pattern.'),
    (None, 'M10-BND', 'INTEGRATION_NOTE', 'phase_9_findings',
     'Phase 8.5 closure — 4 empty-corpus BOUNDARY terms',
     'At Phase 8.5 (2026-05-23), the 4 empty-corpus BOUNDARY-verdict terms (H2475 cha.loph, '
     'H4889 mash.chit, H4892 mash.chet, H4893B ma.she.chat) were confirmed as closed: each has '
     '0 active relevant verses (all set aside at Phase 1 as physical-destruction senses with no '
     'inner-being moral-failure content). The mti_term rows stay in M10 as member terms; the '
     'sub-group M10-BND-VCG-01 is soft-deleted as empty after the a.ven and che.vel verses are '
     'set aside.'),
]


def main() -> int:
    dry = '--dry-run' in sys.argv

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # ============================================================
    # Pre-fetch state
    # ============================================================
    # Inherited VCGs
    inherited_ids = [r[0] for r in cur.execute("""
        SELECT DISTINCT vcg.id FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vt.delete_flagged,0)=0
          AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(vcg.delete_flagged,0)=0
          AND NOT (vcg.group_code LIKE 'M10-%-VCG-%')
    """, (CLUSTER,)).fetchall()]
    print(f"Inherited VCGs to dissolve: {len(inherited_ids)}")

    # Sub-group ids
    sg_id = {r['subgroup_code']: r['id'] for r in cur.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchall()}
    assert len(sg_id) == 23, f"Expected 23 active M10 sub-groups, got {len(sg_id)}"
    print(f"Active sub-groups: {len(sg_id)}")

    # M10-BND active vcg
    bnd_row = cur.execute(
        "SELECT id, group_code FROM verse_context_group "
        "WHERE group_code='M10-BND-VCG-01' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()
    assert bnd_row, 'M10-BND-VCG-01 not found'
    bnd_vcg_id = bnd_row['id']
    print(f"M10-BND-VCG-01 id: {bnd_vcg_id}")

    # BND verses to set-aside (4 a.ven + 1 che.vel)
    bnd_verses = list(cur.execute("""
        SELECT vc.id, vr.reference, mt.strongs_number, mt.transliteration
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        WHERE vc.group_id=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY mt.strongs_number, vr.book_id, vr.chapter, vr.verse_num
    """, (bnd_vcg_id,)).fetchall())
    print(f"M10-BND verses to set-aside: {len(bnd_verses)}")
    for r in bnd_verses:
        print(f"  vc_id={r['id']} {r['reference']} {r['strongs_number']} {r['transliteration']}")
    assert len(bnd_verses) == 5, f"Expected 5 BND verses, got {len(bnd_verses)}"

    a_ven_vc_ids = [r['id'] for r in bnd_verses if r['strongs_number'] == 'H0205H']
    che_vel_vc_ids = [r['id'] for r in bnd_verses if r['strongs_number'] == 'H2256D']
    assert len(a_ven_vc_ids) == 4 and len(che_vel_vc_ids) == 1

    if dry:
        print('\n[DRY-RUN — no writes]')
        conn.close()
        return 0

    # ============================================================
    # APPLY
    # ============================================================
    print()
    print('=== APPLYING (Phase 8 + 8.5 + 8.7) ===')
    cur.execute('BEGIN')
    try:
        # --- Phase 8: dissolve inherited VCGs ---
        if inherited_ids:
            qm = ','.join('?'*len(inherited_ids))
            cur.execute(
                f"""UPDATE verse_context_group SET delete_flagged=1,
                    notes='Dissolved at M10 Phase 8 ' || ? || ' (replaced by M10-*-VCG-NN structure; per dir-004)'
                    WHERE id IN ({qm}) AND COALESCE(delete_flagged,0)=0""",
                [NOW] + inherited_ids,
            )
            n_vcg = cur.rowcount
            cur.execute(
                f"""UPDATE vcg_term SET delete_flagged=1, last_updated_date=?
                    WHERE vcg_id IN ({qm}) AND COALESCE(delete_flagged,0)=0""",
                [NOW] + inherited_ids,
            )
            n_vt = cur.rowcount
            print(f"  Phase 8: dissolved {n_vcg} inherited VCGs + {n_vt} vcg_term links")
        else:
            print("  Phase 8: no inherited VCGs to dissolve")

        # --- Phase 8.5: set-aside BOUNDARY verses + soft-delete empty VCG ---
        # 4 a.ven verses
        qm = ','.join('?'*len(a_ven_vc_ids))
        cur.execute(
            f"UPDATE verse_context SET is_relevant=0, set_aside_reason=? "
            f"WHERE id IN ({qm}) AND is_relevant=1",
            (A_VEN_REASON, *a_ven_vc_ids),
        )
        assert cur.rowcount == 4
        print(f"  Phase 8.5: 4 a.ven (H0205H) verses set_aside")

        # 1 che.vel verse
        cur.execute(
            "UPDATE verse_context SET is_relevant=0, set_aside_reason=? WHERE id=? AND is_relevant=1",
            (CHE_VEL_REASON, che_vel_vc_ids[0]),
        )
        assert cur.rowcount == 1
        print(f"  Phase 8.5: 1 che.vel (H2256D) verse set_aside (Mic 2:10)")

        # Soft-delete M10-BND-VCG-01 (now empty)
        cur.execute(
            "UPDATE verse_context_group SET delete_flagged=1, notes=? "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (f'Dissolved at M10 Phase 8.5 {NOW} (BOUNDARY verses set_aside; VCG empty)', bnd_vcg_id),
        )
        cur.execute(
            "UPDATE vcg_term SET delete_flagged=1, last_updated_date=? "
            "WHERE vcg_id=? AND COALESCE(delete_flagged,0)=0",
            (NOW, bnd_vcg_id),
        )
        print(f"  Phase 8.5: M10-BND-VCG-01 soft-deleted (empty)")

        # --- Phase 8.5: 3 closure observations ---
        for char_seq, sg_code, obs_type, target_phase, title, description in BOUNDARY_CLOSURE_OBS:
            sg_val = sg_id.get(sg_code) if sg_code else None
            cur.execute(
                "INSERT INTO cluster_observation "
                "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
                "observation_type, target_phase, title, description, status, raised_date, "
                "source_file, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'open', ?, ?, ?, ?)",
                (CLUSTER, None, sg_val, 'phase_8_5', obs_type, target_phase,
                 title, description, NOW, 'phase_8_5_closure', NOW, NOW),
            )
        print(f"  Phase 8.5: {len(BOUNDARY_CLOSURE_OBS)} cluster_observation rows recorded")

        # --- Phase 8.7: 22 characteristic rows + 22 links + cross-register obs ---
        char_id_by_seq = {}
        for sg_code, seq, name, definition in CHARACTERISTICS:
            cur.execute(
                "INSERT INTO characteristic "
                "(cluster_code, char_seq, short_name, definition, source, version, "
                "created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'v1', ?, ?)",
                (CLUSTER, seq, name, definition,
                 'wa-cluster-M10-subgroup-design-v1-20260523.md + '
                 'wa-cluster-M10-subgroup-design-revision-v1-20260523.md',
                 NOW, NOW),
            )
            char_id_by_seq[seq] = cur.lastrowid
        print(f"  Phase 8.7: {len(CHARACTERISTICS)} characteristic rows")

        # 22 characteristic_subgroup links (1:1)
        for sg_code, seq, _, _ in CHARACTERISTICS:
            cur.execute(
                "INSERT INTO characteristic_subgroup "
                "(characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, "
                "partial_register_note, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, NULL, ?, ?)",
                (char_id_by_seq[seq], sg_id[sg_code],
                 f'Single-sub-group representation (sub-group = characteristic 1:1).',
                 NOW, NOW),
            )
        print(f"  Phase 8.7: {len(CHARACTERISTICS)} characteristic_subgroup links")

        # Cross-register observations
        for char_seq, sg_code, obs_type, target_phase, title, description in CROSS_REGISTER_OBS:
            char_id = char_id_by_seq.get(char_seq) if char_seq else None
            sg_val = sg_id.get(sg_code) if sg_code else None
            cur.execute(
                "INSERT INTO cluster_observation "
                "(cluster_code, characteristic_id, cluster_subgroup_id, source_phase, "
                "observation_type, target_phase, title, description, status, raised_date, "
                "source_file, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'open', ?, ?, ?, ?)",
                (CLUSTER, char_id, sg_val, 'phase_8_7', obs_type, target_phase,
                 title, description, NOW, 'phase_8_7_characteristic_mapping', NOW, NOW),
            )
        print(f"  Phase 8.7: {len(CROSS_REGISTER_OBS)} cross-register cluster_observation rows")

        conn.commit()
        print(f"  Committed at {NOW}")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise

    # ============================================================
    # POST-STATE
    # ============================================================
    print()
    print('=== POST-STATE ===')
    n_substantive = cur.execute("""
        SELECT COUNT(*) FROM verse_context vc JOIN mti_terms mt ON mt.id=vc.mti_term_id
        WHERE mt.cluster_code=? AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
    """, (CLUSTER,)).fetchone()[0]
    print(f"  M10 substantive verses (post): {n_substantive} (was 1325, -5 set_aside = 1320)")

    n_vcgs = cur.execute("""
        SELECT COUNT(*) FROM verse_context_group
        WHERE group_code LIKE 'M10-%-VCG-%' AND COALESCE(delete_flagged,0)=0
    """).fetchone()[0]
    print(f"  Active M10 VCGs (post): {n_vcgs} (was 69, -1 M10-BND-VCG-01 = 68)")

    n_inherited = cur.execute("""
        SELECT COUNT(*) FROM verse_context_group vcg
        JOIN vcg_term vt ON vt.vcg_id = vcg.id
        JOIN mti_terms mt ON mt.id = vt.mti_term_id
        WHERE mt.cluster_code='M10' AND COALESCE(vcg.delete_flagged,0)=0
          AND COALESCE(vt.delete_flagged,0)=0
          AND NOT (vcg.group_code LIKE 'M10-%-VCG-%')
    """).fetchone()[0]
    print(f"  Remaining active inherited VCGs (post): {n_inherited} (expected 0)")

    n_chars = cur.execute(
        "SELECT COUNT(*) FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    print(f"  M10 characteristics: {n_chars} (expected 22)")

    n_links = cur.execute("""
        SELECT COUNT(*) FROM characteristic_subgroup cs
        JOIN characteristic c ON c.id=cs.characteristic_id
        WHERE c.cluster_code='M10' AND COALESCE(cs.delete_flagged,0)=0
    """).fetchone()[0]
    print(f"  M10 characteristic_subgroup links: {n_links} (expected 22)")

    n_obs = cur.execute(
        "SELECT COUNT(*) FROM cluster_observation WHERE cluster_code=? "
        "AND source_phase IN ('phase_8_5','phase_8_7') AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchone()[0]
    print(f"  M10 Phase 8.5/8.7 cluster_observations: {n_obs}")

    print()
    print('=== M10 PHASES 8 + 8.5 + 8.7 COMPLETE ===')
    conn.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
