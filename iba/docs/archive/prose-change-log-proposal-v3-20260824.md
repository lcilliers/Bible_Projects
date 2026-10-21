# Prose change log — consolidated proposal for approval (#836)

Supersedes: [prose-change-log-proposal-v2-20260824.md](prose-change-log-proposal-v2-20260824.md).
v2 still left the test plan and build sequence as "the next step once approved" — the same class of
mistake as v1's deferred config content, and the researcher caught it the same way: governance already
requires both to be part of the proposal, not deferred. `governance.module_utility_test_plan`
(escalation #828), verbatim: *"every module/utility design **must include** a test plan... it is RUN
after the approved design is built, as a required stage of the existing plan/propose/design → approve
→ build → approve cycle."* "Must include" means in the design/proposal, not written after approval.
Sections 1–15 below are unchanged from v2. **§17–§18 are new.**

Status: **ready for approval.**

---

## 1. Objective

`prose_section` and `prose_section_type` currently have unreliable or absent change-tracking:
`prose_section` has only `created_at`, left stale by its one sanctioned in-place write path
(`session_a_replace`); `prose_section_type` has no version or last-modified trace of any kind despite
being edited in place routinely. This is being fixed now, deliberately built for the actual scale of
what's ahead — years of active editorial work (fact-correction and, increasingly, style/readability
revision) across a fact base of roughly 40,000 verses, 66 books, 50 clusters, and ~4,000
characteristics — not for today's small, early dataset (1,040 `prose_section` rows).

## 2. The model — current-state tables + a shared change log

Both tables become genuinely **mutate-in-place, current-state-only** tables (no historical rows
retained live) — the pattern formalised in the SQL standard as *system-versioned temporal tables*, not
a project invention. A new table, **`record_change_log`**, captures what each change overwrote. This
replaces `prose_section`'s existing insert-a-new-row-per-version mechanism entirely.

`record_change_log` is built **shape-generic** (`target_table`/`target_id`) so it isn't prose-specific,
per direct instruction — but this build only wires up write paths for the two prose tables. Any other
table adopting it later (`finding` is the named candidate, see §8) needs its own follow-on work, not
automatically covered by this build.

## 3. Schema — `prose_section` (revised)

```sql
ALTER TABLE prose_section DROP COLUMN supersedes_id;
ALTER TABLE prose_section DROP COLUMN superseded_by_id;
ALTER TABLE prose_section DROP COLUMN source_file;
ALTER TABLE prose_section ADD COLUMN updated_at TEXT;
```

| Column | Disposition |
|---|---|
| `id`, `registry_id`, `section_type_id`, `heading`, `body`, `word_count`, `status`, `author`, `approved_at`, `approved_by`, `metadata_json`, `delete_flagged` | Unchanged |
| `version` | Unchanged column, **redefined meaning** — now a literal pointer to `record_change_log.id`, not an incrementing counter |
| `created_at` | Meaning fixed — true, immutable original-creation timestamp, never touched again |
| `updated_at` | **New** — touched on every write, including what today is `session_a_replace`; closes the staleness gap that started this whole item |
| `supersedes_id`, `superseded_by_id` | **Dropped** — nothing to chain once there's only ever one live row per section |
| `source_file` | **Dropped** — lives only in `record_change_log.change_source` now |
| `cluster_code`, `characteristic_id`, `cluster_subgroup_id` | Unchanged, out of scope here — separate relocation, #829 D5/D6, future index table |

## 4. Schema — `prose_section_type` (revised)

```sql
ALTER TABLE prose_section_type ADD COLUMN version INTEGER;
ALTER TABLE prose_section_type ADD COLUMN updated_at TEXT;
```

Every other column unchanged in shape. `created_at`'s meaning is fixed the same way as §3 (true
creation time only). This table has never had a version or last-modified concept before — every
change to `chapter_no`/`sort_order`/`book_order`/`book_label`/`section_order`/`section_label` or any
other mutable field now gets a matching `record_change_log` row (§6).

## 5. Schema — `record_change_log` (new)

```sql
CREATE TABLE record_change_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    target_table    TEXT    NOT NULL,
    target_id       INTEGER NOT NULL,
    change_type     TEXT    NOT NULL CHECK (change_type IN ('insert','change','delete')),
    change_datetime TEXT    NOT NULL,
    change_source   TEXT,
    change_reason   TEXT,
    changed_by      TEXT    NOT NULL,
    status          TEXT    NOT NULL DEFAULT 'change_applied'
                        CHECK (status IN ('change_proposed','change_applied','declined')),
    payload         BLOB
);
CREATE INDEX idx_record_change_log_target ON record_change_log (target_table, target_id);
```

| Column | Meaning |
|---|---|
| `id` | Own PK — **the value written into a target row's `version` column** |
| `target_table`, `target_id` | Which row, in which table, this entry describes |
| `change_type` | `insert` / `change` / `delete` — see §6 for the mapping against every existing write operation |
| `change_datetime` | When the change was **applied** (system time — confirmed, not the underlying event's own real-world date) |
| `change_source` | File name, if driven from an input file — otherwise the originating script/module |
| `change_reason` | Population rule, §7 |
| `changed_by` | Who/what executed the change — distinct from `author` (whose authorial voice the text represents) and `approved_by` (who is accountable for sign-off); a genuinely third concept, confirmed against 2026 AI-authorship-accountability practice, not collapsed into one field |
| `status` | `change_proposed` (a not-yet-applied proposal — the natural home for the #835 flag-fix workflow once built) / `change_applied` / `declined` |
| `payload` | Gzip-compressed JSON. **Holds what this change overwrote or removed — its prior content, not its resulting content.** NULL for `insert` events and for the migration's baseline-backfill rows (§9) — there's nothing to have preceded either. One row per target row changed; a single input file/script producing several row-changes produces several `record_change_log` rows, all sharing one `change_source`. |

No `batch_id` — dropped; `change_source` already groups related changes in the expected case.
Table name deliberately avoids `iba.db`'s existing `cfg_change_log` (unrelated — audits config-seed
loads, checked live, not assumed clear).

## 6. `change_type` mapping — every existing write operation covered

| Table | Operation (as built in `apply_session_patch.py`) | `change_type` |
|---|---|---|
| `prose_section` | `insert` | `insert` |
| `prose_section` | `supersede` | `change` |
| `prose_section` | `delete` (soft) | `delete` |
| `prose_section` | `approve` | `change` |
| `prose_section` | `session_a_replace` | `change` |
| `prose_section` | `bulk_supersede` | `change` (one `record_change_log` row per target row) |
| `prose_section_type` | `insert` | `insert` |
| `prose_section_type` | `update` | `change` |

Every one of these gets a `record_change_log` row going forward — closing the exact selective-coverage
gap that motivated this item (`session_a_replace` and `prose_section_type.update` currently bypass all
tracking; soft-delete currently leaves no trace of who/when/why at all).

## 7. `change_reason` — population rule, not a fixed vocabulary

For a flag-driven change (once #835's fix utility is built): `change_reason` = the flag type. In every
other case: `change_reason` = the change's own source reference (the script, module, or process that
originated it) — in most cases the same value as `change_source`, restated as the reason because for
most non-flag changes "what triggered this" and "why" are the same fact.

## 8. Explicitly deferred, not designed here

- **Diff-based storage for `payload`** — scrapped for now (researcher, this round). Full compressed
  snapshots only; MediaWiki-style diffing named and set aside during design (v5 §16.2), not pursued.
- **Findings integration** — stays parked. `bible_research.db` already has a `finding_revision` table
  (0 rows, a genuinely different field-level-delta shape with its own `justified_by_finding_id`
  concept) — noted for whoever picks this up when findings work starts; **no separate escalation
  raised for it**, per direct instruction this round.
- **`prose_section_type.delete_flagged`** — confirmed live to have no code path setting it at all.
  Real, separate gap; not this item's fix.
- **A `stylistic-revision` change-reason value** — the source is real (§0 of the design log) but its
  process is too early to design; `change_reason` stays free-text (§7), so nothing schema-side blocks
  adding this later.

## 9. Migration

1. **The 91 existing superseded `prose_section` rows** — for each, write one `record_change_log` row:
   `target_table='prose_section'`, `target_id` = the row it was superseding *into* (i.e. the row that
   replaced it), `change_type='change'`, `change_reason='migration'`, `payload` = that superseded row's
   own content (compressed JSON) — it *is* a prior state by definition. Then hard-delete the row from
   `prose_section`, per direct instruction.
2. **The 949 currently-live `prose_section` rows and all 108 `prose_section_type` rows** — each gets
   one baseline `record_change_log` row: `change_type='insert'`, `change_reason='migration baseline'`,
   `payload=NULL` (nothing preceded them — as decided this round, matching how a fresh `insert` is
   handled). The row's `version` is then set to that new log row's `id`.
3. **Legacy mixed-type `version` values** (`'1_0'`, `'v1'`, etc., found live during design) resolve
   for free — every row's `version` is being replaced with a fresh `record_change_log.id` regardless
   of its old value, so no separate cleanup pass is needed.
4. **Re-confirm before hard-deleting** that nothing references a soon-to-be-removed row's `id` —
   checked during design (`prose_section_finding_link`/`prose_section_dimension_link` both 0 rows
   today), re-verify live at build time rather than trust a design-time snapshot.
5. **Side effect, not a separate fix:** once step 1 removes superseded rows from `prose_section`,
   `prose_section_fts` naturally stops indexing them too — fixing, as a byproduct, the live defect
   found during design (all 1,040 rows, including every superseded one, are currently searchable).

---

## 10. Config content — what's already there, and the boundary this proposal draws

Checked live, not assumed, before drafting anything below. `cfg_table`/`cfg_column` **already** carry
entries for `prose_section` (20 columns) and `prose_section_type` (16 columns) — an auto-derived
descriptive catalogue, built by `iba/scripts/build_dbschema.py` profiling the live schema (per
CLAUDE.md §3), not hand-authored governance. `cfg_write_grant` and `cfg_behaviour_rule` for either
table are confirmed **empty** — zero rows, matching what #829 already found. `record_change_log`
doesn't exist yet, so it's in none of these tables.

**Boundary drawn, to avoid duplicating or pre-empting #829's own still-pending proposal:**

- §11 (`cfg_table`/`cfg_column`) — new rows for `record_change_log` only, plus the literal deltas
  §3/§4 already specify for the two existing tables (drops/adds). The *rest* of `prose_section`'s/
  `prose_section_type`'s column catalogue is unaffected and re-generates automatically via
  `build_dbschema.py` once the schema changes are applied — not hand-duplicated here.
- §12 (`cfg_write_grant`) — `record_change_log` only, granted to the same `apply_session_patch`
  writer identity #829 §III already proposes for the two prose tables (consistent, not reinvented).
  `prose_section`'s/`prose_section_type`'s own write grants remain #829's proposal to approve, not
  restated here.
- §13 (`cfg_enum`) — `change_type`/`status`, new vocabulary this item introduces; nothing to do with
  `prose_section`'s own `status`/`author` enums, which are #829's scope.
- §14 (`cfg_behaviour_rule`) — four rules genuinely new to this item (the choke-point requirement,
  the `version`-is-a-pointer correction, the payload-is-prior-state rule, and a generalised one-time
  hard-delete exception). Does **not** restate #829's own drafted rules (supersede-only discipline,
  etc.) — those stay #829's to carry, corrected only where §14 below says so.

## 11. `cfg_table` / `cfg_column` — literal content

**`cfg_table`** (new row):

| database | name | grain | use |
|---|---|---|---|
| `bible_research` | `record_change_log` | one row per change event against a covered target row | Generic, project-wide change-audit log for content tables under versioning discipline (`prose_section`, `prose_section_type` to start). Captures the state a change overwrote — a target row's own `version` column is a literal pointer to this table's `id`, not an incrementing counter. Shape-generic (`target_table`/`target_id`) so other tables can adopt it later without a schema change; only the two prose tables are wired to write to it in this build. |

**`cfg_column`** (new rows, `database='bible_research'`, `table_name='record_change_log'`):

| name | ordinal | type | is_pk | notnull | fk | use |
|---|---|---|---|---|---|---|
| `id` | 1 | INTEGER | 1 | 1 | — | Own PK. The value written into a covered target row's `version` column. |
| `target_table` | 2 | TEXT | 0 | 1 | — | Which table this entry describes a change against. |
| `target_id` | 3 | TEXT | 0 | 1 | — | Which row of `target_table` this entry describes. Not a hard FK — deliberately generic across tables. |
| `change_type` | 4 | TEXT | 0 | 1 | — | `insert` / `change` / `delete`, CHECK-constrained. See proposal §6 for the mapping against every existing write operation. |
| `change_datetime` | 5 | TEXT | 0 | 1 | — | When the change was applied (system time, ISO-8601 UTC) — not the underlying event's own real-world date. |
| `change_source` | 6 | TEXT | 0 | 0 | — | File name, if driven from an input file; otherwise the originating script/module identifier. |
| `change_reason` | 7 | TEXT | 0 | 0 | — | Free text, not enum-constrained. Population rule: flag type for a flag-driven change; otherwise the change's own source reference. See proposal §7. |
| `changed_by` | 8 | TEXT | 0 | 1 | — | Who/what executed the change. Distinct from `prose_section.author` (authorial voice) and `.approved_by` (accountable sign-off). |
| `status` | 9 | TEXT | 0 | 1 | — | `change_proposed` / `change_applied` / `declined`, CHECK-constrained. Default `change_applied`. |
| `payload` | 10 | BLOB | 0 | 0 | — | Gzip-compressed JSON. The prior content this change overwrote or removed — never the resulting content. NULL for `insert` events and migration-baseline rows. |

**`cfg_column`** (deltas for `prose_section`, `database='bible_research'`):

| name | change | use (new/updated text) |
|---|---|---|
| `supersedes_id` | **`inactive=1`** (column dropped from schema; row kept for provenance, not deleted, per `governance.tables`' "no longer in use → inactive" convention) | *(unchanged text, historical)* |
| `superseded_by_id` | **`inactive=1`** | *(unchanged text, historical)* |
| `source_file` | **`inactive=1`** | *(unchanged text, historical)* |
| `version` | **use text corrected** | "A literal pointer to `record_change_log.id` — the log row describing this section's own most recent change — not an incrementing per-item counter. Corrects the prior description (`'1_0'`/`'v1'`-style mixed-type drift), resolved by this migration: every row receives a fresh pointer regardless of its old value." |
| `updated_at` | **new row**, ordinal 20 | "When this row was last written, touched on every write path including `session_a_replace` — the gap that motivated this table's versioning rebuild. `created_at` is reserved for true original-creation time only." |

**`cfg_column`** (new row for `prose_section_type`, `database='bible_research'`):

| name | ordinal | type | use |
|---|---|---|---|
| `version` | 16 | INTEGER | Pointer to `record_change_log.id`, same meaning as `prose_section.version`. This table has never carried a version concept before. |
| `updated_at` | 17 | TEXT | Touched on every write. `created_at` reserved for true creation time only. |

## 12. `cfg_write_grant` — literal content

| writer | table_name | database |
|---|---|---|
| `apply_session_patch` | `record_change_log` | `bible_research` |

Reuses the exact writer identity #829 §III already proposes for `prose_section`/`prose_section_type`
(same code path, `apply_session_patch.py`) — not a new identity invented for this table.

## 13. `cfg_enum` — literal content

| name | value | ordinal |
|---|---|---|
| `record_change_log_change_type` | `insert` | 1 |
| `record_change_log_change_type` | `change` | 2 |
| `record_change_log_change_type` | `delete` | 3 |
| `record_change_log_status` | `change_proposed` | 1 |
| `record_change_log_status` | `change_applied` | 2 |
| `record_change_log_status` | `declined` | 3 |

Matches the project's established pattern (seen on `prose_section.status`/`.author` already):
CHECK constraint enforces the vocabulary in the DB; `cfg_enum` documents/governs it as the
config-of-record, per `governance.rules_must_be_config_driven`.

## 14. `cfg_behaviour_rule` — literal content

All four rows: `class='sqlite'`, `source='escalation #836'`.

| rule_key | rule_text |
|---|---|
| `record-change-log-choke-point` | Every write to a table under `record_change_log` versioning discipline (`prose_section`, `prose_section_type`) must produce a matching `record_change_log` row in the same transaction as the write itself — no code path may update a covered table's `version`/`updated_at` without also inserting the corresponding log row. Applies to every operation on the covered tables (proposal §6's full mapping), not only the ones already visible in today's single-writer code path — closing the exact selective-coverage gap (`session_a_replace`, `prose_section_type.update`) that motivated this item. |
| `record-change-log-version-is-pointer` | A covered target row's `version` column is not an incrementing per-item counter — it is a literal foreign key to `record_change_log.id`, the log row describing that row's own most recent change. **Corrects** the `version = old.version + 1` text #829 §5 drafted before this item existed; that text is superseded by this rule, not left standing alongside it. |
| `record-change-log-payload-is-prior-state` | `record_change_log.payload` holds what a change overwrote or removed — its prior content — never the resulting/current content. The covered table's own current row already holds current content exactly once; duplicating it into the log is a defect, not a safety margin. `payload` is NULL for `insert` events and for one-time migration-baseline rows, where no prior state exists. |
| `one-time-hard-delete-exception` | A hard (physical) delete of DB rows is normally disallowed (the standing no-physical-delete-in-automated-flows convention) but is permitted as a **one-time, explicitly-instructed migration action** — first established for #833's prose-quality-table repurpose, applied again here for the 91 superseded `prose_section` rows once their content is captured in `record_change_log`. Each occurrence needs its own explicit researcher instruction; this rule records the pattern, it doesn't pre-authorise future hard deletes generically. |

## 15. `configmaint.propose` batch — sequencing

Per `governance.config_control`, every row above goes through `iba\app\ps\Config-Maintenance.ps1
-Step Propose`, approval-gated, in this order once this proposal is approved:

1. §11 — `cfg_table` + `cfg_column` (schema description first, before anything references it)
2. §13 — `cfg_enum` (vocabulary, before the write grant/behaviour rules that assume it)
3. §12 — `cfg_write_grant`
4. §14 — `cfg_behaviour_rule`

Then, per `governance.governance_md_on_rule_change`: `GOVERNANCE.md` gets updated to reflect §14's
four new rules in the same unit of work as applying them — not left as config-only.

---

## 16. Test plan (required up front — `governance.module_utility_test_plan`, escalation #828)

Results go in the build's escalation resolution when this is built — not just asserted.

| # | Case | Setup | Expected result |
|---|---|---|---|
| 1 | `prose_section` insert | Insert a new section via `apply_session_patch` | 1 `record_change_log` row: `target_table='prose_section'`, `change_type='insert'`, `payload=NULL`; the new row's `version` = that log row's `id` |
| 2 | `prose_section` supersede | Edit an existing section's `body` | 1 log row: `change_type='change'`, `payload`= compressed JSON of the row's content *before* the edit; target's `version` updated to the new log id; `updated_at` touched |
| 3 | `prose_section` soft delete | Delete-flag a section | 1 log row: `change_type='delete'`, `payload` = content immediately before the delete; `delete_flagged=1` set on the target |
| 4 | `prose_section` approve | Approve a `draft`/`in_review` section | 1 log row: `change_type='change'`, `payload` = pre-approval content (status especially); `approved_at`/`approved_by` set on the target |
| 5 | `prose_section` `session_a_replace` | Run a Session A mechanical replace | 1 log row: `change_type='change'`, `payload` = pre-replace content; **`updated_at` touched** — the exact staleness gap this item exists to close |
| 6 | `prose_section` `bulk_supersede`, 3 targets | One patch batch touching 3 sections | 3 separate log rows, one per target, all sharing one `change_source`; each target's `version` independently correct |
| 7 | `prose_section_type` insert | Insert a new section type | 1 log row: `change_type='insert'`, `payload=NULL`; new row's `version` = the log id |
| 8 | `prose_section_type` update | Change `chapter_no` on an existing type | 1 log row: `change_type='change'`, `payload` = pre-change row content; **`updated_at` touched** — this table's own never-had-one gap closed |
| 9 | `change_reason` — flag-driven | Simulate a flag-fix-style change with a flag type given | `change_reason` = the flag type, not the source reference |
| 10 | `change_reason` — default | A normal script-driven change, no flag involved | `change_reason` = the change's own source reference (matches `change_source`) |
| 11 | Migration — superseded rows | Run migration step 1 against the 91 live superseded rows | Each produces exactly 1 log row with its own content as `payload`; all 91 rows are then absent from `prose_section` (hard-deleted); 0 remain |
| 12 | Migration — baseline backfill | Run migration step 2 against the 949 live sections + 108 types | Each gets exactly 1 log row (`change_type='insert'`, `change_reason='migration baseline'`, `payload=NULL`); every target's `version` correctly points at its own new log row |
| 13 | Migration — referential safety | Before hard-deleting the 91 rows | Confirm live: 0 rows in `prose_section_finding_link`/`prose_section_dimension_link` reference any of the 91 ids (re-verified at build time, not assumed from design-time snapshot) |
| 14 | Migration — legacy `version` cleanup | After migration completes | 0 rows anywhere carry a mixed-type legacy `version` value (`'1_0'`, `'v1'`, etc.) — every `version` is a clean integer matching a real `record_change_log.id` |
| 15 | FTS side effect | After migration | `prose_section_fts` row count matches live `prose_section` row count exactly (949) — no superseded content remains searchable |
| 16 | `cfg_write_grant` enforcement | Call `Cfg.may_write('apply_session_patch', 'bible_research')` | Result set includes `record_change_log` |
| 17 | `cfg_write_grant` — negative | Call `Cfg.may_write('some_other_identity', 'bible_research')` | Result set does **not** include `record_change_log` |
| 18 | Config validation | Run `configmaint.validate` after §15's batch is applied | Clean — no orphan enum values, no missing `cfg_column.use` text, no unregistered write-grant writer |

## 17. Build sequence

1. **Approval gate** — this proposal approved by the researcher; nothing below starts before that.
2. **Backup** `bible_research.db` before any write — the migration's hard-delete (§9 step 1) is
   real, non-reversible data loss if something goes wrong; this is exactly the case the
   pre-op-snapshot convention exists for, not one to skip.
3. **Config**: run the `configmaint.propose` batch in §15's order (§11 → §13 → §12 → §14), each
   individually approved.
4. **Schema DDL**: apply §3 (`prose_section` ALTERs), §4 (`prose_section_type` ALTERs), §5
   (`CREATE TABLE record_change_log` + index), in that order.
5. **Re-run `build_dbschema.py`** to regenerate the auto-derived `cfg_table`/`cfg_column` catalogue
   against the new live schema — confirms §11's note that this happens automatically, not by hand.
6. **Code**: add one shared write-path helper in `apply_session_patch.py` implementing the
   `record-change-log-choke-point` rule (§14) — called from all 8 operation branches (§6's mapping),
   computing `change_type`/`payload`/`change_reason` per §6/§7 and writing the target row's `version`
   from the new log row's `id`, in the same transaction as the target-table write. Literal diff
   written at this step, not in this design document.
7. **Register** the changed script per `governance.new_utility_registration_timing` — confirm
   `apply_session_patch.py`'s existing `cfg_utility` row still accurately describes it once the new
   write path is added (it already exists as a registered utility; this is a re-check, not a new
   registration).
8. **Migration**: run §9 in its stated order — referential-safety check (step 4) before the hard
   delete (step 1), then baseline backfill (step 2), then legacy-value cleanup confirmation (step 3).
9. **Run the test plan** (§16) against the built system; record actual results (not asserted) in this
   escalation's resolution, per `governance.module_utility_test_plan`.
10. **Documentation**: update `GOVERNANCE.md` with §14's four rules (same unit of work as step 3, per
    `governance.governance_md_on_rule_change` — listed separately here only for build-step clarity).
    Update `docs/prose-store-architecture.md` where it still describes the insert-per-version
    mechanism §2 replaces.
11. **Close the loop on #829** — correct its §5 draft rule text to point at
    `record-change-log-version-is-pointer` instead of restating the superseded assumption; take #829
    off hold.

`iba/app/BUILD.md` is not triggered by step 6 specifically — `apply_session_patch.py` lives in
`scripts/`, not `iba/app/**`, so `governance.build_md_on_code_change`'s literal scope doesn't cover it;
noted here rather than silently applied or silently skipped. `BUILD.md` **is** updated for the config
changes themselves (steps 3–5), which are IBA-governed regardless of which script performs the write.

---

## 18. What this closes, and what happens next

- Unblocks **#829** — §17 step 11.
- Nothing left deferred: config content (§11–§15), test plan (§16), and build sequence (§17) are all
  in this document now.

This document is the thing awaiting your approval.
