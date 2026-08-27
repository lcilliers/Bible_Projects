---
name: feedback_bake_guidance_into_authoritative_instructions
description: Researcher guidance/rules/corrective actions MUST be written into the AUTHORITATIVE instruction docs, not only into memory.
metadata:
  type: feedback
---

When the researcher gives guidance — a rule, a decision, a corrective action, an answer to a recurring question — I **must update the authoritative instruction docs** in `Workflow/Instructions/` with the detail, not only record it in project memory. Memory is a secondary aid; the **written authoritative instructions are the source of truth** (GR-REF-002, `[current]` resolution) and the place these rules are enforced and found by future sessions (mine and Claude AI's).

**Why:** the researcher noted (2026-07-12) that answers given this session "are all questions I have answered in the past also" — recurring guidance that keeps getting re-explained because it was never baked into the governing docs. Putting it in memory alone lets it drift out of the authoritative record.

**How to apply:** on receiving guidance, (1) identify which authoritative doc OWNS that rule (the role/candidate/lexical model → the cycle + integrity-definition docs; term/registry rules → the term-add pipeline; passage rules → passage-rule; readiness → the readiness assessment); (2) add it there as a **dated amendment section** (`## AMENDMENT YYYY-MM-DD (researcher direction)`) — the established pattern — or version-bump if the doc says so; (3) THEN mirror a pointer in memory. Verified example: the 2026-07-12 role-model/registry-path/staged-sequence guidance was baked into `wa-db-integrity-definition-authoritative-v1` (I12/D1/D2), `wa-term-add-update-AUTHORITATIVE-pipeline-v1` (registry-selection), and `wa-characteristic-role-lexical-cycle-authoritative-v1`. Relates to [[feedback_source_of_truth_is_written_record]], [[feedback_filing_is_first_class_governance]], [[project_book_lexical_readiness_assessment]].
