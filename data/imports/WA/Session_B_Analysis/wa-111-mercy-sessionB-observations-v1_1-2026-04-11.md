# Session B Observations Log
## Registry 111 — mercy
## Version: v1.1 (Stage 1 complete — patch applied, CI results recorded, R1 pending)
## Date: 2026-04-11
## Instruction: WA-SessionB-Analysis-Instruction-v4.7-2026-04-11
## Input file: wa-111-mercy-complete-2026-04-11.json
## Session C word study: wa-111-mercy-word-study-v1-2026-04-11.md
## Session: 1 of N

---

> This log is the complete analytical record for Registry 111 (mercy) Session B.
> Version increments at every pass and stage boundary.
> Writes append within a pass — no overwrite.

---

## STAGE 1 — DATA AUDIT

---

### SECTION 1 — Registry Block

| Field | Value | Status |
|---|---|---|
| `word` | mercy | OK |
| `no` / `id` | 111 / 111 | OK |
| `cluster_assignment` | C17 | OK |
| `verse_context_status` | Complete | OK — Stage 1 may proceed |
| `session_b_status` | Verse Context Reset | NOTE: stale label from pre-VC processing; will be updated in Stage 1 remediation |
| `dim_review_status` | Complete | OK |
| `dim_review_version` | WA-DimensionReview-Instruction-v1.9-2026-04-09 | OK |
| `sb_classification` | null | OK — not yet assigned; Pass 4 task |
| `sb_classification_reasoning` | null | OK — consistent with above |
| `unique_term_count` / `shared_term_count` / `term_sharing_ratio` | 19 / 46 / 0.708 | Registry-level fields — noted, not verified against statistics block (per instruction) |
| `dimensions` | Relational/Social | NOTE: pre-review label; dimension_index now shows full profile |
| `description` | Populated | OK |

**strongs_list cross-check:**
- strongs_list contains 66 entries (stored as JSON string); terms array contains 67 terms
- G8849 (polueleos) is in the terms array but ABSENT from the strongs_list — GAP
- All other 66 strongs_list entries have a corresponding term record — OK
- Two terms with `delete_flagged = 1`: H0834A (a.sher "which" — grammatical particle) and H5921A (al "upon" — preposition). Both have `owner_type = None`, indicating they were captured by the verse extraction engine as incidental co-terms, not as programme terms. Both have `mti_status = delete`. No exclusion_reason recorded but content is transparently non-inner-being (grammatical particles). Deletions confirmed — no reinstatement required.

**Deletion justification review — all delete-status terms:**

| Term | Gloss | Owner type | Exclusion reason | Justification review |
|---|---|---|---|---|
| H0834A | which (relative particle) | None | null | Grammatical particle; 4,974 occurrences; no inner-being content. Deletion confirmed. |
| H5921A | upon (preposition) | None | null | Preposition; 5,802 occurrences; no inner-being content. Deletion confirmed. |
| H2345 | darkened | XREF | null | Sense: dark colour/brown. Related to rachel-family etymology. No inner-being content. Deletion confirmed. |
| H2433 | chin (beauty) | XREF | "Bleed vocabulary — peripheral aesthetic sense" | Adequately documented. Deletion confirmed. |
| H2594 | chaninah (favour) | XREF | (shared note with H2433 and H2606) | Single occurrence; adequately covered by H2603A. Deletion confirmed. |
| H2603B | cha.nan (variant) | XREF | "No corpus evidence — all span matches resolve to H2603A" | No verse data. Deletion confirmed. |
| H2606 | Chananel (Tower of Hananel) | XREF | "Proper noun" | Confirmed proper noun — architectural feature. Deletion confirmed. |
| H2624 | cha.si.dah (stork) | XREF | "Animal name, no love content" | Confirmed. Deletion confirmed. |
| H3724B | ko.pher (pitch) | OWNER | **null** | Sense: asphalt/pitch as a covering material. Etymologically related to H3722A (kip.per/atone) via root meaning "to cover." The covering function is foundational to the atonement concept but H3724B itself refers only to the physical material (pitch coating Noah's ark, Gen 6:14). No inner-being usage context. The covering etymology is already surfaced through H3722A. Deletion confirmed — adequately covered. |
| H3724C | ko.pher (henna) | OWNER | **null** | Sense: henna plant. Homonymous root, not atonement-related in usage. Song of Songs contexts only. No inner-being content. Deletion confirmed. |
| H3724D | ko.pher (village) | OWNER | **null** | Sense: village/settlement. Topographic term. No inner-being content. Deletion confirmed. |
| H6282A | a.tar (worshiper) | OWNER | "Bleed vocabulary. See bulk note." | Sense: suppliant/worshiper — one occurrence. H6279 (a.tar, to pray) is the active term and covers the prayer/supplication semantic. H6282A is a nominal derivation. Deletion confirmed — adequately covered. |
| H6282B | a.tar (odour) | OWNER | "Bleed vocabulary. See bulk note." | Sense: odour/incense smoke. Olfactory/ritual object sense; no inner-being content. Deletion confirmed. |
| H7313 | to rise (Aramaic) | XREF | null | Aramaic verb meaning "to be lifted up/exalted." Related to Hebrew rum. Appears in ra.cha.min (compassion) root family context in some MSS. No direct inner-being content as a standalone term. Deletion confirmed — adequately covered by Hebrew equivalents. |
| H7314 | height (Aramaic) | XREF | null | Aramaic noun "height." Topographic/abstract height. No inner-being content. Deletion confirmed. |
| H7328 | mystery/secret | XREF | null | Aramaic raz — secret/mystery. Appears as a term associated with the ra.cha.min etymology path in some reference works but carries no inner-being mercy content itself. Deletion confirmed. |

**G8849 (polueleos — "full of mercy") — special case:**
- Status: `candidate_delete` (not full `delete`)
- Absent from strongs_list — GAP: should appear with its count
- Has 0 verse records despite occurrence_count = 8 in the term record — data gap
- No VC groups, no dimension_index entry
- Quality flags: NO_VERSES, NO_WORD_ANALYSIS, PROSE_ONLY_MEANING, THIN_DATA
- Exclusion_reason: null
- **Analytical review:** G8849 *polueleos* is a compound Greek term (polus + eleos = "abounding in mercy") occurring 8 times in NT, primarily in the LXX Psalms tradition and echoed in the NT. It names God's character as overflowing mercy — a quantitative intensifier of the central eleos term. It is semantically distinct from G1656 eleos in that it emphasises the abundance and overflow quality. As an owner term in candidate_delete status with no verse records, it cannot be classified or annotated. However, its meaning is not adequately covered by any other single active owner term.
- **Finding:** G8849 should be retained as an active owner term but its verse data gap must be resolved. The candidate_delete status requires researcher review — Claude AI recommends **reinstatement review**: add G8849 to strongs_list and resolve the NO_VERSES gap. This is a researcher decision.

CHECKPOINT — Stage 1 Audit
Last section completed: Section 1 — Registry Block
Next section: Section 2 — Statistics Block
Session may close here.

---

### SECTION 2 — Statistics Block

| Field | Stated | Actual | Status |
|---|---|---|---|
| term_count | 67 | 67 | OK |
| active_term_count | 65 | 65 | OK |
| owner_term_count | 31 | 31 | OK |
| xref_term_count | 34 | 34 | OK |
| verse_count | 2325 | 2325 | OK |
| active_verse_count | 595 | 595 | OK |
| verse_context_group_count | 72 | 72 | OK |
| verse_context_record_count | **1748** | **1051** | **ERROR** |
| anchor_verse_count | 123 | 123 | OK |
| dimension_index_count | 36 | 36 | OK |
| research_flag_count | 1 | 1 | OK |
| session_b_finding_count | **1** | **0** | **ERROR** |
| cross_registry_link_count | 0 | 0 | OK (expected) |
| correlation_xref_pair_count | 20 | 20 | OK |
| correlation_cooccurrence_pair_count | 90 | 90 | OK |
| correlation_dimension_pair_count | 17 | 17 | OK |
| correlation_root_family_count | 1 | 1 | OK |
| correlation_shared_anchor_count | 28 | 28 | OK |

**verse_context_record_count ERROR investigation:**
- Stated: 1748. Actual contexts in VC groups: 1051. Unassigned records: 697. Total: 1748 = 1051 + 697.
- The `phase1_verse_count` on the registry also shows 1748.
- The stated statistics count is including the unassigned records in the total, whereas the actual count of context records in assigned groups is 1051.
- **Finding:** The statistics field `verse_context_record_count` is counting total phase 1 verse records (assigned + unassigned = 1748) rather than the count of context records in `verse_context.groups.contexts` (1051). This is a statistics calculation error in the export script. The correct value depends on the programme's definition: if the field means "context records assigned to groups," the correct value is 1051. If it means "total phase 1 verse records entering the VC process," the value 1748 is defensible. **Researcher decision required:** confirm intended definition before issuing correction patch.

**session_b_finding_count ERROR investigation:**
- Stated: 1. The `session_b_findings` top-level array is empty (count=0). However, `session_b.findings` block inside the session_b object contains 1 record (DIM-111-001).
- The statistics field is counting from `session_b.findings`, not from a `session_b_findings` top-level array. The export script appears to expose `session_b_findings` as a top-level empty array while the actual finding lives inside `session_b.findings`.
- **Finding:** Statistics count is correct (1 finding exists). The export schema exposes findings in two places; the top-level `session_b_findings` array is empty while `session_b.findings` contains the record. This is a data structure inconsistency in the export — the count (1) is correct relative to the actual finding. No correction to the statistics field required; however the export schema inconsistency should be noted for Claude Code.

CHECKPOINT — Stage 1 Audit
Last section completed: Section 2 — Statistics Block
Next section: Section 3 — Terms
Session may close here.

---

### SECTION 3 — Terms

**god_as_subject (all terms = 0):**
Per WA-SessionB-Analysis-Instruction-v4.7 Section 3: `god_as_subject` is a redundant field superseded by `mti_term_flags` flag_id 1 (GOD_AS_SUBJECT). Do NOT update this field. Issue directives to Claude Code to insert correct `mti_term_flags` records in Pass 2.
- Based on context group descriptions and anchor verses, GOD_AS_SUBJECT flags are warranted for: G1653 (eleeō — group 981-001 dominant_subject=GOD), G1656 (eleos — group 983-001 dominant_subject=GOD), G2436 (hileōs — group 3166-001 dominant_subject=GOD), G3628 (oiktirmos — group 992-001 dominant_subject=GOD/NONE), G3629 (oiktirmōn — group 3158-001 dominant_subject=NONE but Luk 6:36 names Father as merciful), H3819 (lo-ruhamah — dim_index dominant_subject=GOD), H7359 (ra.cha.min — group 988-001), H5750 (od — group 990-002 dominant_subject=GOD), H2603A (cha.nan — group 984-001), H3727 (kap.po.ret — group 982-001).
- **Directive captured for Pass 2 delivery (D1):** GOD_AS_SUBJECT flag insertion for identified terms.

**somatic_link (all terms = 0):**
Per instruction Section 3: `somatic_link` is a redundant field. Use `mti_term_flags` SOMATIC_INNER_LINK (flag_id 3) or BODY_INNER_EXPRESSION (flag_id 4). Do NOT update somatic_link field.
- Somatic evidence confirmed in anchor verses: G3628 oiktirmos (Col 3:12 — *splagchna oiktirmou*), G1656 eleos (Luk 1:78 — *splagchna eleos*), G1653 eleeō (Luk 18:13 — chest-beating), H8467 techinah (1Ki 8:38 — stretched hands).
- **Directive captured for Pass 4 delivery (D2):** SOMATIC flag insertion review.

**G8849 polueleos — candidate_delete, no exclusion_reason:**
- Status noted above in Section 1. Owner term, 8 occurrences, no verse records in extract, absent from strongs_list.
- **Open item for researcher:** Recommend reinstatement and verse data resolution.

**OWNER delete terms with null exclusion_reason (H3724B/C/D):**
- Three homonyms of ko.pher: pitch (H3724B), henna (H3724C), village (H3724D)
- All have null exclusion_reason but deletion is analytically justified (see Section 1 review)
- **Directive captured:** Add exclusion_reason text to each of these three terms.

**Root family completeness — all owner active terms have root_family records:** OK

**XREF terms — no root_family records:**
- All 34 XREF active terms have empty root_family arrays
- This is expected: XREF root families are managed in their owning registries
- No action required

**Quality flags summary (owner active terms):**
- THIN_DATA on G0415, G0448, G0462, G2433, G2434, G3629, G3743, H3722B, H3724A, H3725, H3819, H2604, H7359 — noted; these terms have limited verse samples. No action beyond noting.
- NO_VERSES on G8849 — see above.
- NO_WORD_ANALYSIS on G8849, G0448 — noted; prose-only meaning available.

CHECKPOINT — Stage 1 Audit
Last section completed: Section 3 — Terms
Next section: Section 4 — Verse Context Groups
Session may close here.

---

### SECTION 4 — Verse Context Groups

- 72 groups total
- All groups have context_description: OK
- All groups have at least one anchor (is_anchor=1): OK
- No duplicate group codes: OK
- 36 groups belong to XREF terms and have no dimension_index entry — this is correct by design
- 36 groups belong to OWNER terms and all have dimension_index entries — OK

CHECKPOINT — Stage 1 Audit
Last section completed: Section 4 — Verse Context Groups
Next section: Section 5 — Dimension Index
Session may close here.

---

### SECTION 5 — Dimension Index

- 36 entries, all OWNER term groups
- All entries: `dimension_confidence = CLAUDE_AI` — OK
- All entries: `dominant_subject` populated (not null) — OK
- All dimension values reviewed against approved vocabulary:
  - Moral Character, Relational Disposition, Dependence / Creatureliness, Divine-Human Correspondence — all valid
  - No KEYWORD_WEAK entries
- `dim_review_status = Complete`, `dim_review_version` populated — OK
- **Dimension Review sub-process: NOT required**

CHECKPOINT — Stage 1 Audit
Last section completed: Section 5 — Dimension Index
Next section: Section 6 — Session B Block
Session may close here.

---

### SECTION 6 — Session B Block

- `session_b.dimensions`: null — not yet written; Stage 2 Pass 4 task
- `session_b.findings`: 1 record present (DIM-111-001, DIMENSION_REVIEW type, raised 2026-04-08)
  - Finding: atonement/propitiation vocabulary creates a cluster of Transformation/GOD groups — Session B should examine the relationship between mercy as divine inner disposition and atonement as its structural mechanism.
  - This is an active finding requiring attention in Stage 2 Pass 1 and Pass 3.

CHECKPOINT — Stage 1 Audit
Last section completed: Section 6 — Session B Block
Next section: Section 7 — Session D Block
Session may close here.

---

### SECTION 7 — Session D Block

- `sd_pointer_flags`: empty — expected at this stage; will be populated during Stage 2
- `runs`: empty — no Session D has been run

CHECKPOINT — Stage 1 Audit
Last section completed: Section 7 — Session D Block
Next section: Section 8 — Research Flags
Session may close here.

---

### SECTION 8 — Research Flags

| Flag | Label | Priority | Target | Resolved |
|---|---|---|---|---|
| DIMREVIEW_SESSION_D | DIM-111-SD001 | MEDIUM | D | No |

- DIM-111-SD001: mercy-seat / Lo-Ruhamah polarity as structural feature of C17; connection to forgiveness polarity in Reg 64. Session D target — carry forward, no Stage 2 action.

CHECKPOINT — Stage 1 Audit
Last section completed: Section 8 — Research Flags
Next section: Section 9 — Cross-Registry Links
Session may close here.

---

### SECTION 9 — Cross-Registry Links

- Count: 0 — expected gap; populated in Session D. No action required.

CHECKPOINT — Stage 1 Audit
Last section completed: Section 9 — Cross-Registry Links
Next section: Section 10 — Consistency Checks
Session may close here.

---

### SECTION 10 — Consistency Checks

**10a — Root family completeness:**
- 13 root codes identified across owner active terms
- Only ATAR (H6279 + H6282A/B) appears in `correlations.root_families` (registry_count=2, shared with Reg 23 compassion)
- 12 other root codes (ELE, HILEŌS, ANOSI, OIKTIR, OIKTIRMŌN, HOSIŌS, POLUELE, CHANAN, KIPPER, LO RUCHA, OD, RACHAMIN) have terms in this registry but do NOT appear in `correlations.root_families`
- **Investigation:** The correlation signal for root_families fires only when a root code spans multiple registries. Single-registry roots do not appear in the cross-registry correlation signal (expected). For multi-registry roots, the question is whether other registries carry the same root codes:
  - ELE root (G0415/G1653/G1655/G1656): this is the core Greek eleos family. Compassion (Reg 23) shares G1653 and G1656 via xref — and their root family records in Reg 23 may also carry ELE. If so, ELE should appear in correlations.root_families. This warrants a CC investigation directive.
  - CHANAN root (H2603A/H2604/H8467): Grace (Reg 68) and Guilt (Reg 73) share H2603A via xref. If Reg 68 carries CHANAN root code, this should also appear. Warrants CC investigation.
  - KIPPER root: No other registry clearly shares KIPPER-family terms via xref_sharing. Single-registry root — absence from correlation signal expected.
  - All other roots: appear single-registry. Expected absence from signal.
- **Directive captured for CC investigation:** Verify whether ELE and CHANAN root codes appear in other registries and update correlation signal if so.

**10b — Root correlation signal consistency:**
- ATAR appears in correlations.root_families — OK (registry_count=2, Reg 23 compassion)
- ELE and CHANAN: see 10a — open item for CC investigation

**10c — Dimension index vs VC group consistency:**
- 36 of 72 VC group descriptions are not in dimension_index — all 36 belong to XREF terms, as confirmed by mti_term_id check. This is correct by design.
- All 36 dimension_index entries have matching VC group descriptions — OK
- No orphaned dimension_index entries — OK

**10d — Anchor verse consistency:**
- Stated anchor_verse_count (123) = actual is_anchor=1 contexts (123) — OK
- All 72 groups have at least one anchor — OK

**10e — XREF signal vs term inventory:**
- All 20 xref_sharing entries: stated shared_term_count matches actual len(shared_strongs) — OK
- No delete_flagged=1 terms present in any shared_strongs list — OK

**10f — Statistics correlation counts vs correlations block:**
- All five correlation count fields match actual array lengths — OK

**10g — Session B classification consistency:**
- sb_classification and sb_classification_reasoning both null — consistent; Pass 4 task — OK

CHECKPOINT — Stage 1 Audit
Last section completed: Section 10 — Consistency Checks
Next section: AUDIT SUMMARY
Session may close here.

---

## AUDIT SUMMARY — Registry 111 (mercy) | 2026-04-11

### Fields confirmed OK
- word, no, id, cluster_assignment, verse_context_status (Complete), dim_review_status (Complete), dim_review_version
- All statistics fields except verse_context_record_count and session_b_finding_count (see below)
- All correlation count fields
- anchor_verse_count, dimension_index_count, research_flag_count, cross_registry_link_count
- Dimension index: all CLAUDE_AI confidence, all dominant_subject populated
- VC groups: all descriptions present, all anchors present, no duplicates
- xref_sharing signal: all 20 entries internally consistent, no delete_flagged=1 terms
- session_b block: 1 finding present (DIM-111-001), consistent with stated count of 1

### Gaps requiring field-level patch

| Gap | Field | Current value | Correct value | Patch action |
|---|---|---|---|---|
| G1 | strongs_list | G8849 absent | Add G8849 with count=8 | Add entry to strongs_list JSON |
| G2 | mti.exclusion_reason for H3724B | null | "Homonym of H3722A — physical pitch material. No inner-being content. Covered by H3722A." | Update exclusion_reason |
| G3 | mti.exclusion_reason for H3724C | null | "Homonym of H3722A — henna plant. No inner-being content." | Update exclusion_reason |
| G4 | mti.exclusion_reason for H3724D | null | "Homonym of H3722A — village/settlement. No inner-being content." | Update exclusion_reason |

### Consistency failures requiring patch

None confirmed. 10b (ELE and CHANAN root codes missing from correlation root_families) is a CC investigation item, not a direct patch — requires cross-registry data check before a correction can be issued.

### verse_context_record_count — researcher decision required

The stated value (1748) counts total phase1 verse records (assigned + unassigned). The actual context records in assigned groups = 1051. **Researcher must confirm intended definition before a correction patch can be issued.** If the field should count assigned-group contexts only, correct value = 1051.

### Verse Context sub-process required?
[x] No — verse_context_status = Complete; all groups have descriptions and anchors

### Dimension Review sub-process required?
[x] No — dim_review_status = Complete; all groups CLAUDE_AI confidence; no null dominant_subject

### Statistics corrections required?
[x] Yes — verse_context_record_count: stated=1748, pending researcher decision on definition (1051 if assigned-group contexts; 1748 if all phase1 records)
[x] session_b_finding_count: stated=1, actual per top-level array=0, but 1 finding exists in session_b.findings block. Export schema inconsistency — no statistics correction needed; schema note to CC required.

### strongs_list — deletion justification review

[ ] All deletions confirmed — no reinstatement required — **NOT FULLY CONFIRMED: G8849 is open**
[x] G8849 polueleos (candidate_delete, OWNER): recommend reinstatement review — 8 occurrences, no verse records in extract, meaningful semantic content (abounding in mercy) not fully covered by other active terms. Requires researcher decision.
[x] H3724B/C/D: deletions confirmed but null exclusion_reason — patch required (G2/G3/G4 above)
[x] All other delete-status terms: deletions confirmed analytically

### Root family gaps

[ ] Yes — ELE (G0415/G1653/G1655/G1656) and CHANAN (H2603A/H2604/H8467) root codes may be missing from correlations.root_families if other registries share these roots. CC investigation required before patch decision.

### CC investigation items (not patches — require CC data lookup first)

| Item | Question | Action |
|---|---|---|
| CI-001 | Does root code ELE appear in other registries (e.g. Reg 23 compassion)? | CC: query wa_term_root_family for root_code='ELE' across all registries |
| CI-002 | Does root code CHANAN appear in other registries (e.g. Reg 68 grace, Reg 212 pray)? | CC: query wa_term_root_family for root_code='CHANAN' across all registries |
| CI-003 | G8849 polueleos — verse records: why does the term record show occurrence_count=8 but the extract contains 0 verse records? | CC: query wa_term_verses for term_inv_id of G8849 in Reg 111 |
| CI-004 | session_b_findings export schema: top-level `session_b_findings` array is empty while `session_b.findings` contains the record. Is this an export schema issue? | CC: confirm schema and correct if needed |

### Directives captured (for D1 delivery after Pass 3)

| Directive | Pass | Type | Detail |
|---|---|---|---|
| DIR-001 | Pass 2 | mti_term_flags | GOD_AS_SUBJECT flag insertion for: G1653, G1656, G2436, G3628, G3629, H3819, H7359, H5750 (group 990-002), H2603A, H3727 — confirm dominant_subject GOD groups before inserting |
| DIR-002 | Pass 4 | mti_term_flags/phase2_flags | SOMATIC flag review: G3628 (splagchna Col 3:12), G1656 (splagchna Luk 1:78), G1653 (chest-beating Luk 18:13), H8467 (stretched hands 1Ki 8:38) |

### Open items requiring researcher decision

1. **G8849 polueleos** — candidate_delete status, absent from strongs_list, no verse records. Recommend reinstatement. Researcher must confirm before patch is issued. (Required before Stage 2 begins if term is to be analysed in Pass 1.)
2. **verse_context_record_count** — researcher must confirm whether the correct value is 1051 (assigned-group contexts) or 1748 (all phase1 records). Affects whether a statistics patch is needed.


---

## STAGE 1 — RESEARCHER DECISIONS AND REMEDIATION

### Decision 1 — G8849 polueleos

**Researcher instruction:** Issue CC directive to reinstate deleted verses.

**Claude AI investigation findings (post-instruction):**
- `status_note` on G8849 records: *"A6b-F1: zero verses returned by STEP (8 occurrences), zero analytical signals"* — automated extraction correctly found 0 verses.
- All 8 occurrences of *polueleos* are in the LXX Greek OT (Neh 9:17, 9:31; Psa 86:5, 103:8; Joel 2:13; Jon 4:2). No NT occurrences.
- Programme corpus is ESV-based. LXX OT verses are covered by Hebrew terms (H7349, H2617A) already active in this registry. There are no verses to reinstate within corpus scope.
- `testament = NT_only` is an extraction artefact from STEP's Greek search returning no NT matches.

**Revised recommendation accepted by researcher:** Confirm G8849 as delete (corpus scope exclusion, not adequacy-of-coverage). Document exclusion_reason. Add to strongs_list with count=0. No VC sub-process triggered.

### Decision 2 — verse_context_record_count

**Researcher direction:** Option A — accept 1748. Field is computed as `len(vc_rows)` at line ~680 in export script — counts all verse_context table records regardless of classification. Value is a database row count, not a semantic grouping count. Analytical breakdown already captured by anchor (123) + related (928) + set_aside (697) = 1748. No patch required.

---

### REMEDIATION — Patch and CC Directive Produced

**Patch:** `PATCH-20260411-111-PREANALYSIS-V1.json`

Operations:
- OP-001: G8849 — update mti_status from candidate_delete to delete; add exclusion_reason (LXX corpus scope)
- OP-002: H3724B — add exclusion_reason (pitch homonym, no inner-being content)
- OP-003: H3724C — add exclusion_reason (henna homonym, no inner-being content)
- OP-004: H3724D — add exclusion_reason (village homonym, no inner-being content)
- OP-005: word_registry — add G8849 to strongs_list with count=0
- OP-006: registry_note — verse_context_record_count 1748 confirmed correct
- OP-007: schema_investigation_note — session_b_findings export schema inconsistency flagged

**CC Directive:** `wa-111-mercy-sessionB-cc-directive-v1-2026-04-11.md`

Investigation items:
- CI-001: ELE root code cross-registry check
- CI-002: CHANAN root code cross-registry check
- CI-003: G8849 verse record gap verification
- CI-004: session_b_findings export schema clarification

**Status:** Patch and directive produced. Awaiting researcher review and Claude Code application.

CHECKPOINT — Stage 1 Remediation
Last step completed: Patch PATCH-20260411-111-PREANALYSIS-V1 produced; CC directive v1 produced
Next step: Researcher reviews patch → Claude Code applies patch → Claude Code runs investigations CI-001 to CI-004 → Claude Code produces fresh extract R1 → Stage 2 may begin
Session may close here.


---

## STAGE 1 — CI INVESTIGATION RESULTS (returned by Claude Code)

### CI-001 — ELE root family cross-registry

**Result:** Registry 111 only. 4 records (G0415, G1653, G1655, G1656), all in mercy. No cross-registry presence — Reg 23 (compassion) does not carry ELE root_family records on its XREF copies of these terms.

**Implication:** The correlation signal for ELE will not fire until Reg 23 has ELE root records added to its copies of G1653 and G1656. This is a gap in Reg 23's root family data, not in Reg 111. To be raised as a Session D pointer or a Reg 23 Session B action item. No patch required for Reg 111.

### CI-002 — CHANAN root family cross-registry

**Result:** Registry 111 only. 3 records (H2603A, H2604, H8467), all in mercy. Grace (Reg 68) uses root code `CHEN` for the same etymological family (Hebrew חנן). Root code collision: mercy uses `CHANAN`, grace uses `CHEN`. The correlation signal between these registries will not fire until the codes are reconciled.

**Implication:** This is a root code normalisation gap — two registries use different codes for the same root family. Resolution requires either: (a) a programme-wide decision on canonical code for the חנן root, or (b) a cross-registry root reconciliation patch affecting both Reg 111 and Reg 68. This is a Session D / programme-level item. No patch required for Reg 111 in isolation.

**Session D pointer captured:** CHANAN/CHEN root code collision between Reg 111 (mercy) and Reg 68 (grace) suppresses correlation signal. Programme-level root code normalisation required before cross-registry root family signals are reliable for this root.

### CI-003 — G8849 verse record gap

**Result:** Zero `wa_verse_records` in the database. Corpus scope exclusion confirmed — LXX-only term, zero ESV occurrences. `mti_terms` record now carries `status=delete` with exclusion_reason and updated status_note from patch OP-001.

**Implication:** Deletion confirmed. No further action. Corpus scope exclusion is fully documented.

### CI-004 — session_b_findings export schema

**Result:** No top-level `session_b_findings` key in the export schema. Findings live under `session_b.findings` by design. `statistics.session_b_finding_count = 1` correctly counts from that source. No bug — Claude AI was looking for a key that does not exist in the schema.

**Implication:** No action required. Session 1 schema_investigation_note (OP-007) is resolved. The statistics field is correct.

---

## STAGE 1 — PATCH APPLICATION CONFIRMATION

**Patch PATCH-20260411-111-PREANALYSIS-V1 applied:** 4 mti updates, 1 registry update, 2 notes.

**Note on R1 extract:** The post-patch extract referenced by researcher (`data/exports/Session C/wa-111-mercy-complete-2026-04-11.json`) has not yet been uploaded to this session. The R1 spot-check cannot be completed until the file is uploaded. Stage 2 is gated on this.

**Version numbering correction noted:** Observations log should have incremented to v1.1 at Stage 1 completion boundary per instruction. Correcting now by producing v1.1 with the Stage 1 complete marker and CI results appended.

STAGE 1 COMPLETE
All audit sections done. Patch applied. CI results recorded. R1 extract pending upload for spot-check.
Observations log version increments to v1.1 at this boundary.

