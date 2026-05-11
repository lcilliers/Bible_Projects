# wa-cluster-M26-dir-003-A2-vsg-restructure-v1-20260510

**Directive ID:** DIR-M26-20260510-003  
**Prepared by:** Claude AI  
**Date:** 2026-05-10  
**Cluster:** M26 — Righteousness and Justice  
**Sub-group:** M26-A2 — Human Righteousness — State of being right  
**Governed by:** wa-directive-instruction-v1_4-20260506 §11 (Cluster-process directives)  
**Source document:** WA-M26A2-vsg-actions-v1_0-20260510.md (Actions 001–015)  

---

## DIRECTIVE ID

DIR-M26-20260510-003

---

## MOTIVATION

A verse-by-verse reading of all M26-A2 verse context groups (VSGs) against the human righteousness analysis established in `WA-M26A-human-righteousness-by-term-v1_0-20260509.md` revealed that the existing VSG structure was built without reading individual verses. The prior VSGs classified by broad category, resulting in:

- VSG descriptions applied to verses whose content does not match the description
- Verses describing God's attribute or national/royal governance sitting in a human inner-being sub-group
- Distinct analytical dimensions collapsed into single catch-all groups (notably `3246-001` absorbing 107 verses across 9 different meaning patterns)
- Category errors (counterfeit righteousness placed alongside genuine righteousness; absence placed alongside presence)

This directive restructures the entire M26-A2 VSG layer. It is the largest single restructuring operation in the M26 analytical pass. CC must execute the four operational phases in sequence, confirming counts after each phase before proceeding.

---

## SCOPE

**Tables affected:**
- `verse_context_group` — UPDATE (descriptions), INSERT (new groups), soft-deactivate (dissolved/removed)
- `verse_context` — UPDATE (subgroup/group reassignment for individual verse rows)

**Cluster:** M26  
**Sub-group primary scope:** M26-A2  
**Secondary scope:** M26-BOUNDARY (BOUNDARY receives verses), M26-A1 (receives 1 verse)

---

## OUTCOME REQUIRED — FOUR PHASES

---

### PHASE 1 — Remove misplaced VSGs from M26-A2 listing

The following VSGs currently appear in the M26-A2 VSG listing but their descriptions name divine or institutional attributes, not human inner-being righteousness. They should not appear in M26-A2.

**VSGs to remove from M26-A2 scope:**

| Group code | Term | Reason |
|-----------|------|--------|
| `3193-002` | G1342 dikaios | Description: "divine inner attribute of perfect moral justice" — belongs in M26-A1 |
| `942-002` | H6664G tse.deq | Description: "righteousness as attribute of God" — belongs in M26-A1 |
| `942-004` | H6664G tse.deq | Description: "moral basis for just governance — kings, judges, rulers" — belongs in BOUNDARY |
| `911-003` | H6666 tse.da.qah | Description: "divine character quality received" — belongs in M26-A1; its 2 M26-A2 verses are reassigned in Phase 3 |
| `950-003` | G1343 dikaiosune | Dissolved — all 5 verses merged into other groups in Phase 3 |

**Operation:** CC to confirm these group codes are no longer listed as active M26-A2 VSGs after Phase 1. Their verses in M26-A1 and BOUNDARY are unaffected.

**Note on vr_id 93812 (Rom 1:17, G1342 dikaios):** Currently the only M26-A2 verse assigned to `3193-002`. This verse is reassigned in Phase 3 (to NEW-06 hunger/pursuit group). Do not lose it.

---

### PHASE 2 — Rename 8 existing VSGs with new descriptions

Update `context_description` (or equivalent description field) on the following `verse_context_group` rows. Match on `group_code` within cluster M26. CC must verify the group exists before updating.

---

#### 2.1 — Group `911-001` (H6666 tse.da.qah)

**New description:**
> Term names righteousness as a personal inner possession — held fast, carried in the heart, expressed in the whole manner of life. The person's righteousness is their own, concerns themselves (Job 35:8), and does not reproach them (Job 27:6). It is evidenced in walking before God in faithfulness and uprightness of heart (1Ki 3:6), in walking and speaking rightly and despising bribes (Isa 33:15), and in doing righteousness consistently at all times (Psa 106:3). Inner and outer correspondence is the defining quality.

**Retain in group:** vr_ids 25210, 25212, 25167, 25174, 169240, 169297  
**Anchor verse:** vr_id 25210 (Job 27:6) — set `is_anchor = 1`  
All other verses currently in `911-001` are reassigned in Phase 3.

---

#### 2.2 — Group `911-002` (H6666 tse.da.qah)

**New description:**
> Term names righteousness as a personal moral standing that God sees and rewards — the inner condition of the person that God assesses, vindicates, and repays according to faithfulness.

**Retain in group:** vr_ids 169247, 169248, 169243  
**Anchor verse:** vr_id 169247 (2Sa 22:21)  
All other verses currently in `911-002` are reassigned in Phase 3.

---

#### 2.3 — Group `942-001` (H6664G tse.deq)

**New description:**
> Term names the person's righteousness as a personal moral standing before God — the inner condition appealed to in prayer, claimed before divine judgment, and rewarded by God when genuine. The person stands in righteousness before God as an established inner reality they can invoke and be assessed by.

**Retain in group:** vr_ids 96028, 96007, 96009, 96010, 95994, 28342, 28344, 28340  
**Anchor verse:** vr_id 96028 (Psa 7:8)  
All other verses currently in `942-001` are reassigned in Phase 3.

---

#### 2.4 — Group `942-003` (H6664G tse.deq)

**New description:**
> Term names righteousness as an inner orientation actively pursued — seeking the Lord and righteousness together (Isa 51:1), commanded alongside humility and doing God's commands (Zep 2:3). Active seeking is the defining posture.

**Retain in group:** vr_ids 28324, 96041  
**Anchor verse:** vr_id 28324 (Isa 51:1)  
Verses 96005 and 28326 are reassigned in Phase 3.

---

#### 2.5 — Group `950-001` (G1343 dikaiosune)

**New description:**
> Term names righteousness received through faith — credited and counted by God to the person who trusts. The Abraham pattern: belief counted as righteousness, received not earned, grounded in trust not works. The standing is conferred through faith and sealed by it.

**Retain in group:** vr_ids 28759, 28760, 28762, 28756, 28757, 28758, 28763, 28736, 28740, 93731  
**Add to group from 950-003:** vr_ids 28771, 28737  
**Anchor verse:** vr_id 28760 (Rom 4:5)  
Verses 28734, 28735, 28743 are reassigned in Phase 3.

---

#### 2.6 — Group `950-002` (G1343 dikaiosune)

**New description:**
> Term names righteousness as a practiced, lived orientation — ongoing conduct before God expressed in active service, progressive sanctification, and formable through scripture and discipline. Not a one-time standing but a daily life-direction.

**Retain in group:** vr_ids 93734, 93726, 28766, 93724, 28741, 28739  
**Add to group from 950-003:** vr_id 28745  
**Anchor verse:** vr_id 93734 (Luk 1:75)  
Verses 93739, 93738, 93722, 93723, 28730, 28729, 93742, 28731, 28733, 93740, 93735, 93743, 93745 are reassigned in Phase 3.

---

#### 2.7 — Group `3246-002` (H6662 tsad.diq)

**New description:**
> Term names the righteous person as the direct object of God's relational attention — seen, tested, known, loved, upheld, delivered, and heard. God's engagement with the righteous person is personal and active: he does not withdraw his eyes (Job 36:7), his ears are open to their cry (Psa 34:15), and he will never permit them to be moved (Psa 55:22). The righteous person's standing is real and God responds to it specifically.

**Retain in group:** vr_ids 169370, 169463, 169496, 169465, 169484, 169485, 169489, 169495, 169498, 169500, 169480, 169396, 169388, 169439  
**Anchor verse:** vr_id 169484 (Psa 34:15)  
All other verses currently in `3246-002` are reassigned in Phase 3.

---

#### 2.8 — Group `3246-003` (H6662 tsad.diq)

**New description:**
> Term names the characteristic inner response of the righteous person toward God — gladness, exultation, praise, thanksgiving, and joy when justice is enacted. These are not incidental emotions but the natural orientation of the righteous inner being toward God. Joy is fitting for the righteous (Psa 33:1); it arises from the person's own relationship with God and from witnessing divine justice.

**Retain in group:** vr_ids 169392, 169482, 169483, 169497, 169499, 169501, 169502, 169510, 169511, 169470, 169476, 169478, 169449  
**Anchor verse:** vr_id 169482 (Psa 32:11)  
Verses 169443, 169452 are reassigned in Phase 3.

---

### PHASE 3 — Create 17 new verse context groups in M26-A2

INSERT 17 new `verse_context_group` rows. CC assigns group codes following the existing pattern for the relevant term (e.g. `911-004`, `942-005`, `3246-004` etc. — CC to determine next available code per term). Record the assigned codes for Phase 4 verification.

---

#### NEW-01 — Proverbs outcomes: righteousness producing life outcomes  
**Term:** H6666 tse.da.qah (mti_id 911)

**Description:**
> Term names righteousness as a governing quality whose presence produces measurable life outcomes — deliverance from death, stability of the way, sure reward, honour, and enduring legacy. Righteousness is not described here as an inner disposition to be cultivated but as a quality already operative whose consequences are stated. Contrasted consistently with wickedness whose outcomes are death and captivity.

**Anchor verse:** vr_id 169282 (Pro 11:5) — set `is_anchor = 1`

**Assign these verse_context rows to this new group:**

*From former `911-001`:*
169278, 169281, 169282, 169283, 169279, 169280, 169287, 169290, 169289, 169291, 169301, 169302

*From former `3246-001` (H6662 — same meaning pattern):*
169409, 169413, 169414, 169403, 169408, 169421, 169422, 169415, 169416, 169417, 169419, 169430, 169431, 169432, 169433, 169436, 169440, 169442, 169450, 169453, 169459, 169491, 169492, 169406, 169435, 169458, 169507, 169379, 169506, 169447, 169393, 169488, 169426

**Note:** These are vr_ids from two different terms (H6666 and H6662). CC should verify the correct mti_term_id linkage for each verse_context row before assigning to this group. Group covers the shared meaning pattern across both terms.

---

#### NEW-02 — Ezekiel precarious standing  
**Term:** H6666 tse.da.qah (mti_id 911) and H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names righteousness as a dynamic personal standing that must be maintained and can be forfeited. The righteous person who turns from righteousness and does injustice loses the standing and dies; none of their prior righteous deeds are remembered (Eze 33:13). The wicked person who turns and does what is just and right receives life. Righteousness here is non-transferable and non-accumulative — assessed at the point of turning, not across a lifetime. This is the OT's most developed treatment of the inner mechanics of righteousness.

**Anchor verse:** vr_id 169271 (Eze 33:13) — set `is_anchor = 1`

**Assign these verse_context rows:**

*From former `911-001` (ACTION-008c):*
169269, 169268, 169261, 169263, 169265, 169266, 169267, 169270, 169271, 169272, 169273, 169274, 169275

*From former `911-002` (ACTION-009b):*
169259, 169260, 169262, 169264

*From former `3246-001` (ACTION-015i):*
169357, 169349, 169350, 169351, 169359, 169360, 169361, 169352, 169456

*From former `942-001` (ACTION-013h):*
95981

**Duplicate flag:** vr_id 95981 (Eze 3:20, H6664G) and vr_id 169357 (Eze 3:20, H6662) are the same biblical verse under different terms. Both should be in this group. CC to confirm both exist and are distinct rows.

---

#### NEW-03 — Absence, distortion and counterfeit righteousness  
**Term:** H6666 tse.da.qah, G1343 dikaiosune, H6662 tsad.diq

**Description:**
> Term names the failure, distortion, or counterfeit form of righteousness — righteous deeds that are polluted and cannot stand before God; swearing by God's name but not in righteousness; seeking God in outward form while absent inwardly; righteousness that does not profit; self-assessed righteousness producing contempt; law-righteousness that is rubbish compared to God's; outward appearance concealing inner lawlessness. Together these verses define what genuine righteousness is by showing what it is not.

**Anchor verse:** vr_id 25201 (Isa 64:6) — set `is_anchor = 1`

**Assign these verse_context rows:**

*From former `911-001` — Isaiah absence cluster (ACTION-008d):*
25201, 25181, 25182, 25192, 25185

*From former `911-002` (ACTION-009c):*
25191

*From former `950-001` — law-righteousness impossible (ACTION-010b):*
28734, 28735

*From former `950-002` — NT counterfeit cluster (ACTION-011e):*
93740, 93735, 93743, 93745

*From former `942-001` (ACTION-013g):*
28327

*From former `3246-001` (ACTION-015j):*
169394

**Duplicate flag:** vr_id 28327 (Isa 58:2, H6664G) and vr_id 25192 (Isa 58:2, H6666) are the same biblical verse under different terms. Both should be in this group. CC to confirm both exist as distinct rows.

---

#### NEW-04 — Far from righteousness  
**Term:** H6666 tse.da.qah (mti_id 911)

**Description:**
> Term names the condition of being far from or lacking righteousness — the human person or community described as distant from the righteous state, hoping for it but not possessing it. Stubbornness of heart is named as the inner cause of the distance (Isa 46:12); the absence is experienced as darkness and the failure of justice (Isa 59:9). An OT parallel to the NT declaration of universal absence (Rom 3:10), but expressed as a particular condition rather than a universal category.

**Anchor verse:** vr_id 25179 (Isa 46:12) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `911-003`):
25179, 25196

---

#### NEW-05 — Righteousness internalised in the heart  
**Term:** H6664G tse.deq (mti_id 942)

**Description:**
> Term names righteousness as already known and carried in the heart as law. The person addressed is defined by this knowing: righteousness is not something they are seeking but something they already are and have. The internalised state produces courage in the face of reproach. Distinct from righteousness as active pursuit (942-003) and from righteousness as outward expression (942-001).

**Anchor verse:** vr_id 28326 (Isa 51:7) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `942-003`):
28326

---

#### NEW-06 — Hunger and active pursuit of righteousness  
**Term:** G1343 dikaiosune (mti_id 950)

**Description:**
> Term names righteousness as the object of active inner longing and deliberate pursuit — hungered for, thirsted for, fled toward. The righteous person is defined by the direction of inner desire. The degree of righteousness matters (exceeding the scribes and Pharisees). Pursuit is commanded, implying the state is not yet fully arrived at but is the defining goal of the inner person.

**Anchor verse:** vr_id 93739 (Mat 5:6) — set `is_anchor = 1`

**Assign these verse_context rows:**

*From former `950-002` (ACTION-011b):*
93739, 93738, 93722, 93723

*Also assign:* vr_id 93812 (Rom 1:17, G1342 dikaios) — currently assigned to `3193-002` in M26-A2; this verse describes "the righteous shall live by faith" and belongs here as the NT governing principle for faith as the constitutive ground of the righteous state.

---

#### NEW-07 — Righteousness as fruit and productive harvest  
**Term:** G1343 dikaiosune (mti_id 950)

**Description:**
> Term names righteousness as a fruit — something that grows, is harvested, and can increase. The righteous person is characterised by what their righteousness produces outwardly. The fruit comes through Jesus Christ and can be multiplied by God.

**Anchor verse:** vr_id 93742 (Phili 1:11) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `950-002`, ACTION-011c):
28730, 28729, 93742

---

#### NEW-08 — Righteousness as constitution of the new self  
**Term:** G1343 dikaiosune (mti_id 950)

**Description:**
> Term names righteousness as a defining quality of the new self in Christ — the new creation is constituted in true righteousness and holiness (Eph 4:24), and righteousness is worn as a breastplate (Eph 6:14). These verses describe righteousness not as something to be pursued but as something already constitutive of the new identity in Christ.

**Anchor verse:** vr_id 28731 (Eph 4:24) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `950-002`, ACTION-011d):
28731, 28733

---

#### NEW-09 — Righteousness as clothing — worn identity  
**Term:** H6664G tse.deq (mti_id 942)

**Description:**
> Term names righteousness as something worn — it clothes and covers the whole person, like a robe and turban. The imagery conveys total coverage: righteousness is not one quality among others but the defining garment of the person's whole presence. The inner state finds its most complete expression as an enveloping identity.

**Anchor verse:** vr_id 28338 (Job 29:14) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `942-001`, ACTION-013b):
28338

---

#### NEW-10 — Righteousness targeted by injustice  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names the righteous person as the target of systemic and personal injustice — their cause subverted by bribes, their right denied by corrupt judges, their standing falsely condemned. The righteousness is real and legitimate; the violation is the perversion of what should vindicate them. God names such perversion as an abomination (Pro 17:15).

**Anchor verse:** vr_id 169441 (Pro 17:15) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-002`, ACTION-014b):
169346, 169341, 169342, 169441, 169445, 169455, 169383, 169378, 169371, 169444

---

#### NEW-11 — Speech as expression of righteousness  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names righteousness as a governing inner orientation expressed through speech — the mouth, tongue, and lips of the righteous produce life, wisdom, and what is fitting and true. Speech is deliberate rather than reactive; the heart ponders before answering (Pro 15:28). Falsehood is hated as an inner aversion (Pro 13:5).

**Anchor verse:** vr_id 169402 (Pro 10:11) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-001`, ACTION-015a):
169402, 169404, 169405, 169411, 169412, 169438, 169493, 169434

---

#### NEW-12 — Orientation toward others  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names righteousness as an inner orientation that extends outward toward others — guiding the neighbour, giving without withholding, caring for animals, returning good for evil. The righteous person's inner state reaches toward the needs of others beyond social obligation.

**Anchor verse:** vr_id 169451 (Pro 21:26) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-001`, ACTION-015b):
169423, 169427, 169451, 169490, 169332, 169467

---

#### NEW-13 — Stability and resilience of the righteous  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names righteousness as a state whose inner foundation produces lasting stability — rootedness that is never moved, establishment that survives catastrophe, resilience that rises after falling. The righteous person is not protected from difficulty (falls seven times, Pro 24:16) but is not finally overthrown by it.

**Anchor verse:** vr_id 169428 (Pro 12:3) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-001`, ACTION-015c):
169428, 169424, 169407, 169410, 169468, 169454, 169391, 169457, 169418, 169508, 169437

---

#### NEW-14 — Relational orientation toward God  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names righteousness as a state defined by its orientation toward God — walking with God (Gen 6:9), living by faith (Hab 2:4), serving God as the defining mark of the righteous (Mal 3:18), entering through the gate of the Lord (Psa 118:20), and faithfully keeping God's statutes (Eze 18:9). The righteous person's state cannot be separated from this relational grounding.

**Anchor verse:** vr_id 169369 (Gen 6:9) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-001`, ACTION-015d):
169369, 169373, 169399, 169471, 169353, 169390

---

#### NEW-15 — Community identity of the righteous  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names a recognisable community of righteous persons — a congregation (Psa 1:5), a generation (Psa 14:5), a register (Psa 69:28), and a trusted circle whose rebuke is welcomed (Psa 141:5). The righteous person belongs to an identifiable group distinct from the wicked, in whose company God dwells.

**Anchor verse:** vr_id 169462 (Psa 1:5) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-001`, ACTION-015e):
169462, 169475, 169503, 169477

---

#### NEW-16 — Righteousness targeted by opposition  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names the righteous person as a specific target of hostility — plotted against, watched for death, spoken against with contempt, sold for silver, afflicted, deprived of justice, and killed. The opposition is directed precisely because the person is righteous. The righteous person's mere existence constitutes a contrast the wicked cannot ignore.

**Anchor verse:** vr_id 169487 (Psa 37:12) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-001`, ACTION-015f):
169487, 169494, 169486, 169481, 169372, 169338, 169339, 169398, 169509, 169473, 169345, 169337, 169330, 169348, 169385, 169464

---

#### NEW-17 — Life path and way of the righteous  
**Term:** H6662 tsad.diq (mti_id 3246)

**Description:**
> Term names a recognisable life trajectory belonging to the righteous — a path and way that is level (Isa 26:7), grows progressively brighter (Pro 4:18), and can be kept and followed (Pro 2:20). The righteous person's life has a direction and shape that others can observe and walk in.

**Anchor verse:** vr_id 169460 (Pro 4:18) — set `is_anchor = 1`

**Assign these verse_context rows** (from former `3246-001`, ACTION-015g):
169446, 169460, 169377, 169425

---

### PHASE 4 — Verse relocations

#### 4a — Relocate to M26-BOUNDARY (54 verses)

All of these verse_context rows are to be reassigned from M26-A2 to M26-BOUNDARY. CC to resolve the BOUNDARY subgroup_id and update `cluster_subgroup_id` on each row.

**From `942-002` (ACTION-004):**
96015 (Psa 37:6), 28328 (Isa 58:8)

**From `942-004` (ACTION-006):**
95990 (Pro 8:16), 28313 (Isa 16:5), 28316 (Isa 32:1)

**From `942-003` (ACTION-007a):**
96005 (Psa 132:9)

**From `911-001` — governance/national (ACTION-008e):**
25166 (Gen 18:19), 169249 (2Sa 8:15), 169239 (1Ki 10:9), 169238 (1Ch 18:14), 169245 (2Ch 9:8), 25204 (Jer 22:3), 25203 (Jer 22:15), 169292 (Pro 21:3), 169276 (Eze 45:9), 169286 (Pro 14:34), 25207 (Jer 4:2)

**From `911-002` — national/institutional (ACTION-009d):**
169255 (Deu 6:25), 169256 (Deu 9:4), 169257 (Deu 9:5), 169258 (Deu 9:6), 169253 (Deu 24:13), 169241 (1Ki 8:32 H6666), 169244 (2Ch 6:23 H6666), 25211 (Job 33:26), 169298 (Psa 106:31), 169246 (2Sa 19:28)

**From `950-001` (ACTION-010c):**
28743 (Heb 7:2)

**From `950-003` (ACTION-012b):**
28772 (Rom 9:31), 28748 (Rom 10:5)

**From `942-001` (ACTION-013i/j):**
96006 (Psa 15:2), 95985 (Pro 16:13), 28331 (Isa 62:1), 28332 (Isa 62:2), 95980 (Ecc 7:15)

**From `3246-002` — corporate/judicial/rhetorical (ACTION-014c):**
169363 (Gen 18:23), 169364 (Gen 18:24), 169365 (Gen 18:25), 169366 (Gen 18:26), 169367 (Gen 18:28), 169368 (Gen 20:4), 169331 (1Ki 8:32 H6662), 169334 (2Ch 6:23 H6662), 169335 (2Ki 10:9), 169356 (Eze 23:45), 169380 (Isa 41:26), 169382 (Isa 49:24)

**From `3246-003` (ACTION-014i):**
169452 (Pro 23:24)

**From `3246-001` — governance/national (ACTION-015m):**
169336 (2Sa 23:3), 169376 (Isa 26:2), 169386 (Isa 60:21), 169354 (Eze 21:3), 169355 (Eze 21:4)

---

#### 4b — Relocate to M26-A1 (1 verse)

| vr_id | ref | term | reason |
|------:|-----|------|--------|
| 96020 | Psa 45:7 | H6664G tse.deq | Messianic king — "loved righteousness and hated wickedness" — belongs with God/messianic material in M26-A1 |

---

#### 4c — Remaining unassigned verse from 3246-002

| vr_id | ref | note |
|------:|-----|------|
| 169420 | Pro 11:31 | "If righteous repaid on earth, how much more the wicked" — assign to NEW-01 outcomes group |

---

### PHASE 4 — DUPLICATE FLAGS (CC to investigate and resolve)

Before or during execution, CC should verify the following cases where the same biblical reference appears under multiple terms/vr_ids:

| vr_ids | Biblical ref | Terms | Note |
|--------|-------------|-------|------|
| 25184 / present in 3246-002 | Isa 5:23 | H6666 + H6662 | Both should go to NEW-10 (righteousness targeted by injustice) |
| 28327 / 25192 | Isa 58:2 | H6664G + H6666 | Both should go to NEW-03 (distortion/counterfeit) |
| 95981 / 169357 | Eze 3:20 | H6664G + H6662 | Both should go to NEW-02 (Ezekiel precarious) |
| 169241 / 169331 | 1Ki 8:32 | H6666 + H6662 | Both to BOUNDARY (judicial) |
| 169244 / 169334 | 2Ch 6:23 | H6666 + H6662 | Both to BOUNDARY (judicial) |

---

## COMPLETION CONFIRMATION

After all four phases, CC must confirm:

**1. VSG count in M26-A2:**
```sql
SELECT COUNT(*) FROM verse_context_group vcg
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.cluster_code = 'M26'
AND vcg.subgroup_code = 'M26-A2'
AND vcg.active = 1;
```
Expected: 8 renamed + 17 new = 25 active VSGs (minus any deactivated groups)

**2. Verse count in M26-A2 (post-BOUNDARY moves):**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A2'
AND vc.status IN ('extracted', 'extracted_thin');
```
Expected: approximately 345 (original 360 minus ~54 to BOUNDARY minus 1 to A1, plus any from other sub-groups)

**3. BOUNDARY verse count increase:**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-BOUNDARY'
AND vc.status IN ('extracted', 'extracted_thin');
```
Report pre- and post-count; net increase should be approximately 54.

**4. Unassigned verse check (no M26-A2 verse should be groupless):**
```sql
SELECT vc.id, vc.verse_ref, mt.strong
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A2'
AND vc.verse_context_group_id IS NULL
AND vc.status IN ('extracted', 'extracted_thin');
```
Expected: 0 rows.

**5. Confirm new groups created — list all new group codes:**
```sql
SELECT vcg.group_code, vcg.context_description, COUNT(vc.id) as verse_count
FROM verse_context_group vcg
LEFT JOIN verse_context vc ON vc.verse_context_group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
WHERE mt.cluster_code = 'M26'
GROUP BY vcg.group_code, vcg.context_description
ORDER BY vcg.group_code;
```
Report group codes and verse counts for all 25 active M26-A2 VSGs.

---

## EXECUTION ORDER

1. Phase 1 (remove misplaced VSGs from M26-A2 listing) — confirm before proceeding
2. Phase 2 (rename 8 VSGs) — can run immediately after Phase 1
3. Phase 3 (create 17 new VSGs) — must complete before Phase 4 verse assignments
4. Phase 4a (BOUNDARY relocations) — can run in parallel with Phase 3
5. Phase 4b (A1 relocation) — single verse, run with Phase 4a
6. Phase 4c and duplicate flags — run last, as cleanup

---

*DIR-M26-20260510-003 | Prepared by Claude AI | 2026-05-10 | Cluster M26 | wa-directive-instruction-v1_4-20260506 §11*  
*Source: WA-M26A2-vsg-actions-v1_0-20260510.md — Actions 001 through 015*
