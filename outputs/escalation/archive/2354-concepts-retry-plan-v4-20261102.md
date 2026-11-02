# Concepts retry at surface grain, in layers from both ends: plan v4 (#2354, 2026-11-02)

Replaces plan v3. Nothing in this plan is built beyond the `surface_group` column (BUILD 443, 444). Workings, sources and assumptions are in `outputs/escalation/2354-working-log.md` (finding numbers below refer to it). Counts were read from the live tables on 2026-11-01 and 2026-11-02.

## What changed from v3, by your rulings
1. **No cluster or subgroup label assigns a group.** M clusters, T clusters and subgroups all hold surfaces that do not follow the split into behaviour, state and being (ruling 5). The label is a hint for a judgement, never the assignment. v3's L3 ("an unmixed cluster gives its kind with no further assessment") is gone.
2. **not_this_sense and anomaly pairs are not sent out.** They are not fitting for their own cluster's sense (2,593 and 147 pairs), which does not make them outside the inner being. They are judged like the rest. v3's L1 is gone.
3. **The unit is the (code, surface) pair.** Within one code the surfaces differ (M18: 27 of 88 codes in two or more groups, finding 3), so a verdict per Strong's code alone is not enough. The code's stepGloss and meaning tree are read for the code; the verdict is written per pair.
4. **Five values** of `surface_group`: behaviour, inner_being_state, being, qualifier, not_allocated. A qualifier describes something and is not itself a behaviour, state or being ("within" says where). **The use that makes it a qualifier** (place, time, quantity, quality) is kept in the name of the qualifier subgroup it sits in. There is no marker for which group it supports (rulings 7, 9).
5. **The kinds of being are concept domains**, not values (ruling 3).
6. **Not_allocated** holds what cannot be placed, for your detailed inspection, never forced into a value.

## The population
13,462 rows in `surface_subgroup`: 10,613 in group subgroups, 2,593 not_this_sense, 147 anomaly, 109 in the five qualifier subgroups. 10,722 of them (group plus qualifier) are in the 101 concepts now. All are judged.

## Layers (each works on what the earlier layers left; batches of about 100 Strong's codes; each batch's result in its own file under `outputs/concept-mapping/surface-group/` before the next starts; nothing held in memory)
- **L0, inventory, no judgement:** the batch files are cut from the live rows, with per code the stepGloss, the surfaces, the current subgroup and kind, and the stored `reason`. Counts re-queried at the start and written into the first file.
- **L1, clearly not a characteristic (the qualifier end), from your list:** your take-out list (9 words, 26 pairs, "they may bind with a characteristic but are not a characteristic") and the function words of the same kind, drafted by me from the surfaces for your review once (pronouns, prepositions, adverbs, modals, particles). Each gets `qualifier` with its use, or `not_allocated` if no use can be named. Open point Q1.
- **L2, clearly in:** codes whose stepGloss and every surface agree on one of behaviour, state or being are given that value. The cluster and subgroup name are read as a hint only; the agreement is checked in the stepGloss and in the surfaces themselves.
- **L3, the remainder, per pair:** where a code's surfaces differ, or the stepGloss does not settle it, each pair is judged from the surface, the stepGloss, the meaning tree and the stored `reason`. A pair I cannot place goes to `not_allocated`.
- **L4, you inspect** the `not_allocated` file and a sample from each other value; your rulings are recorded verbatim in the working log.

Each batch file gives, per pair, the value, the evidence that decided it (the stepGloss line or surface and the reason), and a mark: **inferential (B:4) until you confirm**. The reason lives in the batch file, not in a new column (ruling 2).

## What must be built before anything is written (B:105: a design, for your approval)
Nothing writes `surface_group` today. A small PowerShell tool `Surface-Group.ps1` on the pattern of `Concept-Edit.ps1`: `List` (counts by value, a batch's rows), `Set` (a batch file as one unit; prints the value it replaces; refuses an unknown value, an unknown pair, or a `qualifier` whose pair is not in a qualifier subgroup), through a `cfg_write_grant` and `run_id`, soft rules as for the other tools. Tested on a copy of iba.db with a test plan (every refusal and the unit rollback) before it is used. This is Developer Mode work and goes on #2354 as its own step.

## Then the concepts
Concepts are compiled from the labelled pairs: behaviour pairs into the behaviour domains, state pairs into the state domains, being pairs into new being domains (as feeling is split), qualifier pairs staying with the word they qualify in the qualifier subgroups. A concept links to a subgroup, not a pair, so a subgroup that holds two values is split first (L3 finds them). I propose the compile only after you have seen the counts of L1 to L3.

## Open points for you
- **Q1, your take-out list:** do those words become `qualifier` (with a use), or are they taken out of the population entirely, as #2344 said? Today all nine are in live group subgroups. "within" you have called a qualifier; "you" and "written" are not obviously one.
- **Q2, where qualifier pairs live:** the use is kept in the name of a qualifier subgroup, and today five exist (M05, M18, M34, M46, M58). A qualifier like "within" is in M47. One qualifier subgroup per use per cluster, or a shared set across clusters? This decides whether pairs move subgroup.
- **Q3, who judges:** I judge in batches in the session (about 27 batches of 100 codes), written to files and shown to you. The local-model pilot (#2339) grouped too coarsely to use (finding 12). Say if you prefer another engine; the cost of a model call per surface would be a decision to make first (B:20).
- **Q4, the mapping to your story, not confirmed:** behaviour is movement II, being is III, state is IV (finding 5). The five open questions of the story-fit file (seat, image of God, God-ward relational concepts, executive summary, life and death) are not answered in any record I found (log, "Still to read"); they do not block L1 to L3 but do block the compile.
- **Q5, the build:** approve the design of `Surface-Group.ps1` above.

## Not claimed
The supporting/qualifying share is your expectation; it is not measured, and L1 gives the first count. Every value I give is my reading of recorded text, inferential until you confirm. The human four-question test CSV (surface-human-test-v1-20261031.csv) was only opened at its first rows, so how far it was run is not known.
