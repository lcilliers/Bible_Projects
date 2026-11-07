# Escalation deep history

## #1591 — surface has real word-alignment defects (192 rows)
type=issue source=researcher

**v1** (2026-09-07T18:29:13Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** surface has real word-alignment defects (192 rows)
> **comment (set this version):** 192 of 544,572 live rows (0.035%) have a surface value that's misattached or empty due to interlinear alignment defects, not legitimate multi-word idiom translation. Confirmed cases: Deut.7.18 position 2 (strong=H2142 'remember') carries surface='of them but you shall', which belongs to an earlier clause entirely, not to 'remember'. 1Thess.1.1 position 17: 4 different strong codes share one position, all with empty surface -- alignment appears to have run out of distinct English words near the end of a long genitive chain. This also means the text_reconstructed_from_codes fallback (BUILD.md #252) inherits the same defect for any verse touching one of these. Not fixed -- parked per researcher's decision to pause this work.
> **context (set this version):** Found live during the same column validation pass, 2026-09-07.

**v2** (2026-09-08T03:48:49Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** the surface column rewrite is subject to approval of 1592

**v3** (2026-09-08T11:24:13Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Repairing live verse-alignment data is a judgment call per project rules (never silent). Need either the original 192-row list/query, or your call on which detection approach (or a different one) defines the defect set, before I can propose a repair method.
> **resolution (set this version):** Attempted to reproduce the 192-row defect set to propose a concrete repair: queried verse_lexical for verse/position slots shared by >1 distinct strong (118,749 slots / 285,070 rows -- mostly legitimate idiom multi-word alignment, not defects); empty-surface rows total only 59 live-wide; a surface>=4-words heuristic found 133 candidates, a different population from the confirmed examples given (Deut.7.18 pos.2, 1Thess.1.1 pos.17). None of these heuristics cleanly isolates the same 192 rows already identified -- I don't have the query/row-list that produced that figure.

**v4** (2026-09-15T04:05:22Z, Claude) state=re-assigned next_action=review assigned_to=Researcher
> **comment (set this version):** Consolidated into #1706 (full lexical stack rebuild proposal). Researcher instruction, verbatim, this chat turn: the new build instructions should be clear on how to determine surface, old records are all set as deleted. research_db records are no longer relevant. Confirmed: surfaces build rule is unchanged and already clear (denormalized from span.surface, #1607 spec item 14) -- nothing new to design. The specific 192-row defect set is now MOOT: those rows belong to data being wholesale soft-deleted for the full verse_lexical rebuild (researchers own confirmed instruction), so there is no old-row list left to repair, and no need to reproduce the original query. What carries forward: a POST-REBUILD validation check (re-run the same detection heuristics against the freshly built rows), not a repair of old rows -- build-list item 9 in #1706.
> **context (set this version):** Full reasoning: iba/docs/1706-lexical-stack-full-rebuild-consolidated-build-proposal-v1-20260915.md section 3.

**v5** (2026-09-15T05:21:54Z, Researcher) state=supersede next_action=reject assigned_to=Claude
> **comment (set this version):** now 1704
> **resolution (set this version):** Researcher, this chat turn: *"the new build instructions should be clear on how to determine
surface, old records are all set as deleted. research_db records are no longer relevant."* Combined
with the confirmed full-rebuild scope (above): the specific 192-row defect set belongs to data being
wholesale retired — there is no old-row list left to repair. **`surface`s build rule is unchanged
and already clear** (denormalized from `span.surface`, #1607 spec item 14) — nothing new to design
there. What carries forward: a **post-rebuild data-quality check** (not a repair of old rows) —
re-run the same detection heuristics (multi-strong-same-position, empty-surface, ≥4-word spans)
against the *freshly built* rows once the rebuild completes, since the underlying interlinear
alignment behavior that caused the original defects is a property of the source data, not of the old
rows specifically, and could still surface in the rebuild. **Build item, not a design decision.**
