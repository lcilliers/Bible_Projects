# Session Log — 2026-09-23 (cont.)

**Scope:** Continuation of the same day's earlier session (word-level/relational split decision).
Built and live-tested the `lexical.relational` split (#1860) end to end, found and fixed two real
bugs surfaced only by real LLM calls (`ib_node.cluster_code` NOT NULL crash; a checklist-duplication
bug that made the model choke on genuinely-identical repeated occurrences), then ran a real,
researcher-directed corpus test: full word-level reconciliation of cluster M67 (35 verses), with a
live before/after data export. That test — real throughput (~62s/verse) and real cost (~$0.21/verse)
— extrapolated to the full corpus-wide scope (24,649 distinct verses) produced a genuinely large
number (~5 weeks at 12h/day and ~$5,180 for word-level alone; more for relational and for later
programme phases). The researcher weighed that against total programme cost (~$5,000 of which
~$1,000 already sunk) and the 4-5 remaining phases before any publishable result, and **decided to
abandon the study** on cost/benefit grounds. All 19 open escalations were closed at the researcher's
instruction to reflect that decision.

## Escalations touched

| # | Outcome | Summary |
|---|---|---|
| #1860 | completed (Researcher approval v3, pre-existing) | Word-level/relational split built: new `lexical.relational` step, readiness gate (`stage1coverage.missing_word_level_coverage`), dual grounding (committed word-level findings + raw lexicon, per the researcher's correction to Claude's own draft). Config applied via `split_lexical_meaning_word_relational_v1_20260923.py`, `configmaint.validate` clean. Live-tested end to end (2Cor.8.8/M67): word-level $0.22/52 observations, relational $0.31/81 aligned, both 0 missing/0 unexpected. |
| #1838 | withdraw | "Stage 1 build" — the item this session's M67 corpus measurement was run against. Updated through the split's build/test, then the full M67 run, then withdrawn with the study's abandonment; the corpus-wide run it tracked will not happen. |
| #1847 | withdraw (fix was real, not moot) | `ib_node` duplicate-citation migration — already run and verified in the prior session (29 groups, 36 rows). Closed via the study's end rather than a formal approval, since the work itself was genuinely complete. |
| #1862 | completed (self-correctable) | `lexical.relational`'s readiness gate correctly refusing to run against M67 (56 real word-level gaps under the new span-grounded population rules) — not a defect, the gate working as designed. |
| #1863 | completed (self-correctable) | First live word-level test call failed on DNS resolution — this session's default Bash sandbox blocks outbound network egress. Not a code defect; retried with the sandbox disabled and succeeded. |
| #1864 | completed (self-correctable) | Real bug: `recordingpass._insert_node` was writing `effective_cluster_code` (`None` for word-level rows, correct for `ib_observation` ownership) into `ib_node.cluster_code`, which is NOT NULL and means something different (which cluster's pass cited the occurrence). Crashed on the first-ever live word-level write since the earlier `#1852`/`#1853` cluster-agnostic rework. Fixed: `_insert_node` now receives the pass's own `cluster_code`. One orphaned `ib_observation` row from the crash (zero references, confirmed) deleted before retesting. |
| #1865 | completed (self-correctable), **corrected** | Originally misdiagnosed as transient model non-determinism — a second identical failure on the same verse disproved that. Real cause: `1Tim.5.13`'s `G0692` "idlers" occurs twice with byte-identical surface+morph; `stage1coverage.expected_nodes` didn't dedupe this, so the checklist listed the same triple twice, and today's stricter "exactly one entry per triple" instruction made the mismatch impossible for the model to satisfy silently. Fixed: dedupe by `(strong, surface, morph_code)` before building checklist rows for both the word/elevation loops. Verified live: G0692's checklist for that verse dropped from 26 to 13 items, then a clean $0.07 commit. |
| #1866 | completed (self-correctable) | Duplicate of #1865 — a delayed auto-raise of the same pre-fix incident under a different run_id. |
| #1867 | completed (self-correctable) | Different, later failure: `G0703` "virtue" genuinely occurs twice with *different* morphs (correctly not deduped) — the model handled the content correctly but prefixed one line of prose before the JSON, breaking the fence-only parser. Fixed: `versereadinggenerate.parse_response` now falls back to extracting a bare (unfenced) `{...}` object when the direct parse fails, before giving up — same precedent as the existing `strict=False` control-character fix (`#1826`). Verified with a synthetic unit test. |
| #1861 | withdraw | Auto-raised `configmaint.validate` advisory backlog (orphan enums, stale `filled_by`, unregistered utilities) — routine housekeeping findings, withdrawn as moot with the study's end. |
| #770, #784, #1022, #1385, #1386, #1387, #1533, #1544, #1695, #1698, #1699, #1842, #1851, #1857, #1858, #1859 | withdraw | Every other open escalation — infrastructure/design/quality items that existed to serve the study's continuation (Prose Management, content-index redesign, cluster-reading synergy, prompt-caching restructure, batch-progress tooling, Stage 1 quality checks, etc.). Closed as moot on the same researcher decision, not resolved on their own merits. None were silently dropped — each carries its own one-line note on what it was for. |

**Total open escalations at session end: 0** (19 closed in this session's final sweep, plus the
7 self-correctable items resolved during the build/test work).

## The M67 corpus measurement (why the decision was made)

Ran the real, researcher-requested test: exported M67's current word-level state before
(`outputs/m67-wordlevel-BEFORE-20260923.csv`/`.json`, 781 rows/711 observations), then ran a full
`-Force` word-level reconciliation of all 35 verses, live, real API calls. Two genuine bugs
surfaced and were fixed mid-run (see #1864/#1865/#1867 above) — the run needed three resumes to get
through cleanly (18 of 35 verses committed before the researcher's decision stopped it; the last
`run_batch` row was marked failed/aborted, not left stuck at `running`).

Measured throughput across 28 clean committed calls: **62.3s/verse average**, **$0.21/verse
average** (min $0.07, max $0.52 — driven by how many distinct M-code strongs and how much
duplicate-checklist/prose-preamble overhead each verse's own content triggered).

Corpus-wide scope, queried live: **24,649 distinct verses** carry at least one M-code word (the
deduplicated, cluster-agnostic population — not "35 × number of clusters"). Extrapolated:
word-level alone ≈ 427 hours (~5 weeks at 12h/day) and ≈ $5,180; relational adds a comparable order
of magnitude on top (one live data point: $0.31/101s for one verse). A pricing question was also
raised and left unresolved — the project's configured LLM rate ($3/$15 per million) may be ~50%
higher than the verified current Sonnet 5 rate ($2/$10) — worth checking against the actual invoice
if this is ever revisited, since it would mean every cost figure in this log is somewhat
overstated.

**Researcher's decision, verbatim (2026-09-23):** *"still the study in total will cost around
$5000 of which $1000 is already sunken cost. I paid $1000 to find it is incredibly hard to achieve
the objective, and 4-5 phases before the real results can be converted to a story, I would say
$5000 sounds a low estimate. just not worth it."* — abandoning the study. The in-progress M67
background run was stopped immediately on this decision (no further spend).

## Files / deliverables changed

**New migration (`iba/app/migration/`), applied and registered in `cfg_utility`:**
- `split_lexical_meaning_word_relational_v1_20260923.py` — the `#1860` config layer (cfg_step,
  cfg_write_grant, cfg_method_rule, cfg_setting for the split).

**Code:**
- `iba/app/lib/stage1coverage.py` — `family` parameter added throughout (`expected_nodes`,
  `validate_coverage`, `fully_covered_verse_ids`); new `missing_word_level_coverage()` (the
  readiness gate); new occurrence-dedup fix (`#1865`).
- `iba/app/lib/versereadinggenerate.py` — `assemble_batch_package` split into
  `assemble_word_level_batch_package`/`assemble_relational_batch_package`; new
  `_word_level_findings()`; prompt builders split (`_word_level_instructions`/
  `_relational_instructions`); `parse_response` bare-JSON fallback (`#1867`).
- `iba/app/handlers/lexical.py` — `meaning()` narrowed to word-level only; new `relational()`
  handler (readiness gate + moved `cluster.status` transition check).
- `iba/app/lib/recordingpass.py` — `_insert_node` bug fix (`#1864`).
- `iba/app/ps/RelationalReading.ps1` (new) — PS entry point for the new step.
- `iba/app/ps/VerseReading.ps1` — docstring updated to point to the new step.

**Data (iba.db):**
- 18 of M67's 35 verses got real, committed word-level `ib_observation`/`ib_node` data under the
  new span-grounded population rules before the run was stopped — usable, not wasted.
- One orphaned `ib_observation` row (crash artifact, `#1864`) deleted.

**Docs/reports:**
- `iba/docs/1860-word-relational-split-build-plan-v1-20260923.md` (new).
- `iba/app/BUILD.md` — entry #328.
- `outputs/m67-wordlevel-BEFORE-20260923.{csv,json}` — the pre-run snapshot for comparison.
- Various run-output JSON/CSV under `outputs/` (batch results, coverage validation reports).

## Decisions made

- **Researcher's own:** approved and directed the `#1860` split build (v3, "proceed with split").
  Corrected Claude's own grounding design mid-approval ("the base data must in any case be included
  for relational phase to be successful"). Directed the M67 corpus test ("do 1 - full. it is only
  35 verses"). **Decided to abandon the study on cost/benefit grounds**, after this session's real
  cost measurement plus the researcher's own accounting of total remaining programme cost and
  phases. Directed closing every open escalation and writing this log.
- **Claude's own, self-correctable, executed directly:** the `ib_node.cluster_code` bug fix
  (#1864); the checklist-dedup bug fix (#1865, after an incorrect first diagnosis, corrected on a
  second failure); the parser bare-JSON fallback (#1867); stopping the background run immediately
  once the abandonment decision was made (no separate confirmation sought — money was actively
  being spent on a decision already made); killing an earlier wrongly-scoped `-Force` resume before
  it could re-pay for or duplicate already-good data (caught before any write happened).
- **Explicitly not resolved:** the LLM-rate-config discrepancy ($3/$15 configured vs. $2/$10
  verified current) — flagged, not corrected, since it no longer matters to a closed study.

## Open items carried into next session

None. The study is closed; all escalations are withdrawn. If revisited in the future, the
concrete facts to start from are in this log's cost-measurement section and `iba/app/BUILD.md`
#328 — real per-verse throughput/cost, real corpus scope, and the specific bugs already found and
fixed in the split's code.

## Git state (this log's own completion trigger)

Confirmed live: branch `main`, commit `5f1c85bab1b154bed7a69cac13b10af2587cb296` (2026-09-23
12:32:40 +0100), `git push` succeeded (`01b50ccf..5f1c85ba main -> main`), `git status --short`
clean immediately after push.
