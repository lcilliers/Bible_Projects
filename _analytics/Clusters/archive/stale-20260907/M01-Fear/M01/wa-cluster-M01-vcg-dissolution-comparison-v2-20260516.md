# M01 Fear, Dread and Terror — VCG dissolution comparison (v2)

**Generated:** 2026-05-16T04:50:36Z  
**Cluster:** `M01` (Fear) · status=Analysis - In Progress · version=v6  
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §11 (Phase 8)  
**Snapshot:** 2026-05-16T04:47:48Z — 1028 vc rows  
**Boundary:** new VCGs = id ≥ 3726; inherited = id < 3726  
**Source:** `database/bible_research.db`  

**Scope:** for each inherited (pre-Phase-7) VCG linked to this cluster's terms, this report shows where its member verses landed under the new (Phase 7) VCG structure. **Researcher reviews and approves dissolution before CC executes the soft-delete directive.**

---

## 1. Header summary

- Inherited VCGs: **115**
- New VCGs: **36**
- Active vc rows (routed to new VCGs): **941**
- Active vc rows (group_id IS NULL — needs Phase 7 follow-up): **0**
- Set-aside vc rows (is_relevant=0): **81**
- Soft-deleted vc rows (delete_flagged=1): **6**

### Disposition counts

| Disposition | Count | Meaning |
|---|---:|---|
| `KEEP-EQUIVALENT` | 0 | Old VCG maps 1:1 to a single new VCG that has no other source. |
| `KEEP-EQUIVALENT-OF-MERGE` | 59 | Old VCG maps to a single new VCG, but that new VCG also receives members from other old VCGs (consolidation). |
| `SPLIT` | 55 | Old VCG's members distributed across 2+ new VCGs. |
| `OBSOLETE` | 1 | Old VCG's members are all set-aside or soft-deleted; no active routed members. |
| `UNROUTED` | 0 | Old VCG has ≥1 member still active and unrouted (needs Phase 7 follow-up before dissolution). |

**Dissolution gate:** inherited VCGs with `UNROUTED` disposition retain `delete_flagged=0` until their remaining active members are routed. All other inherited VCGs are eligible for soft-delete on researcher approval.

---

## 2. Consolidation map (new VCGs that absorbed multiple old VCGs)

These new VCGs each draw their members from 2+ old VCGs. This is the most consequential change in structure — review carefully.

| New VCG | # source old VCGs | Source old VCG codes (id) |
|---|---:|---|
| `M01-A-VCG-01` (id=3726) | 11 | `1682-001` (id=253), `1682-004` (id=256), `1681-001` (id=257), `1681-002` (id=258), `829-001` (id=831), `266-002` (id=894), `269-001` (id=897), `269-002` (id=898), `292-003` (id=923), `298-002` (id=928), `263-001` (id=1042) |
| `M01-A-VCG-02` (id=3727) | 5 | `1682-001` (id=253), `1682-004` (id=256), `269-001` (id=897), `269-002` (id=898), `291-002` (id=1040) |
| `M01-A-VCG-03` (id=3728) | 5 | `1682-002` (id=254), `1682-003` (id=255), `1681-001` (id=257), `1681-002` (id=258), `292-002` (id=922) |
| `M01-A-VCG-04` (id=3729) | 13 | `1682-001` (id=253), `1682-002` (id=254), `1682-003` (id=255), `1682-004` (id=256), `266-001` (id=893), `266-002` (id=894), `266-003` (id=895), `269-002` (id=898), `270-002` (id=901), `271-002` (id=903), `290-001` (id=919), `298-002` (id=928), `298-003` (id=929) |
| `M01-A-VCG-05` (id=3730) | 11 | `1682-001` (id=253), `1682-003` (id=255), `1682-004` (id=256), `1681-002` (id=258), `266-002` (id=894), `270-002` (id=901), `271-002` (id=903), `292-003` (id=923), `298-001` (id=927), `298-002` (id=928), `298-003` (id=929) |
| `M01-A-VCG-06` (id=3731) | 15 | `704-001` (id=246), `1682-001` (id=253), `1682-002` (id=254), `1682-003` (id=255), `1682-004` (id=256), `829-001` (id=831), `266-002` (id=894), `266-003` (id=895), `269-001` (id=897), `269-002` (id=898), `270-002` (id=901), `271-002` (id=903), `292-002` (id=922), `292-003` (id=923), `298-002` (id=928) |
| `M01-A-VCG-07` (id=3732) | 8 | `1682-003` (id=255), `270-001` (id=900), `271-001` (id=902), `290-001` (id=919), `298-002` (id=928), `298-003` (id=929), `291-001` (id=1039), `291-002` (id=1040) |
| `M01-B-VCG-01` (id=3733) | 17 | `1690-001` (id=248), `16-001` (id=720), `829-001` (id=831), `829-003` (id=833), `257-001` (id=885), `257-002` (id=886), `266-001` (id=893), `266-003` (id=895), `283-001` (id=913), `284-001` (id=914), `292-001` (id=921), `294-002` (id=925), `298-001` (id=927), `298-003` (id=929), `1734-001` (id=1023), `291-001` (id=1039), `1733-001` (id=1052) |
| `M01-B-VCG-02` (id=3734) | 4 | `16-001` (id=720), `5126-001` (id=721), `266-001` (id=893), `292-001` (id=921) |
| `M01-B-VCG-03` (id=3735) | 18 | `1690-001` (id=248), `1692-001` (id=249), `1681-002` (id=258), `829-002` (id=832), `829-004` (id=834), `276-001` (id=908), `284-003` (id=916), `290-002` (id=920), `292-001` (id=921), `292-002` (id=922), `292-003` (id=923), `294-001` (id=924), `294-002` (id=925), `298-001` (id=927), `298-002` (id=928), `298-003` (id=929), `305-002` (id=933), `291-003` (id=1041) |
| `M01-B-VCG-04` (id=3736) | 5 | `829-004` (id=834), `266-003` (id=895), `292-001` (id=921), `292-003` (id=923), `298-003` (id=929) |
| `M01-B-VCG-05` (id=3737) | 6 | `1681-002` (id=258), `829-004` (id=834), `266-003` (id=895), `298-001` (id=927), `298-003` (id=929), `305-002` (id=933) |
| `M01-B-VCG-06` (id=3738) | 11 | `1681-002` (id=258), `829-002` (id=832), `267-001` (id=896), `292-001` (id=921), `292-002` (id=922), `292-003` (id=923), `298-001` (id=927), `298-002` (id=928), `298-003` (id=929), `291-003` (id=1041), `297-001` (id=1044) |
| `M01-BOUNDARY-VCG-01` (id=3739) | 8 | `240-001` (id=121), `4814-001` (id=294), `2-001` (id=713), `2-002` (id=714), `152-001` (id=751), `5157-001` (id=759), `289-001` (id=1053), `1245-001` (id=2497) |
| `M01-C-VCG-01` (id=3740) | 4 | `829-003` (id=833), `269-003` (id=899), `284-001` (id=914), `1155-001` (id=2272) |
| `M01-C-VCG-02` (id=3741) | 3 | `286-001` (id=917), `1156-001` (id=2269), `1154-001` (id=2270) |
| `M01-C-VCG-03` (id=3742) | 2 | `1720-001` (id=163), `1151-001` (id=2273) |
| `M01-C-VCG-04` (id=3743) | 8 | `829-001` (id=831), `829-003` (id=833), `284-002` (id=915), `284-003` (id=916), `286-001` (id=917), `1723-001` (id=1019), `1729-001` (id=1021), `1152-001` (id=2274) |
| `M01-C-VCG-05` (id=3744) | 7 | `266-003` (id=895), `284-002` (id=915), `284-003` (id=916), `298-003` (id=929), `1722-001` (id=1017), `1722-002` (id=1018), `1730-001` (id=1022) |
| `M01-D-VCG-01` (id=3745) | 3 | `703-001` (id=250), `92-001` (id=737), `1158-001` (id=2271) |
| `M01-D-VCG-02` (id=3746) | 4 | `703-001` (id=250), `703-002` (id=251), `703-003` (id=252), `92-001` (id=737) |
| `M01-D-VCG-03` (id=3747) | 4 | `703-001` (id=250), `703-003` (id=252), `5187-001` (id=739), `5187-002` (id=740) |
| `M01-D-VCG-04` (id=3748) | 4 | `703-001` (id=250), `703-002` (id=251), `703-003` (id=252), `1732-001` (id=1054) |
| `M01-D-VCG-05` (id=3749) | 6 | `1554-001` (id=147), `1554-003` (id=149), `92-001` (id=737), `92-002` (id=738), `305-002` (id=933), `279-001` (id=1045) |
| `M01-E-VCG-01` (id=3750) | 7 | `1554-001` (id=147), `274-001` (id=906), `305-001` (id=932), `307-001` (id=935), `309-001` (id=938), `306-001` (id=1037), `1793-001` (id=1046) |
| `M01-E-VCG-02` (id=3751) | 7 | `829-001` (id=831), `298-002` (id=928), `310-001` (id=940), `310-002` (id=941), `306-002` (id=1038), `1793-001` (id=1046), `311-001` (id=1048) |
| `M01-E-VCG-03` (id=3752) | 5 | `305-002` (id=933), `305-003` (id=934), `309-001` (id=938), `1744-001` (id=1050), `1746-001` (id=1051) |
| `M01-E-VCG-04` (id=3753) | 12 | `1554-002` (id=148), `1554-003` (id=149), `298-003` (id=929), `305-001` (id=932), `305-002` (id=933), `305-003` (id=934), `309-001` (id=938), `309-002` (id=939), `306-001` (id=1037), `282-001` (id=1043), `1792-001` (id=1047), `311-001` (id=1048) |
| `M01-E-VCG-05` (id=3754) | 6 | `1576-001` (id=155), `1577-001` (id=156), `306-001` (id=1037), `282-001` (id=1043), `1792-001` (id=1047), `1713-001` (id=1049) |
| `M01-E-VCG-06` (id=3755) | 4 | `307-001` (id=935), `308-001` (id=936), `308-002` (id=937), `306-002` (id=1038) |
| `M01-F-VCG-01` (id=3756) | 3 | `349-001` (id=219), `266-003` (id=895), `107-001` (id=2227) |
| `M01-F-VCG-02` (id=3757) | 5 | `829-002` (id=832), `272-001` (id=904), `273-001` (id=905), `296-001` (id=926), `291-001` (id=1039) |
| `M01-F-VCG-03` (id=3758) | 4 | `829-002` (id=832), `829-004` (id=834), `296-001` (id=926), `291-001` (id=1039) |
| `M01-F-VCG-04` (id=3759) | 9 | `829-002` (id=832), `829-003` (id=833), `269-002` (id=898), `269-003` (id=899), `274-001` (id=906), `292-002` (id=922), `291-001` (id=1039), `291-002` (id=1040), `291-003` (id=1041) |
| `M01-F-VCG-05` (id=3760) | 5 | `829-004` (id=834), `266-003` (id=895), `292-002` (id=922), `292-003` (id=923), `291-003` (id=1041) |
| `M01-G-VCG-01` (id=3761) | 6 | `261-001` (id=891), `288-001` (id=918), `292-003` (id=923), `309-002` (id=939), `1701-001` (id=1015), `1701-002` (id=1016) |

---

## 3. Per-inherited-VCG detail

### Old VCG `1554-004` (id=150) — `OBSOLETE`

**Old description:** "Term names the provocation of divine agitation — conduct that disturbs God's inner relational rest, stirring him to respond"

**Old member verses:** 1 total
  Sample: Eze 16:43 (H7264)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | set-aside (is_relevant=0) | _(no VCG; outside programme scope or other reason)_ |  |

---

### Old VCG `1554-001` (id=147) — `SPLIT`

**Old description:** 'Term names the trembling restraint of anger — being agitated without sin, holding inner fury still before God in the privacy of the heart'

**Old member verses:** 3 total
  Sample: Psa 4:4 (H7264), Psa 77:16 (H7264), Psa 99:1 (H7264)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-01` (id=3750) | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |
| 1 | active → new | `M01-D-VCG-05` (id=3749) | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |

---

### Old VCG `1554-003` (id=149) — `SPLIT`

**Old description:** 'Term names grief-disturbance — the agitation of inner pain expressing itself as trembling and mourning in response to devastating loss'

**Old member verses:** 3 total
  Sample: 2Sa 18:33 (H7264), Isa 32:10 (H7264), Isa 32:11 (H7264)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 1 | active → new | `M01-D-VCG-05` (id=3749) | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |

---

### Old VCG `16-001` (id=720) — `SPLIT`

**Old description:** 'Overwhelming inner alarm and awe-struck response'

**Old member verses:** 4 total
  Sample: Mar 14:33 (G1568), Mar 9:15 (G1568), Mar 16:5 (G1568), Mar 16:6 (G1568)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 1 | active → new | `M01-B-VCG-02` (id=3734) | The awe-struck fear produced specifically by witnessing Jesus exercise supernatural power — calming storms, healing, rai |

---

### Old VCG `1681-001` (id=257) — `SPLIT`

**Old description:** 'God-fearer as inner-being identity — those characterised by reverence for God as their defining mark, recipients of divine attention and blessing'

**Old member verses:** 48 total
  Sample: Job 1:1 (H3373), Job 1:8 (H3373), Job 2:3 (H3373), Psa 15:4 (H3373), Psa 22:23 (H3373), ... +43 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 46 | active → new | `M01-A-VCG-03` (id=3728) | Fear of God is presented as the relational posture that aligns a person with God's saving purposes and opens them to his |
| 2 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |

---

### Old VCG `1681-002` (id=258) — `SPLIT`

**Old description:** 'Fear as inner state of anxiety or dread directed at human threats — inner person unsettled by danger, opposition, or uncertain outcomes'

**Old member verses:** 16 total
  Sample: Judg 7:3 (H3373), Gen 32:11 (H3373), 1Sa 23:3 (H3373), Deu 7:19 (H3373), Deu 20:8 (H3373), ... +11 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 4 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 3 | active → new | `M01-B-VCG-05` (id=3737) | Fear as the inner force that directly governs personal decision-making — driving flight, deception, or inaction when lif |
| 2 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |
| 2 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 1 | active → new | `M01-A-VCG-03` (id=3728) | Fear of God is presented as the relational posture that aligns a person with God's saving purposes and opens them to his |

---

### Old VCG `1682-001` (id=253) — `SPLIT`

**Old description:** 'Fear of God as foundational inner-being orientation — commanded disposition of the whole person from which obedience, love, and faithfulness flow'

**Old member verses:** 41 total
  Sample: Ecc 12:13 (H3372H), Deu 6:2 (H3372H), Deu 6:13 (H3372H), Deu 6:24 (H3372H), Deu 8:6 (H3372H), ... +36 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 12 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 10 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 8 | active → new | `M01-A-VCG-02` (id=3727) | Fear of God is identified as the foundational inner orientation from which wisdom, knowledge, and genuine understanding  |
| 7 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 3 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 1 | soft-deleted (duplicate row) | _(vc.delete_flagged=1; identical analytical content preserved on kept row)_ |  |

---

### Old VCG `1682-002` (id=254) — `SPLIT`

**Old description:** 'God-fearer as inner-being identity — divine favour, belonging, and blessing attached to the person characterised by reverence for God'

**Old member verses:** 8 total
  Sample: Psa 34:9 (H3372H), Psa 119:63 (H3372H), Neh 1:11 (H3372H), Neh 7:2 (H3372H), Job 1:9 (H3372H), ... +3 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 3 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 2 | active → new | `M01-A-VCG-03` (id=3728) | Fear of God is presented as the relational posture that aligns a person with God's saving purposes and opens them to his |

---

### Old VCG `1682-003` (id=255) — `SPLIT`

**Old description:** "Awe at God's acts and nature — inner-being response of wonder and reverence to divine power, holiness, and mighty deeds"

**Old member verses:** 47 total
  Sample: Gen 28:17 (H3372H), Exo 14:31 (H3372H), Exo 15:11 (H3372H), Exo 34:10 (H3372H), Deu 7:21 (H3372H), ... +42 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 41 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 2 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 1 | active → new | `M01-A-VCG-03` (id=3728) | Fear of God is presented as the relational posture that aligns a person with God's saving purposes and opens them to his |
| 1 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 1 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |
| 1 | soft-deleted (duplicate row) | _(vc.delete_flagged=1; identical analytical content preserved on kept row)_ |  |

---

### Old VCG `1682-004` (id=256) — `SPLIT`

**Old description:** 'Fear of God expressed in communal and relational life — reverence shaping conduct toward others and covenantal faithfulness'

**Old member verses:** 17 total
  Sample: Mal 2:5 (H3372H), Lev 19:30 (H3372H), Lev 19:32 (H3372H), Lev 25:17 (H3372H), Lev 25:36 (H3372H), ... +12 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 5 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 3 | active → new | `M01-A-VCG-02` (id=3727) | Fear of God is identified as the foundational inner orientation from which wisdom, knowledge, and genuine understanding  |
| 2 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 2 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 1 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 4 | soft-deleted (duplicate row) | _(vc.delete_flagged=1; identical analytical content preserved on kept row)_ |  |

---

### Old VCG `1690-001` (id=248) — `SPLIT`

**Old description:** 'Inner state of terror or startled fright — inner person overwhelmed and destabilised by sudden or threatening encounters'

**Old member verses:** 2 total
  Sample: Luk 21:9 (G4422), Luk 24:37 (G4422)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 1 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

---

### Old VCG `1792-001` (id=1047) — `SPLIT`

**Old description:** 'Term names the trembling that overtakes the inner being under the assault of dread or terror — the inner-somatic response to overwhelming fear'

**Old member verses:** 3 total
  Sample: Psa 55:5 (H7461A), Exo 15:15 (H7461A), Job 4:14 (H7461A)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-05` (id=3754) | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |
| 1 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |

---

### Old VCG `1793-001` (id=1046) — `SPLIT`

**Old description:** 'Term describes the bodily-inner trembling that overtakes a person in the presence of divine holiness or the weight of sin before God'

**Old member verses:** 2 total
  Sample: Dan 10:11 (H7460), Ezr 10:9 (H7460)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-E-VCG-01` (id=3750) | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |
| 1 | active → new | `M01-E-VCG-02` (id=3751) | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |

---

### Old VCG `266-001` (id=893) — `SPLIT`

**Old description:** 'Term names the overwhelming inner awe that arises in response to divine action, presence, or miracle — the fear-and-wonder that leads to worship and praise'

**Old member verses:** 14 total
  Sample: Luk 7:16 (G5401), Act 2:43 (G5401), Mat 14:26 (G5401), Mat 28:4 (G5401), Mat 28:8 (G5401), ... +9 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 8 | active → new | `M01-B-VCG-02` (id=3734) | The awe-struck fear produced specifically by witnessing Jesus exercise supernatural power — calming storms, healing, rai |
| 4 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 2 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

---

### Old VCG `266-002` (id=894) — `SPLIT`

**Old description:** 'Term names the inner orientation of godly fear — the reverential awe before God that shapes conduct, holiness, and ministry'

**Old member verses:** 17 total
  Sample: Act 9:31 (G5401), 2Cor 7:1 (G5401), Rom 3:18 (G5401), Rom 8:15 (G5401), 2Cor 5:11 (G5401), ... +12 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 11 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 3 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 2 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 1 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |

---

### Old VCG `266-003` (id=895) — `SPLIT`

**Old description:** 'Term names the practical inner fear before threatening powers, death, or judgement — the protective or enslaving fear that may need to be overcome or redirected'

**Old member verses:** 12 total
  Sample: Heb 2:15 (G5401), Joh 7:13 (G5401), Joh 19:38 (G5401), Joh 20:19 (G5401), Rom 13:3 (G5401), ... +7 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-B-VCG-04` (id=3736) | The reactive inner dread specifically directed at social consequences — crowd opinion, peer pressure, public exposure, s |
| 2 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 2 | active → new | `M01-B-VCG-05` (id=3737) | Fear as the inner force that directly governs personal decision-making — driving flight, deception, or inaction when lif |
| 1 | active → new | `M01-F-VCG-01` (id=3756) | Anxiety as a sustained, all-pervasive inner burden that saturates every moment and every ordinary activity — not trigger |
| 1 | active → new | `M01-C-VCG-05` (id=3744) | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |
| 1 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 1 | active → new | `M01-F-VCG-05` (id=3760) | A specific form of anticipatory dread characterised by Paul's protective apprehension about the spiritual welfare of his |
| 1 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |

---

### Old VCG `269-001` (id=897) — `SPLIT`

**Old description:** 'Term names the fear of the Lord as the foundational inner orientation of wisdom — the beginning and source of knowledge, wisdom, life, and understanding'

**Old member verses:** 20 total
  Sample: Pro 1:7 (H3374), Psa 111:10 (H3374), Job 28:28 (H3374), Pro 2:5 (H3374), Pro 8:13 (H3374), ... +15 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 17 | active → new | `M01-A-VCG-02` (id=3727) | Fear of God is identified as the foundational inner orientation from which wisdom, knowledge, and genuine understanding  |
| 2 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 1 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |

---

### Old VCG `269-002` (id=898) — `SPLIT`

**Old description:** 'Term names the fear of the Lord as the proper inner orientation of worship and covenant obedience — reverential awe before God that shapes conduct, praise, and faithful living'

**Old member verses:** 19 total
  Sample: Psa 19:9 (H3374), Isa 11:2 (H3374), Gen 20:11 (H3374), Exo 20:20 (H3374), 2Sa 23:3 (H3374), ... +14 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-A-VCG-02` (id=3727) | Fear of God is identified as the foundational inner orientation from which wisdom, knowledge, and genuine understanding  |
| 6 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 4 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 2 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 1 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |

---

### Old VCG `269-003` (id=899) — `SPLIT`

**Old description:** 'Term names terror as divine instrument or existential dread — the fear God places on peoples, or the acute inner anguish before overwhelming threat'

**Old member verses:** 3 total
  Sample: Deu 2:25 (H3374), Psa 55:5 (H3374), Jon 1:10 (H3374)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 1 | active → new | `M01-C-VCG-01` (id=3740) | God deploys dread and terror ahead of Israel as an active weapon that paralyses enemy resistance before battle — an exte |

---

### Old VCG `270-002` (id=901) — `SPLIT`

**Old description:** 'Term names the reverential fear of God as the proper inner orientation — the awe and dread that God is owed as master and father, expressed in covenant fidelity'

**Old member verses:** 5 total
  Sample: Mal 2:5 (H4172A), Isa 8:13 (H4172A), Psa 76:11 (H4172A), Isa 8:12 (H4172A), Mal 1:6 (H4172A)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 2 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 1 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |

---

### Old VCG `271-002` (id=903) — `SPLIT`

**Old description:** 'Term names the reverential fear of God as the proper inner orientation — the awe and dread that God is owed as master and father, expressed in covenant fidelity'

**Old member verses:** 5 total
  Sample: Mal 2:5 (H4172B), Isa 8:13 (H4172B), Psa 76:11 (H4172B), Isa 8:12 (H4172B), Mal 1:6 (H4172B)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 2 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 1 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |

---

### Old VCG `274-001` (id=906) — `SPLIT`

**Old description:** 'Term names the quality of divine judgment or presence as terror-inducing — the inner state of dread that the encounter with the holy God produces'

**Old member verses:** 3 total
  Sample: Heb 10:31 (G5398), Heb 10:27 (G5398), Heb 12:21 (G5398)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 1 | active → new | `M01-E-VCG-01` (id=3750) | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |

---

### Old VCG `282-001` (id=1043) — `SPLIT`

**Old description:** 'Term names the shuddering horror that seizes the inner being under overwhelming dread, appalling revelation, or imminent catastrophe'

**Old member verses:** 4 total
  Sample: Psa 55:5 (H6427), Job 21:6 (H6427), Isa 21:4 (H6427), Eze 7:18 (H6427)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-E-VCG-05` (id=3754) | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |
| 1 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |

---

### Old VCG `284-001` (id=914) — `SPLIT`

**Old description:** 'Term names terror sent by God as an instrument of divine power — the overwhelming inner dread God places on enemies before Israel'

**Old member verses:** 5 total
  Sample: Exo 15:16 (H0367), Exo 23:27 (H0367), Gen 15:12 (H0367), Jos 2:9 (H0367), Deu 32:25 (H0367)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-C-VCG-01` (id=3740) | God deploys dread and terror ahead of Israel as an active weapon that paralyses enemy resistance before battle — an exte |
| 1 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

---

### Old VCG `284-002` (id=915) — `SPLIT`

**Old description:** 'Term names the terror of God experienced by the individual — the inner condition of acute dread before divine presence or judgment'

**Old member verses:** 6 total
  Sample: Job 9:34 (H0367), Psa 55:4 (H0367), Job 13:21 (H0367), Job 20:25 (H0367), Psa 88:15 (H0367), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 5 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |
| 1 | active → new | `M01-C-VCG-05` (id=3744) | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |

---

### Old VCG `284-003` (id=916) — `SPLIT`

**Old description:** 'Term names terror as the quality of overwhelming power — the dread that powerful persons, creatures, or situations generate in others'

**Old member verses:** 4 total
  Sample: Pro 20:2 (H0367), Job 41:14 (H0367), Ezr 3:3 (H0367), Job 33:7 (H0367)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-C-VCG-05` (id=3744) | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 1 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |

---

### Old VCG `286-001` (id=917) — `SPLIT`

**Old description:** 'Term names the comprehensive inner terror of being surrounded on every side — the overwhelming existential condition of fear from which there is no escape'

**Old member verses:** 8 total
  Sample: Psa 31:13 (H4032), Jer 20:10 (H4032), Isa 31:9 (H4032), Jer 6:25 (H4032), Jer 20:4 (H4032), ... +3 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 7 | active → new | `M01-C-VCG-02` (id=3741) | Terror characterised as an active, hunting, encircling force that overwhelms the inner person with no escape — pursuing  |
| 1 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |

---

### Old VCG `290-001` (id=919) — `SPLIT`

**Old description:** 'Term names reverential awe before divine power — the inner posture of standing in awe of God, called for from all creatures'

**Old member verses:** 4 total
  Sample: Psa 22:23 (H1481C), Psa 33:8 (H1481C), 1Sa 18:15 (H1481C), Deu 32:27 (H1481C)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |
| 1 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 1 | set-aside (is_relevant=0) | _(no VCG; outside programme scope or other reason)_ |  |

---

### Old VCG `291-001` (id=1039) — `SPLIT`

**Old description:** 'Term describes the inner experience of dread or terror under threat — a fear that destabilizes, paralyzes, or consumes the person inwardly'

**Old member verses:** 13 total
  Sample: Job 4:14 (H6342), Deu 28:67 (H6342), Deu 28:66 (H6342), Job 3:25 (H6342), Job 23:15 (H6342), ... +8 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 4 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |
| 2 | active → new | `M01-F-VCG-03` (id=3758) | Sustained dread specifically as a form of divine judgment — unrelenting, consuming anxiety that denies rest, distorts ti |
| 2 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 1 | active → new | `M01-F-VCG-02` (id=3757) | Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner |

---

### Old VCG `291-002` (id=1040) — `SPLIT`

**Old description:** 'Term describes the inner orientation of reverential fear and awe toward God — the fear that is the proper and blessed response to divine majesty, word, and goodness'

**Old member verses:** 6 total
  Sample: Pro 28:14 (H6342), Psa 119:161 (H6342), Jer 33:9 (H6342), Hos 3:5 (H6342), Mic 7:17 (H6342), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 1 | active → new | `M01-A-VCG-02` (id=3727) | Fear of God is identified as the foundational inner orientation from which wisdom, knowledge, and genuine understanding  |
| 1 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |

---

### Old VCG `291-003` (id=1041) — `SPLIT`

**Old description:** 'Term describes the absence or displacement of fear — inner peace, confidence, and security that replaces dread through trust in God'

**Old member verses:** 6 total
  Sample: Psa 27:1 (H6342), Psa 78:53 (H6342), Pro 3:24 (H6342), Isa 12:2 (H6342), Isa 44:8 (H6342), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 2 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 1 | active → new | `M01-F-VCG-05` (id=3760) | A specific form of anticipatory dread characterised by Paul's protective apprehension about the spiritual welfare of his |
| 1 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |

---

### Old VCG `292-001` (id=921) — `SPLIT`

**Old description:** 'Term names the theophanic or miraculous inner fear — the overwhelming inner response to divine presence, miracle, or power, leading to awe and worship'

**Old member verses:** 29 total
  Sample: Mat 17:6 (G5399), Mat 27:54 (G5399), Mat 1:20 (G5399), Mat 9:8 (G5399), Mat 14:27 (G5399), ... +24 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 13 | active → new | `M01-B-VCG-02` (id=3734) | The awe-struck fear produced specifically by witnessing Jesus exercise supernatural power — calming storms, healing, rai |
| 10 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 4 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |
| 1 | active → new | `M01-B-VCG-04` (id=3736) | The reactive inner dread specifically directed at social consequences — crowd opinion, peer pressure, public exposure, s |
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |

---

### Old VCG `292-002` (id=922) — `SPLIT`

**Old description:** 'Term names the reverential fear of God as the inner orientation of godly life — fearing God who judges both body and soul; the inner disposition that shapes worship and ethics'

**Old member verses:** 22 total
  Sample: Act 10:2 (G5399), 1Pe 2:17 (G5399), Luk 1:50 (G5399), Luk 12:5 (G5399), Luk 18:2 (G5399), ... +17 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 14 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 3 | active → new | `M01-A-VCG-03` (id=3728) | Fear of God is presented as the relational posture that aligns a person with God's saving purposes and opens them to his |
| 2 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 1 | active → new | `M01-F-VCG-05` (id=3760) | A specific form of anticipatory dread characterised by Paul's protective apprehension about the spiritual welfare of his |
| 1 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 1 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |

---

### Old VCG `292-003` (id=923) — `SPLIT`

**Old description:** 'Term names the practical or self-interested inner fear before humans or consequences — the inner calculation of social, political, or physical danger that drives action'

**Old member verses:** 32 total
  Sample: Mat 14:5 (G5399), Mat 25:25 (G5399), Mat 2:22 (G5399), Mat 10:26 (G5399), Mat 10:31 (G5399), ... +27 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 11 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 11 | active → new | `M01-B-VCG-04` (id=3736) | The reactive inner dread specifically directed at social consequences — crowd opinion, peer pressure, public exposure, s |
| 4 | active → new | `M01-F-VCG-05` (id=3760) | A specific form of anticipatory dread characterised by Paul's protective apprehension about the spiritual welfare of his |
| 2 | active → new | `M01-G-VCG-01` (id=3761) | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |
| 1 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 1 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |
| 1 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 1 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |

---

### Old VCG `294-002` (id=925) — `SPLIT`

**Old description:** 'Term names the inner terror produced by visions, powers, or threatening presences — the overwhelming inner dread before what is terrifying or incomprehensible'

**Old member verses:** 5 total
  Sample: Dan 4:5 (H1763), Dan 7:7 (H1763), Dan 2:31 (H1763), Dan 5:19 (H1763), Dan 7:19 (H1763)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |

---

### Old VCG `296-001` (id=926) — `SPLIT`

**Old description:** 'Term names the inner condition of fearful dread — the apprehensive inner state before what one fears may befall oneself'

**Old member verses:** 5 total
  Sample: Job 3:25 (H3025), Psa 119:39 (H3025), Deu 9:19 (H3025), Deu 28:60 (H3025), Job 9:28 (H3025)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-F-VCG-02` (id=3757) | Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner |
| 1 | active → new | `M01-F-VCG-03` (id=3758) | Sustained dread specifically as a form of divine judgment — unrelenting, consuming anxiety that denies rest, distorts ti |

---

### Old VCG `298-001` (id=927) — `SPLIT`

**Old description:** "Term names divine command not to fear — the divine assurance 'Fear not / Do not be afraid' addressed to individuals in crisis, granting inner peace through the declaration of divine presence"

**Old member verses:** 65 total
  Sample: Isa 41:10 (H3372G), Isa 43:1 (H3372G), Gen 15:1 (H3372G), Gen 21:17 (H3372G), Gen 26:24 (H3372G), ... +60 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 31 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |
| 21 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 6 | active → new | `M01-B-VCG-05` (id=3737) | Fear as the inner force that directly governs personal decision-making — driving flight, deception, or inaction when lif |
| 4 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 3 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

---

### Old VCG `298-002` (id=928) — `SPLIT`

**Old description:** 'Term names the reverential fear of the Lord as the proper inner orientation — fearing God rather than humans as the inner disposition of covenant loyalty, worship, and moral conduct'

**Old member verses:** 32 total
  Sample: Deu 28:58 (H3372G), 1Ki 8:43 (H3372G), Exo 20:20 (H3372G), 1Ki 8:40 (H3372G), 2Ki 17:25 (H3372G), ... +27 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 13 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 7 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 5 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 2 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |
| 2 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 1 | active → new | `M01-E-VCG-02` (id=3751) | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |
| 1 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |

---

### Old VCG `298-003` (id=929) — `SPLIT`

**Old description:** 'Term names the practical inner fear of threatening powers — the inner condition of dread before enemies, authorities, or circumstances that threaten life or wellbeing'

**Old member verses:** 88 total
  Sample: Gen 3:10 (H3372G), 1Sa 28:5 (H3372G), Gen 18:15 (H3372G), Gen 19:30 (H3372G), Gen 26:7 (H3372G), ... +83 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 42 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 13 | active → new | `M01-A-VCG-05` (id=3730) | These meanings address the direction of fear — the command to fear God and not other objects (enemies, idols, the crowd) |
| 10 | active → new | `M01-B-VCG-05` (id=3737) | Fear as the inner force that directly governs personal decision-making — driving flight, deception, or inaction when lif |
| 7 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |
| 6 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 5 | active → new | `M01-B-VCG-04` (id=3736) | The reactive inner dread specifically directed at social consequences — crowd opinion, peer pressure, public exposure, s |
| 2 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |
| 1 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 1 | active → new | `M01-A-VCG-04` (id=3729) | Fear is the inner response evoked by witnessing or contemplating God's mighty deeds, incomparable greatness, holiness, o |
| 1 | active → new | `M01-C-VCG-05` (id=3744) | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |

---

### Old VCG `305-001` (id=932) — `SPLIT`

**Old description:** 'Term names trembling before divine theophanic presence — the total inner agitation produced by the overwhelming encounter with God'

**Old member verses:** 7 total
  Sample: Exo 19:16 (H2729), Job 37:1 (H2729), Gen 27:33 (H2729), Gen 42:28 (H2729), Exo 19:18 (H2729), ... +2 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 5 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 2 | active → new | `M01-E-VCG-01` (id=3750) | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |

---

### Old VCG `305-002` (id=933) — `SPLIT`

**Old description:** 'Term names trembling in fear before threatening powers or circumstances — the inner agitation of panic and dread'

**Old member verses:** 17 total
  Sample: 1Sa 28:5 (H2729), Isa 19:16 (H2729), Judg 8:12 (H2729), 1Sa 13:7 (H2729), 1Sa 14:15 (H2729), ... +12 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-E-VCG-03` (id=3752) | Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities an |
| 5 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 3 | active → new | `M01-D-VCG-05` (id=3749) | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |
| 2 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 1 | active → new | `M01-B-VCG-05` (id=3737) | Fear as the inner force that directly governs personal decision-making — driving flight, deception, or inaction when lif |

---

### Old VCG `305-003` (id=934) — `SPLIT`

**Old description:** 'Term names the inner condition of promised security — dwelling without trembling; the eschatological rest from fear as the divine gift'

**Old member verses:** 8 total
  Sample: Jer 30:10 (H2729), Lev 26:6 (H2729), Jer 46:27 (H2729), Eze 34:28 (H2729), Eze 39:26 (H2729), ... +3 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 2 | active → new | `M01-E-VCG-03` (id=3752) | Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities an |

---

### Old VCG `306-001` (id=1037) — `SPLIT`

**Old description:** 'Term describes the inward disposition of dread or terror before a threatening force — a fear that collapses resolve and drives flight or paralysis; the commanded opposite of courage'

**Old member verses:** 12 total
  Sample: Job 31:34 (H6206), Deu 20:3 (H6206), Deu 1:29 (H6206), Deu 7:21 (H6206), Deu 31:6 (H6206), ... +7 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 8 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 2 | active → new | `M01-E-VCG-05` (id=3754) | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |
| 2 | active → new | `M01-E-VCG-01` (id=3750) | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |

---

### Old VCG `306-002` (id=1038) — `SPLIT`

**Old description:** 'Term describes the inner orientation of holy reverence and awe before God — the fear that is the proper response to divine majesty and holiness'

**Old member verses:** 3 total
  Sample: Isa 8:13 (H6206), Psa 89:7 (H6206), Isa 29:23 (H6206)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-02` (id=3751) | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |
| 1 | active → new | `M01-E-VCG-06` (id=3755) | NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in w |

---

### Old VCG `307-001` (id=935) — `SPLIT`

**Old description:** 'Term names the inner state of trembling fear — an overwhelming inner agitation produced by the presence of the divine or the terrifying, expressing itself in the body'

**Old member verses:** 3 total
  Sample: Act 7:32 (G1790), Act 16:29 (G1790), Heb 12:21 (G1790)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-01` (id=3750) | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |
| 1 | active → new | `M01-E-VCG-06` (id=3755) | NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in w |

---

### Old VCG `309-001` (id=938) — `SPLIT`

**Old description:** 'Term names the inner condition of overwhelming trembling before the sacred or the divine — the total inner agitation that seizes those at the boundary of the holy'

**Old member verses:** 3 total
  Sample: Gen 27:33 (H2731), Dan 10:7 (H2731), Eze 26:16 (H2731)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 1 | active → new | `M01-E-VCG-01` (id=3750) | The involuntary whole-body trembling produced by direct encounter with the divine presence — at Sinai, in theophanies, a |
| 1 | active → new | `M01-E-VCG-03` (id=3752) | Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities an |

---

### Old VCG `309-002` (id=939) — `SPLIT`

**Old description:** 'Term names the inner condition of panic and dread — the acute inner terror before threatening circumstances, battle, or judgement'

**Old member verses:** 4 total
  Sample: 1Sa 14:15 (H2731), Isa 21:4 (H2731), Pro 29:25 (H2731), Jer 30:5 (H2731)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 1 | active → new | `M01-G-VCG-01` (id=3761) | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |

---

### Old VCG `311-001` (id=1048) — `SPLIT`

**Old description:** 'Term names the inner-somatic trembling that characterises the human response to the presence and power of God — whether as fearful collapse in the guilty or as the posture of reverential worship'

**Old member verses:** 3 total
  Sample: Psa 2:11 (H7461B), Psa 48:6 (H7461B), Isa 33:14 (H7461B)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |
| 1 | active → new | `M01-E-VCG-02` (id=3751) | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |

---

### Old VCG `703-001` (id=250) — `SPLIT`

**Old description:** 'Inner state of dismay — inner person overwhelmed, destabilised, and paralysed by threat, shame, or collapse of what was trusted'

**Old member verses:** 9 total
  Sample: Jer 1:17 (H2865), Job 31:34 (H2865), Job 32:15 (H2865), Isa 20:5 (H2865), Isa 37:27 (H2865), ... +4 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-D-VCG-02` (id=3746) | Dismay inflicted by divine action as a form of judgment or punishment — God actively producing inner collapse in those w |
| 1 | active → new | `M01-D-VCG-04` (id=3748) | Meanings where dismay is explicitly forbidden or countered — Israel or prophets commanded not to be dismayed, with the g |
| 1 | active → new | `M01-D-VCG-01` (id=3745) | Dismay arising from receiving terrible news, witnessing catastrophe, or experiencing the withdrawal of God's presence —  |
| 1 | active → new | `M01-D-VCG-03` (id=3747) | Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, han |

---

### Old VCG `703-002` (id=251) — `SPLIT`

**Old description:** 'Commanded absence of dismay — inner steadiness called for in the face of threat, opposition, or cosmic instability'

**Old member verses:** 7 total
  Sample: Isa 51:7 (H2865), Isa 31:4 (H2865), Jer 10:2 (H2865), Jer 17:18 (H2865), Jer 23:4 (H2865), ... +2 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-D-VCG-04` (id=3748) | Meanings where dismay is explicitly forbidden or countered — Israel or prophets commanded not to be dismayed, with the g |
| 1 | active → new | `M01-D-VCG-02` (id=3746) | Dismay inflicted by divine action as a form of judgment or punishment — God actively producing inner collapse in those w |

---

### Old VCG `703-003` (id=252) — `SPLIT`

**Old description:** "Inner terror induced by divine action — overwhelming of the inner person by God's power or judgment, including awe of covenantal reverence"

**Old member verses:** 5 total
  Sample: Isa 30:31 (H2865), Job 7:14 (H2865), Isa 31:9 (H2865), Jer 49:37 (H2865), Mal 2:5 (H2865)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-D-VCG-02` (id=3746) | Dismay inflicted by divine action as a form of judgment or punishment — God actively producing inner collapse in those w |
| 1 | active → new | `M01-D-VCG-03` (id=3747) | Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, han |
| 1 | active → new | `M01-D-VCG-04` (id=3748) | Meanings where dismay is explicitly forbidden or countered — Israel or prophets commanded not to be dismayed, with the g |

---

### Old VCG `829-001` (id=831) — `SPLIT`

**Old description:** 'Dread of God — the inner terror and trembling before divine majesty'

**Old member verses:** 11 total
  Sample: Psa 119:120 (H6343), Gen 31:42 (H6343), Gen 31:53 (H6343), Job 13:11 (H6343), Job 25:2 (H6343), ... +6 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |
| 3 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |
| 2 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |
| 1 | active → new | `M01-E-VCG-02` (id=3751) | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |
| 1 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 1 | set-aside (is_relevant=0) | _(no VCG; outside programme scope or other reason)_ |  |

---

### Old VCG `829-002` (id=832) — `SPLIT`

**Old description:** 'Dread as anticipated inner terror — the fear that comes upon the heart before disaster'

**Old member verses:** 12 total
  Sample: Job 3:25 (H6343), Deu 28:67 (H6343), Job 4:14 (H6343), Job 22:10 (H6343), Pro 1:26 (H6343), ... +7 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-F-VCG-03` (id=3758) | Sustained dread specifically as a form of divine judgment — unrelenting, consuming anxiety that denies rest, distorts ti |
| 3 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 1 | active → new | `M01-F-VCG-02` (id=3757) | Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner |
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 1 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |

---

### Old VCG `829-003` (id=833) — `SPLIT`

**Old description:** 'Dread falling on enemies — the inner terror of nations before God or his people'

**Old member verses:** 19 total
  Sample: Exo 15:16 (H6343), Deu 2:25 (H6343), Deu 11:25 (H6343), 1Sa 11:7 (H6343), 1Ch 14:17 (H6343), ... +14 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 12 | active → new | `M01-C-VCG-01` (id=3740) | God deploys dread and terror ahead of Israel as an active weapon that paralyses enemy resistance before battle — an exte |
| 3 | active → new | `M01-F-VCG-04` (id=3759) | The specific form of anticipatory dread directed at divine judgment — the inner experience of fearing God as judge, eith |
| 2 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |
| 2 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |

---

### Old VCG `829-004` (id=834) — `SPLIT`

**Old description:** 'The absence or presence of dread as inner moral condition — the wicked without fear of God; the righteous without terror'

**Old member verses:** 5 total
  Sample: Job 21:9 (H6343), Job 39:22 (H6343), Psa 31:11 (H6343), Job 15:21 (H6343), Song 3:8 (H6343)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-F-VCG-05` (id=3760) | A specific form of anticipatory dread characterised by Paul's protective apprehension about the spiritual welfare of his |
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |
| 1 | active → new | `M01-B-VCG-04` (id=3736) | The reactive inner dread specifically directed at social consequences — crowd opinion, peer pressure, public exposure, s |
| 1 | active → new | `M01-B-VCG-05` (id=3737) | Fear as the inner force that directly governs personal decision-making — driving flight, deception, or inaction when lif |
| 1 | active → new | `M01-F-VCG-03` (id=3758) | Sustained dread specifically as a form of divine judgment — unrelenting, consuming anxiety that denies rest, distorts ti |

---

### Old VCG `92-001` (id=737) — `SPLIT`

**Old description:** 'Dismay and terror as overwhelming inner affective state'

**Old member verses:** 27 total
  Sample: Psa 6:3 (H0926), Gen 45:3 (H0926), Exo 15:15 (H0926), Judg 20:41 (H0926), 1Sa 28:21 (H0926), ... +22 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 22 | active → new | `M01-D-VCG-01` (id=3745) | Dismay arising from receiving terrible news, witnessing catastrophe, or experiencing the withdrawal of God's presence —  |
| 3 | active → new | `M01-D-VCG-02` (id=3746) | Dismay inflicted by divine action as a form of judgment or punishment — God actively producing inner collapse in those w |
| 2 | active → new | `M01-D-VCG-05` (id=3749) | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |

---

### Old VCG `107-001` (id=2227) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names anxiety as an inner condition — the weight of worry or anxious concern that burdens the person in the face of threat, uncertainty, or distress'

**Old member verses:** 6 total
  Sample: Pro 12:25 (H1674), Eze 12:18 (H1674), Jos 22:24 (H1674), Jer 49:23 (H1674), Eze 4:16 (H1674), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-F-VCG-01` (id=3756) | Anxiety as a sustained, all-pervasive inner burden that saturates every moment and every ordinary activity — not trigger |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names anxiety as an inner condition — the weight of worry or anxious concern that burdens the person in the face of threat, uncertainty, or distress
- New: Anxiety as a sustained, all-pervasive inner burden that saturates every moment and every ordinary activity — not triggered by a specific anticipated event but settling as a constant companion to daily existence under threat or judgment.
- Co-source(s) into same new VCG: `349-001`, `266-003`

---

### Old VCG `1151-001` (id=2273) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Terror spread in the land of the living — the dread imposed by military powers upon subject populations as an inner-being condition of the dominated'

**Old member verses:** 8 total
  Sample: Eze 32:27 (H2851), Eze 32:32 (H2851), Eze 26:17 (H2851), Eze 32:23 (H2851), Eze 32:24 (H2851), ... +3 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 8 | active → new | `M01-C-VCG-03` (id=3742) | Terror as the defining power wielded by great military empires over the land of the living — projected outward as the in |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Terror spread in the land of the living — the dread imposed by military powers upon subject populations as an inner-being condition of the dominated
- New: Terror as the defining power wielded by great military empires over the land of the living — projected outward as the instrument of domination. In Ezekiel's vision of Sheol, this terror is now silenced: the nations that terrorised the living lie stripped of their dread-power in death.
- Co-source(s) into same new VCG: `1720-001`

---

### Old VCG `1152-001` (id=2274) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Terror as inner experience — the dread felt by the person, whether before God or at the threat of enemies; including terror directed toward and away from the person in relation to divine presence'

**Old member verses:** 4 total
  Sample: Jer 17:17 (H4288), Isa 54:14 (H4288), Pro 21:15 (H4288), Pro 18:7 (H4288)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Terror as inner experience — the dread felt by the person, whether before God or at the threat of enemies; including terror directed toward and away from the person in relation to divine presence
- New: Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent character of God's presence, judgment, and risen power that drives people to hide, flee, or be overwhelmed. These meanings describe what the divine majesty itself does to inner composure when it rises in judgment.
- Co-source(s) into same new VCG: `829-003`, `284-002`, `284-003`, `286-001`, `1723-001`, `1729-001`, `829-001`

---

### Old VCG `1154-001` (id=2270) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Terror as the dashing of hope — the inner experience of terror that arrives where peace and healing were expected; the bitter reversal of inner expectation'

**Old member verses:** 2 total
  Sample: Jer 14:19 (H1205), Jer 8:15 (H1205)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-C-VCG-02` (id=3741) | Terror characterised as an active, hunting, encircling force that overwhelms the inner person with no escape — pursuing  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Terror as the dashing of hope — the inner experience of terror that arrives where peace and healing were expected; the bitter reversal of inner expectation
- New: Terror characterised as an active, hunting, encircling force that overwhelms the inner person with no escape — pursuing relentlessly like a predator, overtaking like a flood, surrounding on every side. These meanings emphasise the agency and relentlessness of the terror itself.
- Co-source(s) into same new VCG: `1156-001`, `286-001`

---

### Old VCG `1155-001` (id=2272) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Divine terror as an inner state fallen upon persons — the God-sent terror that falls on surrounding peoples, producing an inner condition that prevents hostile action'

**Old member verses:** 1 total
  Sample: Gen 35:5 (H2847)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-C-VCG-01` (id=3740) | God deploys dread and terror ahead of Israel as an active weapon that paralyses enemy resistance before battle — an exte |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Divine terror as an inner state fallen upon persons — the God-sent terror that falls on surrounding peoples, producing an inner condition that prevents hostile action
- New: God deploys dread and terror ahead of Israel as an active weapon that paralyses enemy resistance before battle — an externally imposed inner state in the enemies that melts their will and renders them motionless. The terror is explicitly divine in origin and instrumentally purposive: God's dread, not Israel's military strength, defeats the enemy.
- Co-source(s) into same new VCG: `829-003`, `284-001`, `269-003`

---

### Old VCG `1156-001` (id=2269) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Terrors as overwhelming inner assault — plural terrors that attack, chase, overtake, and frighten the inner being, including the terror of deep darkness and the king of terrors'

**Old member verses:** 6 total
  Sample: Job 18:11 (H1091), Job 30:15 (H1091), Job 18:14 (H1091), Job 24:17 (H1091), Job 27:20 (H1091), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-C-VCG-02` (id=3741) | Terror characterised as an active, hunting, encircling force that overwhelms the inner person with no escape — pursuing  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Terrors as overwhelming inner assault — plural terrors that attack, chase, overtake, and frighten the inner being, including the terror of deep darkness and the king of terrors
- New: Terror characterised as an active, hunting, encircling force that overwhelms the inner person with no escape — pursuing relentlessly like a predator, overtaking like a flood, surrounding on every side. These meanings emphasise the agency and relentlessness of the terror itself.
- Co-source(s) into same new VCG: `286-001`, `1154-001`

---

### Old VCG `1158-001` (id=2271) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Sheer terror as the inner response to understanding divine judgement — the trembling dread that arises from comprehension of the divine message'

**Old member verses:** 1 total
  Sample: Isa 28:19 (H2113)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-D-VCG-01` (id=3745) | Dismay arising from receiving terrible news, witnessing catastrophe, or experiencing the withdrawal of God's presence —  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Sheer terror as the inner response to understanding divine judgement — the trembling dread that arises from comprehension of the divine message
- New: Dismay arising from receiving terrible news, witnessing catastrophe, or experiencing the withdrawal of God's presence — the inner collapse of confidence and composure that follows a sudden shattering of the assumed order. The person is overwhelmed, speechless, or undone.
- Co-source(s) into same new VCG: `92-001`, `703-001`

---

### Old VCG `1245-001` (id=2497) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner state of amazement — a filling of the person with wonder in response to a divine act'

**Old member verses:** 1 total
  Sample: Act 3:10 (G2285)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner state of amazement — a filling of the person with wonder in response to a divine act
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `4814-001`, `2-001`, `2-002`, `152-001`, `5157-001`, `240-001`, `289-001`

---

### Old VCG `152-001` (id=751) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Anxiety of spirit as inner affective state'

**Old member verses:** 1 total
  Sample: Dan 7:15 (H3735)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Anxiety of spirit as inner affective state
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `1245-001`, `4814-001`, `2-001`, `2-002`, `5157-001`, `240-001`, `289-001`

---

### Old VCG `1554-002` (id=148) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the somatic terror produced by divine power — the body overwhelmed by the experience of God's glory and judgment"

**Old member verses:** 2 total
  Sample: Hab 3:16 (H7264), Jer 33:9 (H7264)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-04` (id=3753) | Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a cam |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the somatic terror produced by divine power — the body overwhelmed by the experience of God's glory and judgment
- New: Bodily trembling as the expression of military fear-alarm in battle contexts — fear spreading contagiously through a camp or army, producing whole-body shaking as composure collapses under threat.
- Co-source(s) into same new VCG: `298-003`, `305-001`, `305-002`, `305-003`, `309-001`, `309-002`, `306-001`, `282-001`, `1554-003`, `1792-001`, `311-001`

---

### Old VCG `1576-001` (id=155) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the trembling heart as divinely imposed inner instability — inner anxiety and restlessness given by God as a consequence of covenantal displacement'

**Old member verses:** 1 total
  Sample: Deu 28:65 (H7268)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-E-VCG-05` (id=3754) | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the trembling heart as divinely imposed inner instability — inner anxiety and restlessness given by God as a consequence of covenantal displacement
- New: The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involuntarily, hair bristling, flesh trembling as the body enacts what the mind perceives. These meanings foreground the flesh's involuntary response.
- Co-source(s) into same new VCG: `306-001`, `282-001`, `1792-001`, `1713-001`, `1577-001`

---

### Old VCG `1577-001` (id=156) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the prophetically embodied inner state of trembling anxiety — the prophet enacting the inner condition of those under judgment as a sign'

**Old member verses:** 1 total
  Sample: Eze 12:18 (H7269)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-E-VCG-05` (id=3754) | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the prophetically embodied inner state of trembling anxiety — the prophet enacting the inner condition of those under judgment as a sign
- New: The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involuntarily, hair bristling, flesh trembling as the body enacts what the mind perceives. These meanings foreground the flesh's involuntary response.
- Co-source(s) into same new VCG: `306-001`, `282-001`, `1792-001`, `1713-001`, `1576-001`

---

### Old VCG `1692-001` (id=249) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Inner state of intimidation — inner person unsettled by hostile opposition, contrasted with inner steadiness of those whose salvation is secure'

**Old member verses:** 1 total
  Sample: Phili 1:28 (G4426)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Inner state of intimidation — inner person unsettled by hostile opposition, contrasted with inner steadiness of those whose salvation is secure
- New: The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous persons. Fear here is episodic and object-directed: it grips the person at the moment of threat perception, governs their will, and drives either fight, flight, or paralysis. Distinguished from social fear by the physical or mortal character of the threat.
- Co-source(s) into same new VCG: `829-002`, `1681-002`, `829-004`, `276-001`, `291-003`, `284-003`, `290-002`, `292-001`, `292-002`, `292-003`, `294-001`, `294-002`, `298-001`, `298-002`, `298-003`, `305-002`, `1690-001`

---

### Old VCG `1701-001` (id=1015) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of fearful timidity associated with deficient faith — cowardly fear that displaces trust'

**Old member verses:** 2 total
  Sample: Mar 4:40 (G1169), Mat 8:26 (G1169)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-G-VCG-01` (id=3761) | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of fearful timidity associated with deficient faith — cowardly fear that displaces trust
- New: Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that should govern the inner person. These meanings evaluate fear as a deficiency of inner constitution — the disposition that God has not implanted, that faith displaces, and that identifies moral failure.
- Co-source(s) into same new VCG: `292-003`, `309-002`, `288-001`, `1701-002`, `261-001`

---

### Old VCG `1701-002` (id=1016) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names cowardice as a moral inner condition — the fearful person as a moral category alongside the faithless and detestable'

**Old member verses:** 1 total
  Sample: Rev 21:8 (G1169)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-G-VCG-01` (id=3761) | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names cowardice as a moral inner condition — the fearful person as a moral category alongside the faithless and detestable
- New: Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that should govern the inner person. These meanings evaluate fear as a deficiency of inner constitution — the disposition that God has not implanted, that faith displaces, and that identifies moral failure.
- Co-source(s) into same new VCG: `292-003`, `309-002`, `288-001`, `1701-001`, `261-001`

---

### Old VCG `1713-001` (id=1049) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the reverential trembling that others display before a person of authority — an inner-being response of awe and deference'

**Old member verses:** 1 total
  Sample: Hos 13:1 (H7578)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-E-VCG-05` (id=3754) | The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involunta |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the reverential trembling that others display before a person of authority — an inner-being response of awe and deference
- New: The specifically visceral, flesh-level quality of shuddering as dread registers in the body — the body quaking involuntarily, hair bristling, flesh trembling as the body enacts what the mind perceives. These meanings foreground the flesh's involuntary response.
- Co-source(s) into same new VCG: `306-001`, `282-001`, `1792-001`, `1576-001`, `1577-001`

---

### Old VCG `1720-001` (id=163) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the fearsome quality that breeds inner self-deception — pride of heart that trusts in its own terrible reputation rather than God'

**Old member verses:** 1 total
  Sample: Jer 49:16 (H8606)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-C-VCG-03` (id=3742) | Terror as the defining power wielded by great military empires over the land of the living — projected outward as the in |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the fearsome quality that breeds inner self-deception — pride of heart that trusts in its own terrible reputation rather than God
- New: Terror as the defining power wielded by great military empires over the land of the living — projected outward as the instrument of domination. In Ezekiel's vision of Sheol, this terror is now silenced: the nations that terrorised the living lie stripped of their dread-power in death.
- Co-source(s) into same new VCG: `1151-001`

---

### Old VCG `1722-001` (id=1017) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the quality that produces inner awe — the overwhelming, awesome quality of beauty or power that generates wonder-fear'

**Old member verses:** 2 total
  Sample: Song 6:4 (H0366), Song 6:10 (H0366)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-C-VCG-05` (id=3744) | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the quality that produces inner awe — the overwhelming, awesome quality of beauty or power that generates wonder-fear
- New: Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The terror here is a projective force characterising a person or entity as intrinsically awe-inspiring and fear-inducing.
- Co-source(s) into same new VCG: `298-003`, `284-002`, `284-003`, `1722-002`, `1730-001`, `266-003`

---

### Old VCG `1722-002` (id=1018) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the quality that produces inner dread — the terrifying character of an enemy or overwhelming power'

**Old member verses:** 1 total
  Sample: Hab 1:7 (H0366)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-C-VCG-05` (id=3744) | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the quality that produces inner dread — the terrifying character of an enemy or overwhelming power
- New: Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The terror here is a projective force characterising a person or entity as intrinsically awe-inspiring and fear-inducing.
- Co-source(s) into same new VCG: `298-003`, `284-002`, `284-003`, `1722-001`, `1730-001`, `266-003`

---

### Old VCG `1723-001` (id=1019) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names terror as a divinely-imposed inner condition — the overwhelming dread placed upon creatures before a superior power'

**Old member verses:** 2 total
  Sample: Gen 9:2 (H2844A), Job 41:33 (H2844A)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names terror as a divinely-imposed inner condition — the overwhelming dread placed upon creatures before a superior power
- New: Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent character of God's presence, judgment, and risen power that drives people to hide, flee, or be overwhelmed. These meanings describe what the divine majesty itself does to inner composure when it rises in judgment.
- Co-source(s) into same new VCG: `829-003`, `1152-001`, `284-002`, `284-003`, `286-001`, `1729-001`, `829-001`

---

### Old VCG `1729-001` (id=1021) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names terrors — the overwhelming inner fears that beset a person, particularly in the face of mortality and the unknown'

**Old member verses:** 1 total
  Sample: Ecc 12:5 (H2849)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-C-VCG-04` (id=3743) | Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent charac |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names terrors — the overwhelming inner fears that beset a person, particularly in the face of mortality and the unknown
- New: Terror as the quality of divine majesty itself — not deployed as a weapon at Israel's enemies but as the inherent character of God's presence, judgment, and risen power that drives people to hide, flee, or be overwhelmed. These meanings describe what the divine majesty itself does to inner composure when it rises in judgment.
- Co-source(s) into same new VCG: `829-003`, `1152-001`, `284-002`, `284-003`, `286-001`, `1723-001`, `829-001`

---

### Old VCG `1730-001` (id=1022) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the inner alarm that produces withdrawal — the fearful inner response to witnessing another's suffering that causes the observer to pull back"

**Old member verses:** 1 total
  Sample: Job 6:21 (H2866)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-C-VCG-05` (id=3744) | Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner alarm that produces withdrawal — the fearful inner response to witnessing another's suffering that causes the observer to pull back
- New: Terror as a quality radiating from powerful beings or nations outward — producing dread in those who encounter them. The terror here is a projective force characterising a person or entity as intrinsically awe-inspiring and fear-inducing.
- Co-source(s) into same new VCG: `298-003`, `284-002`, `284-003`, `1722-001`, `1722-002`, `266-003`

---

### Old VCG `1732-001` (id=1054) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner confusion and bewilderment of mind that comes as divine judgment — the dissolution of rational orientation in the person'

**Old member verses:** 2 total
  Sample: Deu 28:28 (H8541), Zec 12:4 (H8541)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-D-VCG-04` (id=3748) | Meanings where dismay is explicitly forbidden or countered — Israel or prophets commanded not to be dismayed, with the g |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner confusion and bewilderment of mind that comes as divine judgment — the dissolution of rational orientation in the person
- New: Meanings where dismay is explicitly forbidden or countered — Israel or prophets commanded not to be dismayed, with the grounds given. The characteristic is the interaction between the threat of inner collapse and the word that calls for resilience.
- Co-source(s) into same new VCG: `703-001`, `703-002`, `703-003`

---

### Old VCG `1733-001` (id=1052) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the startled astonishment that overtakes a person before the unexpected and miraculous — an inner-being response of shock at divine intervention'

**Old member verses:** 1 total
  Sample: Dan 3:24 (H8429)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the startled astonishment that overtakes a person before the unexpected and miraculous — an inner-being response of shock at divine intervention
- New: The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe-terror produced by confronting what transcends natural categories. These meanings are characterised by the overwhelming quality of the divine encounter itself, which strikes the inner being with fear that often produces prostration, silence, or paralysis.
- Co-source(s) into same new VCG: `829-003`, `291-001`, `16-001`, `283-001`, `284-001`, `829-001`, `292-001`, `1734-001`, `294-002`, `298-001`, `298-003`, `257-001`, `257-002`, `1690-001`, `266-001`, `266-003`

---

### Old VCG `1734-001` (id=1023) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of dread-filled trembling before God — the fearful, cowering inner posture of those who encounter divine power'

**Old member verses:** 1 total
  Sample: Mic 7:17 (H2119B)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of dread-filled trembling before God — the fearful, cowering inner posture of those who encounter divine power
- New: The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe-terror produced by confronting what transcends natural categories. These meanings are characterised by the overwhelming quality of the divine encounter itself, which strikes the inner being with fear that often produces prostration, silence, or paralysis.
- Co-source(s) into same new VCG: `829-003`, `291-001`, `16-001`, `283-001`, `284-001`, `829-001`, `292-001`, `1733-001`, `294-002`, `298-001`, `298-003`, `257-001`, `257-002`, `1690-001`, `266-001`, `266-003`

---

### Old VCG `1744-001` (id=1050) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term describes the shuddering horror that seizes a person before catastrophic destruction — an inner-being terror expressed in involuntary somatic response'

**Old member verses:** 2 total
  Sample: Eze 27:35 (H8175A), Eze 32:10 (H8175A)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-03` (id=3752) | Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities an |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term describes the shuddering horror that seizes a person before catastrophic destruction — an inner-being terror expressed in involuntary somatic response
- New: Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities and empires, or overwhelming catastrophic events. The trembling here is produced by witnessing — it is the body's register of the horror seen.
- Co-source(s) into same new VCG: `309-001`, `1746-001`, `305-002`, `305-003`

---

### Old VCG `1746-001` (id=1051) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the horror that seizes bystanders witnessing catastrophic divine judgment — an inner-being state of appalled dread before overwhelming destruction'

**Old member verses:** 3 total
  Sample: Job 18:20 (H8178A), Eze 27:35 (H8178A), Eze 32:10 (H8178A)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-E-VCG-03` (id=3752) | Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities an |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the horror that seizes bystanders witnessing catastrophic divine judgment — an inner-being state of appalled dread before overwhelming destruction
- New: Involuntary shuddering and trembling as the inner-bodily response to witnessing destruction, the fall of great cities and empires, or overwhelming catastrophic events. The trembling here is produced by witnessing — it is the body's register of the horror seen.
- Co-source(s) into same new VCG: `309-001`, `1744-001`, `305-002`, `305-003`

---

### Old VCG `2-001` (id=713) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the acute inner distress of the person facing suffering and death — the troubled, anguished state of the inner being at the limit of what it can bear'

**Old member verses:** 2 total
  Sample: Mat 26:37 (G0085), Mar 14:33 (G0085)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the acute inner distress of the person facing suffering and death — the troubled, anguished state of the inner being at the limit of what it can bear
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `1245-001`, `4814-001`, `2-002`, `152-001`, `5157-001`, `240-001`, `289-001`

---

### Old VCG `2-002` (id=714) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner distress arising from relational concern — the person troubled in themselves because of the impact of their condition on those they love'

**Old member verses:** 1 total
  Sample: Phili 2:26 (G0085)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner distress arising from relational concern — the person troubled in themselves because of the impact of their condition on those they love
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `1245-001`, `4814-001`, `2-001`, `152-001`, `5157-001`, `240-001`, `289-001`

---

### Old VCG `240-001` (id=121) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names anguish seizing the person in the moment of mortal extremity — the sudden inner grip of distress in the face of death'

**Old member verses:** 1 total
  Sample: 2Sa 1:9 (H7661)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names anguish seizing the person in the moment of mortal extremity — the sudden inner grip of distress in the face of death
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `1245-001`, `4814-001`, `2-001`, `2-002`, `152-001`, `5157-001`, `289-001`

---

### Old VCG `257-001` (id=885) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names overwhelming inner terror before divine presence or theophanic encounter'

**Old member verses:** 3 total
  Sample: Act 10:4 (G1719), Luk 24:37 (G1719), Luk 24:5 (G1719)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names overwhelming inner terror before divine presence or theophanic encounter
- New: The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe-terror produced by confronting what transcends natural categories. These meanings are characterised by the overwhelming quality of the divine encounter itself, which strikes the inner being with fear that often produces prostration, silence, or paralysis.
- Co-source(s) into same new VCG: `829-003`, `291-001`, `16-001`, `283-001`, `284-001`, `829-001`, `292-001`, `1734-001`, `1733-001`, `294-002`, `298-001`, `298-003`, `257-002`, `1690-001`, `266-001`, `266-003`

---

### Old VCG `257-002` (id=886) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names inner alarm triggered by moral and judicial reality — the fear that arises when confronted with divine judgment or its implications'

**Old member verses:** 2 total
  Sample: Act 24:25 (G1719), Rev 11:13 (G1719)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names inner alarm triggered by moral and judicial reality — the fear that arises when confronted with divine judgment or its implications
- New: The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe-terror produced by confronting what transcends natural categories. These meanings are characterised by the overwhelming quality of the divine encounter itself, which strikes the inner being with fear that often produces prostration, silence, or paralysis.
- Co-source(s) into same new VCG: `829-003`, `291-001`, `16-001`, `283-001`, `284-001`, `829-001`, `292-001`, `1734-001`, `1733-001`, `294-002`, `298-001`, `298-003`, `257-001`, `1690-001`, `266-001`, `266-003`

---

### Old VCG `261-001` (id=891) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** "Term names the inner condition of fearful disturbance — the troubled, afraid state of heart that Christ's peace displaces"

**Old member verses:** 1 total
  Sample: Joh 14:27 (G1168)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-G-VCG-01` (id=3761) | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of fearful disturbance — the troubled, afraid state of heart that Christ's peace displaces
- New: Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that should govern the inner person. These meanings evaluate fear as a deficiency of inner constitution — the disposition that God has not implanted, that faith displaces, and that identifies moral failure.
- Co-source(s) into same new VCG: `309-002`, `288-001`, `1701-001`, `1701-002`, `292-003`

---

### Old VCG `263-001` (id=1042) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the disposition of reverential fear toward God that is owed but absent — the inner orientation Israel has forfeited through apostasy'

**Old member verses:** 1 total
  Sample: Jer 2:19 (H6345)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-A-VCG-01` (id=3726) | Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vul |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the disposition of reverential fear toward God that is owed but absent — the inner orientation Israel has forfeited through apostasy
- New: Fear of God functions as the operative interior force that constrains wrongdoing, motivates ethical treatment of the vulnerable, and produces just conduct where no external court can see. These verses show the fear as an internal judge substituting for external accountability — the sole operative restraint against exploiting the poor, the servant, the neighbour in business, the dependent. God-directed reverence is presented as the only adequate check on the impulse to abuse power.
- Co-source(s) into same new VCG: `1682-004`, `1681-001`, `1681-002`, `269-001`, `269-002`, `298-002`, `292-003`, `1682-001`, `266-002`, `829-001`

---

### Old VCG `267-001` (id=896) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of fear before what is frightening — the intimidated inner state that godly courage displaces'

**Old member verses:** 1 total
  Sample: 1Pe 3:6 (G4423)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of fear before what is frightening — the intimidated inner state that godly courage displaces
- New: Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly named, addressed, and countered by an external word of assurance. These meanings document the commanded release of acute fear grounded in divine presence, promise, or power.
- Co-source(s) into same new VCG: `829-002`, `1681-002`, `298-002`, `298-003`, `291-003`, `297-001`, `292-001`, `292-002`, `292-003`, `298-001`

---

### Old VCG `270-001` (id=900) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the terror that God imposes as an instrument of power — the inner dread placed by God upon peoples, nations, and creatures before his purposes'

**Old member verses:** 6 total
  Sample: Gen 9:2 (H4172A), Deu 11:25 (H4172A), Deu 4:34 (H4172A), Deu 26:8 (H4172A), Deu 34:12 (H4172A), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the terror that God imposes as an instrument of power — the inner dread placed by God upon peoples, nations, and creatures before his purposes
- New: Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characterisation as awesome or fear-inducing through his historical acts. The outward-facing dimension of M01-A: how Israel's God produces reverential fear among the nations through the deeds of the Exodus, the conquest, and later history, with the expectation that all nations will ultimately fear him.
- Co-source(s) into same new VCG: `298-002`, `298-003`, `271-001`, `291-001`, `291-002`, `290-001`, `1682-003`

---

### Old VCG `271-001` (id=902) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the terror that God imposes as an instrument of power — the inner dread placed by God upon peoples, nations, and creatures before his purposes'

**Old member verses:** 6 total
  Sample: Gen 9:2 (H4172B), Deu 11:25 (H4172B), Deu 4:34 (H4172B), Deu 26:8 (H4172B), Deu 34:12 (H4172B), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-A-VCG-07` (id=3732) | Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characteri |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the terror that God imposes as an instrument of power — the inner dread placed by God upon peoples, nations, and creatures before his purposes
- New: Fear of God — or of Israel as God's instrument — divinely instilled in foreign peoples and nations, and God's characterisation as awesome or fear-inducing through his historical acts. The outward-facing dimension of M01-A: how Israel's God produces reverential fear among the nations through the deeds of the Exodus, the conquest, and later history, with the expectation that all nations will ultimately fear him.
- Co-source(s) into same new VCG: `298-002`, `298-003`, `270-001`, `291-001`, `291-002`, `290-001`, `1682-003`

---

### Old VCG `272-001` (id=904) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner fears that become the instrument of divine judgement — what the faithless dread is brought upon them as the consequence of their rejection'

**Old member verses:** 1 total
  Sample: Isa 66:4 (H4035)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-F-VCG-02` (id=3757) | Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner fears that become the instrument of divine judgement — what the faithless dread is brought upon them as the consequence of their rejection
- New: Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner anticipatory anguish that proves accurate. The feared event arrives and confirms the dread.
- Co-source(s) into same new VCG: `829-002`, `273-001`, `296-001`, `291-001`

---

### Old VCG `273-001` (id=905) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of fearful dread — the fears that oppress the person, whether delivered by God or brought upon oneself by wickedness'

**Old member verses:** 2 total
  Sample: Psa 34:4 (H4034), Pro 10:24 (H4034)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-F-VCG-02` (id=3757) | Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of fearful dread — the fears that oppress the person, whether delivered by God or brought upon oneself by wickedness
- New: Dread as a forward-looking inner state that precedes and then corresponds to the actual suffering feared — fear as inner anticipatory anguish that proves accurate. The feared event arrives and confirms the dread.
- Co-source(s) into same new VCG: `829-002`, `272-001`, `296-001`, `291-001`

---

### Old VCG `276-001` (id=908) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of fear before a powerful enemy — those whose power generates inner dread in the one who faces them'

**Old member verses:** 2 total
  Sample: Jer 39:17 (H3016), Jer 22:25 (H3016)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of fear before a powerful enemy — those whose power generates inner dread in the one who faces them
- New: The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous persons. Fear here is episodic and object-directed: it grips the person at the moment of threat perception, governs their will, and drives either fight, flight, or paralysis. Distinguished from social fear by the physical or mortal character of the threat.
- Co-source(s) into same new VCG: `829-002`, `1681-002`, `829-004`, `291-003`, `284-003`, `290-002`, `292-001`, `292-002`, `292-003`, `294-001`, `294-002`, `298-001`, `298-002`, `298-003`, `305-002`, `1690-001`, `1692-001`

---

### Old VCG `279-001` (id=1045) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner state of panic that seizes the person or community, immobilizing composure and overthrowing resolve'

**Old member verses:** 1 total
  Sample: Jer 49:24 (H7374)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-D-VCG-05` (id=3749) | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner state of panic that seizes the person or community, immobilizing composure and overthrowing resolve
- New: Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hasty inner drive rather than the shattering of composure. Includes Ecclesiastes corpus of rashness before God and kings, and the panic that dissolves military resolve.
- Co-source(s) into same new VCG: `92-001`, `92-002`, `305-002`, `1554-001`, `1554-003`

---

### Old VCG `283-001` (id=913) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner state of overwhelming terror before divine presence — the total inner overturn of the person in the face of the holy'

**Old member verses:** 2 total
  Sample: Heb 12:21 (G1630), Mar 9:6 (G1630)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-B-VCG-01` (id=3733) | The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner state of overwhelming terror before divine presence — the total inner overturn of the person in the face of the holy
- New: The immediate, involuntary inner response to direct encounter with God, angelic beings, or supernatural reality — an awe-terror produced by confronting what transcends natural categories. These meanings are characterised by the overwhelming quality of the divine encounter itself, which strikes the inner being with fear that often produces prostration, silence, or paralysis.
- Co-source(s) into same new VCG: `829-003`, `291-001`, `16-001`, `284-001`, `829-001`, `292-001`, `1734-001`, `1733-001`, `294-002`, `298-001`, `298-003`, `257-001`, `257-002`, `1690-001`, `266-001`, `266-003`

---

### Old VCG `288-001` (id=918) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner spirit of timidity — the fearful, cowardly disposition that God has not given, contrasted with power, love, and self-control'

**Old member verses:** 1 total
  Sample: 2Ti 1:7 (G1167)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-G-VCG-01` (id=3761) | Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that shou |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner spirit of timidity — the fearful, cowardly disposition that God has not given, contrasted with power, love, and self-control
- New: Cowardly, faithless inner shrinking that is morally condemned or contrasted with the peace, faith, and courage that should govern the inner person. These meanings evaluate fear as a deficiency of inner constitution — the disposition that God has not implanted, that faith displaces, and that identifies moral failure.
- Co-source(s) into same new VCG: `292-003`, `309-002`, `1701-001`, `1701-002`, `261-001`

---

### Old VCG `289-001` (id=1053) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term describes the inner astonishment, wonder, or stupefaction that overwhelms a person before the extraordinary acts of God or the collapse of expected order'

**Old member verses:** 7 total
  Sample: Hab 1:5 (H8539), Gen 43:33 (H8539), Psa 48:5 (H8539), Ecc 5:8 (H8539), Isa 13:8 (H8539), ... +2 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 7 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term describes the inner astonishment, wonder, or stupefaction that overwhelms a person before the extraordinary acts of God or the collapse of expected order
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `1245-001`, `4814-001`, `2-001`, `2-002`, `152-001`, `5157-001`, `240-001`

---

### Old VCG `290-002` (id=920) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names inner dread before a threatening power — the practical fear of persons, nations, or forces that can harm'

**Old member verses:** 6 total
  Sample: Num 22:3 (H1481C), Deu 1:17 (H1481C), Deu 18:22 (H1481C), Job 19:29 (H1481C), Job 41:25 (H1481C), ... +1 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 6 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names inner dread before a threatening power — the practical fear of persons, nations, or forces that can harm
- New: The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous persons. Fear here is episodic and object-directed: it grips the person at the moment of threat perception, governs their will, and drives either fight, flight, or paralysis. Distinguished from social fear by the physical or mortal character of the threat.
- Co-source(s) into same new VCG: `829-002`, `1681-002`, `829-004`, `276-001`, `291-003`, `284-003`, `292-001`, `292-002`, `292-003`, `294-001`, `294-002`, `298-001`, `298-002`, `298-003`, `305-002`, `1690-001`, `1692-001`

---

### Old VCG `294-001` (id=924) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names commanded reverence before God — the inner orientation of trembling fear before the living God, imposed by royal decree'

**Old member verses:** 1 total
  Sample: Dan 6:26 (H1763)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-03` (id=3735) | The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous p |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names commanded reverence before God — the inner orientation of trembling fear before the living God, imposed by royal decree
- New: The reactive inner dread triggered by specific human threats — armies, powerful rulers, armed opponents, and dangerous persons. Fear here is episodic and object-directed: it grips the person at the moment of threat perception, governs their will, and drives either fight, flight, or paralysis. Distinguished from social fear by the physical or mortal character of the threat.
- Co-source(s) into same new VCG: `829-002`, `1681-002`, `829-004`, `276-001`, `291-003`, `284-003`, `290-002`, `292-001`, `292-002`, `292-003`, `294-002`, `298-001`, `298-002`, `298-003`, `305-002`, `1690-001`, `1692-001`

---

### Old VCG `297-001` (id=1044) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner disposition of fear that is commanded against in the context of divine reassurance and the uniqueness of God'

**Old member verses:** 1 total
  Sample: Isa 44:8 (H7297)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-06` (id=3738) | Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly  |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner disposition of fear that is commanded against in the context of divine reassurance and the uniqueness of God
- New: Meanings where the primary content is the divine or authoritative command to cease fear — the inner fear being directly named, addressed, and countered by an external word of assurance. These meanings document the commanded release of acute fear grounded in divine presence, promise, or power.
- Co-source(s) into same new VCG: `829-002`, `267-001`, `1681-002`, `298-002`, `298-003`, `291-003`, `292-001`, `292-002`, `292-003`, `298-001`

---

### Old VCG `308-001` (id=936) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of awe-filled trembling before divine encounter — the overwhelming inner agitation that seizes those at the boundary of the sacred'

**Old member verses:** 1 total
  Sample: Mar 16:8 (G5156)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-E-VCG-06` (id=3755) | NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in w |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of awe-filled trembling before divine encounter — the overwhelming inner agitation that seizes those at the boundary of the sacred
- New: NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in working out salvation, in Paul's vulnerable ministry. This is trembling not as terror but as the appropriate somatic gravity of serious engagement with divine things.
- Co-source(s) into same new VCG: `308-002`, `306-002`, `307-001`

---

### Old VCG `308-002` (id=937) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner disposition of trembling reverential fear in godly service — the humble, dependent inner attitude that characterises authentic Christian obedience and ministry'

**Old member verses:** 4 total
  Sample: Phili 2:12 (G5156), Eph 6:5 (G5156), 1Cor 2:3 (G5156), 2Cor 7:15 (G5156)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-E-VCG-06` (id=3755) | NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in w |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner disposition of trembling reverential fear in godly service — the humble, dependent inner attitude that characterises authentic Christian obedience and ministry
- New: NT trembling as the bodily-emotional tone of reverent, serious engagement — in worship, in receiving God's servant, in working out salvation, in Paul's vulnerable ministry. This is trembling not as terror but as the appropriate somatic gravity of serious engagement with divine things.
- Co-source(s) into same new VCG: `308-001`, `306-002`, `307-001`

---

### Old VCG `310-001` (id=940) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of trembling at the word of God — the responsive, reverent trembling that characterises the person God looks upon with favour'

**Old member verses:** 4 total
  Sample: Isa 66:2 (H2730), Ezr 9:4 (H2730), Ezr 10:3 (H2730), Isa 66:5 (H2730)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-E-VCG-02` (id=3751) | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of trembling at the word of God — the responsive, reverent trembling that characterises the person God looks upon with favour
- New: The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communication, qualifying a person for covenant leadership and forming a community identity. This trembling is not involuntary terror but chosen reverential sobriety before the divine word.
- Co-source(s) into same new VCG: `298-002`, `310-002`, `306-002`, `1793-001`, `311-001`, `829-001`

---

### Old VCG `310-002` (id=941) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Term names the inner condition of fearful trembling before threatening circumstances or the sacred — the inner agitation of fear or reverent anxiety'

**Old member verses:** 2 total
  Sample: Judg 7:3 (H2730), 1Sa 4:13 (H2730)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-E-VCG-02` (id=3751) | The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communi |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Term names the inner condition of fearful trembling before threatening circumstances or the sacred — the inner agitation of fear or reverent anxiety
- New: The distinctive trembling-at-God's-word tradition — trembling as a mark of genuine inner responsiveness to God's communication, qualifying a person for covenant leadership and forming a community identity. This trembling is not involuntary terror but chosen reverential sobriety before the divine word.
- Co-source(s) into same new VCG: `298-002`, `310-001`, `306-002`, `1793-001`, `311-001`, `829-001`

---

### Old VCG `349-001` (id=219) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Anxious unsettling thoughts pressing upon the heart — inner person as site of accumulated care and disturbance'

**Old member verses:** 2 total
  Sample: Psa 94:19 (H8312), Psa 139:23 (H8312)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 2 | active → new | `M01-F-VCG-01` (id=3756) | Anxiety as a sustained, all-pervasive inner burden that saturates every moment and every ordinary activity — not trigger |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Anxious unsettling thoughts pressing upon the heart — inner person as site of accumulated care and disturbance
- New: Anxiety as a sustained, all-pervasive inner burden that saturates every moment and every ordinary activity — not triggered by a specific anticipated event but settling as a constant companion to daily existence under threat or judgment.
- Co-source(s) into same new VCG: `107-001`, `266-003`

---

### Old VCG `4814-001` (id=294) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Inner experience of being overwhelmed — waves of death, divine wrath, or affliction passing through the inner person, threatening to engulf completely'

**Old member verses:** 4 total
  Sample: Psa 42:7 (H4867), 2Sa 22:5 (H4867), Psa 88:7 (H4867), Jon 2:3 (H4867)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Inner experience of being overwhelmed — waves of death, divine wrath, or affliction passing through the inner person, threatening to engulf completely
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `1245-001`, `2-001`, `2-002`, `152-001`, `5157-001`, `240-001`, `289-001`

---

### Old VCG `5126-001` (id=721) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Utter astonishment as inner affective response'

**Old member verses:** 1 total
  Sample: Act 3:11 (G1569)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-B-VCG-02` (id=3734) | The awe-struck fear produced specifically by witnessing Jesus exercise supernatural power — calming storms, healing, rai |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Utter astonishment as inner affective response
- New: The awe-struck fear produced specifically by witnessing Jesus exercise supernatural power — calming storms, healing, raising the dead, walking on water, casting out demons. These meanings form a distinct NT phenomenon: fear as the immediate communal inner response that precedes and accompanies the dawning recognition of who Jesus is. The fear is not paralysing but question-raising.
- Co-source(s) into same new VCG: `16-001`, `292-001`, `266-001`

---

### Old VCG `5157-001` (id=759) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Oppressive pressure as experienced inner-bearing condition'

**Old member verses:** 1 total
  Sample: Psa 55:3 (H6125)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-BOUNDARY-VCG-01` (id=3739) | Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mis |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Oppressive pressure as experienced inner-bearing condition
- New: Terms held for researcher decision at Phase 12: ta.mah (astonishment-bewilderment split), sha.vats (agony of dying), mish.bar (waves of divine pressure), a.qah (crushed by hostile force), sar.ap.pim (anxious ruminating thoughts), ke.ra (spirit-level distress), ademoneo (anguished heaviness), thambos (pure wonder), za.a.vah, sham.mah, a.ruts, pa.lats (empty corpora). These verses cannot be analytically designed into VCGs until the researcher resolves the underlying analytical questions.
- Co-source(s) into same new VCG: `1245-001`, `4814-001`, `2-001`, `2-002`, `152-001`, `240-001`, `289-001`

---

### Old VCG `5187-001` (id=739) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Alarm, anxiety and troubled thoughts as inner affective state'

**Old member verses:** 7 total
  Sample: Dan 7:15 (H0927), Dan 4:5 (H0927), Dan 4:19 (H0927), Dan 5:6 (H0927), Dan 5:9 (H0927), ... +2 more

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 7 | active → new | `M01-D-VCG-03` (id=3747) | Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, han |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Alarm, anxiety and troubled thoughts as inner affective state
- New: Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, hands paralysed. These meanings emphasise the radical interiority-to-exteriority dynamic: the inner collapse is so complete it writes itself on the body.
- Co-source(s) into same new VCG: `703-001`, `703-003`, `5187-002`

---

### Old VCG `5187-002` (id=740) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Urgent haste as expression of inner alarm or urgency'

**Old member verses:** 3 total
  Sample: Dan 3:24 (H0927), Dan 2:25 (H0927), Dan 6:19 (H0927)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 3 | active → new | `M01-D-VCG-03` (id=3747) | Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, han |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Urgent haste as expression of inner alarm or urgency
- New: Dismay characterised by its visible bodily effects — color change, limbs giving way, knees knocking, speechlessness, hands paralysed. These meanings emphasise the radical interiority-to-exteriority dynamic: the inner collapse is so complete it writes itself on the body.
- Co-source(s) into same new VCG: `703-001`, `5187-001`, `703-003`

---

### Old VCG `704-001` (id=246) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Reverent awe as fitting inner disposition for worship of God'

**Old member verses:** 1 total
  Sample: Heb 12:28 (G6015)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 1 | active → new | `M01-A-VCG-06` (id=3731) | Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and ma |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Reverent awe as fitting inner disposition for worship of God
- New: Fear of God as the sustained inner orientation that defines a person's identity, governs their whole way of life, and marks the community of the faithful — transmitted across generations, constitutive of covenant relationship, defining the person who is acceptable to God. This is the enduring, generational, communal dimension of fear-of-God.
- Co-source(s) into same new VCG: `1682-004`, `269-001`, `269-002`, `298-002`, `270-002`, `271-002`, `266-002`, `829-001`, `266-003`, `292-002`, `292-003`, `1682-001`, `1682-002`, `1682-003`

---

### Old VCG `92-002` (id=738) — `KEEP-EQUIVALENT-OF-MERGE`

**Old description:** 'Rashness and hasty inner disposition'

**Old member verses:** 4 total
  Sample: Ecc 7:9 (H0926), Ecc 5:2 (H0926), Ecc 8:3 (H0926), Pro 28:22 (H0926)

**End-state distribution of old members:**

| Verses | End state | Target | Description excerpt |
|---:|---|---|---|
| 4 | active → new | `M01-D-VCG-05` (id=3749) | Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hast |

**Side-by-side QA (KEEP-EQUIVALENT-OF-MERGE):**

- Old: Rashness and hasty inner disposition
- New: Inner agitation in the sense of rashness, impulsive urgency, or panic-driven flight — the ba.hal meanings that name hasty inner drive rather than the shattering of composure. Includes Ecclesiastes corpus of rashness before God and kings, and the panic that dissolves military resolve.
- Co-source(s) into same new VCG: `92-001`, `305-002`, `1554-001`, `279-001`, `1554-003`

---

## 4. Researcher approval

- Eligible for soft-delete on approval: **115** inherited VCGs
- Blocked (UNROUTED — fix Phase 7 follow-up first): **0** inherited VCGs

Approve dissolution by selecting one of the following:

- ☐ **Approve all eligible** — soft-delete all non-UNROUTED inherited VCGs (preferred)
- ☐ **Approve selectively** — list any eligible VCG ids to retain past dissolution: __________
- ☐ **Pause** — researcher will review individual cases before approval

On approval, CC executes `wa-cluster-{code}-dir-NNN-vcg-dissolve-v1-{date}.md` which soft-deletes the approved inherited VCGs + their `vcg_term` links.

*End of comparison report.*