# Session B Observations Log — Registry 103 (love)
## WA Framework B Soul Word Analysis Programme
**File:** wa-103-love-sessionB-observations-v1-2026-04-12.md
**Date:** 2026-04-12
**Instruction:** WA-SessionB-Instruction-v4.7 (2026-04-12)
**Input:** wa-103-love-complete-2026-04-12.json
**Word study input:** wa-103-love-word-study-v1-2026-04-12.md
**Session number:** Session B — Session 1
**Stage:** Stage 1 — Data Audit and Remediation

---

## 1.2 Startup

- Instruction read in full: WA-SessionB-Instruction-v4.7
- Word: love | Registry: 103 | JSON: wa-103-love-complete-2026-04-12.json
- Session B observations log initialised: this file
- Session B session log initialised: wa-103-love-sessionB-log-v1-2026-04-12.md
- Current session number: Session B Session 1
- Stage: Stage 1 — Data Audit

---

---

## Stage 1 Audit — Complete

### Section 1 — Registry Block

| Field | Status | Notes |
|---|---|---|
| word | OK | love |
| no / id | OK | 103 |
| cluster_assignment | OK | C17 |
| verse_context_status | OK | Complete |
| session_b_status | NOTE | "Verse Context Reset" — prior VC reset event; cause not visible in JSON. Not a blocker. |
| dim_review_status | OK | Complete |
| dim_review_version | OK | v1.9-2026-04-09 |
| sb_classification | OK | None — not yet assigned; Stage 2 Pass 4 |
| sb_classification_reasoning | OK | None — consistent |
| unique_term_count | OK | 41 |
| shared_term_count | OK | 96 |
| term_sharing_ratio | OK | 0.701 |
| dimensions | NOTE | "Relational/Social" — pre-review label, not from dimension vocabulary. Acceptable for registry-level field. |
| strongs_list | STRUCTURAL NOTE | JSON string containing 139 entries. 3 terms in terms array absent from strongs_list: G7493 (extracted, 0 verses, no inventory), H0156 (delete, 0 verses), G1207 (delete, 0 verses). H0156 and G1207 deletion confirmed appropriate. G7493 absent from strongs_list is anomalous — extracted status, 0 verses. GAP: needs CC investigation. |

**Deletion justification review — summary:**
- 40 delete-status terms reviewed
- 35 have mti.status=delete but delete_flagged=0 (deferred cascade — expected)
- 5 have delete_flagged=1 (cascade applied)
- All "bleed" deletions confirmed: place names, anatomical/object terms, ordinal "first" cluster (G4409–G4414) — no inner-being content
- **CHALLENGE — H2245 (to love fervently, cherish):** 1 verse (Deu 33:3), exclusion_reason says "Primary in love registry" but term has delete status. Exclusion_reason appears to be an error — the note is the opposite of what delete implies. Analytically: "to love fervently" is structurally distinct from other active love terms. FLAGGED for researcher review.
- **CHALLENGE — H2898 (goodness/good things):** 31 verses, no exclusion_reason, no owner_type. Delete status with no documented rationale and no owner assignment. The goodness vocabulary is shared with Reg 67 (goodness) via TOV root. FLAGGED for researcher review — deletion should be confirmed or documented.
- **H0157G (to love: lover, 184 verses):** XREF delete, no exclusion_reason. 184 verses is a substantial corpus. Per PH2-103-001 flag, primary analysis is in Reg 43 (desire). Deletion at this registry is appropriate IF adequately covered in Reg 43 — but the absence of exclusion_reason is a documentation gap. NOTE only.
- All other deletions confirmed adequate.

---

### Section 2 — Statistics Block

| Field | Stated | Actual | Status |
|---|---|---|---|
| term_count | 142 | 142 | OK |
| active_term_count | 137 | 137 (using term.delete_flagged=0) | OK |
| owner_term_count | 78 | 78 | OK |
| xref_term_count | 59 | 59 | OK |
| verse_count | 3446 | 3446 | OK |
| active_verse_count | 1156 | 1156 | OK |
| verse_context_group_count | 132 | 132 | OK |
| verse_context_record_count | 2421 | 2421 (1888 assigned + 533 unassigned) | OK |
| anchor_verse_count | 190 | 190 | OK |
| dimension_index_count | 66 | 66 | OK |
| research_flag_count | 9 | 9 | OK |
| All correlation counts | All stated | All match | OK |

NOTE: wa_term_inventory object is null for all 142 terms in this export. The delete_flagged field is present at the top-level term record and functions as the inventory flag. This is an export format difference from grace (wa-068) but the data is complete and consistent. No error.

NOTE: session_d_pointer_count stated=2 but session_research_flags contains 9 records including 2 SD_POINTER flags. The session_d block contains 2 sd_pointer_flags. The discrepancy is that 9 research flags include 2 SD_POINTER, 1 DIMREVIEW_SESSION_D, and 6 PH2 flags — the session_d_pointer_count (2) counts only SD_POINTER type. This appears internally consistent. NOTE only.

---

### Section 3 — Terms

**Key findings:**
- G7493 (eraō, to love passionately): extracted status, 0 verses, absent from strongs_list. Has LSJ entry (classical erotic love vocabulary). No wa_term_inventory. This term is analytically significant — erōs is the classical Greek word for passionate/erotic love, present in the vocabulary but with 0 verses (possibly not used in NT/LXX or not captured in current extraction). FLAGGED as data gap.
- H0157H (ahev, to love: friend): extracted_thin, 13 occurrences, no AHAV root record. Root gap — should share AHAV with H0158 and H0160.
- H1730G (dod, beloved): extracted, 33 occurrences, no DOD root record. Root gap — should share DOD with H1730H.
- G5370 (philēma, kiss), G5373 (philia, friendship), G5384 (philos, friend), G2705 (kataphileō, to kiss), G5382 (hospitable): all active, all missing FILOS root code despite being core philo- family members.
- god_as_subject: empty on all terms (field present but blank). Expected per WA-Reference 13.3 — redundant field. mti_term_flags authoritative. NOTE.
- somatic_link: empty on all terms. Same — NOTE.
- phase2_flag_count = 0: confirmed — no phase2 flags on any term. Expected at this stage.

---

### Section 4 — Verse Context Groups

- All 132 groups have context_description: OK
- All groups have at least one anchor verse: OK (confirmed in 10d)
- No groups with zero contexts: OK
- 66 OWNER groups / 66 XREF groups — consistent with term ownership split
- strongs_id null on all groups: NOTED in Session C. Confirmed structural — groups link to mti_term_id not directly to strongs_id in this export format. Not an error.

---

### Section 5 — Dimension Index

- 66 rows: OK
- All rows have CLAUDE_AI confidence: OK
- All rows have dominant_subject populated: OK
- All rows have manual_override = 0: OK
- Dimension Review sub-process: NOT required (dim_review_status = Complete, CLAUDE_AI on all groups)
- 10c: dim_index covers OWNER groups only (66/132). XREF groups correctly excluded — dimension review is the owning registry's responsibility. OK.

---

### Section 6 — Session B Block

- session_b.dimensions = None: expected — not yet assigned
- session_b.findings: 2 records (DIM-103-001, DIM-103-002) — both DIMENSION_REVIEW type, from prior Dimension Review session
- No Session B targets in research flags — all 9 flags target Session D

---

### Section 7 — Session D Block

- sd_pointer_flags: 2 (DIM-103-SD001, DIM-103-SD002) — unresolved, correctly carried forward
- runs: 0 — Session D not yet run

---

### Section 8 — Research Flags

All 9 flags: 2 SD_POINTER + 1 DIMREVIEW_SESSION_D + 6 PH2 — all target Session D, all unresolved.
No flags requiring Stage 2 action.

---

### Section 9 — Cross-Registry Links

8 cross-registry links: desire (Reg 43) ×3, grief (Reg 71), hope (Reg 78) + 3 more. Populated from prior sessions. Expected — no action.

---

### Section 10 — Consistency Checks

| Check | Result |
|---|---|
| 10a — Root family completeness | GAP: 5 active terms missing FILOS root code; H0157H and H1730G missing their root codes |
| 10b — Root family correlation signal | AGAP root not in correlations (registry_count=1, single-registry) — OK. FILOS root not in correlations — expected if single-registry. TOV, RACHAM, AGAV all present — OK |
| 10c — Dim index vs VC groups | OK: XREF groups correctly excluded from dim_index |
| 10d — Anchor verse per group | OK: all groups with contexts have ≥1 anchor |
| 10e — xref_sharing vs inventory | OK: no delete_flagged=1 terms in xref_sharing |
| 10f — Correlation counts | OK: all correlation counts match |
| 10g — SB classification consistency | OK: both null — consistent |

---

## AUDIT SUMMARY — Registry 103 (love) | 2026-04-12

### Fields confirmed OK
word, no, id, cluster_assignment, verse_context_status, dim_review_status, dim_review_version, sb_classification (null — expected), all statistics fields, all correlation counts, all dimension index entries, research flags count, session D block.

### Gaps requiring field-level patch
1. **Root family gaps — 7 active terms:** G5370, G5373, G5384, G2705, G5382 missing FILOS root code; H0157H missing AHAV root code; H1730G missing DOD root code. Patch: insert wa_term_root_family records for each.

### Items requiring CC investigation (not direct patch)
2. **G7493 (eraō) absent from strongs_list:** extracted status, 0 verses. CC to investigate whether this term has verse records outside the current extract scope, and whether it should be in the strongs_list.
3. **H2245 exclusion_reason discrepancy:** exclusion_reason text contradicts delete status. CC to confirm correct status and update exclusion_reason or reinstate.
4. **H2898 (goodness) no exclusion_reason, no owner_type, delete status:** CC to provide documentation for this deletion.

### Verse Context sub-process required?
[x] No — verse_context_status = Complete; no structural group gaps found.

### Dimension Review sub-process required?
[x] No — dim_review_status = Complete; all groups CLAUDE_AI confidence with dominant_subject.

### Statistics corrections required?
[x] No — all statistics verified correct.

### strongs_list — deletion justification review
[ ] Reinstatement required: H2245 — exclusion_reason appears to be in error; needs CC investigation before reinstatement decision can be made. Flagging as open item.

### Root family gaps
[x] Yes — 7 active terms require root family records (see above).

### Open items requiring researcher decision
1. H2245 (to love fervently): delete status with contradictory exclusion_reason. Does this term warrant reinstatement?
2. H2898 (goodness): deleted with no documentation. Confirm deletion or provide rationale.
3. G7493 (eraō): extracted but 0 verses, absent from strongs_list. Is this intentional?


---

## Researcher Decisions — Resolved

### G7493 (eraō, to love passionately)
**Decision received:** No STEP verses — delete status confirmed correct.
**Action:** Add to strongs_list as delete. Correct exclusion_reason (currently null) to document no STEP verse coverage.
**Patch action:** (1) Update strongs_list to include G7493 as delete entry. (2) CC directive to set exclusion_reason = "eraō to love passionately — no STEP verse coverage in this registry."

---

### H2245 (cha.vav, to love fervently/cherish)
**Context from data:** Single verse — Deu 33:3 "Yes, he loved his people, all his holy ones were in his hand." God as subject. Sense: "(Qal) to love fervently, cherish." exclusion_reason reads "cha.vav to love — bleed. Primary in love registry" — contradictory to delete status (if it were primary it should be active). Related words: breast, to hide, Hobab — the root family is CHESED-adjacent (cha.va root), not AHAV.
**Researcher guidance:** God's love for his people, only one verse.
**Analytical assessment:**
- One verse, God as subject, unique sense ("fervently/cherish") not covered by other active terms in exactly this form
- However: H0160 (ahava) and H0157H (ahev) both cover divine love with larger verse corpora
- "To love fervently" is semantic overlap with ahava; one verse does not constitute a structurally distinct register
- Deletion on adequacy-of-coverage grounds is defensible here — one verse, semantically covered
- The exclusion_reason error needs correcting regardless
**Decision:** Confirm deletion. Correct exclusion_reason to: "cha.vav to love fervently — single verse (Deu 33:3); adequately covered by H0160 (ahava). Bleed from related root."
**Patch action:** CC directive to update exclusion_reason on H2245.

---

### H2898 (tuv, goodness) — Verse-level inspection

Verse-level classification of all 31 verses:

**INCLUDE (inner-being relevant — goodness as divine character, inner experience, moral quality):**
- Exo 33:19 — "I will make all my goodness pass before you" — God's inner character/nature. INCLUDE.
- Psa 25:7 — "according to your goodness, O Lord" — divine goodness as ground of mercy. INCLUDE.
- Psa 27:13 — "I shall look upon the goodness of the Lord in the land of the living" — eschatological inner hope. INCLUDE.
- Psa 31:19 — "how abundant is your goodness, stored up for those who fear you" — divine goodness as inner sustenance. INCLUDE.
- Psa 65:4 — "satisfied with the goodness of your house" — inner satisfaction/proximity to God. INCLUDE.
- Psa 119:66 — "teach me good judgment and knowledge" — goodness as inner discernment. INCLUDE.
- Psa 145:7 — "the fame of your abundant goodness" — divine goodness as doxological focus. INCLUDE.
- Isa 63:7 — "the great goodness to the house of Israel" — recounting of divine goodness. INCLUDE.
- Jer 31:12 — "radiant over the goodness of the Lord" — inner response to divine goodness. INCLUDE.
- Jer 31:14 — "my people shall be satisfied with my goodness" — inner satisfaction from God. INCLUDE.
- Hos 3:5 — "they shall come in fear to the Lord and to his goodness" — relational orientation toward divine goodness. INCLUDE.
- Neh 9:35 — "amid your great goodness that you gave them" — divine goodness as relational context for covenant failure. INCLUDE.
- Deu 28:47 — "because you did not serve the Lord with joyfulness... because of the abundance of all things" — inner disposition failure in context of goodness. INCLUDE (borderline — abundance of things, but the inner failure is the point).
- Zec 9:17 — "how great is his goodness, and how great his beauty" — divine goodness as praise object. INCLUDE.

**SET ASIDE (material goods, property, provisions — not inner-being content):**
- Gen 24:10 — "all sorts of choice gifts" — physical goods. SET ASIDE.
- Gen 45:18 — "I will give you the best of the land" — material provision. SET ASIDE.
- Gen 45:20 — "no concern for your goods" — property. SET ASIDE.
- Gen 45:23 — "ten donkeys loaded with the good things of Egypt" — physical goods. SET ASIDE.
- Deu 6:11 — "houses full of all good things" — material abundance. SET ASIDE.
- 2Ki 8:9 — "all kinds of goods of Damascus" — material goods. SET ASIDE.
- Ezr 9:12 — "eat the good of the land" — material provision. SET ASIDE.
- Neh 9:25 — "houses full of all good things" — material abundance. SET ASIDE.
- Neh 9:36 — "enjoy its fruit and its good gifts" — material. SET ASIDE.
- Job 20:21 — "nothing left after he had eaten / his prosperity will not endure" — material wealth. SET ASIDE.
- Job 21:16 — "is not their prosperity in their hand?" — material prosperity. SET ASIDE.
- Psa 128:5 — "prosperity of Jerusalem" — civic/material. SET ASIDE.
- Pro 11:10 — "when it goes well with the righteous" — civic wellbeing. SET ASIDE.
- Isa 1:19 — "you shall eat the good of the land" — material provision. SET ASIDE.
- Jer 2:7 — "plentiful land to enjoy its fruits and good things" — material. SET ASIDE.
- Isa 65:14 — "my servants shall sing for gladness of heart" — NOTE: this verse is about inner joy (gladness of heart) not tuv goodness specifically — the ESV target word appears to be a different term in this verse. SET ASIDE pending verification.
- Hos 10:11 — "Ephraim was a trained calf that loved to thresh" — agricultural/national. SET ASIDE.

**Summary:**
- INCLUDE: 14 verses (divine goodness as character, inner satisfaction, inner hope, inner orientation toward God)
- SET ASIDE: 17 verses (material goods, property, provisions, civic prosperity)

**Analytical conclusion:** H2898 (tuv) does contain meaningful inner-being content — primarily divine goodness as an attribute the inner person orients toward, meditates on, and is satisfied by. This is a different semantic register from H2896A (tov, good/goodness) which is the primary goodness term. Tuv specifically names goodness as abundant divine gift and as the object of inner longing/satisfaction. The deletion is not analytically well-founded. **RECOMMEND REINSTATEMENT** with owner_type = OWNER and verse context classification as described above.

**Patch action required:**
1. Update H2898: status = extracted, delete_flagged = 0, owner_type = OWNER, exclusion_reason = null (remove)
2. Verse context: 14 verses to be classified (include/related/anchor), 17 set aside — requires Verse Context sub-process for this term.


---

## Stage 1 Remediation — Step A Outputs Produced

**PATCH-20260412-103-PREANALYSIS-V1.json** — 4 operations:
- OP-001: G7493 → delete, exclusion_reason set
- OP-002: H2245 → delete confirmed, exclusion_reason corrected
- OP-003: H2898 → extracted reinstated, exclusion_reason cleared
- OP-004: registry_note re. CC directive scope

**wa-103-love-sessionB-cc-directive-v1-2026-04-12.md** — 4 directives:
- DIR-001: G7493 add to strongs_list (SQL)
- DIR-002: H2898 inventory reinstatement — delete_flagged=0, owning_registry_fk=103 (SQL)
- DIR-003a/b/c: Root family inserts — 7 records (SQL): G5370, G5373, G5384, G2705, G5382 → FILOS; H0157H → AHAV; H1730G → DOD
- DIR-004: H2898 Verse Context sub-process — group 2898-001 + 31 verse_context records (4 anchor, 10 related, 17 set aside)

**Status:** Awaiting Claude Code application and confirmation.
**Next step (after CC confirmation):** Fresh extract → Stage 2 analytical passes.


---

## Stage 1 — COMPLETE

### Spot-check results — fresh extract confirmed

| Item | Check | Result |
|---|---|---|
| G7493 in strongs_list count=0 | OK | ✓ |
| H2898 extracted, delete_flagged=0, OWNER | OK | ✓ |
| 7 root family records (FILOS×5, AHAV, DOD) | All OK | ✓ |
| Group 2898-001 present (id=3519) | OK | ✓ |
| verse_context: 4 anchor, 10 related, 17 set-aside | OK | ✓ |
| active_term_count = 138 | OK | ✓ |
| owner_term_count = 79 | OK | ✓ |
| anchor_verse_count = 194 | OK | ✓ |
| verse_context_group_count = 133 | OK | ✓ |
| unassigned = 550 | OK | ✓ |

**Stage 1 COMPLETE. Clean extract confirmed.**
**Input for Stage 2: wa-103-love-complete-2026-04-12.json (post-directive extract)**

---

## Stage 2 — Analytical Passes — OPEN

State: Stage 1 complete. Fresh extract confirmed. Beginning Stage 2 against wa-103-love-complete-2026-04-12.json.

### Cross-registry vision discipline (Section 2.0a) — ACTIVE from this point
All five standing questions active on every data read.


---

## Pass 1 — Meaning and Semantic Range

### AGAP family (G0025, G0026, G0027)
**G0025 agapaō (344 occ, NT only):** PROSE_ONLY meaning — single sense block. No causative stem. Five groups covering the full agapao range: love of God/Christ (commanded, whole-person orientation); God's/Christ's love toward the person (prior divine act); love of neighbour and enemy (outward orientation fulfilling the law); mutual love among believers and in marriage; disordered love (toward world, darkness, money). The five-group structure reveals agapao's semantic range is entirely defined by its object and direction, not by its quality alone. This is a fundamentally directional verb — love as a movement toward.

**Cross-registry flag raised:** Group 571-003 (love of neighbour and enemy) and 571-004 (mutual love in marriage) show agapao operating simultaneously in the ethical and covenantal domains. The love-of-enemy command (Mat 5:44) is also co-present with seeking (Reg 140) and will (Reg 173) in those verse contexts — SD POINTER to raise.

**G0026 agapē (133 occ, NT only):** Three groups — God's love as inner source and ground (poured into hearts, demonstrated in Christ's death); love as the defining inner virtue of the believer (fruit of Spirit, greatest commandment, fulfilment of law, never ends); mutual love as communal orientation (discipleship mark). The noun agapē concentrates what the verb scatters across objects. It names love as a quality that can be possessed, measured, and commanded — which the verb alone does not.

**Session C check (Section 1):** Statement "love operates across every dimension of inner life simultaneously" — CONFIRMED. The three-group structure of agapē (divine source → inner virtue → communal expression) maps exactly onto the three levels described.

**G0027 agapētos (79 occ, NT only):** Two groups — Christ as Father's beloved (divine identity/relationship); believer as beloved (identity address). The adjective form carries significant ontological weight: being beloved is a status that grounds conduct. The believer's identity as loved is treated as prior to the commands to love. CONFIRMED: Section 1 statement "love's deepest level does not originate in the human person."

---

### FILOS family (G5368 phileo + 20 compounds)
**G5368 phileo (52 occ):** Three groups — natural affection and friendship-love (Christ's love for Lazarus and friends); ranking of inner loves and loyalties (love of Christ above natural affection; hating one's life to keep it); Peter's confession (Joh 21 — phileō where agapaō was asked). The three groups reveal phileō's semantic distinctiveness: it is the love of natural attachment, emotional warmth, and personal affection. Its use in Joh 21 is analytically significant — see Pass 3 annotation.

**Session C check:** John 21 agapaō/phileō distinction — the data supports treating this as a meaningful distinction, not mere stylistic variation. Group 572-003 is explicitly named for this dialogue. CORRECTION to Session C Section 4 flag: the distinction is confirmed by grouping, not merely noted as uncertain.

**Cross-registry flag:** Joh 12:25 (group 572-002): "whoever loves his life loses it, whoever hates his life in this world will keep it for eternal life" — agapaō/miseō (love/hate) applied to one's own life. This verse is a structural intersection of love (Reg 103), hatred (Reg 75), soul/life (Reg 182), and will/surrender (Reg 156). SD POINTER required.

**Compound philo- terms:** The compound family maps every major object of inner orientation — money (philarguria/philarguros), pleasure (philēdonos), dispute (philoneikia/philoneikos), primacy (philoprōteuō), brothers (philadelphia/philadelphos), husband (philandros), children (philoteknos), good (philagathos), God (philotheos), strangers (philoxenos), freedom from money (aphilarguros). This is the most systematic taxonomy of loves in the NT vocabulary — every compound names love as the inner orientation toward a specific object, virtuous or disordered.

**Cross-registry flag:** The parallel structure of philo-theos vs philo-ēdonos in 2Ti 3:4 — lovers of God vs lovers of pleasure — is an explicit antithesis. This verse is a key intersection point for love (Reg 103), pleasure/desire (Reg 43), and God-orientation (C15 cluster). SD POINTER required.

---

### Hebrew AHAV family (H0157H, H0158, H0160)
**H0160 ahavah (38 occ):** Primary Hebrew noun for love. Three groups: God's covenantal love (Jer 31:3, Zep 3:17 — everlasting, rejoicing love); intense personal love (Jonathan/David, Song's burning love); love as moral loyalty and kindness (Pro 10:12 — love covers offences; Jer 2:2 — bride-devotion of youth). Causative stem absent from noun; present in verbal form (H0157H). The three-group distribution maps neatly onto the Greek agapē groups — covenantal/divine, personal/intense, moral/ethical.

**H0157H ahev (13 occ, extracted_thin):** Causative stem present (has_causative_stem=1). The causative form means love can be both experienced and caused in another — someone can be made to love, or can cause love to arise. This is semantically significant for the relationship between divine initiative and human response. Single group: the loyal friend whose faithfulness transcends social convention (Abraham as God's friend, Isa 41:8).

**Session C check:** Section 4 statement about causative stem — CONFIRMED for H0157H (ahev), H7355 (racham), H8130 (sane), H2895 (tov). The causative structure is more pervasive than Section 4 noted.

---

### CHESED family (H2617A, H2623)
**H2617A chesed (261 occ):** The most frequent term. Three groups: God's steadfast love as defining attribute (never ceasing, extends to heaven, ground of hope); human covenant loyalty mirroring divine chesed (Ruth, Pro 3:3); chesed's failure/absence (Hos 6:6 — desired above sacrifice; Mic 6:8 — required above ritual). PROSE_ONLY meaning but the three-group structure reveals the semantic architecture clearly: divine chesed → human chesed → chesed's absence.

**Cross-registry flag:** Mic 6:8 places chesed (Reg 103) alongside mishpat/justice and halak-humbly-with-God. The three requirements are structurally parallel inner orientations. SD POINTER: does chesed in Mic 6:8 name the same inner state as agapē in 1Cor 13, or is the OT covenant-faithfulness register structurally distinct from the NT self-giving register? This is one of the deepest semantic questions across the two testaments.

**H2623 hasid (39 occ):** The pious/godly person — one whose character is shaped by covenantal faithfulness. Single group. The noun form of chesed-in-person: the one who embodies chesed becomes hasid. Cross-registry link to holiness/devotion (Reg 46 — C08 cluster). SD POINTER.

---

### RACHAM family (H7355, H7356B, H7349)
**H7355 racham (47 occ, causative):** Full causative stem — to love deeply, have compassion, be compassionate (Qal/Piel/Pual). The causative structure means God both has compassion and causes compassion to arise. Related words include rechem (womb) — structural etymological link. Single group: divine act of compassion — God's inner movement of mercy in restoration after judgment.

**H7356B rachamim (42 occ):** Plural noun — compassion(s). The plural form in Hebrew intensifies and concretises the abstract. Single group: God's compassion as the deep inner movement of mercy — mother-like tenderness. The PH2-103-002 flag noted that some verses use rechem (physical womb) not rachamim — this is confirmed as a data quality issue. The womb/compassion root link is genuine and semantically productive (see Isa 49:15).

**H7349 rachum (13 occ):** Compassionate as divine attribute — "always of God with one possible exception" (BDB). This concentration on God as subject is the highest god_as_subject ratio among all terms in the registry. Cross-registry: shared fully with compassion (Reg 23) and mercy (Reg 111).

**Cross-registry flag:** The racham root (compassion/womb) appears in love (Reg 103), compassion (Reg 23), mercy (Reg 111), and grief (Reg 71). The womb metaphor grounds divine compassion in the most intimate bodily human love. This is the somatic underpinning of divine love — not abstract but visceral. SD POINTER for cross-registry examination of the womb-compassion-love nexus.

---

### SANE family (H8130, H8131)
**H8130 sane (156 occ, causative):** Hate, be hateful — Qal/Niphal/Piel. Three groups: inner hostile disposition toward another (can be concealed); attributed divine enmity; hatred as a constitutive human capacity (listed alongside love and envy). The causative stem means hatred can also be caused — someone can be made to hate. This is structurally parallel to love's causative capacity (H0157H).

**Cross-registry flag:** Group 902-003 (hatred as constitutive human capacity, listed alongside love and envy — Eccl 9:6) is a significant structural verse: the passage names love, hatred, and envy as the three primary inner orientations that cease at death. SD POINTER: does this triadic structure in Ecclesiastes define a fundamental taxonomy of inner relational orientations that Session D should examine?

---

### H2898 (tuv, goodness) — newly reinstated
Single group (2898-001). 14 include verses confirm: divine goodness as an attribute the inner person orients toward, is satisfied by, and looks for eschatologically (Psa 27:13 — "I shall look upon the goodness of the Lord in the land of the living"). Senses 1c/1e confirm: "fairness, beauty, joy, prosperity, goodness (abstract)" and "goodness of God (abstract)." TOV root — cross-cluster link to goodness (Reg 67, C10).

**Cross-registry flag:** The tuv/tov root family (TOV) spans love (Reg 103) and goodness (Reg 67) cross-cluster. Psa 25:7 places tuv (divine goodness) and chesed in the same verse — "according to your steadfast love remember me, for the sake of your goodness." SD POINTER: is divine tuv the content of divine chesed — goodness as what love gives — or are they parallel attributes?

---

### Pass 1 — Session C check summary (Section 1 and 2)
- "Love operates across every dimension simultaneously" — CONFIRMED by AGAP group structure
- "Love is radically directional" — CONFIRMED; every term group defined by its object
- "Bodily dimension clear" — partially confirmed in Pass 1; Pass 4 will complete somatic scan
- "Love does not originate in the human person" — CONFIRMED; agapētos groups make this structural
- "Hatred is the structural contrary" — CONFIRMED; sane causative parallels ahev causative
- "Disordered love misdirects the same capacity" — CONFIRMED; philo- compound taxonomy is explicit

### Pass 1 — meaning_numbered update required
All primary terms (G0025, G0026, H0160, H2617A) carry PROSE_ONLY parse warnings — meaning_numbered fields are null. These should be structured in Session B. Noting for CC directive.

### SD Pointers raised in Pass 1 (preliminary — to be formalised in Section 2.2)
1. Agapao + seeking + will intersection (Mat 5:44 context verses) — Regs 140, 173
2. Joh 12:25 — love/hate of life — Regs 75, 182, 156
3. 2Ti 3:4 — philotheos vs philēdonos antithesis — Regs 43, C15
4. Mic 6:8 — chesed/justice/humility triad — structural cross-registry question OT/NT
5. Racham/womb/compassion nexus — Regs 23, 111, 71
6. Eccl 9:6 — love/hatred/envy as constitutive triad — Reg 75, envy registry
7. Tuv + chesed co-presence (Psa 25:7) — goodness as content of love — Reg 67


---

## Pass 2 — Divine Dimension

### God-as-subject groups: 12 of 66 owner groups (18%)
Dominant pattern: God gives, demonstrates, and constitutes love before commanding it. All 12 god-as-subject groups carry Relational Disposition dimension except one (555-001, Divine-Human Correspondence — Christ as Father's beloved). This is theologically significant: the programme classifies divine love as Relational Disposition not Theological/Divine-Human, consistent with the programme's principle that Theological/Divine-Human names what is constitutively defined by the divine relationship.

### Divine involvement patterns identified

**Pattern 1 — God as the one who loves (primary agent):**
- Jer 31:3 (ahavah): "I have loved you with an everlasting love" — divine love as temporal absolute, predating human existence
- Joh 3:16 (agapaō): "God so loved the world that he gave" — love expressed as self-giving, not merely feeling
- Gal 2:20 (agapaō): "who loved me and gave himself for me" — the love is particular and costly simultaneously
- Zep 3:17 (ahavah): "he will rejoice over you with gladness; he will quiet you by his love; he will exult over you" — God's love as active emotional engagement, not merely disposition

**Pattern 2 — God's love as constitutive attribute:**
- Exo 34:6 (rachum): "a God merciful and gracious, slow to anger, abounding in steadfast love" — love named as character not conduct
- Psa 63:3 (chesed): "your steadfast love is better than life" — divine chesed exceeds the highest human value
- Lam 3:22 (chesed): "the steadfast love of the Lord never ceases" — the negation of cessation is the most precise claim the text makes about divine love

**Pattern 3 — God's love as directed toward the person:**
- Psa 127:2 (yadid): "he gives to his beloved sleep" — divine love expressed as specific particular gift
- Jer 12:7 (yedidut): "the beloved of my soul" — Israel named as the object of God's deepest inner attachment; its abandonment named as God's deepest grief
- Rom 1:7 (agapētos): believers addressed as "loved by God and called to be saints" — belovedness as ontological status preceding calling

**Pattern 4 — God's love mediated through the Spirit/Christ:**
- Rom 5:5 (agapē): "poured into our hearts through the Holy Spirit" — love as pneumatic infusion, not moral attainment
- 1Jo 4:19 (agapaō): "we love because he first loved us" — the logical/temporal priority of divine love is the ground of human love

**Pattern 5 — Divine compassion as womb-love:**
- Isa 49:15 (racham): God's compassion exceeds a nursing mother's — the maternal metaphor grounds divine love in the most bodily, pre-cognitive human attachment
- Isa 63:15 (rachamim): "the stirring of your inner parts and your compassion" — divine inner movement named with the same vocabulary as bodily visceral response
- Jer 31:20 (racham): "my heart yearns for him; I will surely have mercy on him" — divine love for Ephraim as a felt inner movement, not merely a disposition

**Pattern 6 — The Father-Son love as archetype:**
- Mat 3:17 / Mar 12:6 (agapētos): "This is my beloved Son, with whom I am well pleased" — the divine declaration at baptism/transfiguration names the love of Father for Son as the ground-level love in the universe. All human love participates in or reflects this prior love.

### Dominant divine-human relationship pattern
God's love is: (1) prior — it precedes human response; (2) constitutive — it is what God is, not merely what God does; (3) costly — expressed through self-giving; (4) particular — directed at specific persons, not abstractions; (5) bodily-analogue — described through the most intimate bodily love metaphors (womb, nursing, heart-yearning).

Human love is: derivative (from the prior divine love), responsive (answering to God's act), parallel in structure (God loves enemies → humans commanded to love enemies).

### Eschatological dimension
- Psa 27:13 (tuv): "I shall look upon the goodness of the Lord in the land of the living" — eschatological hope grounded in divine goodness
- Hos 3:5 (tuv): "they shall come in fear to the Lord and to his goodness in the latter days" — divine goodness as the eschatological destination
- Jer 31:3 (ahavah): "everlasting love" — love's eschatological character stated as duration

### Session C check (Section 2, dynamic 6 — ultimate source)
"Love's ultimate source is not self-generated" — CONFIRMED with precision. The data shows this is not merely a theological claim but a structural feature of the vocabulary: the god-as-subject groups for agapē and agapaō (562-001, 571-002) are specifically built around the prior divine act. 1Jo 4:19 anchor verse makes the causative sequence explicit.

### mti_term_flags directives required (Pass 2)
Per v4.7 Section Pass 2 — do NOT update god_as_subject field; issue directives for mti_term_flags:
- GOD_AS_SUBJECT flag (flag_id 1) to be inserted for: H2617A, H7349, H7355, H7356B, H3033, H3039A, G0025, G0026, G0027, G5363 — all terms with god-as-subject groups confirmed
- FRAMEWORK_SIGNAL phase2 flag to be added to: G0025, G0026, H0160, H2617A, H7355 — divine-human relationship has direct implications for spirit-soul-body classification (love is spirit-primary in its divine form)
- These will be included in the CC directive for Stage 2

### SD Pointers raised in Pass 2 (additions to Pass 1 list)
SD8: Jer 12:7 (yedidut) — "beloved of my soul" — God abandons his beloved. The grief of abandoned love as a divine inner-being state. Does God experience grief as an inner-being characteristic? Regs 71 (grief), 182 (Soul), 103 (love). Structural question for Session D.
SD9: Mat 3:17/Mar 12:6 (agapētos) — Father-Son love as the archetype. Does the programme have a registry that examines the divine inner life as a model for human inner life? This is the deepest reading of the word study's data and may require a dedicated Session D cross-registry investigation. Reg 68 (grace), C15 cluster.
SD10: Zep 3:17 (ahavah) — "he will rejoice over you with gladness; he will quiet you by his love" — God's love produces rest/quietness in the beloved. Cross-registry: love → peace (Reg 117), love → rest/stillness. SD POINTER.

