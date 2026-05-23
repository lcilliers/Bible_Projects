"""M10 Phase 6 — sub-group structural apply + verse routing.

Per v2_8 §9. Per directive wa-cluster-M10-dir-002-phase6-subgroup-assign-v1-20260523.md.

Operations:
- Op A: INSERT 10 cluster_subgroup rows (M10-A..I + M10-BND).
- Op B: INSERT mti_term_subgroup rows (primary + secondary) for every (term, sub-group) pair.
- Op C: UPDATE verse_context.cluster_subgroup_id for every is_relevant vc row per resolved mapping.
- Op D: skipped — cluster.status already advanced to 'Analysis - In Progress' by Phase 4.

Source: Sessions/Session_Clusters/M10/files phase 5/wa-cluster-M10-subgroup-mapping-v1-20260523.json
(term-level mapping with two split_rule entries — pa.sha and paraptōma). The script
resolves split rules to flat vc_id → subgroup_code before applying.

The resolved mapping is also written for audit:
  Sessions/Session_Clusters/M10/files phase 5/wa-cluster-M10-subgroup-mapping-resolved-v1-20260523.json
"""
from __future__ import annotations
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
DIRECTIVE_ID = 'wa-cluster-M10-dir-002-phase6-subgroup-assign-v1-20260523'
MAPPING_DIR = REPO / 'Sessions' / 'Session_Clusters' / 'M10' / 'files phase 5'
MAPPING_PATH = MAPPING_DIR / 'wa-cluster-M10-subgroup-mapping-v1-20260523.json'
RESOLVED_PATH = MAPPING_DIR / 'wa-cluster-M10-subgroup-mapping-resolved-v1-20260523.json'

# Sub-group definitions: (code, label, core_description)
SUBGROUPS = [
    ('M10-A', 'Sin as committed act',
     'CHAR-1 (Sin as committed act). The will in the moment of moral failure: sinning as a relational act '
     'directed against God, another person, or oneself. Inner-being content is volitional — the conscience '
     'recognising a committed fault, the will that defected or chose wrongly, the act now requiring '
     'acknowledgment and accounting for. The corpus covers sinning as confession (the person who names what '
     'they have done), as deterrence (the inner person who must be restrained), as interpersonal wrong, and '
     'as habitual pattern of the will. Specialised verbal registers include: slander/blasphemy as '
     'sin-of-speech originating in the heart (G0988, G0989), enticement as the mechanism leading inner '
     'desire into sin (G1185), and hypocrisy as the sinful act of false-appearance (G4942). The '
     'characteristic is the active dimension — the moment and act of moral failure.'),
    ('M10-B', 'Sin as moral condition / state',
     'CHAR-2 (Sin as moral condition). Sin as an objective moral reality the inner person carries — not '
     'primarily the act, but the condition of being under sin\'s dominion, burdened by it, enslaved, needing '
     'it removed or covered. Inner-being content is the person\'s moral ontology — what they are under sin '
     'rather than what they did. Covers sin as accumulated moral weight recorded against the person, as '
     'enslaving force mastering the will (Joh 8:34), as universal human condition (Rom 5:12/19), as '
     'death-state from which God must raise (Eph 2:1/5), and as reality requiring atonement before standing '
     'before God. Atonement/sin-offering terms (kip.pu.rim, chat.tat sin-offering — M11 cross-register) sit '
     'here because they evidence sin-as-condition requiring covering. Wickedness-as-inner-condition '
     '(rish.ah) belongs here as the state-dimension of sinful moral character.'),
    ('M10-C', 'The sinner as moral character',
     'CHAR-3 (Sinner as moral character). The constitutive inner moral identity of the person defined by '
     'sin — not what they did or the condition they are in, but what kind of person they are at their moral '
     'core. The sinner as recognisable moral category (Mat 9:10/11), as person owning their sinful identity '
     '(Luk 5:8), as those constituted sinners (Rom 5:8/19), and as habitual extreme sinners whose moral '
     'character is total (Gen 13:13 — Sodom; 1Sa 15:18 — the Amalekites; Amo 9:8 — the sinful kingdom).'),
    ('M10-D', 'Guilt as inner-being state',
     'CHAR-4 (Guilt as inner-being state). The conscience\'s recognition of moral liability before God — '
     'the subjective inner experience of being guilty, of having wronged God or another, of carrying a '
     'weight that cannot be hidden. Inner-being content is the conscience in its guilt-awareness mode: '
     'realisation (Lev 5:2/3/4/5 — guilt arising when a hidden violation becomes known), weight of '
     'acknowledged guilt (Psa 38:4/18; Ezr 9:6 — guilt risen above the head), indelibility before God (Jer '
     '2:22 — no soap removes it), and the grace of guilt\'s removal (Isa 6:7). The a.von punishment '
     'sub-entry belongs here for its punitive-burden-as-inner-experience meanings (Gen 4:13 Cain; Eze 4:4–6 '
     'symbolically borne). The staggering-of-conscience term (pu.qah; M03 cross-register) belongs here as a '
     'single-verse expression of guilt-awareness.'),
    ('M10-E', 'Iniquity as accumulated moral crime',
     'CHAR-5 (Iniquity as accumulated crime). The inner dimension of accumulated moral wrongdoing — crime '
     'in its moral-spiritual sense, the store of inner wrongdoing existing before God as a measured, '
     'generational, heart-seated reality. Distinct from guilt (which is the subjective recognition); '
     'iniquity-as-crime is the objective moral accumulation — what is known by God even when hidden from '
     'others (Psa 90:8), what has built up over generations (Exo 20:5), what is seated in the heart (Eze '
     '14:3/4/7), and what must be confessed before restoration (Lev 26:40/41). The inner-being dimension is '
     'the person\'s moral account before God: the crime-weight carried whether felt or not.'),
    ('M10-F', 'Transgression / rebellion as deliberate boundary-crossing',
     'CHAR-6 (Transgression as boundary-crossing). The wilful defiance of known moral or covenantal order '
     '— the inner act of the will that rebels, crosses a boundary it knows to exist, or deliberately '
     'breaches a covenant or law it is party to. Inner-being content is volitional transgression: the will '
     'that knowingly steps over a line (parabasis — law-violation requiring a law; Rom 4:15), the heart '
     'from which transgression speaks (Psa 36:1), the accumulated rebellions crossing divine tolerance '
     '(Amo 1:3–2:6), Adam\'s paradigmatic conscious violation (Rom 5:14). The salient note is the *knowing* '
     'dimension — not inadvertent sin but wilful boundary-crossing. Revolt (sa.rah) and apostasy '
     '(apostasia) belong here for the rebellion-against-known-authority register.'),
    ('M10-G', 'Faithlessness / treachery as covenant-breaking sin',
     'CHAR-7 (Faithlessness as covenant-breaking sin). The inner disposition of deliberate unfaithfulness '
     '— the will that breaks covenantal loyalty, betrays a trust, or acts treacherously against God or '
     'persons. Distinguishing feature: the *relational* dimension of sinful moral failure — betrayal of a '
     'bond that was known, owed, and wilfully broken. Treachery as a settled inner character (Isa 48:8 — '
     'constitutional unfaithfulness; Isa 24:16 — threefold intensified treachery), unfaithfulness '
     'deepening under pressure rather than breaking (2Ch 28:22 — Ahaz more faithless in distress), and the '
     'call to guard the spirit against faithlessness (Mal 2:15). M13/M31 cross-register flags travel with '
     'all three terms; their M10 representation is the betrayal-as-sin dimension.'),
    ('M10-H', 'Perversion / moral corruption as inner inversion',
     'CHAR-8 (Perversion / corruption). The inner state or disposition of moral distortion — twisting what '
     'is right, corrupting what was good, inverting the moral order from within. Inner-being content '
     'operates at the level of the person\'s moral faculty: perversity originating in the heart and driving '
     'continual evil-devising (Pro 6:14), the mind that becomes depraved (1Ti 6:5 — corruption penetrating '
     'the seat of understanding), the old self corrupted through deceitful desires (Eph 4:22), the person '
     'destroyed from within by what they act on instinctively (Jude 10). Includes: sexual-perversion '
     'terms (te.vel — violation of created/family order), moral-degeneracy terms (sur — the vine turning '
     'wild from within), and lewdness (nav.lut; M07 cross-register). cha.val (M03 cross-register) and a.vah '
     '"to twist" (M03) contribute their moral-distortion verses here.'),
    ('M10-I', 'Injustice as moral failure of right conduct',
     'CHAR-9 (Injustice). The inner state/disposition of doing what is wrong toward persons — unjust '
     'conduct, unjust character, the moral faculty bent toward wrongdoing against others and against right '
     'order. Injustice devised in the heart before enacted by hands (Psa 58:2), as fixed character trait '
     'expressed across all scales (Luk 16:10), as the inner condition the person cannot escape God\'s moral '
     'accounting (Act 24:15; 2Pe 2:9), and as the opposite of righteousness (Deu 32:4; Rom 3:5). M26 '
     'cross-register flags travel with all terms; their M10 representation is the '
     'sinful-conduct-against-right-order dimension.'),
    ('M10-BND', 'Boundary — analytically undecided terms',
     'BOUNDARY. Holds the 6 Phase-3 BOUNDARY-verdict terms (H0205H a.ven, H2256D che.vel, H4889 mash.chit, '
     'H4892 mash.chet, H4893B ma.she.chat, H2475 cha.loph). 5 verses route here (4 from a.ven, 1 from '
     'che.vel); the 4 empty-corpus terms attach as members without verse contributions. Phase 8.5 will '
     'resolve each to SET-ASIDE, ROUTE-TO-CLUSTER, or PROMOTE-TO-SUBGROUP. Pro 12:21 a.ven Phase 1 '
     'borderline is NOT in the corpus (no vc row).'),
]

# Normalise a Bible reference like "Mat 11:1" / "1Cor 7:17" / "Pro  6:14" to canonical "Mat 11:1"
def _norm_ref(ref: str) -> str:
    return ' '.join(ref.split())


def resolve_term_to_vc(conn) -> tuple[dict[int, str], dict[int, int], list[str]]:
    """Read the term-level mapping JSON, resolve split rules to per-vc assignments.

    Returns:
      vc_to_sg: {vc_id: subgroup_code}
      vc_to_mti: {vc_id: mti_term_id}
      warnings: list of strings to surface
    """
    spec = json.loads(MAPPING_PATH.read_text(encoding='utf-8'))
    warnings: list[str] = []

    # Build {(mti_id, ref): vc_id} index for all relevant M10 vc rows
    rows = conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vr.reference
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code='M10'
          AND vc.is_relevant=1
          AND COALESCE(mt.delete_flagged,0)=0
          AND COALESCE(vc.delete_flagged,0)=0
          AND COALESCE(vr.delete_flagged,0)=0
    """).fetchall()
    by_mti_ref: dict[tuple[int, str], int] = {}
    by_mti_vcids: dict[int, list[int]] = defaultdict(list)
    for r in rows:
        ref = _norm_ref(r['reference'])
        by_mti_ref[(r['mti_term_id'], ref)] = r['vc_id']
        by_mti_vcids[r['mti_term_id']].append(r['vc_id'])

    vc_to_sg: dict[int, str] = {}
    vc_to_mti: dict[int, int] = {vc_id: mti for (mti, _), vc_id in by_mti_ref.items()}

    for term in spec['term_assignments']:
        mti = term.get('mti_id')
        strongs = term['strongs']
        primary = term['primary_subgroup']
        split = term.get('split_rule')
        if mti is None:
            warnings.append(f"  {strongs}: mti_id is null — skipped")
            continue
        all_vc_for_term = list(by_mti_vcids.get(mti, []))
        if not all_vc_for_term:
            if term.get('est_verses') in (0, None):
                # Expected (BOUNDARY empty-corpus terms or missing-corpus terms)
                continue
            warnings.append(f"  {strongs} (mti={mti}): no vc rows but est_verses={term.get('est_verses')}")
            continue

        if not split:
            for vc_id in all_vc_for_term:
                vc_to_sg[vc_id] = primary
            continue

        # Split: secondary_verses list of references OR full secondary_verses_rule prose
        secondary_subgroup = split.get('secondary_subgroup')
        secondary_refs_field = split.get('secondary_verses') or []
        rule_prose = split.get('secondary_verses_rule', '')

        # If structured list provided directly:
        if secondary_refs_field:
            secondary_refs = set(_norm_ref(r) for r in secondary_refs_field)
        else:
            # Parse references out of the rule prose: find tokens like "Mat 11:1" or "1Cor 7:17"
            import re
            ref_re = re.compile(r"\b([1-3]?[A-Z][a-z]{1,4})\s*(\d+):(\d+)\b")
            secondary_refs = set()
            for m in ref_re.finditer(rule_prose):
                secondary_refs.add(_norm_ref(f"{m.group(1)} {m.group(2)}:{m.group(3)}"))

        # Apply: vc_ids matching secondary references → secondary_subgroup; rest → primary
        matched = 0
        unmatched_refs = []
        for vc_id in all_vc_for_term:
            # Reverse-lookup the ref for this vc_id
            ref = None
            for (m_id, r), v_id in by_mti_ref.items():
                if v_id == vc_id:
                    ref = r
                    break
            if ref in secondary_refs:
                vc_to_sg[vc_id] = secondary_subgroup
                matched += 1
            else:
                vc_to_sg[vc_id] = primary
        # Sanity: any refs in the secondary list that didn't match any vc?
        actual_term_refs = {ref for (m_id, ref), _ in by_mti_ref.items() if m_id == mti}
        for sr in secondary_refs:
            if sr not in actual_term_refs:
                warnings.append(f"  {strongs}: secondary ref '{sr}' not found in vc corpus")
        print(f"  resolved {strongs} (mti={mti}): primary={primary} (default), "
              f"secondary={secondary_subgroup} matched {matched}/{len(secondary_refs)} refs, "
              f"{len(all_vc_for_term)} total vc rows")
    return vc_to_sg, vc_to_mti, warnings


def write_resolved(vc_to_sg: dict[int, str], vc_to_mti: dict[int, int]) -> None:
    payload = {
        "_resolved_meta": {
            "cluster_code": "M10",
            "phase": 6,
            "date": NOW,
            "source_mapping": MAPPING_PATH.name,
            "vc_count": len(vc_to_sg),
            "note": "Flat vc_id -> subgroup_code mapping resolved from term-level + split rules.",
        },
        "vc_id_to_subgroup": {str(vc_id): sg for vc_id, sg in sorted(vc_to_sg.items())},
        "vc_id_to_mti_term_id": {str(vc_id): mti for vc_id, mti in sorted(vc_to_mti.items())},
    }
    RESOLVED_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\nWrote resolved mapping: {RESOLVED_PATH.relative_to(REPO)}")


def main() -> int:
    dry = '--dry-run' in sys.argv
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print('=== RESOLVE ===')
    vc_to_sg, vc_to_mti_unused, warnings = resolve_term_to_vc(conn)
    print(f"\nTotal vc rows resolved: {len(vc_to_sg)}")

    # Per-subgroup tally
    from collections import Counter
    tallies = Counter(vc_to_sg.values())
    print("Per-subgroup tallies:")
    for code, _, _ in SUBGROUPS:
        print(f"  {code}: {tallies.get(code, 0)}")
    print(f"  TOTAL: {sum(tallies.values())}")

    # Also rebuild vc_to_mti from current DB for write/use:
    rows = cur.execute(f"""
        SELECT id, mti_term_id FROM verse_context
        WHERE id IN ({','.join('?' * len(vc_to_sg))})
    """, list(vc_to_sg.keys())).fetchall()
    vc_to_mti = {r['id']: r['mti_term_id'] for r in rows}

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(w)

    write_resolved(vc_to_sg, vc_to_mti)

    # === PRE-CHECKS ===
    print()
    print('=== PRE-CHECKS ===')
    n_existing_sg = cur.execute(
        "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
    ).fetchone()[0]
    print(f"  Pre-existing M10 sub-groups: {n_existing_sg}")
    assert n_existing_sg == 0, 'M10 sub-groups already exist'

    cluster_status = cur.execute("SELECT status FROM cluster WHERE cluster_code='M10'").fetchone()[0]
    print(f"  cluster.M10.status = {cluster_status!r}")
    assert cluster_status == 'Analysis - In Progress'

    # Confirm count vs DB
    n_total_rel = cur.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code='M10' AND vc.is_relevant=1
          AND COALESCE(mt.delete_flagged,0)=0
          AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]
    print(f"  M10 relevant vc rows in DB: {n_total_rel}")
    print(f"  Resolved vc rows: {len(vc_to_sg)}")
    if n_total_rel != len(vc_to_sg):
        unmapped = n_total_rel - len(vc_to_sg)
        if unmapped > 0:
            # Find which vc rows aren't mapped
            mapped_ids = set(vc_to_sg.keys())
            rows = cur.execute("""
                SELECT vc.id, mt.strongs_number, mt.transliteration, vr.reference
                FROM verse_context vc
                JOIN mti_terms mt ON mt.id = vc.mti_term_id
                JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                WHERE mt.cluster_code='M10' AND vc.is_relevant=1
                  AND COALESCE(mt.delete_flagged,0)=0
                  AND COALESCE(vc.delete_flagged,0)=0
            """).fetchall()
            missing = [r for r in rows if r['id'] not in mapped_ids]
            print(f"  MISSING {len(missing)} vc rows from resolved mapping (first 10):")
            for r in missing[:10]:
                print(f"    vc_id={r['id']} {r['strongs_number']} {r['transliteration']} {r['reference']}")
            raise SystemExit('Resolved mapping incomplete — fix and re-run.')

    if dry:
        print('\n[DRY-RUN — no writes performed.]')
        conn.close()
        return 0

    # === APPLY ===
    print()
    print('=== APPLYING ===')
    cur.execute('BEGIN')
    try:
        # Op A — INSERT cluster_subgroup rows
        sg_id_by_code: dict[str, int] = {}
        for idx, (code, label, descr) in enumerate(SUBGROUPS):
            cur.execute(
                "INSERT INTO cluster_subgroup "
                "(cluster_code, subgroup_code, label, core_description, sort_order, status, "
                "version, source, delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)",
                ('M10', code, label, descr, idx, DIRECTIVE_ID, NOW, NOW),
            )
            sg_id_by_code[code] = cur.lastrowid
        print(f"  Op A: inserted {len(SUBGROUPS)} cluster_subgroup rows")

        # Op B — INSERT mti_term_subgroup rows (primary + optional secondary)
        # First, derive per-term vc counts per subgroup
        term_sg_counts: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        for vc_id, sg in vc_to_sg.items():
            mti = vc_to_mti[vc_id]
            term_sg_counts[mti][sg] += 1
        # Also: BOUNDARY terms with zero verses need member rows (mash.chit, mash.chet, ma.she.chat, cha.loph)
        spec = json.loads(MAPPING_PATH.read_text(encoding='utf-8'))
        for t in spec['term_assignments']:
            mti = t.get('mti_id')
            if mti is None:
                continue
            if mti not in term_sg_counts and t['primary_subgroup'] == 'M10-BND':
                term_sg_counts[mti]['M10-BND'] = 0

        n_links = 0
        for mti_id, sg_counts in term_sg_counts.items():
            sorted_sg = sorted(sg_counts.items(), key=lambda x: -x[1])
            primary_sg = sorted_sg[0][0]
            for sg, count in sorted_sg:
                if count == 0:
                    note = f'[primary] 0 verses (empty-corpus BOUNDARY term)'
                else:
                    note = f'[primary] {count} verses' if sg == primary_sg else f'[secondary] {count} verses'
                cur.execute(
                    "INSERT INTO mti_term_subgroup "
                    "(mti_term_id, cluster_subgroup_id, placement_note, "
                    "delete_flagged, created_at, last_updated_date) "
                    "VALUES (?, ?, ?, 0, ?, ?)",
                    (mti_id, sg_id_by_code[sg], note, NOW, NOW),
                )
                n_links += 1
        print(f"  Op B: inserted {n_links} mti_term_subgroup rows")

        # Op C — UPDATE verse_context.cluster_subgroup_id
        n_routed = 0
        for vc_id, sg in vc_to_sg.items():
            cur.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (sg_id_by_code[sg], vc_id),
            )
            n_routed += cur.rowcount
        print(f"  Op C: routed {n_routed} verses to sub-groups (expected {len(vc_to_sg)})")
        assert n_routed == len(vc_to_sg)

        conn.commit()
        print(f"  Committed at {NOW}")
    except Exception:
        conn.rollback()
        print('ROLLED BACK')
        raise

    # === POST-CHECKS ===
    print()
    print('=== POST-CHECKS ===')
    print('Per-sub-group verse counts:')
    total_routed = 0
    for code, _, _ in SUBGROUPS:
        n = cur.execute(
            "SELECT COUNT(*) FROM verse_context vc "
            "JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id "
            "WHERE cs.cluster_code='M10' AND cs.subgroup_code=? AND vc.is_relevant=1 "
            "AND COALESCE(vc.delete_flagged,0)=0",
            (code,),
        ).fetchone()[0]
        print(f"  {code}: {n}")
        total_routed += n
    print(f"  TOTAL: {total_routed}")

    n_unrouted = cur.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code='M10' AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL
    """).fetchone()[0]
    print(f"\nUnrouted is_relevant verses: {n_unrouted}")
    assert n_unrouted == 0

    cluster_status_post = cur.execute(
        "SELECT status FROM cluster WHERE cluster_code='M10'"
    ).fetchone()[0]
    print(f"cluster.M10.status = {cluster_status_post!r}")
    assert cluster_status_post == 'Analysis - In Progress'

    print()
    print('=== M10 PHASE 6 COMPLETE ===')
    print(f"- {len(SUBGROUPS)} cluster_subgroup rows created (Op A)")
    print(f"- {n_links} mti_term_subgroup rows created (Op B)")
    print(f"- {n_routed} verses routed (Op C)")
    print("- Status flip skipped (already 'Analysis - In Progress' from Phase 4)")
    print('Ready for Phase 7 — VCG design (v2_8 §10).')
    conn.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
