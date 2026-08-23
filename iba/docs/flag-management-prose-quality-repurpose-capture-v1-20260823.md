# Flag Management — disposition of the flag-table family (captured, not yet designed/built)

**Stage: capture only**, per explicit instruction (researcher, 2026-08-23): *"let me stop here for
you to first capture this."* Nothing below has been designed into literal `cfg_*` payloads,
proposed, or built. This is a faithful record of the dictated instruction, for the propose/design
stage that follows once dictation continues/completes.

**Mandate, verbatim**: *"It is the right time to take control of this fragmented situation and to
get rid, or align the structures appropriately."*

---

## 1. What's being decided

**Verdict on the current data**: all of it is invalid, not just untidy.
- `wa_data_quality_flags`' `term_id` values are Strong's-identifying, but *"the strong data (term_id)
  is completely reworked in IBA, and all the data for terms in bible_research_db is no longer
  valid."*
- `file_id` (FK to the legacy `wa_file_index`) is *"redundant."*
- *"The rest of the data in this table is redundant"* — i.e. every column's content, not only these
  two.
- Verdict: *"all the data records, and all the types can be hard deleted from these two tables."*
  Stated as a deliberate, one-time, researcher-authorised purge of data already confirmed invalid —
  not a change to the project's standing no-physical-delete-in-automated-flows convention, which
  governs ongoing/automated processes, not a single dictated cleanup act. Flagging this distinction
  here so it's captured correctly, not raised as an objection.

**Verdict on the tables themselves**: keep the shape, change the purpose. *"These two tables kan
[can] be repurposed for prose quality checks."*

## 2. Structural changes dictated

### `wa_quality_flag_types`

| Change | Detail |
|---|---|
| Rename `deprecated` → *"soft-delete"* | Captured as: rename to `delete_flagged`, the project's standard soft-delete column name everywhere else (`prose_section.delete_flagged`, `finding.delete_flagged`, etc.) — *"to be consistent with other tables"* is read as meaning that specific, already-established name. Flagged for confirmation when this becomes a real proposal, not assumed silently. |

### `wa_data_quality_flags`

| Change | Detail |
|---|---|
| Add a soft-delete column | Same name/shape as above — `delete_flagged`, not currently present on this table at all. |
| Cascade rule | *"Any type that is soft-delete must automatically set the data records also as soft delete."* — soft-deleting a `wa_quality_flag_types` row must automatically soft-delete every `wa_data_quality_flags` row pointing at it. A real behaviour to design/build, not stated as automatic-by-default in SQLite — noted as a design item for the next stage, not resolved here. |
| Rename `term_id` → `strong_id` | Repurposed to hold a Strong's number, prose-quality-checking context. |
| Rename `file_id` → `verse_id` | Repurposed to hold a verse reference, prose-quality-checking context. |
| New column: `corrective_action` | *"The data record will define the change in the description, [and] the corrective action in the new column."* — `description` = what the issue/change is; `corrective_action` = what was/should be done about it. |
| New column: `correction_date` | When the corrective action was taken. |
| `verse_id` and `strong_id` are optional | *"is optional"* — nullable; a prose-quality flag need not always be tied to a specific verse or a specific Strong's number. |

## 3. The new vocabulary — `wa_quality_flag_types`, repurposed content

*"Prose data quality types will emerge as we go along."* Not a closed list — three types named as
already-encountered, real examples, to seed the repurposed table:

- `Terminology change`
- `Methodology change`
- `Style change`

More types are expected to be added as they come up in practice, not designed exhaustively up
front.

## 4. Disposition of the rest of the flag-table family

Continuing dictation, 2026-08-23. Covers the tables from the explore stage (§1.1 of
`flag-management-current-status-v1-20260823.md`) not addressed in §1–§3 above.

| Table | `cfg_table.inactive` today | Decision | Detail |
|---|---:|---|---|
| `wa_session_research_flags` | 0 (active) | **Stays as-is, stays alive, gets incorporated into IBA.** | *"wa_session_research_flags are analysis phase, and at this point stay as is, and should be alive and incorporated in IBA."* No schema change dictated — this is the analysis-phase pointer/observation queue (§2.2 use type B of the current-status doc), kept in its current shape. "Incorporated in IBA" is captured as: needs real IBA governance built around it (write grants, a dispatcher entry point, etc. — not yet designed, next stage's job), distinct from the repurposed pair in §1–§3, which changes shape. |
| `phase2_flag_types` | 0 (active) | **→ `inactive=1`.** | *"Phase2_flag_types is associated with wa_term_phase2_flags, and should be inactive = 1."* Brings it in line with its own junction tables — `wa_term_phase2_flags` (1,570 rows) and `mti_term_flags` (1,005 rows) are already `inactive=1` today; only the vocabulary table itself was still active. All three now consistently inactive. |
| `wa_flag_type_question_link` | 0 (active) | **Stays, no change "for now."** | *"wa_flag_type_question_link must stay for now."* Flagged, not decided: its 12 rows FK to `wa_quality_flag_types.id` for the *old* term-quality vocabulary — once §1–§3's hard delete removes those type rows, these 12 rows lose their target. Left exactly as dictated ("for now"), not fixed or even raised as a blocking concern — noted here so it isn't lost when the hard delete actually executes. |

### 4a. Two dead columns — dictated inactive, mechanism gap found while capturing

*"passage.review_flag must be inactive=1 as well as session_d_observations.researcher_flag."*
(`session_d_overvations` in the original message, read as a typo for `session_d_observations` —
the table already known from the explore stage to be entirely empty, 0 rows.)

Both are **columns**, not tables — and checking the live `cfg_column` schema directly to record
this properly surfaced a real gap: **`cfg_column` has no `inactive` field at all** (its columns are
`database`/`table_name`/`name`/`ordinal`/`type`/`is_pk`/`notnull`/`is_unique`/`dflt`/`fk`/`use`/
`expectation`/`source`/`filled_by` — checked directly, not assumed). `cfg_table.inactive` is what
governs whole tables (used for §4's `phase2_flag_types` decision); there is currently no equivalent
for marking one column of an otherwise-live table dead. `passage.review_flag` sits on `passage`
(bible_research.db), a table that stays very much active for the whole debate/passage pipeline — so
this can't be captured as a table-level `cfg_table.inactive=1` the way `phase2_flag_types` was.
`session_d_observations.researcher_flag` is different in kind — the *table itself* is empty (0
rows, part of the abandoned Session D workstream per the explore stage), so marking the table
inactive would also correctly cover its one column; marking column-level inactive there is
possible but not strictly required by the data.

Captured as: intent = both columns are dead and should read as inactive; mechanism = not yet
decided — either a new `cfg_column.inactive` field (a real, small schema addition to a `cfg_*`
table itself, needing its own decision/build) or some other route. Flagged, not resolved, per the
capture-only stage.

## 5. Explicitly not yet done

- No literal `cfg_*`/DDL payload written.
- No decision on exact column types, ordinals, or `cfg_enum` backing for the new type vocabulary.
- No decision on how/where the cascade rule (soft-delete propagation) gets enforced — trigger,
  application code, or a `cfg_behaviour_rule` naming it as a manual discipline.
- No decision on whether "hard delete" here means a literal `DELETE FROM` (with what pre-backup
  discipline) or some other mechanism.
- The soft-delete rename's exact target name (`delete_flagged`) is captured as the most likely
  reading, not confirmed.

Awaiting the next piece of dictation before moving to propose/design.
