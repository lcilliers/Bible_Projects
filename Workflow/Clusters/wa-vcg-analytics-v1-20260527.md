# VCG analytics — what's actually in the database

_Generated: 2026-05-27 07:29 UTC_  
_Source: `database/bible_research.db` — `verse_context_group` + `vcg_term` + `verse_context.group_id`_

**Purpose:** surface what the VCG layer holds across all clusters so the v3_0 decision (drop VCGs as Phase 7 design layer) can be made with full visibility of what would become legacy.

---

## §1. Cluster-level coverage

Clusters with active VCGs in the DB and their analytical state.

| Cluster | Status | # VCGs | # is_rel verses (in VCGs) | Avg V/VCG | Med V/VCG | Anchors |
|---|---|---:|---:|---:|---:|---:|
| **M01** | Analysis Completed (Terms Added) | 38 | 945 | 24.9 | 18 | 91 |
| **M02** | Analysis Completed (Terms Added) | 27 | 645 | 23.9 | 18 | 55 |
| **M03** | Analysis Completed | 25 | 690 | 27.6 | 17 | 81 |
| **M04** | Analysis Completed | 47 | 1116 | 23.7 | 16 | 73 |
| **M05** | Ready for re-analysis | 123 | 1560 | 12.7 | 6 | 127 |
| **M06** | Analysis Completed | 51 | 429 | 8.4 | 3 | 57 |
| **M07** | Analysis Completed | 28 | 359 | 12.8 | 9 | 28 |
| **M08** | Analysis Completed | 24 | 293 | 12.2 | 11 | 24 |
| **M09** | Analysis Completed | 21 | 97 | 4.6 | 4 | 21 |
| **M10** | Analysis Completed | 68 | 1320 | 19.4 | 17 | 68 |
| **M10b** | Analysis Completed | 36 | 515 | 14.3 | 12 | 42 |
| **M10c** | Analysis Completed | 26 | 263 | 10.1 | 8 | 27 |
| **M15** | Analysis Completed | 58 | 1655 | 28.5 | 19 | 55 |
| **M20** | Analysis Completed (Terms Added) | 26 | 68 | 2.6 | 2 | 26 |
| **M26** | Analysis Completed | 79 | 825 | 10.4 | 6 | 91 |
| **M39** | Analysis Completed | 34 | 718 | 21.1 | 13 | 49 |
| **M46** | Analysis Completed | 34 | 197 | 5.8 | 4 | 31 |
| **TOTAL** | — | **745** | **11,695** | — | — | **946** |

**Orphan VCGs** (active VCG row with zero active is_relevant verses): 255
- `1430-001` (vcg_id=142) — `Term names the excellent spirit as the seat of extraordinary inner character — w`
- `1430-002` (vcg_id=143) — `Term names the hardened spirit as the inner seat of pride — the spirit that stif`
- `1430-003` (vcg_id=144) — `Term names the anxious spirit as the inner reception of divine vision — the spir`
- `1586-001` (vcg_id=160) — `Term names the inner disposition of kindness toward human persons — benevolent o`
- `1589-001` (vcg_id=162) — `Term names the inner disposition of kindly consideration toward others — the ori`
- `4785-001` (vcg_id=259) — `Inner quality of bitter weeping — grief of particular intensity saturated with s`
- `4448-001` (vcg_id=271) — `Inner quality of confident boldness in apostolic communication — willingness to `
- `4011-001` (vcg_id=332) — `Term names the deep, intensely felt compassion of God as a character attribute —`
- `455-001` (vcg_id=365) — `Term names the inward parts as the seat of the innermost self — the deepest laye`
- `455-002` (vcg_id=366) — `Term names the inward parts as the seat of inner experience — the deepest place `

---

## §2. VCG size distribution

Histogram of verses per VCG. **Singleton VCGs (1 verse) are a key signal — do we create VCGs that hold just one verse?**

| Size range | # VCGs | % of total | Cumulative % |
|---|---:|---:|---:|
| 1 verse | 77 | 10.3% | 10.3% |
| 2-3 verses | 96 | 12.9% | 23.2% |
| 4-5 verses | 92 | 12.3% | 35.6% |
| 6-10 verses | 140 | 18.8% | 54.4% |
| 11-20 verses | 161 | 21.6% | 76.0% |
| 21-50 verses | 136 | 18.3% | 94.2% |
| 51-100 verses | 36 | 4.8% | 99.1% |
| 101+ verses | 7 | 0.9% | 100.0% |
| **Total** | **745** | 100% | — |

### §2.1 Singleton VCGs (77 total — each holds exactly 1 verse)

These are the most direct signal for 'VCG layer overhead without analytical density.' One verse cannot internally cluster; the VCG description is effectively a per-verse note.

| Cluster | VCG code | Description excerpt |
|---|---|---|
| M01 | `105-001` | Term names terror or dismay — the inner condition of overwhelming dread in the face of what cannot b |
| M02 | `705-002` | Bitterness as spreading inner root — deeply embedded condition that defiles and corrupts beyond the  |
| M02 | `M02-A-VCG-05` | Wrath understood as an ongoing, settled existential condition resting on those who refuse the Son —  |
| M02 | `M02-C-VCG-03` | The softest anger register — sullen, brooding, situational displeasure that withdraws and shuts down |
| M04 | `M04-P-VCG-03` | Predatory exultation — a.li.tsut as sinister inner gladness in cruelty against the poor. Inner-being |
| M05 | `1008-001` | Term names unity of inner orientation — a shared disposition of mind and spirit among the community |
| M05 | `1009-001` | Term names a tender, friendly inner disposition — the mind oriented toward others with gentleness an |
| M05 | `1402-001` | Term names shared inner disposition — genuine concern and aligned soul-orientation toward others |
| M05 | `1582-002` | Term names hospitality as requiring inner willingness without grumbling — the outer act of welcome o |
| M05 | `1588-001` | Term names friendship with the world as a disordered inner orientation constituting enmity with God  |
| M05 | `1616-001` | Term names the inner quality of compassion as a defining human characteristic — its violation by cir |
| M05 | `1641-001` | Term names doing good as the ongoing inner-being commitment maintained even in suffering — the pract |
| M05 | `1642-001` | Term names the person characterised by doing good — a moral-character designation that reflects an i |
| M05 | `3165-001` | Term names mercilessness as an inner character failure — one of the marks of those whose inner moral |
| M05 | `3980-001` | Term names sympathy as a character disposition of the inner person — the settled quality of being re |
| M05 | `430-001` | Term names the act of making peace — Christ's reconciling work that restores the broken relationship |
| M05 | `535-001` | Term names Israel as the beloved of God's soul — the most intimate inner designation, whose abandonm |
| M05 | `554-001` | Term names tender, family-like affection as the inner disposition of believers toward one another |
| M05 | `559-001` | Term names love of one's children as an inner affective disposition to be cultivated — part of the d |
| M05 | `561-001` | Term names love of one's husband as an inner affective orientation to be cultivated and trained — a  |
| M05 | `565-001` | Term names loveliness as a quality that merits and directs the inner attention of the mind in moral  |
| M05 | `566-001` | Term names love of good as an inner character disposition — required of those who lead the community |
| M05 | `567-001` | Term names love of brothers as an inner disposition among the virtues of the unified community |
| M05 | `5729-001` | Kindness as inner quality of love — outward expression of love's inner character toward others |
| M05 | `731-001` | Term names the divine compassion as an inner disposition of sovereign mercy — God's free inclination |
| M05 | `856-001` | Patient endurance of evil — the inner disposition of forbearance without resentment |
| M05 | `988-001` | Term names divine compassion as the ground of appeal — the inner-being disposition of God toward per |
| M05 | `993-001` | Term names mercilessness as the inner orientation that forfeits mercy — and mercy as the disposition |
| M06 | `1281-001` | Term names contempt as a social-inner contagion — one act of defiance spreading the inner dispositio |
| M06 | `14-001` | Term names the inner disposition of revulsion toward evil — what a person claims as morally repugnan |
| M06 | `14-002` | Term names the person whose inner moral character is itself the object of divine revulsion — charact |
| M06 | `1643-001` | Term names the inner disposition of not loving good — an inner-being orientation that characterises  |
| M06 | `1663-001` | Term (se.na) names the category of those who hate — used as a person-type designation for the king's |
| M06 | `1663-NEW-04` | Term names divine hatred directed at human persons who hate God — God's sustained inner rejection of |
| M06 | `1664-001` | Term names the state of being disfavoured or unloved — an inner relational orientation of lesser lov |
| M06 | `248-001` | Term names divine inner loathing directed specifically at pride — God abhors the arrogance of Jacob |
| M06 | `317-001` | Term names derision — the condition of being an object of mocking contempt among enemies, arising fr |
| M06 | `5519-001` | Term names the illustrating impact of an enemy — the whip / scourge metaphor for hostile domination; |
| M06 | `6968-001` | Akh.ze.riy.yut as inner quality of cruelty: disposition of merciless destructiveness |
| M06 | `7001-001` | Term names the adversary as the object of God's righteous judgment — and the inner response of the p |
| M06 | `7009-001` | A.yav as hostile disposition: enmity as relational-moral stance |
| M09 | `M09-H-VCG-02` | The distinctive register of willing-heartedness as a divine gift that must be sought and may be lost |
| M10 | `M10-L-VCG-03` | Confession without transformed will: the hollow acknowledgment |
| M15 | `523-002` | Term names understanding as a human inner-being capacity — the gift from God enabling discernment of |
| M15 | `M15-BOUNDARY-VCG01` | Jude 9: Michael contending with the devil in disputation about the body of Moses. The dialegō here i |
| M20 | `1403-001` | The fainthearted soul — the inner person diminished in courage (oligopsuchos: small-souled), requiri |
| M20 | `2078-001` | Discouragement as the inner state produced by interpersonal provocation — one person's provoking act |
| M20 | `259-002` | Anxiety as the fuel of contrition — da.ag naming the inner energy that drives genuine sorrow over si |
| M20 | `4483-001` | Term names the inner state of perplexity and bewilderment — the person at a complete loss before an  |
| M20 | `M20-A-NEW-01` | Anxiety cast onto God — the person currently carrying real anxieties commanded to transfer the weigh |
| … | … and 27 more singletons |  |

---

## §3. VCG description distinctness from parent sub-group

For each VCG: how much new analytical content does the VCG description carry over its parent sub-group's `core_description`? Measured by Jaccard token similarity (1.0 = identical token set; 0.0 = no shared tokens). **High similarity = VCG description duplicates sub-group description.**

| Jaccard similarity (VCG desc vs parent sub-group desc) | # VCGs | % |
|---|---:|---:|
| 0.0 <= j < 0.10 | 509 | 68.3% |
| 0.1 <= j < 0.20 | 196 | 26.3% |
| 0.2 <= j < 0.30 | 32 | 4.3% |
| 0.3 <= j < 0.40 | 8 | 1.1% |
| 0.4 <= j < 0.50 | 0 | 0.0% |
| 0.5 <= j < 0.70 | 0 | 0.0% |
| 0.7 <= j <= 1.0 | 0 | 0.0% |

**Average Jaccard:** 0.08. (Lower = VCG descriptions analytically distinct from sub-group; higher = VCG descriptions overlap sub-group content.)

---

## §4. Analytical-rent test — VCG citation in `cluster_finding`

For each cluster, a VCG counts as cited if either form appears in any `cluster_finding.finding_text`:
- **Full form** — the exact `group_code` (e.g. `M10c-A-VCG-07`)
- **Short form** — `VCG-NN` where NN matches the VCG's sequence number (scope-implicit reference within the finding's cluster)

The short-form is scoped per-cluster because the AI cites VCGs by sequence number relying on the finding's cluster context. A VCG may be over-credited when multiple sub-groups in the same cluster share a sequence number — but this is the correct floor measure for a citation-rate metric. **A VCG never referenced by either form paid no Phase 9 rent.**

| Cluster | # VCGs | # cited (full + short) | Citation rate | Short-form distinct |
|---|---:|---:|---:|---:|
| M01 | 38 | 38 | 100% | 7 |
| M02 | 27 | 27 | 100% | 7 |
| M03 | 25 | 25 | 100% | 5 |
| M04 | 47 | 47 | 100% | 6 |
| M05 | 123 | 0 | 0% | 0 |
| M06 | 51 | 24 | 47% | 0 |
| M07 | 28 | 28 | 100% | 5 |
| M08 | 24 | 24 | 100% | 5 |
| M09 | 21 | 21 | 100% | 5 |
| M10 | 68 | 68 | 100% | 9 |
| M10b | 36 | 36 | 100% | 11 |
| M10c | 26 | 26 | 100% | 8 |
| M15 | 58 | 4 | 7% | 12 |
| M20 | 26 | 9 | 35% | 0 |
| M26 | 79 | 61 | 77% | 0 |
| M39 | 34 | 31 | 91% | 0 |
| M46 | 34 | 3 | 9% | 0 |
| **Total** | **745** | **472** | **63%** | — |

**Interpretation:** Citation rate measures Phase 9 rent. Group A clusters (M01-M04, M07-M09) tend to mix full and short citations. Group B clusters (M10, M10b, M10c) cite predominantly short-form. Group C clusters (M06, M15, M20, M26, M39, M46) cite VCGs in neither form — their findings reference verses, sub-groups, and Strong's directly.

---

## §5. Cross-cluster VCG description token patterns

Tokens appearing in VCG descriptions across multiple clusters surface common within-sub-group axes (e.g. 'external' / 'internal' / 'volitional' / 'corporate'). Filtered to tokens with cluster-spread >= 3.

| Token | # clusters | # VCG descs |
|---|---:|---:|
| `god` | 17 | 218 |
| `toward` | 17 | 114 |
| `act` | 17 | 105 |
| `heart` | 17 | 65 |
| `relational` | 17 | 63 |
| `divine` | 16 | 163 |
| `moral` | 16 | 127 |
| `god's` | 16 | 125 |
| `will` | 16 | 68 |
| `quality` | 16 | 65 |
| `directed` | 16 | 56 |
| `orientation` | 15 | 75 |
| `condition` | 15 | 67 |
| `judgment` | 15 | 61 |
| `before` | 15 | 57 |
| `against` | 15 | 43 |
| `people` | 15 | 37 |
| `disposition` | 14 | 106 |
| `character` | 14 | 72 |
| `state` | 14 | 64 |
| `life` | 14 | 56 |
| `community` | 14 | 47 |
| `speech` | 14 | 32 |
| `human` | 13 | 65 |
| `love` | 13 | 53 |
| `persons` | 13 | 47 |
| `response` | 13 | 38 |
| `word` | 13 | 30 |
| `spiritual` | 13 | 29 |
| `communal` | 13 | 25 |

---

## §6. Per-cluster VCG inventory (compact)

Every active VCG, by cluster, with verse count and description excerpt (first 120 chars).

### M01 (38 VCGs · status: Analysis Completed (Terms Added))

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `105-001` | ? | 1 | 1 | ✓ | Term names terror or dismay — the inner condition of overwhelming dread in the face of what cannot be resisted or compre |
| `1153-001` | ? | 3 | 1 | ✓ | Sudden panic and terror as inner affliction — the state of dismay, panic, and anguish that falls upon persons, including |
| `M01-A-VCG-01` | M01-A | 32 | 2 | ✓ | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| `M01-A-VCG-02` | M01-A | 35 | 1 | ✓ | Fear of God is identified as the foundational inner orientation from which wisdom, knowledge, and genuine understanding  |
| `M01-A-VCG-03` | M01-A | 53 | 1 | ✓ | Fear of God is presented as the relational posture that aligns a person with God's saving purposes and opens them to his |
| `M01-A-VCG-04` | M01-A | 80 | 1 | ✓ | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| `M01-A-VCG-05` | M01-A | 54 | 1 | ✓ | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| `M01-A-VCG-06` | M01-A | 54 | 3 | ✓ | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| `M01-A-VCG-07` | M01-A | 25 | 2 | ✓ | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |
| `M01-B-VCG-01` | M01-A | 47 | 6 | ✓ | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| `M01-B-VCG-02` | M01-A | 23 | 3 | ✓ | The awe-struck fear produced specifically by witnessing Jesus exercise supernatural power — calming storms, healing, rai |
| `M01-B-VCG-03` | M01-A | 106 | 5 | ✓ | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| `M01-B-VCG-04` | M01-B | 21 | 1 | ✓ | The reactive inner dread specifically directed at social consequences — crowd opinion, peer pressure, public exposure, s |
| `M01-B-VCG-05` | M01-B | 25 | 1 | ✓ | Fear as the inner force that directly governs personal decision-making — driving flight, deception, or inaction when lif |
| `M01-B-VCG-06` | M01-B | 51 | 3 | ✓ | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |
| `M01-BOUNDARY-VCG-01` | M01-BOUNDARY | 18 | 7 | ✓ | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |
| `M01-C-VCG-01` | M01-C | 19 | 3 | ✓ | God deploys dread and terror ahead of Israel as an active weapon that paralyses enemy resistance before battle — an exte |
| `M01-C-VCG-02` | M01-C | 15 | 3 | ✓ | Terror characterised as an active, hunting, encircling force that overwhelms the inner person with no escape — pursuing  |
| `M01-C-VCG-03` | M01-C | 9 | 2 | ✓ | Terror as the defining power wielded by great military empires over the land of the living — projected outward as the in |
| `M01-C-VCG-04` | M01-C | 22 | 5 | ✓ | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |
| `M01-C-VCG-05` | M01-A | 10 | 2 | ✓ | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |
| `M01-D-VCG-01` | M01-B | 25 | 2 | ✓ | Dismay arising from receiving terrible news, witnessing catastrophe, or experiencing the withdrawal of God's presence —  |
| `M01-D-VCG-02` | M01-D | 14 | 1 | ✓ | Dismay inflicted by divine action as a form of judgment or punishment — God actively producing inner collapse in those w |
| `M01-D-VCG-03` | M01-D | 12 | 1 | ✓ | Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, han |
| `M01-D-VCG-04` | M01-D | 11 | 2 | ✓ | Meanings where dismay is explicitly forbidden or countered — Israel or prophets commanded not to be dismayed, with the g |
| `M01-D-VCG-05` | M01-B | 16 | 3 | ✓ | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |
| `M01-E-VCG-01` | M01-E | 15 | 2 | ✓ | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |
| `M01-E-VCG-02` | M01-A | 12 | 3 | ✓ | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |
| `M01-E-VCG-03` | M01-E | 15 | 3 | ✓ | Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities an |
| `M01-E-VCG-04` | M01-B | 39 | 4 | ✓ | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| `M01-E-VCG-05` | M01-E | 10 | 4 | ✓ | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |
| `M01-E-VCG-06` | M01-E | 7 | 1 | ✓ | NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in w |
| `M01-F-VCG-01` | M01-BOUNDARY | 9 | 2 | ✓ | Anxiety as a sustained, all-pervasive inner burden that saturates every moment and every ordinary activity — not trigger |
| `M01-F-VCG-02` | M01-F | 9 | 3 | ✓ | Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner |
| `M01-F-VCG-03` | M01-B | 10 | 1 | ✓ | Sustained dread specifically as a form of divine judgment — unrelenting, consuming anxiety that denies rest, distorts ti |
| `M01-F-VCG-04` | M01-A | 22 | 1 | ✓ | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| `M01-F-VCG-05` | M01-A | 8 | 1 | ✓ | A specific form of anticipatory dread characterised by Paul's protective apprehension about the spiritual welfare of his |
| `M01-G-VCG-01` | M01-G | 8 | 3 | ✓ | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |

### M02 (27 VCGs · status: Analysis Completed (Terms Added))

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `705-001` | ? | 3 | 1 | ✓ | Bitterness as destructive inner state — disposition of hostility, resentment, or hardness that corrupts the person and d |
| `705-002` | ? | 1 | 1 | ✓ | Bitterness as spreading inner root — deeply embedded condition that defiles and corrupts beyond the individual |
| `M02-A-VCG-01` | M02-A | 25 | 3 | ✓ | God's wrath as the settled inner disposition that grounds binding covenantal outcomes — oaths, exclusions, exile, and ir |
| `M02-A-VCG-02` | M02-A | 16 | 1 | ✓ | Wrath understood as impending future divine force from which people flee, are rescued, or are delivered. The coming wrat |
| `M02-A-VCG-03` | M02-A | 35 | 3 | ✓ | Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against i |
| `M02-A-VCG-04` | M02-A | 32 | 2 | ✓ | Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience,  |
| `M02-A-VCG-05` | M02-A | 1 | 1 | ✓ | Wrath understood as an ongoing, settled existential condition resting on those who refuse the Son — not a momentary reac |
| `M02-B-VCG-01` | M02-B | 67 | 1 | ✓ | God's burning inner heat directed against Israel's persistent covenant violation — the disciplinary fire that kindles at |
| `M02-B-VCG-02` | M02-B | 47 | 4 | ✓ | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |
| `M02-B-VCG-03` | M02-B | 21 | 2 | ✓ | Anger as a force that floods and fills the inner person — welling to full capacity, taking possession, displacing other  |
| `M02-B-VCG-04` | M02-B | 18 | 3 | ✓ | Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from |
| `M02-B-VCG-05` | M02-B | 23 | 1 | ✓ | Anger as an inner state present but requiring management and restraint — either by God whose compassion holds back wrath |
| `M02-B-VCG-06` | M02-B | 84 | 3 | ✓ | God's burning inner rage through sustained imagery of pouring, spending, and releasing — a concentrated intensity that b |
| `M02-B-VCG-07` | M02-B | 3 | 0 | ✓ | Anger understood from the perspective of the person bearing it — the inner experience of being under wrath: crushed, sat |
| `M02-BOUNDARY-VCG-01` | M02-BOUNDARY | 82 | 6 | ✓ | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |
| `M02-C-VCG-01` | M02-C | 32 | 2 | ✓ | God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored an |
| `M02-C-VCG-02` | M02-C | 3 | 3 | ✓ | Indignation in human persons as a morally revelatory inner response — the anger that proves genuine repentance (2Cor 7:1 |
| `M02-C-VCG-03` | M02-C | 1 | 1 | ✓ | The softest anger register — sullen, brooding, situational displeasure that withdraws and shuts down rather than eruptin |
| `M02-D-VCG-01` | M02-D | 47 | 1 | ✓ | The relational dynamic of human idolatry as an act that deliberately stirs God's anger — a covenant breach directed at h |
| `M02-D-VCG-02` | M02-D | 7 | 3 | ✓ | A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being character |
| `M02-D-VCG-03` | M02-D | 4 | 2 | ✓ | Anger arising spontaneously from within the inner person in response to what is encountered — not from deliberate target |
| `M02-E-VCG-01` | M02-E | 7 | 2 | ✓ | God's jealousy as a defining constitutional attribute of his being — not a reaction to offense but a fundamental identit |
| `M02-E-VCG-02` | M02-E | 32 | 1 | ✓ | God's jealousy expressed as fierce protective passion for his people, city, land, and name — firing in their defense and |
| `M02-E-VCG-03` | M02-E | 9 | 1 | ✓ | Human jealousy directed toward God — consuming zeal for his honor that identifies persons with his cause. Elijah, Phineh |
| `M02-E-VCG-04` | M02-E | 29 | 1 | ✓ | Jealousy in human persons directed at others — possessiveness, comparison-based resentment, covetous envy at another's a |
| `M02-F-VCG-01` | M02-F | 12 | 4 | ✓ | Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and q |
| `M02-F-VCG-02` | M02-F | 4 | 2 | ✓ | Anger expressed as the relational atmosphere of inner contention — strife as the condition when pride and self-will go u |

### M03 (25 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M03-A-VCG-01` | M03-A | 54 | 3 | ✓ | Weeping arising from the death of, separation from, or irrecoverable loss of a loved one — the immediate, deeply persona |
| `M03-A-VCG-02` | M03-A | 36 | 4 | ✓ | Weeping directed toward God as an expression of contrition, repentance, confession, or urgent intercession — weeping tha |
| `M03-A-VCG-03` | M03-A | 31 | 1 | ✓ | Weeping that is communal, national, or civic — the collective inner grief response to shared catastrophe, threatened des |
| `M03-A-VCG-04` | M03-A | 32 | 2 | ✓ | Weeping arising from prophetic identification — the prophet or witness who weeps on behalf of a people or nation, enteri |
| `M03-A-VCG-05` | M03-A | 17 | 2 | ✓ | Weeping that is eschatological in character — either the defining inner anguish of those under divine judgment, or the e |
| `M03-B-VCG-01` | M03-B | 40 | 3 | ✓ | Personal and communal mourning rites that accompany death — the structured, socially-recognised expression of grief at t |
| `M03-B-VCG-02` | M03-B | 33 | 1 | ✓ | Mourning arising from communal catastrophe — enemy invasion, famine, exile, national defeat, or the direct intervention  |
| `M03-B-VCG-03` | M03-B | 22 | 3 | ✓ | Mourning in which God is the active agent governing whether it occurs, is suppressed, or is transformed — mourning comma |
| `M03-B-VCG-04` | M03-B | 22 | 4 | ✓ | The mourning vocabulary distinctive to the New Testament: commanded grief over sin, mourning at Christ's departure, past |
| `M03-BOUNDARY-VCG-01` | M03-BOUNDARY | 177 | 26 | ✓ | Aggregating VCG for BOUNDARY terms — pending researcher disposition at Phase 12. Members: 28 terms spanning press/afflic |
| `M03-C-VCG-01` | M03-C | 31 | 3 | ✓ | Grief as a settled, located inner condition — sorrow felt in the soul, heart, and deepest inner being; the weight carrie |
| `M03-C-VCG-02` | M03-C | 12 | 2 | ✓ | Grief that is morally motivated and productive — sorrow arising from witnessing or experiencing moral failure, sin, or r |
| `M03-C-VCG-03` | M03-C | 3 | 1 | ✓ | The unique inner-being grief of Jesus in Gethsemane — soul-located sorrow that reaches the extreme depth of threatening  |
| `M03-D-VCG-01` | M03-D | 56 | 2 | ✓ | The dominant pattern of M03-D's corpus: distress as the inner-being crisis that drives the sufferer to cry out to God, a |
| `M03-D-VCG-02` | M03-D | 5 | 2 | ✓ | Verses that explicitly locate distress in the soul, spirit, or heart of the sufferer — the most directly inner-being evi |
| `M03-D-VCG-03` | M03-D | 12 | 1 | ✓ | Distress in its disciplinary function — distress that God uses as an instrument to press the inner will back toward hims |
| `M03-D-VCG-04` | M03-D | 26 | 1 | ✓ | Distress as a feature of prophetic announcements and oracles — the 'day of distress,' the time of trouble announced for  |
| `M03-D-VCG-05` | M03-D | 6 | 2 | ✓ | The Greek anguish vocabulary in M03-D — terms carrying the anguish register in distinctly New Testament and eschatologic |
| `M03-E-VCG-01` | M03-E | 17 | 3 | ✓ | Groaning and sighing under suffering, oppression, or devastating circumstance — the involuntary vocal expression of inne |
| `M03-E-VCG-02` | M03-E | 4 | 3 | ✓ | The theologically densest groaning texts: the Spirit's intercession in groanings too deep for words within the believer' |
| `M03-E-VCG-03` | M03-E | 10 | 1 | ✓ | The personal, individual sighing of Job and the psalmists — grief made audible as a continuous, exhausting, bodily-perva |
| `M03-F-VCG-01` | M03-F | 16 | 2 | ✓ | Pain that is defined, perceived, or held by God — pain that constitutes an identity or is acknowledged as real by the di |
| `M03-F-VCG-02` | M03-F | 12 | 2 | ✓ | Pain characterised by persistence, resistance to remedy, and its erosive effect on the inner person and the divine relat |
| `M03-F-VCG-03` | M03-F | 8 | 1 | ✓ | Pain vocabulary using the birth-pangs image (che.vel-B) to describe the acute, involuntary, sudden seizure of inner angu |
| `M03-G-VCG-01` | M03-G | 8 | 6 | ✓ | Bitterness as the specific inner quality that grief acquires at its most intense — bitterness-of-soul arising from suffe |

### M04 (47 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M04-A-VCG-01` | M04-A | 58 | 3 | ✓ | God-directed exultation: rejoicing toward YHWH as object and source. Includes God's own delight toward his people. |
| `M04-A-VCG-02` | M04-A | 18 | 3 | ✓ | Inverted, absent, or corrupt joy: rejoicing by negation — misdirected toward evil/idols/death, absent as curse, or enemi |
| `M04-A-VCG-03` | M04-A | 7 | 1 | ✓ | Relational and natural gladness: rejoicing in human bonds, parental delight, creation's personified response. |
| `M04-B-VCG-01` | M04-B | 26 | 1 | ✓ | Festival and feast worship joy: prescribed communal gladness at appointed feasts directed toward God at his sanctuary. |
| `M04-B-VCG-02` | M04-B | 22 | 1 | ✓ | Sanctuary, temple, and ark joy: gladness at the sacred presence returning, established, or worship restored. |
| `M04-B-VCG-03` | M04-B | 21 | 1 | ✓ | Coronation, national, and civic deliverance joy: corporate gladness at legitimate kingship, military victory, or reversa |
| `M04-B-VCG-04` | M04-B | 64 | 1 | ✓ | Relational, personal, and wisdom-life gladness: joy in human bonds, parental delight, domestic life, Ecclesiastes life-e |
| `M04-B-VCG-05` | M04-B | 90 | 1 | ✓ | God-directed psalmist and prophetic gladness: sa.mach/sim.chah rejoicing explicitly toward God, from his saving acts, or |
| `M04-B-VCG-06` | M04-B | 59 | 2 | ✓ | Inverted, absent, corrupt, and judgment-silenced joy: misdirected, hollow, morally condemned, or divinely removed gladne |
| `M04-C-VCG-01` | M04-C | 27 | 4 | ✓ | Synoptic and incarnation joy: gladness at the messianic arrival, kingdom signs, lost-found parables, resurrection encoun |
| `M04-C-VCG-02` | M04-C | 15 | 1 | ✓ | Johannine joy: indwelling, fullness, permanent gladness — Christ's own joy transferred to disciples, joy made complete. |
| `M04-C-VCG-03` | M04-C | 59 | 4 | ✓ | Pauline relational and community joy: gladness in gospel fellowship, pastoral bonds, co-rejoicing, mutual encouragement. |
| `M04-C-VCG-04` | M04-C | 13 | 2 | ✓ | Spirit-given, kingdom, and constant joy: joy as Spirit's fruit, kingdom constituent, constant commanded stance, eschatol |
| `M04-C-VCG-05` | M04-C | 16 | 1 | ✓ | Suffering-paradox, corrupt, and morally complex joy: commanded joy in persecution, joyful endurance, corrupt gladness of |
| `M04-C-VCG-06` | M04-C | 15 | 1 | ✓ | Pauline and heavenly thanksgiving — eucharistia/eucharistos as Godward gratitude. Thanksgiving as constitutionally locat |
| `M04-D-VCG-01` | M04-D | 8 | 2 | ✓ | Shared joy: constitutive co-rejoicing — joy sought out, invited, and completed in community. sunchairo + ched.vah Aramai |
| `M04-E-VCG-01` | M04-E | 24 | 2 | ✓ | OT restoration gladness: sa.s.von and gi.lah corpus — gladness promised as direct reversal of sorrow through God's redem |
| `M04-E-VCG-02` | M04-E | 11 | 1 | ✓ | NT eschatological and suffering-paradox exultation: agalliao — exulting beyond present circumstance, toward future glory |
| `M04-F-VCG-01` | M04-F | 4 | 2 | ✓ | Fragile cheerfulness: ba.lag and mav.li.git — desired but barely attainable inner comfort under extreme adversity. |
| `M04-G-VCG-01` | M04-G | 14 | 5 | ✓ | Law and word delight: affective pleasure in God's statutes, testimonies, commandments — Psalm 119 series anchor. |
| `M04-G-VCG-02` | M04-G | 20 | 1 | ✓ | Delight in YHWH and wisdom's relational delight: a.nog toward God, sha.a.shu.im relational cherishing, sha.a carefree sh |
| `M04-H-VCG-01` | M04-H | 28 | 1 | ✓ | Divine pleasure in the Son and sovereign will: eudokeo baptism/transfiguration + cha.phets/che.phets as God doing what h |
| `M04-H-VCG-02` | M04-H | 31 | 2 | ✓ | God's relational delight toward persons: divine pleasure as redemptive affection motivating rescue, exaltation, and merc |
| `M04-H-VCG-03` | M04-H | 106 | 2 | ✓ | Human volitional willing and personal desire: cha.phets/che.phets marking human inner willingness, longing, directed wil |
| `M04-H-VCG-04` | M04-H | 23 | 1 | ✓ | Negated, absent, and corrupt pleasure: delight withheld, misdirected toward evil, or condemned as morally culpable. |
| `M04-I-VCG-01` | M04-I | 62 | 3 | ✓ | Wonder at God's marvellous works: proclaimed, remembered, thanked — the dominant register of M04-I. |
| `M04-I-VCG-02` | M04-I | 13 | 1 | ✓ | Wonder as incomprehensibility: too-difficult, beyond-reach, impossible barrier — human cognitive limits and affirmation  |
| `M04-I-VCG-03` | M04-I | 10 | 1 | ✓ | Wonder inverted: dark astonishment, dread, and appalling shock — extraordinary vocabulary producing horror rather than j |
| `M04-J-VCG-01` | M04-J | 9 | 1 | ✓ | Divine pleasantness and worship pleasantness: no.am/na.im as attribute of God's character, covenant favour, and the agre |
| `M04-J-VCG-02` | M04-J | 20 | 4 | ✓ | Pleasantness of persons, speech, wisdom, and human bonds: experiential quality of what is agreeable in relationships and |
| `M04-K-VCG-01` | M04-K | 38 | 1 | ✓ | Sacrificial pleasing aroma (ni.cho.ach) — the dominant righteous-worship register. God's receptive inner satisfaction at |
| `M04-K-VCG-02` | M04-K | 8 | 1 | ✓ | Sensory luxury and pampered ease (a.nog, ta.a.nug, a.las) — the refined-comfort inner register, ranging from genuine dom |
| `M04-K-VCG-03` | M04-K | 17 | 1 | ✓ | Wisdom better-than comparatives involving material goods — tov used in wisdom-literature paradigms where a modest materi |
| `M04-L-VCG-01` | M04-L | 32 | 1 | ✓ | Divine character goodness — 'the Lord is good' / ki-tov declarations and the Gen 1 creation appraisals ('God saw that it |
| `M04-L-VCG-02` | M04-L | 45 | 1 | ✓ | Moral-evaluative appraisal of persons and actions — tov as the inner-being faculty by which conduct, character, and choi |
| `M04-L-VCG-03` | M04-L | 5 | 1 | ✓ | Wisdom's surpassing worth — wisdom evaluated as better than gold, silver, or jewels. The inner-being faculty by which wi |
| `M04-M-VCG-01` | M04-M | 2 | 1 | ✓ | Sacrificial-obedience pleasing aroma — ni.cho.ach in righteous cultic worship. The pleasing aroma rising as the inner-be |
| `M04-M-VCG-02` | M04-M | 14 | 1 | ✓ | Doing what is good and right in God's sight — obedient inner orientation as covenantal-good. Tov as the term for the sou |
| `M04-N-VCG-01` | M04-N | 2 | 1 | ✓ | Horizontal relational pleasantness — parental attachment and the value of near neighbour. Inner-being-in-relationship: p |
| `M04-N-VCG-02` | M04-N | 2 | 1 | ✓ | Captivating marvel at a powerful entity — beast-wonder as dangerous horizontal captivation. The collective awe drawn out |
| `M04-O-VCG-01` | M04-O | 9 | 1 | ✓ | Good news and the refreshing word — the soul's response to speech, message, or news received as good. Inner-being-as-cir |
| `M04-O-VCG-02` | M04-O | 16 | 1 | ✓ | Better-than comparatives — the soul's comparative assessment of circumstances. Tov used to name a preferred circumstance |
| `M04-O-VCG-03` | M04-O | 13 | 1 | ✓ | Wellbeing as flourishing — the experienced state of goodness in body, kingdom, or covenant context. Inner-being content  |
| `M04-O-VCG-04` | M04-O | 12 | 1 | ✓ | God's good hand and covenantal promise-goodness; makarismos blessedness. The inner-being state of being under sustained  |
| `M04-P-VCG-01` | M04-P | 3 | 1 | ✓ | Misdirected sacrificial delight — ni.cho.ach aroma directed to idols rather than YHWH. The pleasing-aroma worship-act wi |
| `M04-P-VCG-02` | M04-K | 4 | 1 | ✓ | Lustful captivation — che.med craving directed toward foreign military splendour. Inner-being-as-illicit-desire that dri |
| `M04-P-VCG-03` | M04-P | 1 | 1 | ✓ | Predatory exultation — a.li.tsut as sinister inner gladness in cruelty against the poor. Inner-being-as-corrupt-rejoicin |

### M05 (123 VCGs · status: Ready for re-analysis)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1008-001` | M05-G | 1 | 1 | — | Term names unity of inner orientation — a shared disposition of mind and spirit among the community |
| `1009-001` | M05-A | 1 | 1 | — | Term names a tender, friendly inner disposition — the mind oriented toward others with gentleness and courtesy |
| `1093-001` | M05-G | 4 | 1 | — | Term names reconciliation as the inner-relational restoration of broken relationship between God and humanity — the endi |
| `1187-001` | M05-D | 2 | 1 | — | Inner intention directed toward what is honourable — the inner purposing and aiming toward honourable conduct before God |
| `1290-001` | M05-F | 9 | 1 | — | Term names comfort as God's gift in affliction — the divine consolation that flows through shared suffering and enables  |
| `1290-002` | M05-F | 12 | 1 | — | Term names encouragement as the inner orientation toward hope — the exhortation that calls believers to endurance, the S |
| `1290-003` | M05-F | 7 | 1 | — | Term names encouragement as the inner-community act — the mutual comfort of believers that refreshes hearts, the prophet |
| `1292-001` | M05-F | 5 | 1 | — | Term names consolation as God's gift that cheers the soul amid inner anxiety — the divine presence that offers what no h |
| `1354-001` | M05-BOUNDARY | 7 | 1 | — | Term names the act of demonstrating — the inner being engaged as source or recipient of what is shown: love, earnestness |
| `1402-001` | M05-G | 1 | 1 | — | Term names shared inner disposition — genuine concern and aligned soul-orientation toward others |
| `1579-001` | M05-A | 27 | 1 | — | Term names friendship as a relational bond grounded in inner knowledge, mutual self-giving, and shared life with Christ  |
| `1580-001` | M05-BOUNDARY | 7 | 1 | — | Term names the kiss as the outward expression of an inner relational reality — betrayal, absent love exposed, or holy co |
| `1581-001` | M05-BOUNDARY | 6 | 1 | — | Term names the kiss as physical expression of an inner state — love and grief, contrition and gratitude, betrayal, or jo |
| `1582-001` | M05-A | 2 | 1 | — | Term names hospitality as a leadership character requirement — the inner disposition of welcome as essential qualificati |
| `1582-002` | M05-A | 1 | 1 | — | Term names hospitality as requiring inner willingness without grumbling — the outer act of welcome only genuine when acc |
| `1585-001` | M05-A | 2 | 1 | — | Term names the practice of love for strangers as an inner disposition expressed in conduct — hospitality as a concrete e |
| `1588-001` | M05-A | 1 | 1 | — | Term names friendship with the world as a disordered inner orientation constituting enmity with God — the inward allegia |
| `1600-001` | M05-A | 13 | 1 | — | Term names the loyal friend whose inner orientation of faithfulness transcends social convention — set against flattery, |
| `1614-001` | M05-B | 13 | 1 | — | Term names God's compassion as a defining inner attribute — the divine disposition of tender mercy toward the afflicted  |
| `1616-001` | M05-B | 1 | 1 | — | Term names the inner quality of compassion as a defining human characteristic — its violation by circumstances of extrem |
| `1623-001` | M05-A | 3 | 1 | — | Term names the trusted friend whose inner loyalty shapes courageous action — Hushai's friendship with David as the groun |
| `1633-001` | ? | 99 | 3 | — | Term names God's steadfast love as the defining inner character of his covenantal disposition toward his people — the lo |
| `1633-002` | ? | 39 | 3 | — | Term names the human inner disposition of covenantal loyalty and loving-kindness — the settled character quality of fait |
| `1633-003` | ? | 24 | 2 | — | Term describes the human appeal to and meditation on God's steadfast love as a sustaining inner orientation — the soul's |
| `1635-001` | M05-A | 2 | 1 | — | Term names the responsive quality of inner covenantal mercy — the faithfulness of character that draws out corresponding |
| `1638-001` | M05-D | 8 | 1 | — | Term names the doing of good as the inner-being disposition and practice that characterises those who belong to God — ex |
| `1640-001` | M05-D | 2 | 1 | — | Term names the doing of good as an inner-being orientation — both as God's generous provision that satisfies the human h |
| `1641-001` | M05-D | 1 | 1 | — | Term names doing good as the ongoing inner-being commitment maintained even in suffering — the practice that accompanies |
| `1642-001` | M05-D | 1 | 1 | — | Term names the person characterised by doing good — a moral-character designation that reflects an inner orientation vis |
| `188-001` | M05-E | 2 | 1 | — | Term names gentleness/condescension as an inner quality — either God's toward the person, or the king's inner dispositio |
| `189-001` | M05-E | 5 | 1 | — | Term names humility/meekness as an inner quality — the disposition of the person before God and others that precedes hon |
| `2192-001` | M05-B | 2 | 1 | — | Term names divine compassion as the inward movement of mercy that acts on behalf of those in need, despite their unworth |
| `3158-001` | M05-B | 2 | 1 | — | Term names compassion as the inner character of God and the standard for human inner disposition — to be merciful as God |
| `3164-001` | M05-C | 2 | 1 | — | Term names mercifulness as an inner character quality — the blessed disposition of those who show mercy and the defining |
| `3165-001` | M05-C | 1 | 1 | — | Term names mercilessness as an inner character failure — one of the marks of those whose inner moral fabric has collapse |
| `3168-001` | M05-C | 2 | 1 | — | Term names the pitiable inner condition — the state of the person who is spiritually destitute, whether through false co |
| `3182-001` | M05-B | 8 | 1 | — | Term describes pity and compassion as an inner disposition that moves toward or spares those in need — whether in a pers |
| `3182-002` | M05-B | 16 | 1 | — | Term names the withholding of pity as a judicial inner disposition — the inner setting aside of compassionate impulse in |
| `338-001` | ? | 3 | 1 | — | Term names the act of shaming another — the imposition of social-inner disgrace as a consequence of exposed wrongdoing |
| `3980-001` | M05-B | 1 | 1 | — | Term names sympathy as a character disposition of the inner person — the settled quality of being responsive to the suff |
| `430-001` | M05-BOUNDARY | 1 | 1 | — | Term names the act of making peace — Christ's reconciling work that restores the broken relationship between humanity an |
| `445-001` | M05-F | 41 | 1 | — | Term names the human act of comforting — bringing relief to inner grief through presence, words, or care |
| `445-002` | M05-F | 26 | 1 | — | Term names divine comfort — God actively bringing relief and restoration to the inner grief of his people |
| `46-001` | M05-E | 4 | 1 | — | Term names gentleness/meekness as an inner quality of the person — a settled inner disposition of mildness and strength- |
| `47-001` | M05-E | 4 | 1 | — | Term names gentleness as an inner quality — the disposition that governs the reception of God's word, the exercise of wi |
| `487-001-a` | M05-B | 5 | 1 | — | Term names human compassion as the inner disposition of pity that moves toward and spares those in need — whether a chil |
| `487-001-b` | M05-B | 11 | 1 | — | Term names compassion toward commanded-destruction targets as disobedience — where the inner disposition of pity violate |
| `487-002` | M05-B | 21 | 1 | — | Term names divine compassion or its withholding — God's inner disposition of pity or mercy toward his people, and its wi |
| `510-001` | M05-F | 13 | 1 | — | Term names the comfort directed toward the afflicted inner being — the act of comforting another in suffering, grief, or |
| `510-002` | M05-F | 37 | 1 | — | Term names the urgent plea or earnest appeal arising from inner need, urgency, or desperation — the inner state of the p |
| `510-003-a` | M05-F | 54 | 1 | — | Term names the pastoral or apostolic appeal — the inner relational care and authority of the one urging another toward f |
| `510-003-b` | M05-F | 15 | 1 | — | Term names the social or interpersonal request — inviting, urging, asking someone to do or refrain from something in the |
| `535-001` | M05-A | 1 | 1 | — | Term names Israel as the beloved of God's soul — the most intimate inner designation, whose abandonment into enemy hands |
| `536-001` | M05-A | 67 | 0 | — | Term names God's steadfast love as his defining inner attribute — the covenantal faithfulness that never ceases, extends |
| `536-001-a` | M05-A | 59 | 1 | — | God's chesed as his eternal declared attribute — the covenantal faithfulness that never ceases, is proclaimed in the div |
| `536-001-b` | M05-A | 56 | 1 | — | God's chesed enacted in specific historical acts toward individuals and toward Israel — the covenantal faithfulness made |
| `536-002` | M05-A | 43 | 1 | — | Term names human expressions of covenantal loyalty and kindness — the inner disposition of faithfulness between persons  |
| `536-003` | M05-A | 12 | 1 | — | Term names the failure or withdrawal of chesed — its absence as the condition of moral and spiritual ruin; also the pass |
| `5367-001` | M05-G | 7 | 1 | — | Inner-spiritual participation — the disposition of the person as sharer in divine nature, suffering, comfort, or cultic  |
| `5367-002` | M05-G | 3 | 1 | — | Moral alignment through participation — the inner orientation that places a person in solidarity with righteousness or c |
| `537-001` | M05-A | 8 | 1 | — | Term names God's love for his people — the covenantal inner disposition of steadfast love that persists through and exce |
| `537-002` | M05-A | 26 | 1 | — | Term names the intense mutual love between persons — including Jonathan's love for David and the burning love of the Son |
| `537-003` | M05-A | 11 | 1 | — | Term names love as moral loyalty and kindness — the inner orientation of faithfulness between persons that mirrors divin |
| `539-001` | M05-A | 2 | 1 | — | Term names the lover — either as the rightful object of marital delight, or the hired substitute marking spiritual infid |
| `540-001` | M05-A | 33 | 1 | — | Term names the godly or pious person — one whose inner character is shaped by covenantal faithfulness toward God, set ap |
| `5425-001` | M05-E | 5 | 1 | — | Term names the inner disposition of gentleness and reasonableness — a character quality that avoids quarrelling and forc |
| `544-001` | M05-B | 39 | 1 | — | Term names God's compassion as the deep inner movement of mercy — his mother-like tenderness toward those who suffer, hi |
| `547-001` | M05-BOUNDARY | 14 | 1 | — | Term names what is fitting, lovely, or becoming — expressing the inner sense of rightness and beauty that governs aesthe |
| `551-001` | M05-B | 43 | 1 | — | Term names the divine act of compassion — God's inner movement of mercy and pity toward his people, especially in restor |
| `554-001` | M05-A | 1 | 1 | — | Term names tender, family-like affection as the inner disposition of believers toward one another |
| `556-001` | M05-A | 2 | 1 | — | Term names God's loving kindness toward humanity as an inner divine disposition made manifest — the benevolent character |
| `558-001` | M05-A | 5 | 1 | — | Term names brotherly love as the inner-relational disposition that binds the community of faith — to be cultivated, cont |
| `559-001` | M05-A | 1 | 1 | — | Term names love of one's children as an inner affective disposition to be cultivated — part of the domestic virtue forma |
| `561-001` | M05-A | 1 | 1 | — | Term names love of one's husband as an inner affective orientation to be cultivated and trained — a domestic virtue shap |
| `562-001` | M05-A | 35 | 1 | — | Term names God's love as the inner source and ground of all love — poured into hearts, demonstrated in Christ's death, i |
| `562-002` | M05-A | 42 | 1 | — | Term names love as the defining inner virtue of the believer — the fruit of the Spirit, the greatest commandment, the fu |
| `562-003` | M05-A | 28 | 1 | — | Term names mutual love among believers as the communal inner orientation — the mark of discipleship, the bond of the com |
| `565-001` | M05-BOUNDARY | 1 | 1 | — | Term names loveliness as a quality that merits and directs the inner attention of the mind in moral reflection |
| `566-001` | M05-A | 1 | 1 | — | Term names love of good as an inner character disposition — required of those who lead the community of faith |
| `567-001` | M05-A | 1 | 1 | — | Term names love of brothers as an inner disposition among the virtues of the unified community |
| `569-001` | M05-BOUNDARY | 2 | 1 | — | Term names freedom from love of money as an inner character quality — required of leaders and urged for all believers |
| `571-001` | M05-A | 21 | 1 | — | Term names love of God or Christ as the fundamental inner orientation of the person — the love commanded of the whole he |
| `571-002` | M05-A | 31 | 1 | — | Term names God's or Christ's love toward the person — the divine inner act of love that precedes and enables all human l |
| `571-003` | M05-A | 17 | 1 | — | Term names love of neighbour and enemy — the inner-being orientation outward that fulfils the law |
| `571-004` | M05-A | 53 | 1 | — | Term names mutual love among believers and within marriage — the inner relational orientation that marks discipleship an |
| `571-005` | M05-A | 8 | 1 | — | Term names disordered love — love directed toward the world, darkness, money, or self-glory as the defining inner orient |
| `572-001` | M05-A | 10 | 1 | — | Term names natural affection or friendship-love between persons — including Christ's love for his friends and the relati |
| `572-002` | M05-A | 6 | 1 | — | Term names the ranking of inner loves and loyalties — the cost of placing love of Christ above natural affection, and th |
| `572-003` | M05-A | 5 | 1 | — | Term names Peter's confession of natural love — the Joh 21 dialogue where fileo names the warmth Peter can affirm when a |
| `5729-001` | M05-D | 1 | 1 | — | Kindness as inner quality of love — outward expression of love's inner character toward others |
| `575-001` | M05-BOUNDARY | 13 | 1 | — | Term names the bosom as the seat of intimate trusted relationship — the close inner circle of family and friendship |
| `575-002` | M05-BOUNDARY | 21 | 1 | — | Term names the bosom as the place of cherishing — what the inner person holds closest |
| `587-001` | M05-F | 5 | 1 | — | Term names the act of captivating or encouraging the heart — the inner person stirred through intimate encounter |
| `593-001` | M05-B | 2 | 1 | — | Term names the inner quality of compassion — the tender-hearted disposition marked by kindness and mercy |
| `6209-001` | M05-BOUNDARY | 11 | 1 | — | Term names the solemn assembly as a collective inner-being occasion — the community gathered for worship and covenant re |
| `6845-001` | M05-BOUNDARY | 3 | 1 | — | Term names God's granting of all things needed for inner transformation — life, godliness, participation in the divine n |
| `7064-001` | M05-G | 7 | 1 | — | Epoikodomeō as process of inner-being formation and edification |
| `730-001` | M05-B | 12 | 1 | — | Term names the visceral, inward movement of compassion — the inner person being deeply stirred and moved toward one who  |
| `731-001` | M05-B | 1 | 1 | — | Term names the divine compassion as an inner disposition of sovereign mercy — God's free inclination toward the objects  |
| `734-001` | M05-B | 2 | 1 | — | Term names the inner capacity for fellow-feeling — the disposition to enter into and share the experience of another's s |
| `810-001` | M05-D | 4 | 1 | — | Term names the inner quality of singleness and sincerity — the undivided, transparent orientation of the heart toward Go |
| `810-002` | M05-D | 4 | 1 | — | Term names the inner disposition of generosity — the openhanded orientation of the person that overflows in giving; givi |
| `856-001` | M05-E | 1 | 1 | — | Patient endurance of evil — the inner disposition of forbearance without resentment |
| `873-001` | M05-G | 9 | 1 | — | Vertical fellowship with God — the inner-relational participation in divine nature, the Son, and the Spirit that constit |
| `873-002` | M05-G | 12 | 1 | — | Horizontal fellowship among believers — the inner-relational bond of mutual belonging, shared commitment, and generous p |
| `881-001` | M05-D | 6 | 1 | — | Term names goodness as the exclusive and defining attribute of God's inner being — the standard by which all human goodn |
| `881-002` | M05-D | 30 | 1 | — | Term names goodness as the inner character quality of the person — the good heart, good conscience, good treasure — from |
| `881-003` | M05-D | 39 | 1 | — | Term names goodness as the inner moral orientation and activity that God commands and will judge — doing good, pursuing  |
| `881-004` | M05-D | 11 | 1 | — | Term names goodness as the eschatological and providential good that God works for and toward — the good things to come, |
| `881-005` | M05-D | 4 | 1 | — | Term names the inner conflict between the person's desire for good and their inability to perform it — the good I want b |
| `882-001` | M05-E | 7 | 1 | — | Term names meekness/gentleness as an inner-being disposition of the renewed person — the strength that yields without fo |
| `883-001` | M05-E | 2 | 1 | — | Term names the inner disposition of gracious, reasonable fairness — the gentleness that is willing to yield to the reaso |
| `886-001` | M05-D | 3 | 1 | — | Term names kindness as God's inner disposition of generous goodwill toward humanity — the divine attribute that leads to |
| `886-002` | M05-D | 4 | 1 | — | Term names kindness as a Spirit-produced inner quality of the believer — the disposition to act with goodness toward oth |
| `954-001` | M05-D | 6 | 1 | — | Goodness/kindness as inner quality of God or persons — disposition of gracious favour expressed toward others |
| `981-001` | M05-C | 12 | 1 | — | Term names the act of divine mercy — God having mercy on whom he wills as the ground of salvation and sovereign grace |
| `981-002` | M05-C | 12 | 1 | — | Term names the cry for mercy — the supplicant's inner anguish and hope directed toward Jesus as healer and Saviour |
| `981-003` | M05-C | 5 | 1 | — | Term names the human act of mercy as the inner disposition that receives mercy in return |
| `983-001` | M05-C | 14 | 1 | — | Term names God's mercy as his defining inner attribute — the ground of salvation, the content of covenant faithfulness,  |
| `983-002` | M05-C | 13 | 1 | — | Term names mercy as the inner-being virtue and judicial reality — what God desires above ritual, what the wise show, wha |
| `988-001` | M05-B | 1 | 1 | — | Term names divine compassion as the ground of appeal — the inner-being disposition of God toward persons in extremity |
| `992-001` | M05-B | 5 | 1 | — | Term names the compassions of God as his defining inner character — the mercies that motivate holy living and compassion |
| `993-001` | M05-C | 1 | 1 | — | Term names mercilessness as the inner orientation that forfeits mercy — and mercy as the disposition that triumphs over  |

### M06 (51 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1275-001` | M06-G | 3 | 2 | — | Term names malice as an inner disposition of the soul — the soul's rejoicing in another's destruction, driven by deep-se |
| `1277-001` | M06-B | 3 | 1 | ✓ | Term names the contempt of surrounding nations toward Israel — and God's judgment that removes and avenges that contempt |
| `1280-001` | M06-B | 13 | 2 | ✓ | Term names despising as an inner act with moral and covenantal consequence — directed at birthright, God's word, God's n |
| `1281-001` | M06-B | 1 | 1 | ✓ | Term names contempt as a social-inner contagion — one act of defiance spreading the inner disposition of contempt throug |
| `1283-001` | M06-C | 2 | 2 | ✓ | Term names abhorrence and everlasting contempt as the ultimate inner-being condition of those who rebel against God — th |
| `14-001` | M06-C | 1 | 1 | — | Term names the inner disposition of revulsion toward evil — what a person claims as morally repugnant, whether genuinely |
| `14-002` | M06-C | 1 | 1 | ✓ | Term names the person whose inner moral character is itself the object of divine revulsion — character as abhorrent in G |
| `1567-001` | M06-B | 3 | 1 | ✓ | Term names blasphemous contempt as the inner disposition of rebellion — the speech-act of reviling that reveals the hear |
| `1568-001` | M06-E | 2 | 1 | — | Term names disgrace as an inner condition in extremity — the shame-experience accompanying crisis that overwhelms all ca |
| `1643-001` | BOUNDARY | 1 | 1 | — | Term names the inner disposition of not loving good — an inner-being orientation that characterises the person given ove |
| `1663-001` | M06-A | 1 | 1 | — | Term (se.na) names the category of those who hate — used as a person-type designation for the king's enemies, treating h |
| `1663-NEW-04` | M06-A | 1 | 0 | — | Term names divine hatred directed at human persons who hate God — God's sustained inner rejection of those who reject hi |
| `1664-001` | M06-E | 1 | 1 | ✓ | Term names the state of being disfavoured or unloved — an inner relational orientation of lesser love or active disfavou |
| `172-001` | M06-B | 19 | 1 | ✓ | Term names contempt as the inner disposition of treating what is sacred as beneath regard — the spurning of God, his wor |
| `172-002` | M06-B | 4 | 1 | ✓ | Term names contempt directed at reproof — the inner rejection of correction that closes the person to growth and repenta |
| `172-003` | M06-B | 2 | 1 | ✓ | Term names the inner speech of contempt — what the wicked person says in his heart as the location of his dismissal of G |
| `1775-001` | M06-D | 7 | 1 | ✓ | Ruthlessness as inner moral character — the disposition of those who do not set God before themselves |
| `1775-002` | M06-D | 13 | 1 | ✓ | The ruthless as oppressor — the inner experience of being under ruthless domination and longing for deliverance |
| `247-001` | M06-C | 2 | 1 | ✓ | Term names the objects of idolatrous inner devotion — the detestable things toward which misdirected worship is oriented |
| `247-002` | M06-C | 2 | 0 | — | Term names the commanded inner reaction or response of detestation — the worshipper's required inner-being orientation o |
| `248-001` | M06-C | 1 | 1 | ✓ | Term names divine inner loathing directed specifically at pride — God abhors the arrogance of Jacob |
| `252-001` | M06-C | 5 | 1 | ✓ | Term names the deep inner disposition of abhorrence toward falsehood and evil — the morally alert person's visceral revu |
| `252-002` | M06-C | 4 | 1 | ✓ | Term names the inverted disposition of abhorrence — the capacity for moral revulsion directed against justice and truth  |
| `252-003` | M06-C | 9 | 1 | ✓ | Term names divine sustained inner abhorrence toward those who have persistently corrupted themselves or violated covenan |
| `316-001` | M06-B | 11 | 1 | ✓ | Term names contempt as an inner attitude of disregard — held toward others from pride or comfortable indifference, or ex |
| `317-001` | M06-E | 1 | 1 | — | Term names derision — the condition of being an object of mocking contempt among enemies, arising from moral-spiritual f |
| `3200-001` | M06-F | 4 | 2 | — | Term names the adversary in legal or spiritual contest — the opposition that calls forth inner urgency, persistence, or  |
| `322-001` | M06-E | 27 | 2 | ✓ | Term names reproach as an inner-social condition experienced by individuals — the felt shame of being despised, scorned, |
| `322-002` | M06-E | 45 | 2 | ✓ | Term names reproach as a corporate-communal condition imposed upon God's people as divine judgment or national disgrace  |
| `337-001` | M06-E | 5 | 1 | — | Term names mistreatment that violates inner-relational dignity — the experience of shame through insolent treatment, end |
| `339-001` | BOUNDARY | 21 | 1 | — | Term names the act of taunting or reviling as an expression of contempt, defiance, or hostility directed at persons — th |
| `339-002` | BOUNDARY | 17 | 2 | — | Term names the act of taunting or defying God — expressing an inner orientation of contempt and arrogance toward the div |
| `5179-001` | M06-F | 3 | 1 | — | The adversary relationship as context of inner appeal and conflict |
| `550-001` | M06-A | 88 | 1 | — | Term names hatred as the sustained inner disposition of one person turned against another — the relational form of hatre |
| `550-002` | M06-A | 4 | 1 | — | Term underlies the concept of "enemy" or "foe" — the one who hates functions as the adversary, with the inner-being disp |
| `550-NEW-01` | M06-A | 9 | 1 | ✓ | Term names hatred as the legally and relationally consequential state of one spouse being disfavoured by another — the h |
| `550-NEW-02` | M06-A | 21 | 1 | ✓ | Term names hatred as the commanded inner orientation of the righteous person toward evil, falsehood, and that which is m |
| `550-NEW-03` | M06-A | 19 | 1 | — | Term names divine hatred directed at specific sins, practices, objects, or moral qualities — God's inner disposition of  |
| `550-NEW-04` | M06-A | 14 | 1 | — | Term names divine hatred directed at human persons who hate God — God's sustained inner rejection of those who reject hi |
| `5518-001` | M06-A | 6 | 1 | — | Term names a settled inner hostile disposition — persistent hatred or grudge-bearing directed toward another person, dri |
| `5519-001` | BOUNDARY | 1 | 0 | — | Term names the illustrating impact of an enemy — the whip / scourge metaphor for hostile domination; the term is also us |
| `6966-001` | M06-D | 8 | 2 | ✓ | Akh.za.ri as inner-being quality of cruelty characterising persons and nations |
| `6967-001` | M06-D | 2 | 2 | ✓ | Akh.zar as inner-being disposition of cruelty |
| `6968-001` | M06-D | 1 | 1 | — | Akh.ze.riy.yut as inner quality of cruelty: disposition of merciless destructiveness |
| `7001-001` | M06-F | 1 | 1 | — | Term names the adversary as the object of God's righteous judgment — and the inner response of the person whose enemy is |
| `7009-001` | M06-F | 1 | 1 | — | A.yav as hostile disposition: enmity as relational-moral stance |
| `90-001` | BOUNDARY | 8 | 1 | — | Term names the odium-quality of inner moral failure — the stench-metaphor expressing how wickedness and folly produce co |
| `902-001` | M06-A | 5 | 1 | — | Term names hatred as the noun-form of the inner state — the quality or condition of hatred as it subsists in a person or |
| `902-002` | M06-A | 2 | 1 | — | Term names hatred as an attributed inner disposition of God toward a people — projected or perceived divine enmity used  |
| `902-003` | M06-A | 2 | 1 | — | Term names hatred as a fundamental inner human capacity — listed alongside love and envy as constitutive orientations of |
| `903-001` | M06-A | 2 | 1 | — | Term (mas.te.mah) names hatred as the accumulated inner climate of hostility — the settled hostile atmosphere of a commu |

### M07 (28 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M07-A-VCG-01` | M07-A | 33 | 1 | ✓ | Shame as unjust wound from aggression, circumstance, and loss. Verses where shame operates as an undeserved inner wound  |
| `M07-A-VCG-02` | M07-A | 8 | 1 | ✓ | Shame from disappointed trust in human powers. Verses where shame arises from misplaced reliance on human allies or eart |
| `M07-A-VCG-03` | M07-A | 5 | 1 | ✓ | Shame borne for God's sake and by the righteous sufferer. Verses where shame is consciously carried by the innocent or r |
| `M07-A-VCG-04` | M07-A | 11 | 1 | ✓ | Shame promised removal and transformation. Verses where God explicitly promises to remove, forget, or transform the sham |
| `M07-A-VCG-05` | M07-A | 6 | 1 | ✓ | Shame averted by trust, hope, and divine protection. Verses where shame is the present inner threat and trust in God is  |
| `M07-B-VCG-01` | M07-B | 39 | 1 | ✓ | Shame invoked on enemies as just reversal of their hostility. Verses where the psalmist or community calls shame upon en |
| `M07-B-VCG-02` | M07-B | 22 | 1 | ✓ | Shame from idolatry and false religious trust. Verses where shame falls as the direct consequence of idolatry, false wor |
| `M07-B-VCG-03` | M07-B | 32 | 1 | ✓ | Shame as natural fruit of personal and relational moral failure. Verses where shame is the direct, natural consequence o |
| `M07-B-VCG-04` | M07-B | 8 | 1 | ✓ | Absence of shame: the seared conscience and moral collapse. Verses evidencing the loss of the capacity for shame — those |
| `M07-B-VCG-05` | M07-B | 10 | 1 | ✓ | Corrective shame: blameless conduct, communal discipline, and shame as moral prod. Verses where shame is deployed instru |
| `M07-C-VCG-01` | M07-C | 19 | 1 | ✓ | Guilt-shame before the holy: the face that cannot be lifted. Verses where shame arises from guilt-consciousness before G |
| `M07-C-VCG-02` | M07-C | 16 | 1 | ✓ | Trust in God as shield against shame: refuge and word. Verses where taking refuge in God, holding to his testimonies, wa |
| `M07-C-VCG-03` | M07-C | 9 | 1 | ✓ | Corrective shame awakening conscience toward God. Verses where shame is deployed as an inward corrective force in the ve |
| `M07-C-VCG-04` | M07-C | 6 | 1 | ✓ | Promise: never put to shame in God's presence. Verses where the covenant or eschatological promise of not being put to s |
| `M07-D-VCG-01` | M07-D | 20 | 1 | ✓ | Social and bodily humiliation: enforced downward movement in human community. Verses where humiliation operates through  |
| `M07-D-VCG-02` | M07-D | 20 | 1 | ✓ | Military defeat and national collapse as humiliation. Verses where humiliation comes through military defeat, the collap |
| `M07-D-VCG-03` | M07-D | 27 | 1 | ✓ | Divine abasement of pride: God bringing the lofty low. Verses where humiliation is the direct, sovereign act of God agai |
| `M07-D-VCG-04` | M07-D | 5 | 1 | ✓ | Shame carried into death and as enduring burden. Verses where humiliation is permanent — warriors descending to the pit  |
| `M07-E-VCG-01` | M07-E | 9 | 1 | ✓ | Active dishonour: refusing or withdrawing due regard toward persons. Verses where dishonour is actively enacted through  |
| `M07-E-VCG-02` | M07-E | 6 | 1 | ✓ | Assigned or structural dishonour: standing, nature, and received treatment. Verses where dishonour is assigned, structur |
| `M07-F-VCG-01` | M07-F | 10 | 1 | ✓ | Shameful conduct and objects: the moral quality of what is shameful. Verses where conscience identifies conduct, speech, |
| `M07-F-VCG-02` | M07-F | 3 | 1 | ✓ | Indecent desires and moral disorder: disordered inner appetite. Verses where the shameful characteristic is located in d |
| `M07-F-VCG-03` | M07-F | 3 | 1 | ✓ | Inverted conscience: glorying in shame and the perverted evaluative faculty. Verses where the moral-evaluation apparatus |
| `M07-G-VCG-01` | M07-G | 13 | 1 | ✓ | Dismissive contempt as inner attitude: treating persons as of no account. Verses where the contempt-producing-shame mech |
| `M07-G-VCG-02` | M07-G | 6 | 1 | ✓ | Active contempt expressed through violence, mockery, and rejection. Verses where contempt is enacted through physical vi |
| `M07-G-VCG-03` | M07-G | 5 | 1 | ✓ | Verbal contempt and reputation attack as shaming mechanism. Verses where shame is produced through speech — verbal attac |
| `M07-H-VCG-01` | M07-H | 4 | 1 | ✓ | Innocence as active inner defence: clean conscience before God and persons. Verses where innocence — the integrity of wi |
| `M07-H-VCG-02` | M07-H | 4 | 1 | ✓ | Innocence questioned and incapacity for innocence. Verses where the innocence-shame polarity is evidenced through the qu |

### M08 (24 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M08-A1-VCG-01` | M08-A1 | 6 | 1 | ✓ | Prosperity-Induced Heart-Elevation — pride as the heart lifted up by material satisfaction, success, or divine blessing; |
| `M08-A1-VCG-02` | M08-A1 | 11 | 1 | ✓ | Royal and Conquering Heart-Elevation — the elevation of a ruler's, conqueror's, or prince's heart above proper creaturel |
| `M08-A1-VCG-03` | M08-A1 | 13 | 1 | ✓ | The Proud Heart as Constitutive Inner Condition — pride as a settled, dispositional characteristic of the heart not tied |
| `M08-A2-VCG-01` | M08-A2 | 7 | 1 | ✓ | Haughty Eyes — Pride in the Gaze — verses specifically naming the eyes or gaze as the register of pride; haughty eyes as |
| `M08-A2-VCG-02` | M08-A2 | 4 | 1 | ✓ | Outward Display and Body-Language of Pride — pride's visible register in broader bearing, ornament, and posture: the nec |
| `M08-A3-VCG-01` | M08-A3 | 9 | 1 | ✓ | Moab's Pride and Neighbouring Nations — publicly-known collective arrogance as a reported, multi-layered inner character |
| `M08-A3-VCG-02` | M08-A3 | 8 | 1 | ✓ | Babylon's Pride — National Splendor Destined for Total Ruin — corporate arrogance as self-glorying magnificence that mak |
| `M08-A3-VCG-03` | M08-A3 | 10 | 1 | ✓ | Israel's Pride — The Self-Incriminating Inner Characteristic of God's Own People — pride that testifies against Israel t |
| `M08-A3-VCG-04` | M08-A3 | 13 | 1 | ✓ | Day-of-the-LORD Universal Collective Humbling — everything proud and lofty targeted by divine judgment; the cosmic regis |
| `M08-A4-VCG-01` | M08-A4 | 11 | 1 | ✓ | Self-Love as Root and NT Vice-Catalogue Pride — filautos as the generative root; NT vice-catalogue huperēfanos and hupsē |
| `M08-A4-VCG-02` | M08-A4 | 9 | 1 | ✓ | God Actively Opposing the Proud — Divine Opposition as the Structural Frame — verses where God's watchful eyes on the ha |
| `M08-A4-VCG-03` | M08-A4 | 11 | 1 | ✓ | Psalmic Enemy Portraits — Pride as Predatory Social Aggression — arrogance as the inner driving force of oppressors: pur |
| `M08-A4-VCG-04` | M08-A4 | 16 | 1 | ✓ | Wisdom Maxims — Pride's Self-Defeating Consequences — Proverbs, Job, Ecclesiastes, and Daniel evidencing pride as a stru |
| `M08-A4-VCG-05` | M08-A4 | 21 | 1 | ✓ | Individual Self-Exaltation Against God — The Willed Act of Inner Elevation — the high-hand posture against God, the Psa  |
| `M08-B-VCG-01` | M08-B | 9 | 1 | ✓ | Boiling Presumption — the Zid Register — pride as a will that 'boils over' against a known divine prohibition or command |
| `M08-B-VCG-02` | M08-B | 25 | 1 | ✓ | Arrogant Insolence Against Authority — the Zed/Za.don Register — arrogant presumption against God's law, appointed relig |
| `M08-B-VCG-03` | M08-B | 11 | 1 | ✓ | Self-Willed Presumption in NT Narrative — domineering authority, self-willed dismissal of legitimate constraint, and irr |
| `M08-C-VCG-01` | M08-C | 26 | 1 | ✓ | Condemned Self-Directed Boasting — ha.lal self-boasting (premature glorification, boasting in creaturely assets, empty s |
| `M08-C-VCG-02` | M08-C | 21 | 1 | ✓ | The Pauline Boasting Discourse — Paul's extended examination of legitimate vs illegitimate self-commendation in 2 Corint |
| `M08-C-VCG-03` | M08-C | 23 | 1 | ✓ | Grace-Grounded and God-Directed Boasting — the M22 cross-register — boasting directed wholly toward God (Rom 5:2–3, 5:11 |
| `M08-D-VCG-01` | M08-D | 7 | 1 | ✓ | Intellectual and Partisan Conceit — inflation through knowledge (1Cor 8:1 — knowledge inflates while love builds up), fa |
| `M08-D-VCG-02` | M08-D | 5 | 1 | ✓ | Conceit as Miscalibrated Self-Assessment — overreaching the measure of faith (Rom 12:3 huperfroneō), inflated self-regar |
| `M08-E-VCG-01` | M08-E | 8 | 1 | ✓ | National Proud Might — Strength and Power as Ground for Arrogant Self-Sufficiency — ga.on proud-might vocabulary: nation |
| `M08-E-VCG-02` | M08-E | 9 | 1 | ✓ | Wealth, Position, and Self-Secured Elevation — Material Pride — prosperity and physical fortification as the ground for  |

### M09 (21 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M09-A-VCG-01` | M09-A | 16 | 1 | ✓ | The Old Testament Hebrew register of willed self-lowering — the inner act of ka.na (humbling before God) in response to  |
| `M09-A-VCG-02` | M09-A | 6 | 1 | ✓ | The Greek NT register of the verbal act of self-humbling (tapeinoō) directed Godward, where the willed downward movement |
| `M09-A-VCG-03` | M09-A | 3 | 1 | ✓ | The costlier, service-register expression of willed self-lowering: humility as the inner quality of self-giving in vocat |
| `M09-A-VCG-04` | M09-A | 6 | 1 | ✓ | The relational-disposition register of humility — as a quality of inner bearing toward God and community, contrasted wit |
| `M09-A-VCG-05` | M09-A | 5 | 1 | ✓ | The Pauline epistolary register of tapeinofrosunē — humility as a chosen, genuine inner character disposition placed alo |
| `M09-B-VCG-01` | M09-B | 4 | 1 | ✓ | The register of externally-imposed humbling where God is the agent and the person or people experience being brought low |
| `M09-B-VCG-02` | M09-B | 5 | 1 | ✓ | The register of lowliness as a social or existential condition that stands in relation to divine reversals, reframings,  |
| `M09-B-VCG-03` | M09-B | 4 | 1 | ✓ | The register of lowliness as an experienced inner state produced by affliction, suffering, circumstance, or God's action |
| `M09-C-VCG-01` | M09-C | 5 | 1 | ✓ | The register of submission as inner allegiance of the will — the will's habitual yielding discloses and constitutes whos |
| `M09-C-VCG-02` | M09-C | 4 | 1 | ✓ | The cognitive-volitional register of submission — obedience named in the mind's capture, the conscience's deliberation,  |
| `M09-C-VCG-03` | M09-C | 4 | 1 | ✓ | The register of submission-as-genuine-inner-motive — verses that explicitly distinguish sincere, God-ward inner complian |
| `M09-C-VCG-04` | M09-C | 4 | 1 | ✓ | The register of submission as something acquired, transformative, or costly at the deepest levels of the inner person. C |
| `M09-D-VCG-01` | M09-D | 8 | 1 | ✓ | The gospel-obedience register — obedience of faith as both the response to gospel proclamation and the defining characte |
| `M09-D-VCG-02` | M09-D | 5 | 1 | ✓ | The register of obedience as soteriological and sanctifying telos — the orientation of the will that connects the person |
| `M09-D-VCG-03` | M09-D | 4 | 1 | ✓ | The household and relational register of the submission-obedience pattern — obedience as a shaped quality within the aut |
| `M09-D-VCG-04` | M09-D | 2 | 1 | ✓ | The personal and eschatological allegiance register — obedience as a directed disposition of will toward a named authori |
| `M09-E-VCG-01` | M09-E | 2 | 1 | ✓ | The full contrition register — the acute, grief-laden inner brokenness of spirit that follows genuine confrontation with |
| `M09-F-VCG-01` | M09-F | 2 | 1 | ✓ | The meekness and gentleness characteristic — holding force, capability, or will in calibrated, measured expression. The  |
| `M09-G-VCG-01` | M09-G | 3 | 1 | ✓ | The full dignity characteristic — settled moral seriousness and gravitas that grounds composed, non-self-displaying cond |
| `M09-H-VCG-01` | M09-H | 4 | 1 | ✓ | The register of willing-heartedness as the freely-moved inner disposition driving offering and service without external  |
| `M09-H-VCG-02` | M09-H | 1 | 1 | ✓ | The distinctive register of willing-heartedness as a divine gift that must be sought and may be lost — evidenced in Psa5 |

### M10 (68 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M10-C-VCG-01` | M10-C | 30 | 1 | ✓ | Sinner as social-moral category: exclusion and stigma |
| `M10-C-VCG-02` | M10-C | 20 | 1 | ✓ | Sinner as constituted moral identity: imputed and declared status |
| `M10-C-VCG-03` | M10-C | 14 | 1 | ✓ | Sinner as extreme moral type: habitual wrongdoing defining total character |
| `M10-D-VCG-01` | M10-D | 18 | 1 | ✓ | Guilt-recognition: conscience engaging after the act |
| `M10-D-VCG-02` | M10-D | 19 | 1 | ✓ | Guilt as accumulated weight: communal and personal burden mounting |
| `M10-D-VCG-03` | M10-D | 16 | 1 | ✓ | Guilt as transferable burden: borne on behalf of another |
| `M10-D-VCG-04` | M10-D | 18 | 1 | ✓ | Guilt's punitive consequence: the burden of punishment borne |
| `M10-D-VCG-05` | M10-D | 26 | 1 | ✓ | Guilt exposed, indelible, and removed: the divine perspective |
| `M10-E-VCG-01` | M10-E | 17 | 1 | ✓ | Priestly and cultic bearing of iniquity |
| `M10-E-VCG-02` | M10-E | 18 | 1 | ✓ | Generational iniquity: transmitted across family lines |
| `M10-E-VCG-03` | M10-E | 28 | 1 | ✓ | Iniquity in divine memory: what God sees and does not forget |
| `M10-E-VCG-04` | M10-E | 29 | 1 | ✓ | Iniquity as personal moral crime: individually owned and judged |
| `M10-E-VCG-05` | M10-E | 30 | 1 | ✓ | Iniquity as overwhelming accumulated weight |
| `M10-E-VCG-06` | M10-E | 21 | 1 | ✓ | Iniquity pardoned and removed: divine forgiveness resolves the moral debt |
| `M10-E-VCG-07` | M10-E | 15 | 1 | ✓ | Iniquity as self-destructive force: the inner crime that ruins from within |
| `M10-E-VCG-08` | M10-E | 4 | 1 | ✓ | Iniquity heart-seated: the crime originating in the will |
| `M10-F-VCG-01` | M10-F | 27 | 1 | ✓ | Transgression against God: rebellion in the divine-covenant relationship |
| `M10-F-VCG-02` | M10-F | 7 | 1 | ✓ | Revolt: the inner defiance that speaks and acts against God |
| `M10-F-VCG-03` | M10-F | 13 | 1 | ✓ | Accumulated transgression crossing the threshold of divine tolerance |
| `M10-F-VCG-04` | M10-F | 15 | 1 | ✓ | Transgression as law-violation: the NT parabasis/parabatēs register |
| `M10-F-VCG-05` | M10-F | 5 | 1 | ✓ | Adam-paradigm transgression: the foundational boundary-crossing |
| `M10-F-VCG-06` | M10-F | 13 | 1 | ✓ | Transgression pardoned and erased: divine forgiveness of rebellion |
| `M10-F-VCG-07` | M10-F | 14 | 1 | ✓ | Transgression's oppressive weight: the burden that crushes and enslaves |
| `M10-F-VCG-08` | M10-F | 19 | 1 | ✓ | Transgression as interpersonal breach: wrong done between persons |
| `M10-F-VCG-09` | M10-F | 34 | 1 | ✓ | Transgression as personal moral breach: Job, Psalms, and wisdom |
| `M10-G-VCG-01` | M10-G | 57 | 1 | ✓ | Unfaithfulness toward God: covenant-betrayal directed upward (M13+M31) |
| `M10-G-VCG-02` | M10-G | 34 | 1 | ✓ | Relational treachery: faithlessness between persons (M13+M31) |
| `M10-G-VCG-03` | M10-G | 10 | 1 | ✓ | Treachery as constitutional inner character (M13+M31) |
| `M10-H-VCG-01` | M10-H | 10 | 1 | ✓ | Perversity of speech: the tongue as vehicle of moral inversion |
| `M10-H-VCG-02` | M10-H | 6 | 1 | ✓ | Perversion of judgment: bribery corrupting discernment |
| `M10-H-VCG-03` | M10-H | 19 | 1 | ✓ | Perversion of mind, will, and way: the inwardly twisted person |
| `M10-H-VCG-04` | M10-H | 4 | 1 | ✓ | Sexual perversion and moral degeneracy (M23/M35 bodily-decay) |
| `M10-H-VCG-05` | M10-H | 25 | 1 | ✓ | Moral corruption, decay, and lewdness (M03 cha.val/a.vah; M07 nav.lut) |
| `M10-I-VCG-01` | M10-I | 20 | 1 | ✓ | Judicial and commercial injustice: the corruption of right process (M26) |
| `M10-I-VCG-02` | M10-I | 33 | 1 | ✓ | Injustice as oppression and harm to persons (M26) |
| `M10-I-VCG-03` | M10-I | 19 | 1 | ✓ | Character of the unjust person: adikos, av.val, a.vil, adikēma (M26) |
| `M10-J-VCG-01` | M10-J | 32 | 1 | ✓ | Sin directed against God: the vertical relational offense |
| `M10-J-VCG-02` | M10-J | 18 | 1 | ✓ | Sin against the neighbour: the horizontal relational offense |
| `M10-J-VCG-03` | M10-J | 19 | 1 | ✓ | Sin deterred, restrained, or denied |
| `M10-J-VCG-04` | M10-J | 17 | 1 | ✓ | Sin requiring ritual remedy: the cultic-atonement register |
| `M10-J-VCG-05` | M10-J | 12 | 1 | ✓ | NT wilful sinning: hamartanō and paraptōma in M10-J |
| `M10-K-VCG-01` | M10-K | 10 | 1 | ✓ | Unintentional sin and moral surprise: conscience engaged after the fact |
| `M10-K-VCG-02` | M10-K | 8 | 1 | ✓ | Cultic purification: the ritual-cleansing register |
| `M10-L-VCG-01` | M10-L | 23 | 1 | ✓ | Individual confession: the will naming its own sin |
| `M10-L-VCG-02` | M10-L | 10 | 1 | ✓ | Corporate and communal confession |
| `M10-L-VCG-03` | M10-L | 1 | 1 | ✓ | Confession without transformed will: the hollow acknowledgment |
| `M10-M-VCG-01` | M10-M | 8 | 1 | ✓ | Conscience suppression and self-blindness |
| `M10-N-VCG-01` | M10-N | 18 | 1 | ✓ | Refusal to repent: departure withheld |
| `M10-O-VCG-01` | M10-O | 14 | 1 | ✓ | Habitual defection: the will's settled pattern toward sin |
| `M10-P-VCG-01` | M10-P | 19 | 1 | ✓ | Contagious sin: leadership transmitting moral defection |
| `M10-Q-VCG-01` | M10-Q | 9 | 1 | ✓ | Political revolt: wilful defection from governing relationship |
| `M10-R-VCG-01` | M10-R | 9 | 1 | ✓ | Slander and abusive speech: heart-generated inner corruption (M06) |
| `M10-R-VCG-02` | M10-R | 7 | 1 | ✓ | Blasphemy as divine-authority claim: presumptuous usurpation (M06) |
| `M10-R-VCG-03` | M10-R | 6 | 1 | ✓ | Blasphemy as identity: the beast's constitutive defiance (M06) |
| `M10-S-VCG-01` | M10-S | 5 | 1 | ✓ | Specialised sinful mechanisms: desire exploited (M14), appearance falsified (M08), identity abandoned (M31) |
| `M10-T-VCG-01` | M10-T | 5 | 1 | ✓ | Wickedness as defining inner condition (rish.ah, al.vah) |
| `M10-T-VCG-02` | M10-T | 39 | 1 | ✓ | Sin forgiven and addressed: the NT redemption register |
| `M10-T-VCG-03` | M10-T | 68 | 1 | ✓ | Sin as enslaving and dominating power (Rom 6-7) |
| `M10-U-VCG-01` | M10-U | 9 | 1 | ✓ | Sin as enslaving power: the will under bondage |
| `M10-V-VCG-01` | M10-V | 32 | 1 | ✓ | Chet: personal moral liability before God |
| `M10-V-VCG-02` | M10-V | 9 | 1 | ✓ | Cha.ta.ah: sin as objective moral category requiring covering |
| `M10-V-VCG-03` | M10-V | 5 | 1 | ✓ | Sin under divine scrutiny: Job's surveillance register |
| `M10-V-VCG-04` | M10-V | 46 | 1 | ✓ | Jeroboam-sin legacy: the named sin as recorded pattern |
| `M10-V-VCG-05` | M10-V | 113 | 1 | ✓ | Sin as objective burden before God: the broad chat.tat record |
| `M10-W-VCG-01` | M10-W | 12 | 1 | ✓ | Priestly atonement: kip.pu.rim and chat.tat sin-offering (M11) |
| `M10-W-VCG-02` | M10-W | 12 | 1 | ✓ | Forgiveness declared by Jesus and through Christ's blood (M11) |
| `M10-W-VCG-03` | M10-W | 10 | 1 | ✓ | Forgiveness sought through the Levitical sacrificial-atonement system (M11) |
| `M10-X-VCG-01` | M10-X | 8 | 1 | ✓ | Generational sin: the ancestral moral condition inherited |

### M10b (36 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M10b-A-VCG-01` | M10b-A | 5 | 1 | ✓ | Forensic-verdict register — mandatory polysemy VCG. Verses where ra.sha functions as a legal-status label in forensic/ju |
| `M10b-A-VCG-02` | M10b-A | 8 | 1 | ✓ | Practical atheism — God excluded from the inner mind of the wicked. The wicked person's defining inner characteristic is |
| `M10b-A-VCG-03` | M10b-A | 22 | 1 | ✓ | Pride as inner engine and directed hostility of the wicked. Two closely related registers: pride as the inner engine of  |
| `M10b-A-VCG-04` | M10b-A | 18 | 1 | ✓ | Moral contrast — wickedness defined against the inner status of the righteous. Verses where the wicked person is defined |
| `M10b-A-VCG-05` | M10b-A | 30 | 1 | ✓ | Wickedness condemned, exposed, and publicly judged. Verses where the wicked person's inner character draws visible, publ |
| `M10b-A-VCG-06` | M10b-A | 21 | 1 | ✓ | Wickedness as inner instability and self-destruction. Verses where wickedness is shown to be internally unstable — a con |
| `M10b-A-VCG-07` | M10b-A | 22 | 1 | ✓ | Wickedness as directional orientation — a way the will can turn from. The Ezekiel corpus on wickedness as a volitional d |
| `M10b-A-VCG-08` | M10b-A | 12 | 1 | ✓ | Wickedness expressed through speech — concealment, corruption, and social destruction. Verses where the wicked person's  |
| `M10b-A-VCG-09` | M10b-A | 33 | 1 | ✓ | Wickedness against divine justice — the wicked person's soul, appetites, and moral hollowness. The Proverbs-heavy corpus |
| `M10b-A-VCG-10` | M10b-A | 9 | 1 | ✓ | Job's theological debate — the wicked in the crucible of theodicy. The Job corpus addressing the wicked in the context o |
| `M10b-A-VCG-11` | M10b-A | 10 | 2 | ✓ | re.sha and mir.sha.at — wickedness as abstract condition and the wicked collective. The re.sha corpus (abstract noun: wi |
| `M10b-B-VCG-01` | M10b-B | 13 | 1 | ✓ | Cosmic evil — the evil one, the evil age — mandatory polysemy VCG. Verses where evil names a cosmic, supra-personal powe |
| `M10b-B-VCG-02` | M10b-B | 8 | 1 | ✓ | Constitutional evil — human nature bent toward corruption as baseline condition. Verses where evil names the constitutio |
| `M10b-B-VCG-03` | M10b-B | 8 | 1 | ✓ | The heart as treasury — the inner source and generative organ of evil. Verses where the heart is explicitly named as the |
| `M10b-B-VCG-04` | M10b-B | 17 | 1 | ✓ | Evil as settled deep character of persons. Verses where evil names the settled, characterological identity of persons —  |
| `M10b-B-VCG-05` | M10b-B | 20 | 3 | ✓ | Settled inner malice, entrenched badness, and deep hostile residue — kakia, ponēria, adikia saturation. Verses where the |
| `M10b-B-VCG-06` | M10b-B | 24 | 2 | ✓ | Evil conscience, moral accountability, progressive deterioration, and abhorrence of evil. Verses addressing moral accoun |
| `M10b-C-VCG-01` | M10b-C | 10 | 1 | ✓ | Ethical and character-orientation abomination — dishonest commercial practice, unjust social dealings, and the character |
| `M10b-C-VCG-02` | M10b-C | 9 | 2 | ✓ | Pride, crooked heart, and hidden corruption as abomination. Abomination located most directly in the interior life — pri |
| `M10b-C-VCG-03` | M10b-C | 4 | 1 | ✓ | Corrupt worship — the unclean inner person's religious act as abomination. The religious act (sacrifice, incense, prayer |
| `M10b-C-VCG-04` | M10b-C | 11 | 1 | ✓ | The silenced and awakening conscience before abomination. The faculty of conscience in its various states in relation to |
| `M10b-C-VCG-05` | M10b-C | 6 | 1 | ✓ | Identity and choice constituted by abomination. Abomination as a category defined by divine declaration (Pro 6:16), the  |
| `M10b-D-VCG-01` | M10b-D | 6 | 1 | ✓ | Levitical boundary-laws — abomination as category-violation against created order. The Levitical corpus declaring specif |
| `M10b-D-VCG-02` | M10b-D | 14 | 1 | ✓ | Deuteronomic warnings — the will that must actively resist abominable practices. The Deuteronomic corpus warning against |
| `M10b-D-VCG-03` | M10b-D | 17 | 1 | ✓ | Historical reform narratives — kings institutionalising or purging idolatrous abominations. The historical narratives wh |
| `M10b-D-VCG-04` | M10b-D | 14 | 1 | ✓ | Jeremiah and the Prophets — idolatrous objects installed and the will's stubbornness. The prophetic corpus outside Ezeki |
| `M10b-D-VCG-05` | M10b-D | 43 | 1 | ✓ | Ezekiel — idolatry driving the divine presence away from the sanctuary. Ezekiel's concentrated corpus where accumulated  |
| `M10b-D-VCG-06` | M10b-D | 5 | 1 | ✓ | Sacrilegious desolation and apocalyptic abomination. The eschatological and apocalyptic verses where abomination names a |
| `M10b-E-VCG-01` | M10b-E | 7 | 1 | ✓ | Trouble and distress as the affliction of evil — mandatory polysemy VCG. Verses where a.ven names the trouble, afflictio |
| `M10b-E-VCG-02` | M10b-E | 14 | 1 | ✓ | Iniquity as deliberate inner generation — conceived, devised, schemed. Verses where iniquity is most clearly an active g |
| `M10b-E-VCG-03` | M10b-E | 24 | 1 | ✓ | Evildoers as a defined inner-character class. Verses where iniquity defines a recognisable class of persons whose habitu |
| `M10b-E-VCG-04` | M10b-E | 23 | 1 | ✓ | Iniquity as stored condition — harboured, accumulated, concealed, and exposed. Verses where iniquity is treated as a sto |
| `M10b-E-VCG-05` | M10b-E | 11 | 1 | ✓ | Evil deeds as the outward expression of an inwardly-defiled source. The ro.a evil-deeds corpus — verses where the focus  |
| `M10b-F-VCG-01` | M10b-F | 6 | 1 | ✓ | Hardened defiance and contemptuous blasphemy against God. This VCG groups the verses in which blasphemy is the direct ex |
| `M10b-F-VCG-02` | M10b-F | 5 | 1 | ✓ | Blasphemy as social defamation — moral failure causing dishonour to God's name. This VCG groups the verses in which blas |
| `M10b-F-VCG-03` | M10b-F | 6 | 2 | ✓ | Wrongdoing as a charged and contested category — false accusation and legal-offense register. This VCG groups the verses |

### M10c (26 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M10c-A-VCG-01` | M10c-A | 2 | 1 | ✓ | Defilement incurred through contact the person may not immediately know has occurred; the guilt becomes morally real onl |
| `M10c-A-VCG-02` | M10c-A | 14 | 1 | ✓ | The unclean state incurred by touching, carrying, or eating the carcass of an unclean or dead animal — categorically for |
| `M10c-A-VCG-03` | M10c-A | 7 | 1 | ✓ | The unclean state transmitted from dead creatures to objects — vessels, food, water, ovens, seed, and material surfaces. |
| `M10c-A-VCG-04` | M10c-A | 2 | 1 | ✓ | Defilement through swarming creatures framed explicitly as volitional self-corruption — the person urged to refuse conta |
| `M10c-A-VCG-05` | M10c-A | 16 | 1 | ✓ | The ritual unclean state arising from menstruation and childbirth — physiological in origin, not moral fault, time-bound |
| `M10c-A-VCG-06` | M10c-A | 16 | 1 | ✓ | The unclean state produced by bodily discharge (genital discharge / zav condition) and its transmission to surfaces, obj |
| `M10c-A-VCG-07` | M10c-A | 27 | 1 | ✓ | The most severe sub-register — contact with a human corpse produces a seven-day unclean state requiring red-heifer ash ( |
| `M10c-A-VCG-08` | M10c-A | 9 | 1 | ✓ | Verses that frame the scope, limits, and existential stakes of bodily defilement — uncleanness restricts sacred not secu |
| `M10c-B-VCG-01` | M10c-B | 5 | 1 | ✓ | The cultivation of active moral-spiritual discernment as the inner-being faculty required for distinguishing clean from  |
| `M10c-B-VCG-02` | M10c-B | 13 | 1 | ✓ | The unclean state determined by authoritative priestly examination of skin disease. The priest observes bodily markers,  |
| `M10c-B-VCG-03` | M10c-B | 8 | 1 | ✓ | The experience of the declared unclean person — required to publicly cry out their own contaminated state, compelled to  |
| `M10c-B-VCG-04` | M10c-B | 9 | 1 | ✓ | The categorical unclean state applied to material objects — fabric with spreading disease burned; diseased house stones  |
| `M10c-B-VCG-05` | M10c-B | 5 | 1 | ✓ | The NT register where categorical clean/unclean convictions are formed in conscience, maintained against challenge, and  |
| `M10c-C-VCG-01` | M10c-C | 4 | 1 | ✓ | Verses addressing the human condition itself as inherently compromised before God — the impossibility of clean from uncl |
| `M10c-C-VCG-02` | M10c-C | 8 | 1 | ✓ | Impurity functioning as a prior master, slavery, or dominion over the will and bodily members — the condition to which u |
| `M10c-C-VCG-03` | M10c-C | 5 | 2 | ✓ | Verses where the conscience or will is the named primary locus of defilement, or where deliberate self-purification from |
| `M10c-C-VCG-04` | M10c-C | 6 | 1 | ✓ | The heart-allegiance dimension of moral-inner defilement — impurity equated with idolatry, arising from a heart that has |
| `M10c-C-VCG-05` | M10c-C | 3 | 1 | ✓ | The positive-inverse register — the inner-being condition of those who have not defiled themselves, maintained through c |
| `M10c-D-VCG-01` | M10c-D | 23 | 1 | ✓ | The defilement-state produced by sexual violations of covenantal bonds — adultery, bestiality, violation of a person, tr |
| `M10c-D-VCG-02` | M10c-D | 24 | 1 | ✓ | The defilement-state produced by the will's pursuit of idolatrous attachment — habitual devotion to false gods, spiritua |
| `M10c-D-VCG-03` | M10c-D | 10 | 1 | ✓ | Defilement inflicted on or threatening the sanctuary — by enemy invasion, by deliberate installation of idols and abomin |
| `M10c-D-VCG-04` | M10c-D | 9 | 1 | ✓ | Defilement extending from persons or community to the land itself — the moral-sacral pollution of shared inhabitable spa |
| `M10c-D-VCG-05` | M10c-D | 17 | 1 | ✓ | The consequences of corporate defilement projected into the physical and social condition of the people — expulsion, exi |
| `M10c-E-VCG-01` | M10c-E | 8 | 1 | ✓ | The inner-being condition of the person inhabited and dominated by an unclean spirit — will overridden, bodily agency lo |
| `M10c-E-VCG-02` | M10c-E | 8 | 1 | ✓ | The expulsion event and its dynamics — violent departure through convulsion and outcry, destructive transfer, vocal resi |
| `M10c-E-VCG-03` | M10c-E | 5 | 1 | ✓ | The commissioning of authority over unclean spirits and the spirits' recognition of divine power. Unclean spirits are ho |

### M15 (58 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `523-002` | M15-B | 1 | 0 | ✓ | Term names understanding as a human inner-being capacity — the gift from God enabling discernment of his ways and wise c |
| `525-001` | M15-A | 3 | 0 | ✓ | se.khel names a practical inner quality of good sense, prudence, and wise conduct. It produces outcomes — favour, succes |
| `528-001` | M15-A | 7 | 0 | ✓ | cha.kham in Proverbs, Ecclesiastes, and historical narrative names wisdom as a constituted inner quality of the person — |
| `M15-A-VCG01` | M15-A | 19 | 1 | — | The term names wisdom as belonging to God, to Christ as the embodied wisdom of God, or to Wisdom personified as God's ow |
| `M15-A-VCG02` | M15-A | 40 | 1 | — | The term names wisdom as a divinely-given inner endowment placed into a specific named person — Jesus growing in it, Sol |
| `M15-A-VCG03` | M15-A | 117 | 1 | — | The term names wisdom as the standing inner quality of a person — not the moment of receiving, but the constituted chara |
| `M15-A-VCG04` | M15-A | 13 | 1 | — | The term names what the inner faculty is directed toward — flesh or Spirit, things of God or things of man, things above |
| `M15-A-VCG05` | M15-A | 4 | 1 | — | The term names the inner state of unity or harmony between members of a community — being of the same mind, in accord, i |
| `M15-A-VCG06` | M15-A | 19 | 1 | — | The term names the inner posture of self-attributed wisdom — wisdom held as personal possession, the inner stance of bel |
| `M15-A-VCG07` | M15-A | 34 | 1 | — | The term names the inner orientation that constitutes 'wisdom of this age' or 'wisdom of the world' — overturned by the  |
| `M15-A-VCG08` | M15-A | 10 | 1 | — | The term names the perceptive inner capacity — the act of grasping meaning, understanding what is heard or read, interpr |
| `M15-A-VCG09` | M15-A | 3 | 1 | — | The term names wisdom as the inner state that arises from, or is constituted by, the fear of the Lord, attentiveness to  |
| `M15-A-VCG10` | M15-A | 4 | 1 | — | The term names the inner act of devising artistic designs for sacred construction — the mental forming of pattern that p |
| `M15-B-VCG01` | M15-B | 19 | 1 | — | The term names understanding as belonging to God himself — his self-sufficient, uncreated comprehension of all things. T |
| `M15-B-VCG02` | M15-B | 28 | 1 | — | The term names understanding as a divinely given inner endowment placed into a specific person — Solomon receiving it in |
| `M15-B-VCG03` | M15-B | 161 | 1 | — | The term names understanding as a constituted inner quality that grasps, discerns, and perceives — in leadership, wisdom |
| `M15-B-VCG04` | M15-B | 59 | 1 | — | The term names the inner perceptive faculty by its judicial withholding (God closes it), by its moral blockage (hardened |
| `M15-B-VCG05` | M15-B | 4 | 1 | — | The term names understanding as an inner capacity shaped through repeated practice and sustained discipline — the format |
| `M15-B-VCG06` | M15-B | 25 | 1 | — | The term names the inner perceptive act of grasping disclosed content — visions, prophetic words, Scripture, and the mys |
| `M15-B-VCG07` | M15-B | 11 | 1 | — | The term names sustained reasoned argument directed at persuading the inner person — the systematic engagement of the in |
| `M15-BOUNDARY-VCG01` | BOUNDARY | 1 | 1 | ✓ | Jude 9: Michael contending with the devil in disputation about the body of Moses. The dialegō here is the form taken by  |
| `M15-C-VCG01` | M15-C | 39 | 1 | — | The term names God's comprehensive, self-sufficient knowing of all things — hearts, plans, character, deeds. No one gave |
| `M15-C-VCG02` | M15-C | 9 | 1 | — | The term names God's knowing as an act of electing, choosing, and entering into intimate covenantal relationship — face  |
| `M15-C-VCG03` | M15-C | 88 | 1 | — | The term names God's redemptive self-disclosure through historical events — 'that you/they may know that I am the Lord.' |
| `M15-C-VCG04` | M15-C | 49 | 1 | — | The term names the human person's relational inner knowing of God — pressing on to know him, finding the knowledge of Go |
| `M15-C-VCG05` | M15-C | 50 | 1 | — | The term names the structural opposite — a person, community, or nation that does not know God, refuses the knowledge of |
| `M15-C-VCG06` | M15-C | 63 | 1 | — | The term names knowledge as an inner content or capacity possessed, accumulated, guarded, and transmitted — the Proverbs |
| `M15-C-VCG07` | M15-C | 12 | 1 | — | The term names the specifically moral knowing that distinguishes good from evil — named in the tree of the knowledge of  |
| `M15-C-VCG08` | M15-C | 87 | 1 | — | The term names knowing as a settled inner conviction — the 'we know that' pattern of the Pauline letters; Job's sustaine |
| `M15-C-VCG09` | M15-C | 21 | 1 | — | The term names ignorance that is culpable, structural, or judicially significant — the agnoeō (G0050) pattern: those who |
| `M15-C-VCG10` | M15-C | 134 | 1 | — | The term names the ordinary, practical knowing of persons, facts, situations, and skills — knowing where someone went, k |
| `M15-C-VCG11` | M15-C | 18 | 1 | — | The term names sexual union through the verb 'to know' — the Hebraic expression of the deepest intimacy between persons. |
| `M15-C-VCG12` | M15-C | 2 | 1 | — | The term names the universal knowing of God that marks the end of history — 'the earth shall be full of the knowledge of |
| `M15-D-VCG01` | M15-D | 69 | 1 | — | The term names the inner quality of prudent wisdom as it generates effective, God-aligned action — success in conduct, p |
| `M15-D-VCG02` | M15-D | 19 | 1 | — | The term names the inner act of discriminating — of making evaluative distinctions between persons or things, or of the  |
| `M15-D-VCG03` | M15-D | 24 | 1 | — | The term names the inner act of crediting, imputing, or reckoning — whether divine (counting faith as righteousness, not |
| `M15-D-VCG04` | M15-D | 27 | 1 | — | The term names the inner deliberative act of thinking — forming an assessment through attending to evidence or reflectio |
| `M15-D-VCG05` | M15-D | 11 | 1 | — | The term names tasting as the figure for inner discernment — the palate that tests food becomes the image for the inner  |
| `M15-D-VCG06` | M15-D | 15 | 1 | — | The term names the inner quality of shrewd perceptiveness that can be either wisdom or cunning depending on its directio |
| `M15-D-VCG07` | M15-D | 2 | 1 | — | The term names the cognitive argumentation of the inner person — thoughts that accuse or excuse before the conscience, a |
| `M15-E-VCG01` | M15-E | 44 | 1 | — | The term names the inner volitional act of purposive willing — Joseph's resolution to divorce Mary quietly, Pilate's wil |
| `M15-E-VCG02` | M15-E | 8 | 1 | — | The term names the inner considered resolution — Paul's deliberate judgment offered without a dominical command, the col |
| `M15-E-VCG03` | M15-E | 13 | 1 | — | The term names the divine counsel as irresistible sovereign intent — 'as I have planned, so shall it be; as I have purpo |
| `M15-E-VCG04` | M15-E | 66 | 1 | — | The term names the human counseling relationship — advisors sought, wisdom given, counsel rejected or followed, the coun |
| `M15-E-VCG05` | M15-E | 48 | 1 | — | The term names deliberate purposive devising — the forming of plans in the heart, whether for good (Pro 16:9 the heart p |
| `M15-E-VCG06` | M15-E | 4 | 1 | — | The term names purpose so firmly resolved that it cannot be revoked — human unified purposing (Gen 11:6, Tower of Babel) |
| `M15-E-VCG07` | M15-E | 7 | 1 | — | The term names the deliberate act of directing the heart's attention — setting the heart toward something, or the failur |
| `M15-E-VCG08` | M15-E | 8 | 1 | — | The term names the inner capacity for purposive foresight — the governor's capacity to plan for his community's welfare  |
| `M15-F-VCG01` | M15-F | 27 | 1 | — | The term names inner deliberative reasoning — questioning in the heart, calculating political consequences, reasoning wi |
| `M15-F-VCG02` | M15-F | 7 | 1 | — | The term names sustained inner reflection that produces conceived thoughts — Joseph contemplating his situation before t |
| `M15-F-VCG03` | M15-F | 31 | 1 | — | The term names the sustained inner activity of meditation — dwelling on God's precepts, pondering his mighty acts, musin |
| `M15-F-VCG04` | M15-F | 2 | 1 | — | The term names either Daniel's focused contemplative attention directed at the revelatory vision (se.khal), or the divin |
| `M15-G-VCG01` | M15-G | 11 | 1 | — | The term names the inner cognitive content — the mind's formed thoughts as they can be blinded, captured, corrupted, or  |
| `M15-G-VCG02` | M15-G | 10 | 1 | — | The term names the formed thoughts that arise in the mind — Nebuchadnezzar's night-thoughts producing his dream, Belshaz |
| `M15-G-VCG03` | M15-G | 6 | 1 | — | The term names knowledge as formed inner content — what Solomon requested from God (wisdom and knowledge), what God plac |
| `M15-H-VCG01` | M15-H | 19 | 1 | — | The term names logos as the active divine or apostolic word that engages the inner person — the word of the cross that i |
| `M15-H-VCG02` | M15-H | 21 | 1 | — | The term names logos as the communicative act of the human person — evaluated by whether it is intelligible (reaching th |
| `M15-H-VCG03` | M15-H | 2 | 1 | — | The term names logos as the single moral principle that holds and summarises all the law's content — the whole law is fu |

### M20 (26 VCGs · status: Analysis Completed (Terms Added))

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1288-001` | M20-D | 2 | 1 | — | Doubt as situational faith-wavering — the inner person failing to complete the move from seeing to trusting in a specifi |
| `1398-001` | M20-D | 2 | 1 | — | Double-mindedness as dispositional indecision — the inner person not settling, not committing, hedging between two orien |
| `1403-001` | M20-C | 1 | 1 | — | The fainthearted soul — the inner person diminished in courage (oligopsuchos: small-souled), requiring the response of b |
| `2078-001` | M20-C | 1 | 1 | — | Discouragement as the inner state produced by interpersonal provocation — one person's provoking act creating another's  |
| `259-002` | M20-A | 1 | 1 | ✓ | Anxiety as the fuel of contrition — da.ag naming the inner energy that drives genuine sorrow over sin; the anxious, trou |
| `2709-001` | M20-A | 9 | 1 | ✓ | Anxiety about material provision — the inner person preoccupied with food, drink, clothing, the body, and tomorrow; addr |
| `2709-003` | M20-A | 5 | 1 | ✓ | The anxiety-faculty rightly directed — merimnaō naming the intensity of directed concern for God's things and for others |
| `350-001` | M20-A | 4 | 1 | ✓ | Anxiety as choking weight on the inner person — cares of the world, riches, and pleasures operating together to strangle |
| `4481-001` | ? | 5 | 1 | — | Term names deep inner perplexity — the state of being thoroughly at a loss before spiritual or extraordinary reality |
| `4482-001` | ? | 5 | 1 | — | Term names the inner state of perplexity — being at a loss, uncertain, or disturbed without being driven to despair |
| `4483-001` | ? | 1 | 1 | — | Term names the inner state of perplexity and bewilderment — the person at a complete loss before an inexplicable event |
| `808-001` | M20-B | 2 | 1 | — | Despair as the outer limit of inner endurance — the inner person burdened beyond capacity, despaired of life itself (2Co |
| `M20-A-NEW-01` | M20-A | 1 | 1 | — | Anxiety cast onto God — the person currently carrying real anxieties commanded to transfer the weight to God, with the t |
| `M20-A-NEW-02` | M20-A | 1 | 1 | ✓ | Pastoral burden as the weight of love — merimna naming the daily pressure of apostolic care for the churches; love expre |
| `M20-A-NEW-03` | M20-A | 2 | 1 | ✓ | Anticipatory anxiety about speech and defence under threat — anxiety directed toward a specific future performance situa |
| `M20-A-NEW-04` | M20-A | 1 | 1 | ✓ | Anxiety as proliferation — the inner person anxious and troubled about many things; attentional scattering across multip |
| `M20-A-NEW-05` | M20-A | 2 | 1 | ✓ | Relational anxiety — worried concern for an absent or endangered person; anxiety as the dark face of relational love whe |
| `M20-A-NEW-06` | M20-A | 4 | 1 | ✓ | Anxiety in the face of concrete external threats — and its structural opposite; da.ag applied to real, named dangers (Is |
| `M20-B-NEW-01` | M20-B | 3 | 1 | — | Despair as volitional act — the heart actively surrendered to hopelessness (Ecc 2:20); despair as the natural terminus o |
| `M20-B-NEW-02` | M20-B | 2 | 1 | — | Despair as declaration — the word of hopelessness spoken or withheld, and its consequences; the declaration not made (Is |
| `M20-B-NEW-03` | M20-B | 1 | 1 | — | Despair weaponised — hopelessness-language deployed to foreclose repentance and justify continued rebellion; 'that is in |
| `M20-C-NEW-01` | M20-C | 4 | 1 | — | Discouragement inflicted on the vulnerable — the disheartened as the specific target of cruelty (Psa 109:16: the brokenh |
| `M20-C-NEW-02` | M20-C | 2 | 1 | — | Discouragement producing inner retreat — loss of resolve under military-political pressure, expressed immediately in wit |
| `M20-C-NEW-03` | M20-C | 5 | 1 | — | Loss of heart in sustained effort — long-haul endurance failing under temporal frustration; the discouragement that accu |
| `M20-C-NEW-04` | M20-C | 1 | 1 | — | Loss of heart and the inner person's renewal — the outer person wasting away while the inner person is renewed day by da |
| `M20-C-NEW-05` | M20-C | 1 | 1 | — | The crushed and sinking — total inner overwhelm of the helpless; ka.ah in its most acute form: the victim crushed, sinki |

### M26 (79 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1099-001` | M26-C | 10 | 2 | ✓ | Term names the dikaiōma — whether decree, standard, righteous act, or verdict — as the external reality that discloses,  |
| `1185-001` | M26-F | 7 | 2 | ✓ | Inner valuation and estimation — the act of deeming worthy or unworthy, including inner self-assessment, desire, inner d |
| `1211-001` | M26-B | 5 | 1 | ✓ | Uprightness as an inner quality of the heart — tested by God, contrasted with wickedness, invoked as protection |
| `1211-002` | M26-B | 4 | 1 | ✓ | Uprightness as the path/way — inner orientation expressed in the direction of life |
| `1211-003` | M26-B | 3 | 1 | ✓ | Uprightness expressed in speech — words as disclosure of inner integrity |
| `1212-001` | M26-B | 8 | 1 | ✓ | Uprightness as the standard and quality of right judgment — divine and demanded of human authorities |
| `1212-002` | M26-B | 8 | 1 | ✓ | Uprightness as inner character formation — wisdom's goal; the inmost being rejoices at rightness |
| `1214-001` | M26-B | 4 | 1 | ✓ | Uprightness resisted, absent, or refused — the inner being's failure to receive or produce what is right |
| `1215-001` | M26-B | 1 | 1 | — | Uprightness of heart directed toward God — inner moral orientation of relational fidelity |
| `1218-001` | M26-B | 1 | 1 | ✓ | Uprightness as the defining moral character of Christ's kingship — inner quality expressed in sovereign rule |
| `1225-001` | M26-G | 15 | 1 | ✓ | Acting wickedly — inner act of moral departure from God and righteousness |
| `1225-002` | M26-G | 19 | 1 | ✓ | Condemnation and guilt — the verdict of wickedness on the inner moral condition |
| `2739-001` | ? | 1 | 1 | — | Term names the act of inner self-awareness or conscience — the person's own consciousness of their moral state, which no |
| `3193-001` | M26-A2 | 45 | 2 | — | Term characterises the person as morally righteous — the inner quality of justice and uprightness that defines the perso |
| `3193-002` | M26-A1 | 4 | 1 | — | Term names God and Christ as just and righteous — addressing the Father directly as 'righteous Father' (Joh 17:25), affi |
| `3194-001` | M26-C | 36 | 2 | ✓ | Term names the divine act of justification — the declaration that transforms the person's inner moral standing before Go |
| `3201-001` | M26-E | 4 | 2 | ✓ | Term names the inner act of moral condemnation — the judgment that pronounces another guilty and the divine prohibition  |
| `3203-001` | M26-C | 2 | 2 | ✓ | Term names justification as the act that restores right standing before God — the inner transformation of moral status t |
| `3207-001` | M26-D | 1 | 1 | ✓ | Term names the righteous judgment of God — the divine standard of just assessment that confronts the hard-hearted inner  |
| `3208-001` | M26-F | 1 | 1 | ✓ | Term names the condition of moral accountability before God — the inner standing of being answerable to divine judgment |
| `3246-001` | M26-BOUNDARY | 2 | 0 | ✓ | Term names the righteous person's inner moral character — the constitutive orientation of the whole inner being toward w |
| `3246-002` | M26-A2 | 21 | 1 | ✓ | Term names the righteous person as the direct object of God's relational attention — seen, tested, known, loved, upheld, |
| `3246-003` | M26-A2 | 18 | 1 | ✓ | Term names the characteristic inner response of the righteous person toward God — gladness, exultation, praise, thanksgi |
| `3250-001` | M26-D | 2 | 2 | ✓ | Term names the avenging character of divine authority — the inner justice that punishes wrongdoing and protects the wron |
| `3410-001` | M26-F | 32 | 3 | ✓ | Inner reasoning and reckoning — the cognitive inner act of considering, reasoning, concluding, and the reckoning of fait |
| `4-001` | M26-BOUNDARY | 5 | 0 | ✓ | Term names the moral ground of a person's standing — the charge, reason, or basis for guilt or innocence, including the  |
| `4846-001` | M26-E | 8 | 2 | ✓ | Term describes condemnation as the verdict passed on the inner person on the basis of their inner state — unbelief, doub |
| `4846-002` | M26-E | 6 | 2 | ✓ | Term names the freedom from condemnation — the security of the inner person before God when condemnation is withheld or  |
| `4848-001` | M26-E | 1 | 1 | ✓ | Term names the condition of the inner person whose own beliefs or conduct become the instrument of their condemnation —  |
| `5617-001` | M26-G | 2 | 1 | ✓ | Term names acting unjustly — the inner orientation that produces perverse conduct, unable to perceive righteousness or d |
| `6753-001` | M26-F | 3 | 1 | — | Term names marshalling a legal case before God — inner rational and moral act directed toward accountability |
| `6753-002` | M26-F | 4 | 1 | — | Term performs a comparison disclosing the inner orientation of worship — nothing equals God |
| `6753-003` | M26-F | 2 | 1 | ✓ | Term names an act of preparation expressive of inner devotion — setting oneself before God in prayer |
| `6753-004` | M26-F | 1 | 1 | — | Term describes divine affliction arrayed against the inner being — the assault of divine terrors on the spirit |
| `6753-005` | M26-F | 1 | 1 | — | Term qualifies a covenant as ordered and secure — expressing confident trust in God's reliability |
| `6841-001` | M26-D | 1 | 1 | — | Term names inner self-restrained generosity — giving to those who cannot repay, oriented toward divine reward |
| `6841-002` | M26-D | 2 | 1 | ✓ | Term names the inner relinquishing of personal vengeance — entrusting retribution to God |
| `6841-003` | M26-D | 1 | 1 | — | Term expresses impulse to return thanksgiving — gratitude as inner response to grace |
| `6841-004` | M26-D | 2 | 1 | ✓ | Term names God's just inner commitment to repay — divine retributive justice; impossibility of placing God in debt |
| `7161-001` | M26-F | 1 | 1 | — | Term names impartiality as a defining inner character quality of wisdom from above — the absence of inner wavering or pr |
| `738-001` | M26-E | 2 | 1 | ✓ | Term names condemnation as an inner state produced by the law's verdict — the weight of moral judgment falling on the co |
| `911-001` | M26-A2 | 17 | 1 | ✓ | Term names righteousness as a personal inner possession — held fast, carried in the heart, expressed in the whole manner |
| `911-002` | M26-A2 | 7 | 1 | — | Term names righteousness as a personal moral standing that God sees and rewards — the inner condition of the person that |
| `911-003` | M26-A1 | 1 | 0 | — | Term names God's righteousness as the object of appeal, praise, and proclamation by his people — the quality they invoke |
| `942-001` | M26-A2 | 12 | 1 | ✓ | Term names the person's righteousness as a personal moral standing before God — the inner condition appealed to in praye |
| `942-002` | M26-BOUNDARY | 2 | 0 | — | Term names God's righteousness as his foundational divine attribute — the eternal quality that is the basis of his thron |
| `942-003` | M26-A2 | 4 | 1 | — | Term names righteousness as an inner orientation actively pursued — seeking the Lord and righteousness together (Isa 51: |
| `942-004` | M26-BOUNDARY | 16 | 0 | — | Righteousness as moral basis for just governance — inner character required of kings, judges, and rulers |
| `944-001` | M26-D | 3 | 2 | ✓ | Term names the inner cry and petition for divine justice — the persistent appeal of the wronged person to God for vindic |
| `944-002` | M26-D | 2 | 1 | ✓ | Term names the execution of divine vengeance and justice — God's inner determination to right wrongs and vindicate the o |
| `945-001` | M26-D | 9 | 2 | ✓ | Term names the divine vengeance and justice that arises from God's inner righteousness in response to evil — and the hum |
| `947-001` | M26-C | 30 | 2 | ✓ | Inner moral standing before God — being righteous, accounted righteous, or incapacity to be righteous |
| `947-002` | M26-C | 10 | 2 | ✓ | Judicial act of vindicating the righteous or condemning the wicked — requiring inner moral discernment |
| `949-001` | M26-E | 3 | 2 | ✓ | Term names the just punishment or condemnation that follows moral transgression — the consequence of the inner condition |
| `950-001` | M26-A2 | 18 | 1 | ✓ | Term names righteousness received through a divine crediting act — counted, reckoned, and conferred rather than earned o |
| `950-002` | M26-A2 | 13 | 1 | ✓ | Term names righteousness as a practiced, lived orientation — the daily direction of a person's conduct before God. It is |
| `M26-A1-001` | M26-A1 | 29 | 1 | — | Term declares God's righteousness as a foundational, permanent attribute of his nature — not situational, not responsive |
| `M26-A1-002` | M26-A1 | 27 | 1 | ✓ | Term names God's righteousness as expressed through his judicial acts — judgments that conform to what is right rather t |
| `M26-A1-003` | M26-A1 | 14 | 1 | ✓ | Term names God's righteousness as the quality that makes him reliable and faithful to his covenant people — keeping prom |
| `M26-A1-005` | M26-A1 | 22 | 1 | ✓ | Term names God's righteousness as something that must be declared, proclaimed, and made known — it is not self-evident b |
| `M26-A1-006` | M26-A1 | 10 | 1 | ✓ | Term names God's righteousness as the standard that exposes human unrighteousness by contrast — when God's righteousness |
| `M26-A1-007` | M26-A1 | 39 | 1 | ✓ | Term names righteousness as the defining quality of the coming Messianic figure — the Righteous One, the righteous Branc |
| `M26-A2-001` | M26-A2 | 49 | 1 | ✓ | Term names righteousness as a governing quality whose presence produces measurable outcomes — deliverance from death, st |
| `M26-A2-002` | M26-A2 | 30 | 1 | ✓ | Term names righteousness as a dynamic personal standing — conditional, forfeitable, and non-transferable. In Deuteronomy |
| `M26-A2-003` | M26-A2 | 26 | 1 | ✓ | Term names the failure, distortion, or counterfeit form of righteousness across a wide range of expressions: righteous d |
| `M26-A2-004` | M26-A2 | 5 | 1 | ✓ | Term names the condition of being far from or lacking righteousness — in the person, the community, and the public spher |
| `M26-A2-005` | M26-A2 | 1 | 1 | ✓ | Term names righteousness as already known and carried in the heart as law. The person addressed is defined by this knowi |
| `M26-A2-006` | M26-A2 | 8 | 1 | ✓ | Term names righteousness as the object of active inner longing and deliberate pursuit — hungered for, thirsted for, fled |
| `M26-A2-007` | M26-A2 | 6 | 1 | ✓ | Term names righteousness as a generative quality — something sown, grown, harvested, and multiplied. The agricultural im |
| `M26-A2-008` | M26-A2 | 4 | 1 | ✓ | Term names righteousness as the defining constitution of the new self in Christ. The new self is created after the liken |
| `M26-A2-009` | M26-A2 | 5 | 1 | — | Term names righteousness as something worn — it clothes, covers, and accompanies the person as an enveloping identity. J |
| `M26-A2-010` | M26-A2 | 11 | 1 | ✓ | Term names the righteous person as the target of systemic and personal injustice — their cause subverted by bribes, thei |
| `M26-A2-011` | M26-A2 | 15 | 1 | ✓ | Term names righteousness as a governing inner orientation expressed through speech and discernment. The interior dimensi |
| `M26-A2-012` | M26-A2 | 12 | 1 | ✓ | Term names righteousness as an inner orientation that extends outward toward others — in all relationships and at every  |
| `M26-A2-013` | M26-A2 | 15 | 1 | ✓ | Term names righteousness as a state whose inner foundation produces lasting stability. The rootedness is deep: the root  |
| `M26-A2-014` | M26-A2 | 19 | 2 | ✓ | Term names righteousness as a state defined by and constituted through its orientation toward God. The righteous person  |
| `M26-A2-015` | M26-A2 | 12 | 1 | ✓ | Term names a recognisable community of righteous persons whose collective presence carries weight and consequences. The  |
| `M26-A2-016` | M26-A2 | 18 | 1 | ✓ | Term names the righteous person as a specific target of hostility — plotted against (Psa 37:12), watched for death (Psa  |
| `M26-A2-017` | M26-A2 | 5 | 1 | ✓ | Term names a recognisable life trajectory belonging to the righteous — a path and way that is level (Isa 26:7), grows pr |

### M39 (34 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1299-001` | M39-A | 89 | 2 | ✓ | Term names God's act of blessing — the sovereign covenantal gift of favour, fruitfulness, and life that flows from God's |
| `1299-002` | M39-A | 54 | 2 | ✓ | Term names the human act of blessing God — the inner-being orientation of worship, doxology, and praise that declares Go |
| `1299-003` | M39-A | 91 | 2 | ✓ | Term names the human act of blessing other humans — the covenantal declaration of favour, the prophetic word of blessing |
| `1299-004` | M39-A | 13 | 2 | ✓ | Term names the ironic/euphemistic use of blessing — cursing God under the name of "blessing" (the Job passages), or bles |
| `1301-001` | M39-A | 14 | 2 | ✓ | Term names grace in its Spirit-endowed capacity form — the charisma as the spiritual capacity God gives to each person f |
| `2330-001` | M39-A | 13 | 2 | ✓ | Term designates the constitutional inner character of graciousness — not merely a disposition but the settled identity o |
| `494-001` | M39-A | 6 | 1 | ✓ | Divine goodwill/pleasure as the sovereign inner purpose of God |
| `494-002` | M39-A | 3 | 1 | — | Human goodwill/desire — the inner orientation of longing for good |
| `542-001` | M39-B | 18 | 2 | ✓ | Term names the two-pole goodness characteristic of tov: (i) goodness as heart-quality — the inner moral excellence locat |
| `5470-001` | M39-A | 11 | 1 | ✓ | Term names the concrete acts of divine grace-giving — God giving what the recipient cannot earn or generate: from the su |
| `5470-002` | M39-A | 8 | 1 | ✓ | Term names the human act of forgiving — releasing another from debt, offence, or resentment, patterned on and grounded i |
| `5471-001` | M39-A | 2 | 1 | ✓ | Term names the act of bestowing grace — the divine favour poured upon a person or people as a relational act that marks  |
| `632-001` | M39-B | 10 | 2 | ✓ | Term names the heart being glad or merry — the inner state of lightness and well-being expressed in festive eating, drin |
| `632-002` | M39-B | 61 | 2 | ✓ | Term names moral goodness and doing good: the inner moral orientation from which right action flows; goodness as the gro |
| `632-003` | M39-B | 22 | 2 | ✓ | Term names the inner state of being pleased or finding something good — the approval, satisfaction, or favour that the i |
| `6837-001` | M39-A | 7 | 1 | ✓ | Term names the gift as an act of worship — offering given as expression of inner devotion toward God |
| `6837-002` | M39-A | 2 | 1 | ✓ | Term names the moral claim of relational conscience amid worship — the gift interrupted by reconciliation |
| `6837-003` | M39-A | 2 | 1 | ✓ | Term names misuse of religious dedication as pretext for moral evasion — piety masking filial failure |
| `6837-004` | M39-A | 3 | 1 | ✓ | Term names inner inadequacy of ritual gifts to perfect the conscience — gap between external offering and inner transfor |
| `6837-005` | M39-A | 1 | 1 | — | Term names salvation as God's free gift — not earned but received, establishing inner dependence and gratitude |
| `6837-006` | M39-A | 2 | 1 | ✓ | Term names radical self-giving generosity — total offering from poverty as expression of complete inner trust |
| `795-001` | M39-A | 20 | 1 | ✓ | Divine acceptance of offerings — God's inner-being pleasure in what is offered |
| `795-002` | M39-A | 10 | 1 | ✓ | Divine pleasure in persons/character — God's inner delight in the righteous |
| `795-003` | M39-A | 23 | 1 | ✓ | Term names the human experience of ra.tsah — the inner act of seeking, receiving, or extending acceptance and favour; in |
| `885-001` | ? | 4 | 1 | — | Term names goodness as an inner-being disposition and Spirit-produced fruit — a quality that fills the person and is com |
| `888-001` | M39-A | 22 | 2 | ✓ | Term names grace as the sovereign, unmerited divine disposition toward humanity — the freely given, transforming gift th |
| `888-002` | M39-A | 13 | 2 | ✓ | Term names grace as the relational sphere and power in which the believer stands and lives — the ongoing inner-relationa |
| `888-003` | M39-A | 17 | 1 | ✓ | Term names grace as relational favour — the disposition of goodwill between persons or between a person and God, which o |
| `888-004` | M39-A | 36 | 1 | ✓ | Term names grace as the animating power and sphere of apostolic mission — the word of grace, the commendation to grace,  |
| `889-001` | M39-A | 15 | 2 | ✓ | Term names the divine relational favour bestowed on a person — the inner-relational disposition of God toward those he k |
| `889-002` | M39-A | 38 | 1 | ✓ | Term names relational favour between persons — the inner-relational disposition of goodwill one person seeks and receive |
| `889-003` | M39-A | 14 | 1 | ✓ | Term names favour as inner character quality — the gracious disposition expressed in speech, conduct, and wisdom that ge |
| `984-001` | M39-A | 72 | 2 | ✓ | Term names the two-sided act of grace: (i) God's inner disposition of grace as the ground of his response to the supplic |
| `989-001` | M39-A | 2 | 2 | ✓ | Term names mercy shown in moral action and the plea of prayer — the practice of mercy toward the oppressed and the inner |

### M46 (34 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `111-001` | M46-C | 3 | 1 | — | Term names the inner enrichment or richly-supplied condition of the soul that flows from right inner character — the sou |
| `111-002` | M39-A | 1 | 1 | ✓ | Anointing face — routed to M39-A. Not M46 material. Retained in DB as cross-cluster route. |
| `1142-001` | M46-A | 28 | 2 | — | Term names abundance or greatness as a scalar applied to inner-moral realities — the weight or magnitude of iniquity (Je |
| `3836-001` | M46-D | 1 | 1 | — | Term names the inner act of luxuriating in or delighting in received abundance — specifically delighting in God's goodne |
| `413-001` | ? | 8 | 2 | ✓ | Term names the inner condition of complacent ease that wealth and security produce — the settled, untroubled self-assura |
| `413-002` | M46-D | 1 | 1 | ✓ | Term names the divinely-given condition of secure quietness — the ease of God's people living in genuine peace and safet |
| `4695-001` | M46-A | 3 | 1 | — | Term names material richness as the ambient condition within which the inner person's orientation toward God is tested a |
| `4697-001` | M46-A | 1 | 1 | — | Term names the making-fat of the inner heart as the mechanism of divine judgment — God causing the heart to grow thick a |
| `4697-002` | M46-A | 4 | 1 | — | Term names the spiritual fatness that material prosperity produces — the person who has grown fat through abundance fors |
| `4702-001` | M46-B | 1 | 1 | — | Term names the luxurious goods of Babylon as the object of the soul's longing — 'your soul longed for all your delicacie |
| `4898-001` | M46-D | 1 | 1 | — | Term names contentment as a learned inner disposition — the acquired capacity of the inner person to remain settled and  |
| `681-001` | M46-C | 5 | 2 | — | Term names wealth and treasure as the moral category in which inner character is revealed — in the house of the righteou |
| `7010-001` | M46-B | 12 | 1 | — | Term names material wealth in its relation to the inner life of the person who holds it — its capacity to function as an |
| `7109-001` | M46-D | 1 | 1 | — | Term (in negation) names the inner disposition of not-hoarding — the eschatological ordering in which material wealth is |
| `7577-001` | M46-A | 15 | 2 | — | Term names the inner-closure condition of the self-assessed wealthy person — the one who says 'I am rich, I need nothing |
| `7577-002` | M46-B | 7 | 1 | — | Term names the wealthy person whose abundance has produced hardness toward others — the rich man who feasts daily while  |
| `7577-003` | M46-D | 3 | 0 | — | Term names wealth in its Christological inversion and eschatological revaluation — he who was rich became poor for our s |
| `7578-001` | M46-D | 2 | 1 | — | Term names the abundance of divine provision — God who richly provides all things for enjoyment (1Ti 6:17). The adverb p |
| `7579-001` | M46-A | 6 | 1 | — | Term names the self-directed drive to become rich as the inner-being condition that produces closure and ruin — those wh |
| `7579-002` | M46-D | 4 | 0 | — | Term names becoming rich in its directed-toward-God and toward-others form — not laying up treasure for oneself but bein |
| `7580-001` | M46-D | 3 | 1 | — | Term names the enrichment of others as the inner-being goal and outcome of apostolic poverty — as poor yet making many r |
| `7581-001` | M46-B | 4 | 1 | — | Term names material riches as the choking and deceiving inner force — the deceitfulness (apatē) of riches competes with  |
| `7581-002` | M46-D | 2 | 0 | — | Term names riches in their revaluation by a higher inner-being calculus — the wealth of generosity that flows from pover |
| `7582-001` | M46-D | 1 | 1 | — | Term names the voluntary poverty of Christ as the paradigmatic act of the wealth domain's inversion — though he was rich |
| `7583-001` | M46-D | 9 | 1 | — | Term names poverty as the inner posture of dependence and openness before God — the condition in which the person has no |
| `7583-002` | M46-B | 5 | 0 | — | Term names the poor person as the moral test of the wealthy person's inner condition — the assembly that pays attention  |
| `7583-003` | M46-D | 8 | 0 | — | Term names voluntary giving from poverty and the command to give to the poor as acts that produce genuine enrichment and |
| `7584-001` | M46-B | 13 | 1 | — | Term names the inner condition of the wealthy person whose material abundance has produced specific distortions — wise i |
| `7584-002` | M46-C | 2 | 0 | — | Term names the rich person in the wisdom tradition's moral examination — the rich and poor stand equally before God who  |
| `7585-001` | M46-A | 8 | 0 | — | Term names the inner drive to become rich as the source of moral failure and self-deception — Ephraim declares 'I am ric |
| `7585-002` | M46-C | 6 | 0 | — | Term names enrichment as the fruit of diligence and divine blessing — the hand of the diligent makes rich (Pro 10:4); th |
| `7585-003` | M46-D | 2 | 1 | — | Term names the deliberate refusal of enrichment as an act of inner integrity and wisdom — Abram refuses to take a thread |
| `7586-001` | M46-A | 12 | 1 | — | Term names material riches as the object of misplaced trust and the condition of insatiability — those who trust in thei |
| `7586-002` | M46-C | 15 | 2 | — | Term names material riches as the gift and fruit of the ordered inner life — Wisdom carries riches in her left hand alon |

---

## §7. Summary

- **Clusters with active VCGs:** 17
- **Total active VCGs:** 745
- **Singleton VCGs (1 verse):** 77 (10.3% of all VCGs)
- **VCGs cited in cluster_finding:** 472 of 745 (63%)
- **Avg Jaccard similarity** VCG-desc vs sub-group-desc: 0.08
- **Cross-cluster description tokens (≥3 clusters):** 1141

**For the v3_0 decision:** §2.1 (singleton count), §4 (citation rate), and §3 (Jaccard) are the three direct rent-tests. A low citation rate combined with a high singleton fraction and high Jaccard would argue strongly for dropping the layer. A high citation rate with low singleton fraction would argue for keeping it.