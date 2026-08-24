# Prose management in IBA — first layer: consolidated proposal (escalation #829) — v9

**Supersedes v1–v8** (`prose-management-iba-first-layer-proposal-v1` through `-v8-20260824.md`, all
kept on disk for history). **This is a full consolidation, not another incremental delta.**

> **BUILT 2026-08-24, per direct researcher approval ("approve to go ahead and build").** D10
> explicitly deferred by researcher instruction: *"D10 will be edited in prose edit stage, not in
> this IBA processing build."* Two gaps the researcher found in this document before approving are
> now closed, not just noted: (1) PS-accessibility for every dispatcher step, confirmed live via
> `Prose.ps1` itself (all 5 steps tested through the actual dispatcher, not the Python functions
> directly) — this also surfaced and fixed a real pre-existing bug (`-Input` colliding with
> PowerShell's automatic pipeline variable, renamed `-InputFile`). (2) Script-column update hooks —
> the 4 reactivated scripts were verified live to already delegate entirely to `prosestore.py` (no
> duplicate logic to go stale against the schema changes); `prosestore.py` itself was updated for
> every config/schema change this build makes. Full build record: `GOVERNANCE.md` §53, `BUILD.md`
> §176.

## 0. Why this version exists, and how it differs from v1–v8

**Researcher instruction, verbatim (2026-08-24):** *"I reviewed version 1-8. They all seem to deal
with different topics or answer individual streams of thought. We now need one comprehensive
proposal document that is consolidated and can be reviewed as a whole. This consolidation should
include the final state of all the different areas, including the exact updates that will be made
to configs tables, and prose tables. It is important to check the status of the configs on disk and
the table schemas to ensure that you are not working from memory but from disk. The proposal
document must include all the configurations that build elements that must be updated in the build,
and not silently exclude anything, unless they are already signposted on another escalation."*

**What was wrong with v1–v8 as a set:** each revision answered one review round and then deferred
everything unchanged to the previous file ("Unchanged from v6 — not reproduced again, see v6 §5"),
so v8 alone cannot be read standalone — reconstructing the actual final position meant chasing
references back through v7, v6, and sometimes v4/v1. That is exactly the researcher's complaint.
**This document is self-contained.** No section below says "see vN" for content — every table,
payload, and decision is reproduced in full, as it actually stands today.

**Everything below was re-verified live against `iba.db` and `bible_research.db` this round
(2026-08-24), not carried forward from v8's prose.** Two real discrepancies were found doing that,
neither previously recorded anywhere in this thread:

1. **§1.3d / §5 component V's "drop 3 stale `cfg_column` rows" item is already done — verified
   live, not still open as v7/v8 claimed.** `cfg_column` for `prose_section`'s `supersedes_id`/
   `superseded_by_id`/`source_file` rows are not deleted, but all three are set `inactive=1` — the
   correct, established treatment (`cfg_column.inactive` is a real project-wide field, added by
   escalation #833, `GOVERNANCE.md` §51.2, specifically so "this column is config-known dead" is a
   queryable fact without deleting the row). v7/v8 both proposed a literal `DELETE`, apparently
   without re-checking `cfg_column` after #836's own migration ran — the migration script
   (`iba/app/migration/prose_change_log_build_v1_20260824.py`) already marked them `inactive=1`
   itself. This build item is **removed from the remaining to-do list below**, not carried forward
   as still-pending.
2. **New finding — `prose.book_stage_map`'s design (a stage-list per book) already disagrees with
   live `book_label` data on one row, found by cross-tabbing `source_stage` against `book_label`
   directly.** `prose_section_type` id 78 (`prog_purp_observations_framework`, "The Observations
   Framework — First Tier") has `source_stage='programme'` but `book_label='Detail design'`
   (`section_label='Observation framework'`, `section_order=6`) — the only row where a type's
   `source_stage` and `book_label` don't fall into the same group the proposed `book_stage_map`
   value would assume. Every other `programme`-stage row (51 of them) is `book_label='Programme'`.
   Under the proposed `cfg_prose.book_stage_map` value (§5, component IV below — unchanged from
   v1–v8, a stage-list keyed by book), `prose.extract --book "Detail design"` would **not** include
   this row (its stage isn't in that book's list), and `--book "Programme"` **would** include it
   (its stage is), even though `book_label` — the column that already states the answer directly and
   per-row — says the opposite. This is a genuine, previously-unflagged design tension: the proposed
   config derives book membership indirectly from `source_stage`, when `book_label` already states
   it directly and is the more precise column for exactly this purpose. **Flagged as a decision for
   this round (D10 below), not silently fixed** — the recommendation is to switch `prose.extract`'s
   book-filtering to read `book_label` directly instead of maintaining a separate derived
   `book_stage_map`, but that's a code-behaviour change beyond this proposal's original scope, so it
   is surfaced as a decision, not assumed.

No other content changes from what v8 last stated — this consolidation reproduces the same design,
the same nine (now ten) decisions, the same build spec, in one place, corrected for the two findings
above.

---

## 1. Storage tables in this scope, and how they relate

### 1.1 The table family and its relationships (live, post-#836)

```
prose_section_type  (dictionary — bible_research.db, 108 rows, 18 columns)
      │  section_type_id (FK, required)
      ▼
prose_section  (content — bible_research.db, 949 rows, 18 columns — current-state-only, Model A)
      │
      ├──► prose_section_fts (+ 5 FTS5 shadow tables) — system-driven full-text search index only
      │       (949 rows, kept in sync automatically by trigger)
      ├──► prose_section_dimension_link  — citation-like table, 0 rows; belongs to the analytic
      │       phase of prose development, out of this build (§1.2)
      ├──► prose_section_finding_link    — same kind, same phase, same disposition
      └──► version  ──────────────────────────────────────►  record_change_log.id  (literal
                                                                pointer, not an incrementing counter)

record_change_log  (bible_research.db, 1,148 rows — project-wide, keyed target_table/target_id,
   NOT prose-specific by design — researcher: "this is opening a big door")
   Columns: target_table · target_id · change_type (insert/change/delete) · change_datetime
   (system-applied time) · change_source (file or script/module) · change_reason · changed_by ·
   status (change_proposed/change_applied/declined — change_proposed is the intended home for
   #835's not-yet-built flag-fix workflow) · payload (gzip JSON — the PRIOR content only, never
   the resulting content; NULL for inserts/migration-baseline rows).
   Already fully built and governed: cfg_table + cfg_column rows live; 4 cfg_behaviour_rule rows
   (§2.1 below); 1 cfg_write_grant row (apply_session_patch → record_change_log). Escalation #836.

┄┄┄┄┄┄┄┄┄ NOT linked to prose_section — by design, not by omission (§12.2) ┄┄┄┄┄┄┄┄┄

wa_quality_flag_types (3 codes, group 'PROSE_QUALITY'    wa_session_research_flags (715 rows)
   — repurposed 2026-08-23, escalation #833, hard              — unaffected by #833/#836, has a
   delete confirmed live: 0 rows carried over)                 real resolved lifecycle, but
      │  flag_id                                               targets word_registry, not
      ▼                                                         prose_section — out of this scope
wa_data_quality_flags (0 rows today — hard-deleted and
   repurposed 2026-08-23; strong_id/verse_id both optional,
   loose refs, no enforced FK — SQLite cannot FK across
   bible_research.db/iba.db)
```

**Citation columns — `registry_id`/`cluster_code`/`characteristic_id`/`cluster_subgroup_id` on
`prose_section`.** Researcher framing (2026-08-24): *"referencing the registry/cluster/
characteristic etc. is all about citation. The citation columns cannot be on `prose_section` or
`prose_section_type`, they all belong in separate index tables. Ultimately these index tables will
all form part of book 5 — Concordance."* This decision covers all four columns, not just the two
that were given formal D-numbers (§6 D5/D6). Building the Concordance book is explicitly out of
scope for this first-layer work, so the four columns stay on `prose_section` for now, undecided in
schema terms but **not** undecided in principle — the decision already exists, it just was not yet
written into `cfg_column.use` itself (fixed in §5 below). Live population, checked this round:
`registry_id` 141/949 (14.9%), `cluster_code` 175/949 (18.4%), `characteristic_id` 124/949 (13.1%),
`cluster_subgroup_id` 0/949 (never used).

The quality-flag family is drawn separately because **no FK, junction, or code path connects it to
`prose_section`, by design** (§12.2) — every table in it targets `word_registry`/a bare Strong's
string/a bare verse id, never a prose row, and stays that way.

### 1.2 In / out of this build's scope, per table

| Table | Rows | Columns | This build (§4/§5) | Why |
|---|---:|---:|---|---|
| `prose_section_type` | 108 | 18 | **IN** | `source_stage`/`lifecycle_tag`/`book_label` need `cfg_enum` backing (currently uncontrolled — no CHECK constraint); 4 columns (`book_order`/`book_label`/`section_order`/`section_label`) still have blank `cfg_column.use` text (§1.3b, still open, verified live this round). `version`/`updated_at` (added by #836) already have correct `use` text — nothing to do there. Conceptual role: defines the core structure and sequence of the content of the books contained in prose. |
| `prose_section` | 949 | 18 | **IN** | `status`/`author` CHECK values need `cfg_enum` backing; write operations need `cfg_status_flow`/`cfg_behaviour_rule`/`cfg_write_grant` — the `record_change_log`-choke-point rules already exist (#836), but `prose_section`/`prose_section_type` themselves are not yet granted as writable tables to `apply_session_patch` (only `record_change_log` is, confirmed live). Conceptual role: the sub-chapter text — the paragraphs of the book. |
| `prose_section_fts` + 5 shadow tables | 949 (index) | 24 | **OUT — no action** | SQLite-managed, auto-synced by trigger, already fully catalogued. Row count fell 1,040→949 automatically when #836's migration deleted the 91 superseded rows. |
| `prose_section_dimension_link` | 0 | 4 | **OUT of population — decision §6 D4** | Citation-like table, belongs to the analytic phase of prose development, not simply dead. FK target (`dimension_id`) points at the retired 2026-05-04 dimension-review concept. |
| `prose_section_finding_link` | 0 | 4 | **OUT of population — decision §6 D3** | Same kind, same phase. FK points at the legacy `wa_session_b_findings`, not the live `finding` table. |
| `record_change_log` | 1,148 | 10 | **OUT — already fully built and governed by #836.** Named here only so the table family picture is complete; no action item against it in this proposal. **Cross-reference registered against #831** (its context, updated live 2026-08-24): any new prose-editing tooling #831 designs must also write a matching `record_change_log` row in the same transaction as its own writes — the choke-point rule binds every write path to `prose_section`/`prose_section_type`, not only `apply_session_patch.py`'s existing 8 operations. | |

### 1.3 Real gaps found by reading the live schema directly

**a) Citation-column decision exists but was never written into `cfg_column` itself.** The
researcher's decision (§1.1) covers `registry_id`/`cluster_code`/`characteristic_id`/
`cluster_subgroup_id` together. Checked live this round: all four columns' `cfg_column.use` text
still carries only plain population-percentage description, no citation-column note anywhere. This
is the real, still-open item — not a fresh judgement call, a `governance.rules_must_be_
config_driven` gap this proposal itself was raised to close. **Fix specified in §5.**

**b) Four columns on `prose_section_type` with blank `cfg_column.use` text** —
`book_order`/`book_label`/`section_order`/`section_label` — **re-confirmed live this round** (query
above: `use` is the empty string on all four). A straightforward `governance.table_columns`
violation, the same standing-standard-fix category as §12.1/§12.5's stale-catalogue finding
(`feedback_fix_standard_violations_dont_ask`). **Fix specified in §5.**

**c) `prose.book_stage_map` — what it does, and where it stands.** It is the `cfg_prose` key
`prosestore.py:book_stage_map(cfg)` reads to answer: given one of the 4 live books (Programme /
Detail design / Findings / Essays), which `prose_section_type.source_stage` values belong under it?
Concretely (`prosestore.py` lines 126–127, 433–434), `prose.extract --book <X>` and `Prose.ps1`'s
book-scoped extraction call it to (i) validate `--book` against the real list of choices, and (ii)
filter which `prose_section_type` rows (via `source_stage`) get pulled into that book's extract.
`source_stage` has **11** live distinct values, cross-tabbed against `book_label` this round:

| `source_stage` | `book_label` | count |
|---|---|---:|
| `programme` | `Programme` | 51 |
| `programme` | `Detail design` | 1 *(the D10 anomaly, §0 above)* |
| `session_a` | `Detail design` | 6 |
| `session_b` | `Detail design` | 5 |
| `session_b_phase9` | `Detail design` | 11 |
| `session_c` | `Detail design` | 12 |
| `session_d` | `Detail design` | 10 |
| `synthesis` | `Findings` | 3 |
| `verse-analysis` | `Findings` | 3 |
| `findings` | *(NULL)* | 3 |
| `essay` | `Essays` | 1 |
| `contributor` | *(NULL)* | 2 |

`contributor` and `findings` are both entirely unbooked (`book_label IS NULL`). The proposed
`prose.book_stage_map` value (§5, component IV) corrects the `findings` omission the architecture
doc and the code's own hardcoded default both had, and deliberately leaves `contributor` unbooked
(it's a staging area, not a book, per its own type descriptions — "capture once → route many"). See
§0 finding 2 / D10 for the one row where `source_stage` and `book_label` now disagree.

**d) `cfg_column`'s 3 stale `prose_section` rows — already resolved, verified live this round, not
still to build.** `cfg_column` for `prose_section` still lists `supersedes_id`, `superseded_by_id`,
and `source_file` (all three physically dropped from the live table by #836's migration) — but all
three are already `inactive=1`, not left as live-looking rows. That is the correct, established
treatment (`cfg_column.inactive`, added project-wide by escalation #833 specifically so a
config-known-dead column is a queryable fact without deleting its row — `GOVERNANCE.md` §51.2). v7
and v8 both proposed a literal `DELETE` for these three rows without re-checking `cfg_column` after
#836's migration ran; the migration itself (`prose_change_log_build_v1_20260824.py`) already applied
the correct fix. **No action needed — removed from this round's build list.**

### 1.4 The quality-flag family — pointer only

Live picture: §1.1's diagram above. Design for prose incorporation: §12. Full pre-#833 flag-family
survey (29 codes, 19,866 term-quality instances, since hard-deleted) is preserved at
`iba/docs/flag-management-current-status-v1-20260823.md`, not duplicated here.

### 1.5 Full config definitions — `prose_section` and `prose_section_type` (verified live this round)

**`prose_section`** (`cfg_table.use`, live: *"The DB-canonical store of authored prose: one row per
titled section of narrative — chapter readings, cluster essays, synthesis passages and programme
documentation — with its full body text, version lineage and approval state. Almost all of it is
machine-authored (claude_code or claude_ai); exactly one row is attributed to the researcher."*)

| # | Column | Type | `cfg_column.use` (live) | Status |
|---|---|---|---|---|
| 0 | `id` | INTEGER PK | Surrogate primary key for the prose section. | active |
| 1 | `registry_id` | INTEGER | The `word_registry` entry the section is about, where word-scoped. 86% NULL. | active — citation note pending (§5) |
| 2 | `section_type_id` | INTEGER NOT NULL | The kind of section, referencing `prose_section_type`. | active |
| 3 | `heading` | TEXT | The section's title. Not unique. | active |
| 4 | `body` | TEXT NOT NULL | The prose itself — the payload the table exists to hold. | active |
| 5 | `word_count` | INTEGER NOT NULL DEFAULT 0 | Cached length of `body` in words. Not reliably maintained (escalation #832). | active |
| 6 | `status` | TEXT NOT NULL, CHECK | Editorial state — `draft`/`in_review`/`approved`/`archived`. | active — no `cfg_enum` yet (§5) |
| 7 | `version` | INTEGER NOT NULL DEFAULT 1 | A literal pointer to `record_change_log.id` — no longer an incrementing counter (escalation #836; mixed-type legacy values resolved by the migration). | active |
| 8 | `supersedes_id` | — | The earlier `prose_section` row this replaced, pre-#836. | **inactive=1** — column dropped from live table |
| 9 | `superseded_by_id` | — | Inverse of `supersedes_id`, pre-#836. | **inactive=1** — column dropped |
| 10 | `author` | TEXT NOT NULL, CHECK | Who wrote it — `claude_ai`/`claude_code`/`researcher`. Only 1 of 949 rows is `researcher`. | active — no `cfg_enum` yet (§5) |
| 11 | `created_at` | TEXT NOT NULL | ISO-8601 UTC. Never rewritten after first insert (fixed by #836 — `session_a_replace` used to stamp it on every replace; it now touches `updated_at` instead). | active |
| 12 | `approved_at` | TEXT | 87% NULL even though most rows are `approved` — not kept in step with `status` (escalation #832). | active |
| 13 | `approved_by` | TEXT | `claude_code`, or `'manual_backfill'` for retrospective approval. | active |
| 14 | `metadata_json` | TEXT | Free-form scope/provenance JSON. | active |
| 15 | `source_file` | — | The markdown file the prose was ingested from, pre-#836. | **inactive=1** — column dropped; value now lives inside migrated `record_change_log.payload` for existing rows, `change_source` for new writes |
| 16 | `delete_flagged` | INTEGER NOT NULL DEFAULT 0 | Soft-delete marker; 59 rows flagged out. Sole live meaning of "current row" under Model A. | active |
| 17 | `cluster_code` | TEXT | The M-code cluster the section belongs to, where cluster-scoped. 175/949 populated, no FK. | active — citation note pending (§5) |
| 18 | `characteristic_id` | INTEGER | The characteristic the section discusses, where characteristic-scoped. 124/949 populated. | active — citation note pending (§5) |
| 19 | `cluster_subgroup_id` | INTEGER | Declared and indexed, 100% NULL — never used. | active — citation note pending (§5) |
| 20 | `updated_at` | TEXT | When this row was last written, touched on every write path including `session_a_replace` (escalation #836). | active |

**`prose_section_type`** (`cfg_table.use`, live: *"The controlled vocabulary of prose section
kinds — 108 codes spanning programme documentation, per-session outputs, cluster findings and
lexical prose — each with a label, the stage that produces it, and expected length bounds. It is
the only real enforcement behind `prose_section.section_type_id`, and it has grown by accretion:
over half the types belong to 'programme' rather than to any analytical stage."*)

| # | Column | Type | `cfg_column.use` (live) | Status |
|---|---|---|---|---|
| 0 | `id` | INTEGER PK | Surrogate primary key, referenced by `prose_section.section_type_id`. | active |
| 1 | `code` | TEXT NOT NULL UNIQUE | Short machine name. | active |
| 2 | `label` | TEXT NOT NULL | Human-readable name. | active |
| 3 | `source_stage` | TEXT NOT NULL | The programme stage producing this type. Uncontrolled — no CHECK. 11 live values (§1.3c). | active — no `cfg_enum` yet (§5) |
| 4 | `lifecycle_tag` | TEXT | Generation marker — `v1`/`v2`/`source`. 77% NULL; `v3` has 0 live rows. | active — no `cfg_enum` yet (§5) |
| 5 | `chapter_no` | INTEGER | For cluster-publication types, the chapter of the finished product. | active |
| 6 | `description` | TEXT | What the type is for. Missing on 32 types. | active |
| 7 | `expected_length_min` | INTEGER | Word-count guide; advisory only, NULL on 44 types. | active |
| 8 | `expected_length_max` | INTEGER | Same, upper bound. | active |
| 9 | `sort_order` | INTEGER NOT NULL DEFAULT 0 | Presentation order within a stage/chapter. | active |
| 10 | `delete_flagged` | INTEGER NOT NULL DEFAULT 0 | Soft-delete; no type retired this way, all 108 live. | active |
| 11 | `created_at` | TEXT NOT NULL | Clusters into ~20 batches, April–May 2026. | active |
| 12 | `book_order` | INTEGER | **Blank `use` — §1.3b, fix in §5.** | active, blank use |
| 13 | `book_label` | TEXT | **Blank `use` — §1.3b, fix in §5.** Uncontrolled — no CHECK. | active, blank use |
| 14 | `section_order` | INTEGER | **Blank `use` — §1.3b, fix in §5.** | active, blank use |
| 15 | `section_label` | TEXT | **Blank `use` — §1.3b, fix in §5.** | active, blank use |
| 16 | `version` | INTEGER | Pointer to `record_change_log.id` (escalation #836). `use` text already correct. | active |
| 17 | `updated_at` | TEXT | Touched on every write (escalation #836). `use` text already correct. | active |

`prose_section_dimension_link` (`prose_section_id`, `dimension_id` INTEGER no FK target,
`link_type` DEFAULT `'discusses'`, `created_at`) and `prose_section_finding_link`
(`prose_section_id`, `finding_id` REFERENCES `wa_session_b_findings(id)`, `link_type`,
`created_at`) — both 0 rows, both reproduced in full at §6 D3/D4 alongside their decisions.

---

## 2. Governance — what already regulates prose behaviour today

### 2.1 Existing rules, literal wording (full — nothing deferred)

| Setting / rule | Literal content | What it governs |
|---|---|---|
| `governance.prose_canonical_authority` (`cfg_setting`) | *"The programme prose (Workflow/Programme/programme_prose/) is the canonical authority on what the project is about — researcher, 2026-08-18. Chapters 0-3 are reviewed and final; chapters 4-6 are not yet aligned (escalation pending, part (d)). `cfg_prose_chapter` names each chapter and its status; `cfg_prose_concept` points a key project concept ... at the prose section that defines it..."* | The Programme book's own chapter-alignment status and canonicity |
| `cfg_prose_chapter` (7 rows, live) | Chapters 0–6, `title`, `status` (`reviewed` ×4 / `not_yet_aligned` ×3), `source_doc`, `description` | Which Programme chapters are settled vs. pending (chs. 4–6 tracked at escalation **#739**) |
| `cfg_prose_concept` (2 rows, live: `verse_primacy`, `inner_being_definition`) | Points a concept key at its defining prose section | Two named project concepts' canonical prose location — not a general concept registry |
| `governance.programme_stages` (`cfg_setting`) | *"The research programme has three main stages: Base_data (STEP through lexical); Analysis (deriving understanding of the inner being); Publishing (essays and output for the results)..."* | A coarse 3-stage terminology mapping — does **not** map onto the 11 live `source_stage` values (different altitude, not a conflict — §6 D9) |
| `cfg_behaviour_rule` `record-change-log-choke-point` (class=`sqlite`, built by #836) | *"Every write to a table under `record_change_log` versioning discipline (`prose_section`, `prose_section_type`) must produce a matching `record_change_log` row in the same transaction as the write itself... Applies to every operation on the covered tables..."* | Every write path — already closes the selective-coverage gap (`session_a_replace`, `prose_section_type.update`) |
| `cfg_behaviour_rule` `record-change-log-version-is-pointer` (built by #836) | *"...`version` column is not an incrementing per-item counter — it is a literal foreign key to `record_change_log.id`... Corrects the 'version = old.version + 1' text #829 sec 5 drafted before this item existed..."* | `version`'s real meaning on both tables |
| `cfg_behaviour_rule` `record-change-log-payload-is-prior-state` (built by #836) | *"`record_change_log.payload` holds what a change overwrote or removed — its prior content — never the resulting/current content... NULL for insert events and for one-time migration-baseline rows..."* | `record_change_log.payload`'s field semantics |
| `cfg_behaviour_rule` `one-time-hard-delete-exception` (built by #836) | *"A hard (physical) delete... is permitted as a one-time, explicitly-instructed migration action — first established for #833's prose-quality-table repurpose, applied again here for the 91 superseded `prose_section` rows..."* | Records the precedent behind the 91-row migration |
| `cfg_write_grant` `apply_session_patch → record_change_log` (`database='bible_research'`, built by #836) | Grants `apply_session_patch.py` write access to `record_change_log` | Only `record_change_log` — **not** `prose_section`/`prose_section_type` themselves, which stay ungranted until this build's own §5/III |
| `governance.rules_must_be_config_driven`, `governance.module.config`, `governance.table_columns`, `governance.tables` | Project-wide, quoted in full in CLAUDE.md §12/`GOVERNANCE.md` | Generic requirements this proposal exists to satisfy for prose specifically |

### 2.2 The gap, confirmed live this round (2026-08-24)

**Still genuinely zero, re-checked live this round:** the `cfg_prose` table itself; any `cfg_enum`
group for `prose_section.status`/`.author`/`prose_section_type.source_stage`/`.lifecycle_tag`/
`.book_label`; any `cfg_status_flow` row `entity='prose_section'`; any `cfg_write_grant` row
granting `apply_session_patch` write access to `prose_section`/`prose_section_type` themselves; any
`cfg_work_package`/`cfg_step` row named `prose`. This proposal's own remaining build is exactly that
list.

**No longer zero** (built by #833/#836, confirmed live): 4 `cfg_behaviour_rule` rows naming
`record_change_log`/prose discipline directly (§2.1 above); 1 `cfg_write_grant` row
(`apply_session_patch` → `record_change_log`); `cfg_column.inactive` exists project-wide and is
already correctly applied to `prose_section`'s 3 dropped columns (§1.3d).

### 2.3 New governance wording this proposal still needs to add

Two new `cfg_behaviour_rule` rows (class=`sqlite`) — the `session_a_replace` author gate and the
two-patch ordering rule (§5, component III). **A third rule, `prose-section-supersede-only-
discipline`, drafted in earlier rounds, is dropped, not built** — under Model A (#836), `body` is
updated in place on every revision, so a rule asserting "no `UPDATE` of `body`... is sanctioned"
would directly contradict the already-built `record-change-log-choke-point` +
`record-change-log-version-is-pointer` rules. Building it would leave two `cfg_behaviour_rule` rows
disagreeing about the same table's write discipline. Two new `cfg_enum` groups back `status`/
`author`. Two more back `source_stage`/`lifecycle_tag`, and one more backs `book_label`. A
`cfg_prose` module table replaces the informational-only architecture doc for tool settings.

---

## 3. Scripts and code involved

### 3.1 Operational surface — in scope, changes

| File | Current state | Change in this build |
|---|---|---|
| `iba/app/lib/prosestore.py` | `cfg_utility`, `inactive=0`, already the incorporated logic (rewritten by #836 to route all 8 `prose_section`/`prose_section_type` write ops through `_write_change_log()`) | `CHAPTER_EDIT_OUT_DIR` hardcode → `cfg.module_setting('cfg_prose', 'prose.edit_file_dir')`; `_DEFAULT_BOOK_STAGE_MAP` corrected to match §1.3c's live values. **No change needed to the write-path code itself** — #836 already rewrote it. |
| `iba/app/handlers/prose.py` | Not in `cfg_utility` (handler files are registered via `cfg_step`, matching `handlers/passage.py`'s convention) | Registered via new `cfg_work_package`/`cfg_step` rows, component II |
| `iba/app/ps/Prose.ps1` | Same convention as `Passage.ps1` | Dispatcher-wired via `cfg_step`, no separate `cfg_utility` row |
| `scripts/build_programme_prose_extract.py` | `cfg_utility`, `inactive=1`, NON-COMPLIANT (#648) | Reactivate, superseded-pointer `purpose` text |
| `scripts/export_prose_chapter_edit.py` | `cfg_utility`, `inactive=1`, INACTIVE (#729) | Reactivate, superseded-pointer `purpose` text |
| `scripts/import_prose_chapter_edit.py` | `cfg_utility`, `inactive=1`, INACTIVE (#729) | Reactivate, superseded-pointer `purpose` text |
| `scripts/search_prose.py` | `cfg_utility`, `inactive=1`, NON-COMPLIANT (#648) | Reactivate, superseded-pointer `purpose` text |

### 3.2 Dormant historical scripts touching prose — no action

9 more `cfg_utility` rows match `%prose%`, confirmed live, none part of this build:
`scripts/_apply_file_chapter_lexical_prose_v1_20260702.py`,
`scripts/_apply_file_passage_lexical_prose_v1_20260704.py`,
`scripts/_apply_file_ruthlessness_lexical_prose_20260702.py`,
`scripts/_apply_file_synthesis_prose_v1_20260703.py`,
`scripts/_apply_prose_programme_chapter01.py`,
`scripts/_export_prose_to_md_v1_20260703.py`,
`scripts/_probe_primary_span_prose_reference_v1_20260705.py`,
`scripts/build_corpus_prose.py`, `scripts/build_session_a_prose.py` — the last two belong to the old
per-word Session A/B/C pipeline; disposition tracked at #784 §9, not decided here. All `inactive=1`
per escalation #729's own "leave inactive, don't force compliance until reused" precedent.
`iba/app/migration/prose_change_log_build_v1_20260824.py` (the #836 migration itself) is now also
`inactive=1` — a one-off, already applied, not reusable.

### 3.3 `apply_session_patch.py` — write side, narrow scope

Not in `cfg_utility` (project-wide script, not prose-specific). Only its 6 `prose_section`
operations (`insert`/`supersede`/`delete`/`approve`/`session_a_replace`/`bulk_supersede`) and 2
`prose_section_type` operations (`insert`/`update`) get governance rows in this build — all 8 route
through the shared `_write_change_log()` helper built by #836. The script itself is not
rearchitected (§7).

---

## 4. Full scope — six components

**I. Read/report layer.** Code already built and tested (`extract`/`search`/`export_chapter`/
`import_chapter`). Config missing (§2.2).

**II. Dispatcher registration.** `prose` as a `cfg_work_package` + 5 `cfg_step` rows (4 read/write
ops + `prose.flag`, §12), `kind='utility'`.

**III. Write-layer governance.** `cfg_enum` for `status`/`author`; `cfg_status_flow` (4 rows);
`cfg_behaviour_rule` — 2 rows, not 3 (the drafted supersede-only-discipline rule is dropped, §2.3);
`cfg_write_grant` — 2 new rows granting `apply_session_patch` write access to `prose_section`/
`prose_section_type` themselves (`record_change_log`'s own grant already exists).

**IV. `cfg_prose`** — dedicated per-module table, 4 keys.

**V. `prose_section_type`/`prose_section` column governance.** `cfg_enum` for `source_stage`(11),
`lifecycle_tag`(4), `book_label`(4); real `use` text for the 4 blank `prose_section_type` columns
(§1.3b); citation-column `use` text for `prose_section`'s 4 citation columns (§1.3a). (The 3 stale
`prose_section` `cfg_column` rows — already correctly `inactive=1`, §1.3d — need no further action.)

**VI. Storage-integrity decisions.** §6 D3–D6 and D10 (new this round): `prose_section_finding_
link`'s FK, `prose_section_dimension_link`'s retirement, `cluster_code`'s FK, `cluster_subgroup_id`'s
disposition, and the `book_stage_map`-vs-`book_label` design tension. Each is a genuine decision,
none built without an explicit answer.

**Test plan.** §10.

---

## 5. Detailed build spec — literal payloads (full)

### IV. `cfg_prose` — new table + 4 rows

```sql
CREATE TABLE cfg_prose (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    use TEXT NOT NULL,
    inactive INTEGER NOT NULL DEFAULT 0
);
```

| key | value | use |
|---|---|---|
| `prose.chapter_names` | `{"0":"Preamble","1":"Programme purpose","2":"Research methodology","3":"Research approach","4":"Data architecture","5":"Data integrity & governance","6":"Instruction corpus"}` | Chapter-number → readable-name lookup for the extract's Markdown/Word output. Read by `prosestore.py:chapter_names(cfg)`. Fixes `build_programme_prose_extract.py`'s NON-COMPLIANT (#648) flag. |
| `prose.book_stage_map` | `{"Programme":["programme"],"Detail design":["session_a","session_b","session_b_phase9","session_c","session_d"],"Findings":["synthesis","verse-analysis","findings"],"Essays":["essay"]}` | Allowed `--book` values + `source_stage` filter set for `prose.extract`/`Prose.ps1`. `contributor` (2 types) deliberately excluded — a staging area, not a book. **Known limitation (D10, §0/§1.3c): 1 of 949 `prose_section_type` rows (`prog_purp_observations_framework`) has `source_stage='programme'` but `book_label='Detail design'` — this stage-based map will file it under "Programme," disagreeing with its own `book_label`.** Read by `prosestore.py:book_stage_map(cfg)`. |
| `prose.search_default_limit` | `100` | Default result cap for `search_prose.py`/`prose.search`. Fixes `search_prose.py`'s #648 flag. |
| `prose.edit_file_dir` | `"outputs/markdown/prose-edits"` | Directory `export_chapter` writes editable `.md` into, and `import_chapter` archives from (`{value}/archive/`) on success. Replaces the hardcoded `CHAPTER_EDIT_OUT_DIR` constant. |

### I/III — `cfg_enum` groups — `status`/`author`

| name | value | ordinal |
|---|---|---:|
| `prose_section_status` | `draft` | 0 |
| `prose_section_status` | `in_review` | 1 |
| `prose_section_status` | `approved` | 2 |
| `prose_section_status` | `archived` | 3 |
| `prose_section_author` | `claude_ai` | 0 |
| `prose_section_author` | `claude_code` | 1 |
| `prose_section_author` | `researcher` | 2 |

### V — `cfg_enum` groups — `source_stage`/`lifecycle_tag`/`book_label`

| name | value | ordinal |
|---|---|---:|
| `prose_section_type_source_stage` | `programme` | 0 |
| `prose_section_type_source_stage` | `session_a` | 1 |
| `prose_section_type_source_stage` | `session_b` | 2 |
| `prose_section_type_source_stage` | `session_b_phase9` | 3 |
| `prose_section_type_source_stage` | `session_c` | 4 |
| `prose_section_type_source_stage` | `session_d` | 5 |
| `prose_section_type_source_stage` | `synthesis` | 6 |
| `prose_section_type_source_stage` | `verse-analysis` | 7 |
| `prose_section_type_source_stage` | `findings` | 8 |
| `prose_section_type_source_stage` | `essay` | 9 |
| `prose_section_type_source_stage` | `contributor` | 10 |
| `prose_section_type_lifecycle_tag` | `source` | 0 |
| `prose_section_type_lifecycle_tag` | `v1` | 1 |
| `prose_section_type_lifecycle_tag` | `v2` | 2 |
| `prose_section_type_lifecycle_tag` | `v3` | 3 |
| `prose_section_type_book_label` | `Programme` | 0 |
| `prose_section_type_book_label` | `Detail design` | 1 |
| `prose_section_type_book_label` | `Findings` | 2 |
| `prose_section_type_book_label` | `Essays` | 3 |

(`v3` and the 5 unbooked types are enumerated as valid targets, not asserted as currently correct —
the enum documents the domain, it doesn't retroactively populate NULLs.)

### V — `cfg_column` — fill 4 blank + correct 4 citation-column texts (the 3-stale-row drop needs no action — §1.3d)

Fill (`prose_section_type`, all currently blank `use`):

| column | new `use` |
|---|---|
| `book_order` | "Display order of the 4 live books: 1=Programme, 2=Detail design, 3=Findings, 4=Essays. Paired 1:1 with `book_label`." |
| `book_label` | "Which of the 4 live books this type belongs to — see `cfg_enum` group `prose_section_type_book_label`. NULL on 5 types (`contributor` pair + the 3 unbooked `findings`-stage types, escalation #832). See D10 (§6) for the one row where this disagrees with `prose.book_stage_map`'s stage-based derivation." |
| `section_order` | "Ordering of the named sub-groupings within a book (e.g. within `Detail design`: `Session A`=1, `Session B`=2, ... `Session B Phase 9`=5, `Observation framework`=6) — a level between book and chapter." |
| `section_label` | "The named sub-grouping itself (e.g. `Session A`, `Verse analysis`, `Synthesis`, `Observation framework`) — human label for `section_order`'s position." |

Correct (`prose_section`, currently plain population-percentage text only):

| column | new `use` (replaces the current text) |
|---|---|
| `registry_id` | "The `word_registry` entry the section is about, where word-scoped. 15% populated (141/949) — most sections are chapter- or cluster-scoped rather than word-scoped. **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), not directly on `prose_section` — not acted on now, Concordance is out of scope for this build; likely to become redundant once that index table exists." |
| `cluster_code` | "The M-code cluster the section belongs to, where cluster-scoped. 18% populated (175/949), free text, no FK to `cluster` (0 live orphans, checked). **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), same reasoning as `registry_id` — not hardened with an FK now, not acted on now (§6 D5)." |
| `characteristic_id` | "The characteristic the section discusses, where characteristic-scoped. 13% populated (124/949). **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), same reasoning as `registry_id`/`cluster_code` — not acted on now." |
| `cluster_subgroup_id` | "Declared and indexed to scope a section to a cluster subgroup. 100% NULL — never used. **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), same reasoning as its siblings — not dropped now, not acted on now (§6 D6)." |

### III — `cfg_status_flow` rows, `entity='prose_section'`

| status | set_by | ordinal |
|---|---|---:|
| `draft` | `apply_session_patch.py: prose_section insert/supersede/bulk_supersede (caller-supplied, the default when omitted)` | 0 |
| `in_review` | `apply_session_patch.py: prose_section insert/supersede (caller-supplied status — no dedicated transition op exists; 0 rows currently at this status)` | 1 |
| `approved` | `apply_session_patch.py: prose_section approve (the one dedicated transition op — also stamps approved_at/approved_by)` | 2 |
| `archived` | `apply_session_patch.py: prose_section insert (caller-supplied status only — 11 existing rows were archived at insert time, not via a transition op)` | 3 |

### III — `cfg_behaviour_rule` rows, `class='sqlite'` — 2 rows (not 3)

| rule_key | rule_text | source | enforced_by |
|---|---|---|---|
| `prose-section-session-a-replace-author-gate` | "The `session_a_replace` operation updates a `prose_section` row in place. Code-gated on `author='claude_code'`; permitted only for Session A mechanical extracts, because they are reproducible from structured data rather than analytical judgement. Under Model A (#836) every write is in-place, so this is one of several in-place write paths, distinguished by its author-gate, not by being uniquely non-supersede." | `docs/prose-store-architecture.md` §5.2/§6.1; escalation #784/#829; reworded per #836 | `apply_session_patch.py`'s `UPDATE ... WHERE id=? AND author='claude_code'` clause |
| `prose-section-two-patch-ordering` | "A new prose chapter reaches the database in two ordered patches: `CATALOGUE_POPULATION` first (creates `prose_section_type` handles), then `PROSE` (content, referencing handles by `section_type_id_lookup: {code}`). Applying `PROSE` before its `CATALOGUE_POPULATION` fails at the code lookup, by design." | `docs/prose-store-architecture.md` §7; escalation #784/#829 | `apply_session_patch.py`'s `section_type_id_lookup` resolution |

**Not built:** `prose-section-supersede-only-discipline` — superseded by #836's already-built
`record-change-log-choke-point` + `record-change-log-version-is-pointer` (§2.3).

### III — `cfg_write_grant` rows, `database='bible_research'` — 2 new rows

| writer | table_name |
|---|---|
| `apply_session_patch` | `prose_section` |
| `apply_session_patch` | `prose_section_type` |

One writer identity (D1), not six per-operation identities. `apply_session_patch → record_change_log`
already exists (#836), not duplicated here.

### II — `cfg_work_package` + 5 `cfg_step` rows

`cfg_work_package`: `name='prose'`, `ps_script='iba/app/ps/Prose.ps1'`, `runs_over='none'`,
`chained=0`.

| ordinal | step | handler | kind | does |
|---|---|---|---|---|
| 0 | `prose.extract` | `iba.app.handlers.prose:extract` | utility | Programme-prose extract (JSON/MD/DOCX) |
| 1 | `prose.search` | `iba.app.handlers.prose:search` | utility | FTS/plain search over `prose_section` |
| 2 | `prose.export_chapter` | `iba.app.handlers.prose:export_chapter` | utility | Export a chapter to editable `.md` |
| 3 | `prose.import_chapter` | `iba.app.handlers.prose:import_chapter` | utility | Turn an edited `.md` into a patch file |
| 4 | `prose.flag` | `iba.app.handlers.prose:flag` | utility | Raise one `wa_data_quality_flags` instance (§12.4, angle a) — `--flag-code`, `--description` (required), no prose-section reference |

### I — reactivate the 4 original scripts (`cfg_utility`)

Same 4 rows (§3.1), same superseded-pointer `purpose` text, `inactive: 1 → 0`.

### §12.3 — `cfg_behaviour_rule` — the flag-trigger obligation

| Field | Value |
|---|---|
| `rule_key` | `prose-quality-flag-on-upstream-change` |
| `rule_text` | "When a methodology, terminology, or finding change makes existing prose content stale, the obligation is to raise a `wa_data_quality_flags` entry (`flag_group='PROSE_QUALITY'`) against the affected `prose_section` row(s) — not to stop and rewrite the prose in place. Prose gets fixed later, in its own pass; the flag is what prevents the drift from being silently lost in the meantime." |
| `source` | Researcher, 2026-08-23, escalation #829 |
| `enforced_by` | Not mechanically enforced — a discipline rule, made real and queryable via `cfg_behaviour_rule`, not automated. |

**Write grant for `prose.flag`:** `writer='prose_flag'`, `table_name='wa_data_quality_flags'`,
`database='bible_research'`.

### §12.5 — `cfg_column` recatalogue for `wa_data_quality_flags`/`wa_quality_flag_types`

Verified live this round: still correct from #833's own build (§51.2, `GOVERNANCE.md`) — no action
needed; both tables' `cfg_column` entries already match their post-repurpose schema
(`strong_id`/`verse_id`/`corrective_action`/`correction_date`/`delete_flagged`), no `file_id`/
`term_id`/`deprecated` rows remain.

---

## 6. Decisions needed — consolidated (D1–D10)

| # | Decision | Recommendation | Researcher decision | If deferred, home |
|---|---|---|---|---|
| **D1** | `cfg_write_grant`: one `apply_session_patch` writer identity vs. six per-operation identities | One writer | **Decided: per recommendation.** | n/a |
| **D2** | `prose_section_verse_link` (new table, #784 §13's verse-grounding gap) — build now or defer? | Defer — verse-linking happens at add/edit time, which is #831's territory | **Decided: deferred.** | **#831** |
| **D3** | `prose_section_finding_link`'s FK — fix now (point at live `finding`) or defer? | (originally: fix now) | **Decided: deferred** — citation-like, analytic-phase concern, not patched now. | **#832** |
| **D4** | `prose_section_dimension_link` — formally retire now, or leave dormant? | (originally: retire now) | **Decided: deferred** — same reasoning as D3. | **#832** |
| **D5** | `cluster_code` — add a real FK to `cluster(cluster_code)` (0 live orphans, confirmed) | (originally: include in this build) | **Decided: should not be on `prose_section` at all — belongs in a future index table**, same citation-column reasoning as `registry_id`/`characteristic_id`/`cluster_subgroup_id`. Not hardened with an FK now. | **#832** — eventual relocation, once index tables exist |
| **D6** | `cluster_subgroup_id` — 100% NULL, never used. Drop, leave declared-but-dead, or something else? | (originally: leave as-is) | **Decided: should not be on `prose_section` at all — belongs in a future index table**, same reasoning as D5. Not dropped now. | **#832** — eventual relocation |
| **D7** | Versioning integrity for `prose_section` and `prose_section_type` | Pull into its own escalation | **RESOLVED** — escalation #836, designed (9 rounds), proposed (3 rounds), approved, built (`GOVERNANCE.md` §52). No longer open. | n/a — built |
| **D8** | `word_count`/`approved_at` reliability (not consistently maintained) | Not fixed here — low-urgency data hygiene | **Not fixed.** | **#832** |
| **D9** | `governance.programme_stages` (3-stage abstraction) vs. `prose_section_type_source_stage` (11 concrete values) — reconcile, or keep both? | Keep both — different altitude, not a conflict | **Decided: keep both.** No change to `governance.programme_stages`. | n/a |
| **D10** *(new this round, §0/§1.3c)* | `prose.book_stage_map` (stage-list-per-book, derived) disagrees with `book_label` (direct, per-row) on 1/949 rows. Fix `prose.extract`'s book-filtering to read `book_label` directly instead of maintaining a separate derived map, or accept the 1-row known limitation and keep the stage-based design? | Read `book_label` directly — it is the more precise, already-populated column for exactly this purpose. | **Decided (researcher, 2026-08-24): deferred.** *"D10 will be edited in prose edit stage, not in this IBA processing build."* Not built. | Stage-based `book_stage_map` built as specified in §5, with the known 1-row limitation documented in its `cfg_prose.use` text (built, verified live) |

---

## 7. Explicitly out of scope — every item registered

| Item | Home |
|---|---|
| Migrating the full `wa_patch_type_registry` into `cfg_enum` | No escalation yet — project-wide, larger than any single module's build; raise when `apply_session_patch.py` as a whole comes under IBA |
| Rearchitecting `apply_session_patch.py` into an IBA dispatcher module | Same — no escalation yet |
| Widening `find_unknown_write_grant_writers` to validate `database='bible_research'` grants too | No escalation yet — small, `configmaint.validate`-mechanism-only change |
| `docs/prose-store-architecture.md` §9 stale current-state table | Superseded outright by this build (§8.1) |
| Generic `.md`-marker round-trip import tool | Already deferred by the architecture doc itself |
| Programme Prose Chapter 4 rewrite | **#786** |
| `cfg_prose_chapter` `not_yet_aligned` chapters 4–6 | **#739** |
| The prose-change-flag mechanism (design) | Closed here — §12 (angle a built, angle b designed not built) |
| Chapter-rewrite assistance (downstream of change-flag) | **#831** |
| `prose_section_verse_link` | **#831** (§6 D2) |
| Flag-mechanism project-wide normalisation (beyond prose's own use) | **#833** — built (`GOVERNANCE.md` §51) |
| The Concordance (5th book) | Still at **#784** — not yet its own escalation |
| Raw-material-visibility for writing | Still at **#784** |
| Book-2/book-3 boundary question | Still at **#784** |
| "Delete a section from an edit file" — silent no-op vs. refuse/warn/retire | Still at **#784** §6 |
| `prose_section.version`/`word_count`/`approved_at` data hygiene | **#832** (§6 D7/D8 — D7 itself resolved via #836, but the original mixed-type `version` data issue and `word_count`/`approved_at` reliability remain #832's) |
| `prose_section_finding_link`/`dimension_link` fixes, if not approved in this build | **#832** (§6 D3/D4) |
| Angle (b) of the prose quality-flag mechanism (propose/approve/apply against real flags) | **#835** (on-hold, "will become operational when prose editing comes into action") |
| `finding_revision` — an existing, unused, differently-shaped (field-level-delta) table, distinct from `record_change_log`; reconciling the two if/when `finding` is brought under change-log discipline | Not #829's scope — `GOVERNANCE.md` §52.2 names it as a future item, not yet its own escalation |
| Whatever new write-path tooling #831 builds must comply with #836's `record-change-log-choke-point` | Cross-referenced directly on #831 v3 and §1.2 above |

---

## 8. Documentation updates

**8.1 `docs/prose-store-architecture.md` — SUPERSEDED, not updated.** Once this build (§9) completes
and passes its test plan (§10), the file's content is replaced with a short superseded-pointer
banner naming the new canonical sources: `cfg_prose`/`cfg_enum`/`cfg_status_flow`/
`cfg_behaviour_rule`/`cfg_write_grant` (mechanics), `GOVERNANCE.md` §52 (versioning mechanism)
+ the new section this build adds, `cfg_table`/`cfg_column` (schema — already live, §1.5), and
`iba/app/USER-GUIDE.md` (usage, §8.4). **§3.1 (`prose_section_type`'s column table) was already
fixed live, ahead of full supersession, on 2026-08-24** — it was missing both #836's new columns and
the §1.3b columns entirely, while §3.2 (`prose_section`) had already been corrected in an earlier
round; both now match. The doc's own §11 references (design rationale, the Option-D decision
record) are historical provenance, not operative rules — they stay, cited from the new
`GOVERNANCE.md` section rather than rewritten.

**8.2 `GOVERNANCE.md`** — new section (next `§`), documenting this design and quoting the new
`cfg_behaviour_rule` rows verbatim, matching the existing pattern (§48–§52).

**8.3 `BUILD.md`** — new section, build record across all stages, gaps found/fixed named
individually, including the D3–D6/D10 decisions' actual outcomes.

**8.4 `USER-GUIDE.md`** — new "Prose module" section: the 5 dispatcher steps, the `cfg_prose`
settings, the reactivated scripts' CLI usage.

---

## 9. Sequencing (the "build per the plan" stage)

1. `cfg_prose` table creation + 4 rows (§5, component IV).
2. `cfg_column` — fill the 4 blank `prose_section_type` `use` values, correct the 4 `prose_section`
   citation-column `use` texts (§5, component V). *(The 3 stale `prose_section` rows need no action
   — already `inactive=1`, §1.3d.)*
3. `cfg_enum` — `prose_section_status`(4) + `prose_section_author`(3) +
   `prose_section_type_source_stage`(11) + `prose_section_type_lifecycle_tag`(4) +
   `prose_section_type_book_label`(4).
4. `cfg_status_flow` — 4 rows, `entity='prose_section'`.
5. `cfg_behaviour_rule` — 2 rows (`session_a_replace` gate, two-patch ordering) + 1 row
   (`prose-quality-flag-on-upstream-change`, §12.3).
6. `cfg_write_grant` — 3 rows, `database='bible_research'` (`prose_section`, `prose_section_type`,
   and `prose_flag` → `wa_data_quality_flags`; `record_change_log`'s own grant already exists).
7. `cfg_work_package` `prose` + 5 `cfg_step` rows (incl. `prose.flag`).
8. `cfg_utility` — reactivate the 4 original scripts.
9. Code: `prosestore.py`'s `CHAPTER_EDIT_OUT_DIR` hardcode → `cfg.module_setting`;
   `_DEFAULT_BOOK_STAGE_MAP` corrected. **Only if D10 resolves toward `book_label`:** filter logic
   in `book_stage_map()` changed to read `book_label` directly instead of the derived stage list.
10. **Only if D3/D4/D5 approved:** `prose_section_finding_link`'s FK rebuild;
    `prose_section_dimension_link` → `cfg_table.inactive=1`; `cluster_code` FK rebuild.
11. `docs/prose-store-architecture.md` → superseded banner (§8.1 — §3.1's fix already live, ahead of
    this step).
12. `GOVERNANCE.md`/`BUILD.md`/`USER-GUIDE.md` updates (§8.2–8.4).

---

## 10. Test plan (required up front, results go in the resolution)

| # | Function / operation | Test case | Expected |
|---|---|---|---|
| 1–6 | `prose.extract` (all 4 books + invalid book + `--book contributor`) | After `cfg_prose`/dispatcher build | Correct filtered rows per book; invalid/`contributor` rejected with the real 4-book choice list |
| 7–9 | `prose.search` | Plain + FTS + limit override | Correct hits, `search_default_limit` read from `cfg_prose` |
| 10–12 | `prose.export_chapter` / `prose.import_chapter` | Export → edit → re-import unedited (refused, not silent no-op) → edit → re-import (accepted, archived on success) | Matches file-control discipline already built under #784 |
| 13–18 | `apply_session_patch.py` — all 6 `prose_section` ops | Run each once `cfg_write_grant` is live | Each succeeds, writes a matching `record_change_log` row (choke-point rule), `version` updated to point at it |
| 19–20 | `apply_session_patch.py` — `prose_section_type` `insert`/`update` | Same | Same shape |
| 21 | Dispatcher wiring | `Prose.ps1` all 5 steps | Each resolves to its handler, `cfg_step`-driven |
| 22 | `cfg_write_grant` read | `apply_session_patch` attempts a write to `prose_section` before/after grant exists | Refused before, succeeds after |
| 23 | `cfg.module_setting('cfg_prose', 'prose.edit_file_dir')` | Read | Returns `"outputs/markdown/prose-edits"` |
| 24 | *(only if D5 approved)* insert a `prose_section` row with a `cluster_code` not present in `cluster` | FK violation, insert refused | Confirms the new constraint is real |
| 25 | *(only if D3 approved)* `prose_section_finding_link` schema | `PRAGMA foreign_key_list` | FK now references `finding`, not `wa_session_b_findings` |
| 26 | `cfg_column` query for `prose_section`'s 4 citation columns | After step 2 of §9 | All four carry the "citation column, belongs in a future index table" note, worded consistently |
| 27 | `cfg_column` query for `prose_section_type`'s 4 previously-blank columns | After step 2 of §9 | All four have real `use` text, none blank |
| 28 | `prose.extract --book Programme` | After D10 resolves | If D10 → `book_label`: type id 78 correctly excluded from Programme, included in Detail design. If D10 deferred: documented 1-row limitation stands, not a silent gap |
| 29 | `prose.flag --flag-code "Terminology change" --description "..."` | Raise a flag, angle (a) only | 1 new `wa_data_quality_flags` row, `flag_id` resolves correctly, no prose-section reference |
| 30 | `prose.flag --flag-code "Nonexistent code"` | Invalid flag code | Clean error listing the real `PROSE_QUALITY` codes, not a crash |
| 31 | `configmaint.validate` full run | After all of this build's changes | Clean — confirms no `cfg_behaviour_rule` contradiction (the dropped supersede-only-discipline row is what this specifically guards against) |

---

## 11. What I need from you

One decision structure, widened for this consolidation:

1. **Approve as written** — I submit §5's proposals in §9's order, make the code changes, resolve
   D10 per the stated recommendation (unless told otherwise), run the full test plan (§10), and
   bring results back in one resolution against #829.
2. **Or answer D10 individually**, and/or flag anything in §7's registration table that should get
   its own escalation now rather than staying parked.
3. **§0's two new findings** — no fresh decision is forced by either: finding 1 (the cfg_column
   fix already being done) needs no answer, just noting; finding 2 is D10 above.

---

## 12. Flag-table incorporation into prose

**Instruction captured, verbatim (researcher, 2026-08-23):** *"The new flag table can be introduced
into the prose management system. I imagine you need configs to set its use. important is the
connection that if methodology, terminology, and finding change for stuff that is in use in prose,
that an entry must be generated in the flag table. So I would say there must be a utility that can
be called, or at least raise the attention to rapidly add the entries in the flag table. You can
start this process by flag entries for the change of terminology for sessions. The whole principle
is that one does not need to drop and go and fix prose, but just raise the flag."*

Read as four parts: (a) wire the already-repurposed flag table into prose, config-driven; (b) the
governing principle — a methodology/terminology/finding change that touches content already written
into prose obligates a flag entry, not an immediate fix; (c) a fast-entry utility; (d) start now,
with real entries, for the Session A/B/C/D terminology change.

### 12.1 Gap found live: `wa_data_quality_flags` has no path to `prose_section`

Confirmed schema (`bible_research.db`): `strong_id`/`verse_id` are both loose, documented-only
references (SQLite can't FK across `iba.db`/`bible_research.db`). Neither identifies a
`prose_section` row, and most Programme-book prose is `registry_id IS NULL`/`metadata_json IS NULL`
— not verse- or term-scoped at all. Without a connector, a flag raised today has nothing to point
the prose author back at.

### 12.2 Schema decision: no link table, no schema change at all

Two earlier attempts (a direct column, then a `prose_section_flag_link` junction modelled on
`prose_section_finding_link`/`dimension_link`) were both retracted. The finding/dimension links are
**citation/proof-of-source relationships** — permanent, maintained-as-content. The flag mechanism is
**editorial** — a correction pointer, valid for one fix session. A flag raised now does not need a
*permanently maintained* record of which prose rows it touches; that record would go stale the
moment a new `prose_section` row uses the same superseded terminology. **Dynamic discovery at fix
time** — search `prose_section` for the pattern the flag names, when the fix pass actually runs — is
simpler and always current. `wa_data_quality_flags`/`wa_quality_flag_types` (as #833 already built
them) are already sufficient to record a flag instance: `flag_id` (type), `description` (the issue),
`corrective_action`/`correction_date` (filled in once fixed). **No schema change in this proposal.**

### 12.3 Config — the trigger obligation

Given in full at §5 above (`cfg_behaviour_rule` `prose-quality-flag-on-upstream-change`).

### 12.4 Utility — two angles

**Angle (a) — `prose.flag` — IN this build.** Given in full at §5 (`cfg_step` ordinal 4). Mirrors
the shape `Escalation.ps1 -Action Raise` already uses.

**Angle (b) — design captured, NOT built here.** A separate later run, taking an existing flag's
id/code as input: (1) **Propose** — search `prose_section` for currently-matching rows, write a
fix-proposal record (section reference, pre-fix text, machine-drafted post-fix text) — storage shape
not designed here. (2) **Approve** — researcher reviews the proposal set, approves/rejects per
instance or as a batch. (3) **Apply** — only after approval, writes the approved fixes via
`prose_section`'s ordinary write path (now `record_change_log`-choke-pointed, not the old
supersede-only mechanism this design was originally worded against). Registered as **#835**, on-hold
until prose editing comes into action.

### 12.5 Recatalogue fix — already done (§5, §12.5 note above)

### 12.6 Starting action — moved to #835

The Session A/B/C/D terminology material (the 134-row live measurement, the recommendation to raise
one flag) is #835's seed/motivating case, not part of #829's own build.

### 12.7 Prose change-history/diff — decided: not now, no escalation

A fine-grained change-log/diff mechanism (backward-looking "here's exactly what changed," distinct
from the flag's forward-looking "review this") is correctly timed to a future publishing-phase need
(an external editor), not the current drafting stage. No escalation raised.

---

## 13. §12's decisions — all resolved

1. **§12.2 (no schema, no link table, search-at-fix-time)** — agreed.
2. **§12.4's angle (b)** — agreed; escalation **#835** raised, on-hold.
3. **§12.6's starting action** — moved to #835, its first real case once built.
4. **§12.7 (change-history/diff)** — resolved as a future item, no escalation raised.

§12's own scope is now settled and small: §9's steps 5–7 (`prose.flag`, the trigger-obligation rule,
the write grant) — no schema, no data raised as part of this build.
