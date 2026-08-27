# Directive DIR-20260502-001 — Righteousness vocabulary programme-wide audit

> Produced by: wa-directive-instruction-v1_3-20260422
> Governed by: wa-global-general-rules [current]
> Registry: global (cluster C10 session — cross-registry query)
> Produced date: 2026-05-02
> Researcher approval: PENDING

---

## Motivation

During C10 Dimension Review Phase A, a coherence problem was identified in the current distribution of righteousness vocabulary across the programme.

R077 (labelled "honesty") owns H6662 tsaddiq and H6666 tsedeqah — core Hebrew righteousness terms. The registry label does not match its vocabulary. This is recorded as SD pointer DIM-77-SD001.

R139 (labelled "righteousness") owns only G1345 dikaiōma — a narrow Greek term meaning "righteous requirement / decree / act." It carries 33 XREF terms but only 1 OWNER term, suggesting the primary righteousness vocabulary sits elsewhere in the programme.

G1343 dikaiosynē — the primary Greek righteousness noun — is not visible as an OWNER term in either R077 or R139. Its programme-wide ownership location is not known from the C10 extract alone.

Before any reallocation or ownership-reset proposal can be made to the researcher, Claude AI requires a programme-wide picture of where all righteousness-family vocabulary currently sits: which registries own which terms, what verse evidence each term carries, and how the terms are distributed as cross-references across other registries.

This is a read-only investigative directive. No database changes are made.

---

## Scope

**Tables involved (read only):** `mti_terms`, `word_registry`, `verse_context_group`, `wa_dimension_index`, and whatever table or join mechanism holds cross-reference (XREF) term associations.

**Status filter (GR-DATA-001 mandatory):** All queries that join or filter `mti_terms` must include `AND mt.status IN ('extracted', 'extracted_thin')`.

**Target vocabulary — righteousness family (Hebrew and Greek):**

| Strongs | Transliteration | Gloss |
|---|---|---|
| H6662 | tsaddiq | righteous (adjective) |
| H6663 | tsadaq | to be righteous / to justify |
| H6664 | tsedeq | righteousness / justice |
| H6665 | tsidqah | righteousness (Aramaic) |
| H6666 | tsedeqah | righteousness |
| G1342 | dikaios | righteous (adjective) |
| G1343 | dikaiosynē | righteousness (noun) |
| G1344 | dikaioō | to justify / declare righteous |
| G1345 | dikaiōma | righteous requirement / act / decree |
| G1346 | dikaiōs | righteously (adverb) |
| G1347 | dikaiōsis | justification |
| G1348 | dikastēs | judge |
| G1349 | dikē | justice / penalty |

**Four queries, all read-only:**

**Q1 — Programme-wide term inventory.** From `mti_terms` WHERE `strongs_number IN (target list)` AND `status IN ('extracted','extracted_thin')`. Return: `mti_term_id`, `strongs_number`, `transliteration`, `gloss`, `language`, `status`, `owning_registry_no`, `owning_registry_word` (via join to `word_registry`), `cluster_assignment`, `session_b_status`, `verse_context_status`, `dim_review_status`. Where a target Strongs number has no matching rows, explicitly note its absence.

**Q2 — Registry ownership summary.** Group Q1 results by registry. Return per registry: `registry_no`, `registry_word`, `cluster_assignment`, `session_b_status`, `verse_context_status`, `dim_review_status`, count of terms owned, list of Strongs numbers owned.

**Q3 — Verse evidence footprint per term.** For each term in the target list, return: `strongs_number`, `transliteration`, `owning_registry_no`, `owning_registry_word`, count of `verse_context_group` rows associated with it, count of `wa_dimension_index` rows, total verse count, count of groups where `dominant_subject IS NULL`. CC should adapt field names and joins to the actual schema.

**Q4 — Cross-reference appearances.** For each term in the target list, return all registries where the term appears as a cross-reference (i.e. in scope for that registry's verse context analysis but owned by a different registry). CC should use the actual schema mechanism for XREF associations. Return: `strongs_number`, `transliteration`, `owning_registry_no`, `owning_registry_word`, `xref_registry_no`, `xref_registry_word`, `xref_cluster`. If XREF is not stored in a dedicated table, CC should describe the schema mechanism and return whatever cross-reference data is available.

---

## Outcome required

The database state is unchanged. This directive produces no writes.

The required outcome is a single JSON output file: `wa-dim-c10-righteousness-audit-20260502.json`

Structure:

```json
{
  "meta": {
    "directive_id": "DIR-20260502-001",
    "produced_date": "2026-05-02",
    "produced_by": "Claude Code",
    "db_changes": "none"
  },
  "query_1_term_inventory": [ ... ],
  "query_2_registry_summary": [ ... ],
  "query_3_verse_footprint": [ ... ],
  "query_4_xref_appearances": [ ... ]
}
```

Where a query returns zero rows for a given Strongs number, an explicit null/empty entry with a note is included so that the absence is visible, not silent.

File destination: `Sessions/Session_B/04_dimension_review_process input/` and standard outputs location.

---

## Completion confirmation

CC returns the following on completion:

1. Confirm which of Q1–Q4 executed successfully and which (if any) required schema adaptation — state what was adapted and why.
2. For each query, state the row count returned.
3. List explicitly any Strongs numbers from the target list that returned zero rows in Q1 — these are absent from the extracted programme vocabulary and are analytically significant.
4. Confirm the output file path.
5. State whether any target Strongs number appeared in Q1 with an `owning_registry_no` outside C10 — name the registry if so.
6. For Q4: if the XREF mechanism differs from a dedicated join table, describe the actual schema structure used.

CC does not make analytical judgements about the results. Data is returned to Claude AI for analysis.

---

## Notes

- This directive arises mid-Phase A of C10 Dimension Review. Analytical work on the cluster continues in parallel; Claude AI will incorporate audit results into Phase A completion and before Phase B begins for R077 and R139.
- No registry changes, no ownership resets, no patches are implied by this directive. Those decisions follow after Claude AI analyses the returned data and presents options to the researcher.
- If CC discovers that the XREF schema does not allow Q4 to be answered cleanly, CC should return whatever partial data is available and flag the gap — do not substitute a different query that changes the analytical intent.

---

*wa-dim-c10-dir-001-righteousness-audit-v1_1-20260502.md | DIR-20260502-001 | Status: PENDING RESEARCHER APPROVAL | v1_1: rewritten to canonical template per wa-directive-instruction-v1_3-20260422 | v1_0 withdrawn — template and element-naming non-compliant*
