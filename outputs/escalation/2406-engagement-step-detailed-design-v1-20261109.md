# #2406 — detailed design of the engagement step: calls, config rows, test plan (v1, for approval)

Nothing is built yet. This is the "detailed design" that #2406 v7 names as Claude's follow-up, written from design v3 (`outputs/escalation/2406-engagement-step-design-v3-20261109.md`) with your answers to Q1 to Q4 (all yes). Everything here is a proposal and inferential (B:4) until you approve it. Developer Mode lifts only the `configmaint.propose` gate; the rest still applies (B:97).

## What I read first (B:123)

- `cfg_table.use`: `ib_observation` (the table's recorded meaning is outdated: "81 observations ... transitional store"; it now holds 20,995 rows, so I took its columns from `cfg_column`), `ib_node`, `ib_observation_change`, `surface_term`, `surface_event`, `surface_subgroup`.
- `cfg_column`: `ib_observation.stage`, `.tag`, `.cluster_code`, `.cluster_subgroup_id`, `.parts`, `.route`; `ib_node.role`, `.verse_lexical_id`, `.cluster_subgroup_code`, `.disposition`; `surface_term.surface_group`, `.group_state`, `.group_judged_by`.
- Settings `reading.node_roles`, `reading.observation_parts`, `reading.observation_rules`; USER-GUIDE sections 8.2, 8.11 to 8.15; `iba/app/lib/collectionexport.py` (the pull's join rules) and `iba/app/lib/observationrecord.py` (the write functions).
- **A gap found (raise as an item, not fixed here):** the recorded meaning of `ib_observation` in `cfg_table.use` describes 81 observations; the table has 20,995 and its stages now include `Analysis_phase_1`, `prior-capture`, `reading`. The `ib_observation.stage` column meaning also lacks `Analysis_phase_1` and `prior-capture`.

## The step: one module, `Engagement.ps1`

New work package `engagement`, script `iba/app/ps/Engagement.ps1`, handler `iba/app/handlers/engagement.py`, library `iba/app/lib/engagement.py`. Same pattern as `Collection-Build.ps1`. Six actions, in the order of the v3 step:

| action | what it does | writes |
|---|---|---|
| `Pull -Collection x` | writes the working file of one collection (v3 step 1) | a file only, under `surfaces.working_files_root`/engagement, never overwritten |
| `Record -File f` | checks the filled assessment whole, then writes it (v3 steps 2 and 3) | `ib_observation`, `ib_node`, `ib_observation_change` |
| `Group -Collection x` | sets the surface-level group from the assessments (v3 step 4; R1) | `surface_term`, `surface_event` |
| `Review -Collection x` | writes the second working file: the verses no surface's assessment covers (v3 step 5; D4) | a file only |
| `Close -File f` | records the outcome of the review: observations about the surface in that verse, including no bearing, and verses set aside | `ib_observation`, `ib_node` |
| `Check -Collection x` | every member surface assessed in every one of its verses; every collection verse covered or set aside; report to `engagement.report_path` | a report file |

(`Close` is the v3 step 5 write; it uses the same checks as `Record`.)

### The working file (D5 of your rulings: isolate the AI from the database)

JSON, one per pull, named `engagement-<collection>-pull-v<n>-<yyyymmdd>.json`. It carries only the collection's own surfaces (R4): the collection (id, name, status, pole), each member surface with its tier, current draft group and group state; for each surface the verses it occurs in (`verse_lexical` id, reference, osisId, Strong's code, cluster, subgroup, the ESV text, `surface_kind`, `unit_surface`, `unit_role`); and for each verse every live observation and node on it, any stage, any subgroup (so the existing ones are taken into account). Member surfaces are found by the join rules of `collectionexport.py` (the link's own term and the terms whose base is that term). The assessment reads the file and not the tables.

### What Claude fills (Record)

For each surface in each verse, one evaluation: `result` (`relevant`, `bears_on`, `not_relevant`), `reason` (at least `reading.verse_loop` `min_reason_chars`), and for a relevant surface the `role` (`characteristic` or `qualifier`, with `gives` for a qualifier) and the `test` of spec 4.1 it passed (Q3). Then observations: one per surface and role, with one node per verse where it holds; a second observation for the same surface where another role holds in other verses (D3). Existing observations of those verses take an action (`accept`, `modify`, `delete`, `merge`, `leave`), carried out by the existing functions in `observationrecord.py`, each with its reason in `ib_observation_change`.

### Record's rules (all in config, not code)

- the stage written is the new `engagement` (see choice A below);
- the kind is chosen from `reading.observation_parts` kinds by the surface (R2); where none fits and the surface operates as an inner-being behaviour, it is written as the characteristic, as a `statement`;
- a surface with no bearing in a verse is a `silence`-kind observation with a node on that surface and verse (Q2); `reading.observation_rules` `unused_kinds` (which lists `silence` for Analysis_phase_1) is left as it is, and the check reads the rule of the step it is for;
- a refusal writes nothing; a verse with an error stays open and the others are recorded, as Reading Record does.

### Group (R1, Q1, Q4)

For each member surface, from its live nodes of stage `engagement`:
1. a `characteristic` node in any verse: `behaviour`;
2. else a `qualifier` node in any verse: `inner_being_state`;
3. else (only `bears_on` or no bearing): `other`, which leaves the study group.

The write replaces the draft in `surface_term.surface_group`, `group_state` becomes `corrected`, `group_judged_by` `rule:engagement`, and a `surface_event` (`set_group`) keeps the value before. Refused for a surface with no assessment in every one of its verses. A second Group changes nothing. A surface moved to `other` leaves collection a, so afterwards `Surface-Resolve.ps1 -Action Run -Check` and `Surface-Group.ps1 -Action Repoint -Check` are run, as USER-GUIDE 8.11 says for `Set`. Group never edits a collection (R4).

## Config rows (all new, module `engagement`)

| key | value |
|---|---|
| `engagement.stage` | `engagement` |
| `engagement.roles` | `{"relevant": ["characteristic","qualifier"], "bears_on": ["object","relational_target","enactment"]}` (the same as `reading.node_roles`, held by reference where the code reads it) |
| `engagement.group_rule` | the three-line rule above, as JSON |
| `engagement.no_bearing_kind` | `silence` |
| `engagement.tests` | the spec 4.1 tests, by key (inner-being vocabulary, idiom, volitional sense behind a plain action, party, negation or modifier, link in sequence, nothing beyond grammar) |
| `engagement.working_dir` | `_analytics/surfaces/working_files/engagement` |
| `engagement.report_path` | `outputs/reports/engagement` (checked against the filing convention before use) |
| `engagement.group_judged_by` | `rule:engagement` |

Plus: a cfg_enum value `engagement` for `ib_observation.stage`, the enum value `rule:engagement` where `group_judged_by` is checked, the work package `engagement` and six `cfg_step` rows (`engagement.pull`, `.record`, `.group`, `.review`, `.close`, `.check`) with their `cfg_utility` rows for the library and handler, and the new `cfg_behaviour_rule` or an extension of an existing one only if you say a rule is needed; I propose none (the rules already govern: B:4, B:44, B:114, B:116).

## Test plan (on a copy of the database, B:2; result recorded on #2406)

On a copy of `iba.db` (never the live DB), with `iba/app/tools/temp_2406_engagement_test_run.py`:
1. **Pull** on `aloud`: 8 member surfaces, 153 distinct verses, as found in the exploration; second pull gives an identical file; an existing file name is refused; a surface outside the collection never appears (R4).
2. **Record**: a surface a characteristic in some verses and a qualifier in others (two observations, nodes on the right verses); a surface with no bearing (silence-kind observation); a shared surface (assessed once, accepted by the second collection); a verse with several surfaces; existing observations accepted, modified and merged, each with its change row; a refusal when a surface is evaluated without a reason or a verse is missing, with nothing written.
3. **Group**: the three branches of the rule; refused before assessment; second run unchanged; `surface_event` holds the old value.
4. **Review and Close**: verses uncovered by any assessment are listed; a verse is set aside only when all its surfaces are; a verse the surfaces cannot account for becomes a question on the collection (an escalation raised, not a repair).
5. **Check** passes and fails as expected.
6. **Front door**: the same through `Engagement.ps1` on the copy, then one live run on `aloud` after you approve the test result.

## Choices I make unless you change them

- **A. Stage.** A new stage `engagement`, not `Analysis_phase_1`: that stage's check forbids `silence`, wants the nine items for each characteristic, and its gate is the reading's. A new stage keeps the two steps apart and the rule C1 unchanged. Cost: the reading's Observe sheet already lists every live observation of any stage, so these show up on later sheets as existing observations to accept; that is what D5 wants.
- **B. Documents.** USER-GUIDE.md gets a new section 8.18; BUILD.md gets the entry; `iba/docs/ps tools worksheet.xlsx` gets six rows (I do the first two, you opened the third last time).
- **C. Ollama later.** No prompt now (D5); the first collections are done by Claude, and the prompts come after, as `cfg_ai_prompt` versions through `Ai-Control.ps1`.

## Two questions that need your answer before I build (B:44)

- **Q5. The cluster of an observation.** `ib_observation.cluster_code` is required for a reading, and a surface in a verse sits under one or more clusters (the export gives one row per cluster). For this step I propose: the observation's cluster is the cluster of the surface's Strong's code that the surface's `surface_subgroup` row names; where a surface has several (`surface_subgroup` holds one row per cluster and code), one observation per cluster would multiply the rows, so the observation carries the first by `cluster_strong` order and each node carries its own cluster. Is that right, or should the observation carry the collection (no cluster) and only the nodes carry clusters?
- **Q6. A surface moved to `other`.** Group leaves a collection with a member that is no longer in the study group. I propose that Group only reports it (the surface, the collection, the tier) and raises one escalation for the collection, never removing the link (R4: this step does not reform collections). Is that right?

## Approval sought

Approve this detailed design for building, with your answers to Q5 and Q6, or your corrections to choices A to C. On approval I build in the order: config rows (one named snapshot first), library, handler, script, tests on a copy, documents, then the live run on `aloud`.
