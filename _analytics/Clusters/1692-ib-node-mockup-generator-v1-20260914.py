"""
Phantom ib_node mockup generator -- escalation #1692, researcher request 2026-09-14.
NOT real data. Every id/strong/verse/cluster/subgroup/question value is invented for the sole
purpose of having something to render as a network graph and explore relational-analysis ideas
against, before ib_node/ib_observation are actually built. Schema matches the FINALIZED #1692
design (iba/docs/1692-ib-node-finalization-v1-20260912.md sec1), including the 2026-09-14 seq rule
(span.position for span-grounded rows, plain serial otherwise) and the "one row = one reference"
rule (multiple same-type references = multiple rows sharing one observation_id).
"""
import json
import random

random.seed(1692)  # reproducible

# ---- phantom reference pools -------------------------------------------------

CLUSTERS = ["M10", "M02", "M05", "M15", "M22"]

SUBGROUPS = {
    "M10": ["H_guilt", "B_sin", "G_transgression", "F_violence_wound"],
    "M02": ["A_love", "B_devotion"],
    "M05": ["C_fear", "D_dread"],
    "M15": ["E_wisdom", "F_folly"],
    "M22": ["G_pride", "H_humility"],
}

# a handful of strongs per subgroup, plus a few deliberately shared/hub strongs
STRONGS_BY_SUBGROUP = {
    "H_guilt": ["G1777", "H0816", "H0817", "H0818"],
    "B_sin": ["G0264", "G0265", "H2398", "H2399"],
    "G_transgression": ["G3847", "G3848", "H6586", "H6588"],
    "F_violence_wound": ["G3039", "H1792", "H1854"],
    "A_love": ["G0025", "G5368", "H0157"],
    "B_devotion": ["G4103", "H1697"],
    "C_fear": ["G5401", "H3372", "H3374"],
    "D_dread": ["G1169", "H2731"],
    "E_wisdom": ["G4678", "H2451"],
    "F_folly": ["G0878", "H5039"],
    "G_pride": ["G5187", "H1347"],
    "H_humility": ["G5012", "H6035"],
}
HUB_STRONGS = ["G1777", "H0816", "G3847"]  # reused across observations on purpose

VERSES = [
    "Matt.5.22", "Matt.5.28", "Rom.3.23", "Rom.7.15", "Jas.1.15", "Jas.4.17",
    "Ps.51.5", "Ps.32.5", "Prov.28.13", "1John.1.9", "Gen.4.7", "Gen.6.5",
    "Isa.53.6", "Ezek.18.20", "Lev.5.5", "Num.5.7", "2Sam.12.13", "Luke.15.18",
    "Eph.2.1", "Gal.5.19",
]
HUB_VERSES = ["Matt.5.22", "Rom.3.23", "Jas.1.15"]

MORPHS = ["A-NSM", "V-PAI-3S", "N-NSF", "V-AAI-3S", "A-GSM", "N-GSN"]
SURFACES_BY_STRONG_HINT = ["liable", "sin", "guilty", "transgress", "wound", "afraid",
                           "wise", "proud", "humble", "devoted", "loved", "foolish"]

QUESTIONS = [f"Q{n:02d}" for n in range(1, 13)]

STAGES = ["reading", "answer", "synthesis", "subgroup"]  # 'subgroup' per #1691 sec9 item8, 2026-09-14

TAGS_BY_STAGE = {
    "reading": ["instance-meaning", "verse-grouping", "difference-inference",
                "surface-gloss-divergence", "cross-family", "data-error"],
    "answer": ["needs-follow-up", "no-flag"],
    "synthesis": ["provisional", "corroborated"],
    "subgroup": ["cluster-definition-scope", "data-error", "ambiguous-gloss"],
}

CREATED_DATES = ["2026-09-11T09:14:00Z", "2026-09-11T14:02:00Z", "2026-09-12T10:31:00Z",
                  "2026-09-13T16:47:00Z"]


def home_for_subgroup(sg):
    for c, sgs in SUBGROUPS.items():
        if sg in sgs:
            return c
    raise KeyError(sg)


# ---- build a phantom observation pool ----------------------------------------
# (not part of #1692's own table, but needed so ib_node.observation_id points at
#  something coherent -- kept minimal, cluster_code/stage/tag only)

N_OBSERVATIONS = 30
observations = []
subgroup_pool = [sg for sgs in SUBGROUPS.values() for sg in sgs]

for i in range(1, N_OBSERVATIONS + 1):
    stage = random.choices(STAGES, weights=[55, 25, 10, 10])[0]
    if stage == "synthesis":
        cluster_code = random.choice(CLUSTERS)
        subgroup_code = None  # cross-cluster/cross-subgroup, no single home subgroup
    elif stage == "subgroup":
        cluster_code = random.choice(CLUSTERS)
        subgroup_code = None  # process (b)'s own cluster-wide findings, #1691 sec9 item8
    else:
        subgroup_code = random.choice(subgroup_pool)
        cluster_code = home_for_subgroup(subgroup_code)
    observations.append({
        "id": i,
        "cluster_code": cluster_code,
        "subgroup_code": subgroup_code,
        "stage": stage,
        "tag": random.choice(TAGS_BY_STAGE[stage]),
    })

obs_by_stage = {}
for o in observations:
    obs_by_stage.setdefault(o["stage"], []).append(o)

# ---- build 100 ib_node rows ---------------------------------------------------

nodes = []
node_id = 1


def new_row(obs, **kw):
    global node_id
    row = {
        "id": node_id,
        "observation_id": obs["id"],
        "cluster_code": obs["cluster_code"],
        "cluster_subgroup_code": obs["subgroup_code"],
        "strong": None,
        "verse_reference": None,
        "surface": None,
        "morph_code": None,
        "question_code": None,
        "traced_observation_id": None,
        "source_stage": obs["stage"],
        "seq": 1,
        "created_at": random.choice(CREATED_DATES),
    }
    row.update(kw)
    nodes.append(row)
    return row


TARGET = 100

# 1) reading-stage: verse-grounded citations, sometimes 2-3 strongs in one span (shared seq group)
reading_obs = obs_by_stage.get("reading", [])
for obs in reading_obs:
    if len(nodes) >= TARGET:
        break
    n_citations = random.choices([1, 1, 2, 3], weights=[50, 25, 15, 10])[0]
    verse = random.choice(HUB_VERSES if random.random() < 0.4 else VERSES)
    sg = obs["subgroup_code"]
    strongs = STRONGS_BY_SUBGROUP.get(sg, HUB_STRONGS)
    chosen = random.sample(strongs, k=min(n_citations, len(strongs)))
    # simulate span.position as the seq value for a multi-strong span citation
    positions = sorted(random.sample(range(1, 16), k=len(chosen)))
    for strong, pos in zip(chosen, positions):
        new_row(obs, strong=strong, verse_reference=verse,
                surface=random.choice(SURFACES_BY_STRONG_HINT),
                morph_code=random.choice(MORPHS), seq=pos)
    # occasional cross-family tag: also cite a second, unrelated verse
    if random.random() < 0.2 and len(nodes) < TARGET:
        other_verse = random.choice(VERSES)
        new_row(obs, strong=random.choice(HUB_STRONGS), verse_reference=other_verse,
                surface=random.choice(SURFACES_BY_STRONG_HINT),
                morph_code=random.choice(MORPHS), seq=1)

# 2) answer-stage: question-grounded, occasionally paired with the strong it answers about
answer_obs = obs_by_stage.get("answer", [])
for obs in answer_obs:
    if len(nodes) >= TARGET:
        break
    q = random.choice(QUESTIONS)
    if random.random() < 0.5:
        sg = obs["subgroup_code"]
        strong = random.choice(STRONGS_BY_SUBGROUP.get(sg, HUB_STRONGS))
        new_row(obs, question_code=q, strong=strong, seq=1)
    else:
        new_row(obs, question_code=q, seq=1)

# 3) subgroup-stage (process b): cluster-wide claims (no strong/verse) or one flagged strong
subgroup_obs = obs_by_stage.get("subgroup", [])
for obs in subgroup_obs:
    if len(nodes) >= TARGET:
        break
    if random.random() < 0.5:
        new_row(obs, seq=1)  # cluster-wide only -- cluster_code alone satisfies the CHECK
    else:
        new_row(obs, strong=random.choice(HUB_STRONGS), seq=1)

# 4) synthesis-stage: cross-cluster/cross-subgroup references + traced_observation_id edges
synthesis_obs = obs_by_stage.get("synthesis", [])
non_synthesis_ids = [o["id"] for o in observations if o["stage"] != "synthesis"]
for obs in synthesis_obs:
    if len(nodes) >= TARGET:
        break
    # references multiple clusters -- one row per cluster (2026-09-14 row-shape rule)
    touched = random.sample(CLUSTERS, k=random.choice([2, 3]))
    for i, c in enumerate(touched, start=1):
        if len(nodes) >= TARGET:
            break
        new_row(obs, cluster_code=c, cluster_subgroup_code=None, seq=i)
    # traces back to 1-3 earlier reading/answer observations it synthesizes
    for i, oid in enumerate(random.sample(non_synthesis_ids, k=min(3, len(non_synthesis_ids))),
                             start=len(touched) + 1):
        if len(nodes) >= TARGET:
            break
        new_row(obs, cluster_code=obs["cluster_code"], traced_observation_id=oid, seq=i)

# top up / trim to exactly 100 by cycling through reading observations for extra citations
while len(nodes) < TARGET:
    obs = random.choice(reading_obs or observations)
    verse = random.choice(VERSES)
    sg = obs["subgroup_code"]
    strong = random.choice(STRONGS_BY_SUBGROUP.get(sg, HUB_STRONGS))
    new_row(obs, strong=strong, verse_reference=verse,
            surface=random.choice(SURFACES_BY_STRONG_HINT),
            morph_code=random.choice(MORPHS), seq=random.randint(1, 15))

nodes = nodes[:TARGET]
for idx, row in enumerate(nodes, start=1):
    row["id"] = idx

out = {
    "_notice": "PHANTOM MOCKUP DATA -- not grounded in real results. Generated for escalation "
               "#1692 (ib_node) network-visualization prototyping, researcher request 2026-09-14. "
               "Schema matches iba/docs/1692-ib-node-finalization-v1-20260912.md sec1.",
    "_phantom_observations": observations,
    "ib_node": nodes,
}

with open("ib_node_mockup.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)

print(f"wrote {len(nodes)} ib_node rows, {len(observations)} phantom observations")
