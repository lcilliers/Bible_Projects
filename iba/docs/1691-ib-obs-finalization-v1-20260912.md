# Escalation #1691 — `ib_observation` — columns, governing rules, and JSON specs

**Status:** consolidation for review, decision_required. Nothing built. Table name now settled
(`ib_observation`, per researcher's own naming pass — resolves the long-open `ib_observation`/
`ib_node` concatenation question for both #1691 and #1692). This round folds in a large batch of
researcher decisions plus two new deliverables: the input/output JSON specs per stage, and a
data-driven start on the `tag`/`window` exploration.

**DB location, 2026-09-13 (DB fork, #737/#1682/#1690): `ib_observation` lives in `iba.db`, not
`bible_research.db`.** Every FK on this table (`cluster_subgroup_id` → #1690's `cluster_subgroup`,
now also `iba.db`) needs a same-database target to be real — SQLite doesn't enforce cross-database
foreign keys. **No step of this pipeline (process a/b/c/d/e, or the table-update procedure #1693)
may read or write `bible_research.db`.**

## 1. Columns — final list

```sql
CREATE TABLE ib_observation (
    id                          INTEGER PRIMARY KEY,   -- assigned by the TABLE UPDATE PROCEDURE
                                                            only, never by the LLM session — see §4
    cluster_code                TEXT NOT NULL,
    cluster_subgroup_id         INTEGER NULL REFERENCES cluster_subgroup(id),  -- was family_id;
                                    points at the FRESH cluster_subgroup from #1690 -- NULL only
                                    for stage='synthesis'
    stage                       TEXT NOT NULL,   -- 'reading' | 'answer' | 'synthesis'
    tag                         TEXT NOT NULL,   -- stage-specific enum, cfg_enum-governed -- see §5
    strong                      TEXT NULL,       -- the strong this claim is grounded in
    question_code                TEXT NULL,     -- 'answer' stage only -- NOT an enforced FK, see
                                                     new item below: wa_obs_question_catalogue is
                                                     bible_research.db-only, a second cross-database
                                                     gap the DB fork surfaces, not yet resolved
    window                        TEXT NULL,     -- pipeline-window enum, ALL stages (redefined
                                                     2026-09-13): 1=lexical analysis,
                                                     2=verse-context reading ('reading' stage),
                                                     3=answer stage, 4=multi-cluster synergising,
                                                     more to follow -- see §6
    obs_text                      TEXT NOT NULL, -- was statement; self-standing, no join required
    meaning_source                 TEXT NULL,    -- 'reading' stage only
    status                          TEXT NULL,   -- provisional|corroborated|superseded;
                                                     'synthesis' stage only
    supersedes_observation_id       INTEGER NULL REFERENCES ib_observation(id),  -- 'synthesis'
                                                     stage only, self-referencing
    stable_key                       TEXT NULL,  -- the generating JSON FILE's name -- redefined
                                                     this round, see §3 item 6; open whether this
                                                     applies to every stage or 'synthesis' only
    revisit_note                      TEXT NULL, -- 'synthesis' stage only
    source_json_serial                INTEGER NULL,  -- the LLM session's own local numbering for
                                                     this observation within its JSON, distinct
                                                     from `id`
    created_at                        TEXT NOT NULL,
    updated_at                        TEXT NULL  -- set whenever obs_text is broadened in place
)
```

**No edit-history table.** Researcher's decision: *"I think that would be an overkill. I am not
expecting a large number of edits."* — the old §5 item 3 (an `ib_observation_revision` table) is
closed, not built.

## 2. Staging — confirmed rules

Researcher's own framing, verbatim in substance: **each stage is a separate routine, never run
together.** Each is independently re-runnable — you must be able to re-run any one stage for a
single family/subgroup on its own, not the whole cluster. Each stage's input is the previous
stage's output JSON (reading → answer → synthesis), so a rerun of a later stage always needs the
current state of the earlier one, not a stale copy.

**Confirmed, 2026-09-13:** all three stages — `reading`, `answer`, `synthesis` — each produce their
own JSON output, and each stage's output is captured into `ib_observation` (via the table-update
procedure, #1693 §0's run structure) — not just reading and answer. `synthesis` is not a
downstream/different mechanism; it writes into this same table under `stage='synthesis'`, exactly
as the column definition in §1 already states.

**★ NEW, 2026-09-13 — see #1697** (`iba.cluster.status` lifecycle enum, same sign-off pack): each of
these three stages now also has a hard precondition and postcondition on `cluster.status` — reading
requires `ready_for_reading` and advances the cluster to `ready_for_observations` on success; answer
requires `ready_for_observations` and advances to `ready_for_synthesis`; synthesis requires
`ready_for_synthesis` and advances to `completed`. None of these stages may run against a cluster
sitting at the wrong status, or one reset to `strongs_reassigned` by an intervening `cluster_strong`
change. Full rule at #1697, not restated here.

**RESOLVED, 2026-09-13 — corrects the paragraph above.** Reading/answer's *real* precondition and
postcondition is `cluster_subgroup.status` (#1690 §3a), checked/advanced per-subgroup, since these
stages run per-subgroup (this doc's own §2). `cluster.status`'s `ready_for_reading`/
`ready_for_observations`/`ready_for_synthesis` values are a **rollup** over every subgroup's status,
not an independent gate — the cluster only shows `ready_for_observations` once every one of its
subgroups is individually `ready_for_answer` or beyond (`FLAG` excluded). Synthesis is the exception:
it's cross-family, not subgroup-scoped, so its precondition genuinely is `cluster.status=
'ready_for_synthesis'` directly. Full rule at #1697 §3.

## 3. JSON specs — input and output per stage, including reruns

Researcher's instruction: *"structure and preparation of json must be consistent, every time.
Define how input json is compiled and how output json must look like."*

### (a) Reading — input

Compiled from the tables (process (a)'s existing job, unchanged in mechanism): for every strong in
scope, occurrences (`cluster_code`, `strong`, `stepGloss`, `osisId`, `reference`, `verse.text`,
`span.surface`, `span.morph_code`) and meaning (one row per source, up to 3: `strong_meaning_tree`/
`strong_lexicon.lsj`/`strong_lexicon.mounce`), exactly as specified in the original process spec
§2 (`iba/docs/1682-cluster-reading-process-spec-v1-20260911.md`) and implemented in
`temp_1682_assemble_cluster_json.py`.

**New requirement, not previously specified:** if this is a **re-read** of a family already in the
database, the input must also include that family's **existing `ib_observation` rows** (reading
stage) so the LLM sees what's already been found rather than starting blind. Mechanically: a query
against `ib_observation WHERE cluster_subgroup_id=<this family> AND stage='reading'`, included
alongside the process-(a) occurrence/meaning data.

### (b) Reading — output / Answer — input

Reading's output (process (c)'s existing shape: `observations[]` with `tag`/`obs_text`/`traces`,
now carrying `source_json_serial` per observation) is the input to answer. Answer's own input adds
two things reading's output doesn't carry: the catalogue questions themselves
(`wa_obs_question_catalogue` — **`bible_research.db`-only, see new item below, this read is not yet
resolved under the DB fork**), and — same rerun principle as (a) — the family's **existing
`ib_observation` rows at `stage='answer'`**, when this is a rerun.

### (c) The synergy stage — input — NOT YET DEFINED

Researcher's own words: *"likely to be a json extract from the tables, and is likely to include
the current cluster and other related cluster information. This is not yet fully defined."*
Left open here deliberately, not guessed at — this is also where the "stage synergise... not yet
clear" question from chat lives; needs the researcher's own further thinking before a spec is
written, not a proposal from this side.

## 4. The LLM session vs the table-update procedure — confirmed division

The LLM never touches the database, never assigns `id`, never checks for duplicates, never decides
edit-vs-new. Concretely, on the LLM side: every observation gets its own `source_json_serial`
(local to that JSON); every observation explicitly carries the node segments that support it (the
existing `traces.occurrences` shape). On the table-update-procedure side: it assigns `id`; decides
same/broaden/new per incoming citation (#1693's own core, still-undesigned problem); enforces
self-standing narrative, append-only for `synthesis`, and stage-scoped nullability at write time,
not the LLM.

**One item from the researcher's own notes is truncated and not adopted as a rule yet:** *"search
for a similar observation before creating new - if"* — cuts off mid-sentence, and the researcher
has confirmed (separate chat message) they aren't finished with it. Left open, not guessed at.

## 5. `tag` — data pulled from the prototype, per researcher's request to start there

Researcher's decision: `tag` is stage-specific, **cfg_enum-governed** (closed, not free text), and
needs real data analysis before being settled — not resolved here, but grounded:

**Reading stage — already a real, exercised 8-value taxonomy** (frequency across all 15 M10
families, 394 observations total):

| tag | count |
|---|---|
| `instance-meaning` | 145 |
| `verse-grouping` | 110 |
| `difference-inference` | 39 |
| `surface-gloss-divergence` | 32 |
| `no-human-context` | 23 |
| `cross-family` | 20 |
| `data-error` | 17 |
| `alternative-meaning` | 8 |

**Answer stage — currently has no real tag taxonomy at all**, just the placeholder value `'slant'`
on every row. What the actual data shows instead: `catalogue_scope` already carries 6 distinct
values across 192 answers this round (`Characteristic (HIB behaviour)`: 45, `Verse-context`: 39,
`Other non-human beings`: 39, `Word/term (lexical)`: 36, `Characteristic relational`: 21,
`The HIB`: 12) — this is the catalogue's own field, not a candidate `tag` value itself, but the
clearest existing signal of "different kinds of answer" if `tag` is meant to classify answers the
way it classifies readings. Also present: `needs_adjacent_verse_context` flags (4) and
`cross_family_or_cluster_flags` (15) — currently separate arrays, not `tag` values, but exactly the
kind of thing that could become its own `tag` if answer-stage rows get folded flatter (matching
how `data-error`/flags already work at reading stage).

**RESOLVED, 2026-09-13 — confirmed direction for the answer-stage taxonomy.** Researcher's own
words: *"this is exactly what it should be — the question answer raises a flag that need follow
up."* The `needs_adjacent_verse_context`/`cross_family_or_cluster_flags` shape above is confirmed
as the right axis for `answer`-stage `tag`: a tag value expressing "this answer raises something
that needs follow-up," folded flat into `tag` rather than kept as separate arrays — matching how
`data-error` already works at reading stage. The exact value name(s) are not chosen here (still
needs more answer-stage data, per §5's opening framing), only the direction is confirmed.

**Synthesis stage — only 5 rows exist, too few to generalize from**, all currently tagged
`'synthesis'` uniformly. Their real distinguishing feature so far is `status`
(`provisional`×3, `corroborated`×2) and `grounded_in` size (1 to 15 items) — not an obvious `tag`
axis, but worth the researcher's own eye once more synthesis rounds accumulate.

**Not concluded here** — this is the starting material for the researcher's own further analysis,
per their instruction, not a proposed final taxonomy.

## 6. `window` — RESOLVED (2026-09-13): a project-wide pipeline-stage enum, not answer-scoped

Researcher's decision: `window` is **not** an interpretive-slant field scoped to `answer` — it
identifies which processing window of the overall multi-window pipeline produced the observation,
`cfg_enum`-governed, and open to grow:

| window | meaning |
|---|---|
| 1 | Lexical analysis |
| 2 | Verse-context reading for IB activity (`ib_observation.stage='reading'`) |
| 3 | Answering catalogue questions (`stage='answer'`) |
| 4 | Multi-cluster synergising |

"other windows to follow" — the researcher's own words; the enum is expected to grow past 4.
Applies to every stage's rows, not just `answer` — closes §9 item 3 below.

## 7. `stable_key` — redefined

Researcher's decision: *"this is the link to the json. I suggest it contains the name of the json
file."* Column updated in §1 accordingly. **Open question this raises, not yet answered:** does
this apply to every stage's rows (since every stage now produces a file that could need re-running/
tracing back to), or only `synthesis` rows as originally scoped? Given `source_json_serial` already
exists as the per-row local number, `stable_key` as "which file" seems like it would be useful
project-wide, not synthesis-only — flagged for confirmation, not assumed.

## 7a. New gap, found this round — `wa_obs_question_catalogue` is `bible_research.db`-only — RESOLVED, migration tracked at #1696

Checked live while applying the DB fork (2026-09-13): `question_code` (§1) was going to be an
enforced FK to `wa_obs_question_catalogue(question_code)`. That table exists **only in
`bible_research.db`** (434 rows) — not `iba.db` at all. Under the fork, this is the same
cross-database problem all over again, on a second table this design already depends on (the
answer-stage input, §3(b)).

**Researcher's decision, 2026-09-13:** migrate the table into `iba.db` (option 1 of the 3 originally
laid out here) — matching the same logic already applied to `strong`/`cluster` in #1690. Tracked as
its own escalation, **#1696**, and explicitly folded into the same sign-off pack as #1690/#1691/
#1692/#1693: **none of the five may be built until all five are signed off together.** The
migration itself still needs to decide how the catalogue's own messy lifecycle state travels (only
239/424 rows `active`, 243 `deleted`, the two markers disagreeing in count) — not resolved here,
that's #1696's own scope.

Column definition in §1 keeps the FK syntax removed until #1696 actually executes and the table
exists in `iba.db` — restore `REFERENCES wa_obs_question_catalogue(question_code)` at that point,
not before.

## 8. Filing and naming conventions (project-wide, not `ib_observation`-specific)

Researcher's instructions, recorded here since they arose from this review:
- **File naming convention must be set in `cfg_setting`**, not left to drift — applies to every
  stage's output files, once the naming pattern itself is settled.
- **`_analytics/Clusters/` should have per-cluster subfolders** (e.g. `_analytics/Clusters/M10/...`)
  rather than everything flat in one directory.
Neither built here — recorded as a requirement for whenever the file-producing scripts are
finalized/registered.

## 9. Resolved this round (researcher's answers, 2026-09-13) / still open

1. **RESOLVED — no DB trigger.** Researcher's decision: only the designated table-update procedure
   (#1693) ever interacts with `ib_observation`. Other routines — including any future synergising
   intervention — produce JSON output only; the update procedure alone controls DB writes. The
   single-writer principle is the enforcement mechanism for append-only `synthesis`, not a trigger.
2. **RESOLVED — accepted.** `tag` stays extensible: new values can be added to the `cfg_enum` set
   as real data analysis surfaces them; §5's prototype-derived values are a starting point, not a
   closed list.
3. **RESOLVED — applies to every stage.** See the redefined §6: `window` is a project-wide
   pipeline-stage enum (1=lexical, 2=reading, 3=answer, 4=synergising, more to follow), not scoped
   to `answer`.
4. **RESOLVED — all stages.** `stable_key` (the generating JSON file's name) applies to every
   stage's rows, not `synthesis`-only. Related architecture point raised alongside this: the
   table-update procedure fires immediately after each stage's JSON is produced, as part of one
   run (assemble input → run the stage's sub-process → run the DB update), not on a separate
   deferred trigger — recorded in full at #1693.
5. **STILL OPEN, confirmed.** The synergy-stage (e) input JSON: researcher confirms it genuinely
   can't be defined yet — needs more process-(c)/(d) prototype results first. A dedicated
   escalation for the synergy-stage design has been raised to track this once the prerequisite
   build/test work is done — see escalation #1695 ("Design: cluster-reading synergy stage") — not
   a blocker to finalizing this document, see §10.
6. **RESOLVED, moved to #1693.** The truncated "search for a similar observation before creating
   new" rule: the table-update procedure must first search for a similar existing observation, then
   choose between (a) adding a new `ib_node` row against that existing observation, or (b) creating
   a new `ib_observation` row together with its own new `ib_node` row. This is the same/broaden/new
   decision #1693 §3 already flagged as undesigned — recorded there in full, not duplicated here.

## 10. What "finalized" means — resolved

Researcher's own definition (2026-09-13): finalized = **the researcher's sign-off on escalations
#1690, #1691, #1692, and #1693** as a set — not a mechanical "every open item resolved" gate. Item 5 above (the
synergy-stage input) can remain open past sign-off; it is tracked separately and is not a blocker
to finalizing these four documents. Once signed off: the `CREATE TABLE` in §1 is registered in
`cfg_table`/`cfg_column`, and the JSON specs in §3 become the actual contract the generation
scripts and the table-update procedure (#1693) are built against.
