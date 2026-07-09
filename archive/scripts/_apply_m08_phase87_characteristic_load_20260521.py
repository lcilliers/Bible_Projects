"""M08 Phase 8.7 — Characteristic mapping load (v2_8 §11B as confirmation step).

Under v2_8 §8.0 Phase 5 designed sub-groups to represent characteristics,
so Phase 8.7 reduces to formal load (no retrofit debate). M08's 5
characteristics are implicit in the Phase 5 v2 sub-group structure:

- CHAR-1 Arrogant self-elevation — volume-split into M08-A1, A2, A3, A4 by seat-of-pride axis
- CHAR-2 Presumptuous defiance → M08-B (1:1)
- CHAR-3 Boasting and self-display → M08-C (1:1, M22 cross-register)
- CHAR-4 Vain conceit → M08-D (1:1)
- CHAR-5 Pride of power and position → M08-E (1:1, M23 cross-register)

Inserts:
- 5 characteristic rows
- 8 characteristic_subgroup links (M:N: 4 for CHAR-1 + 1 each for CHAR-2..5)
- 5 cluster_observation rows:
  * 1 INTEGRATION_NOTE for CHAR-1 volume-split
  * 2 INTER_RELATIONSHIP (M08-C ↔ M22, M08-E ↔ M23)
  * 1 SET_ASIDE_NOTE for the 174 Phase 5.5 set-aside verses
  * 1 INTEGRATION_NOTE for the Phase 8.5 G0193 BOUNDARY promotion
"""
import sys, io, sqlite3
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SOURCE = ('WA-M08-subgroup-design-v2-20260520.md (Phase 5 v2 §1 characteristics + §2 sub-group mapping); '
          'WA-M08-constitution-debate-v1-20260520.md (Phase 3 cross-register flags); '
          'WA-M08-dir-005-phase85-boundary-resolution-v1-20260521.md (Phase 8.5 G0193 promotion)')

CHARACTERISTICS = [
    (1, 'Arrogant self-elevation',
     "The inner state in which the heart or will lifts itself above its proper station before God and others, claiming standing, honour, or status that does not belong to it. The dominant characteristic of M08 (51% of substantive verses on v1); per v2_8 §8.0 rule 2 it is volume-split across four sub-groups (M08-A1 heart, M08-A2 eyes/outward bearing, M08-A3 national/collective, M08-A4 general dispositional) by seat-of-pride axis while preserving the single characteristic identity. Primary vocabulary: rum, ga.on, ga.a.vah, ga.vah, ga.vo.ah, ge.eh, huperēfania/huperēfanos, hupsēlos, filautos, qo.mah-pride-uses. Heart is the most-named seat (lev/kardia idiom); eyes/posture is the visible register; national/collective frames the political-social face; general dispositional carries the wisdom/NT-vice-catalogue mass."),
    (2, 'Presumptuous defiance',
     "The inner state in which the will asserts itself against known divinely-established limits, appointed authority, or revealed commands with a boiling-over force — pride-as-deliberate-defiance rather than merely elevated self-regard. The volitional/active form of pride: the self translating its elevation into deliberate transgression. Vocabulary: zid (boiling presumption), za.don (insolent defiance), zed (arrogant disregard for God's law), authadēs (self-will dismissing authority), tolmētēs (reckless presumption against divine beings), archō M08-relational verses (domineering authority and presumptuous self-assertion in NT narratives)."),
    (3, 'Boasting and self-display',
     "The inner impulse to self-glorify through words, visible claims, and public assertion of one's own worth, achievement, credentials, or future plans — pride moving outward through speech and self-presentation. Includes both condemned forms (self-boasting of wisdom/might/wealth, premature self-glorification) and the Pauline examined-boasting discourse (boasting only in the Lord / in weakness / in the cross). Vocabulary: kauchaomai/kauchēma/kauchēsis family (Greek boasting), alazoneia/alazōn (inner boasting disposition), ha.lal self-directed (Hebrew boast sense, distinct from praise sense). CROSS-REGISTER NOTE: M22 (praise/thanksgiving/glory) — kauchaomai and ha.lal also evidence God-directed glorying within their corpora. Phase 7 separated three VCG registers: condemned self-boasting / Pauline examined / God-directed glorying."),
    (4, 'Vain conceit',
     "Pride operating specifically in the cognitive faculty as a false, inflated self-assessment — the mind's wrong picture of itself that produces blindness to truth, fuels controversy, generates communal disorder, and causes the person to claim resources, status, or recognition beyond what is warranted. The cognitive register of pride, distinct from CHAR-1's dispositional posture, CHAR-2's volitional defiance, and CHAR-3's verbal expression. Vocabulary: tufoō (puffed up with conceit), fusioō (inflated through partisan attachment / intellectual pride / ungrounded fantasy), fusiōsis (conceit producing communal disorder), huperfroneō (thinking more highly of oneself than warranted)."),
    (5, 'Pride of power and position',
     "The inner arrogance that arises when strength, social authority, material prosperity, or national might becomes the ground for self-exaltation and contemptuous elevation above others. Pride here is expressed through a specific medium — position, resource, or capacity — making it M08's structural-power register. Vocabulary: ga.on proud-might subset (national/imperial pride), archō domineering-authority verses (Mar 10:42 — rulers lording over), hupsēlofroneō (wealth-pride), ga.vah Eze 28:5 (wealth-induced pride), shal.le.tet (imperious self-will), a.din (voluptuous ease feeding self-sufficiency), ma.rom power-height (fortified elevation as power strategy), qo.mah Eze 19:11 (visible dominance of rulers). CROSS-REGISTER NOTE: M23 (strength/power/dominion) is the primary register for several terms; they remain in M08 because their verses evidence strength-misused-as-self-exaltation."),
]

# (char_seq, subgroup_code, qualifier_note, is_partial, partial_register_note)
LINKS = [
    (1, 'M08-A1', 'Heart-elevation register: pride constitutionally located in the heart (lev/kardia idiom). Volume-split partition of CHAR-1 by seat-of-pride axis.', 0, None),
    (1, 'M08-A2', "Eyes / outward-bearing register: pride registering in the haughty-eyes vocabulary, ostentatious posture, and visible body-language. Volume-split partition of CHAR-1.", 0, None),
    (1, 'M08-A3', 'National / collective register: pride attributed to a nation, people, city, king-as-representative, or collective subject. Dominated by ga.on national-pride corpus (Moab, Babylon, Israel, Egypt, Assyria). Volume-split partition of CHAR-1.', 0, None),
    (1, 'M08-A4', 'General dispositional register: individual pride as settled inner disposition without specific named inner organ or collective framing. Wisdom maxims, NT vice catalogues, psalmic enemy portraits, general individual pride. Largest M08-A partition. Volume-split partition of CHAR-1. (Post-Phase-8.5: 69 verses including G0193 akratēs promotion.)', 0, None),
    (2, 'M08-B', 'Single-sub-group representation.', 0, None),
    (3, 'M08-C', 'Single-sub-group representation. Cross-register flag M22 (praise/thanksgiving/glory) preserved at sub-group level; Phase 7 separated three VCG registers (condemned self-boasting / Pauline examined / God-directed glorying) within this sub-group.', 0, None),
    (4, 'M08-D', 'Single-sub-group representation.', 0, None),
    (5, 'M08-E', 'Single-sub-group representation. Cross-register flag M23 (strength/power/dominion) preserved at sub-group level.', 0, None),
]

# (characteristic_seq | None, subgroup_code | None, observation_type, target_phase, title, description)
OBSERVATIONS = [
    (1, 'M08-A1', 'INTEGRATION_NOTE', 'phase_9_findings',
     'CHAR-1 volume-split across M08-A1 / M08-A2 / M08-A3 / M08-A4',
     "CHAR-1 (Arrogant self-elevation) is the cluster's dominant characteristic (151 of 293 substantive verses = 51.5%). Per v2_8 §8.0 rule 2, volume-split across four sub-groups by seat-of-pride axis: M08-A1 (heart, 33V — including post-Phase-8.5 promotion of G0193 contribution implicit via mti_term routing), M08-A2 (eyes/outward bearing, 11V), M08-A3 (national/collective, 40V), M08-A4 (general dispositional, 69V — post-Phase-8.5). The characteristic identity persists across the four sub-groups; Phase 9 catalogue prompts should evaluate CHAR-1 as a single inner-being faculty manifesting in four registers, not as four separate characteristics. Splitting axis is the anatomical/framing locus where the pride is named (heart vs eyes vs collective subject vs unspecified)."),

    (3, 'M08-C', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M08-C boasting ↔ M22 praise/glory as register-adjacent through shared vocabulary',
     "Phase 3 cross-register analysis (per v2_7 §6.3.2 verse-level relationship test) confirmed the kauchaomai family (kauchaomai/kauchēma/kauchēsis) and ha.lal verb carry three distinct registers within M08-C's 70-verse corpus: (a) condemned self-directed boasting (M08-C-VCG-01); (b) Pauline examined-boasting discourse — boasting only in the Lord / in weakness / in the cross (M08-C-VCG-02); (c) God-directed glorying / praise (M08-C-VCG-03, the M22 register). The same lexemes express both M08 (self-boasting) and M22 (praise-of-God) inner-being content; the register-distinction is verse-level. Phase 9 T6 (Structural Relationships with Other Characteristics) should articulate the M08 ↔ M22 register-adjacency: praise becomes boasting when self-directed; boasting becomes praise when God-directed. When M22 opens, the M08-C-VCG-03 verses (~20-23 verses) and the relevant ha.lal verses may be picked up as cross-cluster contributions to M22's praise vocabulary."),

    (5, 'M08-E', 'INTER_RELATIONSHIP', 'phase_9_findings',
     'M08-E pride-of-power ↔ M23 strength/dominion as misuse-of-faculty register',
     "Phase 3 cross-register analysis confirmed several M08-E terms (ga.on proud-might, archō domineering-authority, hupsēlofroneō wealth-pride, ma.rom fortified-elevation, shal.le.tet imperious self-will, a.din voluptuous ease, qo.mah Eze 19:11) carry their primary register in M23 (strength/power/dominion); they remain in M08 because their verses evidence strength-misused-as-self-exaltation. The pride-of-power register is structurally the M23 faculty turned inward toward self-aggrandisement. Phase 9 T6 should articulate the M08 ↔ M23 misuse-of-faculty pairing: M23 carries strength/capacity as the inner-being faculty; M08-E carries the corruption of that faculty when it becomes the ground for arrogance. When M23 opens, the M08-E sub-group's term list informs which strength terms have a documented misuse-pole at the verse level."),

    (None, None, 'INTEGRATION_NOTE', 'phase_9_findings',
     'Phase 5.5 set-aside: 174 non-M08-content verses (Option 2 researcher decision)',
     "At Phase 5.5 (2026-05-20), 174 verses from polysemic M08 terms were set_aside via CC patch before Phase 6 routing (researcher Option 2 decision). Breakdown: (a) 122 verses with M22-register content (divine majesty / God-directed exaltation) from rum, ga.on, ga.a.vah, ga.vah, ha.lal, ge.ut, go.vah, ma.rom, ga.ah — terms STAY in M08 via §6.3.2 because their pride verses survived, but these individual verses carry M22 not M08 content; set_aside_reason='non-M08 content — M22-register (divine majesty / God-directed exaltation); term STAYS in M08 via other verses (v2_8 §6.3.2)'. (b) 52 verses with no inner-being content (archō temporal/narrative markers; ra.hav positive-assertiveness; H7312 Pro 25:3); set_aside_reason='non-M08 content — narrative marker / neutral assertiveness; no inner-being state evidenced'. These verses are recoverable for cross-cluster analysis if needed (M22 may pick up the 122 M22-register verses when it opens) but do not contribute findings to M08. Substantive M08 corpus reduced from 470 → 296 → 293 (post-Phase-7 duplicate cleanup)."),

    (1, 'M08-A4', 'INTEGRATION_NOTE', 'phase_9_findings',
     'Phase 8.5: G0193 akratēs promoted from BOUNDARY to M08-A4-VCG-01',
     "At Phase 8.5 (2026-05-21), the single BOUNDARY-verdict term G0193 akratēs (intemperate, 1 verse at 2Ti 3:3) was PROMOTED to M08-A4-VCG-01 (NT vice-catalogue register) per researcher decision. Rationale: akratēs sits in the same scriptural vice catalogue as filautos (2Ti 3:2) and huperēfanos (2Ti 3:2), which are already routed to M08-A4-VCG-01. Per the AI's Phase 3 framing, akratēs is the enabling-condition register through which CHAR-1 operates unchecked — the breakdown of inner discipline that lets pride run free. The term is therefore a qualifying/supportive contributor to CHAR-1's NT vice-catalogue VCG rather than its own characteristic. M08-BOUNDARY sub-group + M08-BOUNDARY-VCG-01 soft-deleted; cluster now has 8 sub-groups + 24 VCGs."),
]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Pre-checks
print('=== PRE-CHECKS ===')
n_existing = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
assert n_existing == 0, f'M08 already has {n_existing} characteristic rows'
print(f'  No pre-existing characteristic rows for M08 (clean to insert)')

sg_id = {r['subgroup_code']: r['id'] for r in cur.execute(
    "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0"
).fetchall()}
for _, code, _, _, _ in LINKS:
    assert code in sg_id, f'Sub-group {code} not in DB'
print(f'  All 8 target sub-group codes exist in DB: {sorted(sg_id.keys())}')

n_substantive = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
    WHERE mt.cluster_code='M08' AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
""").fetchone()[0]
print(f'  M08 substantive is_relevant verses: {n_substantive}')

# Apply
print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    char_id_by_seq = {}
    for char_seq, short_name, definition in CHARACTERISTICS:
        cur.execute(
            "INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('M08', char_seq, short_name, definition, SOURCE, 'v1', NOW, NOW),
        )
        char_id_by_seq[char_seq] = cur.lastrowid
    print(f'  Op A: inserted {len(CHARACTERISTICS)} characteristic rows')

    for char_seq, subgroup_code, qualifier, is_partial, partial_note in LINKS:
        cur.execute(
            "INSERT INTO characteristic_subgroup (characteristic_id, cluster_subgroup_id, qualifier_note, is_partial, partial_register_note, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (char_id_by_seq[char_seq], sg_id[subgroup_code], qualifier, is_partial, partial_note, NOW, NOW),
        )
    print(f'  Op B: inserted {len(LINKS)} characteristic_subgroup links')

    for char_seq, sg_code, obs_type, target_phase, title, description in OBSERVATIONS:
        char_id = char_id_by_seq[char_seq] if char_seq else None
        sg_id_val = sg_id[sg_code] if sg_code else None
        cur.execute(
            "INSERT INTO cluster_observation (cluster_code, characteristic_id, cluster_subgroup_id, source_phase, observation_type, target_phase, title, description, status, raised_date, source_file, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('M08', char_id, sg_id_val, 'phase_8_7', obs_type, target_phase, title, description, 'open', NOW, SOURCE, NOW, NOW),
        )
    print(f'  Op C: inserted {len(OBSERVATIONS)} cluster_observation rows')

    conn.commit()
    print(f'  Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

# Post-checks
print()
print('=== POST-CHECKS ===')
n_char = cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f'  characteristic rows for M08: {n_char} (expected 5)')
assert n_char == 5

n_links = cur.execute("""
    SELECT COUNT(*) FROM characteristic_subgroup cs
    JOIN characteristic c ON c.id = cs.characteristic_id
    WHERE c.cluster_code='M08' AND COALESCE(cs.delete_flagged,0)=0
""").fetchone()[0]
print(f'  characteristic_subgroup links for M08: {n_links} (expected 8)')
assert n_links == 8

n_obs = cur.execute("SELECT COUNT(*) FROM cluster_observation WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0").fetchone()[0]
print(f'  cluster_observation rows for M08: {n_obs} (expected 5)')
assert n_obs == 5

print()
print('Characteristic → sub-group binding:')
for r in cur.execute("""
    SELECT c.char_seq, c.short_name, cs.subgroup_code,
           (SELECT COUNT(*) FROM verse_context vc
              JOIN cluster_subgroup cs2 ON cs2.id = vc.cluster_subgroup_id
              WHERE cs2.subgroup_code = cs.subgroup_code AND vc.is_relevant=1
                AND COALESCE(vc.delete_flagged,0)=0) AS verses
    FROM characteristic c
    JOIN characteristic_subgroup cl ON cl.characteristic_id = c.id
    JOIN cluster_subgroup cs ON cs.id = cl.cluster_subgroup_id
    WHERE c.cluster_code='M08' AND COALESCE(c.delete_flagged,0)=0
      AND COALESCE(cl.delete_flagged,0)=0
    ORDER BY c.char_seq, cs.subgroup_code
""").fetchall():
    print(f"  CHAR-{r['char_seq']} ({r['short_name']:<32}) → {r['subgroup_code']:<10} ({r['verses']} verses)")

print()
print('=== M08 PHASE 8.7 COMPLETE ===')
print('- 5 characteristics loaded')
print('- 8 characteristic_subgroup links')
print('- 5 cluster_observation rows (2 INTEGRATION_NOTE + 2 INTER_RELATIONSHIP + 1 Phase 5.5 set-aside record)')
print('Ready for Phase 9 — Catalogue prompts (per characteristic + cluster synthesis, v2_8 §12).')
conn.close()
