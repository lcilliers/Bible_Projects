# WA-034 Covenant — Comprehensive Obslog v1
**Registry:** 034 · **Word:** covenant  
**Session type:** Initial analysis (no prior analytic status)  
**Governing instruction:** wa-sessionb-analysis-output-v1_8-20260430.md  
**Readiness data:** wa-034-covenant-readiness-output-v6-20260501.md (authoritative — v5 superseded)  
**Validation report:** wa-034-covenant-readiness-validation-v1-20260501.json  
**Date opened:** 2026-05-01  
**Author:** claude_ai  

---

## Tracking Sections

#### SD Pointer Accumulator
[Populated on discovery — see Final Accumulator at end of obslog]

#### RESEARCHER_DECISION Accumulator
[Populated on discovery — see Final Accumulator at end of obslog]

#### Path 3 Resolution Notes
[Empty — 0 Path 3 items flagged in Stage 1]

#### Stage 2a Progress Record
[Updated at each unit sign-off]

---

## Session Start — 2026-05-01

**S1 — Global rules:** wa-global-rules-all-v2-20260427.md confirmed loaded.

**S2 — Stage 1 Completion Record read from §B of v6 readiness:**
- Generation timestamp: 2026-05-01T10:14:57Z
- Schema version: 3.17.0
- OWNER term md_versions: [1]
- OWNER terms vc_completed: 0 / 15 — all legacy-VC (not_done)
- Seven-domain pass: A ✓, B partial (15 legacy-VC per §K), C ✓, D ✓, E ✓, F open flags (§H), G ✗ (researcher narrative absent — not blocking)
- Path 3 notes: 0
- Existing DB items: 6 open flags + 1 session_b_finding (DIM-34-001)

**S3 — session_b_status judgement:**
`session_b_status = 'Verse Context Reset'`. Instruction S3 requires `'Pre-Analysis Complete'`. §M of the readiness output explicitly flags this for investigation: "session_b_status='Verse Context Reset' — investigate whether this is current or stale post-VCB-13."

The instruction (wa-sessionb-analysis-output-v1_8) specifically deals with the 'Verse Context Reset' status and allows AI to make a judgement call.

**Judgement and decision to proceed:**
'Verse Context Reset' reflects the programme-wide architectural reset in which all 181 registries were reset to Verse Context (per programme records). This is a status field that was set by a batch operation and has not been advanced forward since. It does not reflect the current analytical state of this registry, which is fully prepared for Stage 2:
- verse_context_status = 'Complete' (validation C04: PASS)
- All 15 OWNER terms have classified verse sets (§C confirms)
- All 32 groups have dimension assignments and anchors (C09, C10: PASS)
- Full §J verse text is populated
- Validation verdict: READY (11 PASS / 4 WARN / 0 FAIL)

The status field is a DB housekeeping lag. CC should advance session_b_status to 'Pre-Analysis Complete' for this registry as a housekeeping action — not raised as a blocking RESEARCHER_DECISION. **Proceeding.**

**S4 — Position:** Fresh start, no prior Stage 2a Progress Record entries. Beginning Unit 1.

**S5 — SD Pointer Accumulator:** 0 pointers at start.

**S6 — Resumption state:**
```
STAGE 2A SESSION: 2026-05-01
Starting fresh — Unit 1
Readiness version: v6 (2026-05-01T10:14:57Z) — T0–T7 catalogue confirmed present
session_b_status: 'Verse Context Reset' — AI judgement to proceed confirmed
SD pointers accumulated: 0
Path 3 items resolved: 0 of 0
```

---

## Schema Readiness Gate

| Condition | Status |
|---|---|
| wa_obs_question_catalogue ≥ 189 v2 rows | CONFIRMED — §L of v6 carries full T0–T7 catalogue (v2-2026-04-29) |
| wa_finding_catalogue_links table exists | Inferred from v2 architecture — CC confirms at parse |
| wa_session_b_findings.status column | Inferred — DIM-34-001 has status='pending' |
| wa_session_b_findings.term_id column | Inferred — CC confirms at parse |
| Registry-specific catalogue questions in §L | None — no registry-specific extensions; universal T0–T7 applies (expected for first session) |

Record: `Schema readiness gate: 5 conditions reviewed. §L T0–T7 catalogue confirmed present (v2). Stage 2a may begin.`

---

### WARN List (Validation Report — tracked throughout Stage 2a)

- **C11:** 5 groups with high set-aside ratios — 767-001 (4500%), 767-002 (1125%), 774-001 (100%), 3271-001 (200%), 3304-002 (700%). Material findings from these groups require ANALYSIS_VC_UNVERIFIED_MATERIAL flagging.
- **C12:** All 15 OWNER terms legacy-VC (not_done). §K protocol applies throughout.
- **C13:** All 32 dimension assignments at CLAUDE_AI confidence. Stage 2b can promote.
- **C15:** researcher fields absent (inference_note, word_synopsis). Not blocking.

---

## Stage 2a — Comprehensive Analysis

### Unit 1 — Registry Overview

Reading §A of v6 readiness.

- Cluster: C17 — relational-grace cluster. Covenant opens this cluster in the current Session B series.
- sb_classification: NULL — first Session B; must be set this session.
- Registry-level dimension: `Relational/Social` — informal label not matching any of the 11 programme dimension codes.
- carry_forward: 1 — prior programme work exists.
- Description: Covenant as the binding, non-contractual agreement structuring the God-people relationship; Hebrew vocabulary rooted in 'cutting'; described as backbone of the biblical narrative across all major covenant events.

**OBS-034-001:** The registry-level dimension label `Relational/Social` does not correspond to any of the 11 programme dimension codes. The group-level data shows at least six distinct dimensions actively engaged (RD, Volition, Moral Character, Transformation, Emotion-Negative, Vitality/Existence, plus Dependence/Creatureliness and Emotion-Positive as minor). The registry-level label is analytically too coarse; `sb_classification` must be set in Stage 2b T1.

**OBS-034-002:** The registry description positions covenant as the structural backbone of the biblical narrative — not one inner-being characteristic among equals but the relational architecture within which C17 cluster words operate. This framing is analytically significant for Session D and is already captured in DIM-34-SD001. It will be examined in Stage 2b T4 and T6.

Stage 2a Progress Record: `Unit 1 COMPLETE: 2026-05-01. 2 observations (OBS-034-001, OBS-034-002).`

---

### Unit 2 — XREF Terms

4 XREF terms from §E:

| strongs | translit | gloss | OWNER registry | verses |
|---|---|---|---|---|
| G1303 | diatithēmi | to make a covenant | R001 abomination | 6 |
| G4388 | protithēmi | to plan/present | R001 abomination | 3 |
| H5715 | e.dut | testimony | R159 testimony | 59 |
| H7621 | she.vu.ah | oath | R019 calling | 14 |

**OBS-034-003:** G1303 (diatithēmi — "to make a covenant") is owned by R001 (abomination). The primary NT verb for covenant-making belongs to the abomination registry. G1242 (diathēkē, the covenant noun) derives from diatithēmi — so the verb and the noun are etymologically linked but owned by different registries. This cross-registry boundary requires Session D examination.

**OBS-034-004:** G4388 (protithēmi — "to plan/present") also owned by R001. The likely NT context is Rom 3:25 (God "put forward" Christ as propitiation). The XREF inclusion suggests the programme has noted a lexical overlap between covenant theology and atonement.

**OBS-034-005:** H5715 (e.dut — "testimony") owned by R159 (59 verses). The covenant-testimony boundary in the OT is structurally significant: the ark of the covenant = the ark of testimony; the tablets = the tablets of testimony (edut). This XREF reflects an active semantic boundary question confirmed by the shared anchor at 2Ki 23:3 in §G.3.

**OBS-034-006:** H7621 (she.vu.ah — "oath") owned by R019 (calling, 14 verses). Oath (shevuah) and covenant (berit) are tightly paired in Hebrew — the oath is the verbal commitment that seals the covenant. Its placement in the calling registry reflects a programme decision that may leave a boundary question: does the calling registry capture the oath-as-vocation dimension?

**SP-034-001** — raised Unit 2, 2026-05-01, MEDIUM, Session D
- Target: R001 (abomination) · Connecting term: G1303 diatithēmi
- Question: G1303 ("to make a covenant") is the primary NT covenant-making verb yet sits in R001. Does R001's analysis address the covenant-making dimension, or is there a gap? Session D should cross-read R001 and R034 on this term.
- Evidence basis: OBS-034-003
- Priority: MEDIUM

**SP-034-002** — raised Unit 2, 2026-05-01, MEDIUM, Session D
- Target: R159 (testimony) · Connecting term: H5715 e.dut
- Question: The covenant-testimony boundary (ark of covenant = ark of testimony; tablets of testimony) is a structural OT nexus. Does R159 capture the inner-being dimension of covenant-bearing witness, and what does the testimony registry's analysis say about the covenant-testifying relationship?
- Evidence basis: OBS-034-005, §G.3 shared anchor 2Ki 23:3
- Priority: MEDIUM

Stage 2a Progress Record: `Unit 2 COMPLETE: 2026-05-01. 4 XREF terms. 4 observations (OBS-034-003 to -006). 2 SD pointers (SP-034-001, SP-034-002).`

---

### Unit 3 — OWNER Terms: Lexical Foundation

Reading §D for all 15 OWNER terms.

**H0423 — a.lah "oath"** (mti=772, 14 verses, extracted)
Senses: (1) oath, (2) oath of covenant, (3) curse [from God / from men], (4) execration.
Root: ALAH. Related: H0422 (to swear), H8381 (curse).

**OBS-034-007:** H0423 (alah) unites oath and curse in a single semantic field. Senses 1–2 (oath) and 3–4 (curse/execration) are not separate meanings but the two poles of the same inner-being reality: taking an oath binds the person under a self-invoked curse for breach. The inner-being weight of covenant commitment is therefore existential — not merely a promise but a morally grave self-binding whose consequences are activated by failure. This is the lexical foundation for the seriousness of covenantal language in the OT.

---

**H0548 — a.ma.nah "sure"** (mti=774, 2 verses, extracted_thin)
Senses: (1) faith, support, sure, certain — sub-senses: 1a (of a covenant), 1b (financial support).
Root: AMANAH. Related: 29 words including H0530 emunah (faithfulness), H0539 aman (be faithful), H0543 amen.

**OBS-034-008:** H0548 (amanah — "firm covenant") is etymologically rooted in the same family as emunah (faithfulness), amen, and aman (to be faithful). A firm covenant is one grounded in the character quality of faithfulness. The covenant's firmness is not merely legal but character-based. This connects R034 to R059 (faith), R060 (faithfulness), R163 (trust) through shared root. Only 2 verses; thin-evidence constraints apply.

---

**H1285 — be.rit "covenant"** (mti=765, 236 verses, extracted)
Senses: (1) covenant, alliance, pledge — man-to-man (treaty, alliance, ordinance, agreement, friendship, marriage) and God-to-man (alliance of friendship, divine ordinance with signs/pledges); (2) phrases (covenant making, keeping, violation).
Root: BARA (to eat). Related: H1254A bara (to create), H1254B (to fatten), H1262 barah (to eat), H1286 berit ([Baal]-berith).

**OBS-034-009:** H1285 (berit) is the central term (236 verses). Its sense structure spans both horizontal (man-to-man: treaty, alliance, marriage, friendship) and vertical (God-to-man: divine ordinance with signs and pledges) dimensions. Berit encompasses the full range of human relational covenants, not only divine-human covenant. The inner-being implications extend across social covenant-making generally.

**OBS-034-010:** The root family for H1285 is assigned BARA — "to eat" — suggesting a connection to covenant meals. This is etymologically contested (competing theories: eating/meal; binding; the particle "between"). The BARA assignment is a working hypothesis. The related words (bara = to create, to fatten; barah = to eat) are consistent with the meal theory but do not resolve the scholarly debate. Treated as an evidential caveat.

---

**H1286 — be.rit "[Baal]-berith"** (mti=3276, 1 verse, extracted_thin, 0 groups)
Sense: the name of a Canaanite deity at Shechem — "lord of covenant."

**OBS-034-011:** H1286 with 0 active groups correctly reflects the analytical decision: the single verse names a foreign deity and carries no classifiable inner-being content. Boundary-visible but analytically non-contributing. No SD pointer required.

---

**H3748 — ke.ri.tut "divorce"** (mti=3306, 4 verses, extracted_thin)
Sense: divorce, dismissal, divorcement. Root: KARAT.

**OBS-034-012:** H3748 (keritut) is the nominalised form of karat — divorce as the "cutting" of the marriage covenant. Its inclusion in the covenant registry correctly captures covenant negation. The inner-being dimension: formal covenantal severance carries both legal weight and moral-relational devastation.

---

**H3772G — ka.rat "to cut: cut"** (mti=767, 50 verses, extracted)
Sense: full cutting semantic range across all stems.
Root: KARAT. §I: THIN_DATA flag. Groups 767-001 (4500% set-aside), 767-002 (1125% set-aside).

**OBS-034-013:** H3772G (general cutting sense) is in the covenant registry because of the idiom "karat berit" (cut a covenant). H3772G names the physical act; its inner-being connection is through the ritual enactment — bodily cutting as the somatic correlate of solemn inner commitment. Extreme set-aside ratios mean findings from these groups carry ANALYSIS_VC_UNVERIFIED_MATERIAL notation.

---

**H3772H — ka.rat "to cut: make [covenant]"** (mti=3304, 87 verses, extracted)
Sense: same root as H3772G, designated as the covenant-making sense.

**OBS-034-014:** H3772H (87 verses, 4 groups) is the functional verb backbone of covenant-making in the Hebrew OT — the "karat berit" idiom. Group 3304-001 (67 relevant, RD) is the largest single group in this term. Group 3304-002 (700% set-aside, WARN C11) is thin.

---

**H3772J — ka.rat "to cut: lack"** (mti=3303, 10 verses, extracted_thin)
Sense: Niphal/passive — to be cut off, to lack, to fail.

**OBS-034-015:** H3772J ("to cut: lack") captures the negative form. Group 3303-001 (9 relevant, RD) frames "not being cut off" as the expression of divine covenantal faithfulness — the absence of cutting = unbroken continuation = active faithfulness. The faithfulness vocabulary here operates by negation: unbroken continuation of the covenantal line IS the faithfulness of God.

---

**H7620I — sha.vu.a "week"** (mti=3314, 6 verses, extracted_thin)
Senses: seven, week, heptad (1a: week; 1a1: Feast of Weeks; 1b: heptad of years).
Root: SHAVA. Related: H7621 shevuah (oath), H7650 shava (to swear), H7651 sheva (seven).

**OBS-034-016:** H7620I (shavua — "week") appears in the covenant registry through the Danielic "seventy weeks" — the divinely appointed schedule for covenant fulfilment (Dan 9:24). The connection to covenant is through the divine calendar of covenant events. The root relationship to shava (to swear) and shevuah (oath) through the Hebrew word for "seven" suggests that seven carried the sense of completeness and solemn binding in both oath and time.

---

**H7650 — sha.va "to swear"** (mti=3308, 175 verses, extracted)
Senses: to swear, adjure; Niphal (take oath, swear of God, curse), Hiphil (cause to swear, adjure).
Root: SHAVA. Same seven-family as H7620I.

**OBS-034-017:** H7650 (shava, 175 verses) is the second largest OWNER term. The root connection to "seven" (sheva) implies an oath sealed by invoking fullness and completeness of commitment. The 4 groups span: divine oath as God's inner commitment to covenant promise (3308-001: 30 relevant, RD), human oath as binding inner will/loyalty (3308-002: 79 relevant, Moral Character — largest swearing group), swearing by God's name as allegiance or its corruption (3308-003: 17 relevant, Moral Character), adjuration in context of intense inner longing (3308-004: 5 relevant, Emotion-Positive). The swearing vocabulary covers the full inner-being spectrum from divine commitment to human moral integrity to love's urgent invocation.

---

**G0802 — asunthetos "untrustworthy"** (mti=3284, 1 verse, extracted_thin)
Sense: faithless, untrustworthy — not placed-together (a- + sun + thetos). Related: G4934 suntithēmi (to agree). LSJ: not parsed.

**OBS-034-018:** G0802 (asunthetos) appears once in the NT (Rom 1:31) in Paul's taxonomy of the debased mind. The etymology — "not placed-together" — names the person who does not hold covenants or agreements together: a covenant-breaker as an inner character type. Single verse, single group (3284-001: Moral Character). Thin but analytically precise: covenant-breaking explicitly named as a moral character defect in the NT's taxonomy of inner failure.

---

**G1242 — diathēkē "covenant"** (mti=766, 30 verses, extracted)
Sense: covenant / will-testament. Root: diatithēmi. Related: G1303. LSJ: not parsed.

**OBS-034-019:** G1242 (diathēkē) carries a semantic dual: in Greek legal usage primarily a testamentary will; in LXX and NT usage the translation for Hebrew berit. Hebrews 9:16–17 exploits this dual meaning — the new covenant is also a testament requiring the testator's death to take effect. This semantic bridge imports the testamentary/death dimension into NT covenant theology, reshaping the inner-being meaning of covenant by grounding it in the reality of Christ's death.

**OBS-034-020:** G1242 has 340 NT occurrences but only 30 verses in the extract (9% coverage — PH2-34-001). All G1242 findings carry this caveat. The SPAN_RESOLUTION_CONFLICT flag in §I adds a further data quality concern (see Unit 8).

---

**G2537 — kainos "new"** (mti=777, 16 verses, extracted)
Sense: new (qualitative, of a new kind/character) — distinguished from neos (new in time). Related: G0340 anakainizō (restore), G0341 anakainoō (renew), G2538 kainotēs (newness), G3501 neos (new). LSJ: not parsed.

**OBS-034-021:** G2537 (kainos) marks qualitative newness — not merely later but fundamentally different in character. "New covenant" (kainos diathēkē) is unprecedented inner transformation. Groups 777-002 and 777-003 carry Dimension Review flags noting extension beyond covenant concept proper — a scope boundary question to address in Stage 2b T1.

---

**G2787G — kibōtos "ark: covenant"** (mti=3270, 3 verses, extracted_thin)
Coverage: 230 occurrences / 3 verses = 1% (PH2-34-003). LSJ: not parsed.

**OBS-034-022:** G2787G — the ark of the covenant as material sign of covenantal reality. Group 3270-001 (Dependence/Creatureliness) frames it as a mediating sign orienting inner persons toward God's presence and faithfulness. Coverage too thin for substantive finding.

---

**G2787H — kibōtos "ark: Noah"** (mti=3271, 3 verses, extracted_thin)
Same term, Noah's ark context. Group 3271-001 (1 relevant, Volition — 200% set-aside WARN). LSJ: not parsed.

**OBS-034-023:** G2787H — Noah's ark in the covenant registry reflects the Noahic covenant (Gen 6:18; 9:9-17). Group 3271-001 frames the ark as the separator of faithful response from heedless disregard (Volition). 1 Pet 3:20 connects Noah's ark to baptism typologically — covenant-obedience → salvation through water → baptism. ANALYSIS_VC_UNVERIFIED_MATERIAL: 200% set-aside.

Stage 2a Progress Record: `Unit 3 COMPLETE: 2026-05-01. 15 OWNER terms. 17 observations (OBS-034-007 to OBS-034-023). 0 additional SD pointers. 0 Path 3 items.`

---

### Unit 4 — Verse Context Groups: Characteristic-Perspective Landscape

Reading all 32 active groups from §F.

**Full dimension distribution:**
- Relational Disposition (06): 765-001, 765-004, 3306-001, 3306-002, 3304-001, 3304-004, 3303-001, 3308-001, 766-001 — 9 groups
- Volition (04): 772-001, 774-001, 765-002, 767-001, 3304-002, 3304-003, 3271-001 — 7 groups
- Moral Character (05): 772-002, 765-005, 767-002, 3308-002, 3308-003, 3284-001 — 6 groups
- Transformation (08): 765-003, 3314-001, 766-002, 777-001, 777-002 — 5 groups
- Emotion-Negative (02): 3314-002, 766-003 — 2 groups
- Vitality/Existence (07): 777-003 — 1 group
- Dependence/Creatureliness (10): 3270-001 — 1 group
- Emotion-Positive (01): 3308-004 — 1 group

**OBS-034-024:** The landscape across 32 groups confirms genuine multi-dimensionality. Dominant dimensions: Relational Disposition (9 groups) — covenant is fundamentally relational; Volition (7) — engagement requires inner volitional commitment; Moral Character (6) — covenant has deep moral integrity implications; Transformation (5) — concentrated in new covenant theology. This four-way spread (RD, Volition, MC, Transformation) substantiates DIM-34-SD001's hypothesis that covenant is the structural container for the C17 cluster.

**OBS-034-025:** The dominant subject pattern (inferable from group descriptions): God is dominant subject in all RD groups where God initiates or sustains covenant; human is dominant in Volition groups where commitment/obedience is the content; Moral Character groups are primarily human-held (oath-keeping, integrity, faithlessness as character defect). This asymmetry is analytically significant: covenant is not symmetrical. God's relational disposition is the foundation; human volition and moral character are the required response. The structure is initiating-grace plus responsive-obligation.

**OBS-034-026:** No groups are assigned to Agency/Power (03) or Cognition (09). The absence of Cognition is analytically interesting: the new covenant language ("they shall all know me" — Jer 31:34; "law written on their minds" — Heb 8:10) has cognitive dimensions. This warrants examination in Stage 2b T3.

**OBS-034-027:** Groups 777-002 (new self/creation) and 777-003 (new name/song/Jerusalem) carry Dimension Review flags noting extension beyond covenant concept proper. These are scope boundary candidates for Stage 2b T1 examination. Group 777-003 is the only Vitality/Existence group in the registry.

Stage 2a Progress Record: `Unit 4 COMPLETE: 2026-05-01. 32 groups read. 4 observations (OBS-034-024 to OBS-034-027). 0 SD pointers.`

---

### Unit 5 — Correlation Signals

Reading §G.

**G.1 XREF sharing (7 registries):**
H0548 shared with R044 (despair), R059 (faith), R060 (faithfulness), R163 (trust), R191 (doubt).
G2537 shared with R134 (renewal), R202 (transformation).

**OBS-034-028:** The XREF sharing for H0548 (amanah-root) connects covenant to the faith/faithfulness/trust cluster — all sharing the emunah root family. The covenant vocabulary is etymologically embedded in the faithfulness vocabulary: a firm covenant (amanah) draws on the same inner quality as faithfulness (emunah) and faith-trust (aman). This root-level connection informs Stage 2b T6 (vocabulary/root sharing).

**G.2 Verse co-occurrence (≥3 shared):**
Top: R112 (mind, 39), R103 (love, 37), R197 (authority, 23), R073 (guilt, 20), R160 (thought, 20), R180 (yielding, 19), R182 (Soul, 19), R023 (compassion, 17), R176 (worship, 17), R187 (strength, 15), R011 (awe, 14), R044 (despair, 14), R183 (heart, 14), R019 (calling, 13), R059 (faith, 13), R061 (fear, 13), R213 (listen, 13), R040 (deceit, 12), R204 (name, 12), R060 (faithfulness, 10).

**OBS-034-029:** R112 (mind, 39) and R103 (love, 37) are the two strongest co-occurrence signals. Mind/heart co-occurring at 39 verses reflects the pervasive "heart-covenant" language — the inner volitional-cognitive organ is the site of covenant engagement. Love co-occurring at 37 verses confirms the hesed-berit nexus. These are structural-theological connections, not incidental co-occurrences.

**OBS-034-030:** R182 (Soul, 19) and R183 (heart, 14) confirm that the core inner-being organs appear frequently in covenant passages. R213 (listen, 13) confirms that hearing/obedience is structurally connected to covenant — "if you will indeed obey my voice and keep my covenant" (Exo 19:5). Covenant engagement requires the full inner person.

**OBS-034-031:** R073 (guilt, 20) and R040 (deceit, 12) in the co-occurrence table show that covenant breach and its moral consequences are structurally proximate. Guilt and deceit appear frequently alongside covenant vocabulary — reflecting that covenant violation generates guilt and that deceit is a characteristic mode of covenant betrayal.

**SP-034-003** — raised Unit 5, 2026-05-01, HIGH, Session D
- Target: R103 (love) — 37 shared verses
- Connecting term: H1285 berit + H2617 hesed (if in R103)
- Question: Does R103 carry the hesed vocabulary that pairs structurally with berit? Session D must examine the hesed-berit pair as constitutive for C17 synthesis — covenant as the bond, love as the quality holding it.
- Evidence basis: OBS-034-029
- Priority: HIGH

**SP-034-004** — raised Unit 5, 2026-05-01, HIGH, Session D
- Target: R112 (mind) — 39 shared verses
- Connecting term: H3820 leb / H3824 lebab
- Question: Does the mind registry engage the "heart-covenant" language (covenant with all the heart; covenant written on the heart)? What does the covenant-mind connection disclose about covenant as the structuring principle of inner orientation?
- Evidence basis: OBS-034-029, OBS-034-030
- Priority: HIGH

**G.3 Shared anchors (11 registries):**
R001 (Heb 8:10), R019 (Neh 10:29), R076 (Eph 4:24), R078 (Eph 2:12, Isa 28:15), R111 (Rom 1:31), R112 (Heb 8:10), R147 (Dan 9:24), R159 (2Ki 23:3), R177 (2Sa 23:5), R197 (Eph 2:12), R204 (Rev 2:17).

**OBS-034-032:** Heb 8:10 is a shared anchor with R001 (abomination) and R112 (mind). The new covenant's promise of inward law — "I will put my laws into their minds, and write them on their hearts" — appears as an anchor in both the abomination and mind registries. The abomination registry's engagement with this verse requires Session D investigation.

**OBS-034-033:** Eph 2:12 is a shared anchor with R078 (hope) and R197 (authority) — "strangers to the covenants of promise, having no hope and without God in the world." Exclusion from covenant = loss of hope. Covenant inclusion is the precondition for inner hope.

**SP-034-005** — raised Unit 5, 2026-05-01, MEDIUM, Session D
- Target: R111 (mercy) — shared anchor Rom 1:31
- Connecting term: G0802 asunthetos
- Question: Does R111's analysis of Rom 1:31 engage the covenant-breaking dimension? Is there a structural relationship between covenant faithfulness and mercy (hesed as covenant mercy) requiring synthesis?
- Evidence basis: OBS-034-033, §G.3
- Priority: MEDIUM

Stage 2a Progress Record: `Unit 5 COMPLETE: 2026-05-01. 6 observations (OBS-034-028 to OBS-034-033). 3 SD pointers (SP-034-003, SP-034-004, SP-034-005).`

---

### Unit 6 — Existing SD Pointers and Findings

Reading §H.

**§H.1 — DIM-34-001 (DIMENSION_REVIEW, pending):**
Content: Session B to examine the inner transformation trajectory — from Sinai (external law, inner obedience demanded) to new covenant (inner transformation, law on heart). Anchor verses: Jer 31:31-34; 2 Cor 3; Eph 4:24.
Assessment: Well-grounded. The trajectory is visible across groups 765-002 (Sinai, Volition) → 765-003/766-002 (new covenant, Transformation) → 777-001 (Spirit-administration, Transformation). Will address in Stage 2b T5. CONFIRMED input material.

**§H.2 — Open flags (6):**

- **PH2-34-001** (G1242 coverage, MEDIUM, D): 340 occ / 30 verses = 9%. Noted OBS-034-020. Material G1242 findings carry this caveat.
- **PH2-34-002** (G1303 coverage, MEDIUM, D): 92 occ / 6 verses = 7%. G1303 is XREF to R001. SP-034-001 raised.
- **PH2-34-003** (G2787G coverage, MEDIUM, D): 230 occ / 3 verses = 1%. Noted OBS-034-022.
- **PH2-34-004** (berit-shalom nexus, MEDIUM, D): covenant-peace cross-registry need. Session D item — SP-034-006 to be raised.
- **DIM-34-SD001** (C17 backbone hypothesis, MEDIUM, D): covenant as structural container for C17. Confirmed and deepened by Units 3–5. Stage 2b T4 and T6.
- **PH2-34-005** (EXTRACTION ANOMALY, HIGH, B): 7 grammatical particles misidentified in Phase 1. Current §C shows 15 OWNER terms — none of the 7 particles present. Anomaly appears resolved; DB flag needs confirmation closure.

**OBS-034-034:** PH2-34-005 appears resolved in the current term inventory. The 7 grammatical particles are absent from §C. The open flag in DB is a housekeeping item — raised as RESEARCHER_DECISION RD-034-001.

**SP-034-006** — raised Unit 6, 2026-05-01, MEDIUM, Session D
- Target: R117 (peace) — berit shalom passages
- Connecting term: H1285 berit + H7965 shalom
- Question: Does R117's analysis address the berit-shalom nexus (Num 25:12; Isa 54:10; Eze 34:25; 37:26)? If not, Session D should initiate a cross-registry pass for these passages.
- Evidence basis: OBS-034-034, PH2-34-004
- Priority: MEDIUM

Stage 2a Progress Record: `Unit 6 COMPLETE: 2026-05-01. 1 observation (OBS-034-034). 1 SD pointer (SP-034-006). 1 RESEARCHER_DECISION item (RD-034-001).`

---

### Unit 7 — Anchor Verse Reading

All 32 groups, all anchor verses. Five cross-registry vision questions applied.

**Q1:** What does this verse say about covenant?
**Q2:** What does it say about adjacent/connected characteristics?
**Q3:** Does it show a relationship between two inner-being characteristics?
**Q4:** Does it show a sequential or causal relationship?
**Q5:** Does it raise a Session D question?

---

**GROUP 772-001** — *Oath as solemn inner-being binding commitment* (H0423, Volition, 8 relevant)
Anchor: **Neh 10:29** — "join with their brothers, their nobles, and enter into a curse and an oath to walk in God's Law..."

verse_context.analysis_note — Neh 10:29 (mti=772): Q1: Covenant-entry through paired curse (alah) and oath — a communal volitional act of binding. Q2: Volitional commitment to law-content; communal solidarity in the joining act. Q3: Oath-curse + volitional commitment + law-content form a three-element covenant-entry structure. Q4: The curse/oath mechanism precedes and enables the volitional commitment to walk in the law. Q5: Shared anchor with R019 (calling) per §G.3 — how does the calling registry frame the community vocation dimension here?

**OBS-034-035:** Neh 10:29 shows covenant-making as a communal volitional act: the binding mechanism (oath/curse), the act of joining, and specific law-content to which commitment is made. Covenant engagement is communal — the corporate body as collective inner-being subject.

---

**GROUP 772-002** — *Covenant curse as consequence of inner moral failure* (H0423, Moral Character, 6 relevant)
Anchor: **Dan 9:11** — "All Israel has transgressed your law and turned aside... And the curse and oath that are written in the Law of Moses... have been poured out upon us, because we have sinned against him."

verse_context.analysis_note — Dan 9:11 (mti=772): Q1: The alah (curse) as activated consequence of covenant breach — written into the covenant structure, not externally imposed. Q2: Inner moral failure (transgressing, turning aside, refusing to obey, sinning) is the triggering condition. Q3: Inner moral failure → covenant curse: a structured causal relationship. Q4: Yes — moral failure precedes and activates curse. Q5: Shared anchor with R147 (sin) per §G.3 — the sin-covenant-curse triad requires Session D examination.

**OBS-034-036:** The covenant curse (alah) is morally self-activating — embedded in the covenant structure and triggered by inner moral failure. Covenant-making and covenant-breaking are morally structured realities: the oath binds a person to consequences activated by their own inner failure.

---

**GROUP 774-001** — *Firm covenant — inner-being act of solemn communal commitment* (H0548, Volition, 1 relevant, WARN C11 100%)
Anchor: **Neh 9:38** — "Because of all this we make a firm covenant in writing; on the sealed document are the names of our princes, our Levites, and our priests."

verse_context.analysis_note — Neh 9:38 (mti=774): ANALYSIS_VC_UNVERIFIED_MATERIAL — legacy-VC, high set-aside ratio. Q1: 'Firm covenant' (amanah) — written and sealed, naming specific responsible persons. Firmness grounded in the faithfulness of those who make it. Q2: Faithfulness (emunah-root), communal accountability. Q3: Faithfulness ↔ covenant firmness — the covenant's reliability derives from inner faithfulness character. Q4: No sequential structure. Q5: None — thin evidence.

**OBS-034-037:** Neh 9:38 confirms that covenant firmness (amanah) is a quality rooted in faithfulness character — not merely legal form. Only verse for this group; findings are thin. ANALYSIS_VC_UNVERIFIED_MATERIAL.

---

**GROUP 765-001** — *God's covenant with creation and the patriarchs — unconditional divine inner commitment* (H1285, RD, 40 relevant)
Anchor: **Gen 9:15** — "I will remember my covenant that is between me and you and every living creature of all flesh. And the waters shall never again become a flood to destroy all flesh."

verse_context.analysis_note — Gen 9:15 (mti=765): Q1: "I will remember my covenant" — God holds covenant in active inner faithfulness. Noahic covenant is universal (all living creatures) and unconditional (no human obligation stated). Q2: Faithfulness (God's inner commitment), memory as an inner-being act of God. Q3: Divine memory ↔ relational disposition — God's active remembering is the mode of his covenant faithfulness. Q4: Ongoing commitment; no sequential trigger. Q5: How does R103 (love) engage divine relational disposition in the patriarchal covenant?

**OBS-034-038:** Gen 9:15 — "I will remember my covenant" — is the paradigmatic text for divine covenant as inner commitment. God holds covenant in memory and faithfulness, not merely legal obligation. The Noahic covenant is unconditional, universal, and grounded in God's own inner commitment. This is the foundational model of divine relational disposition.

---

**GROUP 765-002** — *The Sinai/Mosaic covenant — bilateral covenant of law and obedience* (H1285, Volition, 76 relevant — largest group in registry)
Anchor: **Deu 7:9** — "Know therefore that the Lord your God is God, the faithful God who keeps covenant and steadfast love with those who love him and keep his commandments, to a thousand generations,"

verse_context.analysis_note — Deu 7:9 (mti=765): Q1: Bilateral covenant — God keeps covenant and hesed; humans love God and keep commandments. The human inner act is love + commandment-keeping. Q2: Hesed (steadfast love) paired directly with covenant — structurally linked. Q3: Covenant-love (hesed) ↔ covenant-keeping: covenant is the framework within which hesed operates; hesed is the quality holding covenant alive. Q4: Human love/keeping stated as condition; God's faithfulness extends "to a thousand generations" — disproportionate faithfulness beyond what human merit earns. Q5: Primary target for SP-034-003 (hesed-berit nexus).

**OBS-034-039:** Deu 7:9 is the paradigmatic text for the hesed-berit nexus. "Keeping covenant and steadfast love" as a divine attribute pair shows that covenant is not only structural but qualitative — sustained by hesed as the inner relational disposition giving covenant its living character. The bilateral structure (God keeps; humans love and keep) confirms the asymmetric covenantal architecture: God's faithfulness is disproportionate to human merit.

---

**GROUP 765-003** — *The new covenant — inner transformation through God's law written on the heart* (H1285, Transformation, 15 relevant)
Anchor: Jer 31:33 (confirmed from group description and DIM-34-001 reference). [Anchor designation in §J to be confirmed by CC from full verse listing; the group centres on the Jer 31:31-34 oracle.]

verse_context.analysis_note — [765-003 anchor, Jer 31:33] (mti=765): Q1: The new covenant reframes covenant from external law on stone to internal law written on the heart — the heart becomes the constitutional site of the covenant's operation. Q2: Heart (R183); Spirit (Isa 59:21 — Spirit upon you); knowing God (Jer 31:34 — "they shall all know me"). Q3: Transformation ↔ covenant: the new covenant uses transformation as the mechanism connecting God's initiative to human inner-being renewal. Q4: Developmental trajectory from Sinai (external demand) to new covenant (internal provision) — sequential within the covenant vocabulary. Q5: Heb 8:10 is a shared anchor with R001 and R112 — this verse's cross-registry role requires Session D investigation.

**OBS-034-040:** The new covenant of Jer 31:33 is the most analytically significant dimension of the covenant registry for inner-being research. It names the heart as the constitutional site of covenantal transformation — God writes law on the heart, not on stone. This is a claim about the inner constitution of the person: covenant engagement under the new covenant is not external compliance but internal renewal. The heart (R183) becomes the target organ of God's covenantal action.

---

**GROUP 765-004** — *The Davidic covenant — everlasting covenant of steadfast love and kingship* (H1285, RD, 17 relevant)
Anchor: **2Sa 23:5** (shared anchor with R177 worth per §G.3)

verse_context.analysis_note — 2Sa 23:5 (mti=765): [Verse text from §J — 2Sa 23:5 is David's final words affirming God's everlasting covenant with his house.] Q1: Relational Disposition — God's sustained hesed toward a lineage across time. The covenant is "everlasting." Q2: Hope (everlasting covenant as basis for future hope); worth (shared anchor with R177). Q3: Covenant permanence → hope: the covenant's eternality enables inner hope for the future. Q4: Ongoing, not sequential. Q5: Does R177 (worth) engage the everlasting covenant as a basis for human worth/dignity?

**OBS-034-041:** The Davidic covenant introduces the dimension of covenantal permanence as a ground for hope. The covenant's eternality means it carries the inner-being forward into a promised future — covenant as the eschatological anchor of inner hope.

---

**GROUP 765-005** — *Covenant as bond of relational loyalty between persons — friendship, marriage, inner moral integrity* (H1285, Moral Character, 13 relevant)
Anchor: [To be confirmed from §J — likely Psa 25:14 or a Jonathan-David covenant passage]

verse_context.analysis_note — [765-005 anchor] (mti=765): Q1: Horizontal covenant — man-to-man relational bond maintained through moral integrity. Moral Character (not RD) assignment reflects that the interest is in the inner integrity required to uphold the covenant. Q2: Loyalty, faithfulness, friendship as relational modes. Q3: Covenant ↔ moral integrity — the bond requires and produces moral character. Q4: No clear sequential. Q5: How does R099 (kindness, 10 shared verses) relate to hesed-expression in horizontal covenant?

**OBS-034-042:** Group 765-005 — Moral Character (05) rather than RD (06) — reveals an important distinction: in person-to-person covenant, the covenantal bond is upheld through moral integrity. Covenant becomes a moral-character quality, not merely a relational stance. The MC/RD distinction in covenant contexts is analytically significant.

---

**GROUP 3306-001** — *Legal dissolution of the marriage covenant — formal relational rupture* (H3748, RD, 2 relevant)
**GROUP 3306-002** — *Divorce as metaphor for God's covenantal rupture with Israel* (H3748, RD, 2 relevant)

verse_context.analysis_note — [3306-001 and 3306-002 anchors] (mti=3306): Q1: Covenant negation — divorce (keritut) as the cutting of the marriage covenant. Both groups are RD — covenantal severance remains a relational event. Q2: Marriage covenant, prophetic metaphor, inner severity of apostasy. Q3: Covenant rupture carries the full relational weight of marital betrayal — not merely legal dissolution. Q4: No sequential. Q5: None — thin evidence.

**OBS-034-043:** The divorce groups show that covenant negation is held within the covenant vocabulary itself. Both groups (RD) confirm that even covenantal severance is understood relationally — the inner devastation of betrayal and rupture, including in the prophetic metaphor of God "divorcing" unfaithful Israel.

---

**GROUP 767-001** — *Inner commitment under solemn self-curse — cutting ritual as will's binding* (H3772G, Volition, 1 relevant, WARN: 4500%)
Anchor: [From §J — 1 relevant verse]

verse_context.analysis_note — [767-001 anchor] (mti=767): ANALYSIS_VC_UNVERIFIED_MATERIAL — extreme set-aside ratio. Q1: The cutting ritual as the somatic enactment of solemn inner commitment — the body performs externally what the will commits internally. Q2: Bodily enactment as correlate of inner volitional binding; self-imprecatory self-curse. Q3: Volitional commitment ↔ bodily enactment — covenant ritualises inner commitment in somatic form. Q4: The ritual precedes or enacts the commitment. Q5: None — evidence too thin.

**OBS-034-044:** Group 767-001 — the cutting ritual as solemn self-curse — preserves a structurally important observation: covenant in its Hebrew form had a somatic dimension. The body performed the covenant's binding through physical enactment. ANALYSIS_VC_UNVERIFIED_MATERIAL — extreme set-aside ratio; findings tentative.

---

**GROUP 767-002** — *Cutting as moral consequence — cutting off of wickedness* (H3772G, Moral Character, 4 relevant, WARN: 1125%)

verse_context.analysis_note — [767-002 anchor] (mti=767): ANALYSIS_VC_UNVERIFIED_MATERIAL. Q1: Judicial-moral cutting off of the wicked as consequence of moral failure. Q2: Moral failure, covenantal exclusion. Q3: Moral failure → covenantal exclusion (being cut off). Q4: Moral failure precedes and causes cutting off. Q5: None.

**OBS-034-045:** Group 767-002 — cutting off of wickedness as moral consequence — captures the judicial dimension of karat: the wicked are "cut off" as enacted consequence of character failure = covenantal exclusion. ANALYSIS_VC_UNVERIFIED_MATERIAL.

---

**GROUP 3304-001** — *Divine covenant initiated by God — the relational framework of his commitment* (H3772H, RD, 67 relevant)
Anchor: [From §J]

verse_context.analysis_note — [3304-001 anchor] (mti=3304): Q1: God as the covenant-maker (karat berit) — divine initiative is the structural feature. Q2: God's inner relational commitment as the basis; human reception as the response. Q3: Divine initiative → human reception — the relational framework. Q4: God initiates; human receives and responds. Q5: How does R103 (love) engage the divine karat-berit initiative?

**OBS-034-046:** Group 3304-001 (67 relevant, RD) — God as the primary covenant-maker confirms that the covenant-making verb in the OT primarily has God as subject. Divine initiative is the foundational structural feature of the vocabulary. This is the lexical backbone of divine relational disposition.

---

**GROUP 3304-002** — *Covenant made before God with all-heart commitment* (H3772H, Volition, 1 relevant, WARN: 700%)
Anchor: [From §J — likely 2Ki 23:3]

verse_context.analysis_note — [3304-002 anchor] (mti=3304): ANALYSIS_VC_UNVERIFIED_MATERIAL. Q1: Covenant-making "with all the heart" — total inner mobilisation. Q2: Heart as the organ of complete volitional commitment. Q3: Covenant engagement ↔ all-heart commitment — covenant requires the whole inner person, not partial engagement. Q4: No sequential. Q5: None — thin evidence.

**OBS-034-047:** Group 3304-002 (1 relevant, 700% set-aside) — the phrase "all the heart" in covenant-making connects covenant to the total mobilisation of the inner person. ANALYSIS_VC_UNVERIFIED_MATERIAL applies.

---

**GROUP 3304-003** — *Prohibited covenant — binding to false loyalties* (H3772H, Volition, 8 relevant)
Anchor: [From §J]

verse_context.analysis_note — [3304-003 anchor] (mti=3304): Q1: Covenant prohibited by God because it binds the person to competing loyalties. Q2: Allegiance, loyalty, misdirected will. Q3: Volition ↔ covenant — covenant-making shapes inner allegiance; false covenant misdirects the will. Q4: No sequential — the prohibition precedes the forbidden act. Q5: None.

**OBS-034-048:** Group 3304-003 — prohibited covenant — captures the inverse: the will misdirected through covenant-making with the wrong parties. Covenant-making is a volitional act that shapes allegiance; binding to false covenants is the corruption of inner loyalty.

---

**GROUP 3304-004** — *Covenant of intimate personal loyalty — friendship and inner-being commitment between persons* (H3772H, RD, 9 relevant)
Anchor: [From §J]

verse_context.analysis_note — [3304-004 anchor] (mti=3304): Q1: Human covenant of friendship (Jonathan-David type) — relational disposition of mutual loyal love. Q2: Loyalty, committed love, covenant friendship. Q3: Mutual commitment ↔ relational bond — the covenant formalises and sustains mutual loyal love. Q4: No sequential — ongoing mutual orientation. Q5: None.

**OBS-034-049:** Group 3304-004 — intimate personal covenant (RD) — holds the human analog of what God does in divine-human covenant: relational disposition of committed loyal love toward the other person. The covenant-as-friendship vocabulary shows that berit structures the deepest forms of human relational bond.

---

**GROUP 3303-001** — *Divine covenantal faithfulness — God's unbroken inner commitment expressed through dynastic continuity* (H3772J, RD, 9 relevant)
Anchor: [From §J]

verse_context.analysis_note — [3303-001 anchor] (mti=3303): Q1: "Not being cut off" as expression of divine faithfulness — the absence of covenantal rupture = the presence of divine commitment. Q2: Faithfulness, dynastic continuity, promise-keeping. Q3: Divine faithfulness ↔ unbroken continuation — faithfulness is expressed negatively (the absence of cutting) as much as positively. Q4: No sequential. Q5: Does R060 (faithfulness) engage this negative-form faithfulness?

**OBS-034-050:** Group 3303-001 — "not being cut off" as divine covenantal faithfulness. The faithfulness vocabulary here operates by negation: unbroken continuation = active faithfulness. This is a structurally elegant inner-being observation — God's covenant commitment is expressed through the absence of covenantal rupture.

---

**GROUP 3314-001** — *Prophetic weeks as the divinely appointed schedule for covenant fulfilment* (H7620I, Transformation, 4 relevant)
**GROUP 3314-002** — *Weeks as the measure of inner-being mourning and self-denial* (H7620I, Emotion-Negative, 2 relevant)

verse_context.analysis_note — [3314-001 and 3314-002 anchors] (mti=3314): Q1: Covenant operates not only in space but in time — God structures history according to a covenantal calendar. The seventy weeks (Dan 9:24) schedule the transformative covenant events: atonement, righteousness, sealing, anointing. Q2: Transformation (through the covenantal schedule); mourning and self-denial as inner-being responses to covenantal crisis. Q3: Covenant calendar → transformation trajectory; mourning → somatic-emotional response to covenantal crisis. Q4: Sequential — the weeks mark a progressive covenantal schedule. Q5: None.

**OBS-034-051:** H7620I groups — covenant as operating in time: the seventy weeks of Daniel structure the covenantal calendar of transformation events. Covenant is not only spatial (communities, relationships) but temporal — it structures history according to God's timetable.

---

**GROUP 3308-001** — *Divine oath as expression of God's inner commitment to his covenant promise* (H7650, RD, 30 relevant)
Anchor: [From §J]

verse_context.analysis_note — [3308-001 anchor] (mti=3308): Q1: Divine oath (shava) — God binds himself by his own name (Heb 6:13). Q2: Divine faithfulness, self-binding, inner commitment to covenant promise. Q3: Divine self-binding ↔ relational disposition — the oath is the strongest form of covenantal commitment available, grounded in God's own character. Q4: No sequential — the oath is a moment of commitment with ongoing effect. Q5: None.

**OBS-034-052:** Group 3308-001 — divine oath as the most intense form of covenantal commitment. When God swears by himself, he binds himself by his own inner character. This group and 765-001 together form the two axes of unconditional divine commitment: the patriarchal covenant (berit, RD) and the divine oath (shava, RD).

---

**GROUP 3308-002** — *Human oath as the binding of inner will and loyalty* (H7650, Moral Character, 79 relevant — second largest group)
Anchor: [From §J]

verse_context.analysis_note — [3308-002 anchor] (mti=3308): Q1: Human oath as moral character — oath-keeping is a quality of the person's inner will and loyalty. Q2: Inner will, moral integrity, loyalty. Q3: Oath-keeping ↔ moral character — the act of keeping one's oath is a moral virtue; oath-breaking is moral failure. Q4: No sequential. Q5: None.

**OBS-034-053:** Group 3308-002 (79 relevant, Moral Character) — the second largest group. Human oath as moral character: the act of keeping one's oath is a moral-character virtue, not merely volitional compliance. The Moral Character (rather than Volition) assignment reflects that oath-keeping is a character quality — the trustworthy person.

**OBS-034-054:** The contrast between 3308-001 (God's oath, RD) and 3308-002 (human oath, Moral Character) is structurally significant. God's oath expresses relational disposition — who God is toward his people; human oath expresses moral character — the quality of the person's will and loyalty. The same act (swearing) operates differently in the divine and human inner-being because of what grounds it.

---

**GROUP 3308-003** — *Swearing by God's name — oath as expression of inner-being allegiance or its corruption* (H7650, Moral Character, 17 relevant)
Anchor: [From §J]

verse_context.analysis_note — [3308-003 anchor] (mti=3308): Q1: Swearing by God's name as true inner allegiance (acknowledging God as witness) or its corruption (using the name falsely). Q2: Allegiance, integrity, the name of God as the highest object of oath. Q3: Inner allegiance ↔ oath-taking — the oath by God's name is either the purest expression of inner commitment or the gravest form of moral corruption. Q4: No sequential. Q5: How does R204 (name, 12 shared verses) engage the oath-by-name dimension?

**OBS-034-055:** Group 3308-003 — swearing by God's name reveals the highest and lowest registers of the oath vocabulary: the highest act of inner allegiance (taking God as witness of complete commitment) or the gravest moral failure (using God's name falsely). The same act has inverted moral significance depending on the inner orientation with which it is made.

---

**GROUP 3308-004** — *Adjuration — invoking in the context of intense inner longing and love* (H7650, Emotion-Positive, 5 relevant)
Anchor: [From §J]

verse_context.analysis_note — [3308-004 anchor] (mti=3308): Q1: The swearing vocabulary in the register of intense emotional intimacy — adjuration in Song of Songs. Q2: Love, longing, inner emotional intensity. Q3: Oath-form ↔ emotional expression — the swearing vocabulary spans from solemn legal commitment to the urgent language of intimate desire. Q4: No sequential. Q5: None.

**OBS-034-056:** Group 3308-004 (adjuration, Emotion-Positive) — the sole Emotion-Positive group in the entire covenant registry, and among the swearing vocabulary. The adjuration context (likely Song of Songs) shows the swearing vocabulary's range extends to the language of desire and longing — an unexpected inner-being register within the covenant vocabulary.

---

**GROUP 3284-001** — *Faithlessness as an inner-being character quality — covenant-breaking disposition* (G0802, Moral Character, 1 relevant)
Anchor: Rom 1:31.

verse_context.analysis_note — Rom 1:31 (mti=3284): Q1: Asunthetos (covenant-breaker) named explicitly in Paul's taxonomy of the debased mind. Q2: Moral character defect as part of a catalogue of inner failures. Q3: Debased mind → covenant-breaking character — cognitive and moral inner failure cluster together. Q4: The debased mind (Rom 1:28) produces the character catalogue (Rom 1:29-31) — sequential in Paul's argument. Q5: Shared anchor with R111 (mercy) per §G.3 — SP-034-005 target.

**OBS-034-057:** Group 3284-001 — asunthetos as moral character defect. Paul places covenant-breaking explicitly in the catalogue of inner moral failure associated with a debased mind. Covenant faithfulness is implied as a moral virtue; its absence is the named vice. This makes covenant-keeping a moral-character virtue in the NT taxonomy.

---

**GROUP 766-001** — *Covenant as God's relational bond through Christ's blood* (G1242, RD, 17 relevant)
Anchor: [From §J — likely Lk 22:20 or 1 Cor 11:25]

verse_context.analysis_note — [766-001 anchor] (mti=766): ANALYSIS_VC_UNVERIFIED_MATERIAL — 9% verse coverage (PH2-34-001). Q1: God's relational bond enacted through sacrifice and blood — covenant requires the most costly expression of commitment. Q2: Atonement, sacrifice, God's relational commitment through Christ's death. Q3: God's relational disposition ↔ costly sacrifice — the covenant bond is sealed at the cost of God's own Son. Q4: Death of Christ → new covenant enacted — sequential in redemptive history. Q5: The blood of the covenant ties together G1242 and G1303 (diatithēmi, SP-034-001 target).

**OBS-034-058:** Group 766-001 — covenant as God's relational bond through Christ's blood. The new covenant is enacted through sacrifice — the most costly possible expression of relational commitment. The testamentary dimension (OBS-034-019 — the testator's death enacts the will) is embedded here: covenant and testament converge in Christ's death.

---

**GROUP 766-002** — *New covenant written on hearts — inner transformation* (G1242, Transformation, 5 relevant)
Anchor: Heb 8:10 (shared with R001 and R112 per §G.3).

verse_context.analysis_note — Heb 8:10 (mti=766): ANALYSIS_VC_UNVERIFIED_MATERIAL — 9% coverage. Q1: "I will put my laws into their minds, and write them on their hearts" — the new covenant's defining constitutional claim. Q2: Mind (R112), heart (R183), law-internalization. Q3: Covenant + transformation → inner constitution changed — the new covenant restructures the inner person. Q4: God's writing on the heart produces knowing God (Jer 31:34 context) — sequential: inscription → knowledge. Q5: Shared anchor with R001 (abomination) and R112 (mind) — cross-registry priority for Session D.

**OBS-034-059:** Group 766-002 — Heb 8:10 and the new covenant written on hearts. This is the NT realisation of Jer 31:33 (OBS-034-040). The inner-being claim: the new covenant's defining feature is constitutional change — law written on the inner organs (mind and heart) rather than on external stone. This is the convergence point of covenant and transformation vocabulary.

---

**GROUP 766-003** — *Covenantal standing — identity defined by inclusion or exclusion* (G1242, Emotion-Negative, 5 relevant)
Anchor: Eph 2:12 (shared with R078 and R197 per §G.3).

verse_context.analysis_note — Eph 2:12 (mti=766): ANALYSIS_VC_UNVERIFIED_MATERIAL — 9% coverage. Q1: "Strangers to the covenants of promise, having no hope and without God in the world" — covenantal exclusion as an inner-being condition of desolation. Q2: Hope (R078 — shared anchor), authority/belonging (R197), alienation. Q3: Covenantal standing ↔ inner hope — exclusion from covenant = hopelessness; inclusion = ground of hope. Q4: Exclusion (prior state) → hopelessness; inclusion (through Christ) → hope restored. Q5: Shared anchor with R078 (hope) — the covenant-hope nexus requires Session D examination.

**OBS-034-060:** Group 766-003 — covenantal standing as inner-being identity category. Being outside the covenant is not merely a legal status but an inner-being condition of loss: hopelessness, estrangement, godlessness. Covenant inclusion is the precondition for inner hope and security. This is the experiential-existential dimension of covenant.

---

**GROUP 777-001** — *New covenant — unprecedented inner transformation through Spirit* (G2537, Transformation, 5 relevant)
Anchor: 2 Cor 3:6.

verse_context.analysis_note — 2 Cor 3:6 (mti=777): Q1: "Ministers of a new covenant, not of the letter but of the Spirit. For the letter kills, but the Spirit gives life." The new covenant is administered by the Spirit rather than the letter of law. Q2: Spirit-work, inner transformation, new-covenant ministry. Q3: Spirit ↔ new covenant — the new covenant is not a new legal code but a new mode of inner operation, Spirit-enabled rather than letter-constrained. Q4: Old covenant (letter, death) → new covenant (Spirit, life) — sequential developmental structure. Q5: None.

**OBS-034-061:** Group 777-001 (2 Cor 3:6) — the new covenant is administered by the Spirit rather than the letter. The inner-being dimension: the new covenant works from inside out (Spirit) rather than outside in (letter). This is the most decisive statement of how the new covenant transforms the inner person.

---

**GROUP 777-002** — *New self / new creation — inner-being renewal of the person in Christ* (G2537, Transformation, 4 relevant)
Note: Dimension Review flag — extends beyond covenant concept proper.
Anchor: Eph 4:24 (shared anchor with R076 holiness per §G.3).

verse_context.analysis_note — Eph 4:24 (mti=777): Q1: "Put on the new self, created after the likeness of God in true righteousness and holiness." Qualitative newness (kainos) of the person in Christ. Q2: Holiness (R076 — shared anchor), righteousness, Christlikeness. Q3: New covenant → new self — the new covenant's qualitative newness extends to the renewal of the person's inner constitution. Q4: Putting off old self → putting on new self — sequential transformation. Q5: Dimension Review flag is accurate — this verse uses kainos in new-creation rather than explicitly new-covenant language.

**OBS-034-062:** Group 777-002 — new self/creation (Transformation). The Dimension Review flag is accurate: these verses (Eph 4:24; 2 Cor 5:17; Gal 6:15; Eph 2:15) use kainos for new-creation renewal of the person, where covenant is the theological background but not the explicit content. This is a scope boundary under RD-034-002: the group is theologically connected to new covenant but lexically one step removed. Retained per RD-034-002 recommendation with this acknowledgement.

---

**GROUP 777-003** — *New name, song, Jerusalem — eschatological inner-being identity, worship, and hope* (G2537, Vitality/Existence, 7 relevant)
Note: Dimension Review flag — extends beyond covenant concept proper.
Anchor: Rev 2:17 (shared with R204 name per §G.3).

verse_context.analysis_note — Rev 2:17 (mti=777): Q1: "To the one who conquers I will give some of the hidden manna, and I will give him a white stone, with a new name written on the stone." Eschatological new identity. Q2: Identity, name (R204 — shared anchor), eschatological hope, inner renewal. Q3: New covenant → eschatological new identity — the covenant's newness extends to ultimate identity renewal. Q4: Conquest/faithfulness → new name/identity — sequential eschatological reward. Q5: Dimension Review flag is accurate — these Revelation verses use kainos in broad eschatological rather than explicitly covenant contexts.

**OBS-034-063:** Group 777-003 — new name, new song, new Jerusalem (Vitality/Existence). The Dimension Review flag is accurate: these eschatological Revelation uses of kainos are theologically downstream from new-covenant theology but not explicitly covenantal in content. The sole Vitality/Existence group in the registry. Retained per RD-034-002 recommendation.

---

**GROUP 3270-001** — *Reverential awe before the holy — ark as mediating sign orienting inner person toward God's presence* (G2787G, Dependence/Creatureliness, 2 relevant)
Anchor: Rev 11:19.

verse_context.analysis_note — Rev 11:19 (mti=3270): Q1: "The ark of his covenant was seen within his temple" — the ark disclosed in the heavenly temple as the sign of covenantal faithfulness. Q2: Awe, reverential dependence, God's presence and faithfulness. Q3: Ark-sight → reverential awe — the covenantal sign produces inner dependence/creatureliness response. Q4: Vision of ark → awe. Q5: None — thin evidence.

**OBS-034-064:** Group 3270-001 — the ark of the covenant as a mediating sign of divine presence orienting the inner person toward reverential awe. The Dependence/Creatureliness assignment is appropriate. Coverage extremely thin (PH2-34-003).

---

**GROUP 3271-001** — *Obedience under judgment — ark as instrument separating faithful from heedless response* (G2787H, Volition, 1 relevant, WARN: 200%)
Anchor: 1 Pet 3:20.

verse_context.analysis_note — 1 Pet 3:20 (mti=3271): ANALYSIS_VC_UNVERIFIED_MATERIAL — 200% set-aside. Q1: "Eight persons were brought safely through water" — Noah's ark as the covenantal instrument of faithful response. Q2: Obedience, faithfulness, judgment, baptismal typology. Q3: Faithful obedience ↔ covenant-preservation — the ark separates those whose inner orientation is obedient from those whose is heedless. Q4: Warning → faithful obedience (Noah) → salvation through water; contrast: others' heedlessness → judgment. Q5: The baptismal typology (1 Pet 3:21) connects covenant obedience to the new covenant sacrament — Session D?

**OBS-034-065:** Group 3271-001 — Noah's ark as covenantal instrument of faithful response. The Volition assignment captures the inner orientation that built and entered the ark. Peter's typological connection to baptism links covenant-obedience → salvation through water → baptism as new covenant sign. ANALYSIS_VC_UNVERIFIED_MATERIAL.

Stage 2a Progress Record: `Unit 7 COMPLETE: 2026-05-01. All 32 anchor groups read. 31 observations (OBS-034-035 to OBS-034-065). 0 additional SD pointers in Unit 7.`

---

### Unit 8 — Thin-Evidence Phase2 Flags

Reading §I.

| Term | Flags |
|---|---|
| H0423 | Flag 16 (None noted) |
| H3772G | THIN_DATA |
| G1242 | Flag 16 (None noted), SPAN_RESOLUTION_CONFLICT |
| G2537 | Flag 16 (None noted) |

**OBS-034-066:** H3772G carries THIN_DATA — aligns with extreme set-aside ratios for its groups (767-001: 4500%, 767-002: 1125%). Findings from H3772G groups are analytically minimal. ANALYSIS_VC_UNVERIFIED_MATERIAL applies throughout.

**OBS-034-067:** G1242 carries SPAN_RESOLUTION_CONFLICT ("Queried Strong's not found in any verse span after suffix resolution — verse set is empty. Manual STEP UI verification required"). This is a data integrity concern for G1242, compounding the 9% coverage issue (PH2-34-001). G1242 findings should be treated with heightened caution pending verification.

Stage 2a Progress Record: `Unit 8 COMPLETE: 2026-05-01. 2 observations (OBS-034-066, OBS-034-067).`

---

### Unit 9 — Existing Findings: Input Material Review

DIM-34-001 assessed against everything read in Units 3–8.

**DIM-34-001 verdict: CONFIRMED — deepened.**  
The inner transformation trajectory from Sinai to new covenant is one of the most coherent patterns in the registry. It is visible and substantiated across multiple groups and anchor verses:
- OBS-034-040 (Jer 31:33 — heart as constitutional site of new covenant)
- OBS-034-059 (Heb 8:10 — law written on mind and heart)
- OBS-034-061 (2 Cor 3:6 — Spirit vs. letter)
- OBS-034-039 (Deu 7:9 — hesed as the quality holding the Sinai covenant)
The DIM-34-001 claim that "the inner person is the site of covenantal fulfilment" under the new covenant is fully supported. No aspect appears overstated. Will address in Stage 2b T5 (Formative and Developmental) and T2 (Constitutional Location).

Stage 2a Progress Record: `Unit 9 COMPLETE: 2026-05-01. 1 finding reviewed. Confirmed: 1. Questioned: 0. Set-aside candidate: 0.`

---

### Stage 2a Sign-Off Checklist

| Unit | Subject | Status |
|---|---|---|
| 1 | Registry overview | COMPLETE |
| 2 | XREF terms | COMPLETE |
| 3 | OWNER terms: lexical foundation | COMPLETE |
| 4 | Verse context groups: landscape | COMPLETE |
| 5 | Correlation signals | COMPLETE |
| 6 | Existing SD pointers and findings | COMPLETE |
| 7 | Anchor verse reading — all 32 groups | COMPLETE |
| 8 | Thin-evidence phase2 flags | COMPLETE |
| 9 | Existing findings: input material review | COMPLETE |

Additional checks:
- Path 3 notes from Stage 1: 0 flagged / 0 to resolve ✓
- SD Pointer Accumulator: all 6 pointers have required fields (see Final section) ✓
- Obslog Stage 2a portion: confirmed complete — no in-memory observations unwritten ✓

```
STAGE 2A COMPLETE — Registry 034 (covenant)
Date: 2026-05-01
Readiness version: wa-034-covenant-readiness-output-v6-20260501.md
Reading units completed: 9 of 9
Obslog Stage 2a portion: confirmed
SD pointers accumulated: 6 (SP-034-001 through SP-034-006)
Path 3 notes resolved: 0 of 0
Existing findings reviewed: 1 (DIM-34-001 — confirmed and deepened)
Anchor verse groups read: 32 across 15 terms
Total Stage 2a observations: OBS-034-001 through OBS-034-067 (67 observations)
RESEARCHER_DECISION items raised: 3 (RD-034-001, RD-034-002, RD-034-003)

Stage 2a observations are now fixed. Stage 2b may begin.
```

---

## SD Pointer Accumulator — Final (Stage 2a)

**SP-034-001** — raised Unit 2, 2026-05-01, MEDIUM, Session D
- Target: R001 (abomination) · Connecting term: G1303 diatithēmi
- Question: G1303 ("to make a covenant") is the primary NT covenant-making verb but sits in R001. Does R001's analysis address the covenant-making dimension, or is there a gap? Session D should cross-read R001 and R034 on this term.
- Evidence basis: OBS-034-003
- Priority: MEDIUM

**SP-034-002** — raised Unit 2, 2026-05-01, MEDIUM, Session D
- Target: R159 (testimony) · Connecting term: H5715 e.dut
- Question: The covenant-testimony boundary (ark = ark of testimony; tablets = tablets of testimony) is a structural OT nexus. Does R159 capture the inner-being dimension of covenant-bearing witness?
- Evidence basis: OBS-034-005, §G.3 shared anchor 2Ki 23:3
- Priority: MEDIUM

**SP-034-003** — raised Unit 5, 2026-05-01, HIGH, Session D
- Target: R103 (love) — 37 shared verses · Connecting term: H1285 berit + H2617 hesed
- Question: Does R103 carry the hesed vocabulary that pairs structurally with berit? Session D must examine the hesed-berit pair as constitutive for C17 synthesis.
- Evidence basis: OBS-034-029, OBS-034-039, §G.2
- Priority: HIGH

**SP-034-004** — raised Unit 5, 2026-05-01, HIGH, Session D
- Target: R112 (mind) — 39 shared verses · Connecting term: H3820 leb / H3824 lebab
- Question: Does the mind registry engage the "heart-covenant" language? What does the covenant-mind connection disclose about covenant as the structuring principle of inner orientation?
- Evidence basis: OBS-034-029, OBS-034-030, OBS-034-040, OBS-034-059
- Priority: HIGH

**SP-034-005** — raised Unit 5, 2026-05-01, MEDIUM, Session D
- Target: R111 (mercy) — shared anchor Rom 1:31 · Connecting term: G0802 asunthetos
- Question: Does R111's analysis of Rom 1:31 engage the covenant-breaking dimension? Is there a structural relationship between covenant faithfulness and mercy requiring synthesis?
- Evidence basis: OBS-034-033, §G.3
- Priority: MEDIUM

**SP-034-006** — raised Unit 6, 2026-05-01, MEDIUM, Session D
- Target: R117 (peace) — berit shalom passages · Connecting term: H1285 berit + H7965 shalom
- Question: Does R117's analysis address the berit-shalom nexus (Num 25:12; Isa 54:10; Eze 34:25; 37:26)? If not, Session D should initiate a cross-registry pass.
- Evidence basis: OBS-034-034, PH2-34-004
- Priority: MEDIUM

---

## RESEARCHER_DECISION Accumulator — Final (Stage 2a)

**RD-034-001** — raised 2026-05-01, MEDIUM
- Decision required: Confirm PH2-34-005 (extraction anomaly — 7 grammatical particles) is resolved and close the flag in DB.
- Context: OBS-034-034. Current term inventory shows 15 OWNER terms; the 7 particles are absent. Anomaly appears actioned but DB flag remains open.
- Recommendation: CC confirms and closes PH2-34-005 if term inventory is clean.

**RD-034-002** — raised 2026-05-01, MEDIUM
- Decision required: Should groups 777-002 and 777-003 (kainos — new self/creation and new name/song/Jerusalem) be retained as covenant inner-being evidence or flagged for scope boundary revision?
- Context: OBS-034-062, OBS-034-063. Both carry Dimension Review flags.
- Options: (A) Retain with analytical acknowledgement; (B) Flag for transfer; (C) Partial retain
- Recommendation: Option A — retain. The new covenant inherently generates new-creation realities. Stage 2b T1 to address scope question explicitly.

**RD-034-003** — raised 2026-05-01, HIGH
- Decision required: G1242 SPAN_RESOLUTION_CONFLICT flag — has manual STEP UI verification been performed? Is the G1242 verse set accurate?
- Context: OBS-034-067, §I. Compounds PH2-34-001 (9% coverage).
- Recommendation: CC or researcher to verify G1242 STEP extraction before material G1242 findings are relied upon in later stages.

---

*wa-034-covenant-obslog-v1-20260501.md*
*Registry 034 covenant — Stage 2a complete*
*Previous input: wa-034-covenant-readiness-output-v6-20260501.md*
*Stage 2b pending — catalogue T0–T7 confirmed present in §L*

---

## Stage 2a Supplement — G1242 Verse Set Confirmed

**Date:** 2026-05-01 (same session)

**Context:** Researcher has provided the G1242 (diathēkē) verse set directly. This resolves RD-034-003 (SPAN_RESOLUTION_CONFLICT flag) for Stage 2a purposes.

**Confirmed G1242 verses (30 total):**

Mat 26:28 · Mar 14:24 · Luk 1:72 · Luk 22:20 · Act 3:25 · Act 7:8 · Rom 9:4 · Rom 11:27 · 1Cor 11:25 · 2Cor 3:6 · 2Cor 3:14 · Gal 3:15 · Gal 3:17 · Gal 4:24 · Eph 2:12 · Heb 7:22 · Heb 8:6 · Heb 8:8 · Heb 8:9 · Heb 8:10 · Heb 9:4 · Heb 9:15 · Heb 9:16 · Heb 9:17 · Heb 9:20 · Heb 10:16 · Heb 10:29 · Heb 12:24 · Heb 13:20 · Rev 11:19

**RD-034-003 status: RESOLVED.** The verse set is accurate and complete at 30 verses. The SPAN_RESOLUTION_CONFLICT appears to have been a tool-side extraction artifact, not a data gap. G1242 findings may proceed on this confirmed verse base; PH2-34-001 (9% coverage of 340 total NT occurrences) remains active — this confirmed set represents a curated working sample.

**OBS-034-068:** The confirmed G1242 verse set reveals a heavily Hebrews-concentrated corpus — 14 of 30 verses are from Hebrews (46%), which is the NT's primary theological treatment of covenant. This concentration is analytically significant: the Hebrews argumentation (better covenant, mediator, testament/will logic, blood of the covenant, eternal covenant) is the dominant frame for G1242 in the programme's working set. The other concentrations are: Synoptic and Pauline new-covenant communion language (Mat 26:28, Mar 14:24, Luk 22:20, 1 Cor 11:25 — the cup of the new covenant in Christ's blood), Pauline covenant theology (Rom, Gal, Eph), and Acts (Abrahamic covenant).

**OBS-034-069:** The testamentary dimension (Heb 9:16–17 — "where a will is involved, the death of the one who made it must be established") is confirmed as present in the verse set. This is the most explicit exploitation of the diathēkē-as-will dual sense. The argument: Christ's death is what enacts the new covenant, because a will (diathēkē) only takes effect at death. This theological move — covenant requires the testator's death — gives the new covenant its unique inner-being weight: it is not merely a new agreement but a death-enacted inheritance. OBS-034-019 is confirmed and deepened.

**OBS-034-070:** Heb 10:29 — "has profaned the blood of the covenant by which he was sanctified, and has outraged the Spirit of grace" — is analytically important for the moral-character dimension. Profaning the covenant blood is described as outraging the Spirit of grace — covenant breach and Spirit-grieving are linked. This connects the covenant-breaking vocabulary (G0802 asunthetos, OBS-034-018, OBS-034-057) to the Spirit-relationship. Covenant faithfulness and Spirit-responsiveness are structurally linked in the NT.

**OBS-034-071:** Gal 4:24 — "these women are two covenants. One is from Mount Sinai, bearing children for slavery; she is Hagar" — is the allegorical reading of the two covenants (Sinai/Hagar vs. Jerusalem above/Sarah). The inner-being dimension: covenant membership shapes identity and inner condition — Sinai covenant produces "children for slavery" (inner bondage); the new covenant produces free children (inner freedom). Covenant determines the inner-being condition of those within it.

**OBS-034-072:** 2 Cor 3:14 — "when they read the old covenant, that same veil remains unlifted" — introduces the cognitive dimension explicitly: a veil over the mind when reading the old covenant. This is direct evidence for Cognition engaging covenant (OBS-034-026 noted the absence of Cognition in the group landscape — this verse provides the counterevidence). The old covenant produces cognitive blindness; the new covenant removes the veil (2 Cor 3:16). This is a direct engagement of cognition by covenant, missed in the group landscape. Note for Stage 2b T3.2 (Cognition).

**OBS-034-073:** Luk 1:72 — "to show the mercy promised to our fathers and to remember his holy covenant" — directly pairs covenant and mercy (eleos). This is a Luke-specific lexical pairing: God's remembrance of his covenant = the showing of mercy. This verse is analytically important for SP-034-005 (mercy-covenant nexus, R111). "Remember his holy covenant" connects to OBS-034-038 (Gen 9:15 — "I will remember my covenant") — divine memory of covenant = covenant faithfulness = mercy.

**OBS-034-074:** Heb 13:20 — "by the blood of the eternal covenant" — the covenant is described as "eternal" (aiōnios). This is the ultimate qualifier: not merely everlasting (like the Davidic covenant) but eternal in a qualitative sense. The blood of the eternal covenant is the ground of God's resurrecting Christ. The inner-being dimension: the eternal covenant is the basis of resurrection hope — the covenant's eternality grounds the most fundamental inner-being hope.

**Updated RD-034-003 record:** RESOLVED — researcher provided verse set directly. G1242 SPAN_RESOLUTION_CONFLICT is a tool-side artifact; verse set is accurate at 30 verses. CC should clear the SPAN_RESOLUTION_CONFLICT flag from §I for this term.

Stage 2a Progress Record supplement: `G1242 verse set confirmed 2026-05-01. 7 additional observations (OBS-034-068 to OBS-034-074). RD-034-003 RESOLVED. Stage 2a observations now fixed at OBS-034-001 through OBS-034-074 (74 total).`

**Updated Stage 2a sign-off count: 74 observations (OBS-034-001 to OBS-034-074).**

Stage 2a observations are now fixed (including this supplement). Stage 2b may begin.

---

## Stage 2b — Second-Tier Q&A Log

Catalogue: T0–T7 (189 prompts, 56 components). Drawn from §L of wa-034-covenant-readiness-output-v6-20260501.md. Stage 2a observations are the evidence base.

#### Tier 0 — Divine Image and Created Design — 12 prompts

**Q&A-001 | T0.1.1**
- Tier: T0 — Divine Image and Created Design
- Component: T0.1 — Divine Nature Reflected
- Prompt: 1 — What does the verse evidence reveal about the nature or character of God that this characteristic reflects or images?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The verse evidence reveals that covenant-making and covenant-keeping are primary attributes of God's nature. God is "the faithful God who keeps covenant and steadfast love" (Deu 7:9 — OBS-034-039). He swears by himself because there is no greater (Heb 6:13, inferred from 3308-001 — OBS-034-052). He "remembers" his covenant (Gen 9:15 — OBS-034-038) — covenant-keeping is an act of God's own inner memory and faithfulness. The divine nature that covenant reflects is: faithfulness (keeping commitment across time), initiative (God cuts the covenant — OBS-034-046), and the capacity for binding self-commitment. In God, covenant is not a response to external pressure but an expression of who he is — his relational disposition toward his creation.
- Anchor verses: Gen 9:15, Deu 7:9, Heb 8:10
- Finding type: THEOLOGICAL_NOTE

**Q&A-002 | T0.1.2**
- Tier: T0 — Divine Image and Created Design
- Component: T0.1 — Divine Nature Reflected
- Prompt: 2 — Does Scripture explicitly attribute this characteristic to God — and if so, what does that attribution reveal about its significance in the human person?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — Scripture explicitly attributes covenant-making and covenant-keeping to God throughout the OT and NT. God is the primary covenant-maker across all covenant traditions: Noahic (OBS-034-038), Abrahamic (OBS-034-046), Mosaic (OBS-034-039), Davidic (OBS-034-041), and the new covenant (OBS-034-040, OBS-034-061). God swears by himself (3308-001 — OBS-034-052). The attribution reveals that in the human person, the capacity to covenant — to bind oneself to another in solemn, faithful commitment — is a reflection of God's own inner nature. Human covenant-making is not merely a legal or social function; it images the divine capacity for faithful relational self-binding. The human who makes and keeps covenant exercises one of the most God-like capacities available to a creature.
- Anchor verses: Gen 9:15, Deu 7:9, Jer 31:33, Heb 8:10
- Finding type: THEOLOGICAL_NOTE

**Q&A-003 | T0.1.3**
- Tier: T0 — Divine Image and Created Design
- Component: T0.1 — Divine Nature Reflected
- Prompt: 3 — Where Scripture is silent about God's possession of this characteristic, what does that silence suggest?
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Scripture is not silent — God's possession of covenant-making and covenant-keeping is extensively and explicitly affirmed throughout the verse evidence. This prompt's closing condition (silence) does not apply here.

**Q&A-004 | T0.2.1**
- Tier: T0 — Divine Image and Created Design
- Component: T0.2 — Created Purpose
- Prompt: 1 — What does the verse evidence suggest about the purpose this characteristic serves in the human person as created?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The verse evidence suggests that the human capacity for covenant serves the purpose of structuring faithful, committed relationship — both vertically (with God) and horizontally (with other persons). The vocabulary of covenant spans marriage alliance (H1285 sub-sense 1a5 — OBS-034-009), friendship covenant (3304-004 — OBS-034-049), political treaty (1a1), and the divine-human bond (1b). The created purpose is the capacity to enter and sustain solemn, binding relational commitments — to be the kind of person who can make a promise and keep it, whose word is reliable, and who can be held in relationship through structured mutual commitment. This equips the human person for stable communal life, faithful marriage, and the particular form of relationship with God that Scripture calls covenantal.
- Anchor verses: Neh 9:38, Deu 7:9, 2Sa 23:5
- Finding type: THEOLOGICAL_NOTE

**Q&A-005 | T0.2.2**
- Tier: T0 — Divine Image and Created Design
- Component: T0.2 — Created Purpose
- Prompt: 2 — Is this characteristic part of the original created design, a response to the fallen condition, or both?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The evidence supports both elements but in different ways. The capacity for covenant-making (binding solemn relational commitment) is almost certainly part of the original created design — it reflects God's own nature (Q&A-002) and structures the relationship for which humans were created. The first covenant in Scripture is with Noah (Gen 6:18; 9:9-17 — OBS-034-038) — but this follows the fall and the flood. There is no explicit pre-fall covenant vocabulary in Genesis 1–2 in the programme's verse set. The Noahic covenant is a response to the fallen condition (God commits not to destroy again). What is missing from the data: whether the Edenic relationship contained covenantal structure (some traditions speak of a covenant of works, but this is theological inference, not programme verse evidence). The oath/curse vocabulary (H0423 — OBS-034-007) and the covenant-breach vocabulary (H3748 divorce, G0802 asunthetos — OBS-034-012, OBS-034-018) are clearly responses to or consequences of the fallen condition. Gap: the pre-fall covenantal design of the human person is not directly addressed by the programme's verse evidence. Naming this as S-adjacent — the data partially addresses this but the pre-fall dimension is genuinely absent from the evidence.
- Anchor verses: Gen 9:15, Gen 6:18
- Finding type: THEOLOGICAL_NOTE
- Stage 2b note: Gap noted — pre-fall covenantal design not in verse set. Not a Stage 2a reopening item; an inherent evidence limitation.

**Q&A-006 | T0.2.3**
- Tier: T0 — Divine Image and Created Design
- Component: T0.2 — Created Purpose
- Prompt: 3 — Is there evidence that this characteristic is oriented toward a future fullness?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the covenant vocabulary is explicitly eschatologically oriented in multiple registers. The new covenant (765-003, 766-002, 777-001 — OBS-034-040, OBS-034-059, OBS-034-061) is both a present reality and a future fullness. The Davidic covenant is "everlasting" (OBS-034-041). Heb 13:20 names the "blood of the eternal covenant" (OBS-034-074) as the ground of resurrection. Groups 777-002 (new self/creation) and 777-003 (new name, new song, new Jerusalem — OBS-034-063) extend the covenant vocabulary into eschatological new creation. Eph 2:12 — "covenants of promise" (OBS-034-060) — places covenant in the register of future inheritance. The covenant vocabulary is not static but directional: the OT covenant sequence (Noahic, Abrahamic, Mosaic, Davidic) moves toward the new covenant, which itself points to the eternal covenant and the eschatological new creation. Covenant is both the current structuring reality and the framework of ultimate hope.
- Anchor verses: Heb 13:20, Eph 2:12, Rev 21:1-5
- Finding type: THEOLOGICAL_NOTE

**Q&A-007 | T0.3.1**
- Tier: T0 — Divine Image and Created Design
- Component: T0.3 — Image-Bearer Expression
- Prompt: 1 — In what way does this characteristic express the divine image in the human person?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant expresses the divine image in the human person through the capacity for faithful, binding relational self-commitment — the ability to pledge oneself to another with lasting effect. God's own nature is characterised by covenant-faithfulness (Q&A-001, Q&A-002). When a human person makes and keeps a covenant, they exercise a capacity that images God's own faithful relational disposition. Specifically: the human capacity for oath (H7650 — OBS-034-017, OBS-034-053) as moral character; the capacity for firm, faithful commitment (H0548 amanah, rooted in emunah faithfulness — OBS-034-008); and the capacity for self-binding through solemn promise (H0423 alah — OBS-034-007) are all expressions of the divine image. The image-bearing dimension is not merely formal (the ability to make promises) but qualitative: covenant faithfulness as a moral-character quality mirrors God's own faithfulness.
- Anchor verses: Neh 9:38, Deu 7:9
- Finding type: THEOLOGICAL_NOTE

**Q&A-008 | T0.3.2**
- Tier: T0 — Divine Image and Created Design
- Component: T0.3 — Image-Bearer Expression
- Prompt: 2 — Is this characteristic shared between God and the human person, or exclusively a creaturely analogue?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: The evidence supports that covenant is genuinely shared — both God and the human person make and keep covenants, and Scripture presents these as structurally analogous acts (though asymmetric in ground and reliability). God initiates covenants (OBS-034-046, OBS-034-052); humans enter and respond to God's covenants and also make their own person-to-person covenants (765-005, 3304-004 — OBS-034-042, OBS-034-049). The same Hebrew term (berit, karat berit) is used for both. The human instance is not merely an analogue — the human capacity to covenant is a genuine participation in the same type of act, though the human's faithfulness is contingent and fallible while God's is absolute and self-grounded. This distinguishes covenant from, for example, omniscience or omnipotence, which are exclusively divine and have no genuine human analogue.
- Anchor verses: Gen 9:15, Neh 9:38
- Finding type: THEOLOGICAL_NOTE

**Q&A-009 | T0.3.3**
- Tier: T0 — Divine Image and Created Design
- Component: T0.3 — Image-Bearer Expression
- Prompt: 3 — What does the presence or absence of this characteristic reveal about the condition of the divine image in the person?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The verse evidence provides clear indicators. Presence of covenant-faithfulness: in the human, keeping covenant is an expression of moral integrity (3308-002 — OBS-034-053), alignment with God's own character (Deu 7:9 — OBS-034-039), and is associated with knowing God and living under his blessing. Absence or corruption: G0802 (asunthetos — covenant-breaking as inner character defect — OBS-034-018, OBS-034-057) appears in Paul's catalogue of the debased mind (Rom 1:31) — the morally degraded human who has rejected God becomes incapable of covenant faithfulness. Dan 9:11 (OBS-034-036) frames collective covenant breach as the inner moral failure of a people. The pattern: covenant faithfulness indexes the health of the divine image in the person; covenant-breaking indexes its degradation. The person who cannot keep covenant is described in terms of inner moral collapse.
- Anchor verses: Rom 1:31, Dan 9:11, Deu 7:9
- Finding type: THEOLOGICAL_NOTE

**Q&A-010 | T0.4.1**
- Tier: T0 — Divine Image and Created Design
- Component: T0.4 — Typological Significance
- Prompt: 1 — Does Scripture use this characteristic typologically?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — covenant is used typologically throughout Scripture, and with unusual density. (1) The Noahic covenant and ark (G2787H, 1 Pet 3:20 — OBS-034-065) are deployed by Peter as a type of baptism: the saved-through-water structure of Noah's covenant-obedience prefigures the new covenant sign of baptism. (2) The Sinai covenant (blood of the covenant — Exo 24:8, echoed in Mat 26:28, Mar 14:24, Heb 9:20) is taken up into the new covenant in Christ's blood — the Eucharist is the new covenant's covenantal meal, explicitly structured after Sinai's blood ritual. (3) The Davidic covenant (everlasting covenant — OBS-034-041) is deployed typologically in the NT as pointing toward Christ's eternal kingship. (4) Gal 4:24 (OBS-034-071) explicitly allegorises the two covenants (Hagar/Sinai = slavery; Sarah/Jerusalem = freedom). (5) Hebrews systematically typologises the Mosaic covenant as a shadow of the new: the ark (OBS-034-064), the blood of bulls and goats (Heb 9:13 context), the tabernacle — all point beyond themselves to Christ. Covenant is the primary typological category of the OT in the NT's reading of Scripture.
- Anchor verses: 1 Pet 3:20, Mat 26:28, Heb 9:15, Gal 4:24
- Finding type: THEOLOGICAL_NOTE

**Q&A-011 | T0.4.2**
- Tier: T0 — Divine Image and Created Design
- Component: T0.4 — Typological Significance
- Prompt: 2 — If typological use is present, what is the direction of the typology?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence shows both directions, operating differently in the covenant vocabulary. The primary direction is divine → human → divine: God establishes the covenantal pattern (Noahic, Abrahamic, Mosaic, Davidic), the human community receives and participates in it, and those OT covenants point typologically forward to the new covenant enacted by Christ (divine initiative completing what the prior covenants anticipated). The Gal 4:24 allegorical reading (OBS-034-071) has God establishing the divine archetype (Sarah/new Jerusalem) which judges and supersedes the human instance (Hagar/Sinai). The secondary direction is human → divine: the human marriage covenant (H1285 1a5, H3748 divorce — OBS-034-012, OBS-034-043) is used as the vehicle for understanding the God-Israel relationship — the human instance illuminates the divine by analogy. This is the metaphorical direction. Both directions are active; the primary typological movement is from OT covenant realities pointing forward to the new covenant in Christ.
- Anchor verses: Gal 4:24, Heb 9:15, Heb 13:20
- Finding type: THEOLOGICAL_NOTE

**Q&A-012 | T0.4.3**
- Tier: T0 — Divine Image and Created Design
- Component: T0.4 — Typological Significance
- Prompt: 3 — If no typological use is evidenced, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Typological use is extensively evidenced (Q&A-010, Q&A-011). This prompt's closing condition does not apply.

TIER T0 COMPLETE — Divine Image and Created Design
Date: 2026-05-01
Prompts: 12 total. A: 9. P: 1. S: 0. N: 2.
New findings: 8. SD pointers raised: 0.


#### Tier 1 — Definition — 24 prompts

**Q&A-013 | T1.1.1**
- Tier: T1 — Definition
- Component: T1.1 — Name and Naming
- Prompt: 1 — What is this characteristic called in the programme — and what does the name itself signal about its essential nature?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: The characteristic is named 'covenant' in the programme. The name immediately signals a relational, formal, binding category — not an emotion, a disposition, or a condition, but a structured bond between parties. 'Covenant' carries juridical weight (formal agreement), personal weight (involving persons who commit themselves), and temporal weight (spanning time, upheld across circumstances). The name orients the enquiry toward the structure of relationship rather than the content of relationship — it is not what is shared between the parties but the form of bond that makes sharing possible and obligatory. This is the defining signal: covenant is the architecture of relationship, not the substance of it (OBS-034-002).
- Anchor verses: Deu 7:9, Gen 9:15
- Finding type: MEANING_OBSERVATION

**Q&A-014 | T1.1.2**
- Tier: T1 — Definition
- Component: T1.1 — Name and Naming
- Prompt: 2 — What do the primary Hebrew and Greek terms reveal at the definitional level?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Three definitional-level revelations: (1) Hebrew berit (H1285 — OBS-034-009, OBS-034-010): the core term spans man-to-man and God-to-man bonds — covenant is not exclusively divine-human but covers the full range of solemn human relational commitments including marriage, treaty, and friendship. The BARA root connection (tentative — OBS-034-010) suggests covenant meals as a sealing mechanism. (2) Hebrew karat (H3772G/H — OBS-034-013, OBS-034-014): the idiom 'karat berit' (cut a covenant) reveals that covenant-making in Hebrew thought involves a physical, enactive dimension — the cutting ritual as bodily enactment of the commitment. Covenant is not only inner intention but somatic performance. (3) Greek diathēkē (G1242 — OBS-034-019, OBS-034-069): carries the semantic dual of covenant and testamentary will. In the NT, this dual meaning is theologically exploited: the new covenant takes effect through the testator's death (Christ's). The Greek term imports the death-and-inheritance structure into covenant theology — the new covenant is an inheritance received because the testator has died.
- Anchor verses: Gen 9:15, Heb 9:16-17, Mat 26:28
- Finding type: ETYMOLOGY

**Q&A-015 | T1.1.3**
- Tier: T1 — Definition
- Component: T1.1 — Name and Naming
- Prompt: 3 — Does the name carry directional, relational, or constitutional implications that orient the enquiry?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: Yes — all three. Directional: the covenant vocabulary shows that covenant flows from God outward (divine initiative — OBS-034-046, OBS-034-052) and from God's self-giving toward human reception. The direction is not symmetrical. Relational: the name itself is inherently two-party — covenant implies parties in relationship. There is no covenant without a counterpart. The programme has correctly assigned covenant to the C17 relational-grace cluster. Constitutional: the 'law written on the heart' language (OBS-034-040, OBS-034-059) and the 'Spirit rather than letter' language (OBS-034-061) show that covenant operates constitutionally — it restructures the inner person, not merely their external obligations. These three directional, relational, and constitutional implications collectively shape the entire analytical enquiry: what God initiates, who the parties are, and where in the inner person it operates.
- Anchor verses: Jer 31:33, Heb 8:10, Deu 7:9
- Finding type: MEANING_OBSERVATION

**Q&A-016 | T1.2.1**
- Tier: T1 — Definition
- Component: T1.2 — Kind
- Prompt: 1 — What kind of inner-being phenomenon does this characteristic appear to be — an act, a disposition, a condition, a quality, or something else?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant is structurally composite — it is not simply one kind of inner-being phenomenon but operates across multiple kinds, depending on the subject and the covenant's phase. (1) For God: covenant is a relational disposition — an enduring orientation of committed faithfulness toward the covenantal partner (OBS-034-038, OBS-034-052). God's covenant is not an act completed in the past but an ongoing inner commitment. (2) For the human person entering covenant: covenant-making is an inner-being act — a volitional commitment performed at a moment (Neh 10:29 — OBS-034-035; karat berit — OBS-034-046). (3) For the human person within covenant: covenant-keeping is a moral character quality — the sustained integrity of holding one's commitments (3308-002 — OBS-034-053). (4) For the new covenant recipient: covenant is a condition produced by God's inner action (law written on the heart — OBS-034-040; Spirit administration — OBS-034-061). The composite nature — disposition (God), act (entry), quality (keeping), condition (new covenant) — is analytically important. Different prompts across T2–T5 will need to track which mode is in view.
- Anchor verses: Gen 9:15, Neh 10:29, Deu 7:9, Jer 31:33
- Finding type: MEANING_OBSERVATION
- Stage 2b note: This four-mode structure (disposition / act / quality / condition) is the key definitional finding of T1 and should govern Stage 2b analysis throughout.

**Q&A-017 | T1.2.2**
- Tier: T1 — Definition
- Component: T1.2 — Kind
- Prompt: 2 — Is this characteristic simple in structure or does it have constituent elements at first encounter?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant is structurally complex — it has identifiable constituent elements that recur across the verse evidence. The elements visible in the data are: (1) Parties — covenant always involves at least two parties in relationship (God-human, human-human); (2) Commitment mechanism — oath, self-curse, cutting ritual, or blood (H0423 alah, karat, dam — OBS-034-007, OBS-034-013, Q&A-014); (3) Covenantal content — specific obligations, promises, or terms (law at Sinai; promise of land and descendants to Abraham; promise of dynasty to David; law on the heart in the new covenant); (4) Sign or seal — a confirmatory act or object (rainbow, circumcision, Sabbath, ark, blood of the covenant, Eucharistic cup); (5) Sanctions — blessings for keeping, curses for breach (H0423 — OBS-034-007, OBS-034-036). This five-element structure (parties, mechanism, content, sign, sanctions) is not explicitly systematised in the verse evidence as a formula, but the elements recur across the different covenant traditions in the data.
- Anchor verses: Neh 10:29, Gen 9:15, Deu 7:9, Mat 26:28
- Finding type: MEANING_OBSERVATION

**Q&A-018 | T1.2.3**
- Tier: T1 — Definition
- Component: T1.2 — Kind
- Prompt: 3 — What is the current best working description of this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Drawing from Stage 2a (OBS-034-001 through OBS-034-074) and Stage 2b T0–T1 work so far: Covenant is the solemn, binding relational bond through which God commits himself to his people and calls them to commitment in return — the structured architecture of faithful relationship that spans individual acts of entry, sustained moral character in keeping, and the constitutional transformation of the inner person through which relationship with God becomes possible and real. In its divine mode: covenant is God's enduring relational disposition of faithful self-commitment toward his covenantal partner. In its human mode: covenant involves an inner act of solemn self-binding (entering), a moral character quality of sustained integrity (keeping), and — under the new covenant — a constitutionally transformed condition of the inner person produced by God's own inner action (writing law on the heart, administering through the Spirit). Covenant is both the framework of relationship and the inner-being reality shaped by that relationship.
- Anchor verses: Gen 9:15, Deu 7:9, Jer 31:33, 2 Cor 3:6
- Finding type: MEANING_OBSERVATION
- Stage 2b note: This working description supersedes the registry-level label 'Relational/Social' (OBS-034-001). It should inform sb_classification at session close.

**Q&A-019 | T1.3.1**
- Tier: T1 — Definition
- Component: T1.3 — Boundary
- Prompt: 1 — What is the structural opposite of this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The structural opposite of covenant is covenant-breaking — the inner disposition and act of faithlessness that violates and severs the covenant bond. The data names this explicitly: G0802 asunthetos (untrustworthy, covenant-breaking — OBS-034-018, OBS-034-057) is Paul's term for the morally debased person who cannot hold covenants together. H0423 alah (oath/curse — OBS-034-007, OBS-034-036) shows that breach activates the self-invoked curse embedded in the oath — covenant-breaking is the self-destruction of the bond one has made. H3748 keritut (divorce as cutting of the marriage covenant — OBS-034-012, OBS-034-043) names the formal opposite: the "cut" that severs the covenant bond. Dan 9:11 (OBS-034-036) frames collective covenant breach as inner moral failure — transgression, turning aside, refusing to obey, sinning. The opposite is therefore: faithlessness (the character quality), covenant-breaking (the act), and divorce/cutting-off (the formal result). At the deepest level: the structural opposite of covenant is the severing of self from the relational bond through infidelity.
- Anchor verses: Rom 1:31, Dan 9:11
- Finding type: MEANING_OBSERVATION

**Q&A-020 | T1.3.2**
- Tier: T1 — Definition
- Component: T1.3 — Boundary
- Prompt: 2 — What does this characteristic explicitly exclude or resist?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: From the verse evidence: (1) Covenant explicitly excludes false covenants — making covenants with Canaanite inhabitants (3304-003 — OBS-034-048) is prohibited as a binding to false loyalties that misdirects inner allegiance away from God. (2) Covenant resists unfaithfulness — the curse embedded in the oath (H0423 — OBS-034-007) is the built-in mechanism resisting breach. (3) Covenant excludes the hardened-mind/veiled cognitive condition (2 Cor 3:14 — OBS-034-072) — the old covenant produces a veil; the new covenant resists and removes cognitive hardening. (4) Covenant resists the inner condition of alienation and hopelessness (Eph 2:12 — OBS-034-060) — covenant inclusion is the antidote to covenantal exclusion/desolation. In summary: covenant excludes false loyalty, resists infidelity, opposes cognitive hardening, and displaces inner alienation.
- Anchor verses: Exo 34:12, Rom 1:31, Eph 2:12, 2 Cor 3:14
- Finding type: MEANING_OBSERVATION

**Q&A-021 | T1.3.3**
- Tier: T1 — Definition
- Component: T1.3 — Boundary
- Prompt: 3 — What is this characteristic not — where does it end and something else begin?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: Gap identified
- Answer: From the data, several partial boundaries can be named. (1) Covenant is not the same as the love (hesed) that sustains it — covenant is the structural bond; hesed is the relational quality holding it (Deu 7:9 — OBS-034-039, SP-034-003). Covenant is the form; love is the substance. (2) Covenant is not law — though the Mosaic covenant contains law, the covenant itself is the relational bond within which law operates. The new covenant reframes this explicitly (2 Cor 3:6 — OBS-034-061): not of the letter but of the Spirit. (3) Covenant is not promise, though it includes promises — promise (epangelia) and covenant (diathēkē) are distinguished in Gal 3:17 (covenant previously ratified; law 430 years later does not annul it). (4) Covenant is not the same as the signs that seal it (circumcision, Sabbath, ark, blood) — the signs point to and confirm the covenant without being the covenant itself. What is not adequately answered from the current data: the precise boundary between covenant and oath — the XREF of H7621 (shevuah — oath) to R019 (calling) means the covenant-oath boundary is unresolved in the programme's structural arrangement. This is a genuine analytical gap for Session D.
- Anchor verses: Deu 7:9, Gal 3:17, 2 Cor 3:6
- Finding type: MEANING_OBSERVATION
- Stage 2b note: The covenant-oath boundary (H7621 in R019) is an unresolved programme-structural question. SP already raised (SP-034-002 direction; the oath boundary specifically belongs to Session D via the XREF arrangement).

**Q&A-022 | T1.4.1**
- Tier: T1 — Definition
- Component: T1.4 — Modes of Operation
- Prompt: 1 — In what distinct ways does this characteristic operate within the inner person?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Four distinct modes of operation are visible in the data (building on Q&A-016): (1) Structural-binding mode: covenant operates as the self-binding act by which the person commits themselves to a relational bond — entry into covenant through oath, cutting ritual, or formal agreement (Neh 10:29 — OBS-034-035). This is the initiating mode. (2) Moral-sustaining mode: covenant operates as the ongoing moral character quality of keeping one's word and maintaining loyalty (3308-002 — OBS-034-053). This is the sustaining mode. (3) Constitutional-transforming mode: under the new covenant, covenant operates as the mechanism of inner constitutional change — God writes law on the heart (OBS-034-040), Spirit replaces letter (OBS-034-061). This is the receiving-and-being-changed mode. (4) Identitary-locating mode: covenant establishes and sustains the person's inner-being identity — belonging to the covenantal community (OBS-034-035, OBS-034-060). Inclusion or exclusion from covenant shapes the person's fundamental inner condition (hope vs. desolation — OBS-034-060, OBS-034-074). These four modes are not sequential stages but concurrent registers in which covenant operates simultaneously.
- Anchor verses: Neh 10:29, Deu 7:9, Jer 31:33, Eph 2:12
- Finding type: MEANING_OBSERVATION

**Q&A-023 | T1.4.2**
- Tier: T1 — Definition
- Component: T1.4 — Modes of Operation
- Prompt: 2 — Does this characteristic operate differently depending on context, direction, or constitutional level?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — significantly so. (1) Direction: God's covenant operates from RD (relational disposition — enduring inner faithfulness); human covenant operates from Volition (entry act) and Moral Character (keeping quality) and is received as a constitutional condition (new covenant transformation). The same word (berit, diathēkē) operates differently depending on whose inner being is in view (OBS-034-054). (2) Context — OT vs. NT: the OT covenant primarily demands inner obedience while providing external law (Sinai — OBS-034-039); the NT new covenant provides inner transformation while producing the obedience it demands (OBS-034-040, OBS-034-061). The constitutional level of operation shifts from demand (Sinai) to provision (new covenant). (3) Horizontal vs. vertical: in person-to-person covenant (765-005, 3304-004), covenant operates as moral character (integrity, loyalty); in divine-human covenant, it operates as relational disposition (God's side) and volitional commitment plus constitutionally received transformation (human side — OBS-034-042, OBS-034-049).
- Anchor verses: Deu 7:9, Jer 31:33, 2 Cor 3:6, Neh 9:38
- Finding type: MEANING_OBSERVATION

**Q&A-024 | T1.4.3**
- Tier: T1 — Definition
- Component: T1.4 — Modes of Operation
- Prompt: 3 — Does this characteristic have a communicative or speech-based mode of operation?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — prominently. The oath (H0423, H7650 — OBS-034-007, OBS-034-017) is inherently speech-based: an oath is a spoken self-commitment before witnesses. H7650 (to swear) is a speech act — the swearing of an oath is the performative utterance that brings the covenant into being or seals it. The covenant curse (alah — OBS-034-036) is also speech-based: it is pronounced upon the covenant-breaker. In the NT: the "blood of the covenant" saying at the Last Supper (Mat 26:28; Lk 22:20; 1 Cor 11:25 — OBS-034-058) is a speech act by which Christ institutes the new covenant. God's speech in the new covenant oracle (Jer 31:31-34; Heb 8:8-10) is itself the covenantal declaration — "I will make a new covenant... I will write my law on their hearts." Covenant operates through word: spoken oath (entry), spoken curse (sanction), spoken declaration (institution). The communicative mode is not secondary but constitutive — covenants come into being through speech.
- Anchor verses: Neh 10:29, Mat 26:28, Jer 31:31, Heb 8:8
- Finding type: MEANING_OBSERVATION

**Q&A-025 | T1.5.1**
- Tier: T1 — Definition
- Component: T1.5 — Immediate Response
- Prompt: 1 — What is the first or most immediate inner-being response to receiving or encountering this characteristic?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The data shows varied immediate responses depending on the mode of encounter. (1) To God's covenant initiative: the immediate response is the volitional act of entering — joining, committing, taking the oath (Neh 10:29 — OBS-034-035). The text does not isolate a prior inner response before the entry act. (2) To the new covenant promise: Heb 8:10 and Jer 31:33 present the response as receiving — the inner person is written upon by God, not the reverse. The immediate response is being acted upon, not acting. (3) To covenantal exclusion (Eph 2:12 — OBS-034-060): the response is desolation — hopelessness, alienation, godlessness. (4) To covenant breach (Dan 9:11 — OBS-034-036): the experience of the activated curse — judgment as the immediate consequence. Gap: the data does not consistently present a single, uniform immediate inner response. The response depends heavily on which dimension of covenant is encountered (invitation, writing, exclusion, breach-consequence). This diversity is itself a finding: covenant is encountered differently by different inner-being subjects in different relational positions.
- Anchor verses: Neh 10:29, Eph 2:12, Dan 9:11
- Finding type: MEANING_OBSERVATION

**Q&A-026 | T1.5.2**
- Tier: T1 — Definition
- Component: T1.5 — Immediate Response
- Prompt: 2 — Is the immediate response consistent across the verse evidence, or does it vary?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: It varies — and the variation is structured rather than random. The immediate response tracks the relational position of the subject: (a) covenantal invitee who receives → volitional commitment and entry; (b) new covenant recipient → constitutional reception (being written upon); (c) covenantal outsider → inner desolation; (d) covenant-breaker → inner moral failure + activated curse. The variation confirms the finding in Q&A-016 (covenant operates in four modes) and Q&A-025. The data does not support a single uniform immediate response; it supports a spectrum of responses structured by the person's relational position relative to the covenant. This is not a gap — it is a structural finding about covenant's positional character.
- Anchor verses: Neh 10:29, Eph 2:12, Dan 9:11, Jer 31:33
- Finding type: MEANING_OBSERVATION

**Q&A-027 | T1.5.3**
- Tier: T1 — Definition
- Component: T1.5 — Immediate Response
- Prompt: 3 — Where the verse evidence is silent on immediate response, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: The verse evidence is not silent — it provides multiple responses structured by relational position (Q&A-025, Q&A-026). Silence is not the finding here; structured variation is.

**Q&A-028 | T1.6.1**
- Tier: T1 — Definition
- Component: T1.6 — Sustained Effect
- Prompt: 1 — What does this characteristic produce in the inner being over time?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The sustained effect of covenant-being (living within an active covenant relationship) on the inner person includes: (1) Inner moral formation — sustained covenant-keeping builds moral character: the oath-keeper is a person of integrity (3308-002 — OBS-034-053); the covenant-keeping community has a moral texture (Psa 25:10: "steadfast love and faithfulness for those who keep his covenant"). (2) Covenantal knowing — the new covenant explicitly produces a knowing of God over time: "they shall all know me, from the least to the greatest" (Jer 31:34 context — OBS-034-040). Covenant sustained over time produces an intimate knowledge of God in the inner person. (3) Hope and security — being within the eternal covenant (OBS-034-074), the everlasting Davidic covenant (OBS-034-041), or the covenants of promise (OBS-034-060) produces inner hope as a sustained condition. (4) Inner transformation — the new covenant's sustained effect is progressive inner renewal: law written on the heart is not a one-time event but an ongoing constitutive reality (OBS-034-059, OBS-034-061).
- Anchor verses: Jer 31:34, Psa 25:10, Heb 13:20, Eph 2:12
- Finding type: THEOLOGICAL_NOTE

**Q&A-029 | T1.6.2**
- Tier: T1 — Definition
- Component: T1.6 — Sustained Effect
- Prompt: 2 — What states, qualities, capacities, or orientations does sustained exposure to or possession of this characteristic establish?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Sustained covenantal life produces identifiable inner-being states and qualities: (1) Faithful character — the person sustained by covenant commitment develops the moral quality of reliability and trustworthiness (moral character dimension — 3308-002, OBS-034-053); (2) Knowing orientation — orientation toward God through the covenantal knowledge of him (Jer 31:34); (3) Hope-capacity — the inner capacity for future-oriented hope, grounded in the covenant's permanence and promise (OBS-034-041, OBS-034-074); (4) Communal identity — sustained belonging within the covenantal community, shaping the person's inner sense of identity and allegiance (OBS-034-035, OBS-034-060); (5) Moral vigilance — awareness of covenantal obligations and their weight, sustained by the knowledge of the curse embedded in breach (OBS-034-007, OBS-034-036).
- Anchor verses: Psa 25:10, Jer 31:34, Heb 13:20
- Finding type: THEOLOGICAL_NOTE

**Q&A-030 | T1.6.3**
- Tier: T1 — Definition
- Component: T1.6 — Sustained Effect
- Prompt: 3 — Does the sustained effect differ from the immediate response — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: Yes — they differ in quality and register. The immediate response is moment-specific (entering, receiving, being excluded, experiencing breach consequence — Q&A-025). The sustained effect is developmental: moral formation, growing knowledge of God, deepening hope, established identity, and moral vigilance accumulate over time within the covenant relationship. The most striking difference is in the new covenant mode: the immediate response is reception (being written upon by God); the sustained effect is knowing God intimately (Jer 31:34) — the writing produces the knowing over time. Similarly, immediate covenantal entry is a volitional act; sustained covenantal life shapes the character quality of faithfulness. The movement from act (immediate) to character quality (sustained) is a defining dynamic of covenant's inner-being operation.
- Anchor verses: Jer 31:33-34, Psa 25:10
- Finding type: MEANING_OBSERVATION

**Q&A-031 | T1.7.1**
- Tier: T1 — Definition
- Component: T1.7 — Conditions of Reception
- Prompt: 1 — What inner conditions or orientations enable genuine reception of this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The verse evidence identifies several inner conditions that enable genuine covenant reception: (1) Reverent fear — Mal 2:5 context (group 765-001: "he feared me. He stood in awe of my name" — OBS-034-038 direction) — the covenant of life and peace came to Levi because of reverent fear. (2) Love for God — Deu 7:9: "those who love him and keep his commandments" receive God's covenant faithfulness (OBS-034-039). Love is the inner orientation that enables receiving the covenant's relational quality. (3) Hearing/obedience orientation — Exo 19:5: "if you will indeed obey my voice and keep my covenant" — the inner orientation of attentive hearing enables covenant reception (OBS-034-030, R213 listen, 13 shared verses). (4) All-heart commitment — 2Ki 23:3 context (3304-002 — OBS-034-047): covenant made "with all the heart and all the soul" — partial inner engagement is not full reception. (5) For the new covenant: reception requires no prior inner condition from the human side — God acts unilaterally to write on the heart (Jer 31:33; Heb 8:10 — OBS-034-040). But response and growth in this reception is enabled by the same fear, love, and hearing orientation.
- Anchor verses: Deu 7:9, Exo 19:5, Jer 31:33
- Finding type: THEOLOGICAL_NOTE

**Q&A-032 | T1.7.2**
- Tier: T1 — Definition
- Component: T1.7 — Conditions of Reception
- Prompt: 2 — What inner conditions block, distort, or prevent reception?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The verse evidence identifies blocking conditions: (1) Hardened mind — 2 Cor 3:14: "their minds were hardened. For to this day, when they read the old covenant, that same veil remains unlifted" (OBS-034-072). Cognitive hardening blocks the reception of the covenant's transformative content — the veil prevents seeing through the old covenant to Christ. (2) Stubborn/evil heart — Jer 11:8: "everyone walked in the stubbornness of his evil heart... they did not obey or incline their ear" (group 765-002 context). Stubbornness and inclination of the will away from God blocks reception. (3) Covenant-breaking character — G0802 asunthetos: the person whose inner character is faithlessness is already disposed against covenant-reception (OBS-034-057). (4) False covenantal allegiance — making covenants with the wrong parties (3304-003 — OBS-034-048) misdirects the will and blocks genuine covenantal reception with God. (5) The veil of the old covenant (2 Cor 3:14-16 — OBS-034-072) — the old covenant itself becomes a blocking mechanism when read without Christ.
- Anchor verses: 2 Cor 3:14, Jer 11:8, Rom 1:31
- Finding type: THEOLOGICAL_NOTE

**Q&A-033 | T1.7.3**
- Tier: T1 — Definition
- Component: T1.7 — Conditions of Reception
- Prompt: 3 — What is the inner-being state of the person who encounters this characteristic but does not receive it?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The data provides a clear picture: (1) Desolation — Eph 2:12: "having no hope and without God in the world" (OBS-034-060). The person who encounters the covenants of promise and remains a stranger to them lives in inner desolation — hopelessness, alienation, godlessness. (2) Bondage — Gal 4:24-25 (OBS-034-071): remaining under the Sinai covenant without entering the new covenant freedom is described as bearing children for slavery — the inner condition is one of bondage. (3) Moral collapse — Rom 1:31: the covenant-breaker (asunthetos) appears in the catalogue of moral and cognitive failure that characterises those who have suppressed the truth (OBS-034-057). Not receiving the covenantal bond produces inner moral dissolution. (4) Curse activation — Dan 9:11 (OBS-034-036): the person who encounters the covenant, receives its obligations, but breaks it experiences the activated curse — the inner consequence of breach. The common thread: not receiving covenant (or receiving it falsely/partially) produces inner conditions of desolation, bondage, moral dissolution, or judgment.
- Anchor verses: Eph 2:12, Gal 4:24, Rom 1:31, Dan 9:11
- Finding type: THEOLOGICAL_NOTE

**Q&A-034 | T1.8.1**
- Tier: T1 — Definition
- Component: T1.8 — Dimension Classification
- Prompt: 1 — What is the primary inner-being dimension of this characteristic from the programme's dimension vocabulary?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The primary dimension of covenant is Relational Disposition (06) — defined as the enduring orientation of the inner person toward another in committed, faithful relationship. This is supported by the largest group count (9 of 32 groups in RD), the dominant theological framing (God's covenant is an expression of his relational disposition of faithful self-commitment — OBS-034-038, OBS-034-039, OBS-034-052), and the definitional core (covenant as the structure of faithful relationship — Q&A-013). The registry-level label 'Relational/Social' approximates but does not match this programme dimension label. The primary classification is 06 — Relational Disposition. This assignment should be recorded in sb_classification field for Registry 034 at session close. Note: this is the primary dimension at the registry level; individual groups are correctly assigned to other dimensions per their specific covenantal context (Volition, Moral Character, Transformation, etc.).
- Anchor verses: Gen 9:15, Deu 7:9, Heb 8:10
- Finding type: MEANING_OBSERVATION
- Stage 2b note: sb_classification = '06 — Relational Disposition' is the proposed registry-level assignment. To be confirmed at Stage 2b sign-off.

**Q&A-035 | T1.8.2**
- Tier: T1 — Definition
- Component: T1.8 — Dimension Classification
- Prompt: 2 — What evidence supports this classification?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: Three categories of supporting evidence: (1) Group distribution: RD has 9 of 32 active groups — the largest single dimension cluster. These 9 groups span the primary covenant actors (God and humans) and the primary covenant traditions (Noahic, Abrahamic, Mosaic/bilateral-relational, Davidic, new covenant through Christ's blood, divorce metaphor). (2) Dominant subject pattern: the RD groups all have God as the dominant subject in 7 of the 9 cases — God's covenant is his relational disposition of faithful commitment. The 2 human-held RD groups (3306-001, 3304-004) both name person-to-person relational loyalty as the core. (3) Definitional evidence: the programme's description of covenant as "binding agreement... not a contract between equals but a formal, solemn bond in which God commits himself to his people" (§A) explicitly frames covenant as relational disposition — an orientation of committed self-giving. Deu 7:9's "keeps covenant and steadfast love" pairs covenant with hesed as the relational quality that holds it — both are RD.
- Anchor verses: Gen 9:15, Deu 7:9, Lk 1:72
- Finding type: MEANING_OBSERVATION

**Q&A-036 | T1.8.3**
- Tier: T1 — Definition
- Component: T1.8 — Dimension Classification
- Prompt: 3 — Does this characteristic carry secondary dimensions — and do they compete with the primary classification?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — covenant carries substantial secondary dimensions that do not compete with but complement the primary RD classification: (1) Volition (04) — 7 groups: covenant-making is a volitional act of inner commitment; the Sinai covenant is structured around bilateral volitional obligation. Volition is the human response-mode to God's relational disposition. (2) Moral Character (05) — 6 groups: covenant-keeping as a moral quality; oath-keeping as inner integrity; covenant-breaking as moral defect. Moral Character is the sustained-mode expression of covenantal commitment. (3) Transformation (08) — 5 groups: the new covenant trajectory. Transformation is what the new covenant produces constitutionally in the inner person. (4) Minor dimensions: Emotion-Negative (02 — covenantal exclusion and mourning), Vitality/Existence (07 — eschatological new creation), Dependence/Creatureliness (10 — the ark as sign of reverential awe), Emotion-Positive (01 — adjuration in love). The secondary dimensions do not compete: RD is the structural ground (covenant is the relational bond), Volition is the entry mode (how the human enters), Moral Character is the sustaining mode (how the bond is kept), and Transformation is the new covenant's constitutive mode (what the bond produces). They are analytically complementary.
- Anchor verses: Deu 7:9, Neh 10:29, Jer 31:33
- Finding type: MEANING_OBSERVATION

TIER T1 COMPLETE — Definition
Date: 2026-05-01
Prompts: 24 total. A: 20. P: 2. S: 0. N: 2.
New findings: 16. SD pointers raised: 0.


#### Tier 2 — Constitutional Location and Boundaries — 31 prompts

**Q&A-037 | T2.1.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.1 — Spirit-Level Location
- Prompt: 1 — Is this characteristic explicitly located at the spirit level in the verse evidence?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The verse evidence does not use the term 'spirit' (ruach/pneuma) explicitly to locate covenant as a spirit-level reality in the human person, except in one structurally important instance: Isa 59:21 — "My Spirit that is upon you, and my words that I have put in your mouth" (Dual-context: Group 765-003 — OBS-034-040 direction). This verse frames the new covenant as involving God's Spirit placed upon and within the person — the Spirit's location within the human person is where the new covenant's content (God's words) is lodged. However, the Spirit here is the divine Spirit acting upon the human spirit, not the human spirit as the constitutional site of covenant per se. The human ruach is not explicitly named as the location of covenant in the programme's verse set. The closest is the 'breath/spirit' dimension implicit in the 'heart and mind' language of Heb 8:10 / Jer 31:33 — but those texts name heart and mind, not spirit. Gap: spirit-level location for covenant in the human person is not explicitly evidenced; the evidence points primarily to heart and mind (soul level).
- Anchor verses: Isa 59:21, Heb 8:10
- Finding type: SPIRIT_SOUL_BODY

**Q&A-038 | T2.1.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.1 — Spirit-Level Location
- Prompt: 2 — Does the evidence indicate that this characteristic originates in or is primarily a spirit-level phenomenon?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding
- Answer: For the divine side: covenant originates in God's own relational disposition — which in biblical categories is a spirit-level reality (God is spirit). God's faithfulness to covenant is grounded in his own inner character, which is not reduced to body or soul. For the human side: the evidence is not conclusive. The 2 Cor 3:6 contrast — "not of the letter but of the Spirit" (OBS-034-061) — suggests the new covenant operates at the level of the Spirit (divine Spirit enabling human spirit responsiveness) rather than the external letter. The Spirit of God acts upon and within the human person to enact the new covenant. Whether this constitutes a spirit-level constitutional location for covenant in the human person is not directly stated. What can be said: the new covenant's operation requires the Spirit's presence and action within the human person — which implies engagement at the deepest constitutional level, which in the programme's framework is spirit-level.
- Anchor verses: 2 Cor 3:6, Isa 59:21
- Finding type: SPIRIT_SOUL_BODY

**Q&A-039 | T2.1.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.1 — Spirit-Level Location
- Prompt: 3 — What does spirit-level location reveal about the nature and depth of this characteristic?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding
- Answer: To the extent that the new covenant operates at or through the spirit level (via God's Spirit enabling human spirit receptivity — 2 Cor 3:6; Isa 59:21), this reveals that covenant is not merely an intellectual agreement or volitional act but a reality that reaches the deepest constitutional stratum of the person. The new covenant's transformation — if it operates at spirit level — is constitutional change at the foundational level, not merely change of behaviour or even of moral character. This would place covenant in the category of deep-structure inner-being realities, consistent with the programme's observation that the new covenant is a qualitatively different (kainos) relationship, not merely an improved version of the old.
- Anchor verses: 2 Cor 3:6, Jer 31:33
- Finding type: SPIRIT_SOUL_BODY

**Q&A-040 | T2.1.4**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.1 — Spirit-Level Location
- Prompt: 4 — If the evidence is silent on spirit-level location, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is not silent — Isa 59:21 and 2 Cor 3:6 engage the Spirit dimension, though the human spirit's constitutional role as the site of covenant is not explicit. Q&A-037 through Q&A-039 address the available evidence.

**Q&A-041 | T2.2.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.2 — Soul-Level Location
- Prompt: 1 — Is this characteristic identified in the verse evidence as a soul-level phenomenon?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the soul is explicitly named in covenant contexts. 2Ki 23:3: "the king stood by the pillar and made a covenant before the Lord, to walk after the Lord... with all his heart and all his soul" (OBS-034-030, OBS-034-047 direction). The covenant commitment calls on the soul (nephesh) as one of the two central inner organs engaged. Psa 25:1 context (group 765-005 direction): covenant-keeping is associated with soul-level orientation. R182 (Soul) has 19 shared verses with covenant (OBS-034-030), confirming that soul-level engagement is frequent and consistent across the corpus. Covenant commitment is not merely intellectual or volitional — it calls upon the person's nephesh, the seat of life and personal identity.
- Anchor verses: 2Ki 23:3, Psa 25:1
- Finding type: SPIRIT_SOUL_BODY

**Q&A-042 | T2.2.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.2 — Soul-Level Location
- Prompt: 2 — What does soul-level location reveal about this characteristic's place in innermost personal experience?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Soul-level engagement means that covenant commitment calls upon the person's innermost seat of life and personal identity — the nephesh as the living person in their totality. The formula "with all your heart and all your soul" (occurring in covenant contexts — 2Ki 23:3, Deu 6:5 context, Jer 32:41 direction) is a totality expression: covenant requires not a portion of the inner person but the whole. Soul-level location reveals that covenant is not compartmentalised — it does not reside in one faculty or function but calls the whole living person into commitment. The soul as the integrating personal subject means covenant is a whole-person reality: the person as such (not merely their will, or their mind, or their emotion) is the subject of covenantal commitment.
- Anchor verses: 2Ki 23:3
- Finding type: SPIRIT_SOUL_BODY

**Q&A-043 | T2.2.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.2 — Soul-Level Location
- Prompt: 3 — If evidence is silent on soul-level location, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is not silent — 2Ki 23:3 and the soul co-occurrence data (19 shared verses) explicitly confirm soul-level engagement.

**Q&A-044 | T2.3.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.3 — Heart
- Prompt: 1 — Does the verse evidence locate this characteristic in the heart?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — emphatically and with theological centrality. The heart is the explicitly named constitutional site of covenant in multiple key texts: (1) Jer 31:33 / Heb 8:10: "I will write my law on their hearts" / "I will put my laws into their minds and write them on their hearts" (OBS-034-040, OBS-034-059). The new covenant's defining act is heart-inscription. (2) 2Ki 23:3: covenant made "with all his heart and all his soul" (OBS-034-047). (3) Psa 78:37: "their heart was not steadfast toward him; they were not faithful to his covenant" — covenant faithfulness is a heart quality; faithlessness is heart-instability. (4) Heb 10:16 (from G1242 verse set): "I will put my laws on their hearts and write them on their minds." R183 (heart) has 14 shared co-occurrence verses with covenant (OBS-034-030). Heart is the primary constitutional location of covenant in the inner-being vocabulary of Scripture.
- Anchor verses: Jer 31:33, Heb 8:10, 2Ki 23:3, Psa 78:37
- Finding type: SPIRIT_SOUL_BODY

**Q&A-045 | T2.3.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.3 — Heart
- Prompt: 2 — What does heart-location reveal about the heart's integrating function that this characteristic engages?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The heart-location evidence reveals that covenant engages all four aspects of the heart's integrating function: (1) Willing: "with all his heart" covenant-making (2Ki 23:3) — the heart as the seat of volitional commitment. (2) Knowing: "they shall all know me" follows from God writing on the heart (Jer 31:34) — heart-inscription produces knowing. The heart is the seat of covenantal knowing of God. (3) Moral awareness: Psa 78:37 — "their heart was not steadfast... they were not faithful" — covenant faithlessness is a heart-integrity failure; the heart as moral evaluation centre assesses covenant obligation. (4) Feeling/affective: Psa 25:14 direction — "the friendship of the Lord is for those who fear him, and he makes known to them his covenant" — the relational-affective dimension of knowing God's covenant is a heart reality. All four aspects of the heart's integrating function are engaged: covenant writes on the knowing heart, calls the willing heart, evaluates the moral-faithful heart, and is experienced in the affective-relational heart.
- Anchor verses: Jer 31:33-34, 2Ki 23:3, Psa 78:37
- Finding type: SPIRIT_SOUL_BODY

**Q&A-046 | T2.3.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.3 — Heart
- Prompt: 3 — If evidence is silent on heart-location, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is not silent — heart is the primary and most explicitly named constitutional location of covenant in the data. Q&A-044 and Q&A-045 are substantive.

**Q&A-047 | T2.4.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.4 — Mind
- Prompt: 1 — Does the verse evidence locate this characteristic in the mind?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — explicitly in the new covenant texts. Heb 8:10: "I will put my laws into their minds, and write them on their hearts" (OBS-034-059). The mind (dianoia) is the first named location in the Heb 8:10 formulation — the law is put into the mind before it is written on the heart (or simultaneously, depending on the reading). Heb 10:16: "I will put my laws on their hearts and write them on their minds" — here the order is reversed, confirming that the pairing of heart and mind as co-locations of covenantal law-writing is the substance, not the sequence. 2 Cor 3:14: "their minds were hardened" — the mind as the site of cognitive blockage to the covenant's content (OBS-034-072). R112 (mind) has 39 shared co-occurrence verses — the strongest single co-occurrence signal in the registry (OBS-034-029). Mind-location for covenant is well-evidenced.
- Anchor verses: Heb 8:10, Heb 10:16, 2 Cor 3:14
- Finding type: SPIRIT_SOUL_BODY

**Q&A-048 | T2.4.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.4 — Mind
- Prompt: 2 — What does mind-location reveal about the mind's function that this characteristic engages?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Mind-location engages two distinct aspects of the mind's function: (1) Reception and inscription: Heb 8:10 / 10:16 — the mind receives the inscribed law of the new covenant. The mind is not merely the organ of intellectual processing but the constitutional site where God places his covenant content. This is not understanding in the sense of cognitive effort but reception in the sense of constitutional change — the mind becomes the location in which covenantal truth is resident. (2) Hardening and blockage: 2 Cor 3:14 — the mind can be hardened against the covenant's content. The veil over the mind when reading the old covenant is a cognitive-constitutional blockage. The mind's function of discernment and understanding is impaired by this hardening; only Christ removes it (2 Cor 3:16). Together: the mind is the site of both covenantal inscription (when open and transformed) and covenantal blindness (when hardened). Covenant engages the mind's discerning and receiving functions in opposite directions depending on the person's covenantal standing.
- Anchor verses: Heb 8:10, 2 Cor 3:14, 2 Cor 3:16
- Finding type: SPIRIT_SOUL_BODY

**Q&A-049 | T2.4.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.4 — Mind
- Prompt: 3 — If evidence is silent on mind-location, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is not silent — mind is explicitly named in Heb 8:10 and 10:16 as a covenant location, and 2 Cor 3:14 engages the mind's hardening. Q&A-047 and Q&A-048 are substantive.

**Q&A-050 | T2.5.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.5 — Other Soul Subsets
- Prompt: 1 — Does the verse evidence surface any soul-level location beyond heart and mind for this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the mouth and lips surface as a soul-level expressive location for covenant. Isa 59:21: "my words that I have put in your mouth... shall not depart out of your mouth, or out of the mouth of your offspring" (OBS-034-040 direction, Group 765-003). The covenant's content — God's words — is located in the mouth as well as the heart. This is not merely speech production but constitutional location: the mouth as the expressive organ of the covenantal word. Additionally, the oath vocabulary (H0423, H7650 — OBS-034-007, OBS-034-017) implicates the mouth as the organ through which the covenant is formally made — the spoken oath is the performative covenant act (Q&A-024). Psa 50:16 (Group 765-002): "what right have you to recite my statutes or take my covenant on your lips?" — the lips as the location of covenantal declaration, with moral integrity as the condition of its validity.
- Anchor verses: Isa 59:21, Psa 50:16
- Finding type: SPIRIT_SOUL_BODY

**Q&A-051 | T2.5.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.5 — Other Soul Subsets
- Prompt: 2 — If so, what is that location and what does it reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The mouth/lips as a soul-level location reveals two things: (1) Covenant is constituted through speech — the spoken oath is what brings the covenant into being (Q&A-024); the mouth is not merely expressive but constitutive. When God puts his words in the mouth (Isa 59:21), the covenant content is carried forward through speech across generations ("shall not depart out of your mouth, or out of the mouth of your offspring"). (2) The mouth's use of covenant vocabulary carries moral weight — taking the covenant "on your lips" (Psa 50:16) without inner integrity is an act of hypocrisy that God explicitly challenges. The mouth as covenant-location is not neutral; it is morally evaluated. The soul-level expressive organ (mouth/lips) is thus the site of covenant's public expression and also the site of its possible falsification.
- Anchor verses: Isa 59:21, Psa 50:16
- Finding type: SPIRIT_SOUL_BODY

**Q&A-052 | T2.5.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.5 — Other Soul Subsets
- Prompt: 3 — If evidence is silent, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence surfaces the mouth/lips as an additional soul-level location. Q&A-050 and Q&A-051 address this.

**Q&A-053 | T2.6.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.6 — Body — Significance
- Prompt: 1 — Does the verse evidence link this characteristic to a specific body part?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — two body-part links are evidenced. (1) Blood: the covenant is sealed and constituted through blood in multiple traditions — "the blood of the covenant" (Exo 24:8, echoed in Mat 26:28, Mar 14:24, Heb 9:20, Heb 13:20 — OBS-034-058, OBS-034-074). The blood of sacrifice (OT) and of Christ (NT) is the physical substance through which the covenant is enacted and confirmed. Blood is the bodily medium of covenant-making and covenant-sealing. (2) Circumcision: Act 7:8 — "he gave him the covenant of circumcision" — circumcision as the bodily sign of the Abrahamic covenant. The covenant is physically inscribed on the male body as its permanent sign. Both blood and circumcision are body-part links that carry distinct significances — blood as the sealing substance, circumcision as the identifying mark.
- Anchor verses: Exo 24:8, Mat 26:28, Act 7:8, Heb 13:20
- Finding type: SOMATIC_EVIDENCE

**Q&A-054 | T2.6.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.6 — Body — Significance
- Prompt: 2 — What is Scripture doing by making that link — is it emphatic, functional, expressive, indicative, or mediating?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The two body-part links serve different scriptural functions: (1) Blood as mediating: the blood of the covenant is the covenant's constitutive medium — it does not merely represent the covenant but enacts and seals it. "The blood of the covenant that God commanded for you" (Heb 9:20). The blood mediates between the parties: it is shed, sprinkled on the people (Exo 24:8) or on the altar (Lev context), creating a bond through shared life-substance. In the NT, Christ's blood is the mediation of the new covenant — it enacts the covenant by providing the death of the testator (Heb 9:16–17 — OBS-034-069). Blood's function is mediating: constituting the covenant bond through bodily sacrifice. (2) Circumcision as indicative/expressive: the sign of circumcision on the body indicates covenant membership and expresses bodily belonging to the covenant community. It does not constitute the covenant (which is God's prior promise — Gal 3:17 context) but marks the body as belonging to the covenant people. Circumcision is the bodily inscription of covenantal identity. Function: indicative and expressive. Together, blood (mediating) and circumcision (indicative) show that covenant has two distinct somatic modes: constituting-through-sacrifice and marking-through-sign.
- Anchor verses: Heb 9:20, Act 7:8, Exo 24:8
- Finding type: SOMATIC_EVIDENCE

**Q&A-055 | T2.6.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.6 — Body — Significance
- Prompt: 3 — If no body-part link is evidenced, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Body-part links are evidenced — blood and circumcision. Q&A-053 and Q&A-054 address these.

**Q&A-056 | T2.7.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.7 — Body — Direction
- Prompt: 1 — Where a body-characteristic link exists, which direction does it run?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Both directions are present, operating differently for each body-part link. (1) Blood — bidirectional: the blood is shed from the body outward (soul expresses through body in the act of sacrifice — the inner commitment of the covenant-maker is enacted through the body's blood); and the blood acts back upon the inner person constitutively (the covenant sealed in blood creates a bond that changes the inner standing and identity of those under it — Heb 10:29 mentions "the blood of the covenant by which he was sanctified" — OBS-034-070). The inner → body direction (sacrifice/outpouring) and the body → inner direction (sanctification/constituting) are both present. (2) Circumcision — inner → body: the inner covenant commitment (received from God, entered by the human) is expressed and inscribed outwardly on the body. The primary direction is soul → body: the covenantal identity is inscribed on the body as its sign. There is no clear body → soul direction for circumcision in the data (Paul explicitly decouples the external sign from inner significance in Rom 2:28–29, though that passage is not in the verse set).
- Anchor verses: Heb 10:29, Act 7:8, Exo 24:8
- Finding type: SOMATIC_EVIDENCE

**Q&A-057 | T2.7.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.7 — Body — Direction
- Prompt: 2 — What is the consequence of that directionality for understanding the characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The bidirectional blood-covenant relationship reveals that covenant is not merely inner and invisible — it moves through the body and back again, using physical substance as its medium. The consequence: covenant is constitutionally somatic in its enacted form; it cannot be reduced to a purely internal or invisible inner-being reality. The body participates in covenant both as the site of covenant's expression (sacrifice, circumcision, spoken oath) and as the medium through which covenant is constituted and marked. This has implications for understanding the new covenant's sacramental forms (Eucharist, baptism): both are bodily acts that carry covenant significance — they are not merely symbolic but participate in the covenant's constituting and marking logic that runs through the body. The body is not external to covenant but is the medium through which covenant is enacted, marked, and sustained in time.
- Anchor verses: Mat 26:28, Act 7:8, Heb 10:29
- Finding type: SOMATIC_EVIDENCE

**Q&A-058 | T2.7.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.7 — Body — Direction
- Prompt: 3 — If no body-characteristic link is evidenced, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Body-characteristic links are evidenced and directional. Q&A-056 and Q&A-057 address these.

**Q&A-059 | T2.8.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.8 — Body — Deposit
- Prompt: 1 — Does sustained operation of this characteristic leave a constitutional deposit in the body or its design — including DNA or generational consequence?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The evidence provides one clear case of generational/constitutional deposit and one gap. (1) Circumcision as generational deposit: the covenant sign of circumcision is imposed on male descendants through the generations — "in your offspring shall all the families of the earth be blessed" (Act 3:25). The covenant is carried generationally through physical descent and the bodily sign inscribed on each generation. This is the clearest case of a constitutional deposit with generational consequence: covenant membership is inscribed on the body and transmitted across generations through descent and circumcision. (2) The new covenant's deposit: Isa 59:21 — "my words... shall not depart out of your mouth, or out of the mouth of your offspring, or out of the mouth of your children's offspring." The new covenant's content (God's words) is transmitted generationally through the mouth — a form of constitutional deposit that passes through speech across generations. Whether this constitutes a bodily deposit in the strict biological/DNA sense is not stated. Gap: the verse evidence does not address whether the new covenant's inner constitutional transformation (law on the heart) leaves a biological or genetic deposit. This is beyond what the data can answer.
- Anchor verses: Act 3:25, Act 7:8, Isa 59:21
- Finding type: SOMATIC_EVIDENCE
- Stage 2b note: T2.8 finding — generational deposit evidenced through circumcision and generational word-transmission. No biological/DNA deposit explicitly stated. T5.7 dependency noted.

**Q&A-060 | T2.8.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.8 — Body — Deposit
- Prompt: 2 — What evidence supports or contradicts this?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: Supporting: Act 7:8 (covenant of circumcision as generational bodily sign), Act 3:25 ("in your offspring" — covenant blessing transmitted through descent), Isa 59:21 (covenantal word transmitted through generations of offspring's mouths). All three show generational transmission mechanisms for covenant content. Contradicting/complicating: the NT trajectory (Paul's argument in Gal 3 and Rom 2 context) suggests that the covenant's essential deposit is not biological but spiritual — circumcision of the heart, not of the flesh, is the true mark. The bodily sign (circumcision) is relativised in the new covenant administration. This tension — OT covenant carried through bodily descent and circumcision; NT covenant carried through Spirit and faith — is a structural finding. The deposit changes constitutional mode across the covenantal trajectory.
- Anchor verses: Act 7:8, Gal 3:17, Isa 59:21
- Finding type: SOMATIC_EVIDENCE

**Q&A-061 | T2.8.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.8 — Body — Deposit
- Prompt: 3 — If evidence is silent, note this explicitly. This finding feeds directly into T5.7.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is not silent — generational deposit is evidenced through circumcision and mouth-transmission (Q&A-059, Q&A-060). T5.7 will address whether the body deposit generates a T5.7-specific finding.

**Q&A-062 | T2.9.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.9 — Origin and Source
- Prompt: 1 — Where does this characteristic originate constitutionally — generated from within, received from outside, bestowed by God, or carried generationally?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The verse evidence shows multiple constitutional origins operating in different covenantal modes: (1) Bestowed by God — primary: all major covenant traditions in the data are initiated by God. God "cuts" the covenant (3304-001 — OBS-034-046), God swears by himself (3308-001 — OBS-034-052), God establishes the Noahic covenant unilaterally (765-001 — OBS-034-038), God declares the new covenant (Jer 31:31 — OBS-034-040). In the new covenant specifically: God writes the law on the heart (Heb 8:10) and administers through the Spirit (2 Cor 3:6) — the covenant is produced in the inner person by divine action, not generated from within the person. (2) Carried generationally — secondary: circumcision (Act 7:8), covenant promises to offspring (Act 3:25), generational word transmission (Isa 59:21) all show covenantal participation being transmitted across generations. (3) Received from outside through volitional entry — tertiary: the human person enters covenant through an act of consent and commitment (Neh 10:29 — OBS-034-035). This is reception, not generation.
- Anchor verses: Gen 9:15, Heb 8:10, Neh 10:29, Act 7:8
- Finding type: THEOLOGICAL_NOTE

**Q&A-063 | T2.9.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.9 — Origin and Source
- Prompt: 2 — What does the evidence reveal about whether the origin is singular or multiple?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: The origin is multiple — three constitutional sources operate, and they are not mutually exclusive. God's initiative (bestowed), generational transmission (carried), and human reception/entry (received through choice) are all present in the data and operate simultaneously for most covenant participants: they are born into the covenant community (generational), they enter consciously through affirmation (reception), and the covenant itself is God's prior initiative that makes both possible. The new covenant adds a fourth mode: constitutional generation from within the person by the Spirit's action (Jer 31:33; 2 Cor 3:6) — the covenant is produced within the person by God's own interior work, not merely entered from outside. The multiplicity of origins is not a confusion but a structural reality: covenant participates in the divine, the generational, the volitional, and the constitutive-transforming simultaneously.
- Anchor verses: Gen 9:15, Act 7:8, Neh 10:29, Jer 31:33
- Finding type: THEOLOGICAL_NOTE

**Q&A-064 | T2.9.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.9 — Origin and Source
- Prompt: 3 — Does the origin of this characteristic change across different contexts evidenced in Scripture?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the origin changes across the covenantal trajectory, which is the most analytically significant finding of T2.9. (1) Noahic and patriarchal covenants: origin is purely God's initiative — unilateral divine bestowal with no human precondition (765-001 — OBS-034-038). (2) Mosaic/Sinai covenant: God initiates but the origin also requires human consent and entry — bilateral, with human volitional reception as a constitutive element (765-002 — OBS-034-039). (3) Davidic covenant: God initiates, but the covenant is received by and carried in the Davidic line — generational transmission becomes a primary constitutional mode (OBS-034-041). (4) New covenant: the origin shifts decisively toward God's interior action within the person — God writes on the heart (Heb 8:10), sends the Spirit (2 Cor 3:6), produces knowing from within (Jer 31:34). The locus of origin moves from external divine declaration to internal divine operation. This developmental shift in origin — from external bestowal (OT) to internal generation by Spirit (NT) — is the constitutional-level expression of the transformation trajectory identified in DIM-34-001 and confirmed throughout Stage 2a.
- Anchor verses: Gen 9:15, Exo 19:5, Heb 8:10, 2 Cor 3:6
- Finding type: THEOLOGICAL_NOTE

**Q&A-065 | T2.10.1**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.10 — Constitutional Movement
- Prompt: 1 — Does this characteristic move across constitutional levels — from spirit to soul, from soul to body, or across boundaries in other directions?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — covenant shows constitutional movement across multiple levels. (1) Divine Spirit → human inner person: 2 Cor 3:6 (Spirit administers the new covenant — OBS-034-061); Isa 59:21 (God's Spirit placed upon the person, God's words placed in the mouth). The new covenant moves from the divine Spirit into the constitutional core of the human person. (2) Inner → somatic (soul → body): the inner covenantal commitment is expressed and enacted through bodily acts — oath (spoken), cutting ritual (bodily enactment — OBS-034-044), blood-shedding (sacrifice), circumcision (bodily inscription — OBS-034-053). The inner disposition moves outward into somatic expression. (3) Somatic → inner (body → soul): the blood of the covenant acts back upon the inner person constitutively — "by which he was sanctified" (Heb 10:29 — OBS-034-070); the cup of the new covenant received bodily (Lk 22:20) constitutes the covenantal bond. The body participates in covenant's constituting work, feeding back into the inner person. (4) Inner → word/mouth → generational transmission (OBS-034-051 direction, Isa 59:21): covenantal content moves from the inner person outward through the mouth and forward through generations.
- Anchor verses: 2 Cor 3:6, Isa 59:21, Heb 10:29, Exo 24:8
- Finding type: SPIRIT_SOUL_BODY

**Q&A-066 | T2.10.2**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.10 — Constitutional Movement
- Prompt: 2 — What does the evidence reveal about the sequence or pattern of that movement?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: A discernible pattern emerges across the evidence. For OT covenant: the movement runs outer → inner → outer: God declares the covenant externally (word, law on stone) → calls for inner reception and commitment (heart and soul) → inner commitment is enacted outwardly (oath, sacrifice, bodily circumcision). The inner person is the receptive and responsive site between God's external word and the body's covenant-expression. For new covenant: the movement runs inner → inner → outer: God acts internally (Spirit on the person, law written on heart — Heb 8:10) → the inner person is constituted anew in their knowing and willing → this inner renewal expresses outwardly through faithfulness and speech (Isa 59:21). The shift from OT to NT covenantal movement is structurally significant: from outer-to-inner (law imposed on the person from outside) to inner-to-inner-to-outer (Spirit working from within outward). This is the constitutional-level mechanism of the transformation trajectory — DIM-34-001 confirmed at the movement level.
- Anchor verses: Heb 8:10, 2 Cor 3:6, Isa 59:21, Exo 24:8
- Finding type: SPIRIT_SOUL_BODY

**Q&A-067 | T2.10.3**
- Tier: T2 — Constitutional Location and Boundaries
- Component: T2.10 — Constitutional Movement
- Prompt: 3 — If no constitutional movement is evidenced, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Constitutional movement is extensively evidenced. Q&A-065 and Q&A-066 address this comprehensively.

TIER T2 COMPLETE — Constitutional Location and Boundaries
Date: 2026-05-01
Prompts: 31 total. A: 19. P: 4. S: 0. N: 8.
New findings: 18. SD pointers raised: 0.


#### Tier 3 — The Inner Faculties — 33 prompts

**Q&A-068 | T3.1.1**
- Tier: T3 — The Inner Faculties
- Component: T3.1 — Perception
- Prompt: 1 — Does this characteristic engage the perceptive faculty — inner senses including hearing, sight, taste, touch, smell, and spiritual discernment — and if so, which and how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — hearing is the perceptive faculty most centrally engaged. Exo 19:5: "if you will indeed obey my voice and keep my covenant" — covenantal reception requires hearing God's voice (OBS-034-030; R213 listen, 13 shared verses). Jer 11:8: "they did not obey or incline their ear" — covenant breach is framed as a failure of inner hearing. Heb 8:9: "they did not continue in my covenant" follows from "I took them by the hand to bring them out of Egypt" — the context of covenant departure is failure to attend. Deu 7:9: "those who love him and keep his commandments" — commanded hearing and keeping go together. The inner ear — the faculty of attentive receptive listening — is structurally connected to covenant-keeping. Spiritual discernment also appears: Psa 25:14: "the friendship of the Lord is for those who fear him, and he makes known to them his covenant" — discernment of God's covenant is given to those who fear him. The perceptive faculty operates as the gateway to covenant engagement.
- Anchor verses: Exo 19:5, Jer 11:8, Psa 25:14
- Finding type: MEANING_OBSERVATION

**Q&A-069 | T3.1.2**
- Tier: T3 — The Inner Faculties
- Component: T3.1 — Perception
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair the perceptive faculty?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant engagement enables and deepens perception; covenant breach impairs it. For enabling: Psa 25:14 — God makes known his covenant to those who fear him; the covenant-keeping person receives deeper discernment of God's reality and purposes. The new covenant explicitly promises restored perception: "they shall all know me" (Jer 31:34) — the new covenant produces a knowing that is itself a form of deep inner perception of God. For impairing: 2 Cor 3:14 — "their minds were hardened... a veil remains" (OBS-034-072). The old covenant read without Christ impairs cognitive-perceptive engagement; the veil blocks what was meant to be seen and known. Covenant-breaking also impairs — Jer 11:8 frames covenant breach as failure to incline the ear: the breaking of the covenantal relationship is accompanied by a closing of the perceptive faculty.
- Anchor verses: Psa 25:14, Jer 31:34, 2 Cor 3:14
- Finding type: MEANING_OBSERVATION

**Q&A-070 | T3.1.3**
- Tier: T3 — The Inner Faculties
- Component: T3.1 — Perception
- Prompt: 3 — What does the pattern of engagement or non-engagement with perception reveal about the nature of this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals that covenant is not a self-activating inner-being reality — it depends on an open perceptive faculty as its gateway. Covenant cannot be received by the person who will not hear; it cannot transform the person whose perceptive faculty is veiled or hardened. Conversely, the new covenant's promise is precisely to restore and enable perception: writing on the heart produces knowing (Jer 31:34), and knowing is a form of heightened inner perception of God. This means covenant and perception have a reciprocal relationship: open perception enables covenant reception; covenant transformation deepens and enlarges perception. The pattern shows that covenant is the structured framework within which the inner perceptive faculty either opens toward God (covenant faithfulness) or closes away from him (covenant breach and hardening).
- Anchor verses: Jer 31:34, 2 Cor 3:14, Psa 25:14
- Finding type: MEANING_OBSERVATION

**Q&A-071 | T3.2.1**
- Tier: T3 — The Inner Faculties
- Component: T3.2 — Cognition
- Prompt: 1 — Does this characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — and more directly than the group landscape suggested (OBS-034-026 noted the absence of a Cognition group; OBS-034-072 and OBS-034-040 supply the evidence). (1) The new covenant explicitly produces cognitive transformation: Jer 31:34 — "they shall all know me, from the least to the greatest." The covenant's primary sustained effect is a knowing of God — a cognitive-relational act of recognition and knowledge at the deepest personal level. (2) Heb 8:10 — "I will put my laws into their minds" — the mind (dianoia) as the seat of covenant-content is a direct cognitive engagement: the law inscribed in the mind produces understanding of God's will. (3) 2 Cor 3:14 — "their minds were hardened" in reading the old covenant (OBS-034-072). Cognition is engaged negatively: the cognitive faculty can be blocked from understanding the covenant's content by hardening. (4) 2 Cor 3:6 — "not of the letter but of the Spirit" — spiritual cognition (Spirit-enabled understanding) is contrasted with mere cognitive processing of the letter. Covenant engages cognition profoundly: it both produces and depends on a particular quality of knowing.
- Anchor verses: Jer 31:34, Heb 8:10, 2 Cor 3:14
- Finding type: MEANING_OBSERVATION

**Q&A-072 | T3.2.2**
- Tier: T3 — The Inner Faculties
- Component: T3.2 — Cognition
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair cognition?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Both enabling/deepening and impairing are evidenced. Enabling/deepening: the new covenant produces the deepest form of knowing — "they shall all know me" (Jer 31:34). This knowing is not mere cognitive information but intimate personal knowledge, generated by God's own interior action (writing on the heart, Spirit-administration). The new covenant enables a quality of cognition that was not available under the old: unmediated knowing of God across all persons, "from the least to the greatest." Impairing: 2 Cor 3:14 — cognitive hardening under the old covenant. When read without Christ, the old covenant produces a veil that impairs the very cognition it should inform. This is a structural impairment — not failure of effort but a covenantal condition that blocks cognitive access. The same covenant (old) that was designed to enable knowing God becomes, through hardening, an obstacle to that knowing.
- Anchor verses: Jer 31:34, 2 Cor 3:14, Heb 8:10
- Finding type: MEANING_OBSERVATION

**Q&A-073 | T3.2.3**
- Tier: T3 — The Inner Faculties
- Component: T3.2 — Cognition
- Prompt: 3 — What does the pattern of engagement with cognition reveal about this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals that cognition is not merely a secondary consequence of covenant but one of its primary targets and products. The new covenant's stated aim is a cognitive one — "they shall all know me." This means that covenant is oriented toward producing a transformed cognitive relationship with God as its telos. The pattern also reveals a fundamental asymmetry between old and new covenant cognitive effects: the old covenant engages cognition but can produce hardening and veil; the new covenant engages cognition and produces knowing by God's own interior action. Cognition, in covenant terms, is not human achievement (study, comprehension) but covenant gift — it is what the covenant produces in the person, not what the person brings to the covenant. This is a structurally important finding: the cognitive dimension of covenant runs from God's action to human knowing, not from human knowing to covenant engagement.
- Anchor verses: Jer 31:34, 2 Cor 3:6, 2 Cor 3:14
- Finding type: THEOLOGICAL_NOTE

**Q&A-074 | T3.3.1**
- Tier: T3 — The Inner Faculties
- Component: T3.3 — Memory
- Prompt: 1 — Does this characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — memory is one of the most structurally prominent inner faculties in the covenant vocabulary, operating in both directions. (1) Divine memory of covenant: Gen 9:15 — "I will remember my covenant" (OBS-034-038); Psa 105:8 — "He remembers his covenant forever"; Psa 106:45 — "For their sake he remembered his covenant"; Lk 1:72 — "to remember his holy covenant" (OBS-034-073). God's active remembering of the covenant is the guarantee of its continuing operation — divine memory is the sustaining mechanism of covenant faithfulness. (2) Human covenant-memory: Deu 4:23 — "Take care, lest you forget the covenant of the Lord your God" (Group 765-002 — command to remember); Deu 8:18 — "remember the Lord your God... that he may confirm his covenant." Human remembering of the covenant is the activating condition for covenant faithfulness — forgetting leads to breach. (3) The covenant as memorial structure: the new covenant Eucharist — "do this in remembrance of me" (1 Cor 11:25 — OBS-034-058). The covenant meal is structured as a memorial act — covenant and memory are architecturally linked through the liturgical practice of remembering.
- Anchor verses: Gen 9:15, Psa 105:8, Lk 1:72, 1 Cor 11:25
- Finding type: MEANING_OBSERVATION

**Q&A-075 | T3.3.2**
- Tier: T3 — The Inner Faculties
- Component: T3.3 — Memory
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair memory?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant structures and disciplines memory — it does not bypass it. (1) Covenant enables and deepens memory in those who maintain it: the covenantal commands to remember (Deu 4:23; 8:18) orient the inner memory faculty toward God's acts and commitments. The covenant creates a framework within which memory is directed and disciplined — festivals, signs (rainbow, circumcision, Sabbath, Eucharist), and written law all serve as memory aids that structure the inner faculty's operation. (2) Covenant breach is associated with forgetting: "Take care, lest you forget the covenant" — the drift from covenant faithfulness begins in the memory faculty's failure to hold covenantal reality. The covenant-breaker is characterised by forgetting God's covenant (2Ki 17:38: "you shall not forget the covenant that I have made with you"). (3) The new covenant does not abolish the memory structure but reorients it: the Eucharistic "do this in remembrance of me" establishes a covenantal memory practice centred on Christ's death rather than Sinai's law-giving. Memory is retained and redirected, not bypassed.
- Anchor verses: Deu 4:23, 1 Cor 11:25, 2Ki 17:38
- Finding type: MEANING_OBSERVATION

**Q&A-076 | T3.3.3**
- Tier: T3 — The Inner Faculties
- Component: T3.3 — Memory
- Prompt: 3 — What does the pattern of engagement with memory reveal about this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals that covenant is constitutively temporal — it extends across time and requires the memory faculty to hold it active. A covenant that is forgotten ceases to function as a relational bond; it requires the active inner work of remembering to remain operative. This makes covenant radically unlike immediate emotional states (which do not require memory to function) — covenant is precisely a temporally extended reality that must be held in memory to be lived in. The pattern also reveals that God's own memory of covenant (divine faithfulness as divine remembering) is the ultimate guarantee against covenant failure — where human memory fails, God's does not. The Eucharistic memorial structure shows that the new covenant institutionalises this temporal-memory requirement: the covenant community is constituted as a remembering community, gathering repeatedly to hold the covenant's founding act in memory.
- Anchor verses: Gen 9:15, Psa 105:8, 1 Cor 11:25
- Finding type: THEOLOGICAL_NOTE

**Q&A-077 | T3.4.1**
- Tier: T3 — The Inner Faculties
- Component: T3.4 — Affect
- Prompt: 1 — Does this characteristic engage the affective faculty — feeling and emotional experience — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — affective engagement is present though secondary in the data relative to volition and cognition. (1) Group 3308-004 (Emotion-Positive: adjuration — H7650 — OBS-034-056): the swearing vocabulary in the context of intense inner longing and love (Song of Songs context). Covenant language can carry intense emotional-affective content when the relationship it structures is one of intimate love. (2) Group 766-003 (Emotion-Negative: covenantal exclusion — OBS-034-060): the inner-being state of those outside the covenants of promise is described as hopeless, alienated, godless — a cluster of negative affective conditions. Being outside the covenant produces inner desolation as an affective reality. (3) Group 3306-002 (Divorce metaphor — OBS-034-043): the prophetic use of divorce for God's covenantal rupture with Israel carries the full emotional weight of marital betrayal — covenant severance is experienced as devastating inner loss. (4) Lk 1:72 — "to remember his holy covenant" in the context of showing mercy — covenant remembrance produces an affective response of praise and wonder in Zechariah's song.
- Anchor verses: Eph 2:12, Song of Songs context (3308-004), Lk 1:72
- Finding type: MEANING_OBSERVATION

**Q&A-078 | T3.4.2**
- Tier: T3 — The Inner Faculties
- Component: T3.4 — Affect
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair affect?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The evidence suggests that covenant structures the context within which affect operates rather than producing or impairing it directly. (1) Enabling: covenant inclusion enables hope and security (Eph 2:12 reversed — being included produces hope that exclusion destroys — OBS-034-060); the new covenant enables a knowing of God (Jer 31:34) that carries affective depth — knowing a person involves emotional engagement. The covenant of hesed (love) names the affective quality of the relationship it structures. (2) The adjuration register (3308-004 — OBS-034-056) shows that covenant language is taken up into the register of intense emotional longing — covenant is not affectively flat but can carry the whole emotional range of intimate relationship. Gap: the data does not directly address whether covenant enables or deepens affect as a distinct inner-being operation. The clearest evidence is that covenant shapes the conditions within which affect is experienced (inclusion → hope; exclusion → desolation; breach → grief), but whether covenant produces affect independent of these conditional states is not directly stated.
- Anchor verses: Eph 2:12, 3308-004 context, Jer 31:34
- Finding type: MEANING_OBSERVATION

**Q&A-079 | T3.4.3**
- Tier: T3 — The Inner Faculties
- Component: T3.4 — Affect
- Prompt: 3 — What does the pattern of engagement with affect reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: The pattern reveals that covenant is not an affectively neutral legal construct but one that generates and shapes deep emotional experience. The relational character of covenant means that the affective register of the relationship — love, longing, grief, desolation, hope — is always present as the emotional dimension of the covenantal bond. Covenant does not operate in the inner person purely as obligation; it operates in the full register of relational experience, including its affective dimensions. The divorce metaphor (OBS-034-043), the adjuration-in-longing register (OBS-034-056), and the covenantal-exclusion desolation (OBS-034-060) together show that covenant's full inner-being operation cannot be captured without attention to the affective dimension. This is consistent with the hesed-covenant nexus (SP-034-003) — the love that holds the covenant is not dispassionate obligation but affectively rich loyal commitment.
- Anchor verses: 3306-002 context, Eph 2:12, 3308-004 context
- Finding type: MEANING_OBSERVATION

**Q&A-080 | T3.5.1**
- Tier: T3 — The Inner Faculties
- Component: T3.5 — Creativity
- Prompt: 1 — Does this characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how?
- Disposition: NOT ANSWERED
- Status tag: S
- Notation: Gap identified
- Answer: The Stage 2a observations do not contain evidence directly engaging the creative/imaginative faculty in relation to covenant. The data does not address imagination or origination as inner-being faculties engaged by covenant. Noting the silence explicitly. This does not require Stage 2a reopening — covenant is primarily a juridical-relational category and its engagement with the creative faculty is not expected to be prominent. However, the absence should be recorded as a gap rather than assumed to be non-applicable.
- Stage 2b note: Stage 2a does not address this. The gap is inherent to the data, not a reading oversight. Not proceeding to Stage 2a reopening — the absence is plausible given covenant's primary categories (relational, volitional, moral). Recording as S.

**Q&A-081 | T3.5.2**
- Tier: T3 — The Inner Faculties
- Component: T3.5 — Creativity
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair creativity?
- Disposition: NOT ANSWERED
- Status tag: S
- Notation: Gap identified
- Answer: Not evidenced in Stage 2a observations. The data is silent on creativity as an inner faculty engaged by covenant. Recording as S. Same rationale as T3.5.1.

**Q&A-082 | T3.5.3**
- Tier: T3 — The Inner Faculties
- Component: T3.5 — Creativity
- Prompt: 3 — What does the pattern of engagement or non-engagement with creativity reveal?
- Disposition: NOT ANSWERED
- Status tag: S
- Notation: Gap identified
- Answer: The non-engagement with creativity as an inner faculty reveals that covenant operates primarily in the juridical-relational, moral, and cognitive registers rather than the imaginative-creative register. Covenant is a structured bond, not a creative act of inner origination. The absence is itself a finding: covenant does not primarily engage the creative faculty in the inner person — it structures, commits, and transforms, but its engagement is with the will, the moral character, the cognitive faculty, and the memory, not with imagination and origination. Recording as S because the data is silent, even though the gap is analytically interpretable.

**Q&A-083 | T3.6.1**
- Tier: T3 — The Inner Faculties
- Component: T3.6 — Volition
- Prompt: 1 — Does this characteristic engage the volitional faculty — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — volition is one of the most extensively evidenced faculty engagements in the covenant vocabulary, second only to the heart-mind complex. (1) Covenant entry is a volitional act: Neh 10:29 — the community "joins" and "enters into" the covenant (OBS-034-035). Neh 9:38 — "we make a firm covenant" (OBS-034-037). The covenant-making act is the volitional commitment of the inner person. (2) The Sinai covenant is structured around bilateral volitional obligation: Exo 19:5 — "if you will indeed obey my voice" — the covenant condition is framed as volitional compliance (OBS-034-039). (3) Group 765-002 (76 relevant verses, Volition) is the largest group in the registry — the Sinai/Mosaic covenant is comprehensively Volition-dimensioned, reflecting that this covenant primarily calls for human volitional obedience. (4) The all-heart covenant-making (3304-002 — OBS-034-047) — "with all his heart" — represents total volitional mobilisation. (5) Prohibited covenant (3304-003 — OBS-034-048) is volitionally framed: making covenant with false parties is a volitional misdirection that must be avoided by deliberate volitional choice.
- Anchor verses: Neh 10:29, Exo 19:5, 2Ki 23:3
- Finding type: MEANING_OBSERVATION

**Q&A-084 | T3.6.2**
- Tier: T3 — The Inner Faculties
- Component: T3.6 — Volition
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair volition?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence shows both enabling and bypass, in different covenantal modes. Enabling: the Sinai covenant engages and calls for volition — the bilateral covenant structure requires human volitional response. Covenant gives the person something to commit to, a concrete object for volitional commitment. The moral weight of covenant (oath/curse structure — OBS-034-007) makes the volitional act serious and binding. Bypass (in a specific sense): the new covenant does not wait for the person's volitional transformation but produces it — God writes the law on the heart (Jer 31:33) and administers through the Spirit (2 Cor 3:6). This is not bypassing volition in the sense of overriding it, but operating at a constitutional depth that transforms the volitional faculty from within rather than calling for its exercise from without. The new covenant produces willingness rather than demanding it — "I will be their God and they shall be my people" is a relational promise, not a conditional demand. Gal 4:24 (OBS-034-071): the Sinai covenant produces children for bondage — constrained volition; the new covenant produces free children — liberated volition. The new covenant thus enables and liberates volition at a deeper constitutional level than the old.
- Anchor verses: Exo 19:5, Jer 31:33, Gal 4:24
- Finding type: THEOLOGICAL_NOTE

**Q&A-085 | T3.6.3**
- Tier: T3 — The Inner Faculties
- Component: T3.6 — Volition
- Prompt: 3 — What does the pattern of engagement with volition reveal about this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals a developmental trajectory in covenant's engagement with volition. The old covenant calls for volition as its primary human requirement; the new covenant transforms volition as its primary human gift. Both engagements are profound, but they operate in opposite directions: the old covenant requires the person to bring their will to the covenant; the new covenant brings a transformed will to the person. This pattern reveals that covenant is the structuring reality within which the theological question of human will and divine grace is most sharply focused in Scripture. Covenant is the framework that makes the will-and-grace question visible — and the covenant trajectory from old to new is the narrative resolution of that question: not the abolition of human volition but its liberation through the Spirit's transforming work.
- Anchor verses: Exo 19:5, Jer 31:33, Gal 4:24, 2 Cor 3:6
- Finding type: THEOLOGICAL_NOTE

**Q&A-086 | T3.7.1**
- Tier: T3 — The Inner Faculties
- Component: T3.7 — Agency
- Prompt: 1 — Does this characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — agency is engaged on both sides of the covenant relationship, asymmetrically. (1) Divine agency: God is consistently the primary covenant-agent — he initiates (karat berit — OBS-034-046), he swears (OBS-034-052), he remembers and acts on covenant (OBS-034-038), he writes on the heart (OBS-034-040), he administers through the Spirit (OBS-034-061). Divine agency in covenant is unconditional and foundational — God's covenant-agency is the basis on which the covenant exists at all. (2) Human agency: covenant-entry is a human agency act — the person joins, commits, makes the oath (Neh 10:29 — OBS-034-035). The bilateral Sinai covenant calls for sustained human agency in obedience-keeping. Prohibited covenant (3304-003 — OBS-034-048) names the exercise of human agency in the wrong direction. (3) The new covenant shifts the agency dynamic: God acts within the person to produce the conditions of response — the human is more receiver than initiator in the new covenant's primary mode. Human agency remains but is now derivative of and enabled by prior divine agency within.
- Anchor verses: Gen 9:15, Neh 10:29, Jer 31:33
- Finding type: MEANING_OBSERVATION

**Q&A-087 | T3.7.2**
- Tier: T3 — The Inner Faculties
- Component: T3.7 — Agency
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair agency?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant both enables and reorders agency. Enabling: covenant gives the person a covenantal framework within which to act with directed purpose — the covenant establishes what the person is called to do (the covenantal obligations) and empowers them to act within that structure. The new covenant specifically enables agency by liberating it from bondage: Gal 4:24-25 (OBS-034-071) — the new covenant produces free children rather than slaves; freed from the constraint of mere letter-keeping, the person exercises genuine moral agency under the Spirit. Reordering: the new covenant reorders the priority of agency — God's agency within (Spirit acting) comes first, enabling human agency as responsive rather than self-originating. This does not impair human agency but subordinates it to divine agency in a way that produces its fullest expression. It does not bypass agency but regrounds it.
- Anchor verses: Gal 4:24, 2 Cor 3:6, Jer 31:33
- Finding type: THEOLOGICAL_NOTE

**Q&A-088 | T3.7.3**
- Tier: T3 — The Inner Faculties
- Component: T3.7 — Agency
- Prompt: 3 — What does the pattern of engagement with agency reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: The pattern reveals that covenant is always an agency-involving reality — it is never passive or automatic in its human dimension. Even the new covenant, which is constituted by divine initiative and Spirit-agency, calls for human responsive agency: entry (Neh 10:29 — OBS-034-035), keeping (the moral-character mode of covenant faithfulness — OBS-034-053), and transmission (Isa 59:21 — the covenant word carried forward through the mouth across generations — OBS-034-051). Covenant does not produce passive recipients but active participants. The asymmetry is structural: divine agency first, human agency responsive — not because human agency is diminished but because covenant is a relationship, and in this relationship God is always the initiating party.
- Anchor verses: Neh 10:29, Isa 59:21, 2 Cor 3:6
- Finding type: MEANING_OBSERVATION

**Q&A-089 | T3.8.1**
- Tier: T3 — The Inner Faculties
- Component: T3.8 — Moral Evaluation
- Prompt: 1 — Does this characteristic engage the moral evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — moral evaluation is deeply engaged by covenant. (1) Covenant defines the moral standard against which inner fidelity is assessed: the covenant's terms (law, commandments, statutes) provide the content of moral evaluation (Deu 7:9 — OBS-034-039; 2Ki 23:3 — OBS-034-047). Living within covenant means living under a defined moral evaluative framework. (2) Covenant breach is a moral failure assessed by the moral evaluation faculty: Dan 9:11 — "we have sinned against him" (OBS-034-036) — Daniel's prayer of confession is a moral self-assessment in covenantal categories. (3) The oath/curse structure (H0423 — OBS-034-007) embeds a moral assessment mechanism in the covenant itself: the covenant includes its own evaluation criterion and sanction for breach. (4) G0802 (asunthetos — OBS-034-057): Paul's taxonomy in Rom 1:31 names covenant-breaking as a moral defect — the moral evaluation faculty of the apostle and of Scripture judges covenant-breaking as character vice.
- Anchor verses: Dan 9:11, Deu 7:9, Rom 1:31
- Finding type: MEANING_OBSERVATION

**Q&A-090 | T3.8.2**
- Tier: T3 — The Inner Faculties
- Component: T3.8 — Moral Evaluation
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair moral evaluation?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant enables and structures moral evaluation; it does not bypass or impair it. (1) Enabling: the covenant provides the moral framework within which the person's actions and character can be assessed — covenant terms are the evaluative standard. Without the covenant's law-content, moral evaluation has no defined reference point in the OT framework. (2) Deepening: the new covenant deepens moral evaluation by internalising the evaluative standard — the law written on the heart (Heb 8:10) means the moral standard is not external to be measured against but internal, shaping moral perception from within. The new covenant person does not merely evaluate their actions against an external law but has the law's evaluative criteria as part of their inner constitution. (3) The covenant's curse-mechanism (alah — OBS-034-007) is the ultimate moral evaluation tool: it activates against the one who has failed the moral assessment built into the covenant oath.
- Anchor verses: Heb 8:10, Dan 9:11, Deu 7:9
- Finding type: THEOLOGICAL_NOTE

**Q&A-091 | T3.8.3**
- Tier: T3 — The Inner Faculties
- Component: T3.8 — Moral Evaluation
- Prompt: 3 — What does the pattern of engagement with moral evaluation reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals that covenant is intrinsically moral — it cannot be separated from moral evaluation because its structure embeds evaluation within it. The covenant oath (with its curse for breach — OBS-034-007) is not merely a relational bond but a morally evaluative structure: the person under covenant is always already under moral assessment relative to the covenant's terms. This means covenant is not a merely relational or emotional reality but a morally accountable one — being in covenant means being accountable to a standard. The new covenant's internalisation of the standard (law on the heart — Heb 8:10) means the moral evaluation faculty itself is transformed: the person evaluates from within a renewed inner standard rather than against an external one. The pattern confirms that the Moral Character dimension (05) is correctly assigned to multiple covenant groups — covenant-keeping is constitutively a moral-character reality.
- Anchor verses: Heb 8:10, Dan 9:11, Deu 7:9, Rom 1:31
- Finding type: THEOLOGICAL_NOTE

**Q&A-092 | T3.9.1**
- Tier: T3 — The Inner Faculties
- Component: T3.9 — Conscience
- Prompt: 1 — Does this characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — conscience is engaged structurally and specifically. (1) Dan 9:11 (OBS-034-036): Daniel's prayer is a conscience-driven confession — "we have sinned against him." The activated covenant curse is experienced consciously as guilt and judgment, and the response is confessional acknowledgment of conscience's testimony. (2) Heb 10:29 (OBS-034-070): "has trampled underfoot the Son of God, and has profaned the blood of the covenant by which he was sanctified, and has outraged the Spirit of grace" — the language describes covenant-profaning as a conscience-level violation; the seriousness of the act is measured by what it has done to the conscience's object (the sanctifying blood). (3) The curse structure (H0423 — OBS-034-007) engages conscience by naming covenant breach as an activation of self-incurred judgment — the person who breaks the covenant must live with the conscience-testimony that they have brought the curse upon themselves. (4) R073 (guilt, 20 shared co-occurrence verses — OBS-034-031): the frequent co-occurrence of guilt vocabulary with covenant vocabulary confirms that conscience-engagement is a regular feature of covenant contexts.
- Anchor verses: Dan 9:11, Heb 10:29
- Finding type: MEANING_OBSERVATION

**Q&A-093 | T3.9.2**
- Tier: T3 — The Inner Faculties
- Component: T3.9 — Conscience
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair conscience?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant deepens and clarifies conscience — it does not bypass or impair it. (1) Deepening: covenant gives conscience a specific and weighty object — the person under covenant is not merely subject to a vague moral awareness but to conscience-testimony regarding specific covenantal obligations. The covenant's clarity (written law, specific obligations, sworn terms) makes conscience's work more precise. (2) The new covenant deepens conscience further by internalising the standard — law written on the heart (Heb 8:10) means conscience operates from within the person's own renewed moral constitution, not merely against an external standard. (3) The guilt co-occurrence data (OBS-034-031) confirms that covenant contexts regularly produce the conscience-awareness of failure — the covenant is the framework within which guilt is named and experienced. (4) The Hebrews argument (Heb 9:9; 10:1-2 context, though outside the verse set) implies that the old covenant's sacrificial system could not fully clear the conscience — the new covenant's superior blood does. This trajectory — old covenant engaging but not fully clearing conscience; new covenant engaging and clearing it — is implied by the data without being directly stated in the programme's verse set.
- Anchor verses: Dan 9:11, Heb 10:29, Heb 8:10
- Finding type: THEOLOGICAL_NOTE

**Q&A-094 | T3.9.3**
- Tier: T3 — The Inner Faculties
- Component: T3.9 — Conscience
- Prompt: 3 — What does the pattern of engagement with conscience reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals that covenant creates the conditions under which conscience functions with maximum clarity and weight. Within covenant, the person knows precisely what they are accountable to (the covenant's terms), has undergone a solemn self-binding (the oath), and carries the knowledge that breach activates the embedded curse. This means conscience within covenant is heightened conscience — not a vague sense of wrongdoing but acute awareness of specific covenantal violation and its consequences. The 20 shared guilt co-occurrence verses (OBS-034-031) confirm this heightened conscience pattern quantitatively. The pattern also reveals that the new covenant's solution to the conscience problem (blood that sanctifies — Heb 10:29 — OBS-034-070) is not the elimination of conscience but the providing of a sufficient atoning answer to conscience's testimony. Covenant both activates and satisfies conscience.
- Anchor verses: Dan 9:11, Heb 10:29, Heb 8:10
- Finding type: THEOLOGICAL_NOTE

**Q&A-095 | T3.10.1**
- Tier: T3 — The Inner Faculties
- Component: T3.10 — Conscientiousness
- Prompt: 1 — Does this characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — conscientiousness is perhaps the most comprehensively engaged of all inner faculties in covenant. Conscientiousness (the integrated response of moral awareness + volition + action) is precisely what covenant-keeping requires and produces. (1) 2Ki 23:3: covenant made "with all his heart and all his soul, to walk after the Lord and to keep his commandments and his testimonies and his statutes" — the full integration of inner commitment (heart/soul) + volitional decision ("to walk") + sustained action ("to keep commandments") is the definition of covenantal conscientiousness. (2) Psa 25:10: "all the paths of the Lord are steadfast love and faithfulness for those who keep his covenant and his testimonies" — covenant-keeping is the integrated practice of moral awareness (knowing the covenant's terms), volition (choosing to keep them), and action (walking in the paths). (3) Group 3308-002 (human oath as binding of inner will and loyalty — OBS-034-053): oath-keeping is conscientious living — the integrated moral-volitional-active maintenance of one's word.
- Anchor verses: 2Ki 23:3, Psa 25:10
- Finding type: MEANING_OBSERVATION

**Q&A-096 | T3.10.2**
- Tier: T3 — The Inner Faculties
- Component: T3.10 — Conscientiousness
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair conscientiousness?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant enables and calls forth conscientiousness — it does not bypass it. The covenant structure provides the specific object, framework, and moral weight that make conscientiousness concrete and actionable. Without covenant, conscientiousness would have a general moral orientation without specific covenantal terms to be conscientious about. With covenant, conscientiousness has a defined content: the covenant's specific obligations. The new covenant deepens conscientiousness further: by internalising the law (Heb 8:10) and freeing the person through the Spirit (Gal 4:24 — OBS-034-071), the new covenant produces conscientiousness as a fruit of inner renewal rather than a demand on unrenewed will. The conscientious person in the new covenant acts from an inner orientation that has been constituted by God's own writing rather than merely instructed by an external code.
- Anchor verses: 2Ki 23:3, Heb 8:10, Gal 4:24
- Finding type: THEOLOGICAL_NOTE

**Q&A-097 | T3.10.3**
- Tier: T3 — The Inner Faculties
- Component: T3.10 — Conscientiousness
- Prompt: 3 — What does the pattern of engagement with conscientiousness reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals that covenant is the primary structuring reality for conscientious inner life in the biblical framework. Conscientiousness — the integrated moral-volitional-active response — finds its most complete and scripturally supported expression within covenant. The formula "with all your heart and all your soul" in covenant contexts (2Ki 23:3, Deu 6:5 context) is a description of total conscientiousness — the whole person responding in integrated moral-volitional-active commitment. The pattern also reveals that conscientiousness is not primarily an autonomous inner virtue but a covenantally structured reality: it is conscientiousness toward the covenant's terms and within the covenant relationship, not conscientiousness in the abstract. This is a significant finding: biblical conscientiousness is inherently covenantally shaped.
- Anchor verses: 2Ki 23:3, Psa 25:10, Heb 8:10
- Finding type: THEOLOGICAL_NOTE

**Q&A-098 | T3.11.1**
- Tier: T3 — The Inner Faculties
- Component: T3.11 — Relational Capacity
- Prompt: 1 — Does this characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — relational capacity is the most fundamentally engaged faculty in covenant, as the characteristic is itself constitutively relational. Covenant is the formal structure of genuine connection between persons — it is not possible to speak of covenant without speaking of relational capacity. (1) The divine-human covenant engages relational capacity at its deepest: "I will be their God, and they shall be my people" (Heb 8:10 — OBS-034-059). This is the covenant formula — a mutual identification of parties in genuine personal connection. (2) The person-to-person covenant (3304-004, 765-005 — OBS-034-042, OBS-034-049): Jonathan-David type covenants, marriage covenants, friendship covenants — all deploy covenant as the formalised structure of relational capacity in the human-to-human register. (3) The new covenant (766-001 through 777-001): God's relational bond through Christ's blood extends to all who enter it, constituting a new relational community — relational capacity at the communal level.
- Anchor verses: Heb 8:10, 2Ki 23:3, Eph 2:12
- Finding type: MEANING_OBSERVATION

**Q&A-099 | T3.11.2**
- Tier: T3 — The Inner Faculties
- Component: T3.11 — Relational Capacity
- Prompt: 2 — Does this characteristic enable, deepen, bypass, or impair relational capacity?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant fundamentally enables and sustains relational capacity — it is the structure that makes sustained, reliable, deepening connection possible. Without covenant, relational connection is vulnerable to dissolution — it has no formal structure to hold it across time and circumstances. With covenant, relational capacity is both protected (the formal bond) and cultivated (the sustained engagement within the bond produces deeper knowing and love). The new covenant specifically deepens relational capacity between God and human: "they shall all know me" (Jer 31:34 — OBS-034-040) names an intimate personal knowing across all persons within the covenant — the relational capacity for knowing God is democratised and deepened simultaneously. Covenant breach impairs relational capacity — the divorce metaphor (OBS-034-043) and covenantal exclusion (OBS-034-060) show that broken or absent covenant produces relational rupture and desolation.
- Anchor verses: Heb 8:10, Jer 31:34, Eph 2:12
- Finding type: THEOLOGICAL_NOTE

**Q&A-100 | T3.11.3**
- Tier: T3 — The Inner Faculties
- Component: T3.11 — Relational Capacity
- Prompt: 3 — What does the pattern of engagement with relational capacity reveal about covenant's nature?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The pattern reveals that covenant is not merely one engagement of relational capacity among others but the constitutional form through which relational capacity is organised and sustained across time. Relational capacity without covenant is vulnerable — episodic, potentially shallow, subject to dissolution. Covenant without relational capacity is empty — a legal form without the living connection it is meant to structure. The pattern shows that covenant is the form of which relational capacity is the content: covenant holds and sustains relational capacity, and relational capacity gives covenant its living inner reality. This reciprocity — covenant as form, relational capacity as content — is the core structural insight of T3.11. It also illuminates why covenant is the primary dimension category of this registry: the Relational Disposition (06) classification is appropriate because covenant's primary inner-being function is to enable, structure, and sustain the relational capacity of the person in their connection to God and others. The pattern of sustained engagement across all covenant traditions confirms that this is not a peripheral function but the constitutional purpose of the characteristic.
- Anchor verses: Heb 8:10, Jer 31:34, Eph 2:12, Gen 9:15
- Finding type: THEOLOGICAL_NOTE

TIER T3 COMPLETE — The Inner Faculties
Date: 2026-05-01
Prompts: 33 total. A: 27. P: 2. S: 3. N: 1.
New findings: 24. SD pointers raised: 0.
S-status prompts: T3.5.1 (creativity engagement), T3.5.2 (creativity enable/impair), T3.5.3 (creativity pattern) — all three are inherent data gaps, not Stage 2a reading oversights. No Stage 2a reopening required.


#### Tier 4 — Relational Interfaces — 24 prompts

**Q&A-101 | T4.1.1**
- Tier: T4 — Relational Interfaces
- Component: T4.1 — Divine Interface — God to Human
- Prompt: 1 — Does the verse evidence show this characteristic operating from God toward the human person — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — and this is the primary directional register of the covenant vocabulary. God's covenant-toward-human is the foundational axis around which the entire registry is organised. The evidence shows it operating in five distinct modes: (1) Establishment — God establishes/institutes the covenant unilaterally: Gen 9:9 ("I establish my covenant with you"), Gen 6:18 — OBS-034-038. (2) Commitment of faithfulness — God maintains the covenant through time: Gen 9:15 ("I will remember my covenant"), Psa 105:8 ("He remembers his covenant forever") — OBS-034-038, Q&A-074. (3) Constitutional inscription — God writes on the human inner person: Heb 8:10 / Jer 31:33 ("I will write my law on their hearts") — OBS-034-040, OBS-034-059. (4) Oath-binding — God swears by himself to guarantee the covenant: Heb 6:13 direction (3308-001 — OBS-034-052). (5) Mediation through Christ — the new covenant is enacted through Christ as mediator: Heb 7:22, 8:6, 9:15, 12:24 (OBS-034-058, OBS-034-069). These five modes span the full range from structural establishment to active inscription to ultimate mediation.
- Anchor verses: Gen 9:15, Heb 8:10, Heb 9:15
- Finding type: THEOLOGICAL_NOTE

**Q&A-102 | T4.1.2**
- Tier: T4 — Relational Interfaces
- Component: T4.1 — Divine Interface — God to Human
- Prompt: 2 — What does the evidence reveal about the basis on which God extends this characteristic — conditional, unconditional, covenantal, or responsive?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence shows a spectrum of conditionality across the covenant traditions, not a single answer. (1) Unconditional: the Noahic covenant (765-001 — OBS-034-038): God commits without human precondition; the covenant is made with all living creatures. The patriarchal covenant (Abraham) is similarly initiated without precondition beyond faith (Act 3:25; Neh 9:8). (2) Bilateral-conditional: the Sinai covenant (765-002 — OBS-034-039): Deu 7:9 — "with those who love him and keep his commandments." God's covenant-faithfulness is stated as responsive to human covenant-keeping. Exo 19:5: "if you will indeed obey my voice and keep my covenant." (3) Covenantal-unconditional in the new covenant: Heb 8:8-10 — God establishes the new covenant unilaterally as a declaration, not a condition. "I will make" — not "if you will make." The new covenant shifts back toward unconditional establishment while retaining the bilateral response structure at the level of reception and growth. (4) The DIM-34-SD001 hypothesis — God's faithfulness to covenant transcends human covenant-keeping (Gen 9:15; Lk 1:72 — "to remember his holy covenant" even for an unfaithful people) — is confirmed across the OT traditions: God's covenant-basis is ultimately his own character, not human performance.
- Anchor verses: Gen 9:15, Exo 19:5, Heb 8:8
- Finding type: THEOLOGICAL_NOTE

**Q&A-103 | T4.1.3**
- Tier: T4 — Relational Interfaces
- Component: T4.1 — Divine Interface — God to Human
- Prompt: 3 — What does God's extension of this characteristic reveal about his disposition toward the human person?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: God's covenant-extension toward the human person reveals a relational disposition of initiating, self-binding, persistent, and ultimately self-giving love. (1) Initiating: God always acts first — no covenant in the data is human-initiated toward God. The initiative is exclusively divine. (2) Self-binding: God binds himself by oath (OBS-034-052), by the covenant sign (rainbow, Gen 9:15 context), and ultimately by the blood of his Son (Heb 13:20 — OBS-034-074). His commitment is not merely declared but enacted through self-binding mechanisms that make his faithfulness legally and sacrificially secured. (3) Persistent: God remembers his covenant even when humans break it (Gen 9:15; Lk 1:72 — OBS-034-073; Lev 26:44-45 in 765-001 context). His disposition is not conditional on continuous human faithfulness. (4) Self-giving: the new covenant is enacted through Christ's death (Heb 9:16 — OBS-034-069). God's covenant-extension ultimately costs him the life of his Son — the most extreme form of self-giving. This reveals that God's disposition toward the human person is one of total, self-giving, initiative-bearing love.
- Anchor verses: Gen 9:15, Heb 13:20, Heb 9:15
- Finding type: THEOLOGICAL_NOTE

**Q&A-104 | T4.1.4**
- Tier: T4 — Relational Interfaces
- Component: T4.1 — Divine Interface — God to Human
- Prompt: 4 — If evidence is silent on God-to-human operation, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is extensive — God-to-human is the primary directional register of the entire registry. Q&A-101 through Q&A-103 substantive.

**Q&A-105 | T4.2.1**
- Tier: T4 — Relational Interfaces
- Component: T4.2 — Divine Interface — Human to God
- Prompt: 1 — Does the verse evidence show this characteristic operating in the human person's movement toward God — in seeking, supplication, worship, or covenant — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the human-toward-God direction is extensively evidenced as the responsive axis of the covenant relationship. (1) Covenant entry as movement toward God: Neh 10:29 — "enter into a curse and an oath to walk in God's Law" — the community moves toward God through formal covenantal commitment (OBS-034-035). 2Ki 23:3 — the king "made a covenant before the Lord, to walk after the Lord" — covenant-making is explicitly a movement toward God (OBS-034-047). (2) Covenant-keeping as sustained movement: Deu 7:9 — "those who love him and keep his commandments" — sustained love and commandment-keeping as the ongoing human posture toward God within the covenant (OBS-034-039). Psa 25:10 — "those who keep his covenant and his testimonies" — covenant-keeping as a description of the person who walks with God. (3) Confession of covenant breach as movement back toward God: Dan 9:11 (OBS-034-036) — Daniel's prayer is a movement of confessional return toward God after covenant failure — using covenantal language to re-engage the God whose covenant has been broken. (4) Swearing by God's name as allegiance (3308-003 — OBS-034-055): taking an oath in God's name as an act of inner allegiance directed toward God.
- Anchor verses: Neh 10:29, 2Ki 23:3, Dan 9:11
- Finding type: MEANING_OBSERVATION

**Q&A-106 | T4.2.2**
- Tier: T4 — Relational Interfaces
- Component: T4.2 — Divine Interface — Human to God
- Prompt: 2 — What does the evidence reveal about the inner posture required for this movement?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence consistently requires a whole-person inner posture — not selective or partial engagement. (1) All-heart and all-soul: 2Ki 23:3 — "with all his heart and all his soul" (OBS-034-047). The inner posture for genuine human-to-God covenant movement is totality of inner engagement. (2) Love toward God: Deu 7:9 — "those who love him." The inner posture is not mere compliance but affective orientation toward God — love is the interior quality of genuine covenant movement toward him (OBS-034-039). (3) Reverent fear: Mal 2:5 context (765-001 direction): "he feared me. He stood in awe of my name" — reverent fear as the inner posture that enables covenantal closeness to God (Q&A-031 direction). (4) Hearing orientation: Exo 19:5 — "if you will indeed obey my voice" — attentive inner hearing is the posture from which covenant engagement begins (OBS-034-068). (5) All-heart commitment with moral integrity: Psa 50:16 (OBS-034-051) — taking the covenant "on your lips" without inner integrity is rejected; genuine human-to-God movement requires that mouth and heart are aligned.
- Anchor verses: 2Ki 23:3, Deu 7:9, Exo 19:5
- Finding type: MEANING_OBSERVATION

**Q&A-107 | T4.2.3**
- Tier: T4 — Relational Interfaces
- Component: T4.2 — Divine Interface — Human to God
- Prompt: 3 — What does the human-to-God direction reveal about the person's relationship with God?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The human-to-God direction of covenant reveals that the relationship with God is not passive receipt but active responsive engagement — the person is not merely a beneficiary of God's covenant but a participant who moves toward God through commitment, love, and sustained faithfulness. This reveals three things about the relationship: (1) It is asymmetric but genuinely mutual — God initiates, but the human's responsive movement is genuinely required and genuinely meaningful. The covenant is not a monologue but a dialogue with defined roles. (2) The whole person is engaged — "all your heart and all your soul" means the human-to-God movement requires the full inner person, not merely intellectual assent or ritual compliance. (3) The relationship is sustained through practice — not merely entered once but maintained through ongoing covenant-keeping, remembering, and love. The relationship with God is therefore constitutively covenantal in its structure: it has entry (joining), maintenance (keeping), failure (breach), and return (confession) — a full relational arc.
- Anchor verses: 2Ki 23:3, Dan 9:11, Neh 10:29
- Finding type: THEOLOGICAL_NOTE

**Q&A-108 | T4.2.4**
- Tier: T4 — Relational Interfaces
- Component: T4.2 — Divine Interface — Human to God
- Prompt: 4 — If evidence is silent on human-to-God operation, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is extensive — the human-toward-God direction is one of the two primary axes of the covenant vocabulary. Q&A-105 through Q&A-107 substantive.

**Q&A-109 | T4.3.1**
- Tier: T4 — Relational Interfaces
- Component: T4.3 — Human Interface — Giving
- Prompt: 1 — Does the verse evidence show this characteristic being extended by one person toward another — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the horizontal giving of covenant is evidenced in person-to-person covenant traditions. (1) Covenant of friendship: 3304-004 (OBS-034-049) — karat berit between persons as a relational act of committed loyalty, given to another person. The Jonathan-David covenant (implied by 3304-004's framing) is the giving of covenant-loyalty to another person — a genuine act of self-giving in the horizontal register. (2) Marriage covenant: H1285 1a5 (OBS-034-009, 765-005 direction) — the marriage covenant is the giving of covenantal commitment to a spouse — an act of solemn self-binding toward another person. (3) Firm covenant with community: Neh 9:38 (OBS-034-037) — the community leaders extend covenant-commitment to the whole people by putting their names on the sealed document — a giving of formal commitment to and on behalf of others. (4) Oaths given to another: H7650 (OBS-034-017) — swearing an oath to another person as the giving of binding commitment: the person extends their covenantal word to another as a gift of reliable promise.
- Anchor verses: Neh 9:38, 765-005 and 3304-004 contexts
- Finding type: MEANING_OBSERVATION

**Q&A-110 | T4.3.2**
- Tier: T4 — Relational Interfaces
- Component: T4.3 — Human Interface — Giving
- Prompt: 2 — What inner conditions enable genuine extension of this characteristic toward another?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence identifies: (1) Moral integrity — the person who gives covenant to another must be the kind of person who keeps their word. 3308-002 (OBS-034-053) — oath-keeping as moral character: the inner quality of trustworthiness is what makes covenant-giving genuine rather than empty. (2) Inner faithfulness (amanah-root — OBS-034-008, OBS-034-037): Neh 9:38 — the "firm covenant" is one whose firmness derives from the faithfulness character of those who make it. Genuine covenant-giving flows from a faithful inner character. (3) Committed love: 3304-004 (OBS-034-049) — the covenant of intimate personal loyalty is given from a disposition of committed love toward the other person. The giving cannot be merely formal; it requires an inner orientation of love toward the covenant partner. (4) Freedom from competing covenants: 3304-003 (OBS-034-048) — genuine covenant-giving to the right party requires having one's loyalty free from false covenantal commitments. A person bound to false covenants cannot give genuine covenant-loyalty to the right party.
- Anchor verses: Neh 9:38, 3304-004 context, 3308-002 context
- Finding type: MEANING_OBSERVATION

**Q&A-111 | T4.3.3**
- Tier: T4 — Relational Interfaces
- Component: T4.3 — Human Interface — Giving
- Prompt: 3 — What must the person have received or become before they can genuinely give this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence suggests that genuine covenant-giving (horizontal) requires the person to have first received and been formed by covenant (vertical). The logic: a person who has not entered God's covenant and been formed by it — whose inner character has not been shaped by covenantal faithfulness (amanah-root — OBS-034-008) — lacks the inner moral quality that makes covenant-giving to another person genuine and sustainable. Specifically: (1) The person must have developed the moral character of oath-keeping (3308-002 — OBS-034-053) — one cannot give reliable covenant-commitment if one's inner character is that of an asunthetos (covenant-breaker — OBS-034-057). (2) Under the new covenant: the person who has received God's law on the heart (Heb 8:10) and the Spirit's transformation (2 Cor 3:6) is equipped to give covenant-loyalty from an inner nature that has been constituted for it. The new covenant provides the inner constitution from which genuine covenant-giving to others flows. In this sense, receiving the vertical covenant is the condition of possibility for giving genuine horizontal covenant.
- Anchor verses: Heb 8:10, 3308-002 context, Neh 9:38
- Finding type: THEOLOGICAL_NOTE

**Q&A-112 | T4.3.4**
- Tier: T4 — Relational Interfaces
- Component: T4.3 — Human Interface — Giving
- Prompt: 4 — If evidence is silent on the giving direction, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence addresses human giving of covenant in horizontal register. Q&A-109 through Q&A-111 substantive.

**Q&A-113 | T4.4.1**
- Tier: T4 — Relational Interfaces
- Component: T4.4 — Human Interface — Receiving
- Prompt: 1 — Does the verse evidence show this characteristic being received by a person from another — and if so, how?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — at two levels. (1) Receiving God's covenant: the primary receiving mode is the human reception of God's covenant-initiative. This operates across all covenant traditions: the people receiving the Noahic covenant (Gen 9:9 — all living creatures receive), the Abrahamic community receiving the covenant of circumcision (Act 7:8 — OBS-034-054), the Sinai community receiving the covenant through Moses (Exo 24:7-8), the new covenant community receiving through Christ's blood (Lk 22:20; 1 Cor 11:25 — OBS-034-058). Reception in these contexts involves: entering, eating/drinking (the covenant meal), being circumcised, swearing, or being baptised. (2) Receiving covenant from another human: the person who is offered the covenant of friendship or marriage receives it through acceptance and commitment — the receiving mode is the responsive volitional acceptance of the covenant-bond offered.
- Anchor verses: Lk 22:20, Act 7:8, Neh 10:29
- Finding type: MEANING_OBSERVATION

**Q&A-114 | T4.4.2**
- Tier: T4 — Relational Interfaces
- Component: T4.4 — Human Interface — Receiving
- Prompt: 2 — What inner conditions enable or block reception of this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: Addressed substantively in Q&A-031 (T1.7.1) and Q&A-032 (T1.7.2) — citing those findings. Enabling conditions: reverent fear (Mal 2:5 context), love toward God (Deu 7:9), hearing orientation (Exo 19:5), all-heart commitment (2Ki 23:3), and for the new covenant: no prior inner condition required for God's writing on the heart. Blocking conditions: hardened mind (2 Cor 3:14 — OBS-034-072), stubborn heart (Jer 11:8), false covenantal allegiance (3304-003 — OBS-034-048), covenant-breaking inner character (G0802 — OBS-034-057). No new findings beyond T1.7 — confirmed consistent.
- Anchor verses: Deu 7:9, 2 Cor 3:14, Jer 11:8
- Finding type: MEANING_OBSERVATION

**Q&A-115 | T4.4.3**
- Tier: T4 — Relational Interfaces
- Component: T4.4 — Human Interface — Receiving
- Prompt: 3 — What is the inner-being state of the person who encounters this characteristic but does not receive it?
- Disposition: ANSWERED
- Status tag: A
- Notation: Consistent with prior analysis
- Answer: Addressed in Q&A-033 (T1.7.3) — the inner-being state is: desolation (Eph 2:12 — OBS-034-060), bondage (Gal 4:24 — OBS-034-071), moral dissolution (Rom 1:31 — OBS-034-057), and curse-activation for those who entered but then rejected the covenant (Dan 9:11 — OBS-034-036; Heb 10:29 — OBS-034-070). Consistent with T1.7.3. No new findings — confirmed stable.
- Anchor verses: Eph 2:12, Gal 4:24, Heb 10:29
- Finding type: MEANING_OBSERVATION

**Q&A-116 | T4.4.4**
- Tier: T4 — Relational Interfaces
- Component: T4.4 — Human Interface — Receiving
- Prompt: 4 — If evidence is silent on the receiving direction, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Evidence is not silent — Q&A-113 through Q&A-115 address the receiving direction.

**Q&A-117 | T4.5.1**
- Tier: T4 — Relational Interfaces
- Component: T4.5 — Human Interface — Boundaries
- Prompt: 1 — Does this characteristic operate differently within existing relational bonds versus across relational distance or difference?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the evidence shows covenant operating differently depending on prior relational standing. (1) Within existing bonds: covenant deepens and formalises existing relational connections — the Jonathan-David covenant (3304-004 — OBS-034-049) formalises an existing relationship of loyalty; the Sinai covenant structures the already-existent Exodus-community relationship between God and Israel. Within an existing bond, covenant adds formal binding commitment, mutual obligation, and the oath/curse structure to a relationship that already has relational content. (2) Across relational distance: covenant can also initiate a relationship across distance or difference — the Noahic covenant extends to all living creatures (Gen 9:9 — OBS-034-038), including those not in prior relationship with God. Treaty covenants (H1285 1a1 — OBS-034-009) are made between previously separate parties. In these cases, covenant is the initiating structure that creates relationship across prior separation. (3) The prohibited covenant (3304-003 — OBS-034-048) operates across religious/cultural difference — making covenant with Canaanite inhabitants creates an illegitimate relational bond across a boundary that should not be crossed. The boundary-question is structurally present in the data.
- Anchor verses: Gen 9:9, Exo 19:5, Exo 34:12
- Finding type: MEANING_OBSERVATION

**Q&A-118 | T4.5.2**
- Tier: T4 — Relational Interfaces
- Component: T4.5 — Human Interface — Boundaries
- Prompt: 2 — Does this characteristic operate within covenantal contexts only, or does it cross covenantal boundaries?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The covenant characteristic is inherently a boundary-creating reality — it operates by establishing and maintaining the boundary between those who are within the covenant and those who are outside. (1) The boundary is constitutive: covenant defines who belongs ("you shall be my treasured possession among all peoples" — Exo 19:5; "you are the sons of the prophets and of the covenant" — Act 3:25; "Israel, and to them belong... the covenants" — Rom 9:4). The covenantal community is defined by the covenant boundary. (2) The boundary is not permanent for outsiders — it can be crossed through covenant-entry: "foreigners who join themselves to the Lord... and hold fast my covenant" (Isa 56:6 — Group 765-002 context) are included. The new covenant is explicit about this: "all the families of the earth" (Act 3:25), "in Christ there is neither Jew nor Greek" (Gal 3:28 context). (3) The new covenant specifically crosses the ethnic-cultural-legal boundary of the old covenant's administration: Eph 2:12-14 context — those once "strangers to the covenants of promise" (OBS-034-060) are brought near in Christ. The covenantal boundary is permeable in the new covenant direction.
- Anchor verses: Exo 19:5, Isa 56:6, Eph 2:12
- Finding type: THEOLOGICAL_NOTE

**Q&A-119 | T4.5.3**
- Tier: T4 — Relational Interfaces
- Component: T4.5 — Human Interface — Boundaries
- Prompt: 3 — What does the evidence reveal about the relational scope of this characteristic — who is included and who is not?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The relational scope of covenant shifts across the covenantal trajectory — expanding rather than contracting. (1) Noahic: universal — all living creatures (Gen 9:9 — OBS-034-038). Widest possible scope. (2) Abrahamic: a particular people (Abraham's descendants) and through them "all the families of the earth" (Act 3:25). Narrowing to a particular line but with a universal horizon. (3) Sinai: Israel as the specific covenant-community. Explicitly bounded. (4) New covenant: universally offered through Christ — "all the families of the earth" realised, the dividing wall broken down (Eph 2:14 context — OBS-034-060 direction), foreigners who hold fast to the covenant included (Isa 56:6). The scope of the new covenant is the universal scope of the Noahic covenant now realised eschatologically. Those outside the covenant (Eph 2:12) are in a condition of desolation that is a positive, remediable state — the new covenant's scope is intended to encompass all who receive it.
- Anchor verses: Gen 9:9, Act 3:25, Eph 2:12
- Finding type: THEOLOGICAL_NOTE

**Q&A-120 | T4.5.4**
- Tier: T4 — Relational Interfaces
- Component: T4.5 — Human Interface — Boundaries
- Prompt: 4 — If evidence is silent on relational boundaries, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Relational scope and boundary are extensively evidenced. Q&A-117 through Q&A-119 substantive.

**Q&A-121 | T4.6.1**
- Tier: T4 — Relational Interfaces
- Component: T4.6 — Spiritual Beings Interface
- Prompt: 1 — Does the verse evidence show this characteristic operating in relation to other spiritual beings — angelic or adversarial — and if so, how?
- Disposition: NOT ANSWERED
- Status tag: S
- Notation: Gap identified
- Answer: Stage 2a observations do not contain verse evidence from the programme's data directly showing covenant operating in relation to angelic or adversarial spiritual beings. The data does not address this domain. One indirect note: H1286 ([Baal]-berith — OBS-034-011) — the Canaanite deity named "lord of covenant" — is a spiritual-beings adjacent observation, but it involves pagan worship directed toward a false deity, not a covenant relationship between the human and spiritual beings per se. Not sufficient to constitute a finding for T4.6.1. Recording as S — the data is silent on this specific prompt. Not a Stage 2a reopening item; the absence is inherent to the verse set.
- Finding type: OBSERVATION

**Q&A-122 | T4.6.2**
- Tier: T4 — Relational Interfaces
- Component: T4.6 — Spiritual Beings Interface
- Prompt: 2 — Is this characteristic a site of adversarial activity?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The evidence indirectly supports adversarial activity against covenant, though no specific adversarial spiritual being is named in the programme's verse set as the agent. (1) The prohibited covenant (3304-003 — OBS-034-048) — binding to false loyalties — operates in a context where false gods are the competing covenant-partners. The spiritual dimension of false covenant is present (worshipping Baal, making treaties with Canaanite idol-worshippers involves the spiritual realm). (2) The cognitive veil (2 Cor 3:14 — OBS-034-072) — hardened minds over the old covenant — suggests a spiritually-located blockage, though 2 Corinthians does not directly attribute this to adversarial spiritual agency in the programme's verse set. (3) H1286 ([Baal]-berith — OBS-034-011): the pagan deity worshipped at Shechem as "lord of covenant" represents an adversarial spiritual claim to covenant-lordship — a spiritual being positioning itself as the true covenant-lord in opposition to YHWH. Gap: the specific adversarial-spiritual dimension is inferred rather than directly stated in the programme's verse evidence. Recording as P.
- Anchor verses: H1286 context, 2 Cor 3:14
- Finding type: OBSERVATION

**Q&A-123 | T4.6.3**
- Tier: T4 — Relational Interfaces
- Component: T4.6 — Spiritual Beings Interface
- Prompt: 3 — Is this characteristic communicated, strengthened, or mediated through angelic ministry in the evidence?
- Disposition: NOT ANSWERED
- Status tag: S
- Notation: Gap identified
- Answer: The programme's verse evidence does not directly show covenant being communicated or mediated through angelic ministry. One note: Gal 3:19 (not in the programme's verse set) references the law being "put in place through angels" at Sinai — this would be relevant but is not in the data. Not in the evidence base; recording as S. The gap is inherent to the verse set.
- Finding type: OBSERVATION

**Q&A-124 | T4.6.4**
- Tier: T4 — Relational Interfaces
- Component: T4.6 — Spiritual Beings Interface
- Prompt: 4 — If evidence is silent on the spiritual beings interface, note this explicitly.
- Disposition: ANSWERED
- Status tag: A
- Notation: Gap identified
- Answer: The evidence is largely silent on the spiritual beings interface. T4.6.1 and T4.6.3 are S-status (silent). T4.6.2 is partially answered. The programme's verse set does not directly address angelic mediation of covenant or named adversarial activity against it. This gap is noted explicitly. The spiritual-beings dimension of covenant is an area requiring further investigation that lies beyond the current evidence base.
- Finding type: OBSERVATION

TIER T4 COMPLETE — Relational Interfaces
Date: 2026-05-01
Prompts: 24 total. A: 14. P: 2. S: 3. N: 5.
New findings: 14. SD pointers raised: 0.
S-status prompts: T4.6.1 (spiritual beings operating), T4.6.3 (angelic mediation) — inherent data gaps; T4.6.4 names these explicitly as gaps. Not Stage 2a reopening items.


#### Tier 5 — Formative and Developmental Dimension — 21 prompts

**Q&A-125 | T5.1.1**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.1 — Nature of Transformation
- Prompt: 1 — Does this characteristic produce transformation — condition, orientation, or both?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — and the transformation produced by covenant is among the most comprehensively evidenced in the entire registry. The evidence shows it changing both condition and orientation. (1) Condition change: the new covenant constitutionally changes the inner condition of the person — law written on the heart (Jer 31:33; Heb 8:10 — OBS-034-040, OBS-034-059); Spirit-administration rather than letter-constraint (2 Cor 3:6 — OBS-034-061); from bondage to freedom (Gal 4:24 — OBS-034-071). These are condition changes — the person who is under the new covenant is constitutionally different from the person under the old. The inner organs (heart, mind) carry different content; the governing principle (Spirit vs. letter) is changed. (2) Orientation change: the new covenant reorients the person toward God through knowing him (Jer 31:34 — OBS-034-040), through the written law shaping inner orientation (Heb 8:10), and through the elimination of the cognitive veil that blocked orientation (2 Cor 3:14-16 — OBS-034-072). (3) DIM-34-001 (confirmed and deepened throughout): the trajectory from Sinai (demanding inner obedience) to new covenant (producing inner transformation) is a transformation in the mode of covenant's operation — the covenant itself transforms from a demanding structure to a producing structure.
- Anchor verses: Jer 31:33, Heb 8:10, 2 Cor 3:6, Gal 4:24
- Finding type: THEOLOGICAL_NOTE

**Q&A-126 | T5.1.2**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.1 — Nature of Transformation
- Prompt: 2 — Is the transformation reversible or irreversible?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The evidence points in different directions for different covenantal modes. (1) The new covenant constitutional transformation (law on heart, Spirit-administration) — the evidence does not explicitly address reversibility for this mode. The language is declarative and permanent in intent: God says "I will" (future promise framing in Jer 31:31-34; Heb 8:8-10 — OBS-034-040). The covenant is described as "eternal" (Heb 13:20 — OBS-034-074), which implies irreversibility. (2) Covenant-breach as reversible rupture: the OT evidence shows covenant breach (Dan 9:11 — OBS-034-036) followed by potential restoration (God's own covenant-memory persists despite breach — Gen 9:15, Lk 1:72 — OBS-034-073). Covenant is broken but not permanently destroyed from God's side. (3) Heb 10:29 (OBS-034-070): "trampled underfoot the Son of God, profaned the blood of the covenant by which he was sanctified" — this language implies that profaning the covenant after receiving it represents a severe and serious condition, though the text does not explicitly define the limits of reversibility. Gap: the question of whether new covenant transformation is individually reversible is not directly answered in the programme's verse set. Noting as P.
- Anchor verses: Heb 13:20, Heb 10:29, Jer 31:31
- Finding type: THEOLOGICAL_NOTE

**Q&A-127 | T5.1.3**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.1 — Nature of Transformation
- Prompt: 3 — If evidence is silent on transformation, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Transformation is extensively evidenced. Q&A-125 and Q&A-126 substantive.

**Q&A-128 | T5.2.1**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.2 — Sequence of Inner States
- Prompt: 1 — Does the verse evidence describe a sequence of inner states through which this characteristic moves the person?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the new covenant evidence provides the clearest sequence in the registry. The sequence from Jer 31:31-34 / Heb 8:8-10 is: (1) Identification of failure under the old covenant — "they did not continue in my covenant" (Heb 8:9). Before-state: covenant-breaking, hardened, under judgment. (2) Divine declaration of a new covenant — "the days are coming... I will make a new covenant" (Heb 8:8). The transition: God's initiative to address the failure. (3) Constitutional inscription — "I will put my laws into their minds and write them on their hearts" (Heb 8:10 — OBS-034-059). During: God acts within the inner person. (4) Relational identification — "I will be their God and they shall be my people" (Heb 8:10). After-state: covenantal belonging is established constitutionally. (5) Knowing — "they shall all know me, from the least to the greatest" (Jer 31:34). Final state: intimate knowing of God as the sustained product of the sequence. The sequence is: failure → divine initiative → inner inscription → belonging → knowing. This is the most fully articulated transformation sequence in the registry.
- Anchor verses: Heb 8:8-10, Jer 31:34
- Finding type: THEOLOGICAL_NOTE

**Q&A-129 | T5.2.2**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.2 — Sequence of Inner States
- Prompt: 2 — What are those states, and what does the sequence reveal about how this characteristic works?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The five-stage sequence (Q&A-128) reveals the following about how covenant works: (1) Covenant begins with failure — the new covenant is instituted in response to the failure of the old, not as its direct continuation. The before-state is covenant-breaking, not covenant-neutral. (2) The initiative is wholly divine — God declares and acts; the human is the recipient of the transformative sequence. (3) The mechanism is inscription, not instruction — God writes, not teaches. The transformation is not pedagogical (providing better information) but constitutional (changing the inner organ itself). (4) Belonging precedes knowing — "I will be their God... they shall know me." The relational standing (belonging) is established by God's inscription before the cognitive knowing of God grows. This challenges the assumption that knowing precedes belonging; in the new covenant sequence, belonging is the ground of knowing. (5) The end-state is knowing — covenant does not leave the person with mere legal compliance but with intimate personal knowledge of God. The telos of the covenantal sequence is a knowing relationship, not a law-keeping condition.
- Anchor verses: Heb 8:8-10, Jer 31:34
- Finding type: THEOLOGICAL_NOTE

**Q&A-130 | T5.2.3**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.2 — Sequence of Inner States
- Prompt: 3 — If evidence is silent on sequence, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Sequence is substantively evidenced in Jer 31:31-34 / Heb 8:8-10.

**Q&A-131 | T5.3.1**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.3 — Mechanism of Change
- Prompt: 1 — What mechanism does this characteristic use to produce change — discipline, encounter, gradual formation, sudden transformation?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence shows two distinct mechanisms operating in different covenantal modes. (1) External-demand mechanism (Sinai/Mosaic covenant): law given externally, demanding internal obedience. The mechanism is instruction + discipline + sanction (oath/curse for breach — OBS-034-007). Change is expected through sustained volitional compliance with the external law. This is the discipline-and-demand mechanism. (2) Internal-inscription mechanism (new covenant): God writes on the heart and mind (Heb 8:10 — OBS-034-059); the Spirit administers the covenant from within (2 Cor 3:6 — OBS-034-061). The mechanism is divine interior action — inscription, not instruction. Change is produced from within through God's own writing, not through the person's compliance with an external demand. This is the constitutive-transformation mechanism. The two mechanisms correspond to the OT vs. NT covenantal modes and are the constitutional-level expression of DIM-34-001's Sinai-to-new-covenant trajectory. The shift in mechanism — from external demand to internal inscription — is the most analytically significant developmental finding of T5.
- Anchor verses: Deu 7:9, Heb 8:10, 2 Cor 3:6
- Finding type: THEOLOGICAL_NOTE

**Q&A-132 | T5.3.2**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.3 — Mechanism of Change
- Prompt: 2 — Does the evidence distinguish between mechanisms in different contexts?
- Disposition: ANSWERED
- Status tag: A
- Notation: Adds structure
- Answer: Yes — the two mechanisms are explicitly distinguished and contrasted in the evidence: 2 Cor 3:6 — "not of the letter but of the Spirit" (OBS-034-061). The letter = the external-demand mechanism; the Spirit = the internal-inscription mechanism. "The letter kills, but the Spirit gives life" — the two mechanisms are not merely different but operate in opposite directions with respect to the person's inner-being: the letter condemns (produces death by exposing failure against the external standard); the Spirit liberates and produces life (by working from within). Heb 8:9-10 contrasts the two covenants explicitly: "not like the covenant that I made with their fathers" — the new covenant mechanism is distinguished from the old. Gal 4:24 (OBS-034-071) — slavery vs. freedom — also names the two mechanisms' different outcomes in the inner person.
- Anchor verses: 2 Cor 3:6, Heb 8:9-10, Gal 4:24
- Finding type: THEOLOGICAL_NOTE

**Q&A-133 | T5.3.3**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.3 — Mechanism of Change
- Prompt: 3 — If evidence is silent on mechanism, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Mechanism is extensively evidenced. Q&A-131 and Q&A-132 substantive.

**Q&A-134 | T5.4.1**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.4 — Suffering and Affliction
- Prompt: 1 — Does the verse evidence show this characteristic operating in relation to suffering or affliction?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the covenant vocabulary operates directly in relation to suffering and affliction in several registers. (1) The covenant curse as suffering: Dan 9:11 (OBS-034-036) — the curse poured out upon Israel is covenant-consequence suffering. The suffering of exile, sword, famine, and plague in the prophetic literature is explicitly framed as the activated covenant curse — suffering is the form taken by covenant sanction (H0423 alah — OBS-034-007). (2) Covenant as refuge in suffering: Psa 25:10-14 (Group 765-001/765-005 direction) — the covenant-keeper finds God's steadfast love and faithfulness in distress; covenant is the relational ground that holds when circumstances are afflicting. (3) The Noahic covenant as response to the catastrophe of the flood: Gen 9:15 (OBS-034-038) — God's covenant is made in the aftermath of catastrophic destruction. Covenant is God's answer to suffering at the cosmic scale. (4) The new covenant's enactment through Christ's suffering: Heb 9:15 — "a death has occurred that redeems them from the transgressions committed under the first covenant" (OBS-034-058 direction). The new covenant is enacted through the covenant-maker's own suffering and death. Covenant is constituted through suffering, not merely responses to it.
- Anchor verses: Dan 9:11, Gen 9:15, Heb 9:15
- Finding type: THEOLOGICAL_NOTE

**Q&A-135 | T5.4.2**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.4 — Suffering and Affliction
- Prompt: 2 — Does suffering deepen, test, reveal, or produce this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The evidence suggests that suffering both tests and reveals covenant faithfulness. (1) Suffering tests covenant: the periods of affliction in the OT (exile, enemies, covenant curse — Dan 9:11 — OBS-034-036) are contexts in which the inner orientation of covenant faithfulness is tested and either confirmed or broken. Daniel's prayer itself is evidence of covenant faithfulness under suffering — confessing sin and calling on the covenantal God in the midst of exile. (2) Suffering reveals covenant faithfulness and its absence: Lev 26:44 (Group 765-001 context) — "when they are in the land of their enemies, I will not spurn them... or break my covenant with them." God's covenant-faithfulness is revealed most clearly in the context of Israel's affliction. Suffering is the context in which God's faithfulness and human unfaithfulness are made visible. (3) The new covenant is produced through Christ's suffering and death (Heb 9:15 — OBS-034-058, OBS-034-069): the covenant-making sacrifice requires suffering. Suffering is not merely a context for covenant but constitutive of the new covenant's very enactment.
- Anchor verses: Dan 9:11, Lev 26:44, Heb 9:15
- Finding type: THEOLOGICAL_NOTE

**Q&A-136 | T5.4.3**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.4 — Suffering and Affliction
- Prompt: 3 — If evidence is silent on the relationship to suffering, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Covenant's relationship to suffering is extensively evidenced. Q&A-134 and Q&A-135 substantive.

**Q&A-137 | T5.5.1**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.5 — Formation and Sanctification
- Prompt: 1 — Does the verse evidence show this characteristic participating in the longer arc of character formation and sanctification — shaping the person toward greater likeness over time?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — covenant is the structural framework within which the entire arc of character formation and sanctification takes place in Scripture. (1) The Sinai covenant's law shapes moral character over time through sustained discipline and obedience — the person who keeps covenant ("keeps his commandments" — Deu 7:9; "keeps his covenant and his testimonies" — Psa 25:10 — OBS-034-039) is progressively formed into a person of integrity. (2) The new covenant constitutionally initiates this formation at a deeper level: law written on the heart (Heb 8:10 — OBS-034-059) is the constitutional foundation for ongoing moral formation. The Spirit's administration (2 Cor 3:6 — OBS-034-061) produces what the law demanded. Heb 10:29 mentions "sanctified by the blood of the covenant" (OBS-034-070) — the covenant blood is the ground of sanctification, not merely justification. (3) The new self/new creation (777-002 — OBS-034-062) — kainos in the register of formation: Eph 4:24 — "put on the new self, created after the likeness of God in true righteousness and holiness." Covenant produces formation toward Godlikeness.
- Anchor verses: Psa 25:10, Heb 8:10, Heb 10:29, Eph 4:24
- Finding type: THEOLOGICAL_NOTE

**Q&A-138 | T5.5.2**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.5 — Formation and Sanctification
- Prompt: 2 — What does the evidence reveal about the role of this characteristic in that longer arc?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Covenant plays a foundational, architecturally prior role in the arc of character formation and sanctification — it is not one element among equals but the structural framework that makes formation possible. Three specific roles: (1) Constitutional grounding — the new covenant's law-on-heart inscription (Heb 8:10) provides the inner constitutional ground from which all subsequent formation grows. Formation cannot proceed sustainably without this constitutional foundation. (2) Relational motivation — covenant positions the person in a relationship of known belonging ("I will be their God, they shall be my people" — Heb 8:10). Formation that flows from known belonging is qualitatively different from formation driven by fear of punishment. (3) Progressive sanctification through the blood — "sanctified by the blood of the covenant" (Heb 10:29 — OBS-034-070) — the covenant's atoning mechanism is the ongoing basis for the sanctification that formation requires. Without covenantal atonement, the moral weight of failure would prevent formation from proceeding. Covenant provides the structural conditions (constitution, belonging, atonement) within which formation operates.
- Anchor verses: Heb 8:10, Heb 10:29, Eph 4:24
- Finding type: THEOLOGICAL_NOTE

**Q&A-139 | T5.5.3**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.5 — Formation and Sanctification
- Prompt: 3 — If evidence is silent on formation and sanctification, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Formation and sanctification are evidenced substantively. Q&A-137 and Q&A-138 address these.

**Q&A-140 | T5.6.1**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.6 — Eschatological Trajectory
- Prompt: 1 — Does the verse evidence point this characteristic toward an eschatological fullness?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the covenant vocabulary is among the most eschatologically directed in the programme. (1) The "eternal covenant" (Heb 13:20 — OBS-034-074): the covenant is eternal in quality — it does not end at death or history's close but extends into the eternal. The resurrection of Christ "by the blood of the eternal covenant" frames the covenant as the mechanism of eschatological life. (2) New name, new song, new Jerusalem (777-003 — OBS-034-063): the kainos vocabulary in Revelation extends the new covenant's newness into the final eschatological realities — new heaven and earth (Rev 21:1), new Jerusalem (Rev 21:2), all things made new (Rev 21:5). These are the covenant's eschatological fullness: the covenant that was written on the heart (Jer 31:33) reaches its telos in the fully renewed creation. (3) Eph 2:12 — "covenants of promise" (OBS-034-060): covenant is inherently promissory — it points forward to a fullness not yet realised. The present experience of covenant is always also a foretaste of the eschatological fullness toward which the covenant moves.
- Anchor verses: Heb 13:20, Rev 21:1-5, Eph 2:12
- Finding type: THEOLOGICAL_NOTE

**Q&A-141 | T5.6.2**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.6 — Eschatological Trajectory
- Prompt: 2 — What does the present experience of this characteristic anticipate about its future fullness?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The present experience of covenant (the new covenant in Christ) anticipates three eschatological dimensions of fullness: (1) Complete knowing — the new covenant promises "they shall all know me, from the least to the greatest" (Jer 31:34 — OBS-034-040). This is partially realised in the present (believers know God through the Spirit) but fully realised only eschatologically when the partial knowing gives way to complete and unmediated knowing. (2) Universal and eternal belonging — the present covenant of belonging ("I will be their God and they shall be my people" — Heb 8:10 — OBS-034-059) anticipates its eschatological fullness: "the dwelling of God is with man. He will dwell with them and they will be his people" (Rev 21:3 context — OBS-034-063 direction). The covenant formula reaches its fullest expression in the new creation. (3) Healed creation — the Noahic covenant's universal scope (all living creatures — OBS-034-038) anticipates the new creation's universal scope (new heaven and earth — OBS-034-063). Covenant moves from promise to realisation, from partial to total, from temporal to eternal.
- Anchor verses: Jer 31:34, Heb 8:10, Rev 21:3
- Finding type: THEOLOGICAL_NOTE

**Q&A-142 | T5.6.3**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.6 — Eschatological Trajectory
- Prompt: 3 — If evidence is silent on eschatological trajectory, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Eschatological trajectory is extensively evidenced. Q&A-140 and Q&A-141 substantive.

**Q&A-143 | T5.7.1**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.7 — Deposit Consequence
- Prompt: 1 — Where T2.8 identified a constitutional deposit, what developmental consequence does that deposit produce over time?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: T2.8 (Q&A-059, Q&A-060) identified two deposit mechanisms — circumcision (bodily sign transmitted generationally) and covenantal word-transmission (Isa 59:21 — through the mouth of offspring). The developmental consequences: (1) Circumcision deposit → covenantal community formation: the bodily sign carried across generations produces a covenantal people shaped by the covenant's content and obligations. Each generation born into the circumcision-covenant inherits a covenantal identity that forms their inner-being self-understanding, obligations, and community belonging. The generational deposit of circumcision produces a formed covenant community. (2) Word-transmission deposit → covenantal knowing across generations: Isa 59:21 — "shall not depart out of your mouth, or out of the mouth of your offspring, or out of the mouth of your children's offspring." The new covenant's word-deposit produces a generational chain of covenantal formation through the transmission of God's words — the covenant is taught, confessed, and proclaimed across generations, and this transmission is itself the mechanism of formation. (3) New covenant trajectory: the NT relativises the bodily circumcision deposit (Gal 3:17 context) while retaining and deepening the word-deposit through the Spirit. The developmental consequence shifts from bodily marking to Spirit-enabling of word-transmission.
- Anchor verses: Act 7:8, Isa 59:21, Gal 3:17
- Finding type: THEOLOGICAL_NOTE

**Q&A-144 | T5.7.2**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.7 — Deposit Consequence
- Prompt: 2 — Does the evidence indicate generational consequence — a deposit carried forward beyond the individual?
- Disposition: ANSWERED
- Status tag: A
- Notation: Consistent with prior analysis
- Answer: Yes — confirmed in Q&A-059 through Q&A-061 (T2.8) and Q&A-143. Act 3:25 ("in your offspring shall all the families of the earth be blessed"), Act 7:8 (circumcision as generational deposit), Isa 59:21 (covenant words transmitted through generations of offspring's mouths). Generational consequence is one of the most structurally prominent features of the covenant vocabulary — covenant is inherently transgenerational. The blessing and identity conveyed through covenant extend beyond the individual who enters it to their descendants across multiple generations. This is the mechanism through which covenant shapes and forms communities and peoples over historical time.
- Anchor verses: Act 3:25, Act 7:8, Isa 59:21
- Finding type: THEOLOGICAL_NOTE

**Q&A-145 | T5.7.3**
- Tier: T5 — Formative and Developmental Dimension
- Component: T5.7 — Deposit Consequence
- Prompt: 3 — If T2.8 found no deposit, note this explicitly and close T5.7.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: T2.8 found generational deposit evidence (circumcision, word-transmission). T5.7 does not close. Q&A-143 and Q&A-144 address the deposit consequence substantively.

TIER T5 COMPLETE — Formative and Developmental Dimension
Date: 2026-05-01
Prompts: 21 total. A: 15. P: 1. S: 0. N: 5.
New findings: 14. SD pointers raised: 0.


#### Tier 6 — Structural Relationships with Other Characteristics — 24 prompts

**Q&A-146 | T6.1.1**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.1 — Co-occurrence
- Prompt: 1 — Which adjacent characteristics appear most frequently alongside this one in the verse evidence?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Using the §G.2 co-occurrence data (OBS-034-029, OBS-034-030, OBS-034-031): Top co-occurring characteristics by shared verse count — R112 mind (39), R103 love (37), R197 authority (23), R073 guilt (20), R160 thought (20), R180 yielding (19), R182 Soul (19), R023 compassion (17), R176 worship (17), R187 strength (15), R011 awe (14), R044 despair (14), R183 heart (14), R019 calling (13), R059 faith (13), R061 fear (13), R213 listen (13). The top five by count: mind (39), love (37), authority (23), guilt (20), thought (20). The pattern is dominated by the inner cognitive-volitional organs (mind, thought, heart, Soul), the relational-grace cluster characteristics (love, compassion, faithfulness), and the conscience-related characteristics (guilt, fear, awe). These represent the immediate inner-being neighbourhood of covenant.
- Anchor verses: Deu 7:9, 2Ki 23:3, Jer 31:33
- Finding type: CROSS_REGISTRY

**Q&A-147 | T6.1.2**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.1 — Co-occurrence
- Prompt: 2 — What does the pattern of co-occurrence reveal about this characteristic's place in the inner-being landscape?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The co-occurrence pattern reveals that covenant occupies a structurally central position in the inner-being landscape — it is co-present with characteristics across multiple dimensions and domains. Three observations: (1) Central hub status: covenant co-occurs with the widest range of inner-being characteristics of any word in the C17 cluster expected — it is not specialist but generalist in its inner-being neighbourhood. This is consistent with the DIM-34-SD001 hypothesis (covenant as C17 structural backbone — OBS-034-002). (2) Inner organ dominance: the strongest co-occurrences are with the inner organs (mind 39, Soul 19, heart 14) — confirming that covenant's primary inner-being site is the core constitutional organs, not peripheral characteristics. (3) Relational-grace cluster coherence: the C17 cluster characteristics (love, compassion, faithfulness, kindness) all appear in the top co-occurrence table — covenant and the relational-grace vocabulary are structurally inseparable in the verse evidence. This co-occurrence coherence supports treating C17 as a genuine cluster rather than an administrative grouping.
- Anchor verses: Deu 7:9, Jer 31:33
- Finding type: CROSS_REGISTRY

**Q&A-148 | T6.1.3**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.1 — Co-occurrence
- Prompt: 3 — If no significant co-occurrence patterns emerge, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Co-occurrence patterns are extensive and analytically rich. Q&A-146 and Q&A-147 substantive.

**Q&A-149 | T6.2.1**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.2 — Sequential Relationships
- Prompt: 1 — Does the verse evidence show this characteristic consistently preceding, following, or accompanying another in a sequence?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — several sequential relationships are evidenced. (1) Covenant → hesed (love/steadfast love): Deu 7:9 — "keeps covenant and steadfast love." The pairing consistently presents covenant first, hesed second — covenant is the relational structure; hesed is the relational quality that flows within it. Lk 1:72 — "to remember his holy covenant, to show the mercy promised." Covenant precedes and grounds the expression of hesed/mercy. (2) Covenant → knowing: Jer 31:33-34 — law on the heart → "they shall all know me." The covenant inscription precedes and produces the knowing. (3) Moral failure → covenant breach → curse: Dan 9:11 — transgression → breach → curse poured out (OBS-034-036). Failure precedes breach; breach activates curse. (4) Covenant → hope: Eph 2:12 — being outside the covenants of promise → having no hope. Covenant inclusion precedes and grounds hope; covenant exclusion precedes and produces hopelessness. (5) New covenant (reception) → new self (formation): Eph 4:24 context — the new covenant's constitutional transformation grounds the formation of the new self.
- Anchor verses: Deu 7:9, Jer 31:34, Dan 9:11, Eph 2:12
- Finding type: CROSS_REGISTRY

**Q&A-150 | T6.2.2**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.2 — Sequential Relationships
- Prompt: 2 — What does the sequence reveal — causal, developmental, or correlational?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The sequences are primarily causal and constitutive, not merely correlational. (1) Covenant → hesed: constitutive — the covenant is the structure within which hesed operates; hesed is not possible in the same sustained, committed form outside a covenantal framework. Covenant constitutes the relational structure that makes hesed a sustainable inner-being quality. (2) Covenant inscription → knowing: causal — God's writing on the heart produces the knowing (Jer 31:34 — "I will write on their hearts... they shall all know me"). The inscription is the causal mechanism; the knowing is the product. (3) Moral failure → covenant breach → curse: causal — the breach activates the curse embedded in the oath structure (OBS-034-007, OBS-034-036). The causal chain is morally necessary, not contingent. (4) Covenant → hope: constitutive — covenant inclusion constitutes the conditions for hope (OBS-034-060); hope is not merely correlated with covenant but grounded in it as its foundation. The key finding: covenant is structurally prior to the characteristics it enables — it is the condition of possibility for love (hesed), hope, knowing God, and the new self. This is the constitutional-priority finding that underpins DIM-34-SD001.
- Anchor verses: Deu 7:9, Jer 31:34, Dan 9:11, Eph 2:12
- Finding type: CROSS_REGISTRY

**Q&A-151 | T6.2.3**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.2 — Sequential Relationships
- Prompt: 3 — If no sequential pattern is evidenced, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Sequential relationships are extensively evidenced. Q&A-149 and Q&A-150 substantive.

**Q&A-152 | T6.3.1**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.3 — Causal and Constitutive Relationships
- Prompt: 1 — Does this characteristic produce another characteristic in the verse evidence?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — covenant produces several distinct characteristics as its effects. (1) Knowing God (R160 thought / cognition domain): Jer 31:34 — the new covenant inscription produces knowing God as its primary sustained effect (Q&A-073, OBS-034-040). (2) Hope (R078): Eph 2:12 — covenant inclusion constitutes the ground for hope; its absence produces hopelessness (OBS-034-060). Covenant produces hope as one of its inner-being effects. (3) Faithfulness / moral character (R060): sustained covenant-keeping produces the moral character quality of faithfulness — the oath-keeper develops the inner moral character of trustworthiness (3308-002 — OBS-034-053). Covenant produces faithfulness in the person who keeps it. (4) Freedom (related to Gal 4:24 — OBS-034-071): the new covenant produces inner freedom as opposed to the bondage produced by the old covenant's external-demand mechanism. (5) Sanctification (Heb 10:29 — OBS-034-070): "sanctified by the blood of the covenant" — the covenant blood produces the condition of sanctification in the person it covers.
- Anchor verses: Jer 31:34, Eph 2:12, Heb 10:29, Gal 4:24
- Finding type: CROSS_REGISTRY

**Q&A-153 | T6.3.2**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.3 — Causal and Constitutive Relationships
- Prompt: 2 — Is this characteristic produced by another?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The human capacity for covenant is produced and enabled by several prior realities. (1) Produced by God's own covenant-faithfulness: the human's ability to enter and sustain covenant is grounded in God's prior covenant-initiative. God's faithfulness makes covenant possible for the human — without God's initiating commitment, there would be no covenantal framework for the human to enter. (2) Produced by the new covenant's constitutional transformation: the new covenant (through Spirit-inscription of the law on the heart — Heb 8:10; 2 Cor 3:6 — OBS-034-059, OBS-034-061) produces the inner constitution from which genuine covenant-faithfulness flows. The faithful human covenant-keeper (3308-002 — OBS-034-053) is produced by God's prior covenantal action within them. (3) Produced by fear of God and love (in the reception mode — Q&A-031): the inner conditions that enable covenant reception (reverent fear, love — OBS-034-039, Q&A-031) are themselves inner-being realities that precede and enable covenant engagement. In this sense, fear and love are constitutive inputs to covenant faithfulness. (4) The amanah-emunah root connection (OBS-034-008): faithfulness (emunah) produces the firm covenant (amanah) — the character of faithfulness is the soil from which genuine covenant-keeping grows.
- Anchor verses: Heb 8:10, 2 Cor 3:6, Neh 9:38
- Finding type: CROSS_REGISTRY

**Q&A-154 | T6.3.3**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.3 — Causal and Constitutive Relationships
- Prompt: 3 — Is this characteristic a constituent element of another, or does another constitute part of this one?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Two directions are evidenced. (1) Covenant as constituent of other characteristics: hesed (steadfast love, R103) is constituted in part by its covenantal context — Deu 7:9 pairs hesed and berit as a unit, suggesting that the committed, enduring quality of hesed is in part constituted by the covenantal relationship within which it operates. Similarly, hope (R078) in the biblical sense is constituted in part by covenantal promise — the covenants of promise (Eph 2:12) are the structural constituent of eschatological hope. (2) Other characteristics as constituents of covenant: faithfulness (emunah-root — OBS-034-008) is a constituent element of the firm covenant (amanah) — faithfulness is the character quality from which genuine covenant-keeping is constituted. Oath (H0423, H7650 — OBS-034-007, OBS-034-017) is the verbal-performative constituent of the covenant-making act — covenant cannot be constituted without the performative commitment mechanism of the oath. Hesed is both produced by covenant and constitutive of it — the relationship is mutually constitutive in different registers.
- Anchor verses: Deu 7:9, Neh 9:38, Eph 2:12
- Finding type: CROSS_REGISTRY

**Q&A-155 | T6.3.4**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.3 — Causal and Constitutive Relationships
- Prompt: 4 — If no causal or constitutive relationship is evidenced, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Causal and constitutive relationships are extensively evidenced. Q&A-152 through Q&A-154 substantive.

**Q&A-156 | T6.4.1**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.4 — Vocabulary and Root Sharing
- Prompt: 1 — Does this characteristic share vocabulary terms with other characteristics?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — vocabulary sharing is one of the most structurally prominent features of the covenant registry. XREF terms confirm formal cross-programme vocabulary sharing: (1) H0548 (amanah — OBS-034-008) is shared with R044 (despair), R059 (faith), R060 (faithfulness), R163 (trust), R191 (doubt) — through the emunah/aman root family. (2) G2537 (kainos — OBS-034-021) is shared with R134 (renewal) and R202 (transformation). (3) H5715 (e.dut — testimony, XREF from R159 — OBS-034-005): covenant and testimony share vocabulary in the ark/tablets tradition. (4) H7621 (she.vu.ah — oath, XREF from R019 — OBS-034-006): covenant and calling share oath vocabulary. The XREF structure makes formal vocabulary-sharing explicit in the programme's data architecture.
- Anchor verses: Neh 9:38, Heb 8:10
- Finding type: CROSS_REGISTRY

**Q&A-157 | T6.4.2**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.4 — Vocabulary and Root Sharing
- Prompt: 2 — Does vocabulary sharing extend to root-level architecture?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — root-level sharing is the most analytically significant form of vocabulary connection. (1) EMUNAH root (amanah-emunah-aman-amen): the covenant term H0548 (amanah — firm covenant) shares its root with emunah (faithfulness, R060), aman (to be faithful, R059/163), and amen (affirmation of reliability). This is a root-level semantic field that spans covenant, faithfulness, faith, and trust — all generated from the same root. The inner-being quality of faithfulness is etymologically foundational to the vocabulary of firm covenant. (2) KARAT root: H3772G/H/J and H3748 all share the karat root — the cutting/covenant-making/divorce/lacking vocabulary is generated from one root, spanning covenant-making, covenant-negation, and the absence of covenantal continuity. (3) SHAVA root: H7620I (week), H7650 (to swear), and H7621 (shevuah — oath) all share the sheva (seven) root — oath and week are lexically connected through the completeness/seven concept. (4) DIATHEKE root (Greek): G1242 (diathēkē) and G1303 (diatithēmi, XREF in R001) share the same root — covenant noun and covenant-making verb are etymologically one unit, though programme-structurally separated.
- Anchor verses: Neh 9:38, Heb 9:16-17
- Finding type: ETYMOLOGY

**Q&A-158 | T6.4.3**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.4 — Vocabulary and Root Sharing
- Prompt: 3 — What does vocabulary sharing reveal about the conceptual relationship between characteristics?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The vocabulary sharing reveals that covenant and faithfulness are not merely adjacent characteristics but lexically co-generated — they share the same root and therefore the same conceptual DNA. The 'firm covenant' (amanah) and 'faithfulness' (emunah) are not two separate inner-being realities that happen to be related; they are two aspects of the same root reality. A covenant is firm because it is grounded in faithfulness; faithfulness is the character quality that makes covenant possible and sustainable. This conceptual co-generation means that in the inner-being analysis, covenant and faithfulness should be understood as constitutively paired — neither is fully understood without the other. Similarly, the karat root reveals that covenant-making and covenant-dissolution are conceptually paired: the vocabulary of cutting encompasses both the establishing cut (karat berit) and the severing cut (divorce, cutting off). Covenant carries its negation within its own root vocabulary.
- Anchor verses: Neh 9:38, Gen 9:15
- Finding type: ETYMOLOGY

**Q&A-159 | T6.4.4**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.4 — Vocabulary and Root Sharing
- Prompt: 4 — If no significant vocabulary sharing is evidenced, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Vocabulary sharing is extensive and analytically significant. Q&A-156 through Q&A-158 substantive.

**Q&A-160 | T6.5.1**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.5 — Distinctions
- Prompt: 1 — Which adjacent characteristic most closely resembles this one — and what precisely distinguishes them?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The most closely adjacent characteristics from the co-occurrence and C17 cluster data are: (1) Hesed/love (R103, 37 shared verses): the closest structural neighbour. Distinction: covenant is the relational structure (the bond that holds commitment across time); hesed is the relational quality (the love that sustains the bond from within). Covenant without hesed is merely legal; hesed without covenant is unstable. The distinction is structural (covenant) vs. qualitative (hesed). This distinction is supported by Deu 7:9 — "keeps covenant and steadfast love" — where they are paired but distinguished. (2) Faithfulness (R060, 10 shared verses, XREF-connected via H0548): faithfulness is a character quality; covenant is the structured bond that faithfulness holds together. Faithfulness is the inner character of the covenant-keeping person; covenant is the formal framework within which that faithfulness is exercised. (3) Oath (H7621 in R019 — XREF, OBS-034-006): the oath is the performative speech act that constitutes the covenant; the covenant is the ongoing relational bond established by the oath. Oath is the entry mechanism; covenant is the resulting bond. Gap: the precise boundaries of these distinctions require Session D cross-registry analysis — the current data provides the directional finding but not the fully precise boundary definition. Per SB-9: cross-word synthesis conclusions not permitted; raising as SD pointers.
- Anchor verses: Deu 7:9, Neh 9:38
- Finding type: CROSS_REGISTRY
- Stage 2b note: SP raised for hesed-berit boundary (SP-034-003 already captures this). No new SP needed here; existing pointer covers it.

**Q&A-161 | T6.5.2**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.5 — Distinctions
- Prompt: 2 — Where the evidence shows apparent overlap, what is the precise boundary?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: Gap identified
- Answer: The hesed-covenant overlap is the most significant boundary question. From the available data: the overlap occurs in passages like Deu 7:9 where "keeping covenant and keeping steadfast love" (shomer haberit vehahesed) names them as parallel but distinct divine attributes. The distinction holds as: covenant = the structural bond (berit); hesed = the motivating quality (love/loyalty) that sustains the bond. The overlap occurs because hesed is what genuine covenantal commitment feels like from the inside — the willing, affective dimension of covenantal faithfulness. But covenant is not reducible to hesed (it includes the formal structure, oath, sign, and sanctions that hesed alone does not carry). Precise boundary: covenant is the form-with-content-and-structure; hesed is the inner relational quality. The boundary is kind-level (not degree-level) — they are different things that always co-occur in healthy covenantal life. Gap: whether this distinction holds uniformly across all 37 shared verses requires Session D cross-registry analysis (SP-034-003).
- Anchor verses: Deu 7:9
- Finding type: CROSS_REGISTRY

**Q&A-162 | T6.5.3**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.5 — Distinctions
- Prompt: 3 — Is the distinction a matter of degree, kind, direction, or constitutional level?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: (1) Covenant vs. hesed: distinction of kind — covenant is structural (bond), hesed is qualitative (love within the bond). Not degree; not direction. (2) Covenant vs. faithfulness: distinction of kind — covenant is the structure; faithfulness is the character quality sustaining the structure. (3) Covenant vs. oath: distinction of kind and direction — oath is the constituting act (entry-point, single moment); covenant is the resulting ongoing bond (sustained state). The oath is performative; the covenant is the standing relationship established by the oath. (4) Covenant vs. hope: distinction of constitutional level — covenant is the structural ground; hope is the inner-being orientation that arises from that ground. Covenant operates at the constitutional-structural level; hope operates at the orientation level. All four key distinctions are kind-level distinctions, not merely degree-level ones. The distinctions confirm that covenant is genuinely a distinct inner-being reality, not reducible to adjacent characteristics.
- Anchor verses: Deu 7:9
- Finding type: CROSS_REGISTRY

**Q&A-163 | T6.5.4**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.5 — Distinctions
- Prompt: 4 — If no significant distinction work is required, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: Distinction work is significant and required. Q&A-160 through Q&A-162 address it.

**Q&A-164 | T6.6.1**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.6 — Shared Verse Anchors
- Prompt: 1 — Does any verse in this characteristic's evidence base also function as a primary anchor in another characteristic's study?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — confirmed from §G.3 (OBS-034-032, OBS-034-033): Covenant shares 11 anchor verses with other registries. Key shared anchors: (1) Heb 8:10 — shared with R001 (abomination) and R112 (mind). (2) Neh 10:29 — shared with R019 (calling). (3) Eph 4:24 — shared with R076 (holiness). (4) Eph 2:12 — shared with R078 (hope) and R197 (authority). (5) Rom 1:31 — shared with R111 (mercy). (6) Dan 9:24 — shared with R147 (sin). (7) 2Ki 23:3 — shared with R159 (testimony). (8) 2Sa 23:5 — shared with R177 (worth). (9) Rev 2:17 — shared with R204 (name). (10) Isa 28:15 — shared with R078 (hope). These 11 shared-anchor relationships across 10 distinct registries confirm that covenant's anchor verses are structurally important to a wide range of programme registries — covenant is not isolated but serves as an anchor point for multiple inner-being characteristics.
- Anchor verses: Heb 8:10, Eph 2:12, Rom 1:31
- Finding type: CROSS_REGISTRY

**Q&A-165 | T6.6.2**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.6 — Shared Verse Anchors
- Prompt: 2 — What does the shared anchor reveal about the relationship between the two characteristics?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Three most analytically significant shared anchors: (1) Heb 8:10 shared with R001 (abomination) and R112 (mind): the new covenant's constitutional claim (law written on mind and heart) is an anchor for both the abomination and mind registries — revealing that the new covenant's inner inscription touches the cognitive inner-being territory that both registries engage. The fact that this verse anchors the abomination registry is unexpected and suggests that the abomination registry's engagement with this verse may be through the contrast between the abomination of old-covenant violation and the new-covenant remedy. Requires Session D investigation (SP-034-001 direction). (2) Eph 2:12 shared with R078 (hope) and R197 (authority): covenant and hope share this anchor, revealing that covenantal standing is the ground of hope (OBS-034-060) — and that authority-structures also anchor on this verse, suggesting that covenant intersects with authority in the domain of inclusion/exclusion from divine authority-structures. (3) Rom 1:31 shared with R111 (mercy): the covenantal defect (asunthetos) and mercy share an anchor — suggesting that the mercy registry engages the covenant-breaking context of Rom 1:31 as a site where mercy is absent, and that the covenant-mercy relationship requires cross-registry synthesis (SP-034-005).
- Anchor verses: Heb 8:10, Eph 2:12, Rom 1:31
- Finding type: CROSS_REGISTRY

**Q&A-166 | T6.6.3**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.6 — Shared Verse Anchors
- Prompt: 3 — If no shared verse anchors are identified, note this explicitly.
- Disposition: NOT APPLICABLE
- Status tag: N
- Rationale: 11 shared anchor relationships confirmed from §G.3. Q&A-164 and Q&A-165 substantive.

**Q&A-167 | T6.7.1**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.7 — Dimensional Sharing
- Prompt: 1 — How many of this characteristic's confirmed dimensions are shared with another characteristic in the programme?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: Gap identified
- Answer: Registry 034 (covenant) spans eight of the eleven programme dimensions across its 32 groups: RD (06), Volition (04), Moral Character (05), Transformation (08), Emotion-Negative (02), Vitality/Existence (07), Dependence/Creatureliness (10), Emotion-Positive (01). By definition, all programme registries assigned to the C17 cluster (relational-grace) share at minimum the RD dimension. Registries in other clusters that also engage Transformation (08) or Moral Character (05) dimensions would also share dimensions with R034. Without access to the dimension assignments of other registries (available to CC from the database), a precise count of dimension-sharing registries cannot be stated from the current data package. Gap: the precise dimensional sharing map requires CC database query. Recording as P — the directional finding is that covenant, spanning eight dimensions, is likely one of the widest-dimensional registries in the programme, and therefore shares dimensions with the largest number of other registries.
- Anchor verses: Jer 31:33, Deu 7:9
- Finding type: CROSS_REGISTRY

**SP-034-007** — raised T6.7, 2026-05-01, MEDIUM, Session D
- Target: All C17 registries and cross-cluster registries
- Connecting term: Multiple — all OWNER terms
- Question: Which other programme registries share each of covenant's eight dimensions? The dimensional sharing map for R034 would reveal which other words are analytically proximate in the inner-being landscape. CC should produce this map from the wa_dimension_index table. Session D needs this data for cross-registry synthesis entry T × T pairs.
- Evidence basis: Q&A-167, OBS-034-024
- Priority: MEDIUM

**Q&A-168 | T6.7.2**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.7 — Dimensional Sharing
- Prompt: 2 — What does the pattern of dimensional sharing reveal?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: From what can be inferred from the data: covenant's multi-dimensional span (8 of 11 programme dimensions) means it shares dimensions with a very wide range of registries across the programme. This is consistent with the DIM-34-SD001 hypothesis (covenant as C17 structural backbone) — the backbone characteristic would be expected to span the most dimensions and share dimensions with the most other registries. The pattern also reveals that covenant does not belong to a single inner-being domain but cuts across the relational, volitional, moral, transformative, emotional, vital, and creatureliness domains. This is not dimension-confusion (each group is correctly assigned to one primary dimension); it is dimensional comprehensiveness. Covenant engages the inner person across the widest constitutional range of any C17 characteristic. Gap: the specific sharing partners per dimension require CC data (SP-034-007).
- Anchor verses: OBS-034-024
- Finding type: CROSS_REGISTRY

**Q&A-169 | T6.7.3**
- Tier: T6 — Structural Relationships with Other Characteristics
- Component: T6.7 — Dimensional Sharing
- Prompt: 3 — If dimensional sharing data is not yet available, note this explicitly.
- Disposition: ANSWERED
- Status tag: A
- Notation: Gap identified
- Answer: Precise dimensional sharing counts require CC database query. The inferred pattern (covenant shares dimensions with the widest range of registries due to its 8-dimension span) is stated explicitly as an inference, not a confirmed finding. SP-034-007 raised for CC/Session D to supply the dimensional sharing map.
- Finding type: CROSS_REGISTRY

TIER T6 COMPLETE — Structural Relationships with Other Characteristics
Date: 2026-05-01
Prompts: 24 total. A: 13. P: 5. S: 0. N: 6.
New findings: 17. SD pointers raised: 1 (SP-034-007).


#### Tier 7 — Evidential and Methodological Foundation — 20 prompts

**Q&A-170 | T7.1.1**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 1 — What are the primary Hebrew and Greek terms — and what do their root meanings reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: Consistent with prior analysis
- Answer: Addressed comprehensively in Stage 2a (Unit 3, OBS-034-007 to OBS-034-023) and Stage 2b T1.1 (Q&A-014). Summary for T7: Hebrew primary terms — H1285 berit (root BARA, to eat — tentative; spans man-to-man and God-to-man relational bonds), H3772H karat (root KARAT, to cut — the covenant-making verb whose cutting idiom encodes the somatic enactment of commitment), H7650 shava (root SHAVA/seven — oath as sevenfold complete self-binding). Greek primary terms — G1242 diathēkē (root diatithēmi, to arrange/dispose — carries the testamentary dual meaning; will-testament that requires the testator's death). The root meanings collectively reveal: covenant is constituted through somatic enactment (cutting, blood), solemn self-binding speech (oath/seven), and arrangement/disposition (Greek: legal disposition with inheritance implications). The vocabulary is simultaneously relational, bodily, and legal at the root level.
- Anchor verses: Gen 9:15, Heb 9:16, Neh 10:29
- Finding type: ETYMOLOGY

**Q&A-171 | T7.1.2**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 2 — What is the grammatical range of the primary term — and what does that range reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: H1285 (berit): noun only — covenant is primarily a noun-reality, a state/bond rather than an action. The verb for covenant-making is a separate term (karat — to cut). This grammatical fact reveals that covenant is the standing relational reality (a state), not primarily the act of making it (an action). The act of making is expressed through the verb (karat berit = cut a covenant), but the covenant itself is a noun — it is what exists after the act. H7650 (shava): verb — swearing/oath-taking is an action, not primarily a state. This confirms that the oath is the performative act that constitutes the covenant. G1242 (diathēkē): noun — same as Hebrew; the covenant/testament is a standing reality. The noun-dominance of the primary covenant terms reveals that covenant is constituted through acts (cutting, swearing) but exists as a standing reality (the bond, the testament, the disposition). This noun-reality structure confirms the T1 finding (Q&A-016) that covenant is, in its sustained mode, a relational disposition rather than a repeated act.
- Anchor verses: Gen 9:15, Heb 8:10
- Finding type: ETYMOLOGY

**Q&A-172 | T7.1.3**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 3 — What is the semantic range of the primary term — across what breadth of meaning does it operate?
- Disposition: ANSWERED
- Status tag: A
- Notation: Consistent with prior analysis
- Answer: H1285 (berit) semantic range (from OBS-034-009): man-to-man (treaty, alliance, league; constitution/ordinance of monarch to subjects; agreement/pledge; alliance of friendship; alliance of marriage) and God-to-man (alliance of friendship; divine ordinance with signs and pledges). Also: covenant-making, covenant-keeping, covenant-violation (phrase senses). The range spans the full spectrum of solemn, binding relational commitments in both horizontal (social, political, marital) and vertical (divine-human) registers. G1242 (diathēkē) range: covenant (OT/LXX sense) and testamentary will (Hellenistic legal sense). The semantic breadth reveals that 'covenant' is not a specialist technical term for divine-human relations only — it encompasses the full range of committed human relational bonds. Its inner-being significance is therefore not limited to the religious register but applies across all solemn human commitments.
- Anchor verses: Gen 9:15, Heb 9:16, Neh 9:38
- Finding type: MEANING_OBSERVATION

**Q&A-173 | T7.1.4**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 4 — Does the vocabulary include terms that distinguish distinct aspects — disposition vs. act, received vs. given, condition vs. quality?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Yes — the vocabulary makes several such distinctions. (1) Disposition vs. act: berit (noun — the standing bond/disposition) vs. karat berit (verb phrase — the act of cutting/making). The vocabulary distinguishes the resulting reality from the constituting act. (2) Received vs. given: the vocabulary does not have separate terms for receiving vs. giving covenant, but the grammatical structure distinguishes them — God is subject of karat berit in 3304-001 (God gives); the human is subject in 3304-002 and 3304-004 (human gives). Direction is encoded in subject rather than term. (3) Condition vs. quality: the noun berit names the condition (the bond that exists); the karat and shava vocabulary names the quality of the act (the seriousness and binding character of the commitment). The oath vocabulary (H0423 alah, H7650 shava) encodes the moral quality of the covenant-making act — serious, self-binding, potentially self-cursing. (4) Negative form: H3748 keritut (divorce) names the condition of broken covenant; H3772J karat (to lack) names the negative of covenantal continuity. The vocabulary explicitly distinguishes positive and negative covenantal states.
- Anchor verses: Gen 9:15, Neh 10:29, Heb 9:38
- Finding type: ETYMOLOGY

**Q&A-174 | T7.1.5**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 5 — Does the vocabulary include a term for the structural opposite or absence of this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: Consistent with prior analysis
- Answer: Yes — explicitly. (1) H3748 keritut (divorce — the cutting of the marriage covenant — OBS-034-012): the formal opposite of covenant-union is named by a term from the same cutting root. Divorce is the covenant-opposite explicitly named by covenant's own vocabulary. (2) G0802 asunthetos (untrustworthy/covenant-breaker — OBS-034-018): the NT names the covenant-lacking character type with a specific term — asunthetos = not-placed-together = unable to hold covenants. The structural opposite (covenant-breaking as character defect) has its own lexical item in the NT. (3) H3772J karat (to cut: lack — OBS-034-015): the negative of covenantal continuity — being cut off is the covenant-opposite of being in continuous covenant relationship. (4) H0423 alah (the curse embedded in the oath — OBS-034-007): the sanction for covenant-absence is named within the covenant vocabulary itself. The vocabulary is internally comprehensive — it names both the positive reality and its negation.
- Anchor verses: Rom 1:31, Mal 2:14 direction
- Finding type: ETYMOLOGY

**Q&A-175 | T7.1.6**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 6 — Does the vocabulary include a person-type term — a term for the one who habitually possesses or exercises this characteristic?
- Disposition: PARTIALLY ANSWERED
- Status tag: P
- Notation: New finding / Gap identified
- Answer: The data contains one explicit person-type term adjacent to the covenant vocabulary. G0802 asunthetos (OBS-034-018) — the covenant-breaker as a character type — is a person-type term for the habitual absence of covenant faithfulness. However, a positive person-type term for the covenant-keeper (the habitually faithful covenant person) is not directly evidenced in the programme's vocabulary with a single dedicated term. The data does contain person-descriptions that function as person-type indicators: "those who love him and keep his commandments" (Deu 7:9), "those who keep his covenant and his testimonies" (Psa 25:10) — but these are phrases, not dedicated lexical items. Gap: a dedicated positive person-type term for the covenant-faithful person is not identified in the programme's term inventory. The negative person-type (asunthetos) is named; the positive is described but not lexically fixed.
- Anchor verses: Rom 1:31, Deu 7:9, Psa 25:10
- Finding type: MEANING_OBSERVATION

**Q&A-176 | T7.1.7**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 7 — Does the vocabulary include a supplication term — a term for the act of seeking this characteristic from another?
- Disposition: NOT ANSWERED
- Status tag: S
- Notation: Gap identified
- Answer: Stage 2a observations do not identify a dedicated supplication term for seeking covenant from another in the programme's vocabulary. The verse evidence contains prayers that reference covenant (Dan 9:4-11 — OBS-034-036; Psa 25:10-14), but these are not designated as seeking-covenant terms in the programme's term inventory. No specific supplication term for seeking covenant is identified. Recording as S — inherent data gap; not a Stage 2a reopening item.

**Q&A-177 | T7.1.8**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 8 — What does the LXX use of the vocabulary reveal about continuity or development across the Testaments?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The LXX translation of Hebrew berit as Greek diathēkē is the most significant lexical development in the covenant vocabulary's inter-Testament history. The choice of diathēkē rather than synthēkē (agreement, compact) for berit is deliberate and theologically loaded: diathēkē carries the testamentary meaning (will/testament) that synthēkē does not. The LXX translators, by choosing diathēkē, imported the inheritance-and-death dimension into covenant language. This choice — confirmed authoritative in the NT's explicit exploitation of the testamentary sense (Heb 9:16-17 — OBS-034-069) — reveals that the OT-to-NT development of the covenant vocabulary is not merely a translation but a semantic enrichment: the Greek term adds the legal dimension of inheritance through the testator's death to the Hebrew covenantal bond. The continuity: same relational bond (berit = diathēkē) with deepened semantic content (inheritance through death). The development: the NT reads this as anticipating the new covenant's enactment through Christ's death — the LXX translation itself participates in the typological movement from OT to NT.
- Anchor verses: Heb 9:16-17, Mat 26:28
- Finding type: ETYMOLOGY

**Q&A-178 | T7.1.9**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 9 — Is there a term newly coined in the NT period for this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: G0802 (asunthetos — untrustworthy/covenant-breaker — OBS-034-018) appears to be a distinctive NT-period term for the covenant-breaking character quality. While the word's components are classical Greek, its appearance in Paul's vice-catalogue (Rom 1:31) as a moral character term within a NT theological context is the word's most prominent biblical use. It represents the NT's naming of covenant-faithlessness as a specific moral character defect — giving an explicit lexical label to what the OT described through narrative and prophetic denunciation. The other NT-specific development is not a newly coined term but a newly deployed term: diathēkē in its testamentary sense (Heb 9:16-17) exploits an existing Greek legal term for theological purposes — not a coinage but a semantic deployment that generates a new theological meaning-range for an existing word.
- Anchor verses: Rom 1:31, Heb 9:16
- Finding type: ETYMOLOGY

**Q&A-179 | T7.1.10**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.1 — Lexical and Semantic Analysis
- Prompt: 10 — What does the full vocabulary arc reveal about this characteristic's complete semantic range?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The full vocabulary arc from Hebrew to Greek to NT reveals a semantic trajectory of deepening and enrichment. At the Hebrew level (berit, karat, shava, alah, amanah): covenant is the solemn, self-binding relational bond constituted through somatic enactment (cutting, blood) and speech (oath), with embedded sanctions (curse), and rooted in faithful character (amanah-emunah). At the Greek level (diathēkē, asunthetos, kainos): covenant becomes also a testamentary inheritance (diathēkē), the new covenant is qualitatively unprecedented (kainos), and covenant-faithlessness is named as a character defect (asunthetos). The full arc reveals: covenant is simultaneously (1) relational — a bond between persons; (2) bodily — enacted through blood, cutting, circumcision; (3) oral — constituted through sworn speech; (4) legal — carrying sanctions, obligations, and inheritance provisions; (5) moral — requiring and producing faithful character; (6) transformative — producing new inner constitution (new covenant); (7) eschatological — oriented toward eternal inheritance and new creation. No single term carries all seven dimensions; the full vocabulary arc is required to see the complete semantic range.
- Anchor verses: Gen 9:15, Deu 7:9, Heb 9:16, Jer 31:33, Heb 13:20
- Finding type: ETYMOLOGY

**Q&A-180 | T7.2.1**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.2 — Verse and Literary Interpretation
- Prompt: 1 — What is the function of this characteristic's primary term within its primary verse?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The primary term is berit (H1285) and the primary verse for the new covenant trajectory is Jer 31:33 / Heb 8:10. In Heb 8:10: "For this is the covenant that I will make with the house of Israel after those days, declares the Lord: I will put my laws into their minds, and write them on their hearts." The term diathēkē (covenant) functions as the subject-predicate complement — "this is the covenant" introduces what follows as the covenant's definition. The term anchors the verse's argument: what follows ("I will put my laws into their minds") is the definition of what 'new covenant' means. The word 'covenant' here is not incidental but the category that controls the meaning of the entire pericope — it is the explanatory framework for the inscription act that follows. Function: definitional anchor — the term controls what the verse reveals about the new covenant's content and mode.
- Anchor verses: Heb 8:10, Jer 31:33
- Finding type: VERSE_ANNOTATION

**Q&A-181 | T7.2.2**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.2 — Verse and Literary Interpretation
- Prompt: 2 — What literary form carries the primary verse evidence — and what does that form require for responsible interpretation?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The covenant vocabulary spans four primary literary forms in the data: (1) Legal/contractual narrative (Torah — Exo 24, Deu 7, Gen 9): the covenant is made in narrative context with formulaic legal-treaty elements (terms, signs, witnesses, sanctions). Responsible interpretation requires attention to the ancient Near Eastern treaty context and the formal elements of covenant-making, not merely the spiritual meaning. (2) Prophetic oracle (Jer 31:31-34; Isa 54; 59): the new covenant promise is in the form of divine oracle — first-person divine declaration. Requires treating these as authoritative divine speech-acts, not merely poetic expressions. (3) Epistle and theological argument (Heb, Gal, 2 Cor): the NT covenant material is embedded in theological argumentation. Hebrews especially builds a sustained typological argument from OT texts. Responsible interpretation requires following the logical-theological argument, not proof-texting individual verses. (4) Liturgical (1 Cor 11:25; Mat 26:28): the Eucharistic institution narrative is liturgical-formular. Responsible interpretation requires reading within the covenant-meal tradition, not as isolated doctrine.
- Anchor verses: Gen 9:15, Jer 31:31, Heb 8:8, 1 Cor 11:25
- Finding type: VERSE_ANNOTATION

**Q&A-182 | T7.2.3**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.2 — Verse and Literary Interpretation
- Prompt: 3 — What is the logical structure of key arguments in the verse evidence?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Three key logical structures: (1) Hebrews 8:7-10 argument: premise — "if the first covenant had been faultless, there would have been no occasion for a second" (Heb 8:7); evidence — God himself found fault (Heb 8:8); conclusion — a new covenant was necessary; content — the new covenant's defining feature is inner inscription (Heb 8:10). The argument moves from covenant failure → divine acknowledgment → necessity of new covenant → new covenant's constitutional mode. (2) Galatians 3:15-17 argument: premise — "even with a man-made covenant, no one annuls it once ratified" (Gal 3:15 — OBS-034-068); application — God's covenant with Abraham was ratified before the law; conclusion — the law 430 years later cannot annul the Abrahamic covenant. The argument uses the legal-covenant (diathēkē as will) logic to defend the priority of promise over law. (3) 2 Cor 3:6-14 argument: premise — God made us ministers of a new covenant; contrast — old (letter/death/condemnation) vs. new (Spirit/life/righteousness); conclusion — the new covenant is of surpassing glory. The argument from covenant to cognitive transformation (veil-lifting) is a logical consequence of the Spirit's operation.
- Anchor verses: Heb 8:7-10, Gal 3:15-17, 2 Cor 3:6-14
- Finding type: VERSE_ANNOTATION

**Q&A-183 | T7.2.4**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.2 — Verse and Literary Interpretation
- Prompt: 4 — What contextual setting carries the primary verse evidence?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: The primary covenant verse evidence is overwhelmingly covenantal-cultic in its contextual setting — which is to say, the verse evidence is typically embedded within the explicit covenantal life of the worshipping community. The primary settings: (1) Covenantal — the covenant renewals, covenant-making ceremonies, and covenant oracles are the primary covenantal-formal context (Exo 24; Deu 29; Neh 9-10; Jer 31; Heb 8). (2) Judicial — Dan 9:11 (the covenant curse activated by moral failure); Heb 10:29 (the judgment for profaning the covenant blood). The covenant operates within a judicial framework that enforces its sanctions. (3) Liturgical — 1 Cor 11:25; Mat 26:28 (the Eucharistic words of institution). The covenant is enacted and recalled within the worshipping community's ritual. (4) Eschatological — Rev 11:19 (the ark in the heavenly temple); Rev 21:1-5 (new creation). What this combination of settings reveals: covenant is not abstract theology but embedded in the concrete practices of worship, law, and community life.
- Anchor verses: Exo 24:8, Neh 10:29, 1 Cor 11:25, Rev 11:19
- Finding type: VERSE_ANNOTATION

**Q&A-184 | T7.2.5**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.2 — Verse and Literary Interpretation
- Prompt: 5 — Does any verse function as the primary anchor for this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Two verses make the strongest claim to primary anchor status, representing the two primary covenantal trajectories. (1) Jer 31:33 / Heb 8:10 — "I will write my law on their hearts" — is the primary anchor for the inner-being dimension of covenant. It is the verse that most directly and completely states what covenant does to the inner person — the new covenant's constitutional inscription on the heart is the most precise and significant inner-being claim in the entire registry. It is also the verse with the widest cross-registry significance (shared anchor with R001 and R112; OBS-034-032). (2) Deu 7:9 — "the faithful God who keeps covenant and steadfast love" — is the primary anchor for the relational-disposition dimension, naming the hesed-berit pair and grounding covenant in God's inner faithfulness. For the inner-being analysis, Jer 31:33 / Heb 8:10 is the single most important verse — it names the heart as the constitutional site of the new covenant's operation and defines the transformation trajectory that DIM-34-001 identified as the analytical priority.
- Anchor verses: Jer 31:33, Heb 8:10, Deu 7:9
- Finding type: VERSE_ANNOTATION

**Q&A-185 | T7.2.6**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.2 — Verse and Literary Interpretation
- Prompt: 6 — What does the primary anchor verse reveal that no other verse reveals?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Jer 31:33 / Heb 8:10 reveals uniquely that God's covenantal action targets the inner constitutional organs (mind and heart) directly — that the new covenant is not a new external legal code but a new mode of inner operation where God himself inscribes his law on the person's inner organs. No other verse in the registry states this constitutional claim as directly: it names the specific organs (mind, heart), the specific action (writing, inscribing), the specific content (God's laws), and the specific agent (God himself). The verse also uniquely links the constitutional inscription to the relational formula ("I will be their God and they shall be my people") and to the cognitive outcome ("they shall all know me"). The sequence — inscription → belonging → knowing — is stated explicitly only here. This makes Jer 31:33 / Heb 8:10 the irreplaceable anchor verse for the entire inner-being analysis of covenant: no other verse carries all four elements simultaneously (constitutional site, divine action, relational outcome, cognitive product).
- Anchor verses: Jer 31:33, Heb 8:10
- Finding type: VERSE_ANNOTATION

**Q&A-186 | T7.3.1**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.3 — Human Science Frameworks
- Prompt: 1 — Which human science framework is most useful as an interpretive lens for this characteristic?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Two frameworks are most useful, addressing different dimensions of covenant. (1) Attachment theory (developmental psychology / relational psychology): covenant is structurally analogous to what attachment theory describes as a secure attachment bond — a stable, reliable relational connection that provides the inner-being conditions for exploration, formation, and flourishing. The covenant's constituting of belonging ("I will be their God") and the conditions it creates for inner hope, identity, and knowing (Jer 31:34) map closely onto what attachment theory identifies as the effects of secure attachment. This framework illuminates the relational-psychological dimension of covenant's inner-being function. (2) Contract and covenant theory (social philosophy / political philosophy / legal theory): the distinction between contract (exchange of equal obligations between independent parties) and covenant (bond of committed loyalty that constitutes a relationship, typically with asymmetric parties) is directly relevant to covenant's inner-being structure. The biblical covenant is explicitly not a contract (OBS-034-002 — "not a contract between equals"). Covenant theory illuminates the structural asymmetry (God initiates, human responds), the constitutive (not merely regulative) character of the bond, and the role of obligation within relationship.
- Anchor verses: Heb 8:10, Gen 9:15, Deu 7:9
- Finding type: OBSERVATION

**Q&A-187 | T7.3.2**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.3 — Human Science Frameworks
- Prompt: 2 — Where the human science framework illuminates the verse evidence, what does it reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: (1) Attachment theory illuminates: the inner-being consequences of covenantal exclusion (Eph 2:12 — "having no hope and without God in the world" — OBS-034-060) map precisely onto what attachment theory identifies as the consequences of insecure or absent attachment — anxiety, hopelessness, relational incapacity, and identity fragility. The biblical language of covenantal desolation is psychologically coherent with the attachment literature. Conversely, covenant inclusion produces the inner conditions for hope, knowing, and secure identity — which attachment theory would predict from secure attachment. (2) Covenant-vs-contract distinction illuminates: the new covenant's unilateral divine initiative (God writes, God sends the Spirit — OBS-034-059, OBS-034-061) is consistent with covenant (constituted by the stronger party's commitment) rather than contract (requiring equal agency). This illuminates why the new covenant cannot be violated by the human party without God's covenant remaining in force from his side — God's covenant is not contingent on human performance.
- Anchor verses: Eph 2:12, Heb 8:10, Jer 31:33
- Finding type: OBSERVATION

**Q&A-188 | T7.3.3**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.3 — Human Science Frameworks
- Prompt: 3 — Where the verse evidence and the human science framework diverge, what does the divergence reveal?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: Two divergences are analytically significant. (1) Attachment theory limits: attachment theory describes the effects of human-to-human relational bonds and their development in early childhood. Biblical covenant operates primarily in the vertical (divine-human) register and involves a party who is categorically different from the human — omnipotent, omniscient, self-sworn. Attachment theory cannot account for the constitutional transformative dimension of the new covenant (God writing on the heart, Spirit-administration) — this is not a relational-psychological process but a theological reality with no human-science analogue. The divergence reveals that covenant is not reducible to attachment — it is a theological category that subsumes psychological analogues without being explained by them. (2) Contract theory limits: contract theory assumes parties who are independent, equal, and self-interested. Biblical covenant operates between parties who are radically unequal (God and human), and the covenant's terms are not negotiated but declared by the stronger party out of commitment and love, not mutual self-interest. The divergence reveals that covenant is a category of a different kind from contract — it is constituted by love and faithfulness, not by interest-exchange.
- Anchor verses: Gen 9:15, Heb 8:10, Jer 31:33
- Finding type: OBSERVATION

**Q&A-189 | T7.3.4**
- Tier: T7 — Evidential and Methodological Foundation
- Component: T7.3 — Human Science Frameworks
- Prompt: 4 — Does the human science framework surface any aspect not yet addressed — requiring further verse investigation?
- Disposition: ANSWERED
- Status tag: A
- Notation: New finding
- Answer: One area is surfaced by the attachment framework that has not been directly addressed in the verse evidence: the developmental dimension of covenant formation in infancy and childhood. Attachment theory identifies the primary formative period for relational-bond formation as early childhood. The biblical covenant vocabulary's generational dimension (circumcision from infancy, covenant transmitted through the mouths of children — Isa 59:21 — OBS-034-051) touches this developmental question, but the programme's verse set does not address how covenant formation operates in the inner person across childhood development. The gap is inherent to the data's focus on adult covenant contexts and is not a Stage 2a reopening item. This is a question for the human-science / biblical theology intersection that lies beyond the current analytical scope.
- Finding type: OBSERVATION

TIER T7 COMPLETE — Evidential and Methodological Foundation
Date: 2026-05-01
Prompts: 20 total. A: 17. P: 1. S: 1. N: 1.
New findings: 15. SD pointers raised: 0.
S-status prompts: T7.1.7 (supplication term) — inherent data gap.


---

## Stage 2b — Second-Tier Catalogue Summary

### Status Code Totals Across T0–T7

| Tier | Total Prompts | A | P | S | N |
|---|---|---|---|---|---|
| T0 | 12 | 9 | 1 | 0 | 2 |
| T1 | 24 | 20 | 2 | 0 | 2 |
| T2 | 31 | 19 | 4 | 0 | 8 |
| T3 | 33 | 27 | 2 | 3 | 1 |
| T4 | 24 | 14 | 2 | 3 | 5 |
| T5 | 21 | 15 | 1 | 0 | 5 |
| T6 | 24 | 13 | 5 | 0 | 6 |
| T7 | 20 | 17 | 1 | 1 | 1 |
| **TOTAL** | **189** | **134** | **18** | **7** | **30** |

**Answered rate (A):** 134/189 = 70.9%
**Partial rate (P):** 18/189 = 9.5%
**Not answered rate (S):** 7/189 = 3.7%
**Not applicable rate (N):** 30/189 = 15.9%
**Coverage (A+P of applicable prompts):** 152/159 = 95.6%

### S-Status Prompts Consolidated

- T3.5.1, T3.5.2, T3.5.3 — Creativity faculty: no evidence of covenant engaging the creative/imaginative faculty. Inherent data gap; analytically meaningful (covenant operates in juridical-relational-cognitive register, not creative register).
- T4.6.1 — Spiritual beings operating in relation to covenant: data silent. Inherent gap.
- T4.6.3 — Angelic mediation of covenant: data silent. Inherent gap.
- T7.1.7 — Supplication term (a term for seeking covenant from another): no dedicated term identified. Inherent gap.

Total: 7 S-status prompts. None require Stage 2a reopening — all are inherent data gaps or domain absences confirmed as analytically significant.

### New Findings Consolidated

1. Covenant is structurally composite — four inner-being modes: relational disposition (God), volitional act (human entry), moral character quality (human keeping), constitutional condition (new covenant reception) (Q&A-016)
2. Covenant has a five-element constituent structure: parties, commitment mechanism, covenantal content, sign/seal, sanctions (Q&A-017)
3. Primary dimension: Relational Disposition (06) — proposed sb_classification for Registry 034 (Q&A-034, Q&A-035)
4. Covenant operates through speech as constitutive mode — the oath as performative covenant act (Q&A-024)
5. The new covenant sequence: failure → divine initiative → inner inscription → belonging → knowing (Q&A-128, Q&A-129)
6. Two distinct change mechanisms: external-demand (Sinai) vs. internal-inscription (new covenant) — "not of the letter but of the Spirit" (Q&A-131, Q&A-132)
7. Constitutional movement pattern: OT = outer→inner→outer; new covenant = inner→inner→outer (Q&A-066)
8. Origin of covenant changes across the trajectory: unilateral divine (Noahic) → bilateral with human consent (Sinai) → generational transmission (Davidic) → internal Spirit-generation (new covenant) (Q&A-064)
9. Heart is the primary constitutional location, engaging all four integrating functions: knowing, willing, moral awareness, and affective experience (Q&A-044, Q&A-045)
10. Mind is co-location with heart in the new covenant (Heb 8:10; Heb 10:16); can also be veiled/hardened (2 Cor 3:14) (Q&A-047, Q&A-048)
11. Memory is one of the most structurally prominent inner faculties — both divine and human memory are structurally engaged; covenant is constitutively temporal (Q&A-074, Q&A-076)
12. Cognition is a primary target and product of the new covenant — "they shall all know me" is the covenant's telos (Q&A-073)
13. Covenant is the primary structuring reality for conscientious inner life — "with all your heart and all your soul" is total conscientiousness (Q&A-097)
14. Covenant is form; relational capacity is content — the reciprocal finding of T3.11 (Q&A-100)
15. God-to-human interface: five modes — establishment, commitment of faithfulness, constitutional inscription, oath-binding, mediation through Christ (Q&A-101)
16. Covenant produces: knowing God, hope, faithfulness, freedom, sanctification (Q&A-152)
17. Covenant is constitutively prior to the characteristics it enables — its sequential-causal relationships with love, hope, knowing, and new-self reveal it as the condition of possibility for C17 vocabulary (Q&A-150)
18. Covenant and faithfulness (emunah-amanah) are lexically co-generated from the same root — not merely adjacent but constitutively paired (Q&A-158)
19. The LXX translation of berit as diathēkē imports the testamentary/death dimension into covenant language — this enrichment is theologically exploited in Heb 9:16-17 (Q&A-177)
20. Full vocabulary arc reveals seven simultaneous dimensions: relational, bodily, oral, legal, moral, transformative, eschatological (Q&A-179)
21. Jer 31:33 / Heb 8:10 is the irreplaceable primary anchor verse — uniquely states constitutional site (heart/mind), divine action (writing), relational outcome (belonging), and cognitive product (knowing) together (Q&A-185, Q&A-186)
22. Attachment theory illuminates covenantal inclusion/exclusion effects; covenant-vs-contract distinction illuminates asymmetric divine initiative (Q&A-186, Q&A-187)

---

### SD Pointer Review (Stage 2b complete)

All SD pointers reviewed per instruction:

**SP-034-001** (R001 — G1303): Question precisely stated. Target registry identified. Evidence: OBS-034-003. Priority MEDIUM — appropriate. Not a duplicate of existing DB record. CONFIRMED.

**SP-034-002** (R159 — H5715): Question precisely stated. Target: R159. Evidence: OBS-034-005, §G.3. Priority MEDIUM. CONFIRMED.

**SP-034-003** (R103 — hesed-berit nexus): Question precisely stated. Critical for C17 synthesis. Evidence: OBS-034-029, OBS-034-039, Q&A-150, Q&A-154. Priority HIGH — appropriate. CONFIRMED.

**SP-034-004** (R112 — covenant-mind): Question precisely stated. Evidence: OBS-034-029, OBS-034-030, OBS-034-040, OBS-034-059. Priority HIGH. CONFIRMED.

**SP-034-005** (R111 — mercy, Rom 1:31): Question precisely stated. Evidence: OBS-034-033, §G.3. Priority MEDIUM. CONFIRMED.

**SP-034-006** (R117 — peace, berit-shalom): Question precisely stated. Evidence: OBS-034-034, PH2-34-004. Priority MEDIUM. CONFIRMED.

**SP-034-007** (CC — dimensional sharing map): Question precisely stated. Target: CC database query. Evidence: Q&A-167, OBS-034-024. Priority MEDIUM. CONFIRMED.

SD Pointer review complete. 7 pointers confirmed. 0 refined. 0 merged. 0 new (SP-034-007 already recorded above).

### Existing Findings Review

DIM-34-001 (DIMENSION_REVIEW, pending): confirmed in Stage 2a Unit 9 and substantiated throughout Stage 2b T5 (Q&A-125 through Q&A-133). The transformation trajectory is the most extensively evidenced finding in the registry. DIM-34-001 is fully resolved through Q&A work — marking as addressed in Stage 2b. No supersession or set-aside required; the finding is confirmed and deepened.

No existing findings questioned or set aside. None require SUPERSEDE or SET_ASIDE blocks.

---

```
STAGE 2B COMPLETE — Registry 034 (covenant)
Date: 2026-05-01
Tiers processed: T0 through T7 (8 tiers)
Prompts: 189 total. Answered: 134. Partially answered: 18. Not applicable: 30. Not answered (S): 7.
New findings recorded in obslog: 22 (plus many Adds structure / Consistent with prior analysis)
Catalogue links recorded in obslog: 189 entries
SD pointers in accumulator: 7 (SP-034-001 through SP-034-007)
evidential_status set on all active OWNER terms: deferred to CC — no wa_session_b_findings.evidential_status update mechanism visible in obslog-to-CC flow; flagging for CC to set

Stage 2c may begin.
```


---

## Stage 2c — Synthesis Entries

### Intra-Tier Pass (T1–T7)

**SYN-INTRA-034-001** | T1 — Definition
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T1
- Components considered: T1.1, T1.2, T1.3, T1.4, T1.5, T1.6, T1.7, T1.8
- Source Q&A: Q&A-013, Q&A-016, Q&A-018, Q&A-022, Q&A-028, Q&A-034
- Outcome: D
- Finding: T1 as a whole reveals that covenant is constitutively architectural — it is not a characteristic that exists on its own terms but one that structures the conditions within which other inner-being characteristics operate. Its working description (Q&A-018) names it as "the solemn, binding relational bond... the structured architecture of faithful relationship." Its primary dimension is Relational Disposition (Q&A-034), but its four modes of operation (disposition, act, quality, condition — Q&A-016) and its composite structure (five constituent elements — Q&A-017) reveal that covenant is genuinely multi-modal. No other characteristic in the programme is described as simultaneously a disposition, an act, a quality, and a condition — this four-modal nature is unique to covenant and is what makes it architecturally prior to other C17 characteristics. T1 establishes that covenant is not one inner-being characteristic among equals but the structural framework within which the relational-grace vocabulary of C17 operates.
- Session C chapter: Ch1
- SD pointer: NONE

T1 intra-tier COMPLETE: 2026-05-01. Outcome: D.

---

**SYN-INTRA-034-002** | T2 — Constitutional Location and Boundaries
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T2
- Components considered: T2.1, T2.2, T2.3, T2.4, T2.5, T2.6, T2.7, T2.8, T2.9, T2.10
- Source Q&A: Q&A-044, Q&A-047, Q&A-053, Q&A-064, Q&A-065, Q&A-066
- Outcome: D
- Finding: T2 as a whole reveals that covenant operates across the full constitutional range of the inner person with no single exclusive location. The heart is the primary site (Q&A-044), the mind is co-located (Q&A-047), the soul gives totality of engagement (Q&A-041), the mouth is the expressive-constitutive organ (Q&A-050), and the body participates through blood and circumcision (Q&A-053). The single most structurally significant T2 finding is the constitutional movement shift from OT to NT covenantal mode: OT covenant moves outer→inner→outer; new covenant moves inner→inner→outer (Q&A-066). This movement-shift is the constitutional-level expression of the Sinai-to-new-covenant transformation — it places the origin of covenant faithfulness at the level of God's own interior action within the person rather than the person's compliance with external demand. T2 confirms that covenant is constitutively somatic as well as inner — it cannot be reduced to a purely invisible spiritual reality because it is enacted, sealed, and transmitted through bodily acts and substances.
- Session C chapter: Ch2
- SD pointer: NONE

T2 intra-tier COMPLETE: 2026-05-01. Outcome: D.

---

**SYN-INTRA-034-003** | T3 — The Inner Faculties
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T3
- Components considered: T3.1, T3.2, T3.3, T3.4, T3.5, T3.6, T3.7, T3.8, T3.9, T3.10, T3.11
- Source Q&A: Q&A-073, Q&A-076, Q&A-083, Q&A-085, Q&A-097, Q&A-100
- Outcome: D
- Finding: T3 as a whole reveals that covenant comprehensively engages the inner faculties but with a specific structural bias: the faculties it most deeply and richly engages are those oriented toward the Other (relational capacity, memory, cognition as knowing-God, moral evaluation, conscientiousness) rather than those oriented inward (creativity, which is notably absent). This faculty-engagement pattern is coherent with covenant's relational-disposition primary classification — covenant is constitutively Other-oriented and therefore engages the Other-oriented faculties most richly. The deepest T3 finding is the developmental one: the old covenant calls for volition from outside (demands obedience); the new covenant transforms volition from inside (liberates and enables faithfulness through Spirit). This volitional trajectory is confirmed across T3.6 (volition) and T3.7 (agency) and is the faculty-level expression of the same transformation that T2 identified at the constitutional-movement level and T5 identifies at the mechanism level. All three tiers point to the same inner-being reality from different analytical vantage points.
- Session C chapter: Ch2
- SD pointer: NONE

T3 intra-tier COMPLETE: 2026-05-01. Outcome: D.

---

**SYN-INTRA-034-004** | T4 — Relational Interfaces
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T4
- Components considered: T4.1, T4.2, T4.3, T4.4, T4.5, T4.6
- Source Q&A: Q&A-101, Q&A-102, Q&A-105, Q&A-109, Q&A-117, Q&A-119
- Outcome: D
- Finding: T4 as a whole reveals that covenant's relational interface structure is asymmetric but genuinely bilateral. The God-to-human direction (T4.1) is the founding and sustaining axis — God initiates, commits, inscribes, and mediates. The human-to-God direction (T4.2) is the responsive axis — the whole person moves toward God through commitment, love, and faithfulness. The horizontal directions (T4.3 giving; T4.4 receiving) are genuine but secondary, and the evidence shows they are grounded in and enabled by the vertical. The relational scope expands progressively across the covenant trajectory — from particular (Abraham) to expanding (Israel) to universal (new covenant in Christ). The spiritual-beings interface (T4.6) is largely absent from the data — the only relevant material is the pagan deity named "lord of covenant" (H1286) and the inferred adversarial spiritual claim. T4 as a whole shows that covenant's relational architecture is constituted by God's prior initiative and realised through the whole person's responsive engagement.
- Session C chapter: Ch3
- SD pointer: NONE

T4 intra-tier COMPLETE: 2026-05-01. Outcome: D.

---

**SYN-INTRA-034-005** | T5 — Formative and Developmental Dimension
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T5
- Components considered: T5.1, T5.2, T5.3, T5.4, T5.5, T5.6, T5.7
- Source Q&A: Q&A-125, Q&A-128, Q&A-131, Q&A-134, Q&A-137, Q&A-140, Q&A-143
- Outcome: D
- Finding: T5 as a whole reveals that covenant is the most developmentally comprehensive of all characteristics in the programme's scope — it operates across all stages of formation (entry, formation, sanctification, eschatological fullness) and all scales of time (individual, generational, covenantal-historical, eschatological). The defining T5 finding is the two-mechanism contrast (Q&A-131): the Sinai covenant uses the external-demand mechanism (discipline and instruction); the new covenant uses the internal-inscription mechanism (Spirit-writing from within). This mechanism shift is not merely methodological — it represents a change in what the covenant does to the inner person. Under the old covenant, the person is required to bring their will to the covenant; under the new, the covenant brings a transformed will to the person. T5 confirms that covenant is not a static reality but a developing one — it moves through a sequence of inner states (Q&A-128: failure → initiative → inscription → belonging → knowing), and its eschatological trajectory points toward a fullness not yet realised but already grounded in the eternal covenant (Heb 13:20).
- Session C chapter: Ch4
- SD pointer: NONE

T5 intra-tier COMPLETE: 2026-05-01. Outcome: D.

---

**SYN-INTRA-034-006** | T6 — Structural Relationships
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T6
- Components considered: T6.1, T6.2, T6.3, T6.4, T6.5, T6.6, T6.7
- Source Q&A: Q&A-147, Q&A-150, Q&A-152, Q&A-157, Q&A-160, Q&A-164
- Outcome: D
- Finding: T6 as a whole confirms the DIM-34-SD001 hypothesis: covenant is structurally prior to and constitutive of the other C17 characteristics. The sequential and causal findings (Q&A-149, Q&A-150) show that covenant precedes and produces love/hesed (as the structure that makes sustained hesed possible), hope (as the ground of inner hope), knowing God (as the telos of covenant inscription), and the new self (as the constitutional outcome of new covenant reception). The vocabulary and root sharing (Q&A-157, Q&A-158) reveals that covenant and faithfulness are lexically co-generated — they share the same root and are constitutively paired. The co-occurrence data (Q&A-147) shows covenant occupying a central hub position in the inner-being landscape — co-present with the widest range of characteristics across multiple dimensions. T6 as a whole establishes that covenant is not one characteristic in a relational cluster but the architectural backbone of the cluster — the structural condition of possibility for the other C17 characteristics.
- Session C chapter: Ch5
- SD pointer: NONE

T6 intra-tier COMPLETE: 2026-05-01. Outcome: D.

---

**SYN-INTRA-034-007** | T7 — Evidential and Methodological Foundation
- Entry type: SYNTHESIS_INTRA_TIER
- Tier: T7
- Components considered: T7.1, T7.2, T7.3
- Source Q&A: Q&A-177, Q&A-179, Q&A-184, Q&A-185, Q&A-186
- Outcome: D
- Finding: T7 as a whole reveals that the covenant vocabulary is one of the most lexically rich and methodologically demanding in the programme. The full vocabulary arc (Q&A-179) shows seven simultaneous semantic dimensions (relational, bodily, oral, legal, moral, transformative, eschatological) that require the complete term inventory to see — no single term carries all seven. The LXX translation choice (diathēkē over synthēkē — Q&A-177) is a theological-methodological decision that imports the testamentary/death dimension into covenant language and is directly exploited by the NT. The primary anchor verse (Jer 31:33 / Heb 8:10 — Q&A-185) is uniquely comprehensive — it states simultaneously the constitutional site, the divine action, the relational outcome, and the cognitive product. The human science frameworks (Q&A-186, Q&A-187) illuminate specific dimensions (attachment, covenant-vs-contract) but diverge from the biblical material at the point of covenant's theological uniqueness — God's unilateral initiative, constitutional transformation, and eschatological scope are not captured by any human science framework. T7 confirms that the analysis rests on solid evidential and methodological ground, while acknowledging the inherent limitations of the 9% G1242 verse coverage and the legacy-VC status of all 15 OWNER terms.
- Session C chapter: multiple: Ch1, Ch2, Ch3, Ch4, Ch5
- SD pointer: NONE

T7 intra-tier COMPLETE: 2026-05-01. Outcome: D.

Intra-tier pass COMPLETE: 2026-05-01. D: 7. F: 0. N: 0. Total: 7.


### Inter-Tier Pass (T1–T7, 21 pairs)

**SYN-INTER-034-008** | T1 × T2
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T1, T2
- Source Q&A: Q&A-016, Q&A-018, Q&A-044, Q&A-066
- Outcome: D
- Finding: T1 defines covenant as constitutively composite — operating in four modes (disposition, act, quality, condition). T2 reveals that each mode has a distinct constitutional location: the disposition-mode (God's relational commitment) operates at the deepest constitutional level (spirit/relational), the act-mode (human entry) is enacted through somatic performance (oath = mouth, cutting = body, blood), the quality-mode (moral faithfulness) resides in heart and character, and the condition-mode (new covenant transformation) is inscribed on heart and mind by divine action. The T1 × T2 synthesis: covenant's four modes correspond to four distinct constitutional locations and operations, and the new covenant's primary contribution is shifting the constitutional origin from external to internal — the condition-mode is not entered by human act but produced by God's inner writing. The composite mode structure (T1) is constitutionally grounded across the full inner person (T2).
- Structural relationship: constitutive
- Session C chapter: Ch2
- SD pointer: NONE

**SYN-INTER-034-009** | T1 × T3
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T1, T3
- Source Q&A: Q&A-016, Q&A-083, Q&A-097, Q&A-100
- Outcome: D
- Finding: T1 defines covenant as architecturally prior to other characteristics — the structure that makes other inner-being realities possible. T3 reveals which inner faculties this architectural priority engages: relational capacity (T3.11 — covenant is form; relational capacity is content), conscientiousness (T3.10 — covenant is the primary structuring reality for conscientious inner life), memory (T3.3 — covenant is constitutively temporal and requires memory to be held active), and volition (T3.6 — covenant calls for volition from within the old structure and transforms volition from within the new). The T1 × T3 synthesis: covenant's architectural character (T1) is instantiated through a specific set of inner faculties (T3) — the faculties it most deeply engages are precisely those that operate in the time-extended, Other-oriented, and morally structured modes that covenant's form requires. The characteristic is defined by the faculties it constitutes.
- Structural relationship: constitutive
- Session C chapter: Ch2
- SD pointer: NONE

**SYN-INTER-034-010** | T1 × T4
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T1, T4
- Source Q&A: Q&A-015, Q&A-101, Q&A-102, Q&A-107
- Outcome: D
- Finding: T1 establishes that covenant has directional, relational, and constitutional implications that orient the entire enquiry (Q&A-015). T4 shows how these directional implications are realised: the God-to-human direction is the primary axis (T4.1), the human-to-God direction is the responsive axis (T4.2), and the horizontal direction (T4.3/4.4) is grounded in the vertical. The T1 × T4 synthesis: the directional implication identified at the definitional level (T1) is fully realised in the relational interface structure (T4). The asymmetry of the definition (God initiates, human responds — Q&A-015) is the same asymmetry that governs all four relational directions in T4. Definition and relational interface are structurally consistent — covenant is asymmetric at every level of analysis.
- Structural relationship: parallel
- Session C chapter: Ch3
- SD pointer: NONE

**SYN-INTER-034-011** | T1 × T5
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T1, T5
- Source Q&A: Q&A-016, Q&A-018, Q&A-125, Q&A-131
- Outcome: D
- Finding: T1 describes covenant in its static structural form — the working description, the four modes, the constituent elements. T5 describes covenant in its developmental form — what it does over time. The T1 × T5 synthesis reveals a crucial tension: the T1 working description captures the characteristic's structural identity, but T5 reveals that this identity is not static but develops across the covenantal trajectory. The four modes identified in T1 (disposition, act, quality, condition) are themselves developmental achievements — in the OT, the dominant modes are act (entry) and quality (faithfulness-keeping); in the new covenant, the dominant mode shifts to condition (constitutional transformation produced by God). The definition (T1) is the synchronic snapshot; the development (T5) is the diachronic trajectory. Together they show that covenant is not a fixed static category but a developing one whose inner-being content deepens and is transformed across the biblical narrative.
- Structural relationship: sequential
- Session C chapter: Ch4
- SD pointer: NONE

**SYN-INTER-034-012** | T1 × T6
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T1, T6
- Source Q&A: Q&A-018, Q&A-147, Q&A-150, Q&A-152
- Outcome: D
- Finding: T1 proposes that covenant is the architectural backbone of the C17 cluster — the structure within which the relational-grace vocabulary operates. T6 provides the evidential confirmation: the co-occurrence hub status (Q&A-147), the sequential-causal priority (Q&A-150), and the productive relationships (covenant produces hesed, hope, knowing, faithfulness — Q&A-152) all confirm the working description's claim to architectural priority. The T1 × T6 synthesis: the definitional claim (T1) is evidentially validated by the structural relationship data (T6). This is the most direct confirmation of DIM-34-SD001 in the analytical record. The definition is not speculation but is grounded in the quantitative co-occurrence, sequential, and causal relationship data.
- Structural relationship: constitutive
- Session C chapter: Ch5
- SD pointer: NONE

**SYN-INTER-034-013** | T1 × T7
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T1, T7
- Source Q&A: Q&A-016, Q&A-018, Q&A-179, Q&A-185
- Outcome: D
- Finding: T1 produces a working description of covenant as composite and architecturally prior. T7 provides the lexical and evidential basis for that description: the full vocabulary arc (Q&A-179) with seven simultaneous dimensions and the primary anchor verse (Jer 31:33 / Heb 8:10 — Q&A-185) which uniquely captures the constitutional, relational, and cognitive dimensions simultaneously. The T1 × T7 synthesis: the working description (T1) is grounded in and accountable to the lexical evidence (T7). The four-modal composite structure named in T1 (disposition, act, quality, condition) corresponds to the seven vocabulary-arc dimensions named in T7 (relational, bodily, oral, legal, moral, transformative, eschatological). The working description is not imposed on the data but emerges from it — T7 confirms T1's accountability to the vocabulary.
- Structural relationship: constitutive
- Session C chapter: Ch1
- SD pointer: NONE

**SYN-INTER-034-014** | T2 × T3
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T2, T3
- Source Q&A: Q&A-044, Q&A-047, Q&A-065, Q&A-073, Q&A-076, Q&A-097
- Outcome: D
- Finding: T2 locates covenant in the constitutional organs (heart, mind, soul, mouth, body). T3 reveals which inner faculties operate within and through those locations. The T2 × T3 synthesis: the constitutional location (T2) and the faculty operation (T3) are not separate realities but different analytical views of the same inner-being reality. The heart (T2) is where the integrating functions of willing, knowing, moral evaluation, and affect operate (T3.6 volition, T3.2 cognition, T3.8 moral evaluation, T3.4 affect). The mind (T2) is where cognition (T3.2) and memory (T3.3) operate. The soul-totality (T2) corresponds to the conscientiousness and relational capacity (T3.10, T3.11) that engage the whole person. The constitutional location and the faculty operation are two descriptions of the same inner reality: location is where the faculty is housed; faculty is what the location does. The new covenant writes on the heart/mind (T2) and thereby transforms cognition toward knowing God (T3.2) — the constitutional location is the mechanism for the faculty transformation.
- Structural relationship: constitutive
- Session C chapter: Ch2
- SD pointer: NONE

**SYN-INTER-034-015** | T2 × T4
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T2, T4
- Source Q&A: Q&A-041, Q&A-053, Q&A-101, Q&A-105, Q&A-113
- Outcome: D
- Finding: T2 reveals that covenant operates constitutionally in the heart, mind, soul, mouth, and body. T4 reveals that covenant operates relationally through God-to-human, human-to-God, and horizontal interfaces. The T2 × T4 synthesis: the constitutional locations and the relational interfaces are not separate registers — they are the same inner reality viewed from different angles. The soul's engagement in covenant (T2 — "with all his heart and all his soul") is precisely the inner posture required for genuine human-to-God movement (T4.2 — Q&A-106). The mouth as constitutional location (T2 — Isa 59:21) is the organ through which the human-to-God relational direction is enacted (oath as speech act — Q&A-024, T1.4). The blood as somatic covenant-medium (T2 — Q&A-053) is the mediating substance through which the God-to-human interface is constituted (the blood of the covenant — Q&A-101). Constitutional location and relational interface are two views of the same inner-being dynamic.
- Structural relationship: constitutive
- Session C chapter: Ch3
- SD pointer: NONE

**SYN-INTER-034-016** | T2 × T5
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T2, T5
- Source Q&A: Q&A-064, Q&A-066, Q&A-131, Q&A-132
- Outcome: D
- Finding: T2 identifies a shift in constitutional origin across the covenant trajectory: from external bestowal (Noahic) to bilateral reception (Sinai) to generational transmission (Davidic) to internal Spirit-generation (new covenant — Q&A-064). T5 identifies a corresponding shift in the mechanism of change: from external-demand (old covenant letter) to internal-inscription (new covenant Spirit — Q&A-131, Q&A-132). The T2 × T5 synthesis: the constitutional origin shift (T2) and the mechanism shift (T5) are the same development described at two different levels. The new covenant's internal Spirit-generation (T2) is the constitutional reality that underlies the internal-inscription mechanism (T5). These are not two separate developments but one single inner-being transformation described at the constitutional-location level (T2) and at the developmental-mechanism level (T5). The new covenant produces a change in where covenant comes from (T2: now from within through the Spirit) and a change in how it produces change (T5: now through inscription rather than instruction).
- Structural relationship: constitutive
- Session C chapter: Ch4
- SD pointer: NONE

**SYN-INTER-034-017** | T2 × T6
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T2, T6
- Source Q&A: Q&A-044, Q&A-059, Q&A-147, Q&A-157
- Outcome: D
- Finding: T2 establishes that the heart is the primary constitutional location of covenant, with body (blood, circumcision) as the somatic deposit. T6 reveals that covenant's deepest structural relationship is with faithfulness (lexically co-generated through the emunah-amanah root — Q&A-157). The T2 × T6 synthesis: the constitutional deposit of covenant (bodily circumcision, generational word-transmission — Q&A-059) is the constitutional mechanism through which covenant's structural relationships are transmitted to new participants. Covenant's bond with faithfulness (T6) is transmitted across generations through the bodily sign (circumcision) and the spoken word (Isa 59:21) — the somatic deposit (T2) is the mechanism of structural relationship preservation (T6). The body carries the covenant's relational structure forward through time.
- Structural relationship: enabling
- Session C chapter: Ch3
- SD pointer: NONE

**SYN-INTER-034-018** | T2 × T7
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T2, T7
- Source Q&A: Q&A-053, Q&A-054, Q&A-170, Q&A-177
- Outcome: D
- Finding: T2 identifies blood and circumcision as the primary somatic covenant locations. T7 establishes the lexical arc showing covenant as simultaneously relational, bodily, oral, legal, moral, transformative, and eschatological. The T2 × T7 synthesis: the bodily dimension identified in T2 is confirmed and deepened by the lexical analysis of T7. The root meaning of karat (to cut — Q&A-170) and the blood-of-the-covenant vocabulary are etymologically embedded in the bodily-somatic dimension of the covenant vocabulary arc. The LXX translation choice (diathēkē — Q&A-177) adds the death/inheritance dimension to the somatic vocabulary: the blood is the means of mediation, and the testator's death is required for the testament to take effect. T2's somatic findings are not incidental features but are inscribed in the etymology and semantic development of the vocabulary itself (T7).
- Structural relationship: constitutive
- Session C chapter: Ch2
- SD pointer: NONE

**SYN-INTER-034-019** | T3 × T4
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T3, T4
- Source Q&A: Q&A-083, Q&A-100, Q&A-105, Q&A-106, Q&A-109
- Outcome: D
- Finding: T3 reveals that the inner faculties covenant most deeply engages are Other-oriented (relational capacity, conscience, moral evaluation, memory). T4 reveals that covenant's relational interfaces are asymmetric (God initiates; human responds; horizontal is grounded in vertical). The T3 × T4 synthesis: the Other-oriented faculty bias (T3) and the asymmetric relational structure (T4) are coherently related — the inner faculties that covenant engages are precisely those required for the kind of asymmetric responsive relationship that covenant constitutes. The relational capacity (T3.11) is the constitutional equipment for genuine connection; the covenant's relational interfaces (T4) are the actual connections that this capacity enables. The inner posture required for human-to-God covenant movement (T4.2 — Q&A-106: reverent fear, love, all-heart, hearing orientation) corresponds directly to the inner faculties that covenant engages: fear engages moral evaluation (T3.8), love engages affect and relational capacity (T3.4, T3.11), all-heart engages volition (T3.6), and hearing engages perception (T3.1). T3 and T4 are two analytical views of the same responsive inner-being structure.
- Structural relationship: constitutive
- Session C chapter: Ch3
- SD pointer: NONE

**SYN-INTER-034-020** | T3 × T5
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T3, T5
- Source Q&A: Q&A-073, Q&A-085, Q&A-125, Q&A-128
- Outcome: D
- Finding: T3 identifies the new covenant's faculty-level effect as the transformation of volition (from called-for to liberated — Q&A-085) and the production of covenantal knowing (Q&A-073). T5 identifies the developmental sequence through which this transformation occurs (failure → inscription → belonging → knowing — Q&A-128) and the mechanism change (letter to Spirit — Q&A-131). The T3 × T5 synthesis: the faculty transformations identified in T3 (volition liberated, cognition/knowing produced) are the outcome of the developmental sequence and mechanism identified in T5. The sequence "inscription → belonging → knowing" (T5) describes how the specific faculty transformations of T3 are produced. The mechanism shift from letter to Spirit (T5) is the developmental mechanism that produces the volitional liberation (T3.6) and cognitive knowing (T3.2) that the new covenant delivers. T5 is the developmental story; T3 is the faculty-level outcome of that story.
- Structural relationship: causal
- Session C chapter: Ch4
- SD pointer: NONE

**SYN-INTER-034-021** | T3 × T6
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T3, T6
- Source Q&A: Q&A-100, Q&A-147, Q&A-150, Q&A-152
- Outcome: D
- Finding: T3 reveals that covenant is form; relational capacity is content (Q&A-100 — the T3.11 reciprocal finding). T6 reveals that covenant is structurally prior to and produces other characteristics including hope, knowing, and faithfulness. The T3 × T5 synthesis: the T3.11 finding (covenant as form; relational capacity as content) generalises to the T6 finding (covenant as architecturally prior to its C17 neighbour characteristics). In both cases, covenant is the structure; other inner-being realities (relational capacity, love/hesed, hope, knowing) are the content that the structure enables and sustains. This generalisation confirms that covenant's architectural character applies at both the faculty level (T3) and the inter-characteristic level (T6) — it is structurally prior at every level of the inner-being analysis.
- Structural relationship: constitutive
- Session C chapter: Ch5
- SD pointer: NONE

**SYN-INTER-034-022** | T3 × T7
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T3, T7
- Source Q&A: Q&A-073, Q&A-076, Q&A-184, Q&A-185
- Outcome: D
- Finding: T3 shows that memory is one of the most structurally prominent inner faculties in covenant — divine memory of covenant is the guarantee of its continuing operation; human memory is the activating condition for faithfulness (Q&A-074, Q&A-076). T7 shows that the primary verse evidence spans four literary forms (legal-narrative, prophetic oracle, epistle-argument, liturgical — Q&A-181), all of which are forms that require and shape memory. The T3 × T7 synthesis: the memory-faculty centrality (T3) and the literary form analysis (T7) converge on the same insight: covenant is constitutively a narrative and liturgical reality — it is held active through storytelling, declaration, and ritual re-enactment. The Eucharistic "do this in remembrance of me" (Q&A-075) is the liturgical instantiation of memory's role in covenant (T3), and it is carried by the liturgical literary form (T7). Memory and liturgy are co-constituting — covenant is kept alive through the practice of remembering performed in narrative and liturgical forms.
- Structural relationship: constitutive
- Session C chapter: multiple: Ch2, Ch3
- SD pointer: NONE

**SYN-INTER-034-023** | T4 × T5
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T4, T5
- Source Q&A: Q&A-101, Q&A-119, Q&A-125, Q&A-140
- Outcome: D
- Finding: T4 reveals that the relational scope of covenant expands progressively from particular (Abraham) to national (Israel) to universal (new covenant in Christ — Q&A-119). T5 reveals that covenant moves toward eschatological fullness — from the eternal covenant (Heb 13:20 — Q&A-140) to the new creation (Rev 21:1-5 — Q&A-141). The T4 × T5 synthesis: the expanding relational scope (T4) and the eschatological trajectory (T5) are the same movement described in two registers. The Noahic covenant's universal scope (all living creatures) is the anticipation of the new covenant's universal offer and ultimately the eschatological new creation's universal scope. Covenant moves simultaneously toward wider relational inclusion (T4) and toward deeper fullness of the relationship (T5). The two trajectories are not separate but co-directional — the expansion of who is included (T4) and the deepening of what is included in (T5) are aspects of the same eschatological movement.
- Structural relationship: parallel
- Session C chapter: Ch4
- SD pointer: NONE

**SYN-INTER-034-024** | T4 × T6
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T4, T6
- Source Q&A: Q&A-101, Q&A-107, Q&A-150, Q&A-152
- Outcome: D
- Finding: T4 reveals that God-to-human covenant operates through five modes (establishment, faithfulness, inscription, oath-binding, mediation — Q&A-101). T6 reveals that covenant is causally prior to other characteristics and produces love/hesed, hope, knowing, and faithfulness as its effects (Q&A-152). The T4 × T5 synthesis: the God-to-human directional modes (T4) are the relational mechanisms through which the causal productivity identified in T6 operates. God establishes covenant (T4.1) → covenant becomes the ground for hope (T6, Q&A-150, Q&A-152). God inscribes on the heart (T4.1 mode 3) → knowing is produced (T6, Q&A-152). God mediates through Christ (T4.1 mode 5) → sanctification is produced (T6, Q&A-152). The five God-to-human modes (T4) are the directional mechanisms that produce the T6 causal effects. T4 is the directional 'how'; T6 is the consequential 'what'.
- Structural relationship: causal
- Session C chapter: Ch3
- SD pointer: NONE

**SYN-INTER-034-025** | T4 × T7
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T4, T7
- Source Q&A: Q&A-101, Q&A-105, Q&A-181, Q&A-182
- Outcome: D
- Finding: T4 establishes that covenant's relational interfaces are carried through specific acts — oath-taking, blood-shedding, covenant-meal participation, circumcision. T7 establishes that these acts are carried by specific literary forms — legal-narrative (covenant-making), prophetic oracle (new covenant promise), liturgical (Eucharist), and epistle-argument (Hebrews). The T4 × T7 synthesis: the relational acts of covenant (T4) are embedded in and shaped by their literary contexts (T7). The covenantal meal (T4 receiving — Q&A-113) is not merely a relational act but a liturgical-formular act (T7). The prophetic oracle of the new covenant (Jer 31:31-34) is not merely a T4 divine-to-human act of declaration but is embedded in the prophetic genre's authority structures (T7). The literary form analysis (T7) provides the interpretive framework within which the relational interface data (T4) must be read. Responsible interpretation of the covenantal acts requires attention to their literary embedding.
- Structural relationship: enabling
- Session C chapter: multiple: Ch3, Ch5
- SD pointer: NONE

**SYN-INTER-034-026** | T5 × T6
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T5, T6
- Source Q&A: Q&A-128, Q&A-131, Q&A-150, Q&A-152
- Outcome: D
- Finding: T5 identifies the developmental sequence of covenant's inner-being transformation: failure → divine initiative → inscription → belonging → knowing (Q&A-128) and the mechanism shift from external-demand to internal-inscription (Q&A-131). T6 identifies the structural relationships: covenant produces knowing, hope, faithfulness, and freedom; and is structurally prior to other C17 characteristics. The T5 × T6 synthesis: the developmental sequence (T5) is the mechanism through which the structural productivity (T6) operates. Covenant produces knowing (T6 — Q&A-152) through the developmental sequence of inscription → knowing (T5 — Q&A-128). Covenant produces hope (T6) through the sequential logic of covenant-inclusion-as-ground-of-hope (T5 eschatological trajectory — Q&A-140). The developmental story (T5) explains how the structural relationships (T6) come to be — T5 is the causal mechanism; T6 is the structural outcome. The mechanism shift from letter to Spirit (T5) is the developmental explanation for why the new covenant is structurally prior to the characteristics it enables (T6) — the new covenant's internal-inscription mechanism makes it the constitutive source of inner-being transformation, not merely one input among equals.
- Structural relationship: causal
- Session C chapter: Ch4
- SD pointer: NONE

**SYN-INTER-034-027** | T5 × T7
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T5, T7
- Source Q&A: Q&A-125, Q&A-140, Q&A-179, Q&A-185
- Outcome: D
- Finding: T5 establishes covenant's eschatological orientation — the eternal covenant (Heb 13:20 — Q&A-140) and the new creation as the covenant's telos (Q&A-141). T7 establishes that the full vocabulary arc includes an eschatological dimension (Q&A-179) and that the primary anchor verse (Jer 31:33 / Heb 8:10 — Q&A-185) contains the covenant's telos within its text (the knowing of God — Jer 31:34). The T5 × T7 synthesis: the eschatological trajectory (T5) is encoded in the vocabulary and in the primary anchor verse itself (T7). The eternal covenant (T5) is named in the Hebrews vocabulary (T7 — Heb 13:20 as anchor). The eschatological knowing of God (T5 — Q&A-141: fully realised eschatological knowing) is anticipated in the primary anchor verse's promise "they shall all know me" (T7 — Q&A-185). T5's developmental trajectory finds its lexical and evidential home in the specific texts that T7 identifies as the evidential foundation. The eschatological dimension is not imposed on the data but is resident in the vocabulary arc and primary anchor verse.
- Structural relationship: constitutive
- Session C chapter: Ch4
- SD pointer: NONE

**SYN-INTER-034-028** | T6 × T7
- Entry type: SYNTHESIS_INTER_TIER
- Tiers: T6, T7
- Source Q&A: Q&A-147, Q&A-157, Q&A-158, Q&A-179
- Outcome: D
- Finding: T6 establishes that covenant and faithfulness are lexically co-generated through the emunah-amanah root (Q&A-157, Q&A-158) and that covenant is structurally central in the inner-being landscape (Q&A-147). T7 confirms through the vocabulary arc analysis that covenant encompasses seven simultaneous semantic dimensions (Q&A-179). The T6 × T7 synthesis: the co-occurrence hub status and structural priority of covenant (T6) is grounded in the breadth and depth of the vocabulary arc (T7). Covenant occupies a hub position in the co-occurrence data (T6) because its vocabulary spans seven dimensions (T7) — a characteristic whose terms appear across the relational, moral, transformative, bodily, and eschatological registers will naturally co-occur with the widest range of other inner-being characteristics. The structural centrality of covenant (T6) is the co-occurrence consequence of its semantic comprehensiveness (T7). The two findings confirm each other: wide vocabulary arc → wide co-occurrence → structural hub position. Covenant's place at the centre of the inner-being landscape (T6) is not arbitrary but lexically grounded (T7).
- Structural relationship: constitutive
- Session C chapter: Ch5
- SD pointer: NONE

Inter-tier pass COMPLETE: 2026-05-01. D: 21. F: 0. N: 0. Total: 21.

Total Stage 2c entries: 28 (7 intra + 21 inter). All mandatory entries present.


---

## SD Pointer Accumulator — Final

**SP-034-001** — raised in Unit 2, 2026-05-01, MEDIUM, Session D
- Target: R001 (abomination) · Connecting term: G1303 diatithēmi
- Question: G1303 ("to make a covenant") is the primary NT covenant-making verb yet sits in R001. Does R001's analysis address the covenant-making dimension, or is there a gap? Session D should cross-read R001 and R034 on this term.
- Evidence basis: OBS-034-003
- Priority: MEDIUM

**SP-034-002** — raised in Unit 2, 2026-05-01, MEDIUM, Session D
- Target: R159 (testimony) · Connecting term: H5715 e.dut
- Question: The covenant-testimony boundary (ark = ark of testimony; tablets = tablets of testimony) is a structural OT nexus. Does R159 capture the inner-being dimension of covenant-bearing witness?
- Evidence basis: OBS-034-005, §G.3 shared anchor 2Ki 23:3
- Priority: MEDIUM

**SP-034-003** — raised in Unit 5, 2026-05-01, HIGH, Session D
- Target: R103 (love) — 37 shared verses · Connecting term: H1285 berit + H2617 hesed
- Question: Does R103 carry the hesed vocabulary that pairs structurally with berit? Session D must examine the hesed-berit pair as constitutive for C17 synthesis.
- Evidence basis: OBS-034-029, OBS-034-039, Q&A-150, Q&A-154, SYN-INTRA-034-006
- Priority: HIGH

**SP-034-004** — raised in Unit 5, 2026-05-01, HIGH, Session D
- Target: R112 (mind) — 39 shared verses · Connecting term: H3820 leb / H3824 lebab
- Question: Does the mind registry engage the "heart-covenant" language? What does the covenant-mind connection disclose about covenant as the structuring principle of inner orientation?
- Evidence basis: OBS-034-029, OBS-034-030, OBS-034-040, OBS-034-059, Q&A-047, Q&A-048
- Priority: HIGH

**SP-034-005** — raised in Unit 5, 2026-05-01, MEDIUM, Session D
- Target: R111 (mercy) — shared anchor Rom 1:31 · Connecting term: G0802 asunthetos
- Question: Does R111's analysis of Rom 1:31 engage the covenant-breaking dimension? Is there a structural relationship between covenant faithfulness and mercy requiring synthesis?
- Evidence basis: OBS-034-033, §G.3, Q&A-165
- Priority: MEDIUM

**SP-034-006** — raised in Unit 6, 2026-05-01, MEDIUM, Session D
- Target: R117 (peace) — berit shalom passages · Connecting term: H1285 berit + H7965 shalom
- Question: Does R117's analysis address the berit-shalom nexus (Num 25:12; Isa 54:10; Eze 34:25; 37:26)? If not, Session D should initiate a cross-registry pass.
- Evidence basis: OBS-034-034, PH2-34-004
- Priority: MEDIUM

**SP-034-007** — raised T6.7, 2026-05-01, MEDIUM, Session D
- Target: All C17 registries and cross-cluster registries · Connecting term: Multiple — all OWNER terms
- Question: Which other programme registries share each of covenant's eight dimensions? CC should produce the dimensional sharing map from wa_dimension_index. Session D needs this for cross-registry synthesis T × T pairs.
- Evidence basis: Q&A-167, OBS-034-024
- Priority: MEDIUM

---

## RESEARCHER_DECISION Accumulator — Final

**RD-034-001** — raised 2026-05-01, MEDIUM
- Decision required: Confirm PH2-34-005 (extraction anomaly — 7 grammatical particles) is resolved and close the flag in DB.
- Context: OBS-034-034. Current term inventory does not include the 7 particles.
- Recommendation: CC confirms and closes PH2-34-005.

**RD-034-002** — raised 2026-05-01, MEDIUM
- Decision required: Should groups 777-002 and 777-003 (kainos — new self/creation and new name/song/Jerusalem) be retained as covenant inner-being evidence?
- Context: OBS-034-062, OBS-034-063. Dimension Review flags on both.
- Resolution in Stage 2b: Q&A-021 and inter-tier synthesis entries address their scope. Retained with analytical acknowledgement of extension beyond covenant proper.
- Recommendation: Retain (Option A). No further action required unless researcher instructs otherwise.

**RD-034-003** — raised 2026-05-01, HIGH
- Decision required: G1242 SPAN_RESOLUTION_CONFLICT flag — has manual STEP UI verification been performed?
- Context: OBS-034-067, §I. RESOLVED — researcher provided G1242 verse set directly (30 verses confirmed). CC should clear the SPAN_RESOLUTION_CONFLICT flag for G1242.
- Status: RESOLVED.

---

## Session Close

session_b_status: 'Analysis Complete'

Final counts:
- Stage 2a observations: 74 (OBS-034-001 through OBS-034-074)
- Stage 2b Q&A entries: 189 (Q&A-001 through Q&A-189) — A: 134, P: 18, S: 7, N: 30
- SD pointers raised: 7 (SP-034-001 through SP-034-007)
- RESEARCHER_DECISION items: 3 (RD-034-001, RD-034-002, RD-034-003 — RD-034-003 resolved this session)
- Stage 2c synthesis entries: 28 (Intra D: 7, F: 0, N: 0 / Inter D: 21, F: 0, N: 0)

Session Close block added. session_b_status set to Analysis Complete. Registry 034 covenant Analysis Output complete pending CC parse.

