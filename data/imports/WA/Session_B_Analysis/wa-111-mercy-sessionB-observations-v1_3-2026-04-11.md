# Session B Observations Log
## Registry 111 — mercy
## Version: v1.3 (Pass 3 complete — verse annotations; D1 ready)
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


---

## STAGE 1 — R1 SPOT-CHECK

**Extract:** wa-111-mercy-complete-2026-04-11.json (R1 — post-patch)
**File size:** 4,498,071 bytes (increased from 4,497,241 — patch application confirmed)
**Spot-check date:** 2026-04-11

| Check | Item | Result |
|---|---|---|
| 1 | G8849 mti_status = delete | OK |
| 1 | G8849 exclusion_reason populated (LXX corpus scope) | OK |
| 1 | G8849 status_note updated | OK |
| 2 | H3724B exclusion_reason populated | OK |
| 2 | H3724C exclusion_reason populated | OK |
| 2 | H3724D exclusion_reason populated | OK |
| 3 | G8849 in strongs_list with count=0 | OK |
| 3 | strongs_list total entries = 67 | OK |
| 4 | active_term_count = 65 | OK |
| 4 | owner_term_count = 31 | OK |
| 4 | xref_term_count = 34 | OK |
| 5 | All dimension_index entries CLAUDE_AI confidence | OK |
| 5 | All dominant_subject populated | OK |
| 6 | session_b.findings count = 1 (DIM-111-001) | OK |

**Result: ALL CHECKS PASS. R1 confirmed clean.**

Stage 1 is fully complete. Stage 2 may begin.


---

## STAGE 2 — PASS 1: MEANING AND SEMANTIC RANGE

**Extract in use:** wa-111-mercy-complete-2026-04-11.json (R1)
**Date:** 2026-04-11
**Active owner non-delete terms:** 25 (13 Greek, 12 Hebrew)

---

### Greek mercy-compassion family

**G1656 eleos — mercy, pity**
Primary sense: the moral quality of compassion moved to action — feeling pity and showing kindness toward one in need. Mounce captures both dimensions: feeling and showing. LSJ confirms classical usage from Homer onwards (ἔλεος as pity/compassion), always with a recipient who evokes pity. The NT use extends this: God's eleos is not merely reactive pity toward distress but the proactive covenant faithfulness that grounds salvation (Eph 2:4, Luk 1:78). Two groups: (1) God's mercy as defining inner attribute — ground of salvation and covenant faithfulness; (2) mercy as inner-being virtue and judicial reality — what God desires over ritual, what wisdom produces, what triumphs over judgment.
**Semantic boundary observation:** eleos covers both the divine disposition and the human virtue. The boundary between eleos as divine attribute and eleos as human character quality is not sharp — the groups show both. This is not ambiguity but structural: human mercy is derivative of divine mercy. The term does not bifurcate.
**Session C check:** Section 1 correctly describes eleos as covering felt compassion and concrete action. Section 4 correctly notes the SEMANTIC_RANGE_BREADTH and RELATIONAL_DIRECTION flags. Confirmed.
**meaning_numbered:** Currently null, single prose sense. Sense structure is adequate for a term this well-documented; no update required.
**Cross-registry (2.0a):** Group 983-002 ("what God desires above ritual") — Mat 23:23 places mercy alongside justice and faithfulness as the weightier matters of the law. This is a direct theological connection between mercy and justice (Reg unknown — check cluster C17 for justice registry). Also: mercy triumphing over judgment (Jam 2:13) implies a structural relationship between mercy and judgment/condemnation that Session D needs to examine.
**SD pointer captured:** Jam 2:13 and Mat 23:23 both encode a mercy-justice structural relationship. Does mercy operate as a judicial category in its own right, or as the suspension of justice? Session D to examine across C17.

---

**G1653 eleeō — to have mercy, to show mercy**
Primary sense: the verb form of eleos — to exercise mercy, to show compassion in action. Three groups capture three distinct registers of usage: (1) God's sovereign mercy — "I will have mercy on whom I have mercy" (Rom 9:15) — naming mercy as divine prerogative, not human claim; (2) the supplicant's cry — Bartimaeus, the blind man, the tax collector — naming mercy as the desperate appeal of one who knows they have no claim; (3) the human act of mercy that receives mercy in return (Mat 18:33, Mat 5:7). 
**Semantic tension identified:** The same verb names both the divine sovereign act (Rom 9:15) and the human responsive act (Mat 18:33). This is not a weakness in the term but its theological depth: mercy flows downward from God to human, and horizontally from human to human, and the same word names both movements. The divine usage shapes the human imperative.
**LSJ note:** Classical eleeō means simply "to pity, feel compassion for" — the NT adds the relational and soteriological weight absent in classical usage.
**Cross-registry (2.0a):** Group 981-002 (cry for mercy) — Bartimaeus crying "Son of David, have mercy on me" while being silenced by the crowd (Mar 10:48): the external pressure to silence the cry for mercy is analytically interesting. Persistence under opposition appears as a characteristic linked to the mercy cry. Connection to perseverance/endurance registries possible.
**SD pointer captured:** The mercy cry in synoptic healing narratives encodes persistence under social pressure. Does the cry for mercy share structural features with the vocabulary of hope and perseverance?

---

**G1655 eleēmōn — merciful (adjective)**
Primary sense: the person whose character is marked by mercy — merciful, pitiful, compassionate. Mounce explicitly notes "feelings of pity, with a focus of showing compassion to those in serious need." One group: mercifulness as inner character quality — the Beatitude (Mat 5:7) and Christ as merciful high priest (Heb 2:17). 
**Key semantic contribution:** Where eleos names the quality and eleeō names the act, eleēmōn names the person — the one for whom mercy is a settled character disposition. The Beatitude form ("blessed are the *merciful*") makes this clear: it addresses those for whom mercy is habitual, not occasional.
**Heb 2:17 observation:** Christ becomes eleēmōn through shared human experience ("made like his brothers in every respect"). This is significant for the formation question: merciful character is not innate but formed through participation in vulnerability. The term in this context names an acquired character quality, not a natural attribute.
**Cross-registry (2.0a):** Heb 2:17 pairs eleēmōn with pistos (faithful/trustworthy) as the two defining qualities of the high priest. Mercy and faithfulness appear as structural co-requisites for the priestly mediating role. Connection to faithfulness (Reg 60) and to the priesthood/intercession theme.

---

**G3629 oiktirmōn — compassionate (adjective)**
Primary sense: merciful, compassionate — the character quality of being moved by the suffering of others. Two occurrences in programme groups: Luk 6:36 ("Be merciful as your Father is merciful") and Jam 5:11 ("the Lord is compassionate and merciful"). LSJ confirms classical usage from 5th c. BC, primarily of persons.
**Semantic distinction from eleēmōn:** Both are adjectives naming the merciful person, but oiktirmōn carries a stronger sense of being *moved* emotionally — the visceral quality of compassion before it becomes action. Its root oiktirmos (pity, compassion arising from seeing suffering) emphasises the affective origin.
**Cross-registry (2.0a):** Luk 6:36 — "Be merciful as your Father is merciful" — uses oiktirmōn for both human and divine. The divine-to-human pattern of mercy here is the same as in Col 3:12 (put on oiktirmos as a garment). This links to the image-of-God and character formation themes.

---

**G3628 oiktirmos — compassion (noun)**
Primary sense: compassion, mercy, pity — the feeling that responds to suffering and moves toward relief. Mounce: "kindness, pity in relieving sorrow and want." LSJ: classical usage of pity/compassion from 5th c. BC, NT extends to the plural "mercies" (oiktirmoi) naming the aggregate compassionate acts/dispositions of God. Two groups: (1) God as "Father of mercies" (2Cor 1:3) — oiktirmos as the generative inner character of God; (2) "compassionate hearts" as the garment of the new humanity (Col 3:12).
**Somatic marker confirmed:** The related word "to have compassion" (oiktirō) is associated with visceral inner movement. The Col 3:12 phrase *splagchna oiktirmou* — "bowels/inner organs of mercy" — is the most somatic mercy expression in the NT. The body's interior (splagchna) is named as the location where oiktirmos originates.
**Directive for Pass 4:** SOMATIC flag warranted for G3628 on the basis of splagchna association. Captured for DIR-002 (D2 delivery).
**Cross-registry (2.0a):** 2Cor 1:3 — "Father of mercies and God of all comfort." oiktirmos and parakl sis (comfort) are directly paired. The mercy of God flows into comfort of the afflicted. Connection to Reg for comfort/consolation if one exists in the programme.

---

**G0415 aneleēmōn — merciless, ruthless**
Primary sense: without mercy, uncompassionate, cruel. Single occurrence in programme: Rom 1:31, in the catalogue of collapsed inner character. LSJ confirms classical usage from 4th c. BC, used of the merciless character.
**Semantic contribution:** The negative twin of eleēmōn. Its presence in Rom 1:31 alongside "faithless, heartless" (aspondos, astorgos) is diagnostic: mercilessness is not a standalone vice but part of a cluster of relational failures marking the person who has been "handed over" to the consequences of God-rejection. Mercilessness is the relational face of inner death.
**Cross-registry (2.0a):** Rom 1:31 is a dense inner-being text — the full catalogue (foolish, faithless, heartless, ruthless) names multiple characteristics simultaneously. The verse encodes the co-occurrence of cognitive, relational, and moral collapse. The absence of mercy appears alongside the absence of natural affection (astorgos, which may belong to a love registry).

---

**G0448 anileōs — merciless (Jam 2:13)**
Primary sense: merciless — Attic form, single NT occurrence in Jam 2:13 ("judgment is without mercy to one who has shown no mercy"). LSJ confirms Attic form from 2nd c. AD. The term functions as the judicial counterpart to eleos: the person who has not shown mercy receives judgment-without-mercy.
**Semantic distinction from aneleēmōn:** Where aneleēmōn names a character quality (the merciless *person*), anileōs names a judicial condition (the judgment that operates *without* mercy). The distinction matters: one is dispositional, the other is consequential.
**Cross-registry (2.0a):** Jam 2:13's structure — "judgment without mercy to the one who showed no mercy; mercy triumphs over judgment" — encodes a reciprocal mercy-judgment dynamic. This is the clearest statement of mercy as a judicial category in the NT. Connection to judgment/justice registries.

---

**G2433 hilaskomai — to propitiate, to make atonement**
Primary sense (middle voice): to make atonement for, to propitiate — "with a focus on the means for accomplishing forgiveness, resulting in reconciliation." Passive voice: to have mercy on, to pardon. The same verb covers both the human act of seeking propitiation (Luk 18:13 — "God, be merciful to me") and the divine provision of it (Heb 2:17 — "to make propitiation for the sins of the people").
**Critical semantic observation:** The middle/passive alternation is analytically significant. In the middle, the subject performs propitiation. In the passive, the subject *receives* mercy. The same verb names both the mechanism (atonement made) and the experience (mercy received). This confirms the session_b finding DIM-111-001: propitiation and mercy are not separate concepts but two faces of the same act.
**LSJ classical note:** In classical Greek, hilaskomai meant "to appease or propitiate the gods" — always the human's act toward the divine. The NT radically reverses this: it is God who provides the propitiation (1Jo 4:10 — "he sent his Son to be the propitiation"). The direction of action inverts between classical and NT usage. This inversion is theologically central and not captured in the current meaning_numbered (prose only).
**meaning_numbered update:** The middle/passive distinction and the classical-to-NT direction reversal warrant structured senses. Directive captured for meaning_numbered update.
**Cross-registry (2.0a):** Luk 18:13 — the tax collector's cry is a propitiation cry uttered in a posture of physical self-abasement (chest-beating, eyes downcast). The somatic and the theological are inseparable in this verse. Connection to humility/shame registries.

---

**G2434 hilasmos — propitiation, atoning sacrifice**
Primary sense: the *means* of propitiation — the atoning sacrifice, the covering that effects forgiveness. Two occurrences in NT (1Jo 2:2, 1Jo 4:10), both identifying Christ as the hilasmos. LSJ: classical usage "means of appeasing" (plural). LXX extends to "atonement, sin offering."
**Semantic contribution:** Where hilaskomai names the act and hilastērios names the locus (mercy seat/propitiation), hilasmos names the *provision* — what is given to accomplish propitiation. In 1Jo, this provision is identified with the person of Christ: he is not the one who performs propitiation but the thing that constitutes it. The distinction between act, locus, and provision is subtle but the three terms together map the complete structure.
**Cross-registry (2.0a):** 1Jo 4:10 — "not that we loved God but that he loved us and sent his Son to be the hilasmos." The propitiation is grounded in divine love. This encodes the mercy-love structural relationship: mercy requires a mechanism (propitiation) that love provides. Connection to love (Reg 103) is theological and causal.
**SD pointer captured:** The causal chain in 1Jo 4:10 — divine love → sending of Son → propitiation → forgiveness — encodes a structural relationship between love and mercy that Session D needs to examine. Is mercy the expression of love toward the guilty, or is love the source from which mercy flows?

---

**G2435 hilastērios — mercy seat / propitiation**
Primary sense: dual — (1) the mercy seat (kapporet), the golden cover of the ark where propitiation was enacted (Heb 9:5); (2) the place/means of propitiation, used of Christ in Rom 3:25. The term bridges the spatial-ritual and the personal-theological. SEMANTIC_RANGE_BREADTH flag correctly identifies this term as spanning both.
**Semantic boundary observation:** The dual sense is not polysemy (two unrelated meanings) but typological extension: the mercy seat is the OT type; Christ as hilastērios is the NT antitype. The same term names both because the same theological function is operative — the divinely-provided meeting point where guilt is addressed and mercy is granted.
**Cross-registry (2.0a):** Heb 9:5 — mercy seat described alongside cherubim of glory ("Above it were the cherubim of glory overshadowing the mercy seat"). The mercy seat is associated with divine glory/presence. This connects to the presence/glory theme and potentially to holiness registries. The spatial-architectural dimension of mercy is unique to this term.

---

**G2436 hileōs — propitious, gracious, forgiving**
Primary sense: the *disposition* of being propitious — favorably inclined, gracious, forgiving. Single programme group: the propitious disposition of God in the new covenant ("I will be merciful toward their iniquities" — Heb 8:12). The term names the inner quality of God that makes propitiation operative — not the act or the mechanism but the settled divine disposition from which mercy flows.
**Classical note from LSJ:** Classical hileōs (and hileos) meant "favorable, propitious" — of gods who had been appeased. The NT use loses the "appeasement" dimension: God is hileōs not because he has been placated but because it is his nature. The disposition precedes the act.
**Cross-registry (2.0a):** Heb 8:12 quotes Jer 31:34 — the new covenant promise includes both mercy toward iniquities and sins no longer remembered. The pairing of mercy and forgetting-of-sin is a structural feature of the new covenant mercy. Connection to forgiveness (Reg 64) and memory/forgetting.

---

**G0462 anosios — unholy, impious**
Primary sense: unholy, profane, wicked — the inner character of the person outside covenant moral ordering. LSJ confirms classical opposition of hosios (divinely sanctioned) and anosios (its negation). Two NT occurrences: 1Ti 1:9 (catalogue of the lawless), 2Ti 3:2 (catalogue of end-times inner failure).
**Placement in mercy registry — question:** anosios names the absence of holiness, not the absence of mercy directly. Its presence here is through the holiness terms being part of the registry's vocabulary sweep. The session C word study's Section 4 correctly notes this as a peripheral term.
**Session C check:** Section 4 does not give anosios a full treatment — it is listed under holiness-related terms within the atonement complex. This is appropriate. No correction needed.

---

**G3743 hosiōs — devoutly, in a holy manner**
Primary sense: the adverb of hosios — devoutly, in a manner characterised by inner holiness and faithfulness to God. Single occurrence: 1Th 2:10 ("holy and righteous and blameless was our conduct"). Extracted_thin. LSJ confirms hosios as "hallowed, sanctioned by divine or natural law" — the positive counterpart to anosios.
**Placement in mercy registry:** Like anosios, this term enters the registry through the holiness-vocabulary sweep. Its one group (3181-001) names devout holiness as an inner character quality. The connection to mercy is indirect — holiness and mercy are co-requisites of the covenantal character (Luk 1:75 pairs hosios and dikaios as the shape of the redeemed life before God).
**Cross-registry (2.0a):** 1Th 2:10's triple description (holy, righteous, blameless) is a compressed inner-being character summary. The pairing of holiness with righteousness as the description of the apostolic character connects to righteousness/justice registries.

---

### Hebrew atonement-covering family

**H3722A kip.per — to atone, to cover, to make reconciliation**
Primary sense: to cover over, pacify, propitiate; to atone for sin — the Piel stem is the workhorse form. BDB senses distinguish: (1a1) cover over/pacify/propitiate (relational appeasement); (1a2) cover over/atone for sin (moral-cultic); (1a3) atone for sin and persons by legal rites (institutional). The Pual passive "to be atoned for" and Hithpael "to be covered" complete the picture. Three groups: (1) priestly ritual atonement; (2) God's direct act of forgiving/covering; (3) interpersonal appeasement/covering of relational offence.
**Critical semantic observation:** The three groups reveal that kip.per operates across three distinct registers simultaneously — ritual/cultic, direct divine, and interpersonal. No other term in the registry is this structurally broad. The "covering" metaphor unifies all three: guilt/offence is covered rather than exposed.
**has_causative_stem = 1 confirmed:** The Piel/Pual alternation means kip.per can name both the act of atoning (causative — someone causes atonement to happen) and the state of being atoned for (passive — the person is covered). This is foundational to understanding how mercy operates structurally.
**Cross-registry (2.0a):** Psa 78:38 — "he, being compassionate, atoned for their iniquity and did not destroy them; he restrained his anger." This verse encodes the sequence: inner compassion (rachum) → act of atonement (kip.per) → restraint of anger. The mercy-atonement-wrath triangle is structurally encoded here. Connection to anger/wrath registries (Reg pool1-anger-pair).
**SD pointer captured:** Psa 78:38 shows that kip.per is driven by rachum (compassion). The atonement act is not mechanistic but arises from an inner disposition of mercy. Session D should examine whether this causal chain — inner mercy → atoning act — is consistent across the OT atonement corpus.

---

**H3722B ka.phar — to cover (with pitch)**
Primary sense (Qal): to coat or cover with pitch — the physical base meaning of the kap.har root. Single verse in programme corpus (same anchor verses as H3722A due to shared verse records). Extracted_thin. Three groups matching H3722A's groups — this appears to be a root-form variant that shares the verse classification.
**Analytical note:** H3722B's presence as a separate extracted term alongside H3722A reflects the STEP extraction capturing the root's most primitive usage. The term itself adds etymological depth (the "covering" metaphor is literal before it is theological) but contributes no independent inner-being analysis beyond what H3722A covers.
**meaning_numbered update:** Not required — the single prose sense accurately captures the physical covering meaning. The theological significance flows through H3722A.

---

**H3724A ko.pher — ransom, price of a life**
Primary sense: "price of a life, ransom, bribe" — the substitutionary payment that covers the moral accountability for life before God or human authority. Two groups: (1) ransom as substitutionary price — Job 33:24 ("I have found a ransom"), Psa 49:7 ("no man can ransom another"); (2) bribe as illicit covering — 1Sa 12:3 (bribe that blinds the moral vision).
**Semantic tension identified:** The same root can name both the legitimate ransom (life-covering payment before God) and the illegitimate bribe (payment that corrupts moral vision). This polarity is analytically significant: covering can restore justice (ransom) or corrupt it (bribe). The moral character of the covering depends on whether it is directed toward legitimate moral accountability or away from it.
**Cross-registry (2.0a):** Psa 49:7 — "truly no man can ransom another, or give to God the price of his life." This verse negates the human capacity for self-ransom. The impossibility of self-redemption is a structural feature of the mercy vocabulary — mercy is required precisely because no self-generated ransom exists. Connection to redemption/atonement and to human limitations before God.

---

**H3725 kip.pu.rim — atonement (Day of Atonement)**
Primary sense: atonement — specifically the plural noun naming "atonements" and by metonymy the Day of Atonement (Yom Kippurim). Eight occurrences, exclusively in Leviticus and Numbers. One group: the formal atonement institution as the annual structure addressing Israel's collective moral condition.
**Semantic contribution:** This term names atonement as an *institution* — the structured, recurring, communal act — rather than as an individual event. It is the most institutional term in the registry. The Day of Atonement is not a one-time provision but an annual repetition that acknowledges the ongoing corporate need for mercy-covering.
**Cross-registry (2.0a):** The annual repetition of Yom Kippurim is contrasted in Heb 10 with the once-for-all sacrifice of Christ. The "once vs. annual" structure encodes something about the adequacy vs. inadequacy of the covering — a theme that crosses the atonement and forgiveness registries.

---

**H3727 kap.po.ret — mercy seat**
Primary sense: the golden cover of the ark of the covenant — the specific location where God's presence meets human representation and propitiation is effected. BDB senses make the spatial and theological dimensions explicit: it is simultaneously the physical cover (slab of gold, specified dimensions), the location of divine speech (Exo 25:22 — "from above the mercy seat I will speak"), and the locus of atonement blood-sprinkling (Lev 16:14).
**Critical semantic observation:** kap.po.ret is the only term in this registry that names mercy as a *place*. All other terms name dispositions, acts, or qualities. The mercy seat is where mercy is enacted spatially — it has an address. This makes it structurally unique. The DIM-111-SD001 research flag correctly identifies the mercy seat as one pole of the mercy polarity (mercy granted at the seat vs. mercy withdrawn in Lo-Ruhamah).
**Cross-registry (2.0a):** Exo 25:22 — God speaks from above the mercy seat. The place of mercy is also the place of divine communication. The mercy seat is where God's voice is heard. Connection to the word/revelation and to the presence-of-God themes. Also: Heb 9:5 places the mercy seat in the context of the tabernacle's spatial theology — the mercy seat is in the most holy place, accessible only once a year. The restriction of mercy-seat access maps the human condition before the new covenant.

---

**H3819 Lo-Ruhamah — No Mercy**
Primary sense: a proper name — "she who has not received mercy" — given to Hosea's daughter as a prophetic sign-act (Hos 1:6). The name encodes God's withdrawal of womb-love (rachamim) from covenant-breaking Israel. One group: the prophetic withdrawal of divine compassion — the name embodies God's inner-being relational stance of withheld mercy.
**Semantic boundary observation:** Lo-Ruhamah is the only proper name functioning as a programme term. Its analytical value is not lexical but theological-structural: it names the negative pole of mercy. The meaning is entirely dependent on the root racham (womb-love), of which it is the negation. Its inclusion is justified by RD-PC-001 — the name is a gear in the mercy-machine.
**Session C check:** Section 3 annotation correctly notes the Lo-Ruhamah / mercy-seat polarity. Confirmed. The reversal in 1Pe 2:10 (those who were "not pitied" now "have received mercy") is the New Testament redemption of this name. The annotation handles this well.

---

**H5750 od — still, yet, again**
Primary sense: a particle/adverb meaning "still, yet, continuing, again, besides." Two groups in this registry: (1) persistence and turning — duration of inner moral orientation under affliction or stubbornness; (2) the ongoing character of a divine inner disposition — God's sustained relational stance.
**Analytical concern confirmed:** This is a high-frequency grammatical particle (493 occurrences). Its placement as an owner extracted term in the mercy registry reflects the VC classification identifying specific instances where od functions to name the *continuance* of an inner orientation — moral persistence (Job 2:3 — "he still holds fast his integrity") or divine sustained disposition (Hab 2:3; Isa 5:25 — "his hand is stretched out still").
**Assessment:** The two groups are coherent and the anchor verses justify the inclusion — the continuance/persistence function of od can name something genuinely relevant to the inner life. However, this is not mercy vocabulary per se; it is a modifier that qualifies the duration of mercy-related inner states. Its presence adds a temporal dimension to the registry that no other term carries.
**meaning_numbered update:** The full sense structure is already present in the parsed senses. No update required.
**Cross-registry (2.0a):** Job 2:3 — "he still holds fast his integrity, although you incited me against him to destroy him without reason." The word od here names the *persistence* of inner moral character under external assault. This connects to perseverance/integrity registries and to the suffering vocabulary.

---

**H2603A cha.nan — to be gracious, show favour**
Primary sense: to be gracious, to show favour, to extend compassionate favour toward one who has no claim on it. The stem structure is analytically rich: Qal (show favour — giver's perspective), Niphal (be pitied — recipient's perspective), Piel (make gracious/favourable), Poel (direct favour to), Hophal (be shown favour), Hithpael (seek favour, implore). The has_causative_stem=1 flag is correct.
**Critical observation:** The Hithpael ("to seek favour, implore favour") means that cha.nan names both the granting of grace and the seeking of it. The supplicant's cry uses the same verb root as God's gracious turning. Human supplication and divine grace are lexically unified in this term — the cry for mercy and the mercy itself share a root. This is not coincidental: the human posture of seeking grace is shaped by and oriented toward the divine posture of giving it.
**Cross-registry (2.0a):** The related words include "beauty, favour, Hen, Hannah, Hanun" — the proper names derived from chen/chanan are people whose names mean "favoured" or "gracious." This is the personal dimension of grace vocabulary — people named after what they received (Hannah = "graced"). Session D: does the naming practice encode something about the identity-formation dimension of received grace/mercy?
**CHANAN/CHEN root code collision noted from CI-002:** cha.nan (H2603A) in Reg 111 carries root code CHANAN; grace (Reg 68) uses CHEN for the same etymological family. This suppresses the cross-registry root signal. Captured as programme-level item.

---

**H2604 cha.nan — to show favour (Aramaic)**
Primary sense: Aramaic cognate of H2603A — P'al (show favour) and Ithpael (implore favour). Only 2 occurrences. One group: mercy shown in moral action and the plea of prayer (Dan 4:27 — showing mercy to the oppressed; Dan 6:11 — making petition).
**Semantic contribution:** The Aramaic form confirms the cha.nan root's operation in the Aramaic corpus (Daniel). Dan 4:27 is analytically notable: Nebuchadnezzar is counselled to "break off your iniquities by practicing righteousness, and your iniquities by showing mercy to the oppressed." Mercy-to-oppressed is here presented as the practical moral equivalent of repentance.
**Cross-registry (2.0a):** Dan 4:27 — mercy to the oppressed as a form of practical righteousness. This encodes a mercy-righteousness structural equivalence in the prophetic tradition. Connection to righteousness registries.

---

**H6279 a.tar — to pray, entreat, supplicate**
Primary sense: to pray, entreat, supplicate — with causative stem (Hiphil: to make supplication, plead). Two groups: (1) intercessory prayer — pleading with God on behalf of another; (2) personal prayer — the inner act of bringing one's own need and receiving divine response. The has_causative_stem=1 flag is correct.
**Semantic contribution:** a.tar is the most action-oriented prayer term in the registry. Its root connection to a.tar (odour/incense, H6282B) is etymologically noted but the inner-being content flows entirely through the prayer meaning. The Niphal (to be supplicated, to be entreated) names God as one who responds to supplication — the term describes a responsive relationship, not a one-way act.
**Session C check:** The earlier Session C flag noted H6282A (worshiper) and H6282B (odour) as correctly deleted. Both share the ATAR root code. The prayer meaning is fully carried by H6279 alone. Confirmed.
**Cross-registry (2.0a):** 2Ch 33:13 — Manasseh prays and "God was moved by his entreaty." The a.tar prayer produces a divine inner movement (vayē.cha.ter lo — God was entreated for him). This encodes prayer as an act that moves God's inner disposition. The effectiveness of prayer is framed as God being moved — connecting to the divine inner life and responsiveness themes.

---

**H7359 ra.cha.min — compassion (Aramaic)**
Primary sense: compassion — Aramaic cognate of Hebrew rachamim (H7356B), which derives from rechem (womb). Single occurrence in programme (Dan 2:18 — seeking mercy from the God of heaven). The related words include "womb, compassion, Rehum" — the womb-connection is explicit in the etymology.
**Semantic observation:** The womb etymology is the most somatic of all the mercy terms. ra.cha.min/rachamim names compassion as originating in the visceral, protective, intimate care a mother has for the child she has carried. The plural form suggests not a single act but the total compassionate inner disposition. Dan 2:18 uses it as "mercy from God of heaven" — the most intimate human relational image applied to the cosmic God.
**Somatic confirmation:** The womb etymology makes this term the primary candidate for SOMATIC_INNER_LINK. The body-part (womb/rechem) is the etymological source of the inner disposition. Directive for Pass 4: SOMATIC flag for H7359. Captured for DIR-002.
**Cross-registry (2.0a):** The womb imagery grounds divine compassion in maternal experience. Isa 49:15 ("Can a woman forget her nursing child, that she should have no compassion on the son of her womb?") — not an anchor verse here but a key verse for the womb-compassion theme shared with Reg 23 (compassion). Session D: does the racham/rechem root encode a maternal image of God that crosses mercy, compassion, and love registries?

---

**H8467 te.chin.nah — supplication for favour**
Primary sense: "supplication for favour" — the noun derived from cha.nan naming the act of earnest pleading for grace. Two senses: (1) favour (the thing sought); (2) supplication for favour (the act of seeking). Two groups: (1) supplication to God — from recognition of one's own need and God's disposition to hear; (2) supplication to human authority — the humble inner posture of plea before one with power over life.
**Semantic observation:** te.chin.nah is the most structured of the supplication terms — it names both the content of the request (favour) and the act of requesting (supplication). Its derivation from cha.nan means it is specifically "graciously-favour-seeking" — the supplicant knows what they are asking for and knows who can give it.
**The two groups reveal a structural parallel:** supplication to God (Dan 9:20, 1Ki 8:38) and supplication to human authority (Jer 37:20) use the same word because the inner posture is structurally identical — the person without power pleads with the person who has it. The theological form and the social form are lexically unified.
**Cross-registry (2.0a):** 1Ki 8:38 — "each knowing the affliction of his own heart and stretching out his hands toward this house." te.chin.nah arises from self-knowledge of inner affliction. The supplicant who comes in true te.chin.nah knows their own inner condition. This connects to self-knowledge/conscience registries.

---

### Pass 1 — Semantic synthesis

**The four semantic families of this registry:**

1. **Mercy-compassion** (eleos/eleeō/eleēmōn + oiktirmos/oiktirmōn + ra.cha.min): The core mercy vocabulary — feeling and acting toward those in need. The Greek family names mercy as moral quality, act, and character disposition. The Aramaic ra.cha.min names it as womb-love. The semantic boundary between mercy and compassion is not sharp — the terms overlap and the eleos/oiktirmos distinction is one of degree (eleos = moral mercy-in-action; oiktirmos = visceral compassionate feeling preceding action).

2. **Propitiation-atonement** (hilaskomai/hilasmos/hilastērios/hileōs + kip.per/ka.phar/kap.po.ret/kip.pu.rim/ko.pher): The structural mechanism of mercy — the vocabulary describing how mercy operates in the presence of guilt. The Greek family names the act (hilaskomai), the provision (hilasmos), the locus (hilastērios), and the disposition (hileōs). The Hebrew family names the act (kip.per), the means (ko.pher/ransom), the institution (kip.pu.rim), and the spatial locus (kap.po.ret). Together they describe mercy not as sentiment but as a structured response to the moral condition.

3. **Grace-favour** (cha.nan/cha.nan Aramaic + te.chin.nah): The relational dimension of mercy — favour freely extended to one with no claim, and the human act of seeking it. The cha.nan family is the most relational of the mercy vocabulary: the same root names both the giving and the seeking of grace, encoding the divine-human relational dynamic in a single lexical family.

4. **Negation and persistence** (aneleēmōn/anileōs + anosios + Lo-Ruhamah + od): The boundary terms — what mercy is not (mercilessness, unholiness, withdrawn mercy) and the temporal dimension of how it operates (persistence, continuation). These terms define the edges of the mercy concept by naming its absence and its duration.

**Key semantic tension identified in Pass 1:** The registry contains two distinct analytical layers — mercy as inner disposition/character quality, and atonement as the structural mechanism that makes mercy possible in the presence of guilt. Session B finding DIM-111-001 correctly identifies this tension. The question for Pass 3 and Stage 2 analysis: are these two layers one characteristic or two? The programme's inclusion of both under "mercy" is analytically defensible (mercy requires a structure to operate where guilt exists), but the distinction must be maintained in the word study.

**meaning_numbered directives generated this pass:**
- DIR-MEAN-001: G2433 hilaskomai — the middle/passive distinction and classical-to-NT direction reversal warrant structured senses. Current prose sense inadequate.

**Session C check — Pass 1:** Sections 1 and 2 of the word study are confirmed accurate. The four-family structure is present in the narrative. The atonement-as-mechanism observation in DIM-111-001 is present in Section 3 annotations. No corrections required at this stage.

---

PASS 1 COMPLETE
Date: 2026-04-11
All 25 owner active non-delete terms read. Semantic picture established. Session C confirmed accurate.
Directives captured: DIR-MEAN-001 (G2433 meaning_numbered update). DIR-001 (GOD_AS_SUBJECT flags) and DIR-002 (SOMATIC flags) updated with Pass 1 findings.
SD pointers raised: mercy-justice structural relationship (Jam 2:13 / Mat 23:23); mercy cry and perseverance; love-mercy causal chain (1Jo 4:10); kip.per driven by racham (Psa 78:38); ra.cha.min womb imagery cross-registry; prayer moves divine inner disposition (2Ch 33:13).
Observations log version increments to v1.2 at this boundary.


---

## STAGE 2 — PASS 2: DIVINE DIMENSION

**Date:** 2026-04-11

### Divine involvement pattern

**Dominant subject = GOD groups (from dimension_index):**
G1653 group 981-001 | G1656 group 983-001 | G2434 group 3177-001 | G2436 group 3166-001
H3722A group 3169-002 | H3722B group 3173-002 | H3819 group 986-001 | H5750 group 990-002
H7359 group 988-001

**Dominant subject = NONE (both/either/divine-human meeting):**
G1655 group 3164-001 | G2435 group 991-001 | G3628 group 992-001 | G3629 group 3158-001
H2603A group 984-001 | H3727 group 982-001

**Pattern established:** God is the primary actor or co-actor in 15 of 36 owner dimension groups. The divine dimension is not peripheral — it is constitutive of the mercy vocabulary. The dominant pattern across these groups is:

1. **God as originator of mercy** — eleos, oiktirmos, ra.cha.min all name mercy as God's *defining inner attribute* before they name it as a human quality. God is "rich in mercy" (Eph 2:4), "Father of mercies" (2Cor 1:3), "compassionate and merciful" (Jam 5:11). The human characteristic is derivative.

2. **God as sovereign in mercy** — Rom 9:15 ("I will have mercy on whom I will have mercy") places mercy explicitly within divine sovereignty. Mercy is not owed; it is freely extended. This is the strongest statement of mercy as divine prerogative in the registry.

3. **God as provider of the atonement mechanism** — 1Jo 4:10 encodes the critical reversal: "not that we loved God but that he loved us and sent his Son to be the propitiation." God provides what the human needs to receive mercy. The act of mercy includes providing its own structural mechanism.

4. **God as the one who withholds mercy** — Hos 1:6 (Lo-Ruhamah) and Isa 5:25 (hand stretched out still in judgment) — God's withdrawal of mercy is as theologically intentional as its extension. Mercy is not automatic; its withdrawal is a judicial act.

5. **God as the one whose inner disposition is sustained** — od in group 990-002 names the *persistence* of divine inner disposition — both in judgment (Isa 5:25) and in faithful vision awaiting fulfilment (Hab 2:3). God's inner relational stance is characterised by duration.

**Divine-human relationship classification:** Mercy in this registry is **derivative and responsive** — human mercy derives from divine mercy and is a response to it (Luk 6:36: "be merciful as your Father"). It is not parallel (humans and God independently possess mercy) but typological and participatory (human mercy participates in and reflects divine mercy).

**Eschatological dimension:** No ESCHATOLOGICAL_USAGE phase2 flags are present on any owner active term. However, eschatological content is present in the anchor verses: 1Jo 2:2 ("propitiation...not for ours only but also for the sins of the whole world"), Heb 8:12 (new covenant — sins remembered no more), 1Pe 2:10 (those who were Lo-Ruhamah now receive mercy). The eschatological dimension of mercy is the reversal of the mercy-withdrawal condition: what was "no mercy" becomes "mercy received." This should be flagged for the word study Section 3 update.

**FRAMEWORK_SIGNAL phase2 flags:** Given that God is the primary actor in mercy at every structural level (origin, provision of mechanism, sovereign extension, judicial withdrawal), FRAMEWORK_SIGNAL flags are warranted for the core terms where the divine-human relationship directly shapes the spirit-soul-body classification. Specifically: G1656 eleos (mercy originates at the spirit level — received from God), G2433/G2434/G2435 propitiation family (divine provision, not human achievement), H3727 kap.po.ret (divine meeting point — the mercy location is divinely designated). Captured for DIR-002.

**GOD_AS_SUBJECT mti_term_flags directive — finalised list:**

Based on Pass 2 analysis confirming dominant_subject=GOD or NONE-with-divine-primary:

| Term | Basis |
|---|---|
| G1653 eleeō | group 981-001 dominant_subject=GOD |
| G1656 eleos | group 983-001 dominant_subject=GOD |
| G2434 hilasmos | group 3177-001 dominant_subject=GOD |
| G2436 hileōs | group 3166-001 dominant_subject=GOD |
| G3628 oiktirmos | group 992-001 — "Father of mercies" — GOD primary even with NONE label |
| G3629 oiktirmōn | group 3158-001 — "The Lord is compassionate and merciful" — GOD primary |
| H2603A cha.nan | group 984-001 — God's gracious turning (Num 6:25) — GOD primary |
| H3727 kap.po.ret | group 982-001 — "I will meet with you from above the mercy seat" — GOD primary |
| H3819 lo-ruhamah | group 986-001 dominant_subject=GOD |
| H5750 od | group 990-002 dominant_subject=GOD |
| H7359 ra.cha.min | group 988-001 dominant_subject=GOD |
| H3722A kip.per | group 3169-002 dominant_subject=GOD |
| H3722B ka.phar | group 3173-002 dominant_subject=GOD |

All 13 confirmed. Captured as updated DIR-001 for D1 delivery after Pass 3.

**Session C check — Pass 2:** Sections 1 and 2 correctly state that God is primary actor and source of mercy. "At its source level, mercy in Scripture is not primarily a human achievement" (Section 2) — confirmed. The derivative-and-responsive classification is implicit in the text; it should be made explicit in the v2 update.

**Cross-registry — Pass 2 additional SD pointers:**
- Rom 9:15 — "I will have mercy on whom I have mercy, and I will have compassion on whom I have compassion." The pairing of eleeō and oiktirō in divine sovereignty context encodes mercy and compassion as parallel expressions of the same divine prerogative. Session D: are mercy and compassion structurally synonymous at the divine level, or does one precede the other?
- Eph 2:4 — "God, being rich in mercy, because of the great love with which he loved us." Divine mercy is explicitly grounded in divine love. The causal chain: love → mercy is stated. Session D: does love cause mercy, or does mercy express love toward the undeserving specifically?
- Isa 5:25 — "his anger has not turned away, and his hand is stretched out still." od names the persistence of divine anger — mercy's opposite pole is also sustained. The same vocabulary of divine inner-disposition continuance applies to both mercy and wrath. Session D: do mercy and wrath share a structural feature (both sustained, both arising from divine inner character) that unifies them at a deeper level?

---

PASS 2 COMPLETE
Date: 2026-04-11
Divine dimension fully established. 13 GOD_AS_SUBJECT terms confirmed. DIR-001 finalised.
FRAMEWORK_SIGNAL flags added to DIR-002 scope.
SD pointers raised: mercy-compassion parallel sovereignty; love→mercy causal chain; mercy-wrath shared persistence structure.
Observations log version increments to v1.3 at Pass 3 boundary.


---

## STAGE 2 — PASS 3: VERSE ANNOTATIONS

**Date:** 2026-04-11
**Method:** All owner anchor verse groups read. Annotations written for each. Five standing questions applied. Session C flags noted. SD pointers raised on discovery.

---

### GROUP 3158-001 | G3629 oiktirmōn
**DESC:** Compassion as inner character of God and standard for human inner disposition — to be merciful as God is merciful.

REFERENCE: Jam 5:11
STRONG'S: G3629
CONTEXT GROUP: 3158-001
ANCHOR: yes
ANNOTATION: The verse pairs Job's steadfastness under suffering with the Lord's compassionate and merciful character (*oiktirmōn* and *polysplanchnos* — "compassionate" and "full of tender mercy"). The pairing is theologically purposive: the ground for endurance under suffering is the knowledge of God's inner character. James does not say God will remove suffering quickly; he says God is compassionate in the midst of it. The plural *polysplanchnos* ("many-splanchna") names the abundance of the inner movement of mercy — somatic language for the depth of divine feeling.
SESSION C FLAG: deepen — Section 1 mentions Jam 5:11 but does not surface the pairing of steadfastness and divine compassion as the theological ground for endurance. This connection belongs in the word study.
CROSS-REGISTRY (2.0a): Steadfastness (*hupomone*) as the companion virtue to mercy — endurance is possible because mercy is trusted. Connection to hope/perseverance registries.

REFERENCE: Luk 6:36
STRONG'S: G3629
CONTEXT GROUP: 3158-001
ANCHOR: yes
ANNOTATION: The divine-to-human pattern is stated with maximum compression: "Be merciful as your Father is merciful." God's mercy is the standard, the model, and the ground. The use of *oiktirmōn* (the adjective of compassionate character) rather than a mercy-in-action verb is deliberate — the call is not merely to perform merciful acts but to *be* compassionate as a person. The Greek parallel to the Sermon on the Mount (Mat 5:48 "perfect as your Father") suggests this verse names the character goal of the new humanity.
SESSION C FLAG: confirm — Section 1 correctly identifies Luk 6:36 as the key structural verse. Confirmed.
CROSS-REGISTRY (2.0a): "As your Father is merciful" — the imago Dei pattern. The call to reflect God's compassion is structurally identical to the call to reflect God's holiness (1Pe 1:16 "be holy as I am holy"). Does mercy belong to the same family of character-reflection commands as holiness? Session D to examine.

---

### GROUP 3164-001 | G1655 eleēmōn
**DESC:** Mercifulness as inner character quality — the blessed disposition of those who show mercy and the defining character of Christ as high priest.

REFERENCE: Heb 2:17
STRONG'S: G1655
CONTEXT GROUP: 3164-001
ANCHOR: yes
ANNOTATION: Christ becomes *eleēmōn* (the merciful person) through incarnation — "made like his brothers in every respect." The verse encodes a formation theory: merciful character is not innate but experientially produced through participation in vulnerability. The pairing with *pistos* (faithful) as the two co-requisite high-priestly qualities names mercy and faithfulness as structurally complementary. The high priest must be both — mercy without faithfulness would be indulgent; faithfulness without mercy would be harsh. The verse then immediately states the purpose: "to make propitiation" — the merciful character is the ground for the atoning act.
SESSION C FLAG: confirm — Section 3 annotation correct. Add the mercy-faithfulness pairing explicitly.
CROSS-REGISTRY (2.0a): The mercy-faithfulness pairing in the priestly context connects to faithfulness (Reg 60). Also: the "made like his brothers" — full human solidarity as the precondition for merciful priestly representation. Connection to vulnerability/weakness registries.

REFERENCE: Mat 5:7
STRONG'S: G1655
CONTEXT GROUP: 3164-001
ANCHOR: yes
ANNOTATION: The beatitude form addresses not acts but persons — "the *merciful*" (hoi eleēmones), the class of people for whom mercy is habitual character. The promise is structurally reciprocal: those who exercise mercy receive mercy. This is not strictly contractual — the passive "shall receive mercy" (eleeō passive) likely names divine mercy rather than human, suggesting that merciful character creates the receptivity for divine mercy. The eschatological register of the Beatitudes (future promise) gives this a forward-looking dimension absent from purely ethical readings.
SESSION C FLAG: deepen — Section 3 annotation handles the reciprocal structure but does not name the eschatological register of the Beatitude form.
CROSS-REGISTRY (2.0a): The Beatitude form connects all eight beatitudes structurally. The merciful are blessed in the same register as the pure in heart, the peacemakers, the poor in spirit. Is mercy in the same inner-being family as purity of heart and peace? Session D to examine whether the Beatitudes encode a coherent inner-being portrait.
SD POINTER: The Beatitudes as a structured inner-being portrait — do the eight characteristics form a coherent cluster? Session D.

---

### GROUP 3165-001 | G0415 aneleēmōn
**DESC:** Mercilessness as inner character failure — one of the marks of those whose inner moral fabric has collapsed.

REFERENCE: Rom 1:31
STRONG'S: G0415
CONTEXT GROUP: 3165-001
ANCHOR: yes
ANNOTATION: Paul's four-word catalogue: "foolish, faithless, heartless, ruthless" (*asunetos, asunthetos, astorgos, aneleēmōn*). The final term (*aneleēmōn*) names the relational failure — without mercy, uncompassionate. Its position as the terminal item in the catalogue is significant: mercilessness is the outer expression of the inner collapse named by the preceding terms. The person who is foolish (lost cognitive orientation), faithless (broken relational loyalty), and heartless (without natural affection) is, by extension, without mercy. The four terms together describe a person from whom every quality of inner life that makes human community possible has been stripped.
SESSION C FLAG: confirm and deepen — Section 3 annotation identifies the clustering correctly. Add: mercilessness as *terminal* in the catalogue — the relational face of the complete inner collapse.
CROSS-REGISTRY (2.0a): *Astorgos* (heartless/without natural affection) — a term that likely belongs to love or affection registries. Its co-occurrence with aneleēmōn in the same catalogue positions mercilessness and the absence of natural affection as companion failures. Session D: does the absence of mercy and the absence of natural affection share a structural root?
SD POINTER: Rom 1:31 as a multi-registry inner-being collapse catalogue — asunetos (wisdom/discernment), asunthetos (faithfulness/covenant), astorgos (love/affection), aneleēmōn (mercy). Each term implicates a different registry. Session D.

---

### GROUP 3166-001 | G2436 hileōs
**DESC:** The propitious disposition of God — the mercy that forgives iniquity and remembers sin no more under the new covenant.

REFERENCE: Heb 8:12
STRONG'S: G2436
CONTEXT GROUP: 3166-001
ANCHOR: yes
ANNOTATION: Heb 8:12 quotes Jer 31:34 — the new covenant promise. God will be *hileōs* toward iniquities and will remember sins no more. The term names the settled, sustained, propitious inner disposition that characterises God's stance toward covenant people under the new covenant. Two notes: (1) *hileōs* names a *disposition* not an act — God does not merely forgive; he is *disposed toward* forgiveness as his relational posture. (2) The forgetting of sins is relational, not cognitive — God commits to not holding against the person what could be held. The new covenant mercy is permanent and comprehensive.
SESSION C FLAG: confirm. Add: the distinction between disposition (hileōs) and act (hilaskomai) — mercy under the new covenant is a settled relational posture, not a repeated transaction.
CROSS-REGISTRY (2.0a): "I will remember their sins no more" — connects to memory/forgetting registries and to forgiveness (Reg 64). The mercy and forgiveness connection is causal: God's propitious disposition produces the forgetting-of-sins. Session D: is forgiveness the content of mercy, or its consequence?

---

### GROUPS 3169-001, 3169-002, 3169-003 | H3722A kip.per
**DESC:** Three groups — priestly ritual, divine direct act, interpersonal appeasement.

REFERENCE: Lev 17:11
STRONG'S: H3722A
CONTEXT GROUP: 3169-001
ANCHOR: yes
ANNOTATION: The principle: "the life of the flesh is in the blood, and I have given it for you on the altar to make atonement for your souls." Life (*nephesh*) addresses life (*nephesh*) — the blood carrying life makes atonement for the soul-life of the person. The verse states the mechanism: substitution (one life covering another) and divine provision ("I have given it for you"). The atonement is not a human invention but a divine provision designated for a specific purpose. The word *nephesh* (soul/life) connects the ritual act directly to the inner person.
SESSION C FLAG: confirm. Add: the *nephesh-for-nephesh* substitution principle — the atoning blood addresses the *nephesh* specifically. This is not merely physical; it is inner-being transaction.
CROSS-REGISTRY (2.0a): *Nephesh* appears here as the recipient of atonement. Connection to soul/nephesh registries. The blood-of-life vocabulary connects to flesh (Reg 185) and life/soul registries.

REFERENCE: Lev 4:20
STRONG'S: H3722A
CONTEXT GROUP: 3169-001
ANCHOR: yes
ANNOTATION: The formula "the priest shall make atonement for them, and they shall be forgiven" — atonement produces forgiveness as its stated outcome. The sequence is mechanical in form but relational in substance: the priestly act triggers divine forgiveness. The passive "they shall be forgiven" names divine action in response to the priestly ritual — God is the forgiver; the priest is the mediator. The verse confirms the connection between kip.per and forgiveness as cause and effect.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): Forgiveness (Reg 64) as the stated outcome of atonement. This is a formal data connection.

REFERENCE: Eze 16:63
STRONG'S: H3722A
CONTEXT GROUP: 3169-002
ANCHOR: yes
ANNOTATION: God atones directly ("when I atone for you for all that you have done") — bypassing the priestly mechanism. The context is Ezekiel's extended metaphor of Jerusalem as unfaithful bride: the mercy shown is to one who has been comprehensively faithless. The atonement produces shame ("you may remember and be confounded, and never open your mouth again"). This is the most psychologically precise description of the inner experience of receiving comprehensive atonement: not relief and celebration but silencing shame. The person who has been fully forgiven for the unforgivable has nothing to say.
SESSION C FLAG: confirm. The shame-as-response-to-mercy observation is in the Session C annotation and is confirmed here as analytically correct.
CROSS-REGISTRY (2.0a): Shame as the inner response to mercy received — connection to shame (Reg 146). The specific form of shame named here is not the destructive shame of condemnation but the reverent silence of the fully forgiven. This distinction is important for the shame registry.
SD POINTER: Does the shame vocabulary in Eze 16:63 represent a distinct category of shame — *mercy-induced shame* — that is structurally different from the shame of exposure or condemnation? Session D to examine with Reg 146.

REFERENCE: Psa 78:38
STRONG'S: H3722A
CONTEXT GROUP: 3169-002
ANCHOR: yes
ANNOTATION: "Yet he, being compassionate (*rachum*), atoned for their iniquity and did not destroy them; he restrained his anger often." The sequence is explicit: inner compassion (*rachum*) → atoning act → restraint of wrath. The atonement arises from God's inner character of compassion. Three further observations: (1) God "did not destroy them" — the negative form names mercy as the withholding of what was deserved; (2) "restrained his anger often" — mercy is not a single act but a sustained restraint; (3) the rachum term here is from the womb-love root — the deepest compassion vocabulary grounds the atoning act.
SESSION C FLAG: confirm and deepen — this verse is the strongest statement of the mercy → atonement causal sequence.
CROSS-REGISTRY (2.0a): Rachum (H7349) and ra.cha.min (womb-compassion) driving the atoning act — the somatic compassion vocabulary is the engine of propitiation. Connection between somatic mercy terms and the atonement complex is formally evidenced here. Also: "restrained his anger" — anger (Reg pool1-anger-pair) is restrained by mercy. This is a structural mercy-anger relationship.
SD POINTER: Psa 78:38 — rachum as the inner disposition that *produces* kip.per. Is the atonement mechanism an expression of divine compassion rather than an independent juridical structure? Session D.

REFERENCE: Deu 21:8
STRONG'S: H3722A
CONTEXT GROUP: 3169-003
ANCHOR: yes
ANNOTATION: The communal atonement formula — "accept atonement, O Lord, for your people Israel, whom you have redeemed." The bloodguilt of an unsolved murder is addressed through communal prayer invoking Israel's redemption as the basis for the petition. The atonement vocabulary here operates interpersonally/communally, not only individually or ritually. The appeal to "whom you have redeemed" grounds the request in a prior act of mercy — past mercy is invoked as the basis for present mercy.
SESSION C FLAG: add — Section 3 does not have an annotation for the communal/bloodguilt dimension of kip.per. The community's corporate moral condition before God is part of the mercy picture.
CROSS-REGISTRY (2.0a): The appeal to prior redemption as the ground for present mercy petition — mercy builds on mercy. Connection to redemption registries.

REFERENCE: Gen 32:20
STRONG'S: H3722A
CONTEXT GROUP: 3169-003
ANCHOR: yes
ANNOTATION: Jacob's plan to appease Esau — "I may appease him (*akhapper panav* — I will cover his face/appease him) with the present." The kip.per root in its most interpersonal and relational usage: covering an offence between persons, managing anticipated anger through gift. This usage reveals the root's secular base before its theological elevation. The covering of an offended face (panav = face/presence) is the literal image: mercy restores the ability to face the other person.
SESSION C FLAG: add — the face-covering imagery of interpersonal kip.per is not in the Session C word study. The literal "cover the face" meaning illuminates the theological usage.
CROSS-REGISTRY (2.0a): "See his face" (*panav*) — the restoration of face-access as the outcome of relational covering. Connection to the divine face/presence vocabulary (Num 6:25 "make his face shine upon you"). Mercy restores face-access whether between persons or between the person and God.
SD POINTER: Gen 32:20 and Num 6:25 share the face-vocabulary — covering the offended face (kip.per) and the face shining in grace (cha.nan). Is there a structural correspondence between interpersonal reconciliation-covering and divine gracious-shining that Session D should examine?

---

### GROUPS 3170-001, 3170-002 | H3724A ko.pher
**DESC:** Ransom (substitutionary price) and bribe (corrupting payment).

REFERENCE: Job 33:24
STRONG'S: H3724A
CONTEXT GROUP: 3170-001
ANCHOR: yes
ANNOTATION: "He is merciful to him and says, 'Deliver him from going down into the pit; I have found a ransom.'" The ransom (*ko.pher*) here is found by a divine/angelic mediator and cited as the ground for deliverance from death. The verse encodes: someone in peril of death → divine mercy → ransom found → deliverance. The mercy precedes and motivates the ransom; the ransom makes the mercy operative. This is a miniature of the propitiation structure: mercy drives the provision of the covering.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): Death/pit avoidance as the outcome of ransom — connection to life/death registries.

REFERENCE: Psa 49:7
STRONG'S: H3724A
CONTEXT GROUP: 3170-001
ANCHOR: yes
ANNOTATION: "Truly no man can ransom another, or give to God the price of his life." The impossibility of self-ransom or ransom-by-another is the foundation of the mercy argument: if no human can provide the ko.pher needed before God, then mercy must come from outside the human system entirely. The verse is not merely about money — it is about the structural incapacity of the human person to address their own standing before God. This incapacity is the anthropological premise that makes divine mercy necessary.
SESSION C FLAG: deepen — Session C Section 4 names this but the anthropological weight should be more explicit. The impossibility of self-ransom is the structural reason mercy must be received, not earned.
CROSS-REGISTRY (2.0a): Human incapacity before God — connection to vulnerability/dependence registries and to the Dependence/Creatureliness dimension.

REFERENCE: 1Sa 12:3
STRONG'S: H3724A
CONTEXT GROUP: 3170-002
ANCHOR: yes
ANNOTATION: Samuel's self-defence: "from whose hand have I taken a bribe to blind my eyes?" The ko.pher here is the corrupting payment that distorts the inner moral vision. The bribe *blinds* — it does not merely compromise the decision; it impairs the capacity to see rightly. The inner moral faculty (the eyes that should see justly) is corrupted by the corrupting ko.pher. This negative use of the ransom-root reveals its danger: the covering vocabulary can name either legitimate atonement (moral condition addressed) or illegitimate distortion (moral vision impaired).
SESSION C FLAG: add — the bribe usage of ko.pher and its inner-moral-vision consequence is not in the Session C word study.
CROSS-REGISTRY (2.0a): The inner moral vision (eyes, sight) as a facult that can be corrupted by money — connection to conscience/discernment registries and to the sin-vocabulary around bribery and justice.

---

### GROUP 3171-001 | H3725 kip.pu.rim

REFERENCE: Lev 23:27
STRONG'S: H3725
CONTEXT GROUP: 3171-001
ANCHOR: yes
ANNOTATION: The Day of Atonement (*Yom Kippurim*) — the commanded communal reckoning. "You shall afflict yourselves" (*anitem et nafshoteikhem* — you shall afflict your souls/lives) names the required inner participation: fasting as the outward form of inner affliction. The self-affliction is bodily but its target is the *nephesh* — the soul/inner life. The Day of Atonement is an annual structure that prevents Israel from ignoring the corporate inner-moral condition. The institution itself is an act of mercy: God provides the occasion and the mechanism.
SESSION C FLAG: deepen — the *nephesh*-affliction dimension of Yom Kippurim is not in the Session C annotation.
CROSS-REGISTRY (2.0a): Fasting as the somatic expression of inner affliction directed toward atonement — connection to fasting/mourning/grief registries. The self-affliction of the soul is a somatic inner-being act.
SD POINTER: Does the Day of Atonement's required self-affliction (*anitem et nafshoteikhem*) encode a structural relationship between somatic self-denial and inner moral renewal? Session D to examine across atonement, grief, and repentance registries.

---

### GROUPS 3173-001/002/003 | H3722B ka.phar
**DESC:** Same three groups as H3722A (sharing identical anchor verses). No new annotation required — the ka.phar groups are classified under the same verses as kip.per and the analysis applies equally. The distinction between H3722A and H3722B is at the level of stem morphology (H3722B is the Qal/physical covering usage); the VC groups correctly classify the shared verse evidence under both terms.

SESSION C FLAG: none — Section 4 handles this correctly.

---

### GROUPS 3176-001 | G2433 hilaskomai

REFERENCE: Heb 2:17
STRONG'S: G2433
CONTEXT GROUP: 3176-001
ANCHOR: yes
ANNOTATION: This verse is shared with G1655 (eleēmōn) but from the hilaskomai angle — Christ becomes merciful *in order to* make propitiation. The propitiation act (*hilaskomai* here in infinitive: "to make propitiation") is the functional purpose of his merciful character. The verb in this form names the active atoning work, not the receptive passive. The verse therefore encodes: incarnation → merciful character formed → propitiation made. The atoning act is the product of the merciful person.
SESSION C FLAG: confirm.

REFERENCE: Luk 18:13
STRONG'S: G2433
CONTEXT GROUP: 3176-001
ANCHOR: yes
ANNOTATION: The tax collector's cry: "God, be merciful to me (*hilasthēti moi*), a sinner." This is the *passive* of hilaskomai — "be propitious toward me, let propitiation be turned toward me." The somatic elements are dense: standing far off (spatial distance = moral distance), eyes not lifted to heaven (shame/unworthiness posture), chest-beating (self-identification with guilt). The man does not ask for anything specific — only that God's inner disposition turn toward him in the mercy-direction. The prayer is the most compressed expression of the entire mercy-structure: inner acknowledgement of need + somatic expression + appeal to divine mercy-disposition.
SESSION C FLAG: confirm. Section 3 annotation is accurate and handles the somatic elements. No correction needed.
CROSS-REGISTRY (2.0a): Luk 18:13 — the three somatic elements (distance, downcast eyes, chest-beating) appear together as a mercy-seeking posture. Are these elements of a coherent somatic vocabulary of supplication that appears across registries (prayer, repentance, humility)? Session D.
SD POINTER: The somatic posture of mercy-seeking in Luk 18:13 — spatial distance + downward eyes + breast-beating. Does this posture recur in the repentance and humility registries? Session D.

---

### GROUP 3177-001 | G2434 hilasmos

REFERENCE: 1Jo 2:2
STRONG'S: G2434
CONTEXT GROUP: 3177-001
ANCHOR: yes
ANNOTATION: "He is the propitiation (*hilasmos*) for our sins, and not for ours only but also for the sins of the whole world." Christ is identified *as* the hilasmos — not the one who performs it but the substance of it. The scope — "the whole world" — is the eschatological reach of the propitiation, extending mercy's structural provision universally. The verse makes no distinction between those who have received it and the world for whom it is provided — the provision is comprehensive; its reception is personal.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): "Not for ours only but also for the sins of the whole world" — universalism of provision vs. particularity of reception. Connection to election/calling and to the scope-of-salvation discussion that crosses multiple registries.

REFERENCE: 1Jo 4:10
STRONG'S: G2434
CONTEXT GROUP: 3177-001
ANCHOR: yes
ANNOTATION: "Not that we loved God but that he loved us and sent his Son to be the propitiation for our sins." The causal chain is explicit: divine love → sending of Son → propitiation provided. The propitiation is grounded in love, not in justice-satisfaction alone. The mercy-structure is motivated by love. This challenges any purely juridical reading of propitiation: the mechanism is legal but its motivation is relational and affective. The word "sent" (*apesteilen*) names the *cost* to God — sending his Son is not a neutral provision.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): Love (Reg 103) as the causal ground of mercy's structural mechanism. The propitiation is an act of love before it is an act of justice. This is a formal causal connection requiring Session D examination.
SD POINTER already captured from Pass 1: love → mercy causal chain. 1Jo 4:10 is the primary evidence.

---

### GROUP 3179-001 | G0462 anosios

REFERENCE: 1Ti 1:9
STRONG'S: G0462
CONTEXT GROUP: 3179-001
ANCHOR: yes
ANNOTATION: The law is "for the lawless and disobedient, for the ungodly and sinners, for the unholy and profane." The catalogue pairs anosios with *bebelos* (profane) — the one who violates the boundary between sacred and common. Unholiness in this list names the inner disposition of the person for whom the sacred/common boundary has been erased. The law is given not to form but to restrain — it assumes an inner moral condition that needs external governance.
SESSION C FLAG: add — this verse contributes to the picture of the conditions that require mercy (the inner state that needs atonement). Currently absent from Session C.
CROSS-REGISTRY (2.0a): The catalogue includes "those who strike their fathers and mothers, murderers" — the law is oriented against specific relational violations. Connection to honour/family and to conscience/law registries.

REFERENCE: 2Ti 3:2
STRONG'S: G0462
CONTEXT GROUP: 3179-001
ANCHOR: yes
ANNOTATION: The end-times catalogue: "lovers of self, lovers of money, proud, arrogant, abusive, disobedient to parents, ungrateful, unholy." Anosios here appears with *acharistos* (ungrateful) — the pairing is significant. Unholiness and ingratitude are companion failures in the eschatological moral collapse. Gratitude is the inner response to received mercy/grace; ingratitude names the failure to acknowledge received good. The person who is ungrateful and unholy has lost the relational capacities that mercy both requires and produces.
SESSION C FLAG: add — the ungrateful/unholy pairing and its connection to the inner response to mercy is a new observation for the word study.
CROSS-REGISTRY (2.0a): Ingratitude (*acharistos*) — this term connects to grace/gratitude registries. Ungratitude as the failure of the inner response to received grace/mercy.
SD POINTER: Gratitude as the inner response to received mercy — does the programme have a gratitude registry? If so, 2Ti 3:2's pairing of ingratitude and unholiness may encode a formal connection.

---

### GROUP 3181-001 | G3743 hosiōs

REFERENCE: 1Th 2:10
STRONG'S: G3743
CONTEXT GROUP: 3181-001
ANCHOR: yes
ANNOTATION: "Holy and righteous and blameless was our conduct toward you believers." The triple description (*hosiōs, dikaiōs, amemptōs*) names the apostolic character in terms of its moral quality before both God (*hosiōs* — divinely sanctioned holiness) and humans (*dikaiōs* — righteously, toward others). Devout holiness is here presented as observable through conduct — it is not merely an inner state but a publicly verifiable character. The triple formula suggests that holiness, righteousness, and blamelessness are not three separate qualities but three facets of integrated moral character.
SESSION C FLAG: add — the observable/verifiable dimension of inner holiness through conduct is not currently in the word study.
CROSS-REGISTRY (2.0a): Righteousness (*dikaiōs*) paired with holiness — the mercy-holiness-righteousness cluster that also appears in Luk 1:74-75 ("serve him in holiness and righteousness all our days").

---

### GROUP 981-001 | G1653 eleeō (divine sovereignty)

REFERENCE: Rom 9:15
STRONG'S: G1653
CONTEXT GROUP: 981-001
ANCHOR: yes
ANNOTATION: "I will have mercy on whom I have mercy, and I will have compassion on whom I have compassion." Paul quotes God's words to Moses (Exo 33:19). The repetition is not merely emphasis but theological precision: mercy is not distributed by any criterion external to God's own will. The pairing of *eleeō* and *oiktirō* (compassion) in divine sovereignty language equates them at the highest level — both are expressions of the same divine prerogative. The verse is Paul's proof-text for the non-meritocratic character of mercy: it cannot be claimed, only received.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): The pairing of *eleeō* and *oiktirō* in divine sovereignty — at the highest level, mercy and compassion are interchangeable expressions of divine freedom. This is the strongest evidence for treating mercy and compassion as a unified concept at the divine level. Session D.

REFERENCE: 1Pe 2:10
STRONG'S: G1653
CONTEXT GROUP: 981-001
ANCHOR: yes
ANNOTATION: "Once you were not a people, but now you are God's people; once you had not received mercy (*eleēmenoi*), but now you have received mercy." The verse directly reverses Lo-Ruhamah: those who were "not-pitied" are now "pitied/received-mercy." The before/after structure is identity-constituting — receiving mercy is what makes them "God's people." The community's identity is defined by having-received-mercy. Mercy received is not merely a benefit but an ontological status-change.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): The formal reversal of Lo-Ruhamah in the NT — the programmatic connection between H3819 (Lo-Ruhamah) and G1653 (eleeō) in this verse is the key cross-testament mercy polarity. This is the data for DIM-111-SD001. Confirmed.

---

### GROUP 981-002 | G1653 eleeō (cry for mercy)

REFERENCE: Luk 18:38
STRONG'S: G1653
CONTEXT GROUP: 981-002
ANCHOR: yes
ANNOTATION: "He cried out, 'Jesus, Son of David, have mercy on me!'" The blind man's cry is addressed to Jesus by messianic title — the mercy request is simultaneously a confession of faith. He identifies Jesus as the heir of David (the covenant king through whom mercy flows) before making the request. The cry is public, persistent (Mar 10:48 shows he repeated it despite rebuke), and precisely targeted. The mercy vocabulary here functions as the soteriological shorthand: to ask for mercy is to ask for the full restoration of the person.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): The messianic title "Son of David" in the mercy cry — the mercy request is directed toward Jesus as the covenant king. Connection to covenant (Reg 34) and to Davidic messianism.

REFERENCE: Mar 10:48
STRONG'S: G1653
CONTEXT GROUP: 981-002
ANCHOR: yes
ANNOTATION: "Many rebuked him, telling him to be silent. But he cried out all the more, 'Son of David, have mercy on me!'" The persistence under social pressure is the analytically significant element. The crowd's rebuke attempts to suppress the mercy cry; the blind man intensifies it. The mercy cry is here not a quiet interior prayer but a public act of persistent appeal that refuses to be silenced. The escalation ("all the more") names the quality of urgency in the mercy-seeker.
SESSION C FLAG: deepen — add the persistence-under-opposition dimension to the Section 3 annotation.
CROSS-REGISTRY (2.0a): Persistence in the mercy cry despite social opposition — connection to perseverance/hope registries. The mercy-cry and the perseverance-vocabulary may share structural features.

---

### GROUP 981-003 | G1653 eleeō (human act)

REFERENCE: Mat 18:33
STRONG'S: G1653
CONTEXT GROUP: 981-003
ANCHOR: yes
ANNOTATION: "Should not you have had mercy on your fellow servant, as I had mercy on you?" The logic of the parable is that received mercy should produce extended mercy. The rhetorical question assumes this is self-evident — the one who has been forgiven the greater debt should extend mercy for the lesser. The failure of the unmerciful servant is not merely moral but spiritual: mercy received but not integrated into character produces no transformation. The parable reveals that true reception of mercy changes the recipient's inner disposition toward others.
SESSION C FLAG: confirm. The word study handles this well.
CROSS-REGISTRY (2.0a): The unmerciful servant's failure: mercy received without inner transformation — connection to repentance registries and to heart/hardening vocabulary.

REFERENCE: Mat 5:7
STRONG'S: G1653
CONTEXT GROUP: 981-003
ANCHOR: yes
ANNOTATION: (Second occurrence of this anchor verse — already annotated under G1655 group 3164-001.) The same verse anchors both the adjective (eleēmōn — merciful as character) and the verb (eleeō — showing mercy as act). This double-anchoring confirms the integrity of the mercy vocabulary: being merciful (adjective) and showing mercy (verb) are not distinct activities but the same reality described from the character-perspective and the act-perspective.
SESSION C FLAG: note — Section 3 should acknowledge that Mat 5:7 anchors multiple terms.

---

### GROUP 982-001 | H3727 kap.po.ret

REFERENCE: Lev 16:14
STRONG'S: H3727
CONTEXT GROUP: 982-001
ANCHOR: yes
ANNOTATION: The Day of Atonement blood-sprinkling: "he shall sprinkle some of the blood with his finger on the front of the mercy seat on the east side, and in front of the mercy seat he shall sprinkle some of the blood with his finger seven times." The sevenfold sprinkling before the mercy seat is both liturgical precision and symbolic completeness — seven as the number of completeness means the covering is total and unreserved. The mercy seat is the specific target of the atoning blood: this is where guilt is addressed. The act is intensely physical — finger, blood, sprinkling, seven times — but its target is the relational standing of the people before God.
SESSION C FLAG: add — the sevenfold sprinkling and its completeness symbolism is not in the Session C word study. The somatic/physical intensity of the mercy-seat ritual is underplayed.
CROSS-REGISTRY (2.0a): The blood-as-life principle (Lev 17:11) and the blood-sprinkling ritual — connection to flesh (Reg 185) and to the sacrificial/priestly vocabulary.
SD POINTER: The sevenfold blood-sprinkling on the mercy seat as complete-covering — does the number symbolism of completeness appear across the atonement vocabulary and in the forgiveness registries? Session D.

REFERENCE: Exo 25:22
STRONG'S: H3727
CONTEXT GROUP: 982-001
ANCHOR: yes
ANNOTATION: "There I will meet with you, and from above the mercy seat...I will speak with you." The mercy seat is named as the locus of divine meeting and divine speech. Two observations: (1) meeting — the mercy seat is the designated meeting-point; access to God's presence is mercy-seat access; (2) speech — God speaks *from* above the mercy seat; divine communication is mercy-seat communication. The mercy seat is therefore not only the place of atonement but the place of relationship and revelation. Mercy is not only forgiveness of the past but the ground of ongoing relationship and communication.
SESSION C FLAG: deepen — the speech dimension of the mercy seat is not in the Session C annotation. The mercy seat as locus of divine revelation (not only atonement) is important.
CROSS-REGISTRY (2.0a): Divine speech from above the mercy seat — the mercy seat as the place where God's word is given. Connection to word/revelation registries. Mercy and revelation are structurally linked in the tabernacle architecture.
SD POINTER: The mercy seat as the locus of both atonement and divine communication — does mercy provide the structural ground for divine-human communication? Session D.

---

### GROUPS 983-001, 983-002 | G1656 eleos

REFERENCE: Eph 2:4
STRONG'S: G1656
CONTEXT GROUP: 983-001
ANCHOR: yes
ANNOTATION: "But God, being rich in mercy, because of the great love with which he loved us." The abundance of mercy (*plousios en eleei*) is grounded in love (*agapē*). The adversative "but" contrasts the human condition (dead in trespasses, children of wrath) with the divine action. The causal "because of the great love" names love as the motivation for mercy. Two structural observations: (1) mercy is abundant in character — it is not rationed; (2) love is its cause — mercy is love directed toward those in need/guilt. The love-mercy causal sequence is formally stated.
SESSION C FLAG: confirm.
CROSS-REGISTRY: love → mercy causal chain. Primary evidence for DIR SD pointer from Pass 1.

REFERENCE: Luk 1:78
STRONG'S: G1656
CONTEXT GROUP: 983-001
ANCHOR: yes
ANNOTATION: "Because of the tender mercy of our God (*splagchna eleos*), whereby the sunrise shall visit us from on high." The phrase *splagchna eleos* — "inner organs of mercy" or "tender mercy" — combines the somatic mercy root (splagchna = bowels/viscera as the seat of deep feeling) with eleos (mercy) into a compound expression of the most intimate divine compassion. The mercy is described as a sunrise — light arriving from above into darkness. Three dimensions: (1) somatic — mercy felt in the body's depths; (2) directional — from on high, visiting from above; (3) eschatological — the sunrise imagery names the dawning of the messianic age.
SESSION C FLAG: deepen — Section 3 annotation is good but does not name the compound splagchna-eleos as linguistically significant, nor the eschatological sunrise dimension.
CROSS-REGISTRY (2.0a): *Splagchna* as the most somatic mercy term — bodily interior as the location of compassion. Connection between G1656 and G3628 (oiktirmos) through the splagchna vocabulary.
SD POINTER: Luk 1:78 *splagchna eleos* as the intersection of bodily-mercy vocabulary and eschatological dawn imagery. Does the somatic mercy vocabulary systematically appear in eschatological contexts? Session D.

REFERENCE: Jam 3:17
STRONG'S: G1656
CONTEXT GROUP: 983-002
ANCHOR: yes
ANNOTATION: "Wisdom from above is...full of mercy (*mestē eleous*) and good fruits." Mercy is named as a constitutive quality of genuine wisdom — not an add-on to wisdom but an essential component. The phrase "full of mercy" is quantitative: wisdom is characterized by mercy in abundance. The association with "good fruits" connects mercy to visible outcomes — wisdom-mercy produces fruit. The verse positions mercilessness as a marker of false or earthly wisdom (cf. 3:14-16 on "earthly, unspiritual, demonic" wisdom).
SESSION C FLAG: confirm. Wisdom-mercy structural connection is in Section 3.
CROSS-REGISTRY (2.0a): Wisdom as mercy-full — connection to wisdom (Reg for wisdom/discernment). The absence of mercy in false wisdom (earthly/demonic) makes mercilessness a diagnostic marker of non-wisdom.

REFERENCE: Mat 23:23
STRONG'S: G1656
CONTEXT GROUP: 983-002
ANCHOR: yes
ANNOTATION: "You have neglected the weightier matters of the law: justice (*krisis*) and mercy (*eleos*) and faithfulness (*pistis*)." Jesus names three "weightier" inner-being qualities that outweigh the scrupulous tithing of minor items. The triad justice-mercy-faithfulness appears as a structural cluster — the heart of what the law is actually commanding. The term "weightier" (*barytera*) implies a hierarchy within the law itself. The fact that mercy appears alongside justice (not instead of it) is significant: mercy does not replace justice but operates with it.
SESSION C FLAG: confirm. The weightier-matters observation is in Section 3.
CROSS-REGISTRY (2.0a): The justice-mercy-faithfulness triad — three registries in one phrase. The triad structure may encode the core of covenantal character. Session D to examine whether this triad recurs across the prophetic literature (Mic 6:8 parallel: justice, mercy, humility).
SD POINTER: The Micah 6:8 / Matthew 23:23 parallel — "do justice, love mercy, walk humbly" vs. "justice, mercy, faithfulness." Does the programme's mercy registry connect formally to a justice-mercy-faithfulness/humility cluster that recurs in the prophetic and wisdom traditions? Session D.

---

### GROUP 984-001 | H2603A cha.nan

REFERENCE: Num 6:25
STRONG'S: H2603A
CONTEXT GROUP: 984-001
ANCHOR: yes
ANNOTATION: "The Lord make his face to shine upon you and be gracious to you." The Aaronic blessing invokes divine graciousness (*cha.nan*) as the content of the shining face. Three structural elements: (1) the shining face — divine favour expressed as light directed toward the person; (2) be gracious — the inner disposition of favour extended; (3) the priestly pronouncement — mercy is declared over the congregation, not merely requested. The blessing is an authoritative speech-act that invokes God's gracious disposition. The face-shining vocabulary connects cha.nan to the presence-of-God vocabulary in a formal way.
SESSION C FLAG: confirm. The face-vocabulary connection is present in Section 3.
CROSS-REGISTRY (2.0a): Face-shining as the spatial metaphor for divine grace — connection to God's presence/glory vocabulary and to the face/presence (panim) registries.

REFERENCE: Psa 51:1
STRONG'S: H2603A
CONTEXT GROUP: 984-001
ANCHOR: yes
ANNOTATION: "Have mercy on me, O God, according to your steadfast love (*chesed*); according to your abundant mercy (*rachamim*) blot out my transgressions." Three mercy-terms in one verse: cha.nan (the cry for grace), chesed (the steadfast love appealed to), rachamim (the abundant mercies invoked). The supplicant addresses God using the full mercy vocabulary as the ground of appeal — three different registers of mercy simultaneously invoked. The verse is the most condensed statement of mercy-seeking in the OT and formally links the cha.nan, chesed, and rachamim vocabulary families.
SESSION C FLAG: deepen — Section 3 has an annotation for Psa 51:1 but does not name the three-mercy-term concentration as analytically significant.
CROSS-REGISTRY (2.0a): Psa 51:1 as a three-registry convergence point — cha.nan (grace/mercy), chesed (steadfast love — Reg 103 and 99), rachamim (compassion — Reg 23). The verse formally connects mercy to love and compassion in a single supplication. This is the primary cross-registry evidence for the mercy-love-compassion cluster.
SD POINTER already captured: Psa 51:1 as three-registry convergence.

---

### GROUPS 985-001, 985-002 | H8467 te.chin.nah

REFERENCE: Dan 9:20
STRONG'S: H8467
CONTEXT GROUP: 985-001
ANCHOR: yes
ANNOTATION: "While I was speaking and praying, confessing my sin and the sin of my people Israel, and presenting my plea (*te.chin.nah*) before the Lord." Daniel's supplication is accompanied by confession — the te.chin.nah arises in the context of moral self-awareness. The plea is both personal (my sin) and communal (my people). The temporal detail "while I was speaking" names the activity as continuous — the supplication is not a single moment but a sustained disposition of prayer. The *te.chin.nah* here names the innermost appeal directed toward God in a posture of acknowledged need.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): Confession accompanying supplication — the inner act of moral self-acknowledgement as the ground of the mercy appeal. Connection to confession/repentance registries.

REFERENCE: 1Ki 8:38
STRONG'S: H8467
CONTEXT GROUP: 985-001
ANCHOR: yes
ANNOTATION: "Whatever prayer, whatever plea (*te.chin.nah*) is made by any man...each knowing the affliction of his own heart and stretching out his hands toward this house." Three elements: (1) self-knowledge — "knowing the affliction of his own heart" (*yada et nega levavo*) — the supplicant knows their own inner condition; (2) somatic — "stretching out his hands toward this house" — physical gesture of appeal directed toward the mercy seat location; (3) orientation — toward "this house" = toward the mercy seat within. The supplication is constituted by inner self-knowledge, outward physical gesture, and theological orientation toward the locus of mercy.
SESSION C FLAG: deepen — the inner self-knowledge (*yada et nega levavo*) as the prerequisite for te.chin.nah is not in the Session C annotation. Add: supplication presupposes inner self-knowledge.
CROSS-REGISTRY (2.0a): "Knowing the affliction of his own heart" — self-knowledge as a precondition for authentic mercy-seeking. Connection to self-knowledge, conscience, and heart-examination registries.
SD POINTER: Does authentic supplication require prior self-knowledge of inner condition? 1Ki 8:38 suggests yes. Session D to examine whether mercy-seeking vocabulary consistently involves inner self-awareness.

REFERENCE: Jer 37:20
STRONG'S: H8467
CONTEXT GROUP: 985-002
ANCHOR: yes
ANNOTATION: "Let my humble plea (*te.chin.nah*) come before you...do not send me back to the house of Jonathan the secretary, lest I die there." Jeremiah's plea to the king is formally identical in structure to supplication to God — the person without power appeals to the person with power over their life. The te.chin.nah directed to human authority uses the same inner posture as the te.chin.nah directed to God: recognition of the other's power and one's own dependence. The verse reveals that the mercy vocabulary is not exclusively theological — it names a structural dynamic of vulnerability and petition that operates at the human level as well.
SESSION C FLAG: add — the formal equivalence of supplication to God and supplication to human authority through the same te.chin.nah vocabulary is not in the Session C word study.
CROSS-REGISTRY (2.0a): The structural equivalence of dependence before God and dependence before human authority — connection to power/authority registries and to the vulnerability/dependence vocabulary.

---

### GROUP 986-001 | H3819 lo-ruhamah

REFERENCE: Hos 1:6
STRONG'S: H3819
CONTEXT GROUP: 986-001
ANCHOR: yes
ANNOTATION: "Call her name No Mercy (*Lo-Ruhamah*), for I will no more have mercy (*racham*) on the house of Israel, to forgive them at all." The name embodies a divine judicial act: mercy withdrawn as covenant consequence. The root *racham* (womb-love) is negated — the most intimate mercy vocabulary is inverted to name the most severe relational withdrawal. The phrase "to forgive them at all" (*nasa*) names what mercy normally produces — forgiveness; its absence names what judgment without mercy means. The naming of the child is a prophetic sign-act: the child's existence makes God's relational stance visible.
SESSION C FLAG: confirm. Section 3 annotation is accurate.
CROSS-REGISTRY (2.0a): The inversion of womb-love — the racham root's negation. The connection between Lo-Ruhamah and the mercy reversal in 1Pe 2:10 is the formal NT redemption of this name. Already captured as DIM-111-SD001.

---

### GROUPS 987-001, 987-002 | H6279 a.tar

REFERENCE: 2Ch 33:13
STRONG'S: H6279
CONTEXT GROUP: 987-001
ANCHOR: yes
ANNOTATION: "He prayed to him (*yē.cha.ter*), and God was moved by his entreaty (*vayē.cha.ter lo*) and heard his plea." The same root appears in both subject positions: Manasseh prays (*a.tar*), and God is *entreated/moved* (Niphal of a.tar). The prayer of the supplicant produces a movement in God — he is "moved by his entreaty." This is one of the clearest statements in Scripture that prayer can affect the divine inner disposition. The result: God "brought him again to Jerusalem" — physical/historical restoration following the inner movement of divine mercy.
SESSION C FLAG: add — the a.tar Niphal ("God was moved by his entreaty") as evidence that prayer produces inner movement in God is a significant observation not in the Session C word study.
CROSS-REGISTRY (2.0a): Prayer producing divine inner movement — connection to prayer (Reg 212), sovereignty, and divine responsiveness. The tension between divine sovereignty and divine responsiveness to prayer is encoded in this verse.
SD POINTER: 2Ch 33:13 — prayer producing divine inner movement (God is *entreated*). Does the prayer vocabulary consistently encode a theology of divine responsiveness? Session D to examine across prayer, mercy, and divine-inner-disposition registries.

REFERENCE: Exo 8:30
STRONG'S: H6279
CONTEXT GROUP: 987-001
ANCHOR: yes
ANNOTATION: "Moses went out from Pharaoh and prayed (*va.ye.tar*) to the Lord." The intercessory prayer here is simple in form: Moses leaves the human context (Pharaoh) and enters the prayer context (the Lord). The movement between human and divine registers is physical — he goes out and prays. The a.tar intercession is directional: it stands between the human situation and the divine response, mediating the two. Moses as intercessor models the structure of mercy-seeking on behalf of another.
SESSION C FLAG: add — intercessory prayer as directional mediation between human need and divine mercy is not currently in the Section 3 annotations.
CROSS-REGISTRY (2.0a): The mediating structure of intercession — connection to prayer (Reg 212), priesthood/mediation themes.

REFERENCE: Gen 25:21
STRONG'S: H6279
CONTEXT GROUP: 987-002
ANCHOR: yes
ANNOTATION: "Isaac prayed (*va.ye.tar*) to the Lord for his wife, because she was barren. And the Lord granted his prayer (*va.ye.a.ter*), and Rebekah his wife conceived." Again the Niphal response: the Lord "was entreated for him" — the prayer was received, and the divine response was concrete (conception). The prayer is motivated by another's need (his wife's barrenness), directed toward God, and receives a visible answer. The a.tar prayer here names a complete mercy cycle: need → prayer → divine response → resolution.
SESSION C FLAG: add — the complete mercy cycle (need → prayer → divine response) visible in Gen 25:21 is not currently in the Session C word study.
CROSS-REGISTRY (2.0a): Barrenness as the condition that generates the mercy appeal — connection to suffering/affliction registries.

REFERENCE: Job 33:26
STRONG'S: H6279
CONTEXT GROUP: 987-002
ANCHOR: yes
ANNOTATION: "Then man prays (*yē.tar*) to God, and he accepts him; he sees his face with a shout of joy, and he restores to man his righteousness." The prayer produces face-access — "he sees his face" — and restoration of righteousness. The mercy cycle here includes: prayer → divine acceptance → restored access to God's face → restored righteousness → joy. The *shout of joy* (teru'ah) at the sight of God's face is the affective climax. Mercy received produces joy expressed in the body (shout).
SESSION C FLAG: add — the face-access restored through prayer, and the somatic joy response (shout) are significant observations for the word study.
CROSS-REGISTRY (2.0a): The restoration of face-access through prayer — connects to the face/presence vocabulary (panim). Also: the *shout of joy* as the somatic response to mercy received — connection to joy/praise registries.
SD POINTER: Job 33:26 — restored face-access and somatic joy as the outcome of prayer/mercy. Does the mercy vocabulary systematically produce joy as its affective result? Session D.

---

### GROUP 988-001 | H7359 ra.cha.min

REFERENCE: Dan 2:18
STRONG'S: H7359
CONTEXT GROUP: 988-001
ANCHOR: yes
ANNOTATION: "Seek mercy (*cha.nin*) from the God of heaven concerning this mystery." The Aramaic ra.cha.min is invoked as the target of Daniel's appeal — the compassion of God is what is sought. The context is extremity: Daniel and his companions face death. The mercy-appeal in extremity names ra.cha.min as the resource that humans reach for when all human options are exhausted. The womb-love vocabulary used for cosmic God in a death-threat context is theologically bold — the most intimate maternal mercy-image applied to the Lord of Nebuchadnezzar.
SESSION C FLAG: deepen — the intimacy of the womb-love vocabulary in a cosmic/extremity context is not sufficiently developed in the Session C annotation.
CROSS-REGISTRY (2.0a): Extremity as the generator of the mercy appeal — connection to suffering/distress registries.

---

### GROUPS 989-001 | H2604 cha.nan (Aramaic)

REFERENCE: Dan 4:27
STRONG'S: H2604
CONTEXT GROUP: 989-001
ANCHOR: yes
ANNOTATION: "Break off your sins by practicing righteousness, and your iniquities by showing mercy (*cha.nan*) to the oppressed." The Aramaic cha.nan here names mercy toward the oppressed as the practical equivalent of repentance and righteousness. Daniel counsels Nebuchadnezzar to demonstrate inner moral change through mercy toward the vulnerable. Mercy is here presented as the outward evidence of inner transformation — not merely a feeling but a practice that demonstrates the inner condition has changed. The oppressed (*ani* — the poor/afflicted) are the specific recipients: mercy flows downward to the vulnerable.
SESSION C FLAG: deepen — the mercy-as-evidence-of-repentance dimension is not in the Session C word study. Add: mercy to the oppressed as the practical indicator of inner moral change.
CROSS-REGISTRY (2.0a): Mercy to the oppressed as the expression of righteousness — connection to justice/righteousness registries. Also: the oppressed (*ani*) as the specific object of mercy — connection to poverty/affliction registries.

REFERENCE: Dan 6:11
STRONG'S: H2604
CONTEXT GROUP: 989-001
ANCHOR: yes
ANNOTATION: "These men...found Daniel making petition and plea (*ve.cha.ne*) before his God." Daniel's regular prayer practice (*te.chin.nah* form) is here used as evidence against him. The fact that his prayer practice is observable and regular makes it a vulnerability. The verse encodes an important observation: Daniel's mercy-seeking before God is a *habitual inner discipline* expressed in a regular, observable external practice. Prayer as habitual inner discipline rather than crisis response.
SESSION C FLAG: add — the habitual character of Daniel's prayer/petition practice as a form of regular mercy-seeking is not in the Session C word study.
CROSS-REGISTRY (2.0a): Prayer as habitual discipline rather than crisis response — connection to prayer (Reg 212) and spiritual discipline vocabulary.

---

### GROUPS 990-001, 990-002 | H5750 od

REFERENCE: Jer 3:17
STRONG'S: H5750
CONTEXT GROUP: 990-001
ANCHOR: yes
ANNOTATION: "They shall no more (*lo' od*) stubbornly follow their own evil heart." The od particle here names the cessation of persistent inner moral stubbornness — the turning of a stubborn inner orientation. The inner condition named (*sherrirut lev* — stubbornness of heart) is specifically a characterisation of the will directed against God. The eschatological promise is the end of this stubbornness — the heart's persistent resistance will cease. The verse is a mercy-promise: the condition that has made mercy-seeking unnecessary (self-sufficient stubbornness) will be removed.
SESSION C FLAG: add — the od particle naming the cessation of inner stubbornness in an eschatological mercy-promise context is a new observation.
CROSS-REGISTRY (2.0a): *Sherrirut lev* (stubbornness of heart/will) as the inner disposition that resists mercy — connection to will (Reg 173) and to heart/stubbornness vocabulary.

REFERENCE: Job 2:3
STRONG'S: H5750
CONTEXT GROUP: 990-001
ANCHOR: yes
ANNOTATION: "He still (*od*) holds fast his integrity, although you incited me against him to destroy him without reason." The od here names the persistence of inner moral integrity under extreme assault — Job maintains his integrity *still*, despite divine permission for his suffering. The "without reason" (*chinnam* — from the cha.nan root: "for nothing, gratis") names the gratuitous character of the trial. Mercy language appears at the edges: the suffering is *chinnam* (free/without cause), and Job's persistence is the inner quality that makes him a candidate for mercy's vindication.
SESSION C FLAG: add — the chinnam/cha.nan root connection (Job suffers "without reason" — the same root as "grace/favour") is not in the Session C word study and is semantically significant.
CROSS-REGISTRY (2.0a): chinnam (without reason/freely) from the cha.nan root — suffering that is gratuitous shares a root with grace that is freely given. The semantic overlap between "unmerited suffering" and "unmerited favour" through the cha.nan root. Session D.
SD POINTER: Is there a structural relationship between chinnam-suffering (unmerited affliction) and chen-grace (unmerited favour)? Both are "without cause/for free" — is the gratuitous character of mercy and the gratuitous character of suffering etymologically and theologically related? Session D.

REFERENCE: Hab 2:3
STRONG'S: H5750
CONTEXT GROUP: 990-002
ANCHOR: yes
ANNOTATION: "For still (*od*) the vision awaits its appointed time; it hastens to the end...if it seems slow, wait for it." The od here names the temporal persistence of a divine promise not yet fulfilled. The mercy embedded in this verse is the mercy of God's faithfulness to his own word: what he has promised will come, even if delayed. The inner quality demanded from the hearer is *waiting* — active expectation. The verse encodes the temporal dimension of divine mercy: mercy is not only for the present moment but is guaranteed for the appointed future time.
SESSION C FLAG: add — the temporal dimension of divine mercy (mercy that persists toward the appointed time) is not in the Session C word study.
CROSS-REGISTRY (2.0a): Hope as the inner response to divine faithfulness-in-time — connection to hope (Reg for hope) and to faith/waiting vocabulary.

REFERENCE: Isa 5:25
STRONG'S: H5750
CONTEXT GROUP: 990-002
ANCHOR: yes
ANNOTATION: "His anger has not turned away, and his hand is stretched out still (*od*)." The od here names the persistence of divine anger — mercy's opposite as equally sustained. God's wrath has duration just as his mercy has duration. The verse is analytically significant: the same vocabulary that names mercy's persistence (God's mercy "endures forever" in Ps 136) is used to name anger's persistence. Divine inner dispositions — both mercy and wrath — are characterised by sustained duration. The contrast with mercy is not that wrath is temporary and mercy permanent (a common oversimplification) but that both represent sustained divine inner orientations.
SESSION C FLAG: add — the od vocabulary naming sustained wrath as structurally parallel to sustained mercy is a new and significant observation. The word study should include this.
CROSS-REGISTRY (2.0a): Sustained divine wrath as structural parallel to sustained divine mercy — connection to anger/wrath registries (pool1-anger-pair). The persistence vocabulary (od) connects both.
SD POINTER: Already captured from Pass 2: mercy and wrath share the od-persistence structure. Confirmed and expanded here.

---

### GROUP 991-001 | G2435 hilastērios

REFERENCE: Heb 9:5
STRONG'S: G2435
CONTEXT GROUP: 991-001
ANCHOR: yes
ANNOTATION: "Above it were the cherubim of glory overshadowing the mercy seat. Of these things we cannot now speak in detail." The mercy seat in Hebrews is mentioned in passing — Hebrews 9 does not pause to explain it because the readers understand the reference. The cherubim overshadow it: the mercy seat is covered by the presence of divine glory. The phrase "we cannot now speak in detail" is significant — the author is aware of depths in the mercy-seat theology that the current argument cannot fully explore. The restraint itself is theologically honest.
SESSION C FLAG: add — the "we cannot speak in detail" note from Hebrews acknowledges inexhaustible depth in the mercy-seat theology.
CROSS-REGISTRY (2.0a): Cherubim of glory overshadowing the mercy seat — the mercy seat as the meeting point of mercy and divine glory. Connection to holiness/glory vocabulary.

REFERENCE: Rom 3:25
STRONG'S: G2435
CONTEXT GROUP: 991-001
ANCHOR: yes
ANNOTATION: "Whom God put forward as a propitiation (*hilastērios*) by his blood, to be received by faith." The mercy seat becomes personal — Christ is the hilastērios. Three structural moves: (1) God put forward (divine initiative — mercy is divinely provided); (2) by his blood (the atoning mechanism is carried in Christ's person); (3) received by faith (access to the mercy seat is now personal and immediate, not mediated by priestly ritual). The verse formally ends the spatial-architectural mercy-seat theology and relocates it in the person and reception of Christ.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): Faith as the mode of accessing the mercy seat (hilastērios) — connection to faith (Reg 59). The mercy-seat theology and the faith vocabulary converge in this verse: faith is what brings the supplicant to the mercy seat.
SD POINTER: Rom 3:25 — faith as mercy-seat access. Does the faith vocabulary consistently appear in mercy-reception contexts? Session D.

---

### GROUP 992-001 | G3628 oiktirmos

REFERENCE: 2Cor 1:3
STRONG'S: G3628
CONTEXT GROUP: 992-001
ANCHOR: yes
ANNOTATION: "Blessed be the God and Father of our Lord Jesus Christ, the Father of mercies (*oiktirmōn*) and God of all comfort (*paraklēseōs*)." God is named as *pater tōn oiktirmōn* — the Father of mercies — the generative source of all compassionate mercy. The plural *oiktirmōn* names God's mercies as multiple, layered, abundant acts and dispositions of compassion. The pairing with *paraklēsis* (comfort, consolation, encouragement) names the pastoral outcome of mercy: the Father of mercies produces comfort in those who are afflicted. Mercy and comfort are functionally connected — mercy is what God is; comfort is what he produces in others from that inner character.
SESSION C FLAG: confirm.
CROSS-REGISTRY (2.0a): Mercy → comfort causal chain. *Paraklēsis* (comfort/consolation/encouragement) as the pastoral output of divine mercy. Connection to comfort/consolation registries if they exist. Also: the Paraclete title for the Spirit — is there a connection between divine comfort (paraklēsis) and the Spirit as Paraclete?
SD POINTER: 2Cor 1:3 — does the mercy → comfort causal chain correspond to the Spirit's parakletos function? Session D.

REFERENCE: Col 3:12
STRONG'S: G3628
CONTEXT GROUP: 992-001
ANCHOR: yes
ANNOTATION: "Put on then, as God's chosen ones, holy and beloved, compassionate hearts (*splagchna oiktirmou*)." The phrase *splagchna oiktirmou* — "inner organs of mercy" — is the most somatic mercy expression in the NT. Mercy originates in the body's depths (*splagchna* = viscera, bowels). The metaphor of clothing (*put on*) names mercy as a character garment — something consciously assumed and worn. The list following (kindness, humility, meekness, patience) names mercy as the first and foundational garment, with the others following from it. The addressees are "holy and beloved" — the call to wear mercy arises from an identity of being chosen and beloved.
SESSION C FLAG: confirm and deepen — the splagchna oiktirmou as founding garment of the new humanity is confirmed. Add: the identity-grounding of the call ("chosen and beloved") — the call to mercy arises from received mercy.
CROSS-REGISTRY (2.0a): The list of character virtues in Col 3:12 — compassionate hearts, kindness, humility, meekness, patience. Each term likely has a registry. Mercy is the first garment; the others are co-garments. Session D to examine whether this list encodes a structured inner-being portrait.
SD POINTER: Already captured: Col 3:12 as a multi-registry inner-being portrait. Confirmed.

---

### GROUP 993-001 | G0448 anileōs

REFERENCE: Jam 2:13
STRONG'S: G0448
CONTEXT GROUP: 993-001
ANCHOR: yes
ANNOTATION: "For judgment is without mercy to one who has shown no mercy. Mercy triumphs over judgment." Two clauses encoding the mercy-judgment structural relationship. First: the person who withheld mercy receives judgment-without-mercy (*anileōs*) — a precise reciprocal. Second: "mercy triumphs over judgment" (*katakauchātai*) — mercy is the stronger category; it overcomes (*kauchaomai* root: to boast over, exult over) judgment. The first clause is a warning; the second is a promise. Together they name the two possible outcomes of the mercy-judgment dynamic: the person who extended mercy stands on the mercy-triumphant side; the person who withheld it stands on the judgment-without-mercy side.
SESSION C FLAG: confirm. Section 3 annotation is accurate and full.
CROSS-REGISTRY (2.0a): Mercy triumphing over judgment — the most direct statement of the mercy-judgment structural relationship. Connection to judgment/condemnation registries. The verb "triumphs over" (*katakauchaomai*) is an inner-disposition term — pride/boasting root applied to mercy's superiority over judgment.
SD POINTER: The mercy-triumph-over-judgment formula — is mercy structurally superior to judgment in the biblical economy, or does it presuppose judgment? Session D to examine whether this is mercy *replacing* judgment or mercy *addressing* judgment that has been acknowledged.

---

### PASS 3 SUMMARY

**Total owner anchor verses annotated:** 63
**XREF anchor verses:** 60 — handled in owning registries per instruction

**Session C flags generated:**
- confirm: 18 groups (annotations accurate, no correction needed)
- deepen: 15 groups (correct but insufficient; specific deepening noted)
- add: 20 groups (observation missing from Session C v1; new content to add)
- none: 3 groups (H3722B groups — same verses as H3722A; no new annotation required; G8849 deleted)

**Supplementary verses flagged (non-anchor verses with significant content not represented by anchors):**
- Mat 18:33 and Mat 5:7 both anchor multiple terms — this is noted but requires no additional action
- Psa 51:1 is the primary three-registry convergence verse — should anchor the cha.nan/chesed/rachamim connection explicitly in Session C Section 5

**SD pointers raised in Pass 3 (cumulative):**
- Mercy-justice structural relationship (Mat 23:23 / Jam 2:13)
- Beatitudes as structured inner-being portrait (Mat 5:7)
- Rom 1:31 as multi-registry collapse catalogue
- Shame as mercy-induced (Eze 16:63) — distinct from shame-of-exposure
- Mercy-seat as locus of divine communication (Exo 25:22)
- Somatic supplication posture in Luk 18:13
- Mercy cry and perseverance (Mar 10:48)
- Sevenfold blood-sprinkling completeness symbolism (Lev 16:14)
- Yom Kippurim self-affliction and inner renewal (Lev 23:27)
- Mercy-compassion parallel in divine sovereignty (Rom 9:15)
- Gen 32:20 face-covering / Num 6:25 face-shining correspondence
- Psa 51:1 three-registry convergence
- 1Ki 8:38 self-knowledge as supplication prerequisite
- 2Ch 33:13 prayer producing divine inner movement
- Chinnam (Job 2:3) / chen root connection — unmerited suffering and unmerited grace
- Mercy and wrath sharing od-persistence structure (confirmed from Pass 2)
- Faith as mercy-seat access (Rom 3:25)
- Mercy → comfort causal chain and Paraclete question (2Cor 1:3)
- Col 3:12 multi-registry inner-being portrait
- Mercy triumph over judgment structural question (Jam 2:13)

---

PASS 3 COMPLETE
Date: 2026-04-11
All 63 owner anchor verses annotated. Session C flags generated for each group. SD pointers raised throughout.
meaning_numbered directive: DIR-MEAN-001 (G2433 hilaskomai) confirmed.
Observations log version increments to v1.3 at this boundary. D1 directives ready for assembly and delivery.

