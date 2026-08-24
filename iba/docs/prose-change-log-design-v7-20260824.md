> **Superseded by [prose-change-log-design-v8-20260824.md](prose-change-log-design-v8-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v6-20260824.md](prose-change-log-design-v6-20260824.md) (v1–v6
kept on disk for history). Researcher answers this round (2026-08-24): 21.2 `status` gets a third
value (`declined`); 21.3 the version-as-log-id simplification is fully accepted, no longer an open
question; 21.1 raises a real mechanical question (source file vs. multiple target rows/tables) worth
resolving concretely; 21.4 **scope is confirmed project-wide** ("this is opening a big door, and I
think we should consider it"), with two new columns named and a live-DB check this round turned up
something directly relevant to the researcher's own findings forward-note.

Status: mechanically much more concrete after this round. One live discovery (§25) needs surfacing
before the table can be called settled.

---

## 23. Decisions recorded, no longer open

| Item | Answer |
|---|---|
| **21.2** — `status` third value | **Added: `declined`.** Vocabulary is now `change_proposed` / `change_applied` / `declined`. |
| **21.3** — version-as-log-id tradeoff (v6 §19.4) | **Fully accepted.** Researcher, verbatim: *"individual row version sequencing is meaningless, I am happy to simplify it to use a single reference to the log and the log id is as good as anything."* No longer flagged as an open question — `version` on the target row is a plain reference to `change_log.id`, not a per-item counter, by design. |

---

## 24. 21.1 — the source-file-to-multiple-rows mechanics, resolved concretely

The researcher's own framing: *"the source may be a single file, the target changes may be multiple
rows, multiple tables — the payload is likely to be a section row, or section-type row. Is this stored
as a compressed JSON file, and how would the split of rows work?"*

**The split:** one input file (or script/module run) can touch several target rows across both
tables in a single pass (§5's "multi-table, multi-section" source, already documented). The correct
model is **one `change_log` row per target row changed**, not one row per source file/run — matching
the researcher's own "the payload is likely to be a section row, or section-type row" framing exactly.
A chapter-edit import that supersedes 3 sections and updates the chapter's `prose_section_type` row
produces **4** `change_log` rows, each carrying one row's own payload, all sharing the same
`change_source` value (the one input file) so they remain queryable together without needing a
separate grouping field.

This resolves the `batch_id` question v6 §19.2/§22 left open: with `change_source` now covering
"file name, or originating script/module" (per 21.4 below), grouping "which changes happened
together" is already answered by *"all rows sharing this `change_source`"* in the expected case — a
separate `batch_id` isn't needed unless two genuinely different source files could land in one atomic
transaction, which hasn't come up as a real case anywhere in this thread. **Proposing to drop
`batch_id`** rather than carry it forward unresolved — flagged as a proposal, not asserted, since
it reverses something v4/v6 both listed as still-open rather than closing it silently.

**Storage format:** yes — `payload` stored as **gzip-compressed JSON text**. One JSON object per
`change_log` row, holding that one target row's relevant prior-state fields (e.g. for a
`prose_section` change: `body`, `heading`, `word_count`, `status`, `author`, `source_file`; for a
`prose_section_type` change: whichever fields actually differ, or the full prior row — per §18's
"no fine-grained isolation required," either is acceptable, full-row-snapshot is simpler to implement
correctly and is what's proposed). JSON is the right shape here specifically because it's
self-describing and works uniformly across differently-shaped target tables without needing a
different payload column per table.

---

## 25. 21.4 — scope confirmed project-wide, plus a live check that changes the picture

Researcher, verbatim: *"this is opening a big door, and I think we should consider it. table name =
not prose specific; potentially missing columns: change_type (insert / change / delete); change_source
(originating script or module). I can see potential use for it findings, but it will only become
clearer when we get to findings."*

Two new columns confirmed:

- **`change_type`** — `insert` / `change` / `delete`. Maps cleanly onto every operation already
  enumerated for the two prose tables (v4 §7): `insert`→`insert`; `supersede`, `approve`,
  `session_a_replace`, `bulk_supersede`, `prose_section_type:update`→`change`; `delete`→`delete`.
- **`change_source`** — broadened from "file name" to **file name, or originating script/module
  identifier** — covers changes with no single input file behind them at all (e.g. a future
  automated/bulk process).

**Table name** — agreed, should not be `prose_`-prefixed given project-wide scope. **Checked live
before proposing anything, not assumed clean:** `iba.db` already has a table called
**`cfg_change_log`** — unrelated in scope (12 rows, audits config-seed *loads*, not content/row
changes: `config_version`/`seed_hash`/`loaded_at`/`validated`) but close enough in name that reusing
"`change_log`" plainly for this new table would collide/confuse. Proposing a name that avoids that
clash — e.g. `content_change_log` or `record_change_log` — researcher's call on the exact word.

**The findings forward-note — a live discovery worth surfacing now, not solved now.** Checked
`bible_research.db` before writing this, per the researcher's own note that findings usage "will only
become clearer when we get to findings": a table called **`finding_revision`** already exists —
declared, currently **0 rows**, structured as:

```
finding_revision(id, finding_id, field, value_from, value_to, reason,
                  justified_by_finding_id, revised_at, revised_by)
```

This is a genuinely different shape from what's being designed here — a **field-level delta**
(`field`/`value_from`/`value_to`, one row per changed field) rather than a generic opaque `payload`,
and it carries a `finding`-specific concept (`justified_by_finding_id` — which *other* finding
justifies this revision) that has no equivalent in the prose design. It already has `reason`,
`revised_at`, `revised_by` — the same three concepts as this design's `change_reason`,
`change_datetime`, `changed_by`, independently arrived at for a different table.

Not resolving this now — the researcher's own instruction is to wait until findings work starts. But
recording it plainly so it isn't lost: whoever picks this up when findings-integration becomes
concrete will face a real choice between (a) migrating `finding` onto the new generic table too
(retiring `finding_revision`'s bespoke shape), or (b) leaving `finding_revision` as `finding`'s own
purpose-built mechanism and treating the new table as covering everything *except* findings — i.e.
"project-wide" turning out to mean "every table except the one that already had its own answer."
Either is legitimate; neither is decided here.

---

## 26. Updated field list — `content_change_log` (working name, pending §25's naming call)

| Field | Source |
|---|---|
| `id` | Own PK — **is** the `version` value written onto a target row (§18/§23) |
| `target_table`, `target_id` | Proposed in v6 §19.2, still needed for "across tables and rows" to work mechanically |
| `change_type` | New, 21.4 — `insert` / `change` / `delete` |
| `change_datetime` | Dictated, v6 §19.1 |
| `change_source` | Dictated, broadened 21.4 — file name or script/module |
| `change_reason` | Dictated, population rule per §18 |
| `changed_by` | Proposed in v6 §19.2, not contradicted |
| `status` | Dictated + 21.2's third value — `change_proposed` / `change_applied` / `declined` |
| `payload` | Proposed in v6 §19.2, confirmed this round (§24) — gzip-compressed JSON, one target row's snapshot |
| ~~`batch_id`~~ | **Proposed dropped** this round (§24) — `change_source` already answers the grouping question in the expected case |

---

## 27. Still open

- §25's table-name word choice (`content_change_log` vs. `record_change_log` vs. other).
- §25's findings-integration choice — explicitly parked until findings work starts, not this item's
  decision.
- §24's proposal to drop `batch_id` — flagged as a proposal, confirm or keep it.
- Migration of the 91 existing superseded `prose_section` rows and mixed-type legacy `version` values
  (v4 §14) — still a build-phase task, not designed.
- Diff-based storage for `payload` (v5 §16.2) — still a named future option, not scheduled.
