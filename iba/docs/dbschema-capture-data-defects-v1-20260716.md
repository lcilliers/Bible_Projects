# Data defects surfaced by the DBSchema capture — v1, 2026-07-16

> **What this is.** Describing all 110 tables / 1177 columns of `bible_research.db` from the **live data** (not the prior docs) meant profiling every column. That profiling surfaced defects across every layer. This is the by-catch, filed separately: these are findings about **the database**, not about the register.
>
> **Source:** `iba/config/DBSchema/DBSchema.json` (schema 3.40.0, captured 2026-07-16). Rebuild: `python iba/scripts/build_dbschema.py --db bible_research`.
> **Nothing here has been changed.** This is a report, not a repair.
>
> Every claim below is checkable against the profile in the register, and a sample was independently re-queried against the DB.

---

## 1. The register contradicts CLAUDE.md — CLAUDE.md is wrong

| CLAUDE.md says | The DB says |
|---|---|
| DB is ~165 MB | **766 MB** (corrected in CLAUDE.md this session) |
| `mti_terms` = one row per Strong's | **7,861 rows / 4,221 distinct Strong's.** Holds only for the 2,730 live rows; 5,131 delete-flagged rows repeat 2,567 Strong's. This is OT-DBR-009, still open. |
| 128 characteristics | **277 rows** in `characteristic` |
| `ve_nr` = 101–116 | `ve_dimension_scoreboard` runs **101–118** (adds 117 `device`, 118 `direction`) |
| `word_registry.word_synopsis` = researcher-authored, pipeline must not overwrite | **100% NULL** — never populated |

## 2. Declared type contradicts contents

- **`word_registry.phase2_datasets`** — declared `REAL`, holds 26 numeric counts *and* 4 filenames (`FrameworkB-SessionB-Registry111-Mercy-20260326.docx`). Confirmed by `typeof()`: 26 real, 4 text. Conflates a count with a file pointer.
- **`prose_section.version`** — declared `INTEGER`, holds `'1_0'`, `'2_0'`, `'v1'`, `'1_1'` mixed with integers. Not numerically comparable.
- **`wa_file_index.filename`** — 148/308 rows hold an engine **run id** (`RUN-20260318_134133-BULK_GAP_FILL` on 132 alone), not a filename.
- **`word_registry.last_automation_run`** — 193/222 rows hold the literal `'AUDITED'` instead of a timestamp. Neither status nor date.
- **`wa_meaning_parsed.strongs_number`** — declared `NOT NULL`, holds an empty string on 7,736/7,748 rows. The constraint is satisfied and meaningless.

## 3. ★ Fields that are actively misleading if read

- **`wa_meaning_parsed.language` is wrong on 31% of rows.** Reads `Hebrew` for 2,199 Greek and 187 Aramaic terms; only the 9 rows carrying a real Strong's are right. It is a hardcoded default, not a classification. `project_morph_is_source_of_truth` already says language derives from `morph_code` — but this column is a live trap for anything that reads it.
- **`ve_lexical.direction` is contaminated.** 68,568 rows hold `1to2`; ~300 distinct values are truncated prose spilled into the field (`'static — 29:22).'`, `'toward-god — the whole heart's cry for answer.'`).
- **`ve_lexical.from_span` / `to_span` are not usable as span references.** Only 5,851/74,419 `from_span` and 16,047/95,881 `to_span` are numeric; the rest are lemmas, English words, or Strong's numbers.
- **`lexicon.occurrence_count` is capped, not counted.** Five entries sit at exactly 10000 (a STEP ceiling). Any frequency arithmetic over the high-frequency tail is wrong.
- **`finding_citation` is misnamed** — its CHECK binds `source_table` to `cluster_finding`/`cluster_observation`. It does not cite `finding` at all.
- **`wa_verse_term_links.verse_id` points at `wa_verse_records.id`, not `verse.id`.** A naming hazard that will silently mis-join.
- **`reread_worklist.committed_sha`** — 111/150 rows hold `'batch'` (78) or `'bankd'` (33, a typo) instead of a commit hash. Unusable as a commit reference.

## 4. Half-finished migrations

- **`mti_terms.owning_registry_fk`** — 3,522 rows carry an `owning_registry` **text** value with no matching FK. The legacy text column is *better* populated (8 nulls) than the typed FK (3,525 nulls). Ownership queries via the FK silently lose 45% of the table.
- **`ib_characteristic`** — 7 columns 100% NULL (`aka`, `books`, `gist`, `colour_range`, `junctions`, `open_questions`, `discovery_doc`). That material **is** fully authored in `ib_characteristic_legacy` (29 rows): the rebuild dropped the hand-authored layer. `char_key` is **not unique** (1,455 distinct / 1,634). `cluster` NULL on 1,009 (62% unmapped).
- **`ve_lexical.verse_context_id` is 74% NULL** (461,208/620,151) — the FK survives only on carried-over rows; `verse_span_id` is the live anchor.
- **`wa_verse_records.verse_id` NULL on ~7%** — and `verse_evidence_orphan` records exactly these (all 222 rows). A concrete, fixable gap.
- **`registry_id` formatting differs across tables** — `word_run_state` zero-pads (`'001'`), `wa_file_index` does not. They will not join without normalisation.

## 5. Declared and never used

**Empty tables (0 rows):** `sources`, `themes`, `finding_revision`, `prose_section_dimension_link`, `prose_section_finding_link` (its FK points at legacy `wa_session_b_findings` — superseded before use), and all four `session_d_*`.

**100% NULL columns:** `verse_context.sense_id` / `sense_multiplicity` / `step_envelope_note` / `pole` (the whole pole/sense model, declared across 55,775 rows, never used); `ve_lexical.related_tier` (620,151 rows); `wa_session_b_findings.term_id` (**no finding there is bound to a term** — none is reachable via the term model); `wa_verse_records.claude_output`; `finding.justified_by_finding_id`; `word_registry.word_synopsis`; `wa_term_inventory.term_introduction_source`/`_rationale`/`_date`; `wa_meaning_sense.stem_label`/`domain_tag`; `wa_lsj_parsed.lsj_cognate_forms`; and others (see the register).

**Redundant:** `word_registry.no` ≡ `id` on all 222 rows; `books.book_order` ≡ `id` on all 66; `word_registry.carry_forward` = 1 on every populated row.

## 6. Frozen snapshots that silently under-cover the canon

`verse_coverage` and `verse_morph_complexity` each carry one identical `built_at` (2026-06-27) and stop at `verse_id` 23593, while `verse` holds **25,634 — 2,041 verses are invisible to both**. `verse_term_index` shares the ceiling. And `verse_coverage.scope_basis` carries a self-declared health warning on all 23,593 rows: *"debunked anchor; recomputable"*.

`verse_span_index` is a materialised copy of `verse_morphology` (`source='verse_morphology'` on every row) but sits **33 rows short** of its source — already drifted.

## 7. Vocabulary drift (values are convention, not control)

The profiler flags `UNCONTROLLED-VOCAB` where a small repeating value-set has **no CHECK and no FK** behind it. Only **6 CHECK constraints exist in the entire 110-table database**. Consequences visible in the data:

- `cluster_subgroup.status`: both `active` (142) and `Active` (16)
- `lemma_faculty_map.confidence`: `med` (366) **and** `medium` (234)
- `cluster_observation.target_phase`: `session_d`, `Session_D`, bare `D`
- `wa_session_research_flags.session_target`: three targets spelled seven ways; `priority` mixes two scales
- `finding.finding_status`: 14 lowercase `'active'` against otherwise-uppercase
- `finding_verse_link.role`: `'anchor'` vs `'SUPPORT'`
- `wa_term_inventory.testament`: `NT` vs `NT_only`
- `wa_finding_catalogue_links.pattern_type`: `'New finding'` **and** `'*New finding*'` — markdown leaked into data
- `word_registry.cluster_assignment`: `DEFAULT "unassigned"` — a **double-quoted** literal; SQLite accepts it as a string only by falling back from identifier parsing
- Version columns mix incompatible schemes and are not sortable: `cluster_finding.version` (`v1` / `v2-20260511` / `v2.1-2026-05-13`), `characteristic.version` (`v1` / `v1.0` / `v2.0`)
- Timestamps use at least three forms: ISO-8601 Z, SQLite `datetime('now')` space-separated (`ib_observation.created`), and `20260711T202140Z` (`ib_characteristic.created_at`)

## 8. Provenance / approval trails that do not hold

- **`word_run_state`** — approval never operated: `researcher_approved`=0 on all 539, `approved_at` 100% NULL, `approved_by` only ever `'PROVISIONAL'`. Only **8 of 539** runs returned PASS (491 REVIEW): REVIEW is the norm, not the exception.
- **`prose_section`** — 922 rows `approved`, but `approved_at` 87% NULL and 14 approvals attributed to `'manual_backfill'`.
- **`wa_finding_catalogue_links`** — `validated_date` == `mapped_date` on 6,055/6,199; `validated_by` is NULL on exactly the 488 rows marked `'validated'` — the inverse of what the name implies.
- **`wa_addendum_registry`** — all 22 rows `obsolete=1` (so the default of 0 describes a state that never occurs) yet all 22 still `migration_status='pending'`. The table contradicts itself.
- **`wa_obs_question_catalogue`** — `deleted=1` on 243 rows but `status` marks only 185 non-active. Two disagreeing lifecycle markers; neither is trustworthy alone.
- **`cluster.status`** — 2/49 rows hold free-text history (`'Merged into M10 (2026-06-23)'`) in place of a status. The column mixes state and history.
- **`cluster_finding.source_file`** — 911 rows hold the literal `'[stub-loader-step1]'`.
- **`cluster_finding.finding_type`** — declared, 100% NULL across 19,997 rows.

## 9. The lexical layer — evidence on the known failure

- **`ve_dimension_scoreboard`: no dimension carries a PASS.** 8 FAILED, 10 IN-PROGRESS, from one 2026-07-14 snapshot over samples of 4–12 instances. This is the record of `project_lexical_rule_validation_failed_build_headless_app`, in the DB.
- **`ve_lexical_verification` does not check what it samples.** Covers only ve_nr 101, only in Psalms, and **only 13 of its 46 rows come from `ve_verification_sample`** — the check is not drawn from its own sampling frame. Of 5 `wrong` verdicts only 1 records a `correct_value`; all 5 came from the *fullest* source set. The notes diagnose one recurring failure: **the stored sense states an inferred inner state, or the verse's effect, rather than what the word means.**
- **`finding` is ~92% soft-deleted** — 438,099 rows, of which all `l2_api` (186,455), all `l2_mechanical` (145,720) and 70,947 `l2_meaning` are `delete_flagged=1`. ~35k live. Consistent with the reset, but the table is mostly retained substrate.
- **`finding_question_link.coverage` is not an independent judgement** — `'direct'` maps exactly 1:1 onto the 186,455 `l2_api` findings and `'full'` exactly onto the 145,720 `l2_mechanical`. It restates provenance. It reaches **31 of 424** catalogue questions, against 375 in its legacy predecessor `wa_finding_catalogue_links`.
- **`wa_dimension_index`** — 1,542/3,509 entries rest on `KEYWORD_WEAK`; 244 are `UNCLASSIFIED`. `wa_dim_review_cluster_log` closed only 6 of 22 C-codes, **each under a different instruction version**.
- **`wa_term_phase2_flags`** — 1,092/1,570 are `bulk_patch` with no per-term justification. Its single retracted row documents the failure mode exactly: a `SEMANTIC_RANGE_BREADTH` flag asserting 4+ semantic domains, withdrawn because the term's actual 17-verse corpus did not support it. **That is one flag checked against verse evidence out of ~1,092 asserted.**
- **`wa_term_root_family`** — 2,188/2,234 backfilled by clustering `wa_term_related_words`. Root families derive from STEP's related-word data, not etymology.
- **`wa_lsj_parsed` has misfired, not merely stalled** — 9 rows against 2,221 terms holding an `lsj_entry`. `lsj_domains` holds `["Refs"]` on 5 of 7 populated rows (the lexicon's own citation marker parsed as a domain); `lsj_philosophical_note` holds the fragment `Plut`; `lsj_gloss` is a truncation of `raw_lsj` with citation apparatus intact. If resumed, the parser needs rewriting, not extending.

## 10. The 2026-06-26 backup tables — resolved from the data

Cross-joining each dated backup's ids against `ve_lexical` and `ve_lexical_legacy` resolved every one:

- All nine resolve **100% into `ve_lexical_legacy`, 0% into `ve_lexical`** — except **`ve_lexical_faculty_backup`, whose rows are gone from both** (2 of 29,031 survive). It is the **only surviving copy** of the pre-rebuild engine faculty derivation.
- **Quarantine / reverse / pre_reset** tables: every legacy counterpart is now `delete_flagged=1`. They preserve withdrawn output.
- **premap** tables preserve values overwritten in place, and the diff is exact: divinv roles `object/agent/possessor/addressee/giver` → **`present`**; objtype `thing/abstract`, `abstract`, `thing` → **`impersonal`**. **These two tables are the sole surviving record of those distinctions.**

---

## What I would do next (recommendation, not a decision)

1. **Nothing here is repaired.** Read it before the new IBA DB is designed — §5 (declared-never-used) and §6 (frozen snapshots) are directly the migration-disposition question, and §10 says which backups are load-bearing.
2. **Three findings are urgent if anything still reads them:** `wa_meaning_parsed.language` (wrong on 31%), `lexicon.occurrence_count` (capped), and `mti_terms.owning_registry_fk` (loses 45% on join).
3. **§7 is the argument for the new DB's constraint layer.** 6 CHECK constraints across 110 tables is why every one of those vocabularies drifted. In IBA terms, each is a config rule that was never projected into the schema (`_manifest.json` `meta.envelope.validation.enforcement`).
4. **§9 is the lexical failure, evidenced in data** rather than asserted — useful input to the headless validator in `project_lexical_rule_validation_failed_build_headless_app`.
