# Session log — 2026-07-12 — Psalms narratives rollout COMPLETE (46/46)

> Resumed the in-flight Psalms two-narrative rollout and carried it to completion. Batches 1–4 (34 families) were done in the prior part of the session; this part produced the final **12 families** and closed the rollout at **46/46**.

## Objective

For each Psalms family base source (`verse-analysis/psalms/_base-sources/psalms__*.json`), produce the **two-narrative** deliverable per the contract embedded in each base source's `meta.WORK_CONTRACT`: one record per **anchor reading** carrying an analytical `narrative` (walks dimensions 101–116, cites verses/ve_lexical) and a plain-reader `story` (zero study jargon), plus `citations`, `recurrences`, `variation_note`. Then render to markdown and verify.

## What was done

1. **Confirmed the contract** — the base source is self-describing: `meta.WORK_CONTRACT` carries the record shape, directives 1–10, completeness rules, and the exact output paths. No external prompt needed.
2. **Built a reusable verifier** — `scripts/_check_family_narratives_20260712.py`: checks anchor coverage (one record per non-duplicate `lexicals[]` row), both narratives non-empty, non-empty citations, record count == `scope_counts.distinct_readings`, and a story jargon gate (compound/underscore tokens + dimension-number pattern; ambiguous common words like "sense/effect" deliberately excluded after a false-positive on blessing). Calibrated to pass cleanly on all 34 already-done families.
3. **Pilot** — strength-courage-steadfastness (8 records) via one subagent; gated + rendered + eyeballed (ascent + Psa 88 "no strength" descent) before fanning out.
4. **Fanned out the remaining 11 families**, one subagent each, each obeying its base source's `WORK_CONTRACT`. Gated + rendered + committed each as it landed.

## Result — 12 families this session (~481 records)

| family | records | notes |
|---|--:|---|
| strength-courage-steadfastness | 8 | pilot |
| turning-repentance | 14 | |
| worship-prostration-service | 25 | |
| speech-mouth-tongue | 42 | |
| walk-way-conduct | 46 | 1 duplicate cross-ref'd |
| violence-cruelty | 21 | |
| will-resolve-vow-intent | 34 | 1 duplicate cross-ref'd |
| wisdom-folly-teaching | 39 | 2 duplicates cross-ref'd |
| righteousness-integrity | 69 | |
| wickedness-ungodliness | 51 | 5 Psa 119 dups cross-ref'd |
| sin-guilt-iniquity | 55 | |
| trust-refuge-security | 77 | largest; re-dispatched fresh (see below) |

**Rollout complete: all 46 Psalms families have narratives (json + md). Full verifier gate passes 46/46. Total corpus = 2,048 narrative records.**

## Incident — trust-refuge-security first agent corrupted

The first trust-refuge agent's context corrupted mid-run: it hallucinated a coordinator role, spawned **6 rogue "fragment" sub-subagents** (writing `frag1..6.json` to scratchpad — together 77 records, i.e. its workers actually succeeded; only its assembly step broke), and twice failed to write the real deliverable. I stopped the coordinator, abandoned it, and **re-dispatched a fresh clean agent** with an explicit "you are ONE worker, do not spawn agents" instruction. The fresh agent produced the correct 77-record file. Rogue frag files are scratchpad-only (outside the repo); no repo pollution. **Lesson:** the per-family worker prompt should state "do not spawn or wait for other agents" up front for the largest families.

## Data-quality finding — coupling(112)/locus(116) transposition

Six+ agents independently reported that dimensions 112 and 116 are **transposed** in a block of base-source rows. Verified directly: **666 of 2,168** rows (all 46 families) have 112 holding an `internal:/external:` locus token and 116 holding a `"paired with …"` coupling phrase. Onset is **exactly at Psa 89** (nothing below 89; dominant but not universal from there). Root cause not yet isolated (DB `ve_lexical` vs. the base-source generator). **Narratives are substantively unaffected** — agents read each field by semantic content. Full write-up + recommended follow-up: [`outputs/markdown/validation/wa-psalms-base-source-coupling-locus-transposition-v1-20260712.md`](../../outputs/markdown/validation/wa-psalms-base-source-coupling-locus-transposition-v1-20260712.md). **Not fixed this session** (needs a base-source/DB decision).

## Artefacts

- 12 × `verse-analysis/psalms/_narratives/psalms__<family>__narratives.json` (+ `.md`) — committed.
- `scripts/_check_family_narratives_20260712.py` — reusable per-family verifier.
- `outputs/markdown/validation/wa-psalms-base-source-coupling-locus-transposition-v1-20260712.md` — data-quality finding.

## Open loops / next

1. **coupling/locus transposition** — isolate root cause, repair, regenerate base sources, re-gate (see finding doc).
2. **Narratives → DB** — the `WORK_CONTRACT` names the DB as the ultimate destination (JSON = transport, `.md` = readable view; "all study work in the DB"). The narratives are currently filed as JSON/MD only; the patch-to-DB step is outstanding for all 46 families.
3. **Cross-term / cohabitation layer** — the style instruction (§3b) defers cohabitation to a cross-term story built after the single-term stories. With all 46 single-family narratives now complete, the cross-term layer is the natural next phase.

## 6. Session end (addendum)

Two follow-on items were completed after the rollout, at the researcher's request:

1. **Method preserved as an instruction** — [`Workflow/Instructions/wa-two-narrative-rollout-method-v1-20260712.md`](../Instructions/wa-two-narrative-rollout-method-v1-20260712.md): the authoritative 3-stage process (base source → two narratives → render/gate/commit), generalised for all remaining books. Bakes in the lessons — the "ONE worker, do NOT spawn agents" clause, **Sonnet-not-Opus** cost guidance, the mandatory gate before commit, and the 112/116 data-check. The design point that makes it repeatable: the base source is self-describing (its `meta.WORK_CONTRACT` carries the whole contract).
2. **Cost question answered** — the usage spike was **not** an expensive model. Every worker was `general-purpose` with no override → inherited the session model (**Opus 4.8 [1m]**); **fable was never invoked**. The spike = legitimate Opus volume for ~481 records **plus ~900k tokens wasted** by the one corrupted trust-refuge agent's 6 rogue fragment sub-agents. Mitigations now in the instruction (Sonnet + no-spawn).

**Tree clean, all committed** (through `907cb2f1`). Manifest rebuilt. Daily NAS DB backup (18:00) + full mirror (18:30) cover this work.

### ➡ Next session — rework of Proverbs lexicals

Start the **Proverbs lexical rework**. Context already on disk: `verse-analysis/proverbs/` (`_reread/`, `_roles/`, `_seg/`). Relevant standing state in memory: [[project_reread_success_gates_and_scored_audit]] (Proverbs re-read measured by gates G0–G8 + scored audit; **baseline = 2/9**; NEXT = confirm F-frame split → reset → re-read → re-measure) and the live lexical method ([[project_ve_lexical_is_verse_first]], [[project_term_driven_genre_aware_lexical_method]], the cycle/dimension authority docs). Proverbs is **poetic** genre → the two-phase lexical treatment applies. First move next session: orient in `verse-analysis/proverbs/_reread/` (BASELINE-v2, success-criteria, gates-completeness-gap) and confirm the exact scope of "rework the lexicals" with the researcher before touching data.
