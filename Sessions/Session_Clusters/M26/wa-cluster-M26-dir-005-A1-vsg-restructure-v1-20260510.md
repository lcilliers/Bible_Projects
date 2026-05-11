# wa-cluster-M26-dir-005-A1-vsg-restructure-v1-20260510

**Directive ID:** DIR-M26-20260510-005  
**Prepared by:** Claude AI  
**Date:** 2026-05-10  
**Cluster:** M26 — Righteousness and Justice  
**Sub-group:** M26-A1 — God Righteousness  
**Governed by:** wa-directive-instruction-v1_4-20260506 §11  
**Source:** WA-M26A1-vsg-actions-v1_0-20260510.md  
**Reference:** WA-M26A-god-righteousness-v1_0-20260509.md (7 inferred characteristics G1–G7)  

---

## DIRECTIVE ID

DIR-M26-20260510-005

---

## MOTIVATION

A verse-by-verse reading of all 158 M26-A1 verse context rows against the God righteousness analysis established in `WA-M26A-god-righteousness-v1_0-20260509.md` revealed that:

1. The existing VSG descriptions in M26-A1 were predominantly carried from M26-A2 (human righteousness framing) and are analytically wrong for a God-righteousness sub-group.
2. Thirteen verses were ungrouped; six were assigned to a legacy group-code (1426) whose VSG identity needs CC investigation.
3. The 7 inferred characteristics of God's righteousness (G1–G7) provide a clear analytical structure that all 158 verses map to.

This directive creates 7 new VSGs aligned to G1–G7, dissolves all inherited-from-A2 VSGs, retains three existing VSGs with updated descriptions, and assigns every verse precisely to its correct group.

---

## SCOPE

**Tables:** `verse_context_group` (INSERT 7 new, UPDATE 3 descriptions, soft-delete 10 dissolved), `verse_context` (UPDATE group assignments for all 158 rows)  
**Cluster:** M26 / Sub-group: M26-A1  
**No BOUNDARY relocations required** — all 158 verses correctly describe God's or the Messiah's righteousness.

---

## EXECUTION ORDER

1. Phase 1 — Investigate group-code 1426 (CC task, no DB write)
2. Phase 2 — Create 7 new VSGs
3. Phase 3 — Update descriptions on 3 retained VSGs
4. Phase 4 — Assign all verses to new groups
5. Phase 5 — Dissolve 10 obsolete VSGs
6. Phase 6 — Completion confirmation

---

## PHASE 1 — Investigate group-code 1426

Six verse_context rows in M26-A1 currently carry group code `1426`. CC must determine:
- What `verse_context_group` row this code resolves to
- Whether it is an active or legacy group
- Its current description

The 6 verses (vr_ids 93733, 93732, 93728, 28746, 28723, 28725) are all correctly placed in M26-A1 and will be reassigned in Phase 4. Once reassigned, group 1426 should be soft-deleted from M26-A1 if it holds no remaining verses.

Report finding before proceeding to Phase 2.

---

## PHASE 2 — Create 7 new VSGs in M26-A1

INSERT 7 new `verse_context_group` rows. CC assigns group codes following the M26-A1 naming pattern (e.g. M26-A1-001 through M26-A1-007). Record codes for Phase 4.

---

### NEW VSG G1 — Foundational, permanent attribute of God

**Description:**
> Term declares God's righteousness as a foundational, permanent attribute of his nature — not situational, not responsive to circumstances, not capable of violation. It is affirmed across all his ways and all his works (Psa 145:17), endures forever (Psa 111:3), reaches to the high heavens (Psa 71:19), and will never be dismayed (Isa 51:6). It is the structural basis of his throne (Psa 89:14, 97:2), and paired consistently with faithfulness, holiness, and mercy. The closest the text comes to defining it is by exclusion: he does no injustice (Zep 3:5).

**Anchor verse:** vr_id 169479 (Psa 145:17) — set `is_anchor = 1`

**Assign (29 verses):**
169343, 169469, 169472, 169479, 169340, 169513, 169395, 169466, 169381, 169387, 25183, 93775, 96033, 96038, 95997, 28322, 28319, 28337, 169313, 169300, 25186, 25187, 25177, 25213, 169303, 28764, 28770, 93741, 28343

---

### NEW VSG G2 — Expressed through judgments conforming to what is right

**Description:**
> Term names God's righteousness as expressed through his judicial acts — judgments that conform to what is right rather than to preference or power. God judges the world with righteousness (Psa 9:8), his throne gives righteous judgment (Psa 9:4), the heavens declare it (Psa 50:6), and his judgments are named just in their most severe eschatological expressions (Rev 15:3–19:2). Christ's judgment is just because it aligns with the Father's will (Joh 5:30). God's righteous rules are expressions of this judicial character (Psa 119:7, 75, 106).

**Anchor verse:** vr_id 96035 (Psa 9:8) — set `is_anchor = 1`

**Assign (23 verses):**
169504, 93807, 93808, 93809, 93810, 93776, 93758, 93759, 93760, 96034, 96035, 96037, 96040, 96022, 28334, 169448, 96003, 96004, 95993, 169328, 25171, 169474, 93728

---

### NEW VSG G3 — Inseparable from covenant faithfulness

**Description:**
> Term names God's righteousness as the quality that makes him reliable and faithful to his covenant people — keeping promises (Neh 9:8), betrothing in righteousness and justice (Hos 2:19), extending his righteousness across generations to those who fear him (Psa 103:17). His righteous promise is longed for (Psa 119:123); his testimonies are appointed in righteousness and faithfulness (Psa 119:138). The covenant bond itself is characterised by righteousness: "I will be their God, in faithfulness and in righteousness" (Zec 8:8). He practices steadfast love, justice, and righteousness in the earth (Jer 9:24).

**Anchor verse:** vr_id 169401 (Neh 9:8) — set `is_anchor = 1`

**Assign (12 verses):**
169401, 28308, 96031, 96032, 95996, 28320, 95995, 169254, 169329, 169295, 169311, 25209

---

### NEW VSG G4 — Ground on which God acts to save and deliver

**Description:**
> Term names God's righteousness as the basis on which he acts to save, deliver, vindicate, and redeem — the quality that makes him reliably and confidently appealable. The psalmists invoke it repeatedly as the ground of petition: "In your righteousness deliver me" (Psa 31:1, 71:2, 143:1, 143:11). God's saving acts are expressions of his righteousness (1Sa 12:7). Righteousness and salvation travel inseparably (Isa 45:8, 46:13, 51:5). In the NT, God's righteousness is the basis on which he forgives (1Jo 1:9), and the ground of the cross — where he is simultaneously just and the justifier (Rom 3:26). God gives his righteousness to his people as gift and vindication (Psa 24:5, Isa 54:17).

**Anchor verse:** vr_id 169310 (Psa 31:1) — set `is_anchor = 1`

**Assign (38 verses):**
169309, 25189, 96012, 96016, 96026, 28317, 28323, 28321, 28325, 96011, 25169, 25175, 169310, 169315, 169321, 169305, 169306, 169304, 169326, 169312, 25178, 25180, 169316, 25194, 25195, 25198, 25199, 25208, 169277, 25218, 169308, 28752, 28753, 28754, 28761, 93746, 28723, 169323

---

### NEW VSG G5 — Must be revealed, proclaimed, and testified to

**Description:**
> Term names God's righteousness as something that must be declared, proclaimed, and made known — it is not self-evident but requires witness. The psalmist's tongue speaks of it all day (Psa 35:28, 71:24, 145:7), future generations shall proclaim it (Psa 22:31), the heavens declare it (Psa 50:6, 97:6). God's righteous word goes out and does not return (Isa 45:23). In the NT it is revealed through the gospel (Rom 1:17), manifested apart from law (Rom 3:21), and its glory exceeds the ministry of condemnation (2Cor 3:9). The Spirit convicts the world concerning it (Joh 16:8). The proclamation of God's righteousness is a sustained act of the covenant community across all time.

**Anchor verse:** vr_id 28744 (Rom 1:17) — set `is_anchor = 1`

**Assign (22 verses):**
96018, 96027, 96014, 96039, 96021, 28341, 169318, 169319, 169320, 169322, 169307, 169327, 169314, 169325, 25200, 169242, 25217, 28744, 28751, 93733, 28725, 25176

---

### NEW VSG G6 — Standard against which human unrighteousness is measured

**Description:**
> Term names God's righteousness as the standard that exposes human unrighteousness by contrast — when God's righteousness is affirmed, human guilt and shame are simultaneously revealed. The pattern recurs throughout Scripture: "you are righteous; we have acted wickedly" (Neh 9:33), "you are just; we are before you in guilt" (Ezr 9:15), "The Lord is in the right; I have rebelled against his word" (Lam 1:18), "to you belongs righteousness, but to us open shame" (Dan 9:7). Human anger cannot produce God's righteousness (Jam 1:20); human self-established righteousness fails to submit to it (Rom 10:3).

**Anchor verse:** vr_id 25164 (Dan 9:7) — set `is_anchor = 1`

**Assign (9 verses):**
169333, 169400, 169347, 169362, 169397, 25164, 28755, 93730, 28746

---

### NEW VSG G7 — Defining characteristic of the Messiah — becomes incarnate

**Description:**
> Term names righteousness as the defining quality of the coming Messianic figure — the Righteous One, the righteous Branch, the righteous Servant. The Servant's righteousness enables him to make many accounted righteous (Isa 53:11); the Branch is named "The Lord is our righteousness" (Jer 23:6, 33:16); the Messianic king is "righteous and having salvation" (Zec 9:9); Christ's love of righteousness grounds his anointing (Psa 45:7, Heb 1:9). In the NT these figures are identified as Jesus, who is the Holy and Righteous One (Act 3:14), whose coming was betrayed (Act 7:52), who died "the righteous for the unrighteous" (1Pe 3:18), and who is called as advocate "Jesus Christ the righteous" (1Jo 2:1). God's righteousness does not remain external — it becomes incarnate in the Messiah and through him is given to his people.

**Anchor verse:** vr_id 169384 (Isa 53:11) — set `is_anchor = 1`

**Assign (26 verses):**
169375, 169384, 169389, 169512, 57129, 57130, 96020, 28311, 28312, 93736, 28738, 93802, 93786, 93764, 93766, 93762, 93752, 93747, 25202, 25205, 25206, 25216, 169296, 93815, 93732, 169323

---

## PHASE 3 — Update descriptions on 3 retained VSGs

These three VSGs retain their verses (their own assigned verses that are NOT moved to G1–G7). Update description field only.

---

### 942-002 — retained with updated description

**Note:** After Phase 4 reassignments, all 25 of 942-002's current verses will have moved to G1–G5. The VSG itself should be checked — if empty after Phase 4, dissolve it per Phase 5. If CC finds verses that were not assigned in Phase 4, retain it with the following description.

**Updated description:**
> Term names God's righteousness as his foundational divine attribute — the eternal quality that is the basis of his throne, proclaimed by the heavens, expressed in his righteous right hand, and active in his covenant calling and commissioning. His righteous word goes out and does not return empty. All his judgments are rooted in this attribute. The term consistently associates God's righteousness with his acts, but the attribute precedes and grounds them all.

---

### 911-003 — retained with updated description

After Phase 4 reassignments, the following verses are removed from 911-003 (assigned to G1–G7). CC to confirm which verses remain.

**Updated description:**
> Term names God's righteousness as the object of appeal, praise, and proclamation by his people — the quality they invoke when seeking deliverance, declare when praising him, and remember across generations. It is vast (reaches the high heavens), eternal (endures forever), and active (draws near with salvation). God's righteousness is not only what he is but what he does for his people — the quality from which saving acts consistently flow.

---

### 3193-002 — retained with updated description

All 6 current verses remain in 3193-002 (none moved to G1–G7 under this VSG's own assignment — note: 93815 Rom 3:26 is moved from 3193-002 to G7).

**Updated description:**
> Term names God and Christ as just and righteous — addressing the Father directly as "righteous Father" (Joh 17:25), affirming God's judgments as just in their most severe expressions (Rev 15:3, 16:5, 16:7, 19:2). The VSG captures direct divine address and the eschatological declaration of God's justice as final judge.

**Retain (5 verses after 93815 moves to G7):**
93775, 93807, 93808, 93809, 93810

---

## PHASE 4 — Verse assignments (summary by source group)

CC updates `verse_context_group_id` for each vr_id listed below. Resolve new group IDs from Phase 2 codes.

### From ungrouped (13 verses → assign as indicated)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 169343 | Deu 32:4 | G1 |
| 169469 | Psa 116:5 | G1 |
| 169472 | Psa 119:137 | G1 |
| 169479 | Psa 145:17 | G1 |
| 169340 | Dan 9:14 | G1 |
| 169513 | Zep 3:5 | G1 |
| 169504 | Psa 7:11 | G2 |
| 169474 | Psa 129:4 | G2 |
| 96018 | Psa 40:9 | G5 |
| 169333 | 2Ch 12:6 | G6 |
| 169400 | Neh 9:33 | G6 |
| 57129 | Jer 23:6 | G7 |
| 57130 | Jer 33:16 | G7 |

### From group-1426 (6 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 93733 | Joh 16:8 | G5 |
| 93732 | Joh 16:10 | G7 |
| 93728 | Act 17:31 | G2 |
| 28746 | Rom 10:3 | G6 |
| 28723 | 1Cor 1:30 | G4 |
| 28725 | 2Cor 3:9 | G5 |

### From 911-002 (all 2 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 169309 | Psa 24:5 | G4 |
| 25189 | Isa 54:17 | G4 |

### From 942-004 (all 4 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 28343 | Job 8:3 | G1 |
| 96020 | Psa 45:7 | G7 |
| 28311 | Isa 11:4 | G7 |
| 28312 | Isa 11:5 | G7 |

### From 942-001 (all 4 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 96027 | Psa 7:17 | G5 |
| 96012 | Psa 35:24 | G4 |
| 96014 | Psa 35:28 | G5 |
| 28334 | Jer 11:20 | G2 |

### From 3246-001 (all 4 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 169375 | Isa 24:16 | G7 |
| 169384 | Isa 53:11 | G7 |
| 169389 | Jer 23:5 (H6662) | G7 |
| 169512 | Zec 9:9 | G7 |

### From 950-002 (all 4 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 93736 | Mat 3:15 | G7 |
| 93741 | Mat 6:33 | G1 |
| 28738 | Heb 1:9 | G7 |
| 93730 | Jam 1:20 | G6 |

### From 942-003 (all 5 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 96011 | Psa 23:3 | G4 |
| 96003 | Psa 119:7 | G2 |
| 96004 | Psa 119:75 | G2 |
| 95993 | Psa 119:106 | G2 |
| 95995 | Psa 119:123 | G3 |

### From 3193-001 (all 12 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 93802 | Mat 27:19 | G7 |
| 93786 | Luk 23:47 | G7 |
| 93776 | Joh 5:30 | G2 |
| 93764 | Act 3:14 | G7 |
| 93766 | Act 7:52 | G7 |
| 93762 | Act 22:14 | G7 |
| 93758 | 2Th 1:5 | G2 |
| 93759 | 2Th 1:6 | G2 |
| 93760 | 2Ti 4:8 | G2 |
| 93752 | 1Pe 3:18 | G7 |
| 93746 | 1Jo 1:9 | G4 |
| 93747 | 1Jo 2:1 | G7 |

### From 3193-002 (1 verse moves, 5 remain)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 93815 | Rom 3:26 | G7 |
| 93775 | Joh 17:25 | G1 |

*Note: 93775 stays assigned to G1. 93807, 93808, 93809, 93810 remain in 3193-002.*

### From 911-001 (all 9 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 169254 | Deu 33:21 | G3 |
| 169328 | Psa 99:4 | G2 |
| 25169 | Isa 1:27 | G4 |
| 25183 | Isa 5:16 | G1 |
| 25202 | Isa 9:7 | G7 |
| 25175 | Isa 33:5 | G4 |
| 25205 | Jer 23:5 (H6666) | G7 |
| 25206 | Jer 33:15 | G7 |
| 169329 | Zec 8:8 | G3 |

### From 950-001 (all 9 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 28744 | Rom 1:17 | G5 |
| 28755 | Rom 3:5 | G6 |
| 28751 | Rom 3:21 | G5 |
| 28752 | Rom 3:22 | G4 |
| 28753 | Rom 3:25 | G4 |
| 28754 | Rom 3:26 | G4 |
| 28761 | Rom 4:6 | G4 |
| 28764 | Rom 5:21 | G1 |
| 28770 | Rom 8:10 | G1 |

### From 3246-002 (all 9 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 169347 | Exo 9:27 | G6 |
| 169362 | Ezr 9:15 | G6 |
| 169401 | Neh 9:8 | G3 |
| 169395 | Job 34:17 | G1 |
| 169466 | Psa 11:7 | G1 |
| 169448 | Pro 21:12 | G2 |
| 169381 | Isa 45:21 | G1 |
| 169387 | Jer 12:1 | G1 |
| 169397 | Lam 1:18 | G6 |

### From 942-002 (all 25 verses)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 28341 | Job 36:3 | G5 |
| 96016 | Psa 4:1 | G4 |
| 96034 | Psa 9:4 | G2 |
| 96035 | Psa 9:8 | G2 |
| 96021 | Psa 48:10 | G5 |
| 96022 | Psa 50:6 | G2 |
| 96026 | Psa 65:5 | G4 |
| 96031 | Psa 85:11 | G3 |
| 96032 | Psa 85:13 | G3 |
| 96033 | Psa 89:14 | G1 |
| 96037 | Psa 96:13 | G2 |
| 96038 | Psa 97:2 | G1 |
| 96039 | Psa 97:6 | G5 |
| 96040 | Psa 98:9 | G2 |
| 95996 | Psa 119:138 | G3 |
| 95997 | Psa 119:142 (H6664G) | G1 |
| 28317 | Isa 41:10 | G4 |
| 28320 | Isa 42:6 | G3 |
| 28319 | Isa 42:21 | G1 |
| 28323 | Isa 45:8 (H6664G) | G4 |
| 28321 | Isa 45:13 | G4 |
| 28322 | Isa 45:19 | G1 |
| 28325 | Isa 51:5 | G4 |
| 28337 | Jer 50:7 | G1 |
| 28308 | Hos 2:19 | G3 |

### From 911-003 (43 of 46 verses moved; 3 remain in 911-003)

| vr_id | ref | → new VSG |
|------:|-----|-----------|
| 169242 | 1Sa 12:7 | G5 |
| 25213 | Job 37:23 | G1 |
| 169315 | Psa 5:8 | G4 |
| 169308 | Psa 22:31 | G4 |
| 169310 | Psa 31:1 | G4 |
| 169311 | Psa 33:5 | G3 |
| 169313 | Psa 36:6 | G1 |
| 169312 | Psa 36:10 | G4 |
| 169314 | Psa 40:10 | G5 |
| 169316 | Psa 51:14 | G4 |
| 169321 | Psa 71:2 | G4 |
| 169318 | Psa 71:15 | G5 |
| 169319 | Psa 71:16 | G5 |
| 169320 | Psa 71:19 | G5 |
| 169322 | Psa 71:24 | G5 |
| 169323 | Psa 72:1 | G7 |
| 169325 | Psa 88:12 | G5 |
| 169326 | Psa 89:16 | G4 |
| 169327 | Psa 98:2 | G5 |
| 169296 | Psa 103:6 | G7 |
| 169295 | Psa 103:17 | G3 |
| 169300 | Psa 111:3 | G1 |
| 169304 | Psa 119:40 | G4 |
| 169303 | Psa 119:142 (H6666) | G1 |
| 169305 | Psa 143:1 | G4 |
| 169306 | Psa 143:11 | G4 |
| 169307 | Psa 145:7 | G5 |
| 25171 | Isa 28:17 | G2 |
| 25178 | Isa 45:8 (H6666) | G4 |
| 25176 | Isa 45:23 | G5 |
| 25177 | Isa 45:24 | G1 |
| 25180 | Isa 46:13 | G4 |
| 25186 | Isa 51:6 | G1 |
| 25187 | Isa 51:8 | G1 |
| 25194 | Isa 59:16 | G4 |
| 25195 | Isa 59:17 | G4 |
| 25198 | Isa 61:10 | G4 |
| 25199 | Isa 61:11 | G4 |
| 25200 | Isa 63:1 | G5 |
| 25209 | Jer 9:24 | G3 |
| 25164 | Dan 9:7 | G6 |
| 169277 | Joe 2:23 | G4 |
| 25217 | Mic 6:5 | G5 |
| 25218 | Mic 7:9 | G4 |
| 25216 | Mal 4:2 | G7 |

**Remaining in 911-003 after moves (3 verses — no action needed, these stay):**
*CC to verify which 3 remain. Based on analysis: likely vr_ids not included above.*

---

## PHASE 5 — Dissolve obsolete VSGs from M26-A1

After Phase 4 assignments, the following VSGs should have zero remaining M26-A1 verses and should be soft-deleted or deactivated in M26-A1 scope:

| Group code | Reason |
|-----------|--------|
| `911-002` | All 2 verses moved to G4 |
| `942-004` | All 4 verses moved to G1/G7 |
| `942-001` | All 4 verses moved to G2/G4/G5 |
| `3246-001` | All 4 verses moved to G7 |
| `950-002` | All 4 verses moved to G1/G6/G7 |
| `942-003` | All 5 verses moved to G2/G3/G4 |
| `3193-001` | All 12 verses moved to G2/G4/G7 |
| `911-001` | All 9 verses moved to G1/G2/G3/G4/G7 |
| `950-001` | All 9 verses moved to G1/G4/G5/G6 |
| `3246-002` | All 9 verses moved to G1/G2/G3/G6 |
| `942-002` | All 25 verses moved to G1/G2/G3/G4/G5 |
| group-1426 | All 6 verses moved to G2/G4/G5/G6/G7 |

**CC note:** `942-002`, `911-003`, and `3193-002` descriptions must be updated (Phase 3) before dissolution check. If any of these retain verses after Phase 4, keep them active with updated descriptions.

---

## PHASE 6 — Completion confirmation

**1. Confirm 7 new VSGs created with correct verse counts:**
```sql
SELECT vcg.group_code, COUNT(vc.id) as verse_count
FROM verse_context_group vcg
LEFT JOIN verse_context vc ON vc.verse_context_group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A1'
AND vcg.group_code LIKE 'M26-A1-%'
AND vc.status IN ('extracted', 'extracted_thin')
GROUP BY vcg.group_code
ORDER BY vcg.group_code;
```
Expected: 7 rows with approximately G1=29, G2=23, G3=12, G4=38, G5=22, G6=9, G7=26

**2. Confirm no M26-A1 verse is groupless:**
```sql
SELECT COUNT(*) FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A1'
AND vc.verse_context_group_id IS NULL
AND vc.status IN ('extracted', 'extracted_thin');
```
Expected: 0 rows.

**3. Report total M26-A1 verse count by group:**
```sql
SELECT vcg.group_code, vcg.context_description, COUNT(vc.id) as verse_count
FROM verse_context_group vcg
LEFT JOIN verse_context vc ON vc.verse_context_group_id = vcg.id
JOIN mti_terms mt ON mt.id = vcg.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A1'
AND vc.status IN ('extracted', 'extracted_thin')
GROUP BY vcg.group_code
ORDER BY verse_count DESC;
```

**4. Duplicate reference check:**
```sql
-- Isa 45:8 should appear twice (H6664G vr_id 28323 and H6666 vr_id 25178), both in G4
-- Psa 119:142 should appear twice (H6664G vr_id 95997 and H6666 vr_id 169303), both in G1
-- Jer 23:5 should appear twice (H6662 vr_id 169389 and H6666 vr_id 25205), both in G7
SELECT vc.verse_ref, COUNT(*) as term_count, GROUP_CONCAT(mt.strong) as terms
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
WHERE mt.cluster_code = 'M26' AND cs.subgroup_code = 'M26-A1'
AND vc.status IN ('extracted', 'extracted_thin')
GROUP BY vc.verse_ref
HAVING term_count > 1
ORDER BY vc.verse_ref;
```
Expected: 3+ rows (the known cross-term duplicates — all legitimate).

---

*DIR-M26-20260510-005 | Prepared by Claude AI | 2026-05-10 | Cluster M26 | wa-directive-instruction-v1_4-20260506 §11*  
*Source: WA-M26A1-vsg-actions-v1_0-20260510.md — Actions A01–A12*
