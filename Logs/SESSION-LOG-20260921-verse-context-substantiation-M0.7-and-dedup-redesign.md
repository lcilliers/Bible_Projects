# Session Log — 2026-09-21 — Verse-context substantiation (M0.7) built; structured-key dedup redesign

**Scope, one line:** Corrected the pipeline's architecture (char-reading/char-answers must consume Stage-1 *observations*, never re-interpret raw verse content), designed and built the missing verse-context substantiation layer (M0.7.1-16), fixed 4 real bugs found live-testing it, and rebuilt the same/broaden/new dedup mechanism on structured keys after confirming the prose-similarity version never once fired correctly.

**Status:** #1806 and #1824 both `ready_for_approval` — researcher review pending. #1804 (the living pipeline-trace document) stays assigned to Claude per standing instruction, updated throughout. No escalation in this session was left silently unprogressed.

---

## 1. Catalogue status check → comprehensive gap-closure design (#1806)

Researcher asked whether the coverage CSV reflected the latest question handling, including never-answered questions and suggested new ones to cover gaps. Re-read the coverage mechanism fresh from live code (not from a stale prior report) and delivered `outputs/catalogue-coverage-audit-20260921-v2.md`+csv, then was asked to go further: **design a closure for every one of the 31 unanswerable/incomplete-data questions**, not just list them.

Delivered `outputs/gap-closure-design-20260921.md` — 5 categories by what it actually takes to close each gap:
- **A** (16 questions) — re-scope + dynamic Stage-1 feed
- **B** (4) — re-scope only
- **C** (2) — new Stage-1 pin
- **D** (5) — needs an unbuilt char-synergy stage (tracked separately on #1695)
- **E** (4) — science-extract, already designed under #1805

This first-pass design (Category A specifically) placed the new questions as direct, characteristic-scoped Stage-1 additions. That placement is now known wrong — see §2 — and the file has not yet been rewritten to reflect the correction (carried to next session, §5).

## 2. Architecture correction: verse-reading must feed char-reading, not answer for it

Researcher, verbatim: *"Category A: D10*, D3, D7, F0 are all questions for stage char-reading, but it is dependent on the output of verse-reading observations that need to produce a observations that supports the char-reading. This means new questions that is pure verse context must be in place that will produce the outputs that the char-reading use. this is a missing link for the transition between verse-context and char implications in char-reading."*

Then generalized to Categories B/C/D: *"nothing is prompting stage 1 to generate the observation based on the word and verse context to provide the basis for the char related questions to be answered."* And named the constraint driving it: *"char-reading (determination of the sub groups) and char-answers (char behaviours) both should only use the output (observations) from stage 1 (verse context)."*

I initially misread this as "move these into Stage 1, scoped like the existing `M0.6.5`." Two further corrections followed, each tightening the design:

- **Static vs interpretive data, not a flat re-scope.** Researcher: *"Stage char-reading, and char-answers use two types of data: verse-context interpretive data and static data... The T1-T9 was an attempt to show how it all fits together, and these principles still apply. the analytic pipeline is indeed the latter part of T1-T9. I don't want to pull the pipeline in its current format apart and start over again. we now need to focus on getting the observations output of verse-reading to substantiate every char related question."* This grounds the fix in the existing `WA-verse-reading-technique-v4-2026-08-05.md` T1-T9 doc (confirmed still valid, not superseded) rather than inventing a new framework.
- **Characteristic-agnostic, work backward from the char question.** Researcher: *"it should not be necessary for char analysis to re-run a verse interpretation... Start at the char question. work question by question. determine what must be known from the verse to answer the question. then design the verse-reading question that will generate the data in the right format. the difference is verse-reading does not know, and does not answer to a char, it purely based on the meaning of the words and there inter relationship."* This corrected my second wrong instinct — keeping the new questions characteristic-scoped like `M0.6.5`.
- **Per-occurrence, not front-loaded-once.** Researcher: *"yes - be careful because we know that a strong can be different in different verses, and that difference must create separate observations, each of which will have its verses associated with that particular variation."* This ruled out treating the new questions like `M0.1`'s once-per-strong-ever battery.

Mid-cycle, an explicit exhaustion/frustration exchange: *"I have now been working 12 hours straight just to unpick and reset the pipeline... where are we now, what is not clear, why cant you just do it right in the first place... a mixture of what is there, what is not there and what is wrong and unpicking it without doing it myself seems a lost case."* I gave an honest self-assessment in reply, naming the actual failure mode: *"every round this session, I was pattern-matching to the nearest existing code mechanism instead of reasoning from the actual principle underneath."* Researcher's response shifted the working mode: *"not sure how to evaluate anything any longer, so I will just approve everything and then test the results."*

Net design, confirmed correct on the fourth pass: new questions are **verse-first, word-level, per-occurrence, characteristic-agnostic** Stage-1 observations. Built as the `M0.7` family (§3).

## 3. Built and verified: M0.7.1–16 verse-context substantiation

Work sequence, deliberately not rushed past the point where Stage 3/4 would lose their only current data source:

1. **Conciseness rule** (`add_concise_verse_specific_rule_v1_20260921.py`) — new `cfg_method_rule` `concise-and-verse-specific-obs-text` for `lexical.meaning`/`cluster.reading`/`cluster.answer`, closing the root cause behind #1824 (generic LLM prose made dedup undetectable).
2. **`M0.6.5` enriched + `M0.6.6` added** (`enrich_verse_relational_reading_v1_20260921.py`) — relational-reading depth fix (escalation #1819).
3. **`M0.1`/`M0.5` "primary term" fix** (`fix_primary_term_terminology_v1_20260921.py`) — undefined-referent fix (#1822).
4. **`M0.7.1`-`16` inserted** (`add_verse_substantiation_questions_v1_20260921.py`) — new component `M0.7`, tier `M0`, scope `Verse-context`, catalogue_version `v8-verse-substantiation-20260921`. Word-level, per-occurrence, no characteristic framing.
5. **Wired into Stage 1** (`iba/app/lib/versereadinggenerate.py`): selection query extended to include `M0.7%`; `assemble_batch_package()` extended so `M0.7` questions are asked for every M-code strong in a verse-batch (not just the cluster's own members, matching the existing front-loading pattern for `M0.1`/`M0.5`, but WITHOUT the once-ever skip — `M0.7` is asked fresh per occurrence, per the per-occurrence correction in §2); `_instructions()` gained a "THREE KINDS OF QUESTION" section explaining the distinction to the LLM; output JSON shape extended with `meaning_keywords` (built ahead for #1824, see §4).
6. **Applied live** (#1806 v21) and confirmed via `assemble_batch_package` no-API-call structural test before spending on a real run.
7. **First live test, cluster M67** — 4 real failures in sequence, each individually diagnosed and fixed (full detail in §4's error log). Fifth attempt confirmed clean: **18/18 batches, $3.12, 845 real M0.7 observations across 42 strongs**, content spot-checked directly against source verses.

Recorded as BUILD.md #310 (mechanism built + verified structurally) and #311 (live test result).

## 4. M67 live-test saga — 4 bugs, each root-caused before the next fix was written

| # | Failure (escalation) | Root cause | Fix |
|---|---|---|---|
| 1 | #1825 — chunk 1/4, invalid JSON at char 0 | `M0.7` roughly doubled Stage 1's per-strong question count (14→30); response truncated before the closing fence | First attempt: halve `lexical.meaning_max_verses_per_batch` (10→5) |
| 2 | #1826 — chunk 1/4, unterminated string (retest) | Same truncation, reproduced — proved the verse-count halving was the wrong lever, not just the wrong number | Queried real M67 data: strong density varies 3.5x (6–21 distinct M-code strongs) across same-size 5-verse chunks, so a fixed verse-count cap can never reliably bound output |
| 3 | #1827 — chunk 4/7, invalid control character | A *different* bug surfaced because the batch halving partially worked (chunks 1-3 succeeded, 170 real observations confirmed good) — unescaped control character (raw newline) inside `obs_text` | Reproduced in isolation first (`json.loads` strict vs `strict=False` on a synthetic string) before touching live code; applied `json.loads(candidate, strict=False)` across all 5 stage-generator modules sharing the parse pattern |
| 4 | #1828 — chunk 5/7, same truncation signature | Confirmed batch-halving alone was insufficient even with the control-character fix in place | Built the real fix: `_chunk_verses_by_strong_density()` in `iba/app/handlers/lexical.py`, replacing verse-count chunking with cumulative-M-code-strong-count chunking (cap=8, new setting `lexical.meaning_max_strongs_per_batch`); verified directly against real M67 data (18 resulting chunks, all ≤8 strongs) before spending on another live call |

All 4 resolved and closed same session; 5th attempt (post-fix) ran clean end to end.

## 5. Structured-key dedup rebuild (#1824)

Researcher challenge, opening this thread: *"I thought the rule is that the same observation should never be repeated, if another verse or instance in the same verse refers to the same observation then it creates another node, not another observation... I doubt if these rules have ever been applied."* Queried real data: **0 of 378 real `H3034`/`M0.1.1` comparison pairs ever crossed the `difflib.SequenceMatcher` 0.85 threshold** (max observed 0.51) — confirmed the dedup mechanism had never once fired correctly against real LLM paraphrase variance, not just under-tuned.

Researcher's own diagnosis of why: *"LLM simply need to do the interpretation without trying to figure out if this is a new or existing observation. LLM output is filed in Json. then as a separate operation from LLM, CC will check if this observation already exist. Where it failed in the clusters already analysed is because LLM output was not generic nonsense, and not concide and specific to the verse, so it was impossible to make any differentiation visible."* — tying back to the design flow: *"CC -> json input LLM -> json output CC -> DB update CC -next phase json input"* and to the conciseness rule already built in §3 step 1.

My first fix attempt (prompt-only conciseness) was superseded by a researcher correction posted directly on the escalation (not in chat): *"similarity is not matching sentences. Similarly to matching keys. For instance to check for matching word meaning: match a) surface b) meaning extraction keywords c) morph."*

Built and verified (scoped to the new `M0.7` family only — `M0.1`/`M0.5` already have a separate, working per-strong skip-check from #1820):
- `add_meaning_keywords_column_v1_20260921.py` — new `ib_observation.meaning_keywords` column (JSON array), registered in `cfg_column`. Hit a `notnull`-as-SQL-keyword syntax error in the INSERT column list (fixed by quoting `"notnull"`), then discovered the `ALTER TABLE` had already taken effect despite the subsequent `except`/rollback — SQLite DDL isn't rolled back by the surrounding transaction the way the `try/except` assumed; re-ran just the `cfg_column` INSERT once the syntax was fixed and confirmed both the column and its registration present.
- `recordingpass.py`: `_insert_observation()` takes and stores `meaning_keywords`; new `_keyword_match_candidate()` requires BOTH keyword overlap (`meaning_keywords`) AND matching `(surface, morph_code)` against a candidate's existing `ib_node` citations before treating two observations as the same; `record_one_observation()` checks this structured path FIRST, falling back to the old prose-similarity path only where `meaning_keywords` is absent (i.e. every stage except the new `M0.7` family, for now).
- `versereadinggenerate.py`: output JSON shape instructs the LLM to fill `meaning_keywords` only for `M0.7.1`-`16`.
- Verified 3 ways: unit-level synthetic match/no-match cases, a prompt-wiring check (confirmed the field actually reaches the LLM instructions), and a full integration test with rollback against real data.

Recorded as BUILD.md #312.

## 6. Escalations touched this session

| id | outcome |
|---|---|
| #1805 | completed — science-question build design proposed (source located, 99 files, 1:1 cluster coverage) |
| #1806 | re-assigned, `ready_for_approval` — coverage audit, wording review, gap-closure design, M0.7 build, all consolidated as the thread's single index |
| #1814 | completed — deep catalogue wording review, v4 |
| #1815 | completed as scoped — `_effective_cluster_code` misattribution root-caused, fix is 2 lines pending researcher's pick of (a)/(b), not applied yet |
| #1816 | completed — prose tables exempted from research_db exclusion, applied live |
| #1817 | completed — 3 of 9 unmapped strongs reclassified to real T-codes, applied live |
| #1818 | completed — catalogue column-alignment gaps fixed, applied live |
| #1819 | completed — `M0.6.5` enriched + `M0.6.6` added, wired and verified |
| #1820 | completed — Stage 1 word-level battery skip-check extended to home strongs too |
| #1821 | completed — `compute_question_checks` undercount root-caused (fix tracked on #1820) |
| #1822 | completed — "the primary term" terminology fixed across 4 rows |
| #1823 | completed — 15 dead-gate-citation fixes, 3 dependent reports regenerated |
| #1824 | re-assigned, `ready_for_approval` — structured-key dedup built and verified 3 ways |
| #1825 | completed — M67 truncation, 1st occurrence |
| #1826 | completed — M67 truncation, 2nd occurrence (proved verse-count lever wrong) |
| #1827 | completed — control-character JSON bug, `strict=False` fix |
| #1828 | completed — M67 truncation, 3rd occurrence (drove the real strong-density fix) |
| #1804 | in-progress, stays assigned to Claude — living pipeline-trace document, updated throughout (v4→v12 this session) |
| #1695 | in-progress, untouched this session — char-synergy stage design (Category D dependency) |
| #1698 | in-progress, untouched this session — synthesis cross-cluster gap |

## 7. Files created or changed

**Code:**
- `iba/app/handlers/lexical.py` — `_chunk_verses_by_strong_density()`, new setting `lexical.meaning_max_strongs_per_batch`
- `iba/app/lib/versereadinggenerate.py` — M0.7 selection/wiring, `_prior_network_context()`, `meaning_keywords` output field, `_instructions()` signature change
- `iba/app/lib/recordingpass.py` — `meaning_keywords` param, `_keyword_match_candidate()`, structured-key-first matching in `record_one_observation()`
- `iba/app/lib/subgroupgenerate.py`, `charreadinggenerate.py`, `charanswergenerate.py`, `lexicalenrichgenerate.py` — `json.loads(candidate, strict=False)`
- `iba/app/lib/lexical.py` — (batching-adjacent change, part of the same working set)

**Migrations (registered in `cfg_utility`, run, `inactive=1`):**
- `add_concise_verse_specific_rule_v1_20260921.py`
- `enrich_verse_relational_reading_v1_20260921.py`
- `fix_primary_term_terminology_v1_20260921.py`
- `add_verse_substantiation_questions_v1_20260921.py`
- `add_meaning_keywords_column_v1_20260921.py`
- `fix_dead_gate_citations_v1_20260921.py`
- `assign_1807_unmapped_strongs_v1_20260921.py`
- `catalogue_column_governance_v1_20260921.py`
- `apply_catalogue_wording_v1_20260921.py`

**Documentation record:**
- `iba/app/BUILD.md` — #305 through #312
- `outputs/cluster-reading-pipeline-full-trace-20260920-v2.md` — Findings 12-17 plus multiple dated addenda (M67 saga, #1824 resolution)
- `outputs/gap-closure-design-20260921.md` — 5-category design for all 31 gaps (Category A placement now superseded, not yet rewritten — see §8)
- Regenerated report chain (v2→v8 wording review, v2→v5 coverage audit, v2→v4 wiring audit, v2→v3 density reports) — each round triggered by a real fix landing, not cosmetic re-runs
- `outputs/configs/CONFIG-REPORT.md`, `research/discovery/lexical-readiness.md`, `research/discovery/spine-check.md` — refreshed snapshots

**Deliverables (this session's outputs, `outputs/` and `research/discovery/`):** catalogue-coverage-audit (v2-v5), catalogue-question-wording-review (v2-v8), pipeline-wiring-audit (v2-v4), population/density reports (v2-v3), gap-closure-design, cluster-strong-span-verselexical-crosscheck, observations-based-on-incorrect-role, verse-reading-observations-exposed-to-contaminated-role.

## 8. Decisions — researcher's own vs Claude self-correctable

**Researcher's own (design/architecture, not mine to make unilaterally):**
- The static-vs-interpretive data split governing what char-reading/char-answers may use.
- Verse-reading must be characteristic-agnostic ("does not know, and does not answer to a char").
- `M0.7`-family questions must be per-occurrence, not front-loaded once per strong.
- Structured-key matching (surface + meaning-extraction keywords + morph) replaces prose similarity for the dedup mechanism.
- Working mode shift mid-session: approve on the researcher's trust, verify via live-tested results rather than round-by-round re-litigation.

**Claude self-correctable (found and fixed without needing a researcher decision):**
- `notnull` SQL-keyword quoting in the `cfg_column` INSERT.
- Partial-migration state after the DDL/rollback mismatch (manually completed the `cfg_column` registration).
- `json.loads` control-character rejection (`strict=False`).
- Verse-count batching's failure to bound output (replaced with strong-density batching) — root-caused and fixed without further researcher input once the real cause (density variance, not batch size per se) was confirmed against real data.
- Wrong `Escalation.ps1` actions attempted (`Update`/`AnswerRun` on dispatcher-tied and `decision_required` items) — corrected to `ResolveSelfCorrectable`/`Update` as appropriate.

**Not self-correctable — surfaced and escalated, not decided by Claude:**
- `#1815` (`_effective_cluster_code` misattribution) — 2 options proposed, researcher's pick still pending.
- `#1810` redo-scope question (7,046 pre-fix observations) — open.
- `M83`'s `MultipleOverCapStrongs` blocker — open.
- `M0.6.5`/`M0.6.6`'s own characteristic-scoped design — flagged as predating the "verse-reading doesn't know about a char" correction, tension not resolved.

## 9. Open items carried into the next session

- Rewrite `gap-closure-design-20260921.md`'s Category A section to reflect the corrected architecture (M0.7-style substantiation feeding Stage 3, not direct characteristic-scoped Stage-1 placement).
- Wire Stage 3 (`charreadinggenerate.py`) to actually consume `M0.7` observations and answer the original char-questions (`D10.1.1` etc.) — currently writes 0 real question_codes; the materially bigger next step, deliberately not rushed into this session.
- Stage 3/4's raw-data-access removal (`_full_occurrences`/`_meaning_sources`) — must wait until the M0.7 replacement data path is actually consumed, not before (a near-miss this session — caught before acting).
- Category D (5 questions) — needs the unbuilt char-synergy stage, tracked on #1695.
- `#1805` science-extract wiring — design proposed on #1805, not built.
- `#1815` `_effective_cluster_code` fix — pending researcher's pick of option (a) or (b).
- `#1821` `compute_question_checks` undercount — root cause tracked on #1820, fix itself not separately applied.
- `#1810` redo-scope question (7,046 pre-fix observations) — open.
- `M83`/`A_general_seeking`'s `MultipleOverCapStrongs` blocker — open.
- A minor unregistered `not-stated` tag gap (1 occurrence, correctly refused rather than corrupted) — not yet registered.
- #1804 (living trace document) stays assigned to Claude, per standing instruction, until the #1806 gap-closure work is complete.

## 10. Git state

- Branch: `main`
- Commit: `38b410faa5cf47ab74316ddd946ff07f3e3bc44e` (2026-09-22T04:07:58+01:00) — "session 20260921: verse-context substantiation (M0.7) built, dedup redesigned onto structured keys"
- Pushed: `398ea944..38b410fa main -> main` — confirmed via `git push`
- `git status` after push: `On branch main. Your branch is up to date with 'origin/main'. nothing to commit, working tree clean.`

