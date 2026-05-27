# VCG analytics — what's actually in the database

_Generated: 2026-05-27 04:21 UTC_  
_Source: `database/bible_research.db` — `verse_context_group` + `vcg_term` + `verse_context.group_id`_

**Purpose:** surface what the VCG layer holds across all clusters so the v3_0 decision (drop VCGs as Phase 7 design layer) can be made with full visibility of what would become legacy.

---

## §1. Cluster-level coverage

Clusters with active VCGs in the DB and their analytical state.

| Cluster | Status | # VCGs | # is_rel verses (in VCGs) | Avg V/VCG | Med V/VCG | Anchors |
|---|---|---:|---:|---:|---:|---:|
| **FLAG** | Not started | 189 | 2047 | 10.8 | 6 | 273 |
| **M01** | Analysis Completed (Terms Added) | 38 | 945 | 24.9 | 18 | 91 |
| **M02** | Analysis Completed (Terms Added) | 27 | 645 | 23.9 | 18 | 55 |
| **M03** | Analysis Completed | 25 | 690 | 27.6 | 17 | 81 |
| **M04** | Analysis Completed | 47 | 1116 | 23.7 | 16 | 73 |
| **M05** | Analysis Completed (Terms Added) | 123 | 1560 | 12.7 | 6 | 127 |
| **M06** | Analysis Completed | 51 | 429 | 8.4 | 3 | 57 |
| **M07** | Analysis Completed | 28 | 359 | 12.8 | 9 | 28 |
| **M08** | Analysis Completed | 24 | 293 | 12.2 | 11 | 24 |
| **M09** | Analysis Completed | 21 | 97 | 4.6 | 4 | 21 |
| **M10** | Analysis Completed | 68 | 1320 | 19.4 | 17 | 68 |
| **M10b** | Analysis Completed | 36 | 515 | 14.3 | 12 | 42 |
| **M10c** | Analysis Completed | 26 | 263 | 10.1 | 8 | 27 |
| **M11** | Parked - Methodology Review | 26 | 288 | 11.1 | 9 | 30 |
| **M12** | Not started | 58 | 454 | 7.8 | 5 | 78 |
| **M13** | Not started | 46 | 592 | 12.9 | 9 | 62 |
| **M14** | Not started | 53 | 372 | 7.0 | 3 | 64 |
| **M15** | Analysis Completed | 58 | 1655 | 28.5 | 19 | 55 |
| **M16** | Not started | 39 | 164 | 4.2 | 4 | 40 |
| **M17** | Not started | 31 | 256 | 8.3 | 4 | 39 |
| **M18** | Not started | 37 | 258 | 7.0 | 4 | 46 |
| **M19** | Not started | 43 | 329 | 7.7 | 3 | 50 |
| **M20** | Analysis Completed (Terms Added) | 26 | 68 | 2.6 | 2 | 26 |
| **M21** | Not started | 48 | 508 | 10.6 | 6 | 63 |
| **M22** | Not started | 80 | 1013 | 12.7 | 7 | 122 |
| **M23** | Not started | 158 | 1267 | 8.0 | 4 | 234 |
| **M24** | Not started | 94 | 567 | 6.0 | 4 | 102 |
| **M25** | Not started | 27 | 503 | 18.6 | 6 | 28 |
| **M26** | Analysis Completed | 79 | 825 | 10.4 | 6 | 91 |
| **M27** | Not started | 30 | 172 | 5.7 | 5 | 33 |
| **M28** | Not started | 58 | 343 | 5.9 | 3 | 62 |
| **M29** | Not started | 22 | 294 | 13.4 | 9 | 24 |
| **M30** | Not started | 43 | 639 | 14.9 | 4 | 51 |
| **M31** | Not started | 25 | 313 | 12.5 | 3 | 39 |
| **M33** | Not started | 67 | 442 | 6.6 | 4 | 104 |
| **M34** | Not started | 40 | 169 | 4.2 | 2 | 45 |
| **M35** | Not started | 25 | 177 | 7.1 | 6 | 41 |
| **M36** | Not started | 28 | 312 | 11.1 | 4 | 33 |
| **M37** | Not started | 27 | 384 | 14.2 | 7 | 40 |
| **M38** | Not started | 20 | 320 | 16.0 | 12 | 30 |
| **M39** | Analysis Completed | 34 | 718 | 21.1 | 13 | 49 |
| **M41** | Not started | 60 | 1098 | 18.3 | 11 | 63 |
| **M42** | Not started | 45 | 418 | 9.3 | 5 | 60 |
| **M43** | Not started | 22 | 89 | 4.0 | 4 | 28 |
| **M44** | Not started | 23 | 236 | 10.3 | 3 | 30 |
| **M45** | Not started | 19 | 172 | 9.1 | 2 | 21 |
| **M46** | Analysis Completed | 34 | 197 | 5.8 | 4 | 31 |
| **T2** | Not started | 621 | 5772 | 9.3 | 4 | 845 |
| **TOTAL** | — | **2849** | **31,663** | — | — | **3726** |

**Orphan VCGs** (active VCG row with zero active is_relevant verses): 413
- `79-001` (vcg_id=43) — `Term names divine anger as the response to idolatry — the kindling of God's wrat`
- `79-002` (vcg_id=44) — `Term names divine anger as tempered by steadfast love — the characterisation of `
- `79-003` (vcg_id=45) — `Term names human anger as the inner response to relational conflict — the kindli`
- `79-004` (vcg_id=46) — `Term names the mastery of anger as the measure of inner greatness — governing an`
- `79-005` (vcg_id=47) — `Term names divine anger as the experience of hiddenness — the face turned away a`
- `1430-001` (vcg_id=142) — `Term names the excellent spirit as the seat of extraordinary inner character — w`
- `1430-002` (vcg_id=143) — `Term names the hardened spirit as the inner seat of pride — the spirit that stif`
- `1430-003` (vcg_id=144) — `Term names the anxious spirit as the inner reception of divine vision — the spir`
- `1586-001` (vcg_id=160) — `Term names the inner disposition of kindness toward human persons — benevolent o`
- `1589-001` (vcg_id=162) — `Term names the inner disposition of kindly consideration toward others — the ori`

---

## §2. VCG size distribution

Histogram of verses per VCG. **Singleton VCGs (1 verse) are a key signal — do we create VCGs that hold just one verse?**

| Size range | # VCGs | % of total | Cumulative % |
|---|---:|---:|---:|
| 1 verse | 528 | 18.5% | 18.5% |
| 2-3 verses | 567 | 19.9% | 38.4% |
| 4-5 verses | 371 | 13.0% | 51.5% |
| 6-10 verses | 536 | 18.8% | 70.3% |
| 11-20 verses | 434 | 15.2% | 85.5% |
| 21-50 verses | 324 | 11.4% | 96.9% |
| 51-100 verses | 73 | 2.6% | 99.4% |
| 101+ verses | 16 | 0.6% | 100.0% |
| **Total** | **2849** | 100% | — |

### §2.1 Singleton VCGs (528 total — each holds exactly 1 verse)

These are the most direct signal for 'VCG layer overhead without analytical density.' One verse cannot internally cluster; the VCG description is effectively a per-verse note.

| Cluster | VCG code | Description excerpt |
|---|---|---|
| FLAG | `1109-001` | Term names absence of inner restraint as vulnerability — a person without self-control is exposed li |
| FLAG | `1261-001` | Term applied to wisdom's worth — exceeding human capacity to assess, engaging the inner epistemic li |
| FLAG | `1261-002` | Term describes a relational equal — a valued inner bond whose betrayal is deeply felt |
| FLAG | `1364-003` | Term describes the wilful overriding of divine covenant — an inner act of defiance against binding o |
| FLAG | `1367-005` | Term expresses renown or known standing |
| FLAG | `1377-001` | Term describes the person's inner conformity to Christ through suffering — the act of becoming like  |
| FLAG | `1396-001` | Term names the natural/soul-level inner condition — operating from the soul alone, incapable of rece |
| FLAG | `1679-001` | Term names the birthright as sacred inheritance — whose careless disposal reveals inner contempt for |
| FLAG | `1724-001` | Term names inner dismay — the condition of being broken and shattered in spirit by overwhelming fear |
| FLAG | `1864-003` | Term names the dulling or weighting of the inner faculty of spiritual hearing and understanding |
| FLAG | `1866-001` | Term names the volitional closing of the inner faculty of spiritual hearing — the person deliberatel |
| FLAG | `215-002` | Iniquity bound up — stored guilt as inner moral condition |
| FLAG | `2979-001` | Term names the rule of other lords over the people — the domination experienced by those whose inner |
| FLAG | `2980-002` | Term names the marriage bond as the expression of spiritual allegiance — its faithful or unfaithful  |
| FLAG | `3304-002` | Covenant made before God with all-heart commitment |
| FLAG | `415-001` | Wellbeing expressed in greeting — the inner orientation of goodwill and wholeness directed toward an |
| FLAG | `4190-001` | Term names the formation of inner dispositions through training — shaping the affective and relation |
| FLAG | `4198-001` | Term names inner division — the split allegiance of the person who cannot commit fully to God's law |
| FLAG | `4667-002` | Term names the divine yielding to inner distress — God himself moved by the misery of his people |
| FLAG | `5034-001` | Term names the inner condition of distraction — the person whose inner orientation is pulled and sca |
| FLAG | `5237-002` | Slippery footing — the inner instability of those who appear to prosper |
| FLAG | `5300-001` | Distinguished inner excellence — the excellent spirit as the ground of outward distinction |
| FLAG | `5951-001` | Term names a divine overthrow that should have produced inner return — the overwhelming judgment des |
| FLAG | `5954-001` | Term names a perverse contrariness — the inner orientation that inverts right relationship, giving w |
| FLAG | `6211-001` | Term names absence of restraint as the ground for inner confidence — nothing can hinder God from sav |
| FLAG | `6511-001` | Moral-cognitive inexperience — the state of being unskilled in the word of righteousness, designatin |
| FLAG | `6709-001` | Term names the true worshiper as a person defined by their inner-being orientation — worship in spir |
| FLAG | `6713-001` | Term names deliberate inner intention or scheming — the inner act of purposing to change or overturn |
| FLAG | `7332-001` | Term frames a simile that characterises a predatory inner disposition — eager to destroy and lying i |
| FLAG | `7473-001` | Term names the inner participation in creation's anguish — the corporate groan of all things awaitin |
| FLAG | `7544-001` | broken relational state as inner obstacle to authentic worship — reconciliation required |
| FLAG | `7573-001` | indelibly formed inner moral character depicted as fixed marking |
| FLAG | `760-001` | Term names the act of divine counsel as a call to attend to the inner condition — guidance that addr |
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
| … | … and 478 more singletons |  |

---

## §3. VCG description distinctness from parent sub-group

For each VCG: how much new analytical content does the VCG description carry over its parent sub-group's `core_description`? Measured by Jaccard token similarity (1.0 = identical token set; 0.0 = no shared tokens). **High similarity = VCG description duplicates sub-group description.**

| Jaccard similarity (VCG desc vs parent sub-group desc) | # VCGs | % |
|---|---:|---:|
| 0.0 <= j < 0.10 | 2613 | 91.7% |
| 0.1 <= j < 0.20 | 196 | 6.9% |
| 0.2 <= j < 0.30 | 32 | 1.1% |
| 0.3 <= j < 0.40 | 8 | 0.3% |
| 0.4 <= j < 0.50 | 0 | 0.0% |
| 0.5 <= j < 0.70 | 0 | 0.0% |
| 0.7 <= j <= 1.0 | 0 | 0.0% |

**Average Jaccard:** 0.02. (Lower = VCG descriptions analytically distinct from sub-group; higher = VCG descriptions overlap sub-group content.)

---

## §4. Analytical-rent test — VCG code citation in `cluster_finding`

For each cluster, count how many of its VCGs are mentioned by code at least once in any `cluster_finding.finding_text` body. **A VCG that is never cited is analytical overhead that paid no Phase 9 rent.**

| Cluster | # VCGs | # cited at least once | Citation rate |
|---|---:|---:|---:|
| FLAG | 189 | 5 | 3% |
| M01 | 38 | 31 | 82% |
| M02 | 27 | 24 | 89% |
| M03 | 25 | 25 | 100% |
| M04 | 47 | 43 | 91% |
| M05 | 123 | 3 | 2% |
| M06 | 51 | 25 | 49% |
| M07 | 28 | 14 | 50% |
| M08 | 24 | 24 | 100% |
| M09 | 21 | 14 | 67% |
| M10 | 68 | 1 | 1% |
| M10b | 36 | 9 | 25% |
| M10c | 26 | 21 | 81% |
| M11 | 26 | 0 | 0% |
| M12 | 58 | 1 | 2% |
| M13 | 46 | 0 | 0% |
| M14 | 53 | 0 | 0% |
| M15 | 58 | 1 | 2% |
| M16 | 39 | 0 | 0% |
| M17 | 31 | 0 | 0% |
| M18 | 37 | 1 | 3% |
| M19 | 43 | 0 | 0% |
| M20 | 26 | 9 | 35% |
| M21 | 48 | 1 | 2% |
| M22 | 80 | 1 | 1% |
| M23 | 158 | 4 | 3% |
| M24 | 94 | 4 | 4% |
| M25 | 27 | 0 | 0% |
| M26 | 79 | 61 | 77% |
| M27 | 30 | 3 | 10% |
| M28 | 58 | 3 | 5% |
| M29 | 22 | 0 | 0% |
| M30 | 43 | 0 | 0% |
| M31 | 25 | 0 | 0% |
| M33 | 67 | 0 | 0% |
| M34 | 40 | 5 | 12% |
| M35 | 25 | 0 | 0% |
| M36 | 28 | 0 | 0% |
| M37 | 27 | 0 | 0% |
| M38 | 20 | 0 | 0% |
| M39 | 34 | 31 | 91% |
| M41 | 60 | 0 | 0% |
| M42 | 45 | 2 | 4% |
| M43 | 22 | 0 | 0% |
| M44 | 23 | 0 | 0% |
| M45 | 19 | 0 | 0% |
| M46 | 34 | 3 | 9% |
| T2 | 621 | 10 | 2% |
| **Total** | **2849** | **379** | **13%** |

**Interpretation:** the citation rate is the most direct measure of whether VCGs paid analytical rent during Phase 9. Codes that never appear in any finding text were structural overhead. (Note: synthesis findings may cite sub-group codes more than VCG codes, which is consistent with Phase 9 firing at characteristic scope.)

---

## §5. Cross-cluster VCG description token patterns

Tokens appearing in VCG descriptions across multiple clusters surface common within-sub-group axes (e.g. 'external' / 'internal' / 'volitional' / 'corporate'). Filtered to tokens with cluster-spread >= 3.

| Token | # clusters | # VCG descs |
|---|---:|---:|
| `god` | 48 | 776 |
| `divine` | 47 | 548 |
| `act` | 47 | 387 |
| `toward` | 46 | 359 |
| `god's` | 45 | 392 |
| `orientation` | 44 | 338 |
| `moral` | 42 | 409 |
| `disposition` | 42 | 266 |
| `heart` | 42 | 198 |
| `term` | 41 | 1814 |
| `names` | 41 | 1677 |
| `condition` | 41 | 240 |
| `spiritual` | 41 | 198 |
| `relational` | 41 | 165 |
| `human` | 40 | 215 |
| `self` | 40 | 206 |
| `life` | 40 | 188 |
| `will` | 39 | 146 |
| `directed` | 38 | 126 |
| `before` | 37 | 202 |
| `quality` | 37 | 187 |
| `people` | 37 | 102 |
| `person's` | 36 | 125 |
| `character` | 35 | 213 |
| `against` | 35 | 98 |
| `state` | 34 | 150 |
| `persons` | 34 | 116 |
| `spirit` | 33 | 131 |
| `one` | 33 | 117 |
| `response` | 33 | 98 |

---

## §6. Per-cluster VCG inventory (compact)

Every active VCG, by cluster, with verse count and description excerpt (first 120 chars).

### FLAG (189 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1079-001` | ? | 12 | 1 | — | Term names the goal or outcome that orients the inner person's striving and choices — the telos that gives moral meaning |
| `1079-002` | ? | 8 | 1 | — | Term names endurance to the end as the inner disposition of faithful perseverance under pressure — the completion of the |
| `1108-001` | ? | 3 | 1 | — | Term names sound-mindedness as an inner quality — the rational, morally disciplined disposition of the person, whether i |
| `1109-001` | ? | 1 | 1 | — | Term names absence of inner restraint as vulnerability — a person without self-control is exposed like a city without wa |
| `1124-001` | ? | 5 | 1 | — | Term names moral-spiritual completion or termination — the state of being blameless/complete in integrity, or the eschat |
| `1186-001` | ? | 30 | 3 | — | Judging as inner disposition and inner self-examination — the act of judging others as expressing an inner attitude, jud |
| `1240-001` | ? | 13 | 1 | — | Eschatological orientation — things to come, the age to come, glory to be revealed — shaping inner hope and expectation |
| `1240-002` | ? | 7 | 1 | — | Imminence of consequence or trial — shaping inner response of fear, endurance, or urgent action |
| `1240-003` | ? | 3 | 1 | — | Faith acting toward the future — Abraham, Isaac, future blessings |
| `1249-001` | ? | 35 | 2 | — | Term names genuine worship as the inner-being act of prostration and devotion directed toward God or Christ — the comple |
| `1249-002` | ? | 11 | 1 | — | Term names idolatrous worship as the inner-being act of prostration misdirected toward false gods, demons, or the beast  |
| `1249-003` | ? | 8 | 1 | — | Term names social prostration as an act of relational deference — a physical expression of respect ranging from courtesy |
| `1261-001` | ? | 1 | 1 | — | Term applied to wisdom's worth — exceeding human capacity to assess, engaging the inner epistemic limit |
| `1261-002` | ? | 1 | 1 | — | Term describes a relational equal — a valued inner bond whose betrayal is deeply felt |
| `1302-001` | ? | 46 | 2 | — | Term names God as the object of direct personal address, petition, trust, and relational orientation — the God toward wh |
| `1302-002` | ? | 35 | 2 | — | Term names God's character or nature as an attribute that calls forth or grounds inner response — what God is like that  |
| `1302-003` | ? | 21 | 2 | — | Term names God's identity in theological declaration — assertions of his singularity, incomparability, and saving nature |
| `1334-001` | ? | 16 | 5 | — | Term names the filling or completing of the inner being — whether filled with joy, comfort, wisdom, knowledge, the Spiri |
| `1360-001` | ? | 3 | 1 | — | Term describes the human person's constitutive likeness to God — the imago Dei as the inner ground of human dignity |
| `1360-002` | ? | 4 | 1 | — | Term mediates the encounter between the human person and the divine presence in human form, producing an inner response  |
| `1360-003` | ? | 3 | 1 | — | Term frames a comparison that exposes or characterises an inner disposition — moral malice, misplaced craving, or the te |
| `1364-001` | ? | 3 | 1 | — | Term describes the inner renewal of strength and vitality that comes through waiting on or turning to God |
| `1364-002` | ? | 4 | 1 | — | Term expresses the transience of human life and creation — the rapid passing that characterises human existence |
| `1364-003` | ? | 1 | 1 | — | Term describes the wilful overriding of divine covenant — an inner act of defiance against binding obligation |
| `1364-004` | ? | 3 | 1 | — | Term describes the passing of God or divine spirit near the person, engaging the person's inner capacity for perception  |
| `1366-001` | ? | 42 | 2 | — | Term names the divine name as the embodied self-disclosure of God's character, nature, and presence |
| `1366-002` | ? | 112 | 2 | — | Term is used in expressions of human inner orientation toward God — calling upon, trusting in, praising, fearing, honour |
| `1366-003` | ? | 21 | 2 | — | Term designates a person's name as the bearer of their character, moral quality, and reputation |
| `1366-004` | ? | 33 | 2 | — | Term appears in a theologically weighted naming act — the giving or changing of a name expresses an inner state, divine  |
| `1366-005` | ? | 15 | 2 | — | Term expresses renown or social standing — name as fame, legacy, and honour in the eyes of others |
| `1367-001` | ? | 7 | 2 | — | Term names the divine name as the embodied self-disclosure of God's character, nature, and presence |
| `1367-002` | ? | 61 | 2 | — | Term is used in expressions of human inner orientation toward Christ/God — calling upon, trusting in, praising, fearing, |
| `1367-003` | ? | 11 | 2 | — | Term designates a person's name as their identity, moral standing, and belonging — including names written in the book o |
| `1367-004` | ? | 10 | 2 | — | Term appears in a theologically weighted naming act — the giving of a name expresses divine declaration or identity conf |
| `1367-005` | ? | 1 | 1 | — | Term expresses renown or known standing |
| `137-001` | ? | 4 | 1 | — | Term names the inner warming process of developing intensity — anger or passionate feeling as a thermal process building |
| `1377-001` | ? | 1 | 1 | — | Term describes the person's inner conformity to Christ through suffering — the act of becoming like him in his death as  |
| `1396-001` | ? | 1 | 1 | — | Term names the natural/soul-level inner condition — operating from the soul alone, incapable of receiving spiritual trut |
| `1396-002` | ? | 4 | 1 | — | Term names the natural body as the lower form — sown natural, raised spiritual; soul-level as pre-resurrection mode |
| `1602-001` | ? | 27 | 2 | — | Term names the beloved as the object of intense longing, delight, and exclusive devotion — the relational centre of the  |
| `1679-001` | ? | 1 | 1 | — | Term names the birthright as sacred inheritance — whose careless disposal reveals inner contempt for what is holy, a war |
| `1724-001` | ? | 1 | 1 | — | Term names inner dismay — the condition of being broken and shattered in spirit by overwhelming fear or defeat |
| `175-001` | ? | 2 | 1 | — | Term names the inner bearing of grudge — sustained anger retained in the heart against another, named as the interior co |
| `175-002` | ? | 6 | 1 | — | Term names the duration of divine anger — how long God holds wrath and whether it resolves into mercy, with the answer c |
| `1848-001` | ? | 2 | 1 | — | Term names the act of foreseeing — the inner capacity of prophetic or divine perception that reads the future and shapes |
| `1864-001` | ? | 6 | 2 | — | Term names the volitional or divinely imposed hardening of the heart — the capacity for responsive obedience becomes wei |
| `1864-002` | ? | 3 | 1 | — | Term describes the moral gravity of sin or iniquity as a weight that is borne by the person or community |
| `1864-003` | ? | 1 | 1 | — | Term names the dulling or weighting of the inner faculty of spiritual hearing and understanding |
| `1864-004` | ? | 5 | 1 | — | Term measures the inner weight of suffering, anguish, or divine discipline experienced by the person |
| `1866-001` | ? | 1 | 1 | — | Term names the volitional closing of the inner faculty of spiritual hearing — the person deliberately makes themselves u |
| `201-001` | ? | 3 | 1 | ✓ | Inner constraint and compulsion — the spirit pressed from within |
| `201-002` | ? | 7 | 1 | — | Oppressive pressing from without — distress experienced under siege and oppression |
| `2070-001` | ? | 39 | 1 | — | God's delight in or non-delight in persons, sacrifices, and ways |
| `2070-002` | ? | 6 | 1 | — | Human delight in God, his law, or his ways — the inner orientation of the righteous |
| `2070-003` | ? | 26 | 1 | — | Human desire/will in various contexts — including desire for what is wrong |
| `215-001` | ? | 10 | 1 | — | Being in distress, constrained and afflicted — inner experience of pressure and suffering |
| `215-002` | ? | 1 | 1 | — | Iniquity bound up — stored guilt as inner moral condition |
| `217-001` | ? | 24 | 1 | — | The adversary/foe as source of inner distress — enmity, reproach, and the experience of being vexed |
| `226-001` | ? | 17 | 1 | — | Hardening of heart and stubborn will — inner moral resistance to God |
| `226-002` | ? | 2 | 1 | — | Inner character of harshness and severity — expressed in speech and conduct |
| `2591-001` | ? | 3 | 1 | — | Term names God's disturbing/stirring power in creation — an expression of divine inner capacity and sovereignty |
| `2654-001` | ? | 4 | 1 | — | Term names the act of turning or transferring as inner spiritual change — deserting truth, perverting grace, or the inst |
| `2707-001` | ? | 2 | 1 | — | Term names troubled, disquieting thoughts — the inner agitation of the mind under pressure or in visionary states |
| `2779-001` | ? | 2 | 1 | — | Term names the eschatological possession of the kingdom by the saints — the inner being engaged through hope and the ori |
| `2785-001` | ? | 4 | 2 | — | Term names Christ as the originating source and perfecting Lord of salvation and faith — the inner being engaged through |
| `2867-001` | ? | 8 | 2 | — | Term names divine appointment or ordering — the inner being engaged through calling, commission, election, and submissio |
| `2960-001` | ? | 2 | 1 | — | Term names the divinely assigned portion as the condition imposed on human pride — what God apportions to the person who |
| `2961-001` | ? | 8 | 1 | — | "The Lord is my portion" — God as the ultimate inner orientation of trust and belonging |
| `2961-002` | ? | 7 | 1 | — | Portion as lot and inner acceptance — finding contentment in one's assigned place |
| `2961-003` | ? | 12 | 1 | — | Portion as moral destiny and spiritual belonging — receiving or losing one's share in God's community |
| `2979-001` | ? | 1 | 1 | — | Term names the rule of other lords over the people — the domination experienced by those whose inner allegiance is drawn |
| `2980-001` | ? | 6 | 2 | — | Term names God as husband of his people — the defining relational bond expressing belonging, delight, and faithful claim |
| `2980-002` | ? | 1 | 1 | — | Term names the marriage bond as the expression of spiritual allegiance — its faithful or unfaithful orientation toward G |
| `2981-001` | ? | 5 | 1 | — | Term names the owner's relationship to possessions — the inner futility and self-harm of holding wealth as master over i |
| `2982-001` | ? | 7 | 2 | — | Term names the marital bond as the arena of inner honour, trust, and grief — the husband-relationship as constitutive of |
| `2983-001` | ? | 5 | 2 | — | Term names a person as "master" of an inner quality or capacity — defined by anger, appetite, or ability as their charac |
| `2985-001` | ? | 5 | 2 | — | Term names a person as the possessor of an inner quality or capacity — wisdom, wickedness, a sworn commitment — that def |
| `3084-001` | ? | 3 | 1 | — | Divine appointment — God's will expressed in calling and commissioning persons for purposes |
| `3189-001` | ? | 6 | 2 | — | Term names justice as the defining inner character of God — the disposition of right dealing that flows from who God is |
| `3189-002` | ? | 11 | 2 | — | Term names justice as the inner moral orientation of the person — the disposition to seek, do, and love what is right in |
| `3189-003` | ? | 9 | 2 | — | Term names the inner cry for justice — the longing of the person denied their right, reaching toward God for vindication |
| `3233-001` | ? | 18 | 2 | — | Term names the divine act of judging — God's inner determination to vindicate his people, execute justice among the nati |
| `3233-002` | ? | 6 | 2 | — | Term names the human act of judging on behalf of the poor — the inner moral obligation to give right judgment to the vul |
| `3241-001` | ? | 9 | 2 | — | Term names the inner act of perceiving or approving something as right — the moral/personal assessment that something ac |
| `3241-002` | ? | 9 | 2 | — | Term names the quality of moral uprightness — the straight inner path and conduct that reflects alignment with God's way |
| `3303-001` | ? | 9 | 1 | — | Divine covenantal faithfulness — God's unbroken inner commitment expressed through the promise of dynastic continuity |
| `3304-001` | ? | 67 | 1 | — | Divine covenant initiated by God — the relational framework of his commitment |
| `3304-002` | ? | 1 | 1 | — | Covenant made before God with all-heart commitment |
| `3304-003` | ? | 8 | 1 | — | Prohibited covenant — binding to false loyalties |
| `3304-004` | ? | 9 | 1 | — | Covenant of intimate personal loyalty — friendship and inner-being commitment between persons |
| `3600-001` | ? | 3 | 1 | — | God's forming of the inner person — heart and spirit |
| `3601-001` | ? | 4 | 1 | — | Potter-clay metaphor as inner-being orientation — human dependence, formation, and moral shaping before God |
| `3602-001` | ? | 6 | 1 | — | Term names purposive formation — the inner act of planning or forming a purpose, whether divine sovereign intention or h |
| `415-001` | ? | 1 | 1 | — | Wellbeing expressed in greeting — the inner orientation of goodwill and wholeness directed toward another through formal |
| `4190-001` | ? | 1 | 1 | — | Term names the formation of inner dispositions through training — shaping the affective and relational life toward godly |
| `4198-001` | ? | 1 | 1 | — | Term names inner division — the split allegiance of the person who cannot commit fully to God's law |
| `4667-001` | ? | 5 | 1 | — | Term names the anguish of the shortcut — the inner impatience that drives the spirit to abandon the divinely appointed p |
| `4667-002` | ? | 1 | 1 | — | Term names the divine yielding to inner distress — God himself moved by the misery of his people |
| `5034-001` | ? | 1 | 1 | — | Term names the inner condition of distraction — the person whose inner orientation is pulled and scattered by competing  |
| `5235-001` | ? | 2 | 1 | — | A pleasant portion despoiled — God's inner grief over the loss of what is precious |
| `5237-001` | ? | 4 | 1 | — | Flattering lips and double heart — the inner moral quality of deceptive smoothness |
| `5237-002` | ? | 1 | 1 | — | Slippery footing — the inner instability of those who appear to prosper |
| `5273-001` | ? | 5 | 1 | — | Partial knowledge and present inner limitation — knowing in part, seeing dimly |
| `5273-002` | ? | 7 | 1 | — | Portion and belonging — sharing in spiritual realities, included or excluded |
| `5276-001` | ? | 4 | 1 | — | Portion as inner belonging — choosing, sharing, and being excluded from spiritual participation |
| `5300-001` | ? | 1 | 1 | — | Distinguished inner excellence — the excellent spirit as the ground of outward distinction |
| `533-001` | ? | 11 | 2 | — | Term names the love-relationship in its full range — from covenantal God-Israel love and the Song's mutual delight to ad |
| `534-001` | ? | 8 | 2 | — | Term names the beloved as the object of God's deepest attachment and delight — used for persons and Israel in election;  |
| `555-001` | ? | 9 | 2 | — | Term names Christ as the Father's beloved — the unique inner-relationship of love between Father and Son expressed in th |
| `555-002` | ? | 63 | 2 | — | Term names the believer as beloved — addressed as the cherished object of God's and the community's love, called to live |
| `5694-001` | ? | 5 | 2 | — | Term names the obtaining of eschatological realities — salvation, resurrection, a better life — as the object of inner h |
| `5807-001` | ? | 3 | 2 | — | Term marks completion of an inner act — prayer or inward speech — naming the moment the inner address to God concludes |
| `5807-002` | ? | 12 | 2 | — | Term names the ending or exhaustion of an inner state or divine attribute — spent quality or inexhaustible character |
| `5808-001` | ? | 11 | 2 | — | Consuming action of God's inner wrath, anger, or jealousy — divine inner passion expressed in judgment |
| `5808-002` | ? | 7 | 2 | — | Consuming as consequence of moral/spiritual failure — person or community consumed by inner rebellion or hardness |
| `5809-001` | ? | 16 | 2 | — | Spent or failing inner self — strength, heart, life, or hope exhausted through grief, longing, or affliction |
| `5809-002` | ? | 10 | 2 | — | Spending or exhausting of God's inner wrath, anger, or fury in judgment — divine inner passion expressed to its limit |
| `5810-001` | ? | 16 | 2 | — | Full-end capacity of divine judgment and its deliberate restraint — expressions of God's inner moral character, whether  |
| `5811-001` | ? | 6 | 2 | — | Inner resolution or fixed determination — settled inner purpose that drives subsequent action |
| `5811-002` | ? | 4 | 2 | — | Soul's consuming longing — inner being spent in yearning for God, his salvation, and his word |
| `5812-001` | ? | 2 | 2 | — | Extreme or total quality of an inner state — unsearchable limit of God; completeness of inner moral orientation |
| `5949-001` | ? | 10 | 2 | — | Term names the transformation of the inner person — the heart, mind, or character overturned, renewed, or corrupted |
| `5949-002` | ? | 8 | 2 | — | Term names the transformation of inner experience — mourning turned to joy, or joy to mourning, as God acts |
| `5949-003` | ? | 7 | 2 | — | Term names God's inner orientation overturn — God's heart recoiling, his compassion stirred, or his disposition changing |
| `5949-004` | ? | 8 | 2 | — | Term names the moral perversion of justice or speech — the overturn of right into wrong as an inner-motivated moral act |
| `5951-001` | ? | 1 | 1 | — | Term names a divine overthrow that should have produced inner return — the overwhelming judgment designed to evoke repen |
| `5954-001` | ? | 1 | 1 | — | Term names a perverse contrariness — the inner orientation that inverts right relationship, giving what should not be gi |
| `6030-001` | ? | 22 | 2 | — | Term names the lifted heart — pride, forgetfulness of God, self-exaltation |
| `6030-002` | ? | 26 | 2 | — | Term names God exalting persons |
| `6030-003` | ? | 21 | 2 | — | Term names doxological exaltation of God |
| `6030-004` | ? | 8 | 2 | — | Term names divine reversal and justice through exaltation |
| `6084-001` | ? | 2 | 1 | — | Term names the edict or judgment as something that shapes inner disposition — delay in executing judgment hardens the he |
| `6211-001` | ? | 1 | 1 | — | Term names absence of restraint as the ground for inner confidence — nothing can hinder God from saving, which grounds J |
| `6511-001` | ? | 1 | 1 | — | Moral-cognitive inexperience — the state of being unskilled in the word of righteousness, designating inner formation de |
| `67-001` | ? | 8 | 1 | ✓ | Term names the Christ as the anointed one whose identity is the object of inner faith — the person of Jesus as the groun |
| `67-002` | ? | 9 | 1 | — | Term names union with Christ as the defining inner reality of the person — being in Christ as the location of the transf |
| `67-003` | ? | 5 | 1 | — | Term names the death and resurrection of Christ as the inner transformative foundation — Christ died for sins; this is r |
| `6700-001` | ? | 2 | 1 | — | Term names the incomprehensible as a quality of divine identity or knowledge that surpasses human inner capacity — evoki |
| `6709-001` | ? | 1 | 1 | — | Term names the true worshiper as a person defined by their inner-being orientation — worship in spirit and truth as the  |
| `6713-001` | ? | 1 | 1 | — | Term names deliberate inner intention or scheming — the inner act of purposing to change or overturn what is established |
| `6750-001` | ? | 6 | 2 | — | Term names the act of comparison — setting things side by side to establish worth, likeness, or incomparability, especia |
| `6750-002` | ? | 11 | 2 | — | Term names the inner act of setting forth a case or argument before God — the person marshalling their moral position, r |
| `6752-001` | ? | 9 | 2 | — | Term names the ordered arrangement of showbread set perpetually before the Lord — a covenant liturgical act expressing I |
| `6899-001` | ? | 27 | 2 | — | Ga.dal as magnification of God: inner-being act of praise and worship |
| `6899-002` | ? | 16 | 2 | — | Ga.dal as human self-magnification and pride against God |
| `6899-003` | ? | 31 | 2 | — | Ga.dal as growth of person in stature, standing, and divine favour |
| `6947-001` | ? | 2 | 2 | — | Transformation from judgment — ud as the prophetic figure of the person snatched from fire: the inner hardness confronte |
| `7029-001` | ? | 4 | 2 | — | Term names military force as the object of misplaced inner trust — where reliance on armies and warriors displaces trust |
| `7029-002` | ? | 3 | 2 | — | Term names God's army as the instrument of his sovereign power — in judgment, in deliverance, and as the eschatological  |
| `7031-001` | ? | 6 | 2 | — | Term names wealth as an object of inner trust, pride, or misplaced confidence — and its judgment as the ground of trust  |
| `7031-002` | ? | 2 | 2 | — | Term names wealth as the occasion for the heart's prideful self-inflation or joyful thanksgiving — wealth as moral revea |
| `7032-001` | ? | 6 | 2 | — | Term names the beast-state as a spiritual and cognitive debasement of the human person — the removal of the human mind a |
| `7032-002` | ? | 9 | 2 | — | Term names the beast form as the inner character of God-defying kingdoms — predatory, domineering, and opposed to God's  |
| `7034-001` | ? | 7 | 2 | — | Term names moral-character excellence as a quality of the inner person — the competence and capability that flows from i |
| `7068-001` | ? | 2 | 2 | — | Oikeios as relational belonging to household of faith or God |
| `7332-001` | ? | 1 | 1 | — | Term frames a simile that characterises a predatory inner disposition — eager to destroy and lying in wait |
| `736-001` | ? | 2 | 1 | — | Term names God's judicial acts as the consequence flowing from inner moral failure — the execution of judgment that refl |
| `739-001` | ? | 5 | 2 | — | Term names judgment as the coming event that orients and shapes the inner life — the fearful expectation of divine verdi |
| `743-001` | ? | 2 | 1 | — | Term names the inner state of contentment and sufficiency — the condition of the person whose inner life is settled and  |
| `7430-001` | ? | 3 | 2 | — | Inner-being commitment of dying together — loyalty and union through shared death including Christ |
| `7473-001` | ? | 1 | 1 | — | Term names the inner participation in creation's anguish — the corporate groan of all things awaiting redemption, shared |
| `7544-001` | ? | 1 | 1 | — | broken relational state as inner obstacle to authentic worship — reconciliation required |
| `7573-001` | ? | 1 | 1 | — | indelibly formed inner moral character depicted as fixed marking |
| `760-001` | ? | 1 | 1 | — | Term names the act of divine counsel as a call to attend to the inner condition — guidance that addresses the real pover |
| `765-001` | ? | 40 | 1 | — | God's covenant with creation and the patriarchs — unconditional divine inner commitment |
| `765-002` | ? | 76 | 1 | — | The Sinai/Mosaic covenant — bilateral covenant of law and obedience |
| `765-003` | ? | 15 | 1 | — | The new covenant — inner transformation through God's law written on the heart |
| `765-004` | ? | 17 | 1 | — | The Davidic covenant — everlasting covenant of steadfast love and kingship |
| `765-005` | ? | 13 | 1 | — | Covenant as bond of relational loyalty between persons — friendship, marriage, and inner moral integrity |
| `766-001` | ? | 17 | 1 | — | Covenant as God's relational bond through Christ's blood |
| `766-002` | ? | 5 | 1 | — | New covenant written on hearts — inner transformation |
| `766-003` | ? | 5 | 1 | — | Covenantal standing — identity defined by inclusion or exclusion |
| `83-001` | ? | 12 | 1 | ✓ | Term names the prolonging of life as covenantal promise — obedience to God's commands linked to length of days as the in |
| `83-002` | ? | 9 | 1 | — | Term names the inner disposition of patience or anger-restraint — slowness as a character quality prolonging relationshi |
| `84-001` | ? | 14 | 2 | ✓ | Term names slowness to anger as a divine and human inner disposition — the character of patient restraint that holds wra |
| `940-001` | ? | 21 | 2 | — | Soul's orientation toward God's mishpat — longing, delight, fear, praise, hope |
| `940-002` | ? | 44 | 2 | — | Moral-spiritual orientation of the heart — faithfulness, rebellion, or Spirit-enabled transformation |
| `940-003` | ? | 12 | 2 | — | Inner moral standard for human judgement — impartiality, righteousness, God-accountability |
| `940-004` | ? | 33 | 2 | — | Judicial arena where inner life meets divine justice — humility, complaint, vindication-hope |
| `940-005` | ? | 4 | 1 | — | Justice as spirit-given capacity for inner discernment and righteous action |
| `941-001` | ? | 22 | 1 | — | Judging as requiring inner moral discernment — righteousness, impartiality, God-accountability in the judge |
| `941-002` | ? | 20 | 2 | — | Inner appeal to God as judge — cry for divine vindication, justice, or moral verdict |
| `941-003` | ? | 21 | 2 | — | Divine judgement engaging inner moral condition — judged according to ways, wickedness, spiritual orientation |
| `941-004` | ? | 16 | 2 | — | God as righteous judge whose inner character is expressed through just acts — indignation, equity, faithfulness |
| `943-001` | ? | 11 | 2 | — | Term names the cause or right of the person — the just claim that calls for inner moral commitment from the judge and fr |
| `943-002` | ? | 6 | 2 | — | Term names divine and judicial verdict — the authoritative inner determination of guilt or innocence pronounced by God o |
| `999-001` | ? | 3 | 1 | — | Term names the restoration of sound mind — the inner rational and moral faculties recovered from disruption |
| `999-002` | ? | 3 | 1 | — | Term names sound-mindedness as a moral disposition — thinking about oneself and others with measured, humble judgment |
| `M26-A1-004` | M26-A1 | 41 | 1 | ✓ | Term names God's righteousness as the basis on which he acts to save, deliver, vindicate, and redeem — the quality that  |

### M01 (38 VCGs · status: Analysis Completed (Terms Added))

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `105-001` | ? | 1 | 1 | — | Term names terror or dismay — the inner condition of overwhelming dread in the face of what cannot be resisted or compre |
| `1153-001` | ? | 3 | 1 | — | Sudden panic and terror as inner affliction — the state of dismay, panic, and anguish that falls upon persons, including |
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
| `M01-BOUNDARY-VCG-01` | M01-BOUNDARY | 18 | 7 | — | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |
| `M01-C-VCG-01` | M01-C | 19 | 3 | ✓ | God deploys dread and terror ahead of Israel as an active weapon that paralyses enemy resistance before battle — an exte |
| `M01-C-VCG-02` | M01-C | 15 | 3 | — | Terror characterised as an active, hunting, encircling force that overwhelms the inner person with no escape — pursuing  |
| `M01-C-VCG-03` | M01-C | 9 | 2 | ✓ | Terror as the defining power wielded by great military empires over the land of the living — projected outward as the in |
| `M01-C-VCG-04` | M01-C | 22 | 5 | ✓ | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |
| `M01-C-VCG-05` | M01-A | 10 | 2 | — | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |
| `M01-D-VCG-01` | M01-B | 25 | 2 | ✓ | Dismay arising from receiving terrible news, witnessing catastrophe, or experiencing the withdrawal of God's presence —  |
| `M01-D-VCG-02` | M01-D | 14 | 1 | ✓ | Dismay inflicted by divine action as a form of judgment or punishment — God actively producing inner collapse in those w |
| `M01-D-VCG-03` | M01-D | 12 | 1 | ✓ | Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, han |
| `M01-D-VCG-04` | M01-D | 11 | 2 | ✓ | Meanings where dismay is explicitly forbidden or countered — Israel or prophets commanded not to be dismayed, with the g |
| `M01-D-VCG-05` | M01-B | 16 | 3 | ✓ | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |
| `M01-E-VCG-01` | M01-E | 15 | 2 | ✓ | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |
| `M01-E-VCG-02` | M01-A | 12 | 3 | ✓ | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |
| `M01-E-VCG-03` | M01-E | 15 | 3 | ✓ | Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities an |
| `M01-E-VCG-04` | M01-B | 39 | 4 | — | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| `M01-E-VCG-05` | M01-E | 10 | 4 | ✓ | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |
| `M01-E-VCG-06` | M01-E | 7 | 1 | — | NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in w |
| `M01-F-VCG-01` | M01-BOUNDARY | 9 | 2 | ✓ | Anxiety as a sustained, all-pervasive inner burden that saturates every moment and every ordinary activity — not trigger |
| `M01-F-VCG-02` | M01-F | 9 | 3 | ✓ | Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner |
| `M01-F-VCG-03` | M01-B | 10 | 1 | ✓ | Sustained dread specifically as a form of divine judgment — unrelenting, consuming anxiety that denies rest, distorts ti |
| `M01-F-VCG-04` | M01-A | 22 | 1 | ✓ | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| `M01-F-VCG-05` | M01-A | 8 | 1 | ✓ | A specific form of anticipatory dread characterised by Paul's protective apprehension about the spiritual welfare of his |
| `M01-G-VCG-01` | M01-G | 8 | 3 | ✓ | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |

### M02 (27 VCGs · status: Analysis Completed (Terms Added))

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `705-001` | ? | 3 | 1 | — | Bitterness as destructive inner state — disposition of hostility, resentment, or hardness that corrupts the person and d |
| `705-002` | ? | 1 | 1 | — | Bitterness as spreading inner root — deeply embedded condition that defiles and corrupts beyond the individual |
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
| `M02-BOUNDARY-VCG-01` | M02-BOUNDARY | 82 | 6 | — | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |
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
| `M04-A-VCG-03` | M04-A | 7 | 1 | — | Relational and natural gladness: rejoicing in human bonds, parental delight, creation's personified response. |
| `M04-B-VCG-01` | M04-B | 26 | 1 | ✓ | Festival and feast worship joy: prescribed communal gladness at appointed feasts directed toward God at his sanctuary. |
| `M04-B-VCG-02` | M04-B | 22 | 1 | ✓ | Sanctuary, temple, and ark joy: gladness at the sacred presence returning, established, or worship restored. |
| `M04-B-VCG-03` | M04-B | 21 | 1 | ✓ | Coronation, national, and civic deliverance joy: corporate gladness at legitimate kingship, military victory, or reversa |
| `M04-B-VCG-04` | M04-B | 64 | 1 | ✓ | Relational, personal, and wisdom-life gladness: joy in human bonds, parental delight, domestic life, Ecclesiastes life-e |
| `M04-B-VCG-05` | M04-B | 90 | 1 | ✓ | God-directed psalmist and prophetic gladness: sa.mach/sim.chah rejoicing explicitly toward God, from his saving acts, or |
| `M04-B-VCG-06` | M04-B | 59 | 2 | ✓ | Inverted, absent, corrupt, and judgment-silenced joy: misdirected, hollow, morally condemned, or divinely removed gladne |
| `M04-C-VCG-01` | M04-C | 27 | 4 | ✓ | Synoptic and incarnation joy: gladness at the messianic arrival, kingdom signs, lost-found parables, resurrection encoun |
| `M04-C-VCG-02` | M04-C | 15 | 1 | — | Johannine joy: indwelling, fullness, permanent gladness — Christ's own joy transferred to disciples, joy made complete. |
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
| `M04-J-VCG-01` | M04-J | 9 | 1 | — | Divine pleasantness and worship pleasantness: no.am/na.im as attribute of God's character, covenant favour, and the agre |
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
| `M04-P-VCG-03` | M04-P | 1 | 1 | — | Predatory exultation — a.li.tsut as sinister inner gladness in cruelty against the poor. Inner-being-as-corrupt-rejoicin |

### M05 (123 VCGs · status: Analysis Completed (Terms Added))

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
| `46-001` | M05-E | 4 | 1 | ✓ | Term names gentleness/meekness as an inner quality of the person — a settled inner disposition of mildness and strength- |
| `47-001` | M05-E | 4 | 1 | ✓ | Term names gentleness as an inner quality — the disposition that governs the reception of God's word, the exercise of wi |
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
| `567-001` | M05-A | 1 | 1 | ✓ | Term names love of brothers as an inner disposition among the virtues of the unified community |
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
| `14-001` | M06-C | 1 | 1 | ✓ | Term names the inner disposition of revulsion toward evil — what a person claims as morally repugnant, whether genuinely |
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
| `M07-A-VCG-05` | M07-A | 6 | 1 | — | Shame averted by trust, hope, and divine protection. Verses where shame is the present inner threat and trust in God is  |
| `M07-B-VCG-01` | M07-B | 39 | 1 | ✓ | Shame invoked on enemies as just reversal of their hostility. Verses where the psalmist or community calls shame upon en |
| `M07-B-VCG-02` | M07-B | 22 | 1 | ✓ | Shame from idolatry and false religious trust. Verses where shame falls as the direct consequence of idolatry, false wor |
| `M07-B-VCG-03` | M07-B | 32 | 1 | ✓ | Shame as natural fruit of personal and relational moral failure. Verses where shame is the direct, natural consequence o |
| `M07-B-VCG-04` | M07-B | 8 | 1 | ✓ | Absence of shame: the seared conscience and moral collapse. Verses evidencing the loss of the capacity for shame — those |
| `M07-B-VCG-05` | M07-B | 10 | 1 | ✓ | Corrective shame: blameless conduct, communal discipline, and shame as moral prod. Verses where shame is deployed instru |
| `M07-C-VCG-01` | M07-C | 19 | 1 | ✓ | Guilt-shame before the holy: the face that cannot be lifted. Verses where shame arises from guilt-consciousness before G |
| `M07-C-VCG-02` | M07-C | 16 | 1 | ✓ | Trust in God as shield against shame: refuge and word. Verses where taking refuge in God, holding to his testimonies, wa |
| `M07-C-VCG-03` | M07-C | 9 | 1 | ✓ | Corrective shame awakening conscience toward God. Verses where shame is deployed as an inward corrective force in the ve |
| `M07-C-VCG-04` | M07-C | 6 | 1 | ✓ | Promise: never put to shame in God's presence. Verses where the covenant or eschatological promise of not being put to s |
| `M07-D-VCG-01` | M07-D | 20 | 1 | — | Social and bodily humiliation: enforced downward movement in human community. Verses where humiliation operates through  |
| `M07-D-VCG-02` | M07-D | 20 | 1 | — | Military defeat and national collapse as humiliation. Verses where humiliation comes through military defeat, the collap |
| `M07-D-VCG-03` | M07-D | 27 | 1 | ✓ | Divine abasement of pride: God bringing the lofty low. Verses where humiliation is the direct, sovereign act of God agai |
| `M07-D-VCG-04` | M07-D | 5 | 1 | — | Shame carried into death and as enduring burden. Verses where humiliation is permanent — warriors descending to the pit  |
| `M07-E-VCG-01` | M07-E | 9 | 1 | — | Active dishonour: refusing or withdrawing due regard toward persons. Verses where dishonour is actively enacted through  |
| `M07-E-VCG-02` | M07-E | 6 | 1 | — | Assigned or structural dishonour: standing, nature, and received treatment. Verses where dishonour is assigned, structur |
| `M07-F-VCG-01` | M07-F | 10 | 1 | — | Shameful conduct and objects: the moral quality of what is shameful. Verses where conscience identifies conduct, speech, |
| `M07-F-VCG-02` | M07-F | 3 | 1 | — | Indecent desires and moral disorder: disordered inner appetite. Verses where the shameful characteristic is located in d |
| `M07-F-VCG-03` | M07-F | 3 | 1 | — | Inverted conscience: glorying in shame and the perverted evaluative faculty. Verses where the moral-evaluation apparatus |
| `M07-G-VCG-01` | M07-G | 13 | 1 | — | Dismissive contempt as inner attitude: treating persons as of no account. Verses where the contempt-producing-shame mech |
| `M07-G-VCG-02` | M07-G | 6 | 1 | — | Active contempt expressed through violence, mockery, and rejection. Verses where contempt is enacted through physical vi |
| `M07-G-VCG-03` | M07-G | 5 | 1 | — | Verbal contempt and reputation attack as shaming mechanism. Verses where shame is produced through speech — verbal attac |
| `M07-H-VCG-01` | M07-H | 4 | 1 | — | Innocence as active inner defence: clean conscience before God and persons. Verses where innocence — the integrity of wi |
| `M07-H-VCG-02` | M07-H | 4 | 1 | — | Innocence questioned and incapacity for innocence. Verses where the innocence-shame polarity is evidenced through the qu |

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
| `M09-A-VCG-02` | M09-A | 6 | 1 | — | The Greek NT register of the verbal act of self-humbling (tapeinoō) directed Godward, where the willed downward movement |
| `M09-A-VCG-03` | M09-A | 3 | 1 | ✓ | The costlier, service-register expression of willed self-lowering: humility as the inner quality of self-giving in vocat |
| `M09-A-VCG-04` | M09-A | 6 | 1 | ✓ | The relational-disposition register of humility — as a quality of inner bearing toward God and community, contrasted wit |
| `M09-A-VCG-05` | M09-A | 5 | 1 | ✓ | The Pauline epistolary register of tapeinofrosunē — humility as a chosen, genuine inner character disposition placed alo |
| `M09-B-VCG-01` | M09-B | 4 | 1 | — | The register of externally-imposed humbling where God is the agent and the person or people experience being brought low |
| `M09-B-VCG-02` | M09-B | 5 | 1 | — | The register of lowliness as a social or existential condition that stands in relation to divine reversals, reframings,  |
| `M09-B-VCG-03` | M09-B | 4 | 1 | — | The register of lowliness as an experienced inner state produced by affliction, suffering, circumstance, or God's action |
| `M09-C-VCG-01` | M09-C | 5 | 1 | ✓ | The register of submission as inner allegiance of the will — the will's habitual yielding discloses and constitutes whos |
| `M09-C-VCG-02` | M09-C | 4 | 1 | — | The cognitive-volitional register of submission — obedience named in the mind's capture, the conscience's deliberation,  |
| `M09-C-VCG-03` | M09-C | 4 | 1 | — | The register of submission-as-genuine-inner-motive — verses that explicitly distinguish sincere, God-ward inner complian |
| `M09-C-VCG-04` | M09-C | 4 | 1 | ✓ | The register of submission as something acquired, transformative, or costly at the deepest levels of the inner person. C |
| `M09-D-VCG-01` | M09-D | 8 | 1 | ✓ | The gospel-obedience register — obedience of faith as both the response to gospel proclamation and the defining characte |
| `M09-D-VCG-02` | M09-D | 5 | 1 | ✓ | The register of obedience as soteriological and sanctifying telos — the orientation of the will that connects the person |
| `M09-D-VCG-03` | M09-D | 4 | 1 | ✓ | The household and relational register of the submission-obedience pattern — obedience as a shaped quality within the aut |
| `M09-D-VCG-04` | M09-D | 2 | 1 | — | The personal and eschatological allegiance register — obedience as a directed disposition of will toward a named authori |
| `M09-E-VCG-01` | M09-E | 2 | 1 | ✓ | The full contrition register — the acute, grief-laden inner brokenness of spirit that follows genuine confrontation with |
| `M09-F-VCG-01` | M09-F | 2 | 1 | ✓ | The meekness and gentleness characteristic — holding force, capability, or will in calibrated, measured expression. The  |
| `M09-G-VCG-01` | M09-G | 3 | 1 | ✓ | The full dignity characteristic — settled moral seriousness and gravitas that grounds composed, non-self-displaying cond |
| `M09-H-VCG-01` | M09-H | 4 | 1 | ✓ | The register of willing-heartedness as the freely-moved inner disposition driving offering and service without external  |
| `M09-H-VCG-02` | M09-H | 1 | 1 | ✓ | The distinctive register of willing-heartedness as a divine gift that must be sought and may be lost — evidenced in Psa5 |

### M10 (68 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M10-C-VCG-01` | M10-C | 30 | 1 | — | Sinner as social-moral category: exclusion and stigma |
| `M10-C-VCG-02` | M10-C | 20 | 1 | — | Sinner as constituted moral identity: imputed and declared status |
| `M10-C-VCG-03` | M10-C | 14 | 1 | — | Sinner as extreme moral type: habitual wrongdoing defining total character |
| `M10-D-VCG-01` | M10-D | 18 | 1 | — | Guilt-recognition: conscience engaging after the act |
| `M10-D-VCG-02` | M10-D | 19 | 1 | — | Guilt as accumulated weight: communal and personal burden mounting |
| `M10-D-VCG-03` | M10-D | 16 | 1 | — | Guilt as transferable burden: borne on behalf of another |
| `M10-D-VCG-04` | M10-D | 18 | 1 | — | Guilt's punitive consequence: the burden of punishment borne |
| `M10-D-VCG-05` | M10-D | 26 | 1 | — | Guilt exposed, indelible, and removed: the divine perspective |
| `M10-E-VCG-01` | M10-E | 17 | 1 | — | Priestly and cultic bearing of iniquity |
| `M10-E-VCG-02` | M10-E | 18 | 1 | — | Generational iniquity: transmitted across family lines |
| `M10-E-VCG-03` | M10-E | 28 | 1 | — | Iniquity in divine memory: what God sees and does not forget |
| `M10-E-VCG-04` | M10-E | 29 | 1 | — | Iniquity as personal moral crime: individually owned and judged |
| `M10-E-VCG-05` | M10-E | 30 | 1 | — | Iniquity as overwhelming accumulated weight |
| `M10-E-VCG-06` | M10-E | 21 | 1 | — | Iniquity pardoned and removed: divine forgiveness resolves the moral debt |
| `M10-E-VCG-07` | M10-E | 15 | 1 | — | Iniquity as self-destructive force: the inner crime that ruins from within |
| `M10-E-VCG-08` | M10-E | 4 | 1 | — | Iniquity heart-seated: the crime originating in the will |
| `M10-F-VCG-01` | M10-F | 27 | 1 | — | Transgression against God: rebellion in the divine-covenant relationship |
| `M10-F-VCG-02` | M10-F | 7 | 1 | — | Revolt: the inner defiance that speaks and acts against God |
| `M10-F-VCG-03` | M10-F | 13 | 1 | — | Accumulated transgression crossing the threshold of divine tolerance |
| `M10-F-VCG-04` | M10-F | 15 | 1 | — | Transgression as law-violation: the NT parabasis/parabatēs register |
| `M10-F-VCG-05` | M10-F | 5 | 1 | — | Adam-paradigm transgression: the foundational boundary-crossing |
| `M10-F-VCG-06` | M10-F | 13 | 1 | — | Transgression pardoned and erased: divine forgiveness of rebellion |
| `M10-F-VCG-07` | M10-F | 14 | 1 | — | Transgression's oppressive weight: the burden that crushes and enslaves |
| `M10-F-VCG-08` | M10-F | 19 | 1 | — | Transgression as interpersonal breach: wrong done between persons |
| `M10-F-VCG-09` | M10-F | 34 | 1 | — | Transgression as personal moral breach: Job, Psalms, and wisdom |
| `M10-G-VCG-01` | M10-G | 57 | 1 | — | Unfaithfulness toward God: covenant-betrayal directed upward (M13+M31) |
| `M10-G-VCG-02` | M10-G | 34 | 1 | — | Relational treachery: faithlessness between persons (M13+M31) |
| `M10-G-VCG-03` | M10-G | 10 | 1 | — | Treachery as constitutional inner character (M13+M31) |
| `M10-H-VCG-01` | M10-H | 10 | 1 | — | Perversity of speech: the tongue as vehicle of moral inversion |
| `M10-H-VCG-02` | M10-H | 6 | 1 | — | Perversion of judgment: bribery corrupting discernment |
| `M10-H-VCG-03` | M10-H | 19 | 1 | — | Perversion of mind, will, and way: the inwardly twisted person |
| `M10-H-VCG-04` | M10-H | 4 | 1 | — | Sexual perversion and moral degeneracy (M23/M35 bodily-decay) |
| `M10-H-VCG-05` | M10-H | 25 | 1 | — | Moral corruption, decay, and lewdness (M03 cha.val/a.vah; M07 nav.lut) |
| `M10-I-VCG-01` | M10-I | 20 | 1 | — | Judicial and commercial injustice: the corruption of right process (M26) |
| `M10-I-VCG-02` | M10-I | 33 | 1 | — | Injustice as oppression and harm to persons (M26) |
| `M10-I-VCG-03` | M10-I | 19 | 1 | — | Character of the unjust person: adikos, av.val, a.vil, adikēma (M26) |
| `M10-J-VCG-01` | M10-J | 32 | 1 | — | Sin directed against God: the vertical relational offense |
| `M10-J-VCG-02` | M10-J | 18 | 1 | — | Sin against the neighbour: the horizontal relational offense |
| `M10-J-VCG-03` | M10-J | 19 | 1 | — | Sin deterred, restrained, or denied |
| `M10-J-VCG-04` | M10-J | 17 | 1 | — | Sin requiring ritual remedy: the cultic-atonement register |
| `M10-J-VCG-05` | M10-J | 12 | 1 | — | NT wilful sinning: hamartanō and paraptōma in M10-J |
| `M10-K-VCG-01` | M10-K | 10 | 1 | — | Unintentional sin and moral surprise: conscience engaged after the fact |
| `M10-K-VCG-02` | M10-K | 8 | 1 | — | Cultic purification: the ritual-cleansing register |
| `M10-L-VCG-01` | M10-L | 23 | 1 | — | Individual confession: the will naming its own sin |
| `M10-L-VCG-02` | M10-L | 10 | 1 | — | Corporate and communal confession |
| `M10-L-VCG-03` | M10-L | 1 | 1 | — | Confession without transformed will: the hollow acknowledgment |
| `M10-M-VCG-01` | M10-M | 8 | 1 | — | Conscience suppression and self-blindness |
| `M10-N-VCG-01` | M10-N | 18 | 1 | — | Refusal to repent: departure withheld |
| `M10-O-VCG-01` | M10-O | 14 | 1 | — | Habitual defection: the will's settled pattern toward sin |
| `M10-P-VCG-01` | M10-P | 19 | 1 | — | Contagious sin: leadership transmitting moral defection |
| `M10-Q-VCG-01` | M10-Q | 9 | 1 | — | Political revolt: wilful defection from governing relationship |
| `M10-R-VCG-01` | M10-R | 9 | 1 | ✓ | Slander and abusive speech: heart-generated inner corruption (M06) |
| `M10-R-VCG-02` | M10-R | 7 | 1 | — | Blasphemy as divine-authority claim: presumptuous usurpation (M06) |
| `M10-R-VCG-03` | M10-R | 6 | 1 | — | Blasphemy as identity: the beast's constitutive defiance (M06) |
| `M10-S-VCG-01` | M10-S | 5 | 1 | — | Specialised sinful mechanisms: desire exploited (M14), appearance falsified (M08), identity abandoned (M31) |
| `M10-T-VCG-01` | M10-T | 5 | 1 | — | Wickedness as defining inner condition (rish.ah, al.vah) |
| `M10-T-VCG-02` | M10-T | 39 | 1 | — | Sin forgiven and addressed: the NT redemption register |
| `M10-T-VCG-03` | M10-T | 68 | 1 | — | Sin as enslaving and dominating power (Rom 6-7) |
| `M10-U-VCG-01` | M10-U | 9 | 1 | — | Sin as enslaving power: the will under bondage |
| `M10-V-VCG-01` | M10-V | 32 | 1 | — | Chet: personal moral liability before God |
| `M10-V-VCG-02` | M10-V | 9 | 1 | — | Cha.ta.ah: sin as objective moral category requiring covering |
| `M10-V-VCG-03` | M10-V | 5 | 1 | — | Sin under divine scrutiny: Job's surveillance register |
| `M10-V-VCG-04` | M10-V | 46 | 1 | — | Jeroboam-sin legacy: the named sin as recorded pattern |
| `M10-V-VCG-05` | M10-V | 113 | 1 | — | Sin as objective burden before God: the broad chat.tat record |
| `M10-W-VCG-01` | M10-W | 12 | 1 | — | Priestly atonement: kip.pu.rim and chat.tat sin-offering (M11) |
| `M10-W-VCG-02` | M10-W | 12 | 1 | — | Forgiveness declared by Jesus and through Christ's blood (M11) |
| `M10-W-VCG-03` | M10-W | 10 | 1 | — | Forgiveness sought through the Levitical sacrificial-atonement system (M11) |
| `M10-X-VCG-01` | M10-X | 8 | 1 | — | Generational sin: the ancestral moral condition inherited |

### M10b (36 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `M10b-A-VCG-01` | M10b-A | 5 | 1 | ✓ | Forensic-verdict register — mandatory polysemy VCG. Verses where ra.sha functions as a legal-status label in forensic/ju |
| `M10b-A-VCG-02` | M10b-A | 8 | 1 | ✓ | Practical atheism — God excluded from the inner mind of the wicked. The wicked person's defining inner characteristic is |
| `M10b-A-VCG-03` | M10b-A | 22 | 1 | — | Pride as inner engine and directed hostility of the wicked. Two closely related registers: pride as the inner engine of  |
| `M10b-A-VCG-04` | M10b-A | 18 | 1 | ✓ | Moral contrast — wickedness defined against the inner status of the righteous. Verses where the wicked person is defined |
| `M10b-A-VCG-05` | M10b-A | 30 | 1 | ✓ | Wickedness condemned, exposed, and publicly judged. Verses where the wicked person's inner character draws visible, publ |
| `M10b-A-VCG-06` | M10b-A | 21 | 1 | — | Wickedness as inner instability and self-destruction. Verses where wickedness is shown to be internally unstable — a con |
| `M10b-A-VCG-07` | M10b-A | 22 | 1 | ✓ | Wickedness as directional orientation — a way the will can turn from. The Ezekiel corpus on wickedness as a volitional d |
| `M10b-A-VCG-08` | M10b-A | 12 | 1 | ✓ | Wickedness expressed through speech — concealment, corruption, and social destruction. Verses where the wicked person's  |
| `M10b-A-VCG-09` | M10b-A | 33 | 1 | — | Wickedness against divine justice — the wicked person's soul, appetites, and moral hollowness. The Proverbs-heavy corpus |
| `M10b-A-VCG-10` | M10b-A | 9 | 1 | — | Job's theological debate — the wicked in the crucible of theodicy. The Job corpus addressing the wicked in the context o |
| `M10b-A-VCG-11` | M10b-A | 10 | 2 | ✓ | re.sha and mir.sha.at — wickedness as abstract condition and the wicked collective. The re.sha corpus (abstract noun: wi |
| `M10b-B-VCG-01` | M10b-B | 13 | 1 | ✓ | Cosmic evil — the evil one, the evil age — mandatory polysemy VCG. Verses where evil names a cosmic, supra-personal powe |
| `M10b-B-VCG-02` | M10b-B | 8 | 1 | — | Constitutional evil — human nature bent toward corruption as baseline condition. Verses where evil names the constitutio |
| `M10b-B-VCG-03` | M10b-B | 8 | 1 | — | The heart as treasury — the inner source and generative organ of evil. Verses where the heart is explicitly named as the |
| `M10b-B-VCG-04` | M10b-B | 17 | 1 | — | Evil as settled deep character of persons. Verses where evil names the settled, characterological identity of persons —  |
| `M10b-B-VCG-05` | M10b-B | 20 | 3 | — | Settled inner malice, entrenched badness, and deep hostile residue — kakia, ponēria, adikia saturation. Verses where the |
| `M10b-B-VCG-06` | M10b-B | 24 | 2 | — | Evil conscience, moral accountability, progressive deterioration, and abhorrence of evil. Verses addressing moral accoun |
| `M10b-C-VCG-01` | M10b-C | 10 | 1 | — | Ethical and character-orientation abomination — dishonest commercial practice, unjust social dealings, and the character |
| `M10b-C-VCG-02` | M10b-C | 9 | 2 | — | Pride, crooked heart, and hidden corruption as abomination. Abomination located most directly in the interior life — pri |
| `M10b-C-VCG-03` | M10b-C | 4 | 1 | — | Corrupt worship — the unclean inner person's religious act as abomination. The religious act (sacrifice, incense, prayer |
| `M10b-C-VCG-04` | M10b-C | 11 | 1 | — | The silenced and awakening conscience before abomination. The faculty of conscience in its various states in relation to |
| `M10b-C-VCG-05` | M10b-C | 6 | 1 | — | Identity and choice constituted by abomination. Abomination as a category defined by divine declaration (Pro 6:16), the  |
| `M10b-D-VCG-01` | M10b-D | 6 | 1 | — | Levitical boundary-laws — abomination as category-violation against created order. The Levitical corpus declaring specif |
| `M10b-D-VCG-02` | M10b-D | 14 | 1 | — | Deuteronomic warnings — the will that must actively resist abominable practices. The Deuteronomic corpus warning against |
| `M10b-D-VCG-03` | M10b-D | 17 | 1 | — | Historical reform narratives — kings institutionalising or purging idolatrous abominations. The historical narratives wh |
| `M10b-D-VCG-04` | M10b-D | 14 | 1 | — | Jeremiah and the Prophets — idolatrous objects installed and the will's stubbornness. The prophetic corpus outside Ezeki |
| `M10b-D-VCG-05` | M10b-D | 43 | 1 | — | Ezekiel — idolatry driving the divine presence away from the sanctuary. Ezekiel's concentrated corpus where accumulated  |
| `M10b-D-VCG-06` | M10b-D | 5 | 1 | — | Sacrilegious desolation and apocalyptic abomination. The eschatological and apocalyptic verses where abomination names a |
| `M10b-E-VCG-01` | M10b-E | 7 | 1 | — | Trouble and distress as the affliction of evil — mandatory polysemy VCG. Verses where a.ven names the trouble, afflictio |
| `M10b-E-VCG-02` | M10b-E | 14 | 1 | ✓ | Iniquity as deliberate inner generation — conceived, devised, schemed. Verses where iniquity is most clearly an active g |
| `M10b-E-VCG-03` | M10b-E | 24 | 1 | — | Evildoers as a defined inner-character class. Verses where iniquity defines a recognisable class of persons whose habitu |
| `M10b-E-VCG-04` | M10b-E | 23 | 1 | — | Iniquity as stored condition — harboured, accumulated, concealed, and exposed. Verses where iniquity is treated as a sto |
| `M10b-E-VCG-05` | M10b-E | 11 | 1 | — | Evil deeds as the outward expression of an inwardly-defiled source. The ro.a evil-deeds corpus — verses where the focus  |
| `M10b-F-VCG-01` | M10b-F | 6 | 1 | — | Hardened defiance and contemptuous blasphemy against God. This VCG groups the verses in which blasphemy is the direct ex |
| `M10b-F-VCG-02` | M10b-F | 5 | 1 | — | Blasphemy as social defamation — moral failure causing dishonour to God's name. This VCG groups the verses in which blas |
| `M10b-F-VCG-03` | M10b-F | 6 | 2 | — | Wrongdoing as a charged and contested category — false accusation and legal-offense register. This VCG groups the verses |

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
| `M10c-C-VCG-04` | M10c-C | 6 | 1 | — | The heart-allegiance dimension of moral-inner defilement — impurity equated with idolatry, arising from a heart that has |
| `M10c-C-VCG-05` | M10c-C | 3 | 1 | ✓ | The positive-inverse register — the inner-being condition of those who have not defiled themselves, maintained through c |
| `M10c-D-VCG-01` | M10c-D | 23 | 1 | — | The defilement-state produced by sexual violations of covenantal bonds — adultery, bestiality, violation of a person, tr |
| `M10c-D-VCG-02` | M10c-D | 24 | 1 | ✓ | The defilement-state produced by the will's pursuit of idolatrous attachment — habitual devotion to false gods, spiritua |
| `M10c-D-VCG-03` | M10c-D | 10 | 1 | ✓ | Defilement inflicted on or threatening the sanctuary — by enemy invasion, by deliberate installation of idols and abomin |
| `M10c-D-VCG-04` | M10c-D | 9 | 1 | ✓ | Defilement extending from persons or community to the land itself — the moral-sacral pollution of shared inhabitable spa |
| `M10c-D-VCG-05` | M10c-D | 17 | 1 | — | The consequences of corporate defilement projected into the physical and social condition of the people — expulsion, exi |
| `M10c-E-VCG-01` | M10c-E | 8 | 1 | — | The inner-being condition of the person inhabited and dominated by an unclean spirit — will overridden, bodily agency lo |
| `M10c-E-VCG-02` | M10c-E | 8 | 1 | — | The expulsion event and its dynamics — violent departure through convulsion and outcry, destructive transfer, vocal resi |
| `M10c-E-VCG-03` | M10c-E | 5 | 1 | ✓ | The commissioning of authority over unclean spirits and the spirits' recognition of divine power. Unclean spirits are ho |

### M11 (26 VCGs · status: Parked - Methodology Review)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1094-001` | ? | 1 | 1 | — | Term names the covenantal casting away of a people and its inner-relational consequence — the loss carries redemptive si |
| `3169-001` | ? | 60 | 2 | — | Term names the priestly/ritual act by which human guilt is covered before God and forgiveness granted — atonement as the |
| `3169-002` | ? | 12 | 2 | — | Term names God's direct act of forgiving and covering iniquity — atonement as divine grace beyond or fulfilling the ritu |
| `3169-003` | ? | 9 | 2 | — | Term names interpersonal or communal appeasement — covering relational offence or bloodguilt between persons or before G |
| `446-001` | ? | 4 | 1 | — | Term names human relenting — the inner change of heart toward repentance before God or reversal of a previous dispositio |
| `446-002` | ? | 30 | 2 | — | Term names divine relenting — God's inner-being disposition changing in response to human repentance or intercession, tu |
| `450-001` | ? | 7 | 1 | — | Term names the inner act of recalling and turning to mind — deliberate inner movement of memory and reflection that lead |
| `4701-001` | ? | 2 | 1 | — | Term names the blotting out of sin as the erasure of the inner record — anointing-reversal as the act of forgiveness tha |
| `4701-002` | ? | 2 | 1 | — | Term names the eschatological wiping away of tears and sorrow — the final reversal of all inner suffering in the renewed |
| `5376-001` | ? | 13 | 1 | — | Term names the deliberate inner act of leaving — forsaking possessions, family, or prior obligations for the sake of dis |
| `5376-002` | ? | 9 | 1 | — | Term names the abandonment of what is owed — leaving a spouse, neglecting the weightier matters of the law, or forsaking |
| `5376-003` | ? | 10 | 1 | — | Term names the relational priority inherent in the leave/stay act — leaving a gift to seek reconciliation first, leaving |
| `5377-001` | ? | 26 | 1 | — | Term names God's act of releasing a person from the guilt and penalty of sin — the vertical forgiveness that restores th |
| `5377-002` | ? | 11 | 1 | — | Term names the human act of forgiving another — the horizontal release of an offender from the inner claim of the offend |
| `5378-001` | ? | 12 | 1 | — | Term names the act of permitting or granting access as an inner-being posture — the receptivity, welcome, or restraint t |
| `5378-002` | ? | 6 | 1 | — | Term names the withholding of permission as an act reflecting the inner-being condition of the actor — whether as spirit |
| `5379-001` | ? | 13 | 1 | — | Term names God's act of forgiving sin as the outcome of atonement — the cultic and covenantal restoration of the person' |
| `5379-002` | ? | 17 | 1 | — | Term names the intercession for divine forgiveness — the act of seeking God's pardon on behalf of oneself or others, and |
| `5379-003` | ? | 15 | 1 | — | Term names God's promised and proclaimed forgiveness in the new covenant context — the unconditional covenantal act by w |
| `5380-001` | ? | 1 | 1 | — | Term names forgiveness as a characteristic attribute of God's inner being — the disposition of readiness to pardon that  |
| `6114-001` | ? | 5 | 1 | — | Term names the act of reconciliation — the active work of restoring broken inner-relational standing, whether between Go |
| `6548-001` | ? | 1 | 1 | — | Inner steadfastness in the face of external snare — not forgetting the law as an act of inner faithfulness despite const |
| `7543-001` | ? | 3 | 1 | — | divine reconciliation transforming relational enmity and moral standing before God |
| `879-001` | ? | 13 | 1 | — | Term names forgiveness of sins as the spiritual transaction through which the inner person is released from guilt and re |
| `879-002` | ? | 3 | 1 | — | Term names the absolute limit of forgiveness — the unforgivable sin against the Holy Spirit, and the conditions under wh |
| `880-001` | ? | 3 | 1 | — | Term names forgiveness as a divine attribute and possession — a quality that belongs to God's character, that grounds th |

### M12 (58 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1062-001` | ? | 2 | 1 | — | Term names moral and relational purity as an inner character disposition — the quality of heart and motivation governing |
| `1063-001` | ? | 6 | 1 | — | Term describes the purity of the heart and inner person as moral and spiritual integrity before God — an inner life free |
| `1063-002` | ? | 3 | 1 | — | Term describes purity attributed to God's word and the fear of the Lord — the quality of inner spiritual integrity that  |
| `1063-003` | ? | 6 | 1 | — | Term describes the covenantal and spiritual restoration of the inner person — being made clean before God through divine |
| `1063-004` | ? | 43 | 1 | — | Term describes ritual/levitical cleanness as a covenantal condition governing access to God and sacred space — the state |
| `1064-001` | ? | 1 | 1 | — | Term names purity as an inner character quality among the dispositions through which authentic apostolic ministry is exp |
| `1125-001` | ? | 1 | 1 | — | Term names the inner-moral condition of sinlessness — the state of being without transgression, functioning as a criteri |
| `1229-001` | ? | 16 | 2 | — | Term names acquittal or the withholding of punishment — the inner-being state of being declared innocent before God or o |
| `15-001` | ? | 1 | 1 | — | Term names the anointing of inner perception — the invitation to receive what opens the eyes of the heart to see one's t |
| `18-001` | ? | 2 | 1 | ✓ | Term names the anointing of the eyes as the restoration of inner perception — the outer act whose purpose is the return  |
| `2426-001` | ? | 2 | 1 | — | Term names guiltlessness — the inner moral condition of innocence recognised and vindicated by God, whose condemnation r |
| `3178-001` | ? | 3 | 2 | — | Term names holiness as an inner moral quality of the person — the character of being set apart inwardly from defilement, |
| `3179-001` | ? | 2 | 2 | — | Term names unholiness as an inner character disposition — among the catalogue of inner moral failures marking those outs |
| `4867-001` | ? | 7 | 2 | — | Term names the dedication of persons or places to God as an expression of covenantal belonging — the act of setting some |
| `4870-001` | ? | 7 | 2 | — | Term names the manifestation of divine holiness — the revealing of God's inner character of holiness before the nations  |
| `4877-001` | ? | 7 | 2 | — | Term designates those whose inner life is set apart to God — the holy person or saint whose character, orientation, and  |
| `4996-001` | ? | 1 | 1 | — | Purity — the absence of deceit as the quality of what the inner person longs for |
| `5312-001` | ? | 2 | 1 | — | Innocence as inner character — guileless purity and vulnerability to deception |
| `5545-001` | ? | 6 | 1 | — | Term names genuineness as an inner quality — the absence of outward performance disconnected from inner reality; love, f |
| `5575-001` | ? | 18 | 1 | — | Term names the physical or ritual act of cleansing — the healing of leprosy or the purification of ritual impurity, whic |
| `5575-002` | ? | 11 | 2 | — | Term names the inner cleansing — the purification of the conscience, heart, hands, and soul from sin and defilement |
| `5576-001` | ? | 9 | 1 | — | Term names purity as an inner quality of the person — a clean heart, clear conscience, or pure motivation, which is the  |
| `5576-002` | ? | 9 | 1 | — | Term names cleanness as a status conferred by Christ or declared by God — the removal of defilement so that the person s |
| `5577-001` | ? | 6 | 1 | — | Term names the act of purification — whether ritual or atoning, naming the process by which impurity is removed from the |
| `5582-001` | ? | 28 | 1 | — | Term names uncleanness as a condition separating the person from God and community — whether ritual impurity requiring c |
| `5621-001` | ? | 18 | 2 | — | Term characterizes the person as morally innocent or free from guilt — the inner moral standing of a person before God a |
| `5621-002` | ? | 14 | 2 | — | Term identifies "innocent blood" as a moral category — the shedding of which constitutes moral pollution and the protect |
| `5621-003` | ? | 7 | 2 | — | Term marks freedom from moral obligation or liability — clearance from a sworn commitment, legal claim, or culpability |
| `5624-001` | ? | 18 | 2 | — | Term characterizes the person as morally innocent or free from guilt — the inner moral standing of a person before God a |
| `5624-002` | ? | 14 | 2 | — | Term identifies "innocent blood" as a moral category — the shedding of which constitutes moral pollution and the protect |
| `5624-003` | ? | 7 | 2 | — | Term marks freedom from moral obligation or liability — clearance from a sworn commitment, legal claim, or culpability |
| `5637-001` | ? | 27 | 2 | — | Term characterizes the person as inwardly blameless and whole before God — the quality of heart and conduct that constit |
| `5641-001` | ? | 3 | 1 | — | Term names the absence of soundness as the condition of the person or people under divine discipline or moral corruption |
| `5642-001` | ? | 1 | 1 | — | Term names the Thummim as the instrument of divine disclosure of inner moral guilt — the means by which God reveals what |
| `5815-001` | ? | 1 | 1 | — | Limit of human perfection perceived by the discerning inner mind — set against the inexhaustible scope of God's commandm |
| `5948-001` | ? | 4 | 1 | — | Term names moral or ritual defilement — the corruption or staining of the inner person (mind, conscience) or the body as |
| `6053-001` | ? | 5 | 1 | — | Term describes the morally pure inner character — the quality of heart, mind, and motivation that is free from defilemen |
| `6053-002` | ? | 3 | 1 | — | Term describes relational and covenantal purity — inner disposition of fidelity and undivided orientation in relationshi |
| `6054-001` | ? | 3 | 1 | — | Term names the act of inner moral and spiritual purification — soul, heart, and self purified through obedience, hope, a |
| `6054-002` | ? | 4 | 1 | — | Term names ritual purification as an act of preparation expressing inner orientation of readiness and covenantal reveren |
| `6055-001` | ? | 1 | 1 | — | Term names the structured purification process as an act of ritual preparation expressing inner readiness and covenantal |
| `6057-001` | ? | 11 | 1 | — | Term describes the purification of the inner person from sin and moral defilement — the heart and soul made pure through |
| `6057-002` | ? | 43 | 1 | — | Term describes ritual cleansing as a covenantal act of transition — the person made ritually clean through prescribed ac |
| `6057-003` | ? | 17 | 1 | — | Term describes God's purifying action upon priests, Levites, and people — cleansing for restored covenantal service and  |
| `6058-001` | ? | 8 | 1 | — | Term names the prescribed purification procedure as the covenantal pathway governing a person's return to community and  |
| `6058-002` | ? | 3 | 1 | — | Term names purification as a covenantal service and inner-oriented commitment — the person setting their heart toward Go |
| `6059-001` | ? | 3 | 1 | — | Term names the ritual period of purification following childbirth — the covenantal state of the post-partum woman and he |
| `6060-001` | ? | 1 | 1 | — | Term describes the absolute moral purity of God's character — an inner quality of divine nature that is incompatible wit |
| `6061-001` | ? | 3 | 1 | — | Term names the ritual purification period as a state of cleansing — the post-partum woman's covenantal condition during  |
| `6231-001` | ? | 2 | 1 | — | Term names inner purity or sincerity — the quality of being unmixed, genuine, and morally uncontaminated in inner dispos |
| `7377-001` | ? | 1 | 1 | — | Term describes the interior formation of Christ within the person — a process of inner shaping toward Christ-likeness |
| `741-001` | ? | 4 | 2 | — | Term names the divine act of consecrating persons — setting them apart through his own holiness to belong to him, consti |
| `741-002` | ? | 10 | 2 | — | Term names the inner act of consecrating oneself — the voluntary self-dedication and orientation of the whole person tow |
| `741-003` | ? | 7 | 2 | — | Term names the sanctification of time — keeping the Sabbath holy as an inner orientation of the person toward the rhythm |
| `934-001` | ? | 5 | 2 | — | Term characterises God's way, works, and knowledge as perfect — the inner perfection of divine character and action as t |
| `934-002` | ? | 1 | 1 | — | Term characterises the Torah as perfect — its completeness as the source of inner renewal of the soul |
| `935-001` | ? | 4 | 2 | — | Term names the eschatological transformation of the person — the putting on of incorruptibility and immortality at resur |
| `935-002` | ? | 2 | 2 | — | Term names incorruptibility as the quality of inner love and the inner orientation of those who seek God's glory |

### M13 (46 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1126-001` | ? | 3 | 1 | — | Term names sincerity as an inner quality of unmixed, genuine motivation — the condition of acting from pure inner integr |
| `1197-001` | ? | 8 | 1 | — | Truth as transforming/shaping force on the inner person — sanctification, purification, self-orientation |
| `1197-002` | ? | 18 | 1 | — | Truth as the proper object of the will — accepting, obeying, refusing, or rejecting truth as inner act |
| `1197-003` | ? | 18 | 1 | — | Truth as inner quality of character — integrity, authenticity, living and speaking truthfully |
| `1197-004` | ? | 6 | 1 | — | Truth as the Spirit's identity and work in the inner person — Spirit of truth |
| `1197-005` | ? | 12 | 1 | — | Truth as relational/theological identity — who Christ is; worship in spirit and truth |
| `1197-006` | ? | 14 | 1 | — | Truth as the gospel received inwardly — knowledge of truth as saving and formational event |
| `1216-001` | ? | 37 | 1 | — | Regnal moral assessment — "did right/what was right in the eyes of the Lord" — moral orientation of the will under divin |
| `1216-002` | ? | 8 | 1 | — | "Right in his own eyes" — moral self-determination; inner conscience as its own arbiter |
| `1216-003` | ? | 46 | 1 | — | "The upright" / "upright in heart" — uprightness as stable inner moral character, especially in Psalms and Proverbs |
| `1216-004` | ? | 6 | 1 | — | Uprightness as divine character — God and his word described as upright/right |
| `1216-005` | ? | 9 | 1 | — | Job as the upright man — blameless and upright as defining inner character under testing |
| `1216-006` | ? | 1 | 1 | — | "God made man upright, but they have sought out many schemes" — original moral constitution and its departure |
| `1217-001` | ? | 4 | 1 | — | Straightforwardness as honest inner character — rightness of speech, claims, and conduct |
| `3244-001` | ? | 3 | 2 | — | Term names the quality of moral and spiritual uprightness — the inner straightness of the person who walks rightly befor |
| `3747-001` | ? | 10 | 1 | — | Term names God's truth as a quality of his character and word — the ground on which the inner being anchors its trust an |
| `3747-002` | ? | 18 | 1 | — | Term names truth-speaking as a moral disposition of the inner being — speaking truth as a character quality that reflect |
| `3747-003` | ? | 19 | 1 | — | Term names truth as the content of a verified report or declaration — factual certainty as the basis for inner discernme |
| `3749-001` | ? | 11 | 1 | — | Term names certainty or reliability as the ground on which the inner being rests — the sure foundation that enables trus |
| `3758-001` | ? | 1 | 1 | — | Term names faithfulness as the quality of God's inner purposive reliability — the sure foundation of his plans and deeds |
| `440-001` | ? | 2 | 1 | — | Term names the irrevocable quality of God's gifts and calling (grounding identity) and the quality of genuine repentance |
| `5000-001` | ? | 6 | 1 | — | Dealing falsely as a violation of inner-being integrity — and its refusal as faithfulness |
| `5035-001` | ? | 2 | 1 | — | Term names the inner quality of soundness and wholeness of orientation — the undivided inner focus that allows the whole |
| `6546-001` | ? | 9 | 2 | — | Prophetic testimony as directed at inner orientation — the divine and prophetic warning that calls to inner repentance,  |
| `6587-001` | ? | 6 | 1 | — | Genuineness as inner-being orientation — true worship, turning to the true God, inner fidelity |
| `6588-001` | ? | 8 | 1 | — | Truthfulness as inner character quality — integrity, genuineness, the true heart |
| `6590-001` | ? | 2 | 1 | — | Truthful speech as inner act of integrity — in relationship and spiritual growth |
| `7082-001` | ? | 8 | 2 | — | Bebaioō as confirming that grounds the inner person in faith and grace |
| `7084-001` | ? | 2 | 1 | — | Bebaiōsis as confirmation establishing inner assurance |
| `774-001` | ? | 1 | 1 | — | Firm covenant — the inner-being act of solemn communal commitment |
| `804-001` | ? | 38 | 1 | — | Term names the inner act of believing — the person's inner orientation of trust directed toward God, his word, or his me |
| `804-002` | ? | 38 | 1 | — | Term names faithfulness as inner character — the quality of reliability, steadfastness, and trustworthiness as a disposi |
| `804-003` | ? | 10 | 1 | — | Term names trust withheld or broken — the inner state of refusal to believe, inability to trust, or the collapse of conf |
| `863-001` | ? | 39 | 2 | — | Term names divine faithfulness as the reliable inner character of God — his steadfast love and faithfulness as the groun |
| `863-002` | ? | 23 | 2 | — | Term names human faithfulness as the inner quality of integrity and reliability in covenant — walking before God with a  |
| `863-003` | ? | 5 | 2 | — | Term names the absence of faithfulness as moral crisis — truth perished, faithfulness gone; the inner condition of a com |
| `868-001` | ? | 5 | 2 | — | Term names faithfulness as the inner moral quality of reliability and integrity — the character of being trustworthy in  |
| `868-002` | ? | 3 | 2 | — | Term names the faithful as a moral category of persons — those whose inner character of reliability marks them as belong |
| `869-001` | ? | 23 | 2 | — | Term names divine faithfulness as an enduring inner attribute — God's reliability extending across all generations, unde |
| `869-002` | ? | 16 | 2 | — | Term names human faithfulness as an inner moral quality chosen and practised — reliability and integrity in conduct befo |
| `869-003` | ? | 7 | 2 | — | Term names faithfulness as the inner quality whose absence constitutes moral and spiritual crisis — truth and faithfulne |
| `871-001` | ? | 15 | 2 | — | Term names divine faithfulness as the reliable inner character of God — he cannot deny himself; he will do what he has p |
| `871-002` | ? | 36 | 2 | — | Term names human faithfulness as the inner quality demonstrated in reliable service — the faithful person is reliable ov |
| `871-003` | ? | 10 | 2 | — | Term names believers as a moral category — the faithful as those who trust in Christ, contrasted with the unbelieving |
| `931-001` | ? | 21 | 2 | — | Term names integrity as the inner moral condition of the person — the wholeness and blamelessness of heart and conduct t |
| `933-001` | ? | 5 | 2 | — | Term names integrity as the inner quality that the person holds fast and presents before God — the moral wholeness that  |

### M14 (53 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1025-001` | ? | 2 | 2 | — | Term names the crookedness or perverseness that destroys — the inner moral distortion that fractures both the self and o |
| `1057-001` | ? | 1 | 1 | — | Term names the whispered prayer — the desperate, intimate inner-being cry poured out when under divine discipline |
| `1073-001` | ? | 38 | 2 | — | Term names human inner thought and planning — the purposive deliberation of the heart, whether toward good or evil, fait |
| `1073-002` | ? | 14 | 2 | — | Term names the divine thoughts and purposes — God's inner deliberative will that exceeds human understanding and stands  |
| `1128-001` | ? | 2 | 1 | — | Term names slander as an act of malicious speech arising from inner hostility — a moral failure that damages relational  |
| `1130-001` | ? | 1 | 1 | — | Term names slander as an act of inner-relational betrayal — speaking against one's own kin, the sharpest form of contemp |
| `1131-001` | ? | 5 | 2 | — | Term names the act of bringing a false or malicious report — the verbal expression of an inner orientation of contempt,  |
| `1133-001` | ? | 3 | 1 | — | Term names the act of going about as a slanderer — the inner-moral condition of one whose habitual speech expresses cont |
| `1134-001` | ? | 1 | 1 | — | Term names slander as an experience endured — the condition of being maliciously defamed, received as a test of inner fa |
| `1365-001` | ? | 3 | 1 | — | Term characterises a person by the inner disposition and act of betrayal — treachery as a defining moral quality of the  |
| `1611-001` | ? | 2 | 2 | — | Term names the false brother as one whose inner orientation is concealed deception — appearing to share the community bo |
| `2110-001` | ? | 1 | 1 | — | Term names the inner experience of enduring hostile plots — suffering, tears, and faithful perseverance of the person wh |
| `3284-001` | ? | 1 | 1 | — | Faithlessness as an inner-being character quality — covenant-breaking disposition |
| `3338-001` | ? | 2 | 1 | — | Term names the product of human ingenuity — devices or schemes formed by the inner inventive capacity, whether for const |
| `3786-001` | ? | 2 | 1 | — | Term names treachery as an inner moral condition — the act and disposition of betrayal as a defining moral characteristi |
| `3787-001` | ? | 2 | 1 | — | Term names the treacherous as those whose outward conduct conceals an inward failure of wholehearted devotion — treacher |
| `3789-001` | ? | 1 | 1 | — | Term names treachery as an inner moral character — the disposition of faithlessness and betrayal as a defining quality o |
| `3868-001` | ? | 4 | 2 | — | Term names the devious inner character — the crooked orientation of the person whose ways depart from righteousness, exp |
| `3868-002` | ? | 2 | 1 | — | Term names the act of turning away from wisdom — the inner movement of deviating from sound judgement and heart-orientat |
| `417-001` | ? | 6 | 1 | — | Term names the inner devising of evil — the heart plotting harm or crafting schemes against another |
| `417-002` | ? | 5 | 1 | — | Term names the metaphorical plowing of iniquity — inner sin etched deeply into the heart or expressed as a pattern of mo |
| `4456-001` | ? | 1 | 1 | — | Term names cunning or craftiness as a disposition of the inner person — the shrewd inner orientation toward deceptive se |
| `4991-001` | ? | 8 | 1 | — | Deception as the act of inner betrayal — violating trust through deliberate misleading |
| `4992-001` | ? | 10 | 1 | — | Slackness/deceit as inner disposition — parallel to H7423A |
| `4993-001` | ? | 5 | 1 | — | Deceitfulness as the inner disposition from which false speech and resistance to God originate |
| `4997-001` | ? | 1 | 1 | — | Deceitfulness as an inner-being character quality |
| `4998-001` | ? | 1 | 1 | — | Deception as the expression of inner moral corruption through speech |
| `4999-001` | ? | 1 | 1 | — | Distortion of truth as a violation of inner-being integrity — and its renunciation |
| `522-001` | ? | 3 | 1 | — | Term names prudence as an inner quality that wisdom imparts — enabling the simple to navigate life with discernment |
| `522-002` | ? | 2 | 1 | — | Term names craftiness as an inner disposition of deliberate cunning — premeditated malice or strategic deception |
| `5544-001` | ? | 16 | 1 | — | Term names the hypocrite as a person whose inner life is defined by disconnection between outward performance and inward |
| `5544-002` | ? | 1 | 1 | — | Term names the hypocrite as one who reads external signs but fails to discern the inner realities of God's action in his |
| `5547-001` | ? | 1 | 1 | — | Term names the act of pretending — the deliberate inner intention to perform a quality one does not possess, with a hidd |
| `5730-001` | ? | 1 | 1 | — | Deceptive inner disposition expressed as flattering speech — false kindness targeting the naive |
| `5957-001` | ? | 1 | 1 | — | Term names the crooked inner orientation of the guilty — a moral character quality expressed in the way one walks |
| `6046-001` | ? | 8 | 2 | — | Term names the false prophet as an inwardly deceptive figure — whose inner orientation is predatory, self-serving, or de |
| `6046-002` | ? | 3 | 1 | — | Term names the eschatological False Prophet — the end-times figure of deception who drives worship of the beast, ultimat |
| `6252-001` | ? | 1 | 1 | — | Term names the slanderer as a character — one whose inner orientation is expressed through malicious speech directed at  |
| `7112-001` | ? | 8 | 2 | — | Term names the hiddenness of sin from the inner person or community — and the moment of moral awakening when hidden guil |
| `7112-002` | ? | 6 | 2 | — | Term names God's hiddenness from the person who cries to him — the inner anguish of divine withdrawal in trouble — and p |
| `7112-003` | ? | 8 | 2 | — | Term names the moral act of hiding oneself from responsibility — deliberate inner blindness to obligation — and its cond |
| `780-001` | ? | 38 | 1 | — | Deceit as the inner orientation of the wicked — deceitful tongue, deceitful heart |
| `781-001` | ? | 12 | 1 | — | Deceit as inner character quality and its absence as integrity |
| `782-001` | ? | 10 | 1 | — | Deceit as an inner quality and its absence as the mark of integrity |
| `783-001` | ? | 1 | 1 | — | Treachery as covert inner-being betrayal |
| `784-001` | ? | 73 | 1 | — | Falsehood as the inner orientation of the wicked — lying tongue and lying heart |
| `784-002` | ? | 25 | 1 | — | Prophetic falsehood — lies spoken in God's name corrupting inner spiritual life |
| `784-003` | ? | 14 | 1 | — | Abhorrence of falsehood — the inner-being posture of the righteous |
| `786-001` | ? | 3 | 1 | — | Deceit as the inner mechanism that corrupts desire, hardens the heart, and takes the person captive |
| `835-001` | ? | 1 | 1 | — | Term names human malicious scheming — inner plotting directed harmfully against another |
| `835-002` | ? | 1 | 1 | — | Term names moral corruption as an inner quality expressed outwardly in conduct |
| `835-003` | ? | 4 | 2 | — | Term names divine purposing — resolute inner intention of God, explicitly located in heart and mind |
| `912-001` | ? | 6 | 1 | — | Term names hypocrisy as an inner condition — the state of inner pretence in which outward performance is disconnected fr |

### M15 (58 VCGs · status: Analysis Completed)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `523-002` | M15-B | 1 | 0 | — | Term names understanding as a human inner-being capacity — the gift from God enabling discernment of his ways and wise c |
| `525-001` | M15-A | 3 | 0 | — | se.khel names a practical inner quality of good sense, prudence, and wise conduct. It produces outcomes — favour, succes |
| `528-001` | M15-A | 7 | 0 | — | cha.kham in Proverbs, Ecclesiastes, and historical narrative names wisdom as a constituted inner quality of the person — |
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

### M16 (39 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1000-001` | ? | 5 | 1 | — | Term names the disruption or perceived disruption of rational inner faculties — being out of one's mind, whether genuine |
| `1006-001` | ? | 1 | 1 | — | Term names the state of mental derangement — the collapse of rational inner faculties attributed to excessive learning |
| `1191-001` | ? | 1 | 1 | — | Transgression noted but not punished — the inner moral condition of transgression as the object of divine discernment wi |
| `1376-001` | ? | 3 | 1 | — | Term names the inner disposition of laziness and reluctance — contrasted with zealous, fervent inner engagement |
| `2627-001` | ? | 1 | 1 | — | Term names the inner condition of cognitive and moral dullness — the stupidity that results from following false instruc |
| `3057-001` | ? | 4 | 1 | — | Foolishness as inner-being condition — deluded judgment, sinful folly, and the incapacity to know God's way |
| `3350-001` | ? | 1 | 1 | — | Dream-visions and inner fancies — the mental images and fantasies produced in the mind during sleep, which alarm and dis |
| `4185-001` | ? | 1 | 1 | — | Term names the mode of expression that departs from rational restraint — speaking beyond reason, used rhetorically to ma |
| `4187-001` | ? | 1 | 1 | — | Term names the madness of disordered inner impulse — the prophet's irrational compulsion rebuked by God through a donkey |
| `4331-001` | ? | 4 | 1 | — | Term names madness or derangement — the inner disruption of reason and moral orientation, whether feigned, induced, or c |
| `4331-002` | ? | 5 | 1 | — | Term names boasting arrogance as an inner orientation — the exaltation of self before God and others |
| `4335-001` | ? | 5 | 1 | — | Term names raving madness or contemptuous derision — the expression of disordered inner intensity, whether in mockery, f |
| `4337-001` | ? | 4 | 1 | — | Term names madness as an inner condition — the disordered, futile orientation of the human heart and mind, investigated  |
| `4339-001` | ? | 1 | 1 | — | Term names madness as the culmination of foolishness — the final, evil expression of a disordered inner life |
| `4450-001` | ? | 5 | 1 | — | Term names the inner condition of brutish insensibility — the person who is beast-like in understanding, unable or unwil |
| `4469-001` | ? | 2 | 1 | — | Term describes the inner transformation into folly — the process by which a person or their thinking becomes foolish bef |
| `4469-002` | ? | 2 | 1 | — | Term describes the loss of distinctive inner character — the becoming flat or flavourless through failure to maintain on |
| `4479-001` | ? | 2 | 1 | — | Term names apparent or feigned madness — the inner state or outer presentation that leads others to perceive a person as |
| `4479-002` | ? | 4 | 1 | — | Term names the dismissal of prophetic intensity as madness, or the inner disintegration produced by divine judgment |
| `4480-001` | ? | 3 | 1 | — | Term names madness as a condition of the inner being — whether reckless furious intensity or the madness of divine judgm |
| `4485-001` | ? | 1 | 1 | — | Term names reckless instability of character — the inner disposition that acts impulsively without regard for moral boun |
| `5368-001` | ? | 6 | 1 | — | Term names folly as the observed inner-opposite of wisdom — a condition the searching mind investigates, compares, and r |
| `5369-001` | ? | 6 | 1 | — | Term names the fool's inner condition of lacking sense and understanding — a pervasive inner blindness evident in speech |
| `5370-001` | ? | 1 | 1 | — | Term names folly as an inner condition of those in positions of leadership — the inversion where those lacking wisdom ar |
| `5371-001` | ? | 6 | 1 | — | Term names the inner condition of foolishness as failure to perceive and attend to spiritual realities — blindness to wh |
| `5371-002` | ? | 4 | 1 | — | Term names the inner posture of self-boasting folly — speaking and presenting oneself outside the orientation of God's w |
| `5372-001` | ? | 11 | 1 | — | Term names the fool's inner disposition of rejecting wisdom and instruction — the orientation that despises correction a |
| `5372-002` | ? | 8 | 1 | — | Term names the fool's inner volatility and impulsive expression — the orientation that quickly vents vexation, quarrels, |
| `5372-003` | ? | 6 | 1 | — | Term names the consequences of the fool's inner condition — the ruin and mortality that result from persisting in foolis |
| `5373-001` | ? | 1 | 1 | — | Term names the foolishness of a leader who abandons responsibility — an inner-being disposition of negligence and self-i |
| `5374-001` | ? | 5 | 1 | — | Term names the inner epistemic verdict of foolishness — how the word of the cross or spiritual truth is assessed by the  |
| `7156-001` | ? | 13 | 2 | — | Term names folly as the inner moral disposition that commits outrageous acts against covenant, personhood, and God — the |
| `874-001` | ? | 1 | 1 | — | Term names folly as an object of the searching inner mind — a condition placed alongside wisdom as something the person  |
| `875-001` | ? | 4 | 1 | — | Term names foolishness as a disposition of the inner person — a mode of self-presentation and reasoning that departs fro |
| `877-001` | ? | 17 | 1 | — | Term names folly as the characteristic inner condition of the person who lacks wisdom — an orientation of the heart that |
| `877-002` | ? | 7 | 1 | — | Term names folly as the inner root of emotional volatility and moral failure — hasty temper, self-produced ruin, and the |
| `878-001` | ? | 4 | 1 | — | Term names the inner condition of foolishness as unpreparedness and failure to think ahead — the disposition that hears  |
| `878-002` | ? | 4 | 1 | — | Term names the inner-epistemic reversal through which God chooses the world's foolish and calls the wise to embrace appa |
| `878-003` | ? | 4 | 1 | — | Term names the inner condition of moral/spiritual blindness or contemptuous judgment — the foolishness that fails to dis |

### M17 (31 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1042-001` | ? | 2 | 1 | — | Term names the beginning that discloses an inner-being condition — either the moment when prayer begins and God responds |
| `1065-001` | ? | 5 | 1 | — | Term names God's sovereign inner purpose and counsel — the divine intention that precedes and governs all things, includ |
| `1065-002` | ? | 2 | 1 | — | Term names the human inner purpose — the settled inner resolve and purposeful aim that orients a person's life and condu |
| `1328-001` | ? | 37 | 2 | — | Term names 'the beginning' as the origin-point of inner-being realities — love, sin, testimony, truth, and faith — whose |
| `1328-002` | ? | 11 | 2 | — | Term names cosmic or spiritual ruling powers — the inner being engaged through spiritual warfare, Christ's supremacy ove |
| `1328-003` | ? | 4 | 2 | — | Term names elementary or foundational teaching — the inner being engaged through the call to grow from first principles  |
| `3380-001` | ? | 1 | 1 | — | Term names the inner purposeful scheming of the wicked — a deliberate inner plan conceived and pursued against others, c |
| `3554-001` | ? | 2 | 1 | — | Term names purposive cause or intent — the inner purpose for which something is done, whether to disclose thoughts of th |
| `391-001` | ? | 33 | 2 | — | Term names the inner act of waiting for God — the sustained inner orientation of expectation directed toward God's salva |
| `391-002` | ? | 9 | 1 | — | Term names the inner experience of unfulfilled or hostile waiting — hope directed toward good but met with evil, or enem |
| `392-001` | ? | 7 | 2 | — | Term names the inner act of looking to or hoping in God — the expectant orientation of persons or creation toward God as |
| `4650-001` | ? | 2 | 1 | — | Term names the inner orientation toward wisdom — the person who seeks and receives counsel as an expression of inner hum |
| `4650-002` | ? | 2 | 1 | — | Term names counsel as the expression of inner character — the quality of a person's counsel reveals the quality of their |
| `4650-003` | ? | 2 | 1 | — | Term names counsel as the instrument of inner planning — the deliberate use of guidance in forming decisions that achiev |
| `4837-001` | ? | 5 | 2 | — | Term names the divine Helper whose ministry engages and transforms the inner life of the believer through teaching, reca |
| `4921-001` | ? | 1 | 1 | — | Term names the counsellor as a category that the human person cannot fill for God — the recognition of the incomparable  |
| `499-001` | ? | 2 | 1 | — | Term names a determined purposive will — human deliberate intention or divine sovereign resolve — as the inner origin of |
| `748-001` | ? | 50 | 1 | — | Counsel as wisdom given or received, orienting the inner person |
| `748-002` | ? | 1 | 1 | — | Inner counsel of the soul in anguish — self-directed deliberation under distress |
| `748-003` | ? | 22 | 1 | — | Divine counsel as God's eternal inner purpose |
| `748-004` | ? | 9 | 1 | — | Rejection or spurning of divine counsel — inner failure of orientation |
| `750-001` | ? | 2 | 1 | — | Term names the taking of counsel as an expression of inner moral intention — the deliberation that reveals the orientati |
| `751-001` | ? | 10 | 1 | — | Divine intimate friendship and confident disclosure |
| `751-002` | ? | 4 | 1 | — | Membership in or access to the divine council/assembly |
| `751-003` | ? | 3 | 1 | — | Secret plots — hidden inner scheming of the wicked |
| `751-004` | ? | 5 | 1 | — | Trustworthiness in keeping intimate confidence |
| `752-001` | ? | 5 | 2 | — | Term names the inner deliberative purpose or resolved intention of a person, located within the heart as the seat of pur |
| `752-002` | ? | 8 | 2 | — | Term names God's sovereign purposive counsel that directs human events and vocation, intersecting with the inner life of |
| `758-001` | ? | 6 | 1 | — | Counsels as product of a rebellious or wicked inner heart |
| `758-002` | ? | 1 | 1 | — | Counsel as recorded wisdom addressed to the inner person |
| `997-001` | ? | 3 | 1 | — | Term names the settled orientation of the inner mind — the deep dispositional set of the person toward flesh or Spirit,  |

### M18 (37 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1296-001` | ? | 1 | 1 | — | Term names the inner aspiration toward the heavenly — the deep desire that orients the inner person beyond the earthly t |
| `130-001` | ? | 12 | 2 | — | Term names the inner act of waiting with hope — the expectant orientation of the soul toward God's action, help, or timi |
| `2619-001` | ? | 22 | 2 | — | Term names the inner act of hoping in God — the orientation of the soul toward God's steadfast love and salvation as the |
| `2619-002` | ? | 4 | 1 | — | Term names hope tested or disappointed — waiting in vain, hoping for good only to receive evil, or hoping despite anguis |
| `2620-001` | ? | 11 | 2 | — | Term names the inner act of patient waiting — the posture of sustained expectant attention, whether directed toward God, |
| `2711-001` | ? | 10 | 1 | — | Inner orientation of active expectation and watchful waiting — person directed toward what is coming, with hope, longing |
| `2711-002` | ? | 5 | 1 | — | Eschatological expectation as governing inner orientation — whole inner life directed toward and shaped by what God has  |
| `351-001` | ? | 2 | 1 | — | Expectation as an inner state with affective weight — anticipation carrying dread, foreboding, or intensity of directed  |
| `353-001` | ? | 1 | 1 | — | Inner condition of freedom from anxious care — the state of being untroubled as a desirable orientation of the inner per |
| `383-001` | ? | 5 | 1 | — | Term names hope as the inner orientation of a people toward God — the expectation of restoration and faithfulness ground |
| `385-001` | ? | 31 | 2 | — | Term names hope as the fundamental inner expectation of the person — the capacity for anticipating good, future, and res |
| `386-001` | ? | 3 | 1 | — | Term names expectation as an inner orientation — the forward-looking hope directed at a specific source, here misplaced  |
| `387-001` | ? | 4 | 1 | — | Term names hope as an inner quality — the expectation of the person that produces joy when fulfilled and heart-sickness  |
| `387-002` | ? | 2 | 1 | — | Term names the perishing or collapse of hope — inner hope withdrawn, lost, or proven false |
| `388-001` | ? | 2 | 1 | — | Term names hope in God — the inner orientation of trust and expectation toward God as the source of blessing and protect |
| `399-001` | ? | 1 | 1 | — | Term names the inner act of waiting quietly — a posture of patient, still expectation directed toward God's salvation |
| `401-001` | ? | 37 | 2 | — | Term names hope as an eschatological inner orientation — the confident forward expectation toward God's promised future, |
| `401-002` | ? | 10 | 2 | — | Term names hope as a constitutive permanent inner quality held alongside faith and love — one of the abiding characteris |
| `401-003` | ? | 3 | 2 | — | Term names the absence or loss of hope as an inner condition of desolation — the state of the person without God or with |
| `402-001` | ? | 1 | 1 | — | Term names the inner disposition of expecting nothing in return — the absence of self-directed hope as the posture of ge |
| `404-001` | ? | 14 | 2 | — | Term names the inner act of setting hope on God or Christ — the orientation of the whole person's expectation toward God |
| `404-002` | ? | 19 | 2 | — | Term names the inner act of hoping for a specific future outcome, person, or event — forward orientation of expectation  |
| `483-001` | ? | 4 | 1 | — | Term names intense personal longing — the inner being straining, fainting, or yearning toward what it desires with great |
| `484-001` | ? | 6 | 1 | — | Term names intense panting desire — the inner being straining urgently, gasping, or panting toward its object; longing e |
| `495-001` | ? | 1 | 1 | — | Long-held longing for relational presence |
| `496-001` | ? | 2 | 1 | — | Longing as inner-being response to godly grief and separation |
| `507-001` | ? | 6 | 1 | — | Longing for persons — deep inner-being desire for relational presence |
| `507-002` | ? | 3 | 1 | — | Longing for God, the heavenly, or spiritual nourishment |
| `508-001` | ? | 8 | 1 | — | Desire as covetous or lustful inner orientation |
| `508-002` | ? | 8 | 1 | — | Deep earnest longing as a positive inner-being orientation |
| `5571-001` | ? | 13 | 1 | — | Term names wandering or fleeing as an inner experience — restlessness of sleep fleeing, the anguish of spiritual strayin |
| `5804-001` | ? | 1 | 1 | — | The beloved person as object of deep inner longing — toward whom the heart reaches in yearning affection |
| `63-001` | ? | 2 | 1 | — | Term names inner aspiration toward pleasing God — the will directed entirely toward divine approval as the supreme ambit |
| `63-002` | ? | 1 | 1 | — | Term names inner aspiration toward a quality of personal life — the ambitious pursuit of quietness, dignity, and diligen |
| `965-001` | ? | 1 | 1 | — | Failing of the eyes through consuming longing — inner grief of powerless yearning for what has been taken |
| `967-001` | ? | 1 | 1 | ✓ | All-consuming longing of the soul for God's word and rules — inner being entirely taken up with desire for the divine |
| `968-001` | ? | 1 | 1 | — | Intense, forward-straining inner disposition of eager expectation — longing that stretches the whole being toward a not- |

### M19 (43 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1106-001` | ? | 3 | 1 | — | Term names self-control as an inner character quality — the capacity to govern oneself, listed as a fruit of the Spirit  |
| `1107-001` | ? | 2 | 1 | — | Term names the exercise of self-control as an inner capacity — governing appetite and desire in both relational and comp |
| `1112-001` | ? | 1 | 1 | — | Term names self-discipline as an inner gift of the Spirit — the quality of a sound and controlled inner life given by Go |
| `1195-001` | ? | 1 | 1 | — | Trust as inner disposition of reliance on God — source of strength |
| `1196-001` | ? | 8 | 1 | — | Inner disposition of trust/security as relational posture toward God |
| `1196-002` | ? | 22 | 1 | — | Security as covenantal/eschatological promise — divinely granted dwelling in safety |
| `1196-003` | ? | 4 | 1 | — | Personal security as inner fruit of integrity and wise living |
| `2611-001` | ? | 1 | 1 | — | Term names the inner state of security or settled ease — the condition of feeling safe and undisturbed, even when ground |
| `2624-001` | ? | 2 | 1 | — | Term names confidence as an inner quality — the settled inner assurance grounded in fear of God and integrity of conduct |
| `2628-001` | ? | 1 | 1 | — | Term names the refuge or shelter sought — the object toward which the inner act of seeking safety is directed, here misp |
| `2748-001` | ? | 2 | 1 | — | Fervency of spirit — the inner burning disposition of spiritual engagement |
| `340-001` | ? | 4 | 1 | — | Earnest desire and eager zeal — the inner longing for what is good and spiritual |
| `340-002` | ? | 7 | 1 | — | Jealousy and covetous desire — inner hostility and consuming want |
| `3752-001` | ? | 3 | 1 | — | Term names the inner act of trust in God — the person's inner orientation of faith expressed in faithfulness of characte |
| `3773-001` | ? | 1 | 1 | — | Term names the inner state of firm conviction — being fully persuaded and settled in what has been learned and believed |
| `384-001` | ? | 7 | 1 | — | Term names confidence in God — the inner quality of assurance and reliance directed toward God as the ground of blessing |
| `384-002` | ? | 8 | 1 | — | Term names confidence in inadequate objects — trust placed in gold, human strongholds, or false gods, which is severed o |
| `390-001` | ? | 15 | 2 | — | Term names God as the inner person's refuge — the place of safety and strength to which the whole person turns in distre |
| `390-002` | ? | 2 | 1 | — | Term names a misplaced inner refuge — false security found in lies or inadequate protection, which God will sweep away |
| `396-001` | ? | 33 | 2 | — | Term names the inner act of taking refuge in God — the whole-person orientation of fleeing to God as the source of prote |
| `396-002` | ? | 3 | 1 | — | Term names the inner act of taking refuge in inadequate objects — misplaced refuge in Egypt, human power, or idols, cont |
| `397-001` | ? | 60 | 3 | — | Term names the inner act of trusting in God — the orientation of the whole person's reliance and confidence directed tow |
| `397-002` | ? | 43 | 1 | — | Term names trust in persons, things, or self — misplaced or tested inner reliance on inadequate objects, contrasted with |
| `397-003` | ? | 14 | 1 | — | Term names trust as an inner state of security or ease — the condition of being settled, unguarded, or confident in one' |
| `398-001` | ? | 3 | 1 | — | Term names the ground or object of inner trust — what the person's confidence rests on, whether God or human power |
| `4031-001` | ? | 2 | 1 | — | Confident assurance directed toward God or Christ — inner disposition of relational trust upward |
| `4031-002` | ? | 4 | 1 | — | Confidence as inner disposition of assurance toward persons or in one's own standing |
| `4102-001` | ? | 5 | 1 | — | Inner reliance on God as the proper object of trust |
| `4102-002` | ? | 7 | 1 | — | Misplaced or hypocritical inner reliance on wrong objects — people, military, self |
| `4104-001` | ? | 2 | 1 | — | Divine support as inner-being ground of confidence in calamity |
| `4105-001` | ? | 2 | 1 | — | Divine support as inner-being ground of confidence in calamity |
| `4160-001` | ? | 1 | 1 | — | Trust in God expressed through courageous inner commitment at cost to self |
| `4188-001` | ? | 4 | 1 | — | Term names self-control as an inner character quality — the disciplined mind that governs its impulses, required for god |
| `4315-001` | ? | 3 | 1 | — | Term names sobriety of mind as a character quality — the inner disposition of measured, clear-headed judgment required f |
| `4451-001` | ? | 1 | 1 | — | Term names the inner disposition of careful attentiveness — the thoughtful orientation of the person toward devoted acti |
| `4465-001` | ? | 8 | 1 | — | Term names inner-disposition of eager striving toward a spiritual, formative, or eschatological end — diligence pressing |
| `4465-002` | ? | 3 | 1 | — | Term names pastoral-relational urgency expressed in travel imperatives — the apostolic-protégé eagerness for personal pr |
| `482-001` | ? | 8 | 1 | — | Term names the directing or lifting of the inner being toward its object — lifting the soul to God in trust and prayer,  |
| `6203-001` | ? | 1 | 1 | — | Term names self-controlled as an inner character requirement — among the virtues required of one who leads others |
| `659-001` | ? | 13 | 2 | — | Term names God as the inner refuge and stronghold of the person — the secure centre of the self, the source of strength  |
| `659-002` | ? | 7 | 2 | — | Term names the false refuge — the misplaced trust in human or material security in place of God — and its exposure as sh |
| `7081-001` | ? | 7 | 2 | — | Bebaios as firmness grounding inner-being states of hope, confidence, and faith |
| `7086-001` | ? | 1 | 1 | — | Steadfast order and firm faith — stereōma as the inner quality of ordered stability and firmness in faith: the inner-bei |

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

### M21 (48 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1053-001` | ? | 17 | 2 | — | Term names prayer as the sustained inner orientation of the person toward God — the discipline, posture, and practice of |
| `1053-002` | ? | 17 | 2 | — | Term names prayer as the inner-being medium of access and petition — through which faith receives, the saints's needs as |
| `1054-001` | ? | 16 | 2 | — | Term names petition as the inner-being act of bringing specific need before God — the orientation of the whole person to |
| `1058-001` | ? | 2 | 1 | — | Term names intercession as an inner-being act — the petition offered on behalf of others or for sanctification of that w |
| `1059-001` | ? | 3 | 2 | — | Term names vow and prayer as inner-being acts of commitment and faith — the binding of the will to God and the trusting  |
| `1256-001` | ? | 1 | 1 | — | Term names worship as a directed inner orientation toward a divine object — naming the inner posture of piety |
| `1697-001` | ? | 1 | 1 | — | Term names reverence for God as an inner disposition that expresses itself in good works and proper conduct |
| `1931-001` | ? | 1 | 1 | — | Term names fasting as the physical expression of an inner-being posture of grief, penitence, and humble submission befor |
| `2336-001` | ? | 14 | 2 | — | Term names earnest petition to God — the inner-being act of urgent, sometimes desperate, prayer directed toward God or J |
| `2336-002` | ? | 2 | 1 | — | Term names apostolic entreaty — the earnest inner-being appeal from one person to another calling them toward God, recon |
| `2381-001` | ? | 2 | 1 | — | Term names the act of prayer — the deliberate inner orientation of the person toward God in petition, thanksgiving, and  |
| `260-001` | ? | 7 | 2 | — | Term names the inner orientation of reverent devotion — the disposition that characterises the God-fearer and true worsh |
| `260-002` | ? | 3 | 1 | — | Term names the inner act of worship directed at God or idols — reverent devotion that can be genuine or misdirected, fru |
| `2742-001` | ? | 6 | 1 | — | Zealotry as inner commitment — devoted passion for a cause, law, or calling |
| `278-001` | ? | 1 | 1 | — | Term names the God-fearer as one whose inner orientation of reverence and obedience opens divine attentiveness |
| `281-001` | ? | 2 | 2 | ✓ | Term names reverence as the inner posture of godly fear before God — the disposition that makes prayer heard and worship |
| `302-001` | ? | 1 | 1 | — | Term names reverential fear that produces faithful obedience — the inner disposition of awe-driven trust that acts on di |
| `302-002` | ? | 1 | 1 | — | Term names practical inner fear for physical safety — the inner assessment of danger that produces protective action |
| `3272-001` | ? | 2 | 1 | — | Term names the covenantal act whose content is the writing of divine law on the inner mind and heart — inner transformat |
| `348-001` | ? | 7 | 1 | — | Zeal as passionate inner devotion — consuming fervour for God and his cause |
| `348-002` | ? | 8 | 1 | — | Jealousy as inner hostility — envy, rivalry, and divisive passion |
| `348-003` | ? | 2 | 1 | — | Divine jealousy — God's passionate inner claim on his people |
| `4336-001` | ? | 28 | 2 | — | Term names prayer as the inner-being act of bringing the will before God — including surrender, petition, and watchfulne |
| `4336-002` | ? | 18 | 2 | — | Term names prayer as the instructed inner-being discipline — the shape, posture, and conditions of authentic prayer taug |
| `4336-003` | ? | 39 | 2 | — | Term names corporate and intercessory prayer — the community's inner-being act of praying together, or one person's inne |
| `473-001` | ? | 2 | 1 | — | Term names the desires of the heart as petitions before God — what the inner being asks for and hopes to receive |
| `477-001` | ? | 7 | 1 | — | Term names prayer as urgent petition to God — the inner movement of the person toward God in need, crisis, or desire for |
| `477-002` | ? | 2 | 1 | — | Term names petition directed toward human authority — the inner orientation of request toward one in power |
| `478-001` | ? | 45 | 1 | — | Term names inquiring of God — the inner orientation of seeking divine guidance, oracle, or provision through direct peti |
| `478-002` | ? | 65 | 1 | — | Term names asking or inquiring of a person — relational request, petition, or inquiry directed to another human |
| `478-003` | ? | 4 | 1 | — | Term names inquiry by divination — seeking oracles through occult or disordered means; the inner orientation misdirected |
| `478-004` | ? | 7 | 1 | — | Term names God questioning or requiring — God's inner purposive demand or questioning addressed to humans |
| `478-005` | ? | 4 | 1 | — | Term names asking as the expression of personal desire or inner appetite — the person's own craving or longing framed as |
| `502-001` | ? | 30 | 1 | — | Asking Jesus — the inner-being posture of those who approach Jesus with need or faith |
| `502-002` | ? | 6 | 1 | — | Jesus asking the Father — his inner-being orientation of prayer and intercession |
| `502-003` | ? | 12 | 1 | — | Apostolic asking — pastoral concern expressed as appeal |
| `512-001` | ? | 8 | 1 | — | Seeking after earthly or invalid things — misdirected inner orientation |
| `512-002` | ? | 4 | 1 | — | Seeking what is truly good — inner-being orientation toward the word and the heavenly |
| `5480-001` | ? | 38 | 2 | — | Term names the act and habitual inner posture of giving thanks — primarily to God in response to grace received, but ext |
| `553-001` | ? | 1 | 1 | — | Term names God-loving as the defining inner orientation — the standard from which the last days' pleasure-loving represe |
| `5696-001` | ? | 1 | 1 | — | Term names the Spirit's intercession within the person — the divine inner advocacy that arises from human weakness and e |
| `714-001` | ? | 9 | 1 | — | Bold proclamation as inner-being posture — speaking with unrestrained confidence in the face of opposition and risk, gro |
| `7520-001` | ? | 1 | 1 | — | Intentional inner attentiveness to worship — epakroaomai as the receptive inner posture drawn toward prayer and praise |
| `890-001` | ? | 18 | 2 | — | Term names the inner act of earnest supplication — the plea for mercy that arises from deep need and relational vulnerab |
| `985-001` | ? | 21 | 2 | — | Term names supplication to God — the inner act of pleading for mercy, rooted in recognition of one's own need and God's  |
| `985-002` | ? | 3 | 1 | — | Term names supplication to human authority — the humble inner posture of plea before one with power over the supplicant' |
| `987-001` | ? | 14 | 2 | — | Term names the act of intercessory prayer — pleading with God on behalf of another's need or the removal of a burden fro |
| `987-002` | ? | 5 | 2 | — | Term names personal prayer — the inner act of bringing one's own need, trust, or longing to God and receiving divine res |

### M22 (80 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1027-001` | ? | 2 | 2 | — | Term names praise as the defining inner orientation of the person before God — the mouth and heart continually directed  |
| `1027-002` | ? | 11 | 2 | — | Term names God himself as the content and source of praise — what the inner life is oriented toward and what enables pra |
| `1027-003` | ? | 9 | 2 | — | Term names praise as a transforming garment — replacing the faint spirit with the inner orientation of worship |
| `1029-001` | ? | 2 | 2 | — | Term names thanksgiving to God as a whole-person inner act — the deliberate orientation of the entire inner being toward |
| `1029-002` | ? | 12 | 2 | — | Term names confession of sin as an inner-being act of transparency before God — the acknowledgment of guilt that enables |
| `1029-003` | ? | 5 | 1 | — | Term names the acknowledgement of God's name as the inner-being act of returning to God — the turning of the heart towar |
| `1030-001` | ? | 2 | 2 | — | Term names the inner-sourced praise that comes from God — the true commendation that reaches the hidden life of the hear |
| `1030-002` | ? | 5 | 1 | — | Term names the doxological purpose orientation — all of life directed toward the praise of God's glory |
| `1030-003` | ? | 1 | 1 | — | Term names the inner orientation of the mind toward what is praiseworthy — thinking on praiseworthy things as a discipli |
| `1032-001` | ? | 2 | 1 | — | Term names praise as the universal inner-being response to God — the call to all peoples to orient themselves toward God |
| `1034-001` | ? | 3 | 1 | — | Term names the inner-being act of praise directed toward God — gratitude for wisdom given, or awe at divine sovereignty |
| `1034-002` | ? | 2 | 1 | — | Term names praise misdirected to false gods — the inner orientation of worship toward objects that cannot see, hear, or  |
| `1035-001` | ? | 2 | 1 | — | Term names praise as the spontaneous inner-being response to God's action — whether from children or crowds, the outward |
| `1036-001` | ? | 3 | 2 | — | Term names singing praise as an integrated inner-being act — engaging spirit, mind, and heart simultaneously in musical  |
| `1038-001` | ? | 2 | 1 | — | Term names praise-celebration as an inner-being act of devotion — whether rightly directed toward God or misdirected tow |
| `1039-001` | ? | 15 | 2 | — | Term names the thanksgiving sacrifice as an inner-being act of worship — the offering that glorifies God and expresses t |
| `1039-002` | ? | 13 | 2 | — | Term names thanksgiving as song and communal expression — the inner-being of gratitude voiced in congregation, processio |
| `1045-001` | ? | 2 | 2 | — | Term names the high/exalted praise that rises from the inner life — the extolling of God as the fullest expression of th |
| `1046-001` | ? | 1 | 1 | — | Term names praise as a test of inner character — what a person does with praise reveals their inner moral formation |
| `1047-001` | ? | 9 | 2 | — | Term names the glory of God as the supreme inner-being orientation of the human person — what is sought, hoped for, and  |
| `1047-002` | ? | 9 | 2 | — | Term names glory as transforming — the process by which the inner person is changed from one degree of glory to another  |
| `1047-003` | ? | 13 | 2 | — | Term names doxological inner orientation — the purpose of all human action and the direction of the inner life toward th |
| `1047-004` | ? | 11 | 2 | — | Term names eschatological glory — the future condition of the person and creation fully realized in glory, which functio |
| `1050-001` | ? | 1 | 1 | — | Term names the singing of praise as an inner-being act of worship — declaring God's name in congregational song |
| `1051-001` | ? | 1 | 1 | — | Term names praise as a sacrificial inner-being act — the offering of the inner life to God expressed through deliberate  |
| `1262-001` | ? | 5 | 2 | — | Term names worthiness as a divine attribute — the intrinsic moral and ontological deservingness of God and the Lamb to r |
| `1262-002` | ? | 6 | 2 | — | Term names worthiness or desert as a moral quality of persons — whether a person's inner character qualifies them for ho |
| `1298-001` | ? | 18 | 2 | — | Term names the blessing of God — pronouncing his name over creation, persons, bread — as the inner act of consecration a |
| `1298-002` | ? | 18 | 2 | — | Term names the blessing declared over persons — the prophetic and covenantal words of blessing spoken over individuals,  |
| `1298-003` | ? | 4 | 2 | — | Term names blessing as the inner act of responding to curse with blessing — the counterintuitive orientation of the inne |
| `1321-001` | ? | 17 | 2 | — | Term names the divine splendour or majesty of God — evoking inner responses of awe, wonder, and worship |
| `1321-002` | ? | 4 | 2 | — | Term names human or royal honour — bestowed, withheld, or forfeited — engaging the inner being through dignity, shame, o |
| `1652-001` | ? | 6 | 1 | — | Pleasantness in relationship with God — the delight of dwelling in God's presence and praise |
| `1652-002` | ? | 5 | 1 | — | Term names pleasantness as the quality of harmonious human relationships and wisdom — the inner-being experience of what |
| `1861-001` | ? | 74 | 2 | — | Term names the manifest presence of God's glory as an encounter that human beings experience — producing awe, prostratio |
| `1861-002` | ? | 32 | 2 | — | Term names the human inner act of directing honour and glory toward God — the worship orientation expressed in ascriptio |
| `1861-003` | ? | 8 | 2 | — | Term names the inner self or whole being of the person as the seat of praise, dignity, and orientation — the "glory" as  |
| `1861-004` | ? | 17 | 1 | — | Term names human honour as the outer expression of inner character — wisdom, humility, and fear of the Lord as the sourc |
| `1861-005` | ? | 48 | 2 | — | Term names human honour as a relational-social condition of dignity and worth — received from God, threatened by others, |
| `1868-001` | ? | 2 | 1 | — | Term describes the splendour or magnificence that accompanies a person's position or status — framing the conditions in  |
| `1870-001` | ? | 2 | 1 | — | Term names material richness or splendour as the setting in which inner spiritual orientation — faithfulness or its corr |
| `2695-001` | ? | 1 | 1 | — | Term names the communal act of praise and thanksgiving directed toward God — the expressive inner orientation of gratitu |
| `3080-001` | ? | 1 | 1 | — | Term names the nobility of the soul — the inner-being quality of generosity and dignity in their highest expression |
| `410-001` | ? | 47 | 2 | ✓ | Term names divine blessing as the inner-dispositioned gift of God — the overflow of God's favour toward persons, bringin |
| `410-002` | ? | 16 | 1 | — | Term names the inner act of bestowing blessing — the patriarch, leader, or friend invoking divine favour upon another as |
| `4333-001` | ? | 11 | 1 | — | Term names the sustained inner orientation of praise toward God — the deliberate, personal direction of the whole being  |
| `4333-002` | ? | 59 | 1 | — | Term names corporate/liturgical praise — the community's inner-being act of worship organized for God's service |
| `4333-003` | ? | 12 | 2 | — | Term names the praise of the worthy — what and who deserves to be praised, as a reflection of inner-being discernment an |
| `4875-001` | ? | 4 | 2 | — | Term names the divine spirit's indwelling as the source of inner wisdom, discernment, and holy capacity in the person |
| `4875-002` | ? | 8 | 2 | — | Term designates the saints of the Most High — those whose inner identity and destiny is constituted by belonging to the  |
| `5071-001` | ? | 5 | 1 | — | Term names the inner disposition of honour and respect — the recognition of worth in another person; and its negation: p |
| `5072-001` | ? | 4 | 1 | — | Term names the sacred adornment of worship — the splendour of holiness as the context and expression of the inner act of |
| `5298-001` | ? | 1 | 1 | — | Perpetual inner moral condition — chronic spiritual backsliding without return |
| `5986-001` | ? | 2 | 2 | — | Term names the inner-being act of thanks and praise — the deliberate, sustained orientation of the person toward God in  |
| `5989-001` | ? | 1 | 1 | — | Term names the call to extol God — the inner-being orientation of all peoples toward God in praise |
| `5990-001` | ? | 57 | 2 | — | Term names the psalm/song as a designated form of inner-being expression — the compositional act of directing one's whol |
| `5992-001` | ? | 4 | 2 | — | Term names melody as the vehicle of inner-being worship — both its proper expression and the failure of melody when deta |
| `609-001` | ? | 42 | 1 | — | Term names the Holy Spirit as the divine agent who fills, leads, empowers, and transforms the inner being of the person |
| `609-002` | ? | 42 | 1 | — | Term names holiness as the inner character calling — being holy in all conduct, body, and spirit, as God is holy |
| `609-003` | ? | 42 | 1 | — | Term names the blasphemy against the Holy Spirit — the inner moral act of attributing divine works to Satan; the unforgi |
| `609-004` | ? | 42 | 1 | — | Term names the Holy Spirit as capable of being grieved, lied to, or resisted — susceptible to harm through human inner c |
| `609-005` | ? | 42 | 1 | — | Term names the Holy One — Christ or God as holy; divine transcendence and moral purity as an object of inner recognition |
| `634-001` | ? | 9 | 2 | — | Eufrainō as authentic gladness in restoration, hope, and divine presence |
| `634-002` | ? | 5 | 2 | — | Eufrainō as disordered or worldly celebration |
| `649-001` | ? | 8 | 2 | — | Go.del as greatness of God as basis of prayer, worship, and covenant confidence |
| `649-002` | ? | 5 | 2 | — | Go.del as pride or self-exalting greatness subject to divine judgment |
| `6903-001` | ? | 9 | 2 | — | Ge.dul.lah as greatness of God as object of worship and doxological declaration |
| `813-001` | ? | 11 | 1 | — | Term names divine majesty as the object of inner awe, worship, and doxological meditation — the glory that the inner per |
| `813-002` | ? | 7 | 1 | — | Term names dignity as an inner-being quality bestowed on persons — glory and honour given by God to humanity, king, or t |
| `813-003` | ? | 5 | 1 | — | Term names the loss of dignity as inner-being lament — majesty departed, nobility brought low, beauty and splendour stri |
| `904-001` | ? | 17 | 2 | — | Term names holiness as the inner moral character and set-apart orientation by which the person is consecrated to God — t |
| `904-002` | ? | 24 | 1 | — | Term names the person's inner response — reverence, worship, and desire — evoked by encountering the holiness of God in  |
| `904-003` | ? | 3 | 2 | — | Term names the Spirit's holiness as the divine inner presence that grieves over human rebellion and is placed within the |
| `905-001` | ? | 10 | 2 | — | Term names sanctification as the inner moral condition and transformative process by which a person is set apart for God |
| `906-001` | ? | 2 | 2 | — | Term names holiness as the inner moral quality of the person actively pursued and established in the heart — the conditi |
| `907-001` | ? | 2 | 2 | — | Term names holiness as the inner moral character of the renewed person — the quality of the whole life lived before God, |
| `908-001` | ? | 12 | 1 | — | Term names holiness as the inner moral character God calls the person to embody — the imperative to be holy as God is ho |
| `908-002` | ? | 27 | 1 | — | Term names the inner orientation of the person toward the Holy One — the response of the inner being (trust, awe, joy, r |
| `908-003` | ? | 9 | 1 | — | Term names holiness as the identity-constituting set-apart status of the person before God — the person's sacred standin |
| `910-001` | ? | 1 | 1 | — | Term names holiness as the divine character quality that the person is disciplined to share — an inner transformation ma |

### M23 (158 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1148-001` | ? | 32 | 2 | — | Term names voluntary submission as the fundamental inner-relational orientation of the person before God and within huma |
| `1177-001` | ? | 19 | 2 | — | Inner estimation and revaluation — the act of counting, considering, and esteeming as inner cognitive and moral acts; in |
| `1266-001` | ? | 53 | 1 | — | Term names patient inner forbearance — bearing-with of the faithless or difficult, at inner cost |
| `1266-002` | ? | 1 | 1 | — | Term names spiritual fruit-bearing — the inner productive life emerging from abiding in Christ, requiring pruning and se |
| `1266-003` | ? | 1 | 1 | — | Term names being carried along by the Spirit — the inner experience of prophets borne by the Holy Spirit in inspired spe |
| `1266-004` | ? | 1 | 1 | — | Term names divine upholding — Christ bearing all things by the word of his power |
| `1266-005` | ? | 1 | 1 | — | Term names God's patient endurance — divine long-suffering borne toward the resistant |
| `1266-006` | ? | 1 | 1 | — | Term names the inner bearing of reproach — carrying the shame of Christ as costly discipleship |
| `1266-007` | ? | 1 | 1 | — | Term names the inner movement toward maturity — pressing forward to full spiritual development |
| `1266-008` | ? | 1 | 1 | — | Term names inner disposition of hope toward coming grace — setting hope fully on what will be brought at Christ's revela |
| `1304-001` | ? | 1 | 1 | — | Term names the act of domineering over others as an exercise of power — the inner being is engaged through the dispositi |
| `1310-001` | ? | 3 | 1 | — | Term names forceful proclamation — a declaration made with commanding intensity that originates in an inner urgency or a |
| `1311-001` | ? | 1 | 1 | — | Term names the power that God bestows on his people — a capacity imparted to the inner being |
| `1312-001` | ? | 1 | 1 | — | Term names governing authority held by a person by God's appointment — the inner being is engaged through the exercise o |
| `1313-001` | ? | 2 | 1 | — | Term names power as the capacity to command or control — the inner being is engaged through the recognition of the limit |
| `1314-001` | ? | 3 | 1 | — | Term names the capacity to rule or exercise power over others — the inner being is engaged through the divine granting o |
| `1316-001` | ? | 5 | 2 | — | Term names God's active energeia — the working power that raised Christ from the dead, enables Paul's ministry, builds u |
| `1317-001` | ? | 3 | 2 | — | Term names the exercise of authority over persons or oneself — engaging the inner being through disposition toward power |
| `1318-001` | ? | 6 | 2 | — | Term names dominion as the sovereign scope of God's reign or the authority entrusted to persons — the inner being engage |
| `1319-001` | ? | 2 | 1 | — | Term names domineering rule contrasted with servant-oriented inner character — the inner being engaged through orientati |
| `1320-001` | ? | 4 | 2 | — | Term names lordship as a cosmic category — above which Christ reigns, and which persons either submit to or defy, engagi |
| `1322-001` | ? | 16 | 5 | — | Term names the exercise of dominion — the inner being is engaged through the creational mandate to rule with responsibil |
| `1325-001` | ? | 3 | 1 | — | Term names dominion as a capacity to rule — the inner being engaged through the character, scope, and will of those who  |
| `1326-001` | ? | 1 | 1 | — | Term names the exercise of domineering authority in relational/ecclesial context — engaging the inner being through disp |
| `1347-001` | ? | 3 | 1 | — | H7337 describes the expansion or widening of a negative inner drive — greed, consuming appetite, or spiritual unfaithful |
| `1347-002` | ? | 2 | 1 | — | H7337 describes the enlarging of the heart or mouth as an expressive inner-being act — joyful exultation or contemptuous |
| `1355-001` | ? | 6 | 2 | — | Term names the everlasting dominion of God as the object that grounds inner praise, fear, and obedience — and human domi |
| `1356-001` | ? | 18 | 2 | — | Term names divine rule — God's sovereign dominion over nations, nature, and creation — engaging the inner being through  |
| `1356-002` | ? | 49 | 2 | — | Term names human rule — the exercise, experience, or resistance of authority over others — engaging the inner being thro |
| `1356-003` | ? | 2 | 1 | — | Term names the rule of the inner person over themselves — self-mastery over the spirit, passions, and the pull of sin —  |
| `1357-001` | ? | 4 | 2 | — | Term names dominating lordship as a power — sin, death, or law exercising control over the inner life of the person |
| `1357-002` | ? | 2 | 1 | — | Term names the domineering lordship over others' faith and freedom — the disposition of authority that overpowers rather |
| `1358-001` | ? | 11 | 2 | — | The kingdom as the sphere entered through inner transformation — repentance, humility, righteousness as entry conditions |
| `1358-002` | ? | 9 | 2 | — | The kingdom as the supreme object of desire, seeking, and prayer — the will oriented toward the kingdom |
| `1358-003` | ? | 15 | 1 | — | The kingdom as the inheritance conditioned on moral character — those who will or will not inherit |
| `1358-004` | ? | 20 | 2 | — | The kingdom as the identity, belonging, and lived reality of the redeemed |
| `1358-005` | ? | 10 | 1 | — | The kingdom as the object of hope that orients the person toward the eschatological future |
| `204-001` | ? | 1 | 1 | — | Being hemmed in, distressed and confined — the experience of inner constraint before God or suffering |
| `211-001` | ? | 2 | 1 | ✓ | Hardness of constraint as inner-bearing experience — adversity and envious limitation |
| `2775-001` | ? | 2 | 1 | — | Term names persons of high authority or eminence — the inner being engaged through prayer for, humility before, or renun |
| `2805-001` | ? | 5 | 2 | — | Term applied to God's sovereign rule over kingdoms — the inner being engaged through the repeated, humbling recognition  |
| `2808-001` | ? | 1 | 1 | — | Term names messianic dominion extending to universal peace — the inner being engaged through eschatological hope |
| `2837-001` | ? | 50 | 2 | — | Term names the master in parable and teaching contexts — the inner being engaged through faithfulness, fear, accountabil |
| `2837-002` | ? | 5 | 2 | — | Term names the human master in direct household-code instruction — the inner being engaged through the call to sincere o |
| `2837-003` | ? | 9 | 2 | — | Term names the mode of personal address to Jesus as 'Sir/Lord' — the inner being engaged through petition, recognition,  |
| `2847-001` | ? | 3 | 1 | — | Term names the prevailing of a superior force over a person — the inner being engaged through the wisdom of companionshi |
| `2849-001` | ? | 1 | 1 | — | Term names divine might as the limit of human contention — the inner being confronted with the wisdom of submission befo |
| `2850-001` | ? | 1 | 1 | — | Term names royal might as the object of pride — the inner being's self-glorification in its own power, at the very momen |
| `2876-001` | ? | 4 | 1 | — | Term names greatness, majority, or abundance as a quality of persons or communities — the inner being engaged through lo |
| `2877-001` | ? | 3 | 1 | — | Term names the growth of power and pride — addressed through prophetic vision as a warning to the inner being of the sov |
| `2908-001` | ? | 2 | 1 | — | Term names governance as the outward expression of the ruler's inner character — wisdom, justice, righteousness, and pea |
| `2942-001` | ? | 4 | 2 | — | Term names reigning as the domination of sin or grace over the inner life — the person as one who is ruled by competing  |
| `2942-002` | ? | 4 | 1 | — | Term names reigning as the vocation and eschatological state of the faithful — those whose inner fidelity issues in co-r |
| `2942-003` | ? | 3 | 1 | — | Term names reigning as the authority the inner will either refuses or submits to — the disposition of rejection or accep |
| `2943-001` | ? | 1 | 1 | — | Term qualifies the law of love as royal — the supremacy of love as the governing principle of inner conduct toward other |
| `2944-001` | ? | 2 | 1 | — | Term names co-reigning with Christ as the eschatological outcome of inner faithfulness and endurance |
| `2946-001` | ? | 1 | 1 | — | Term names the royal-priestly identity bestowed on the people of God — their constituted dignity and calling before him |
| `2947-001` | ? | 1 | 1 | — | Term names the proud inner self-designation of arrogance — claiming queenly immunity from loss and mourning |
| `2953-001` | ? | 1 | 1 | — | Term names the kingdom as what is given or withdrawn in response to the moral character of its holder |
| `2970-001` | ? | 5 | 2 | — | Kreissōn as inner-being moral judgement that one course is better than another |
| `2970-002` | ? | 14 | 2 | — | Kreissōn as superior quality of new covenant realities constituting faith orientation |
| `2974-001` | ? | 1 | 1 | — | Term names the rule of cosmic order as beyond human establishment — evoking the inner posture of humility before divine  |
| `2992-001` | ? | 4 | 2 | — | Term names the domineering exercise of authority over others — the disposition of control that stands opposed to servant |
| `4517-001` | ? | 2 | 1 | — | Term describes the quality of faith or ministry as genuinely operative — producing real inner-being fruit in knowing and |
| `4517-002` | ? | 1 | 1 | — | Term describes the word of God as actively operative in the inner being — penetrating, dividing, and discerning soul, sp |
| `4518-001` | ? | 2 | 1 | — | Term names the divinely produced inner-operative activities or workings — expressions of God's power active in and throu |
| `4587-001` | ? | 1 | 1 | — | Term names the inner perseverance that overcomes in faith — the volitional struggle that achieves its goal |
| `4923-001` | ? | 15 | 1 | — | Hardening of the heart — wilful inner resistance to God |
| `4923-002` | ? | 36 | 1 | — | 'Be strong and courageous' — divine or prophetic command to inner courage grounded in divine presence |
| `4923-003` | ? | 10 | 1 | — | Strengthening the weak — care for the inner being of another |
| `4923-004` | ? | 12 | 1 | — | Self-strengthening in God — inner act of drawing on divine strength in crisis or mission |
| `4923-005` | ? | 17 | 1 | — | Strengthening that enables or reflects a moral orientation — toward good or ill |
| `4924-001` | ? | 10 | 1 | — | Holding fast to integrity, wisdom, or covenant |
| `4924-002` | ? | 7 | 1 | — | God holding the person — divine grasp as reassurance and covenant |
| `4924-003` | ? | 10 | 1 | — | Being seized by inner anguish, fear, or grief |
| `4924-004` | ? | 5 | 1 | — | The inner-being act of grasping — idols or false support vs God |
| `4925-001` | ? | 2 | 1 | — | Inner resolve expressed as firm insistence or determined compliance |
| `4926-001` | ? | 4 | 1 | — | Prevailing through inner strength or resolve |
| `4926-002` | ? | 3 | 1 | — | Inner character in contest — resolute or irresolute, audacious or guile-driven |
| `4930-001` | ? | 4 | 1 | — | Force as coercive domination — inner disposition of aggression and self-willed domination |
| `4930-002` | ? | 1 | 1 | — | Force as urgent intensity in prayer and repentance |
| `4932-001` | ? | 1 | 1 | — | Comparative growth of strength — prevailing over opposition |
| `4948-001` | ? | 4 | 1 | — | Strength as an inner quality — stoutness of heart, or strength that commands inner awe |
| `4952-001` | ? | 1 | 1 | — | Inner strength as an inadequate resource before divine judgment |
| `5166-001` | ? | 3 | 1 | — | Term names compulsion on inner religious identity and practice — external pressure forcing conformity in the domain of f |
| `5166-002` | ? | 3 | 1 | — | Term names compulsion that overrides or presses on the inner will and disposition — the person constrained to act agains |
| `54-001` | ? | 4 | 1 | — | Inner compulsion, constraint, and distress as motivating or anguishing force |
| `54-002` | ? | 1 | 1 | — | Being seized with fear as inner affective state |
| `601-001` | ? | 13 | 1 | — | Term names the inner command to take heart — courage addressed to the inner life, grounded in Christ's presence and vict |
| `644-001` | ? | 11 | 2 | — | Term names the act of being strong or prevailing — in its inner-being dimension: the Spirit-given strength that prevails |
| `651-001` | ? | 30 | 2 | — | Ge.vu.rah as might of God: object of worship and ground of prayer |
| `651-002` | ? | 16 | 2 | — | Ge.vu.rah as human might: inner-being quality with warning not to boast |
| `653-001` | ? | 8 | 2 | — | Term names the inner dimensions of might — where vastness of power produces inner dread, misplaced trust, unjust oppress |
| `661-001` | ? | 1 | 1 | — | E.yal as inner vitality named in its total absence |
| `662-001` | ? | 1 | 1 | — | Dependence in extremity — e.ya.lut as the inner capacity whose total absence reveals that the person has no resource of  |
| `663-001` | ? | 1 | 1 | — | Dependence-grounded strength — am.tsah as the inner capacity whose source and sustaining ground is God, not the self: st |
| `664-001` | ? | 1 | 1 | ✓ | O.mets as inner moral strength growing in the righteous person |
| `6644-001` | ? | 1 | 1 | — | Divine strengthening of the inner being after suffering — God restores what weakness has depleted |
| `665-001` | ? | 5 | 2 | — | On as vital strength: firstborn as firstfruits of vital energy |
| `665-002` | ? | 4 | 2 | — | Creaturely capacity — on as inner vitality understood as divinely given and controlled: the strength that belongs to the |
| `668-001` | ? | 2 | 1 | — | Term names the inner dynamic where personal strength becomes the condition for pride and spiritual unfaithfulness — stre |
| `668-002` | ? | 1 | 1 | — | Term names the divine hand/strength that comes upon the prophet, orienting and commissioning his inner being |
| `669-001` | ? | 3 | 1 | — | Term names God's redemptive power — the strong hand by which he delivered Israel from Egypt — as the basis for covenanta |
| `669-002` | ? | 1 | 1 | — | Term names the inner disposition of self-reliant pride in one's own strength, set against dependence on God |
| `670-001` | ? | 1 | 1 | — | Term names God as the strength and sufficiency of the inner person, the object of love and relational orientation |
| `671-001` | ? | 1 | 1 | — | Assurance of adequate provision — do.ve as the inner ground of confidence that sufficient strength will be given for eac |
| `672-001` | ? | 2 | 2 | — | Term names strength as either God's gift to the depleted or the power of occult practice that competes with divine autho |
| `673-001` | ? | 3 | 2 | — | Term names the inner substance/might of the person — in its self-attributed pride or genuine divine endowment — as the d |
| `674-001` | ? | 10 | 2 | — | Term names strength as the intensity of inner character — fierce anger, passionate love, or the vigour of committed acti |
| `675-001` | ? | 18 | 2 | — | Term names God as the strength and song of the worshipper — the inner source of praise who is himself the ground of conf |
| `675-002` | ? | 18 | 2 | — | Term names God's strength as the object of communal worship — the strength ascribed to God in the sanctuary as the expre |
| `675-003` | ? | 12 | 2 | — | Term names God's strength as the inner refuge and security of those who trust him — the safe place to which the person r |
| `675-004` | ? | 10 | 2 | — | Term names strength as the attribute tied to moral character — wisdom-linked strength that exceeds raw force, and the et |
| `675-005` | ? | 10 | 2 | — | Term names human strength as the object of God's judgment — the pride of power brought low, the collapse of the strong u |
| `676-001` | ? | 23 | 2 | — | Courage called forth — am.mits as the inner act of strengthening resolve against fear; the divine or prophetic call to b |
| `676-002` | ? | 13 | 2 | — | Care for another's inner capacity — am.mits as the relational act by which one person strengthens the failing inner reso |
| `677-001` | ? | 7 | 2 | — | E.tan as quality of enduring inner strength or resolute capacity |
| `682-001` | ? | 59 | 2 | ✓ | Term names authority granted to persons or God — a legitimate capacity to act, govern, forgive, judge, or rule within a  |
| `682-002` | ? | 15 | 2 | — | Term names a right or legitimate entitlement belonging to persons in personal, communal, or covenantal relationship — th |
| `682-003` | ? | 16 | 2 | ✓ | Term names cosmic or spiritual powers — principalities, forces of darkness, or spiritual authorities — whose existence a |
| `683-001` | ? | 5 | 2 | — | Effective inner agency — ischuō as the inner capacity whose exercise proves effective: faith working through love as the |
| `683-002` | ? | 11 | 2 | — | Ischuō as persons capacity or incapacity in spiritually significant situations |
| `684-001` | ? | 30 | 2 | — | Term names the power of God as the ground of salvation, resurrection, and the believer's hope — the divine capacity upon |
| `684-002` | ? | 43 | 2 | — | Term names a capacity imparted to or operative within persons — empowering the inner being for witness, endurance, minis |
| `684-003` | ? | 2 | 1 | — | Term names the power of sin, law, death, or the adversary as a constraining force over the inner being — from which God  |
| `685-001` | ? | 5 | 2 | — | Divine power as the ground of the inner person's strength — kratos as the might of God that operates as the active sourc |
| `685-002` | ? | 7 | 2 | — | Devotional awe before divine sovereignty — kratos as the prevailing might of God that calls forth inner responses of wor |
| `686-001` | ? | 3 | 2 | — | Ischus as faculty of the whole person for loving God |
| `686-002` | ? | 6 | 2 | — | Ischus as might of God empowering the believer for ministry |
| `688-001` | ? | 9 | 2 | — | Ischuros as comparative strength naming basis for authority or capacity to overcome |
| `688-002` | ? | 6 | 2 | — | Ischuros as inner-being condition of strength or its divine source |
| `689-001` | ? | 1 | 1 | — | Term names the act of strengthening persons with divine power, directed toward inner endurance, patience, and joy |
| `6892-001` | ? | 6 | 2 | — | Term names vastness in the inner-being dimension — the uncountable greatness of God's thoughts and works, and the overwh |
| `6904-001` | ? | 3 | 2 | — | Ga.del as growth of person in inner-being stature and moral character |
| `692-001` | ? | 2 | 1 | — | Katischuō as power that prevails over the church or through inner conviction |
| `6936-001` | ? | 18 | 2 | — | Ga.var as prevailing of strength in inner-being, moral, and covenantal contexts |
| `694-001` | ? | 8 | 2 | — | Term names the act of being strengthened by God in one's inner capacity — for faithfulness, endurance, and effective act |
| `6943-001` | ? | 4 | 2 | — | Term names the overpowering strength of kingdoms — as iron ruthlessness or inner political domination — and its ultimate |
| `6944-001` | ? | 4 | 2 | — | Term names the growth of inner pride into visible strength — the tree that reaches the sky as the image of self-exalting |
| `695-001` | ? | 2 | 2 | — | Inner firmness through faith — stereoō as the establishing of the inner person in stable strength, grounded in and produ |
| `6965-001` | ? | 37 | 2 | — | Term names God's sovereign strength expressed in creation, redemption, judgment, and sustaining power — the incomparable |
| `6965-002` | ? | 23 | 2 | — | Term names the failure and depletion of human strength — in grief, crisis, spiritual exhaustion, and confrontation with  |
| `6965-003` | ? | 6 | 2 | — | Term names human strength as a false object of inner trust or idolatrous self-reliance — the confidence in one's own pow |
| `6965-004` | ? | 9 | 2 | — | Term names God as the giver of renewed strength to the depleted — the inner gift of capacity for those who wait on God,  |
| `6965-005` | ? | 24 | 2 | — | Term names strength as a quality of the inner person — encompassing wisdom-linked capacity, character revealed under adv |
| `7030-001` | ? | 10 | 2 | — | Term names moral-character strength as a quality of the inner person — encompassing the capable woman of Pro 31, the fai |
| `7030-002` | ? | 9 | 2 | — | Term names strength as a God-given inner endowment — the capacity for valour, action, and faithfulness that God gives an |
| `7030-003` | ? | 6 | 2 | — | Term names strength as a false object of inner trust — where military, personal, or national might becomes the basis of  |
| `7030-004` | ? | 7 | 2 | — | Term names acts of valour and worthy conduct as expressions of the inner person's moral and spiritual character |
| `7083-001` | ? | 4 | 2 | — | Stereos as firmness of inner-being foundation and maturity |
| `7107-001` | ? | 1 | 1 | — | Term names the strength of the morally corrupt person as the very substance that will be consumed in judgment — power tu |
| `7108-001` | ? | 1 | 1 | — | Term names God's incomparable might as the ground of the worshipper's awe and dependence — the power that transcends all |
| `7182-001` | ? | 10 | 2 | — | Term names God as the Almighty — the All-Sovereign whose absolute power is the object of worship, the ground of covenant |
| `763-001` | ? | 5 | 1 | — | Divine address of inner courage in personal need, fear, or healing |
| `763-002` | ? | 2 | 1 | — | Divine address of inner courage for mission and endurance under tribulation |
| `859-001` | ? | 12 | 2 | — | Term names divine power or the Spirit operative within persons — God or the Spirit working in the inner life to enable,  |
| `859-002` | ? | 4 | 2 | — | Term names a corrupting or hostile power operative in persons — sinful passion, a hostile spirit, or the mystery of lawl |
| `859-003` | ? | 3 | 2 | — | Term names faith, love, prayer, or the word as operative inner-being forces — these inner realities are active and worki |

### M24 (94 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `104-001` | ? | 3 | 1 | — | Term names the inner condition of languishing — the gradual fading of the person under the weight of sorrow, grief, or u |
| `108-001` | ? | 1 | 1 | — | Term names the aching of the heart — the inner condition of pining, heartache that arises from distress and covenant jud |
| `109-001` | ? | 2 | 1 | — | Term names illness or loathsome condition — the state of being sick or repulsed, and the inner condition that accompanie |
| `1219-001` | ? | 10 | 1 | — | Weakness as the inner-being condition of limitation, vulnerability, and human frailty — the site of divine power |
| `1219-002` | ? | 3 | 1 | — | Weakness and power in tension — the body's present weakness versus resurrection power; Christ's weakness as the pattern |
| `1295-001` | ? | 1 | 1 | — | Term names the sick/morbid craving of the inner person — the unhealthy inner obsession with controversy that produces en |
| `133-001` | ? | 9 | 1 | — | Term names sickness and grief as an inner-being condition — the suffering, grief, and moral sickness borne by persons, n |
| `1372-001` | ? | 16 | 1 | — | Term names spiritual blindness as the inner condition of the person who claims to see but does not — self-deception, har |
| `1372-002` | ? | 22 | 1 | — | Term names physical blindness as the condition the Messiah proclaims he will heal — the restoration of perceptual capaci |
| `1373-001` | ? | 2 | 1 | — | Term names slothfulness as an inner disposition that produces stupor and material ruin — inaction consuming the person f |
| `1374-001` | ? | 11 | 1 | — | Term names the sluggard as a person whose inner desire craves but whose will refuses to act — passivity, inertia, and se |
| `1374-002` | ? | 3 | 1 | — | Term names the sluggard's inner self-deception — rationalisation and inflated self-regard enabling continued avoidance |
| `1375-001` | ? | 13 | 1 | — | Term names the inner collapse of courage and resolve — feeble hands, fainting spirit, melting heart in the face of threa |
| `1375-002` | ? | 6 | 1 | — | Term expresses divine faithfulness as the refusal to forsake — the assurance that addresses the inner fear of abandonmen |
| `1375-003` | ? | 12 | 1 | — | Term describes the inner act of releasing, ceasing, or becoming still — letting go of wrath, being still before God, hol |
| `1375-004` | ? | 4 | 1 | — | Term names the inner disposition of slackness and procrastination — the failure to act that is morally equivalent to des |
| `1397-001` | ? | 3 | 1 | — | Term names the moment of expiry as consequence of inner moral failure — deception and pride resulting in death as divine |
| `1399-001` | ? | 1 | 1 | — | Term names overwhelming inner fear and foreboding causing fainting — the person's inner being overtaken by eschatologica |
| `141-001` | ? | 8 | 1 | — | Term names the inner suffering inflicted on the person — grief from oppression, exile, and divine discipline, which God  |
| `153-001` | ? | 18 | 2 | — | Term names inner weariness — the exhaustion of the inner person (or divine person) through sustained effort, trial, or m |
| `156-001` | ? | 2 | 1 | — | Term names the constraining quality of anguish and its resolution — inner experience of being hemmed in, cramped, and th |
| `162-001` | ? | 3 | 1 | — | Term names the narrow straits of extreme inner distress — the pressing constraint from which prayer rises and God respon |
| `173-001` | ? | 9 | 1 | — | Oppression as force bearing down on the inner person — the experience of being driven, pressed, afflicted |
| `186-001` | ? | 2 | 1 | — | Term names the inner-being condition of the person in misery — the one whose inner life is consumed by bitter suffering  |
| `187-001` | ? | 12 | 1 | — | Term names the humble/meek person — one whose inner disposition is characterised by lowliness, teachableness, and openne |
| `187-002` | ? | 9 | 1 | — | Term names the poor/afflicted person — one whose inner experience is shaped by material need, oppression, and dependence |
| `190-001` | ? | 18 | 1 | — | Term names the affliction of the person or people as it is seen and heard by God — the inner-being suffering that draws  |
| `190-002` | ? | 18 | 1 | — | Term names affliction as the inner experience of the person — the furnace through which God refines and teaches, the con |
| `191-001` | ? | 13 | 1 | — | Grief and inner pain — being grieved, distressed, or pained at heart |
| `1923-001` | ? | 33 | 1 | — | Term names the experience of being afflicted or oppressed — the inner suffering, loss of dignity, and vulnerability of t |
| `1923-002` | ? | 15 | 2 | — | Term names God's deliberate humbling of a person or people — the inner work of affliction that tests what is in the hear |
| `1923-003` | ? | 15 | 1 | — | Term names the inner act of self-humbling before God — the voluntary afflicting of oneself through fasting, penitence, a |
| `1923-004` | ? | 9 | 1 | — | Term names the inner experience of the afflicted person — the condition of deep suffering through which faith is tested, |
| `21-001` | ? | 5 | 1 | — | Term names the affliction overcome in Christ — anguish as the condition the world inflicts but Christ has conquered, giv |
| `21-002` | ? | 4 | 1 | — | Term names affliction as the ground of inner character formation — anguish producing endurance, character, and hope thro |
| `21-003` | ? | 8 | 1 | — | Term names the anguish of shared suffering and consolation — the inner participation in Christ's afflictions as the grou |
| `21-004` | ? | 8 | 1 | — | Term names the anguish of the great tribulation — the maximum suffering of the end times as the context of final purific |
| `212-001` | ? | 2 | 1 | ✓ | Times of distress as context of inner appeal and trust in God |
| `214-001` | ? | 2 | 1 | ✓ | The vexer as source of inner distress — provocation grieving the spirit |
| `216-001` | ? | 4 | 1 | — | Distress as acute inner condition — the moment of extremity, terror, and desperate appeal to God |
| `2494-001` | ? | 5 | 2 | — | Term names the hardship endured on the way — the suffering borne by a people under God's leadership or under judgment, e |
| `25-001` | ? | 2 | 1 | ✓ | Distress and oppression as inner and social suffering |
| `2770-001` | ? | 2 | 2 | — | Term names oppression as a power exerted over persons — engaging the inner being through bondage, suffering, and the dig |
| `2781-001` | ? | 1 | 1 | — | Term names moral deficiency revealed by divine assessment — the inner being found morally wanting before God |
| `4816-001` | ? | 1 | 1 | — | Breaking of the heart — inner person shattered by grief, expressed in embodied anguish as a sign before others |
| `51-001` | ? | 4 | 1 | — | Distress as existential suffering condition |
| `5192-001` | ? | 10 | 1 | — | Stubbornness and stiff-necked resistance — inner moral obstinacy |
| `5192-002` | ? | 13 | 1 | — | Harshness and rough treatment as inner character quality expressed outward |
| `5192-003` | ? | 4 | 1 | — | Broken spirit under harsh oppression — inner bearing of suffering |
| `5311-001` | ? | 6 | 1 | — | Harm inflicted and inner assurance against it — the fear of harm and God's protection |
| `5493-001` | ? | 2 | 1 | — | Term names divine inviolability of those held in the Father's and Son's hand — the inability of any agent to seize the C |
| `5493-002` | ? | 5 | 1 | — | Term names the divine catching away of the person — eschatological rapture, Spirit transportation, and protective snatch |
| `5493-003` | ? | 2 | 1 | — | Term names violent assault on inner being — the snatching-away of the implanted word from the heart, or the wolf-attack  |
| `5493-004` | ? | 1 | 1 | — | Term names forceful inner pursuit — the kingdom-of-heaven seized by force, the inner-being violence that lays hold of Go |
| `5493-005` | ? | 1 | 1 | — | Term names redemptive rescue by human agent — the snatching-out of others from fire-judgement context as an act of mercy |
| `5813-001` | ? | 2 | 1 | — | Failing of inner faculties — trembling heart, failing eyes, languishing soul — marks of the person under judgment |
| `5840-001` | ? | 12 | 2 | — | Term names crushing as an inner moral reality — the oppression that degrades and destroys the vulnerable, and the gentle |
| `5841-001` | ? | 1 | 1 | — | Term names oppression as the outward expression of an inward orientation — the eyes and heart fixed wholly on dishonest  |
| `588-001` | ? | 11 | 1 | — | Term names the withering of inner vigour — the fading of inner strength or courage under pressure or judgment |
| `588-002` | ? | 10 | 1 | — | Term names the withering of the spirit as a moral metaphor — spiritual apostasy pictured as withering |
| `6210-001` | ? | 3 | 1 | — | Term names coercive oppression and restraint — where oppression diminishes the inner life, the barren womb expresses ins |
| `6384-001` | ? | 2 | 1 | — | Term names an inner condition of sickness or faintness — applied to the heart as the inner organ, expressing grief-induc |
| `6639-001` | ? | 2 | 1 | — | "The spirit is willing but the flesh is weak" — the inner-being's aspiration limited by the weakness of the flesh |
| `6639-002` | ? | 5 | 1 | — | Weak in conscience — vulnerability of the inner moral faculty |
| `6639-003` | ? | 9 | 1 | — | Human weakness as the condition of grace — God chooses, Christ dies for, the weak |
| `6642-001` | ? | 6 | 1 | — | Weakness in faith and conscience — the inner-being condition of limited conviction or vulnerable moral formation |
| `6642-002` | ? | 7 | 1 | — | Weakness as the inner-being posture Paul embraces — solidarity, paradox, and power through weakness |
| `6643-001` | ? | 1 | 1 | — | The failings of the weak — inner-being scruples to be borne in community |
| `69-001` | ? | 4 | 1 | — | Term names the inner-experiential dimension of intense anguish — birth pangs as a figure for overwhelming spiritual-exis |
| `6948-001` | ? | 4 | 2 | — | Term names the fainting/exhaustion of human strength as the condition of those who wait without God — and the divine ren |
| `6948-002` | ? | 4 | 2 | — | Term names exhaustion/wearying as the consequence and expression of misdirected inner effort — the labour that leads to  |
| `709-001` | ? | 4 | 1 | ✓ | Bitter toxic quality of suffering and judgment — poison/gall as inner experience of affliction brought before God, or as |
| `716-001` | ? | 4 | 1 | — | Breaking of the spirit — inner person shattered by perversion, pride, or affliction, with the spirit explicitly named as |
| `716-002` | ? | 9 | 1 | — | Inner wound — the deep hurt of person or people that demands honest naming and resists superficial healing |
| `716-003` | ? | 3 | 1 | — | Brokenness healed and brokenness mourned — God's binding up of the broken inner person, and inner grief of those who fee |
| `7222-001` | ? | 11 | 2 | — | Term names illness as the condition that Jesus heals — the embodied suffering that he takes upon himself and from which  |
| `7353-001` | ? | 1 | 1 | — | Term names sluggishness as the inner disposition of hesitation that must be overcome in pursuing God's purpose |
| `7354-001` | ? | 1 | 1 | — | Term names idleness as an inner disposition that the person of virtue refuses — its absence marking inner diligence and  |
| `7422-001` | ? | 2 | 1 | — | Deliberate mortification of inner-being capacities — putting to death what is earthly |
| `7438-001` | ? | 3 | 1 | — | Term describes the act of blinding the inner capacities — eyes and mind — whether through hatred, spiritual adversary, o |
| `7446-001` | ? | 1 | 1 | — | Term names disease as a condition in which the inner person encounters divine restoration — illness as the context of fo |
| `7552-001` | ? | 3 | 1 | — | inner-being anguish — the crushing of the person by suffering, adversity, or hostile words |
| `7552-002` | ? | 2 | 1 | — | substitutionary crushing — the Servant's inner person crushed for iniquity, producing peace and healing |
| `7552-003` | ? | 2 | 1 | — | the contrite and crushed inner spirit — the condition of brokenness before God that occasions divine presence, and its r |
| `7554-001` | ? | 3 | 1 | — | the broken and contrite heart as the inner sacrifice acceptable to God — inner brokenness in penitence and suffering |
| `7554-002` | ? | 1 | 1 | — | corporate inner desolation under divine crushing — the community broken by God in distress |
| `7555-001` | ? | 1 | 1 | — | the humble and contrite spirit — the broken inner posture before God that receives divine attention |
| `7556-001` | ? | 1 | 1 | — | inner terror and panic — the inner state of dismay accompanying devastating defeat |
| `805-001` | ? | 1 | 1 | — | Term names the inner collapse of the person under reproach — the condition of despair in which the heart is broken, pity |
| `857-001` | ? | 7 | 1 | — | Wrongdoing and suffering wrong — the inner moral act and its bearing on the one wronged and the wrongdoer |
| `892-001` | ? | 2 | 1 | — | Term names rapacity as inner moral condition — the inner fullness of greedy desire that the Pharisees' outward propriety |
| `892-002` | ? | 1 | 1 | — | Term names the external plundering accepted with inner joy — the loss occasioned by faith that has secured 'a better pos |
| `926-001` | ? | 19 | 1 | — | Term names the afflicted/poor person — one whose inner experience is defined by material need, oppression, and dependenc |
| `926-002` | ? | 4 | 1 | — | Term names the afflicted person as the object of God's compassion — the one to whom God attends, comforts, and promises  |

### M25 (27 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1390-001` | ? | 3 | 1 | — | Term names the refreshing of the inner person through rest — restoration of the inner being through Sabbath rest |
| `4638-001` | ? | 5 | 1 | — | Term names the divine rousing of the human spirit to action — God stirring the inner person to a specific volitional res |
| `4638-002` | ? | 4 | 1 | — | Term names the restraint of inner love-arousal — the guarding of love against premature or disordered awakening |
| `4638-003` | ? | 4 | 1 | — | Term names the inner moral stirring of the person toward righteousness or God — self-rousing of the inner life in respon |
| `4738-001` | ? | 33 | 1 | — | Life as contingent on inner-being orientation — obedience, fear, seeking, and choosing God as the condition of life; als |
| `4738-002` | ? | 27 | 1 | — | Word of God and the Spirit as source of inner-being life — life received from God's word, promise, or Spirit as sustaini |
| `4738-003` | ? | 12 | 1 | — | Divine revival of the inner person — God restoring life to the spirit and heart of those depleted, contrite, or despairi |
| `4738-004` | ? | 6 | 1 | — | Inner-being wrestling with life — weight, value, perplexity, and hope of being alive in the face of death |
| `4739-001` | ? | 3 | 1 | — | God's gift of reviving — inner-being renewal of a people or person after affliction, understood as divine favour overtur |
| `4742-001` | ? | 1 | 1 | — | Living in inner-being suspension — physically alive but existentially and relationally confined, as if dead |
| `613-001` | ? | 48 | 1 | — | Term names the Holy Spirit as the divine transforming presence — filling, leading, interceding, bearing witness with the |
| `613-002` | ? | 48 | 1 | — | Term names the human spirit as the seat of inner life — the person's spirit that prays, serves, is troubled, fervent, re |
| `613-003` | ? | 48 | 1 | — | Term names the spirit-flesh contrast — the spirit willing but flesh weak; inner orientation toward God vs. the flesh's o |
| `613-004` | ? | 48 | 1 | — | Term names the unclean/evil spirit — the spiritual being oppressing human persons; the inner-being impact of spiritual a |
| `613-005` | ? | 48 | 1 | — | Term names spirit-characterised orientations — spirit of adoption, stupor, fear, power/love/self-control; shaping the pe |
| `613-006` | ? | 48 | 1 | — | Term names the life-giving Spirit and the giving up of spirit — Christ as life-giving spirit; the moment of death as yie |
| `613-007` | ? | 53 | 1 | — | Term names the spiritual gifts — the Spirit's varied manifestations for the common good; the distribution of the Spirit' |
| `614-001` | ? | 3 | 1 | — | Term names breath/wind as a metaphor for the Spirit's sovereign invisible inner work; and divine breath as the vehicle o |
| `615-001` | ? | 2 | 1 | — | Term names the divine breath of life — God breathing into the person the breath constituting inner human existence; prop |
| `615-002` | ? | 4 | 1 | — | Term names the divine breath as judgment or discipline — God blowing in wrath or covenantal intervention |
| `615-003` | ? | 6 | 1 | — | Term names breath as inner vitality — fainting when inner vitality is exhausted; the life-breath connection to inner ene |
| `699-001` | ? | 12 | 1 | — | Living God as ground and object of the inner person's deepest orientation — soul's thirst, worship, and trust directed t |
| `699-002` | ? | 10 | 1 | — | Life as the God-given condition within which the inner person exists, fears, and responds — fearing God all one's days |
| `699-003` | ? | 16 | 1 | — | Inner-being quality of the living — awareness of mortality, hope, wisdom, and thanksgiving as distinguishing capacities  |
| `699-004` | ? | 4 | 1 | — | Life as fruit of divine redemption and inner-being turning — restoration to life as outcome of repentance, trust, or div |
| `7035-001` | ? | 1 | 1 | — | Term names the sovereign's arbitrary power over life — whose will decides whether another lives or dies — expressing the |
| `744-001` | ? | 6 | 2 | — | Term names corruption/decay as the condition the inner person faces in death — and the overcoming of this corruption thr |

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

### M27 (30 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1343-001` | ? | 2 | 1 | — | H8074G describes the desolation of a person or personified community in a way that directly discloses or occasions an in |
| `197-001` | ? | 3 | 1 | — | Term names the ritual category of defilement as a boundary of inner spiritual integrity — what the inwardly devoted pers |
| `235-001` | ? | 5 | 1 | — | Bad news and evil report as occasion of inner fear, grief or sadness |
| `235-002` | ? | 6 | 1 | — | Bad/harmful spirit as inner torment — the harmful spirit afflicting Saul |
| `235-003` | ? | 8 | 1 | — | Evil experienced as inner-bearing suffering condition — unhappy business, grievous evil |
| `237-001` | ? | 17 | 1 | — | Evil as inner moral disposition — wickedness conceived in the heart, intended, and enacted |
| `237-002` | ? | 10 | 1 | — | Evil as experienced suffering — distress, harm, and calamity borne by persons |
| `237-003` | ? | 10 | 1 | — | Evil repaid and returned — the moral economy of wrong done and consequences borne |
| `239-001` | ? | 14 | 1 | — | Being evil and doing wickedly — inner moral disposition enacted |
| `239-002` | ? | 14 | 1 | — | Displeasure and anger as inner affective response — being displeased, grieved, or made sad |
| `239-003` | ? | 10 | 1 | — | Harm and calamity as inner-bearing experience — being treated harshly, brought low, or suffering hurt |
| `246-001` | ? | 2 | 1 | ✓ | Term names the commanded inner revulsion — the active rejection of what is unclean as an expression of obedience and mor |
| `246-002` | ? | 1 | 1 | ✓ | Term names the reflexive self-defilement — the inner corruption that results from transgression, making the person thems |
| `246-003` | ? | 1 | 1 | ✓ | Term names divine non-revulsion toward the afflicted — God does not abhor those who suffer; affliction does not make a p |
| `4901-001` | ? | 10 | 2 | — | Term names the corruption of the inner moral life — acting corruptly before God as the expression of the person's inward |
| `4901-002` | ? | 2 | 2 | — | Term names self-destruction as the consequence of inner moral failure — the person who corrupts themselves bringing ruin |
| `4901-003` | ? | 2 | 2 | — | Term names the divine act of destruction as the response to inner moral corruption — God's judgment that mirrors the peo |
| `5196-001` | ? | 8 | 1 | — | Idol as object of inner attachment, devotion and spiritual bondage |
| `5548-001` | ? | 5 | 1 | — | Term names the idol as the object of misplaced inner orientation — the thing toward which the person's allegiance, rejoi |
| `5548-002` | ? | 6 | 1 | — | Term names the idol in relation to inner conviction or conscience — in theological understanding, moral formation, or th |
| `5549-001` | ? | 10 | 1 | — | Term names food sacrificed to idols as the occasion of an inner conscience crisis — the act of eating or abstaining gove |
| `5550-001` | ? | 7 | 1 | — | Term names the idolater as a person whose inner orientation is toward created things rather than God — a defining inner  |
| `5552-001` | ? | 1 | 1 | — | Term names the idol's temple as the site where a brother's weak conscience can be damaged — the location triggers an inn |
| `5553-001` | ? | 1 | 1 | — | Term names a city full of idols — the external condition that provokes an inner response of the spirit, disclosing the p |
| `612-001` | ? | 4 | 1 | — | Term names the shades as those who have lost the capacity for praise — the departed whose inner-being engagement with Go |
| `612-002` | ? | 3 | 1 | — | Term names the path of folly leading to the company of the dead — inner moral choices directing the person toward Sheol |
| `612-003` | ? | 1 | 1 | — | Term names the resurrection hope — the dead of God's people shall live and rise; the inner-being of the righteous awaiti |
| `807-001` | ? | 1 | 1 | — | Term names the condition of devastation as the context for an inner failure of response — the desolation that no one rec |
| `843-001` | ? | 4 | 1 | — | Doing evil as inner moral choice — the choice between good and harm as an inner-being decision |
| `913-001` | ? | 4 | 1 | — | Term names idolatry as an inner orientation — the displacement of God by created things as the object of the heart's ult |

### M28 (58 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1111-001` | ? | 1 | 1 | — | Term names lack of self-control as an inner vulnerability — the absence of inner restraint that creates exposure to temp |
| `1220-001` | ? | 10 | 1 | — | Whoredom as a spiritual / inner-being condition — the spirit of whoredom within that orients people away from God toward |
| `1221-001` | ? | 37 | 1 | — | Spiritual whoredom — Israel/Judah "whoring after" foreign gods, forsaking the Lord; covenantal heart-departure |
| `1221-002` | ? | 2 | 1 | — | "A spirit of whoredom" — whoredom as a driving inner disposition and inner-being faculty |
| `1221-003` | ? | 1 | 1 | — | "Your heart and your own eyes, which you are inclined to whore after" — the inner mechanism of desire as the root of who |
| `1221-004` | ? | 15 | 1 | — | Term names whoredom or its state in inner-being-engaged ways — the active will and desire engaged in sexual unfaithfulne |
| `1221-005` | ? | 18 | 1 | — | Ezekiel's "whoring heart" allegory — inner-being characterisation of Jerusalem/Israel's spiritual condition |
| `1222-001` | ? | 9 | 1 | — | Whoredom as inner-being corruption — defilement of the relational space with God; the act that takes away understanding |
| `1630-001` | ? | 5 | 1 | — | Term names the precious/desirable thing as the object of inner-being longing — the valued possession or quality that the |
| `1630-002` | ? | 3 | 1 | — | The loss or desecration of what is precious — inner-being grief |
| `19-001` | ? | 6 | 1 | — | Term names self-seeking rivalry as an inner disposition — the heart oriented toward self-promotion, expressed through co |
| `218-001` | ? | 1 | 1 | ✓ | Rivalry as relational dynamic producing inner jealousy and distress |
| `3008-001` | ? | 1 | 1 | — | Term names the fleshly heart as the tablet of new covenant writing — the Spirit inscribing the new covenant on the inner |
| `3008-002` | ? | 1 | 1 | — | Term names physical/fleshly descent as insufficient — contrasted with the inner power of indestructible life |
| `3090-001` | ? | 5 | 1 | — | Pleasure as the competing inner orientation — desires that war within and displace the good |
| `342-001` | ? | 9 | 1 | — | Envy as inner moral disposition — resentment of another's good and murderous rivalry |
| `345-001` | ? | 1 | 1 | — | Envying as inner disposition of competitive resentment |
| `347-001` | ? | 1 | 1 | — | The envious gaze — inner resentment expressed as hostile watching |
| `460-001` | ? | 9 | 1 | — | Term names the cherished object of deepest desire — what the inner being holds most dear, and whose loss or destruction  |
| `462-001` | ? | 9 | 1 | — | Term names desirability or preciousness as the quality that draws the inner being — what is cherished, longed for, or gr |
| `464-001` | ? | 12 | 2 | — | Term names destructive inner desire — the evil craving or ruinous orientation of the wicked person's soul, which drives  |
| `465-001` | ? | 4 | 1 | — | Term names the object of inner desire — what the person specifically longs for or purposes; desire as directed toward a  |
| `467-001` | ? | 5 | 1 | — | Term names the inner longing or attachment of a person — the soul's desire for another person, or purposive desire direc |
| `467-002` | ? | 3 | 1 | — | Term names divine inner attachment — God's love set on a person or people as an act of inner binding |
| `469-001` | ? | 9 | 1 | — | Term names the destructive craving of the wicked — desire as an inner force that boasts, grasps, goes unsatisfied, and u |
| `469-002` | ? | 9 | 1 | — | Term names the righteous person's desire — the inner longing that orients toward God or what is genuinely good, and that |
| `469-003` | ? | 2 | 1 | — | Term names desire as a primal inner state — the original experience of the inner being drawn toward what appears good or |
| `470-001` | ? | 3 | 1 | ✓ | Term names desire as a deep relational force of attraction — the inner pull of one being toward another, capable of bein |
| `471-001` | ? | 2 | 1 | ✓ | Term names lust or erotic desire as an inner disposition — the inner appetite that shapes speech and outward conduct whi |
| `4784-001` | ? | 2 | 1 | — | Inner quality of bitterness characterising destructive inner dispositions — bitter jealousy as inner state of the heart |
| `480-001` | ? | 3 | 1 | — | Term names craving or appetite as a disruptive inner force — desire for physical gratification that overrides proper ori |
| `480-002` | ? | 17 | 1 | — | Term names desire as the governing orientation of the soul — what the inner being inclines toward, craves, or chooses as |
| `480-003` | ? | 3 | 1 | — | Term names intense personal longing — the soul expressing deep yearning toward a specific person or object |
| `480-004` | ? | 3 | 1 | — | Term names the sovereign desire of God — his inner purposive longing or choice expressed as divine will toward its objec |
| `481-001` | ? | 9 | 1 | — | Term names coveting — the prohibited inner desire for what belongs to another; desire as acquisitive grasping that viola |
| `481-002` | ? | 5 | 1 | — | Term names desire as positive inner orientation — delight in what is genuinely good, beautiful, or worthy |
| `481-003` | ? | 3 | 1 | — | Term names idolatrous or misdirected desire — inner longing directed toward what does not profit or toward spiritual fal |
| `481-004` | ? | 1 | 1 | — | Term names the divine inner desire — God's own longing for a place or his people |
| `492-001` | ? | 32 | 1 | — | The desires of the flesh — competing inner orientation against God, driving sin |
| `492-002` | ? | 3 | 1 | — | Earnest desire as positive inner-being orientation — longing for what is good |
| `492-003` | ? | 2 | 1 | — | Desire as the generative mechanism — origin of sin in the inner being |
| `497-001` | ? | 1 | 1 | — | Term names consuming inner appetite or passion driving disordered conduct — desire as an overpowering inner force |
| `505-001` | ? | 1 | 1 | — | Term names a compelling inner passion or sensual desire that draws the person away from a prior commitment — the force o |
| `506-001` | ? | 1 | 1 | — | Term names deep personal affective longing — an inner state of tender desire for another person |
| `548-001` | ? | 1 | 1 | — | Term names the inner disposition of lust — the corrupted desire that drives spiritual adultery and moral ruin |
| `564-001` | ? | 1 | 1 | — | Term names love of money as a disordered inner orientation — a root of all kinds of evils that corrupts faith and pierce |
| `568-001` | ? | 2 | 2 | — | Term names love of money as an inner character trait — a disposition marking the Pharisee's distorted orientation and th |
| `570-001` | ? | 1 | 1 | — | Term names love of pleasure as a disordered inner orientation — set in direct contrast to love of God as the mark of the |
| `623-001` | ? | 10 | 1 | — | Term names the inner disposition of debauchery — shameless abandonment to sensuality; the callous inner self-surrender t |
| `626-001` | ? | 3 | 1 | — | Term names the fleshly inner condition — the person dominated by the flesh, manifesting in jealousy, strife, and spiritu |
| `626-002` | ? | 5 | 1 | — | Term names the fleshly inner orientation in conflict with the Spirit — fleshly wisdom, weapons, passions warring against |
| `778-001` | ? | 9 | 1 | — | Covetousness as the insatiable inner orientation toward possessing more |
| `778-002` | ? | 2 | 1 | — | Covetousness as idolatry — the ultimate inner-being misalignment |
| `779-001` | ? | 3 | 1 | — | Debauchery as the inner orientation of dissolute self-indulgence, contrasted with Spirit-filling |
| `893-001` | ? | 4 | 1 | — | Term names the greedy person as a moral-character type — the inner disposition of insatiable acquisitive desire that con |
| `939-001` | ? | 3 | 2 | — | Term names the provocation of human jealousy as a divine redemptive instrument — the inner state of jealousy stirred to  |
| `939-002` | ? | 1 | 1 | — | Term names the provocation of divine jealousy — the inner disposition of God stirred when his people turn to idols |
| `969-001` | ? | 19 | 2 | — | Term names Israel's spiritual fornication — the inner disposition of disordered desire driving pursuit of foreign gods a |

### M29 (22 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `2074-001` | ? | 5 | 1 | — | Eagerness as the inner disposition of forward-leaning readiness toward God and good |
| `3055-001` | ? | 19 | 1 | — | Being willing, content, or pleased — the inner state of consent, determination, or desire governing action |
| `3058-001` | ? | 3 | 1 | — | Term names the freewill inner disposition — voluntary offering or willingness expressed in dedication to God's house |
| `3059-001` | ? | 15 | 2 | — | Term names the inner disposition of willing, voluntary devotion — the heart spontaneously moved to give or serve without |
| `3081-001` | ? | 2 | 1 | — | Acting of one's own accord — voluntary inner impulse expressed in giving and service |
| `456-001` | ? | 18 | 1 | — | Term names divine favour — God's inner disposition of acceptance, goodwill, and relational warmth extended to a person o |
| `456-002` | ? | 22 | 1 | — | Term names what is acceptable or delightful to God — God's inner moral and aesthetic standard by which offerings, conduc |
| `456-003` | ? | 7 | 1 | — | Term names the divine will as sovereign purpose — what God wills and takes pleasure in as an act of inner purposive auth |
| `456-004` | ? | 9 | 1 | — | Term names human will or pleasure — what the person wills, desires, or takes pleasure in as an expression of their inner |
| `488-001` | ? | 6 | 1 | — | Term names the sovereign divine will — God's inner purposive willing expressed in the giving, ordering, and overturning  |
| `488-002` | ? | 1 | 1 | — | Term names the human inner desire for understanding — the person's will directed toward knowing truth |
| `498-001` | ? | 1 | 1 | — | The one who desires evil — inner orientation defined by craving what is wrong |
| `513-001` | ? | 7 | 1 | — | Term names the divided inner will — the person wills the good but finds themselves doing what they do not will; inner co |
| `513-002` | ? | 14 | 1 | — | Term names God's own inner willing — his purposive desire toward mercy, election, redemption, and his sovereign ordering |
| `513-003` | ? | 14 | 1 | — | Term names the submitted or aligned will — human willingness to follow, yield, or conform to God's will, including the s |
| `513-004` | ? | 15 | 1 | — | Term names the misdirected or self-serving will — human willing oriented toward wrong ends, defiance, self-advancement,  |
| `513-005` | ? | 70 | 1 | — | Term names the direction of the human will in ordinary personal, relational, and pastoral contexts — what the person inc |
| `514-001` | ? | 26 | 1 | — | Term names the divine will as the object of human alignment, obedience, and discernment — the inner posture of submissio |
| `514-002` | ? | 25 | 1 | — | Term names the divine will as God's sovereign inner purpose — the ground of election, calling, providence, and redemptio |
| `514-003` | ? | 7 | 1 | — | Term names the human will or desire as an inner faculty — capable of self-determination, misdirection, or capture by an  |
| `936-001` | ? | 5 | 2 | — | Term names the formed inner inclination of the heart — the moral orientation shaped within the person, inclining toward  |
| `936-002` | ? | 3 | 1 | — | Term names the creaturely formation known and addressed by God — the constitution of the human person as formed creature |

### M30 (43 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1085-001` | ? | 2 | 1 | — | Term names rebellion as an inner act of hardening — the wilful resistance to God's voice expressed as a hardened heart r |
| `1086-001` | ? | 12 | 1 | — | Term names rebellion against God as an inner act of wilful defiance — the deliberate rejection of covenantal obligation  |
| `1086-002` | ? | 9 | 1 | — | Term names rebellion against human authority as an inner act of will — the deliberate choice to resist political authori |
| `1087-001` | ? | 1 | 1 | — | Term names rebellion as an inner act of wilful breach against the Lord — the covenantal heart-posture of defiance acknow |
| `1088-001` | ? | 1 | 1 | — | Term names rebellion as the characteristic inner disposition of a community in persistent defiance of authority |
| `1145-001` | ? | 10 | 2 | — | Term names stubbornness of heart — the inner condition of wilful self-determination that refuses God's word and follows  |
| `1146-001` | ? | 1 | 1 | — | Term names stubbornness as an inner condition of hardened resistance to God — the refusal to yield, named alongside wick |
| `1193-001` | ? | 1 | 1 | — | Prophetic madness as the inner expression of lawlessness — the transgression of Balaam expressed as inner madness restra |
| `1199-001` | ? | 4 | 1 | — | Term names refusal of the Son / word / gospel — inner-being refusal directed at the divine self-revelation in Christ |
| `1199-002` | ? | 3 | 1 | — | Term names active unbelief expressing itself in hostility against gospel-bearers — the persistent inner refusal that iss |
| `1199-003` | ? | 1 | 1 | — | Term names refusal of moral truth — inner non-conformity that prefers unrighteousness |
| `1199-004` | ? | 4 | 1 | — | Term names corporate covenantal disobedience in salvation-history — the persistent inner refusal of a people that occasi |
| `1199-005` | ? | 2 | 1 | — | Term names covenantal disobedience as relational state in Paul's mercy-logic — the prior or current state that mercy is  |
| `1226-001` | ? | 4 | 1 | — | Lawlessness as an inner disposition requiring forgiveness and forming a bond of slavery |
| `1226-002` | ? | 1 | 1 | — | Loving righteousness and hating wickedness — inner dispositions in contrast |
| `332-001` | ? | 1 | 1 | — | Term names inner callousness — the loss of moral sensitivity that opens the inner person to sensuality and every kind of |
| `4379-001` | ? | 193 | 2 | — | Term names the inner disposition of covenantal obedience — the will, heart, and soul directed toward faithful keeping of |
| `4380-001` | ? | 40 | 2 | — | Term names God's guarding of his people — the divine inner disposition of protective care that preserves, shields, and k |
| `4380-002` | ? | 36 | 2 | — | Term names self-keeping from moral harm — the inner discipline of guarding one's ways, mouth, and soul from sin and its  |
| `4381-001` | ? | 22 | 1 | — | Term names attentive moral observation — watching over conduct, marking iniquity, or directing inner regard toward a per |
| `4382-001` | ? | 75 | 2 | — | Term names careful, attentive inner vigilance — the disposition of watchfulness toward one's conduct, duties, or dangers |
| `4478-001` | ? | 1 | 1 | — | Term names the insensitive heart — rendered unfeeling like fat, incapable of genuine response to God or his word |
| `4786-001` | ? | 1 | 1 | — | Bitter rebellion — inner act of wilful embittered resistance against God's word after having heard it; hardening against |
| `4838-001` | ? | 1 | 1 | — | Term names the hardened, unrepentant condition of the inner person — the heart closed against God's claims, resistant to |
| `5111-001` | ? | 1 | 1 | — | Term names the wilful refusal to hear — the inner orientation of closed attention or contempt expressed through the repe |
| `5502-001` | ? | 5 | 2 | — | Term names the hardening of the inner being — the heart or mind rendered impervious to spiritual perception, understandi |
| `597-001` | ? | 3 | 1 | — | Term names hardness of heart as a moral condition — inner disposition of stubborn resistance refusing God's covenantal p |
| `6007-001` | ? | 20 | 2 | — | Term names rebellion as an inner-being condition of the community before God — the persistent, characterising orientatio |
| `6075-001` | ? | 26 | 1 | — | Term names the removal of idols and objects of false worship as an inner act of reorientation — putting away foreign god |
| `6075-002` | ? | 38 | 1 | — | Term names the removal or loss of inner-being realities — God's steadfast love withdrawn, the heart of stone removed, gu |
| `6075-003` | ? | 17 | 1 | — | Term names the moral-volitional act of putting away inner dispositions and corrupting elements — vexation, false ways, c |
| `6076-001` | ? | 21 | 1 | — | Term names the inner act of turning aside from God's way — the volitional departure from covenantal faithfulness express |
| `6076-002` | ? | 20 | 1 | — | Term names the inner disposition of faithfulness expressed by not turning aside — remaining on the path of God's command |
| `6076-003` | ? | 7 | 1 | — | Term names the inner-responsive act of turning aside toward God or his revelation — directing attention and presence tow |
| `6077-001` | ? | 5 | 1 | — | Term names the departure or withdrawal of God's Spirit, presence, face, or steadfast love — the inner-relational consequ |
| `6077-003` | ? | 3 | 1 | — | Term names the departure of inner strength or spiritual endowment — the loss of an inward empowerment that sustained the |
| `6090-001` | ? | 1 | 1 | — | Term names rebelliousness as an entrenched inner character trait — a deeply embedded disposition of perversity attribute |
| `6208-001` | ? | 16 | 1 | — | Term names inner restraint — the holding back or releasing of inner content (prophetic compulsion, honest speech, moral  |
| `6208-002` | ? | 18 | 1 | — | Term names divine restraint of human capacity — shutting the womb, stopping strength, withholding rain — as divine sover |
| `819-001` | ? | 4 | 1 | — | Term names disobedience as the inner condition and defining orientation of the person before God — the state of being ch |
| `819-002` | ? | 2 | 1 | — | Term names disobedience as the inner failure that excludes from rest — the disposition of the heart that prevents entry  |
| `820-001` | ? | 3 | 1 | — | Term names disobedience as the defining inner act with moral and covenantal consequence — the primal refusal that consti |
| `901-001` | ? | 3 | 2 | — | Term names the state of hardening — the condition of the inner being rendered insensible to God, expressed as hardness o |

### M31 (25 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1198-001` | ? | 4 | 1 | — | Term names corporate covenantal unbelief — the inner state of a people that issues in covenantal-historical limitation o |
| `1198-002` | ? | 1 | 1 | — | Term names individual self-acknowledged unbelief co-existing with faith — the inner state confessed in personal struggle |
| `1198-003` | ? | 1 | 1 | — | Term names disciples' post-resurrection unbelief under apostolic-formation rebuke — the inner state of the appointed wit |
| `1198-004` | ? | 1 | 1 | — | Term names hypothetical covenantal infidelity as rhetorical foil — Israelite faithlessness invoked argumentatively again |
| `1198-005` | ? | 1 | 1 | — | Term names the inner state in negated role — the unbelief that did not arise to govern Abraham's response, against which |
| `1198-006` | ? | 1 | 1 | — | Term names continuing-but-not-permanent corporate unbelief — the inner state as a condition that may be discontinued, ho |
| `1198-007` | ? | 1 | 1 | — | Term names autobiographical pre-conversion unbelief — the prior inner state into which mercy was given, ground for the a |
| `1198-008` | ? | 1 | 1 | — | Term names the heart's susceptibility to an unbelieving condition leading to apostasy — directive warning to believers a |
| `1258-001` | ? | 1 | 1 | — | Term names religion or worship as an organised inner orientation toward a divine object — designating the person's devot |
| `262-001` | ? | 3 | 2 | — | Term names the devout person characterised by inner godly reverence — the inner moral quality of reverential fear expres |
| `2774-001` | ? | 29 | 2 | — | Term names what is lawful or permitted — engaging the inner being through the conscience's reckoning with divine or huma |
| `3768-001` | ? | 3 | 2 | — | Term names faithfulness as a stable inner disposition of reliability and integrity — whether as a divine attribute, a Sp |
| `3769-001` | ? | 9 | 2 | — | Term names the inner condition of unbelief — the inner non-reception of divine truth, linked to spiritual blindness, def |
| `3769-002` | ? | 12 | 2 | — | Term names the unbelieving as a moral category of persons — those whose inner orientation is faithlessness, contrasted w |
| `3771-001` | ? | 6 | 2 | — | Term names the act of inner disbelief — the refusal or failure to receive testimony or truth as credible; the inner non- |
| `3771-002` | ? | 2 | 1 | — | Term names inner faithlessness — the failure of inner reliability and covenant fidelity, contrasted with divine faithful |
| `4835-001` | ? | 10 | 2 | — | Term designates the person whose identity and standing is constituted by divine calling — being called as the defining c |
| `718-001` | ? | 11 | 2 | — | Term names the divine calling as a constitutive act that establishes the person's identity, vocation, and orientation be |
| `860-001` | ? | 87 | 2 | — | Term names faith as the inner act and disposition of trust — the inner orientation of reliance on God or Christ that rec |
| `860-002` | ? | 9 | 2 | — | Term names faith as a corporate body of belief and the community that holds it — the faith as the content of Christian c |
| `864-001` | ? | 4 | 2 | — | Term names the inner condition of diminished faith — the insufficient inner trust that gives rise to fear, doubt, and an |
| `865-001` | ? | 2 | 1 | — | Term names the inner condition of insufficient faith — a diminished or weak inner trust that falls short of what is need |
| `866-001` | ? | 105 | 2 | — | Term names the inner act of believing and trusting — the fundamental inner disposition of reception and reliance on God, |
| `866-002` | ? | 3 | 2 | — | Term names believing that reveals the limits or conditions of faith — sign-dependent believing, intellectual assent with |
| `866-003` | ? | 6 | 2 | — | Term names believers as the community constituted by the inner act of having believed — defined by belief as the constit |

### M33 (67 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1044-001` | ? | 1 | 1 | — | Term names the inner-being quality of wisdom-restraint — the capacity to soothe and hold back what the spirit would othe |
| `1291-001` | ? | 2 | 2 | — | Term names comfort as the inner state grounded in faithfulness to God's word and promise — the comfort that comes not fr |
| `1293-001` | ? | 1 | 1 | — | Term names the tender comfort of love — the personal warmth that soothes the inner person within the community of Christ |
| `1294-001` | ? | 1 | 1 | — | Term names the comfort given by faithful companions — the inner sustenance received through loyal fellowship in ministry |
| `1651-001` | ? | 1 | 1 | — | Term names the peacemaker as one whose inner orientation produces peace — a beatitude character quality |
| `2508-001` | ? | 19 | 5 | — | Term names shalom as the inner condition of the whole person — peace, welfare, and wholeness experienced inwardly; the o |
| `2508-002` | ? | 24 | 3 | — | Term names shalom as the covenantal peace between God and his people — given by God, grounded in covenant, expressed in  |
| `2508-003` | ? | 25 | 2 | — | Term names shalom as the inner orientation of the person toward peace — as character, disposition, and telos; both its a |
| `2508-004` | ? | 15 | 3 | — | Term names shalom as the peace that belongs to and proceeds from the messianic king — eschatological, comprehensive, emb |
| `2509-001` | ? | 13 | 2 | — | Term names shalom as the comprehensive inner condition of welfare and well-being — the wholeness of the person as divine |
| `2509-002` | ? | 4 | 1 | — | Term names shalom as the falsely promised or self-deceived condition of welfare — the inner state wrongly claimed when j |
| `2510-001` | ? | 5 | 1 | — | Term names shalom as the inner relational bond of close friendship — the bond of trust, loyalty, and mutual allegiance w |
| `2511-001` | ? | 1 | 1 | — | Term names shalom as the substantive peace-blessing invoked in greeting — the comprehensive peace of the whole person ca |
| `2558-001` | ? | 4 | 1 | — | Term names a disposition of quiet attentiveness or ordered restraint — the inner quality of settled quiet that enables l |
| `2559-001` | ? | 2 | 1 | — | Term names a gentle, quiet spirit as an inner-being quality — the disposition of settled peace within, precious in God's |
| `2560-001` | ? | 2 | 1 | — | Term names profound silence as an inner-being atmosphere — the hush of awe before a significant moment |
| `2583-001` | ? | 1 | 1 | — | Term names quietness as a condition of divinely bestowed peace — the character of a reign and its people under God's gif |
| `2585-001` | ? | 4 | 1 | — | Term names the soul's own rest — the inner condition of peace, security, and settled orientation toward God |
| `2585-002` | ? | 7 | 2 | — | Term names the covenantal rest given by God to his people — a condition of settled security, peace, and inheritance prom |
| `2585-003` | ? | 3 | 1 | — | Term names an eschatological or divine resting-place — where God dwells, and the orientation of his own will and delight |
| `2586-001` | ? | 3 | 2 | — | Term names a state of existential restlessness — the absence of resting-place as the condition of the whole person, part |
| `2587-001` | ? | 5 | 2 | — | Term names quietness as an inner-being condition of peace, receptivity to wisdom, and strength before God |
| `2593-001` | ? | 1 | 1 | — | Term names rest as the condition of the soul that walks in the right way — an inner-being orientation of peace attained  |
| `2594-001` | ? | 1 | 1 | — | Term names divine repose offered to the weary — the condition of inner rest available through God's provision |
| `2595-001` | ? | 1 | 1 | — | Term names the restful inner posture of the peaceable person — the quality of quietness as a character orientation, in c |
| `2596-001` | ? | 15 | 2 | — | Term names the inner act of becoming or keeping silent — the stilling of the self before God, in grief, in reverence, or |
| `2597-001` | ? | 9 | 2 | — | Term names the inner state of stillness or its absence — being motionless before God in awe, patient waiting, or unceasi |
| `2603-001` | ? | 3 | 1 | — | Term names the stillness from which the divine voice is heard — the profound inner and outer silence that attends divine |
| `2879-001` | ? | 1 | 1 | — | Term names the increasing scope of God's government and peace — the inner being engaged through messianic hope |
| `33-001` | ? | 9 | 2 | — | Term names longsuffering/patience as an inner character quality and fruit of the Spirit — the sustained inner dispositio |
| `33-002` | ? | 5 | 2 | — | Term names divine longsuffering — God's patient endurance of human sin, restraining judgment to extend the opportunity f |
| `352-001` | ? | 4 | 1 | — | Inner condition of ease and security — freedom from dread as positive state, often fruit of trust or divine promise |
| `352-002` | ? | 1 | 1 | — | Complacent ease — inner condition of undisturbed settledness that has become spiritual stagnation |
| `354-001` | ? | 1 | 1 | — | Inner condition of relief from anxiety — reduction of grief-laden concern through wellbeing of a beloved person |
| `406-001` | ? | 1 | 1 | — | Term names shalom as the divine identity commemorated in the altar name YHWH-Shalom — God identified as peace in the alt |
| `408-001` | ? | 6 | 2 | — | Term names the posture of inner restraint — holding silence in response to emotional provocation, injustice, or the desi |
| `408-002` | ? | 9 | 2 | — | Term names the receptive posture of silence — an inner orientation of attentive submission, readiness to hear or receive |
| `408-003` | ? | 2 | 1 | — | Term names the posture of wisdom — silence as an expression of inner discernment, understanding, or moral restraint |
| `408-004` | ? | 6 | 2 | — | Term names the inner condition when an appeal is made for God not to be silent — the psalmist's existential need for div |
| `408-005` | ? | 4 | 2 | — | Term names God's own posture of silence or its breaking — divine inner restraint, patience, or deliberate withholding |
| `408-006` | ? | 3 | 1 | — | Term applied to ethical-existential confrontation — the moral weight of remaining silent at a critical moment of injusti |
| `418-001` | ? | 5 | 2 | — | Term names the inner condition of quietness, rest, and trust as the spiritual posture of the person before God — the con |
| `418-002` | ? | 4 | 2 | — | Term names the inner restlessness of the wicked or troubled person — the inability to be quiet as an expression of inner |
| `418-003` | ? | 5 | 2 | — | Term names the quiet of God — God's own inner posture of watchful stillness, or the breaking of it in response to his pe |
| `418-004` | ? | 9 | 1 | — | Term names the promised rest of God's people — the condition of quiet and ease as covenant blessing, contrasted with res |
| `419-001` | ? | 4 | 1 | — | Term names the Spirit resting upon a person — divine inner-being impartation resulting in transformed capacities |
| `419-002` | ? | 26 | 2 | — | Term names God's gift of rest to his people — the settled condition of security, peace, and wholeness bestowed as covena |
| `419-003` | ? | 10 | 2 | — | Term names the inner restlessness or rest of the human person — the condition of the inner life in the absence or presen |
| `419-004` | ? | 6 | 2 | — | Term names wisdom, anger, or another inner quality resting in a place within the person |
| `419-005` | ? | 9 | 2 | — | Term names God's own inner rest, restraint, satisfaction, or calm — the inner orientation of God expressed through this  |
| `419-006` | ? | 3 | 2 | — | Term names the call or appeal not to be abandoned by God — the inner-being distress of one fearing divine withdrawal |
| `4192-001` | ? | 6 | 1 | — | Term names the commanded inner disposition of sober alertness — the mind clear and watchful, not given to spiritual or m |
| `420-001` | ? | 3 | 2 | — | Term names the rest or respite sought or denied — the inner-being condition of peace in exile, distress, or covenant pro |
| `421-001` | ? | 8 | 2 | — | Term names the commanded inner silence — the hush of reverence, awe, or holy restraint before God or in the face of his  |
| `422-001` | ? | 4 | 1 | — | Term names the inner disposition and active practice of relational peace — the will directed toward harmony with others |
| `423-001` | ? | 11 | 2 | — | Term names the inner state and act of silence — holding the voice still in the presence of power, shame, or reverence |
| `424-001` | ? | 5 | 2 | — | Term names the inner disposition of settling into quiet — the ceasing of noise, argument, or resistance, whether in reve |
| `426-001` | ? | 14 | 2 | — | Term names the inner-being peace given by God through Christ — the reconciled state before God and the interior experien |
| `426-002` | ? | 35 | 1 | — | Term names peace as apostolic blessing and greeting — the invocation of divine shalom upon persons in the community of C |
| `426-003` | ? | 35 | 2 | — | Term names peace as the eschatological and relational fruit of the kingdom — achieved by Christ, to be pursued in commun |
| `427-001` | ? | 2 | 1 | — | Term names peaceableness as an inner character quality — the disposition of the trained person or the wisdom from above, |
| `428-001` | ? | 1 | 1 | — | Term names peaceful quietude as an inner-being quality of life — the disposition of undisturbed, godly calm in social co |
| `429-001` | ? | 5 | 1 | — | Term names relief from pressure or affliction — the inner-being experience of rest when burdens are lifted, or its absen |
| `5118-001` | ? | 1 | 1 | — | Term names the dwelling of God's presence as an inner-oriented rest-place, where his people find salvation and joy |
| `5118-002` | ? | 1 | 1 | — | Term names relief as a condition of the inner life freed from threat |
| `608-001` | ? | 2 | 1 | — | Term names inner corporate unity — being same-souled, sharing one inner orientation, love, and mind in the community |
| `733-001` | ? | 3 | 2 | — | Term names the compassionate inner movement of comfort — the tender, stirring compassion that arises from within the per |

### M34 (40 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1-001` | ? | 1 | 1 | ✓ | Term names the anguish of supreme inner crisis driving intensified prayer and somatic manifestation |
| `1268-001` | ? | 1 | 1 | — | Term names physical haste expressing negative-moral inner urgency — the haste of compliance with a murderous demand |
| `1268-002` | ? | 1 | 1 | — | Term names physical haste expressing positive-obedient inner eagerness — the haste of joyful response after divine revel |
| `1268-003` | ? | 1 | 1 | — | Term names the author's inner-eagerness as urgency-of-writing-desire — the disposition disclosed in autobiographical add |
| `1268-004` | ? | 2 | 1 | — | Term names inner zeal as the right Christian disposition for body-life — fervency of spirit appropriate to gift-exercise |
| `1268-005` | ? | 1 | 1 | — | Term names earnestness as the inner-being fruit produced by godly grief — the disposition that arises in true repentance |
| `1268-006` | ? | 1 | 1 | — | Term names earnestness revealed under apostolic disciplinary writing — the relational disposition disclosed in the sight |
| `1268-007` | ? | 1 | 1 | — | Term names earnestness as one virtue among others in which a church excels — the inner disposition listed alongside fait |
| `1268-008` | ? | 1 | 1 | — | Term names earnestness as the evidence of genuine love — the inner disposition that proves love by comparison with other |
| `1268-009` | ? | 1 | 1 | — | Term names earnest care as God-given inner disposition — the heart-implanted same-care of one minister mirroring another |
| `1268-010` | ? | 1 | 1 | — | Term names earnestness oriented toward eschatological assurance — the inner disposition pursuing full assurance of hope  |
| `1268-011` | ? | 1 | 1 | — | Term names inner effort directed at moral-formative supplementation — making every effort to supplement faith with virtu |
| `2076-001` | ? | 2 | 1 | — | The willing spirit — inner eagerness toward God in tension with fleshly weakness |
| `2076-002` | ? | 1 | 1 | — | Eagerness as the inner motivation for mission |
| `2909-001` | ? | 2 | 1 | — | Term names striving with God as the defining inner act — tenacious, costly engagement with the divine that transforms id |
| `3078-001` | ? | 2 | 1 | — | Term names the noble person as a moral character type — inner dignity and reliability contrasted with the fool and the s |
| `32-001` | ? | 7 | 2 | ✓ | Term names patient forbearance as an inner disposition — the willingness to wait, endure, or bear with others without gi |
| `32-002` | ? | 2 | 1 | ✓ | Term names divine patience — God's inner disposition of forbearance toward human disobedience |
| `4444-001` | ? | 1 | 1 | — | Prophetic boldness — inner audacity to declare what runs counter to expectation or convention, grounded in divine revela |
| `4467-001` | ? | 1 | 1 | — | Term names inner earnestness as voluntary self-motivation — the disposition that goes beyond what was asked, expressed i |
| `4467-002` | ? | 1 | 1 | — | Term names inner earnestness as a tested and intensifying character quality — diligence proven across many matters and n |
| `4583-001` | ? | 7 | 1 | — | Term names directed inner volitional striving toward God and spiritual goals — the will engaged in sustained effort thro |
| `4585-001` | ? | 1 | 1 | — | Term names inner volitional resistance directed against sin — the striving of the will against a named inner adversary |
| `4588-001` | ? | 1 | 1 | — | Term names the inner volitional striving alongside another in prayer — shared struggle as intercession |
| `4927-001` | ? | 3 | 1 | — | Perseverance as inner-being posture — standing firm despite pressure, grounded in resolve or knowledge of God |
| `5066-001` | ? | 4 | 1 | — | Term names the inner quality of gravity and honourableness — the settled inner character that commands respect; moral di |
| `5638-001` | ? | 11 | 2 | — | Term characterizes the person as inwardly blameless and morally whole — the quality of inner character that defines one  |
| `5638-002` | ? | 2 | 2 | — | Term characterizes the beloved as wholly complete and perfect — the wholeness that evokes delight and singular devotion |
| `61-001` | ? | 14 | 2 | ✓ | Term names steadfast endurance under trial — the inner disposition that holds firm under pressure, suffering, or persecu |
| `62-001` | ? | 31 | 2 | — | Term names perseverance as the sustained inner disposition of steadfast endurance under trial — producing character, hop |
| `6465-001` | ? | 7 | 1 | — | Term names the act of struggling or striving in conflict — physical and social contention that originates in inner hosti |
| `6518-001` | ? | 1 | 1 | — | Divine preservation from spiritual falling — the blameless inner condition in which one stands before God's glory |
| `713-001` | ? | 10 | 1 | ✓ | Boldness as inner posture of access to God — confident approach to God's presence made possible through Christ, expresse |
| `713-002` | ? | 11 | 1 | — | Boldness as inner quality of apostolic proclamation — confident unrestrained declaration of the gospel grounded in encou |
| `713-003` | ? | 1 | 1 | — | Boldness as inner quality of relational confidence — freedom to speak openly and without self-protective restraint in si |
| `762-001` | ? | 4 | 1 | — | Bold inner action in service of mission or truth |
| `762-002` | ? | 3 | 1 | — | Inner discipline of restraint — not presuming beyond what is appropriate |
| `831-001` | ? | 12 | 1 | — | Lament over God's apparent perpetual absence — inner anguish of "how long?" |
| `831-002` | ? | 4 | 1 | — | Perpetual inner suffering and unceasing pain — anguish that will not relent |
| `831-003` | ? | 10 | 1 | — | Everlasting joy, hope and divine faithfulness — inner orientation toward what endures |

### M35 (25 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1104-001` | ? | 2 | 1 | — | Term names the inner decision to attempt an action — whether motivated by hostile intent or by presumptuous religious in |
| `1115-001` | ? | 2 | 1 | — | Term names the act of causing another to stumble morally — the inner-relational damage done when one person's conduct tr |
| `1118-001` | ? | 7 | 1 | — | Term names a stumbling block — something that triggers inner-moral failure, hinders spiritual integrity, or constitutes  |
| `1150-001` | ? | 9 | 2 | — | Temptation as a condition of inner exposure — the state of being vulnerable to the solicitation of desire, evil, or the  |
| `1194-001` | ? | 35 | 3 | — | Inner persuasion, trust, and conviction — the state of being inwardly convinced, of trusting or relying upon someone or  |
| `1348-001` | ? | 1 | 1 | — | Term names the sifting of the inner being by a hostile spiritual agent — the adversarial trial to which faith is subject |
| `4584-001` | ? | 6 | 2 | — | Term names the sustained inner volitional effort of the faith-life — contending, running, fighting as the core experienc |
| `4683-001` | ? | 1 | 1 | — | Term names unceasing inner-experiential torment — the absolute absence of rest as the defining quality of final sufferin |
| `4683-002` | ? | 3 | 1 | — | Term names torment as the object of inner dread — suffering as counterpart to pride and as the judgement that answers se |
| `4841-001` | ? | 11 | 2 | — | Term names the inner act of moral and spiritual discernment — the mind's tested capacity to distinguish what is genuinel |
| `4841-002` | ? | 8 | 2 | — | Term names the process by which character is tested and proven — trial that discloses the genuine quality of the inner p |
| `4842-001` | ? | 7 | 2 | — | Term designates the person whose inner character has been proved genuine through testing — approved by God and recognisa |
| `4843-001` | ? | 2 | 1 | — | Term names the testing-process itself as the instrument by which inner faith is proved genuine and produces inner transf |
| `6504-001` | ? | 11 | 2 | — | Testing/trials as the inner-being context of faith formation — the experience of trial that pressures faith, endurance,  |
| `6505-001` | ? | 19 | 3 | — | Testing as expression of inner disposition — the act of testing Jesus or God expressing hostility, unbelief, or the hard |
| `6506-001` | ? | 12 | 2 | — | Temptation as assault on the inner being — the devil's solicitation of desire, weakness, and the will, including Jesus's |
| `6507-001` | ? | 4 | 2 | — | Testing God — the inner disposition of demanding proof from God, testing the limit of divine faithfulness; including the |
| `6510-001` | ? | 2 | 1 | — | Attempting as expression of inner desire or hostility — acts of trying that originate in changed inner orientation or in |
| `6514-001` | ? | 4 | 2 | — | Spiritual/moral stumbling — the inner act of falling in faith, disobedience, or moral failing; including stumbling becau |
| `6515-001` | ? | 6 | 2 | — | The stumbling block as moral-faith obstacle — something that causes another to stumble in faith, conscience, or moral st |
| `6516-001` | ? | 4 | 2 | — | Moral stumbling and spiritual failing — the inner act of falling in the law, in speech, or in steadfastness of calling |
| `6517-001` | ? | 2 | 1 | — | Moral blamelessness and clear conscience — the inner state of moral integrity described as the absence of stumbling befo |
| `728-001` | ? | 6 | 2 | — | Term names the proven character that emerges from testing — the demonstrable inner quality of the person revealed throug |
| `7500-001` | ? | 11 | 1 | — | Patient endurance as inner character — anechō as expression of the inner disposition of forbearance toward others and un |
| `7500-002` | ? | 2 | 1 | — | Inner disposition toward received teaching — anechō as the will's posture of acceptance or rejection of truth |

### M36 (28 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1252-001` | ? | 25 | 2 | — | Term names service of God as the directed inner orientation of the person — the wholehearted devotion that God requires  |
| `1252-002` | ? | 12 | 1 | — | Term names service of idols and false gods as the inner-being act of devotion misdirected — Israel's persistent defectio |
| `4804-001` | ? | 20 | 1 | — | Slave of Christ as inner-being identity — defining self-understanding of the apostle and believer as one wholly given ov |
| `4804-002` | ? | 6 | 1 | — | Slavery to sin and bondage as former or present inner-being condition apart from God |
| `4804-003` | ? | 11 | 1 | — | Faithful servanthood as inner-being quality — stewardship, trustworthiness, and humility before the master as inner disp |
| `4804-004` | ? | 7 | 1 | — | Social and eschatological levelling of slave and free — inner-being equality of all persons before God transcending soci |
| `4805-001` | ? | 8 | 1 | — | Inner-being impossibility of divided ultimate loyalty — heart's singular orientation toward one master; service to God a |
| `4805-002` | ? | 3 | 1 | — | Slavery to disordered inner desires — state of the person bound in service to passions, pleasures, and appetite rather t |
| `4805-003` | ? | 7 | 1 | — | Willing service as inner-being expression of love, fervency, and Spirit-led freedom — what distinguishes God-directed se |
| `4807-001` | ? | 2 | 1 | — | Slavery to righteousness and God — inner-being reorientation from bondage to sin to willing service of God, producing ho |
| `4807-002` | ? | 3 | 1 | — | Inner bondage to disordered desires — state of the inner person enslaved to passions, pleasures, or substances |
| `4807-003` | ? | 2 | 1 | — | Voluntary servanthood for others — inner act of self-subordination in service of another's flourishing |
| `4808-001` | ? | 3 | 1 | — | Inner posture of the Lord's servant — willing humble availability to God's word and purpose as defining inner-being self |
| `4809-001` | ? | 2 | 1 | — | Act of bringing others into bondage — external imposition of spiritual or relational enslavement that threatens the inne |
| `4810-001` | ? | 1 | 1 | — | Inner act of bringing the body under disciplined governance — inner will asserting mastery over bodily impulses in servi |
| `5162-001` | ? | 1 | 1 | — | Exhausting toil as inner-bearing weariness |
| `6715-001` | ? | 122 | 2 | — | Term names the service of God as the central obligation of Israel's life — the commanded inner orientation of devoted se |
| `6715-002` | ? | 20 | 1 | — | Term names Levitical priestly service as an enacted inner-being vocation — ministry in the tabernacle/temple as a callin |
| `6716-001` | ? | 4 | 1 | — | Term names diligent labour as an expression of inner wisdom — the wise person's orientation toward productive work contr |
| `6717-001` | ? | 2 | 1 | — | Term names the burden of service — worship obligations that weigh the worshiper, or human sin that weighs God, revealing |
| `6719-001` | ? | 19 | 2 | — | Term names temple/tabernacle ministry as a vocation expressing the community's inner orientation toward God — ordered se |
| `6720-001` | ? | 3 | 1 | — | Term names work as a human vocation and moral measure — the ordinary labour of life, and the fruit of righteous inner or |
| `6721-001` | ? | 5 | 1 | — | Term names purposeful action — especially God's acts of wonder and Daniel's act of prayer — naming inner devotion throug |
| `6722-001` | ? | 12 | 2 | — | Term names service as an inner-being experience — both oppressive bondage producing inward groaning, and devoted service |
| `6723-001` | ? | 3 | 1 | — | Term names slavery as an inner-being condition of bondage — experienced as degradation but also as the context for divin |
| `7066-001` | ? | 3 | 2 | — | Divided or undivided allegiance — oiketēs as the figure of the household slave whose inner-being orientation is either d |
| `715-001` | ? | 4 | 1 | — | Spiritual slavery as inner-being condition — bondage to fear, law, or death that characterises the person apart from Chr |
| `715-002` | ? | 2 | 1 | — | Eschatological liberation from bondage — creation and persons set free from corruption into the freedom of God's glory |

### M37 (27 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1331-001` | ? | 4 | 1 | — | Term names the inner-being goal of winning others — the motivating purpose behind Paul's self-subordination; love for ot |
| `1671-001` | ? | 7 | 2 | — | Term names Christ as firstborn — carrying theological weight about his identity, primacy, and the inner-being significan |
| `1842-001` | ? | 4 | 2 | — | Term names the divine act of foreknowing as the ground of election and identity — the prior knowing of persons by God th |
| `1847-001` | ? | 2 | 1 | — | Term names divine foreknowledge as the sovereign inner ground of God's redemptive purpose — the prior knowing from which |
| `3083-001` | ? | 3 | 1 | — | Choosing as inner act of will — divine election and human deliberate choice |
| `3085-001` | ? | 1 | 1 | — | Divine election as inner-being delight — God's chosen servant named with his soul's pleasure |
| `3087-001` | ? | 1 | 1 | — | The heart's inner decision as the governing act of will — giving from inner resolve, not compulsion |
| `3088-001` | ? | 1 | 1 | — | Divine pre-selection of witnesses — God's choice of those who encounter the risen Christ |
| `479-001` | ? | 48 | 1 | — | Term names God's elective choosing of a person or people — the expression of divine inner will in covenant election and  |
| `479-002` | ? | 43 | 1 | — | Term names God's choosing of a place — divine designation of a location as the dwelling of his name and the site of cove |
| `479-003` | ? | 32 | 1 | — | Term names the human moral or volitional choosing — the inner will of the person directed toward good or evil, wisdom or |
| `479-004` | ? | 20 | 1 | — | Term names practical human choosing — selecting persons or options in leadership, strategy, or administration; the act o |
| `4822-001` | ? | 12 | 2 | — | Term describes naming as an act that expresses or constitutes inner identity, relational standing, and covenantal belong |
| `4822-002` | ? | 12 | 2 | — | Term captures naming as an expression of the namer's inner experience — grief, longing, gratitude, or wrestling — given  |
| `4823-001` | ? | 35 | 2 | — | Term names the intense cry that originates in the inner person — the compelled, forceful outward expression of urgency,  |
| `4823-002` | ? | 45 | 2 | — | Term names the cry of proclamation — the inner person or God declaring what truth, character, word, or judgment demands  |
| `4825-001` | ? | 4 | 2 | — | Term describes the act of going out to encounter God, framing the inner preparation, orientation, and accountability req |
| `717-001` | ? | 26 | 2 | — | Term describes calling upon the name of God — the inner orientation of prayer, worship, and dependence expressed in invo |
| `717-002` | ? | 13 | 2 | — | Term describes God's sovereign call to persons — the divine act that constitutes identity, relationship, and vocation fo |
| `717-003` | ? | 9 | 1 | — | Term describes the cry of the inner person directed to God in distress or longing — the soul calling out from the depths |
| `720-001` | ? | 5 | 2 | — | Term describes the divine act of calling persons to specific vocation, service, and relationship, engaging the inner ori |
| `722-001` | ? | 29 | 2 | — | Term describes God's sovereign call that constitutes the person's identity, vocation, and relational standing before him |
| `722-002` | ? | 13 | 2 | — | Term describes identity-conferral through naming, which constitutes or reveals the inner nature, vocation, or standing o |
| `722-003` | ? | 4 | 1 | — | Term describes the call to repentance or discipleship that engages the will and inner orientation of the person |
| `726-001` | ? | 5 | 1 | — | Term names the soul's orientation of faith expressed in appealing to and invoking God or Christ |
| `726-002` | ? | 1 | 1 | — | Term describes the act of calling God as witness, engaging inner moral accountability before God |
| `938-001` | ? | 5 | 2 | — | Term names the act of intercession — the inner act of pleading before God on behalf of another, or the divine advocacy u |

### M38 (20 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1306-001` | ? | 22 | 2 | — | Term names salvation as the object of inner longing, hope, trust, and anticipation — and as the divine act that transfor |
| `3166-001` | ? | 2 | 1 | — | Term names the propitious disposition of God — the mercy that forgives iniquity and remembers sin no more under the new  |
| `3173-001` | ? | 60 | 2 | — | Term names the priestly/ritual act by which human guilt is covered before God and forgiveness granted |
| `3173-002` | ? | 12 | 2 | — | Term names God's direct act of forgiving and covering iniquity |
| `3173-003` | ? | 9 | 2 | — | Term names interpersonal or communal appeasement — covering relational offence or bloodguilt |
| `3176-001` | ? | 2 | 2 | — | Term names the act of propitiation — the sinner's inner cry for God to turn his face in mercy, and Christ's atoning act  |
| `3177-001` | ? | 2 | 2 | — | Term names the propitiation — Christ as the atoning covering for sin that restores the inner relationship between God an |
| `4986-001` | ? | 57 | 1 | — | Salvation of the inner person — saved by grace through faith |
| `4986-002` | ? | 16 | 1 | — | Healing through faith — the inner instrument of salvation in physical need |
| `4986-003` | ? | 21 | 1 | — | Cry for rescue — inner-being posture of dependent appeal |
| `4988-001` | ? | 7 | 1 | — | The Savior as the object of inner-being trust, joy, and hope |
| `4988-002` | ? | 16 | 1 | — | The Savior as Jesus — his identity and the inner-being transformation he brings |
| `4989-001` | ? | 5 | 1 | — | Salvation as God's inner-being transformative gift seen and received |
| `5280-001` | ? | 12 | 1 | — | The remembered redemption — gratitude, obligation and trust grounded in God's ransoming act |
| `5280-002` | ? | 20 | 1 | — | The appeal for redemption — inner longing and cry for God to ransom the soul |
| `641-001` | ? | 21 | 2 | — | Sōteria as received inner-being condition of the saved person |
| `641-002` | ? | 21 | 2 | — | Sōteria as eschatological and proclaimed reality of salvation |
| `6838-001` | ? | 11 | 2 | — | Term names the divine free gift received by the person — grace, righteousness, calling — that transforms the inner being |
| `6846-001` | ? | 2 | 1 | — | Term names the divine perfect gift — every good gift from above; gift bringing justification where condemnation was due |
| `991-001` | ? | 2 | 2 | — | Term names the mercy seat — the place of propitiation fulfilled in Christ as the living propitiation received by faith |

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

### M41 (60 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1100-001` | ? | 51 | 1 | — | Term names the seeking of God as the primary inner orientation of the person — the whole-hearted turning toward God in w |
| `1100-002` | ? | 47 | 2 | — | Term names the act of seeking divine guidance through inquiry of the Lord — expressing inner dependence and orientation  |
| `1100-003` | ? | 23 | 1 | — | Term names seeking evil or worthless things as an inner orientation away from God — pursuing harm, seeking the favour of |
| `1100-004` | ? | 24 | 1 | — | Term names God seeking his people — the divine inner-relational initiative of pursuing, caring for, and requiring accoun |
| `1103-001` | ? | 4 | 1 | — | Term names earnest inner-directed seeking — the soul and spirit yearning and seeking God, particularly in distress or ne |
| `1180-001` | ? | 181 | 2 | — | Term names the commanded human act of remembering — calling to mind God's acts, his covenant, one's own ways, and those  |
| `1180-002` | ? | 24 | 2 | — | Term names divine remembering — God holding persons, his covenant, and his people in active attentiveness, with grace or |
| `1203-001` | ? | 30 | 1 | — | God hears — attentive divine listening to prayer, affliction, and cry |
| `1203-002` | ? | 26 | 1 | — | Hearing as responsive obedience or wilful refusal — inner act of compliance or hardness toward God's word |
| `1203-003` | ? | 77 | 1 | — | Hearing as receptive understanding — attentive inner engagement with God's word, wisdom, or prophetic speech |
| `1203-004` | ? | 30 | 1 | — | The inner responsiveness produced by hearing — the full range of inner-being movement that hearing triggers: fear, grief |
| `3370-001` | ? | 6 | 1 | — | Term names the inner act of forgetting or neglecting — the failure to retain in active consciousness what matters morall |
| `4291-001` | ? | 3 | 1 | — | Term names the act of reminding as a pastoral instrument — stirring up the inner life by bringing truth back to active c |
| `4292-001` | ? | 7 | 1 | — | Term names the prompting of inner remembrance — bringing truth or prior words back into active inner awareness through t |
| `4411-001` | ? | 18 | 1 | — | Term names the commanded inner act of remembrance — calling to mind persons, words, or events as the basis for present f |
| `4411-002` | ? | 3 | 1 | — | Term names the inner orientation of remembrance as motivating force — thinking of, being concerned with, or holding in m |
| `4412-001` | ? | 1 | 1 | — | Term names the capacity for recall — the ability to bring to active consciousness what has been received |
| `4413-001` | ? | 15 | 1 | — | Term names human remembrance — the inner act of bringing to mind what was said, experienced, or promised |
| `4413-002` | ? | 4 | 1 | — | Term names divine remembrance — God holding a person or their deeds in active attentiveness, with grace or judgment as t |
| `4413-003` | ? | 2 | 1 | — | Term names God's chosen non-remembrance — the new covenant promise to remember sins no more |
| `4416-001` | ? | 6 | 1 | — | Term names affectionate remembrance of persons — holding them in active prayerful awareness before God |
| `4417-001` | ? | 2 | 1 | — | Term names the inner act of mindful attentiveness — holding another in active awareness with moral or relational consequ |
| `4424-001` | ? | 6 | 1 | — | Term names the inner act of bringing prior knowledge or experience back into active awareness — voluntary recall or prom |
| `4426-001` | ? | 3 | 1 | — | Term names the eucharistic act of remembrance — inner and communal re-presentation of Christ's self-giving before God an |
| `4426-002` | ? | 1 | 1 | — | Term names the annual reminder of unresolved sin — the old covenant's inability to finally cleanse the conscience |
| `486-001` | ? | 39 | 1 | — | Term names seeking God — the inner orientation of the person directed toward God in prayer, inquiry, worship, repentance |
| `486-002` | ? | 59 | 1 | — | Term names the hostile will seeking to harm or destroy — the inner intention of enmity expressed as purposive pursuit of |
| `486-003` | ? | 18 | 1 | — | Term names seeking wisdom, understanding, or moral good — the inner orientation of the mind toward truth, knowledge, or  |
| `486-004` | ? | 10 | 1 | — | Term names seeking the beloved — the inner longing of the person for another in love, relational desire, or longing for  |
| `486-005` | ? | 27 | 1 | — | Term names petitioning or seeking a person in authority — the inner orientation of dependence, request, or enquiry direc |
| `486-006` | ? | 19 | 1 | — | Term names God seeking — the divine inner purposive search for righteousness, the lost, or a faithful person; and divine |
| `511-001` | ? | 12 | 1 | — | Term names the inner orientation of the will and desire directed toward God, his kingdom, or righteousness — the command |
| `511-002` | ? | 12 | 1 | — | Term exposes the inward misdirection of desire toward self-interest, self-glory, or human approval in contrast to God-or |
| `511-003` | ? | 13 | 1 | — | Term names the inner movement of the person toward God himself — in longing, worship, encounter, or relational desire |
| `511-004` | ? | 4 | 1 | — | Term names the inner demand or desire for external confirmation — seeking a sign, proof, or wisdom as a substitute for t |
| `511-005` | ? | 15 | 1 | — | Term names the inward intention of hostility, betrayal, or lethal opposition expressed through purposeful directed actio |
| `511-006` | ? | 2 | 1 | — | Term names the paradox of inner self-preservation instinct and its inversion — the desire to preserve life as the condit |
| `7496-001` | ? | 22 | 1 | — | Inner attentiveness called to God's word — a.zan as the summons to the receptive inner posture that constitutes covenant |
| `7496-002` | ? | 2 | 1 | — | Inner hardness refusing God's ear — a.zan as the inner act of attentiveness withheld, expressing resistance to God |
| `7496-003` | ? | 1 | 1 | — | Inner attentiveness oriented toward evil — a.zan as the disposition of the character that gives ear to wickedness |
| `7496-004` | ? | 13 | 1 | — | Prayer as inner cry seeking God's ear — a.zan as the act of the soul urgently addressing God for mercy and deliverance |
| `7498-001` | ? | 10 | 1 | — | Faith reception — akoē as the channel through which faith, understanding and inner response to the word arrive |
| `7503-001` | ? | 84 | 1 | — | Covenantal obedience — sha.ma as the inner act of the will submitting to God's voice, constituting the fundamental coven |
| `7503-002` | ? | 29 | 1 | — | Covenantal disobedience — sha.ma refused as the expression of the inner hardness of will that walks in its own counsel a |
| `7503-003` | ? | 6 | 1 | — | Obedience to human authority — sha.ma as the inner act of submission to parental and leadership voice, placing obedience |
| `7504-001` | ? | 21 | 1 | — | Proclamation arising from or producing inner response — sha.ma as the act of making heard what generates inner transform |
| `7505-001` | ? | 2 | 1 | — | The hearing heart as inner discernment — sha.ma as the faculty of understanding that discerns truth, meaning and moral d |
| `7506-001` | ? | 1 | 1 | — | Judicial hearing as inner discernment — sha.ma as the inner capacity to discern rightly between good and evil in governa |
| `7507-001` | ? | 1 | 1 | — | Welcoming reception as inner disposition — sha.ma as the act of receptive welcome that discloses the inner orientation o |
| `7508-001` | ? | 18 | 1 | — | The heard word producing inner response — she.mu.ah as the report or proclamation that generates belief, fear, courage,  |
| `7509-001` | ? | 12 | 1 | — | Hearing of God's fame producing inner response — she.ma as the report of God's character and acts that generates faith,  |
| `7512-001` | ? | 2 | 1 | — | Report producing inner anguish or recognition — sho.ma as the received word that collapses inner strength or generates i |
| `7514-001` | ? | 1 | 1 | — | Discernment beyond the ear — mish.ma as the faculty deliberately transcended in favour of inner discernment rooted in fe |
| `7521-001` | ? | 24 | 1 | — | Inner attentiveness to God's word — qa.shav as the deliberate inner posture of heeding that constitutes covenantal respo |
| `7521-002` | ? | 6 | 1 | — | Inner stubbornness refusing to attend — qa.shav as the inner act of deliberate non-attentiveness expressing hardness tow |
| `7521-003` | ? | 11 | 1 | — | Prayer urgently seeking God's attention — qa.shav as the inner cry addressed to God asking him to attend and respond |
| `7521-004` | ? | 2 | 1 | — | The attentive inner posture in wisdom teaching — qa.shav as the inner disposition of the learner giving careful heed |
| `7522-001` | ? | 1 | 1 | — | Diligent inner attentiveness — qe.shev as the quality of careful heed given to what is heard |
| `7523-001` | ? | 3 | 1 | — | Prayer invoking divine attentiveness — qash.shuv as the quality of attentiveness called for in God, expressing human inn |
| `7524-001` | ? | 2 | 1 | — | Prayer invoking divine attentiveness — qash.shav as the quality of attentiveness called for in God, expressing human inn |

### M42 (45 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1013-001` | ? | 1 | 1 | — | Term names the professional act of mourning chant — the skilled expression of communal grief through formal lamentation |
| `1031-001` | ? | 41 | 2 | — | Term names the act of singing praise as a whole-person inner orientation — heart, soul, spirit, and voice directed towar |
| `1033-001` | ? | 6 | 2 | — | Term names song as the inner-being expression of orientation toward God — the statutes, the praises, and the voice from  |
| `1071-001` | ? | 7 | 1 | — | Term names the answering word as an expression of inner orientation — the source and quality of a person's answer traces |
| `1132-001` | ? | 1 | 1 | — | Term names the act of slandering — verbal contempt directed at another that incurs moral guilt before God and community |
| `116-001` | ? | 7 | 1 | — | Outcry as expression of suffering, affliction and plea for help |
| `116-002` | ? | 7 | 1 | — | Outcry as communal lamentation — grief and mourning expressed publicly |
| `200-001` | ? | 4 | 1 | — | Outcry as expression of inner pain, anguish and distress — from heart to voice |
| `2684-001` | ? | 1 | 1 | — | Term names the shout or song of deliverance — the joyful cry that arises from rescue and divine protection |
| `2694-001` | ? | 1 | 1 | — | Term names the joyful shout whose absence marks a condition of inner desolation — the missing expression of joy signalli |
| `367-001` | ? | 22 | 2 | — | Term names the inner cry of joy and triumph — the ringing shout that expresses inner exultation before God and in his sa |
| `367-002` | ? | 11 | 2 | — | Term names the inner cry of prayer and petition — the urgent and heartfelt appeal that arises from the depths of the spi |
| `368-001` | ? | 4 | 2 | — | Term names the communal shout of joy or harvest celebration — and its absence as the marker of judgment and inner grief |
| `369-001` | ? | 1 | 1 | — | Term names the communal cry of joy and praise — the expressive inner jubilation voiced by peoples and places in response |
| `372-001` | ? | 53 | 2 | — | Term names the inner act of singing for joy — the vocalized overflow of inner delight and exultation directed toward God |
| `409-001` | ? | 4 | 1 | — | Term names the inward suppression of speech under emotional or spiritual pressure, with deteriorating inner consequence |
| `409-002` | ? | 3 | 1 | — | Term names the moral dimension of silence — the choice to be silent or not at a moment of ethical weight |
| `409-003` | ? | 4 | 2 | — | Term names God's posture of silence and its breaking — divine restraint, patience, or resolve |
| `409-004` | ? | 3 | 1 | — | Term names prophetic inner resolve — refusing silence in advocacy for God's purposes |
| `425-001` | ? | 9 | 1 | — | Term names the inner discipline of silence — the restraint of voice in reverence, receptiveness, or ordered worship |
| `4639-001` | ? | 2 | 1 | — | Term names the groaning of inner distress and suppressed grief — somatic expression of inner suffering breaking through  |
| `4840-001` | ? | 1 | 1 | — | Term is used analogically to describe the Spirit's hidden, inner-working movement — perceived but not tracked, like wind |
| `49-001` | ? | 6 | 1 | ✓ | Term names the inward groan of the person under the weight of embodied limitation, eschatological longing, and unresolve |
| `5171-001` | ? | 32 | 1 | — | Cry of distress and plea to God as expression of inner anguish or urgency |
| `5171-002` | ? | 23 | 1 | — | Cry of grief, anguish or mourning as outward expression of inner pain |
| `5171-003` | ? | 1 | 1 | — | Cry of outcry against injustice, reproach or moral outrage |
| `5494-001` | ? | 2 | 1 | — | Term names the groaning of the person in extremis — the soul's cry under mortal wounding, heard or unheard, expressing t |
| `5500-001` | ? | 7 | 1 | — | Term names the divine roaring that demands inner response — the lion-voice of God that produces unavoidable fear, trembl |
| `5500-002` | ? | 2 | 1 | — | Term names the inner groaning and roaring of anguish — the tumult of the heart expressed as an uncontainable inner sound |
| `5501-001` | ? | 7 | 2 | — | Term names the inner act of meditation — deep, habitual pondering of God's word and deeds that characterises the righteo |
| `5501-002` | ? | 7 | 1 | — | Term names the inner sounds of mourning, groaning, and scheming — the muttering of grief, the devising of violence in th |
| `5994-001` | ? | 3 | 1 | — | Term names the Lord himself as the inner song of the redeemed — the person's strength and salvation expressed as song, G |
| `6045-001` | ? | 10 | 2 | — | Term names prophesying as Spirit-enabled inner-being speech — the act of declaring divine truth through the Holy Spirit' |
| `6045-002` | ? | 10 | 2 | — | Term names the communal exercise of prophecy — its purpose, order, and effect in building up the inner life of the congr |
| `6045-003` | ? | 7 | 2 | — | Term names the fulfilment and testing of prophetic speech — both the historical fulfilment of prophetic words and the mo |
| `6050-001` | ? | 16 | 2 | — | Term identifies the act of prophesying as a Spirit-empowered inner event — the Spirit of God resting on or rushing upon  |
| `6050-002` | ? | 27 | 1 | — | Term identifies prophesying as expression of a true inner commission and orientation toward God — the genuine prophet sp |
| `6050-003` | ? | 26 | 1 | — | Term identifies prophesying as expression of inner deceit and corrupt orientation — false prophets speak from their own  |
| `6050-004` | ? | 21 | 2 | — | Term identifies the prophetic act as obedient expression of divine commission — the prophet's inner responsiveness to Go |
| `719-001` | ? | 4 | 2 | — | Term describes the personal call that reaches the inner person — evoking trust, identity recognition, or spiritual surre |
| `727-001` | ? | 3 | 2 | — | Term describes the inner-being's spontaneous expression of sonship, longing, or appeal arising from the Spirit's work wi |
| `7529-001` | ? | 1 | 1 | — | Voice as expression of inner anguish — qal as the quality of cry that discloses the inner state of the one who speaks |
| `77-001` | ? | 2 | 1 | ✓ | Term names lamentation as the full-voiced inner expression of grief — communal or national mourning that arises from dev |
| `842-001` | ? | 3 | 1 | — | Slander as inner moral failure — speaking evil against others as an act of inner judgement and hostility |
| `895-001` | ? | 5 | 1 | — | Term names the roaring groan as inner-being expression — the cry of dereliction, the groan of unconfessed guilt, and the |

### M43 (22 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1060-001` | ? | 11 | 2 | — | Term names prophecy as a spiritual gift given through the Spirit — the capacity to receive and speak divine disclosure,  |
| `1060-002` | ? | 8 | 2 | — | Term names prophecy as the revelatory word preserved in Scripture and Revelation — the divinely authorised word to which |
| `1061-001` | ? | 3 | 1 | — | Term names the prophetic word as a communication that engages or targets the inner life — heard prophecy moves to courag |
| `1169-001` | ? | 6 | 2 | — | Signs as the direct conditions of inner belief — miraculous signs that function to produce or test faith, with belief or |
| `1200-001` | ? | 3 | 1 | — | Insight as a Spirit-endowed inner capacity — divine gift producing interpretive and cognitive power |
| `1257-001` | ? | 1 | 1 | — | Term qualifies worship as spiritual or rational — arising from the inner person rather than being merely external ritual |
| `1359-001` | ? | 4 | 1 | — | Term defines the human person as bearing the image of God — the constitutive inner dignity and moral ground of the perso |
| `1359-002` | ? | 4 | 1 | — | Term names the objects of idolatrous self-worship, expressing the person's inner orientation of misplaced allegiance and |
| `1359-003` | ? | 2 | 1 | — | Term characterises the person as phantom-like or insubstantial — a statement about the person's inner or existential sta |
| `1361-001` | ? | 2 | 1 | — | Term describes the human person's constitutive dignity as image-bearer — what the person is by divine creation |
| `1361-002` | ? | 3 | 1 | — | Term describes the ongoing renewal and conformity of the inner person toward the divine image |
| `1361-003` | ? | 9 | 1 | — | Term identifies the object of misplaced worship, revealing the person's inner orientation of false allegiance or faithfu |
| `2307-001` | ? | 4 | 1 | — | Term names the spiritual person — one whose inner life is ordered by the Spirit, capable of discerning all things, contr |
| `2307-002` | ? | 5 | 1 | — | Term names spiritual gifts and blessings — the Spirit's concrete manifestations of inner transformation and community en |
| `2307-003` | ? | 5 | 1 | — | Term names the spiritual law and body — the law as spiritual in character; the progression from natural to spiritual in  |
| `2307-004` | ? | 1 | 1 | — | Term names the spiritual forces of evil — the dark spiritual realm opposing the inner life |
| `2307-005` | ? | 6 | 1 | — | Term names spiritual wisdom and understanding — inner capacity for wisdom flowing from the Spirit's work |
| `5862-001` | ? | 5 | 2 | — | Term names the act of interpretation that opens meaning for inner understanding — Scripture interpreted to illuminate Ch |
| `5863-001` | ? | 2 | 2 | — | Term names translation of meaning that discloses theological significance — the name's inner meaning as part of God's re |
| `6052-001` | ? | 1 | 1 | — | Term identifies prophesying as an inner-originating expression that sustains and motivates the inner disposition of hear |
| `7160-001` | ? | 3 | 2 | — | Term names discernment as an inner spiritual capacity — trained by practice to distinguish good from evil, or exercised  |
| `817-001` | ? | 1 | 1 | — | Term names the inner capacity of perception and discernment — the faculty by which love and knowledge translate into pra |

### M44 (23 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1048-001` | ? | 3 | 2 | — | Term names the inner-being act of confessing/acknowledging — the orientation of the person or of Christ toward public de |
| `1208-001` | ? | 2 | 1 | — | Unity as inner-being relational achievement and goal — the Spirit's bond and the faith's convergence |
| `1234-001` | ? | 2 | 1 | — | Divine betrothal — God's covenantal commitment grounded in inner-being character qualities; the goal: knowing the Lord |
| `1609-001` | ? | 6 | 2 | — | Term names "sister" as relational identity grounded in spiritual orientation — redefining family on the basis of obedien |
| `1610-001` | ? | 2 | 2 | — | Term names the brotherhood of believers as a shared inner-being reality — of love to be directed toward it and suffering |
| `210-001` | ? | 1 | 1 | — | Term names the anguish of being given over to enemies — distress as the covenantal consequence of rebellion, with delive |
| `251-001` | ? | 1 | 1 | — | Term names the inner capacity for endurance under increasing pressure — the ability of the inner person to sustain more  |
| `251-002` | ? | 1 | 1 | — | Term names competition as an exposure of inner character — striving for display reveals the poverty of the inner life co |
| `4586-001` | ? | 1 | 1 | — | Term names the inner volitional contending for the faith — earnest defence of what has been entrusted to the inner perso |
| `4806-001` | ? | 6 | 1 | — | Inner bond of shared servanthood — relational identity of those who serve together under the same Lord, characterised by |
| `5178-001` | ? | 10 | 1 | — | Contending with God — inner existential struggle and appeal for divine response |
| `5178-002` | ? | 14 | 1 | — | Pleading one's cause — inner appeal to God or human authority for justice and vindication |
| `5178-003` | ? | 28 | 1 | — | Quarrelling and contention as inner conflict — grievance, frustration, and dispute between persons |
| `5279-001` | ? | 1 | 1 | — | Sharing as inner participation in common calling and service |
| `6843-001` | ? | 5 | 1 | — | Term names inner disposition of sharing — giving from oneself to another in need from love and reoriented will; extendin |
| `7007-001` | ? | 73 | 2 | — | O.yev in lament and prayer: enemy as occasion of inner-being distress |
| `7007-002` | ? | 19 | 2 | — | O.yev in moral instruction: inner-being orientation toward enemy as test of character |
| `7007-003` | ? | 49 | 2 | — | O.yev in theology of divine enmity and deliverance |
| `7008-001` | ? | 5 | 2 | — | E.vah as inner-being disposition of enmity and hostile relational orientation |
| `7566-001` | ? | 2 | 1 | — | companionship as chosen moral and spiritual alignment |
| `7566-002` | ? | 3 | 1 | — | companionship as moral alignment with wickedness |
| `7566-003` | ? | 1 | 1 | — | companionship as mutual relational support |
| `7566-004` | ? | 1 | 1 | — | divinely-willed communal restoration as inner-being oneness |

### M45 (19 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `1097-001` | ? | 2 | 1 | — | Term names the renewal of the inner person — the mind transformed by the Spirit as the foundation for discerning God's w |
| `1098-001` | ? | 3 | 1 | — | Term names change as inner transformation — the hoped-for renewal of one's condition through patient waiting, or the fai |
| `1362-001` | ? | 2 | 1 | — | Term describes the inner transformation of the person toward conformity with God — renewal of mind and progressive confo |
| `1362-002` | ? | 2 | 1 | — | Term describes Christ's visible transformation, which mediates an inner encounter between the disciples and divine reali |
| `2662-001` | ? | 1 | 1 | — | Term names the reversal of inner judgment — changing one's assessment of a person or situation |
| `2753-001` | ? | 1 | 1 | — | Rekindling the inner gift — stirring up spiritual vitality from within |
| `441-001` | ? | 22 | 2 | — | Term names repentance as the inner-being transformation — the godly grief that leads to reorientation of life toward God |
| `443-001` | ? | 1 | 1 | — | Term names the withholding of divine compassion — the inner-relational disposition of God toward a people under judgment |
| `447-001` | ? | 32 | 2 | — | Term names repentance as the inner-being act of turning — the complete reorientation of the person from sin toward God,  |
| `448-001` | ? | 5 | 1 | — | Term names the inner reversal of a previous decision — the change of mind or feeling of regret that follows a prior acti |
| `451-001` | ? | 62 | 1 | — | Term names repentance as the inner act of turning toward God — the deliberate inner reorientation of the whole person fr |
| `451-002` | ? | 15 | 1 | — | Term names God's relenting as a divine inner-relational response to human repentance — God turning from judgment when hi |
| `6132-001` | ? | 2 | 1 | — | Term names the progressive inner renewal of the self — the ongoing transformation of the inner person toward God's image |
| `7360-001` | ? | 2 | 1 | — | Term describes the person's conformity to the image and likeness of Christ — the inner and eschatological telos of the p |
| `7542-001` | ? | 2 | 1 | — | relational reorientation of the self through volitional exchange or affective realignment |
| `7542-002` | ? | 2 | 1 | — | eschatological transformation of the person's constitution |
| `777-001` | ? | 5 | 1 | — | New covenant — unprecedented inner transformation through Spirit |
| `777-002` | ? | 4 | 1 | — | New self / new creation — inner-being renewal of the person in Christ |
| `777-003` | ? | 7 | 1 | — | New name, song, Jerusalem — eschatological inner-being identity, worship, and hope |

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

### T2 (621 VCGs · status: Not started)

| VCG code | Sub-group | V | Anchors | Cited | Description excerpt |
|---|---|---:|---:|:-:|---|
| `10-001` | ? | 5 | 1 | ✓ | Existential distress and hardship as experienced inner pressure |
| `10-002` | ? | 4 | 1 | — | Compulsion vs willing inner orientation — freedom of will |
| `1028-001` | ? | 2 | 1 | — | Term names the shining of divine light upon the person — God's illuminating presence as the condition of the inner life' |
| `1037-001` | ? | 1 | 1 | — | Term names the inner-being act of beautifying God through praise — the person's deliberate orientation toward adorning G |
| `1041-001` | ? | 4 | 2 | — | Term names the oneness of covenantal union — the 'one flesh' or 'one heart and one way' that defines the depth of relati |
| `1041-002` | ? | 5 | 1 | — | Term names the corporate oneness of inner resolve — the united will of a community described as one man or one people |
| `1041-003` | ? | 4 | 2 | — | Term names the uniqueness of God or of the irreplaceable — the one that shapes the weight of divine identity or the cost |
| `1041-004` | ? | 1 | 1 | — | Term names the quantifier that intensifies inner-being experience — the one that shapes the subjective inner weight |
| `1068-001` | ? | 9 | 1 | — | Term names work as divinely commissioned activity — work done for or by God's direction, where inner faithfulness or sla |
| `1068-002` | ? | 21 | 1 | — | Term names work in the context of Sabbath prohibition — where the choice to abstain from work expresses an inner orienta |
| `1101-001` | ? | 1 | 1 | — | Term names the finding of relational favour or grace — finding favour in another's eyes as an inner relational state of  |
| `1101-002` | ? | 1 | 1 | — | Term names the finding of wisdom, understanding, or inner character qualities — the discovery of what is truly good thro |
| `1101-003` | ? | 31 | 1 | — | Term names God finding sin, iniquity, or faithfulness in a person — the divine discernment of the inner moral condition  |
| `1101-004` | ? | 41 | 1 | — | Term names finding rest, refuge, comfort, or the absence of such — the inner state of having found what one needs, or th |
| `1129-001` | ? | 3 | 1 | — | Term names the act of slandering — going about with malicious speech, an inner act of verbal contempt that violates rela |
| `1136-001` | ? | 3 | 1 | — | Term names sorcery as an inner-spiritual practice of rebellion — the orientation that seeks supernatural power outside o |
| `1137-001` | ? | 6 | 2 | — | Term names the practice of sorcery — the act of engaging occult power as an expression of the inner spiritual orientatio |
| `1149-001` | ? | 1 | 1 | — | Closing the heart against compassion — the inner act of hardening whereby the inner being shuts itself off from pity |
| `1163-001` | ? | 14 | 2 | — | The testimony as the object of inner heart-engagement — the divine testimony to which the heart is inclined, which the s |
| `1167-001` | ? | 2 | 1 | — | Testimony sealed within disciples — the divine testimony committed to an inner circle, with spiritual condition (having  |
| `1175-001` | ? | 6 | 2 | — | Intending and planning as inner acts — the inner disposition of purpose, aspiration, and design, including divine and hu |
| `1228-001` | ? | 20 | 2 | — | Term names deliberate human action as the expression of inner character and will — what a person does as the outward ena |
| `1233-001` | ? | 3 | 2 | — | Term names the broken spirit as an inner-being condition of contrition — the crushed and humbled heart that God does not |
| `1233-002` | ? | 7 | 2 | — | Term names the breaking of the inner person by grief, shame, or divine judgment — the shattering of the human spirit und |
| `1235-001` | ? | 11 | 1 | — | Divine commission — "Go!" as the inner-being call to prophetic obedience and vocation |
| `1235-002` | ? | 11 | 1 | — | Going after other gods / false loves — inner-being movement toward idolatry and spiritual infidelity |
| `1235-003` | ? | 8 | 1 | — | The way you should go — divine guidance of inner direction; God going before or with his people |
| `1235-004` | ? | 12 | 1 | — | Going to/seeking God or failing to find him — inner-being orientation toward the divine |
| `1235-005` | ? | 7 | 1 | — | Going toward death — inner-being confrontation with mortality and departure |
| `1235-006` | ? | 1 | 1 | — | "My heart has gone after my eyes" — inner-being mechanism of moral departure |
| `1238-001` | ? | 5 | 1 | — | God enthroned / dwelling in the midst of his people — divine presence as the ground of inner security |
| `1238-002` | ? | 9 | 1 | — | Dwelling in darkness / sitting in ashes — inner-being conditions of desolation, lament, and humiliation |
| `1238-003` | ? | 7 | 1 | — | Dwelling as eschatological rest and security — the promise of peaceful habitation |
| `1238-004` | ? | 8 | 1 | — | Covenantal dwelling — "dwell as mine", "I will dwell in your midst", the intimate possession of dwelling |
| `1238-005` | ? | 6 | 1 | — | The arrogant heart's aspiration to sit on high — inner pride named in the will to enthrone oneself |
| `1238-006` | ? | 5 | 1 | — | Inner-being grief and solidarity expressed in sitting — sitting in ashes, sitting with the suffering |
| `1239-001` | ? | 21 | 1 | — | Inner-being identity and relational status — "I am," "we are," being named in relation to God, sin, grace, the flesh |
| `1239-002` | ? | 12 | 1 | — | No one righteous, no one seeks — the universal inner-being condition of humanity |
| `1239-003` | ? | 25 | 1 | — | The word is near, in your mouth and in your heart; hope, conviction, calling — inner-being states named through "being" |
| `1248-001` | ? | 52 | 2 | — | Term names worship as the act of prostration and bowing before God — the complete physical and inner-being orientation o |
| `1248-002` | ? | 42 | 1 | — | Term names idolatrous prostration — bowing to other gods or images as the inner-being act of misplaced worship |
| `1248-003` | ? | 54 | 2 | — | Term names social prostration as an act of relational deference — the physical expression of honour, petition, or submis |
| `1250-001` | ? | 1 | 1 | — | Term names worship-prostration as an inner devotional response to divine revelation — recognition of God's presence and  |
| `1250-002` | ? | 10 | 1 | — | Term names commanded or coerced prostration before a human image — the false worship system that demands inner-being all |
| `1251-001` | ? | 15 | 2 | — | Term names worship/service as the inner devotional orientation of the person directed toward God — enacted in prayer, fa |
| `1251-002` | ? | 3 | 1 | — | Term names service rendered to idols or false gods — the inner devotion misplaced toward counterfeit objects |
| `1251-003` | ? | 3 | 1 | — | Term names worship as a priestly/liturgical act — ordered service in the sanctuary expressing the community's inner orie |
| `1253-001` | ? | 5 | 2 | — | Term names worship as a divinely oriented inner service — the person's orientation of devoted service toward God, enacte |
| `1255-001` | ? | 19 | 2 | — | Term names priestly or Levitical ministry as a devoted inner vocation — standing before God to serve, a calling requirin |
| `1255-002` | ? | 2 | 1 | — | Term names personal attendance and service as an expression of relational devotion — the servant who attends and support |
| `1259-001` | ? | 3 | 1 | — | Term names ministry as a sacred service rendered to God and to the community — an act of devotion expressing inner commi |
| `1260-001` | ? | 4 | 1 | — | Term assesses inner worth of things — what the person considers valuable, comparative moral reasoning |
| `1260-002` | ? | 1 | 1 | — | Term describes setting God's law before oneself — will oriented toward divine standards |
| `1260-003` | ? | 1 | 1 | — | Term describes the stilling of one's soul — deliberate inner rest and contented trust before God |
| `1260-004` | ? | 4 | 1 | — | Term evokes God's incomparability — the worshiper's inner recognition that nothing equals the divine |
| `1260-005` | ? | 2 | 1 | — | Term applies to character likeness — the risk of becoming like another in inner disposition |
| `1260-006` | ? | 1 | 1 | — | Term expresses grief beyond comparison — incomparability of suffering, failing to find any adequate parallel |
| `1265-001` | ? | 52 | 1 | — | Term used in moral sowing metaphors — sowing righteousness or injustice as inner character dispositions that determine w |
| `1265-002` | ? | 1 | 1 | — | Term used of God's sowing of inner states — light, joy, restoration, re-planting as covenantal love |
| `1265-003` | ? | 1 | 1 | — | Term names sowing in tears — grief-laden faithful labour as an inner experience anticipating joyful harvest |
| `1267-001` | ? | 4 | 1 | — | Term names inner moral integrity of fulfilling sworn commitments to God — weight of conscience under oath |
| `1267-002` | ? | 3 | 1 | — | Term names inner sincerity of devotional acts — giving, praying, fasting toward God rather than human approval |
| `1267-003` | ? | 13 | 1 | — | Term names moral accountability before God — giving account for words, deeds, stewardship, at final judgment |
| `1267-004` | ? | 5 | 1 | — | Term names inner moral discernment of dual obligation — rendering to human authority and to God what each is owed |
| `1267-005` | ? | 3 | 1 | — | Term names inner restraint of refusing evil for evil — the moral choice to bless rather than retaliate |
| `1267-006` | ? | 3 | 1 | — | Term names inner transformation of repentance expressed through generous voluntary restitution |
| `1267-007` | ? | 2 | 1 | — | Term names inner fruit produced by endured discipline — peaceable righteousness formed through training |
| `1267-008` | ? | 1 | 1 | — | Term names inner failure of misplaced valuation — selling eternal inheritance for immediate appetite |
| `1267-009` | ? | 6 | 1 | — | Term names inner disposition of honouring obligations — giving respect and honour as moral debts |
| `1267-010` | ? | 5 | 1 | — | Term names the act of giving testimony — expressing inner conviction through witness |
| `1276-001` | ? | 25 | 2 | — | Term names cursing as an inner-being act — directed against parents, God, rulers, or God's anointed — with moral and cov |
| `1276-002` | ? | 16 | 2 | — | Term names contempt as the inner disposition that evaluates another as light/worthless — looking down on persons, treati |
| `1276-003` | ? | 5 | 2 | — | Term names the lightening of burden or minimising of difficulty — in its inner-being dimension: divine perspective on di |
| `1284-001` | ? | 1 | 1 | — | Term names the contempt directed at the Son of Man — the inner-being experience of rejection and disgrace borne as the p |
| `1286-001` | ? | 13 | 2 | — | Term names tearing as the expression of violent inner states — divine wrath, human predatory character, destructive ange |
| `1305-001` | ? | 15 | 2 | — | Term names divine ability as the ground of faith, hope, and inner orientation — what God is able to do that the inner be |
| `1305-002` | ? | 15 | 2 | — | Term names a person's inner capacity — strength, ability, self-control, or competence — as a quality of the inner being  |
| `1308-001` | ? | 35 | 2 | — | Term names a person's inner moral or spiritual capacity or incapacity — the ability or inability that is rooted in the i |
| `1308-002` | ? | 12 | 2 | — | Term names God's sovereign moral capacity or incapacity — what God can or cannot do as a disclosure of his inner charact |
| `1309-001` | ? | 18 | 2 | — | Term names the hands lifted, spread, or stretched toward God in prayer and worship — the physical posture of the hands e |
| `1309-002` | ? | 23 | 2 | — | Term names the hands as the moral expression of the inner life — clean or defiled hands as the outer form of inner integ |
| `1309-003` | ? | 14 | 2 | — | Term names the hands as the vehicle of emotional and spiritual expression — clapping, striking, or gesturing that gives  |
| `1309-004` | ? | 27 | 2 | — | Term names the hand as the place of power, custody, or deliverance — being held under another's power or freed from it,  |
| `1315-001` | ? | 10 | 2 | — | Term names the hand as metonymy for power, custody, and authority — the inner being engaged through trust, fear, depende |
| `1327-001` | ? | 7 | 2 | — | Term names a command issued with authority — the inner being engaged through apostolic commission, divine mandate, or th |
| `1332-001` | ? | 4 | 1 | — | H7161A as metaphor for the dignity, strength, and honour of a person or people — the inner-being quality of strength in  |
| `1335-001` | ? | 6 | 1 | — | H4592 qualifies the significance, sufficiency, or weight of inner-being experience, spiritual privilege, or relational c |
| `1335-002` | ? | 2 | 1 | — | H4592 qualifies the temporal scope or duration of a divine inner-being state (wrath, anger) |
| `1339-001` | ? | 2 | 1 | — | H3627 as vessel metaphor conveying the inner quality, worth, or relational status attributed to a person or people |
| `1339-002` | ? | 3 | 1 | — | H3627 as vessel metaphor conveying inner character formation, moral orientation, or condition of desolation |
| `134-001` | ? | 72 | 2 | — | Term names the act of profaning what is sacred — the inner-moral act of treating holy things, God's name, or the Sabbath |
| `1340-001` | ? | 96 | 10 | — | Term names the coming or approach that engages the inner being through encounter with God — God coming to humans in theo |
| `1340-002` | ? | 11 | 4 | — | Term names the arrival of calamity, distress, dread, and mortality upon the inner being — the moment when feared things  |
| `1340-003` | ? | 19 | 2 | — | Term in relational and covenantal entry with inner-being moral dimension — entering another person with longing, decepti |
| `1344-001` | ? | 2 | 1 | — | H1934 predicates an inner character quality or spiritual state as present within a person |
| `1344-002` | ? | 1 | 1 | — | H1934 as the verbal form carrying an act of inner contemplation or reflective observation |
| `1352-001` | ? | 41 | 5 | — | Term names the becoming of the inner being — transformation, formation, identity-shift, disclosure, and accountability;  |
| `1353-001` | ? | 3 | 1 | — | Term names the receiving of what is due — whether divine inheritance, adopted sonship, or inward penalty; the inner bein |
| `1368-001` | ? | 2 | 1 | — | Term describes the pouring out of the innermost self — the soul poured to death, the Spirit poured upon the people — the |
| `1368-002` | ? | 2 | 1 | — | Term describes the divine act of uncovering and exposing the person in judgment, bringing shame and humiliation |
| `1368-003` | ? | 2 | 1 | — | Term names the violation of intimate covering — the uncovering of sexual boundaries that carries moral consequence and i |
| `1368-004` | ? | 1 | 1 | — | Term expresses the person's inner vulnerability and the prayer not to be left defenseless before God |
| `1369-001` | ? | 1 | 1 | — | Term names the pre-fall state of nakedness without shame — the person's original inner freedom from guilt and fear befor |
| `1369-002` | ? | 2 | 1 | — | Term expresses the radical existential nakedness of the human person — coming and returning with nothing, utterly depend |
| `1369-003` | ? | 4 | 1 | — | Term describes nakedness as prophetic or ecstatic expression — the person's body and inner being made a visible sign bef |
| `1369-004` | ? | 5 | 1 | — | Term names the nakedness of the vulnerable, the oppressed, and the captive — a condition that calls for inner-being resp |
| `1369-005` | ? | 3 | 1 | — | Term names the nakedness of divine judgment — the stripping that accompanies wrath, exposing what was hidden |
| `1370-001` | ? | 1 | 1 | — | Term describes total exposure before God — the person fully seen with no inner reality concealed |
| `1370-002` | ? | 3 | 1 | — | Term characterises the person's inner state of spiritual nakedness — unpreparedness, self-unawareness, or eschatological |
| `1370-003` | ? | 4 | 1 | — | Term names physical nakedness as a condition of human need that calls for a morally engaged inner response of compassion |
| `1370-004` | ? | 2 | 1 | — | Term describes nakedness as the experience of exposure and shaming in judgment or spiritual encounter |
| `1371-001` | ? | 1 | 1 | — | Term describes the plunging of the person/domain into darkness as divine judgment, producing inner anguish |
| `1378-001` | ? | 15 | 2 | — | Spiritual deadness as the person's condition — dead in sin, dead to God |
| `1378-002` | ? | 4 | 2 | — | Dead to sin / dead to the law — inner-being reorientation through Christ |
| `1378-003` | ? | 2 | 2 | — | Dead works — works from spiritual deadness; conscience purified from them |
| `1378-004` | ? | 2 | 1 | — | Dead faith — faith as a dead inner-being capacity without works |
| `1378-005` | ? | 16 | 2 | — | Resurrection of the dead as ground for inner-being hope, faith, and aspiration |
| `1379-001` | ? | 18 | 2 | — | Death as consequence of inner moral failure — dying as outcome of folly, wickedness, sin |
| `1379-002` | ? | 30 | 2 | — | Death as object of inner-being orientation — fear, longing, resolve, wisdom on mortality |
| `1379-003` | ? | 5 | 2 | — | God's sovereignty over death as ground of inner-being trust and confidence |
| `1379-004` | ? | 9 | 2 | — | The dead in relation to God — cut off from his hand; loss of praise capacity |
| `1380-001` | ? | 1 | 1 | — | Spiritual deadness in a living person — physically alive but inwardly dead through self-indulgence |
| `1400-001` | ? | 1 | 1 | — | Term names the lifeless/soulless state of an instrument — implying the person, unlike a lifeless object, has inner life  |
| `145-001` | ? | 7 | 1 | — | Distress and anguish as experienced inner condition — fear, torment, suffering |
| `154-001` | ? | 1 | 1 | — | Term names dullness or covering of the heart — the inner condition of hardened insensitivity, imposed as a divine judgme |
| `1562-001` | ? | 1 | 1 | — | Term names the sharp inner conflict of disagreement — the cutting edge of contention between persons of conviction |
| `1562-002` | ? | 1 | 1 | — | Term names the deliberate inner-stimulation toward love and good works — the intentional provoking of others' inner life |
| `158-001` | ? | 1 | 1 | — | Term names the anointed guardian cherub as the one whose privileged inner access to God was corrupted by pride — anointi |
| `1613-001` | ? | 15 | 1 | — | Term names the womb as the threshold of human existence over which God exercises sovereign care — the space where divine |
| `1613-002` | ? | 8 | 1 | — | Term names the womb as the origin of human existence — its use in lament and ethical reflection grounds the human person |
| `1617-001` | ? | 152 | 2 | — | Term names the neighbour as the moral category defining the inner person's obligation — the one toward whom honesty, car |
| `1619-001` | ? | 2 | 2 | — | Term names the companion as the one to whom loyalty is shown or from whom it is withheld — the relational bond whose pre |
| `1624-001` | ? | 2 | 2 | — | Term names the companion in communal grief — the friends who accompany another in their inner lamentation |
| `163-001` | ? | 7 | 1 | — | Term names the bitterness of soul in deep distress — the inner taste-quality of grief, anguish, and sorrow experienced i |
| `163-002` | ? | 3 | 1 | — | Term names the bitter intensity of anger — the fierce, biting quality of wrath in action and in character |
| `163-003` | ? | 2 | 1 | — | Term names the bitterness of the human condition — the taste of life as toil, futility, and moral poison under the sun |
| `1655-001` | ? | 1 | 1 | — | Refusing the delicacies of the wicked — inner-being discipline against enticement |
| `167-001` | ? | 4 | 1 | — | Term names the anointing that confers the Spirit — the act of anointing as the occasion of the Spirit rushing upon the p |
| `167-002` | ? | 6 | 1 | — | Term names the sacred inviolability of the anointed — the inner prohibition against harming the one whom God has set apa |
| `167-003` | ? | 8 | 1 | — | Term names anointing as divine appointment and blessing — the act that designates the person for a calling and marks div |
| `169-001` | ? | 4 | 1 | — | Term names the anointing oil as the sacred medium of consecration — the oil prepared and applied in the act of setting a |
| `1691-001` | ? | 1 | 1 | — | Act of terrifying — inner-being impact of overwhelming authoritative force, in context of pastoral authority and its app |
| `170-001` | ? | 4 | 1 | — | Term names the anointing oil as the sacred medium of consecration — the oil prepared and applied in the act of setting a |
| `171-001` | ? | 5 | 1 | — | Term names the anointed priest whose inner condition carries covenantal weight — the priest whose sin or purity affects  |
| `171-002` | ? | 10 | 1 | — | Term names the anointed king as the person set apart for divine rule — the one whom God has chosen and whose protection  |
| `171-003` | ? | 2 | 1 | — | Term names the anointed one whose coming is the fulfilment of divine promise — Messiah as the eschatological figure whos |
| `179-001` | ? | 4 | 1 | — | Term names the deliberate abstention from anointing as a practice of mourning — not anointing as the outward expression  |
| `179-002` | ? | 1 | 1 | — | Term names the anointing of restoration — God anointing the person as the act of claiming and beautifying what had been  |
| `1801-001` | ? | 10 | 1 | — | Term names the inner parts as the seat of compassion and tender emotion — the physical location of deep emotional stirri |
| `1801-002` | ? | 10 | 1 | — | Term names the inner parts as the seat of grief and anguish — the physical location of acute inner pain |
| `1801-003` | ? | 10 | 1 | — | Term names the inner parts as the origin of speech and wisdom — the source from which words and understanding flow |
| `183-001` | ? | 1 | 1 | — | Term names verbal aggression as the outer expression of inner hostility — railing and abuse as manifestations of the con |
| `1860-001` | ? | 1 | 1 | — | Term names a visceral physical expression that carries the inner state of grief and anguish at communal devastation |
| `196-001` | ? | 5 | 1 | — | Term names the inner-being sorrow and injury that afflicts the person — sorrows that multiply for those who follow other |
| `2071-001` | ? | 1 | 1 | — | Divine delight expressed as a new name — God's inner joy in his people |
| `208-001` | ? | 2 | 1 | ✓ | Narrowness and constraint as inner-bearing experience of distress and limitation |
| `219-001` | ? | 8 | 1 | — | Term names the inner-being darkness of mourning — the darkened inner state of the person who goes about in grief, whose  |
| `225-001` | ? | 1 | 1 | ✓ | Term names the shortness of spirit that closes the inner ear — the anguish of impossible burden that renders the person  |
| `23-001` | ? | 1 | 1 | — | Term names inner fury triggered by perceived betrayal — the rage that erupts when deception is discovered, driving viole |
| `230-001` | ? | 4 | 2 | — | Term names the cosmic defeat of Rahab — God's inner-being of power and understanding expressed in the crushing of the pr |
| `243-001` | ? | 7 | 1 | — | Oil as metaphor for quality and character of the inner person |
| `243-002` | ? | 4 | 1 | — | Oil of gladness — inner joy and divine bestowing of flourishing |
| `243-003` | ? | 7 | 1 | — | Oil as outward sign of divine appointment and inner consecration |
| `243-004` | ? | 9 | 1 | — | Oil as marker of disordered inner orientation — self-indulgence and spiritual unfaithfulness |
| `243-005` | ? | 1 | 1 | — | Oil as image of inner penetration — reaching the deepest interior of the person |
| `2444-001` | ? | 2 | 1 | — | Term names the sin committed before Paul's coming — the prior inner-being condition of unrepented sin that Paul mourns o |
| `2502-001` | ? | 2 | 1 | — | Term names extended duration that shapes inner orientation — length of time pressing upon the inner life of those who wa |
| `2521-001` | ? | 7 | 2 | — | Term names a signal or banner that orients the inner life — the object to which hope, fear, or trust is directed, or fro |
| `2577-001` | ? | 1 | 1 | — | Term names the inner condition of ease and security — the state of the person wholly undisturbed, here in the context of |
| `2589-001` | ? | 1 | 1 | — | Term names the granting of relief — a remission that brings rest and lightening of burden to those who receive it |
| `2601-001` | ? | 7 | 1 | — | Term names the cessation or ruination of the inner person — the collapse of human dignity, prophetic undoing before holi |
| `2617-001` | ? | 22 | 1 | — | Term names the inner act of looking to God — the orientation of the person's gaze toward God in prayer, trust, hope, or  |
| `2617-002` | ? | 29 | 1 | — | Term names looking that discloses an inner state — contempt, envy, mourning, longing, or divine regard withheld — where  |
| `2617-003` | ? | 8 | 1 | — | Term names the divine act of looking — God's inner attentive regard toward humanity, which is relational inner engagemen |
| `2658-001` | ? | 2 | 1 | — | Term names the unchangeable character of God's purpose and truthfulness as the foundation for inner encouragement and ho |
| `2693-001` | ? | 8 | 1 | — | Joy as the inner-being overflow of delight — exultation, gladness, exceeding rejoicing |
| `2708-001` | ? | 1 | 1 | — | Inner condition of unresolved division — will suspended between two incompatible orientations, committed to neither |
| `2710-001` | ? | 1 | 1 | — | Inner state of anticipatory pre-worry — anxiety about a future threatening situation before it arrives |
| `275-001` | ? | 1 | 1 | — | Term names terror-producing events or phenomena — the things that generate overwhelming inner fear at the end of the age |
| `2764-001` | ? | 82 | 2 | — | Term names human inner capacity or incapacity — what a person morally, spiritually, or by faith can or cannot do — the a |
| `2764-002` | ? | 12 | 2 | — | Term names God's or Christ's sovereign capacity — what he can do for the inner being: save, strengthen, sympathize, keep |
| `2768-001` | ? | 2 | 2 | — | Term names a ruler or sovereign whose position engages the inner being — through divine reversal, awe, or theological co |
| `2772-001` | ? | 1 | 1 | — | Term names the power of Christ operative within a community — inner-being empowerment |
| `2798-001` | ? | 1 | 1 | — | Term names citizen-subjects whose inner attitude of rejection toward the ruler is expressed |
| `2799-001` | ? | 1 | 1 | — | Term names covenantal/communal belonging — alienation from it engaging the inner being through separation from God's peo |
| `2800-001` | ? | 2 | 2 | — | Term names the manner of life as a citizen — the inner being engaged through orientation toward worthy, gospel-shaped co |
| `2803-001` | ? | 6 | 2 | — | Term names a commanding act that evokes inner responses of awe, submission, or dread — the authority behind the command  |
| `2810-001` | ? | 8 | 2 | — | Term names the act of using a proverb or parable — the inner being engaged through the wisdom tradition's address to the |
| `2811-001` | ? | 7 | 2 | — | Term names the act of comparison or likening — the inner being engaged through self-recognition, theological discernment |
| `2815-001` | ? | 9 | 2 | — | Term names the hand as the seat of ownership, rule, or custodial power — the inner being engaged through deliverance, su |
| `2816-001` | ? | 29 | 2 | — | Term names the hands raised, lifted, or spread in prayer and worship — the physical posture of the hands expressing the  |
| `2816-002` | ? | 73 | 2 | — | Term names the hands as the moral expression of the inner life — clean or defiled hands as the outer index of inner inte |
| `2816-003` | ? | 16 | 2 | — | Term names the hands as the vehicle of emotional and spiritual expression — gestures of defiance, grief, silence, awe, o |
| `2816-004` | ? | 137 | 2 | — | Term names the hand as the locus of deliverance, power, divine action, and custodial authority — the inner being engaged |
| `2817-001` | ? | 267 | 2 | — | Term names the hand as the seat of power, custody, authority, and stewardship — the inner being engaged through being he |
| `2818-001` | ? | 8 | 1 | — | Inner-being self-direction: yielding, restraining, consecrating, or pledging the self before God or others |
| `2820-001` | ? | 3 | 1 | — | Moral accountability and covenantal claim |
| `2821-001` | ? | 1 | 1 | — | Measure of inner-being excellence |
| `2822-001` | ? | 1 | 1 | — | The monument as lasting inner-being identity and legacy |
| `2826-001` | ? | 1 | 1 | — | Divine presence as spacious refuge |
| `2827-001` | ? | 12 | 2 | — | Term names the filling or consecration of the hand in priestly ordination — the inner being engaged through the inner de |
| `2828-001` | ? | 17 | 2 | — | Term names the raising of the hand in sworn oath — the inner being engaged through covenantal commitment, the binding of |
| `2830-001` | ? | 5 | 1 | — | Human purposeful undertaking as the site of divine blessing and inner-being rejoicing |
| `2832-001` | ? | 4 | 1 | — | Term names the placement of the hand under the thigh in solemn oath — the inner being engaged through the binding covena |
| `2835-001` | ? | 2 | 1 | — | Sole of foot as marker of total inner-being suffering and restlessness |
| `2835-002` | ? | 3 | 1 | — | Foot as marker of divine presence, submission, and holiness |
| `2846-001` | ? | 3 | 2 | — | Term names the governor's exercise of authority at the boundary of the sacred — the inner being engaged through rulings  |
| `2854-001` | ? | 31 | 2 | — | Term names rulers — human, demonic, or cosmic — whose authority and action engage the inner being through recognition, f |
| `2868-001` | ? | 2 | 1 | — | Term names a divinely-ordained arrangement or ordinance — the inner being engaged through reception of or resistance to  |
| `2869-001` | ? | 1 | 1 | — | Term names a royal edict whose threat is met by faith — the inner being engaged through the choice to fear God rather th |
| `2870-001` | ? | 7 | 2 | — | Term names a strict charge or instruction laid upon persons — the inner being engaged through the weight of obligation a |
| `2872-001` | ? | 27 | 5 | — | Term names the multiplication of sin, transgression, iniquity, evil, and abomination — the inner being morally corrupted |
| `2872-002` | ? | 6 | 2 | — | Term names the multiplication of spiritual unfaithfulness — whoring after other gods, multiplying idolatrous altars, and |
| `2872-003` | ? | 11 | 4 | — | Term names the multiplication of inner-being suffering — pain, sorrow, mourning, vexation, distress, fear, and grief int |
| `2872-004` | ? | 13 | 3 | — | Term names the multiplication of wisdom, knowledge, understanding, and their counterparts — foolish excess of words, van |
| `2872-005` | ? | 9 | 6 | — | Term names the multiplication of divine grace — abundant pardon, plentiful redemption, enlargement of the inner being th |
| `2872-006` | ? | 22 | 4 | — | Term names multiplication as moral and covenantal consequence — increase predicated on obedience, prayer, inner posture, |
| `2882-001` | ? | 53 | 2 | — | Term names appointment to oversight or charge — the inner being engaged through the trust, responsibility, and accountab |
| `2883-001` | ? | 10 | 2 | — | Term names the act of numbering/listing that carries covenantal or moral significance — the inner being engaged through  |
| `2885-001` | ? | 48 | 2 | — | Term names divine punishment as a reckoning — the inner being engaged through moral accountability, the fear of God's ju |
| `2886-001` | ? | 37 | 2 | — | Term names divine visitation — God's gracious or judicial coming to persons that transforms their circumstances and enga |
| `2887-001` | ? | 12 | 2 | — | Term names the state of being missed or missing — the inner being engaged through relational longing, concern for absent |
| `2889-001` | ? | 12 | 2 | — | Term names divine punishment as an appointed reckoning — the inner being engaged through the dread of God's judicial day |
| `2889-002` | ? | 18 | 2 | — | Term names an appointed charge, duty, or oversight — the inner being engaged through stewardship, care, and accountabili |
| `2890-001` | ? | 24 | 2 | — | Term names the precepts of the Lord — divine instructions that engage the inner being through meditation, love, obedienc |
| `2891-001` | ? | 13 | 2 | — | Term names a person appointed to oversee — the inner being engaged through the authority of appointed office, the respon |
| `2892-001` | ? | 1 | 1 | — | Term names appointment to authoritative oversight — the inner being engaged through the bestowal of responsibility and t |
| `2893-001` | ? | 3 | 1 | — | Term names a deposit entrusted to another's care — the inner being engaged through the moral obligation of faithful stew |
| `2895-001` | ? | 1 | 1 | — | Term names the exercise of oversight authority — the inner being engaged through the use of appointed authority over per |
| `2951-001` | ? | 10 | 1 | — | Term names the queen as one whose inner will, courage, and intercession move history — inner resistance, love for her pe |
| `2951-002` | ? | 1 | 1 | — | Term names the queen as the one whose incomparable worth evokes praise — even rivals are moved to honour what they recog |
| `2962-001` | ? | 3 | 1 | — | Division as inner conflict and relational fracture — people divided, desire to dominate |
| `2962-002` | ? | 7 | 1 | — | Portion allotted by God — the divine distribution of understanding, pain, and eschatological reward |
| `2972-001` | ? | 1 | 1 | — | Krataios as divine might calling forth inner response of humility |
| `2975-001` | ? | 4 | 2 | — | Term names the official as the one required to address and shape the inner dispositions of those under authority — deman |
| `2978-001` | ? | 1 | 1 | — | Term marks the point of convergence of the peoples' obedience and allegiance — the fulfilment of inner loyalty directed  |
| `2987-001` | ? | 2 | 1 | — | Term names a person as the possessor of spiritual power — a medium or sorceress defined by her mastery of occult capacit |
| `2993-001` | ? | 4 | 2 | — | Term names inner restlessness — the driven, unsettled condition of one in distress, or the restless spirit that refuses  |
| `301-001` | ? | 12 | 2 | ✓ | Term describes the inner dissolution of heart and spirit under overwhelming fear, dread, or threatening circumstance — t |
| `3012-001` | ? | 1 | 1 | — | Term names the kinship bond of flesh — the close bodily relation between persons that creates an inviolable inner moral  |
| `3077-001` | ? | 25 | 1 | — | The freewill offering — inner-being voluntary devotion expressed in giving, sacrifice, and praise |
| `3082-001` | ? | 6 | 1 | — | Sect/faction as an expression of chosen inner orientation — religious commitment, communal division, or doctrinal choice |
| `3094-001` | ? | 10 | 2 | — | Term names inheritance as a moral-spiritual outcome — what a person receives as the result of their inner character and  |
| `3094-002` | ? | 3 | 1 | — | Term names God as the inheritance of the person — the inner-being orientation of those who possess God himself as their  |
| `3095-001` | ? | 7 | 2 | — | Term names God himself or divine presence as the inheritance of the faithful person — the ultimate inner-being possessio |
| `3095-002` | ? | 5 | 1 | — | Term names the inheritance of the righteous as a moral-spiritual promise — what the upright receive as the outcome of th |
| `3095-003` | ? | 6 | 1 | — | Term names what is received as an inner-being treasure — the law, children, or wisdom as inheritance of the heart |
| `3167-001` | ? | 13 | 2 | — | Term names almsgiving as the outward expression of an inward disposition of mercy and generosity — the inner orientation |
| `3170-001` | ? | 10 | 2 | — | Term names a substitutionary price paid for a life — ransom as the means by which moral accountability for life is addre |
| `3170-002` | ? | 3 | 1 | — | Term names illicit payment that corrupts the inner moral vision of the recipient — a bribe that blinds or deflects justi |
| `3204-001` | ? | 2 | 2 | — | Term names the human judge or ruler in the context of the inner act of rejecting divinely appointed authority |
| `3220-001` | ? | 7 | 2 | — | Term names the law or decree as the framework within which inner moral and religious commitment is tested — the external |
| `3237-001` | ? | 2 | 2 | — | Term names God as the divine judge — the one whose inner justice and attentiveness to the wronged defines the nature of  |
| `3270-001` | ? | 2 | 1 | — | Reverential awe before the holy — the ark as the mediating sign that orients the inner person toward the presence and fa |
| `3271-001` | ? | 1 | 1 | — | Obedience under judgment — the ark as the instrument that separates the inner orientation of faithful response from heed |
| `3306-001` | ? | 2 | 1 | — | Legal dissolution of the marriage covenant — formal relational rupture |
| `3306-002` | ? | 2 | 1 | — | Divorce as metaphor for God's covenantal rupture with Israel — inner-being severity of apostasy |
| `3308-001` | ? | 30 | 1 | — | Divine oath as expression of God's inner commitment to his covenant promise |
| `3308-002` | ? | 79 | 1 | — | Human oath as the binding of inner will and loyalty |
| `3308-003` | ? | 17 | 1 | — | Swearing by God's name — oath as expression of inner-being allegiance or its corruption |
| `3308-004` | ? | 5 | 1 | — | Adjuration — invoking in the context of intense inner longing and love |
| `3314-001` | ? | 4 | 1 | — | Prophetic weeks as the divinely appointed schedule for covenant fulfillment |
| `3314-002` | ? | 2 | 1 | — | Weeks as the measure of inner-being mourning and self-denial |
| `34-001` | ? | 1 | 1 | — | Term names anointing in anticipation of death — the act of love that prepares the body of Christ for burial, performed i |
| `343-001` | ? | 6 | 1 | — | The eye as inner moral organ — healthy and bad eye as inner orientation of the whole person |
| `343-002` | ? | 9 | 1 | — | Spiritual blindness and the closed eye — inner failure of perception and understanding |
| `343-003` | ? | 9 | 1 | — | Eyes opened to spiritual reality — the inner moment of recognition and illumination |
| `343-004` | ? | 11 | 1 | — | Desires of the eyes and envy — the eye as instrument of inner covetousness |
| `3498-001` | ? | 11 | 2 | — | Term names the institutional memorial — an act, object, or day established to keep an event or person before God and the |
| `3498-002` | ? | 6 | 1 | — | Term names the priestly/liturgical keeping of persons before God — the act of bearing names or offerings into God's pres |
| `3498-003` | ? | 5 | 1 | — | Term names the inner act of remembrance — the capacity to hold persons and events in living consciousness, and the absen |
| `3499-001` | ? | 7 | 1 | — | Term names the memorial portion of an offering — the part burned before God as an act of bringing the offerer to divine  |
| `3591-001` | ? | 1 | 1 | — | Term identifies deliberate inner intentionality — whether an action is purposed and willed, here probing the inner resol |
| `370-001` | ? | 2 | 2 | — | Term names the spontaneous cry of joy that breaks out in response to a direct divine act — the inner overflow of awe and |
| `3833-001` | ? | 3 | 1 | — | Term names the delicacy or delight as what gives the inner person deep satisfaction — the luxurious good that is held as |
| `403-001` | ? | 1 | 1 | — | Term names the inner act of being first to hope in Christ — the prior orientation of hope toward him before his revelati |
| `4649-001` | ? | 2 | 1 | — | Term names the moral-economic violation in pledge-taking — inner conduct that exploits the vulnerable through use of wha |
| `4668-001` | ? | 2 | 1 | — | Term names the short-tempered person as one lacking inner governance — the outer pattern of quick anger as the expressio |
| `4692-001` | ? | 3 | 1 | — | Term names the antichrist as the paradigm of inner spiritual deception — the spirit of denial as the inner orientation t |
| `4703-001` | ? | 5 | 1 | — | Term names the anointing oil as the vehicle of devotion — the costly perfume offered as the expression of inner love and |
| `4722-001` | ? | 3 | 1 | — | Term names the satisfaction of the soul — the inner fullness of delight when the person is nourished by what God provide |
| `4723-001` | ? | 1 | 1 | — | Term names the flourishing of the inner person in old age — the fat and fresh quality of the soul that continues to bear |
| `4815-001` | ? | 3 | 1 | — | Inner experience of being at the threshold of birth — extreme distress and exhaustion at the crisis moment, and failure  |
| `4832-001` | ? | 1 | 1 | — | Term names the prophetic proclamation as an act of divine communication that calls persons to inner accountability and r |
| `4862-001` | ? | 2 | 1 | — | Term names the crown as the symbol of the consecrated or covenantal state — the outward sign of inner dedication and hol |
| `4863-001` | ? | 1 | 1 | — | Term names the consecrated hair as the symbol of dedication to God — its cutting away marking the inner rupture of conse |
| `4864-001` | ? | 5 | 2 | — | Term names the act of self-separation or dedication — the inner movement of consecrating oneself to God or, inversely, s |
| `4865-001` | ? | 5 | 2 | — | Term names the voluntary inner commitment of total dedication to God — the Nazirite vow as the outward form of an inner  |
| `4873-001` | ? | 10 | 2 | — | Term names the sanctuary as the space of divine presence — the place that calls forth and shapes the inner orientation o |
| `4874-001` | ? | 2 | 1 | — | Term names the Holy Place as the threshold of divine encounter — the approach to which demands inner readiness, solemnit |
| `4879-001` | ? | 1 | 1 | — | Term names the cult prostitute practice as the marker of inner spiritual adultery — the violation of covenantal fidelity |
| `4908-001` | ? | 8 | 2 | — | Term names the pit/grave as a moral and existential reality — the trap that wicked persons set for others falls back on  |
| `4910-001` | ? | 10 | 2 | — | Term names Gehenna as the eschatological consequence of inner moral failure — the destination that orients the inner lif |
| `4910-002` | ? | 2 | 1 | — | Term names Gehenna as the source of inner corruption — the hellish origin of moral destruction that corrupts from within |
| `4911-001` | ? | 5 | 2 | — | Term names Hades as the realm that threatens the soul — the place of the dead whose power over the inner person is overc |
| `504-001` | ? | 1 | 1 | — | Forceful demanding desire — the aggressive inner claim of hostile acquisition |
| `5098-001` | ? | 3 | 1 | — | Term names the inner orientation of prudent attention — the quality of discretion and measured regard that shapes how th |
| `5129-001` | ? | 7 | 1 | — | Digging/plotting as expression of inner malice and scheming |
| `5129-002` | ? | 1 | 1 | — | Opened ear as inner receptivity to God |
| `518-001` | ? | 1 | 1 | — | Term designates a skilled or instructive song as an act of worship — the inner devotional origin implied in the call to  |
| `5189-001` | ? | 1 | 1 | — | Urgent haste as expression of inner urgency or determination |
| `521-001` | ? | 8 | 2 | — | Term names inner discernment or good judgment — the person's capacity to perceive situations wisely and respond with app |
| `5212-001` | ? | 27 | 1 | — | Rock as divine epithet — God as the object of inner trust, refuge and security |
| `5212-002` | ? | 8 | 1 | — | Rock forgotten or abandoned — inner apostasy and unfaithfulness to God |
| `5213-001` | ? | 2 | 1 | — | Siege as context engaging inner trust and watchful orientation |
| `5272-001` | ? | 3 | 1 | — | Division of a community — relational fracture producing inner-social split |
| `5274-001` | ? | 7 | 1 | — | Inner division — competing loyalties and split allegiances |
| `5274-002` | ? | 2 | 1 | — | The measure of faith and calling as inner-assigned portion |
| `5275-001` | ? | 4 | 1 | — | Division against oneself — inner relational fracture and competing loyalties |
| `5282-001` | ? | 1 | 1 | — | The costliness of ransom — the impossibility of self-redemption and inner insufficiency before God |
| `545-001` | ? | 18 | 2 | — | Term names the darling or beloved as the cherished object of delight — the intimate address of love in the Song |
| `5627-001` | ? | 1 | 1 | — | Term names what covers the person in death and judgment — the inverted image of pride and pomp brought to humiliation be |
| `563-001` | ? | 1 | 1 | — | Term names love of dispute as an inner orientation toward rivalry and status — the disciples' competitive inner state at |
| `573-001` | ? | 2 | 1 | — | Term names the love of being first as an inner character disposition — the drive for primacy that refuses to acknowledge |
| `5732-001` | ? | 5 | 2 | — | Military force as communal subject of inner responses to battle — fear, courage, trust in God, inner orientation require |
| `5733-001` | ? | 20 | 2 | — | Relational community of belonging — gathered to or cut off from one's people as inner belonging, covenant faithfulness,  |
| `5739-001` | ? | 427 | 2 | — | Covenant community as object of God's relational love and moral claim — 'my people' as relational partner of the divine |
| `5739-002` | ? | 2 | 2 | — | Corporate inner spiritual condition of the people — rebellion, fear, trust, shame, orientation toward God |
| `5739-003` | ? | 1 | 1 | — | People as bearer of communal inner identity — shared moral-spiritual character defining who 'the people' are |
| `576-001` | ? | 1 | 1 | — | Term names the bosom as the seat of hidden inner knowledge — concealing transgression within oneself rather than confess |
| `577-001` | ? | 42 | 1 | — | Term names the inner parts as the seat of the indwelling divine presence — God in the midst of his people as the most in |
| `577-002` | ? | 42 | 1 | — | Term names the inner parts as the seat of moral character — what lies within the person as the source of their conduct |
| `577-003` | ? | 42 | 1 | — | Term names the inner parts as the location of renewal — God's new covenant work written within the person |
| `577-004` | ? | 42 | 1 | — | Term names the inner parts as the location of false prophets' lies — the source of deceptive claims about God |
| `5859-001` | ? | 5 | 2 | — | Term names manna as the instrument of God's inner-forming provision — humbling, testing, and teaching dependence on ever |
| `5866-001` | ? | 1 | 1 | — | Term names difficulty of interpretation as an inner condition of the hearer — spiritual dullness making what is teachabl |
| `590-001` | ? | 4 | 1 | — | Term names the seat of compassion — deep inner stirring of tender mercy toward another |
| `590-002` | ? | 4 | 1 | — | Term names the innermost affection — the deepest bond of love described as a physical inner stirring |
| `590-003` | ? | 6 | 1 | — | Term names the inward parts as the seat of Christian character qualities placed there by Christ |
| `5968-001` | ? | 1 | 1 | — | Term names the shining figure whose pride produces catastrophic inner-spiritual collapse — the inner-being of pride that |
| `6016-001` | ? | 1 | 1 | — | Term names the barely-surviving inner condition — the smoldering wick that God will not quench, disclosing his compassio |
| `602-001` | ? | 2 | 1 | — | Term names the inaugural inner renewal — the heart opened to new covenant access through Christ's blood |
| `6026-001` | ? | 12 | 2 | — | Term names the contribution that arises from the stirred heart and moving spirit — the inner-being act of giving to God  |
| `6026-002` | ? | 13 | 2 | — | Term names the contribution as the condition of divine blessing and the measure of faithfulness — giving to God as the i |
| `6028-001` | ? | 4 | 1 | — | Term names the lofty place of misdirected worship — the physical expression of Israel's inner spiritual prostitution, bu |
| `6034-001` | ? | 1 | 1 | — | Term names the uplifting of God — the rising of divine majesty before which nations scatter |
| `6042-001` | ? | 1 | 1 | — | Term names insolent fury — the inner-being condition of violent, arrogant rage exercised against the vulnerable, and cel |
| `6044-001` | ? | 24 | 2 | — | Term names the prophet as one specially oriented toward God — called to receive and declare his word, with an inner orie |
| `6044-002` | ? | 19 | 2 | — | Term names the prophet as the one who suffers for God's word — the inner-being posture of endurance under rejection and  |
| `6044-003` | ? | 27 | 2 | — | Term names the prophetic canon — the Law and the Prophets as the scriptural testimony that orients the inner life toward |
| `6047-001` | ? | 2 | 2 | — | Term names the prophetic written word as the inner-being lamp — the Scripture-canon of prophecy that illuminates the inn |
| `6048-001` | ? | 2 | 2 | — | Term names the prophetess — whether the authentic inner calling or the false claim to prophetic authority used for seduc |
| `605-001` | ? | 7 | 1 | — | Term names the Belial inner character — the worthless inner disposition of wickedness, plotting evil, contempt for justi |
| `6051-001` | ? | 6 | 1 | — | Title identifies a person whose identity and function is the mediation of divine inner-being communication — expressed i |
| `606-001` | ? | 1 | 1 | — | Term names the divining spirit — a false spiritual power inhabiting a person, counterfeiting prophetic inner capacity fo |
| `6065-001` | ? | 5 | 1 | — | Term names the native language as the vehicle through which inner understanding, recognition, and response are engaged — |
| `607-001` | ? | 2 | 1 | — | Term names the mistaken perception of a ghost producing inner terror — the fear arising from false spiritual perception |
| `6080-001` | ? | 3 | 1 | — | Term names flax as the object of misplaced inner desire (spiritual unfaithfulness) or as the material worked with willin |
| `6081-001` | ? | 6 | 1 | — | Term names the king's food as the occasion for inner moral decision — the choice not to defile oneself expresses inner c |
| `6082-001` | ? | 2 | 1 | — | Term names the wick or flax as a metaphor for the fragile or defeated person — in which divine compassion toward the vul |
| `6083-001` | ? | 1 | 1 | — | Term in Isa 3:17 appears in a judgment oracle bringing shame and exposure to the daughters of Zion — the inner-being dim |
| `610-001` | ? | 9 | 1 | — | Term names the medium as a false spiritual access point — the inner prohibition against seeking guidance through forbidd |
| `610-002` | ? | 7 | 1 | — | Term names the desperate consultation of a medium — inner act of seeking forbidden spiritual guidance driven by despair |
| `621-001` | ? | 7 | 2 | — | Ya.tsa as going-out of the soul or spirit |
| `621-002` | ? | 16 | 2 | — | Ya.tsa as going-forth of Gods word, law, righteousness, or judgment |
| `621-003` | ? | 14 | 2 | — | Ya.tsa as expression of inner states going outward |
| `621-004` | ? | 9 | 2 | — | Ya.tsa as divine going-out: God going forth in theophanic action |
| `6212-001` | ? | 1 | 1 | — | Term names the restraining authority as the social structure enforcing inner moral accountability — its absence leaves t |
| `6253-001` | ? | 37 | 2 | — | Term is used as a metaphor for the course and direction of a person's moral-spiritual life — feet as the expression of i |
| `6253-002` | ? | 6 | 1 | — | Term is used in relational acts of submission, supplication, or devotion — falling at someone's feet as an expression of |
| `6254-001` | ? | 1 | 1 | — | Term is used metaphorically for the inner capacity of perseverance under testing — the challenge of competing on foot as |
| `6275-001` | ? | 5 | 1 | — | Term names sorcery as a spiritual-relational practice — the use of occult means as a substitute for God, with specific i |
| `6276-001` | ? | 1 | 1 | — | Term names the sorcerer as a character type — one whose inner-spiritual orientation is defined by occult practice, and w |
| `6337-001` | ? | 2 | 1 | — | Term is used of God's inner anguish at handing over — disclosing the divine inner conflict between justice and compassio |
| `638-001` | ? | 1 | 1 | — | Term names the drying of inner vitality — the draining of the person's life-sap under the weight of divine conviction an |
| `639-001` | ? | 10 | 2 | — | Oikodomeō as inner-being edification through love and ministry |
| `639-002` | ? | 4 | 2 | — | Inner foundation — oikodomeō as figure for the inner-being basis of the person who hears and does God's word: the wise b |
| `639-003` | ? | 2 | 2 | — | Oikodomeō as the act by which persons are formed into God's spiritual house — the inner-being reality of being constitut |
| `642-001` | ? | 4 | 2 | — | Term names the inner vitality of youth and its passage — the vigor that fades to dust — and the inner shame associated w |
| `6426-001` | ? | 2 | 1 | — | Term names the act of being pierced or stricken in the inner being — used of the Servant's vicarious suffering for trans |
| `6427-001` | ? | 1 | 1 | — | Term names the wounded, stricken heart of the afflicted person — the inner-being condition of one who is poor, needy, an |
| `6428-001` | ? | 1 | 1 | — | Term names the wounded, stricken heart of the afflicted person — the inner-being condition of one who is poor, needy, an |
| `6433-001` | ? | 6 | 1 | — | Term names the condition of the wounded — the inner experience of pain, anguish, and distress expressed through groaning |
| `6434-001` | ? | 2 | 1 | — | Term is used as an image for the inner experience of grief — the mournful sound of the flute as a figure for the moaning |
| `6462-001` | ? | 1 | 1 | — | Term names the act of quarrelling — contentious striving; here named by its absence as a characteristic of the Servant's |
| `6463-001` | ? | 1 | 1 | — | Term names quarrelling about words — the inner disposition of contentious argument that produces no good and harms those |
| `65-001` | ? | 2 | 1 | — | Term names the anointing of the Spirit as inner knowledge and protection — the anointing that remains in the person and  |
| `6545-001` | ? | 9 | 2 | — | Witnessing as inner moral act and relational accountability — the bearing of witness (true or false) as an expression of |
| `6547-001` | ? | 14 | 2 | — | Divine testimonies as the object of inner devotion — the testimonies kept with the whole heart, delighted in, clung to,  |
| `655-001` | ? | 4 | 2 | — | Term names God's incomparable supremacy — in strength, in wealth, and in cosmic sovereignty — as the ground of inner awe |
| `6586-001` | ? | 2 | 1 | — | Opening the lips as expression of inner recklessness and the opening of the self to moral corruption |
| `66-001` | ? | 2 | 1 | ✓ | Term names the anointing of the Spirit as inner knowledge and protection — the anointing that remains in the person and  |
| `660-001` | ? | 1 | 1 | — | Term names the collapse of the inner capacity to stand — the inability to hold ground before God's holiness, under suffe |
| `6635-001` | ? | 8 | 1 | — | The only/beloved — preciousness of the unique as inner-being object of love and grief |
| `6635-002` | ? | 4 | 1 | — | The solitary/alone — inner-being condition of aloneness and its resolution |
| `6636-001` | ? | 2 | 1 | — | Inner-being joining — the soul/heart united in its orientation; refusing solidarity with the violent |
| `6670-001` | ? | 3 | 1 | — | Term names the divinely-imposed humiliation that continues until the inner transformation occurs — the recognition of Go |
| `6672-001` | ? | 1 | 1 | — | Term names the physical mark of divine humiliation — the beast-like degradation of a person whose inner pride brought th |
| `6672-002` | ? | 1 | 1 | — | The inner desire to understand divine mysteries — Daniel's deep drive to comprehend the meaning of the terrifying apocal |
| `6678-001` | ? | 1 | 1 | — | Term names philosophy as a human system of wisdom — an inner orientation toward knowledge that can become a deceptive su |
| `6679-001` | ? | 1 | 1 | — | Term names the philosopher as a person oriented toward human wisdom — whose inner pursuit of knowledge encounters the go |
| `6706-001` | ? | 2 | 1 | — | Term names the pit of destruction as existential peril — the state of being trapped or facing annihilation, from which G |
| `6707-001` | ? | 1 | 1 | — | Term names the pit as a metaphor for moral self-entrapment — the consequence of misleading others returns upon the one w |
| `6711-001` | ? | 4 | 1 | — | Term names prostration in worship misdirected toward idols — the physical expression of inner devotion wrongly oriented |
| `6725-001` | ? | 1 | 1 | — | Term names human works as objects of divine moral scrutiny — acts whose inner origins are known to God and subject to ju |
| `6726-001` | ? | 1 | 1 | — | Term names human works as resting in God's hand — linking inner character to outward acts under divine oversight |
| `6732-001` | ? | 4 | 1 | — | Term describes setting the Lord always before oneself — God as the stable centre of the inner life |
| `6732-002` | ? | 1 | 1 | — | Term describes the deliberate inner composing of oneself in affliction — inner regulation under extreme pressure |
| `6732-003` | ? | 1 | 1 | — | Term describes God's bestowal of splendour — the inner elevation of the person through divine grant |
| `6733-001` | ? | 1 | 1 | — | Term describes transformation of the mind into beast-likeness — the inner being as subject of radical punitive transform |
| `6755-001` | ? | 1 | 1 | — | Term names the plans of the heart — the inner-being act of purposeful arrangement belonging to the human person, whose o |
| `68-001` | ? | 2 | 1 | — | Term names the anointing of Jesus with the Holy Spirit as the equipping for inner authority and action — Spirit-receptio |
| `68-002` | ? | 1 | 1 | — | Term names the anointing of the believer by God as the ground of inner certainty — divine anointing as the establishing  |
| `6831-001` | ? | 1 | 1 | — | Term used in metaphor of divine sowing — God causing righteousness and praise to sprout; naming inner character qualitie |
| `6835-001` | ? | 71 | 2 | — | Term names betrayal — the inner moral act of handing over a trusted person to harm for treacherous or self-interested mo |
| `6835-002` | ? | 2 | 2 | — | Term names the passion of Christ — Jesus delivered over by the Father's eternal purpose to suffering and death |
| `6835-003` | ? | 1 | 1 | — | Term names Christ's voluntary self-giving — the inner act of love in which Christ gives himself over for others |
| `6835-004` | ? | 1 | 1 | — | Term names God's judicial delivering over — abandoning the rebellious to their own inner lusts and debased mind |
| `6835-005` | ? | 1 | 1 | — | Term names the apostolic handing on of tradition — the deliberate inner commitment to faithful transmission of received  |
| `6835-006` | ? | 1 | 1 | — | Term names the disciple's inner experience of being delivered up for Christ's sake — requiring trust in divine provision |
| `6835-007` | ? | 1 | 1 | — | Term names the entrustment of stewardship — the master's trust in servants and the servant's calling of faithful managem |
| `6835-008` | ? | 1 | 1 | — | Term names continual inner self-entrustment to God — trusting self-surrender to the one who judges justly under unjust s |
| `6835-009` | ? | 1 | 1 | — | Term names the inner moral act of giving oneself over to desire — the hardened self-abandonment to sensuality |
| `6835-010` | ? | 1 | 1 | — | Term names the divine delegation of all authority — the Father handing over all things to the Son |
| `6835-011` | ? | 1 | 1 | — | Term names disciplinary delivering over to Satan — aimed at the inner restoration and salvation of the spirit |
| `6835-012` | ? | 1 | 1 | — | Term names the heart's obedience to a received pattern of teaching — the inner act of self-surrender to a shaping tradit |
| `6836-001` | ? | 61 | 1 | — | Term in the water/Spirit contrast — water as the outward insufficient sign pointing to inner transformation of Spirit ba |
| `6836-002` | ? | 1 | 1 | — | Term as living water — metaphor for inner spiritual life permanently satisfying inner thirst, welling up to eternal life |
| `6836-003` | ? | 1 | 1 | — | Term in the context of inner cleansing — water as instrument of purification touching conscience and moral state |
| `6836-004` | ? | 1 | 1 | — | Term associated with inner anguish and desperate craving — the tormented soul's thirst for relief |
| `6836-005` | ? | 1 | 1 | — | Term in the act of washing hands as moral self-exculpation — the external act revealing inner conflict over guilt |
| `6836-006` | ? | 1 | 1 | — | Term as water of life in eschatological promise — eternal inner satisfaction and refreshment of the redeemed |
| `6836-007` | ? | 1 | 1 | — | Term as element of faith-testing — water on which the person either walks by trust or sinks through doubt |
| `6836-008` | ? | 1 | 1 | — | Term revealing inner disposition through contrast — water not given (indifference) vs. tears given (love) |
| `6839-001` | ? | 7 | 1 | — | Term names inner disposition of good giving — a father giving to a son who asks; and God's generous orientation toward t |
| `6839-002` | ? | 3 | 1 | — | Term names the giving that designates the betrayer — the final extension of grace in the moment before betrayal |
| `6842-001` | ? | 4 | 1 | — | Term names inner disposition of radical generosity — distributing to those in need from a transformed orientation toward |
| `6842-002` | ? | 1 | 1 | — | Term names surrender of power as expression of inner allegiance — handing authority to the object of devotion |
| `6848-001` | ? | 1 | 1 | — | Term names the impossibility of preceding God in giving — no person can give first so as to put God in debt; establishin |
| `6885-001` | ? | 1 | 1 | — | Epischuō as urgent insistence arising from inner conviction |
| `6888-001` | ? | 1 | 1 | — | Term names the constellations as objects of idolatrous worship — the astronomical host to which the inner person directs |
| `6893-001` | ? | 6 | 2 | — | Term names vastness in the inner-being dimension — the uncountable greatness of God's thoughts and works, and the overwh |
| `6895-001` | ? | 12 | 2 | — | Term names the posture of standing before God — in theophanic encounter, covenant service, and the vocation of the perso |
| `6895-002` | ? | 2 | 2 | — | Term names the standing of self-assertion, pride-display, or moral failure — the inner posture of those who position the |
| `6895-003` | ? | 6 | 2 | — | Term names Wisdom's or God's standing — the posture of authoritative address, appeal, and presence that calls the inner  |
| `6896-001` | ? | 3 | 2 | — | Ne.phaq as theophanic emergence that discloses divine sovereignty — the exit of the faithful from fire as God's protecti |
| `6900-001` | ? | 2 | 2 | — | Term names the tower as the expression of human inner pride and collective self-assertion — the Babel impulse to make a  |
| `6900-002` | ? | 2 | 2 | — | Term names God as the strong tower of refuge — the inner security that the righteous run to and find safety in |
| `6900-003` | ? | 5 | 2 | — | Term names the tower as the site of spiritual seeking and watchfulness — the built place from which the inner person loo |
| `6907-001` | ? | 1 | 1 | — | Term names the eschatological restoration of Zion's kingship — the return of God's sovereign rule as the inner hope of t |
| `6908-001` | ? | 1 | 1 | — | Term names the greatness of God's salvation and covenant love shown to his anointed — the towering scope of divine faith |
| `691-001` | ? | 1 | 1 | — | Exischuō as inner capacity to comprehend dimensions of divine love |
| `693-001` | ? | 1 | 1 | — | Enischuō as divine strengthening of the person in inner-being crisis |
| `6937-001` | ? | 7 | 2 | — | Ge.ve.ret as relational position disclosing inner-being orientations |
| `6938-001` | ? | 3 | 2 | — | Ge.vi.rah as position of authority whose inner-being exercise is morally judged |
| `6940-001` | ? | 2 | 1 | — | Authority as identity — ge.vir as the inner dignity and standing of the person reconstituted through the bestowal of lor |
| `6973-001` | ? | 2 | 1 | — | Term names the mountain as the image of God's ultimate, all-filling kingdom — the inner-being orientation toward the con |
| `6989-001` | ? | 16 | 2 | — | Term names the chosen place where God causes his name to dwell — the destination of inner pilgrimage and covenantal wors |
| `6989-002` | ? | 6 | 2 | — | Term names a theophanic place — the location where God reveals his presence, making it holy and establishing it as the g |
| `6989-003` | ? | 9 | 2 | — | Term names the place as the site of covenantal moral conditions — where dwelling in the land depends on inner obedience, |
| `6989-004` | ? | 3 | 2 | — | Term names the place in contexts of eschatological joy, restoration, and universal gathering — the future space of God's |
| `6996-001` | ? | 3 | 1 | — | Term names the scope of existence brought under divine judgment — every living thing, every breath — as the universal ho |
| `7-001` | ? | 2 | 1 | ✓ | Term names anointing as an expression of honour, love, and hospitality — the outer act of anointing as the vehicle of in |
| `7-002` | ? | 1 | 1 | ✓ | Term names anointing as the designated means of healing prayer — the outer act accompanying faith and intercession in th |
| `7002-001` | ? | 1 | 1 | — | Term names the rising of enemies as the constant occasion of the inner person's prayer and God's answering intervention |
| `7003-001` | ? | 1 | 1 | — | Term names the rising up against God as the object of the psalmist's inner moral resistance and appeal to divine justice |
| `7017-001` | ? | 6 | 2 | — | Ay.yal as figure of vital need — the deer's panting longing imaging the person's deep thirst for God (Ps 42:1), and the  |
| `7018-001` | ? | 8 | 2 | — | Divine-given sure-footedness and relational grace — ay.ya.lah as the figure of the doe imaging: God-given sure-footednes |
| `7054-001` | ? | 6 | 2 | — | Inner foundation — oikia as the figure for the inner-being basis of the person who hears and does (or fails to do) God's |
| `7054-002` | ? | 2 | 2 | — | Oikia as domain of spiritual captivity and power |
| `7054-003` | ? | 4 | 2 | — | Costly discipleship-surrender — oikia as the object whose surrender at God's call reveals and expresses the depth of inn |
| `7054-004` | ? | 8 | 2 | — | Watchfulness and moral readiness — oikia as the household context in which the master may return at any hour: the parabl |
| `7054-005` | ? | 4 | 2 | — | Oikia as dwelling of eternal belonging: Fathers house |
| `7056-001` | ? | 14 | 2 | — | Oikos as covenantal community identity: house of Israel/God |
| `7056-002` | ? | 13 | 2 | — | Oikos as household as unit of faith, salvation, and moral formation |
| `7057-001` | ? | 15 | 2 | — | Communal formation — oikodomē as the building up of the inner person and community through prophetic speech, love, and m |
| `7058-001` | ? | 3 | 2 | — | Oikoumenē as scope of spiritual conflict and deception |
| `7059-001` | ? | 10 | 2 | — | Parabolic disclosure of inner qualities of the master-figure — oikodespotēs figuring the inner qualities of the househol |
| `7060-001` | ? | 8 | 2 | — | Oikonomos figuring inner-being qualities of faithfulness and wisdom |
| `7061-001` | ? | 6 | 2 | — | Oikeō as indwelling of sin or Spirit within the inner person |
| `7062-001` | ? | 8 | 2 | — | Oikia (household) as collective unit of faith, division, or moral vulnerability |
| `7063-001` | ? | 6 | 2 | — | Oikonomia as stewardship entrusted by God: inner-being sense of calling |
| `7065-001` | ? | 5 | 2 | — | Enoikeō as inhabitation of formative divine reality within the inner person |
| `7070-001` | ? | 1 | 1 | — | Oikētērion as heavenly dwelling as object of inner longing and hope |
| `7072-001` | ? | 1 | 1 | — | Enkatoikeō as dwelling context producing ongoing inner torment |
| `7079-001` | ? | 1 | 1 | — | Sunoikeō as marital cohabitation calling for inner-being virtues |
| `7080-001` | ? | 1 | 1 | — | Sunoikodomeō as spiritual incorporation of person into Gods dwelling |
| `7093-001` | ? | 1 | 1 | — | Term names the act of going in to prayer — Daniel entering his house to kneel and give thanks before God despite royal p |
| `7096-001` | ? | 1 | 1 | — | Term names the refining furnace as the image of God's word's absolute moral purity — purified beyond all dross |
| `7113-001` | ? | 4 | 2 | — | Term names the maiden as a participant in and witness to the inner life of love, worship, and divine mystery — from the  |
| `7151-001` | ? | 1 | 1 | — | Term names the inner act of swerving toward the proud and the lie — the misdirection of trust that the blessed person av |
| `7162-001` | ? | 10 | 2 | — | Term names prey in its inner-being dimension — the predatory inner character of unjust leaders and oppressors, God's fie |
| `7163-001` | ? | 3 | 2 | — | Term names the torn animal as the boundary that tests inner integrity — the person who refuses defilement, bears losses  |
| `7164-001` | ? | 1 | 1 | — | Term names the fresh-plucked olive leaf as the sign of renewed hope — the communicative act that produces inner recognit |
| `7186-001` | ? | 1 | 1 | — | Term names the universal drawing of people toward Jesus from every quarter — the inner orientation of seeking that comes |
| `724-001` | ? | 8 | 2 | — | Term names the oath as an act of inner moral commitment — the binding of the will through solemn promise before God |
| `724-002` | ? | 3 | 2 | — | Term names the oath sworn by God — the divine commitment of character expressed as a binding promise that grounds covena |
| `729-001` | ? | 2 | 1 | — | Term is used as the vehicle of a maternal metaphor grounding divine compassion in the image of carrying from the womb —  |
| `7328-001` | ? | 6 | 1 | — | Term names the object whose worship or refusal becomes the direct test of a person's inner allegiance and courage before |
| `7352-001` | ? | 1 | 1 | — | Term is used of the divine name as supreme over all named powers |
| `7352-002` | ? | 3 | 1 | — | Term denotes the act of invoking or naming the Lord's name, expressing an inner orientation of faith or moral commitment |
| `7352-003` | ? | 2 | 1 | — | Term is used of bearing or naming an identity, with the name revealing or contrasting with the inner moral state of the  |
| `7352-004` | ? | 4 | 2 | — | Term denotes a theologically weighted naming act — Jesus names individuals or groups, conferring identity and role |
| `740-001` | ? | 10 | 2 | — | Term names the state of consecration itself — the dedicated condition of the person who has set themselves apart to God, |
| `7407-001` | ? | 27 | 1 | — | Term names the intimate dignity of the person — the nakedness that the law protects from sexual violation and that defin |
| `7407-002` | ? | 3 | 1 | — | Term names nakedness as the person's vulnerability that God covers in covenantal love — the act of covering as the found |
| `7407-003` | ? | 7 | 1 | — | Term names nakedness as the shame and exposure that follows spiritual unfaithfulness — judgment as uncovering |
| `7407-004` | ? | 3 | 1 | — | Term names the covering required for dignity in the divine presence — nakedness that must not be exposed before the holy |
| `7408-001` | ? | 1 | 1 | — | Term names the razor as the instrument of divine shaming — used to strip the honour and dignity of the person in judgmen |
| `7408-002` | ? | 2 | 1 | — | Term names the razor as what the consecrated person avoids — its avoidance marking the person's inner dedication to God |
| `7408-003` | ? | 1 | 1 | — | Term frames a comparison that characterises the inner disposition of deceit — the tongue like a razor, plotting destruct |
| `7409-001` | ? | 2 | 1 | — | Term names the originary nakedness and bareness of the person — utter vulnerability before God's care intervenes |
| `7409-002` | ? | 3 | 1 | — | Term names nakedness as the shame and exposure that judgment brings upon spiritual unfaithfulness |
| `7410-001` | ? | 1 | 1 | — | Term names nakedness exposed in divine judgment — the public shame and disgrace of the person laid bare before others |
| `7414-001` | ? | 3 | 1 | — | Term names the inner experience of shame, fear, and self-concealment that nakedness brings — the person's first response |
| `7414-002` | ? | 2 | 1 | — | Term describes the person's originary condition of naked vulnerability before God acts in care — helpless, uncovered, an |
| `7414-003` | ? | 2 | 1 | — | Term names the nakedness of the person in need that the just person is called to cover — an inner-being imperative of co |
| `7414-004` | ? | 4 | 1 | — | Term names nakedness as the state of covenant judgment and shame — exposure as the consequence of spiritual unfaithfulne |
| `7416-001` | ? | 1 | 1 | — | Term names nakedness deliberately exposed through exploitation — the stripping of another's dignity revealing the perpet |
| `7417-001` | ? | 1 | 1 | — | Term names physical nakedness as a condition of the vulnerable other whose clothing becomes an act of inner compassion |
| `7420-001` | ? | 1 | 1 | — | Term names the spiritual nakedness of the person as a state of inner shame that requires the covering only Christ can pr |
| `7420-002` | ? | 2 | 1 | — | Term names physical nakedness as a condition of extreme hardship and inner vulnerability — that which cannot separate th |
| `7421-001` | ? | 1 | 1 | — | Term names physical nakedness/deprivation as a condition of apostolic vulnerability — the person's inner orientation of  |
| `7423-001` | ? | 24 | 2 | — | Death as end/consequence of a moral path — wickedness leads to death; choosing life vs death |
| `7423-002` | ? | 43 | 2 | — | Death as power/threat/reality the person faces, fears, chooses, or is delivered from |
| `7423-003` | ? | 5 | 2 | — | God's sovereignty over death as ground of redemption and inner-being hope |
| `7423-004` | ? | 3 | 2 | — | The dead and inner-being capacities — those who no longer praise, remember, or are remembered |
| `7427-001` | ? | 28 | 2 | — | Death as spiritual/moral condition — separation from God, consequence of sin |
| `7427-002` | ? | 9 | 1 | — | Death as power/threat that dominates or enslaves through fear |
| `7427-003` | ? | 7 | 2 | — | Believer's inner identification with Christ's death as transformative reality |
| `7427-004` | ? | 5 | 2 | — | Faithful inner-being orientation toward death — perseverance, defiance, hope |
| `7427-005` | ? | 2 | 1 | — | Death as measure of extreme inner suffering — soul sorrowful even to death |
| `7429-001` | ? | 4 | 2 | — | Mortal body as site of inner-being orientation, longing, and moral struggle |
| `7432-001` | ? | 13 | 1 | — | Term names darkness as the inner-spiritual domain the person inhabits, is rescued from, or identifies with — their funda |
| `7432-002` | ? | 5 | 1 | — | Term names darkness as the moral domain of works and powers the person either participates in or is called to renounce |
| `7432-003` | ? | 3 | 1 | — | Term names the darkness of the inner life — hidden purposes, corrupted inner light, self-deception about one's inner sta |
| `7432-004` | ? | 5 | 1 | — | Term names the outer darkness of eschatological judgment — the ultimate inner-being consequence of exclusion from God |
| `7433-001` | ? | 8 | 1 | — | Term names darkness as the inner condition of spiritual alienation — the state of the person who hates, does not know wh |
| `7433-002` | ? | 2 | 1 | — | Term names the darkness of concealment — the inner life hidden in secret, which will be brought to light |
| `7434-001` | ? | 3 | 1 | — | Term describes the darkening of inner capacities — understanding, heart, and eyes — as the consequence of wilful rejecti |
| `7435-001` | ? | 3 | 1 | — | Term names the inner darkness that fills the person when their inner orientation is corrupted — the whole inner life dar |
| `7449-001` | ? | 2 | 1 | — | Term names the birth-moment of inner emergence — the person breaking forth from constraint into new life or new capacity |
| `747-001` | ? | 10 | 2 | — | Term names the pit/Sheol as the threat to the soul — the place of death from which the inner person cries out to God for |
| `7493-001` | ? | 36 | 1 | — | Spiritual receptivity and its refusal — o.zen as the inner faculty through which divine word is received, the heart open |
| `7493-002` | ? | 22 | 1 | — | The discerning ear — o.zen as the inner organ that tests, evaluates and seeks wisdom |
| `7493-003` | ? | 25 | 1 | — | Prayer addressing God's ear — o.zen as the inner cry of the soul urgently seeking divine attention and response |
| `7493-004` | ? | 3 | 1 | — | Wilful closing of the ear — o.zen as the inner organ deliberately shut against evil or against God |
| `7493-005` | ? | 3 | 1 | — | Ears tingling — o.zen as the somatic-inner receptor of divine judgment producing inner-physical response of shock |
| `7494-001` | ? | 6 | 1 | — | Hearing that opens into inner transformation — o.zen as the event of communal hearing that triggers inner covenant commi |
| `7495-001` | ? | 6 | 1 | — | Revelation received and inner courage kindled — o.zen as the channel of divine disclosure that produces inner courage, p |
| `7501-001` | ? | 3 | 1 | — | Spiritual receptivity — echō as indicator of the inner capacity to hear and respond to divine word |
| `7501-002` | ? | 12 | 1 | — | Possession of spiritual endowments — echō as the condition of having or lacking love, faith and the Spirit as inner real |
| `7501-003` | ? | 8 | 1 | — | Emotive inner states — echō as carrier of compassion, fear, joy and zeal as active inner movements |
| `7501-004` | ? | 2 | 1 | — | Inner deficit and corruption — echō as indicator of rootlessness, debased mind and inner spiritual lack |
| `7501-005` | ? | 3 | 1 | — | Peace, hope and access — echō as the condition of holding peace, hope and relational access to God as inner states |
| `7501-006` | ? | 5 | 1 | — | Inner cognitive and moral faculties — echō as the condition of possessing or lacking knowledge, conscience and inner dis |
| `7501-007` | ? | 10 | 1 | — | Will, motivation and inner orientation — echō as the condition of the volitional and motivational inner life |
| `7510-001` | ? | 4 | 1 | — | Hearing producing inner recognition, distress or obedience — she.ma as the act of receiving a report that moves the inne |
| `7526-001` | ? | 1 | 1 | — | Inner attentiveness called for — enōtizomai as the summons to receptive inner attention to proclaimed word |
| `7527-001` | ? | 15 | 1 | — | Spiritual receptivity — ous as the inner organ of capacity to hear and respond to divine word (the hearing formula) |
| `7527-002` | ? | 6 | 1 | — | Inner hardness and resistance — ous as the organ of spiritual receptivity closed, dulled or uncircumcised by inner rebel |
| `7527-003` | ? | 3 | 1 | — | Blessed receptivity and deep reception — ous as the open inner organ through which grace and divine direction enter |
| `7545-001` | ? | 1 | 1 | — | interpersonal conflict and the attempt to restore relational wholeness through appeal to shared identity |
| `7557-001` | ? | 2 | 1 | — | the crushed/contrite inner spirit — brokenness before God drawing divine nearness |
| `7565-001` | ? | 5 | 1 | — | idolatrous or wrongful relational alliance as volitional inner joining |
| `7565-002` | ? | 2 | 1 | — | occult charming as forbidden inner-spiritual practice |
| `7565-003` | ? | 1 | 1 | — | joining words as inner rhetorical expression |
| `7565-004` | ? | 1 | 1 | — | communal participation as ground of inner hope |
| `7568-001` | ? | 2 | 1 | — | disciplinary wound as instrument of inner moral purification |
| `7568-002` | ? | 2 | 1 | — | redemptive wound producing inner healing and restoration |
| `7569-001` | ? | 2 | 1 | — | occult charming as forbidden spiritual practice |
| `7569-002` | ? | 2 | 1 | — | reliance on occult power as spiritual misdirection and arrogance |
| `7574-001` | ? | 1 | 1 | — | keeping company with evildoers as moral alignment |
| `7576-001` | ? | 1 | 1 | — | covenantal companionship as the relational bond that faithlessness violates |
| `761-001` | ? | 12 | 1 | — | The prophet as vessel of the divine word — inner-being vocation |
| `761-002` | ? | 26 | 1 | — | The false prophet — inner-being failure of self-generated speech, greed, and deception |
| `761-003` | ? | 10 | 1 | — | Rejection of the prophet — Israel's inner-being resistance to God's claim through prophetic calling |
| `767-001` | ? | 1 | 1 | — | Inner commitment under solemn self-curse — the cutting ritual as the enactment of the will's binding to covenant terms,  |
| `767-002` | ? | 4 | 1 | — | Cutting as moral consequence — cutting off of wickedness |
| `772-001` | ? | 8 | 1 | — | Oath as solemn inner-being binding commitment |
| `772-002` | ? | 6 | 1 | — | Covenant curse as consequence of inner moral failure |
| `791-001` | ? | 2 | 1 | — | Blinding of inner perception — the hardening of heart and eye against understanding |
| `799-001` | ? | 2 | 1 | — | Delight and its loss — where delicacies represent the satisfaction of the inner person |
| `801-001` | ? | 1 | 1 | — | The name Hephzibah — divine delight encoded as identity |
| `82-001` | ? | 2 | 1 | ✓ | Term names the inner heat of anger as a smoldering thermal process — the self-sustaining build of inner fury toward erup |
| `821-001` | ? | 1 | 1 | — | Willing inner disposition in service — every willing person offering skill to God's work |
| `822-001` | ? | 6 | 1 | — | Division within a community — inner relational fracture over allegiance, identity, and unity of mind |
| `824-001` | ? | 4 | 1 | — | Redemption as divine provision and ground of inner hope |
| `826-001` | ? | 1 | 1 | — | Division as the inner relational rupture produced by ultimate allegiance |
| `827-001` | ? | 1 | 1 | — | Schismatic disposition — inner character producing division |
| `828-001` | ? | 1 | 1 | — | Division of soul and spirit — the word of God penetrating the innermost person |
| `830-001` | ? | 3 | 1 | — | Boasting in human might — the inner moral failure of self-reliance and pride |
| `830-002` | ? | 7 | 1 | — | The Lord as mighty warrior — inner confidence and boldness grounded in divine presence |
| `830-003` | ? | 4 | 1 | — | The heart of warriors overcome — inner terror and collapse under God's judgement |
| `85-001` | ? | 10 | 2 | ✓ | Term names length of days as covenantal gift and inner aspiration — the divine promise of a long life as the fruit of wi |
| `858-001` | ? | 11 | 2 | — | Term names the theophanic appearing of God — the divine self-disclosure constituting the moment of encounter, producing  |
| `858-002` | ? | 13 | 2 | — | Term names divine seeing of the inner moral life — God's perception penetrates to the thoughts, intentions, or state of  |
| `858-003` | ? | 32 | 2 | — | Term names seeing that triggers an inner response — the visual act discloses or activates an inner state: desire, love,  |
| `858-004` | ? | 9 | 2 | — | Term names spiritual blindness — seeing without inner perception; the deliberate or divinely-imposed failure of inner co |
| `858-005` | ? | 6 | 2 | — | Term names the moral discipline of deliberate not-seeing — choosing not to witness evil or another's shame, as an act of |
| `858-006` | ? | 16 | 2 | — | Term names seeing God or divine glory as the transforming inner-being encounter — the apex of inner-being experience: pr |
| `858-007` | ? | 14 | 2 | — | Term names seeing as an act of faith — looking in trust, watching in expectation, or receiving divine promise or provisi |
| `858-008` | ? | 11 | 2 | — | Term names prophetic or Spirit-enabled seeing — visionary perception of what is not physically present or not yet, given |
| `858-009` | ? | 20 | 2 | — | Term names seeing as moral witness and inner obligation — seeing need, suffering, or moral failure creates an inner obli |
| `858-010` | ? | 33 | 2 | — | Term names divine or human seeing of suffering or pride as the basis for response — seeing affliction moves God to compa |
| `87-001` | ? | 9 | 1 | — | Term names the guilt offering as the divinely instituted response to guilt — the atonement mechanism that addresses the  |
| `872-001` | ? | 37 | 2 | — | Term names divine giving as the expression of covenant faithfulness — God's giving of land, promise, and blessing as the |
| `872-002` | ? | 30 | 2 | — | Term names divine giving as the expression of inner love and compassion — God gives in direct response to inner need, lo |
| `872-003` | ? | 6 | 2 | — | Term names the giving of inner-being capacities — wisdom, spirit, understanding, songs, and strength given directly to t |
| `872-004` | ? | 11 | 2 | — | Term names divine giving as moral judgement — God gives into the hand of enemies or destruction as the moral expression  |
| `872-005` | ? | 19 | 2 | — | Term names the inner act of human giving — self-giving, sacrificial giving, votive giving, or giving as the expression o |
| `872-006` | ? | 6 | 2 | — | Term names the giving or withholding of glory and honour — the inner-being act of ascribing worth to God, or divine with |
| `872-007` | ? | 11 | 2 | — | Term names eschatological or restorative giving — God gives to transform inner conditions: ashes to beauty, mourning to  |
| `916-001` | ? | 3 | 1 | — | Term names the figure or imagination as an inner mental content — the inner picture the person holds of reality, whether |
| `929-001` | ? | 1 | 1 | — | Term names a metaphorical covering of moral reproach — the public declaration of innocence and vindication |
| `929-002` | ? | 3 | 1 | — | Term names the absence of covering as the condition of inner vulnerability and exposure — of the poor, and of the realm  |
| `929-003` | ? | 2 | 1 | — | Term frames covering as divine response to vulnerability and divine expression of grief — God's compassion for the expos |
| `937-001` | ? | 10 | 2 | — | Term names the inner act of intercession — entreaty or pleading on behalf of another before God, or the absence of such  |
| `937-002` | ? | 1 | 1 | — | Term names the substitutionary laying of iniquity on another — the moral burden of the many placed on the one who bears  |
| `953-001` | ? | 16 | 2 | — | Inner moral condition characteristic of humanity — evil inclination of the heart, capacity for wickedness |
| `953-002` | ? | 11 | 2 | — | Human frailty and dependence before God — inner limitation and creaturely orientation defining adam |
| `953-003` | ? | 11 | 2 | — | Humanity as object of God's purposeful action — created in God's image, known, called to reflect divine character |
| `953-004` | ? | 10 | 2 | — | Specific inner dispositions of individual persons as representative human qualities — meekness, wisdom, contrition, humi |
| `966-001` | ? | 2 | 2 | ✓ | Rushing, yearning intensity of the soul's inner longing — deep craving driving the inner being toward what it desires |
| `970-001` | ? | 1 | 1 | — | Term names the craving or lust for tribute as an inner disposition of greed that God opposes |
| `971-001` | ? | 1 | 1 | — | Term names animal-like instinctual lust that cannot be restrained — used as a metaphor for Israel's insatiable craving f |
| `976-001` | ? | 1 | 1 | — | Term names the call to inner meditation and musical reflection at a moment of divine action — a pause for the heart to r |
| `979-001` | ? | 9 | 2 | — | Term names the inner act of remembrance — the capacity by which God, persons, or deeds are held in living consciousness; |
| `979-002` | ? | 15 | 2 | — | Term names the memorial as moral legacy — the lasting presence or extinction of a person's name in communal memory, carr |
| `980-001` | ? | 3 | 2 | — | Term names the memorial — the preserved memory of love and prayer held before God and in the community, ensuring that ac |
| `982-001` | ? | 22 | 2 | — | Term names the mercy seat as the physical locus of divine-human encounter — the point where God's presence meets human r |

---

## §7. Summary

- **Clusters with active VCGs:** 48
- **Total active VCGs:** 2849
- **Singleton VCGs (1 verse):** 528 (18.5% of all VCGs)
- **VCGs cited in cluster_finding:** 379 of 2849 (13%)
- **Avg Jaccard similarity** VCG-desc vs sub-group-desc: 0.02
- **Cross-cluster description tokens (≥3 clusters):** 2202

**For the v3_0 decision:** §2.1 (singleton count), §4 (citation rate), and §3 (Jaccard) are the three direct rent-tests. A low citation rate combined with a high singleton fraction and high Jaccard would argue strongly for dropping the layer. A high citation rate with low singleton fraction would argue for keeping it.