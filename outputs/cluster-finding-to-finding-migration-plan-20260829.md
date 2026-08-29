# Folding `cluster_finding` into `finding` — feasibility, schema changes, migration plan

Requested (4.3): is it possible to fold `cluster_finding` (19,997 rows, real content, frozen since
2026-06-19, never migrated — see the landscape review) into the live `finding` table, with no data
loss, changing `finding`'s schema if needed. **Answer: yes — full column-by-column mapping below.
Not yet executed; this is the plan, awaiting your go-ahead on the schema addition before any
`ALTER TABLE` or data copy runs.**

## 1. Column-by-column mapping

| `cluster_finding` column | populated | destination in `finding` |
|---|---|---|
| `finding_text` | 19,997/19,997 | `finding_value` — direct match, already exists |
| `finding_status` | 19,997/19,997 | `finding_status` — direct match, already exists |
| `cluster_code` | 19,997/19,997 | `cluster_code` — direct match, already exists |
| `created_at` / `last_updated_date` / `delete_flagged` | — | same-named columns — direct match |
| `obs_id` | 19,997/19,997 | **not a `finding` column at all** — becomes a new row in `finding_question_link` (`question_id = obs_id`). This is the actual answer to "do these records link to the catalogue, is this what the link tables are" — yes, and post-migration `finding_question_link` becomes the *only* live link mechanism, exactly as it already is for the rest of `finding`. |
| `characteristic_id` | 17,662/19,997 (88%) | **new column** `finding.characteristic_id` (FK → `characteristic.id`) — real structural data, no existing home |
| `cluster_subgroup_id` | 7,282/19,997 (36%) | **new column** `finding.cluster_subgroup_id` (FK → `cluster_subgroup.id`) — checked whether derivable from `characteristic_id` via `characteristic_subgroup`; not safe to assume, kept as its own column so nothing is lost |
| `vcg_scope` | populated, real VCG identifiers (e.g. `M03-C-VCG-02`, sometimes `;`-joined multiples) | **new column** `finding.vcg_scope` (TEXT) — no existing equivalent |
| `notes` | 8,920/19,997 (45%) | **new column** `finding.notes` (TEXT) — no existing free-text field on `finding` |
| `source_file`, `version`, own `id` | real provenance strings | **no new column** — folded into `finding.source_legacy_ref` as a tagged string, same convention already used for the `wa_session_b_findings` migration (`SB:{registry}-{finding_id}\|type:...`). Proposed tag: `CF:{cluster_finding.id}\|source_file:{...}\|version:{...}` |
| `finding_type` | **0/19,997 — always NULL** | dropped, nothing to migrate |
| `needs_research` | **0/19,997 — always 0** | dropped, nothing to migrate |

**Net schema change: 4 new nullable columns on `finding`** (`characteristic_id`, `cluster_subgroup_id`,
`vcg_scope`, `notes`) — smaller than it first looks, because `finding_type`/`needs_research` carry
no data at all, and `source_file`/`version` fold into the existing `source_legacy_ref` pattern
rather than needing dedicated columns.

## 2. Migration steps

1. **Schema change** (via the sanctioned path — `cfg_table`/`cfg_column` first, `configmaint.propose`
   per row, then the actual `ALTER TABLE finding ADD COLUMN ...` × 4, then a `schema_version` bump
   per project convention).
2. **Data copy**: one INSERT per `cluster_finding` row into `finding` — `level='CLUSTER'`,
   `provenance='cluster_finding_migration'` (a new provenance tag, parallel to
   `'session_b_migration'`), `source_legacy_ref` built as above, the 4 new columns carrying
   `characteristic_id`/`cluster_subgroup_id`/`vcg_scope`/`notes` verbatim.
3. **Catalogue links**: one INSERT per migrated row into `finding_question_link`
   (`finding_id` = the new `finding.id`, `question_id = cluster_finding.obs_id`, `coverage` left
   NULL — `cluster_finding` has no coverage-judgement equivalent to carry over).
4. **Verification**: row-count match (19,997 in each direction), a sample spot-check of
   `finding_value` text against the source `finding_text`, and a referential check that every new
   `finding_question_link` row resolves both ways.
5. **`cluster_finding` itself**: **not physically dropped** — soft-deleted / marked inactive in
   `cfg_table` once verified, same as `wa_session_b_findings` today. It stays on disk as the
   historical source, per the project's own no-physical-deletes convention.

## 3. What this does NOT decide

- Whether `characteristic_id`/`cluster_subgroup_id` on a VERSE/GLOBAL-level `finding` row ever make
  sense outside the CLUSTER level this migration produces — worth a look once live, but not a
  blocker (they're nullable, unused elsewhere).
- The citations question (§4 of the landscape review) — raised separately as escalation **#1022**,
  seeded with the discovery that `finding_citation` has never once cited the live `finding` table.
  Relevant here because after this migration, `finding_citation`'s current exclusive use
  (`cluster_finding`/`cluster_observation`) would point at a retired source — one more reason #1022
  is worth resolving alongside or before this migration, not after.

**Awaiting your go-ahead on the 4-column schema addition before I run any `ALTER TABLE` or data
copy.**
