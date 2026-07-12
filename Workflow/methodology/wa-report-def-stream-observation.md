# Report Definition — CHARACTERISTIC_OBSERVATION (narrative rollup of one characteristic)

- **Type:** living definition spec · Version 2 · 2026-06-30 (renamed from Stream_observations; reframed per architecture register §8)
- **Report class:** whole-characteristic **rollup** → living generated page, no `-vN` (history in git)
- **Generator:** `scripts/_assess_characteristic_observations.py` (**to build**)
- **Output path:** `verse-analysis/_characteristics/wa-characteristic-{name}-observations.md`
- **Sample:** [SAMPLE-characteristic-observation-ruthlessness.md](samples/SAMPLE-characteristic-observation-ruthlessness.md)
- **Source of truth:** the DB only; never hand-edited.

---

## 1. Purpose
Collate **every observation for one characteristic** across **all its verses**, and **convert them to a narrative** — the cross-verse picture of one inner-being movement, the place a focus point can be seen. "Stream / track" is retired; the grouping is the **`characteristic`** (between cluster, too coarse, and term, too narrow — DEC-4).

## 2. Input
- `--characteristic <name|id>`. `--all` to regenerate every characteristic's page.

## 3. Sections
1. **The narrative** — the observations read as one movement (assembled from the stored narratives; adds no meaning beyond them — synthesis into a focus point remains the researcher's act).
2. **By dimension** — *source `ib_observation` grouped by `dimension` (D1–D13)*.
3. **Dimension coverage — what is NOT yet there** — populated vs empty dimensions; the empty ones are the next questions (the most valuable view).
4. **Verses that built this characteristic** — *source `ib_observation.origin_verse`*: each verse, its obs count, the dimensions it contributed.

## 4. Versioning & filing
- Whole-characteristic rollup → **living page, no `-vN`.** Overwritten on demand; history in git.

## 5. Constraints
- Read-only; regenerated on demand; always current.
- Presents stored narratives; the narrative section *arranges* them, it does not synthesise new claims.

## 6. Build status & prerequisites
- **Generator to build.** Prerequisite (register §9): the stream→characteristic mapping (DEC-4) — until then, grouping runs on the current `operation` label as a proxy.

---

## Provenance — researcher comments that shaped this spec (verbatim)
Maybe I need to revise the use of the word stream or track. It introduces a new grouping concept that is pervasive. It was used to facilitate the analysis of different lemma in the verse. The cluster is too course of a grouping, the term is too narrow — it is actually the **characteristic** which is likely to include multiple terms. The stream observations collate the observations by stream across multiple verses. The observations are converted to a narrative.
