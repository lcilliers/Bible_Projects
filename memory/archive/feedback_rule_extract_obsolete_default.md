---
name: feedback_rule_extract_obsolete_default
description: When extracting from wa_rule_registry (or any rule list), exclude obsolete=1 rows by default; include only when user explicitly asks
type: feedback
originSessionId: 12f3ee6c-eace-4fa2-87e3-9c4257076ae7
---
When producing extracts, reports, or summaries from `wa_rule_registry` — or any registry/list that has an `obsolete` (or equivalent retired/superseded) flag — **exclude obsolete rows by default**. Include them only when the user explicitly asks for them (e.g., "include obsolete", "show retired rules", "full history").

**Why:** The user is consolidating rules and views obsolete rows as historical noise that distracts from the operational rule set. Stated 2026-04-26 in the context of optimising `wa_rule_registry`. Including obsolete rows by default contradicts the working assumption that an extract represents the *current* rules in force.

**How to apply:**
- Default `WHERE obsolete = 0` (or `obsolete IS NULL`) in any rule-extract query.
- If a query is ambiguous, prefer active-only and note in the output that obsoletes were excluded.
- Generalise to other tables with retirement semantics: `wa_term_inventory.term_owner_type='XREF'` is *not* obsolete, but `delete_flagged=1`, `mti_terms.status IN ('candidate_delete','delete','excluded')`, and similar are — check with the user before applying generalisation, but lean toward exclusion.
- The extract I wrote earlier today (`outputs/markdown/wa-rule-registry-session_startup-observation_discipline-v1-20260426.md`) included obsoletes — that violated this principle. Re-issue as v2 if asked.
