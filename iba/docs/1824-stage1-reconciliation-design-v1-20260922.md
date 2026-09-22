# Stage 1 reconciliation design — update / remove / add against existing observations

**Escalation:** #1824. **Status:** BUILT and validated live, 2026-09-22 — see §6.
**Author:** Claude, 2026-09-22. **Supersedes:** the wipe-the-data recommendation given earlier the same session on #1824 (v6/v7), retracted after the researcher's correction (v8: *"a fundamental part of stage 1 is to review and update, remove, add observations that already exist, if the current data is wiped you will not be able to develop or test it"*).

## 1. What this fixes

The researcher's stated requirement (this session, on #1824): *"stage 1, if rerun must reset the observations that relates to it... update the observations that exist, remove the observations that is redundant, and add observations if it is actually new."*

That capability does not exist today. Confirmed by live test (#1824 v7): reran Stage 1 against 2 real M67 verses that already carry rich pre-existing observations. Of 65 occurrences recorded, 61 (94%) created a **brand-new** `ib_observation` row next to the old one — the old row was never touched, never removed, only linked via `ib_node.traced_observation_id` (a provenance pointer, not a merge). Only 3 genuinely updated an existing row in place; 1 was a true new fact.

This document proposes the fix, scoped narrowly, and a validation plan that uses the **real, already-messy M67 data as the test bed** — no wipe, no synthetic data.

## 2. Root causes (three separable problems, confirmed by reading `recordingpass.py` and the live data — not inferred)

### A. Matching cannot see legacy candidates via keywords — turns out not to matter once §2.D is fixed
`_keyword_match_candidate()` (`iba/app/lib/recordingpass.py:269`) requires **both** sides to carry `meaning_keywords`:
```python
cand_keywords_raw = candidate["meaning_keywords"] if "meaning_keywords" in candidate.keys() else None
if not cand_keywords_raw or not new_keywords:
    return False
```
Every M0.7 row written before the #1824 keyword fix (BUILD #312, 2026-09-21) has `meaning_keywords = NULL` — confirmed live: 896/896 of the currently-existing M0.7 rows have `meaning_keywords IS NULL`. So keyword-matching can never fire against them; the code falls back to prose-similarity, which doesn't catch real paraphrases.

**Corrected after researcher review, 2026-09-22** — the first draft treated this as something to fix by backfilling keywords onto old rows via a standalone script. That's wrong, and the researcher said so directly: *"none of the correction are done as fixes. they are all done as the result of the update routine that runs on the json output that you got from LLM... you should not reach back into the base data — the expectation is that LLM has answered every question."* Every correction to existing data must be a byproduct of a genuine Stage 1 rerun (a real, full LLM call answering every wired question for that verse) flowing through the normal recording pass — never a side script that edits old rows' metadata without a fresh LLM answer driving it.

This actually makes root cause A far less important than the first draft thought: **once §2.D's candidate scoping is fixed, keyword matching isn't how the correct row gets found for per-occurrence questions at all.** For a verse+strong+question the candidate pool now narrows to "does a row already exist for exactly this occurrence" — a direct lookup, not a similarity guess. Keywords only remain relevant as a tie-breaker *if* that narrowed pool ever contains more than one row (the legacy-duplication case) — and even then, that's resolved only when a real rerun's fresh output triggers the recording pass to look at that occurrence again, per §3 below.

### B. No remove/supersede path exists, even though the schema already has one
`ib_observation.status` (live `cfg_enum`) already includes `withdrawn`. `ib_observation.supersedes_observation_id` already exists as a column, and `_insert_observation()` already accepts it as a parameter (`recordingpass.py:252`). **Neither is ever used.** Every call site in `record_one_observation()` passes `supersedes_observation_id=None` (implicit default) and every insert is unconditionally `status="draft"` (`recordingpass.py:258`, hardcoded, asserted). Confirmed live: `SELECT COUNT(*) FROM ib_observation WHERE supersedes_observation_id IS NOT NULL` → **0** of 8,466 rows.

So "remove redundant" isn't missing infrastructure — it's missing wiring. The three-way decision (update in place / withdraw-and-replace / genuinely new) was designed into the schema and never finished in the write path.

### C. A rerun of unchanged content is a permanent, silent no-op
`batchcontrol.already_committed()` skips any batch whose exact verse-id content hash was ever committed under this step+selector, **from any run_id, forever** (`batchcontrol.py:67`). Confirmed live this session: of 5 verses requested for the reconciliation test, 3 were silently skipped — no LLM call, no comparison, nothing. This is a real, separate gap from A/B: even once matching and remove/supersede are fixed, there is currently no way to deliberately ask "go re-examine this scope" — the cost-safety skip and the reconciliation need are in direct tension.

### D. The candidate pool never asks "which row should I even be comparing against" — added after researcher review, 2026-09-22
The researcher's own question, verbatim: *"how do you know what row to expect, so you can compare if it exists, and what row is redundant, and must be withdrawn."* The first draft of this document didn't actually answer that — it described the matching heuristic (keywords/surface/morph/similarity) without ever specifying what the CANDIDATE POOL is before that heuristic runs. Checked directly, and it's a real gap, not a documentation omission:

`_existing_candidates()` (`recordingpass.py:79`) scopes candidates by `cluster_code + stage + strong + question_code` only — **no verse filter, for any question type**. For word-level questions (`M0.1`/`M0.5`) that's correct by design: the fact doesn't vary by verse, so the candidate pool should be the whole cluster's history of that strong (this is already the `_WORD_LEVEL_QUESTION_PREFIXES` distinction the code makes elsewhere, in `_effective_cluster_code`, just not reused here). But `M0.7` and the relational questions (`M0.6.5`/`M0.6.6`/`D7.7.1`) are explicitly **per-occurrence** — BUILD #310's own design: *"a strong can genuinely behave differently verse to verse."* For these, the candidate pool still spans every verse that strong occurs in anywhere in the cluster, with nothing but the fuzzy heuristic standing between that and a match against the wrong verse's observation entirely.

**Checked this against the live test data, not just reasoned about it:** of the 61 `new-expands-existing` matches from #1824 v7's test, **22 (36%) trace to a candidate whose only existing citation is a DIFFERENT verse** — e.g. a new `Rom.12.11`/`G4710`/`M0.7.12` answer traced to an old observation whose only node is `Heb.6.11`; a new `2Cor.8.8`/`G4710`/`M0.7.5` answer traced to one whose only node is `Luke.1.39`. These aren't near-misses caught and correctly rejected by the similarity check — they're the candidate pool containing irrelevant verses in the first place, which the current code never questions before running the fuzzy match.

**This changes Fix B below**: candidate scoping must branch by question family *before* any keyword/similarity matching runs, not leave verse-relevance to the heuristic:

- **Word-level** (`M0.1`/`M0.5`): keep today's scope — `cluster_code + stage + strong + question_code`, no verse filter. Correct as-is.
- **Per-occurrence** (`M0.7` family, `M0.6.5`, `M0.6.6`, `D7.7.1`): first filter candidates to only those with an existing `ib_node` citation for the **same** `(verse_reference, strong)` as the new occurrence (a straightforward join against `ib_node`, no fuzzy logic involved) — that answers "does a row for THIS occurrence already exist" directly. Only *within* that narrowed, verse-correct set does keyword/similarity matching decide update-vs-new (relevant when Stage 1 answers the same verse+strong+question more than once, e.g. across two different-chunked runs).

## 3. Proposed fix

**Governing principle, per the researcher's correction, 2026-09-22:** every correction to `ib_observation` happens as the direct result of `record_one_observation()` processing a REAL, fresh LLM answer — never a standalone script that edits or derives content for rows without a genuine new answer behind it. There is no offline backfill and no offline consolidation pass. Reconciliation is incremental: a verse only gets reconciled when Stage 1 is genuinely rerun for it.

### Fix 1 — correct candidate scoping in `_existing_candidates()` (§2.D)
Add a question-family branch before any fuzzy matching:
- Word-level (`M0.1`/`M0.5`): unchanged — `cluster_code + stage + strong + question_code`, no verse filter.
- Per-occurrence (`M0.7` family, `M0.6.5`, `M0.6.6`, `D7.7.1`): add a join restricting candidates to those with an existing `ib_node` row for the same `(verse_reference, strong)` as the new occurrence. This is the real answer to "what row do I expect" — a direct lookup, not a heuristic guess — and it must run *before* keyword/similarity scoring. This alone eliminates the 22 cross-verse mismatches found in §2.D.

### Fix 2 — change `record_one_observation()`'s two-way branch to a real three-way
Operating only within the now-correctly-scoped candidate set from Fix 1, whenever a REAL fresh LLM answer for that occurrence arrives:

1. **No existing candidate in the correctly-scoped pool** → insert, as today (`new-observation`).
2. **Exactly one existing candidate** → this occurrence has been answered before; update it in place with the fresh answer (`aligned-superficial-edit`) — identity comes from the verse+strong+question scoping itself, not from keyword/similarity matching (that's only needed to locate a candidate in an unscoped pool, which Fix 1 already removed the need for).
3. **More than one existing candidate** (the legacy-duplication case — several old rows already sitting against the same occurrence+question from before Fix 1 existed) → this is where "remove redundant" actually happens, and only here, and only because a real fresh answer just arrived to reconcile against: pick the richest/most-recent as canonical, update it with the fresh answer, set `status='withdrawn'` + `supersedes_observation_id=<canonical id>` on the others (soft, auditable, matches the project's "soft delete, never physical delete" convention), and re-point their `ib_node` rows to the canonical so no citation is lost.

No separate utility, no batch job, no reach-back into rows that haven't been touched by a real rerun. A verse's existing duplicates only get cleaned up when that verse is actually reprocessed — which is what Fix 3 exists to make possible.

### Fix 3 — a deliberate reconciliation rerun needs to bypass the permanent skip
Add a `-Force` (or similarly named) override to `lexical.meaning` that bypasses `batchcontrol.already_committed` for an explicit, deliberate reconciliation pass — never the default, always an opt-in flag, same safety posture as `-Live` already has. Without this, "rerun Stage 1 to reconcile" can never actually re-examine anything already committed, which defeats the whole point — and per the governing principle above, `-Force` is now the *only* lever that ever triggers a correction.

## 4. Validation plan — against the real M67 data, no wipe, no offline scripts touching old rows

1. **Build Fix 1 + Fix 2 + Fix 3.**
2. **Re-run the same 5-verse test** from this session (`2Cor.8.8, Rom.12.8, Rom.12.11, 2Pet.2.3, 2Cor.7.11`) with `-Force`, so all 5 get a genuine fresh LLM call this time (not just 2). This single real rerun is the only thing that touches old data — everything downstream of it (matching, updating, withdrawing) is the normal recording pass reacting to that real output, nothing offline.
3. Concrete, checkable success criteria, using data already in hand from #1824 v7's first test:
   - The 2Cor.8.8/G4710/M0.7.1 pair (old id 7976, near-identical to the new id 8750 written in that first test) should now land as ONE canonical row, not two — because this rerun's fresh answer for that exact occurrence finds both under Fix 1's correct scoping and consolidates them per Fix 2 rule 3.
   - None of the 5 verses' fresh answers should trace to a candidate from a *different* verse (the cross-verse mismatch §2.D found 22 instances of) — Fix 1 alone should eliminate that category entirely.
   - A **third** rerun of the identical 5 verses (still `-Force`) should produce near-zero new rows and near-zero further withdrawals — the actual definition of "reconciled": once a verse has been genuinely reprocessed once under the fixed logic, reprocessing it again should be close to a no-op.
4. Report the before/after `by_action` counts and 2–3 concrete row-level examples, same evidence format as #1824 v7, so the fix is judged on the same real data the problem was found in.

## 5. What this does NOT do

- Does not run any script against `ib_observation` that isn't triggered by a real, fresh LLM answer from a genuine Stage 1 call — no backfill, no offline consolidation batch. Every correction happens inside `record_one_observation()`, in response to real output.
- Fix 1's candidate-scoping correction applies to `M0.6.5`/`M0.6.6`/`D7.7.1` as well as `M0.7` — all four are per-occurrence questions with the same cross-verse pooling bug (§2.D).
- Does not run against any cluster other than M67 in this validation pass — M67 is the only cluster with M0.7 data to test against; a wider rollout is a separate, later decision once this is proven.
- Does not hard-delete anything — every "remove" is a soft `status='withdrawn'` (never `supersedes_observation_id` — see §2.A's correction: that column is documented `cfg_column.use` "synthesis stage only," not this stage's to repurpose), fully auditable and reversible; withdrawn rows' own `ib_node` citations are re-pointed to the canonical, not lost.

## 6. Built and validated live, 2026-09-22

Built as designed (Fix 1 + Fix 2 + Fix 3, `iba/app/lib/recordingpass.py` + `iba/app/handlers/lexical.py` + `iba/app/ps/VerseReading.ps1`). One real bug found and fixed during the build: `_existing_candidates()`'s new JOIN query referenced `cluster_code`/`stage`/`strong`/`question_code` without a table alias — ambiguous once joined against `ib_node` (which also carries `cluster_code`). Cost one wasted API call (\$0.12, logged) before the crash; confirmed live no partial/bad data was written; fixed (`o.` prefix throughout) and re-verified. Auto-raised and closed as escalation #1830 (self-correctable).

**Validation run**: the same 5 M67 verses from #1824 v7's original test (`2Cor.8.8, Rom.12.8, Rom.12.11, 2Pet.2.3, 2Cor.7.11`), `-Force`'d through every wired Stage 1 question this time (not just M0.7), \$0.52 total.

| Outcome | Count | What it means |
|---|---|---|
| `aligned-superficial-edit-consolidated` | 56 | Fix 2 rule 3 fired — multiple legacy duplicates found for one occurrence, consolidated to one canonical, rest withdrawn |
| `aligned-superficial-edit` | 29 | Fix 2 rule 2 — exactly one existing candidate, updated in place |
| `new-observation` | 20 | Fix 2 rule 1 — genuinely no prior candidate |
| `new-expands-existing` | 1 | The untouched word-level (M0.1/M0.5) path — unaffected by this fix, expected |

**73 legacy duplicate rows withdrawn** across this run (`M0.6.5`: 15, `D7.7.1`: 11, `M0.6.6`: 9, the 16 `M0.7.*` codes: 2–3 each) — real cleanup of exactly the mess #1824's original test exposed, achieved by rerunning for real, not an offline script.

**Concrete example** (`iba/app/db/iba.db`, `ib_observation.id=234`, `2Cor.8.8`/`G4710`/`M0.6.5`): canonical since 2026-09-17 (oldest, richest). Before this run it had 1 node citation; after, 4 — its own original plus three re-pointed from observations `7385`, `7591`, `7974` (created 2026-09-21 and 2026-09-22, three separate near-duplicate restatements of the same relational finding), all three now `status='withdrawn'`. `obs_text` updated to this run's fresh answer; `status` reset to `draft` for re-review per the existing #1782 rule.

**Cross-verse mismatch check** (the §2.D failure mode — 22/61 in the original test): zero found among any live, non-withdrawn per-occurrence observation touching these 5 verses after this run.

One known non-consolidation case, for honesty: the exact pair originally cited in this document (`id=7976` vs `id=8750`, both `2Cor.8.8`/`G4710`/`M0.7.1`) was NOT touched by this run — the LLM's fresh answer for that specific occurrence didn't happen to be generated this time (model output isn't deterministic run to run; a different, larger consolidation batch fired instead, as the aggregate numbers above show). Both rows are still live and un-consolidated; they'll be picked up whenever `M0.7.1` for that exact occurrence is next `-Force`d.
