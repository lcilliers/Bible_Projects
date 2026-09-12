# Escalation #1691 — `ib_observation` — columns, governing rules, and JSON specs

**Status:** consolidation for review, decision_required. Nothing built. Table name now settled
(`ib_observation`, per researcher's own naming pass — resolves the long-open `ib_observation`/
`ib_node` concatenation question for both #1691 and #1692). This round folds in a large batch of
researcher decisions plus two new deliverables: the input/output JSON specs per stage, and a
data-driven start on the `tag`/`window` exploration.

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
    question_code                TEXT NULL REFERENCES wa_obs_question_catalogue(question_code),
                                                     -- 'answer' stage only
    window                        TEXT NULL,     -- was slant_label -- see §6, scope beyond
                                                     'answer' stage still being explored
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
(`wa_obs_question_catalogue`, unchanged), and — same rerun principle as (a) — the family's
**existing `ib_observation` rows at `stage='answer'`**, when this is a rerun.

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

**Synthesis stage — only 5 rows exist, too few to generalize from**, all currently tagged
`'synthesis'` uniformly. Their real distinguishing feature so far is `status`
(`provisional`×3, `corroborated`×2) and `grounded_in` size (1 to 15 items) — not an obvious `tag`
axis, but worth the researcher's own eye once more synthesis rounds accumulate.

**Not concluded here** — this is the starting material for the researcher's own further analysis,
per their instruction, not a proposed final taxonomy.

## 6. `window` — scope question, not yet explored

Currently `window` only exists at answer stage (was `slant_label`). Researcher wants to explore
whether it applies to reading and synthesis too. No prototype data currently populates a
window-like field outside answer stage — reading's `alternative-meaning` tag (8 occurrences) is the
closest existing analog to "more than one way of reading the same evidence," but it's expressed as
a `tag` value today, not a separate `window` field. Not explored further here; flagged as the next
piece of data analysis, same status as `tag`.

## 7. `stable_key` — redefined

Researcher's decision: *"this is the link to the json. I suggest it contains the name of the json
file."* Column updated in §1 accordingly. **Open question this raises, not yet answered:** does
this apply to every stage's rows (since every stage now produces a file that could need re-running/
tracing back to), or only `synthesis` rows as originally scoped? Given `source_json_serial` already
exists as the per-row local number, `stable_key` as "which file" seems like it would be useful
project-wide, not synthesis-only — flagged for confirmation, not assumed.

## 8. Filing and naming conventions (project-wide, not `ib_observation`-specific)

Researcher's instructions, recorded here since they arose from this review:
- **File naming convention must be set in `cfg_setting`**, not left to drift — applies to every
  stage's output files, once the naming pattern itself is settled.
- **`_analytics/Clusters/` should have per-cluster subfolders** (e.g. `_analytics/Clusters/M10/...`)
  rather than everything flat in one directory.
Neither built here — recorded as a requirement for whenever the file-producing scripts are
finalized/registered.

## 9. Still not settled

1. Does append-only for `synthesis` need mechanical enforcement (a DB trigger refusing `UPDATE`
   where `stage='synthesis'`), or is it enforced purely by the table-update procedure's own code
   with no DB-level backstop? **Expanding per the researcher's request for more detail:** the risk
   is specifically that some OTHER future script — a fix-up, a bulk correction, anything that isn't
   the table-update procedure itself — could `UPDATE` an `ib_observation` row directly and silently
   violate the non-destructive-revision guarantee with no error. A trigger makes that impossible at
   the database layer regardless of which code path attempts it; relying on the table-update
   procedure's own discipline only protects against that ONE procedure, not every future writer.
   Not decided which the researcher wants — the tradeoff is a marginal amount of DB complexity
   (one trigger) against closing that gap for good.
2. `tag`: closed via `cfg_enum` — confirmed this round (§5) — but the actual taxonomy values for
   `answer`/`synthesis` stages are not yet chosen, pending more data as more families/rounds run.
3. `window`'s scope beyond `answer` stage — open, §6.
4. `stable_key`'s scope (every stage, or `synthesis` only) — open, §7.
5. The synergy-stage (e) input JSON — explicitly not yet defined by the researcher themselves, §3(c).
6. §4's truncated rule — waiting on the researcher to finish it.

## 10. What "finalized" would mean

Once §9 items 1–4 are resolved and the synergy-stage input (§3c) is defined: the `CREATE TABLE` in
§1, registered in `cfg_table`/`cfg_column`; the JSON specs in §3 become the actual contract the
generation scripts and the table-update procedure (#1693) are built against.
