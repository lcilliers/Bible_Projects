# #2538 — Stages 1 to 4 with the validation, runnable on one verse first: plan for approval (v1, 2026-11-24)

Researcher, 2026-11-24, in chat: the main focus is completing the codification, not fixing data; the repeatable process delivers stages 1 to 4 of a collection with all the validation checks as its outcome; it must also run on one verse, because an individual verse is revisited as well as the verses of a collection; build the code for one verse first, so the routine is finalised and refined on a small set of data. Nothing is built. This file states what I understood, what the code does today, the design the verse scope needs, the increments and the decisions I need (rule B:17).

## 1. What I understood

One routine, two scopes. The unit of work stays the same (a step, its rows, a record, a check, the gates); the scope is a verse or a collection. A verse run does stages 1 to 4 for the occurrences of that verse, with the marker, node columns, older-observation answers, text clash and gates applying to that verse. A collection run is the same routine over every verse of the collection, so a collection is finished when each of its verses is, plus what is collection-level by nature. I build and refine on a verse (and a handful of verses) first, then widen.

## 2. What the code does today (read from the code and the tables)

- Every step starts from `layerreading.load(name)`, which builds the collection's occurrences (`L["d"]["occurrences"]`, by the evidence report's membership rule) and its pairings. `derive` (the rows a step demands), `expected_nodes` (the nodes a row must carry), `pull`, `record`, `check` and the new `buildvalidate` all read those occurrences. So the scope enters at one point.
- The ledger `collection_layer_item` has no verse: a row is (collection, step, item, subgroup, subject). `open_step` adds rows the data demands and **retires** rows it no longer demands. Run on a narrowed load, that would retire every row outside the verse. This is the one hazard of a naive filter.
- `check` requires that an answered row's nodes equal what the data demands (word-sense rows: the senses together cover the occurrences). A row answered for one verse only would fail it.
- Some rows are collection-level by nature: the grouping of surfaces (stage 2, `collection_subgroup`), `group-definition` and `strong-enrichment` per subgroup, step 3.2 (the behaviours of the collection) and 3.3 (the collection with its partners).

## 3. The design

1. **Scope is a filter on the occurrences a run is asked for and records, not a second ledger.** A run has a scope: `-Verse <osis ref>` (one or several) or the whole collection. `load(name, verses=None)` returns the collection's occurrences restricted to those verses (pairings likewise). Nothing outside the scope is derived, pulled, expected or checked, and nothing outside it is retired.
2. **A row is complete when the occurrences it demands are covered, by however many runs.** A word-sense row for a word of the collection demands all its occurrences in the collection; a verse run records the senses and nodes for that verse's occurrences only; the row's state is `partial` until every occurrence is covered, then `observed`, then validated by the check. The same observation gains nodes in later runs (RW-03: the same description is never written twice; it gains a node), so a collection run after verse runs asks only for what is not yet covered. A word-level step (S1, the pairings in 2.1) works in this way directly.
3. **Collection-level aspects stay collection-level, and a verse run depends on them.** The grouping (stage 2) is done and closed for the collection before a verse can be run through stages 3 and 4, because stage 3 reads the groups and the node's subgroup. Stage 1 of a verse needs no grouping, as today. `group-definition` and `strong-enrichment` are written once for a subgroup; a verse run adds nodes for its occurrences to that observation.
4. **Stage 4 on a verse.** Step 3.1 (the elements of the subgroup) runs on a verse: its findings rest on the stage 3 observations of that verse and its nodes are that verse's occurrences. Step 3.2 (behaviours of the collection) and 3.3 (across collections) need the collection's elements together; a verse run does not close them, and a collection is closed only when they are done over all its verses. This is the main decision in section 6.
5. **The validation applies to the scope.** The marker, node columns, older-observation answers, text clash and trace tests apply to the observations of the verse's occurrences (already so, since `older_on` is by occurrence). The evidence gate before 3.1 and the closing gate are computed for the scope: the observations that have a node on the scope's occurrences.
6. **Revisiting a verse.** A verse run records again over observations that already cover it: the earlier answers on its occurrences are withdrawn by the existing re-record rule (only the nodes and observations tied to the rows being re-recorded), and an observation that also covers other verses loses only the nodes of this verse.

## 4. Increments, each tested on a copy and on a small verse set before the next

1. **Scope plumbing, stage 1 on one verse.** `load` with a verse scope; `derive`, `open_step`, `pull`, `record`, `check` for S1 on a scope, the `partial` state, no retirement outside the scope; PS entry point `-Verse` on `LayerOpen`, `LayerPull`, `LayerRecord`, `LayerCheck`. Test on three verses of the test collection and on one real verse of a real collection, on a copy.
2. **Stages 2 and 3 on a verse** (grouping read, 1.1, 1.2, 2.1 by occurrence coverage).
3. **Stage 4 on a verse** (3.1), and the scope's gates.
4. **Repeat on a handful of verses, then a whole small collection run verse by verse**, comparing it with the collection run of the same data (the same observations, nodes and markers).
5. **Records:** rules amended, USER-GUIDE and BUILD, migration for the state value and any schema, a named snapshot before any live apply.

The end-to-end tests the last review found missing (a file refused for an unanswered older observation and accepted once answered, through `lr.record`, the stage 4 path, the multi-sense path, adoption) are written in increment 1, since the scope work touches those paths.

## 5. What I will not do

No live change, no change to the data, no rerun of thought. The migration of #2538 stays unapplied until a build is complete and reviewed. Note that the working tree already holds code that needs the unapplied config (`layer.scan` and the gates), so the live `LayerRecord` and `LayerCheck` would refuse until that is applied or the code is held back; I will not apply anything live without your word.

## 6. Decisions I need from you

1. **A row complete by coverage** (section 3.2), with state `partial`, rather than a separate verse ledger. My recommendation: coverage, because a verse run and a collection run then share the rows and nothing is written twice.
2. **Stage 4 at verse level** (section 3.4): 3.1 runs on a verse; 3.2 and 3.3 are collection-level and close only when every verse of the collection is covered. Confirm, or say which of 3.2 and 3.3 you want a verse to produce.
3. **Grouping first:** a verse run through stages 3 and 4 requires the collection's grouping closed. Confirm.
4. **Which verses to refine on:** the test collection `backsliding` first (small, safe copy), then one verse of your choice that you know well. Which verse?
