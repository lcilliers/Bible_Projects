> **Superseded by [prose-change-log-proposal-v2-20260824.md](prose-change-log-proposal-v2-20260824.md)**
> — v2 adds the literal config content (§11–§15) this version wrongly deferred. Kept on disk for
> history.

# Prose change log — consolidated proposal for approval (#836)

Status: **ready for approval.** This consolidates nine rounds of design work
([prose-change-log-design-v1](prose-change-log-design-v1-20260824.md) through
[-v9-20260824.md](prose-change-log-design-v9-20260824.md), kept on disk as the reasoning trail) into
one standalone specification. Every decision below is settled; nothing here is presented as still
open. This round also closes the last three items: baseline-payload = NULL as proposed; diff-based
storage scrapped for now; findings-integration stays parked, no separate escalation raised for it.

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
table adopting it later (`finding` is the named candidate, see §7) needs its own follow-on work, not
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
other mutable field now gets a matching `record_change_log` row (§5).

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
| `change_reason` | Population rule, §8 |
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

## 10. What this closes, and what happens next

- Unblocks **#829** — its §5 draft `cfg_behaviour_rule` text (`version = old.version + 1`) needs
  correcting to describe the pointer semantics in §5 above, not an incrementing counter; #829 can come
  off hold once this proposal is approved.
- **Governance/config registration** (per `governance.rules_must_be_config_driven`,
  `governance.module.config`) — not done in this design round: `cfg_table`/`cfg_column` entries for
  `record_change_log` and the two revised tables, a `cfg_write_grant` for whichever process writes to
  it, and a `cfg_enum` entry documenting `change_type`/`status` (matching `prose_section`'s own
  existing pattern — literal `CHECK` constraints on the table, governed/documented via `cfg_enum`
  alongside them) — all follow-on build-stage work, once this specification is approved.
- **Test plan** — required up front per the standing rule (escalation #828) before building — not
  drafted in this document; the next step once approved.

This document is the thing awaiting your approval. Once approved, the next round drafts the test plan
and literal `configmaint.propose` payloads, matching the cycle used for #829/#833.
