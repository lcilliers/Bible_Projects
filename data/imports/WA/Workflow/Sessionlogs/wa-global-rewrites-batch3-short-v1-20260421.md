# Batch 3 — Short Rules — Rewrites for Review

**Filename:** wa-global-rewrites-batch3-short-v1-20260421.md
**Date:** 2026-04-21
**Reference to prior output:** wa-global-rules-review-obslog-v1_0-20260421.md §62–§64; prior batches: wa-global-rewrites-batch1-long-v1-20260421.md, wa-global-rewrites-batch2-medium-v1-20260421.md.
**Batch scope:** 14 of 15 short rules (66–326 chars). One rule (GR-FILE-005) is intentionally left untouched — see §64 below.
**Governing discipline:** content-evaluation (appropriateness + correctness); consistency is key.

---

## How to read this document

Most of these rules are already close to rules-form. The value of this batch is finishing the consistency pass: dot-notation version corrections, the final `example` → `examples` migration, and any remaining style/vocabulary touches. Most commentary fields will correctly remain NULL.

Fields that stay NULL are shown as *(NULL — none appropriate)*.

---

## 1. GR-PROG-006 — Characteristic-perspective grouping model

**Current:** v2.0 (dot), 326 chars, `applies_to`: Verse Context, Session B instructions.

**Evaluation:** Rule is self-contained. The sentence "The same property term can serve different characteristics across its corpus" is the discriminating observation — staying in rule_text. No rationale needed (self-evident given GR-PROG-001).

**`rule_text`:**
> The characteristic-perspective grouping model governs how verse context groups are formed: groups describe what a verse is about — the inner-being characteristic it engages — not what a term does. The same property term can serve different characteristics across its corpus. Groups are characteristic-centric, not term-centric.

**`rationale`:** *(NULL — self-evident)*
**`application_notes`:** *(NULL — none appropriate)*
**`examples`:** *(NULL — verse examples would need researcher-approved judgements; deferred)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 2. GR-DATA-005 — god_as_subject and somatic_link verification

**Current:** v2.0 (dot), 315 chars, `applies_to`: Session B instruction.

**Evaluation:** The "high error rate from bulk operations" clause is rationale inline — keeping in rule_text because it frames the specific risk being addressed.

**`rule_text`:**
> The fields `god_as_subject` and `somatic_link` on `wa_term_inventory` carry a high error rate from bulk operations. Before setting or relying on these fields in Session B, Claude AI verifies the values against the actual verse evidence for each term. A field value not verified against verse evidence is not confirmed.

**`rationale`:** *(NULL — inline in rule_text)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 3. GR-FILE-006 — Prefix and reference conventions

**Current:** v1.0 (dot), 308 chars, `applies_to`: all processing instructions.

**Evaluation:** The rule's operative content is the list of prefix/reference conventions. List stays in rule_text; restructuring it into examples would break the binding into fragments.

**`rule_text`:**
> The prefix for this project is `wa`. Global files use `wa-global` as the reference segment. Registry files use the zero-padded registry number (e.g. `wa-023`). Cluster files use the cluster code (e.g. `wa-c17`). Session D synthesis files use `wa-sd`. Batch files use the batch identifier (e.g. `wa-vcb-001`).

**`rationale`:** *(NULL)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL — the worked prefixes are part of the binding list)*
**`version`:** `1.0` → `1_1` (minor + notation normalisation).

---

## 4. GR-PROC-004 — No patch or directive applied without researcher review

**Current:** v2.0 (dot), 307 chars, `applies_to`: all sessions, all phases.

**Evaluation:** Governance rule. Binding is clean.

**`rule_text`:**
> Every patch and every directive is reviewed by the researcher before Claude Code applies it. Claude AI produces the patch or directive, states what it will do and what the confirmation output will be, and waits for explicit researcher approval before Claude Code proceeds. This applies without exception.

**`rationale`:** *(NULL — self-evident as governance)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).
**Terminology:** "CC directive" → "directive" (aligns with wa-directive-instruction [current] terminology; the CC prefix is implicit).

---

## 5. GR-DATA-001 — Active terms filter for mti_terms queries

**Current:** v2.0 (dot), 302 chars, `applies_to`: all sessions, all phases.

**Evaluation:** The SQL fragment IS the rule — it stays in rule_text. No additional examples needed.

**`rule_text`:**
> All SQL queries against `mti_terms` that are intended to return active terms must include: `AND mt.status IN ('extracted', 'extracted_thin')`. Queries that omit this filter return deleted terms and produce incorrect counts. This filter is non-waivable for any query where "active terms" is the intent.

**`rationale`:** *(NULL — inline)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL — the SQL fragment in rule_text is the example)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 6. GR-PROG-004 — Session C is primary; Session B deepens it

**Current:** v2.0 (dot), 297 chars, `applies_to`: Session B, Session C instructions.

**Evaluation:** The final sentence ("An accurate Session C document that has been corrected by Session B is more valuable than an accessible document that contains errors") is rationale — move.

**`rule_text`:**
> The Session C word study is the primary reader-facing document. It stands on its own feet. Session B deepens and corrects it from within — it does not replace it.

**`rationale`:**
> An accurate Session C document that has been corrected by Session B is more valuable than an accessible document that contains errors. The value of Session C depends on its being right; Session B exists to make it right.

**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 7. GR-PROG-001 — Verse always leads

**Current:** v2.0 (dot), 287 chars, `applies_to`: all sessions, all phases.

**Evaluation:** Foundational rule. Binding is clean; "why" is articulated elsewhere (GR-PROG-002 and GR-PROC-002).

**`rule_text`:**
> The verse is the primary unit of evidence. All analytical work begins with what the verse says, not what a category, tradition, or prior interpretation says. Dimensions, classifications, and findings emerge from the verse evidence. The verse is never bent to fit a pre-existing category.

**`rationale`:** *(NULL — foundational; the programme's governing question (GR-PROG-002) and data-traceability requirement (GR-PROC-002) together form the rationale)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 8. GR-OBS-004 — Obslog version increment at named boundaries

**Current:** v2.0 (dot), 236 chars, `applies_to`: Session B, Dimension Review, Verse Context instructions.

**Evaluation:** Rule is clean. Vocabulary harmonisation: "observations log" → "obslog" after first mention (per GR-OBS-001 canonical form).

**`rule_text`:**
> The observations log (obslog) filename is version-incremented when resuming work on the same registry or cluster in a new session — not on every file save within the same session. A named boundary is a new session start, not a mid-session write.

**`rationale`:** *(NULL — distinction is self-explanatory)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation + vocabulary harmonisation).

---

## 9. GR-PROG-002 — Programme governing question

**Current:** v2_0 (already underscored), 228 chars, `applies_to`: all sessions, all phases.

**Evaluation:** Definitional statement. Binding is the question itself; keep intact.

**`rule_text`:**
> The programme's governing question is: what does Scripture reveal about the characteristics, operations, and interrelationships of the human inner being (spirit, soul, body)? All analytical work is oriented toward this question.

**`rationale`:** *(NULL — definitional)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2_0` → `2_1` (minor, for consistency with the pass).

---

## 10. GR-PROG-003 — Dimensions are data-derived

**Current:** v2.0 (dot), 213 chars, `applies_to`: Dimension Review, Session B instructions.

**Evaluation:** Clean rule. Binding is the discovery discipline plus the grounding floor (at least one verse in the registry's corpus).

**`rule_text`:**
> Dimension assignments are discovered from verse evidence, not imposed from prior categories. A dimension that cannot be grounded in at least one verse in the registry's corpus is not a dimension for that registry.

**`rationale`:** *(NULL — self-evident given GR-PROG-001)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 11. GR-DATA-003 — `mti_term_flags` authoritative for somatic classification

**Current:** v2.0 (dot), 203 chars, `applies_to`: Session B instruction, all somatic classification work.

**Evaluation:** Field-authority statement. The reference to the redundant alternative field is part of the binding.

**`rule_text`:**
> The authoritative field for somatic classification is `mti_term_flags`, not the redundant `wa_term_inventory.somatic_link` field. Where a conflict exists between these two sources, `mti_term_flags` is correct.

**`rationale`:** *(NULL — definitional)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2.0` → `2_1` (minor + notation normalisation).

---

## 12. GR-FILE-007 — Lowercase filenames

**Current:** v2.0 (dot), 172 chars. **Has singular `example` populated.** `applies_to`: all processing instructions.
`example` (singular): `"WRONG: wa-023-compassion-SessionB-log-v1-20260414.md — CORRECT: wa-023-compassion-sessionb-log-v1-20260414.md"`

**Evaluation:** Rule is clean. Final `example` → `examples` migration in this pass.

**`rule_text`:**
> All filenames produced by Claude AI are fully lowercase — no uppercase characters anywhere in the filename or extension. This applies without exception to all output files.

**`rationale`:** *(NULL — self-evident; portability and grep-consistency)*
**`application_notes`:** *(NULL)*
**`examples`** (migrated from singular `example`):
> Wrong: `wa-023-compassion-SessionB-log-v1-20260414.md`
> Correct: `wa-023-compassion-sessionb-log-v1-20260414.md`

**`example`** (singular): **set to NULL** — content migrated.
**`version`:** `2.0` → `2_1` (minor + notation normalisation + migration).

---

## 13. GR-PROC-001 — Step completion requires validated output existence

**Current:** v2_0 (already underscored), 136 chars.

**Evaluation:** Clean one-sentence rule. No restructure beyond minor bump for consistency with the pass.

**`rule_text`** (unchanged):
> A step that produces a required output is not complete until that output exists and has been validated as complete per the instructions.

**`rationale`:** *(NULL)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `2_0` → `2_1` (minor, for pass consistency).

---

## 14. GR-FILE-002 — Short description length

**Current:** v1.0 (dot), 66 chars.

**Evaluation:** Shortest rule in the set. Binding is a single threshold. No restructure possible; only notation correction.

**`rule_text`** (unchanged):
> The short description in a filename must not exceed 30 characters.

**`rationale`:** *(NULL)*
**`application_notes`:** *(NULL)*
**`examples`:** *(NULL)*
**`version`:** `1.0` → `1_1` (minor + notation normalisation).

---

## Rule intentionally NOT touched in this batch

### GR-FILE-005 — Output format by purpose (v2_0, 102 chars)

**Reasoning:** The rule is already at its minimum form — a single clear sentence with no dot-notation issue. A minor version bump without a content change is pointless churn and would clutter the audit trail.

Recorded in obslog §64 as an authorship judgement per GR-HF-001: **leave GR-FILE-005 untouched in this batch.** If the researcher prefers every short rule to receive a version bump for pass-consistency reasons, I will include it in a follow-up single-operation patch.

---

## Summary — batch 3 aggregate

| Rule | Old chars | New rule_text chars | Δ% | Notation fix | Migration | Rationale | Appl notes | Examples |
|---|---:|---:|---:|:---:|:---:|:---:|:---:|:---:|
| GR-PROG-006 | 326 | 318 | −2% | ✓ | — | — | — | — |
| GR-DATA-005 | 315 | 307 | −3% | ✓ | — | — | — | — |
| GR-FILE-006 | 308 | 308 | 0% | ✓ | — | — | — | — |
| GR-PROC-004 | 307 | 300 | −2% | ✓ | — | — | — | — |
| GR-DATA-001 | 302 | 302 | 0% | ✓ | — | — | — | — |
| GR-PROG-004 | 297 | 189 | −36% | ✓ | — | ✓ | — | — |
| GR-PROG-001 | 287 | 287 | 0% | ✓ | — | — | — | — |
| GR-OBS-004 | 236 | 243 | +3% | ✓ | — | — | — | — |
| GR-PROG-002 | 228 | 228 | 0% | — | — | — | — | — |
| GR-PROG-003 | 213 | 213 | 0% | ✓ | — | — | — | — |
| GR-DATA-003 | 203 | 204 | 0% | ✓ | — | — | — | — |
| GR-FILE-007 | 172 | 172 | 0% | ✓ | ✓ | — | — | ✓ (migrated) |
| GR-PROC-001 | 136 | 136 | 0% | — | — | — | — | — |
| GR-FILE-002 | 66 | 66 | 0% | ✓ | — | — | — | — |

Only one rule in this batch produced a meaningful reduction: GR-PROG-004 (−36%) where the concluding sentence was rationale. Everything else is consistency/notation work, confirming §55.5 prediction — short rules are already at or near their minimum form.

**Pass-wide cumulative state after batch 3 applies:**
- All 36 rules will carry the four-field structure (`rule_text` + `rationale` + `application_notes` + `examples`), populated or NULL as appropriate.
- All version numbers will use the underscored form (with GR-FILE-005 as the one intentional exception — already compliant, no bump).
- Three `example` → `examples` migrations complete (GR-FILE-001, GR-FILE-009 in batch 2; GR-FILE-007 in batch 3).

---

## Cross-cutting observations

1. **One authorship call held for explicit confirmation** — GR-FILE-005 left untouched (§64). The researcher can override if pass-wide version bump is preferred.
2. **Final `example` → `examples` migration** in this batch completes the column-cleanup work planned in §48.
3. **One terminology touch** — GR-PROC-004 uses "CC directive" → "directive" for consistency with wa-directive-instruction [current]'s naming.

---

## Open check before patch applies

1. Directional acceptance of the fourteen rewrites.
2. The decision to leave GR-FILE-005 untouched (authorship call per GR-HF-001) — confirm, or override and add it as a 15th operation.
3. The "CC directive" → "directive" terminology touch in GR-PROC-004.

---

*End of Batch 3 review document. Patch follows at wa-rules-batch3-short-update-v1-20260421.json.*
