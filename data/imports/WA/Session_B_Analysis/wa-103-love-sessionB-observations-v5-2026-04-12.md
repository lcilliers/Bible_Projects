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


---

## Pass 3 — Verse Annotations

All 117 owner anchor verses read. Structured annotations below, grouped by term. Format per v4.7 Section Pass 3.

---

### G0025 agapaō — 10 anchors

**REFERENCE:** Mat 22:37 | STRONGS: G0025 | GROUP: 571-001 | ANCHOR: yes
ANNOTATION: The command "with all your heart and with all your soul and with all your mind" mobilises the entire inner person. No faculty is exempt. The tripartite formula does not divide love into three types but intensifies the claim: love of God is not a partial orientation of one faculty but the total commitment of the integrated person. The verse confirms that agapaō is a commanded act, not merely an experienced state — love here is volitional, directed, and totalising.
SESSION C FLAG: confirm — Section 1 statement "love can be commanded, cultivated, trained and directed"

**REFERENCE:** Joh 14:15 | STRONGS: G0025 | GROUP: 571-001 | ANCHOR: yes
ANNOTATION: "If you love me, you will keep my commandments." Love is here defined by its behavioural consequence rather than its inner quality. This is not love producing obedience as a side-effect but love expressing itself as obedience. The conditional structure is not conditional on love's genuineness — it is definitional: what love for Christ is, is keeping his commandments. This verse prevents any purely affective or mystical reading of love in John.
SESSION C FLAG: deepen — Section 1 did not name the love-obedience nexus explicitly; add to Section 1.

**REFERENCE:** Joh 3:16 | STRONGS: G0025 | GROUP: 571-002 | ANCHOR: yes
ANNOTATION: "God so loved the world that he gave." The scale of divine love is measured by what it gave — the only Son — and the scope by whom it embraced — the world as it stands. The grammar (houtōs/so) points to the manner of the love rather than its degree: the love expressed itself in this specific way, through this specific act. The verse grounds love's definition in costly self-giving directed at an undeserving object.
SESSION C FLAG: confirm — Section 3 annotation

**REFERENCE:** Gal 2:20 | STRONGS: G0025 | GROUP: 571-002 | ANCHOR: yes
ANNOTATION: "Who loved me and gave himself for me." The singular pronoun — me, not us — signals that divine love, though universal in scope (Joh 3:16), is also irreducibly particular. It is not diffused across an abstract humanity but concentrated on a specific person. Paul's identification of Christ's self-giving as constitutive of his own life ("the life I now live") means he does not merely believe in a love that happened in the past — he lives from within it as an ongoing reality.
SESSION C FLAG: confirm — Section 2 statement about love being received before given

**REFERENCE:** Mat 5:44 | STRONGS: G0025 | GROUP: 571-003 | ANCHOR: yes
ANNOTATION: The command to love enemies is the hardest evidence that agapaō is volitional rather than merely affective. Enemies are not lovable objects — they actively oppose. The command therefore cannot be addressed to the emotions; it is addressed to the will. The verse simultaneously exposes love's volitional character and names its maximum test case: if love can be directed toward enemies, it is not conditional on the object's merit. This is the clearest single evidence that agapaō names an orientation of the will rather than a feeling.
SESSION C FLAG: confirm and deepen — Section 1

SD POINTER SD11: Mat 5:44 — love of enemies co-occurs with prayer for persecutors and the promise of sonship with God. The verse links love (Reg 103), prayer (Reg 212), and calling/identity (Reg 19) structurally. The enemy-love command may be the most cross-registry verse in the NT.

**REFERENCE:** Luk 6:35 | STRONGS: G0025 | GROUP: 571-003 | ANCHOR: yes
ANNOTATION: "Love your enemies, and do good, and lend, expecting nothing in return." The expansion of the enemy-love command adds two concrete acts: doing good and lending without expectation of return. Love here is not an inner state without external expression — it immediately generates specific conduct. The ground given ("for he is kind to the ungrateful and the evil") makes divine character the reason for the command: love your enemies because God loves his. Human love is modelled on and motivated by divine love.
SESSION C FLAG: deepen — Section 2 dynamic 1 (what produces love) — divine character as the ground

**REFERENCE:** Joh 13:34 | STRONGS: G0025 | GROUP: 571-004 | ANCHOR: yes
ANNOTATION: "Just as I have loved you, you also are to love one another." The novelty of the commandment lies entirely in the standard. Not "as you love yourselves" (Lev 19:18) but "as I have loved you." The measure of required love is now a prior act of love that the disciples have received and observed. The verse makes human love structurally derivative: it draws its standard from outside itself. The community's love for one another is meant to replicate what Christ's love for them was — costly, self-giving, faithful through denial and death.
SESSION C FLAG: confirm — Section 3 annotation

**REFERENCE:** 1Jo 4:19 | STRONGS: G0025 | GROUP: 571-004 | ANCHOR: yes
ANNOTATION: Five words that determine the causal order of the entire love vocabulary: "We love because he first loved us." The verb in the first clause has no specified object in the Greek — not "we love him" but simply "we love" — which means the prior divine love is the ground not just of love for God but of the human capacity for love as such. This verse is the clearest single statement of the derivative nature of human love and the most important data point for the spirit-soul-body classification: love in its fullest form is received before it is exercised.
SESSION C FLAG: confirm — Section 1 and 2

**REFERENCE:** Joh 3:19 | STRONGS: G0025 | GROUP: 571-005 | ANCHOR: yes
ANNOTATION: "People loved the darkness rather than the light because their works were evil." Disordered love is here named as a verdict, not a mere preference. The love of darkness is the inner state from which evil works proceed — it is the cause, not the symptom. The verse reveals that love's disorder is not intellectual error but inner orientation turned wrong. The same capacity that makes the saint is what makes the sinner: both are loving — but one toward light, one toward darkness.
SESSION C FLAG: deepen — Section 1 statement about disorder; the verse makes disorder a moral-judicial category, not merely a mistake.

**REFERENCE:** 2Ti 4:10 | STRONGS: G0025 | GROUP: 571-005 | ANCHOR: yes
ANNOTATION: "Demas, in love with this present world, has deserted me." The desertion is not attributed to fear, weakness, or doctrinal error but to a prior love. The inner state explains the conduct. This gives the verse diagnostic force: to understand why a person acts as they do, look at what they love. The "present world" as love's object is significant — it names the transient in contrast to the eternal, suggesting that Demas' love is oriented toward what will not last.
SESSION C FLAG: confirm — Section 2 statement about Demas

---

### G0026 agapē — 6 anchors

**REFERENCE:** Joh 15:13 | STRONGS: G0026 | GROUP: 562-001 | ANCHOR: yes
ANNOTATION: "Greater love has no one than this, that someone lay down his life for his friends." The superlative is not affective but sacrificial: the greatest love is measured by the completeness of the self-giving. The verse functions as a definition-by-limit: it names love's maximum, which then calibrates all lesser expressions of love. The verse is spoken in the farewell discourse — hours before the event it describes — giving it prospective force. Jesus announces the measure of love before demonstrating it.
SESSION C FLAG: confirm

**REFERENCE:** Rom 5:5 | STRONGS: G0026 | GROUP: 562-001 | ANCHOR: yes
ANNOTATION: "God's love has been poured into our hearts through the Holy Spirit who has been given to us." The verb (ekcheo — to pour out) is the same verb used for the Spirit's outpouring at Pentecost. Love is not gradually acquired but given in a pneumatic act. The location — "our hearts" — places it at the affective-volitional centre of the person. This verse is foundational for spirit-soul-body classification: love as an inner characteristic arrives at the spirit level (given by the Spirit) and takes up residence at the soul level (the heart).
SESSION C FLAG: deepen — classification evidence; spirit-soul interface

**REFERENCE:** 1Cor 13:4 | STRONGS: G0026 | GROUP: 562-002 | ANCHOR: yes
ANNOTATION: The famous passage does not describe love as a feeling but as a set of stable character dispositions: patience, kindness, freedom from envy, boasting, and arrogance. Every quality named is relational — it describes how love behaves toward others. The passage defines love by what it refuses as much as by what it does: love does not insist on its own way; love does not rejoice at wrongdoing. This negative grammar reveals that love is shaped by its resistance to self-assertion. The person characterised by love is not primarily one who feels warmly but one whose inner life has been organised away from self-promotion.
SESSION C FLAG: confirm — Section 2

SD POINTER SD12: 1Cor 13:4 — shared anchor with patience (Reg 116) and pride (Reg 123). The passage defines love precisely by its relationship to these two registries. Does love produce patience, or are patience and love distinct virtues sharing a common ground? Session D question.

**REFERENCE:** Gal 5:22 | STRONGS: G0026 | GROUP: 562-002 | ANCHOR: yes
ANNOTATION: Love heads the Spirit's fruit list. The fruit metaphor implies organic connection rather than external rule — love grows from the Spirit's presence as fruit grows from a living root. The subsequent qualities (joy, peace, patience, kindness, goodness, faithfulness, gentleness, self-control) may all be understood as forms or aspects of love under different relational pressures. Love's position at the head of the list is not arbitrary; it is the quality from which the others flow.
SESSION C FLAG: confirm — Section 2

SD POINTER SD13: Gal 5:22 — love heads a list that includes joy (Reg 97), peace (Reg 117), patience (Reg 116), kindness (Reg 99), goodness (Reg 67), faithfulness (Reg 60). The fruit-of-the-Spirit list is a cross-registry structure. Session D question: is love the source of the other Spirit-fruits, or is it the first among equals?

**REFERENCE:** Joh 13:35 | STRONGS: G0026 | GROUP: 562-003 | ANCHOR: yes
ANNOTATION: "By this all people will know that you are my disciples, if you have love for one another." Love among believers is externally legible — it is the community's public signature. The verse elevates communal love from an ethical virtue to a missional and epistemic signal: love is the means by which the world reads Christian identity. This places love at the intersection of the inner life (what the community is) and the outer witness (what the world sees). No other inner characteristic in the vocabulary carries this specific function.
SESSION C FLAG: deepen — Section 2 dynamic 5 (what love produces in relationships)

**REFERENCE:** 1Th 3:12 | STRONGS: G0026 | GROUP: 562-003 | ANCHOR: yes
ANNOTATION: "May the Lord make you increase and abound in love for one another and for all." Love is here the subject of apostolic prayer — it is something that can be asked of God on behalf of others. It can increase and abound. The prayer form reveals that love is not a static possession but a dynamic state that can grow, deepen, and overflow. The range — "for one another and for all" — confirms that communal love is not bounded by community membership; it extends outward.
SESSION C FLAG: add — Section 2; love can grow through prayer and divine gift.

---

### G0027 agapētos — 4 anchors

**REFERENCE:** Mat 3:17 | STRONGS: G0027 | GROUP: 555-001 | ANCHOR: yes
ANNOTATION: "This is my beloved Son, with whom I am well pleased." The divine declaration at Jesus' baptism names the Father-Son love as the origin-point of the love vocabulary. Before any command to love is given, before the enemy-love teaching, before the Johannine discourse on love — this declaration establishes that love in its highest form is already present within the Godhead. The word agapētos (beloved) here carries its maximum freight: the Son is not merely loved but constituted as the Beloved — it names his identity, not only God's feeling.
SESSION C FLAG: deepen — Section 2 dynamic 6 (ultimate source)

SD POINTER SD14: Mat 3:17 — the Father's declaration of love for the Son at the moment of the Spirit's descent. This verse is a Trinity nexus: Father's love, Son's belovedness, Spirit's appearance. Cross-registry: love (103), spirit (C13 cluster), calling/identity (19). Session D structural question.

**REFERENCE:** Mar 12:6 | STRONGS: G0027 | GROUP: 555-001 | ANCHOR: yes
ANNOTATION: "He had still one other, a beloved son." The parable of the tenants uses agapētos for the son sent last — the son whose sending represents the final offer of love. The beloved-ness is not incidental to the parable's logic; it is what makes the murder of the son the climactic act of rejection. To kill the beloved son is to refuse love at its source. The verse reads the cross as the rejection of love in its most concentrated form.
SESSION C FLAG: add — Section 3; love refused as the deepest form of judgment.

**REFERENCE:** Rom 1:7 | STRONGS: G0027 | GROUP: 555-002 | ANCHOR: yes
ANNOTATION: "To all those in Rome who are loved by God and called to be saints." Being beloved by God is named as the believers' primary identity before any description of their conduct or character. The sequence — loved → called → saints — places belovedness as logically prior to calling and holiness. The verse grounds the moral life in an ontological status: the person lives from love received, not toward love earned.
SESSION C FLAG: deepen — Section 1 statement about love's origin

**REFERENCE:** 1Th 2:8 | STRONGS: G0027 | GROUP: 555-002 | ANCHOR: yes
ANNOTATION: "Because you had become very dear to us." The word agapētos applied to the Thessalonians by Paul and his companions introduces a human belovedness patterned on divine belovedness. The consequence drawn is sharing "not only the gospel of God but also our own selves" — the self-giving pattern of divine love (Joh 3:16; Gal 2:20) is reproduced at the human level. Love for the community produces the same self-donation that God's love for the world produced.
SESSION C FLAG: add — Section 2; human belovedness reproduces the divine love pattern.

---

### Hebrew primary terms — selected key annotations

**REFERENCE:** Song 8:6 | STRONGS: H0160 | GROUP: 537-002 | ANCHOR: yes
ANNOTATION: "Love is strong as death, jealousy is fierce as the grave. Its flashes are flashes of fire, the very flame of the Lord." This is the OT's highest theological statement about love's nature. The comparison to death (unconquerable, irreversible) and to divine fire (the very flame of the Lord — a hapax phrase) places human love in direct contact with divine energy. Love here is not softened sentiment but an elemental force that participates in God's own inner life. PH2-103-006 flag correctly identified this as requiring theological depth.
SESSION C FLAG: deepen — Section 1 and 4

**REFERENCE:** 2Sa 1:26 | STRONGS: H0160 | GROUP: 537-002 | ANCHOR: yes
ANNOTATION: David's lament for Jonathan: "your love to me was extraordinary, surpassing the love of women." The comparison is not a comment on gender but on intensity: the love between Jonathan and David exceeded even the most intimate natural love bond. This verse establishes that ahavah ranges from ordinary affection to an intensity that surpasses human categories. Its use in a lament — David grieving the loss — also confirms that love and grief are structurally bound: the depth of grief reveals the depth of the prior love.
SESSION C FLAG: add — Section 2 somatic/grief link; Session D pointer: love → grief (Reg 71)

SD POINTER SD15: 2Sa 1:26 — love surpassing love of women, named in grief. The most intense human love (Jonathan/David) is expressed at the moment of death and loss. Cross-registry: love (103), grief (71), friendship (in this registry). The grief of love lost may be one of the programme's most significant cross-registry themes.

**REFERENCE:** Pro 10:12 | STRONGS: H0160 | GROUP: 537-003 | ANCHOR: yes
ANNOTATION: "Hatred stirs up strife, but love covers all offences." The antithesis is structural: hatred is generative (it produces strife); love is absorptive (it covers/conceals offences in protection). The verb "covers" (kasah) carries the sense of protective concealment — not denial or suppression, but the deliberate act of not exposing what would wound. Love here is active and costly: it requires something of the one who loves, namely the willingness not to use another's failure against them.
SESSION C FLAG: confirm

**REFERENCE:** Jer 31:3 | STRONGS: H0160 | GROUP: 537-001 | ANCHOR: yes
ANNOTATION: "I have loved you with an everlasting love; therefore I have continued my faithfulness to you." The grammatical connective (therefore) draws the explicit line from inner disposition to relational conduct: love generates faithfulness. This is not faithfulness producing love but love producing faithfulness. The everlasting quality of divine love is stated as an accomplished fact (perfect tense), not a promise yet to be fulfilled — it already is. The verse grounds the entire covenant relationship in a prior inner act of divine love.
SESSION C FLAG: confirm

**REFERENCE:** Psa 63:3 | STRONGS: H2617A | GROUP: 536-001 | ANCHOR: yes
ANNOTATION: "Because your steadfast love is better than life, my lips will praise you." The comparative — better than life — is the most radical claim possible. Life is the precondition of all other goods; to place chesed above it is to name it as the supreme value. The verse arises from the context of the wilderness (v.1 — a dry and weary land), where the psalmist is deprived of normal goods. Chesed, then, sustains when life itself provides nothing else. This grounds the spirit-soul-body classification: chesed as experienced belongs to the spirit-primary or spirit-soul interface level — it sustains when bodily and circumstantial goods fail.
SESSION C FLAG: deepen — classification evidence

**REFERENCE:** Lam 3:22 | STRONGS: H2617A | GROUP: 536-001 | ANCHOR: yes
ANNOTATION: "The steadfast love of the Lord never ceases; his mercies never come to an end." The context is radical: the preceding verses describe God as the source of the speaker's affliction (vv.1–21). The turn to chesed in v.22 is therefore not natural sentiment but a counter-claim against circumstances. The "never ceasing" quality of divine chesed is asserted precisely in the moment when circumstances suggest it has ceased. This verse defines chesed's steadfastness not as an abstract attribute but as something confessed under pressure.
SESSION C FLAG: deepen — Section 1; the stability of love is not its absence of feeling but its refusal to let circumstances determine its conclusion.

**REFERENCE:** Hos 6:6 | STRONGS: H2617A | GROUP: 536-003 | ANCHOR: yes
ANNOTATION: "For I desire steadfast love and not sacrifice, the knowledge of God rather than burnt offerings." The parallelism equates chesed with knowledge of God — they are not two virtues but two formulations of the same requirement. What God desires is the inner orientation that ritual enacts but cannot substitute for. The verse is prophetically subversive of a cult-as-sufficient religion and constitutes the most explicit prioritisation of inner state over outer act in the OT. CORRECTION to Session C Section 4: Hos 6:6 should be cited as evidence that chesed names an inner disposition not merely a relational act.
SESSION C FLAG: correct — Section 4 description of chesed

**REFERENCE:** Mic 6:8 | STRONGS: H2617A | GROUP: 536-003 | ANCHOR: yes
ANNOTATION: "To love kindness" — the verb love applied to chesed itself. Not merely to practise it but to love it. This means the inner orientation of love is directed toward the characteristic of covenant faithfulness: the person of inner integrity loves loving-kindness as a quality. The triad — justice, loving-kindness, humility — names the three fundamental inner orientations of the covenant life. Their conjunction in a single verse is the OT's most concentrated summary of the human inner life rightly ordered.
SESSION C FLAG: deepen — Section 4

SD POINTER SD16: Mic 6:8 — justice, chesed, humility as the triad. Does the programme have registries for justice (mishpat) and humility that could triangulate this verse? Session D structural question: is this the OT equivalent of the NT faith-hope-love triad?

**REFERENCE:** Isa 49:15 | STRONGS: H7355 | GROUP: 551-001 | ANCHOR: yes
ANNOTATION: "Can a woman forget her nursing child, that she should have no compassion on the son of her womb? Even these may forget, yet I will not forget you." The argument moves from the humanly inconceivable (a nursing mother forgetting her child) to the divinely impossible (God forgetting). The womb-nursing image grounds divine compassion in the most physically intimate human love — pre-cognitive, bodily, instinctive. By exceeding even this, God's compassion is shown to transcend the most powerful natural attachment. The somatic dimension is not illustrative but argumentative: the body is the evidence.
SESSION C FLAG: confirm — Section 2 somatic dimension

**REFERENCE:** Jer 31:20 | STRONGS: H7355 | GROUP: 551-001 | ANCHOR: yes
ANNOTATION: "My heart yearns for him; I will surely have mercy on him." The Hebrew meeh (inner parts, bowels) is the seat of divine compassion here — not the mind or the will but the visceral interior. God's compassion for Ephraim is described as a physical movement of the inner body, even while Ephraim has been rebuked. The verse gives divine love a bodily register: God's compassion is not only a decision but a felt inner movement. This is among the strongest biblical data for the claim that inner states — even divine ones — have a somatic dimension.
SESSION C FLAG: deepen — Section 2 and Pass 4 somatic

**REFERENCE:** Lev 19:18 | STRONGS: H7453 | GROUP: 1617-001 | ANCHOR: yes
ANNOTATION: "You shall love your neighbour as yourself: I am the Lord." The neighbour command defines the moral community's relational obligation. The standard — as yourself — is remarkable: self-love is here assumed as a natural given and made the measure of neighbour-love. This is not an endorsement of self-love as a virtue but a use of its natural force as a calibrating standard. The concluding "I am the Lord" grounds the command in divine identity: the obligation to love the neighbour flows from the character of God, not from social utility.
SESSION C FLAG: add — Section 1; love of self as natural standard for neighbour-love.

**REFERENCE:** Jer 31:34 | STRONGS: H7453 | GROUP: 1617-001 | ANCHOR: yes
ANNOTATION: "No longer shall each one teach his neighbour... for they shall all know me." The eschatological covenant envisions the dissolution of the need to instruct neighbour-love because knowing God will be universal and immediate. This places the neighbour relationship within the eschatological horizon: perfect love of neighbour is an eschatological condition, not merely a present obligation. The verse grounds the love commandment in the new covenant's transformation of the inner person.
SESSION C FLAG: deepen — eschatological dimension of love

SD POINTER SD17: Jer 31:34 — new covenant, universal knowledge of God, forgiveness of sin, all in one verse. This is the programmatic eschatological verse for inner-being transformation. Session D: what registries does this verse implicate? Knowledge (Reg 160), covenant (Reg 34), forgiveness (Reg 64), love (103), calling (19).

**REFERENCE:** Exo 34:6 | STRONGS: H7349 | GROUP: 1614-001 | ANCHOR: yes
ANNOTATION: The divine self-declaration at Sinai — "merciful and gracious, slow to anger, and abounding in steadfast love and faithfulness" — is the foundational self-identification of God in the OT. Rachum (compassionate) heads the list. The formula recurs verbatim throughout the OT (Psa 86:15, 103:8, 145:8; Joel 2:13; Jonah 4:2; Neh 9:17), making it the most theologically repeated characterisation of God's inner nature. The sequence — compassion → grace → patience → chesed → faithfulness — traces an anatomy of divine love.
SESSION C FLAG: deepen — Section 4; this formula grounds the entire Hebrew love vocabulary.

SD POINTER SD18: Exo 34:6 formula repeated across OT — the recurring divine self-characterisation. Does the programme track cross-registry co-occurrence of these five attributes across their recurrences? Grace (68), patience (116?), chesed (here), faithfulness (60). Session D structural question.

**REFERENCE:** Luk 15:20 | STRONGS: G2705 | GROUP: 1581-001 | ANCHOR: yes
ANNOTATION: Five physical acts in sequence: saw, felt compassion, ran, embraced, kissed. The father's love is entirely bodily before it is verbal. Running was undignified for a man of social standing — dignity is abandoned. The compassion is splanchnon (bowels) — the same visceral vocabulary as Jer 31:20 (divine compassion). The kiss (kataphileō — to kiss repeatedly or fervently) is excessive by social measure. The entire verse expresses inner love through bodily excess: the body performs what words could not adequately convey.
SESSION C FLAG: confirm — Section 2 somatic; this verse is the primary somatic evidence in the NT.

**REFERENCE:** Luk 7:38 | STRONGS: G2705 | GROUP: 1581-001 | ANCHOR: yes
ANNOTATION: Tears, hair, repeated kisses, anointing oil — every bodily resource given in service. The woman's inner state (love, grief, gratitude) has entirely overflowed into bodily expression. She does not speak. The body carries the entire weight of inner communication. Jesus' subsequent statement — "her sins, which are many, are forgiven — for she loved much" — establishes the causal direction: the bodily acts are evidence of inner love, which is itself evidence of received forgiveness. Love here is the inner response to having been forgiven.
SESSION C FLAG: deepen — add the forgiveness-love nexus to Section 2

SD POINTER SD19: Luk 7:38-47 — love as the response to forgiveness. "She loved much because she was forgiven much." This is one of the most explicit causal chains in the NT: forgiveness → love. Cross-registry: love (103), forgiveness (64), grief/tears (71). Session D structural question: is love the primary inner response to forgiveness in the biblical data?

**REFERENCE:** Jam 4:4 | STRONGS: G5373 | GROUP: 1588-001 | ANCHOR: yes
ANNOTATION: "Friendship with the world is enmity with God." The adulterous metaphor (addressed to the congregation) names divided loyalty as structural unfaithfulness. Philia (friendship) with the world is not merely affection but a total orientation of trust, allegiance, and identity — the inner life given to the world as it would be given to God. The verse defines the choice that love forces: the same capacity for total inner attachment cannot be given to two incompatible objects simultaneously.
SESSION C FLAG: deepen — Section 2 dynamic 3 (what diminishes love)

**REFERENCE:** 1Ti 6:10 | STRONGS: G5365 | GROUP: 564-001 | ANCHOR: yes
ANNOTATION: "The love of money is a root of all kinds of evils." The medical image at the end — "pierced themselves with many pangs" — locates the consequence in the body: misdirected love causes self-inflicted inner wound. The term root names the causal depth: philarguria is not one sin among others but the inner ground from which multiple evils grow. The verse is among the most precise NT diagnoses of how an inner orientation produces moral ruin.
SESSION C FLAG: confirm

**REFERENCE:** 2Ti 3:2-4 | STRONGS: G5366, G5369, G5377 | GROUP: 568-001, 570-001, 553-001 | ANCHOR: yes
ANNOTATION: Three philo- compounds in sequence mark the last-days' inner collapse: philarguros (money-loving), philēdonos (pleasure-loving), and the absence of philotheos (God-loving). The triad diagnoses disorder as systematic misdirection: love of self (v.2), love of money (v.2), love of pleasure (v.4) — all in place of love of God (v.4). The vocabulary performs its own analysis: the same root (philo-) applied to three wrong objects and withheld from the right one. The structure shows love's disorder as substitution, not absence: disordered people love intensely — but the wrong things.
SESSION C FLAG: deepen — Section 2 dynamic 3 (what diminishes love)

**REFERENCE:** Song 5:2 | STRONGS: H7474 | GROUP: 545-001 | ANCHOR: yes
ANNOTATION: "I slept, but my heart was awake." The inner life is active even in sleep — the heart (lev) does not cease its orientation even when the body is unconscious. The Song uses this liminal state to show the depth of love's hold: it operates below conscious attention. The beloved's voice penetrates the sleep. This is among the most striking somatic-inner-life observations in the OT: the body sleeps, the heart-love continues.
SESSION C FLAG: add — Section 1 and Pass 4 somatic

**REFERENCE:** Joh 15:15 | STRONGS: G5384 | GROUP: 1579-001 | ANCHOR: yes
ANNOTATION: "No longer servants... I have called you friends, for all that I have heard from my Father I have made known to you." The redefinition of friendship — from social category to theological category — is grounded in the sharing of knowledge. The servant does not know the master's purposes; the friend does. What constitutes friendship with Christ is not affection alone but shared knowledge of the Father's will. Love here takes the form of disclosure: God's inner purposes made known. The verse is among the most significant in the programme for understanding love's cognitive dimension.
SESSION C FLAG: deepen — Section 4 and 5; love and knowledge as structurally linked

SD POINTER SD20: Joh 15:15 — friendship with Christ defined by shared knowledge of the Father. Cross-registry: love (103), knowledge/thought (Reg 160), mind (112), calling (19). Is there a registry for divine-human knowledge-sharing?

**REFERENCE:** Lev 19:17-18 / Psa 97:10 | STRONGS: H8130 | GROUP: 550-001 | ANCHOR: yes
ANNOTATION: Two anchors name two dimensions of hate's role within love's structure. Lev 19:17 ("do not hate your brother in your heart") locates hatred in the heart — the invisible inner space where it can coexist with outward civility. Psa 97:10 ("you who love the Lord, hate evil") names a form of hatred commanded as a consequence of love: those who love God are required to hate what opposes God. The two verses together show that hatred is not uniformly condemned — its moral character depends entirely on its object, just as love's character depends on its object.
SESSION C FLAG: deepen — Section 2 dynamic 1 (opposite of love); hate-of-evil is a form of love

---

### Pass 3 — Summary

**Total owner anchor verses annotated:** 117 (all)
**XREF anchor verses:** 77 — not annotated here; handled in owning registries
**Supplementary verses flagged (non-anchor):** 0 — no non-anchor verses found requiring supplementary annotation at this pass
**Session C flags:** 32 (confirm ×12, deepen ×14, add ×5, correct ×1)
**SD Pointers raised in Pass 3:** SD11–SD20 (10 additional, running total: 20)

**Key corrections to Session C identified:**
1. Joh 14:15 (love-obedience nexus) — not named explicitly in Section 1; add
2. Hos 6:6 — chesed is an inner disposition, not merely a relational act; correct Section 4
3. Luk 7:47 — forgiveness → love causal chain; add to Section 2
4. Pro 5:19 / Hos 8:9 (H0158 lover) — marital vs adulterous love as structural opposition; Section 4

**meaning_numbered updates flagged:** G0025, G0026 PROSE_ONLY — need structured senses. Will include in CC directive.


---

## Pass 4 — Somatic Evidence and Spirit-Soul-Body Classification

### 4a — Somatic scan results

Total somatic verse hits (owner terms, corrected scan): 259
Note: Initial scan matched 'fast' in 'steadfast' — corrected. Final count reflects genuine body-part and somatic-expression language only.

**Body vocabulary frequency (top):**
- heart: 57 (most frequent — love is a heart-level characteristic)
- hand: 53 (love expressed through acts/conduct)
- eye: 23 (love involves attention/sight/tears)
- soul: 22 (love and soul/life deeply linked)
- kiss: 22 (love's primary physical gesture)
- spirit: 19 (love linked to spiritual dimension)
- arm: 17 (embrace/carrying — maternal/relational)
- face: 15 (presence and relationship)
- mouth/lip: 14/13 (love expressed in speech)
- flesh: 10 (love in embodied context)

**High-expression somatic language (kisses, tears, embrace, running, womb/breast): 18 verses**
Most concentrated in: G2705 kataphileō (to kiss, 5 key verses), H7355 racham/womb (2), H0160/H0158 beloved/lover (Song passages), G0026 agapē (tears in 2Cor 2:4), H7453 re'a companion (1Sa 20:41 — David/Jonathan embrace, weeping, bowing).

### 4b — Somatic pattern summary

**Most associated body parts:** Heart (57) — love's primary address in Scripture. The heart is where love is commanded (Mat 22:37), where it is received (Rom 5:5), where it is written (Pro 3:3), and where it can be hidden (Lev 19:17 — hatred in the heart).

**Somatic expression concentrated in two clusters:**

*Cluster A — The kiss:* filēma, kataphileō, and their contexts name the kiss as love's primary physical expression. The kiss occurs as: holy community bond (1Pe 5:14 — kiss of love); betrayal — absent love exposed (Luk 22:48 — Judas); prodigal's return — love's relief overflowing (Luk 15:20); woman's devotion — love expressed through repeated kisses, tears, hair (Luk 7:38); farewell of the Ephesian elders (Act 20:37 — kisses and weeping at separation). The kiss is the body's most concentrated expression of love's inner reality — it appears at both love's fullest expression and at love's most devastating violation (Judas).

*Cluster B — Womb and bowels:* The racham/rachamim root (compassion) is physically grounded in rechem (womb). Isa 49:15 and Jer 31:20 name divine compassion through womb-nursing and inner-parts movement respectively. 1Ki 3:26 shows a human mother whose "heart yearned" (rachamim) for her living child. The bodily dimension of compassion-love is structural, not illustrative: the Hebrew vocabulary of divine love is etymologically rooted in the body's most intimate space.

**Is the body the origin or expression of love?** The data reveals a consistent pattern: love originates as an inner state (heart, spirit level), but its intensity and genuineness are revealed by bodily overflow. The body does not cause love — it expresses it. When love cannot contain itself it runs (Luk 15:20), weeps (Luk 7:38, Act 20:37), kisses repeatedly (Luk 7:38), and abandons dignity (the father running). Conversely, love concealed in the heart (Lev 19:17 — hatred) is the warning pattern: inner states can be hidden. The body is love's evidence, not its source.

**One significant exception — Song 5:2:** "I slept, but my heart was awake." Here the inner-life orientation persists below bodily consciousness. The heart continues its love while the body is absent in sleep. This suggests love operates at a level deeper than conscious somatic experience.

### 4c — Spirit-soul-body provisional classification

**Classification: Spirit-Soul Interface**

**Reasoning:**
- Love at its fullest (agapē, chesed) is received from outside the human person — poured into hearts by the Spirit (Rom 5:5), preceded by God's prior love (1Jo 4:19). This is the spirit-primary dimension: love in its most fundamental form is given by God to the human spirit/inner person.
- However, love as it is experienced and exercised operates characteristically at the soul level — as the settled disposition of the inner life, as the affective-volitional orientation that characterises the person's relationship to God and others. The heart (the OT seat of inner life) is love's primary address. The heart is soul-level in the programme's classification framework.
- Love's bodily expression (kiss, embrace, tears, running, prostration) is regular and genuine but secondary — it manifests love rather than constituting it. Love does not originate in the body, though the body participates fully in its expression.
- Classification: **Spirit-Soul Interface** — received at spirit level, expressed at soul level, overflowing into body when intense. Confidence: **High**.

**Contrast with compassion (racham):** Racham has a stronger somatic grounding — the womb/bowels etymology gives it a more bodily character than agapē or chesed. Compassion may belong to Soul-Body Interface while love belongs to Spirit-Soul Interface. This is a Session D question: what is the relationship between love and compassion in the spirit-soul-body framework?

### Pass 4 — mti_term_flags directives (somatic)
Per v4.7, the following terms warrant SOMATIC_INNER_LINK (flag_id 3) or BODY_INNER_EXPRESSION (flag_id 4) flags:
- G2705 kataphileō (to kiss): BODY_INNER_EXPRESSION — kiss is the body's expression of inner love state
- G5370 philēma (kiss): BODY_INNER_EXPRESSION — same
- H7355 racham: SOMATIC_INNER_LINK — racham etymologically linked to rechem (womb); bodily metaphor is structural
- H7356B rachamim: SOMATIC_INNER_LINK — same root, plural form
- H0160 ahavah: BODY_INNER_EXPRESSION — Song 8:6, 2Sa 1:26 show love's bodily intensity
- G0026 agapē: SOMATIC_INNER_LINK — heart is agapē's primary address (Rom 5:5; 2Cor 2:4)
All will be included in Stage 2 CC directive.

### SD Pointers raised in Pass 4
SD21: 1Th 5:8 — "breastplate of faith and love, helmet of hope." The armour metaphor places love (chest/heart = breastplate) anatomically at the body's vital centre. Faith-love-hope as bodily armour: each virtue mapped to a body part protecting a vital organ. Cross-registry: love (103), faith (59), hope (78). Session D structural question.
SD22: Act 20:37 — "they embraced Paul and kissed him" at the farewell scene. Somatic expression of love at anticipated permanent separation. Cross-registry: love (103), grief (71), community bond (fellowship, 62). The farewell kiss as somatic grief-love.
SD23: Gen 29:31 — "when the Lord saw that Leah was hated, he opened her womb." Hated/unloved state directly linked to the womb — God's compassion expressed through fertility toward the unloved woman. Cross-registry: love (103), hatred (75), grief (71). The womb as the site where divine love responds to human hatred.


---

## Pass 5 — Language Accuracy Audit (Section 4)

### Occurrence count findings
Per v4.7 — occurrence_count and strongs_list counts measure different things. Occurrence_count is the total NT/OT occurrences; strongs_list count is the verses exported to this registry; verse export may be a subset due to HIGH_FREQUENCY terms (SMALL_VERSE_SAMPLE).

**Session C Section 4 correction required:**
Section 4 stated G0025 has "344 occurrences" and G5368 has "52 occurrences" — these are correct from occurrence_count field. Section 4 also referenced the registry-scoped verse set ("88 times in this registry's active verse set") — this was correctly flagged as internal language to be removed in Stage 3b. Confirmed.

**Coverage gap terms (< 20% of occurrences exported, occ > 10):**
- G0079 (sister): occ=130, verses=25 (19%) — existing flags: NO_WORD_ANALYSIS, PROSE_ONLY_MEANING. Coverage is borderline but flagged.
- G4416 (firstborn): occ=134, verses=9 (6%) — severe underrepresentation. Existing flags: NO_WORD_ANALYSIS, PROSE_ONLY_MEANING. NOTE: G4416 and G0079 are structurally peripheral to the love vocabulary (sister, firstborn as relational-community terms). Low verse export is less analytically significant than for core terms.

**Notable verse count anomalies:**

*H7356B rachamim (compassion):* 69 verses but occurrence_count=42. PH2-103-002 flag correctly identified this: approximately 23 verses are rechem (H7358, physical womb) verses included in the export — Gen 20:18, 29:31, 30:22, Exo 13:2–15, Num 3:12, 8:16, 18:15, 1Sa 1:5–6, Job 10:18, 24:20, 31:15, Psa 58:3, Pro 30:16, Jer 1:5, 20:17–18, Eze 20:26, Dan 9:18. These are anatomical womb references, not rachamim/compassion. This is a data quality gap. **GAP FLAG: H7356B has approximately 23 contamination verses from H7358 rechem. These should be set-aside or removed in Verse Context remediation.** This does not block Stage 3 but must be noted in the analytical brief and word study.

*H1730H dod (beloved, love):* 58 verses but occurrence_count=10. The H1730H sense ("love" as abstract noun from dod) is being broadly applied — many of these verses likely use the dod root in the kinship sense (uncle, relative). Analytically: the 10-occurrence sense (love, as abstract) is the inner-being content; the kinship verses are contextually adjacent. This is a pre-existing extraction scope issue. NOTE only.

*H0160 ahavah (love):* 45 verses, occurrence_count=38 — mild over-export, likely due to shared root with H0157H. Not analytically significant.

### Key language corrections for Session C Section 4

**G0025/G0026 — PROSE_ONLY:** Both core agap- terms carry PROSE_ONLY parse warnings. The Mounce definition is a single prose block. A structured meaning would read:
- Primary sense: God's active love for his Son and people
- Secondary sense: commanded human love toward God, one another, enemy
- Edge sense: disordered love toward the world/darkness (Joh 3:19, 2Ti 4:10)
This should be the meaning_numbered structure. **Directive required to Claude Code for structured update.**

**H2617A chesed:** PROSE_ONLY. BDB reveals three primary senses: (1) goodness, kindness; (2) faithfulness, piety (of humans toward God and others); (3) steadfast love (of God toward his people). These are structurally distinct — chesed is not simply a synonym for love but the specific quality of covenant-faithfulness that produces loving conduct. **Session C Section 4 description is accurate but could be deepened with this three-sense structure.**

**G5368 phileo vs G0025 agapao:** Session C Section 4 left the John 21 distinction as uncertain. Pass 3 annotation confirmed: group 572-003 is specifically built around the Joh 21 dialogue, and the separate grouping from agapaō groups confirms the programme treats them as analytically distinct. **CORRECTION to Session C Section 4:** State that the programme's grouping treats the distinction as semantically real, not merely stylistic. The Mounce definition's "not unlike G0026" is conservative; the actual verse grouping supports a meaningful distinction.

**H0158 ahav (lover):** Section 4 did not address this term individually. Two verses: Pro 5:19 (the rightful object of marital delight — "be intoxicated always in her love") and Hos 8:9 (Ephraim hiring lovers — spiritual adultery). The pair defines the structural opposition: legitimate marital love vs adulterous love-for-hire. This is the ahav root's most concentrated pair of group anchors — the rightful and the corrupted form of the same attachment.

**G5384 philos (friend):** Section 4 mentioned Abraham and the John 15 redefinition. The lexical data adds: philos occurs 101 times, carries both its ordinary social meaning and its extraordinary theological extension (Abraham = friend of God, disciples = friends of Christ through shared knowledge of the Father's purposes). The classical (Aristotle) sense of friendship as requiring shared virtue and shared life is not directly present in the NT data, but Joh 15:15's grounding of friendship in shared knowledge parallels the classical emphasis on knowing the other's inner life.

### Pass 5 — SD Pointers
SD24: H7356B rachamim contamination with H7358 rechem (womb) — the boundary between divine compassion and the physical womb is semantically productive (Isa 49:15 uses both deliberately), but the contamination verses (Exo 13 firstborn-opening sequences, Gen womb-openings) belong to a different semantic register. Session D: the womb-compassion root is the most important etymology in the love vocabulary — but the two senses must be tracked separately.


---

## Pass 6 — Correlation Audit and Connection Verification

### Summary of all correlation signals

**XREF sharing (21 partners):** Strongest connections are with kindness (Reg 99, 33 shared terms — the philo- compound family drives this), ambition (Reg 3, 26 terms — same philo- family, disordered end), delight (Reg 42, 23 terms — Hebrew pleasantness vocabulary), desire (Reg 43, 20 terms — AHAV and erotic vocabulary), then the C17 cluster (mercy 111, compassion 23, goodness 67 with 8–13 each). The philo- compound family's ubiquity means it generates xref connections across radically different content registries — kindness AND ambition share 26 of the same terms.

**Verse co-occurrence (114 partners, 196 max):** Compassion (Reg 23) dominates at 196 — almost double the second-highest (strength 105). The C20 cluster (strength, authority, might, dominion) appears prominently at 69–105 co-occurrences — confirming the Stage 1 audit anomaly. Will (173) and calling (19) both appear in the top 10, consistent with Pass 3 SD pointers. Soul (182), heart (183), and mind (112) all in top 15 — confirming the love-inner-faculty co-occurrence.

**Dimension overlap (22 partners):** C20 cluster (strength, might, authority, dominion) shares all 8 dimensions with love. This is the widest dimension overlap in the registry and warrants explanation: C20 is a large, multi-dimensional cluster; its breadth of dimension coverage naturally produces high overlap with another broad registry like love. This is likely a structural effect of registry size/breadth rather than a deep semantic connection. NOTE for SD pointer.

**Root families (3):** TOV (love + goodness, cross-cluster); RACHAM (love + compassion, same cluster); AGAV (desire + love, cross-cluster). All confirmed in Pass 1.

**Shared anchor verses (90 records, 20 partners):** Compassion leads with 7 shared anchors. Mind (Reg 112) has 6 — confirming the cognitive dimension of love (Mat 22:37 includes "with all your mind"). Yielding (Reg 180) has 4 — unexpected; likely the surrender vocabulary overlapping with the love-as-self-giving passages.

### Pass 6 — Session C Section 5 verification

Checking every Section 5 connection against correlation signals:

| Section 5 connection | Signals present | Nature confirmed | Priority confirmed |
|---|---|---|---|
| Compassion (23) | xref(13) + coo(196) + dim(4) + root(RACHAM) + anchor(7) | Formal — all 4 signal types | High ✓ |
| Kindness (99) | xref(33) + coo(34) + dim(6) + anchor(2) | Formal — 3 signal types | High ✓ |
| Mercy (111) | xref(13) + dim(3) + anchor(3) | Formal — 3 signal types | High ✓ |
| Grace (68) | dim(2) | Formal — dimension only | High — revise to Medium |
| Covenant (34) | coo(33) + dim(6) | Formal — 2 signal types | High ✓ |
| Goodness (67) | xref(13) + root(TOV) + anchor(3) | Formal — 3 signal types | High ✓ |
| Desire (43) | xref(20) + coo(49) + root(AGAV) | Formal — 3 signal types | High ✓ |
| Ambition (3) | xref(26) + dim(3) | Formal — 2 signal types | Medium ✓ |
| Delight (42) | xref(23) + coo(33) | Formal — 2 signal types | Medium ✓ |
| Peace (117) | xref(5) + coo(68) + dim(7) + anchor(2) | Formal — all 4 signal types | Medium — revise to High |
| Strength/Might/Authority/Dominion (187/198/197/199) | coo(105/69) + dim(8/7) | Formal — 2 signal types | Medium ✓ |
| Hatred (75) | xref(3) | Formal — xref only | Medium ✓ |
| Heart/Soul/Mind (183/182/112) | coo(47/50/52) + xref(6/0/1) + anchor(0/0/6) | Formal — coo confirmed | Lower ✓ |
| Fellowship (62) | dim(3) | Formal — dimension only | Lower ✓ |
| Forgiveness (64) | dim(4) | Formal — dimension only | Medium — add to table |
| Faithfulness (60) | xref(1) | Formal — weak xref | Lower ✓ |
| Faith (59) | xref(6) + coo(62) + anchor(3) | Formal — 3 signal types | Lower — revise to Medium |

**Corrections to Section 5:**
1. Grace (Reg 68): dimension-only signal — revise from High to Medium
2. Peace (Reg 117): 4 signal types including high co-occurrence — revise from Medium to High
3. Faith (Reg 59): 3 signal types — revise from Lower to Medium
4. Forgiveness (Reg 64): dimension signal confirmed — add to table
5. Yielding/surrender (Reg 156/180): 33/4 co-occurrence/anchor — not in Section 5, add as Medium connection
6. Joy (Reg 97): 35 co-occurrences, 2 shared anchors — not in Section 5, add as Medium
7. Calling (Reg 19): 51 co-occurrences, 3 shared anchors — not in Section 5, add as Medium

**Connections in Section 5 NOT confirmed by any signal:**
None — all 17 connections have at least one signal. Section 5 is clean. Three corrections needed (priority adjustments) and 3 omitted connections to add.

**Additional high-signal partners not in Section 5:**
- Surrender/yielding (Reg 156/180): 33/4 co-occurrence — consistent with the love-as-self-giving theme
- Joy (Reg 97): 35 co-occurrences — love produces joy; joy accompanies love
- Calling (Reg 19): 51 co-occurrences — love is foundational to calling/identity language in Paul

### Pass 6 — New SD Pointers
SD25: C20 cluster (strength, might, authority, dominion) shares all 8 dimensions with love. This is likely a registry-breadth effect, but the co-occurrence is also genuine (105 verses with strength). Session D question: does the biblical vocabulary connect love and power structurally — is love the form that power takes in the kingdom, and power the form that love takes in creation?

SD26: Yielding/surrender (Reg 156) has 33 co-occurrences and 4 shared anchor verses with love. The connection between love as self-giving and surrender as giving up the self may be one of the deepest structural connections in the programme. Session D: is surrender the inner movement that makes love possible?

SD27: Reg 73 (guilt) has 32 co-occurrences with love. Guilt and love co-occurring at this level is unexpected and significant. Session D: Luk 7:47 (she loved much because she was forgiven much) — is guilt the prior inner state that love-as-forgiveness-response resolves?

### SD Pointer count — all passes
Passes 1–6 total: SD1–SD27 = 27 SD pointers raised.


---

## Section 2.2 — SD Pointer Persistence

SD pointer count from observations log (Passes 1-6): 27 new pointers (SD1-SD27, renumbered SD003-SD028 in patch to account for pre-existing SD001-SD002).
Patch produced: PATCH-20260412-103-SDPOINTERS-V1.json (26 insert operations + 1 registry_note)
Pre-existing in database: DIM-103-SD001, DIM-103-SD002 (from prior Dimension Review session)
Expected database total after patch: 28 SD_POINTER records

NOTE per patch_specification v1.10: SDPOINTERS patch type carries session_b_status=null; applicator may reject null for non-exempt types — manual application may be required. Flagged in patch description.

Analytical Brief produced: wa-103-love-sessionB-brief-v1-2026-04-12.md
SD pointer count confirmed in brief: 27 new (observations log count matches patch count).

STATUS: Stage 2 COMPLETE. Awaiting CC confirmation of SD pointer patch before Stage 3 begins.

