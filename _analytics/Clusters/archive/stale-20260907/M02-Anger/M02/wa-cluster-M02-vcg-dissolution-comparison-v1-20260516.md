# M02 Anger, Wrath and Indignation — VCG dissolution comparison (v2)

**Generated:** 2026-05-16T13:13:16Z  
**Cluster:** `M02` (Anger) · status=Analysis - In Progress · version=v6  
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §11 (Phase 8)  
**Snapshot:** 2026-05-16T13:13:02Z — 695 vc rows  
**Boundary:** new VCGs = id ≥ 3762; inherited = id < 3762  
**Source:** `database/bible_research.db`  

**Scope:** for each inherited (pre-Phase-7) VCG linked to this cluster's terms, this report shows where its member verses landed under the new (Phase 7) VCG structure. **Researcher reviews and approves dissolution before CC executes the soft-delete directive.**

---

## 1. Header summary

- Inherited VCGs: **68**
- New VCGs: **25**
- Active vc rows (routed to new VCGs): **641**
- Active vc rows (group_id IS NULL — needs Phase 7 follow-up): **0**
- Set-aside vc rows (is_relevant=0): **54**
- Soft-deleted vc rows (delete_flagged=1): **0**

### Disposition counts

| Disposition | Count | Meaning |
|---|---:|---|
| `KEEP-EQUIVALENT` | 3 | Old VCG maps 1:1 to a single new VCG that has no other source. |
| `KEEP-EQUIVALENT-OF-MERGE` | 54 | Old VCG maps to a single new VCG, but that new VCG also receives members from other old VCGs (consolidation). |
| `SPLIT` | 11 | Old VCG's members distributed across 2+ new VCGs. |
| `OBSOLETE` | 0 | Old VCG's members are all set-aside or soft-deleted; no active routed members. |
| `UNROUTED` | 0 | Old VCG has ≥1 member still active and unrouted (needs Phase 7 follow-up before dissolution). |

**Dissolution gate:** inherited VCGs with `UNROUTED` disposition retain `delete_flagged=0` until their remaining active members are routed. All other inherited VCGs are eligible for soft-delete on researcher approval.

---

## 2. Consolidation map (new VCGs that absorbed multiple old VCGs)

These new VCGs each draw their members from 2+ old VCGs. This is the most consequential change in structure — review carefully.

| New VCG | # source old VCGs | Source old VCG codes (id) |
|---|---:|---|
| `M02-A-VCG-01` (id=3762) | 2 | `1405-001` (id=139), `256-001` (id=2578) |
| `M02-A-VCG-03` (id=3764) | 4 | `37-001` (id=21), `223-001` (id=115), `223-002` (id=116), `227-001` (id=118) |
| `M02-A-VCG-04` (id=3765) | 4 | `37-002` (id=22), `37-003` (id=23), `222-001` (id=113), `222-002` (id=114) |
| `M02-B-VCG-01` (id=3767) | 3 | `139-002` (id=63), `140-001` (id=65), `140-002` (id=66) |
| `M02-B-VCG-02` (id=3768) | 7 | `38-001` (id=24), `38-002` (id=25), `38-003` (id=26), `139-001` (id=62), `139-002` (id=63), `254-001` (id=2568), `255-001` (id=2569) |
| `M02-B-VCG-03` (id=3769) | 4 | `135-001` (id=57), `136-002` (id=59), `139-001` (id=62), `6801-001` (id=2571) |
| `M02-B-VCG-04` (id=3770) | 5 | `38-001` (id=24), `136-001` (id=58), `139-001` (id=62), `1552-001` (id=146), `921-001` (id=1312) |
| `M02-B-VCG-05` (id=3771) | 4 | `136-002` (id=59), `136-003` (id=60), `139-003` (id=64), `140-002` (id=66) |
| `M02-B-VCG-06` (id=3772) | 3 | `136-001` (id=58), `139-002` (id=63), `140-001` (id=65) |
| `M02-BOUNDARY-VCG-01` (id=3774) | 10 | `151-001` (id=72), `151-002` (id=73), `151-003` (id=74), `4556-001` (id=166), `4556-002` (id=167), `205-001` (id=767), `234-001` (id=787), `234-002` (id=788), `2747-001` (id=841), `1091-001` (id=2068) |
| `M02-C-VCG-01` (id=3775) | 4 | `114-001` (id=52), `114-002` (id=53), `115-001` (id=54), `115-002` (id=55) |
| `M02-C-VCG-02` (id=3776) | 3 | `1410-001` (id=140), `1411-001` (id=141), `922-001` (id=1311) |
| `M02-D-VCG-02` (id=3779) | 4 | `40-001` (id=29), `149-002` (id=70), `149-003` (id=71), `177-001` (id=97) |
| `M02-D-VCG-03` (id=3780) | 3 | `39-001` (id=27), `39-002` (id=28), `1141-001` (id=2211) |
| `M02-E-VCG-01` (id=3782) | 2 | `2528-001` (id=858), `2756-001` (id=862) |
| `M02-E-VCG-02` (id=3783) | 3 | `341-002` (id=856), `341-003` (id=857), `344-003` (id=861) |
| `M02-E-VCG-03` (id=3784) | 4 | `341-001` (id=855), `341-002` (id=856), `341-003` (id=857), `344-002` (id=860) |
| `M02-E-VCG-04` (id=3785) | 3 | `341-001` (id=855), `341-003` (id=857), `344-001` (id=859) |
| `M02-F-VCG-01` (id=3786) | 4 | `1431-001` (id=145), `560-001` (id=1570), `1139-001` (id=2206), `6464-001` (id=2208) |
| `M02-F-VCG-02` (id=3787) | 2 | `1140-001` (id=2209), `6467-001` (id=2210) |

---

## 3. Per-inherited-VCG detail

### Old VCG `136-001` (id=58) — `SPLIT`

**Old description:** "Term names divine wrath as consuming inner fire — the heat of God's anger poured out in judgment, spending itself completely"

**Old member verses:** 8 total
  Sample: Eze 5:13 (H2534), Eze 6:12 (H2534), Eze 7:8 (H2534), Eze 13:13 (H2534), Eze 20:8 (H2534), ... +3 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 7 | active → new | `M02-B-VCG-06` (id=3772) | God's burning inner rage through sustained imagery of pouring, spending, and releasing — a concentrated intensity that b |
| 1 | active → new | `M02-B-VCG-04` (id=3770) | Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from |

---

### Old VCG `136-002` (id=59) — `SPLIT`

**Old description:** 'Term names anger as the inner state that transforms countenance and drives extreme action — human fury at its most visible and disruptive'

**Old member verses:** 3 total
  Sample: Est 1:12 (H2534), Psa 6:1 (H2534), Psa 38:1 (H2534)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-B-VCG-05` (id=3771) | Anger as an inner state present but requiring management and restraint — either by God whose compassion holds back wrath |
| 1 | active → new | `M02-B-VCG-03` (id=3769) | Anger as a force that floods and fills the inner person — welling to full capacity, taking possession, displacing other  |

---

### Old VCG `139-001` (id=62) — `SPLIT`

**Old description:** "Term names the kindling of inner anger as the first act of moral rebellion — Cain's anger at divine rejection as the origin-point of the anger characteristic in Scripture"

**Old member verses:** 9 total
  Sample: Gen 4:5 (H2734), Gen 4:6 (H2734), Gen 31:36 (H2734), Num 22:27 (H2734), 1Sa 17:28 (H2734), ... +4 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M02-B-VCG-02` (id=3768) | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |
| 2 | active → new | `M02-B-VCG-03` (id=3769) | Anger as a force that floods and fills the inner person — welling to full capacity, taking possession, displacing other  |
| 1 | active → new | `M02-B-VCG-04` (id=3770) | Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from |

---

### Old VCG `139-002` (id=63) — `SPLIT`

**Old description:** "Term names divine anger as the inner response to Israel's repeated covenant violation — the burning of God's wrath in the moment of particular transgression"

**Old member verses:** 9 total
  Sample: Exo 32:10 (H2734), Num 11:1 (H2734), Num 11:10 (H2734), Num 12:9 (H2734), Num 25:3 (H2734), ... +4 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 7 | active → new | `M02-B-VCG-01` (id=3767) | God's burning inner heat directed against Israel's persistent covenant violation — the disciplinary fire that kindles at |
| 1 | active → new | `M02-B-VCG-06` (id=3772) | God's burning inner rage through sustained imagery of pouring, spending, and releasing — a concentrated intensity that b |
| 1 | active → new | `M02-B-VCG-02` (id=3768) | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |

---

### Old VCG `140-001` (id=65) — `SPLIT`

**Old description:** "Term names the burning intensity of divine wrath at its maximum — fierce anger as the pinnacle of God's response to covenant violation, carrying cosmic consequences"

**Old member verses:** 14 total
  Sample: Jer 4:8 (H2740), Num 25:4 (H2740), Deu 13:17 (H2740), Jos 7:26 (H2740), 1Sa 28:18 (H2740), ... +9 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 10 | active → new | `M02-B-VCG-01` (id=3767) | God's burning inner heat directed against Israel's persistent covenant violation — the disciplinary fire that kindles at |
| 4 | active → new | `M02-B-VCG-06` (id=3772) | God's burning inner rage through sustained imagery of pouring, spending, and releasing — a concentrated intensity that b |

---

### Old VCG `140-002` (id=66) — `SPLIT`

**Old description:** 'Term names human burning anger as the inner response to perceived injustice or affront — the fierce heat of personal wrath that drives consequential action'

**Old member verses:** 5 total
  Sample: 2Ch 28:11 (H2740), Exo 32:12 (H2740), Num 32:14 (H2740), 2Ch 28:13 (H2740), 2Ch 30:8 (H2740)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-B-VCG-01` (id=3767) | God's burning inner heat directed against Israel's persistent covenant violation — the disciplinary fire that kindles at |
| 1 | active → new | `M02-B-VCG-05` (id=3771) | Anger as an inner state present but requiring management and restraint — either by God whose compassion holds back wrath |

---

### Old VCG `341-001` (id=855) — `SPLIT`

**Old description:** "Human jealousy and envy — resentment of another's blessing or standing"

**Old member verses:** 13 total
  Sample: Gen 30:1 (H7065), Gen 26:14 (H7065), Gen 37:11 (H7065), Psa 37:1 (H7065), Psa 73:3 (H7065), ... +8 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 12 | active → new | `M02-E-VCG-04` (id=3785) | Jealousy in human persons directed at others — possessiveness, comparison-based resentment, covetous envy at another's a |
| 1 | active → new | `M02-E-VCG-03` (id=3784) | Human jealousy directed toward God — consuming zeal for his honor that identifies persons with his cause. Elijah, Phineh |

---

### Old VCG `341-002` (id=856) — `SPLIT`

**Old description:** 'Zeal for God — passionate inner devotion expressed as jealous advocacy'

**Old member verses:** 8 total
  Sample: 1Ki 19:10 (H7065), 1Ki 19:14 (H7065), Num 25:11 (H7065), Num 25:13 (H7065), Eze 39:25 (H7065), ... +3 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-E-VCG-03` (id=3784) | Human jealousy directed toward God — consuming zeal for his honor that identifies persons with his cause. Elijah, Phineh |
| 4 | active → new | `M02-E-VCG-02` (id=3783) | God's jealousy expressed as fierce protective passion for his people, city, land, and name — firing in their defense and |

---

### Old VCG `341-003` (id=857) — `SPLIT`

**Old description:** "Provoking God to jealousy — Israel's idolatry as inner spiritual betrayal"

**Old member verses:** 8 total
  Sample: Deu 32:21 (H7065), Deu 32:16 (H7065), 1Ki 14:22 (H7065), Psa 78:58 (H7065), Eze 8:3 (H7065), ... +3 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 5 | active → new | `M02-E-VCG-02` (id=3783) | God's jealousy expressed as fierce protective passion for his people, city, land, and name — firing in their defense and |
| 2 | active → new | `M02-E-VCG-04` (id=3785) | Jealousy in human persons directed at others — possessiveness, comparison-based resentment, covetous envy at another's a |
| 1 | active → new | `M02-E-VCG-03` (id=3784) | Human jealousy directed toward God — consuming zeal for his honor that identifies persons with his cause. Elijah, Phineh |

---

### Old VCG `37-001` (id=21) — `SPLIT`

**Old description:** 'Term names divine wrath as the revealed inner response to human unrighteousness and ungodliness — anger as the consistent inner orientation of God toward sin'

**Old member verses:** 3 total
  Sample: Rom 1:18 (G3709), Joh 3:36 (G3709), Rev 19:15 (G3709)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-A-VCG-03` (id=3764) | Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against i |
| 1 | active → new | `M02-A-VCG-05` (id=3766) | Wrath understood as an ongoing, settled existential condition resting on those who refuse the Son — not a momentary reac |
| 1 | active → new | `M02-A-VCG-02` (id=3763) | Wrath understood as impending future divine force from which people flee, are rescued, or are delivered. The coming wrat |

---

### Old VCG `38-001` (id=24) — `SPLIT`

**Old description:** 'Term names morally accountable anger — the inner state of anger that exists under divine command and requires governance before it becomes sin'

**Old member verses:** 2 total
  Sample: Eph 4:26 (G3710), Mat 5:22 (G3710)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-B-VCG-04` (id=3770) | Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from |
| 1 | active → new | `M02-B-VCG-02` (id=3768) | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |

---

### Old VCG `1091-001` (id=2068) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names dispute and hostility as expressions of inner rebellion or occasions for inner endurance — endurance against hostility guards against inner weariness, and rebellion names an inner disposition of defiance'

**Old member verses:** 4 total
  Sample: Heb 12:3 (G0485), Heb 6:16 (G0485), Heb 7:7 (G0485), Jude 11 (G0485)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names dispute and hostility as expressions of inner rebellion or occasions for inner endurance — endurance against hostility guards against inner weariness, and rebellion names an inner disposition of defiance
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-001`, `151-002`, `151-003`, `2747-001`, `234-001`, `234-002`, `205-001`

---

### Old VCG `1139-001` (id=2206) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names strife or quarrelling as an inner-moral condition — the orientation of contention that arises from jealousy, envy, and disordered self-assertion, listed among works of the flesh'

**Old member verses:** 9 total
  Sample: 1Cor 3:3 (G2054), Gal 5:20 (G2054), 1Cor 1:11 (G2054), 2Cor 12:20 (G2054), Rom 1:29 (G2054), ... +4 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 9 | active → new | `M02-F-VCG-01` (id=3786) | Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and q |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names strife or quarrelling as an inner-moral condition — the orientation of contention that arises from jealousy, envy, and disordered self-assertion, listed among works of the flesh
- New: Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and quarreling. Strife as a work of the flesh, quarreling as an inner drive of the sinful nature, word-quarrels from inner craving for controversy. The inner-being characteristic is contentious anger as a dispositional feature of the person.
- Co-source(s) into same new VCG: `6464-001`, `1431-001`, `560-001`

---

### Old VCG `114-001` (id=52) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names divine indignation as sustained moral disposition — the ongoing inner displeasure of God toward wickedness, felt daily'

**Old member verses:** 5 total
  Sample: Psa 7:11 (H2194), Pro 22:14 (H2194), Isa 66:14 (H2194), Zec 1:12 (H2194), Mal 1:4 (H2194)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 5 | active → new | `M02-C-VCG-01` (id=3775) | God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored an |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names divine indignation as sustained moral disposition — the ongoing inner displeasure of God toward wickedness, felt daily
- New: God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored and purposefully timed, defining historical periods, and sometimes permanent toward specific offenders. The inner-being characteristic is indignation as God's standing moral verdict held as a determined, principled inner disposition.
- Co-source(s) into same new VCG: `114-002`, `115-001`, `115-002`

---

### Old VCG `114-002` (id=53) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names human indignation as responsive inner emotion — the emotional-moral reaction of moral displeasure arising from provocation or perceived injustice'

**Old member verses:** 3 total
  Sample: Pro 24:24 (H2194), Pro 25:23 (H2194), Dan 11:30 (H2194)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M02-C-VCG-01` (id=3775) | God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored an |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names human indignation as responsive inner emotion — the emotional-moral reaction of moral displeasure arising from provocation or perceived injustice
- New: God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored and purposefully timed, defining historical periods, and sometimes permanent toward specific offenders. The inner-being characteristic is indignation as God's standing moral verdict held as a determined, principled inner disposition.
- Co-source(s) into same new VCG: `114-001`, `115-001`, `115-002`

---

### Old VCG `1140-001` (id=2209) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names strife as the fruit of inner pride and moral disorder — contention that arises from insolence, self-assertion, and refusal to submit'

**Old member verses:** 3 total
  Sample: Pro 13:10 (H4683), Pro 17:19 (H4683), Isa 58:4 (H4683)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M02-F-VCG-02` (id=3787) | Anger expressed as the relational atmosphere of inner contention — strife as the condition when pride and self-will go u |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names strife as the fruit of inner pride and moral disorder — contention that arises from insolence, self-assertion, and refusal to submit
- New: Anger expressed as the relational atmosphere of inner contention — strife as the condition when pride and self-will go unchecked in relationship. Strife rooted in insolence, strife as an inner appetite aligned with sin, strife as corrupt inner motive underlying religious performance. The inner-being characteristic is anger as the relational output of inner pride and self-will.
- Co-source(s) into same new VCG: `6467-001`

---

### Old VCG `1141-001` (id=2211) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names provocation or strife in a relational-spiritual context — the quarrelling that represents inner rebellion against God or relational breakdown between persons'

**Old member verses:** 2 total
  Sample: Num 27:14 (H4808), Gen 13:8 (H4808)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-D-VCG-03` (id=3780) | Anger arising spontaneously from within the inner person in response to what is encountered — not from deliberate target |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names provocation or strife in a relational-spiritual context — the quarrelling that represents inner rebellion against God or relational breakdown between persons
- New: Anger arising spontaneously from within the inner person in response to what is encountered — not from deliberate targeting but from the conscience's encounter with idolatry, injustice, or wrong. The inner-being characteristic is spontaneous anger arising from moral perception.
- Co-source(s) into same new VCG: `39-001`, `39-002`

---

### Old VCG `115-001` (id=54) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names divine indignation as purposive instrument of judgment — God's inner wrath deployed purposively against wickedness and idolatry"

**Old member verses:** 18 total
  Sample: Isa 10:5 (H2195), Psa 38:3 (H2195), Psa 69:24 (H2195), Psa 78:49 (H2195), Psa 102:10 (H2195), ... +13 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 18 | active → new | `M02-C-VCG-01` (id=3775) | God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored an |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names divine indignation as purposive instrument of judgment — God's inner wrath deployed purposively against wickedness and idolatry
- New: God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored and purposefully timed, defining historical periods, and sometimes permanent toward specific offenders. The inner-being characteristic is indignation as God's standing moral verdict held as a determined, principled inner disposition.
- Co-source(s) into same new VCG: `114-001`, `114-002`, `115-002`

---

### Old VCG `115-002` (id=55) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the prophet's inner state as divinely imparted indignation — God's own indignation placed within the person called to speak for him"

**Old member verses:** 2 total
  Sample: Jer 15:17 (H2195), Hos 7:16 (H2195)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-C-VCG-01` (id=3775) | God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored an |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the prophet's inner state as divinely imparted indignation — God's own indignation placed within the person called to speak for him
- New: God's indignation as a persistent, principled inner moral posture — a standing disposition against wickedness, stored and purposefully timed, defining historical periods, and sometimes permanent toward specific offenders. The inner-being characteristic is indignation as God's standing moral verdict held as a determined, principled inner disposition.
- Co-source(s) into same new VCG: `114-001`, `114-002`, `115-001`

---

### Old VCG `135-001` (id=57) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names rage as inner fury producing visible physical transformation and extreme action — the Aramaic term for anger at its most intense somatic expression'

**Old member verses:** 2 total
  Sample: Dan 3:13 (H2528), Dan 3:19 (H2528)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-B-VCG-03` (id=3769) | Anger as a force that floods and fills the inner person — welling to full capacity, taking possession, displacing other  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names rage as inner fury producing visible physical transformation and extreme action — the Aramaic term for anger at its most intense somatic expression
- New: Anger as a force that floods and fills the inner person — welling to full capacity, taking possession, displacing other faculties temporarily, and visibly transforming the person. The inner-being characteristic is anger as a filling, possessing force that takes over until spent or satisfied.
- Co-source(s) into same new VCG: `136-002`, `6801-001`, `139-001`

---

### Old VCG `136-003` (id=60) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner heat of habitual anger — the fury characteristic as a settled disposition that requires management and produces destruction when uncontrolled'

**Old member verses:** 4 total
  Sample: Pro 19:19 (H2534), Pro 15:1 (H2534), Pro 21:14 (H2534), Pro 27:4 (H2534)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-B-VCG-05` (id=3771) | Anger as an inner state present but requiring management and restraint — either by God whose compassion holds back wrath |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner heat of habitual anger — the fury characteristic as a settled disposition that requires management and produces destruction when uncontrolled
- New: Anger as an inner state present but requiring management and restraint — either by God whose compassion holds back wrath, or by wisdom commanding relinquishment. The inner-being characteristic is anger as a force subject to inner governance: present in the person but whose expression depends on will and wisdom.
- Co-source(s) into same new VCG: `139-003`, `140-002`, `136-002`

---

### Old VCG `139-003` (id=64) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner injunction against anger as spiritual counsel — do not let anger kindle; cease from it; it leads only to harm'

**Old member verses:** 3 total
  Sample: Psa 37:8 (H2734), Psa 37:1 (H2734), Psa 37:7 (H2734)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M02-B-VCG-05` (id=3771) | Anger as an inner state present but requiring management and restraint — either by God whose compassion holds back wrath |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner injunction against anger as spiritual counsel — do not let anger kindle; cease from it; it leads only to harm
- New: Anger as an inner state present but requiring management and restraint — either by God whose compassion holds back wrath, or by wisdom commanding relinquishment. The inner-being characteristic is anger as a force subject to inner governance: present in the person but whose expression depends on will and wisdom.
- Co-source(s) into same new VCG: `140-002`, `136-002`, `136-003`

---

### Old VCG `1405-001` (id=139) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names divine relational anger — God's inner anger toward specific persons in response to covenant violation, expressed personally and resolved personally"

**Old member verses:** 6 total
  Sample: 1Ki 11:9 (H0599), Deu 1:37 (H0599), Deu 4:21 (H0599), Psa 79:5 (H0599), Psa 85:5 (H0599), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M02-A-VCG-01` (id=3762) | God's wrath as the settled inner disposition that grounds binding covenantal outcomes — oaths, exclusions, exile, and ir |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names divine relational anger — God's inner anger toward specific persons in response to covenant violation, expressed personally and resolved personally
- New: God's wrath as the settled inner disposition that grounds binding covenantal outcomes — oaths, exclusions, exile, and irrevocable verdicts. Wrath here has legal and covenantal weight: it grounds sworn oaths, bars from rest, and produces lasting territorial and relational consequences. The inner-being characteristic is wrath as settled moral verdict with covenantal bindingness.
- Co-source(s) into same new VCG: `256-001`

---

### Old VCG `1410-001` (id=140) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names quick-temperedness as a disqualifying character trait — habitual anger as evidence of inner instability incompatible with leadership'

**Old member verses:** 1 total
  Sample: Tit 1:7 (G3711)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-C-VCG-02` (id=3776) | Indignation in human persons as a morally revelatory inner response — the anger that proves genuine repentance (2Cor 7:1 |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names quick-temperedness as a disqualifying character trait — habitual anger as evidence of inner instability incompatible with leadership
- New: Indignation in human persons as a morally revelatory inner response — the anger that proves genuine repentance (2Cor 7:11), and the dispositional anger-susceptibility that disqualifies from leadership (Tit 1:7). The inner-being characteristic is indignation as a moral inner indicator.
- Co-source(s) into same new VCG: `1411-001`, `922-001`

---

### Old VCG `1411-001` (id=141) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the anger that hardens into danger without resolution — the sunset-bounded inner state that must be addressed before becoming settled resentment'

**Old member verses:** 1 total
  Sample: Eph 4:26 (G3950)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-C-VCG-02` (id=3776) | Indignation in human persons as a morally revelatory inner response — the anger that proves genuine repentance (2Cor 7:1 |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the anger that hardens into danger without resolution — the sunset-bounded inner state that must be addressed before becoming settled resentment
- New: Indignation in human persons as a morally revelatory inner response — the anger that proves genuine repentance (2Cor 7:11), and the dispositional anger-susceptibility that disqualifies from leadership (Tit 1:7). The inner-being characteristic is indignation as a moral inner indicator.
- Co-source(s) into same new VCG: `1410-001`, `922-001`

---

### Old VCG `1431-001` (id=145) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names inner fury driving political and power conflicts — fierce anger in an authority figure expressed through hostile action'

**Old member verses:** 1 total
  Sample: Act 12:20 (G2371)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-F-VCG-01` (id=3786) | Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and q |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names inner fury driving political and power conflicts — fierce anger in an authority figure expressed through hostile action
- New: Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and quarreling. Strife as a work of the flesh, quarreling as an inner drive of the sinful nature, word-quarrels from inner craving for controversy. The inner-being characteristic is contentious anger as a dispositional feature of the person.
- Co-source(s) into same new VCG: `6464-001`, `560-001`, `1139-001`

---

### Old VCG `149-002` (id=70) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the inner vexation of relational cruelty — the distress produced in a person's inner life by another's deliberately provocative conduct"

**Old member verses:** 2 total
  Sample: 1Sa 1:6 (H3707), 1Sa 1:7 (H3707)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-D-VCG-02` (id=3779) | A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being character |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner vexation of relational cruelty — the distress produced in a person's inner life by another's deliberately provocative conduct
- New: A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being characteristic is anger aroused from the outside — a provoked inner state rather than self-generated.
- Co-source(s) into same new VCG: `177-001`, `40-001`, `149-003`

---

### Old VCG `149-003` (id=71) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner lodging of vexation as a marker of folly — anger that settles and remains as a characteristic of the unwise person'

**Old member verses:** 1 total
  Sample: Ecc 7:9 (H3707)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-D-VCG-02` (id=3779) | A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being character |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner lodging of vexation as a marker of folly — anger that settles and remains as a characteristic of the unwise person
- New: A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being characteristic is anger aroused from the outside — a provoked inner state rather than self-generated.
- Co-source(s) into same new VCG: `177-001`, `40-001`, `149-002`

---

### Old VCG `151-001` (id=72) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the vexation of inner grief and provocation — the broad register of inner distress from existential burden, rivalry, and sorrow expressed before God in prayer'

**Old member verses:** 10 total
  Sample: 1Sa 1:16 (H3708B), 1Sa 1:6 (H3708B), Psa 6:7 (H3708B), Psa 10:14 (H3708B), Psa 31:9 (H3708B), ... +5 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 10 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the vexation of inner grief and provocation — the broad register of inner distress from existential burden, rivalry, and sorrow expressed before God in prayer
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-002`, `151-003`, `2747-001`, `234-001`, `234-002`, `1091-001`, `205-001`

---

### Old VCG `151-002` (id=73) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the anger that lodges in the fool's heart — inner vexation as the resident condition of one who lacks inner governance"

**Old member verses:** 5 total
  Sample: Ecc 7:9 (H3708B), Ecc 1:18 (H3708B), Ecc 2:23 (H3708B), Ecc 5:17 (H3708B), Ecc 11:10 (H3708B)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 5 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the anger that lodges in the fool's heart — inner vexation as the resident condition of one who lacks inner governance
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-001`, `151-003`, `2747-001`, `234-001`, `234-002`, `1091-001`, `205-001`

---

### Old VCG `151-003` (id=74) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the conduct that provokes divine inner anger — Israel's actions causing God's vexation, with covenantal consequences"

**Old member verses:** 6 total
  Sample: 1Ki 15:30 (H3708B), Deu 32:19 (H3708B), Deu 32:27 (H3708B), 1Ki 21:22 (H3708B), 2Ki 23:26 (H3708B), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the conduct that provokes divine inner anger — Israel's actions causing God's vexation, with covenantal consequences
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-001`, `151-002`, `2747-001`, `234-001`, `234-002`, `1091-001`, `205-001`

---

### Old VCG `1552-001` (id=146) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names fierce inner anger co-existing with grief and loyalty — the intensity qualifier that characterises anger at its most burning while accompanying care'

**Old member verses:** 4 total
  Sample: 1Sa 20:34 (H2750), Exo 11:8 (H2750), 2Ch 25:10 (H2750), Lam 2:3 (H2750)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-B-VCG-04` (id=3770) | Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names fierce inner anger co-existing with grief and loyalty — the intensity qualifier that characterises anger at its most burning while accompanying care
- New: Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from conscience and covenantal concern, driving confrontation and intercession rather than impulsive action. The inner-being characteristic is anger as a conscience-grounded moral response.
- Co-source(s) into same new VCG: `921-001`, `38-001`, `136-001`, `139-001`

---

### Old VCG `177-001` (id=97) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the fall of the face as the first bodily expression of inner anger — countenance as the mirror of the inner emotional state'

**Old member verses:** 1 total
  Sample: Gen 4:5 (H5307K)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-D-VCG-02` (id=3779) | A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being character |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the fall of the face as the first bodily expression of inner anger — countenance as the mirror of the inner emotional state
- New: A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being characteristic is anger aroused from the outside — a provoked inner state rather than self-generated.
- Co-source(s) into same new VCG: `40-001`, `149-002`, `149-003`

---

### Old VCG `205-001` (id=767) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Provocation and harassment as hostile inner-driven action — stirring up enmity and opposition'

**Old member verses:** 4 total
  Sample: Judg 9:31 (H6696B), Psa 139:5 (H6696B), Song 8:9 (H6696B), 2Ch 6:28 (H6696B)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Provocation and harassment as hostile inner-driven action — stirring up enmity and opposition
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-001`, `151-002`, `151-003`, `2747-001`, `234-001`, `234-002`, `1091-001`

---

### Old VCG `222-001` (id=113) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names divine anger as the inner response to persistent covenant violation — God's wrath kindled by Israel's rebellion against his ways"

**Old member verses:** 2 total
  Sample: Isa 64:5 (H7107), Zec 1:15 (H7107)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-A-VCG-04` (id=3765) | Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience,  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names divine anger as the inner response to persistent covenant violation — God's wrath kindled by Israel's rebellion against his ways
- New: Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience, offense, or injustice. Anger as the inner state of moral authority when its order is violated. Includes the human anger that requires governance (Jam 1:19-20), Jesus's anger at hardness of heart, and the pattern of royal and prophetic anger.
- Co-source(s) into same new VCG: `222-002`, `37-002`, `37-003`

---

### Old VCG `222-002` (id=114) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names human anger as the inner response to subordinate failure or betrayal — the superior's wrath provoked by those under his authority"

**Old member verses:** 2 total
  Sample: Gen 40:2 (H7107), Lev 10:16 (H7107)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-A-VCG-04` (id=3765) | Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience,  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names human anger as the inner response to subordinate failure or betrayal — the superior's wrath provoked by those under his authority
- New: Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience, offense, or injustice. Anger as the inner state of moral authority when its order is violated. Includes the human anger that requires governance (Jam 1:19-20), Jesus's anger at hardness of heart, and the pattern of royal and prophetic anger.
- Co-source(s) into same new VCG: `222-001`, `37-002`, `37-003`

---

### Old VCG `223-001` (id=115) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names divine anger as momentary against the backdrop of everlasting love — the transient quality of God's wrath contrasted with the permanence of his compassion"

**Old member verses:** 2 total
  Sample: Psa 38:1 (H7110A), Isa 54:8 (H7110A)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-A-VCG-03` (id=3764) | Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against i |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names divine anger as momentary against the backdrop of everlasting love — the transient quality of God's wrath contrasted with the permanence of his compassion
- New: Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against impenitence, produced by law's encounter with transgression, channeled through institutions, and falling on communities for covenant violation. Distinguished from VCG-02 by its present/historical operation rather than future-eschatological framing.
- Co-source(s) into same new VCG: `223-002`, `37-001`, `227-001`

---

### Old VCG `223-002` (id=116) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the communal consequences of anger — how one person's anger destabilises the whole community around them"

**Old member verses:** 1 total
  Sample: Est 1:18 (H7110A)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-A-VCG-03` (id=3764) | Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against i |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the communal consequences of anger — how one person's anger destabilises the whole community around them
- New: Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against impenitence, produced by law's encounter with transgression, channeled through institutions, and falling on communities for covenant violation. Distinguished from VCG-02 by its present/historical operation rather than future-eschatological framing.
- Co-source(s) into same new VCG: `223-001`, `37-001`, `227-001`

---

### Old VCG `227-001` (id=118) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the act of provoking divine inner anger — the causal triggering of God's wrath through covenant violation, with historical consequence"

**Old member verses:** 1 total
  Sample: Ezr 5:12 (H7265)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-A-VCG-03` (id=3764) | Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against i |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the act of provoking divine inner anger — the causal triggering of God's wrath through covenant violation, with historical consequence
- New: Wrath as an active, revealed, ongoing force operating against human sin — descending from heaven, accumulating against impenitence, produced by law's encounter with transgression, channeled through institutions, and falling on communities for covenant violation. Distinguished from VCG-02 by its present/historical operation rather than future-eschatological framing.
- Co-source(s) into same new VCG: `223-001`, `223-002`, `37-001`

---

### Old VCG `234-001` (id=787) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Strife and contention as inner conflict — quarrelling, dispute, and the experience of ongoing enmity'

**Old member verses:** 19 total
  Sample: Pro 30:33 (H7379), Gen 13:7 (H7379), Exo 17:7 (H7379), Deu 1:12 (H7379), 2Sa 22:44 (H7379), ... +14 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 19 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Strife and contention as inner conflict — quarrelling, dispute, and the experience of ongoing enmity
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-001`, `151-002`, `151-003`, `2747-001`, `234-002`, `1091-001`, `205-001`

---

### Old VCG `234-002` (id=788) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Pleading one's cause — inner appeal for justice and divine advocacy"

**Old member verses:** 26 total
  Sample: Mic 7:9 (H7379), 1Sa 24:15 (H7379), 1Sa 25:39 (H7379), Job 13:6 (H7379), Job 29:16 (H7379), ... +21 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 26 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Pleading one's cause — inner appeal for justice and divine advocacy
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-001`, `151-002`, `151-003`, `2747-001`, `234-001`, `1091-001`, `205-001`

---

### Old VCG `2528-001` (id=858) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'God as Jealous — the divine inner passion that will not share worship with other gods'

**Old member verses:** 5 total
  Sample: Exo 34:14 (H7067H), Exo 20:5 (H7067H), Deu 4:24 (H7067H), Deu 5:9 (H7067H), Deu 6:15 (H7067H)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 5 | active → new | `M02-E-VCG-01` (id=3782) | God's jealousy as a defining constitutional attribute of his being — not a reaction to offense but a fundamental identit |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: God as Jealous — the divine inner passion that will not share worship with other gods
- New: God's jealousy as a defining constitutional attribute of his being — not a reaction to offense but a fundamental identity-level property: his very name is 'Jealous.' The inner-being characteristic is jealousy as God's exclusive-claim identity attribute from which all other expressions flow.
- Co-source(s) into same new VCG: `2756-001`

---

### Old VCG `254-001` (id=2568) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term describes inner state from troubled agitation to fierce rage — emotionally intense inner condition'

**Old member verses:** 3 total
  Sample: Gen 40:6 (H2196), Pro 19:3 (H2196), 2Ch 26:19 (H2196)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M02-B-VCG-02` (id=3768) | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term describes inner state from troubled agitation to fierce rage — emotionally intense inner condition
- New: Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The transition from inner burning to outward act is immediate and direct. The inner-being characteristic is anger as an action-driving force: inner heat producing immediate consequential behaviour.
- Co-source(s) into same new VCG: `255-001`, `38-001`, `38-002`, `38-003`, `139-001`, `139-002`

---

### Old VCG `255-001` (id=2569) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names intense inner rage — emotionally charged anger at extreme moral intensity'

**Old member verses:** 4 total
  Sample: 2Ch 16:10 (H2197), 2Ch 28:9 (H2197), Pro 19:12 (H2197), Isa 30:30 (H2197)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-B-VCG-02` (id=3768) | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names intense inner rage — emotionally charged anger at extreme moral intensity
- New: Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The transition from inner burning to outward act is immediate and direct. The inner-being characteristic is anger as an action-driving force: inner heat producing immediate consequential behaviour.
- Co-source(s) into same new VCG: `254-001`, `38-001`, `38-002`, `38-003`, `139-001`, `139-002`

---

### Old VCG `256-001` (id=2578) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names divine wrath as an inner state whose potential application motivates obedience'

**Old member verses:** 1 total
  Sample: Ezr 7:23 (H7109)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-A-VCG-01` (id=3762) | God's wrath as the settled inner disposition that grounds binding covenantal outcomes — oaths, exclusions, exile, and ir |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names divine wrath as an inner state whose potential application motivates obedience
- New: God's wrath as the settled inner disposition that grounds binding covenantal outcomes — oaths, exclusions, exile, and irrevocable verdicts. Wrath here has legal and covenantal weight: it grounds sworn oaths, bars from rest, and produces lasting territorial and relational consequences. The inner-being characteristic is wrath as settled moral verdict with covenantal bindingness.
- Co-source(s) into same new VCG: `1405-001`

---

### Old VCG `2747-001` (id=841) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Hot or cold — the inner temperature of spiritual commitment and fervour'

**Old member verses:** 2 total
  Sample: Rev 3:15 (G2200), Rev 3:16 (G2200)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Hot or cold — the inner temperature of spiritual commitment and fervour
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `4556-002`, `151-001`, `151-002`, `151-003`, `234-001`, `234-002`, `1091-001`, `205-001`

---

### Old VCG `2756-001` (id=862) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'God as jealous avenger — the inner passion of divine justice and exclusive claim'

**Old member verses:** 2 total
  Sample: Nah 1:2 (H7072), Jos 24:19 (H7072)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-E-VCG-01` (id=3782) | God's jealousy as a defining constitutional attribute of his being — not a reaction to offense but a fundamental identit |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: God as jealous avenger — the inner passion of divine justice and exclusive claim
- New: God's jealousy as a defining constitutional attribute of his being — not a reaction to offense but a fundamental identity-level property: his very name is 'Jealous.' The inner-being characteristic is jealousy as God's exclusive-claim identity attribute from which all other expressions flow.
- Co-source(s) into same new VCG: `2528-001`

---

### Old VCG `344-001` (id=859) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Human jealousy and envy — the consuming inner force of resentment and possessive passion'

**Old member verses:** 11 total
  Sample: Pro 14:30 (H7068), Job 5:2 (H7068), Ecc 4:4 (H7068), Ecc 9:6 (H7068), Pro 6:34 (H7068), ... +6 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 11 | active → new | `M02-E-VCG-04` (id=3785) | Jealousy in human persons directed at others — possessiveness, comparison-based resentment, covetous envy at another's a |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Human jealousy and envy — the consuming inner force of resentment and possessive passion
- New: Jealousy in human persons directed at others — possessiveness, comparison-based resentment, covetous envy at another's advantage. Marital jealousy, sibling envy, inter-tribal rivalry, and the warning against envying sinners. The inner-being characteristic is possessive jealousy and covetous envy as a reactive comparison-based inner passion.
- Co-source(s) into same new VCG: `341-003`, `341-001`

---

### Old VCG `344-002` (id=860) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Human zeal for God — inner passionate devotion as jealous advocacy'

**Old member verses:** 3 total
  Sample: Psa 69:9 (H7068), 2Ki 10:16 (H7068), Psa 119:139 (H7068)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M02-E-VCG-03` (id=3784) | Human jealousy directed toward God — consuming zeal for his honor that identifies persons with his cause. Elijah, Phineh |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Human zeal for God — inner passionate devotion as jealous advocacy
- New: Human jealousy directed toward God — consuming zeal for his honor that identifies persons with his cause. Elijah, Phinehas, the psalmists consumed from within by zeal for God. The inner-being characteristic is human jealous passion directed upward: ardor for God's honor as personally at stake.
- Co-source(s) into same new VCG: `341-002`, `341-003`, `341-001`

---

### Old VCG `344-003` (id=861) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Divine jealousy and zeal — God's consuming inner claim on his people"

**Old member verses:** 23 total
  Sample: Isa 59:17 (H7068), Num 25:11 (H7068), Deu 29:20 (H7068), 2Ki 19:31 (H7068), Psa 79:5 (H7068), ... +18 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 23 | active → new | `M02-E-VCG-02` (id=3783) | God's jealousy expressed as fierce protective passion for his people, city, land, and name — firing in their defense and |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Divine jealousy and zeal — God's consuming inner claim on his people
- New: God's jealousy expressed as fierce protective passion for his people, city, land, and name — firing in their defense and motivating restorative action. The inner-being characteristic is jealousy as protective inner passion aroused by desecration of what is covenantally his.
- Co-source(s) into same new VCG: `341-002`, `341-003`

---

### Old VCG `37-002` (id=22) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names human anger as requiring governance — the inner state that must be put away, not nursed, as incompatible with righteous living'

**Old member verses:** 3 total
  Sample: Jam 1:20 (G3709), Eph 4:31 (G3709), Col 3:8 (G3709)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M02-A-VCG-04` (id=3765) | Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience,  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names human anger as requiring governance — the inner state that must be put away, not nursed, as incompatible with righteous living
- New: Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience, offense, or injustice. Anger as the inner state of moral authority when its order is violated. Includes the human anger that requires governance (Jam 1:19-20), Jesus's anger at hardness of heart, and the pattern of royal and prophetic anger.
- Co-source(s) into same new VCG: `222-001`, `222-002`, `37-003`

---

### Old VCG `37-003` (id=23) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names righteous anger co-existing with grief — the simultaneous presence of anger and sorrow as the inner response to hardness of heart'

**Old member verses:** 1 total
  Sample: Mar 3:5 (G3709)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-A-VCG-04` (id=3765) | Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience,  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names righteous anger co-existing with grief — the simultaneous presence of anger and sorrow as the inner response to hardness of heart
- New: Anger in human persons — leaders, prophets, officials — as a morally grounded inner response to perceived disobedience, offense, or injustice. Anger as the inner state of moral authority when its order is violated. Includes the human anger that requires governance (Jam 1:19-20), Jesus's anger at hardness of heart, and the pattern of royal and prophetic anger.
- Co-source(s) into same new VCG: `222-001`, `222-002`, `37-002`

---

### Old VCG `38-002` (id=25) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names anger as an inner action-driver — the fury that compels the person to respond, act, or enforce consequences'

**Old member verses:** 4 total
  Sample: Luk 15:28 (G3710), Mat 18:34 (G3710), Mat 22:7 (G3710), Luk 14:21 (G3710)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M02-B-VCG-02` (id=3768) | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names anger as an inner action-driver — the fury that compels the person to respond, act, or enforce consequences
- New: Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The transition from inner burning to outward act is immediate and direct. The inner-being characteristic is anger as an action-driving force: inner heat producing immediate consequential behaviour.
- Co-source(s) into same new VCG: `254-001`, `255-001`, `38-001`, `38-003`, `139-001`, `139-002`

---

### Old VCG `38-003` (id=26) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names anger as cosmic inner rebellion against God — the hostility of nations and powers in ultimate opposition to divine rule'

**Old member verses:** 2 total
  Sample: Rev 11:18 (G3710), Rev 12:17 (G3710)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-B-VCG-02` (id=3768) | Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names anger as cosmic inner rebellion against God — the hostility of nations and powers in ultimate opposition to divine rule
- New: Anger in human persons as an inner force erupting outward — driving speech, physical action, and punitive decisions. The transition from inner burning to outward act is immediate and direct. The inner-being characteristic is anger as an action-driving force: inner heat producing immediate consequential behaviour.
- Co-source(s) into same new VCG: `254-001`, `255-001`, `38-001`, `38-002`, `139-001`, `139-002`

---

### Old VCG `39-001` (id=27) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names righteous inner spirit-provocation — the spirit of the person stirred to righteous indignation by idolatry and the honour of God'

**Old member verses:** 1 total
  Sample: Act 17:16 (G3947)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-D-VCG-03` (id=3780) | Anger arising spontaneously from within the inner person in response to what is encountered — not from deliberate target |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names righteous inner spirit-provocation — the spirit of the person stirred to righteous indignation by idolatry and the honour of God
- New: Anger arising spontaneously from within the inner person in response to what is encountered — not from deliberate targeting but from the conscience's encounter with idolatry, injustice, or wrong. The inner-being characteristic is spontaneous anger arising from moral perception.
- Co-source(s) into same new VCG: `1141-001`, `39-002`

---

### Old VCG `39-002` (id=28) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names love's non-irritability — the inner disposition of love that displaces reactive anger and refuses to be provoked"

**Old member verses:** 1 total
  Sample: 1Cor 13:5 (G3947)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-D-VCG-03` (id=3780) | Anger arising spontaneously from within the inner person in response to what is encountered — not from deliberate target |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names love's non-irritability — the inner disposition of love that displaces reactive anger and refuses to be provoked
- New: Anger arising spontaneously from within the inner person in response to what is encountered — not from deliberate targeting but from the conscience's encounter with idolatry, injustice, or wrong. The inner-being characteristic is spontaneous anger arising from moral perception.
- Co-source(s) into same new VCG: `39-001`, `1141-001`

---

### Old VCG `40-001` (id=29) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names anger as a provoked inner response to injustice or disobedience — the arousal of wrath in another as consequence of conduct'

**Old member verses:** 2 total
  Sample: Eph 6:4 (G3949), Rom 10:19 (G3949)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-D-VCG-02` (id=3779) | A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being character |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names anger as a provoked inner response to injustice or disobedience — the arousal of wrath in another as consequence of conduct
- New: A human person's anger being deliberately or repeatedly stirred by another's targeted actions. The inner-being characteristic is anger aroused from the outside — a provoked inner state rather than self-generated.
- Co-source(s) into same new VCG: `177-001`, `149-002`, `149-003`

---

### Old VCG `4556-001` (id=166) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the positive inner stimulation of motivation — one person's zeal provoking another to greater inner response and generosity"

**Old member verses:** 1 total
  Sample: 2Cor 9:2 (G2042)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the positive inner stimulation of motivation — one person's zeal provoking another to greater inner response and generosity
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-002`, `151-001`, `151-002`, `151-003`, `2747-001`, `234-001`, `234-002`, `1091-001`, `205-001`

---

### Old VCG `4556-002` (id=167) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the negative inner provocation that crushes the spirit — conduct by an authority figure that damages the inner person and produces discouragement'

**Old member verses:** 1 total
  Sample: Col 3:21 (G2042)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-BOUNDARY-VCG-01` (id=3774) | Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or e |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the negative inner provocation that crushes the spirit — conduct by an authority figure that damages the inner person and produces discouragement
- New: Aggregating placeholder VCG for 6 BOUNDARY terms designated at Phase 3 whose corpora were too mixed-register, thin, or edge-case for placement in characteristic sub-groups. Members: antilogia (mixed dispute registers), erethizō (constructive/damaging provocation, thin corpus), zestos (spiritual fervor not anger), ka.a.s (anger-register and grief-register split), riv (anger-driven contention and legal-procedural dispute split), tsur (no active relevant corpus — structural-only). Pending researcher disposition at Phase 12.
- Co-source(s) into same new VCG: `4556-001`, `151-001`, `151-002`, `151-003`, `2747-001`, `234-001`, `234-002`, `1091-001`, `205-001`

---

### Old VCG `560-001` (id=1570) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the contentious inner disposition — the inner inclination toward argument that Paul refuses to validate as a community practice'

**Old member verses:** 1 total
  Sample: 1Cor 11:16 (G5380)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-F-VCG-01` (id=3786) | Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and q |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the contentious inner disposition — the inner inclination toward argument that Paul refuses to validate as a community practice
- New: Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and quarreling. Strife as a work of the flesh, quarreling as an inner drive of the sinful nature, word-quarrels from inner craving for controversy. The inner-being characteristic is contentious anger as a dispositional feature of the person.
- Co-source(s) into same new VCG: `6464-001`, `1431-001`, `1139-001`

---

### Old VCG `6464-001` (id=2208) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names quarrelling about words as an expression of pride and disordered craving — the inner orientation of conceit that produces relational destruction'

**Old member verses:** 1 total
  Sample: 1Ti 6:4 (G3055)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-F-VCG-01` (id=3786) | Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and q |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names quarrelling about words as an expression of pride and disordered craving — the inner orientation of conceit that produces relational destruction
- New: Anger as a settled inner disposition toward contention — a habitual orientation of the inner person toward dispute and quarreling. Strife as a work of the flesh, quarreling as an inner drive of the sinful nature, word-quarrels from inner craving for controversy. The inner-being characteristic is contentious anger as a dispositional feature of the person.
- Co-source(s) into same new VCG: `1431-001`, `560-001`, `1139-001`

---

### Old VCG `6467-001` (id=2210) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names those who contend in strife — the inner disposition of hostile contention directed against God's people, which will ultimately come to nothing"

**Old member verses:** 1 total
  Sample: Isa 41:12 (H4695)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-F-VCG-02` (id=3787) | Anger expressed as the relational atmosphere of inner contention — strife as the condition when pride and self-will go u |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names those who contend in strife — the inner disposition of hostile contention directed against God's people, which will ultimately come to nothing
- New: Anger expressed as the relational atmosphere of inner contention — strife as the condition when pride and self-will go unchecked in relationship. Strife rooted in insolence, strife as an inner appetite aligned with sin, strife as corrupt inner motive underlying religious performance. The inner-being characteristic is anger as the relational output of inner pride and self-will.
- Co-source(s) into same new VCG: `1140-001`

---

### Old VCG `6801-001` (id=2571) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names sullen vexation withdrawing from engagement — resentful displeasure manifesting in physical withdrawal'

**Old member verses:** 2 total
  Sample: 1Ki 21:4 (H2198), 1Ki 20:43 (H2198)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M02-B-VCG-03` (id=3769) | Anger as a force that floods and fills the inner person — welling to full capacity, taking possession, displacing other  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names sullen vexation withdrawing from engagement — resentful displeasure manifesting in physical withdrawal
- New: Anger as a force that floods and fills the inner person — welling to full capacity, taking possession, displacing other faculties temporarily, and visibly transforming the person. The inner-being characteristic is anger as a filling, possessing force that takes over until spent or satisfied.
- Co-source(s) into same new VCG: `135-001`, `136-002`, `139-001`

---

### Old VCG `921-001` (id=1312) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names hot indignation as an inner moral response — the rising of righteous outrage at wickedness that forsakes God's law"

**Old member verses:** 1 total
  Sample: Psa 119:53 (H2152)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-B-VCG-04` (id=3770) | Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names hot indignation as an inner moral response — the rising of righteous outrage at wickedness that forsakes God's law
- New: Anger in human persons as a morally calibrated response to injustice, theological error, or moral failure — arising from conscience and covenantal concern, driving confrontation and intercession rather than impulsive action. The inner-being characteristic is anger as a conscience-grounded moral response.
- Co-source(s) into same new VCG: `38-001`, `1552-001`, `136-001`, `139-001`

---

### Old VCG `922-001` (id=1311) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names indignation as an inner response to wrong — the rising of righteous anger produced by godly grief and repentance'

**Old member verses:** 1 total
  Sample: 2Cor 7:11 (G0024)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-C-VCG-02` (id=3776) | Indignation in human persons as a morally revelatory inner response — the anger that proves genuine repentance (2Cor 7:1 |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names indignation as an inner response to wrong — the rising of righteous anger produced by godly grief and repentance
- New: Indignation in human persons as a morally revelatory inner response — the anger that proves genuine repentance (2Cor 7:11), and the dispositional anger-susceptibility that disqualifies from leadership (Tit 1:7). The inner-being characteristic is indignation as a moral inner indicator.
- Co-source(s) into same new VCG: `1410-001`, `1411-001`

---

### Old VCG `149-001` (id=69) — `KEEP-EQUIVALENT`

**Old description:** "Term names the provoking of divine vexation — Israel's conduct as the trigger of God's inner anger, creating a recurring covenantal pattern of provocation and response"

**Old member verses:** 15 total
  Sample: 1Ki 14:15 (H3707), 1Ki 15:30 (H3707), 1Ki 16:2 (H3707), 1Ki 16:7 (H3707), 1Ki 16:13 (H3707), ... +10 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 15 | active → new | `M02-D-VCG-01` (id=3778) | The relational dynamic of human idolatry as an act that deliberately stirs God's anger — a covenant breach directed at h |

**Side-by-side QA (KEEP-EQUIVALENT):**

- Old: Term names the provoking of divine vexation — Israel's conduct as the trigger of God's inner anger, creating a recurring covenantal pattern of provocation and response
- New: The relational dynamic of human idolatry as an act that deliberately stirs God's anger — a covenant breach directed at his exclusive claim, provoking his inner anger through repeated, willful, and cumulative offense. The inner-being characteristic is idolatry as a directed relational provocation that arouses anger.

---

### Old VCG `255-002` (id=2570) — `KEEP-EQUIVALENT`

**Old description:** "Term names bearing divine indignation — accepting God's anger as just, waiting for vindication"

**Old member verses:** 1 total
  Sample: Mic 7:9 (H2197)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-B-VCG-07` (id=3773) | Anger understood from the perspective of the person bearing it — the inner experience of being under wrath: crushed, sat |

**Side-by-side QA (KEEP-EQUIVALENT):**

- Old: Term names bearing divine indignation — accepting God's anger as just, waiting for vindication
- New: Anger understood from the perspective of the person bearing it — the inner experience of being under wrath: crushed, saturated, overwhelmed, and unable to stand. The inner-being characteristic is the experience of bearing anger as weight, saturation, and inner collapse.

---

### Old VCG `91-001` (id=735) — `KEEP-EQUIVALENT`

**Old description:** 'Distress and displeasure as inner affective state'

**Old member verses:** 1 total
  Sample: Dan 6:14 (H0888)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M02-C-VCG-03` (id=3777) | The softest anger register — sullen, brooding, situational displeasure that withdraws and shuts down rather than eruptin |

**Side-by-side QA (KEEP-EQUIVALENT):**

- Old: Distress and displeasure as inner affective state
- New: The softest anger register — sullen, brooding, situational displeasure that withdraws and shuts down rather than erupting. The inner-being characteristic is displeasure as a brooding closed-down inner state, the person in inner conflict with their circumstances.

---

## 4. Researcher approval

- Eligible for soft-delete on approval: **68** inherited VCGs
- Blocked (UNROUTED — fix Phase 7 follow-up first): **0** inherited VCGs

Approve dissolution by selecting one of the following:

- ☐ **Approve all eligible** — soft-delete all non-UNROUTED inherited VCGs (preferred)
- ☐ **Approve selectively** — list any eligible VCG ids to retain past dissolution: __________
- ☐ **Pause** — researcher will review individual cases before approval

On approval, CC executes `wa-cluster-{code}-dir-NNN-vcg-dissolve-v1-{date}.md` which soft-deletes the approved inherited VCGs + their `vcg_term` links.

*End of comparison report.*