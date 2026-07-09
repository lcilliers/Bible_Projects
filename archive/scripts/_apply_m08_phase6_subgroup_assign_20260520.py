"""M08 Phase 6 — sub-group structural apply + verse routing.

Per v2_8 §9. Per directive WA-M08-dir-002-subgroup-assign-v1-20260520.md.

Operations:
- Op A: INSERT 9 cluster_subgroup rows (M08-A1..A4, M08-B, M08-C, M08-D, M08-E, M08-BOUNDARY).
- Op B: INSERT mti_term_subgroup rows for every (term, sub-group) pair derived from the mapping.
- Op C: UPDATE verse_context.cluster_subgroup_id for every is_relevant vc row per mapping.
- Op D: skipped — cluster.status already advanced to 'Analysis - In Progress' by Phase 4.

Source: WA-M08-subgroup-mapping-resolved-v2-20260520.json (flat vc_id → subgroup_code).
"""
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
DIRECTIVE_ID = 'wa-cluster-M08-dir-002-subgroup-assign-v1-20260520'
MAPPING_PATH = REPO / 'Sessions' / 'Session_Clusters' / 'M08' / 'WA-M08-subgroup-mapping-resolved-v2-20260520.json'

# Sub-group definitions: (code, label, core_description)
SUBGROUPS = [
    ('M08-A1', 'Heart-Elevation — Pride Seated in the Heart',
     'CHAR-1 split (seat_of_pride: heart). Verses where pride is constitutionally located in the heart (lev/kardia) — the "lifted-up heart" idiom: prosperity causing the heart to be lifted up and forget God (Deu 8:14); the king\'s heart not to be raised above his brothers (Deu 17:20); pride explicitly located in the heart as what drives unfaithful action (2Ch 26:16; 2Ch 32:25; Pro 18:12; Eze 28:2; Eze 28:17; Eze 31:10; Dan 11:12; Hos 13:6; Dan 5:20); NT: huperēfania/huperēfanos locating arrogance in the thoughts of the heart (Mar 7:22; Luk 1:51). The anatomical core of CHAR-1.'),
    ('M08-A2', "Eye-Elevation and Outward Bearing — Pride's Visible Register",
     'CHAR-1 split (seat_of_pride: eyes_and_outward_bearing). Verses where the inner posture of pride registers in the outward-facing organs and bearing of the inner person — the eyes, the gaze, posture, neck. Includes "haughty eyes" vocabulary (Psa 18:27; Pro 6:17; Pro 30:13; Psa 131:1; Isa 2:11; Isa 2:17; Isa 5:15); pride as outward display (Psa 73:6); daughters of Zion\'s ostentatious posture (Isa 3:16); face-posture shutting out God (Psa 10:4); head lifted up in pride (Job 10:16). Pride that has become visible body-language.'),
    ('M08-A3', 'National and Collective Pride — Pride as a Corporate Inner Characteristic',
     'CHAR-1 split (seat_of_pride: national_collective). Verses where the subject of pride is a nation, people, city, king-as-representative, or collective. Dominated by ga.on national-pride register (Moab, Babylon, Israel, Assyria, Egypt). Includes Moab\'s pride (Isa 16:6; Jer 13:9; Jer 48:29; Zep 2:10); Babylon\'s pride (Isa 13:11, 13:19, 14:11, 23:9); Israel\'s pride (Hos 5:5, 7:10; Amo 6:8, 8:7); collective pride brought low at the day of judgment (Isa 2:11, 2:17, 2:12). M08\'s political and social face.'),
    ('M08-A4', 'General Dispositional Pride — Individual Self-Elevation (Unspecified Seat)',
     'CHAR-1 split (seat_of_pride: general_dispositional_individual). Verses describing individual pride as settled inner disposition without a specific named inner organ (heart, eyes) or collective framing. Includes Proverbs wisdom maxims (Pro 16:18; Pro 16:19; Pro 29:23); NT vice catalogues (Rom 1:30; 2Ti 3:2; Jam 4:6; 1Pe 5:5); psalmic portraits of arrogant enemy (Psa 123:4; Psa 36:11); rum self-exaltation individual verses; self-love (filautos 2Ti 3:2) as dispositional root. The broadest expression of CHAR-1.'),
    ('M08-B', 'Presumptuous Defiance — Pride as Willful Transgression',
     'CHAR-2. Verses where pride expresses itself as boiling-over self-will that deliberately overrides divinely-established limits, appointed authority, and revealed commands. Hebrew zid (boiling presumption), za.don (insolent defiance), zed (arrogant disregard for God\'s law); Greek authadēs (self-will dismissing authority), tolmētēs (reckless presumption against divine beings), archō M08-relational verses (domineering authority and presumptuous self-assertion in narrative contexts: Mat 16:22, Mar 8:32, etc.). Pride moving from disposition to act.'),
    ('M08-C', "Boasting and Self-Display — Pride's Verbal and Public Form",
     'CHAR-3. Inner impulse to self-glorify through words, visible claims, and public assertion. Greek kauchaomai/kauchēma/kauchēsis family (32+11+12V), alazoneia/alazōn (inner boasting disposition), ha.lal self-directed boasting subset (10V — boasting of wisdom/might/wealth, premature self-glorification before battle is won, empty self-promotion); ro.hav (Psa 90:10). **Cross-register flag: M22** — Phase 7 VCG design distinguishes self-directed condemned boasting from Pauline examination of legitimate boasting grounds from God-directed glorying register within kauchaomai and ha.lal.'),
    ('M08-D', "Vain Conceit — Inflated Self-Estimate in the Mind",
     'CHAR-4. Pride in the cognitive faculty as inflated, ungrounded self-assessment — the mind\'s false picture of itself. Greek inflation vocabulary: tufoō (puffed up with conceit, 3V), fusioō (inflated through partisan attachment, intellectual pride over knowledge, ungrounded mental fantasy, 7V), fusiōsis (conceit generating communal disorder, 1V), huperfroneō (thinking more highly of oneself than warranted, 1V). Pride as cognitive self-deception.'),
    ('M08-E', 'Pride of Power and Position — Arrogance in Strength, Wealth, and Authority',
     'CHAR-5. Inner arrogance arising when strength, social authority, material prosperity, or national might becomes the ground for self-exaltation and contemptuous elevation above others. ga.on proud-might verses (Lev 26:19; Eze 7:24, 16:49, 24:21, 30:6, 30:18, 32:12, 33:28); archō domineering-authority (Mar 10:42); hupsēlofroneō (1Ti 6:17 wealth-pride); ga.vah Eze 28:5 (wealth-induced pride); shal.le.tet imperious self-will; a.din voluptuous ease; ma.rom fortified-elevation register (Jer 49:16; Obd 3; Hab 2:9); qo.mah Eze 19:11 (visible dominance of rulers). **Cross-register flag: M23** (strength/power/dominion).'),
    ('M08-BOUNDARY', 'BOUNDARY — Qualifying / Supportive Register',
     'BOUNDARY verdict from Phase 3 (§6.3.1 reason 3 — supportive/qualifying). G0193 akratēs (intemperate, mti_id=1113, 1V at 2Ti 3:3): lack of self-control placed in M08\'s characteristic vice-cluster alongside huperēfanos and filautos — the enabling condition through which pride operates unchecked. Researcher decision needed: M08 qualifying component, or transfer to future will/self-control cluster?'),
]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Load mapping
spec = json.loads(MAPPING_PATH.read_text(encoding='utf-8'))
vc_to_sg: dict[int, str] = {int(k): v for k, v in spec['vc_id_to_subgroup'].items()}
print(f'Loaded {len(vc_to_sg)} vc_id → subgroup assignments from {MAPPING_PATH.name}')

# === PRE-CHECKS ===
print()
print('=== PRE-CHECKS ===')

# Op A pre: no sub-groups yet
n_existing_sg = cur.execute(
    "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0"
).fetchone()[0]
print(f'  Pre-existing M08 sub-groups: {n_existing_sg}')
assert n_existing_sg == 0, 'M08 sub-groups already exist'

# Op C pre: confirm all 296 vc_ids exist and are is_relevant=1 (post Phase 5.5)
all_ids = list(vc_to_sg.keys())
qmarks = ','.join('?'*len(all_ids))
rows = cur.execute(f"""
    SELECT vc.id, vc.is_relevant, vc.cluster_subgroup_id, mt.cluster_code, COALESCE(vc.delete_flagged,0) AS df
    FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE vc.id IN ({qmarks})
""", all_ids).fetchall()
problems = 0
for r in rows:
    if r['cluster_code'] != 'M08':
        print(f'  WARN vc_id={r["id"]} not M08 (cluster={r["cluster_code"]})'); problems += 1
    if r['is_relevant'] != 1:
        print(f'  WARN vc_id={r["id"]} is_relevant={r["is_relevant"]} (expected 1)'); problems += 1
    if r['cluster_subgroup_id'] is not None:
        print(f'  WARN vc_id={r["id"]} cluster_subgroup_id already set to {r["cluster_subgroup_id"]}'); problems += 1
    if r['df']:
        print(f'  WARN vc_id={r["id"]} delete_flagged=1'); problems += 1
if problems:
    raise SystemExit(f'Pre-check failures: {problems}')
print(f'  All {len(rows)}/{len(all_ids)} vc rows in M08, is_relevant=1, cluster_subgroup_id=NULL OK')

# Cluster status
cluster_status = cur.execute("SELECT status FROM cluster WHERE cluster_code='M08'").fetchone()[0]
print(f'  cluster.M08.status = {cluster_status!r}')
assert cluster_status == 'Analysis - In Progress'

# === APPLY ===
print()
print('=== APPLYING ===')
cur.execute('BEGIN')
try:
    # Op A — INSERT cluster_subgroup rows
    sg_id_by_code: dict[str, int] = {}
    for idx, (code, label, descr) in enumerate(SUBGROUPS):
        cur.execute(
            "INSERT INTO cluster_subgroup (cluster_code, subgroup_code, label, core_description, "
            "sort_order, status, version, source, created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, 'active', 'v1', ?, ?, ?)",
            ('M08', code, label, descr, idx, DIRECTIVE_ID, NOW, NOW),
        )
        sg_id_by_code[code] = cur.lastrowid
    print(f'  Op A: inserted {len(SUBGROUPS)} cluster_subgroup rows')

    # Op B — INSERT mti_term_subgroup rows
    # Build per-term counts of vc rows per sub-group
    term_sg_counts: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    # For this we need mti_id for each vc_id
    vc_to_mti = {}
    rows = cur.execute(f"""
        SELECT id, mti_term_id FROM verse_context WHERE id IN ({qmarks})
    """, all_ids).fetchall()
    for r in rows:
        vc_to_mti[r['id']] = r['mti_term_id']
    for vc_id, sg in vc_to_sg.items():
        mti_id = vc_to_mti[vc_id]
        term_sg_counts[mti_id][sg] += 1

    n_links = 0
    for mti_id, sg_counts in term_sg_counts.items():
        sorted_sg = sorted(sg_counts.items(), key=lambda x: -x[1])
        primary_sg = sorted_sg[0][0]
        for sg, count in sorted_sg:
            note = f'[primary] {count} verses' if sg == primary_sg else f'[secondary] {count} verses'
            cur.execute(
                "INSERT INTO mti_term_subgroup (mti_term_id, cluster_subgroup_id, placement_note, "
                "delete_flagged, created_at, last_updated_date) VALUES (?, ?, ?, 0, ?, ?)",
                (mti_id, sg_id_by_code[sg], note, NOW, NOW),
            )
            n_links += 1
    print(f'  Op B: inserted {n_links} mti_term_subgroup rows')

    # Op C — UPDATE verse_context.cluster_subgroup_id
    n_routed = 0
    for vc_id, sg in vc_to_sg.items():
        cur.execute(
            "UPDATE verse_context SET cluster_subgroup_id=? "
            "WHERE id=? AND COALESCE(delete_flagged,0)=0",
            (sg_id_by_code[sg], vc_id),
        )
        n_routed += cur.rowcount
    print(f'  Op C: routed {n_routed} verses to sub-groups (expected {len(vc_to_sg)})')
    assert n_routed == len(vc_to_sg)

    conn.commit()
    print(f'  Committed at {NOW}')
except Exception:
    conn.rollback()
    print('ROLLED BACK')
    raise

# === POST-CHECKS ===
print()
print('=== POST-CHECKS ===')

print('Per-sub-group verse counts:')
total_routed = 0
for (code, label, _) in SUBGROUPS:
    n = cur.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id "
        "WHERE cs.cluster_code='M08' AND cs.subgroup_code=? AND vc.is_relevant=1 "
        "AND COALESCE(vc.delete_flagged,0)=0",
        (code,),
    ).fetchone()[0]
    print(f'  {code}: {n}')
    total_routed += n
print(f'  TOTAL: {total_routed}')

# Unrouted check
n_unrouted = cur.execute("""
    SELECT COUNT(*) FROM verse_context vc
    JOIN mti_terms mt ON mt.id = vc.mti_term_id
    WHERE mt.cluster_code='M08' AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL
""").fetchone()[0]
print()
print(f'Unrouted is_relevant verses: {n_unrouted}')
assert n_unrouted == 0

cluster_status_post = cur.execute("SELECT status FROM cluster WHERE cluster_code='M08'").fetchone()[0]
print(f'cluster.M08.status = {cluster_status_post!r}')
assert cluster_status_post == 'Analysis - In Progress'

print()
print('=== M08 PHASE 6 COMPLETE ===')
print(f'- {len(SUBGROUPS)} cluster_subgroup rows created (Op A)')
print(f'- {n_links} mti_term_subgroup rows created (Op B)')
print(f'- {n_routed} verses routed (Op C)')
print(f'- Status flip skipped (already \'Analysis - In Progress\' at Phase 4)')
print('Ready for Phase 7 — VCG design (v2_8 §10).')
conn.close()
