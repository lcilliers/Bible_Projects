"""M09 Phase 6 — sub-group structural apply + verse routing.

Per v2_8 §9. Per directive wa-cluster-M09-dir-002-phase6-subgroup-assign-v1-20260521.md.

Operations:
- Op A: INSERT 8 cluster_subgroup rows (M09-A..H).
- Op B: INSERT mti_term_subgroup rows for every (term, sub-group) pair derived from the mapping.
- Op C: UPDATE verse_context.cluster_subgroup_id for every is_relevant vc row per mapping.
- Op D: skipped — cluster.status already advanced to 'Analysis - In Progress' by Phase 4.

Source: wa-cluster-M09-subgroup-mapping-resolved-v1-20260521.json (flat vc_id → subgroup_code).
"""
import sys, io, json, sqlite3
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
DB = REPO / 'database' / 'bible_research.db'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
DIRECTIVE_ID = 'wa-cluster-M09-dir-002-phase6-subgroup-assign-v1-20260521'
MAPPING_PATH = REPO / 'Sessions' / 'Session_Clusters' / 'M09' / 'wa-cluster-M09-subgroup-mapping-resolved-v1-20260521.json'

# Sub-group definitions: (code, label, core_description)
SUBGROUPS = [
    ('M09-A', 'Humility — willed self-lowering',
     'CHAR-1 (Humility) — voluntary/dispositional split (C1a of volume-split). The inner disposition of willed self-lowering before God and others: heart-level humbling (ka.na voluntary verses — 2Ch 7:14; 2Ch 33:12; 2Ki 22:19), the chosen character-garment of tapeinofrosunē (Col 3:12; Phili 2:3; Act 20:19), Christ\'s self-emptying paradigm (Phili 2:8), willed self-lowering as the way to exaltation (Mat 18:4; Luk 14:11; Luk 18:14; Jam 4:10; 1Pe 5:6), tapeinos as inner relational disposition (Mat 11:29; Rom 12:16; Jam 4:6; 1Pe 5:5), and Hebrew comprehensive walking-humbly-with-God (Mic 6:8) + humility-paired-with-wisdom (Pro 11:2).'),
    ('M09-B', 'Lowliness — experienced and imposed state',
     'CHAR-1 (Humility) — condition/state/imposed split (C1b of volume-split). The state of being-lowered: social/circumstantial lowliness drawn into divine favour (Luk 1:48 Mary\'s tapeinōsis; Luk 1:52 tapeinos exalted), suffering-imposed lowliness (Act 8:33; 2Cor 7:6; 2Cor 12:21), creaturely physical lowliness awaiting transformation (Phili 3:21), the deflation of pride rooted in wealth (Jam 1:9-10), cultivated contentment through circumstantial lowering (Phili 4:12), and the externally-imposed-humbling instances of ka.na (2Ch 28:19; Job 40:12; Psa 106:42; Psa 107:12) that evidence what divine lowering looks like when the voluntary posture is absent.'),
    ('M09-C', 'Submission — inner disposition of will',
     'CHAR-2 (Submission) — heart/conscience-located split (C2a of volume-split). The inner heart/conscience disposition of willing yielding to legitimate authority. Cross-register flag: M30 (Obedience). Heart-located submission (Rom 6:17 obedience from the heart; Eph 6:5 / Col 3:22 with sincere heart / fearing the Lord; Phili 2:12 working out salvation with fear and trembling), conscience-yielding (Heb 5:8 Christ learned obedience through what he suffered; Heb 11:8 Abraham obeyed by faith; 1Pe 3:6 Sarah obeyed Abraham), faith-rooted submission of mind (2Cor 10:5 taking every thought captive; 2Cor 10:6 readiness to punish disobedience), willing-receptive learner-posture (1Ti 2:11 in submission with quietness), and the negative use exposing competing inner yielding (Rom 6:12-16 — what one obeys determines whose servant one is). One diatassō verse (Luk 17:10 — self-assessing servant posture) carries M09-relational content and routes here.'),
    ('M09-D', 'Submission — relational pattern of obedience',
     'CHAR-2 (Submission) — lived expression/relational pattern split (C2b of volume-split). The lived relational pattern of obedience-in-context: obedience to the gospel as inner-being event (Rom 1:5; 16:26; Rom 10:16; Rom 15:18-19; Rom 16:19; 2Th 1:8), early-Christian responsive obedience (Act 6:7; 1Pe 1:2; 1Pe 1:14; 1Pe 1:22), gospel\'s social-relational expression (2Cor 7:15 — Titus\'s reception; 2Cor 9:13 confession; Phile 21 — confidence in obedience; 2Th 3:14 not obeying), family-relational obedience patterns (Eph 6:1; Col 3:20; 1Ti 3:4), eschatological-allegiance submission (Gen 49:10; Heb 5:9), Pro 30:17 (negation), and Gal 2:5 submission deliberately withheld to protect gospel. **PHASE_8_5_FLAG**: 11 G1299 diatassō verses (Mat 11:1; Luk 3:13; Luk 17:9; Act 7:44; Act 18:2; 1Cor 7:17; 1Cor 9:14; 1Cor 11:34; 1Cor 16:1; Gal 3:19; Tit 1:5) provisionally routed here pending Phase 8.5 SET-ASIDE or ROUTE-TO-M23.'),
    ('M09-E', 'Contrition — crushed and broken spirit',
     'CHAR-3 (Contrition) — single-sub-group representation. The acute form of humility produced by genuine confrontation with one\'s failure or with the holiness of God. Inner brokenness located in spirit and heart. Psa 34:18 (the LORD is near to the broken-hearted, saves the crushed in spirit); Isa 57:15 (God dwells with him who is contrite and lowly in spirit, reviving spirit and heart). dak.ka pairs structurally with lowliness — the crushed/broken inner posture that opens the person to divine encounter.'),
    ('M09-F', 'Meekness — calibrated restraint and gentleness',
     'CHAR-4 (Meekness/Gentleness) — single-sub-group representation. The inner quality of calibrated restraint and gentleness — controlled strength, capacity to hold force in measured response. Heb 5:2 (metriopatheō — high priest deals gently/measuredly with the ignorant grounded in his own creaturely weakness); Act 9:38 (okneō — absence of hesitation, immediate unimpeded responsiveness as volitional readiness). Multi-faceted note: Mat 11:29 tapeinos (Christ "gentle and lowly in heart") provides a secondary anchor for this sub-group — its primary placement is M09-A but its gentleness dimension contributes to M09-F.'),
    ('M09-G', 'Dignity — grounded moral gravity',
     'CHAR-5 (Dignity) — single-sub-group representation. semnotēs as grounded moral gravity and seriousness of character — inner-grounded worth that does NOT require self-promotion or status-seeking. Cross-register flag: M08 (structural opposite of proud self-display). 1Ti 2:2 (the inner quality of a peaceable, godly life); 1Ti 3:4 (the character from which orderly household governance flows); Tit 2:7 (the gravitas authenticating teaching). Not the social-honour-rank sense.'),
    ('M09-H', 'Willing-heartedness — the freely-moved spirit',
     'CHAR-6 (Willing-heartedness) — single-sub-group representation. na.div as the freely-moved willing disposition of the heart/spirit. Cross-register flags: M04 (joy/delight — spontaneous-generosity dimension); M29 (desire/will — volitional dimension). Exo 35:5 (a willing heart bringing the LORD\'s contribution); Exo 35:22 (every willing-hearted person came); 1Ch 28:21 (willing-hearted skilled craftsmen); 2Ch 29:31 (willing-hearted offerings); Psa 51:12 (uphold me with a willing spirit — pairing willing spirit with joy of salvation in penitential context). The inner posture of the will that opens toward God and community rather than self-protects.'),
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
    "SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code='M09' AND COALESCE(delete_flagged,0)=0"
).fetchone()[0]
print(f'  Pre-existing M09 sub-groups: {n_existing_sg}')
assert n_existing_sg == 0, 'M09 sub-groups already exist'

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
    if r['cluster_code'] != 'M09':
        print(f'  WARN vc_id={r["id"]} not M09 (cluster={r["cluster_code"]})'); problems += 1
    if r['is_relevant'] != 1:
        print(f'  WARN vc_id={r["id"]} is_relevant={r["is_relevant"]} (expected 1)'); problems += 1
    if r['cluster_subgroup_id'] is not None:
        print(f'  WARN vc_id={r["id"]} cluster_subgroup_id already set to {r["cluster_subgroup_id"]}'); problems += 1
    if r['df']:
        print(f'  WARN vc_id={r["id"]} delete_flagged=1'); problems += 1
if problems:
    raise SystemExit(f'Pre-check failures: {problems}')
print(f'  All {len(rows)}/{len(all_ids)} vc rows in M09, is_relevant=1, cluster_subgroup_id=NULL OK')

# Cluster status
cluster_status = cur.execute("SELECT status FROM cluster WHERE cluster_code='M09'").fetchone()[0]
print(f'  cluster.M09.status = {cluster_status!r}')
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
            ('M09', code, label, descr, idx, DIRECTIVE_ID, NOW, NOW),
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
        "WHERE cs.cluster_code='M09' AND cs.subgroup_code=? AND vc.is_relevant=1 "
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
    WHERE mt.cluster_code='M09' AND vc.is_relevant=1
      AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL
""").fetchone()[0]
print()
print(f'Unrouted is_relevant verses: {n_unrouted}')
assert n_unrouted == 0

cluster_status_post = cur.execute("SELECT status FROM cluster WHERE cluster_code='M09'").fetchone()[0]
print(f'cluster.M09.status = {cluster_status_post!r}')
assert cluster_status_post == 'Analysis - In Progress'

print()
print('=== M09 PHASE 6 COMPLETE ===')
print(f'- {len(SUBGROUPS)} cluster_subgroup rows created (Op A)')
print(f'- {n_links} mti_term_subgroup rows created (Op B)')
print(f'- {n_routed} verses routed (Op C)')
print(f'- Status flip skipped (already \'Analysis - In Progress\' at Phase 4)')
print('Ready for Phase 7 — VCG design (v2_8 §10).')
conn.close()
