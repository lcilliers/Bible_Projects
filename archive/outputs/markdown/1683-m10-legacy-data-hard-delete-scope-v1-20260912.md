# M10 legacy characteristic/subgroup data — hard-delete feasibility check

**Status:** investigation only, nothing deleted or renamed. Requested this chat turn: confirm
whether the M10 legacy rows can be hard-deleted (researcher's preferred path) so `cluster_subgroup`/
`mti_term_subgroup` can be reused clean, or whether that's "troublesome" enough to fall back to
rename-old/create-new instead.

## Verdict: hard delete is troublesome — the blast radius is much wider than the 2 tables in question

| Table | Live rows referencing M10's characteristic/cluster_subgroup ids |
|---|---|
| `characteristic` (M10 rows themselves) | 32 |
| `characteristic_subgroup` (links characteristic → cluster_subgroup) | 33 |
| `cluster_subgroup` (M10 rows themselves) | 34 |
| `mti_term_subgroup` (term placements) | 125 |
| `cluster_observation` | 36 (+56 via `cluster_subgroup_id`) |
| `cluster_finding` | 6,048 |
| `finding` | 6,048 |
| `verse_context` (`cluster_subgroup_id`) | **2,103** |
| `prose_section` | 0 |

**Total: ~14,500 rows across 9 tables**, not the 2 tables ("family"/`cluster_subgroup`) in scope for
the naming decision.

## Why it's not as bad as the raw number looks, but still not clean

- The 6,048 `finding`/`cluster_finding` rows are already known dead weight — confirmed live just
  now: all 6,048 carry `provenance='cluster_finding_migration'`, the same already-superseded
  migration-artifact layer the earlier findings-table design doc flagged (`outputs/markdown/
  1682-findings-table-design-options-v1-20260911.md` §2). Deleting these specifically would not
  lose anything live.
- CLAUDE.md's own 2026-06-25 method-reset banner already declares "all M01–M11 'completed' + all
  in-progress work is LEGACY to be revisited" — M10 falls inside that range, so the *characteristic*
  layer's irrelevance isn't a new claim, it's already the project's own documented verdict.
- **But `verse_context` is a different case.** It's a live, heavily-used, per-verse classification
  table — 2,103 rows is real per-verse data, not obviously junk the way the migration-tagged
  `finding` rows are. I have not checked whether those specific 2,103 `cluster_subgroup_id` values
  are themselves stale/unused fields on otherwise-live verse_context rows, or whether removing them
  would blank out something still read elsewhere. Not confirmed either way — flagged, not assumed.
- `cluster_observation` (36+56) is smaller but its own live-vs-dead status isn't checked either.

## The standing project convention this collides with

CLAUDE.md §3 Conventions: *"Soft deletes: `delete_flagged = 1`; no physical deletes in automated
flows."* Hard-deleting here would be a deliberate, one-off exception to a written project-wide rule
— worth doing consciously if that's the decision, not silently.

## Recommendation

Given the real scope (9 tables, not 2; one of them — `verse_context` — not confirmed safe to touch)
and the standing no-physical-delete convention, **this matches your own stated fallback: rename the
old tables, build the new family/subgroup infrastructure under the original names, fresh.**
Scoped narrowly to what "family" actually needs (`cluster_subgroup`, `mti_term_subgroup`) rather
than also trying to resolve the wider characteristic/`finding`/`verse_context` legacy-data question
in the same move — that's a separate, larger cleanup decision (whether to purge the whole
`cluster_finding_migration` layer project-wide) this doesn't have to be bundled with.

**Concretely, if approved:** rename `cluster_subgroup` → `cluster_subgroup_legacy_pre_reset` (or
similar) and `mti_term_subgroup` → `mti_term_subgroup_legacy_pre_reset`, all 175/1,196 rows
project-wide moving with them (M10's 34/125 are only part of each table); create fresh
`cluster_subgroup`/`mti_term_subgroup` tables for the new family model to write into. This means
the OTHER 141 `cluster_subgroup` rows (non-M10, other clusters) and their term memberships move to
the renamed legacy table too, not just M10's — worth confirming that's intended before executing,
since this decision, once made for M10, effectively retires the old characteristic-subgroup method
project-wide, not just for M10.
