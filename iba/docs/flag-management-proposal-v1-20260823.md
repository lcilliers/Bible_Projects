# Flag Management — proposal (escalation #833)

**Stage: propose/design**, per the confirmed cycle (explore → **propose/design** → approve → build
→ test → approve). Built directly from the two capture documents produced during dictation —
[`flag-management-current-status-v1-20260823.md`](flag-management-current-status-v1-20260823.md)
(explore) and
[`flag-management-prose-quality-repurpose-capture-v1-20260823.md`](flag-management-prose-quality-repurpose-capture-v1-20260823.md)
(dictated decisions) — nothing re-derived, no new judgement calls beyond what was explicitly asked
for in §3d/§3e below. Nothing submitted to `configmaint.propose` or built yet.

**Scope, confirmed by the researcher (2026-08-23):** everything captured across both documents is
in scope for this build *except* what the data itself says — *"it is a good analysis and worth
keeping, but the value of the data can only be assessed when analytics kicks back in. Everything
else is left untouched for now."* §4 states exactly what that excludes.

---

## 1. Storage tables in scope, and their disposition

| Table | Today | This build |
|---|---|---|
| `wa_quality_flag_types` | 29 codes, active, term-quality vocabulary | **Repurposed** — all data hard-deleted, restructured, reseeded for prose quality (§3a) |
| `wa_data_quality_flags` | 19,866 rows, `inactive=1`, term-quality instances | **Repurposed** — all data hard-deleted, restructured (§3a) |
| `wa_session_research_flags` | 715 rows, active, analysis-phase queue | **Kept exactly as-is**, brought under real IBA governance (§3b) |
| `phase2_flag_types` | 25 codes, active | **→ `inactive=1`** (§3c), matching its own junctions |
| `mti_term_flags` / `wa_term_phase2_flags` | Already `inactive=1` | Unchanged — already consistent with `phase2_flag_types`'s new state |
| `wa_flag_type_question_link` | 12 rows, active | **Unchanged**, "for now" — its FK target is due to disappear in §3a's hard delete; explicitly not fixed here (researcher instruction) |
| `passage.review_flag` (column, `bible_research.db`) | Barely used, TEXT-typed | **Marked inactive** — new mechanism required, §3d |
| `session_d_observations.researcher_flag` (column) | Table empty (0 rows) | **Marked inactive** — same mechanism, §3d |

---

## 2. Governance — what regulates this today

No table in this family had any prose- or flag-specific `cfg_behaviour_rule`/`cfg_enum`/
`cfg_status_flow` before this proposal — the generic rules apply and this build is what satisfies
them for the first time: `governance.rules_must_be_config_driven`, `governance.tables`/
`governance.table_columns` (already satisfied at the catalogue level for every table here — the gap
is behavioural, not cataloguing), and `governance.redundancy_archiving` (bears on §3c's retirement).
`governance.escalation.scope` is the mechanism that raised this whole item — no separate flag-system
governance rule exists yet; §5's open question (weight class vs. escalation) is exactly this gap,
explicitly deferred (§4).

---

## 3. Detailed build spec

### 3a. `wa_quality_flag_types` / `wa_data_quality_flags` — hard delete + repurpose

**Sequencing matters here — data must go before schema, schema before reseed:**

1. **Pre-op backup.** Full `bible_research.db` snapshot before any step below (standard
   `_apply_*`-class discipline — `feedback_pre_op_db_snapshots_prune_or_skip` still applies: one
   snapshot for this whole operation, not one per step).
2. **Hard delete, in FK order** (children before parents): `DELETE FROM wa_data_quality_flags;`
   then `DELETE FROM wa_quality_flag_types;`. Confirmed nothing else references either table except
   `wa_flag_type_question_link` (§3e handles that separately) and `mti_term_flags`/
   `wa_term_phase2_flags` (a *different* vocabulary, `phase2_flag_types` — not touched by this
   delete).
3. **Rebuild both tables to the new shape.** Since every row is gone, a straight `DROP`/`CREATE` is
   simpler and safer than `ALTER TABLE RENAME COLUMN` + constraint surgery on a table carrying no
   data to preserve (`feedback_simple_steps_not_engineered_designs`):

```sql
DROP TABLE wa_quality_flag_types;
CREATE TABLE wa_quality_flag_types (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    flag_group    TEXT NOT NULL,
    flag_code     TEXT NOT NULL UNIQUE,
    description   TEXT,
    delete_flagged INTEGER NOT NULL DEFAULT 0,   -- renamed from `deprecated`
    deprecation_note TEXT,                       -- kept unchanged (still meaningful: why retired)
    category      TEXT,
    research_actions TEXT
);

DROP TABLE wa_data_quality_flags;
CREATE TABLE wa_data_quality_flags (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    strong_id        TEXT,                          -- renamed from term_id; optional
    verse_id         INTEGER,                        -- renamed from file_id; optional
    flag_id          INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
    description      TEXT,
    corrective_action TEXT,                          -- new
    correction_date  TEXT,                            -- new
    delete_flagged   INTEGER NOT NULL DEFAULT 0,     -- new
    last_changed     TEXT
);
```

**Decided (researcher, 2026-08-23): cross-database reference for `strong_id`/`verse_id`, approved
as proposed.** *"The strong data (term_id) is completely reworked in IBA"* — the natural target for
`strong_id` is `iba.db`'s own `strong` table (`strongNumber TEXT PRIMARY KEY`, confirmed live), not
anything in `bible_research.db`. SQLite cannot enforce a foreign key across two separate database
files — this is a **documented, informational reference only** (`cfg_column.fk` states it; nothing
in the schema enforces it), same limitation every other `bible_research.db`↔`iba.db` cross-reference
in this project already has. `verse_id`'s target is less concrete — no verse-quality-check precedent
exists yet to point at. Both typed as loose references (`strong_id TEXT`, `verse_id INTEGER`) with
`cfg_column.fk` stating the intended target in prose, not enforced.

**Cascade rule** — *"any type that is soft-deleted must automatically set the data records also as
soft delete"* — built as a trigger, matching this database's own existing convention (`prose_section
_ai`/`_au`/`_ad`, `wa_verse_records_updated_at`):

```sql
CREATE TRIGGER wa_quality_flag_types_cascade_delete
AFTER UPDATE OF delete_flagged ON wa_quality_flag_types
WHEN NEW.delete_flagged = 1 AND OLD.delete_flagged = 0
BEGIN
    UPDATE wa_data_quality_flags SET delete_flagged = 1 WHERE flag_id = NEW.id;
END;
```

**Reseed** — 3 named types, `flag_group` left as a free descriptive label since the old
`DATA_COVERAGE`/`DATA_QUALITY`/etc. grouping no longer applies (a new prose-specific grouping isn't
named yet — proposed as a single group `PROSE_QUALITY` for now, revisited as more types emerge, per
*"prose data quality types will emerge as we go along"*):

| `flag_group` | `flag_code` | `description` |
|---|---|---|
| `PROSE_QUALITY` | `Terminology change` | Prose text uses terminology superseded by a later methodology/naming decision. |
| `PROSE_QUALITY` | `Methodology change` | Prose describes a process or method that has since changed. |
| `PROSE_QUALITY` | `Style change` | Prose doesn't conform to the current style/authoring convention. |

**`cfg_table`/`cfg_column` re-catalogue** — both tables' `use` text and every column's `use` text
gets rewritten to describe the new prose-quality purpose (currently describes the retired
term-quality purpose); `wa_data_quality_flags.inactive` flips back to `0` (it's `1` today, correctly
describing the *retired* mechanism — the repurposed table is a live, active one).

### 3b. `wa_session_research_flags` — incorporated into IBA, unchanged shape

No schema change. "Alive and incorporated" is scoped narrowly here, since no specific build was
dictated beyond that phrase and nothing in governed code (`iba/app/lib/`, `iba/app/handlers/`)
currently reads or writes this table — checked directly, not assumed. Proposed as the minimum that
makes "incorporated" true without inventing unrequested functionality:

- A `cfg_write_grant` row is **not** proposed yet — no current writer exists to grant (the table's
  715 rows were all written by pre-IBA one-off scripts). Adding a grant with no real writer would be
  governance theatre.
- Instead: one `cfg_behaviour_rule` row (class=`sqlite`) stating plainly that this table is the
  retained, live analysis-phase flag mechanism, its shape is intentionally unchanged by the
  2026-08-23 flag-management review, and its known data-quality issues (`priority`/`session_target`
  vocabulary drift, `cluster_link` as a non-junction string) are deferred to the analytics-phase
  restart (§4) — so the *fact* that it's alive and deliberate is now config-recorded, even though no
  write path is built yet.
- When analytics work actually resumes and something needs to write to this table again, that's the
  point a real `cfg_write_grant`/dispatcher entry gets added — not invented ahead of need.

### 3c. `phase2_flag_types` → `inactive=1`

One `cfg_table` row update. Matches its two junctions (`mti_term_flags`, `wa_term_phase2_flags`),
already `inactive=1`.

### 3d. `passage.review_flag` / `session_d_observations.researcher_flag` — column-level inactive

**Decided (researcher, 2026-08-23): Option A, approved.** *"cfg_column should have inactive field.
this may not be DB enforceable, but at least it sets the config that the column is not used."*
`cfg_column` has no `inactive` field today (confirmed live, §4a of the capture doc) — this build
adds one:

```sql
ALTER TABLE cfg_column ADD COLUMN inactive INTEGER NOT NULL DEFAULT 0;
```

Symmetric with `cfg_table.inactive`; not DB-enforced (nothing stops a column from still being
written to — same honest limitation the researcher named directly), but it makes "this column is
config-known-dead" a real, queryable fact for the first time, general to the whole project, not a
one-off for these two columns. Then: `inactive=1` on the two named rows (`passage.review_flag`,
`session_d_observations.researcher_flag`). Note: `session_d_observations` the *table* is empty and
part of the abandoned Session D workstream — its `cfg_table.inactive` is not touched by this
proposal (not dictated), only the one column, per the instruction's literal scope.

(Option B — encoding it in `use` text only, no schema change — considered and not taken: cheaper,
but not machine-checkable, and inconsistent with how every other dead-marker in this project is a
real field, not a text convention.)

### 3e. `wa_flag_type_question_link` — explicitly untouched

No build action. Registered here (again) so the FK-orphan risk from §3a's hard delete isn't lost:
once `wa_quality_flag_types`' old rows are gone, this table's 12 rows point at nothing. Left exactly
as instructed — *"must stay for now."*

---

## 4. Explicitly deferred — the data-quality/design questions, not attempted this round

Per the researcher's own framing: *"the value of the data can only be assessed when analytics kicks
back in."* Everything below is real, already found, and stays parked — not silently dropped:

| Item | Where it's recorded |
|---|---|
| Weight-class question — flags vs. escalation, one mechanism or two | `flag-management-current-status-v1` §5 Q1 |
| `wa_session_research_flags`' `priority`/`session_target` vocabulary drift, `cluster_link` string-not-junction | Same doc §1.2/§2.3; restated in §3b above as the reason no write-grant is built yet |
| `verse_context.flagged_for_review` vs. `triage_status='ESCALATE'` — likely duplicate | Same doc §5 Q3 |
| Which generation's shape (on-record vs. separate-table) is right going forward, generally | Same doc §5 Q6 |
| Scope of "normalise" — full migration vs. design-only | Same doc §5 Q4 |
| Two-database split for the mechanism | Same doc §5 Q5 |

None of these block §3a–§3e's build — they're a different, later stage of this same escalation.

---

## 5. Test plan (required up front, results go in the resolution)

| # | Item | Test | Expected |
|---|---|---|---|
| 1 | Pre-op backup | Confirm snapshot exists and is restorable before proceeding | File present, size sane, openable |
| 2 | Hard delete | Row counts after §3a step 2 | `wa_data_quality_flags` = 0, `wa_quality_flag_types` = 0 |
| 3 | Rebuild | New schema matches §3a's DDL exactly | `PRAGMA table_info` on both, column-for-column |
| 4 | Cascade trigger | Insert 1 type + 2 data rows against it; set the type's `delete_flagged=1` | Both data rows flip to `delete_flagged=1` automatically |
| 5 | Cascade trigger — no false positives | Set `delete_flagged=1` on a type with no data rows | No error, no unrelated rows touched |
| 6 | Reseed | 3 named types present, `flag_group='PROSE_QUALITY'` | Confirmed by direct query |
| 7 | Optional columns | Insert a `wa_data_quality_flags` row with `strong_id`/`verse_id` both NULL | Succeeds |
| 8 | `phase2_flag_types` | `cfg_table.inactive` | `1`, `mti_term_flags`/`wa_term_phase2_flags` unchanged at `1` |
| 9 | `cfg_column.inactive` | Column exists, defaults `0` on every existing row | Confirmed; 2 target rows flip to `1` |
| 10 | `wa_session_research_flags` | Row count and schema unchanged | 715 rows, same `CREATE TABLE` as before |
| 11 | `wa_flag_type_question_link` | Unchanged | 12 rows, same schema, now pointing at nonexistent `wa_quality_flag_types` ids (expected — not fixed) |
| 12 | `configmaint.validate` | Full run after all steps | Clean, or only the expected §3e orphan noted as a known, accepted finding |

---

## 6. Documentation updates

- `iba/app/GOVERNANCE.md` — new section: the repurpose rationale, the cascade-trigger rule, the
  `wa_session_research_flags` retention decision, the `cfg_column.inactive` addition (if approved).
- `iba/app/BUILD.md` — build record, matching the project's existing per-build entry style.
- `iba/docs/flag-management-current-status-v1-20260823.md` and
  `-prose-quality-repurpose-capture-v1-20260823.md` — left as-is, historical record of how this was
  decided; not rewritten.
- `iba/app/USER-GUIDE.md` — not touched by this build (no new CLI surface — §3b deliberately builds
  no dispatcher entry point yet).

---

## 7. Sequencing

1. Pre-op backup.
2. Hard delete (`wa_data_quality_flags` then `wa_quality_flag_types`).
3. Rebuild both tables (§3a DDL).
4. Cascade trigger.
5. Reseed 3 types.
6. `cfg_table`/`cfg_column` re-catalogue for both tables (new `use` text, `wa_data_quality_flags.
   inactive` → `0`).
7. `phase2_flag_types.inactive` → `1`.
8. `cfg_column.inactive` column addition + set on the 2 named rows (§3d).
9. `cfg_behaviour_rule` row for `wa_session_research_flags` (§3b).
10. Run the test plan (§5), results into the resolution.
11. Documentation (§6).

---

## 8. What I need from you

Both flagged decisions answered (researcher, 2026-08-23): `strong_id`/`verse_id` typing (§3a)
approved as proposed; `cfg_column.inactive`, Option A (§3d) confirmed. Nothing else in this
document was a decision point — **one thing outstanding**: an explicit go-ahead to actually run §7's
sequence against the live databases. This includes an irreversible-in-spirit step (the hard delete
in §3a, even with a pre-op backup) — asking plainly rather than treating "the two decisions are
answered" as implicit authorisation to execute. Say the word and I'll run it, test it (§5), and
bring the full results back in one resolution.
