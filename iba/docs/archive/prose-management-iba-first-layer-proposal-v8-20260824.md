# Prose management in IBA — first layer: proposal (escalation #829) — v8

> **#829 resumed 2026-08-24.** #836 ("Prose change log design (versioning integrity)") is complete
> and built (`GOVERNANCE.md` §52) — `prose_section`/`prose_section_type` were rebuilt onto Model A
> (mutate-in-place, current-state-only) with a new project-wide `record_change_log` table. v7 brought
> this build spec up to date with #836's schema/governance changes. **v8 answers your review of v7**
> — 6 concrete points, each checked live, not assumed: (1) §1.2 — a cross-reference registered
> against **#831**, that its future write-path tooling must also comply with #836's discipline; (2)
> §1.3a — the citation-column decision was real but never actually written into `cfg_column`, only
> into this proposal's prose; the real config correction is now in §5; (3) §1.3b — reframed: not an
> open decision, a straightforward compliance fix already fully specified; (4) §1.3c — direct answer
> to what `prose.book_stage_map` does; (5) §1.3d/§1.5 — `docs/prose-store-architecture.md` §3.1 was
> missing `prose_section_type`'s own new #836 columns (and the §1.3b columns) even though §3.2
> already had them — **fixed live this round**, not deferred; (6) §1.5 — the live table genuinely
> does carry `version`/`updated_at` (verified three independent ways below), the gap was the
> documentation, not the data.

**Supersedes v7** (`prose-management-iba-first-layer-proposal-v7-20260824.md`, left on disk for
history, itself superseding v6/v5/v4/v3/v2/v1 — all kept on disk). **Stage:** still
plan/propose/design (in detail), per `cfg_behaviour_rule` class=`development`,
rule_key=`test-plan-per-module-utility` (escalation #828). Nothing in this document has been
submitted to `configmaint.propose` or built — confirmed live, this round: zero `cfg_prose` table,
zero `cfg_work_package` row named `prose`, zero `cfg_status_flow` row for `prose_section`, zero
`cfg_behaviour_rule` row named `prose-section-*` exist in `iba.db` today. **#836's own build is the
only thing that has actually landed** in this whole document's scope so far — plus, this round, one
documentation fix (`docs/prose-store-architecture.md` §3.1, made directly, not a `cfg_*` change).

**Original v6/v4 banners, unchanged, kept for continuity:** this revision's flag-incorporation
content lives at §12–§13 (closed, all four decisions resolved — see v6's own §13). #833 ("Flag
Management") is built. #831/#832/#835 remain the registered homes for everything explicitly out of
scope (§7).

---

## 0. Compliance map — every review point, and where it's answered

*(Unchanged from v6 — reproduced by reference, not repeated. New review point this round:)*

| Review point | Answered in |
|---|---|
| **v7:** bring the in-progress proposal up to date with the new `record_change_log` mechanism for version control (#836, built 2026-08-24) | §1.1/§1.2/§1.3d/§1.5 (schema — checked live), §2.1/§2.2/§2.3 (governance — #836's rules already exist), §5 III (the `supersede-only-discipline` row this proposal drafted is dropped, not duplicated — #836 already built the correct version), §6a (D7 — now resolved, not open), §9 (sequencing note), §10 (test-plan cases updated) |
| **v8 (this revision):** §1.2 — register #831's own compliance obligation | §1.2, and escalation #831 itself (context updated live, this round) |
| **v8:** §1.3a — these already have decisions; the proposal should include the actual config correction | §1.3a (reframed) + §5 (new `cfg_column.use` payloads for all 4 citation columns) |
| **v8:** §1.3b — why recorded as a "gap" at all | §1.3b (reframed — compliance fix, not a judgement call) |
| **v8:** §1.3c — what is `prose.book_stage_map` used for | §1.3c (direct answer) |
| **v8:** §1.3d — proposal documentation to be updated, config corrections included in the design | §1.3d (architecture doc fixed live this round) + §5 (config corrections, already present since v7, cross-referenced) |
| **v8:** §1.5 — the new `prose_section_type` columns aren't in "the table" | §1.5 (live verification, 3 ways) — the gap was `docs/prose-store-architecture.md` §3.1, not the DB; fixed live |

---

## 1. Storage tables in this scope, and how they relate

### 1.1 The table family and its relationships

> **Corrected again 2026-08-24 (v7), against live schema, not the v6/#836 design docs.** `prose_
> section` and `prose_section_type` are no longer supersede-chained, in-table, self-referential
> version histories — escalation #836 rebuilt both onto **Model A** (SQL-standard system-versioned
> temporal tables): each table now holds **current content only** (`supersedes_id`/
> `superseded_by_id`/`source_file` dropped from `prose_section`; nothing comparable was ever on
> `prose_section_type`), and a new, deliberately generic `record_change_log` table
> (`bible_research.db`, 1,148 rows today) holds one row per change event, keyed by `target_table`/
> `target_id` — not prose-specific, `finding` is named as a future candidate. A target row's own
> `version` column is now a **literal pointer to `record_change_log.id`**, not an incrementing
> counter and not a chain of prior rows. `prose_section` fell from 1,040 to **949** rows at migration
> (91 formerly-superseded rows hard-deleted, one-time exception, their content preserved as
> `record_change_log.payload`). Full detail: `GOVERNANCE.md` §52.

```
prose_section_type  (dictionary — 108 codes, 18 columns — version + updated_at added, #836)
      │  section_type_id (FK, required)
      ▼
prose_section  (content — 949 rows, 18 columns — current-state-only under Model A, #836)
      │
      ├──► prose_section_fts (+ 5 FTS5 shadow tables) — system-driven, full-text search index only
      │       (row count fell 1,040 → 949 automatically, sync trigger fired on the migration DELETE)
      ├──► prose_section_dimension_link  — citation-like table, 0 rows; belongs to the analytic
      │       phase of prose development (not this build — §1.2 below)
      ├──► prose_section_finding_link    — same kind, same phase, same disposition
      └──► version  ──────────────────────────────────────►  record_change_log.id  (literal FK
                                                                pointer, not a chain — #836)

record_change_log  (bible_research.db, 1,148 rows — project-wide, keyed target_table/target_id,
   NOT prose-specific by design — researcher instruction: "this is opening a big door")
   change_type (insert/change/delete) · change_datetime · change_source · change_reason ·
   changed_by · status (change_proposed/change_applied/declined — change_proposed is the
   intended home for #835's not-yet-built flag-fix workflow, per GOVERNANCE.md §52.2) ·
   payload (gzip JSON, the PRIOR content only, NULL for inserts/migration-baseline rows)

┄┄┄┄┄┄┄┄┄ NOT linked to prose_section — by design, not by omission (§12.2) ┄┄┄┄┄┄┄┄┄

wa_quality_flag_types (3 codes, 1 group        wa_session_research_flags (715 rows)
   'PROSE_QUALITY' — repurposed 2026-08-23,          — unaffected by #833/#836, has a real
   escalation #833, hard-delete confirmed)            resolved lifecycle, but targets
      │  flag_id                                      word_registry, not prose_section
      ▼
wa_data_quality_flags (0 rows today — hard-deleted
   and repurposed 2026-08-23, no data raised yet;
   strong_id/verse_id both optional, loose refs)
```

`registry_id`/`cluster_code`/`characteristic_id`/`cluster_subgroup_id` — **unaffected by #836**,
carried forward from v6 unchanged (citation-column framing, deferred to a future Concordance index
table, §6 D5/D6, home #832). Live population re-checked against the post-migration 949-row table,
this round: `cluster_code` 175/949 (18.4%, essentially unchanged from v6's 192/1,040=18.5% — most
of the 91 hard-deleted rows didn't carry it), `characteristic_id` 124/949 (identical count to v6's
124/1,040 — none of the deleted rows had it set), `cluster_subgroup_id` still 0/949 — unchanged.

### 1.2 In / out of this build's scope, per table

| Table | Rows | Columns | This build (§4/§5) | Why |
|---|---:|---:|---|---|
| `prose_section_type` | 108 | 18 *(v7: was 16 — `version`/`updated_at` added by #836)* | **IN** | `source_stage`/`lifecycle_tag`/`book_label` still need `cfg_enum` backing (unaffected by #836); 4 columns still need real `cfg_column.use` text (confirmed live, this round — still blank, §1.3b). **#836 already added correct `use` text for the 2 new columns** (`version`, `updated_at`) — nothing to do there. |
| `prose_section` | 949 *(v7: was 1,040 — 91 rows migrated out by #836)* | 18 *(v7: was 20 — `supersedes_id`/`superseded_by_id`/`source_file` dropped by #836)* | **IN** | `status`/`author` CHECK values still need `cfg_enum` backing (unaffected); write operations still need `cfg_status_flow`/`cfg_behaviour_rule`/`cfg_write_grant` — **but the specific rule this proposal (v6) drafted for supersede-only discipline is now wrong and dropped, §2.3/§5 below** — #836 already built the correct version. |
| `prose_section_fts` + 5 shadow tables | n/a (index) | 24 (unaffected) | **OUT — no action** | Unchanged from v6. |
| `prose_section_dimension_link` | 0 | 4 | **OUT of population — decision on retirement, §6 D4** | Unchanged from v6 — untouched by #836. |
| `prose_section_finding_link` | 0 | 4 | **OUT of population — decision on FK fix, §6 D3** | Unchanged from v6 — untouched by #836. |
| `record_change_log` **(v7 — new, not this build's to govern)** | 1,148 | 10 | **OUT — already fully built and governed by #836** (`cfg_table`/`cfg_column`/4 `cfg_behaviour_rule` rows/`cfg_write_grant` for `apply_session_patch`/2 `cfg_enum` groups all confirmed live, this round). Named here only so the table family picture is complete — no action item against it in this proposal. | **(v8) Cross-reference registered against #831:** the `record-change-log-choke-point` rule (§2.1) binds *every* write path to `prose_section`/`prose_section_type`, not only `apply_session_patch.py`'s existing 8 operations. #831 ("Prose add/edit operational rules layer") is the escalation that will design any *new* prose-editing tooling — its own scope now explicitly includes: whatever it builds must also write a matching `record_change_log` row in the same transaction, not bypass the choke-point by writing to `prose_section`/`prose_section_type` through a separate path. Recorded directly on #831 itself this round (context updated live), not left only in this document. |

### 1.3 Real gaps found by reading the live schema directly (not carried over from any prior doc)

**a)** Three live columns on `prose_section` not in the architecture doc — `cluster_code`/
`characteristic_id`/`cluster_subgroup_id` — unchanged from v6 (§1.1 above has current live counts).

**Reframed (v8, per your review — this is not still an open question.)** A decision already exists,
and has existed since v6: the researcher's own §1.1 framing (*"the citation columns cannot be on
`prose_section` or `prose_section_type`, they all belong in separate index tables... Ultimately these
index tables will all form part of book 5 — Concordance"*) covers all four citation columns together
— `registry_id`, `cluster_code`, `characteristic_id`, `cluster_subgroup_id` — not just the two that
got formal D-numbers (D5 `cluster_code`, D6 `cluster_subgroup_id`, §6). `registry_id` and
`characteristic_id` were never given their own D-item, but the same decision plainly applies to them
too — nothing about the reasoning is column-specific. **What was actually still missing, checked
live this round:** the decision was written into this *proposal's own prose* (§1.1/§1.5, both
rounds) but never into the *config itself* — `cfg_column.use` for all four columns, queried live
today, carries none of it (plain population-percentage text only, no citation-column note anywhere).
That is the real, still-open item: not a fresh judgement call, but a `governance.rules_must_be_
config_driven` gap this proposal itself was raised to close, sitting unfixed inside its own drafting.
**Fixed this round — literal `cfg_column.use` text for all four columns, consistently, is in §5.**

**b)** Four columns on `prose_section_type` with blank `cfg_column.use` text —
`book_order`/`book_label`/`section_order`/`section_label` — **re-confirmed live, this round,
unaffected by #836's build** (#836 touched `version`/`updated_at` only).

**Reframed (v8, per your review.)** This one was never a judgement call, and "gap" was the wrong
word for it — a blank `cfg_column.use` cell is a straightforward `governance.table_columns`
violation (*"each column... must be listed in `cfg_column` with a proper use text"*), the same
standing-standard-fix category as §12.1/§12.5's stale-catalogue finding
(`feedback_fix_standard_violations_dont_ask`: a deviation from an established standard is a bug to
fix, not a decision to ask about). Its correction has been **fully specified, with literal text, in
§5 since v6** — nothing about it was ever left open; §1.3 just filed it under "gaps found" alongside
genuinely open items (§1.3a) without distinguishing the two. Listed here only as the finding that
motivates §5's fix, not as something awaiting an answer.

**c)** `prose.book_stage_map` — **direct answer to what it's used for (v8):** it is the config
`cfg_prose` key that `prosestore.py:book_stage_map(cfg)` reads to answer one question — *given one of
the 4 live books (Programme / Detail design / Findings / Essays), which `prose_section_type.
source_stage` values belong under it?* Concretely, in code (`prosestore.py` lines 126–127,
433–434): `prose.extract --book <X>` and `Prose.ps1`'s book-scoped extraction both call it to (i)
validate the `--book` argument — an unrecognised book name is rejected with the real list of choices,
not a silent empty result — and (ii) filter which `prose_section_type` rows (via `source_stage`) get
pulled into that book's extract. E.g. `--book "Detail design"` resolves to the 5 stages
`session_a`/`session_b`/`session_b_phase9`/`session_c`/`session_d`, so only sections whose type has
one of those `source_stage` values are included. Its *value* (which stages map to which book) is
what §1.3c's original finding corrected against live data (the `findings` stage was missing) — this
answers what the *key itself* does, separate from that correction.

**d) New this round (v7) — `cfg_column` now carries 3 stale rows for columns #836 dropped.**
Checked live: `cfg_column` for `prose_section` still lists `supersedes_id`, `superseded_by_id`, and
`source_file` — all three physically removed from the table by #836's migration (§1.1). This is the
exact same class of gap this proposal already found and fixed once, for a different table pair, at
§12.1/§12.5 (`wa_data_quality_flags`/`wa_quality_flag_types` left stale after #833's rebuild) —
`governance.table_columns` requires the catalogue to match the live table, and it currently doesn't.
Proposed fix, folded into this build's existing §5 component V (already touching `cfg_column` for
this exact table): drop the 3 stale rows. Logged as a correction against **#836**, since that
build's own sequencing should have included this and didn't — same disposition as §12.1's second
finding was logged against #833, not re-litigated as a fresh judgement call here
(`feedback_fix_standard_violations_dont_ask`).

**Your review (v8): "the proposal documentation to be updated, and the config corrections for it to
be included in the design."** Two separate things, both now done: **(1) the config correction** —
already was in §5 as of v7 (the drop-3-stale-rows table), unchanged this round, cross-referenced
here so it isn't read as still pending. **(2) the documentation** — read as `docs/prose-store-
architecture.md` itself, which is a real, separate document from this proposal and was found, this
round, to have exactly the same class of staleness as `cfg_column`'s: its §3.2 (`prose_section`) was
already corrected for #836 (a prior round), but its **§3.1 (`prose_section_type`) was never touched
— missing not only the 2 new #836 columns but also the 4 §1.3b columns entirely.** Per this
project's own precedent (proposal v26/v27 fixed `docs/prose-store-architecture.md` directly, live,
mid-proposal, rather than waiting for the full build's §8.1 supersession) — this is a factual
documentation correction, not a judgement call, so **fixed live this round**, not deferred to §8.1:
both tables' column lists in the architecture doc now match. See §1.5 below for the verification.

### 1.4 The quality-flag family — pointer only

Unchanged from v6. Live picture: §1.1's diagram. Design for prose incorporation: §12.

### 1.5 Full config definitions — `prose_section` and `prose_section_type`

**v7 — both tables' column lists rewritten below against live `cfg_column` content, checked this
round** (not v6's pre-#836 dump). `governance.table_columns` is satisfied for both tables except the
4 blank `prose_section_type` rows (§1.3b, unaffected by #836, fixed in §5) and the 3 stale
`prose_section` rows (§1.3d, new this round, fixed in §5).

**Your review (v8): "the new columns for `prose_section_type` is not in the table."** Checked
directly, three independent ways, before answering — they genuinely are live columns, not a claim
taken on faith: (1) `PRAGMA table_info(prose_section_type)` lists `version` (cid 16) and `updated_at`
(cid 17); (2) the table's own `sqlite_master` DDL confirms it (`..., version INTEGER, updated_at
TEXT)` appended by the migration's `ALTER TABLE`); (3) sample data has zero NULLs on either column
across all 108 rows, and every `version` value resolves to a real `record_change_log` row with
`change_reason='migration baseline'` — 0 orphan pointers. **The gap was real, but it wasn't the
database — it was `docs/prose-store-architecture.md` §3.1**, the human-readable schema table for
`prose_section_type`, which still listed only the pre-#836 8 columns even though §3.2
(`prose_section`, right below it) had already been corrected for #836 in an earlier round. Fixed
live this round (§1.3d above) — §3.1 now lists all 18 columns, matching §3.2's own treatment.

**`prose_section`** (`cfg_table.use`, unchanged: *"The DB-canonical store of authored prose: one row
per titled section of narrative — chapter readings, cluster essays, synthesis passages and
programme documentation — with its full body text, version lineage and approval state."*)

| Column | Type | `cfg_column.use` (live, checked this round) |
|---|---|---|
| `id` | INTEGER PK | Surrogate primary key for the prose section. |
| `registry_id` | INTEGER | The `word_registry` entry the section is about, where word-scoped. 86% NULL — most sections are chapter- or cluster-scoped rather than word-scoped. Citation-column note (§1.1) carried forward unchanged. |
| `section_type_id` | INTEGER NOT NULL | The kind of section, referencing `prose_section_type`. Heavily skewed — one type (lexical prose at chapter level) accounts for roughly half of all rows. |
| `heading` | TEXT | The section's title. Not unique. |
| `body` | TEXT NOT NULL | The prose itself — the payload the table exists to hold. |
| `word_count` | INTEGER NOT NULL DEFAULT 0 | Cached length of `body` in words. Not reliably maintained (escalation #832). |
| `status` | TEXT NOT NULL, CHECK | Editorial state — `draft`/`in_review`/`approved`/`archived`. Great majority `approved`. |
| `version` | INTEGER NOT NULL DEFAULT 1 | **(v7 — corrected by #836.)** A literal pointer to `record_change_log.id` — the log row describing this section's own most recent change. No longer an incrementing counter, no longer holds mixed-type strings (the `'1_0'`/`'v1'`/`'v2'` data-quality issue escalation #832 flagged is resolved by the migration itself). |
| `author` | TEXT NOT NULL, CHECK | Who wrote it — `claude_ai`/`claude_code`/`researcher`. Only 2 of 949 rows are `researcher`. |
| `created_at` | TEXT NOT NULL | ISO-8601 UTC. **(v7 — `session_a_replace`'s old defect fixed by #836:** this column is never rewritten after a row's first insert, including by `session_a_replace` — it used to stamp `created_at=now()` on every replace, corrupting "true creation time"; it now touches `updated_at` instead.) |
| `approved_at` | TEXT | 87% NULL even though most rows are `approved` — not kept in step with `status` (escalation #832), unaffected by #836. |
| `approved_by` | TEXT | `claude_code`, or `'manual_backfill'` for retrospective approval. |
| `metadata_json` | TEXT | Free-form scope/provenance JSON — book/chapter/verse list, term, `cluster_code`, source, version. |
| `delete_flagged` | INTEGER NOT NULL DEFAULT 0 | Soft-delete marker; 59 rows flagged out. `delete_flagged=0` is now the sole live meaning of "current row" under Model A (the 3 partial indexes that referenced `superseded_by_id` were dropped and recreated against this column by #836). |
| `cluster_code` | TEXT | The M-code cluster the section belongs to, where cluster-scoped. 175/949 populated (§1.1), free text, no FK to `cluster` (§6 D5). |
| `characteristic_id` | INTEGER | The characteristic the section discusses, where characteristic-scoped. 124/949 populated. |
| `cluster_subgroup_id` | INTEGER | Declared and indexed to scope a section to a cluster subgroup. Still 100% NULL — never used (§6 D6). |
| `updated_at` | TEXT | **(v7 — new column, added by #836.)** When this row was last written, touched on every write path including `session_a_replace` — closes the staleness gap D7 originally raised (§6a). |
| ~~`supersedes_id`~~ | — | **(v7 — dropped by #836.)** No longer exists; nothing to chain once only one row per section exists under Model A. Prior-version content is preserved in `record_change_log.payload`, not as a live pointer column. `cfg_column` still lists this row — stale, fixed in §5 (§1.3d). |
| ~~`superseded_by_id`~~ | — | **(v7 — dropped by #836.)** Same disposition as `supersedes_id`. |
| ~~`source_file`~~ | — | **(v7 — dropped by #836.)** The value now lives inside migrated `record_change_log.payload` blobs for existing rows, not as a live column; new writes record it via `change_source` on the `record_change_log` row instead. `cfg_column` still lists this row — stale, fixed in §5 (§1.3d). |

**`prose_section_type`** (`cfg_table.use`, unchanged: *"The controlled vocabulary of prose section
kinds — 108 codes spanning programme documentation, per-session outputs, cluster findings and
lexical prose — each with a label, the stage that produces it, and expected length bounds. The only
real enforcement behind `prose_section.section_type_id`."*)

| Column | Type | `cfg_column.use` (live, checked this round) |
|---|---|---|
| `id` | INTEGER PK | Surrogate primary key, referenced by `prose_section.section_type_id`. |
| `code` | TEXT NOT NULL UNIQUE | Short machine name (e.g. `cluster_essay`, `lexical_prose`, `cf_char_synth`). |
| `label` | TEXT NOT NULL | Human-readable name, usually stating what it is and who it's for. |
| `source_stage` | TEXT NOT NULL | The programme stage producing this type. Uncontrolled — no CHECK constraint. 11 live values (§1.3c), not the 5 the architecture doc names. |
| `lifecycle_tag` | TEXT | Generation marker — `v1`/`v2`/`source`. 77% NULL. `v3` has 0 live rows. |
| `chapter_no` | INTEGER | For cluster-publication types, the chapter of the finished product. |
| `description` | TEXT | What the type is for. Missing on 32 types. |
| `expected_length_min`/`_max` | INTEGER | Word-count guide; advisory only, NULL on 44 types. |
| `sort_order` | INTEGER NOT NULL DEFAULT 0 | Presentation order within a stage/chapter; repeats across groups. |
| `delete_flagged` | INTEGER NOT NULL DEFAULT 0 | Soft-delete; no type retired this way, all 108 live. |
| `created_at` | TEXT NOT NULL | Clusters into ~20 batches, April–May 2026. |
| `book_order` | INTEGER | **(§1.3b — blank `use`, still unfixed, confirmed live this round. Fixed in §5.)** |
| `book_label` | TEXT | **(§1.3b — blank `use`, still unfixed.)** |
| `section_order` | INTEGER | **(§1.3b — blank `use`, still unfixed.)** |
| `section_label` | TEXT | **(§1.3b — blank `use`, still unfixed.)** |
| `version` | INTEGER | **(v7 — new column, added by #836.)** Pointer to `record_change_log.id`, same meaning as `prose_section.version`. `use` text already correct live (#836's own build wrote it) — nothing to do here. |
| `updated_at` | TEXT | **(v7 — new column, added by #836.)** Touched on every write. `created_at` reserved for true creation time only. `use` text already correct live — nothing to do here. |

`prose_section_dimension_link` and `prose_section_finding_link` — unchanged from v6, reproduced at
§6 D3/D4.

---

## 2. Governance — what already regulates prose behaviour today

### 2.1 Existing rules, literal wording

*(v6's original 5 rows — `governance.prose_canonical_authority`, `cfg_prose_chapter`,
`cfg_prose_concept`, `governance.programme_stages`, the generic project-wide rules — all unchanged,
not reproduced again. New this round:)*

| Setting / rule | Literal content | What it actually governs | What it does *not* cover |
|---|---|---|---|
| **(v7, new)** `cfg_behaviour_rule` `record-change-log-choke-point` (class=`sqlite`, built by #836) | *"Every write to a table under `record_change_log` versioning discipline (`prose_section`, `prose_section_type`) must produce a matching `record_change_log` row in the same transaction as the write itself... Applies to every operation on the covered tables..."* | Every write path to `prose_section`/`prose_section_type` — already closes the exact selective-coverage gap (`session_a_replace`, `prose_section_type.update`) v6's own §2.2 flagged as ungoverned | Doesn't touch `status`/`author` enum-backing, dispatcher registration, or `cfg_prose` settings — those are still this proposal's own scope |
| **(v7, new)** `cfg_behaviour_rule` `record-change-log-version-is-pointer` (built by #836) | *"...`version` column is not an incrementing per-item counter — it is a literal foreign key to `record_change_log.id`... Corrects the 'version = old.version + 1' text #829 sec 5 drafted before this item existed; that text is superseded by this rule, not left standing alongside it."* | The exact correction this v7 revision exists to fold in — see §2.3/§5 below | — |
| **(v7, new)** `cfg_behaviour_rule` `record-change-log-payload-is-prior-state` (built by #836) | *"`record_change_log.payload` holds what a change overwrote or removed — its prior content — never the resulting/current content..."* | `record_change_log`'s own field semantics | Not `prose_section`-specific — applies to any future table brought under this discipline |
| **(v7, new)** `cfg_behaviour_rule` `one-time-hard-delete-exception` (built by #836) | *"A hard (physical) delete... is permitted as a one-time, explicitly-instructed migration action — first established for #833's prose-quality-table repurpose, applied again here for the 91 superseded `prose_section` rows..."* | Records the precedent this proposal's own §1.1 migration numbers depend on | Doesn't pre-authorise future hard deletes generically |

### 2.2 The gap, re-confirmed live today (2026-08-24) — **corrected from v6, not still "zero"**

**v6 stated:** *"Zero `cfg_behaviour_rule`, `cfg_enum`, `cfg_status_flow`, `cfg_write_grant`,
`cfg_work_package`, or `cfg_step` row exists anywhere naming `prose_section`, `prose_section_type`,
or any `prose.*` operation."* **That is no longer fully true — #836 has since built 4
`cfg_behaviour_rule` rows (§2.1 above) and 1 `cfg_write_grant` row** (`apply_session_patch` →
`record_change_log`, `database='bible_research'` — confirmed live) that name these tables directly.
**Still genuinely zero, re-checked live this round:** any `cfg_enum` group for `prose_section.
status`/`.author`/`prose_section_type.source_stage`/`.lifecycle_tag`/`.book_label`; any
`cfg_status_flow` row `entity='prose_section'`; any `cfg_write_grant` row granting
`apply_session_patch` write access to `prose_section`/`prose_section_type` themselves (only
`record_change_log` is granted so far); any `cfg_work_package`/`cfg_step` row named `prose`; the
`cfg_prose` table itself. This proposal's own remaining scope is exactly that list — narrower than
v6 stated, not because anything was removed from scope, but because #836 has already closed part of
the same gap this proposal was raised to close.

### 2.3 New governance wording this proposal adds — **revised this round (v7)**

**v6's three `cfg_behaviour_rule` rows reduce to two, not three — the middle one is dropped, not
duplicated.** The `session_a_replace` author gate and the two-patch ordering rule both still stand,
literal wording unchanged (§5). **`prose-section-supersede-only-discipline` — the rule v6 drafted
asserting *"a revision creates a new row (`version = old.version + 1`, `supersedes_id = old.id`); no
`UPDATE` of `body`... is a sanctioned operation"* — is now factually wrong and is dropped from this
proposal's own build list entirely**, not fixed in place: under Model A, `body` **is** updated in
place on every revision (`GOVERNANCE.md` §52.5 — "`supersede` and `bulk_supersede` are genuine
rewrites: in-place `UPDATE`, not insert-a-new-row"), and the correct governing rule already exists,
built by #836 (`record-change-log-choke-point` + `record-change-log-version-is-pointer`, §2.1
above). Restating a contradicting rule here would leave two `cfg_behaviour_rule` rows disagreeing
about the same table's own write discipline — this proposal's own build must not do that. One new
`cfg_enum` group backs `status`, one backs `author` — unchanged from v6. Two *additional* new
`cfg_enum` groups back `source_stage` and `lifecycle_tag` — unchanged from v6. A `cfg_prose` module
table — unchanged from v6.

---

## 3. Scripts and code involved

*(Unchanged from v6 — §3.1/§3.2/§3.3 not reproduced. One live fact worth noting: `apply_session_
patch.py`'s 6 `prose_section` operations were themselves rewritten by #836 to route through a shared
`_write_change_log()` helper — GOVERNANCE.md §52.5. That's a code change #836 already made; nothing
in this proposal's own §3 scope needs to touch that code again.)*

---

## 4. Full scope — five components — **unchanged in shape, narrowed in III by #836**

**I. Read/report layer.** Unchanged from v6.

**II. Dispatcher registration.** Unchanged from v6.

**III. Write-layer governance.** `cfg_enum` for `status`/`author` — unchanged. `cfg_status_flow` (4
rows) — unchanged. `cfg_behaviour_rule` — **now 2 rows, not 3** (`session_a_replace` gate /
two-patch ordering — the supersede-only-discipline row is dropped, §2.3). `cfg_write_grant` — **now
needs granting `apply_session_patch` → `prose_section`/`prose_section_type` specifically** (the
`record_change_log` grant already exists, built by #836 — not duplicated here).

**IV. `cfg_prose`.** Unchanged from v6.

**V. `prose_section_type` column governance.** Unchanged in the `cfg_enum` groups (§1.3c). **`cfg_
column` fix widened again this round (v8):** fills the 4 blank `prose_section_type` rows (§1.3b),
drops the 3 stale `prose_section` rows `supersedes_id`/`superseded_by_id`/`source_file` (§1.3d), and
**now also corrects the `use` text on `prose_section`'s 4 citation columns** (`registry_id`/
`cluster_code`/`characteristic_id`/`cluster_subgroup_id`) to state the already-made "belongs in a
future index table" decision, consistently — that decision existed since v6 but had never actually
been written into the config itself (§1.3a).

**VI. Storage-integrity decisions.** Unchanged from v6 (§6 D3–D6).

**Test plan.** §10, updated this round for the new model.

---

## 5. Detailed build spec — literal payloads

*(§IV `cfg_prose`, §I/§III `status`/`author` `cfg_enum`, §V `source_stage`/`lifecycle_tag`/
`book_label` `cfg_enum`, §III `cfg_status_flow`, §II `cfg_work_package`/`cfg_step`, §I script
reactivation — all **unchanged from v6**, not reproduced again; see v6 §5 for the literal payloads.
Only the sections below actually change this round.)*

### V — `cfg_column` — **widened again this round (v8): fill 4 blank + drop 3 stale + correct 4 citation-column texts**

Fill (unchanged from v6, §1.3b):

| table | column | new `use` |
|---|---|---|
| `prose_section_type` | `book_order` | "Display order of the 4 live books: 1=Programme, 2=Detail design, 3=Findings, 4=Essays. Paired 1:1 with `book_label`." |
| `prose_section_type` | `book_label` | "Which of the 4 live books this type belongs to — see `cfg_enum` group `prose_section_type_book_label`. NULL on 5 types (`contributor` pair + the 3 unbooked `findings`-stage types, escalation #832)." |
| `prose_section_type` | `section_order` | "Ordering of the named sub-groupings within a book (e.g. within `Detail design`: `Session A`=1, `Session B`=2, ... `Session B Phase 9`=5, `Observation framework`=6) — a level between book and chapter." |
| `prose_section_type` | `section_label` | "The named sub-grouping itself (e.g. `Session A`, `Verse analysis`, `Synthesis`, `Observation framework`) — human label for `section_order`'s position." |

Drop (new in v7, §1.3d — logged as a correction against #836's own build sequencing):

| table | column | action |
|---|---|---|
| `prose_section` | `supersedes_id` | DELETE from `cfg_column` — column no longer exists on the live table |
| `prose_section` | `superseded_by_id` | DELETE from `cfg_column` — same |
| `prose_section` | `source_file` | DELETE from `cfg_column` — same |

Correct (new this round, v8, §1.3a — the decision already exists, only the config text was
missing; wording consistent across all four so none reads as a special case):

| table | column | new `use` (replaces the current plain population-percentage text) |
|---|---|---|
| `prose_section` | `registry_id` | "The `word_registry` entry the section is about, where word-scoped. 86% NULL — most sections are chapter- or cluster-scoped rather than word-scoped. **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), not directly on `prose_section` — not acted on now, Concordance is out of scope for this build; likely to become redundant once that index table exists." |
| `prose_section` | `cluster_code` | "The M-code cluster the section belongs to, where cluster-scoped. 175/949 populated (18.4%), free text, no FK to `cluster` (0 live orphans, checked). **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), same reasoning as `registry_id` — not hardened with an FK now, not acted on now (§6 D5)." |
| `prose_section` | `characteristic_id` | "The characteristic the section discusses, where characteristic-scoped. 124/949 populated. **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), same reasoning as `registry_id`/`cluster_code` — not acted on now." |
| `prose_section` | `cluster_subgroup_id` | "Declared and indexed to scope a section to a cluster subgroup. 100% NULL — never used. **Citation column (researcher, 2026-08-24):** belongs in a future index table (book 5, Concordance), same reasoning as its siblings — not dropped now, not acted on now (§6 D6)." |

### III — `cfg_behaviour_rule` rows, `class='sqlite'` — **now 2 rows, not 3 (v7)**

| rule_key | rule_text | source | enforced_by |
|---|---|---|---|
| `prose-section-session-a-replace-author-gate` | "The `session_a_replace` operation updates a `prose_section` row in place. Code-gated on `author='claude_code'`; permitted only for Session A mechanical extracts, because they are reproducible from structured data rather than analytical judgement. **(v7 — reworded:** under Model A (#836) every write is in-place, so this is no longer framed as *the one exception* to a supersede-insert discipline — it is one of several in-place write paths, distinguished by its author-gate, not by being uniquely non-supersede.)" | `docs/prose-store-architecture.md` §5.2/§6.1; escalation #784/#829; reworded per #836 | `apply_session_patch.py`'s `UPDATE ... WHERE id=? AND author='claude_code'` clause |
| `prose-section-two-patch-ordering` | "A new prose chapter reaches the database in two ordered patches: `CATALOGUE_POPULATION` first (creates `prose_section_type` handles), then `PROSE` (content, referencing handles by `section_type_id_lookup: {code}`). Applying `PROSE` before its `CATALOGUE_POPULATION` fails at the code lookup, by design." | `docs/prose-store-architecture.md` §7; escalation #784/#829 | `apply_session_patch.py`'s `section_type_id_lookup` resolution — fails loudly, not silently, if violated |

**Dropped, not built (v7):** `prose-section-supersede-only-discipline` — v6's drafted text is
factually superseded by #836's already-built `record-change-log-choke-point` +
`record-change-log-version-is-pointer` rules (§2.1/§2.3 above). Building it would create two
`cfg_behaviour_rule` rows disagreeing about the same table.

### III — `cfg_write_grant` rows, `database='bible_research'` — **unchanged content, note added (v7)**

| writer | table_name |
|---|---|
| `apply_session_patch` | `prose_section` |
| `apply_session_patch` | `prose_section_type` |

*(D1 still standing — one writer identity, not six. Note: `apply_session_patch` →
`record_change_log` is **already granted**, built by #836 — confirmed live, not duplicated here.)*

---

## 6. Decisions needed — consolidated

*(Unchanged from v6 — D1–D9 and their researcher decisions all stand, not re-litigated. D5/D6's
"belongs in a future index table" framing and D3/D4's "deferred to #832" are untouched by #836 — the
citation-column question is orthogonal to the versioning-mechanism question. Not reproduced again;
see v6 §6 for the full table.)*

### 6a. D7 — versioning integrity for `prose_section` *and* `prose_section_type` — **RESOLVED (v7)**

**v6 left this open**, with a recommendation to pull it into its own escalation. **That happened**:
escalation #836 was raised, designed (9 rounds), proposed (3 rounds), approved, and built — the
whole of D7's original concern (no `updated_at` on either table, `prose_section_type` not versioned
at all, the mixed-type `version` data, the source-file/granularity mismatch) is now answered by the
Model A + `record_change_log` design, `GOVERNANCE.md` §52. **Nothing left open here.** The one
concrete consequence for *this* document, carried through above: v6's own §5 `cfg_behaviour_rule`
draft (`version = old.version + 1`) is not marked "provisional" as v6's closing paragraph proposed —
it is **dropped outright** (§2.3/§5), because the correct rule is already built, not merely pending
verification.

---

## 7. Explicitly out of scope — every item registered

Unchanged from v6 — not reproduced again (see v6 §7). One addition:

| Item | Home |
|---|---|
| **(v7, new)** `finding_revision` — an existing, unused, differently-shaped (field-level-delta) table found live during #836's build, distinct from `record_change_log`; reconciling the two if/when `finding` is brought under change-log discipline | Not #829's scope — `GOVERNANCE.md` §52.2 names it as a future item for "whoever picks up findings-integration," not raised as its own escalation yet |

---

## 8. Documentation updates

Unchanged from v6 (§8.1–8.4) — `docs/prose-store-architecture.md`'s eventual supersession banner
should now also point at `GOVERNANCE.md` §52 for the versioning mechanism specifically, alongside
the other new sections already named there.

---

## 9. Sequencing (the "build per the plan" stage)

Unchanged ordinal structure from v6, with step 5 narrowed and step 2 widened per this round's
findings:

1. `cfg_prose` table creation + 4 rows (§5, component IV).
2. `cfg_column` — fill the 4 blank `prose_section_type` `use` values, drop the 3 stale
   `prose_section` rows, **and correct the 4 citation-column `use` texts** (§5, component V —
   *widened again, v8*).
3. `cfg_enum` — `prose_section_status`(4) + `prose_section_author`(3) + `prose_section_type_source_stage`(11) + `prose_section_type_lifecycle_tag`(4) + `prose_section_type_book_label`(4).
4. `cfg_status_flow` — 4 rows, `entity='prose_section'`.
5. `cfg_behaviour_rule` — **2 rows, not 3** (`session_a_replace` gate, two-patch ordering — *narrowed, v7*).
6. `cfg_write_grant` — 2 rows, `database='bible_research'` (`prose_section`/`prose_section_type` — `record_change_log`'s own grant is already built).
7. `cfg_work_package` `prose` + 4 `cfg_step` rows.
8. `cfg_utility` — reactivate the 4 original scripts.
9. Code: `prosestore.py`'s `CHAPTER_EDIT_OUT_DIR` hardcode → `cfg.module_setting`; `_DEFAULT_BOOK_STAGE_MAP` corrected. *(No change needed to the write-path code itself — #836 already rewrote it.)*
10. **Only if D3/D4/D5 approved:** `prose_section_finding_link`'s FK rebuild; `prose_section_dimension_link` → `cfg_table.inactive=1`; `cluster_code` FK rebuild.
11. `docs/prose-store-architecture.md` → superseded banner (§8.1, now also citing GOVERNANCE.md §52). *(§3.1's missing columns already fixed live, v8, ahead of the full supersession — see §1.3d.)*
12. GOVERNANCE.md/BUILD.md/USER-GUIDE.md updates (§8.2–8.4).

---

## 10. Test plan (required up front, results go in the resolution)

v1/v2's 28 cases (unchanged in substance, reproduced by reference — extract/search/export/import,
all 6 `apply_session_patch.py` operations, dispatcher wiring, `cfg_write_grant` read, the
`book_stage_map`/`cfg_column` cases) **plus §12's 4 flag cases (§10 v6, unchanged)** **plus, new
this round (v7):**

| # | Function / operation | Test case | Expected |
|---|---|---|---|
| 33 | `apply_session_patch.py` `prose_section` `supersede` op, once this build's `cfg_write_grant` is live | Run against a real edit | A matching `record_change_log` row is written in the same transaction (`record-change-log-choke-point`), and the updated `prose_section.version` equals that new row's `id` — confirms the built config governs a real write, not just a documented intention |
| 34 | Same, for `prose_section_type` `update` | Run a real type-metadata edit | Same shape — `record_change_log` row + `version` pointer, closing the exact selective-coverage gap #836 targeted |
| 35 | `cfg_column` query for `prose_section` | after step 2 of §9 | `supersedes_id`/`superseded_by_id`/`source_file` no longer appear; all 18 live columns catalogued, none blank |
| 36 | `configmaint.validate` full run | after all of this build's changes | Clean — confirms no `cfg_behaviour_rule` contradiction was introduced (the dropped supersede-only-discipline row, §2.3, is the thing this specifically guards against) |
| 37 | *(v8)* `cfg_column` query for `prose_section`'s 4 citation columns | after step 2 of §9 | `registry_id`/`cluster_code`/`characteristic_id`/`cluster_subgroup_id` all carry the "citation column, belongs in a future index table" note, worded consistently across all four — not just `registry_id` alone |

---

## 11. What I need from you

Same structure as v6 — unchanged. Neither v7's nor v8's own new content needs a separate decision —
v7 was a schema/governance reconciliation with #836, v8 is (a) a documentation fix already made
live and (b) writing an already-made decision (§1.3a) into the actual config, both corrections to
keep the proposal factually accurate and closed-loop, not fresh judgement calls. If you approve as
written, §9's sequence (as revised above) is what gets submitted.

---

## 12. Flag-table incorporation into prose — proposal (closes §1.4.4)

Unchanged from v6 — not reproduced again. One live cross-reference worth noting for whoever builds
**#835** (angle b, not this proposal's own scope): `record_change_log.status`'s `change_proposed`
value was **explicitly reserved** by #836's design for #835's future propose/approve/apply workflow
(`GOVERNANCE.md` §52.2) — #835's own storage-shape design (v6 §12.4, "needs its own storage shape,
not designed here") may now have a real candidate to evaluate rather than starting from nothing.
Flagged here as a pointer, not acted on — #835 remains on-hold, out of this proposal's scope.

---

## 13. §12's four decisions — all resolved

Unchanged from v6 — not reproduced again.
