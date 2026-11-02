# Concepts retry at surface grain: plan v2 for approval (#2354, 2026-11-01)

Nothing is built or written to iba/app/db/iba.db.

## Your decisions (verbatim, chat 2026-11-01, recorded on #2354 v3)
"sub groups have a mixture of the three separate groups in on sub group, that is why I think we need to resort to surface groups. place Spirit in a beings. it is not a behaviour, and not a state. but Spirit can be either divine, other spirits, or human spirit. The old tables will be re-used, and overwritten with the new allocation. D is correct, there are a number of surfaces that does not fit in any of these three."

## What this means, checked against the live tables
- The unit is now the surface pair in `surface_subgroup`: 13,462 live (strong, surface) pairs over 2,948 Strong's codes, all `provisional`. By their subgroup's kind: group 10,613; not_this_sense 2,593; anomaly 147; qualifier 109. 114 pairs are flagged `two_sense`.
- Each pair gets one of four labels: **behaviour**, **inner being state**, **being** (divine, other spirits, human spirit; also angels, Satan and demons, other people), or **none of these**. A pair that is two kinds is listed with both, not forced.
- Concepts are then formed from the pairs of each kind, and the 14 domains and 101 concepts are overwritten with the new set.

## Two things this raises
1. **Storage (a build, so a design decision for you, B:105).** `concept_subgroup` links a concept to a whole subgroup (411 rows). A concept made of surface pairs needs a link from `surface_subgroup` to `concept`, for example a `concept_id` column on `surface_subgroup`. That is a physical column, which standard mode cannot add: the same gap as #2355. Until it is settled, I can produce the allocation as a review file only.
2. **Cost (B:20).** 13,462 pairs is too many to judge one by one with a full reading each. Cheaper path with the same outcome: judge per Strong's code first (2,948) from its lexical meaning and the `reason` of its pairs; a code whose surfaces split across kinds is then split per surface (the mixed cases you found).

## Proposed steps
1. **Sample:** about 100 pairs, spread over the four labels and over mixed subgroups, to `outputs/concept-mapping/2354-surface-kinds-sample-v1-<date>.md` with the evidence quoted per pair, so the method can be seen working before the full run.
2. **Full allocation:** all 13,462 pairs to a review file, inferential (B:4), nothing written to the database.
3. **Concepts compiled** from the allocation, per kind, to a second review file.
4. **Write:** the new set overwrites the existing concept tables. This needs the storage decision above.

## Decisions I need
- **E. Storage:** approve a Developer Mode session to add the link (and the three `description` columns of #2355 in the same migration), or a different route you choose.
- **F. Method:** approve the cheaper path (per Strong's code first, split by surface where they differ).

## Not claimed
Every label is my reading of recorded text (`reason`, `core_description`, the lexical meaning), not a verse-level reading, and is inferential until you confirm it.
