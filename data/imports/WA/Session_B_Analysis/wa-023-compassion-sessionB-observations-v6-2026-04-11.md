# WA-023-Compassion — Session B Observations Log
**Filename:** wa-023-compassion-sessionB-observations-v6-2026-04-11.md  
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

