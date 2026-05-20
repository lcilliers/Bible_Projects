"""M07 Phase 8.7 — Characteristic mapping load (v2_8 §11B as confirmation step).

Under v2_8 §8.0 Phase 5 designed sub-groups to represent characteristics,
so Phase 8.7 reduces to formal load (no retrofit debate needed). M07's
6 characteristics are implicit in the Phase 5 sub-group structure:

- CHAR-1 Shame as experienced inner state — volume-split into M07-A, M07-B, M07-C
- CHAR-2 Humiliation as enforced abasement → M07-D (1:1)
- CHAR-3 Dishonour as relational worth-denial → M07-E (1:1)
- CHAR-4 Shamefulness as moral-evaluative judgment → M07-F (1:1)
- CHAR-5 Shame produced by contempt → M07-G (1:1, M06 cross-register)
- CHAR-6 Innocence as structural counter → M07-H (1:1, M12 cross-register)

Inserts:
- 6 characteristic rows
- 8 characteristic_subgroup links (M:N: 3 for CHAR-1 + 1 each for CHAR-2..6)
- ~5 cluster_observation rows (the carry-forward observations surfaced
  through the M07 process)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SOURCE = 'WA-M07-subgroup-design-v1-20260519.md (Phase 5 §1 characteristics + §2 sub-group mapping); WA-M07-constitution-debate-v2-20260519.md (Phase 3 v2 cross-register flags); WA-M07-phase85-researcher-decisions-v1-20260520.md (Phase 8.5 cross-cluster carry-forward)'

CHARACTERISTICS = [
    # (char_seq, short_name, definition)
    (1, 'Shame as experienced inner state',
     "The painful inner experience of being exposed as inadequate, wrong, or unworthy — the felt collapse of dignity, confidence, and standing. The primary and dominant characteristic of M07; expressed across three registers (unjust-wound, moral-consequence, and divine-encounter) which are volume-split into M07-A/B/C while preserving the single characteristic identity. The vocabulary centres on bosh, aischunē, aischunō, bo.shet, ke.lim.mah, cha.pher, kataischunō, entropē, ka.lam."),
    (2, 'Humiliation as enforced abasement',
     "Shame inflicted through an active downward movement of standing — the enforced lowering of a person, people, or pride-structure through social demotion, military defeat, physical exposure, or divine judgment. Distinct from CHAR-1 (the felt experience) by emphasising the mechanism of abasement and the reversal of exaltation. Primary vocabulary: ka.lam (bodily/social), bosh (military/cosmic abasement), atimia (mortal degradation), qa.lon (pride brought low), fimoō (silencing-as-humiliation), sha.phel (divine abasement of pride — joined at Phase 8.5)."),
    (3, 'Dishonour as relational worth-denial',
     "The relational dimension of shame — treating persons as having less worth than they possess; the active denial or stripping of honour through attitude, conduct, or social judgment. Distinct from CHAR-1 (felt inner state) and CHAR-2 (enforced downward movement): dishonour is specifically the relational dynamic of worth-assignment between persons or between person and God. Primary vocabulary: atimazō, atimia, kataischunō (relational uses), qa.lon, paradeigmatizō, entrepō (absence of regard), qa.lah."),
    (4, 'Shamefulness as moral-evaluative judgment',
     "The category of what is morally shameful, indecent, or degraded — the conscience's recognition that certain conduct or conduct-patterns violate inner propriety and cannot bear scrutiny before God or community. The evaluative/qualitative dimension of shame, not the experienced inner state. Primary vocabulary: aischros, aschēmosunē. Secondary uses (where the term names the inverted moral judgment): aischunē (Phili 3:19 inverted conscience; 2Cor 4:2 shameful conduct), atimia (Rom 1:26 dishonorable passions), qa.lon (Hos 4:18 perverted love of dishonour), bo.shet (idolatrous shameful objects)."),
    (5, 'Shame produced by contempt and rejection',
     "The shame experience arising from being treated with dismissive contempt or active rejection — the received, experiential face of the contempt-shame dynamic. The mechanism is contempt/rejection (M06's source-side characteristic); what M07 holds is the shame inflicted on the recipient. Three contempt modalities evidenced: dismissive inner attitude (exoutheneō), active mockery/violence (atimazō, paradeigmatizō uses), verbal attack (loidoria, kakologeō). CROSS-REGISTER NOTE: M06 (contempt-projection) is the source; Phase 9 T6 should address the M06 ↔ M07 cluster relationship."),
    (6, 'Innocence as structural counter to shame',
     "The inner moral-purity state that functions as the structural opposite and protection against shame — blameless conscience, clean inner will, and moral integrity as the inner condition that shields against guilt-shame, allows approach to God without shame, and whose absence sustains the shamed condition before God. Primary vocabulary: niq.qa.von, qe.ha.von (the four shared verses Gen 20:5; Psa 26:6; Psa 73:13; Hos 8:5). CROSS-REGISTER NOTE: M12 (purity/holiness) is the term's primary register; they are retained in M07 because every verse evidences the innocence-shame polarity directly. Phase 9 T6 should address the M07 ↔ M12 relationship."),
]

# (char_seq, subgroup_code, qualifier_note, is_partial, partial_register_note)
LINKS = [
    (1, 'M07-A', 'Unjust-wound register: shame as undeserved inner wound inflicted by enemies, circumstances, or collapse of trust. Volume-split partition of CHAR-1.', 0, None),
    (1, 'M07-B', 'Moral-consequence register: shame as deserved outcome of sin, folly, idolatry, wickedness — including absence of shame as moral collapse and corrective shame. Volume-split partition of CHAR-1. (Post-Phase-8.5: 111 verses including ni.dah Lam 1:8 promotion.)', 0, None),
    (1, 'M07-C', 'Divine-encounter register: shame in the vertical relationship between person and God — guilt-consciousness before the holy, covenant failure, soul-exposure in the divine presence. Volume-split partition of CHAR-1.', 0, None),
    (2, 'M07-D', 'Single-sub-group representation. (Post-Phase-8.5: 72 verses including 22 sha.phel promotions — God-abases-the-proud verses routed to VCG-03, social/bodily verses to VCG-01.)', 0, None),
    (3, 'M07-E', 'Single-sub-group representation.', 0, None),
    (4, 'M07-F', 'Single-sub-group representation.', 0, None),
    (5, 'M07-G', 'Single-sub-group representation. Cross-register flag M06 (contempt-projection) preserved at sub-group level and at each VCG description.', 0, None),
    (6, 'M07-H', 'Single-sub-group representation. Cross-register flag M12 (purity) preserved at sub-group level. The 4 verses (Gen 20:5; Psa 26:6; Psa 73:13; Hos 8:5) are shared between niq.qa.von and qe.ha.von — same verse_records, separate mti_terms.', 0, None),
]

# (characteristic_seq | None, subgroup_code | None, observation_type, target_phase, title, description)
OBSERVATIONS = [
    (1, 'M07-A', 'INTEGRATION_NOTE', 'phase_9_findings',
     'CHAR-1 volume-split across M07-A / M07-B / M07-C',
     "CHAR-1 (Shame as experienced inner state) is the cluster's dominant characteristic (224 of 359 substantive verses = 62%). Per v2_8 §8.0 rule 2, volume-split across three sub-groups by moral-direction axis: M07-A (unjust wound), M07-B (moral consequence), M07-C (divine encounter). The characteristic identity persists across the three sub-groups; Phase 9 catalogue prompts should evaluate CHAR-1 as a single inner-being faculty manifesting in three registers, not as three separate characteristics."),

    (5, 'M07-G', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M07-G shame ↔ M06 contempt as relational complements',
     "Phase 3 v2 cross-register analysis (per v2_7 §6.3.2 verse-level relationship test) confirmed the M07-G sub-group holds the shame-recipient face of a contempt-shame dynamic whose source-side (contempt-projection) lives in M06. Every verse in M07-G's 24-verse corpus (especially the 11 exoutheneō verses) evidences contempt as the active mechanism producing shame in the recipient. The two characteristics are relational complements: M06 contempt produces; M07-G shame receives. Phase 9 T6 (Structural Relationships with Other Characteristics) should make this M06 ↔ M07 relationship explicit; M06's eventual Phase 9 will see the same dynamic from the contempt side."),

    (6, 'M07-H', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M07-H innocence ↔ M12 purity as structural counters to shame',
     "Phase 3 v2 cross-register analysis flagged niq.qa.von and qe.ha.von with M12 (purity/holiness) as the terms' primary register; they remain in M07 because every verse evidences the innocence-shame polarity directly (innocence as shield, innocence in tension with experienced shame, incapacity-for-innocence sustaining the shamed condition). Phase 9 T6 should articulate the M07 ↔ M12 cross-cluster relationship: innocence is the inner moral state that protects against guilt-shame; its absence sustains the condition shame names."),

    (None, None, 'CROSS_CLUSTER_HANDOFF', 'session_d',
     'M09 pickup note: Pro 16:19 sha.phel (set-aside at Phase 8.5)',
     "At Phase 8.5 BOUNDARY resolution, Pro 16:19 (sha.phel — 'a lowly spirit with the poor', voluntary lowliness as morally superior) was SET-ASIDE from M07 because the verse evidences M09 (Humility/Meekness/Submission) directly, not M07 shame. ROUTE-TO-CLUSTER M09 was blocked at §18.2 eligibility check because no M09 term exists at this verse yet. WHEN M09 OPENS: sha.phel (H8213) is a likely M09 home-registry term; Pro 16:19 should be picked up there. CC tracks this for the M09 session-start prep."),

    (None, None, 'CROSS_CLUSTER_HANDOFF', 'session_d',
     'M09 pickup note: Pro 29:23 sha.phel (kept in M07-D at Phase 8.5; M09 dimension present)',
     "Pro 29:23 (sha.phel — 'one's pride will bring him low, but he who is lowly in spirit will obtain honor') was PROMOTED to M07-D at Phase 8.5 based on the 'pride brings him low' half (researcher decision). The 'lowly of spirit obtains honor' half is M09 content. Phase 9 T6 should articulate this M07 ↔ M09 pairing in one proverb. When M09 opens, sha.phel may need to also pick up Pro 29:23 as a secondary/shared-anchor case across clusters."),
]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Pre-checks
print('=== PRE-CHECKS ===')
n_existing = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
assert n_existing == 0, f"M07 already has {n_existing} characteristic rows"
print(f"  No pre-existing characteristic rows for M07 (clean to insert)")

# Resolve sub-group ids
sg_id = {r['subgroup_code']: r['id'] for r in cur.execute(
    "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0"
).fetchall()}
for _, code, _, _, _ in LINKS:
    assert code in sg_id, f"Sub-group {code} not in DB"
print(f"  All target sub-group codes exist in DB")

# Verify counts after Phase 8.5
n_substantive = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE mt.cluster_code='M07' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
      AND cs.subgroup_code != 'M07-BOUNDARY'
""").fetchone()[0]
print(f"  M07 substantive is_relevant verses (post Phase 8.5): {n_substantive}")

# Apply
print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    # Op A — INSERT characteristic rows
    char_id_by_seq = {}
    for char_seq, short_name, definition in CHARACTERISTICS:
        cur.execute(
            "INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, "
            " source, version, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('M07', char_seq, short_name, definition, SOURCE, 'v1', NOW, NOW),
        )
        char_id_by_seq[char_seq] = cur.lastrowid
    print(f"  Op A: inserted {len(CHARACTERISTICS)} characteristic rows")

    # Op B — INSERT characteristic_subgroup links
    for char_seq, subgroup_code, qualifier, is_partial, partial_note in LINKS:
        cur.execute(
            "INSERT INTO characteristic_subgroup (characteristic_id, cluster_subgroup_id, "
            " qualifier_note, is_partial, partial_register_note, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (char_id_by_seq[char_seq], sg_id[subgroup_code], qualifier, is_partial, partial_note, NOW, NOW),
        )
    print(f"  Op B: inserted {len(LINKS)} characteristic_subgroup links")

    # Op C — INSERT cluster_observation rows
    for char_seq, sg_code, obs_type, target_phase, title, description in OBSERVATIONS:
        char_id = char_id_by_seq[char_seq] if char_seq else None
        sg_id_val = sg_id[sg_code] if sg_code else None
        cur.execute(
            "INSERT INTO cluster_observation (cluster_code, characteristic_id, cluster_subgroup_id, "
            " source_phase, observation_type, target_phase, title, description, status, "
            " raised_date, source_file, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('M07', char_id, sg_id_val, 'phase_8_7', obs_type, target_phase, title, description,
             'open', NOW, SOURCE, NOW, NOW),
        )
    print(f"  Op C: inserted {len(OBSERVATIONS)} cluster_observation rows")

    conn.commit()
    print(f"  Committed at {NOW}")
except Exception:
    conn.rollback()
    print("ROLLED BACK")
    raise

# Post-checks
print()
print('=== POST-CHECKS ===')
n_char = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  characteristic rows for M07: {n_char} (expected 6)")
assert n_char == 6

n_links = cur.execute("""
    SELECT COUNT(*) FROM characteristic_subgroup cs
    JOIN characteristic c ON c.id = cs.characteristic_id
    WHERE c.cluster_code='M07' AND COALESCE(cs.delete_flagged,0)=0
""").fetchone()[0]
print(f"  characteristic_subgroup links for M07: {n_links} (expected 8)")
assert n_links == 8

n_obs = cur.execute("SELECT COUNT(*) FROM cluster_observation WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f"  cluster_observation rows for M07: {n_obs} (expected 5)")
assert n_obs == 5

# Distribution of characteristic_subgroup
print()
print("Characteristic → sub-group binding:")
for r in cur.execute("""
    SELECT c.char_seq, c.short_name, cs.subgroup_code,
           (SELECT COUNT(*) FROM verse_context vc
              JOIN cluster_subgroup cs2 ON cs2.id = vc.cluster_subgroup_id
              WHERE cs2.subgroup_code = cs.subgroup_code AND vc.is_relevant=1
                AND COALESCE(vc.delete_flagged,0)=0) AS verses
    FROM characteristic c
    JOIN characteristic_subgroup cl ON cl.characteristic_id = c.id
    JOIN cluster_subgroup cs ON cs.id = cl.cluster_subgroup_id
    WHERE c.cluster_code='M07' AND COALESCE(c.delete_flagged,0)=0
      AND COALESCE(cl.delete_flagged,0)=0
    ORDER BY c.char_seq, cs.subgroup_code
""").fetchall():
    print(f"  CHAR-{r['char_seq']} ({r['short_name'][:40]:<40}) → {r['subgroup_code']:<14} ({r['verses']} verses)")

print()
print('=== M07 PHASE 8.7 COMPLETE ===')
print(f"- 6 characteristics loaded")
print(f"- 8 characteristic_subgroup links")
print(f"- 5 cluster_observation rows (1 INTEGRATION + 2 INTER_RELATIONSHIP + 2 CROSS_CLUSTER_HANDOFF)")
print("Ready for Phase 9 — Catalogue prompts (per characteristic + cluster synthesis, v2_8 §12).")
conn.close()
