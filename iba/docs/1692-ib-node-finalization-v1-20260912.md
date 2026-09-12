# Escalation #1692 — `ib_node` (was trace) — columns + governing rules, for final sign-off

**Status:** consolidation for review, decision_required. Nothing built. Same structure as
#1691's own consolidation, per the researcher's LLM-session/table-update-procedure split — an
`ib_node` row **never exists at LLM-generation time**; it is created entirely by the table-update
procedure, from the node segments an observation carries in its JSON.

## 1. Columns — final list as decided so far

```sql
CREATE TABLE ib_node (   -- name confirmed by researcher, resolves the old #1691/#1692 concatenation question
    id                     INTEGER PRIMARY KEY,   -- assigned by the TABLE UPDATE PROCEDURE only
    observation_id         INTEGER NOT NULL REFERENCES ib_observation(id),  -- real id: both sides are
                                                     this new schema, no cross-db/legibility reason
                                                     to denormalize this one
    cluster_code           TEXT NOT NULL,          -- denormalized VALUE, not an id (per researcher
                                                     instruction: store values, not ids, even for
                                                     same-database references)
    cluster_subgroup_code  TEXT NULL,               -- was `family_key`; denormalized copy of
                                                     cluster_subgroup.subgroup_code, e.g. "H_guilt"
    strong                 TEXT NULL,               -- denormalized copy
    verse_reference        TEXT NULL,               -- resolved FRESH against iba.db.verse.reference
                                                     at load time, never trusted from the LLM's JSON
                                                     directly (escalation #1693's own fix) -- set
                                                     only when grounded in a verse
    surface                TEXT NULL,               -- was `span_surface`; matches span.surface
    morph_code              TEXT NULL,              -- was `span_morph`; matches span.morph_code
    traced_observation_id   INTEGER NULL REFERENCES ib_observation(id),  -- set when grounded in ANOTHER
                                                     observation instead of a verse -- real id, same
                                                     reasoning as `observation_id`
    source_stage             TEXT NOT NULL,         -- 'reading' | 'answer' | 'synthesis'
    seq                       INTEGER NOT NULL,     -- ordering within one observation's citations
                                                     -- INADEQUATE AS-IS, see §4 item 1
    created_at                 TEXT NOT NULL,
    CHECK: exactly one of (verse_reference IS NOT NULL) / (traced_observation_id IS NOT NULL)
)
```

## 2. The LLM session — what it must produce for `ib_node` to be buildable

No `ib_node` row is ever written by the LLM. What the LLM DOES have to produce, on every
observation in its JSON (this is really an `ib_observation`-JSON-shape rule, repeated here because
`ib_node` is entirely derived from it): the exact node segments — verse + surface + morph, or a
reference to another observation — that support or address that observation, per #1691 §2 item 2.
Nothing else for this table; there is nothing an `ib_node` row does that the LLM decides directly.

## 3. The table-update procedure — what creates and populates `ib_node`

1. **Reads each observation's node-segment citations from the JSON** and creates one `ib_node` row
   per citation, linked to whichever `ib_observation.id` the reconciliation logic (#1693) assigned that
   observation (new or existing).
2. **Denormalizes at write time** — `cluster_code`, `cluster_subgroup_code`, `strong` are copied
   onto the row from context, not computed by the LLM.
3. **Resolves `verse_reference` fresh against `iba.db.verse.reference`** (matched via strong +
   occurrence) rather than trusting whatever string the LLM's JSON contains — closes the
   verse-reference-consistency risk found in #1682/#1693 by construction.
4. **Assigns `id`** — the one true unique id for the citation row, same pattern as `ib_observation.id`.

## 4. Still not settled

1. **The uniqueness/`seq` defect, unresolved from the first round.** H_guilt/G1777's Matt 5:22 has
   3 separate spans, all identically "liable"/`A-NSM` — `seq` alone doesn't give a stable business
   key, and nothing currently distinguishes them except insertion order. `iba.db.span.position`
   exists for exactly this; the table-update procedure likely needs to carry that value through
   (still a VALUE, not an id) so re-loading the same JSON is idempotent and distinguishable
   citations aren't silently merged. Not fixed here — flagged as blocking before this table is
   safe to build.
2. **Polymorphic single table vs two tables** — one `ib_node` shape covering both verse-grounded
   and observation-grounded citations (via the `CHECK`), or two dedicated tables (a verse-trace
   table and an observation-link table)? Unchanged from the first round, still open.
3. **Is the denormalized field list complete?** — e.g. should the verse's own text be carried too
   (process (d) restores `verse_text` for exactly this reason), or does that duplicate too much of
   `iba.db`? Unchanged, still open.
4. ~~Table name~~ — **resolved**, `ib_node` confirmed (see §1).

## 5. What "finalized" would mean

§4 items 1–2 are the real blockers — item 1 especially, since building this table with the current
`seq`-only uniqueness approach would ship a known data-loss bug on day one. Once resolved: the
`CREATE TABLE` in §1 (amended per §4), registered in `cfg_table`/`cfg_column`; the table-update
procedure's §3 responsibilities become part of #1693's full spec, same as #1691's §3.
