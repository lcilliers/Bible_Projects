# Cluster-reading findings table -- design options (escalation #1682, follow-on)

**Status:** design proposal, decision_required -- not applied to any database. Written per
researcher instruction ("lets complete the rest of M10, then I want to simulate how the findings
table would need to be structured"), after all 15 M10 buckets were completed under the round-2
process. **Extended below** (§1A) after two further rounds the original proposal did not yet
account for: process (d) (per-family catalogue question-answering, multi-slant, added same day)
and process (e) (cross-family/cross-round synthesis findings, added after H_guilt/B_sin/
G_transgression were compared against each other). The researcher's own framing for this
extension: "we now need to figure out how to codify and capture all of this so it can accumulate
with grace and not get lost because there will be more than one revisit to it, from very different
angles" -- a requirement §1A and the revised options below are written to satisfy directly.

## 1. What the data actually looks like now

Each family's process-(c) output (`_analytics/Clusters/1682-test-m10-process-c-<FAMILY>-v2-*.json`)
is a JSON document shaped like this (see spec: `iba/docs/1682-cluster-reading-process-spec-v1-20260911.md`):

```
{
  cluster_code, family_id, process, spec_round,
  strongs_in_family: [strong, ...],
  observations: [
    {
      tag,            -- enum: instance-meaning | alternative-meaning | verse-grouping |
                          difference-inference | surface-gloss-divergence | no-human-context |
                          cross-family | data-error
      statement,      -- free text, the actual analytical claim
      traces: {
        cluster, family, strong,           -- strong is nullable (cross-family/no-strong obs)
        occurrences: [ {verse, span_surface, span_morph}, ... ],  -- 0..N, mechanically checkable
        meaning_source,                    -- strong_meaning_tree | strong_lexicon.lsj | ... | null
        related_family, related_cluster    -- optional, only on cross-family observations
      }
    }, ...
  ],
  strong_checks: [
    { strong, occurrence_count, traced_count, missing_verses: [...] }, ...
  ]
}
```

Across the finished M10 pass: 15 buckets, ~500+ observations total, one `strong_checks` row per
strong per family (mechanically computed by `temp_1682_verify_strong_checks.py`, not eyeballed).

The three things a findings table must be able to hold, faithfully and queryably, are:
1. **The observation** itself (tag + statement + which strong/family/cluster it belongs to).
2. **Its trace** -- the exact verse+span_surface+span_morph occurrences that ground it, so a
   reader (or a later query) can go from any verse back to every observation that cites it, and
   from any observation to the exact spans that support it. This is the part round 1 got wrong
   (a flat semicolon-joined verse string) and round 2 exists specifically to fix.
3. **The verification record** -- for a given family/strong, how many occurrences exist, how many
   were actually traced by some observation, and which (if any) were missed. This has no obvious
   analog anywhere in the existing schema; it is process metadata about the *reading*, not a
   finding about the text.

## 1A. What process (d) and (e) add -- and why they change the shape of this decision

Process (d) (`_analytics/Clusters/1682-test-m10-process-d-<FAMILY>-v1-*.json`) answers a fixed set
of 64 catalogue questions (T0-T5) per family, each with **multiple slants** where the family's own
evidence genuinely diverges (H_guilt: 64 questions, 134 slants; B_sin: 110 slants; G_transgression:
102 slants), each slant carrying its own verse+span+morph+**verse_text** trail (restored here --
process (c) deliberately dropped it) and, where applicable, a pointer back to the specific
process-(c) observation(s) it was read off. Two more fields per question that §1 did not
anticipate: `needs_adjacent_verse_context` (flagged, not fetched) and
`cross_family_or_cluster_flags` (flagged, not resolved inline). This is a second, structurally
different tier from process (c)'s observations -- not more observations, but *answers to a fixed,
comparable question set*, which is exactly what makes cross-family comparison possible at all.

Process (e) (`_analytics/Clusters/1682-test-m10-process-e-synthesis-<round>-v1-*.json`) is a third
tier again: claims that reference *multiple* process-(c)/(d) items, often across families, that
have no home in any single family's file -- e.g. "H_guilt shows no constitutional-level engagement
anywhere, B_sin shows a systemic one, G_transgression sits between the two" (a claim that requires
reading three families' T2 answers together) or the T4.6 three-way spiritual-beings pattern. These
were, before being filed as process (e), living only in chat and an escalation comment -- exactly
the "get lost" risk the researcher named. Process (e)'s own rule (§4B of the spec doc): a later
revisit of a synthesis finding files a **new** entry with `supersedes` pointing at the old
`synthesis_id`; the old entry's `status` changes to `superseded` but it is never deleted or
overwritten. This is the mechanism that lets the same ground be "revisited... from very different
angles" without any earlier pass's finding silently vanishing.

**This changes the persistence decision in one important way:** any schema now needs to hold THREE
tiers, not one -- observations (c), question-answers-with-slants (d), and cross-referencing
syntheses-with-non-destructive-revision (e) -- and the tier-3 requirement (a claim that can
reference other claims, and be superseded without being destroyed) is not satisfied by any
verse-trace table design, however good. Worth noting: `finding.supersedes_id` already exists as a
column in the live schema (for "correction / resolution lineage") -- the *concept* of
non-destructive supersession is already a recognized project pattern, just not wired to this
process yet.

## 2. What already exists that's relevant

| Table | Shape | Fit |
|---|---|---|
| `finding` | `level` (VERSE/TERM/CLUSTER/GLOBAL), `verse_context_id`, `mti_term_id`, `cluster_code`, `finding_value`, `finding_status`, `provenance`, `strong_number` (added later), `notes` | Close on `cluster_code`+`strong_number`+`finding_value`, but **one row = one strong, no family concept, no tag taxonomy that matches ours, no multi-verse span storage** |
| `finding_verse_link` | `finding_id`, `verse_record_id`, `reference`, `role` (anchor/evidence) | Right shape for "one finding, many verses" but **no span_surface/span_morph columns** -- exactly the round-1 flaw this whole process was designed to fix, reappearing at the DB layer |
| `finding_citation` | `source_table` (constrained to `cluster_finding`/`cluster_observation` only), `citation_type` (verse/strongs/cross_char/vcg), `citation_value` (free text) | Flexible citation-list pattern, but `citation_value` is unstructured text -- span_surface/span_morph would have to be packed into a string and parsed back out, the opposite of what round 2 was built to avoid |
| `cluster_finding` / `cluster_observation` | Both keyed to `characteristic_id`/`cluster_subgroup_id` -- the **pre-reset characteristic/tier-grid model** the 2026-06-25 method reset explicitly closed | Wrong era. Checked live: **6,430 of the 6,431 `finding` rows currently tagged `cluster_code='M10'` at `level='CLUSTER'` are `provenance='cluster_finding_migration'`, almost all `finding_status='CLOSED'`** -- i.e. already-superseded migration artifacts, not live data this new process should sit alongside as if it were the same kind of thing. |

**Conclusion of the audit:** nothing in the current schema stores a structured, mechanically-
verifiable verse+span trace against a multi-verse, multi-tag observation. The closest analog
(`finding` + `finding_verse_link`) is missing exactly the two columns (span_surface, span_morph)
that round 2 added specifically because their absence was round 1's core defect. Building on top
of that pair without adding those columns would silently reintroduce the round-1 flaw at the DB
layer.

## 3. Three options

### Option A -- extend `finding` + `finding_verse_link` in place

- `ALTER TABLE finding ADD COLUMN family_id TEXT` (nullable; NULL for all non-cluster-reading rows)
- `ALTER TABLE finding ADD COLUMN observation_tag TEXT` (the 8-value enum above; distinct from the
  existing `finding_status` enum, which means something else -- workflow state, not claim-type)
- `ALTER TABLE finding_verse_link ADD COLUMN span_surface TEXT, ADD COLUMN span_morph TEXT`
- New table `cluster_reading_strong_check` (nothing existing fits this at all): `family_id,
  strong, occurrence_count, traced_count, missing_verses (TEXT, JSON array), checked_at`
- Use `finding.level='CLUSTER'`, `cluster_code='M10'`, `strong_number=<strong or NULL>`,
  `finding_value=<statement>`, `provenance='cluster_reading_v2'` (a new, honest provenance value
  distinguishing this from the legacy migration rows already sitting at that level).

**Pro:** reuses infrastructure that already has citation/verse-link plumbing and sits inside the
one live finding-centric model the project has settled on; a later query across ALL cluster-code
findings (old and new) stays possible without a UNION across unrelated table families.
**Con:** `finding_verse_link.span_surface/span_morph` would be NULL for every pre-existing row
(they simply don't have that data) -- a genuinely mixed-quality column from day one. `finding`
already carries a lot of columns for other eras' concerns (`characteristic_id`,
`cluster_subgroup_id`, `vcg_scope`, `justified_by_finding_id`, `supersedes_id`) that don't apply
here and would sit NULL on every cluster-reading row -- workable, but not clean.

### Option B -- new, dedicated table set (now three tiers, not one)

```
-- tier 2a: process (c) observations
cluster_reading_observation (
  id, cluster_code, family_id, process, spec_round, tag, statement,
  strong,                     -- nullable
  meaning_source,             -- nullable
  related_family, related_cluster,  -- nullable
  created_at
)
cluster_reading_trace (
  id, observation_id -> cluster_reading_observation.id,
  verse, span_surface, span_morph, seq
)
cluster_reading_strong_check (
  id, cluster_code, family_id, strong,
  occurrence_count, traced_count, missing_verses (TEXT/JSON), checked_at
)

-- tier 2b: process (d) question-answers, one-to-many slants, one-to-many traces per slant
cluster_reading_answer (
  id, cluster_code, family_id, process, spec_round,
  question_code, tier, component_code, component_title, question_text, catalogue_scope,
  created_at
)
cluster_reading_slant (
  id, answer_id -> cluster_reading_answer.id,
  slant_label, answer_text, strong             -- strong nullable
)
cluster_reading_slant_trace (
  id, slant_id -> cluster_reading_slant.id,
  verse, span_surface, span_morph, verse_text, seq
)
cluster_reading_slant_observation_ref (         -- ties a slant back to the process-c observation(s) it read
  id, slant_id -> cluster_reading_slant.id,
  observation_id -> cluster_reading_observation.id NULL,  -- resolvable link where possible
  observation_ref_text                                     -- free text fallback where not
)
cluster_reading_answer_flag (                    -- needs_adjacent_verse_context / cross_family_or_cluster
  id, answer_id -> cluster_reading_answer.id,
  flag_type ('adjacent_verse_context'|'cross_family_or_cluster'),
  verse, why,                                    -- adjacent-context flags
  statement, related_family, related_cluster     -- cross-family flags
)

-- tier 3: process (e) cross-family/cross-round synthesis, non-destructively revisable
cluster_reading_synthesis (
  id, synthesis_id (stable slug, unique),         -- referenceable by a LATER synthesis's supersedes
  cluster_code, process, spec_round, statement,
  status ('provisional'|'corroborated'|'superseded'),
  supersedes_synthesis_id -> cluster_reading_synthesis.synthesis_id NULL,  -- never an UPDATE, always a new row
  revisit_note, created_at
)
cluster_reading_synthesis_grounding (
  id, synthesis_id -> cluster_reading_synthesis.synthesis_id,
  family_id, question_code NULL, process ('process-c'|'process-d'), note NULL
)
```

**Pro:** exactly matches the JSON shape already produced and already mechanically verified against
process-A's occurrence list -- a near-1:1 load with no lossy mapping or nullable-everything-else
columns. Keeps this process's data fully separable from the legacy migration noise already sitting
in `finding`/`cluster_finding`/`cluster_observation`, so a query never has to filter out 6,430
superseded rows to find the live ~500. Cheapest to build and to reason about; easiest to drop/
rebuild wholesale if the process spec changes again (it already has once).
**Con:** a third parallel "observation" concept alongside `finding` and `cluster_finding`/
`cluster_observation` -- one more table family a future reader has to know to check. Cross-cluster-
code querying ("everything the project has ever found about M10") means a UNION across this new
set and the old `finding` rows, rather than one table.

### Option C -- hybrid

Store the tier-2a observation row itself in `finding` (Option A's two column additions to
`finding` only, not `finding_verse_link`), but give it its own dedicated trace child table
(`cluster_reading_trace`, same shape as Option B) instead of trying to retrofit
`finding_verse_link`. Tier 2b (process d) and tier 3 (process e) get the same dedicated tables as
Option B either way -- nothing about `finding`'s shape helps with a multi-slant question-answer or
a self-referencing, non-destructively-superseded synthesis claim, so there is no equivalent
"hybrid" move available for those two tiers. This keeps one canonical "list of all
project-findings" table for tier 2a specifically, while keeping every tier's actual load-bearing
content (verse-span traces, slants, synthesis grounding, supersession) in tables built exactly for
each shape. `strong_checks` still needs its own new table either way (Option A/B/C all require it).

## 4. Recommendation

**Option C for tier 2a (process-c observations); Option B's dedicated tables, unconditionally, for
tiers 2b and 3 (process d/e).** Reasoning: `finding` is explicitly the project's live universal
finding store per CLAUDE.md ("the `finding` table is now real findings only... the live unit"), so
a brand-new *observation* is worth registering there for cross-project discoverability -- but
forcing the verse-and-span trace through `finding_verse_link` either leaves two new columns NULL
on 12,491+ pre-existing VERSE-level rows and 6,430+ legacy CLUSTER-level rows, or requires
backfilling span data that may not be recoverable. A dedicated trace table sidesteps that without
giving up the one-place-to-look-for-observations property Option A was trying to preserve. For
tiers 2b and 3, `finding` offers nothing worth forcing the shape into: a slant is not "one finding,"
it is one of several possible answers to one question, and a synthesis is a claim about *other
claims* with a revision history `finding.supersedes_id` gestures at but was never built out with
the grounding-link table a real supersession chain needs. `cluster_reading_strong_check` and
`cluster_reading_answer_flag` are process/verification metadata, not findings, and have no home in
`finding` under any option.

This is a genuine judgment call, not a self-correctable implementation detail -- filed here for
researcher decision rather than applied. If approved, promoting the round-2/3 spec's temp-prefixed
scripts and this table set into permanently-registered `cfg_utility`/DB-migration work would follow
the normal `iba\app\ps\Config-Maintenance.ps1 -Step Propose` gate, not a direct edit.

## 5. Open questions for the researcher

1. The tier-2a split above (C for observations, dedicated tables for everything else), or a
   different split entirely -- including, now that three tiers exist, whether it is worth
   reconsidering Option B (fully separate for ALL three tiers, including observations) simply for
   uniformity, rather than mixing B and C by tier as recommended above?
2. Does this whole table set belong in `bible_research.db` (where `finding`/`cluster_finding`/
   `cluster_observation` already live) or `iba.db` (where this cluster-reading process's config/
   governance and its `cfg_setting.cluster_path` live)? The two DBs are currently split by a
   base-data/process-control line (`project_current_architecture_and_status` memory) that this new
   table set doesn't map onto cleanly either way -- and now less cleanly still, since process (e)'s
   synthesis tier is arguably closer to "process output" (iba.db's territory) than "base data"
   (bible_research.db's) even though it references bible_research.db-shaped verse evidence.
3. Should `missing_verses` on `cluster_reading_strong_check` ever be non-empty in a *stored* row --
   i.e. should a family's observations only be written to the DB once
   `temp_1682_verify_strong_checks.py` reports 100%, with an incomplete run never reaching the DB
   at all (matching how this session actually worked, fix-before-file)? Or is a stored "incomplete"
   snapshot itself useful history?
4. For process (e)'s `supersedes_synthesis_id` chain specifically: when a later pass supersedes an
   earlier synthesis, should the OLDER entry's `status` flip automatically (a trigger/application
   rule). to `superseded`, or should that be a separate, explicit write every time -- i.e. is
   "new row with `supersedes` set" alone sufficient provenance, or does the superseded row also
   need its own status actively updated to be found by a "show me only what's current" query?
   (This session's process-(e) JSON output does the latter by hand; a DB implementation should
   decide once, not per-write.)
5. Does H_guilt/SUNDRY's now-corrected round-2 upgrade (this session) retroactively invalidate the
   escalation #1683 question about the 32 legacy M10 characteristic rows, or is that still a fully
   separate, still-open researcher decision? (Recommendation: still separate -- #1683 is about
   whether *this whole process's output* is sufficient input to Window 2 characteristic analysis,
   not about this table-design question.)
