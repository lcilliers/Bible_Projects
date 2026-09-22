# Session Log — 2026-09-22 (continuation session)

**Scope:** Started via `/start-project`. Worked through the escalation backlog from the prior
session, then diagnosed and fixed two real Stage 1 defects (M0.8.1 duplicate-observation gating
bug; strong-density batch chunking causing truncated LLM calls), reverted chunking to a
researcher-directed verse-count unit, ran live reconciliation/verification against real data, and
then opened a serious cost/architecture review of the whole Stage 1 approach that the session ended
without resolving.

## Escalations touched

| # | Outcome | Summary |
|---|---|---|
| #1804 | completed | "Full pipeline trace" living document — researcher confirmed complete, moved to ready_for_approval, approved. |
| #1837 | completed | `translit-never-without-gloss` cfg_method_rule restored (escalation #1836's finding) — proposed, approved, applied, verified live (cfg_method_rule id=111). |
| #1840 | completed | Real root cause found for M0.8.1 duplicate rows: `_is_per_occurrence_question` in `recordingpass.py` was never updated when M0.8.1 joined the strong-specific-occurrence family, so it fell through to the word-level keyword/similarity branch instead of exact-occurrence matching. Fixed (delegated to the correct predicate), verified live on the confirmed case (Ezra.7.17/H9010: 3 duplicate rows → 1 canonical + 2 withdrawn). Researcher approved a full M67 `-Force` reconciliation; it ran 13/18 batches before hitting a truncation failure (see #1842) — remainder tracked as #1846. |
| #1841 | completed | Auto-raised duplicate of #1840's own failure signature — closed, pointed to #1840/#1842. |
| #1842 | **open, ready_for_approval with Researcher** | M49 Stage 1 batch failed: chunk 1/76 truncated (genuine max_tokens hit, confirmed via usage log: 27044 in / 40000 out / $0.68 real cost). Root cause revised twice as evidence came in (see Decisions below). Code fix built (`_chunk_verses_fixed_size`, verse-count chunking) and the companion config changes (#1843/#1844) were approved and applied — but **M49 itself was never actually retried live under the new chunking**; the session moved into the cost/architecture review before that happened. Carries into next session. |
| #1843 | completed | Reactivated `cfg_setting lexical.meaning_max_verses_per_batch` (value 5→1, inactive→active) per researcher instruction ("the units of operation is verses not strongs"). Proposed, approved by researcher ("yes"), applied, verified live. |
| #1844 | completed | Marked `cfg_setting lexical.meaning_max_strongs_per_batch` inactive (superseded by #1843). Proposed, approved, applied, verified live. |
| #1845 | completed | Auto-raised duplicate of the M67 batch-14/18 truncation — closed, pointed to #1846/#1842. |
| #1846 | completed | Follow-on to finish M67's 13 remaining verses under the new single-verse chunking. Ran live: 13/13 committed, **0 truncation failures**, $3.05 real spend (vs $8.25 preview) — confirms the chunking fix holds under real use. Surfaced one small unrelated finding (node-level duplicate residue) → filed as #1847. |
| #1847 | **open, raised, with Researcher** | Small, non-urgent: 2 verses (2Cor.8.16, 2Pet.1.5) carry pre-existing duplicate `ib_node` citations of the identical occurrence, underneath an already-correctly-consolidated single observation. Residue from earlier dedup rework (11:19–12:31, before this session), not created by anything this session did. Not building without researcher sign-off (per the no-offline-script-touches-old-data principle). |
| #1838 | unchanged, carried forward | Pre-existing from before this session (Stage 1 build for M67, `ready_for_approval` with Researcher) — not touched this session. |

## Files / deliverables changed

- `iba/app/handlers/lexical.py` — added `_chunk_verses_fixed_size()` (fixed verse-count chunking);
  `meaning()` now calls it instead of `_chunk_verses_by_strong_density()` (kept, unused, for
  provenance).
- `iba/app/lib/recordingpass.py` — `_is_per_occurrence_question()` now delegates to
  `_is_strong_specific_occurrence_question()` instead of keeping its own separate copy of the
  condition (the actual #1840 fix).
- `cfg_setting` (iba.db): `lexical.meaning_max_verses_per_batch` (5→1, reactivated),
  `lexical.meaning_max_strongs_per_batch` (marked inactive).
- `cfg_method_rule` (iba.db): inserted id=111, `translit-never-without-gloss` (step
  `lexical.meaning`).
- Memory (`~/.claude/projects/.../memory/`): three new feedback files —
  `feedback_powershell_dollar_escaping.md`, `feedback_escalation_reassign_requires_assignedto.md`,
  `feedback_verify_live_data_before_raising_design_question.md` — and `MEMORY.md` compacted (was
  over the 24.4KB read limit, trimmed to ~17.5KB) with pointers to the three new entries added.
- Generated reports (outputs/, research/discovery/, _analytics/) — escalation history exports,
  spine-check, CONFIG-REPORT regenerations, stage1-batch preview/run CSVs, stage1-coverage-
  validation CSVs. Routine artefacts of the work above, not separate deliverables.

## Decisions

**Researcher's own decisions (not self-correctable):**
- Approved the M67 `-Force` reconciliation for #1840 (real spend, ~$0.15–0.78/batch).
- Approved lowering the M49 chunk cap direction generally, then explicitly corrected the *unit*:
  "batching based on strongs is inappropriate, the units of operation is verses not strongs" —
  this reversed a documented 2026-09-21 decision (strong-density chunking was adopted specifically
  because a fixed verse count was found unsafe then). Flagged that conflict rather than silently
  overriding it.
- Approved `lexical.meaning_max_verses_per_batch=1` (#1843) and the companion #1844, explicitly
  ("yes"), after being shown the real per-verse density evidence.
- Approved the M67 13-verse cleanup run implicitly by approving the config change it depended on.
- Raised the decisive cost/architecture concern that the session did not resolve: real per-verse
  cost (~$0.25, confirmed from 4 live single-verse calls) extrapolated across the true 24,649-verse
  Stage 1 scope (confirmed via direct query, not a guess) is ~$6,150 — "prohibitive," and evidence
  of "something materially wrong." Correctly rejected the idea of narrowing question scope (AI
  self-selecting relevance has a 9-month track record of failing), and separately identified that
  the fixed ~7,245-token instructions block being resent on every single-verse call, uncached,
  adds roughly 179M tokens (~$537) of pure repetition across the full corpus — a real, previously
  unaddressed inefeciency (no prompt caching implemented anywhere in this codebase).

**Claude's self-correctable fixes (found and fixed directly, not escalated as judgment calls):**
- #1840's actual root cause (a predicate-function drift bug) — built, verified against live data,
  reported as done, not a design question (my first framing of it as a design tradeoff was wrong;
  corrected once the live rows were actually checked).
- #1841/#1845 — closed as duplicates of already-tracked items.
- Reassignment bug (setting `-NextAction ready_for_approval` without `-AssignedTo`, leaving items
  silently still assigned to Claude) — caught and corrected on #1804/#1837/#1840, saved to memory.
- A PowerShell string-escaping bug that silently corrupted dollar figures in two escalation
  comments — caught, corrected, saved to memory.

**Genuinely still open / unresolved at session end:**
- Whether/how to reduce the real fixed-overhead-repetition cost (prompt caching) — proposed, not
  built or tested.
- Whether the M0.8.1 answer format should be tightened (data showed M0.8.1 answers average LONGER
  than the M0.7 family's own answers, despite being a conceptually simpler check) — proposed, not
  built.
- M49 itself was never actually retried live under the new chunking fix.
- The researcher's larger question, unresolved: given the pattern of real defects found across
  ~10 redesigns over 9 months, whether this method/tooling approach is fit for purpose at all. The
  session ended on this note, explicitly not pushed toward a technical next step by Claude — the
  researcher asked to close with a session log rather than continue.

## Open items carried into next session

- **#1842** — M49 not yet retried live under the fixed chunking.
- **#1847** — small node-level duplicate cleanup, awaiting researcher sign-off.
- **#1838** — unchanged, pre-existing, `ready_for_approval` with Researcher.
- Prompt-caching implementation — proposed, not built.
- M0.8.1 answer-length tightening — proposed, not built.
- The open architecture/trust question the researcher raised — no technical action was agreed;
  next session should ask directly rather than assume where the researcher landed.

## Git state (this log's own completion trigger)
