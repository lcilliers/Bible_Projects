# WA-023 Compassion — Audit Patch Specification

**Filename:** wa-023-compassion-audit-patch-v1-2026-04-13.md
**Date:** 2026-04-13
**Version:** 1.0
**Previous output ref:** wa-global-general-rules-v1-2026-04-13.json; wa-global-obs-schema-v1-2026-04-13.md; wa-023-compassion-wordstudy-audit-findings-v1-2026-04-13.md
**Status:** Forward-staged patch specification. Cannot be applied until the observations schema (wa-global-obs-schema-v1-2026-04-13.md) is implemented. Stages all 16 compassion audit findings plus the false-positive from Pass 5 for eventual database application.

## Change note
Version 1.0. Initial specification. Converts the audit findings from wa-023-compassion-wordstudy-audit-findings-v1-2026-04-13.md into database operations against the proposed observation_description and obser_[entity]_index tables. The markdown artefacts (brief v1, word study v3) are **not** corrected in this document — that is Layer B and deferred to a subsequent session per researcher scoping decision (2026-04-13).

---

## 1. Scope

This patch specification converts the 17 items from the compassion audit (16 findings plus the meaning_numbered false-positive) into database operations of four types:

- **UPDATE** — modify an existing (b) observation
- **ADD** — create a new (b) observation
- **OBSOLETE** — mark an existing (b) observation obsolete with reason and supersession link
- **DROP** — remove from rendered prose; no database action (because category (a) drops have no database home)

Each item also specifies:
- Which markdown source contains the error (observations log, brief, word study)
- Which entity or entities the observation is keyed to
- The `study_segment` declaration
- Any related Session B or Session D pointer interaction

## 2. Applicability note

The schema in wa-global-obs-schema-v1-2026-04-13.md is not yet implemented. This patch specification is forward-staged. When the schema is live, the operations below can be applied. In the meantime, the specification serves as:

1. The authoritative list of corrections to be made to Reg 23's analytical content
2. The input for Artefact 4 (session actions) — which addresses how to handle the errors in the current markdown artefacts pending schema implementation
3. The migration starting point when Reg 23 is moved into the new schema

---

## 3. Operations

### Item 1 — *chus* "fourteen of twenty-four" → "sixteen of twenty-four"

**Source locations in markdown:**
- Word study v3 Section 1: "fourteen of twenty-four verses"
- Word study v3 Section 4 CHUS family: "fourteen of twenty-four occurrences"
- Brief v1 Section 2: "In 14 of 24 occurrences God or the law commands the withholding of pity"
- Observations log Pass 2 line 754: "~14/24" (rough count, but the origin of the error — this count referred to God-as-subject verses, not prohibition verses)

**JSON verification:**
`verse_context.groups` shows group 3182-002 (the judicial withholding group) contains 16 contexts. Group 3182-001 (affirmative/appeal) contains 8. Total: 24.

**Operations:**

**OBSOLETE — the prohibition-count observation carrying the wrong figure.**
```
target_table: observation_description
target_id: [the observation holding the "14 of 24" claim — to be identified during migration]
delete: 1
obsolete_reason: "Factually incorrect. Correct count is 16 of 24 verses in the judicial-withholding group (3182-002). Source of error: Pass 2 observation '~14/24' referenced God-as-subject verses, which the brief misread as a prohibition-context count. Verified against wa-023-compassion-complete-2026-04-13-v1.json verse_context.groups."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the correct observation.**
```
obser_desc: "H2347 chus (to pity) appears in 24 verses in the corpus. Of these, 16 belong to group 3182-002, which carries the judicial-withholding sense ('your eye shall not pity', 'my eye will not spare'). The remaining 8 belong to group 3182-001, which carries the affirmative sparing sense (pity shown or appealed to). The judicial-withholding frame is the term's most frequent context. Verified against verse_context.groups for mti_term_id 3182."
delete: 0
study_segment: word_study_section_1_characteristic (primary); also referenced from word_study_section_4_eleein_chus and word_study_section_2_how_it_works
origin_session: Session B Pass 1 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_term_index`: key to H2347 in Reg 23
- `obser_group_index`: key to group 3182-001 and group 3182-002

---

### Item 2 — Ezekiel "seven times, first person, eye will not spare and will not pity" → accurate count

**Source locations:**
- Word study v3 Section 2 "Compassion's limits"
- Word study v3 Section 3 Eze 7:4 annotation
- Brief v1 Section 3: "seven times in Ezekiel, each in God's first person"
- Brief v1 Section 6 Correction #8: same formulation
- Observations log Pass 3 line 920: "appears seven times in Ezekiel (5:11; 7:4,9; 8:18; 9:5,10; 20:17 — the last being the exception where God does spare)" — the observations log had the nuance; the brief flattened it

**JSON verification (from verse_text in terms[].verses):**
- Ezek 5:11 — first-person God: "My eye will not spare, and I will have no pity" ✓
- Ezek 7:4 — first-person God: "my eye will not spare… nor will I have pity" ✓
- Ezek 7:9 — first-person God: same ✓
- Ezek 8:18 — first-person God: "My eye will not spare, nor will I have pity" ✓
- Ezek 9:5 — God instructing executioners: "Your eye shall not spare" — **not first-person about God's own eye**
- Ezek 9:10 — first-person God: "my eye will not spare, nor will I have pity" ✓
- Ezek 20:17 — first-person God **affirmative**: "my eye spared them" — opposite of the claim
- Ezek 24:14 — first-person God: "I will not spare, I will not relent" — no "eye", no "pity"

Five first-person "my eye will not spare… no pity" declarations (5:11; 7:4; 7:9; 8:18; 9:10). The observations log's list of seven conflated three different phenomena.

**Operations:**

**OBSOLETE — the flattened seven-times claim.**
```
target_table: observation_description
target_id: [the observation holding "seven times, first person, eye will not spare and will not pity"]
delete: 1
obsolete_reason: "Factually incorrect. The 'seven times' count conflates (a) first-person divine declarations using the 'my eye will not spare / no pity' formula, (b) God's instruction to executioners (Ezek 9:5 — 'your eye shall not spare'), and (c) the affirmative exception (Ezek 20:17 — 'my eye spared them'). Also present: Ezek 24:14 is first-person but uses 'I will not spare' without the eye/pity formula. Verified against verse_text in wa-023-compassion-complete-2026-04-13-v1.json."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the accurate observation.**
```
obser_desc: "God declares 'my eye will not spare, nor will I have pity' in the first person five times in Ezekiel (5:11; 7:4; 7:9; 8:18; 9:10). The formula is striking in its repetition: God names his own pity-withdrawal deliberately, which means the compassion being suspended is real and felt, not absent. Three related occurrences sit alongside this pattern but do not match the first-person eye-and-pity formula: Ezek 9:5 is God instructing executioners ('your eye shall not spare'); Ezek 24:14 is first-person but without eye/pity language ('I will not spare, I will not relent'); Ezek 20:17 is first-person and affirmative — the exception where God does spare ('my eye spared them, and I did not destroy them'). The affirmative exception is significant: it shows that the withholding is deliberate, not automatic."
delete: 0
study_segment: word_study_section_2_how_it_works (primary); cross_segment to word_study_section_3_verses Eze 7:4 annotation
origin_session: Session B Pass 3 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_term_index`: key to H2347 in Reg 23
- `obser_verse_index`: key to each of Ezek 5:11, 7:4, 7:9, 8:18, 9:10, 20:17, 24:14, 9:5

---

### Item 3 — Desire/Yearning "through the womb and *chesed* vocabularies" → "through the CHEMLAH root"

**Source locations:**
- Word study v3 Section 5 Desire entry and Yearning entry
- Brief v1 Section 7 Desire row: "RACHAM/CHESED vocabulary overlap with C04"
- Brief v1 Section 7 Yearning row: "Somatic vocabulary overlap"
- Observations log SD-024: raises desire/yearning as a connection question; does not identify mechanism

**JSON verification:**
`correlations.xref_sharing` shows Reg 43 (desire) and Reg 179 (yearning) each share exactly three terms with Compassion: H2551 *chem.lah*, H2550 *cha.mal*, H4263 *mach.mal*. All three belong to the **CHEMLAH** root family (sparing/compassion), per `terms[H2551].root_family`. Neither RACHAM nor CHESED terms are shared.

**Operations:**

**OBSOLETE — the RACHAM/CHESED mechanism claim.**
```
target_table: observation_description
target_id: [the observation asserting RACHAM/CHESED mechanism for Desire/Yearning]
delete: 1
obsolete_reason: "Factually incorrect mechanism claim. The shared vocabulary between Compassion (Reg 23) and Desire (Reg 43) / Yearning (Reg 179) is the CHEMLAH root (H2551 chem.lah, H2550 cha.mal, H4263 mach.mal), not RACHAM or CHESED. Verified against correlations.xref_sharing and terms[].root_family in wa-023-compassion-complete-2026-04-13-v1.json."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the correct observation.**
```
obser_desc: "Compassion (Reg 23) shares three terms with both Desire (Reg 43) and Yearning (Reg 179): H2551 chem.lah (compassion), H2550 cha.mal (to spare), and H4263 mach.mal (compassion). The shared root is CHEMLAH — sparing/compassion — which emphasises restraint on behalf of the other, the withholding of force or judgment in response to need. This is a root-level connection from C17 into C04. The connection does not run through the RACHAM (womb) root or the CHESED (covenantal loyalty) root; these are internal to the C17 vocabulary and do not extend into the desire/yearning cluster."
delete: 0
study_segment: word_study_section_5_reg_43_desire and word_study_section_5_reg_179_yearning
origin_session: Session B Pass 6 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_xref_index`: keyed to Reg 23↔Reg 43 and Reg 23↔Reg 179
- `obser_root_index`: keyed to CHEMLAH

---

### Item 4 — Calling "Jeremiah 1:5 and Isaiah 46:3" → "Exodus 34:6"

**Source locations:**
- Word study v3 Section 5 Calling entry
- Brief v1 Section 7 calling row: "Jer 1:5 (womb → calling); Isa 46:3 (womb → carried from birth)"

**JSON verification:**
`correlations.shared_anchor_verses` shows Compassion↔Calling (Reg 19) share **Exodus 34:6** as an anchor verse (twice — once for group 2330-001 and once for group 1633-001). Neither Jer 1:5 nor Isa 46:3 appears in the shared_anchor_verses table for Reg 19.

**Operations:**

**OBSOLETE — the misattribution.**
```
target_table: observation_description
target_id: [the observation claiming Jer 1:5 / Isa 46:3 as shared anchor between Compassion and Calling]
delete: 1
obsolete_reason: "Factually incorrect shared-anchor attribution. Compassion and Calling (Reg 19) share anchor verses, but the shared verse is Exodus 34:6, not Jeremiah 1:5 or Isaiah 46:3. Verified against correlations.shared_anchor_verses."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the correct observation.**
```
obser_desc: "Compassion (Reg 23) and Calling (Reg 19) share Exodus 34:6 as an anchor verse. The Exod 34:6 divine self-revelation formula ('The Lord, the Lord, a God merciful and gracious, slow to anger, abounding in steadfast love and faithfulness') anchors multiple characteristics simultaneously: compassion (rachum), grace (channun), patience (slow to anger), love (chesed), and faithfulness. Calling is anchored here through the divine self-declaration pattern — God reveals his name and character at the point of renewing the covenant, which is a calling act. The shared anchor reflects the formula's role as a foundational divine character statement. The womb-vocabulary verses (Jer 1:5, Isa 46:3) that might at first seem to connect compassion to calling are not in fact shared anchors — they belong to separate registries and are semantically adjacent but not formally linked."
delete: 0
study_segment: word_study_section_5_reg_19_calling
origin_session: Session B Pass 6 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_xref_index`: keyed to Reg 23↔Reg 19
- `obser_verse_index`: keyed to Exod 34:6 in Reg 23

---

### Item 5 — Patience "James 5:11" → "Exodus 34:6"

**Source locations:**
- Word study v3 Section 5 Patience entry
- Brief v1 Section 7 patience row: "Jas 5:11 — polusplanchnos + Job's patience"

**JSON verification:**
`correlations.shared_anchor_verses` shows Compassion↔Patience (Reg 116) share **Exodus 34:6** (twice). Jas 5:11 is shared only with Mercy (Reg 111), not with Patience.

**Operations:**

**OBSOLETE — the misattribution.**
```
target_table: observation_description
target_id: [the observation claiming Jas 5:11 as shared anchor between Compassion and Patience]
delete: 1
obsolete_reason: "Factually incorrect shared-anchor attribution. Compassion and Patience (Reg 116) share anchor verses, but the shared verse is Exodus 34:6, not James 5:11. Jas 5:11 is a shared anchor with Mercy (Reg 111) only. Verified against correlations.shared_anchor_verses."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the correct observation.**
```
obser_desc: "Compassion (Reg 23) and Patience (Reg 116) share Exodus 34:6 as an anchor verse. The formula names God as 'slow to anger' (the patience attribute) alongside 'merciful and gracious' (the compassion attributes). The co-presence in this foundational divine character statement makes compassion and patience structurally linked attributes of God's inner character — not independent qualities but paired facets of the same disposition of restraint. The connection with Jas 5:11 (polusplanchnos + Job's patient endurance) is a contextual co-presence, not a shared anchor: the verse is an anchor for Mercy (Reg 111), not Patience."
delete: 0
study_segment: word_study_section_5_reg_116_patience
origin_session: Session B Pass 6 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_xref_index`: keyed to Reg 23↔Reg 116
- `obser_verse_index`: keyed to Exod 34:6 in Reg 23

---

### Item 6 — Heart "shares anchor verses" → "no shared anchors"

**Source locations:**
- Word study v3 Section 5 Heart entry
- Brief v1 Section 7 heart row: "xref (2) + shared_anchor (2)"

**JSON verification:**
`correlations.shared_anchor_verses` shows **no shared anchor verses between Compassion (Reg 23) and Heart (Reg 183)**. The "shared_anchor (2)" in the brief appears to have been confused with the Mind (Reg 112) row, which does have 2 shared anchors (both from 1Pe 3:8).

**Operations:**

**OBSOLETE — the misattribution.**
```
target_table: observation_description
target_id: [the observation claiming shared anchors between Compassion and Heart]
delete: 1
obsolete_reason: "Factually incorrect. Compassion (Reg 23) and Heart (Reg 183) do not share any anchor verses in correlations.shared_anchor_verses. The brief v1 Section 7 heart row appears to have confused Heart (Reg 183) with Mind (Reg 112), which does have 2 shared anchors via 1Pe 3:8. Verified against correlations.shared_anchor_verses."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the correct observation.**
```
obser_desc: "Compassion (Reg 23) and Heart (Reg 183) share 2 terms in the correlation data: G4697 splanchnizō and G4698 splanchnon. These shared terms reflect the body-part logic — splanchnon names the inner organs (bowels/entrails) that are the physical seat of compassion, and the heart vocabulary overlaps at this point. Hos 11:8 uses 'my heart recoils within me' as the setting for the ni.chum warmth, which makes the heart the narrative location where compassion stirs. However, there are no shared anchor verses between Compassion and Heart in the correlation data — the connection is at the term-sharing level and at the verse-level observation of Hos 11:8, not at the anchor-verse level. (Mind (Reg 112) is the registry with 2 shared anchors via 1Pe 3:8, and this may be where the brief v1 entry was confused.)"
delete: 0
study_segment: word_study_section_5_reg_183_heart
origin_session: Session B Pass 6 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_xref_index`: keyed to Reg 23↔Reg 183
- `obser_term_index`: keyed to G4697, G4698

---

### Item 7 — Sorrow "Lamentations 4:10" → "Hosea 11:8"

**Source locations:**
- Word study v3 Section 5 Sorrow entry: "including the Lamentations 4:10 verse"
- Brief v1 Section 7 sorrow row: "(Lam 4:10)"

**JSON verification:**
`correlations.shared_anchor_verses` shows one shared anchor between Compassion (Reg 23) and Sorrow (Reg 151): **Hosea 11:8**. Lam 4:10 is not in the shared_anchor_verses list for Reg 151.

**Operations:**

**OBSOLETE — the misattribution.**
```
target_table: observation_description
target_id: [the observation claiming Lam 4:10 as shared anchor between Compassion and Sorrow]
delete: 1
obsolete_reason: "Factually incorrect shared-anchor attribution. The shared anchor between Compassion (Reg 23) and Sorrow (Reg 151) is Hosea 11:8, not Lamentations 4:10. Lam 4:10 is a significant compassion verse (the inversion under catastrophe, SD-003) but is not listed as a shared anchor with Sorrow. Verified against correlations.shared_anchor_verses."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the correct observation.**
```
obser_desc: "Compassion (Reg 23) and Sorrow (Reg 151) share Hosea 11:8 as an anchor verse. The verse ('How can I give you up, O Ephraim?... my heart recoils within me; my compassion grows warm and tender') simultaneously names divine grief over the prospect of judgment and divine compassion that overrides judgment. The inner-being content is the co-presence of sorrow and compassion in divine inner deliberation. The shared anchor points to the structural question of how sorrow and compassion function together in the divine characterisation at moments of decision."
delete: 0
study_segment: word_study_section_5_reg_151_sorrow
origin_session: Session B Pass 6 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_xref_index`: keyed to Reg 23↔Reg 151
- `obser_verse_index`: keyed to Hos 11:8 in Reg 23

**Note on Lam 4:10:** This verse remains an important observation about compassion (SD-003 and the ra.cha.ma.ni observation in Pass 1 Term 3). It is keyed to Compassion directly via the H7362 *ra.cha.ma.ni* term and to the C05 cluster thematically. It is simply not a *shared anchor* with Sorrow in the correlation data. The correction here is precise: the existing Lam 4:10 observation stays; the claim that it is a shared anchor with Sorrow is wrong.

---

### Item 8 — Mercy "largest term-sharing in the programme" → DROP superlative

**Source locations:**
- Word study v3 Section 5 Mercy entry
- Brief v1 Section 7 mercy row: "Largest term-sharing in programme"

**JSON / verification:**
The JSON contains only Reg 23's correlation data. It confirms 38 shared terms with Mercy is the highest *within Reg 23's xref_sharing list*, but does not confirm this is the highest in the programme. The superlative is unverified. Per GR-PROG-006, unsupported superlatives are category (a) — drop.

**Operations:**

**OBSOLETE — the superlative claim.**
```
target_table: observation_description
target_id: [the observation asserting "largest term-sharing in programme"]
delete: 1
obsolete_reason: "Superlative claim without source. The 38 shared terms figure is correct, but 'largest in the programme' is a programme-wide comparative claim that cannot be verified from Reg 23's extract alone. Per GR-PROG-006, unsupported superlatives are dropped. The underlying fact (38 shared terms) is preserved as a non-superlative observation."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the factual statement without the superlative.**
```
obser_desc: "Compassion (Reg 23) shares 38 terms with Mercy (Reg 111). The two registries also share a root (ATAR) and three anchor verses (Jas 5:11, Num 6:25, Rom 9:15). Luke 10:33-37 shows the sequence splanchnizō → eleos (compassion → mercy): the inward movement generates the outward act. The question of whether compassion and mercy are distinguishable characteristics or aspects of a single reality is raised as SD-Q1 and is open for Session D."
delete: 0
study_segment: word_study_section_5_reg_111_mercy
origin_session: Session B Pass 6 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_xref_index`: keyed to Reg 23↔Reg 111
- `obser_root_index`: keyed to ATAR

---

### Item 9 — Love "highest verse co-occurrence in the research corpus" → DROP superlative

**Source locations:**
- Word study v3 Section 5 Love entry
- Brief v1 Section 7 love row: "Highest co-occurrence in programme"

**JSON verification:** Same as Item 8 — the 196 figure is confirmed as Reg 23's highest xref partner, but the programme-wide superlative is unverified.

**Operations:**

**OBSOLETE — the superlative.**
```
target_table: observation_description
target_id: [the observation asserting "highest verse co-occurrence in programme"]
delete: 1
obsolete_reason: "Superlative claim without source. 196 co-occurrence verses is correct, but 'highest in the research corpus' is a programme-wide claim not verifiable from Reg 23's data. Per GR-PROG-006, dropped."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the factual statement.**
```
obser_desc: "Compassion (Reg 23) shares 13 terms with Love (Reg 103) and co-occurs with Love in 196 verses. Both registries share the RACHAM root family, linking compassion's womb-vocabulary to love's womb-vocabulary at the root level. Isaiah 54:8 and 63:9 name love and compassion together as divine inner motivation for redemption. Six shared anchor verses (1Pe 3:8, Exo 33:19, Exo 34:6, Hos 6:6, Lam 3:22, Mic 6:8) further connect the two registries. The question of whether compassion is a form of love, a consequence of love, or a structurally prior disposition is raised as SD-Q2 and is open for Session D."
delete: 0
study_segment: word_study_section_5_reg_103_love
origin_session: Session B Pass 6 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_xref_index`: keyed to Reg 23↔Reg 103
- `obser_root_index`: keyed to RACHAM

---

### Item 10 — Exod 34:6 "cited more than any other OT passage" → DROP superlative

**Source locations:**
- Word study v3 Section 3 Exo 34:6 annotation (not in the brief)

**JSON / verification:** The underlying observation that the formula is cited or echoed across the OT (Neh 9:17; Ps 86:15; 103:8; 145:8; Joel 2:13; Jon 4:2) is supported by SD-017. The comparative claim "more than any other OT passage about God's inner character" is not verified anywhere.

**Operations:**

**OBSOLETE — the superlative.**
```
target_table: observation_description
target_id: [the observation asserting Exo 34:6 is cited more than any other OT passage about God's inner character]
delete: 1
obsolete_reason: "Superlative claim without source. Per GR-PROG-006, dropped. The underlying fact — that the formula is cited or echoed across multiple OT passages — is preserved in a separate observation."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the factual statement.**
```
obser_desc: "The Exodus 34:6 divine self-revelation formula (rachum ve-channun — 'merciful and gracious, slow to anger and abounding in steadfast love and faithfulness') is cited, echoed, or alluded to across multiple OT passages: Neh 9:17, 9:31; Psa 86:15, 103:8, 145:8; Joel 2:13; Jon 4:2. The formula is a foundational divine character statement that binds together multiple inner-being characteristics (compassion, grace, patience, steadfast love, faithfulness). Whether Exod 34:6 functions as a unified theological statement that should be analysed as a whole, or whether its component parts map independently to their respective registries, is raised as SD-017 and is open for Session D."
delete: 0
study_segment: word_study_section_3_verses (Exo 34:6 annotation); cross_segment to word_study_section_4_chesed
origin_session: Session B Pass 2 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_verse_index`: keyed to Exo 34:6 in Reg 23
- `obser_term_index`: keyed to H2587 chan.nun and H2617B che.sed

---

### Item 11 — "NT does not develop [participatory compassion] at the same depth" → DROP comparative

**Source locations:**
- Word study v3 Section 2 "Compassion and suffering"

**JSON / verification:** The observation that the *sym-* compounds are a NT-concentrated development is supported by Pass 1 Term 16 and Pass 2. The comparative claim "does not develop at the same depth" in the OT is not supported anywhere.

**Operations:**

**OBSOLETE — the comparative claim.**
```
target_table: observation_description
target_id: [the observation asserting the OT does not develop participatory compassion at the same depth]
delete: 1
obsolete_reason: "Comparative claim without source. The observation that sym- compounds are a NT-concentrated development is supported. The comparative 'OT does not develop this at the same depth' is an interpretive framing with no evidential source. Per GR-OBS-006, analytical claims must derive from observations; this one does not."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the non-comparative statement.**
```
obser_desc: "The Greek sym- compounds (G4834 sumpatheō, G4835 sumpathēs, G4841 sumpaschō, G3356 metriopatheō) name compassion as participation in another's experience — suffering-with rather than suffering-at. These terms are concentrated in the NT epistles. They introduce a Christological ground: Heb 4:15 attributes sumpatheō to Christ as an ongoing capacity acquired through incarnate experience. Rom 8:17 carries sumpaschō to an eschatological conclusion: 'if we suffer with him, we may also be glorified with him.' The NT sym- compound vocabulary is distinctive to its corpus; the question of whether the OT develops an equivalent participatory compassion, and how, is open and belongs to Session D cross-testament analysis."
delete: 0
study_segment: word_study_section_2_how_it_works (primary); also word_study_section_4_path
origin_session: Session B Pass 1 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_term_index`: keyed to G4834, G4835, G4841, G3356
- `obser_root_index`: keyed to PATH

---

### Item 12 — Lam 3:22 "defiant confession in the face of catastrophe" → REVIEW

**Source locations:**
- Word study v3 Section 3 Lam 3:22 annotation

**Analysis:** This is a literary framing with no source in observations or brief. Under GR-OBS-006, Session C prose must derive from (b) observations. The framing may be defensible but has no audit trail.

**Operations:**

**OBSOLETE — the literary framing.**
```
target_table: observation_description
target_id: [the observation containing the "defiant confession" framing for Lam 3:22]
delete: 1
obsolete_reason: "Literary framing introduced at Session C level without derivation from any (b) observation. Per GR-OBS-006, Session C prose must derive from observations. The framing may be defensible but has no audit trail in the observations log or the analytical brief. Obsoleted pending review."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the evidentially grounded replacement observation.**
```
obser_desc: "Lam 3:22 — 'The steadfast love of the LORD never ceases; his mercies never come to an end' — is the clearest canonical example of chesed declared as persisting when all circumstantial evidence argues against it. The verse appears in the context of Lamentations, which is the most sustained canonical expression of grief. The word 'mercies' in the verse is rachamim, pairing directly with chesed: steadfast love and tender compassion together define what keeps God's people alive when the city is destroyed. The verse is a covenantal confession made against the evidential pressure of catastrophe."
delete: 0
study_segment: word_study_section_3_verses (Lam 3:22 annotation); cross_segment to word_study_section_4_chesed
origin_session: Session B Pass 3 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_verse_index`: keyed to Lam 3:22 in Reg 23
- `obser_term_index`: keyed to H2617B che.sed

**Note:** The replacement observation retains the substance (the verse's force comes from its covenantal claim made against catastrophic circumstance) but removes the "defiant" framing, which is author interpretation not present in the evidence. If the researcher decides the "defiant" framing should be preserved, a separate observation can be added that makes the framing explicit and sources it.

---

### Item 13 — Gen 19:16 "mercy in the face of inadequacy" → REVIEW

**Source locations:**
- Word study v3 Section 3 Gen 19:16 annotation

**Analysis:** Literary framing not in observations or brief. Same pattern as Item 12.

**Operations:**

**OBSOLETE — the literary framing.**
```
target_table: observation_description
target_id: [the observation containing "mercy in the face of inadequacy" for Gen 19:16]
delete: 1
obsolete_reason: "Literary framing introduced at Session C level without derivation. Per GR-OBS-006. Obsoleted pending review."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the evidentially grounded replacement.**
```
obser_desc: "Gen 19:16 narrates Lot's rescue from Sodom: 'But he lingered. So the men seized him and his wife and his two daughters by the hand, the Lord being merciful (chem.lah) to him, and they brought him out and set him outside the city.' The verse names divine compassion (chem.lah) as the cause of the rescue — not Lot's readiness, which is named as hesitant ('he lingered'). The observation: divine compassion acts on behalf of those whose own actions would otherwise frustrate the rescue. The inner-being content is that compassion, as a divine act, does not require the recipient's worthiness or readiness as its trigger."
delete: 0
study_segment: word_study_section_3_verses (Gen 19:16 annotation); cross_segment to word_study_section_4_chemlah
origin_session: Session B Pass 3 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_verse_index`: keyed to Gen 19:16 in Reg 23
- `obser_term_index`: keyed to H2551 chem.lah

---

### Item 14 — Jon 4:11 "creatureliness" → REVIEW

**Source locations:**
- Word study v3 Section 3 Jon 4:11 annotation

**Analysis:** The word "creatureliness" is used as a framing label in the word study without source in observations. The underlying substance (God's pity for Nineveh grounded in the simple fact of creaturely need) is present in the observations (Pass 3 line 917 discussion of Jon 4:10-11).

**Operations:**

**OBSOLETE — the framing-label version.**
```
target_table: observation_description
target_id: [the observation using "creatureliness" as framing label for Jon 4:11]
delete: 1
obsolete_reason: "Framing label 'creatureliness' introduced at Session C level without derivation. The substance is in Pass 3 but the label is not. Per GR-OBS-006, obsoleted pending review. Replacement observation retains the substance."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the substance without the framing label.**
```
obser_desc: "Jonah 4:11 — God's rhetorical question: 'And should not I pity (chus) Nineveh, that great city, in which there are more than 120,000 persons who do not know their right hand from their left, and also much cattle?' — grounds divine pity in the simple fact of the Ninevites' number and ignorance, including the cattle. The structure is the parallelism with Jon 4:10: Jonah pitied the plant that he did not labour over; should God not pity a city of 120,000 with their animals? The verse shows that chus can operate both in morally trivial cases (plant) and morally weighty cases (city), and it is the same inner movement in both. The basis for divine pity here is not moral desert but creaturely need — God's pity is grounded in the existence and condition of those who cannot help themselves, not in their moral renewal."
delete: 0
study_segment: word_study_section_3_verses (Jon 4:11 annotation); cross_segment to word_study_section_4_eleein_chus
origin_session: Session B Pass 3 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_verse_index`: keyed to Jon 4:11 and Jon 4:10 in Reg 23
- `obser_term_index`: keyed to H2347 chus

---

### Item 15 — Isa 54:8 "settles the question" → RESTORE SD-019 as open

**Source locations:**
- Word study v3 Section 2 "The deliberative quality of divine compassion"

**Analysis:** SD-019 was raised by Session B Pass 3 as a Session D question. The word study treats the question as settled. This is the most significant methodological error in the audit — it silently closes a Session D pointer at the Session C level.

**Operations:**

**OBSOLETE — the "settles the question" framing.**
```
target_table: observation_description
target_id: [the observation asserting Isa 54:8 settles the question of which impulse is more fundamental]
delete: 1
obsolete_reason: "Premature closure of Session D pointer SD-019. Per GR-OBS-002 and GR-OBS-006, Session D questions are not resolved at Session C level. SD-019 was raised as a Session D question by Session B Pass 3; the word study treated it as settled. Obsoleted, and SD-019 is restored as open."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the observation that treats Isa 54:8 as evidence for an open question.**
```
obser_desc: "Isaiah 54:8 — 'In overflowing anger for a moment I hid my face from you, but with everlasting love (chesed) I will have compassion (racham) on you' — establishes a temporal asymmetry in divine inner-being: a moment of anger versus everlasting chesed/racham. This verse is strong evidence for the question raised in SD-019 (whether compassion is the more fundamental divine characteristic than judgment), but it is evidence, not a resolution. The question remains open for Session D. The temporal contrast is notable but does not by itself answer whether 'more permanent' is the same as 'more fundamental' at the level of divine inner constitution."
delete: 0
study_segment: word_study_section_2_how_it_works (primary)
origin_session: Session B Pass 3 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_verse_index`: keyed to Isa 54:8 in Reg 23
- `obser_term_index`: keyed to H2617B che.sed, H7356A ra.cham
- `related_obser_id`: references the SD-019 pointer record

**Action on `session_d.sd_pointer_flags`:**
```
target_table: session_d.sd_pointer_flags
target_record: SD-019 (DIM-023-SD019 or equivalent)
action: set resolved = 0
note: "Reopened 2026-04-13. Prematurely closed by word study v3 Section 2. Restored as open Session D question per audit. See superseding observation [new id]."
```

---

### Item 16 — *chesed*/shame "eschatological horizon" → REVIEW

**Source locations:**
- Word study v3 Section 2 "Chesed: when compassion becomes character"

**Analysis:** The "eschatological horizon" label is author framing not in observations or brief. The underlying substance (the CHASAD root carries both positive and negative poles) is well-supported (Pass 1 Term 9, SD-008, brief Section 2). The framing label is what needs correction.

**Operations:**

**OBSOLETE — the framing label.**
```
target_table: observation_description
target_id: [the observation labelling the chesed/shame pole as "eschatological horizon"]
delete: 1
obsolete_reason: "Framing label 'eschatological horizon' introduced at Session C level without derivation. The underlying substance (chesed/shame root polarity) is in Pass 1 Term 9 and SD-008, which treats this as a root-level semantic paradox and Session D question — not as an eschatological claim. Obsoleted. Replacement retains the substance."
obsolete_date: 2026-04-13
superseded_by_id: [id of the ADD operation below]
```

**ADD — the substance without the framing label.**
```
obser_desc: "The CHASAD Hebrew root yields both chesed (steadfast love) and a negative-pole sub-entry meaning shame/disgrace. The same root that names the highest expression of covenantal loyalty also names its most painful violation. This root-level paradox means that where chesed fails, what remains is not neutral absence but its opposite pole — shame as a register of chesed's violation. The structural question — whether this semantic paradox reflects a genuine inner-being relationship (the failure of covenantal compassion producing shame as its consequence) or is purely a lexicographic artefact — is raised as SD-008 and is open for Session D."
delete: 0
study_segment: word_study_section_2_how_it_works (primary); word_study_section_4_chesed
origin_session: Session B Pass 1 (corrected 2026-04-13)
origin_registry_id: 23
origin_instruction_version: WA-SessionB-Instruction-v4.7
created_date: 2026-04-13
```

**Index rows:**
- `obser_term_index`: keyed to H2617B che.sed (carries both poles in this registry)
- `obser_root_index`: keyed to CHASAD
- `related_obser_id`: references the SD-008 pointer record

---

### Item 17 (additional) — "meaning_numbered null for all Hebrew active OWNER terms" → OBSOLETE as false positive

**Source locations:**
- Observations log Pass 5 language accuracy audit, lines 1008–1012
- Brief v1 Section 9 Open Items #2

**Analysis:** Per researcher clarification (2026-04-13) and GR-DATA-004, the `meaning_numbered` field is a deprecated Phase 1 working field with ~1% population, superseded by `wa_meaning_parsed`. The Pass 5 finding is a false positive — the field is not expected to be populated in the final state.

**Operations:**

**OBSOLETE — the gap finding.**
```
target_table: observation_description
target_id: [the Pass 5 observation flagging meaning_numbered null as a gap]
delete: 1
obsolete_reason: "False positive. Per GR-DATA-004, meaning_numbered is a deprecated Phase 1 working field (~1% population, superseded by wa_meaning_parsed). The field is not expected to be populated in the final state. Hebrew active OWNER terms showing null meaning_numbered is the programme-level normal state, not a gap. The observation is retired."
obsolete_date: 2026-04-13
superseded_by_id: NULL (no replacement — the finding was simply wrong)
```

**No ADD.** This is a pure retirement. The Pass 5 "meaning_numbered gap" was identifying a condition that is not a gap.

**Action on brief v1 Section 9 Open Items:** Item 2 (meaning_numbered fields null for all Hebrew active OWNER terms) is retired as a false positive. The Open Items list becomes a shorter list.

---

## 4. Operations summary

| Item | Action type | Obsolete count | Add count | Entity(s) | Pointer interaction |
|---|---|---|---|---|---|
| 1 | OBSOLETE + ADD | 1 | 1 | term H2347, groups 3182-001/002 | — |
| 2 | OBSOLETE + ADD | 1 | 1 | term H2347, 8 verses in Ezek | — |
| 3 | OBSOLETE + ADD | 1 | 1 | xref Reg 23↔43, xref Reg 23↔179, root CHEMLAH | — |
| 4 | OBSOLETE + ADD | 1 | 1 | xref Reg 23↔19, verse Exo 34:6 | — |
| 5 | OBSOLETE + ADD | 1 | 1 | xref Reg 23↔116, verse Exo 34:6 | — |
| 6 | OBSOLETE + ADD | 1 | 1 | xref Reg 23↔183, terms G4697/G4698 | — |
| 7 | OBSOLETE + ADD | 1 | 1 | xref Reg 23↔151, verse Hos 11:8 | — |
| 8 | OBSOLETE + ADD | 1 | 1 | xref Reg 23↔111, root ATAR | cross-ref SD-Q1 |
| 9 | OBSOLETE + ADD | 1 | 1 | xref Reg 23↔103, root RACHAM | cross-ref SD-Q2 |
| 10 | OBSOLETE + ADD | 1 | 1 | verse Exo 34:6, terms H2587/H2617B | cross-ref SD-017 |
| 11 | OBSOLETE + ADD | 1 | 1 | terms G4834/G4835/G4841/G3356, root PATH | — |
| 12 | OBSOLETE + ADD | 1 | 1 | verse Lam 3:22, term H2617B | — |
| 13 | OBSOLETE + ADD | 1 | 1 | verse Gen 19:16, term H2551 | — |
| 14 | OBSOLETE + ADD | 1 | 1 | verses Jon 4:10-11, term H2347 | — |
| 15 | OBSOLETE + ADD | 1 | 1 | verse Isa 54:8, terms H2617B/H7356A | SD-019 reopened |
| 16 | OBSOLETE + ADD | 1 | 1 | term H2617B, root CHASAD | cross-ref SD-008 |
| 17 | OBSOLETE only | 1 | 0 | (Pass 5 gap finding) | — |
| **Totals** | | **17** | **16** | | **SD-019 reopened; three open pointers cross-referenced** |

---

## 5. Pre-application verification steps

When the schema is live and this patch is ready for application, the following verification steps must run:

1. **Identify the target records.** Each `target_id` in an OBSOLETE operation currently reads `[the observation holding ...]`. These ids do not exist yet because the current observations are in markdown, not in the new schema. The migration of Reg 23 material into the schema must run first. Each target observation must be identified by content match against the markdown source.

2. **Verify JSON sources.** Each ADD operation cites JSON evidence. Before applying, the patch applicator should re-verify the citation against a current extract of Reg 23 to ensure the correction has not itself gone stale.

3. **Run the SD-019 restoration.** The change to `session_d.sd_pointer_flags` must be applied and verified.

4. **Fresh extract after apply.** Per GR-PASS-002, a fresh extract must be pulled after the patch is applied.

5. **Spot-check the corrected record set.** After fresh extract, the 16 new observations should be retrievable by their `study_segment` values, and the 17 obsoleted records should be present with `delete = 1` and `obsolete_reason` populated.

---

## 6. What this patch does not do

This patch does **not**:

- Correct the markdown artefacts (observations log v14, brief v1, word study v3). Those corrections are Layer B and are specified in `wa-023-compassion-session-actions-v1-2026-04-13.md`.
- Implement the observations schema. Schema implementation is a separate Layer C task deferred to the next session.
- Migrate the existing Reg 23 markdown observations into the new schema. Migration is a substantial one-time task flagged in the schema proposal (Section 8 Item 4).
- Address errors in other registries (C17 cluster or beyond). The programme-wide implications of these errors — specifically whether the same correlation-mechanism and shared-anchor misattributions exist in the mercy (111), grace (68), kindness (99) briefs — is flagged in the session log as a follow-up check.

---

*Produced under GR-OBS-002, GR-OBS-005, GR-PROG-006. Forward-staged for application after schema implementation.*
