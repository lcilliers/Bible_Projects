# Validation report — seed-recall additions + candidate-char setting

> 2026-07-19 · confirms the seed-list process (candidate-characteristic recall additions) and the
> setting of candidate chars on spans are **complete and integrity-clean**. Inputs: the two seed
> quality reviews (`iba/app/docs/seed-quality-review-{greek,hebrew-aramaic}-v1-20260719.md`).
> Applied via 289 `accept` rules in `cfg_candidate_rule` → `candidate.seed` (global) →
> `candidate.set` (all 66 books). DB: `iba/app/db/iba.db`.

## Verdict: **PASS — 10/10 checks**

| # | check | result | detail |
|--|-------|--------|--------|
| 1 | accept-rules-loaded | PASS | 289 `accept` rules in `cfg_candidate_rule` |
| 2 | all-accepts-are-candidates | PASS | 0 accept lemmas failed to become a candidate |
| 3 | candidate-count | PASS | **2,013** candidates (was 1,732; **+281**) |
| 4 | candidate-lemma-in-inventory | PASS | 0 candidate lemmas absent from `lemma_inventory` |
| 5 | span_candidate-stamped | PASS | **87,922** stamps written |
| 6 | no-orphan-stamps | PASS | 0 stamps whose span is missing/deleted |
| 7 | **candidate-has-verse-record** (integrity invariant) | PASS | 0 stamped spans with no verse-record |
| 8 | stamped-lemma-is-candidate | PASS | 0 stamps whose lemma is not a candidate |
| 9 | all-books-stamped | PASS | 66 / 66 books carry candidate stamps |
| 10 | recall-additions-stamped | PASS | 489 recall lemmas now stamped; *thanks* (G2168) = 6 stamps in Romans |

Check 7 is the researcher's DB integrity invariant (`gate.char.candidate-verse-record`, LIVE): a
candidate span with no verse-record is a violation. Zero violations after the re-stamp.

## State after the run

- **candidate_seed** — 2,013 candidates. Layers: `registry-direct` 1,349 · `ib-judgement` 489
  (was 202; the recall accepts landed here) · `read-emergent` 175. **190** candidates now carry no
  registry word (the double-control signal — the recall additions with no registry coverage, e.g.
  *thanks*, the sluggard, self-control).
- **span_candidate** — 87,922 stamps across all 66 books.
- **Primary-read gate** — candidate-bearing verses (verses that enter the primary read): **25,775 /
  29,037** whole-Bible. Romans: **382 / 424** (was 363 — +19 verses recovered into the read).
- **Recall landing (Romans sample)** — G2168 *thank* (6) · G4567 Satan (1) · G2190 enemy (3) ·
  G5381 hospitality (1) · G5542 flattery (1) · G0463 tolerance (2) · G2432 cheerfulness (1).

## Notes carried forward (not defects)

- **Divine-name footprint is heavy** — bare "God" (G2316) stamps 151 spans in Romans alone. This is
  the confirmed "can-interact → include" ruling working as intended; the read / Screen 0 must sort
  God-as-arena from God-as-counterpart per verse. If it proves noisy in analysis, the one reversible
  lever is bare divine *names* (divine *dispositions* stay in regardless).
- **Passages untouched.** The passage-build method is parked as not-yet-fit-for-purpose; this run
  covered seed + candidate-char setting only. Verse selection (the seed) is done; context scoping
  (the passage) remains open.

## Reproduce

`cfg_candidate_rule.csv` (289 `accept` rows) → `python -m iba.app.run set-candidates --step
candidate.seed --run-id <id>` → `--step candidate.set --param Book=<bk>` per book.
