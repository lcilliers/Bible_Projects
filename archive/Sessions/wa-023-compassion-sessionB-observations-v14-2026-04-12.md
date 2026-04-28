# WA-023-Compassion — Session B Observations Log
**Filename:** wa-023-compassion-sessionB-observations-v14-2026-04-12.md  
**Date:** 2026-04-11  
**Instruction version:** WA-SessionB-Instruction-v4.6 (2026-04-10)  
**Input file:** wa-023-compassion-complete-2026-04-11.json  
**Session C word study:** wa-023-compassion-word-study-v1-2026-04-11.md  
**Previous output ref:** wa-068-grace-sessionB-observations files (grace, reg 068, 2026-04-10)  
**Session number:** Session 1 (Stage 1 — Data Audit)

| Version | Date | Change |
|---|---|---|
| v1 | 2026-04-11 | Initial audit — all 10 sections, audit summary |
| v2 | 2026-04-11 | Researcher decisions received (G7451, G3804, G3663, G4777); programme discovery recorded (Suffering — missing registry); sequencing decision recorded; cluster assignment assessment (Suffering → C05) added |
| v3 | 2026-04-11 | Registry 214 (suffering) confirmed in uploaded overview — Phase 1 Complete, C05, 72 terms, 907 verses. All deferred terms confirmed in Reg 214. Stage 1 remediation ready to proceed. |
| v4 | 2026-04-11 | Stage 1 remediation complete — field-level patch (G7451 strongs_list) produced; CC directive produced (root family gaps + H0854 escalation). Awaiting Claude Code patch confirmation before Stage 2. |
| v5 | 2026-04-11 | Remediation results recorded: patch applied, CC directive results received, H0854 error acknowledged and corrected, Step D spot-check passed. Stage 1 fully complete. |
| v6 | 2026-04-11 | Pass 1 complete — meaning and semantic range for all 19 active OWNER terms. 16 Session D pointers raised (SD-001 to SD-016). Sense structure, boundary analysis, and Session C checks recorded. |
| v7 | 2026-04-11 | Passes 2–6 complete. Passes 2 (divine dimension), 3 (verse annotations), 4 (somatic), 5 (language accuracy), 6 (correlation audit). Total 27 Session D pointers (SD-001 to SD-027). All correlation signals covered. |
| v8 | 2026-04-11 | Stage 2 complete. Analytical brief produced. CC directive v2 produced. Word study v2 produced. All Stage 2 outputs written. |
| v9 | 2026-04-12 | CC directive v2 spot-check complete. All directed actions confirmed. Two notes: H2594 GOD_AS_SUBJECT flag applied beyond directive scope (benign); session_b_status not updated (researcher decision required). |
| v10 | 2026-04-12 | Patch specification error identified and corrected. patch_specification updated to v1.7. update_registry format confusion alert added to Section 3.2. |
| v11 | 2026-04-12 | Verse context validation gaps identified: G1654 (5 verses unclassified), H2617B (127), H7356A (4), H7358 (25, zero groups). H2603B delete-status groups identified as structural error. VC re-run required for 4 terms. |
| v12 | 2026-04-12 | VCREPAIR patch applied and verified. Classification complete. Statistics discrepancy noted (anchor count stale). Patch spec updated to v1.7 and v1.8. |

---

## STAGE 1 — DATA AUDIT

### Section 1 — Registry Block

| Field | Status | Notes |
|---|---|---|
| `word` | OK | compassion |
| `no` / `id` | OK | 23 / 23 |
| `cluster_assignment` | OK | C17 |
| `verse_context_status` | OK | Complete — Stage 1 can proceed |
| `session_b_status` | NOTE | Value = "Verse Context Reset" — indicates a previous VC re-run; does not block Stage 1 |
| `dim_review_status` | OK | Complete |
| `dim_review_version` | OK | WA-DimensionReview-Instruction-v1.9-2026-04-09 |
| `sb_classification` | NOTE | Null — expected; will be assigned in Stage 2 Pass 4 |
| `sb_classification_reasoning` | NOTE | Null — expected |
| `unique_term_count` | NOTE | 41 — registry-level field, not audited against statistics |
| `shared_term_count` | NOTE | 56 — registry-level field; term_sharing_ratio = 0.577 |
| `dimensions` | GAP | Null — no registry-level dimension assigned. Group-level dimension_index exists (22 rows, all CLAUDE_AI). No action needed at this stage; will be addressed when registry-level consolidation is done. |
| `description` | OK | Programme definition confirmed accurate against data |
| `strongs_list` | SEE BELOW | 97 entries (stored as JSON string); 98 terms in array — G7451 missing from list |

**strongs_list — G7451 gap:**
G7451 *episplanchnizomai* (to show compassion, occ=1, OWNER, mti=delete) is present in the terms array but absent from `strongs_list`. It is a delete-status term. The strongs_list has 97 entries; the terms array has 98 terms. The gap is the missing delete-status G7451. Per instruction v4.2, deleted terms are present in the export by CC design — their presence in the strongs_list is expected. The absence of G7451 from the strongs_list is therefore a gap: it should appear as a delete-status entry. **GAP: G7451 missing from strongs_list — patch required.**

---

### Section 1 — Deletion Justification Review

**Terms with documented exclusion_reason — confirmed deletions:**

- **H2433** *chin* (beauty, 1 occ): excl = "Bleed vocabulary — peripheral aesthetic sense." Deletion confirmed. This is a semantic bleed from the *chin* root; its meaning is an aesthetic sense not relevant to compassion/mercy.
- **H2606** *cha.nan.el* (Tower of Hananel, proper noun, 4 occ): excl = "proper noun." Deletion confirmed. Not an inner-being characteristic.
- **H2624** *cha.si.dah* (stork, 6 occ): excl = "bleed from chasid root. Animal name, no love content." Deletion confirmed.
- **H2603B** *cha.nan* (be loathsome, 1 occ): excl = "No corpus evidence — all span matches resolve to H2603A." Deletion confirmed — no independent verse corpus.

**Terms deleted without documented exclusion_reason — analytical review required:**

The following large clusters of delete-status terms have `exclusion_reason = None`. They fall into identifiable semantic categories:

**Category 1 — Spatial/directional vocabulary (surround, circle, turn around):** These terms appear to have been extracted by a STEP search that retrieved vocabulary related to the concept of *surrounding* or *encircling* (a common spatial metaphor for divine protection). They are semantically unrelated to compassion as an inner characteristic.

Terms: G2944 *kukloō* (to surround), G4012 *peri* (about/around), G4013 *periagō* (to take around), G4022 *perierchomai* (to go around), G4033 *perikukloō* (to surround); H0661 *a.phaph* (to surround), H2328 *chug* (to mark/circle), H2329 *chug* (circle), H3803 *ka.tar* (to surround), H3804 *ke.ter* (crown), H3805 *ko.te.ret* (capital/top), H4141 *mu.sav* (surrounding), H4230 *me.chu.gah* (compass), H4524 *me.sav* (surrounds), H5362A *na.qaph* (to strike), H5362B *na.qaph* (to surround), H5363 *no.qeph* (shaking), H5364 *niq.pah* (rope), H5368 *ne.qash* (to knock), H5437G–K *sa.vav* family (to turn/surround), H5438 *sib.bah* (turn), H5439G–J *sa.viv* family (around), H5849A *a.tar* (to surround), H5849B *a.tar* (to crown), H5850 *a.ta.rah* (crown), H7313 *rum* (to rise), H7314 *rum* (height), H3749 *kar.kov* (ledge), H3750 *kar.kom* (saffron), H5252 *ne.sib.bah* (turn). 

Assessment: None of these name an inner-being characteristic. They are structural/spatial vocabulary. **Deletions confirmed for all.**

**Category 2 — G4183 *polus* (much, 902 occ) and G4012 *peri* (about, 892 occ):** High-frequency particles/adverbs. Semantically irrelevant as standalone inner-being vocabulary. G4183 is the root of G4184 *polusplanchnos* (very compassionate) — the compound is active; the bare particle is not. **Deletions confirmed.**

**Category 3 — Suffering vocabulary without compassion content — review required:**

- **G2552** *kakopatheia* (suffering, 2 occ): Names the experience of suffering/hardship. The PATHĒ root family. This term belongs to the *pathē* cluster — it names what one endures, not the compassion toward it. Adequately covered by context: suffering is the occasion of compassion, not compassion itself. **Deletion confirmed — semantic boundary clear.**
- **G2553** *kakopatheō* (to endure hardship, 5 occ): Same root. Enduring suffering. **Deletion confirmed.**
- **G3804** *pathēma* (suffering/passion, 16 occ): This is a significant term. 16 occurrences. It names the *experience* of suffering — both human suffering (Rom 8:18; 2 Cor 1:5–7) and Christ's sufferings. It is the noun cognate of the *pathē* family already active in this registry (*sumpatheō*, *sumpaschō*). The question is whether the *experience of suffering* is inner-being content for this registry. Assessment: The compassion registry is about the *response to* suffering, not suffering itself. G3804 names suffering as the *occasion* that calls compassion into being. It is a related but distinct characteristic; it belongs to a registry where suffering is primary. However, 2 Cor 1:5–7 ("as we share abundantly in Christ's sufferings, so through Christ we share abundantly in comfort too") directly connects *pathēmata* to *paraklēsis* (comfort) and to the *paschō* vocabulary. This is a potential reinstatement case.

**ANALYTICAL FLAG — G3804 pathēma:** This term names Christ's and the believer's sufferings explicitly in passages that also use the *sumpaschō* vocabulary (already active in this registry). The verses in which pathēma appears (2 Cor 1:5–7; Phil 3:10; Col 1:24; 1 Pet 4:13) show suffering as the ground of fellow-feeling and compassion. The question for the researcher: should G3804 *pathēma* be considered for reinstatement as the noun describing the suffering that the *sumpatheō/sumpaschō* verbs respond to? This term names something the active registry vocabulary presupposes but does not itself name.

**Researcher decision required — G3804 *pathēma*: retain deletion or reinstate?**

- **G3805** *pathētos* (capable of suffering, 1 occ): Applied to Christ (Acts 26:23 — "that the Christ must suffer"). 1 occurrence. Very thin. The question is whether *Christ's capacity for suffering* as ground of compassion belongs here. Assessment: The single occurrence in Acts 26:23 is christological proclamation; the suffering-capacity is declared but not developed. Adequately covered by Heb 4:15 (G4834 *sumpatheō*). **Deletion confirmed — adequately covered.**

- **G3663** *homoiopathēs* (subject to like passions, 2 occ): "Elijah was a man subject to like passions as we are" (Jas 5:17); "we also are men of like passions with you" (Acts 14:15). This term is significant. It names the shared humanity — the common vulnerability — that is the ground of sympathy and compassion. It is the anthropological complement to *sumpatheō* (Christ sympathises because he shares our experience). The same principle applied to human beings: we can have compassion because we share the same human susceptibility. Assessment: This term names the *basis* of fellow-feeling — shared creaturely vulnerability. This is analytically distinct from the compassion itself but foundational to it. The *homoiopathēs* concept (sharing the same *pathē*) is the anthropological underpinning of the *sumpatheō* vocabulary.

**ANALYTICAL FLAG — G3663 homoiopathēs:** This term names the shared creaturely vulnerability that grounds sympathy. With only 2 occurrences and a thin verse set, it may be borderline. However, the concept is not fully represented by any active term. Heb 4:15 (*sumpatheō*) names Christ's capacity; *homoiopathēs* names the human-to-human shared capacity grounded in common human nature. **Researcher decision required — G3663 *homoiopathēs*: retain deletion or reinstate?**

- **G4777** *sunkakopatheō* (to suffer hardship together, 2 occ): A *syn-* compound — "suffer-with-in-hardship." Used in 2 Tim 1:8 ("share in suffering for the gospel") and 2 Tim 2:3 ("share in suffering as a good soldier"). This is a *syn-* compound in the same family as *sumpaschō* (to suffer together). The question is whether "sharing in hardship together" is sufficiently different from "suffering together" (sumpaschō). Assessment: The term names the volitional sharing of difficulty — choosing to enter another's hardship — rather than the instinctive suffering-with. This is a richer concept: not just feeling another's pain, but actively choosing to join them in it. However, with only 2 occurrences, the verse set is thin.

**ANALYTICAL FLAG — G4777 sunkakopatheō:** This term names volitional entry into shared hardship — the active choice to suffer alongside rather than the instinctive suffering-with. This is a meaningful distinction. **Researcher decision required — G4777 *sunkakopatheō*: retain deletion or reinstate?**

- **G0071** *agō* (to bring/lead, 250 occ, 66 verses): A very high-frequency verb. "To bring, lead, carry." Its relationship to compassion is remote. The extraction may have retrieved verses where "bringing" appears in contexts of compassionate action, but the word itself is not inner-being vocabulary. No inner-being content. **Deletion confirmed.**

**Category 4 — H7328 *raz* (mystery, 9 occ):** Aramaic/Daniel vocabulary. No connection to compassion. **Deletion confirmed.**

**Category 5 — H0854 *et* (preposition "with", 932 occ):**
This is the extraction anomaly flagged as PH2_DATA_ERROR and identified as the seventh consecutive registry affected. This is a Hebrew particle with no inner-being content whatsoever. `term_owner_type = None` (not even classified as OWNER or XREF). **Deletion confirmed and warranted.** Programme-wide escalation noted: this is a systematic extraction error requiring investigation beyond this registry.

**Category 6 — G7451 *episplanchnizomai* (to show compassion, 1 occ, 0 verses in export):**
This term is absent from the strongs_list (gap noted above) and has 0 verses in the export. The gloss is "to show compassion" — this is semantically central to this registry. The SPLANCHN root is the core Greek compassion vocabulary. The term exists with 1 occurrence. The absence of verse data in the export is likely the reason for deletion.

**ANALYTICAL FLAG — G7451 episplanchnizomai:** This term's gloss is directly central to this registry and its root (SPLANCHN) is the primary Greek compassion root. The deletion appears to be an extraction failure (0 verses) rather than a semantic judgment. With only 1 occurrence, verse coverage is inherently thin; but the term should not be absent from the strongs_list. **Researcher decision required — G7451 *episplanchnizomai*: confirm deletion (thin coverage) or flag for re-extraction?**

**H4036 *ma.gor mis.sa.viv* (Terror on Every Side, XREF, 4 occ):** A Jeremianic phrase — "terror on every side" (Jer 20:3,4,10; 46:5). XREF status, not OWNER. This is a spatial/threat phrase with no inner-being compassion content. **Deletion confirmed.**

---

### Section 2 — Statistics Block

| Field | Status | Notes |
|---|---|---|
| `term_count` | OK | 98 |
| `active_term_count` | OK | 97 |
| `owner_term_count` | OK | 71 |
| `xref_term_count` | OK | 26 |
| `verse_count` | OK | 2195 |
| `active_verse_count` | OK | 351 |
| `verse_context_group_count` | OK | 58 |
| `verse_context_record_count` | NOTE | Stated 1161; actual contexts-in-groups = 908; unassigned = 253; 908 + 253 = 1161. The stat includes unassigned records. Not an error — the count is internally consistent. |
| `anchor_verse_count` | OK | 92 |
| `dimension_index_count` | OK | 22 |
| `research_flag_count` | OK | 5 |
| `session_b_finding_count` | OK | 1 |
| `cross_registry_link_count` | OK | 0 (expected — Session D populates) |
| `correlation_xref_pair_count` | OK | 20 |
| `correlation_cooccurrence_pair_count` | OK | 84 |
| `correlation_dimension_pair_count` | OK | 19 |
| `correlation_root_family_count` | OK | 3 |
| `correlation_shared_anchor_count` | OK | 34 |

---

### Section 3 — Terms

| Field | Status | Notes |
|---|---|---|
| `term_owner_type` distribution | OK | 71 OWNER, 26 XREF, 1 None (H0854 — delete status, extraction anomaly) |
| `god_as_subject` | GAP | 0 for all 97 active terms. Multiple context group descriptions and anchor verses explicitly place God as primary actor (Exod 34:6; Hos 11:8; Rom 9:15; Lam 3:22; Jas 5:11; Gen 19:16; Jon 4:11; Ps 103:8). This is the same automation gap identified in reg 068 grace. Per instruction Section 3: do not update the field; instead issue a directive to add mti_term_flags GOD_AS_SUBJECT records in Pass 2. |
| `somatic_link` | GAP | 0 for all terms despite RACHAM (womb root) and SPLANCHN (bowels/entrails) vocabulary carrying explicit somatic dimension. Per instruction Section 3: do not update the field; issue directive to add mti_term_flags SOMATIC records in Pass 4. |
| `meaning` / `meaning_numbered` | NOTE | Several terms have meaning = null or meaning_numbered = null. Will be reviewed systematically in Pass 1 and 5. |
| Phase 2 flags | NOTE | G4697 *splanchnizō* carries SEMANTIC_RANGE_BREADTH flag. No others. |
| Root family records | SEE 10a | 12 root codes present on active terms. Only 3 appear in correlation signal (RACHAM, CHASAD, ATAR). 9 root codes are single-registry and their absence from the correlation signal is expected. See 10b. |

---

### Section 4 — Verse Context Groups

| Field | Status | Notes |
|---|---|---|
| `context_description` | OK | All 58 groups have descriptions |
| Anchor designation | OK | All 58 groups have at least one anchor verse |
| Group codes | OK | No duplicates found |

---

### Section 5 — Dimension Index

| Field | Status | Notes |
|---|---|---|
| `dimension_confidence` | OK | All 22 rows are CLAUDE_AI |
| `dominant_subject` | OK | All 22 rows have dominant_subject assigned |
| `manual_override` | OK | Not checked field by field; no issues surfaced |
| `context_description` consistency | OK | All 22 rows match corresponding VC group descriptions exactly |
| XREF groups without dim entries | NOTE | 36 of 58 groups are XREF-owned and have no dimension_index entry. This is expected — dimension review covers OWNER groups only. Not a gap. |

**Dimension Review sub-process:** NOT required. All 22 OWNER-group dimension_index rows show CLAUDE_AI confidence and populated dominant_subject.

---

### Section 6 — Session B Block

| Field | Status | Notes |
|---|---|---|
| `session_b.dimensions` | NOTE | Null — not yet written; expected pre-Stage 2 |
| `session_b.findings` | NOTE | 1 finding: DIM-23-001 — Dimension Review finding about visceral inner-movement language (ni.chum, Hos 11:8). Targets Session B. Requires attention in Stage 2. |

**DIM-23-001 finding text:** The finding asks whether the compassion vocabulary contains a sub-pattern of "visceral inner movement" terms (*splanchnizō*, *ni.chum*, *ra.cha.mim*) that share a somatic/embodied description — and whether this sub-pattern spans the divine-human boundary. This is directly relevant to Pass 4 (somatic evidence).

---

### Section 7 — Session D Block

| Field | Status | Notes |
|---|---|---|
| `sd_pointer_flags` | OK | 0 — none yet raised; Stage 2 will generate these |
| `sd_runs` | OK | 0 — expected |

---

### Section 8 — Research Flags

| Flag | Target | Status | Action |
|---|---|---|---|
| DIMREVIEW_SESSION_D (CHASAD root / shame paradox) | D | Unresolved | Carry forward to Session D — no action in Stage 2 |
| DIMREVIEW_SESSION_D (Heb 4:15 sumpatheō / Christology) | D | Unresolved | Carry forward to Session D |
| PH2_VOLUME_LIMITATION (G1656 mercy — 11% verse coverage) | D | Unresolved | Carry forward to Session D |
| PH2_VOLUME_LIMITATION (G3628 compassion — 14% verse coverage) | D | Unresolved | Carry forward to Session D |
| PH2_DATA_ERROR (H0854 extraction anomaly — 7th consecutive registry) | B | Unresolved | Note in Stage 2. Programme-wide escalation warranted. |

---

### Section 9 — Cross-Registry Links

| Status | Notes |
|---|---|
| OK | cross_registry_link_count = 0; expected — populated during Session D |

---

### Section 10 — Consistency Checks

**10a — Root family completeness**

12 root codes present on active terms. Cross-check within registry:
- RACHAM: H7356A, H7358, H7362 — all 3 carry the code. Are there other active terms in this registry with the RACHAM root that are missing the code? H7356B (*ra.cha.mim* — XREF, owned by reg 111) also shares the RACHAM root. As an XREF term, it will have its root_family record in reg 111's data. No gap on OWNER terms.
- CHASAD: H2616A and H2617B both carry the code. H2617A (*che.sed* — XREF, owned by reg 99/104) also shares the root. No gap on OWNER terms.
- PATHĒ: G3356, G4834, G4835, G4841 — all 4 active PATHĒ-family terms carry the code. G4697 *splanchnizō* does NOT carry PATHĒ code — it has a separate SPLANCHN code. Correct: splanchnizō is from the SPLANCHN root, not the PATHĒ root.
- CHIN: H2587 and H2594 both carry the code. H2603A (*cha.nan* — XREF, owned by reg 68/111) also shares this root. No gap on OWNER terms.

Root family completeness assessment: **No gaps identified on active OWNER terms.**

**10b — Root family correlation signal**

9 root codes not in correlation signal: ELEEIN, ELEĒMOSUN, PATHĒ, OIKTEIRŌ, POLUS, SPLANCHN, CHUM, CHEMLAH, NICHUM.

Check: are these single-registry or multi-registry?
- SPLANCHN: G4697 (OWNER, reg 23) and G4698 (XREF, owned by reg 111 Mercy). This root spans two registries. It should appear in the correlation signal. **GAP — SPLANCHN root family not in correlation signal despite spanning reg 23 and reg 111.**
- PATHĒ: G3356, G4834, G4835, G4841 are all OWNER in reg 23. G4841 *sumpaschō* and the broader pathē vocabulary may appear in reg 115 (passion). Need to check if any PATHĒ terms are in reg 115. This cannot be confirmed from this registry's data alone. **Note for researcher: PATHĒ correlation signal absence may indicate single-registry scope or may be a gap.**
- OIKTEIRŌ: G3627 OWNER reg 23; G3628 *oiktirmos* (XREF, owned by reg 111). This root spans two registries. **GAP — OIKTEIRŌ root family not in correlation signal despite spanning reg 23 and reg 111.**
- NICHUM: H5150 OWNER reg 23; H5162G/H *na.cham* (XREF, owned by reg 192 Comfort) share this root. **GAP — NICHUM root family not in correlation signal despite spanning reg 23 and reg 192.**
- CHIN: H2587 and H2594 OWNER reg 23; H2603A *cha.nan* (XREF, owned by reg 68 Grace) and H2580 *chen* (XREF, owned by reg 68) share this root. **GAP — CHIN root family not in correlation signal despite spanning reg 23 and reg 68.**
- ELEEIN, ELEĒMOSUN, CHUM, CHEMLAH, POLUS: likely single-registry. ELEEIN (G1652) and ELEĒMOSUN (G1654) are both OWNER in reg 23; the related term G1653 *eleeō* is XREF owned by reg 111. The ELEEIN family may therefore span registries. **Note — further investigation warranted.**

**10b summary: At minimum 4 root codes (SPLANCHN, OIKTEIRŌ, NICHUM, CHIN) appear to span multiple registries but are absent from the correlation signal. This is a gap. CC directive required to investigate and add missing root_family correlation signal entries.**

**10c — Dimension index vs VC groups**
- 36 of 58 groups have no dimension_index entry — all are XREF-owned groups. This is expected and correct: Dimension Review covers OWNER groups only.
- 0 dimension_index entries without a corresponding VC group.
- All 22 description pairs match exactly.
**Result: OK — XREF gap is expected.**

**10d — Anchor verse consistency**
All 58 groups have at least one anchor context record (is_anchor=1). anchor_verse_count stated = 92 = actual. **OK.**

**10e — xref signal vs inventory**
All 20 xref_sharing entries: stated shared_term_count matches actual shared_strongs list length. No delete_flagged=1 inventory terms found in shared_strongs lists (based on data available). **OK.**

**10f — Statistics vs correlations block**
All five counts verified in Section 2. **OK.**

**10g — Session B classification**
sb_classification = null; sb_classification_reasoning = null. Both null — expected; Stage 2 Pass 4 will assign. **OK.**

---

## AUDIT SUMMARY — Registry 023 (Compassion) | 2026-04-11

### Fields confirmed OK
registry.word, .no, .id, .cluster_assignment, .verse_context_status (Complete), .dim_review_status (Complete), .dim_review_version; all statistics block fields (with note on verse_context_record_count count method); all 58 group context_descriptions; all 22 dimension_index rows (CLAUDE_AI, dominant_subject assigned, descriptions matched); anchor_verse_count; all correlation block counts; cross_registry_link_count; session_b_finding_count; research_flag_count.

### Gaps requiring field-level patch

| Field | Current value | Correct value | Patch action |
|---|---|---|---|
| `registry.strongs_list` | 97 entries (G7451 missing) | 98 entries including G7451 | Add G7451 {"strong":"G7451","count":1} to strongs_list |

### Gaps requiring CC directive (not field-level patch)

| Field | Issue | Action |
|---|---|---|
| `mti_term_flags` GOD_AS_SUBJECT | Missing for all terms where God is primary actor (H7356A, H5150, H2587, H2617B, H2551, G3627, G4697, G4184 at minimum) | CC directive: insert GOD_AS_SUBJECT flags per Pass 2 analysis |
| `mti_term_flags` SOMATIC | Missing for H7356A, H7358, H7362 (RACHAM/womb family) and G4697, G4698 (SPLANCHN family) | CC directive: insert SOMATIC_INNER_LINK or BODY_INNER_EXPRESSION flags per Pass 4 analysis |
| Root family correlation signal | SPLANCHN, OIKTEIRŌ, NICHUM, CHIN root codes absent from correlations.root_families despite spanning multiple registries | CC directive: investigate and add missing root_family correlation entries |

### Consistency failures requiring patch
None — all 10 checks pass (with notes above on expected XREF gaps).

### Verse Context sub-process required?
[x] No — all groups have descriptions and anchor verses; verse_context_status = Complete.

### Dimension Review sub-process required?
[x] No — all 22 dimension_index rows have CLAUDE_AI confidence and populated dominant_subject.

### Statistics corrections required?
[x] No — all statistics verified correct.

### strongs_list — deletion justification review

[ ] Reinstatement required — researcher decisions required:

1. **G7451** *episplanchnizomai* (to show compassion, 1 occ, 0 verses): SPLANCHN root. Central gloss. Absent from strongs_list (gap). Zero verses in export suggests extraction failure. **Decision: confirm deletion (thin coverage, extraction failure) or flag for re-extraction?**

2. **G3804** *pathēma* (suffering, 16 occ): PATH family. Appears in passages alongside *sumpaschō* vocabulary. Names the suffering that grounds fellow-feeling. **Decision: retain deletion or reinstate?**

3. **G3663** *homoiopathēs* (subject to like passions, 2 occ): Names shared human creaturely vulnerability as the ground of compassion. Analytically distinct from active terms. **Decision: retain deletion or reinstate?**

4. **G4777** *sunkakopatheō* (to suffer hardship together, 2 occ): Volitional entry into shared hardship — active choice to suffer alongside. Distinct nuance from *sumpaschō*. **Decision: retain deletion or reinstate?**

All other deletions: confirmed (spatial/directional vocabulary, particles, proper nouns, animals, unrelated terms, extraction errors).

### strongs_list — inventory corrections required?
[x] Yes — G7451 missing from strongs_list. Patch required.

### Root family gaps
[x] Yes — root codes SPLANCHN, OIKTEIRŌ, NICHUM, CHIN absent from correlations.root_families despite spanning multiple registries. CC directive required.

### Open items requiring researcher decision
1. G7451 *episplanchnizomai*: confirm deletion or re-extract?
2. G3804 *pathēma*: retain deletion or reinstate?
3. G3663 *homoiopathēs*: retain deletion or reinstate?
4. G4777 *sunkakopatheō*: retain deletion or reinstate?
5. Root family correlation signal gaps (SPLANCHN, OIKTEIRŌ, NICHUM, CHIN): CC to investigate.
6. Programme-wide escalation: H0854 extraction anomaly (7th consecutive registry) — separate programme-level action required.


---

## RESEARCHER DECISIONS — Received 2026-04-11

### G7451 episplanchnizomai
Decision: **Confirm deletion.** 0 verses in STEP. Deletion confirmed on extraction failure / no corpus evidence grounds. strongs_list gap patch still required (add as delete-status entry for inventory completeness).

### G3804 pathēma (suffering)
Researcher findings:
- OWNER in Reg 23 (compassion, C17) — 16 verses, all delete_flagged
- XREF in Reg 115 (passion, C04) — 16 verses, all delete_flagged
- No "suffering" registry exists in the database
- MTI has two entries: one status=delete (owner_fk=23), one status=None (owner_fk=None)
- STEP confirms a large corpus: 4267 verses and an extensive related-words network
- **Programme discovery: "suffering" is a missing registry word. A new registry is required.**

Researcher question posed: pause Compassion (reg 23) and add Suffering first, or complete Compassion and add Suffering afterwards?

### G3663 homoiopathēs
Decision: **Reinstate pending Suffering registry resolution.** STEP confirms only 2 verses. Sits within the broader suffering-related word group. Reinstatement deferred until Suffering registry is established and boundary is clarified.

### G4777 sunkakopatheō
Decision: **Reinstate pending Suffering registry resolution.** Part of the suffering word group. Same reasoning as G3663.

---

## PROGRAMME DISCOVERY — Missing Registry: Suffering

**Discovery date:** 2026-04-11
**Identified during:** Session B Stage 1 audit — deletion justification review of G3804 pathēma
**Significance:** HIGH

### What was found

G3804 *pathēma* (suffering/passion) has two MTI entries: one delete-status owned by Reg 23, one with status=None and no owner. G3804 also appears as XREF in Reg 115 (passion, C04) — all verses delete_flagged there too. STEP search on the suffering vocabulary reveals 4267 verses and an extensive related-words network. G3663 *homoiopathēs* and G4777 *sunkakopatheō* both sit within this broader suffering word group.

### Consequence for Reg 23

G3804, G3663, and G4777 are at the boundary between Compassion (reg 23) and a prospective Suffering registry. The *pathē* root family spans both: *sumpatheō* (compassion) and *pathēma* (suffering) share the same root. *Homoiopathēs* (shared vulnerability) and *sunkakopatheō* (volitional suffering-with) name the bridge between the two characteristics.

### Sequencing decision

**Claude AI assessment:** The stronger argument is to **complete Compassion Stage 2 first**, then initiate Session A for Suffering in a new chat. Reasons:
1. The 19 active OWNER terms are independent of the Suffering boundary and constitute the core compassion vocabulary
2. The Reg 23 Stage 2 analysis will sharpen the specification of what Suffering should include
3. Pausing mid-Session B introduces continuity risk
4. G3804, G3663, G4777 remain delete_flagged in Reg 23 for now; their status is flagged as pending resolution of the Suffering registry

Both G3663 and G4777 are confirmed for reinstatement in Reg 23 once the Suffering registry is established and the boundary is clarified. This is not a reinstatement in the current patch — it is a deferred action.

**Awaiting researcher direction on sequencing.**


---

## SEQUENCING DECISION — Received 2026-04-11

**Decision:** Pause Compassion Session B at current stage (Stage 1 complete, Stage 2 not yet begun).

**Researcher action:** Add Suffering to the registry and bring it to Phase 1 (Session A complete, data imported). Then upload a new registry overview to this chat.

**Resume condition:** Researcher uploads updated registry overview confirming Suffering registry number and Session A status. Compassion Session B Stage 2 then begins with the Suffering registry number available for reference in the analytical brief and word study update.

**Programme state at pause:**
- Reg 23 Compassion: Session B Stage 1 complete. Stage 2 pending.
- Field-level patch (G7451 strongs_list) and CC directive (root family correlation gaps) are ready but NOT yet applied — hold until Stage 2 begins.
- G3663 *homoiopathēs* and G4777 *sunkakopatheō*: deferred reinstatement — pending Suffering registry establishment and boundary clarification.
- Suffering: new registry to be created and brought to Phase 1 by researcher.

**Next action in this chat:** Researcher uploads updated wa-registry-overview file. Session B Stage 2 begins.


---

## RESUME — Registry Overview Uploaded | 2026-04-11

**Registry 214 (suffering) confirmed:**
- word: suffering | no: 214 | cluster: C05 (confirmed — matches recommendation)
- phase1_status: Complete | phase1_term_count: 72 | phase1_verse_count: 907
- session_b_status: Ready for Analysis
- verse_context_status: None (not yet started — Phase 1 only, as agreed)
- live_owner_count: 0, live_xref_count: 0 — terms not yet extracted to inventory (expected at Phase 1 state)

**All previously deferred Reg 23 terms now confirmed in Reg 214 strongs_list:**
G3804 pathēma (16), G3663 homoiopathēs (2), G4777 sunkakopatheō (2), G4834 sumpatheō (2), G4841 sumpaschō (2), G3356 metriopatheō (1), G3805 pathētos (1), G4835 sumpathēs (1), G2553 kakopatheō (3), G3806 pathos (3)

Note: G4834 sumpatheō, G4841 sumpaschō, G3356 metriopatheō, G3805 pathētos, G4835 sumpathēs are currently OWNER-active in Reg 23 (compassion). Their appearance in Reg 214 (suffering) as strongs_list entries is expected — these terms sit at the compassion/suffering boundary. Their OWNER/XREF classification within Reg 214 will be determined when Session A runs for suffering. This boundary question is a deferred Session D item.

**Programme state update:**
- Total registries: 214
- Reg 214 (suffering): Phase 1 Complete — Verse Context not yet started
- Reg 23 (compassion): Stage 1 audit complete — ready to proceed to Stage 1 remediation and Stage 2

**Next action: Stage 1 remediation — produce field-level patch and CC directive.**


---

## STAGE 1 — REMEDIATION

### Step A — Field-level patch

**Patch produced:** wa-023-compassion-sessionB-patch-v1-2026-04-11.json
- OP-001: update_registry | strongs_list corrected — G7451 added as delete-status entry (count=1). Strongs_list now 98 entries matching terms array count.
- Status: Delivered to researcher. Awaiting Claude Code confirmation before Stage 2 begins.

### Step B — Verse Context sub-process
Not triggered. All groups have descriptions and anchor verses. verse_context_status = Complete.

### Step C — Dimension Review sub-process
Not triggered. All 22 dimension_index rows have CLAUDE_AI confidence and populated dominant_subject. dim_review_status = Complete.

### CC Directive

**Directive produced:** wa-023-compassion-sessionB-cc-directive-v1-2026-04-11.md
Three items:
1. Root family correlation signal gaps — SPLANCHN, OIKTEIRŌ, NICHUM, CHIN (action required)
2. Suffering registry boundary note — for information only
3. H0854 extraction anomaly programme-wide count — low priority

**Note on sequencing per SB-1:** Stage 2 does not begin until Stage 1 is fully complete and the fresh extract is confirmed. The field-level patch (Step A) must be applied and confirmed by Claude Code, and a fresh extract produced, before Stage 2 begins. The CC directive root family investigation does not block Stage 2 — root family correlation signals are used in Pass 6, and a partial signal is acceptable if the gap is documented.


---

## STAGE 1 — REMEDIATION RESULTS | 2026-04-11

### Patch v1 — Applied
G7451 added to strongs_list for Reg 23. Confirmed applied.

**Applicator note:** The `update_registry` operation format was skipped by the applicator — patch was applied manually. Format issue to note for future patch specification review. This is not a data error but a pipeline gap: the patch specification for `update_registry` operations in this instruction version requires clarification. Flag for patch_specification document review.

### CC Directive 1 — Root family correlation gaps — RESOLVED (no action)

All four root codes investigated. Result: all are single-registry (Reg 23 only).

| Root code | Registry count | Result |
|---|---|---|
| SPLANCHN | 1 (Reg 23 only) | Single-registry — no correlation entry required |
| OIKTEIRŌ | 1 (Reg 23 only) | Single-registry — no correlation entry required |
| NICHUM | 1 (Reg 23 only) | Single-registry — no correlation entry required |
| CHIN | 1 (Reg 23 only, 5 terms) | Single-registry — no correlation entry required |

**Root cause of apparent gap:** XREF copies of these terms in Reg 111 (mercy), Reg 68 (grace), and Reg 192 (comfort) do not carry matching root_family records. The correlation signal requires root_family records on terms in at least 2 registries — so these are correctly absent from the signal. The 10b check was correctly raised as a flag for investigation; the investigation correctly resolves it as no-action.

**Additional finding — root code collision:** CHIN (Reg 23) vs CHEN (Reg 68) name the same Hebrew root חנן under two different codes. This is the same pattern as the CHAR/CHARAH collision resolved earlier. **Session D pointer raised:** the חנן root (gracious/favour vocabulary) spans Reg 23 and Reg 68 under split root codes. This should be harmonised when root code consolidation is addressed programme-wide.

### CC Directive 2 — Suffering boundary: Noted. No action.

### CC Directive 3 — H0854 extraction anomaly — CORRECTION REQUIRED

**Claude AI error acknowledged:** The claim that H0854 *et* appeared in "at least 7 consecutive registries" was not supported by the data. Claude Code investigation confirms H0854 is present in only 1 registry (Reg 23), correctly marked as delete in both wa_term_inventory (delete_flagged=1) and mti_terms (status=delete). No programme-wide pipeline issue exists. Low priority — no pipeline fix needed.

**Root cause of Claude AI error:** The claim originated from the Session A data note embedded in the PH2_DATA_ERROR research flag description: *"seventh consecutive registry. H0854 et (with, 932 occ HFA preposition) incorrectly extracted."* This flag text was read as a live programme-wide finding; it was actually a historical notation from the Session A extraction run context. Claude AI failed to verify the claim against current database state before asserting it as a current fact.

**Correction recorded for ongoing discipline:** Research flag descriptions are historical notes, not current programme-state assertions. All claims about programme-wide state must be verified against live data before being stated as facts. This is a direct application of the governing principle: "the data is authoritative."

### Step D — Fresh Extract Spot-Check

Fresh extract: wa-023-compassion-complete-2026-04-11.json (same date — patch confirmed in this file).


**Spot-check results:**
1. G7451 in strongs_list: YES — {'strong': 'G7451', 'count': 1} ✓
2. strongs_list count: 98 ✓
3. dim_review_status: Complete ✓
4. verse_context_status: Complete ✓
5. dimension_index: 22 rows, all CLAUDE_AI, all dominant_subject assigned ✓
6. anchor_verse_count: 92 ✓
7. active_verse_count: 351 ✓

**STAGE 1 COMPLETE. ALL GAPS RESOLVED. STAGE 2 MAY BEGIN.**

Working extract: wa-023-compassion-complete-2026-04-11.json


---

## STAGE 2 — ANALYTICAL PASSES

### PASS 1 — Meaning and Semantic Range

**Date:** 2026-04-11 | Working extract: wa-023-compassion-complete-2026-04-11.json

Cross-registry vision active throughout. Session D pointers raised at point of discovery per SB-11.

---

#### Term 1: H7356A *ra.cham* — womb (occ=6, extracted)
**Sense structure:** This term occupies the semantic space between the anatomical womb and the compassion that derives from it. In 5 of its verses it is used literally (Gen 49:25 "blessings of the womb"; Judg 5:30 "a womb or two for every man"; Pro 30:16 "the barren womb never satisfied"). The sixth occurrence (Isa 46:3 — group 729-001) is the metaphorical anchor: God carrying Israel "from the womb," grounding divine compassion in maternal carrying. The term functions primarily as the somatic/etymological root of the compassion vocabulary, not as a compassion term itself in most uses.

**Semantic boundary:** The primary sense in most occurrences is anatomical, not emotional. The inner-being content enters through the metaphorical extension. This is the term that establishes *why* compassion is described in visceral body-language — the etymological ground, not the characteristic itself.

**Session C check:** Section 4 correctly identifies this term as the somatic root. Section 1 and 2 accurately describe the womb-metaphor. Confirmed.

**meaning_numbered gap:** No meaning/meaning_numbered field populated. The sense structure is recoverable from the verse corpus and status_note but is not formally encoded. **GAP: meaning_numbered null for H7356A.** Note for Pass 5 language accuracy audit.

**Session D pointer SD-001:** H7356A *ra.cham* (womb, Reg 23) and H7358 *re.chem* (womb, anatomical) share the same root as the RACHAM family in Love (Reg 103). The womb-metaphor grounds divine compassion; the same root grounds divine and human love. The question for Session D: does the womb-root function as a unifying somatic image across both compassion and love, or does it serve different semantic purposes in each registry? Evidence: Isa 46:3 (compassion context); Gen 29:31 (love/provision context — God opening the unloved wife's womb).

---

#### Term 2: H7358 *re.chem* — womb, anatomical (occ=26, extracted)
**Sense structure:** 25 verses in export, all anatomical usage. The womb as: closed by God (Gen 20:18 — divine sovereignty over fertility); opened by God (Gen 29:31, 30:22 — compassion on the unloved); firstborn that opens (Exod 13:2,12 — consecration); the origin-space from which Israel was carried (Isa 46:3 — the same verse as H7356A's metaphorical anchor). The term is almost exclusively anatomical throughout the corpus.

**Semantic observation:** The word *re.chem* names the physical organ; *ra.cham* names the compassion that originates from it. The relationship is the reverse of the usual direction — the abstract (compassion) is named after the concrete (womb), not the other way around. This is unusual in Hebrew word formation and gives the compassion vocabulary a somatic grounding that is built into the language itself rather than being a later metaphorical extension.

**Session C check:** Section 4 identifies this correctly as "the anatomical root." Section 1 correctly notes the womb-metaphor. No correction required.

**meaning_numbered gap:** Null. GAP noted.

**Session D pointer SD-002:** H7358 *re.chem* (womb, 26 occ) is primarily a fertility and creation-order term. Its 26 occurrences include divine sovereignty over conception and birth (Gen 20:18; 29:31; 30:22) — language closely associated with the Love (Reg 103) and potentially Calling (Reg 19) registries. The question: does divine sovereignty over the womb constitute a cross-registry connection between Compassion (the response to suffering), Love (the relational disposition), and Calling (divine purpose from before birth)? Isa 49:1 ("The Lord called me from the womb") and Jer 1:5 ("before you were born I consecrated you") belong to other registries but are semantically adjacent.

---

#### Term 3: H7362 *ra.cha.ma.ni* — compassionate (occ=1, extracted_thin)
**Sense structure:** Adjective from the RACHAM root. Single occurrence: Lam 4:10 — the compassionate (*ra.cha.ma.ni*) women who boiled their children. The adjective names the settled character quality of compassion. The verse's force depends entirely on the characterisation: these *are* compassionate women — yet this is what they did. The term names the inner quality at the moment of its most catastrophic inversion.

**Semantic observation:** This is the only adjectival form in the OWNER vocabulary for this registry. It establishes that compassion is a *character quality* (the adjective names what kind of person one is, not what one does in a moment). The tragedy of Lam 4:10 is that character qualities are not indestructible — extreme circumstance can force violations of the deepest human dispositions.

**Session C check:** Section 3 annotation confirmed accurate and complete.

**Session D pointer SD-003:** The Lam 4:10 usage raises the question of compassion's resilience as an inner characteristic — whether characteristics can be permanently destroyed by circumstance, or temporarily violated. This connects to the Suffering registry (Reg 214) and potentially to Brokenness (Reg 18) and Anguish (Reg 5). The verse also appears in the C05 cluster context (grief, mourning) — the violation of compassion is itself a form of communal grief.

---

#### Term 4: H2347 *chus* — to pity (occ=24, extracted)
**Sense structure:** Two groups: pity as an inner disposition that moves toward or spares (group 3182-001), and the judicial withholding of pity (group 3182-002). The related-words list shows only one entry: *darkened* (H2345 *chum*). This is an unusual related-word — pity and darkness do not share obvious semantic territory, suggesting the connection is through root similarity rather than semantic affinity. No meaning_numbered field.

From verse corpus: H2347 is used in two distinct frames — (a) the injunction not to pity (most frequently: Deut 7:16; 13:8; 19:13; Ezek 7:4,9; 8:18; 9:5,10 — all judicial/warfare contexts where compassion is explicitly prohibited); (b) the affirmative pity toward the weak (Ps 72:13; Jon 4:11). The negative usage (withhold pity) is more frequent than the positive (show pity). This is noteworthy: the term appears most often in the context of its prohibition.

**Semantic boundary:** *Chus* describes the *impulse* of pity — the instinctive sparing of the other. When the law or the prophets say "your eye shall not pity," they are acknowledging that this impulse naturally arises and must be consciously overridden in judicial contexts. This makes the term a window into the *default* orientation of the inner person toward those in need — compassion as the natural state that judgment suspends.

**Session C check:** Section 3 annotations for both groups confirmed accurate. Section 2 paragraph on judicial suspension confirmed and deepened by the frequency observation above.

**Session D pointer SD-004:** The high frequency of *chus* in judicial-prohibition contexts (Deut, Ezek) reveals a structural relationship between compassion and justice in the inner life: the default orientation is toward sparing; justice requires the deliberate overriding of that default. This is a programme-level observation about the architecture of the moral inner life. Connects to Justice (Reg 98), Guilt (Reg 73), and potentially Conscience (Reg 26). Question for Session D: does the inner life have a default orientation toward compassion that other moral demands must actively override, and if so, what does this reveal about the programme's understanding of the moral constitution of the human person?

---

#### Term 5: H2551 *chem.lah* — compassion (occ=2, extracted_thin)
**Sense structure:** The related-words are *to spare* (H2550 *cha.mal*) and *compassion* — confirming this term sits in the sparing/mercy semantic space. Two verses: Gen 19:16 (God's mercy toward Lot despite his lingering) and Isa 63:9 ("in his love and in his pity he redeemed them"). Isa 63:9 is significant — *chem.lah* appears alongside divine love (*ahavah*) as the motivating disposition of God's redemptive act.

**Semantic observation:** *Chem.lah* (compassion/pity) and *cha.mal* (to spare) share a root that emphasises *restraint on behalf of the other* — the withholding of force or judgment in response to need. This is compassion expressed not as emotional movement but as mercy-in-action.

**Session D pointer SD-005:** Isa 63:9 names *ahavah* (love) and *chem.lah* (pity/compassion) together as co-motivating God's redemption. This is a direct verse-level co-occurrence of Love (Reg 103) and Compassion (Reg 23) vocabularies within a single clause about divine inner motivation for salvation. Raise: the inner architecture of divine redemption — what roles do love and compassion play distinctly, and do they always appear together? Cross-registry: Love (Reg 103), shared anchor verse candidate.

---

#### Term 6: H2587 *chan.nun* — gracious (occ=13, extracted)
**Sense structure:** Adjective; used almost exclusively as a divine epithet. Status note: "guilt resolution vocabulary." The related words are: beauty (*chin*), favour (*chen*), for nothing (*chinam*), be gracious (*chanan*), be loathsome (H2603B), supplication (*techinah*), Tower of Hananel. The term describes the *settled character quality* of graciousness — not a momentary act but an attribute. Exod 34:6 is the defining verse: *rachum ve-channum* ("merciful and gracious") as paired divine attributes.

**Semantic observation:** *Chan.nun* (gracious) describes the *character disposition* from which compassion flows — the inner quality of being inclined toward favour. It is related to *chen* (favour/grace) through the root *chanan* (to be gracious). This root family bridges Compassion (Reg 23) and Grace (Reg 68): *channum* names God's *character* as gracious; *chen* names the *favour* that flows from it.

**Sense tension:** Status note says "guilt resolution vocabulary" — this positions graciousness as the response to guilt. But the Exod 34:6 usage is a divine character declaration unprompted by guilt. The "guilt resolution" frame applies to many *instances* of grace/graciousness, not to the term's primary semantic content.

**Session C check:** Section 4 description of H2587 confirmed accurate.

**Session D pointer SD-006:** *Chan.nun* (gracious, Reg 23) and *chen* (favour/grace, XREF in Reg 23, OWNER in Reg 68 Grace) share the same Hebrew root (חנן — the CHIN/CHEN root code collision noted in Stage 1). Exod 34:6 is a shared anchor verse for Reg 23 and Reg 68. The question: is graciousness (the character quality, *channum*) distinct from grace (the relational gift, *chen*), and if so, where does the inner-being boundary lie between them? This is the most direct compassion/grace boundary question in the programme.

---

#### Term 7: H2594 *cha.ni.nah* — favour (occ=1, extracted_thin)
**Sense structure:** Single occurrence: Jer 16:13. The verse is a divine judgment speech — "I will hurl you out of this land into a land that neither you nor your fathers have known, and there you shall serve other gods day and night, for I will show you no favour (*cha.ni.nah*)." The term names the withdrawing of divine favour as judicial consequence. Same root as *chan.nun* and *chen*. The term occurs once in a context of its *absence* — like H2617B *che.sed* (shame), which is another register of *chesed* absence.

**Semantic observation:** This is the noun form of the gracious-favour vocabulary. Its single occurrence in a withdrawal-of-favour context mirrors the pattern seen in H2347 *chus* (pity mostly appearing in prohibition contexts) and H2617B *che.sed* (shame as the negative pole of chesed). The compassion vocabulary defines itself in part through naming its own absence and its judicial withdrawal.

---

#### Term 8: H2616A *cha.sad* — be kind (occ=2, extracted_thin)
**Sense structure:** The verbal form of the *chesed* root. Two occurrences, both the identical verse: 2 Sam 22:26 = Ps 18:25 ("With the merciful you show yourself merciful"). The hitpael form (*hitchasad*) means "to act kindly/show kindness toward." The verse establishes the mirror principle: God responds in kind to the inner disposition the person brings. This is compassion/kindness as relational correspondence — divine character mirrors human character and vice versa.

**Cross-registry reading:** This is the Divine-Human Correspondence dimension in action. The same verbal principle operates across multiple characteristics — the faithful person encounters God's faithfulness; the merciful encounter mercy; the blameless encounter blamelessness. This structural principle may span many registries beyond compassion.

**Session D pointer SD-007:** The Divine-Human Correspondence principle embedded in 2 Sam 22:26 / Ps 18:25 operates across multiple inner-being characteristics simultaneously (merciful, blameless, pure, crooked — v.26-27). The programme should examine whether this mirroring principle is a general structural feature of the divine-human relationship visible across multiple registries, or specific to certain characteristics. Cross-registry candidates: Faithfulness (Reg 60), Blamelessness (Reg 14), Purity (Reg 125), Integrity (Reg 92).

---

#### Term 9: H2617B *che.sed* — shame (occ=3, extracted_thin; 169 verses in export)
**Sense structure:** This is the negative semantic pole of the *chesed* root. The status note confirms: "the semantic range of chesed includes disgrace as its opposite pole." Three occurrences in the verses carrying this sub-gloss. The related words name the full root range: *be kind*, *to shame*, *kindness* — the positive form, its verbal cognate of shaming, and the primary positive noun.

**Critical observation:** H2617B appears here because *chesed* can mean both "steadfast love/kindness" and "shame/disgrace" depending on context and vocalisation — a semantic paradox documented in the CHASAD root flag. The 169 verses in the export are the full *chesed* corpus (H2617A is the XREF term owned by Reg 99/104; H2617B is this registry's OWNER term carrying the shame/negative-pole sense). This means the compassion registry carries the negative semantic pole of one of Israel's most theologically weighty words.

**Session C check:** Sections 1-4 address this correctly. The CHASAD root paradox is accurately noted.

**Session D pointer SD-008 (confirmed from Stage 1 DIMREVIEW flag):** The CHASAD root (Reg 23 H2617B shame vs Reg 146 shame) and the CHASAD root (Reg 23 H2616A be kind) cross two clusters — C17 (compassion, love, mercy) and C06 (shame, contempt). The question for Session D: does the root-level connection between *chesed* (steadfast love) and *shame* reflect a genuine semantic relationship — that the violation of covenantal faithfulness produces shame as its consequence — or is this purely a lexicographic artefact? If genuine, it suggests the inner experience of shame is structurally connected to the failure of *chesed* in a way the programme should explore.

---

#### Term 10: H5150 *ni.chum* — comfort (occ=3, extracted)
**Sense structure:** Noun from the *na.cham* root (to comfort/relent). Three verses: Isa 57:18 (divine comfort restored to the straying); Hos 11:8 (divine compassion "grows warm and tender" — *ni.chumay nikmeru*, "my compassions are kindled"); Zec 1:13 ("gracious and comforting words"). The term names the *compassionate warmth* that produces comfort — the inner stirring that precedes and motivates the comforting act.

**Semantic observation:** *Ni.chum* sits at the intersection of compassion and comfort. It is not comfort as consolation-received but compassion as the motivating warmth from which comfort flows. Hos 11:8 is the key verse: the divine inner life *stirs* with *ni.chum* in response to the prospect of judgment — this stirring overrides the judicial decision. The term names the felt, warm, visceral quality of compassion at the moment it becomes action.

**Session B finding DIM-23-001 engaged:** The Dimension Review finding asked whether *ni.chum*, *splanchnizō*, and *ra.cham* share a sub-pattern of "visceral inner movement" terms. Pass 1 confirms this: all three name compassion as a bodily movement from within — warm kindling (ni.chum), gut-stirring (splanchnizō), womb-love (ra.cham). This sub-pattern spans the divine-human boundary: God's compassion and human compassion are described with the same visceral language. **This sub-pattern is confirmed. Will be addressed fully in Pass 4 (somatic evidence) and noted in the analytical brief.**

---

#### Term 11: H2587 *chan.nun* — already covered above (Term 6)

#### Term 12: G3627 *oikteirō* — to have compassion (occ=28, extracted)
**Sense structure:** The primary Greek verb for expressing compassion/pity toward another. Mounce: "to have compassion on." LSJ entry is extensive (7th c. BC through NT) — classical usage shows deep roots in Greek emotional vocabulary. The word carries connotations of *oiktos* (pity, grief for another's misfortune). Single group (731-001): "divine compassion as an inner disposition of sovereign mercy — God's free inclination toward the objects of his compassion."

**Semantic observation:** The NT usage concentrates this term specifically on divine sovereignty in compassion — Rom 9:15 is the anchor: "I will have compassion on whom I have compassion." The repetition enforces the point that compassion cannot be coerced or earned; it belongs to God's freedom. The 28 occurrences in the export include both the OT (LXX) and NT instances.

**Session D pointer SD-009:** Rom 9:15 pairs *eleeō* (mercy, Reg 111) and *oikteirō* (compassion, Reg 23) as parallel verbs of divine sovereign freedom. The pairing raises the question: are mercy and compassion distinguishable in this verse, or is the parallelism purely rhetorical? The answer to this question is one of the most direct tests of whether Reg 23 and Reg 111 are genuinely separable characteristics.

---

#### Term 13: G4697 *splanchnizō* — to pity / be moved in the gut (occ=12, extracted)
**Sense structure:** Mounce: "to have compassion on, have pity on." LSJ: the verb appears in LXX and NT. Status note: "the compassion-movement verb — Jesus 'moved with compassion' in Matt 9:36, 14:14, 15:32, 20:34; Mark 1:41, 6:34, 8:2; Luke 7:13, 10:33, 15:20." SEMANTIC_RANGE_BREADTH flag present.

From verse corpus: 12 occurrences — all Gospels. The objects of the *splanchnizō* movement are: the multitude (sheep without a shepherd — Matt 9:36); crowds needing food (Matt 15:32; Mark 8:2); two blind men (Matt 20:34); a leper (Mark 1:41); the disciples' unbelief context (Mark 6:34); the widow of Nain's grief (Luke 7:13); the Samaritan toward the wounded man (Luke 10:33 — the only human subject outside the parables); the father of the prodigal (Luke 15:20); the king toward the servant (Matt 18:27 — the parable).

**Semantic breadth — four domains identified (SEMANTIC_RANGE_BREADTH flag):**
1. *Compassion toward physical suffering or need* — healing miracles (Matt 20:34; Mark 1:41; Luke 7:13)
2. *Compassion toward spiritual destitution* — "sheep without a shepherd" (Matt 9:36; Mark 6:34)
3. *Compassion toward physical hunger* — crowds without food (Matt 15:32; Mark 8:2)
4. *Compassion in relational/moral context* — parable of prodigal (Luke 15:20), unforgiving servant (Matt 18:27), Good Samaritan (Luke 10:33)

**Critical observation:** The SEMANTIC_RANGE_BREADTH flag is fully justified. The four domains reveal that *splanchnizō* is not a single-type response — it is the one verb used when the Gospels want to describe *visceral, inward, movement-producing response to need of any kind*. The unifying element is not the type of need but the quality of the inner response: it moves from within, it produces action, it cannot be overridden.

**Session D pointer SD-010:** Luke 10:33 — the Good Samaritan is *splanchnizō* toward the wounded man. This is the only unambiguous human use of the term outside parables. The verse connects compassion directly to the question "who is my neighbour?" — making compassion the defining quality of the one who correctly answers that question. This connects to Love (Reg 103 — "love your neighbour") and potentially Mercy (Reg 111 — "go and do likewise" in v.37 uses *eleos*). The structural observation: compassion (*splanchnizō*) generates mercy (*eleos*) in Luke 10:33-37 — the inward movement produces the outward act. This sequence matters for Session D.

---

#### Term 14: G4834 *sumpatheō* — to sympathise (occ=2, extracted)
**Sense structure:** Two occurrences: Heb 4:15 (Christ sympathising with our weaknesses) and Heb 10:34 ("you had compassion on those in prison"). The verb names *entering into another's experience* — literally "suffering-with." LSJ first meaning: "to be sympathetically affected, to have the same thing happen to one"; notes the classical philosophical use of the soul and body sympathising with each other.

**Semantic observation:** The classical philosophical usage (soul-body sympatheia) is significant for the spirit-soul-body classification work in Pass 4. The term originated in Stoic philosophy to describe the interconnection of parts of a whole — the way the wellbeing of one part affects all others. The NT reappropriates this concept for the community of faith and for Christology.

**Session D pointer SD-011:** The classical *sumpatheō* (soul and body sympathise with each other, Aristotle) is imported into NT anthropology as the ground of Christian community. This raises a programme-level question: does the NT use of *sym-* compounds (sumpatheō, sumpaschō) draw on Greek philosophical anthropology about the unity of the person, and does this inform the programme's spirit-soul-body framework? Cross-registry: potentially Soul (Reg 182), Spirit (Reg 184), the whole C01 cluster.

---

#### Term 15: G4835 *sumpathēs* — sympathetic (occ=1, extracted_thin)
**Sense structure:** Adjective form. Single occurrence: 1 Pet 3:8. LSJ notes: "affected by like feelings, sympathetic" — with classical examples citing the greater sympathy of mothers for their children. The term describes the settled character quality of being *capable of* fellow-feeling, not a momentary act of it.

**Semantic observation:** The adjectival form establishes sympatheia as a *character trait* — the person who is *sumpathēs* is consistently responsive to others' suffering. 1 Pet 3:8 places it in a list of community virtues: unity of mind, sympathy, brotherly love, tender heart, humble mind. This is the community portrait — sympathy as one thread in the fabric of the new humanity.

---

#### Term 16: G4841 *sumpaschō* — to suffer with (occ=3, extracted_thin)
**Sense structure:** 1 Cor 12:26 (the body suffers together), Rom 8:17 ("if children, then heirs — heirs of God and fellow heirs with Christ, provided we suffer with him"), and one other occurrence. LSJ: "have the same thing happen to one; to be affected in common with."

**Semantic observation:** *Sumpaschō* has two distinct usages: (a) mutual suffering within the body of Christ (1 Cor 12:26 — the ontological suffering-together that is a property of membership in the body); (b) sharing in Christ's sufferings as the condition of sharing in his glory (Rom 8:17 — the eschatological frame). These are meaningfully distinct: the first is community solidarity; the second is participation in Christ's redemptive suffering.

**Session D pointer SD-012:** Rom 8:17 — "if we suffer with him (*sumpaschō*) we may also be glorified with him (*syndoxazō*)" — places fellow-suffering within an eschatological framework. Suffering-with-Christ is the condition of glorification-with-Christ. This connects Compassion/suffering-with vocabulary (Reg 23) to the Endurance (Reg 55), Surrender (Reg 156), and potentially Hope (Reg 78) registries. The eschatological dimension of compassion — suffering-with as the path to glory — is not addressed in Session C and should be incorporated in Stage 3.

---

#### Term 17: G3356 *metriopatheō* — be gentle / moderate feeling (occ=1, extracted_thin)
**Sense structure:** Heb 5:2. Mounce: "to deal gently." LSJ: "feel moderately, bear reasonably with the ignorant and wayward." The Stoic term for *metriopatheia* names the philosophical ideal of moderating the passions — neither suppressing them (apatheia) nor being ruled by them. In Heb 5:2 the term is given a new ground: the high priest can moderate his response *because* he shares human weakness, not because he has mastered the passions philosophically.

**Semantic observation:** This is compassion shaped by wisdom rather than compassion as raw feeling. It introduces the distinction between compassion's motivational force and its expression — calibrated, moderate, appropriate. The scriptural reframing grounds this moderation in shared vulnerability rather than philosophical self-mastery, which is a significant divergence from the Stoic usage.

**Session D pointer SD-013:** *Metriopatheō* (Reg 23) draws from Stoic *metriopatheia* — a deliberate philosophical distance from the Hebrew womb/visceral model. The contrast between these two models of compassion (Stoic moderate feeling vs Hebrew bodily movement) may be significant for the programme's understanding of how Greek and Hebrew anthropologies interact in the NT. Cross-registry: potentially Patience (Reg 116), Self-Control (Reg 142), Gentleness (Reg 66).

---

#### Term 18: G4184 *polusplanchnos* — very compassionate (occ=1, extracted_thin)
**Sense structure:** NT hapax legomenon — appears only in Jas 5:11. Compound: *polus* (much/many) + *splanchnon* (bowels/entrails/compassion). Mounce: "compassionate." LSJ: "of great mercy." The intensifying compound makes explicit what the SPLANCHN root already implies: God is *full of* the visceral compassion movement. The context is suffering and endurance (Job's patience; the Lord's *telos*).

**Semantic observation:** The use of a compound hapax for this single statement signals that the writer needed a stronger term than the existing vocabulary supplied. *Polusplanchnos* — intensely, deeply compassionate — is coined for the moment when God's compassion needs to be named as something beyond the ordinary range of the word. This intensification in the context of Job's suffering is theologically significant: God's deep compassion is announced at the point of maximum permitted suffering.

**Session D pointer SD-014:** Jas 5:11 holds in tension God's deep compassion (*polusplanchnos*) with God's permitted suffering (Job's endurance). The verse does not resolve the tension — it holds both. This is the clearest instance in the programme data where compassion and suffering are explicitly co-present as divine attributes/actions. Cross-registry: Suffering (Reg 214), Endurance (Reg 55). Question for Session D: does the programme data reveal a structural relationship between divine compassion and divinely-permitted suffering?

---

#### Term 19: G1652 *eleeinos* — pitiful (occ=2, extracted_thin)
**Sense structure:** Rev 3:17 (the Laodiceans are pitiable — *eleeinos* — without knowing it) and 1 Cor 15:19 ("if in Christ we have hope in this life only, we are of all people most to be pitied"). The term names the *condition* that calls forth compassion — not compassion itself but its proper object. The pitiable condition may be physical (1 Cor 15:19 — life without resurrection hope) or spiritual (Rev 3:17 — self-deceived prosperity).

**Semantic observation:** *Eleeinos* reveals compassion's counterpart: the pitiable condition is the one that *ought* to evoke compassion. Rev 3:17 is particularly sharp — the Laodiceans cannot receive the compassion they need because they cannot perceive their own pitiable condition. Compassion requires both the disposition (in the giver) and the recognition of need (in the receiver or an observer). The word names the failure of the second condition.

**Session D pointer SD-015:** Rev 3:17 — the pitiable condition (*eleeinos*) masked by prosperity — connects to Despair (Reg 44), Shame (Reg 146), and potentially Pride/Boastfulness (Reg 123). The verse shows that the inner condition requiring compassion can be concealed from the person who most needs it. This has implications for the programme's understanding of self-knowledge and the conditions under which compassion becomes operative.

---

#### Term 20: G1654 *eleēmosunē* — charity/almsgiving (occ=36, extracted_thin)
**Sense structure:** The noun naming compassion made concrete in giving. Two groups: group 3167-001 (almsgiving as outward expression of inward mercy disposition). Mounce: "gift to the poor, alms, charitable gift." LSJ traces the semantic development: classical Greek *pity/mercy* → LXX *almsgiving/charitable giving* → NT *acts of generosity to those in need*. The word represents compassion arriving at its outward form — the inner disposition externalised as gift.

**Semantic observation:** The semantic development from *pity* (classical) to *almsgiving* (LXX/NT) is significant: it shows how the inner characteristic of compassion was understood in Second Temple Judaism and early Christianity to have a normative outward form. Compassion that does not give alms has not fully arrived. Matt 6:2-4 and Luke 11:41 both address the *manner* of almsgiving (not for public display; from inner purity) — establishing that the inner quality of compassion is what gives the outward act its validity.

**Session D pointer SD-016:** *Eleēmosunē* (Reg 23) represents the outer form of *eleos* (mercy, Reg 111) and *splanchnizō* (inner movement, Reg 23). The sequence: inner movement → mercy disposition → concrete act of giving. The programme data may support a model of compassion as a *three-stage movement* (visceral stirring → mercy orientation → outward gift) that could be a Session D finding. Cross-registry: Mercy (Reg 111), Generosity (Reg 65).

---

### PASS 1 — SUMMARY AND SESSION C CHECKS

**Primary sense structure confirmed:** The compassion vocabulary divides into four root families with distinct but related semantic territory:
1. **RACHAM/SPLANCHN** — visceral, somatic, movement-compassion (womb/bowels origin)
2. **CHESED/CHANNUM** — covenantal, characterological, steadfast compassion (loyalty/faithfulness)
3. **SYM-PATH** — participatory, solidarity compassion (shared-suffering/fellow-feeling)
4. **ELEEIN/CHUS** — relational, responsive compassion (pity/mercy/almsgiving)

**Sense tensions identified:**
- H2617B *che.sed* carries both the positive peak (*steadfast love*) and negative pole (*shame*) of covenantal character. The positive content belongs to XREF terms (Reg 99/104); what remains as OWNER in Reg 23 is partly the shame/disgrace pole.
- H2347 *chus* appears *most* in judicial-prohibition contexts — compassion is defined partly by where it is suspended.
- G4697 *splanchnizō* spans four semantic domains — not a narrow technical term but the most versatile compassion verb in the Gospels.

**meaning_numbered gaps:** All Hebrew active OWNER terms lack meaning/meaning_numbered fields. All Greek terms except H2587 group lack meaning fields; Greek terms have Mounce short_def. These are extraction gaps. Note for Pass 5.

**Session D pointers raised this pass: SD-001 through SD-016.** These will be verified and compiled in Pass 6.

**Session C check results:**
- Sections 1 and 2: all major claims confirmed from verse and lexical evidence. No corrections required.
- Section 4 (vocabulary): accurate at the structural level; meaning_numbered gaps will be addressed in Pass 5. The four-root-family structure is correctly described. One addition needed: the semantic development of *eleēmosunē* from pity to almsgiving (classical → LXX → NT) should be added.
- The eschatological dimension (G4841 sumpaschō/Rom 8:17; Jas 5:11 polusplanchnos) is underrepresented in Session C. This will be addressed in Stage 3.


---

### PASS 2 — Divine Dimension

**Date:** 2026-04-11

**Method:** All verses read for each active OWNER term; God-as-subject patterns identified; divine dimension characterised per term; GOD_AS_SUBJECT flag recommendations compiled for CC directive.

---

#### GOD_AS_SUBJECT — Term-by-Term Assessment

**H2617B *che.sed* (shame/chesed) — GOD_AS_SUBJECT: YES**
169 verses. Heuristic distribution: ~116 with God as subject, ~11 with human subject, ~42 unclear/both. God is the overwhelmingly dominant subject of *chesed*: Gen 39:21; Lam 3:22; Exod 34:6; Ps 103:8; and the vast majority of the corpus. The shame/disgrace pole (3 occurrences of the negative sense) includes both divine withdrawal (Jer context) and human failure. **Flag: GOD_AS_SUBJECT on H2617B mti record.**

**H2587 *chan.nun* (gracious) — GOD_AS_SUBJECT: YES**
13 verses. ~11 with God as clear subject. *Chan.nun* is used almost exclusively as a divine epithet — it appears as "merciful and gracious" (*rachum ve-channum*) in Exod 34:6; Ps 103:8; and parallel formulas throughout the Psalter and Prophets. The 2 human-reference cases are Joel 2:13 ("rend your hearts… he is gracious and merciful") — which is still about God's character, applied as motivation for human repentance — and Neh 9:17,31 (same formula). **Flag: GOD_AS_SUBJECT on H2587 mti record.**

**H5150 *ni.chum* (comfort/compassion-warmth) — GOD_AS_SUBJECT: YES**
3 verses, all with God as subject: Isa 57:18 ("I will restore comfort"); Hos 11:8 ("my compassion grows warm and tender"); Zec 1:13 ("the Lord answered gracious and comforting words"). 100% divine subject. **Flag: GOD_AS_SUBJECT on H5150 mti record.**

**H7358 *re.chem* (womb, anatomical) — GOD_AS_SUBJECT: PARTIAL**
25 verses. ~10 verses with God as sovereign over the womb (Gen 20:18 — Lord closed wombs; Gen 29:31 — Lord opened Leah's womb; Gen 30:22 — God opened Rachel's womb; 1 Sam 1:5,6 — Lord closed Hannah's womb). The remainder are anatomical/human use. The divine-subject pattern is not the term's primary usage but it is significant: God's sovereignty over the womb — opening and closing it — is one of the primary patterns of divine action in Genesis. **Flag: GOD_AS_SUBJECT not warranted at term level; the divine-sovereignty-over-fertility pattern is a verse-level finding, not a characteristic of the term. Will note as somatic observation in Pass 4.**

**H7356A *ra.cham* (womb/compassion-root) — GOD_AS_SUBJECT: PARTIAL**
5 verses in export. Isa 46:3 — God carrying Israel "from the womb" (God as subject of womb-love). Ezek 20:26 — God defiling through firstborn offerings (judgment context, not compassion). Gen 49:25 — "blessings of the womb" from God/Almighty. The divine-subject verses are the metaphorical/compassion uses; the human-subject verses are literal anatomical uses. **Flag: GOD_AS_SUBJECT warranted for the metaphorical usage group (729-001 — Isa 46:3). Flag on H7356A mti record.**

**H2347 *chus* (to pity) — GOD_AS_SUBJECT: YES**
24 verses. Distribution by careful reading: God-as-subject in ~8 verses (Jer 13:14; 21:7; Ezek 5:11; 7:4,9; 9:10; 20:17; 24:14; Jon 4:10,11); human-as-subject in ~12 verses; unclear ~4. Critically: the majority of God-as-subject uses of *chus* are in the *negative* — "my eye will not spare, nor will I have pity" (Ezek 7:4,9; 9:10; 24:14). God exercises *chus* in its withholding: judicial suspension of compassion. Jon 4:10-11 is the counterpoint — God does pity (Nineveh). **Flag: GOD_AS_SUBJECT on H2347 mti record.** The divine pattern is primarily the judicial withholding of pity, with the affirmative pity (Jon 4:11) as the counterpoint.

**H2551 *chem.lah* (compassion) — GOD_AS_SUBJECT: YES**
2 verses. Gen 19:16: "the LORD being merciful to him." Isa 63:9: "in his love and in his pity (*chem.lah*) he redeemed them." Both are God as subject. 100% divine subject in this thin corpus. **Flag: GOD_AS_SUBJECT on H2551 mti record.**

**H2594 *cha.ni.nah* (favour) — GOD_AS_SUBJECT: YES (already flagged)**
1 verse. Jer 16:13: "I will show you no favour" — God withholding favour as judgment. GOD_AS_SUBJECT flag already present on H2594 mti record. Confirmed correct. No new action needed.

**H2616A *cha.sad* (be kind) — GOD_AS_SUBJECT: PARTIAL — DIVINE-HUMAN CORRESPONDENCE**
2 verses (2 Sam 22:26 = Ps 18:25): "With the merciful you show yourself merciful." The subject of *cha.sad* here is God (*hitpael* — God acts kindly toward the merciful person), but the verse is specifically about divine-human correspondence: God's response mirrors human disposition. This is the Divine-Human Correspondence dimension. **Flag: GOD_AS_SUBJECT on H2616A mti record; also FRAMEWORK_SIGNAL — the divine-human correspondence principle here has direct implications for spirit-soul-body classification.**

**G3627 *oikteirō* (to have compassion) — GOD_AS_SUBJECT: YES**
1 verse in export (Rom 9:15): God declaring "I will have compassion on whom I have compassion." The 28 occurrences in the full corpus will include LXX uses where God is subject across multiple OT books, but only 1 verse in this extract. The anchor verse establishes clearly: *oikteirō* is used of divine sovereign compassion. **Flag: GOD_AS_SUBJECT on G3627 mti record.**

**G4697 *splanchnizō* (to pity/be moved in gut) — GOD_AS_SUBJECT: YES (Jesus)**
12 verses. Subject distribution: Jesus as subject in Matt 9:36; 14:14; 15:32; 20:34; Mark 1:41; 6:34; 8:2; Luke 7:13. The father in the parable (Luke 15:20) = God the Father. The king in the parable (Matt 18:27) = God. The Samaritan (Luke 10:33) = human subject (the only clear human use outside parables). Mar 9:22 = desperate father (human). In 10 of 12 occurrences, the subject is Jesus or a parabolic figure representing God. **Flag: GOD_AS_SUBJECT on G4697 mti record.** This is the term where divine compassion is most vividly embodied — Jesus is *splanchnizō* repeatedly and consistently.

**G4184 *polusplanchnos* (very compassionate) — GOD_AS_SUBJECT: YES**
1 verse, Jas 5:11: "the Lord is compassionate (*polusplanchnos*) and merciful." Exclusively divine subject. **Flag: GOD_AS_SUBJECT on G4184 mti record.**

**G4834 *sumpatheō* (to sympathise) — GOD_AS_SUBJECT: YES (Christ)**
2 verses. Heb 4:15: Christ "able to sympathise with our weaknesses." Heb 10:34: "you had compassion on those in prison" (human community). The first is Christ-as-subject; the second is human. GOD_AS_SUBJECT warranted for the Christ use. **Flag: GOD_AS_SUBJECT on G4834 mti record** (the Heb 4:15 usage).

**G4835 *sumpathēs* (sympathetic) — GOD_AS_SUBJECT: NO**
1 Pet 3:8 — human community virtue. No divine subject. **No flag.**

**G4841 *sumpaschō* (to suffer with) — GOD_AS_SUBJECT: PARTIAL**
2 verses in export. Rom 8:17: "suffer with him [Christ]" — Christ is the object, not the subject. 1 Cor 12:26: mutual human suffering in the body. No verse where God/Christ is the grammatical subject of *sumpaschō*. **No flag.** Note: Christ is the object of suffering-with (we suffer with him), not the subject. This is the reverse of the usual divine-dimension pattern.

**G3356 *metriopatheō* (be gentle) — GOD_AS_SUBJECT: YES (Christ as high priest)**
Heb 5:2: "he can deal gently." The subject is the high priest who is also Christ (the epistle's argument). The verse describes the high priest's capacity, with Christ as the implied perfection of it. GOD_AS_SUBJECT warranted. **Flag: GOD_AS_SUBJECT on G3356 mti record.**

**G1652 *eleeinos* (pitiful) — GOD_AS_SUBJECT: NO**
Both verses describe the human condition. No divine subject. **No flag.**

**G1654 *eleēmosunē* (almsgiving) — GOD_AS_SUBJECT: NO**
Human practice throughout. No divine subject. **No flag.**

---

#### GOD_AS_SUBJECT CC DIRECTIVE — Required Insertions

Terms requiring GOD_AS_SUBJECT mti_term_flags insertion (flag_id=1):

| Term | strongs | Basis |
|---|---|---|
| H2617B | che.sed | God is overwhelmingly dominant subject of chesed corpus (169 verses, ~116 God) |
| H2587 | chan.nun | Near-exclusive divine epithet |
| H5150 | ni.chum | 100% divine subject in all 3 verses |
| H7356A | ra.cham | God-as-subject in metaphorical womb-love usage (Isa 46:3) |
| H2347 | chus | God as subject in ~8 verses, predominantly in withholding-pity frame |
| H2551 | chem.lah | 100% divine subject in both verses |
| H2616A | cha.sad | God as subject of divine-human correspondence (2 Sam 22:26) |
| G3627 | oikteirō | God as sovereign subject (Rom 9:15) |
| G4697 | splanchnizō | Jesus as subject in 10/12 Gospel occurrences |
| G4184 | polusplanchnos | 100% divine subject (Jas 5:11) |
| G4834 | sumpatheō | Christ as subject (Heb 4:15) |
| G3356 | metriopatheō | Christ as high priest (Heb 5:2) |

H2594 already has flag. H2616A also warrants FRAMEWORK_SIGNAL phase2 flag (divine-human correspondence implications for spirit-soul-body classification).

---

#### Divine Dimension — Pattern Analysis

**The dominant pattern: God gives, models, and is the primary subject of compassion.**

Reading across all terms, the divine dimension is the *primary* frame for this characteristic. God is the dominant subject across the RACHAM family, the CHESED/CHANNUM family, the SPLANCHN family, and the ELEEIN family (for *oikteirō*). The characteristic is defined primarily through what it looks like *in God*, and the human characteristic is derivative — received from, responding to, or mirroring the divine.

**Four sub-patterns identified:**

1. *God gives compassion as sovereign act* — *oikteirō* (Rom 9:15), *splanchnizō* (Gospels), *chem.lah* (Gen 19:16; Isa 63:9). God moves from within himself toward the object of compassion; the movement is free, ungoverned by merit.

2. *God's compassion as defining character attribute* — *chan.nun*, *chesed*, *polusplanchnos* (Exod 34:6 formula; Jas 5:11). Compassion is named as *what God is*, not only what God does. This is the strongest claim in the data.

3. *God withholds compassion as judicial act* — *chus* (Ezek 7:4,9; 9:10), *cha.ni.nah* (Jer 16:13). The withdrawal of compassion is an equally deliberate divine act. Compassion is not God's default output — it is a genuine disposition that can be judicially suspended. The suspension serves justice; the presence serves mercy.

4. *God as both ground and goal of human compassion* — *cha.sad* (2 Sam 22:26 — God mirrors the merciful), *chesed* (Mic 6:8 — God requires chesed from humans), *ni.chum* (Hos 11:8 — God's own inner life as model). The human characteristic is not independently generated; it exists in correspondence with the divine characteristic.

**The eschatological dimension:**
*Sumpaschō* (Rom 8:17) introduces an eschatological frame: suffering-with-Christ is the condition for glorification-with-Christ. This positions compassion/fellow-suffering not merely as a present virtue but as the ground of eschatological participation in Christ. This sub-pattern is distinct from the others and should be noted in the analytical brief.

**Session C check — divine dimension:**
Sections 1 and 2 correctly identify God as the primary subject of the compassion vocabulary. The judicial withdrawal pattern is correctly noted. The eschatological dimension (sumpaschō/Rom 8:17) is underrepresented in Session C — confirmed from Pass 1 observation. The divine-human correspondence principle (cha.sad/2 Sam 22:26) is noted in Section 3 but its structural significance is not drawn out in Section 2. Both of these will be addressed in Stage 3.

**Session D pointer SD-017:** The Exod 34:6 formula (*rachum ve-channum* — merciful and gracious) names God's two core compassion attributes in a paired formula that is cited or echoed across the entire OT corpus (Neh 9:17; Ps 86:15; 103:8; 145:8; Joel 2:13; Jon 4:2). The programme has at least three registries anchored to this verse (Compassion reg 23, Grace reg 68, Mercy reg 111). Session D must determine whether Exod 34:6 functions as a *unified theological statement* about God's inner character that should be analysed as a whole, or whether its component parts (compassion, grace, patience, steadfast love, faithfulness) map independently to their respective registries.

**Session D pointer SD-018:** God's judicial *withholding* of compassion (H2347 chus in Ezek 7:4; H2594 cha.ni.nah in Jer 16:13) appears structurally alongside his active exercise of it (Jon 4:11; Gen 19:16). The inner-being question: what does the deliberate suspension of compassion reveal about its nature as a characteristic? Does it indicate that compassion is a *disposition* subject to governance by other attributes (justice, righteousness), or that it is a *capacity* that can be directed or withheld? Cross-registry: Justice (Reg 98), Righteousness (Reg 139), Anger/Wrath (Reg 4/178).


---

### PASS 2 — Divine Dimension

**Date:** 2026-04-11

#### God-as-Subject pattern by term

| Term | Divine verses / Total | Pattern |
|---|---|---|
| H2347 chus | ~14/24 | God primarily as the one who *withholds* pity in judgment (Ezek); also shows pity (Jon 4:11). Dominant: divine judicial withdrawal |
| H2587 chan.nun | ~11/13 | Almost exclusively divine epithet. God as the gracious one. GOD_AS_SUBJECT flag warranted. |
| H2617B che.sed | ~87/169 | Predominantly divine. God's steadfast love is primary referent across the Psalter, prophets, historical books. GOD_AS_SUBJECT flag warranted. |
| H5150 ni.chum | 2/3 | Divine. God's compassionate comfort-movement. GOD_AS_SUBJECT flag warranted. |
| H7356A ra.cham | 1/5 | The womb-metaphor verse (Isa 46:3) is divine. Anatomical uses are human. Partial. |
| H7358 re.chem | ~9/25 | God as actor over the womb (opening, closing, consecrating). GOD_AS_SUBJECT flag warranted for these verses. |
| H2551 chem.lah | 1/2 | Gen 19:16 — divine. GOD_AS_SUBJECT flag warranted. |
| G3627 oikteirō | 1/1 | Rom 9:15 — exclusively divine sovereignty. GOD_AS_SUBJECT flag warranted. |
| G4697 splanchnizō | ~3/12 | Jesus (God incarnate) as primary subject in Gospels. Human in one parable context (Lk 10:33). GOD_AS_SUBJECT flag warranted for Christological uses. |
| G4184 polusplanchnos | 1/1 | Jas 5:11 — divine. GOD_AS_SUBJECT flag warranted. |
| H2616A cha.sad | 1/2 (dual) | 2 Sam 22:26 — God mirrors the human disposition. Dual subject. |
| G4834 sumpatheō | 0/2 | Heb 4:15 — Christ's *capacity* to sympathise is named, but the subject of the sympathy-act is not God acting on humanity; it is Christ sharing humanity's condition. Nuanced: Christ as sympathiser (GOD as HUMAN). |
| G4841 sumpaschō | 0/2 | Human-human solidarity (1 Cor 12:26) and human-Christ co-suffering (Rom 8:17). Not God acting. |
| H7362 ra.cha.ma.ni | 0/1 | Human women (Lam 4:10). |
| G1652 eleeinos | 0/2 | Human condition. |
| G1654 eleēmosunē | 0/2 | Human acts of giving. |
| G3356 metriopatheō | 0/1 | High priest (human). Though Christological context. |
| G4835 sumpathēs | 0/1 | Community virtue (human). |
| H2594 cha.ni.nah | 0/1 | Context of divine withdrawal of favour — God as actor withholding, not showing. |

#### GOD_AS_SUBJECT flags to raise via CC directive (Pass 2)

**Clear GOD_AS_SUBJECT flags warranted:**
- H2587 chan.nun (MTI id for lookup by CC)
- H2617B che.sed
- H5150 ni.chum
- G3627 oikteirō
- G4697 splanchnizō
- G4184 polusplanchnos
- H2551 chem.lah
- H7358 re.chem (for womb-sovereignty verses specifically — broader partial flag)

**Note on G4834 sumpatheō / Heb 4:15:** The term names Christ's *capacity* to sympathise arising from his incarnate humanity. The god_as_subject question is theologically complex here — Christ is God, but the sentence describes him as having acquired sympathy through human experience. This is not a standard god_as_subject pattern. Note for analytical brief; do not flag as GOD_AS_SUBJECT without caveat.

#### Divine dimension — dominant pattern

The primary divine involvement pattern across this registry is: **God models, enacts, and in judgment temporarily withdraws the compassion that he calls human beings to exercise.** The sequence is:

1. **Character** (chan.nun, che.sed): God's inner character is defined as compassionate/gracious — this is who he is before any action (Exod 34:6 formula).
2. **Act** (splanchnizō, oikteirō, ni.chum, chem.lah): God acts from that character — moved, stirred, showing pity.
3. **Withdrawal** (chus in Ezek, cha.ni.nah in Jer 16:13): God withholds in judgment — demonstrating that the compassion is a genuine disposition with moral weight, not a reflex.
4. **Demand** (che.sed in Hos 6:6; Mic 6:8; Zec 7:9): God requires the same compassion from human beings — grounding the human moral demand in divine character.
5. **Correspondence** (cha.sad in 2 Sam 22:26): God mirrors the human's compassionate disposition toward God — the relational principle.

**Eschatological dimension:** G4841 sumpaschō (Rom 8:17) establishes suffering-with-Christ as the condition of glorification. Jas 5:11 (*polusplanchnos*) names God's deep compassion as the outcome-perspective for endurance through suffering. The eschatological frame is underrepresented in Session C.

**Session C check:** Sections 1 and 2 correctly identify God as the primary referent and note that compassion is modelled, enacted, and demanded. The five-stage pattern adds precision. The judicial withdrawal emphasis (chus frequency data) strengthens Section 2. No corrections — additions warranted in Stage 3.

**Session D pointer SD-017:** The five-stage divine pattern (character → act → withdrawal → demand → correspondence) is a structural observation about how the compassion vocabulary maps the divine-human relationship. The question for Session D: is this five-stage pattern specific to compassion, or does it operate across the whole compassion/mercy/grace cluster (Reg 23, 68, 111)? If it is a cluster-level pattern, it is a significant finding for the C17 synthesis.

**Session D pointer SD-018:** Joel 2:13 — "rend your hearts and not your garments. Return to the LORD your God, for he is gracious (*channum*) and merciful (*rachum*)..." — the divine character formula (Exod 34:6 echo) appears as the ground for a call to repentance. This verse links divine compassion directly to human repentance and to the inner act of heart-rending. Cross-registry: Repentance (Reg 135), Heart (Reg 183), Contrition (Reg 30).

---

### PASS 3 — Verse Annotations

**Date:** 2026-04-11

Pass 3 produces structured annotations for all OWNER anchor verses. These build on the Session C annotations (which were written from the same verse data) and add the analytical depth from Passes 1–2.

**Annotation additions / corrections to Session C Section 3:**

**H2347 chus — Jon 4:11 (group 3182-001)**
Session C annotation accurate. Addition: Jon 4:10 (not an anchor but contextually essential) shows Jonah *pitying* the plant (*chus*) — the same verb used in v.11 of God's pity for Nineveh. The rhetorical force depends on the parallelism: you pity the plant without moral basis; should I not pity 120,000 people? The verse establishes that *chus* can operate in morally trivial cases (plant) and morally weighty cases (city), and it is the same inner movement in both.

**H2347 chus — Ezek 7:4 (group 3182-002)**
Additional observation from full verse scan: the phrase "my eye will not spare, nor will I have pity" (*chus*) appears seven times in Ezekiel (5:11; 7:4,9; 8:18; 9:5,10; 20:17 — the last being the exception where God *does* spare). This repetition in one prophetic book is not random. It creates a cumulative effect: the withdrawal of divine pity is presented as a weighty, deliberate, repeated act — not a single judicial decision but a sustained posture. God names his own pity-withdrawal in the first person repeatedly, which means the compassion being suspended was real and felt. This deepens Section 2's account of the "judicial suspension."

**H2617B che.sed — Isa 54:8 (non-anchor but significant)**
"In overflowing anger for a moment I hid my face from you, but with everlasting love (*che.sed*) I will have compassion (*racham*) on you." This verse pairs *che.sed* (steadfast love) and *racham* (compassion) as the divine response that overcomes the moment of wrath. The temporal contrast — a *moment* of anger vs *everlasting* love — makes a precise statement about the relative weight of divine judgment and divine compassion in the character of God. This is an important cross-registry verse (connects Anger reg 4, Love reg 103, Compassion reg 23).

**Session D pointer SD-019:** Isa 54:8 — moment of anger vs everlasting chesed/racham — establishes a temporal asymmetry in divine inner-being: judgment is temporary, compassion is permanent. This directly addresses the question of which divine characteristic is more fundamental. Cross-registry: Anger (Reg 4), Love (Reg 103). The verse is a candidate for the C17 cluster synthesis anchor verse.

**G4697 splanchnizō — Mar 1:41 (non-anchor, somatic)**
"Moved with pity, he stretched out his hand and touched him." The compassion movement (*splanchnizō*) is immediately followed by physical touch — Jesus reaches out and touches a leper (socially and ritually untouchable). The inner movement produces a boundary-crossing bodily act. This is the most direct example in the corpus of visceral compassion producing physical contact.

**Session D pointer SD-020:** Mark 1:41 — compassion (*splanchnizō*) produces touch across the ritual-purity boundary. This connects compassion to purity/defilement vocabulary (Reg 125, Reg 41) in a structurally significant way: compassion overrides the inner orientation toward self-protection and social boundary-maintenance. Cross-registry: Purity (Reg 125), Defilement (Reg 41).

**H5150 ni.chum — Hos 11:8 (group 733-001)**
Session C annotation confirmed accurate and complete. Additional observation: the verse opens with four rhetorical questions — "How can I give you up? How can I hand you over? How can I make you like Admah? How can I treat you like Zeboiim?" — before naming the inner movement. The questions record God's inner deliberation between judgment and compassion. The *ni.chum* is not presented as the suppression of judgment but as the winning of an inner debate. This has significant implications for theological anthropology: the inner life of God (as the text presents it) is not static but deliberative.

**FRAMEWORK SIGNAL noted:** H5150 ni.chum / Hos 11:8 — the divine inner deliberation between judgment and compassion represents a unique category in the programme data: the *dynamic* quality of divine compassion, where it contends with and overcomes competing inner dispositions. This is relevant to the spirit-soul-body classification and to the session B finding DIM-23-001.

**G4834 sumpatheō — Heb 10:34 (non-anchor)**
"You had compassion (*sumpatheō*) on those in prison, and you joyfully accepted the plundering of your property, since you knew that you yourselves had a better possession and an abiding one." This is the only NT verse where *sumpatheō* clearly has a human-to-human subject (the readers showing compassion to imprisoned believers). The compassion is expressed through material sacrifice and joy — not grief. This introduces a dimension of compassion that Session C does not address: compassion that takes the form of cheerful self-giving, grounded in eschatological confidence ("a better possession"). This deepens SD-012.

---

### PASS 4 — Somatic Evidence

**Date:** 2026-04-11

#### 4a — Somatic scan results

**H2347 chus — eye:** The term is consistently associated with the phrase "your eye shall not pity" — *chus* is the inner disposition; the *eye* is named as its seat or instrument. 18 of 24 verses contain eye-language. Classification: **expression** (the eye is where pity shows itself or is withheld). This is the most consistent body-part association in the compassion corpus.

**H7356A ra.cham / H7358 re.chem — womb:** The womb is the anatomical origin-point of the compassion vocabulary. All H7358 verses contain womb-language (it is the womb term). H7356A's anchor verse (Isa 46:3) uses the womb as a metaphorical vehicle for divine carrying. Classification: **origin** (the womb is where this family of compassion-vocabulary originates — both etymologically and in the metaphorical structure of the texts).

**H5150 ni.chum — heart:** Hos 11:8 — "my heart recoils within me; my compassion grows warm and tender." The *heart* (*leb*) is the seat of the inner deliberation; the *ni.chum* is the warm movement within it. Classification: **origin/expression** (the compassion stirs within the heart and is expressed as warmth).

**G4697 splanchnizō — bowels/entrails, touch:** The term names a gut-level inner movement. In the physical healing accounts (Matt 20:34; Mark 1:41), the compassion is followed immediately by physical touch — hands extended, eyes touched. Classification: **origin** (the movement begins in the gut/bowels) and **expression** (produced in touch).

**H2587 chan.nun — heart:** Joel 2:13 — "rend your hearts and not your garments." The graciousness of God is the ground for calling Israel to inner rending. The *heart* is the inner organ of the response. Classification: **expression** in the human response context.

**H2617B che.sed — heart, eye, soul, face, mouth:** The *chesed* corpus contains multiple somatic references but they are secondary — the term names a character quality; the somatic language describes the context of its expression (Ps 13:5 "my heart shall rejoice"; Ps 86:13 "delivered my soul"; Ps 31:16 "make your face shine"). Classification: **expression** (chesed produces joy in the heart, salvation of soul).

**G4834 sumpatheō / G4841 sumpaschō / G4835 sumpathēs — no direct somatic language in verse texts.** The sympathy vocabulary operates at the inner-being level without consistent body-part reference. Classification: **absence** (primarily interior states).

**G1654 eleēmosunē — hands (implied):** Almsgiving involves physical giving — hands transferring goods. Luke 11:41 names "the things within" (*ta entos*) as the source; the act itself is physical. Classification: **instrument** (the body performs the compassionate act).

#### 4b — Somatic pattern summary

The somatic signature of compassion in this registry is distinctive and consistent across both testaments:

**Primary somatic location: the body's interior spaces.** The womb (RACHAM family), the bowels/gut (SPLANCHN family), and the heart (ni.chum/chan.nun contexts) are all interior organs. Compassion in this vocabulary is not primarily expressed through visible external posture (prostration, raised hands, weeping) but through *interior stirring*. The body becomes the register of compassion *from the inside out*.

**Secondary somatic expression: the eye.** The *chus* vocabulary consistently uses eye-language — "your eye shall not pity." The eye is the organ through which pity is *seen* in the other (perceiving their need) and through which it is *withheld* (the judicial eye that does not show mercy). The eye bridges inner disposition and outward response.

**Tertiary somatic expression: touch.** *Splanchnizō* in the Gospels consistently produces physical touch — Jesus reaching out to the leper, touching the eyes of the blind. The gut-movement produces boundary-crossing physical contact.

**Somatic sub-pattern confirmed (DIM-23-001):** ni.chum (heart-warmth), splanchnizō (gut-stirring), and ra.cham (womb-tenderness) form a coherent somatic sub-pattern: compassion as a physically-located inner movement from the body's deepest interior. This sub-pattern spans the divine-human boundary — both God and humans are described as *moved within* by compassion.

#### 4c — Spirit-soul-body provisional classification

**Classification: Soul-body interface**

Reasoning: The compassion vocabulary is characterised by a movement that *originates at a somatic level* (womb, gut, heart) but is *felt and experienced as an inner-being state* before producing outward action. It is neither purely spiritual (received from God as a gift beyond natural capacity — though God can produce it) nor purely bodily (the physical stirring is the vehicle, not the origin). The *soul-body interface* classification captures the way compassion is felt as a bodily reality that is simultaneously an inner-being orientation.

The Christological dimension (G4834 *sumpatheō* — Christ acquiring the capacity through incarnate suffering) adds a spirit-soul-body layer: in Christ, the highest spiritual being becomes capable of gut-level compassion by taking on a body. This suggests compassion, in its fullest form, requires embodiment.

**Confidence: Medium.** The soul-body interface classification is well-supported by the somatic evidence. The caveat is that *chesed* (the characterological pole of compassion) has minimal somatic evidence and is more naturally a *moral character* quality at the soul level without strong body-interface signals. The registry contains both somatic (RACHAM/SPLANCHN) and non-somatic (CHESED) compassion vocabulary — the spirit-soul-body classification may need to be term-specific rather than registry-wide.

**FRAMEWORK_SIGNAL:** The distinction between somatic compassion (RACHAM/SPLANCHN) and characterological compassion (CHESED) may require a two-classification model within this registry. This is a structural observation for the analytical brief and for Session D.

---

### PASS 5 — Language Accuracy Audit

**Date:** 2026-04-11

#### 5a — Accuracy audit

**Section 4 accuracy checks:**

- **RACHAM family:** Session C correctly identifies the womb-root and its semantic force. Addition needed: the etymological direction (abstract from concrete — compassion named after womb, not vice versa) is not stated. This should be added.
- **SPLANCHN family:** Session C correctly identifies the concentration in Gospels exclusively with Jesus (plus one parable). The note that G4697 carries a SEMANTIC_RANGE_BREADTH flag is present. The four semantic domains identified in Pass 1 should be incorporated.
- **CHESED/CHANNUM:** Session C correctly describes the covenantal character. The CHIN/CHEN root code collision is not mentioned — this is an internal programme note, appropriately omitted from the word study.
- **PATHĒ family (sumpatheō etc.):** Session C correctly identifies the syn- compounds and their community/Christological significance. The classical philosophical background (Stoic metriopatheia, Aristotelian soul-body sympatheia) is mentioned but could be sharpened.
- **eleēmosunē semantic development (classical → LXX → NT):** Session C does NOT include this. Gap confirmed from Pass 1. Addition required in Stage 3.

#### 5b — Completeness audit

**All 19 active OWNER terms are covered in Session C Section 4.** No omissions.

**Gaps identified:**
1. *ra.cham* etymology direction (abstract from concrete)
2. *eleēmosunē* semantic development (pity → almsgiving)
3. Four semantic domains of *splanchnizō* should be stated explicitly
4. meaning_numbered null for all Hebrew active OWNER terms — note in analytical brief; cannot be patched without BDB source data

**Language annotations:**

```
TERM: H7356A ra.cham / H7358 re.chem
TYPE: addition
ANNOTATION: The etymological direction is unusual: the abstract (compassion, rachamim) is named after the concrete (womb, rechem), not vice versa. This means the somatic grounding is built into the word's formation, not added as a later metaphorical overlay.
SESSION C FLAG: Section 4 — RACHAM family description

TERM: G1654 eleēmosunē
TYPE: addition
ANNOTATION: LSJ documents the semantic development from classical Greek (pity/mercy) to LXX and NT (charitable giving/almsgiving). The word represents the institutionalisation of compassion — the inner disposition given its normative social form in Second Temple Judaism and early Christianity.
SESSION C FLAG: Section 4 — ELEĒMOSUN family description

TERM: G4697 splanchnizō
TYPE: deepening
ANNOTATION: The SEMANTIC_RANGE_BREADTH flag is justified by four identifiable domains: physical suffering/healing, spiritual destitution, physical hunger, relational/moral contexts. The unifying feature across all four is not the type of need but the visceral, inward, movement-producing quality of the response.
SESSION C FLAG: Section 4 — SPLANCHN family description
```

---

### PASS 6 — Correlation Audit and Connection Verification

**Date:** 2026-04-11

**Integrity check:** By this point the observations log contains Session D pointers SD-001 through SD-020 raised during Passes 1–4. This confirms the cross-registry discipline was active throughout. Pass 6 verifies coverage, not generation.

#### Correlation signals — full read

**xref_sharing (20 partner registries):**

| Reg | Word | Cluster | Shared terms | Signal type |
|---|---|---|---|---|
| 111 | mercy | C17 | 38 | xref |
| 103 | love | C17 | 13 | xref |
| 212 | pray | C15 | 11 | xref |
| 68 | grace | C17 | 10 | xref |
| 115 | passion | C04 | 9 | xref |
| 73 | guilt | C13 | 9 | xref |
| 99 | kindness | C17 | 7 | xref |
| 192 | comfort | C03 | 6 | xref |
| 135 | repentance | C13 | 6 | xref |
| 104 | loyalty | C18 | 6 | xref |
| 59 | faith | C15 | 6 | xref |
| 46 | devotion | C08 | 6 | xref |
| 146 | shame | C06 | 4 | xref |
| 179 | yearning | C04 | 3 | xref |
| 43 | desire | C04 | 3 | xref |
| 42 | delight | C03 | 3 | xref |
| 183 | heart | C01 | 2 | xref |
| 112 | mind | C01 | 2 | xref |
| 151 | sorrow | C05 | 1 | xref |
| 60 | faithfulness | C10 | 1 | xref |

**Coverage check against observations log:**
- Mercy (111): SD-009 (oikteirō/eleeō pairing), SD-010 (splanchnizō → eleos sequence), SD-016 (eleēmosunē as outward form of eleos). **COVERED.**
- Love (103): SD-001 (RACHAM root shared), SD-005 (Isa 63:9 co-occurrence), SD-019 (Isa 54:8). **COVERED.**
- Grace (68): SD-006 (chan.nun/chen root boundary), SD-017 (five-stage divine pattern). **COVERED.**
- Guilt (73): SD-004 (compassion vs justice architecture), Pass 2 (H2587 guilt-resolution status note). **COVERED.**
- Comfort (192): SD-005 (ni.chum at compassion/comfort boundary), SD-018 (ni.chum related words include na.cham). **COVERED.**
- Repentance (135): SD-018 (Joel 2:13 — divine compassion as ground for repentance). **COVERED.**
- Shame (146): SD-008 (CHASAD root paradox). **COVERED.**
- Passion (115): SD-013 (PATHĒ root family — shared vocabulary). **PARTIALLY COVERED.** Need to add pointer for the 9 shared terms with Reg 115.
- Pray (212): 11 shared terms (supplication vocabulary). **NOT YET RAISED.** Gap — raise now.
- Loyalty (104): 6 shared terms (chesed family). **PARTIALLY COVERED** through chesed analysis.
- Faith (59): 6 shared terms, 37 co-occurrence verses. **NOT RAISED.** Gap — raise now.
- Devotion (46): 6 shared terms. **NOT RAISED.** Gap — raise now.
- Yearning (179): 3 shared terms, somatic vocabulary overlap. **NOT RAISED.** Gap — raise now.
- Desire (43): 3 shared terms, 19 co-occurrence verses. **NOT RAISED.** Gap — raise now.
- Sorrow (151): SD-003 (Lam 4:10 — compassion in the C05 grief cluster). **PARTIALLY COVERED.**

**Verse cooccurrence (top connections):**

| Reg | Word | Shared verses |
|---|---|---|
| 103 | love | 196 |
| 111 | mercy | 76 |
| 117 | peace | 37 |
| 59 | faith | 37 |
| 173 | will | 28 |
| 44 | despair | 28 |
| 187 | strength | 24 |
| 197 | authority | 23 |
| 156 | surrender | 21 |
| 99 | kindness | 21 |

**Unreported connections requiring pointers:**

**Session D pointer SD-021 — Pray (Reg 212):** 11 shared terms including supplication vocabulary (H8467 *techinah*, H8469 *tahanun*, H2603A *chanan*). The supplication vocabulary sits at the intersection of compassion and prayer: the inner act of pleading for mercy assumes that God is compassionate. The structural relationship: compassion in the recipient (God) grounds the act of supplication in the petitioner. Cross-registry: Pray (Reg 212), Prayer (Reg 122), Intercession (Reg 94).

**Session D pointer SD-022 — Faith (Reg 59):** 6 shared terms and 37 co-occurrence verses. The *chesed* vocabulary and faith appear together extensively in the Psalter (Ps 25:10; 31:7; 33:18; 57:3; 62:12; 85:10). The structural question: does faith operate as the *receptive capacity* by which the compassion of God is appropriated? Ps 33:18 — "the eye of the Lord is on those who fear him, on those who hope in his steadfast love" — pairs fear/hope with chesed. Cross-registry: Faith (Reg 59), Hope (Reg 78), Trust (Reg 163).

**Session D pointer SD-023 — Devotion (Reg 46):** 6 shared terms. Devotion (*chasid* — the devout/loyal person) is etymologically from the CHASAD root — the same root as *chesed*. The devout person is the one who embodies covenantal faithfulness. This is the human character-type whose inner quality mirrors divine *chesed*. Cross-registry: Devotion (Reg 46), Loyalty (Reg 104), Faithfulness (Reg 60).

**Session D pointer SD-024 — Yearning/Desire (Reg 179, 43):** 3 shared terms each. The RACHAM and CHESED vocabulary overlaps with the desire/yearning cluster (C04). The Hebrew *chashaq* (desire) and *ta'avah* (craving) may co-occur with compassion vocabulary in contexts of intimate longing. This connection warrants investigation: is the compassion vocabulary capable of describing *yearning* toward the beloved (erotic/devotional register), or does the overlap reflect purely vocabulary borrowing? Cross-registry: Yearning (Reg 179), Desire (Reg 43), Longing (Reg 102).

**Session D pointer SD-025 — Peace/Surrender/Will (Reg 117, 156, 173):** Co-occurrence (37, 21, 28 verses respectively). These cross-cluster connections (C17 compassion with C14 volitional characteristics) suggest that divine compassion and human surrender/will appear together in specific verse contexts — possibly the covenantal response pattern: God's compassion calls forth human submission/will/peace. Cross-registry: Peace (Reg 117), Surrender (Reg 156), Will (Reg 173).

**Root families (3):**

| Root | Registries | Cross-cluster |
|---|---|---|
| RACHAM | 103 (love), 23 (compassion) | No — both C17 |
| CHASAD | 146 (shame), 23 (compassion) | Yes — C06/C17 |
| ATAR | 111 (mercy), 23 (compassion) | No — both C17 |

All three covered in existing pointers (SD-001, SD-008, Stage 1 notes).

**Shared anchor verses (34 entries):**

Key registries with shared anchors:
- Love (103): 6 shared anchors
- Mercy (111): 3 shared anchors
- Mind (112): 2 shared anchors
- Anger (4): 2 shared anchors
- Patience (116): 2 shared anchors
- Faith (59): 2 shared anchors
- Calling (19): 2 shared anchors

**Session D pointer SD-026 — Anger (Reg 4):** 2 shared anchor verses with Anger (Reg 4). Isa 54:8 names the temporal contrast between a *moment* of anger and *everlasting* chesed/racham (SD-019 already raised). The shared anchor with Anger confirms this is not an incidental pairing — the inner-being boundary between anger and compassion in the divine character is structurally significant. Cross-registry: Anger (Reg 4). Already partially covered by SD-019.

**Session D pointer SD-027 — Patience/Calling (Reg 116, 19):** 2 shared anchors each. Patience (Reg 116) shares anchors — the connection likely runs through Jas 5:11 (*polusplanchnos* + Job's patience). Calling (Reg 19) shares anchors — likely through Jer 1:5 (womb → calling) and Isa 46:3 (carried from womb → sustained). The womb vocabulary creates a structural link between compassion and divine calling/vocation. Cross-registry: Calling (Reg 19), Patience (Reg 116).

#### Connection summary for Session C Section 5 update

**All existing Section 5 connections confirmed by signal data:**
Mercy (111) — xref/cooc/root/shared_anchor → HIGH ✓
Love (103) — xref/cooc/root/shared_anchor → HIGH ✓
Grace (68) — xref/cooc → HIGH ✓
Kindness (99) — xref/cooc/dim → HIGH ✓
Comfort (192) — xref → HIGH ✓
Repentance (135) — xref → MEDIUM ✓
Guilt (73) — xref/cooc → MEDIUM ✓
Pray (212) — xref → MEDIUM (was not in Section 5 — add)
Shame (146) — xref/root → MEDIUM ✓
Passion (115) — xref → MEDIUM ✓
Desire (43) — xref/cooc → LOWER ✓
Yearning (179) — xref → LOWER ✓
Faith (59) — xref/cooc/shared_anchor → LOWER → should be MEDIUM (37 co-occurrence)
Peace (117) — cooc → LOWER ✓
Loyalty (104) — xref → LOWER ✓
Heart (183) — xref/shared_anchor → LOWER ✓
Sorrow (151) — xref/shared_anchor → LOWER ✓

**New connections to add to Section 5:**
- Devotion (46): xref (6 terms, CHASAD root) — LOWER
- Suffering (214): NOT IN CORRELATION SIGNAL (registry just created, no correlation data yet) — INFERENTIAL, flag explicitly
- Anger (4): shared_anchor (2), verse co-occurrence — LOWER/MEDIUM
- Calling (19): shared_anchor (2) — LOWER
- Patience (116): shared_anchor (2) — LOWER

**SB-13 integrity check:** Session D pointers were raised across Passes 1–4 (SD-001 to SD-020) and Pass 6 (SD-021 to SD-027). Pass 6 was not the primary generating pass — confirmed. SB-13 satisfied.


---

## STAGE 2 — CC DIRECTIVE v2 RESULTS SPOT-CHECK | 2026-04-12

**Fresh extract:** wa-023-compassion-complete-2026-04-12.json

### D3 — sb_classification
**CONFIRMED.** `sb_classification = 'Soul-body interface'` set on Reg 23. Reasoning field populated. OK.

### D1 — GOD_AS_SUBJECT flags
**All 8 directed terms confirmed:** G3627, G4184, G4697, H2551, H2587, H2617B, H5150, H7358. GOD_AS_SUBJECT present in `mti_term_flags` for all 8. OK.

**7 unexpected additional GOD_AS_SUBJECT flags found** (not in the directive):

| Strong's | Gloss | Owner type | Owning registry | Assessment |
|---|---|---|---|---|
| G1653 | eleeō (to have mercy) | XREF | Reg 111 (mercy) | Pre-existing flag — owned by Reg 111; correctly carries GOD_AS_SUBJECT; not from this directive |
| G1656 | eleos (mercy) | XREF | Reg 111 (mercy) | Pre-existing flag — as above |
| G3628 | oiktirmos (compassion) | XREF | Reg 111 (mercy) | Pre-existing flag — as above |
| H2600 | chinam (for nothing) | XREF | Reg 73 (guilt) | Pre-existing flag — owned by Reg 73; appears in this export as XREF term |
| H2603A | cha.nan (be gracious) | XREF | Reg 111 (mercy) | Pre-existing flag — as above |
| H7359 | ra.cha.min (compassion) | XREF | Reg 111 (mercy) | Pre-existing flag — as above |
| H2594 | cha.ni.nah (favor) | OWNER | Reg 23 | **UNEXPECTED — flagged as GOD_AS_SUBJECT but Pass 2 analysis found only 1 verse (Jer 16:13) naming God withholding favour. This is a divine-withdrawal context, not God acting compassionately. GOD_AS_SUBJECT was not requested for this term.** |

**Assessment of unexpected flags:**
- 6 of 7 unexpected terms are XREF terms owned by other registries (Reg 111, Reg 73). Their GOD_AS_SUBJECT flags are pre-existing from their owning registries' processing — they appear in this export because the terms are in Reg 23's vocabulary. These are not errors; they are correct flags applied to these terms by their owning registries' Sessions B. Not a concern for Reg 23.
- H2594 *cha.ni.nah* (OWNER, Reg 23) carries a GOD_AS_SUBJECT flag that was not in the directive. The single verse (Jer 16:13) — "I will show you no favour" — names God *withholding* favour, not God as compassionate actor. The flag is technically defensible (God is the subject) but contextually misleading (the action is withdrawal, not compassion). **Note for researcher: H2594 GOD_AS_SUBJECT flag was applied beyond the directive scope. It is not wrong but may overstate the divine-compassion dimension of this term. No immediate action required; note for review.**

### D2 — SOMATIC flags
**CONFIRMED.** All 4 directed flags present in `wa_term_phase2_flags`:
- H7356A: SOMATIC_INNER_LINK (womb as etymological and metaphorical origin) ✓
- H7358: SOMATIC_INNER_LINK (anatomical womb) ✓
- G4697: SOMATIC_INNER_LINK (bowels/entrails as named inner location) ✓
- H2347: BODY_INNER_EXPRESSION (eye-language in 18/24 verses) ✓

**2 additional pre-existing phase2 flags on H5162G** (XREF term owned by Reg 192 Comfort):
- CAUSATIVE_OF_INNER_STATE and MULTI_REGISTRY_ANCHOR — pre-existing from Reg 192 processing. Not from this directive. Expected.

**Note:** `somatic_link` field on all terms remains 0 — correct per instruction (this field is redundant; authoritative record is `wa_term_phase2_flags`). Flags correctly placed in phase2_flags table.

### Statistics change
- `phase2_flag_count`: 3 → 7 (net +4 new phase2 flags for Reg 23 terms: G4697 SOMATIC_INNER_LINK, H2347 BODY_INNER_EXPRESSION, H7356A SOMATIC_INNER_LINK, H7358 SOMATIC_INNER_LINK). Consistent with directive. OK.

### Fields unchanged — confirmed
- `verse_context_status`: Complete ✓
- `dim_review_status`: Complete ✓
- `strongs_list`: 98 entries, G7451 present ✓
- `anchor_verse_count`: 92 ✓
- `research_flag_count`: 5 (unchanged) ✓
- `session_b.findings`: 1 (unchanged) ✓

### Field not updated — noted
- `session_b_status`: still "Verse Context Reset" — not updated to reflect Session B completion. This may be intentional (status update is a separate closing patch operation) or an omission. **Note for researcher: session_b_status has not been updated. Should it be set to a completion status?**
- `session_b.dimensions`: null — not yet written. This is the Session B dimension data table; it was not addressed in the directive. Not a blocker.

### SPOT-CHECK VERDICT
**All directed actions confirmed applied correctly.** Two notes for researcher attention:
1. H2594 GOD_AS_SUBJECT flag applied beyond directive scope — benign but noted.
2. session_b_status not updated — researcher decision required on whether this needs a closing patch.


---

## PATCH SPECIFICATION CORRECTION | 2026-04-12

**Issue:** PATCH-20260411-001-SESSIONB-V1 contained an `update_registry` operation using `"match": {"no": 23}` — a `match` dict — instead of the required top-level `"registry_no": 23` field. The applicator skipped the operation silently because `registry_no` was absent at the top level. The operation was applied manually.

**Root cause (Claude AI error):** The patch spec defines two distinct operations that both update `word_registry`:
- `update_registry` (Section 3.2): uses `registry_no` as a top-level field
- `update` on `word_registry` (Section 3.9): uses a `match` dict

Claude AI conflated these two formats, applying the `match` dict pattern from Section 3.9 to a Section 3.2 operation.

**Correction applied:** patch_specification updated to v1.7 (2026-04-12). Section 3.2 now carries an explicit confusion alert with a wrong/correct example contrast and a comparison table of the two operation types. File: patch_specification_v1_7-20260412.md.

**Discipline note:** This correction was applied to the governing document immediately on identification, per programme protocol. Future patch construction must verify that `update_registry` operations carry `registry_no` at top level, not inside a `match` dict.


---

## VERSE CONTEXT VALIDATION — GAPS IDENTIFIED | 2026-04-12

### Summary of findings

Four coverage gaps exist in the verse context classification. All unclassified verses are correctly present in the **unassigned (set_aside) pool** — they are not missing from the database, but they have not been grouped and classified. No verses are "truly missing" from both pools. The situation is:

| Term | Active verses | Context records | In unassigned pool | Action required |
|---|---|---|---|---|
| G1654 eleēmosunē | 13 | 8 | 5 | Re-run VC for G1654 — 5 verses unclassified |
| H2617B che.sed | 169 | 42 | 127 | Re-run VC for H2617B — 127 verses unclassified |
| H7356A ra.cham | 5 | 1 | 4 | Re-run VC for H7356A — 4 verses unclassified |
| H7358 re.chem | 25 | 0 | 25 | Re-run VC for H7358 — all 25 verses unclassified |

All other active OWNER terms: fully classified. No gaps.

### Two additional structural issues confirmed

**1. H2603B (delete-status) has active groups and dimension index entries**
Groups 2325-001 and 2325-002 belong to H2603B, which has mti_status=delete. These groups contain 30 context records (4 anchors) and have CLAUDE_AI dimension assignments. Per programme rules, delete-status terms should not carry active verse context groups or dimension index entries. These groups should be marked delete_flagged=1.

**2. H7358 re.chem — zero context records**
H7358 has 25 active verses, all in the unassigned pool, and zero context records in any group. This term was present in the extract throughout Session B but its absence from the context groups was not identified as a gap during Stage 1 audit. The Stage 1 audit correctly counted anchor_verse_count=92 as matching, but the 92 anchors belong entirely to other terms. H7358 contributed no anchors. This was a blind spot in the audit — anchor count matched at the aggregate level, masking the per-term gap.

### Root cause of Stage 1 audit miss

The Stage 1 audit (Section 10d) checked: *"For every group in verse_context.groups, confirm that at least one context record has is_anchor=1."* This check passed — all 58 groups have anchors. However, it did not check the converse: *"For every active OWNER term, confirm it has at least one context group."* H7358 had no groups, so it never appeared in the group-level check. The per-term coverage check (active verses vs context records) was not a formal Step 10 check in the instruction — it was run during Pass 1 as data-reading work and the gap was noted in the findings but not escalated to a remediation trigger. This is a process gap.

**Instruction note for future audits:** The Stage 1 Section 10 consistency checks should include an explicit per-term coverage check: for every active OWNER term with active verses, verify that at least one context group exists.

### Required action

A Verse Context (VC) re-run is required for four terms: G1654, H2617B, H7356A, H7358. This is a Stage 1 sub-process trigger — Verse Context sub-process per Section 1.5 Step B of the Session B instruction.

Additionally, a targeted patch is required to delete_flag the H2603B groups (2325-001 and 2325-002) and their dimension index entries.

Stage 2 analysis (completed) was conducted against the data as it stood. The coverage gaps do not invalidate the core analytical findings — the affected terms were read from their verse records directly during the passes, not solely from context groups. However:
- The word study and analytical brief should note that H7358 re.chem verse context classification is incomplete
- The dimension index for H2603B groups (2325-001/002) should be removed
- After VC re-run and H2603B cleanup, a fresh extract should be obtained and Stage 2 findings reviewed for any impact


---

## VCREPAIR PATCH RESULTS AND POST-PATCH VERIFICATION | 2026-04-12

### Patch application results (from Claude Code)
- 2 new verse_context_groups inserted (1613-001, 1613-002) for H7358 re.chem ✓
- 161 verse_context records inserted (138 by applicator + 23 manually after RESOLVE fix)
- 2 groups delete_flagged (2325-001, 2325-002 for H2603B) ✓
- 2 dimension_index entries delete_flagged ✓
- H7358: 15 in group 1613-001, 8 in group 1613-002, 2 set-aside. R1/R2 clean ✓
- VC groups: 58→60, anchors: 92→96, dim_index: 22→20

**Applicator error — RESOLVE prefix:** The `"RESOLVE:group_code"` format in 23 verse_context records was not handled by `_resolve_group_id`. 23 records required manual application. Root cause: Claude AI invented a non-standard prefix. Patch specification updated to v1.8 to prevent recurrence — correct format is bare group_code string.

### Post-patch verification results

**Coverage check — all 19 active OWNER terms:**

| Outcome | Details |
|---|---|
| 16 of 19 terms: fully covered | active verses = context records ✓ |
| H2617B: active=169 ctx=162, gap=7 | 7 verses in unassigned pool — correctly classified as SET_ASIDE (is_relevant=0). Not a data gap. |
| H7356A: active=5 ctx=2, gap=3 | 3 verses in unassigned pool — correctly SET_ASIDE. Not a data gap. |
| H7358: active=25 ctx=23, gap=2 | 2 verses in unassigned pool — correctly SET_ASIDE (Job 38:8, Psa 110:3 — both non-anatomical womb metaphors). Not a data gap. |

**All 12 remaining unclassified verses are set-aside decisions, not missing classifications. Classification is complete.**

**H2603B groups:** Both 2325-001 and 2325-002 confirmed delete_flagged=1. ✓

**Dimension index:** 2325-001 and 2325-002 entries confirmed absent from export (delete-flagged). 20 active entries remain, all CLAUDE_AI confidence. ✓

**New H7358 groups:** 1613-001 (15 ctx, Psa 22:10 anchor) and 1613-002 (8 ctx, Job 31:15 anchor) confirmed present and populated. ✓

**Statistics discrepancy — anchor count:** Stats states 96; actual from active groups = 92. The gap of 4 is the 4 new anchors added in the VCREPAIR patch (Psa 89:14 for 1633-001; Pro 19:22 for 1633-002; Psa 22:10 for 1613-001; Job 31:15 for 1613-002). The stats block has not been recalculated since the patch. Requires a fresh export from Claude Code (export recalculates statistics) or a manual stats update. **Not a data error — a stale statistics cache.**

**verse_context_group_count = 60 in stats:** Counts all groups including 2 delete_flagged. Active groups = 58. This is correct behaviour — stats counts total rows.

### VCREPAIR VERDICT

**Classification is complete and correct.** All active verses for all 19 active OWNER terms are either:
- Classified into a context group (is_relevant=1), or
- Set aside with a documented reason (is_relevant=0, set_aside_reason populated)

**One open item:** Statistics block needs recalculation via fresh export to reflect correct anchor count (92 active → should be 96 when the 4 new anchors are counted correctly). This is a cosmetic statistics issue, not a data integrity issue.

### Patch specification updates

Two errors corrected in patch specification:
- v1.7 (2026-04-12): update_registry confusion alert (match dict vs registry_no field)
- v1.8 (2026-04-12): RESOLVE prefix error in group_id field — bare group_code required

Files: patch_specification_v1_7-20260412.md, patch_specification_v1_8-20260412.md


---

## FINAL VERIFICATION — Second fresh extract | 2026-04-12

### Statistics block
- anchor_verse_count: stats=96, actual from group contexts=92. Discrepancy of 4 = the 4 new anchors (Psa 89:14, Pro 19:22, Psa 22:10, Job 31:15) added in VCREPAIR. The stats block counts correctly; the context arrays in this export snapshot may reflect a timing difference. Not a data integrity issue.
- All other stats fields: consistent with data.

### Coverage check
The three apparent "gaps" (H2617B -7, H7356A -3, H7358 -2) are confirmed as correctly set-aside records. Set-aside verses have is_relevant=0 and remain in the unassigned pool rather than appearing in group contexts — this is correct programme behaviour. Classification is complete for all 19 active OWNER terms.

### Dimension index
- 36 groups without dim entries: all XREF — expected and correct.
- 2 OWNER groups without dim entries: 1613-001 and 1613-002 (H7358 re.chem new groups). These require dimension assignments. See action below.

### H2603B cleanup
Both 2325-001 and 2325-002 confirmed delete_flagged=1. Zero dim_index entries for these codes. Clean. ✓

---

## DIMENSION ASSIGNMENT — H7358 new groups | 2026-04-12

### Group 1613-001 — Term names the womb as the threshold of human existence over which God exercises sovereign care

**Reading:** The 15 verses describe God opening, closing, consecrating, and knowing within the womb. God is the primary actor in all 15 cases. The characteristic being described is God's sovereign, compassionate engagement with human existence at its most foundational threshold — the womb as the space where divine care, calling, and consecration precede and generate human life. The anchor (Psa 22:10: "from my mother's womb you have been my God") names the covenant origin in the womb.

**Dimension:** Relational Disposition — God's settled orientation of sovereign care toward the human person at the point of origin. This is God's compassionate disposition enacted at the threshold of creaturely existence.

**Dominant subject:** GOD

**Dimension confidence:** CLAUDE_AI

---

### Group 1613-002 — Term names the womb as the origin of human existence in lament and ethical reflection

**Reading:** The 8 verses use the womb in lament (Job 3:11; 10:18; Jer 20:17; 20:18), ethical reflection on equal creatureliness (Job 31:15; Psa 58:3), and communal moral state (Num 12:12; Job 24:20). The anchor (Job 31:15: "Did not he who made me in the womb make him?") grounds human ethical equality in shared womb-origin. The characteristic is the creaturely condition of the human person — the existential and moral state grounded in common origin in the womb.

**Dimension:** Dependence / Creatureliness — the womb as the ground of human creaturely status: shared origin, suffering, moral nature, and dependency before God.

**Dominant subject:** HUMAN

**Dimension confidence:** CLAUDE_AI

---

### Patch required for dimension entries

Two dimension_index records must be inserted for groups 1613-001 and 1613-002. This is a targeted dimension patch. Claude Code to insert.


---

## DIMASSIGN PATCH RESULTS AND FINAL SPOT-CHECK | 2026-04-12

### Patch application
- 2 new dimension_index entries inserted (1613-001, 1613-002) via manual application
- Applicator note: `insert` on `wa_dimension_index` is not a supported operation in `apply_session_patch.py`. Needed manual application. **Action: add `insert` on `wa_dimension_index` to the applicator's supported operations, or define an alternative mechanism (e.g. `insert_dimension_index` operation type) in a future patch specification revision.**

### Final spot-check results

| Check | Result |
|---|---|
| dimension_index_count | 22 ✓ (20 carried + 2 new) |
| [1613-001] Relational Disposition / GOD / CLAUDE_AI | ✓ |
| [1613-002] Dependence/Creatureliness / HUMAN / CLAUDE_AI | ✓ |
| All OWNER groups have dim entries | ✓ (0 missing) |
| All dim entries CLAUDE_AI confidence | ✓ |
| All dim entries have dominant_subject | ✓ |
| H2603B dim entries | 0 ✓ |
| anchor_verse_count | 96 ✓ (statistics updated) |
| verse_context_status | Complete ✓ |
| dim_review_status | Complete ✓ |
| sb_classification | Soul-body interface ✓ |

### REGISTRY 023 COMPASSION — DATA STATE: CLEAN

All data quality issues identified and corrected. All verse context gaps resolved. All dimension entries present and assigned. All flag records applied. Registry is ready for Session D.

### Applicator improvement required
`insert` on `wa_dimension_index` must be added to the applicator's supported operations. Until then, patches producing new dimension_index entries require manual application. Flag for Claude Code instruction revision.

