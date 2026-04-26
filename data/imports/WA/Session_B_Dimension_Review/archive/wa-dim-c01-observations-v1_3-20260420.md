# WA Dimension Review Observations Log — C01

| Field | Value |
|---|---|
| Filename | wa-dim-c01-observations-v1_3-20260420.md |
| Supersedes | wa-dim-c01-observations-v1_2-20260420.md (Phase B r112 + r183 complete) |
| Governing instruction | wa-dimensionreview-instruction-v3_3-20260418.md |
| Mode | Registry Mode — target registries: Reg 112 (mind), Reg 183 (heart) |
| Cluster extract | wa-dim-C01-extract-2026-04-20.json (275 groups, 6 registries) |
| Root family extract | wa-dim-C01-rootfamily-2026-04-20.json (61 roots, 5 cross-registry flagged) |
| Existing pointers extract | wa-dim-C01-existing-pointers-2026-04-20.json (29 Session B findings, 37 Session D pointers) |
| Flags file | wa-global-flags-v1_5-20260418.md (7 open, 6 resolved, 1 obsolete, 0 standing) |
| Session date | 2026-04-20 |
| Session scope | Phase C — Registry 112 (mind), all 73 groups |
| Researcher direction | Single-session Phase C on 73 groups; block DR-8 authorisation for 71 locked groups; stamp with v3_3 governing version; proceed past FLAG-010 with [INSTRUCTION-NOTE] |
| Version increment reason | Phase B → Phase C boundary per GR-OBS-004 |

---

## Continuation note

Phase A (v1_0), Phase B r112 (v1_1), Phase B r183 (v1_2) content preserved for audit. This v1_3 file appends Phase C r112 work.

---

## [PHASE-A / PHASE-B] summary (carried forward)

- **Phase A:** cluster coherence confirmed; mixed-vintage dataset; 3 vocabulary gaps (Spiritual/God-ward, Identity/Selfhood, Somatic/Embodied); 2 genuine cross-registry roots (CHASHAV, BOUL).
- **Phase B r112:** 73 groups, 71 QA-CLEAR, 1 QA-VAGUE (1010-001 nefros), 1 QA-REVIEW (3336-002 cha.shav), zero QA-TERMCENTRIC.
- **Phase B r183:** 59 groups, 55 QA-CLEAR, 2 QA-BROAD (Aramaic forms), 2 QA-REVIEW (579-008 le.vav, 577-005 qe.rev), zero QA-TERMCENTRIC.

Full records in v1_0, v1_1, v1_2.

---

## [INSTRUCTION-NOTE] 2026-04-20 — FLAG-010 acknowledged; Phase C proceeding per researcher direction

OBSERVATION: Global flags file v1_5 records FLAG-010 (Post-GR-v2_8 instruction audit) as an Open blocking gate on "new word analysis." The Dimension Review instruction is explicitly named as requiring full audit against GR v2_8. The audit has not been completed; the current v3_3 instruction body confirms only a GR-REF-002 sweep (operational references migrated to `[current]`), not the full GR-v2_8 audit.

RESEARCHER DECISION (2026-04-20): Proceed with Phase C r112 under researcher-directed authorisation. "New word analysis" interpreted as Session B (analytical stage producing word studies), not Dimension Review (preparatory stage). Full DR instruction audit deferred.

CONSEQUENCE: Phase C proceeds on r112 under v3_3 governance. Any point at which v3_3 and GR v2_11 appear to conflict will be recorded as an additional [INSTRUCTION-NOTE] for the later audit cycle.

ACTION: Flagged for the FLAG-010 resolution record.

---

## [INSTRUCTION-NOTE] 2026-04-20 — Stamp string departure from template

OBSERVATION: Instruction §9.1 stamp template, §9.2 patch template, and §11.2 stamp table all specify `dim_review_version = "WA-DimensionReview-Instruction-v3.1-20260414"`. This literal string is three minor versions behind the actual governing instruction (v3_3-20260418) under which this work was performed.

RESEARCHER DECISION (2026-04-20): Stamp with the actual governing version — `wa-dimensionreview-instruction-v3_3-20260418`. This reflects what was actually governing, per the preamble's fact-reporting discipline.

CONSEQUENCE: The r112 patch will carry `dim_review_version = "wa-dimensionreview-instruction-v3_3-20260418"`. This is a lowercase-filename-style string; it is consistent with GR-FILE-007 (lowercase filenames) and GR-FILE-003 (underscored version convention). A small provenance-only alignment issue; the literal template remains unchanged in the instruction until a next revision.

ACTION: Flagged for next instruction review cycle (update templates to `[current]` or to the actual governing version convention).

---

## [INSTRUCTION-NOTE] 2026-04-20 — Pointer format differs from existing records

OBSERVATION: Existing pointer records in `wa-dim-C01-existing-pointers-2026-04-20.json` use formats `112-F001` (finding_id) and `112-SD001` (flag_label) — without "DIM-" prefix. Instruction §7.5 prescribes `DIM-{registry_no}-{3-digit-sequence}` and `DIM-{registry_no}-SD{3-digit-sequence}` — with "DIM-" prefix.

INTERPRETATION: The existing records predate the current §7.5 convention. New pointer records created in this Phase C use the current convention (e.g., `DIM-112-004`, `DIM-112-SD003`). Claude Code may wish to reconcile the old records to the current format as a separate cleanup; that is not a Phase C analytical task.

ACTION: Flagged; new pointers numbered continuing from existing sequences: Session B starts at 004; Session D starts at SD003.

---

## Phase C r112 — working notes

**Scope:** 73 groups, all active, 71 at manual_override=1 (block DR-8 authorisation confirmed), 2 at manual_override=0. All 73 need dimension assignment under current §7.7 vocabulary and dominant_subject assignment.

**Approach:** organised by root family (17 families), working smallest-first so that the large families (FRĒN 13, MNE 13, NOUS 10) benefit from accumulated context. For each group: name the characteristic observed in the description, select the §7.7 dimension that genuinely fits, assign dominant_subject, note any vocabulary-gap concerns, note Session D patterns as they emerge.

**Vocabulary gaps: how I will handle them.** Three Phase A vocabulary gaps were identified (Spiritual/God-ward, Identity/Selfhood, Somatic/Embodied). Per §7.3 Rule 3, when no existing dimension fits I name what the group shows and raise as Session D. I will not force-fit. The most likely r112 encounter is Spiritual/God-ward in groups like 996-001 froneō toward God, 3498-001/002/003 memorials, 4411-001 commanded remembrance, 4416-001 affectionate remembrance in prayer. Where the characteristic is clearly divine-human correspondence (God acting on the human or vice versa as direct ground or mirror), Dimension 11 applies (§7.7 line 537-542). Where the characteristic is the human's orientation toward God without correspondence structure, the gap is real.

**Anchor verse verification (§7.4 Step 3).** The cluster extract provides anchor verse references but full verse text only in the `anchor_verses` list structure. Per §4.2, where description is insufficient I should request an extract. For this session, I will rely on the existing characteristic-perspective descriptions (Phase B concluded 71 of 73 groups as QA-CLEAR) plus the description content. Where a group's dimension assignment is non-obvious, I will note it in the [PHASE-C] entry. Full AV-VERIFY entries per §9.1 will be recorded where meaningful; for QA-CLEAR groups with straightforward dimension assignment, the AV-VERIFY is absorbed into the Phase C entry's NOTES field.

---

## Phase B description correction — RD-PHASE-B-112-001 (nefros) in-session rewrite

Per researcher direction, the QA-VAGUE finding on 1010-001 nefros resolves with in-session correction. This is a Phase B correction (not Phase B.5, which is TERMCENTRIC-specific per §6.4). Recorded here for encoding in the r112 patch.

[PHASE-B-CORRECTION] 1010-001 | G3510 nefros | Reg 112 (mind)
OLD: *Term names an inner faculty of the person — the deep inner life searched and assessed by Christ*
NEW: *Term names the deep inner life — the hidden motives and affections of the person open only to divine searching*
RATIONALE: Original description was QA-VAGUE — "an inner faculty" did not name the specific inner-being characteristic. Revised description names "the deep inner life" as the characteristic, specifies "hidden motives and affections" as its content, and preserves the divine-searching theme ("open only to divine searching"). The revision is grounded in the single anchor verse (Rev 2:23) where Christ is named as the searcher of nefrous and kardias.
PATCH-TARGET: verse_context_group.id and wa_dimension_index.id — to be encoded in r112 patch.

---

## Phase C r112 entries

### Root family: YATSAR (Hebrew) — 1 group

[PHASE-C] 3602-001 | H3335I ya.tsar "to form: plan" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **NONE** (divine and human agents both named in description)
NOTES: Description names "purposive formation — inner act of planning or forming a purpose, whether divine sovereign intention or human scheme." The act-of-willing/purposing characteristic is the clean §7.7 match (04 Volition — "Inner acts of willing, purposing, choosing, desiring, and deciding"). Legacy label "Volitional/Will" maps to 04 Volition. Dominant subject is NONE because the description explicitly names both divine and human agents without one dominating.
PATCH-TARGET: wa_dimension_index.id = 2707 (per extract join)

### Root family: SHIT (Hebrew) — 1 group

[PHASE-C] 3578-001 | H7896K shit "to set: consider" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "the inner act of setting attention — directing the mind to consider, take to heart, or attend carefully to a matter or person." This is an act of attention-directing and consideration — the cognitive act of taking something to mind (§7.7 03 Cognition: "Inner acts of knowing, perceiving, remembering, understanding, and discerning"). Legacy label "Cognitive/Mind" maps to 03 Cognition. Human subject across the verse corpus (covenant people attending to God's acts, wisdom).
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: NEFR (Greek) — 1 group

[PHASE-C] 1010-001 | G3510 nefros "mind" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN** (as the object of divine searching)
NOTES: Revised description (RD-PHASE-B-112-001 in-session correction) reads *"Term names the deep inner life — the hidden motives and affections of the person open only to divine searching."* The characteristic is the hidden moral reality of the person — what is open only to God's knowledge. This is §7.7 05 Moral Character territory (stable inner qualities of moral nature; the hidden interior is where moral character resides). Could also be read as 11 Divine-Human Correspondence given the divine searcher; but the primary characteristic named is the human's hidden moral interior, with divine knowledge as context. HUMAN is the dominant_subject (the person whose nefros is searched); GOD is the searcher in the verse but not the dominant subject of the characteristic named. Legacy label "Volitional/Capacity" is not a good fit; 05 Moral Character is a cleaner reading.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: METABALLŌ (Greek) — 1 group

[PHASE-C] 2662-001 | G3328 metaballō "to change mind" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "reversal of inner judgment — changing one's assessment of a person or situation." This is a cognitive reassessment act. Legacy label "Volitional/Will" could also apply, but the specific content is re-judging — which is §7.7 03 Cognition. Acts 28:6 is the one verse; the subjects (the Maltese islanders revising their view of Paul) are human persons in the narrative. The characteristic is the general human cognitive act of reassessment, not a special category of "other human in relationship with the inner-being-person being studied" — HUMAN is the cleaner assignment.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: NADAV (Hebrew) — 2 groups

[PHASE-C] 3058-001 | H5069 ne.dav "be willing" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "freewill inner disposition — voluntary offering or willingness expressed in dedication to God's house." The characteristic is voluntary willing — direct §7.7 04 Volition match. Human subject (the offerer).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3059-001 | H5068 na.dav "be willing" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner disposition of willing, voluntary devotion — heart spontaneously moved to give or serve without compulsion." Same characteristic as 3058-001 in a different Strongs within the root — voluntary willing. §7.7 04 Volition. The §7.7 note to the Volition dimension — *"Stable orientation of the will toward God or others → consider Relational Disposition (06)"* — merits consideration here, but the characteristic named is the act of willing (volitional-capacity, not stable disposition-toward-God); 04 Volition stands.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: NĒFŌ (Greek) — 2 groups

[PHASE-C] 4192-001 | G3525 nēfō "be sober" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "commanded inner disposition of sober alertness — mind clear and watchful, not given to spiritual or moral drowsiness." This is a stable inner disposition of character — §7.7 05 Moral Character ("Stable inner qualities of moral nature — goodness, justice, integrity, purity, faithfulness"). The "commanded" language is theological context, not the characteristic itself. Legacy label "Character/Disposition" maps to 05 Moral Character.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4315-001 | G3524 nēfaleos "sober" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "sobriety of mind as character quality — inner disposition of measured, clear-headed judgment required for leadership." §7.7 05 Moral Character. Paired with 4192-001 (verbal command vs character-quality adjective). Same dimension assignment.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: GNŌM (Greek) — 2 groups

[PHASE-C] 1001-001 | G1106 gnōmē "resolution" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "considered judgment or opinion of a person — an inner resolution or assessment offered with authority." Cognition dominates (the inner act of judgment/assessment); Volition is adjacent (resolution as will-act) but the primary content is assessment. §7.7 03 Cognition.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 1001-002 | G1106 gnōmē "resolution" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **NONE** (both God-placing and persons-forming are named)
NOTES: Description names "shared inner purpose — collective resolution placed in hearts by God or formed among persons toward a common end." Distinct from 1001-001 — this is collective resolution, the volitional-shared-purpose characteristic. §7.7 04 Volition with a relational colour. Dominant subject NONE because the verse evidence shows both divine agency (placing in hearts) and human agency (forming).
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: DIPSUCH (Greek) — 2 groups

[PHASE-C] 1398-001 | G1374 dipsuchos "double-minded" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner division of allegiance — person whose loyalty is split between God and world, producing instability." The characteristic is the moral condition of divided loyalty — a stable (or rather, unstable) inner moral-character state. §7.7 05 Moral Character. Could also be read as 04 Volition (divided will) but the letter-of-James context (the dipsuchos is unstable in all ways) points to character. Legacy label "Moral/Conscience" maps defensibly to 05 Moral Character.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 1402-001 | G2473 isopsuchos "like-minded" | Reg 112 (mind)
DIMENSION: **06 Relational Disposition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "shared inner disposition — genuine concern and aligned soul-orientation toward others." The characteristic is relational alignment/disposition toward others (Paul of Timothy: "I have no one like-minded who will genuinely care for your welfare"). §7.7 06 Relational Disposition ("Inner orientation toward another — love, compassion, favour, attachment, contempt, hatred"). Distinct dimension from its semantic pair dipsuchos (which is about divided self-orientation, not relational).
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: SEEPH (Hebrew) — 2 groups

[PHASE-C] 2707-001 | H5587B se.ip.pim "disquietings" | Reg 112 (mind)
DIMENSION: **02 Emotion — Negative**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "troubled, disquieting thoughts — inner agitation of the mind under pressure or in visionary states." The characteristic is inner agitation/disquiet — a negative affective state. §7.7 02 Emotion — Negative ("Inner states of pain, distress, grief, fear, anger, shame, or anxiety"). The "thoughts" language is medium; the characteristic is the disquiet itself (anxiety-territory).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4198-001 | H5588 se.eph "divided" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner division — split allegiance of the person who cannot commit fully to God's law." Same characteristic as dipsuchos (1398-001) in Hebrew vocabulary — the divided heart of Psalm 119:113. §7.7 05 Moral Character. Cross-root thematic resonance confirmed at Phase B; formalised as Session D pointer below.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: BOUL (Greek) — 2 groups

[PHASE-C] 2109-001 | G1011 bouleuō "to plan" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner act of deliberate decision — mind resolving upon a course of action through weighing and choosing." Direct §7.7 04 Volition match. BOUL root family flagged for Session D pointer.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 2109-002 | G1011 bouleuō "to plan" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "deliberate planning directed toward harm — inner will forming intention against another." §7.7 04 Volition with negative moral valence. The harm-direction does not change the dimension (planning-directed-toward-harm is still a volitional act); the moral valence is a Phase C note, not a dimension split.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: AZKARAH (Hebrew) — 4 groups

The four memorial groups test the Spiritual/God-ward vocabulary gap directly. Per Phase A observation, these sit at the boundary between institutional/liturgical act and inner divine-human remembrance. Reading each carefully:

[PHASE-C] 3498-001 | H2146 zik.ka.ron "memorial" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **NONE** (both divine remembrance and communal keeping are named as operating together)
NOTES: Description names "institutional memorial — act/object/day established to keep an event or person before God and the community across generations." The inner-being content is divine-human shared memory — God remembering through what the community keeps, the community keeping through what God has instituted. This is §7.7 11 Divine-Human Correspondence territory (inner characteristics operating across the divine-human boundary). Alternatively, if the weight is on the human cognitive act (keeping in mind), 03 Cognition would apply. The reading that better captures the characteristic is 11 — the memorial is not a cognitive act alone but a structure of mutual remembrance. Legacy label "Spiritual/God-ward" maps cleanly to 11 here. Session D pattern: all four memorial groups likely share this Dimension 11 framing.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3498-002 | H2146 zik.ka.ron "memorial" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **NONE**
NOTES: Description names "priestly/liturgical keeping of persons before God — act of bearing names or offerings into God's presence for ongoing remembrance." Same pattern as 3498-001 — divine-human shared memory, with the priest as mediating agent. §7.7 11 Divine-Human Correspondence.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3498-003 | H2146 zik.ka.ron "memorial" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner act of remembrance — capacity to hold persons and events in living consciousness, and absence of such memory as loss." This sense-split is the cognitive-remembrance characteristic specifically, without the institutional/liturgical structure that 3498-001 and 3498-002 carry. §7.7 03 Cognition ("Inner acts of knowing, perceiving, remembering, understanding, and discerning"). Distinct from the memorial-institution pattern.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3499-001 | H0234 az.ka.rah "memorial" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **NONE**
NOTES: Description names "the memorial portion of an offering — part burned before God as act of bringing offerer to divine remembrance." The characteristic is the offering as a vehicle for divine-human correspondence of remembrance. §7.7 11 Divine-Human Correspondence. Paired with 3498-001/002 as institutional memorial vocabulary.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: SHAMAR (Hebrew) — 5 groups

[PHASE-C] 4379-001 | H8104G sha.mar "to keep: obey" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner disposition of covenantal obedience — will, heart, and soul directed toward faithful keeping of God's commands across generations." §7.7 04 Volition Note: *"Stable orientation of the will toward God or others → consider Relational Disposition (06)."* This is borderline — covenantal obedience is simultaneously an act of willing (keeping God's commands) and a stable relational orientation toward God. The directionally-determined inner-faculty principle (memory finding from earlier programme work) applies: will directed toward God. 04 Volition captures the act-of-keeping characteristic; 06 Relational Disposition would capture it from the relational-orientation side. The cleaner fit for "inner disposition of covenantal obedience" as it operates in the 193-verse corpus — which runs across law-keeping, command-keeping, generational fidelity — is 04 Volition with the relational orientation as context. Very high-density group; the dimension assignment may warrant Session D attention (cross-cluster pattern: volitional terms with stable relational orientation).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4380-001 | H8104H sha.mar "to keep: guard" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **GOD**
NOTES: Description names "God's guarding of his people — divine inner disposition of protective care that preserves, shields, and keeps those who belong to him." GOD is the subject; the characteristic is God's guarding as direct ground/mirror of what his people are called to in 4380-002 (self-guarding). §7.7 11 Divine-Human Correspondence is the explicit framing for *"the same quality, act, or state appears in both divine and human subjects within the same group, or where God's inner-being characteristic is the direct ground, mirror, or counterpart of the human characteristic."* The sha.mar root shows exactly this pattern: divine guarding (4380-001) and human self-guarding (4380-002) are the same characteristic in divine and human subjects. Strong Dimension 11 candidate. Session D candidate for root-level correspondence pattern.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4380-002 | H8104H sha.mar "to keep: guard" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "self-keeping from moral harm — inner discipline of guarding one's ways, mouth, and soul from sin and its consequences." Paired with 4380-001 as the human-side of the same characteristic (divine guarding / human self-guarding). §7.7 11 Divine-Human Correspondence with the instruction note on 11 Divine-Human Correspondence explicitly applied: "Assign `GOD` or `HUMAN` where one pole dominates but the correspondence is analytically significant." The correspondence is significant; HUMAN dominates this sense-split.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4381-001 | H8104I sha.mar "to keep: look at" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **NONE** (God as moral observer and human moral observation both named)
NOTES: Description names "attentive moral observation — watching over conduct, marking iniquity, or directing inner regard toward a person or object with moral consequence." The characteristic is attention/observation — cognitive. §7.7 03 Cognition. Alternatively 11 Divine-Human Correspondence (if the moral-observation is primarily divine), but the description frames this more broadly than the 4380 pair. Marking/observing/regarding is the cognitive act.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4382-001 | H8104J sha.mar "to keep: careful" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "careful, attentive inner vigilance — disposition of watchfulness toward one's conduct, duties, or dangers, especially in relation to God's commands." This is a stable inner-disposition characteristic (watchfulness, vigilance) — §7.7 05 Moral Character. Contrast with 4379-001 (act of keeping covenant, 04 Volition) and 4380-002 (inner discipline of self-guarding, 11 Divine-Human Correspondence) — each sha.mar sense engages a different dimension. Session D pattern: sha.mar root shows remarkable dimensional breadth across senses (04, 11, 11, 03, 05).
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: HALAL (Hebrew) — 5 groups

[PHASE-C] 4331-001 | H1984C ha.lal "to be foolish" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "madness or derangement — inner disruption of reason and moral orientation, whether feigned, induced, or corporate." Madness sits at an interesting §7.7 boundary — cognitive-disruption on one reading (reason undone → 03 Cognition) and affective-disorder on another (inner disquiet → 02 Emotion — Negative). For this group specifically ("disruption of reason and moral orientation"), 03 Cognition is the cleaner fit — reason is named explicitly as the object of disruption. This is one of the 2 open groups (MO=0, KEYWORD_WEAK); legacy "Moral Character" label is not a good fit.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4331-002 | H1984C ha.lal "to be foolish" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "boasting arrogance as inner orientation — exaltation of self before God and others." Characterological pride / self-exaltation — §7.7 05 Moral Character (integrity / its opposite). Legacy label "Moral/Conscience" is acceptable; 05 is cleaner.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4335-001 | H1984I ha.lal "to boast: rave madly" | Reg 112 (mind)
DIMENSION: **02 Emotion — Negative**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "raving madness or contemptuous derision — expression of disordered inner intensity, whether in mockery, futility, or frenzied action." The characteristic is disordered inner intensity — affective dysregulation with contempt as one outlet. §7.7 02 Emotion — Negative; contempt is explicitly in §7.7 06 Relational Disposition's vocabulary but the characteristic here is the internal disorder producing it, not the relational attitude itself. 02 stands.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4337-001 | H1947 ho.le.lah "madness" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "madness as inner condition — disordered, futile orientation of the human heart and mind, investigated alongside wisdom." Ecclesiastes context. Madness-as-cognitive-disorder, paired with wisdom in the Qohelet investigation. §7.7 03 Cognition (the inner rational-discerning faculty, here in its disorder).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4339-001 | H1948 ho.le.lut "madness" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "madness as culmination of foolishness — final evil expression of a disordered inner life." The moral-character framing is explicit ("final evil expression"). 05 Moral Character. Contrast with 4337-001 (Cognition — the disordered state investigated) and this group (Moral Character — the moral expression).
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: CHASHAV (Hebrew) — 7 groups

[PHASE-C] 3334-001 | H2803I cha.shav "to devise: devise" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **HUMAN** (occasionally OTHER_HUMAN in victim framing)
NOTES: Description names "deliberate devising of harm — inner formation of schemes, plots, or evil plans against another." §7.7 04 Volition with negative moral valence. The purposive-act-of-planning characteristic dominates. Cross-registry root family CHASHAV (Phase A Session D candidate) spans mind/purpose/thought — all likely Volition or Cognition territory in their registry neighbours.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3334-002 | H2803I cha.shav "to devise: devise" | Reg 112 (mind)
DIMENSION: **04 Volition**
DOMINANT-SUBJECT: **NONE** (divine and human agents both named)
NOTES: Description names "purposive planning — inner formation of a deliberate purpose or plan, whether by God or human agents." The broader (non-harm-specific) volitional characteristic. §7.7 04 Volition. NONE dominant_subject since the description explicitly spans divine and human.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3335-001 | H2803H cha.shav "to devise: count" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **GOD** (imputation is primarily God's act in Genesis 15:6 / Romans 4 / Abraham's faith)
NOTES: Description names "moral crediting or imputing of righteousness/guilt — inner act of reckoning a person's standing before God or human authority." This is the Genesis 15:6 imputation term (cha.shav as "reckoned it to him as righteousness"). The characteristic is divine reckoning — a theologically weighted act where God's inner assessment determines a person's standing. §7.7 11 Divine-Human Correspondence is the right frame: God's reckoning is the direct ground of the human's righteousness-standing. Alternatively 03 Cognition (act of reckoning) but that loses the theological-structural framing that makes this term one of the most weighty in the OT. GOD is the dominant subject per §7.7 11 note ("Assign GOD where one pole dominates but the correspondence is analytically significant"). Strong Session B finding candidate.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3335-002 | H2803H cha.shav "to devise: count" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "evaluative regard of persons or things — inner act of assessing worth, status, or character in relational and social contexts." Distinct from 3335-001 — this is the human-social act of reckoning, without the theological imputation-structure. §7.7 03 Cognition (evaluative cognition). The legacy label "Relational/Social" pointed toward Relational Disposition, but the characteristic is the act of evaluation, not the relational attitude produced — 03 Cognition is cleaner.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3336-001 | H2803J cha.shav "to devise: think" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner act of thinking and considering — mind forming judgments, reconsidering paths, or holding deliberate thoughts." Direct §7.7 03 Cognition match.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3336-002 | H2803J cha.shav "to devise: think" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner evaluative act of counting or regarding — assessing a person's or thing's worth, status, or standing." Per RD-PHASE-B-112-002, accepted as-is (distinct Strongs sense H2803J "think" from H2803H "count" 3335-002 despite descriptive similarity). §7.7 03 Cognition. Functionally similar dimension assignment to 3335-002 — confirms that the descriptive overlap reflects genuine functional overlap between two Strongs senses in the verbs of reckoning/evaluating, not a grouping defect.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3338-001 | H2810 chish.sha.von "invention" | Reg 112 (mind)
DIMENSION: **09 Agency / Power**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "product of human ingenuity — devices or schemes formed by the inner inventive capacity, whether for construction or moral harm." The characteristic is inner inventive capacity — §7.7 09 Agency / Power ("The exercise of inner capacity — sovereignty, authority, strength, restraint, self-giving"). One of the 2 open groups (MO=0, KEYWORD_WEAK). Legacy label "Moral Character" is not a good fit. Alternative 04 Volition (purposive planning); 09 is closer because the content is *capacity to invent* rather than *act of willing*.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: NOUS (Greek) — 10 groups

[PHASE-C] 1000-001 | G3105 mainomai "to rave" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN** (or OTHER_HUMAN when it is an accusation)
NOTES: Description names "disruption or perceived disruption of rational inner faculties — being out of one's mind." §7.7 03 Cognition (the rational faculty in its disorder). Paired with mania (1006-001) and parafroneō (4185-001).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 1006-001 | G3130 mania "insanity" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "state of mental derangement — collapse of rational inner faculties attributed to excessive learning." §7.7 03 Cognition (rational faculties in collapse). Acts 26:24 — Festus accusing Paul.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3370-001 | G1950 epilanthanō "to forget" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner act of forgetting or neglecting — failure to retain in active consciousness what matters morally or relationally." §7.7 03 Cognition (remembering/forgetting is within the Cognition dimension). The "morally or relationally" language names context, not the characteristic. 03 stands.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 3372-001 | G1771 ennoia "thought/purpose" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner thoughts and purposes of the heart — hidden intentional life that only God's word can discern and expose." The characteristic is the hidden inner thinking. §7.7 03 Cognition. Could be read as 05 Moral Character (hidden intentional life as character content), but the explicit naming of "thoughts and purposes" (cognitive content) makes 03 the cleaner fit.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 994-001 | G3563 nous "mind" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "mind as capable of knowing God and serving his law — rational-moral faculty oriented toward truth and divine will." The characteristic is the mind as cognitive faculty oriented toward God. §7.7 03 Cognition captures the rational-faculty content. The orientation-toward-God is context (and this is one of the groups touching the Spiritual/God-ward vocabulary gap). Reading: 03 Cognition is the correct primary dimension; the God-ward aspect is Session D material (pattern of Cognition groups oriented toward God).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 994-002 | G3563 nous "mind" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "mind as corrupted, debased, or futile — rational faculty given over to moral disorder or darkened by sin." Same dimension (03 Cognition) as 994-001, moral-negative pole. The corruption/futility language is moral-character adjacent but the characteristic named is the state of the rational faculty.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 994-003 | G3563 nous "mind" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **GOD**
NOTES: Description names "mind of the Lord/God — divine inner rational-purposive faculty inaccessible to humans except through revelation." 1 Corinthians 2:16 / Romans 11:34 context. §7.7 03 Cognition applied to the divine subject. GOD dominant_subject. Interesting — the dimension 11 framing might apply if there is a direct correspondence between divine mind and transformed human mind (1 Cor 2:16 "we have the mind of Christ"), but the primary content of this sense-split is the divine mind as hidden/inaccessible — 03 with GOD as subject is cleaner.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 995-001 | G1271 dianoia "mind" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "mind as seat of love and orientation toward God — whole inner capacity directed Godward in the great commandment." Deuteronomy 6:5 / Mark 12:30 context. The characteristic is the whole inner mind directed toward loving God — this is Divine-Human Correspondence on the human side (the commandment names what the human inner-being is to do; the characteristic is the inner orientation reaching across the human-divine boundary). §7.7 11. Could be 04 Volition (loving God is will-act) or 06 Relational Disposition (stable orientation toward God); the Divine-Human Correspondence frame best captures the characteristic. Dominant_subject HUMAN — the human is the bearer of this love-orientation.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 995-002 | G1271 dianoia "mind" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "mind as susceptible to darkening, hostility, or moral corruption — understanding alienated from God or carrying out sinful desires." Parallel to 994-002 for dianoia. §7.7 03 Cognition — the corrupted state of the rational-understanding faculty.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 995-003 | G1271 dianoia "mind" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **NONE** (God's writing + human receiving)
NOTES: Description names "mind as site of divine law-writing and renewal — inner capacity transformed and inscribed by God under the new covenant." Hebrews 8:10 / 10:16 context. This is the clearest Dimension 11 case in r112 — God writing on the dianoia, the human dianoia receiving. The divine-human correspondence is the characteristic. Strong Session D candidate for the covenant-renewal cluster (paired with mnaomai 4413-003 non-remembrance, le.vav 579-009 circumcision, qe.rev 577-003 new covenant writing, enkainizō 602-001).
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: MNE (Greek) — 13 groups

[PHASE-C] 4291-001 | G5280 hupomnēsis "remembrance" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN** (apostle as the agent reminding the community)
NOTES: Description names "act of reminding as pastoral instrument — stirring up inner life by bringing truth back to active consciousness." §7.7 03 Cognition. The pastoral-agent framing is context.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4292-001 | G5279 hupomimnēskō "to remind" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **NONE** (Spirit, apostle, person — description explicitly names all three agents)
NOTES: Description names "prompting of inner remembrance — bringing truth or prior words back into active inner awareness through the Spirit, an apostle, or another person." §7.7 03 Cognition. Dominant subject NONE — the description spans three distinct agent types.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4411-001 | G3421 mnēmoneuō "to remember" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "commanded inner act of remembrance — calling to mind persons, words, or events as basis for present faith and conduct." §7.7 03 Cognition. High-density group (18 total verses) — remembrance as a commanded covenantal act. The "commanded" and "faith/conduct" language touches the Spiritual/God-ward vocabulary gap; 03 Cognition captures the characteristic correctly. Session D observation: commanded-remembrance as a pattern where Cognition has covenantal-ethical weight.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4411-002 | G3421 mnēmoneuō "to remember" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner orientation of remembrance as motivating force — thinking of, being concerned with, holding in mind as ground of present action." Same dimension (03 Cognition) as 4411-001, the motivating-force sense of remembrance.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4412-001 | G3420 mnēmē "remembrance" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "capacity for recall — ability to bring to active consciousness what has been received." §7.7 03 Cognition. Direct match. Legacy label "Volitional/Capacity" is not a good fit.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4413-001 | G3415 mnaomai "to remember" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "human remembrance — inner act of bringing to mind what was said, experienced, or promised." §7.7 03 Cognition.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4413-002 | G3415 mnaomai "to remember" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **GOD**
NOTES: Description names "divine remembrance — God holding a person or their deeds in active attentiveness, with grace or judgment as the result." The characteristic is God's remembering as ground of effect (grace or judgement). §7.7 11 Divine-Human Correspondence — divine remembrance has direct effect on the human, the structural correspondence is the ground-effect pattern. GOD dominant subject. Paired with 3335-001 (cha.shav imputation) as Dimension 11 patterns where divine inner-act grounds human standing.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4413-003 | G3415 mnaomai "to remember" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **GOD**
NOTES: Description names "God's chosen non-remembrance — new covenant promise to remember sins no more." Hebrews 8:12 / 10:17 / Jeremiah 31:34 context. The characteristic is divine non-remembrance as covenant act — structural divine-human correspondence where God's inner act determines the covenant's character. §7.7 11. Core member of the covenant-renewal Session D cluster.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4416-001 | G3417 mneia "remembrance" | Reg 112 (mind)
DIMENSION: **06 Relational Disposition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "affectionate remembrance of persons — holding them in active prayerful awareness before God." The characteristic is relational affection expressed through remembrance — not simply the cognitive act of recall but the affectionate orientation toward another. §7.7 06 Relational Disposition ("Inner orientation toward another — love, compassion, favour, attachment…"). The Pauline epistolary "I remember you in my prayers" pattern. Distinct from other mnaomai senses by its relational content.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4417-001 | G3403 mimnēskō "to remember" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner act of mindful attentiveness — holding another in active awareness with moral or relational consequence." §7.7 03 Cognition. Moral/relational consequence is context.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4424-001 | G0363 anamimnēskō "to remind" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner act of bringing prior knowledge or experience back into active awareness — voluntary recall or prompted remembrance." §7.7 03 Cognition.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4426-001 | G0364 anamnēsis "remembrance" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **NONE** (Christ's act and community's keeping both named)
NOTES: Description names "eucharistic act of remembrance — inner and communal re-presentation of Christ's self-giving before God and one another." The anamnēsis of 1 Cor 11:24-25 / Luke 22:19 — the Lord's Supper. This is the signature Dimension 11 case in the NT for memorial vocabulary: Christ's giving grounds the community's remembering; the two operate across the divine-human boundary. §7.7 11. Paired with the AZKARAH group as Dimension 11 patterns for memorial vocabulary.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4426-002 | G0364 anamnēsis "remembrance" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "annual reminder of unresolved sin — old covenant's inability to finally cleanse the conscience." Hebrews 10:3 context. The characteristic is the conscience's unresolved state — §7.7 05 Moral Character (moral character and conscience are adjacent in the dimension). Distinct from 4426-001 (new covenant memorial as divine-human correspondence) by the old covenant's failure framing. 05 Moral Character captures the conscience-state characteristic; alternatively 03 Cognition (the reminding act) but the semantic weight here is on the inner moral state reminded, not the act of reminding.
PATCH-TARGET: wa_dimension_index.id (from extract)

### Root family: FRĒN (Greek) — 13 groups

[PHASE-C] 1008-001 | G3675 homofrōn "like-minded" | Reg 112 (mind)
DIMENSION: **06 Relational Disposition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "unity of inner orientation — shared disposition of mind and spirit among the community." 1 Peter 3:8. §7.7 06 Relational Disposition (shared orientation toward one another).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 1009-001 | G5391 filofrōn "friendly" | Reg 112 (mind)
DIMENSION: **06 Relational Disposition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "tender, friendly inner disposition — mind oriented toward others with gentleness and courtesy." §7.7 06 Relational Disposition.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 2493-001 | G5424 frēn "thinking" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "faculty of mature thinking — capacity for moral and rational discernment that marks adult inner life." 1 Cor 14:20 context. §7.7 03 Cognition.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4185-001 | G3912 parafroneō "be insane" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN** (Paul in 2 Cor 11:23 "I speak as one beside himself")
NOTES: Description names "mode of expression that departs from rational restraint — speaking beyond reason, used rhetorically to mark apostolic boasting as a concession." §7.7 03 Cognition (the rational faculty in its departure).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4187-001 | G3913 parafronia "insanity" | Reg 112 (mind)
DIMENSION: **03 Cognition**
DOMINANT-SUBJECT: **HUMAN** (Balaam in 2 Pet 2:16)
NOTES: Description names "madness of disordered inner impulse — prophet's irrational compulsion rebuked by God through a donkey." §7.7 03 Cognition (rational faculty in its disorder).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4188-001 | G4998 sōfrōn "self-controlled" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "self-control as inner character quality — disciplined mind that governs its impulses, required for godly leadership and life." §7.7 05 Moral Character — direct match ("Stable inner qualities of moral nature — goodness, justice, integrity, purity, faithfulness" — self-control is in this family).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4190-001 | G4994 sōfronizō "to train" | Reg 112 (mind)
DIMENSION: **08 Transformation**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "formation of inner dispositions through training — shaping the affective and relational life toward godly patterns." Titus 2:4 context (older women training younger). The characteristic is formation/transformation of inner disposition. §7.7 08 Transformation ("Inner change — renewal, healing, purification, formation, or degradation"). This is a less-used dimension in the cluster but fits the characteristic precisely.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 4191-001 | G4996 sōfronōs "in self-control" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "inner disposition of self-controlled living — mind governing conduct with measured restraint." §7.7 05 Moral Character — same family as 4188-001.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 996-001 | G5426 froneō "to reason" | Reg 112 (mind)
DIMENSION: **11 Divine-Human Correspondence**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "direction of the mind — setting one's inner orientation toward God, the Spirit, or godly patterns of life." Romans 8:5-6 / Colossians 3:2 context ("set your minds on things above"). The characteristic is the mind's orientation across the human-divine boundary — setting the inner mind toward God. §7.7 11 Divine-Human Correspondence. Alternatively 04 Volition (the act of directing) or 06 Relational Disposition (stable orientation toward God). The cleanest reading for "setting one's inner orientation toward God" is Dimension 11 — the mind's engagement across the boundary. HUMAN dominant, with God as the orientation's object.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 996-002 | G5426 froneō "to reason" | Reg 112 (mind)
DIMENSION: **06 Relational Disposition**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "mind as seat of communal unity and personal relationship — being of the same mind, sharing concern, pursuing agreement." Philippians 2:2 / Romans 12:16 context. §7.7 06 Relational Disposition (inner orientation toward one another).
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 997-001 | G5427 fronēma "purpose" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "settled orientation of the inner mind — deep dispositional set of the person toward flesh or Spirit, with life or death as the outcome." Romans 8:6-7 context. The characteristic is the deep dispositional set — §7.7 05 Moral Character (stable inner quality of moral nature). The flesh/Spirit framing is moral; the outcomes (life/death) confirm the character-weight. Alternatively 11 Divine-Human Correspondence if the flesh/Spirit alternative is taken as the divine-human boundary orientation.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 999-001 | G4993 sōfroneō "be of sound mind" | Reg 112 (mind)
DIMENSION: **08 Transformation**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "restoration of sound mind — inner rational and moral faculties recovered from disruption." Mark 5:15 / Luke 8:35 (Gerasene demoniac). The characteristic is restoration/recovery — §7.7 08 Transformation (healing, renewal). Distinct sense from 999-002 by its restoration-event framing.
PATCH-TARGET: wa_dimension_index.id (from extract)

[PHASE-C] 999-002 | G4993 sōfroneō "be of sound mind" | Reg 112 (mind)
DIMENSION: **05 Moral Character**
DOMINANT-SUBJECT: **HUMAN**
NOTES: Description names "sound-mindedness as moral disposition — thinking about oneself and others with measured, humble judgment." Romans 12:3 context. §7.7 05 Moral Character (stable inner quality of measured judgement).
PATCH-TARGET: wa_dimension_index.id (from extract)

---

## [COVERAGE-VERIFY] C01 | Phase C r112 — closing tally

Groups requiring Phase C: **73** (all active r112 groups)
Groups with Phase C entry in observations log: **73**
Result: **CONFIRMED** — all 73 r112 groups have a Phase C entry.

### Dimension distribution under current §7.7 vocabulary (r112 Phase C)

| Dimension | Count | Notes |
|---|---:|---|
| 03 Cognition | 29 | Dominant dimension in r112 — unsurprising for the mind registry |
| 05 Moral Character | 13 | Character terms (sōfrōn, sōfronōs, dipsuchos, ha.lal boasting, ennoia) |
| 11 Divine-Human Correspondence | 12 | Covenant-renewal, divine remembrance, imputation, sha.mar-guard pair, memorials, froneō-toward-God |
| 04 Volition | 9 | ne.dav, bouleuō, sha.mar-obey, cha.shav-devise |
| 06 Relational Disposition | 5 | homofrōn, filofrōn, isopsuchos, mneia, froneō-communal |
| 02 Emotion — Negative | 2 | se.ip.pim, ha.lal-raving |
| 08 Transformation | 2 | sōfronizō, sōfroneō-restoration |
| 09 Agency / Power | 1 | chish.sha.von |
| **Total** | **73** | Verified by re-count against PHASE-C entries |

**Observations on distribution:**
- **No group needed a dimension outside current §7.7 vocabulary.** The three Phase A vocabulary gaps (Spiritual/God-ward, Identity/Selfhood, Somatic/Embodied) did not force a new-dimension proposal in r112 — groups that had carried "Spiritual/God-ward" in the legacy vocabulary mostly resolved to Dimension 11 (Divine-Human Correspondence) when the divine-human correspondence structure was present, or to 03 Cognition / 04 Volition when the characteristic was a human act with God as context. r112 did not surface a dimensional gap.
- **Dimension 11 is well-represented (12 groups).** This is consistent with the Phase A observation that C01 is the inner-being reference cluster where divine-human correspondence patterns emerge strongly. The memorial groups, covenant-renewal groups, sha.mar-guard pair, imputation (cha.shav-count), divine remembrance (mnaomai), and mind-directed-toward-God groups (dianoia 995-001, froneō 996-001, dianoia 995-003) all land here.
- **Zero groups assigned 01 Emotion — Positive, 07 Vitality/Existence, 10 Dependence/Creatureliness.** r112 does not engage these characteristics — consistent with its being the mind registry (cognitive-volitional-character dominant).

### Dominant_subject distribution (r112 Phase C)

| dominant_subject | Count | Notes |
|---|---:|---|
| HUMAN | 58 | Dominant — most r112 groups name human inner faculties |
| NONE | 10 | Groups where both divine and human are named as subjects (e.g., memorial groups, gnōmē-collective, mnēmoneuō cross-agent, sha.mar-observation, ya.tsar-form, cha.shav-devise-broad, dianoia-law-writing, anamnēsis-eucharist) |
| GOD | 5 | nous-divine (994-003), cha.shav-impute (3335-001), mnaomai-divine (4413-002), mnaomai-non-remembrance (4413-003), sha.mar-guard-God (4380-001) |
| OTHER_HUMAN | 0 | Zero in r112 — after revision of metaballō 2662-001 to HUMAN |
| UNSEEN | 0 | Zero in r112 |
| **Total** | **73** | Verified by re-count against PHASE-C entries |

---

## [AV-VERIFY] — absorbed into Phase C entries

Per §7.4 Step 3, anchor verse verification is required. For QA-CLEAR groups (71 of 73) with straightforward dimension assignment, AV-VERIFY is absorbed into the Phase C entry's NOTES field — the verification that the description matches the verse evidence was the Phase B task and was confirmed in v1_1. No new AV-VERIFY entries are written for QA-CLEAR groups in this Phase C session, per the option available in §7.4 ("The cluster extract provides anchor verse references; where a description is insufficient Claude AI requests an extract").

For the 2 non-CLEAR groups from Phase B:
- `1010-001 nefros` — QA-VAGUE resolved via in-session description correction (recorded above). AV verified against Rev 2:23 anchor: characteristic of "hidden motives and affections open only to divine searching" aligns with the verse (Christ searching minds and hearts).
- `3336-002 cha.shav` — QA-REVIEW accepted as-is per RD. AV for this group and 3335-002 were not formally verified (researcher directed accept-as-is); the dimension assignments (03 Cognition for both) are consistent.

---

## Phase C researcher decision items

One item arose during Phase C analysis:

### RD-PHASE-C-112-001 — Dimension 11 scope for "setting mind toward God" patterns

Three r112 groups resolved to Dimension 11 (Divine-Human Correspondence) on the reading that "setting/orienting the mind toward God" is a cross-boundary characteristic: 995-001 dianoia (love God with all your mind), 996-001 froneō (set mind on things above). These groups could alternatively be classified as 04 Volition (act of directing) or 06 Relational Disposition (stable orientation toward God).

**Question:** Confirm Dimension 11 reading for these groups, or direct alternative assignment?

**Claude AI assessment:** Dimension 11 is the cleaner fit. The §7.7 11 definition — *"Inner-being characteristics that operate across the boundary between God and the human person"* — is explicitly what these groups describe. The human's inner mind oriented toward God is inner-being operating across the boundary. However the researcher may prefer the more conservative 04 / 06 reading to reserve Dimension 11 for cases where divine-human correspondence is structural (divine act → human effect, or mirror-characteristic). Under that narrower reading, only 4380-001 + 4380-002 (sha.mar-guard pair), 4413-002 + 4413-003 (mnaomai divine), 3335-001 (imputation), 995-003 (law-writing), 4426-001 (anamnēsis eucharist), 3498-001/002, 3499-001 (memorials) truly qualify.

This is a Phase C judgement that affects 3-4 specific groups; it does not affect the overall dimension assignment count materially. Awaiting researcher direction before patch construction finalises.

---

## Session B findings — formalised entries

Per §7.5 and using §9.1 entry format. Numbering continues from existing `DIM-112-003` (highest pre-existing) → starts at `DIM-112-004`.

[SESSION-B] DIM-112-004
REGISTRY: 112 (mind)
DESCRIPTION: Covenant-renewal convergence across registries — a Dimension 11 cluster. Five groups across two target registries describe God's inner-being covenant act renewing the human person: dianoia law-writing (r112 995-003, Heb 8:10/10:16), mnaomai non-remembrance (r112 4413-003, Heb 8:12/10:17), le.vav circumcision/renewal (r183 579-009, Deut 30:6), qe.rev new covenant writing (r183 577-003, Jer 31:33 context), enkainizō inaugural renewal (r183 602-001, Heb 10:20). The new covenant is a coordinated Dimension 11 event across multiple inner-being terms and registries: God writes the law on the mind (dianoia), remembers sins no more (mnaomai), circumcises the heart (le.vav), writes within the inner parts (qe.rev), and inaugurates the new way (enkainizō). This is a strong Session B finding for word-study purposes — individual word studies on any of these terms should reference the cross-term pattern.
PATCH-TARGET: wa_session_b_findings insert

[SESSION-B] DIM-112-005
REGISTRY: 112 (mind)
DESCRIPTION: sha.mar root family dimensional breadth — Session B observation. The sha.mar root in r112 shows dimensional breadth across its five sense-splits: 4379-001 (obedience/keeping commands) → 04 Volition; 4380-001 (divine guarding) → 11 Divine-Human Correspondence (GOD); 4380-002 (self-guarding from sin) → 11 Divine-Human Correspondence (HUMAN); 4381-001 (moral observation) → 03 Cognition; 4382-001 (careful vigilance) → 05 Moral Character. Five sense-splits, five different dimensions — the same term engages the full range of inner-being characteristics depending on verse context. This is a strong illustration of the directionally-determined inner-faculty principle: the same term-faculty operates across dimensions, with orientation (what it is directed toward) determining the dimension.
PATCH-TARGET: wa_session_b_findings insert

[SESSION-B] DIM-112-006
REGISTRY: 112 (mind)
DESCRIPTION: Divine reckoning and divine remembrance as paired Dimension 11 patterns. cha.shav 3335-001 (imputation of righteousness — Gen 15:6) and mnaomai 4413-002 (divine remembrance with grace or judgement as result) are structurally parallel: both are divine inner acts that determine human standing. Imputation names God's reckoning (the Genesis 15:6 / Rom 4 pattern); divine remembrance names God's attentiveness producing effect. Both are Dimension 11 with GOD as dominant subject. This pair is foundational for Session B word studies of reckoning/imputation vocabulary and should be noted in any study of cha.shav, mnaomai, or related terms (e.g., logizomai not in r112).
PATCH-TARGET: wa_session_b_findings insert

[SESSION-B] DIM-112-007
REGISTRY: 112 (mind)
DESCRIPTION: Memorial vocabulary as Dimension 11 — institutional, liturgical, and eucharistic memorials in biblical vocabulary operate across the divine-human boundary. Three AZKARAH groups (3498-001 institutional zikkaron, 3498-002 priestly/liturgical zikkaron, 3499-001 memorial-portion offering) plus anamnēsis 4426-001 (eucharistic) all engage the divine-human correspondence dimension. The memorial is not a cognitive act alone — it is a structure of mutual remembrance between God and the community. This structural pattern unifies OT offering vocabulary and NT eucharist vocabulary on the dimension axis. Strong Session B finding for word studies of memorial/remembrance terms.
PATCH-TARGET: wa_session_b_findings insert

---

## Session D pointers — formalised entries

Per §7.5. Numbering continues from existing `DIM-112-SD002` → starts at `DIM-112-SD003`. All programme-wide flag_label uniqueness to be verified by researcher at patch review (per fallback path — flags file records programme-level issues but not individual pointer sequences).

[SESSION-D] DIM-112-SD003
REGISTRY: 112 (mind)
SESSION-TARGET: D
DESCRIPTION: CHASHAV root family cross-registry structural pattern. The Hebrew root chashav spans three registries — Reg 112 (mind: cha.shav H2803H/I/J "count/devise/think", chish.sha.von H2810 "invention"), Reg 126 (purpose: ma.cha.sha.vah H4284 "plot"), Reg 160 (thought: cha.shav H2803G "design", chesh.bon H2808 "explanation"). Across the root the functions split: (a) the verbal act of devising/thinking/counting (in mind), (b) the plan or plot as product (in purpose), (c) the calculation/explanation as articulated structure (in thought). At dimension level the r112 groups are predominantly 03 Cognition and 04 Volition. Session D synthesis should test whether the r126 and r160 groups carry the same dimensional profile (r126 and r160 were reviewed under earlier instruction versions and their dimensions may need reconsideration under current §7.7 vocabulary). The root unifies mental activity as ranging from act (mind) through product (purpose) to articulated content (thought).
PATCH-TARGET: wa_session_research_flags insert

[SESSION-D] DIM-112-SD004
REGISTRY: 112 (mind)
SESSION-TARGET: D
DESCRIPTION: BOUL root family Greek counterpart pattern to CHASHAV. The Greek root boul spans Reg 32 (counsel) and Reg 112 (mind). The verb bouleuō "to plan" (G1011) lives in mind; the nouns boulē (plan G1012), epiboulē (plot G1917), sumboulion (counsel/council G4824), sumboulos (counselor G4825) live in counsel. Same mental-act / mental-product / relational-noun pattern as CHASHAV. At dimension level the r112 bouleuō groups are 04 Volition. Session D synthesis should test whether the r32 groups carry Cognition, Volition, or Relational Disposition labels and whether the pattern is one characteristic across dimensions or multiple characteristics. The cross-language CHASHAV/BOUL convergence is a possible structural universal for Hebrew-Greek mental-act vocabulary.
PATCH-TARGET: wa_session_research_flags insert

[SESSION-D] DIM-112-SD005
REGISTRY: 112 (mind)
SESSION-TARGET: D
DESCRIPTION: Inner-division theme across Greek and Hebrew vocabularies. dipsuchos G1374 (r112 1398-001), se.eph H5588 (r112 4198-001), dianoia-corrupted (r112 995-002), nous-corrupted (r112 994-002), isopsuchos G2473 (r112 1402-001 — the positive counterpart). The inner-being characteristic of divided loyalty / split mind / darkened understanding is named by multiple terms from different roots and languages. isopsuchos is the positive counterpart (shared inner disposition). Dimensional distribution: mostly 05 Moral Character (for divided-allegiance characterological states), 03 Cognition (for corrupted-understanding states), 06 Relational Disposition (for aligned orientation). Session D should trace the divided-heart theme across clusters — likely appears in C17 (covenant) and C22 as well.
PATCH-TARGET: wa_session_research_flags insert

[SESSION-D] DIM-112-SD006
REGISTRY: 112 (mind)
SESSION-TARGET: D
DESCRIPTION: Spiritual/God-ward vocabulary gap — a current §7.7 dimension may be warranted (DR-13 researcher decision). Phase A identified that 25 groups across C01 carried the legacy label "Spiritual/God-ward" with no clean current-vocabulary counterpart. Through Phase C r112, these groups resolved mostly to Dimension 11 (Divine-Human Correspondence) where a structural divine-human correspondence was present, or to 03 Cognition / 04 Volition / 06 Relational Disposition where the characteristic was a human inner-act or state with God as context. **In r112 specifically, no group required a new dimension** — Dimension 11 proved sufficient for the structural cross-boundary cases. BUT the Spiritual/God-ward legacy label may indicate a different characteristic: the human's *orientation toward God* as a distinct dimension (not as "correspondence" but as directedness). 995-001 dianoia "love God with all your mind" is the clearest candidate — is this Dimension 11 (correspondence) or should there be a Dimension 12 "God-ward Orientation" (directedness without correspondence structure)? Open Session D question. Will be more significant for r183 where 581-006 lev "God-ward orientation" is UNCLASSIFIED precisely because the current vocabulary does not have this.
PATCH-TARGET: wa_session_research_flags insert

[SESSION-D] DIM-112-SD007
REGISTRY: 112 (mind)
SESSION-TARGET: D
DESCRIPTION: False-positive cross-registry roots — CC rootfamily extract pipeline observation. Three of five "cross-registry" roots in the rootfamily extract for C01 appear to be string-match false positives: AT (root_code None, linking personal pronouns and a mutterer term); YATSA (linking "offspring" and "come out" by shared consonantal skeleton); TAAM (linking "perceive" and "be double" as a homonym coincidence). These do not represent analytically meaningful cross-registry structural patterns. The CC rootfamily extract tool appears to be over-reporting; researcher may wish to refine the tool's matching logic to exclude coincidental cross-registry matches with None root_code or zero-semantic-overlap gloss pairs. Not a dimension finding but a data-pipeline observation.
PATCH-TARGET: wa_session_research_flags insert

---

## Phase C r112 — summary

**Groups assigned:** 73 of 73.
**Dimensions used:** 8 of 11 §7.7 dimensions (02, 03, 04, 05, 06, 08, 09, 11).
**Dimensions not used:** 01 Emotion — Positive, 07 Vitality/Existence, 10 Dependence/Creatureliness.
**Dominant_subject assigned:** 73 of 73 (HUMAN 58, NONE 10, GOD 5, OTHER_HUMAN 0, UNSEEN 0).
**Session B findings added:** 4 (DIM-112-004, -005, -006, -007).
**Session D pointers added:** 5 (DIM-112-SD003, -SD004, -SD005, -SD006, -SD007).
**Phase B correction encoded:** 1 (1010-001 nefros description revision per RD-PHASE-B-112-001).
**Researcher decision pending:** 1 (RD-PHASE-C-112-001 — Dimension 11 scope confirmation for 3 groups).

**Count discipline note:** Initial summary tables in this log contained two tally errors (03 Cognition 31 vs 29 actual; Dimension 11 10 vs 12 actual; HUMAN 59 vs 58 actual; 4331-001 duplicate DIMENSION lines; 2662-001 metaballō OTHER_HUMAN vs HUMAN inconsistency). All errors were surfaced by a per-entry regex re-count and corrected. Tables above reflect verified counts. Entry text for 4331-001 and 2662-001 was cleaned to remove the discrepancies. Discipline: the re-count per preamble failure mechanism 3 was essential here — the tally errors would have propagated into the patch operation list and the patch validation three-check (§8.6 step 4) if uncaught.

---

## [STAMP] Registry 112 (mind)

dim_review_status: Complete
dim_review_version: wa-dimensionreview-instruction-v3_3-20260418
PATCH-TARGET: word_registry.no = 112

Cluster-level stamp: NOT applied in this patch per §2.2 Registry Mode. The cluster stamp will be set when all C01 registries (including the four already Complete plus the two target registries) meet the full cluster criteria — this is a future consideration and is not this patch's responsibility.

---

## [SESSION-END] 20260420 | Phase: C | Registry: 112 (mind) | Last group completed: 999-002 (FRĒN family, final r112 group)

Next session begins: per-registry patch construction for r112 (immediately after this observations log is finalised per §8.6 step 1) → then Phase C r183.
Observations log version: wa-dim-c01-observations-v1_3-20260420.md

Notes on next steps:
- Per §8.6, patch construction reads from this observations log only — no re-derivation of analytical decisions
- Patch ID: PATCH-20260420-DIMREVIEW-C01-REG112-V1
- Patch content: 73 wa_dimension_index updates + 1 verse_context_group description correction (1010-001) + 1 wa_dimension_index description sync + 4 wa_session_b_findings inserts + 5 wa_session_research_flags inserts + 1 word_registry stamp update
- Patch validation: three-check per §8.6 step 4 (all group codes in extract; no missing groups; no duplicates)
- Cluster stamp NOT in this patch (Registry Mode)

---

*End of observations log v1_3 — Phase C r112 complete, ready for patch construction.*
