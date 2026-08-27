> **Superseded by [prose-change-log-design-v5-20260824.md](prose-change-log-design-v5-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v3-20260824.md](prose-change-log-design-v3-20260824.md) (v1–v3
kept on disk for history). Researcher decisions this round (2026-08-24): §0d.1 **yes** — Option A
decided, `prose_section` will not carry old versions live. §0d.2 **yes** — the stylistic-revision
source is real, but its process is too early to design now (parked as a placeholder, not built). This
round (§10–§14) works through the actual column design for the current-state tables and the new
change-log table(s), including what moves/retires off the existing tables, per the researcher's
direct instruction.

Status: still **design/analysis only** — one precursor structural question is flagged for
confirmation (§10) before the column lists (§11–§13) can be taken as final; the rest is a concrete
proposal, not yet built.

---

## 10. Precursor structural question — how does "no old versions live" actually work mechanically?

Today, `supersede` works by **inserting a new row** per version and chaining
`supersedes_id`/`superseded_by_id` — the old row physically stays in `prose_section` forever (that's
the mechanism §0d.1 just ruled out). Deciding "no old versions in the live table" doesn't by itself
say *how* the row changes — there are two mechanically different ways to get there, and the column
design below depends on which one is meant:

| | **Model A — mutate in place** | **Model B — insert-then-prune** |
|---|---|---|
| Shape | One stable row per section (`id` never changes across edits). An edit is an `UPDATE` on that same row; the *prior* state is written to the history table first, in the same transaction. | Keep today's insert-new-row-per-version mechanism exactly as built; immediately after each supersede, move the now-superseded row's content into the history table and physically remove it (or blank its `body`) from `prose_section`. |
| Matches | `prose_section_type`'s existing shape (already mutate-in-place today) and `escalation`'s own current-state row (also mutated in place, with `escalation_history` alongside it) | Today's `prose_section` supersede code, unchanged, plus a new prune step bolted on after it |
| `id` stability | A section's `id` is a permanent handle — never orphaned, never points at a retired row | `id` keeps changing per version as today; the "current" row is always the newest `id` in a chain, found by walking `superseded_by_id IS NULL` |
| `supersedes_id`/`superseded_by_id` | **No longer needed at all** — nothing to chain, only one row per section ever exists live | Still needed, unchanged — the live table still needs the same chain-walking to find "current" |
| New code required | Rewrite the `supersede` operation (and `session_a_replace`, which already mutates in place, needs almost no change) | Keep `supersede` as-is; add a new prune/archive step, plus a way to keep `id` referencable from wherever it's cited elsewhere in the DB even after the row it names is gone |
| Risk | Real rewrite of a built, tested, live code path (91 real supersede events exist today) | Smaller code change, but leaves the "id changes every edit" referencing problem live — anything that stored a `prose_section.id` (e.g. `prose_section_finding_link`, `prose_section_dimension_link`, the future citation/index tables #829 D5/D6 defers) would need updating on every edit to keep pointing at the current row, or accept that it's pointing at a row that's about to be pruned out from under it |

**Recommendation:** Model A. It reads as the natural mechanical meaning of "prose should not include
the old versions" (one row, current only — not "keep inserting rows and clean up after"), it matches
the shape already proven twice in this project (`prose_section_type` today, `escalation`/
`escalation_history` as the reference pattern), and it removes the `id`-instability problem Model B
would otherwise hand to every other table that references a `prose_section.id` — a real, concrete
risk given `prose_section_finding_link`/`prose_section_dimension_link` already exist and more
citation-style links are expected later (#829 D5/D6). Model B's only advantage is smaller code churn
today, which doesn't outweigh handing a stability problem to every future consumer of the table.

**§11–§13 below are written against Model A.** Flagging this plainly rather than silently assuming
it — if Model B was actually intended, the column lists change (supersedes_id/superseded_by_id would
stay, and the history table would be populated by the new prune step instead of by the mutate-in-place
write path).

---

## 11. Revised `prose_section` — current-state only, under Model A

| Column | Change from today | Notes |
|---|---|---|
| `id` | Unchanged | Now a genuinely permanent handle — never repointed, never orphaned by an edit |
| `registry_id`, `section_type_id` | Unchanged | |
| `heading`, `body` | Unchanged **shape**, but now always reflect only the current text — prior text lives in history, not here | |
| `word_count` | Unchanged | Still cached/derived from current `body` |
| `status` | Unchanged | |
| `version` | Unchanged **shape** (still a small integer), but now increments via `UPDATE ... SET version = version + 1` in place, not via a new inserted row | Legacy mixed-type values (`'1_0'`, `'v1'`, etc. — §1's finding) need normalizing to clean integers as part of the build migration, not designed here |
| `supersedes_id`, `superseded_by_id` | **Dropped entirely** | No longer meaningful under Model A — nothing to chain |
| `author` | Unchanged **shape** — now reads as "who made the current version," full trail moves to history | |
| `created_at` | **Meaning fixed**: becomes the row's true, immutable original-creation timestamp — never touched again after the row is first inserted | |
| `updated_at` | **New column** | The one thing `prose_section` has never had — always touched on every write, including what today is `session_a_replace`, closing the exact gap §1 identified |
| `approved_at`, `approved_by` | Unchanged | |
| `metadata_json` | Unchanged | |
| `source_file` | Unchanged **shape** — now reads as "source of the current version" | Per §1, still not a reliable single-event key on its own; the history row for this edit records it too |
| `delete_flagged` | Unchanged shape, but the delete **event** itself now gets a history row (§13) — currently has none at all | |
| `cluster_code`, `characteristic_id`, `cluster_subgroup_id` | Unchanged, out of scope here | Separate relocation, #829 D5/D6, future index table — not this item |

## 12. Revised `prose_section_type` — current-state only (already mutate-in-place, no shape change to the write pattern)

| Column | Change from today | Notes |
|---|---|---|
| `id`, `code`, `label` | Unchanged | |
| `source_stage`, `lifecycle_tag`, `chapter_no`, `description`, `expected_length_min`, `expected_length_max`, `sort_order`, `book_order`, `book_label`, `section_order`, `section_label` | Unchanged shape — every change to any of these now also writes a history row (§13) | These are exactly the "chapter sequence, paragraph sequencing, book names" fields named as the direct-update source (§5) |
| `delete_flagged` | Unchanged (still declared, still unused — separate gap, not this item's fix) | |
| `created_at` | **Meaning fixed**, same treatment as `prose_section` | True creation time only |
| `updated_at` | **New column** | |
| `version` | **New column** | This table has never had one; needed for the same current-state-answerability reason as `prose_section` |

## 13. Two new history tables — different internal shape, for a real reason

Both follow the escalation precedent's overall pattern (current-state table + separate append-only
history table, `version` mirrored as a join key per §8's recommendation) — but the *internal* shape of
each history table differs, because the two current-state tables don't have the same shape of content:

- `prose_section`'s content is dominated by **one large field** (`body`) that changes wholesale on
  essentially every edit — there's little value in a field-by-field delta (escalation's pattern) when
  the one field that matters always changes together. A **full snapshot of the prior state** is both
  simpler and more directly useful here (it's literally "what version 3 said," needed for rollback,
  diff, and read-back).
- `prose_section_type`'s content is **many small, independently-changeable structural fields**
  (11 of them) — exactly the shape escalation's delta pattern (`NULL` unless that transaction actually
  set the field) was built for, and exactly the shape that makes a full-snapshot design lose "what
  actually changed this round" the way the rejected pre-2026-08-20 escalation design did. This table
  should use a **true delta**, matching `escalation_history` exactly.

### 13.1 `prose_section_history` — full snapshot per version

| Column | Purpose |
|---|---|
| `id` | Own PK (physical row identity, independent of `version`) |
| `section_id` | FK → `prose_section.id` |
| `version` | Mirrored ordinal — the version number this snapshot *was*, `UNIQUE(section_id, version)` |
| `heading`, `body`, `word_count`, `status`, `author`, `source_file`, `metadata_json` | Full prior-state snapshot — what the row looked like before this change was applied |
| `changed_at` | When this version was retired (replaces the role `created_at` used to unreliably play) |
| `changed_by` | Who/what performed the change — the actor, not just `author` (may differ: e.g. a researcher-approved flag-fix applied by Claude Code) |
| `change_reason` | Vocabulary value — see §13.3 |
| `batch_id` | Nullable — links rows changed together in one editorial pass (§0c); natural candidate value is the applied patch's own id/filename, since patches are already uniquely named and archived |

### 13.2 `prose_section_type_history` — true delta per version (escalation-style)

| Column | Purpose |
|---|---|
| `id` | Own PK |
| `type_id` | FK → `prose_section_type.id` |
| `version` | Mirrored ordinal, `UNIQUE(type_id, version)` |
| `source_stage`, `lifecycle_tag`, `chapter_no`, `description`, `expected_length_min`, `expected_length_max`, `sort_order`, `book_order`, `book_label`, `section_order`, `section_label` | Each `NULL` unless THIS transaction actually changed that field — true delta, matching `escalation_history` |
| `changed_at`, `changed_by`, `change_reason`, `batch_id` | Same meaning as §13.1 |

### 13.3 `change_reason` — vocabulary, deliberately left open now (per §0d.2)

Needs at minimum a value for every real write path found in §7 (insert, supersede/update,
delete, approve, `session_a_replace`) plus the flag-fix routine once built (#835) — that much is
concrete today. Per the researcher's own §0d.2 answer, the stylistic-revision source is real but its
process isn't ready to design — so the vocabulary should reserve a value for it now (so the column
never needs a breaking change later) without building any process around that value yet. Proposed as
a `cfg_enum` group (matching project convention, not a hardcoded `CHECK`), populated with the concrete
values now and left open to add the stylistic-revision value's real definition later without a schema
change.

---

## 14. What this drops, and what the build-phase migration needs to handle (not designed here)

- **Dropped from `prose_section` entirely:** `supersedes_id`, `superseded_by_id` (§10/§11).
- **Migration needed, not designed in this round:** the 91 existing superseded rows and their chains
  need converting into `prose_section_history` rows before/as part of the build that implements this
  — a real migration step, not a fresh-start table. Also needed: normalizing the mixed-type legacy
  `version` values (`'1_0'`, `'v1'`, etc.) to clean integers, and re-pointing anything that currently
  references a now-to-be-retired old-version `id` (checked earlier: `prose_section_finding_link`/
  `prose_section_dimension_link` are both 0 rows today, so no live references exist to migrate — worth
  re-confirming at build time, not assumed stale by then).
- **Not addressed in this round:** the FTS index change (§6's finding that all rows, including
  superseded ones, are currently searchable) is a direct, expected consequence of Model A — once old
  rows no longer live in `prose_section`, `prose_section_fts` naturally only ever indexes current
  rows. No separate fix needed; noting it here so it isn't mistaken for still-open.

---

## 15. Still open

- Confirm §10's Model A reading is correct (or correct it) before this is taken as final.
- `change_reason` vocabulary's exact value list (§13.3) — draftable next round once §10 is confirmed.
- Everything already carried from v1 §4 not resolved by this round: the real change-event unit if
  `source_file` alone isn't it (largely answered now via `batch_id` + `change_reason` together,
  worth confirming explicitly next round), and the relationship to #833/#829 §12.7 (unchanged, still
  parked).
