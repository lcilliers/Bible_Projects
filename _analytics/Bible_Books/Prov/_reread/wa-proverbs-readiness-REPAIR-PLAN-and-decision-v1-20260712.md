# Proverbs readiness — repair plan + decision request (v1, 2026-07-12)

> **RESOLVED 2026-07-12 (researcher):** decision = **registry path (i)** (existing-registry-first; new rarely). Role model corrected — `char_candidate` (seed) vs `role` (read-assigned) MAY differ; `qualifier` is VALID; defects are **D1** (lexical w/ null role → backfill) and **D2** (lexical only on `characteristic`). These are baked into the instruction §2 and the corrected runner. **Current verdict: `wa-proverbs-readiness-REPORT-v2-20260712.md`** (1 red I4, amber I2/D2/I8). True pre-read blockers = **I2 onboarding (~30 terms + 104 records)** and **I4 v2 passages**; D2/I8 are read-stage. The §1–§3 framing below is superseded by that; §4–§5 sequence stands. Next segment: the Stage-1 onboarding worklist.

> The readiness assessment returned **NOT READY**. On drilling into each gap to repair it, **none is a clean mechanical fix** — every one either (a) hinges on the *register-terms-vs-relax-registry* architecture decision the 2026-07-11 session **put to the researcher and did not resolve** (`verse-analysis/psalms/_model/wa-evidence-261-orphans-18-passages-and-char-model-20260711.md`), (b) needs a **v2 candidate-driven passage builder that does not exist yet**, or (c) is a **stale label the re-read self-resolves**. So I stopped short of writing to the DB. This doc gives the precise blocker anatomy, my recommendation, and the decision I need to proceed. Read-only analysis; no DB changes made.

## 1. Why I did not auto-repair

- **The main blockers ARE the deferred decision.** I2 (verse-record coverage) and I10 (chars the seed missed) are the same "the reading outran the up-front scaffolding" gap Psalms hit. The chosen-but-unexecuted Psalms remedy is **engine onboarding (step d)** — register the term, pull its verses, build the links. Doing that for Proverbs commits the whole programme to path (i) below; that is the researcher's call.
- **The passage tool is misaligned.** `_apply_passage_completeness_v1_20260707.py --book 20 --dry-run` does **not** target the actual gap (Pro 22:27); it proposes reshaping **Pro 2:1, 5:17, 7:9** by its own v1 rule. passage-rule-**v2** (candidate-driven) is the current authority and has **no apply script yet** (the readiness instruction §D and the cycle both note a v2 successor must be built). Running v1 would misalign Proverbs' existing 799 passages.
- **A role-model ambiguity.** The authoritative integrity doc I6 (2026-07-11) lists `role ∈ {characteristic, **qualifier**, standalone}` — i.e. `qualifier` is *valid* — while memory `project_candidate_characteristic_seed_and_role_model` says qualifier is *retired*. Until that is reconciled I will not mass-migrate 601 `qualifier` spans (risk of destroying valid labels).

## 2. Precise blocker anatomy (verified against the DB, 2026-07-12)

| gate | count | breakdown | true nature | fix path |
|---|--:|---|---|---|
| **I2** master coverage | 104 | **71** term missing from `mti_terms` · **33** term present, no verse-record | the deferred decision | engine onboarding (path i) |
| **I10** candidate flag | 266 | old-model `characteristic` role (`lexical-model-2026`=245, `role-reassess-2026`=21) on **non-candidate** spans; **0** have a read char-word or `ib_char_id` (never read); **6** also term-missing | seed under-coverage of wisdom vocab (e.g. prudence H6195, learning H3948, complacency H7962) **+** stale old-model roles | seed reconciliation (per decision) |
| **I4** passage membership | 1 | Pro 22:27 ("pay" H7999, standalone candidate) has no passage; sits between passages 1930 and 3667 | needs a **v2** single-verse passage | build/So run a v2 passage pass |
| **I8** pair endpoints | 2,437 | pairs with Strong's-encoded `from/to_span` | known re-read requirement | the re-read writes span-id endpoints (not a pre-read repair) |
| retired roles | 998 | `qualifier` 601 (92 candidate / 509 not) · `process-qualifier` 397 (109 / 288) | candidate ones self-resolve in the read; non-candidate ones are stale labels; **`qualifier` may be valid** (I6) | reclassify — see §4 |
| I6 undecided | 40 | candidate spans with `role=NULL` | the read assigns their role | not a blocker — reclassify |

**Reclassification (readiness-instrument correction):** the retired-role and undecided-role checks should be **READ-OUTPUT / informational**, not preconditions — the re-read (`_apply_reread_lexical`, `role_provenance='read-2026'`) rewrites every candidate span's role. Only char_candidate coverage, verse-record coverage, and passages actually gate what gets read. I will make this correction to the readiness instruction + runner once the role-model ambiguity (§1) is settled. **Net true blockers: I2 (104), I10 (266), I4 (1).**

## 3. The decision (unchanged from 2026-07-11, now forced by Proverbs)

> **(i) Register path** — make every characteristic word a registered term: onboard the 71 missing Proverbs terms + build the 33 records via the engine (`_apply_gate1_term_onboard_v1` / `_run_gate1_onboard_batch_v1`), reconcile the 266 seed-missed chars into the seed, then build v2 passages. The old term-backbone then matches the reading. This is what passage-rule-v2's invariant *requires* and what the Psalms memory records as the intended remedy.
>
> **(ii) Relax path** — treat the lemma-based `ib_characteristic` index as the primary backbone and relax the term-registry requirement for emergent/seed-missed chars; verse-records/onboarding become optional for them.

**My recommendation: path (i) — register via onboarding.** Reasons: it is already the Psalms-chosen remedy (consistency across books); passage-rule-v2's integrity invariant assumes it; it keeps a single traceable backbone (span→record→term→registry) rather than two competing ones; and it directly produces the missing wisdom-vocabulary chars the study wants. Cost: onboarding ~71 terms is a STEP-backed, per-term operation (heavier than a SQL patch) — a bounded batch, not open-ended.

## 4. Recommended sequence (on approval of path i)

1. **Reconcile I10 (266) into the seed** — triage the 266 old-model chars: genuine IB/wisdom words → add to the seed inventory (`lemma-inventory-master`) + re-stamp `char_candidate`; non-IB old-model false positives → clear the stale role. (This is a read-driven judgement, done per the IB screen, not a blind flip.)
2. **Onboard I2 (71 terms + 33 records)** via the gate-1 engine batch; re-check I2→0.
3. **Build v2 candidate-driven passages** for Proverbs (write/extend the v2 apply script per passage-rule-v2); fixes Pro 22:27 and any others; re-check I4→0.
4. **Correct the readiness instrument** (reclassify role checks per §2) once the qualifier question is answered.
5. **Re-run readiness** → expect READY; then Stage 0 → the lexical read.

Note: executing step 2 for Proverbs also establishes the pattern to finally close **Psalms I2=261**, which is still outstanding.

## 5. What I need from you

- **Confirm path (i) or (ii)** (I recommend i).
- **Resolve the role model**: is `qualifier` valid (I6) or retired (memory)? Is `process-qualifier` valid?
- **Scope for this session**: do you want me to (a) start with the I10 seed-triage + the v2 passage builder (no term onboarding yet), (b) go straight to the gate-1 term onboarding batch, or (c) just lock the plan and schedule the heavy onboarding separately?

*Filed 2026-07-12. Read-only analysis. No DB writes performed. Blocks Stage 0 until §5 is decided.*
