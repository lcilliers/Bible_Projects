# Reference Migration M33–M35 — Close Record + Doc Sweep — 2026-04-20

| Field | Value |
|---|---|
| Migrations | M33 (rules), M34 (programme prose types), M35 (patch types + file patterns + label patterns) |
| Schema version | 3.12.0 → 3.13.0 |
| Framework | `research/investigations/reference-as-database-framework-execution-20260420.md` |
| Status | All three migrations CLOSED — reference-as-DB framework fully operational |
| Produced | 2026-04-20 |

---

## 1. Outcome — full migration chain

The reference-as-DB 3-layer architecture is now live end-to-end:

| Layer | Storage | Post-M35 state |
|---|---|---|
| **L1 Taxonomic** | DB | ✅ 5 vocabularies + 36 active rules + 22 addenda + 15 patch types + 23 file patterns + 11 label patterns |
| **L2 Narrative** | Prose store (`source_stage='programme'`) | ✅ 8 section types seeded; content population (via PROSE patches) pending |
| **L3 Process** | Instruction documents | ✅ Unchanged (still markdown); now point at DB as canonical for L1 content |

## 2. What each migration delivered

### M33 — Global rules + addenda

- `wa_rule_registry` + `wa_addendum_registry` tables + 2 indexes
- 59 rules seeded from `wa-global-general-rules-v2_11-20260418.json` (36 active + 23 obsolete/superseded)
- 22 addenda across 3 groups (`addendum_instructions` 10, `addendum_patch_directive` 9, `addendum_reference` 3)
- `wa-global-general-rules-v2_11-20260418.json` annotated with `canonical_source` pointer → DB

### M34 — Programme prose section types

8 section types seeded with `source_stage = 'programme'`:

| Code | Label |
|---|---|
| `prog_anchor_verse` | Programme — Anchor Verse Definition |
| `prog_xref_architecture` | Programme — XREF Architecture |
| `prog_validation_standard` | Programme — Document Validation Standard |
| `prog_delete_discipline` | Programme — Soft-Delete Discipline |
| `prog_field_authority` | Programme — Field Authority Rules |
| `prog_backup_discipline` | Programme — Backup Discipline |
| `prog_patch_failure_protocol` | Programme — Patch Failure / REPAIR Protocol |
| `prog_instruction_override_protocol` | Programme — Instruction Override Protocol |

Content is empty — researcher + AI author via PROSE patches (L2 content migration is the separate follow-on step).

### M35 — Patch types + file patterns + label patterns

- `wa_patch_type_registry` — 15 patch types seeded
- `wa_file_name_pattern` — 23 patterns (word-level, VCB, programme, instruction, patch ID/filename, dim review family, Session A, SD pointers, final extract, reference snapshot)
- `wa_label_pattern` — 11 patterns (DIM finding/pointer, PH2, legacy formats, group code, VCB, Q-COV, directive, patch, flag)
- Schema version bumped to 3.13.0

## 3. Snapshot — post-migration state

`scripts/build_reference_snapshot.py --also-markdown` produces:

- `Workflow/reference/wa-reference-snapshot-20260420.json` — full L1 + L2 index + schema
- `Workflow/reference/wa-reference-snapshot-20260420.md` — human-readable view

Snapshot now carries:

| Section | Entries |
|---|---:|
| `vocabularies` | 5 sets, 27 members |
| `schema` | 61 tables (live) |
| `rules` | 36 active rules + 22 addenda |
| `patch_types` | 15 |
| `file_name_patterns` | 23 |
| `label_patterns` | 11 |
| `programme_prose_index` | 8 section types (content population pending) |

## 4. Document sweep performed

Consolidated sweep across docs that **declare** L1 content (vs docs that use values in narrative):

| Document | Section | Change |
|---|---|---|
| `wa-reference-v5_7-20260420.md` | §1 File Naming Conventions | Added canonical-source pointer → `wa_file_name_pattern` |
| `wa-reference-v5_7-20260420.md` | §5.4 flag_label convention | Added canonical-source pointer → `wa_label_pattern` + listed additional patterns in DB |
| `wa-reference-v5_7-20260420.md` | §12 Patch Index | Added canonical-source pointer → `wa_patch_type_registry` |
| `wa-reference-v5_7-20260420.md` | §4.3 dimensions | Already done in M32 sweep (points at `wa_vocab_set.DIMENSION_LABEL`) |
| `wa-reference-v5_7-20260420.md` | §10 evidential_status | Inline vocabulary retained (M32-era repurposing — already DB-mirrored in §9.4 methodology note) |
| `wa-dimensionreview-instruction-v3_3-20260418.md` | §7.7 dimension vocabulary | Already done in M32 sweep |
| `wa-global-general-rules-v2_11-20260418.json` | `document` block | Added `canonical_source` + `m33_note` fields pointing at DB |
| Other Session_B docs (rules referenced by ID, patch types used in narrative, file patterns cited) | various | Left as narrative USE per sweep protocol — declarations moved, pointers within docs refer to rule IDs / type codes (these are stable identifiers; DB lookup resolves current state) |

Sweep protocol: only DECLARATIONS of reference content (authoritative lists, enumerations, catalogues) are redirected to DB. Narrative USE of values (e.g. "when dominant_subject is HUMAN, proceed with...") remains intact — those are process instructions, not reference declarations.

## 5. Validator + extractor state

`scripts/apply_session_patch.py`:

- `_load_vocab_set(conn, set_code)` — generic DB-sourced vocabulary loader
- `_canonical_dimensions(conn)` — DB-first; hardcoded fallback retained for safety
- Validator sites rewired: `wa_dimension_index.dimension` + `wa_dimension_index.dominant_subject` (M32 scope)
- Other vocabularies (QA flags, MANUAL_OVERRIDE, DIMENSION_CONFIDENCE, patch types, rules) available via `_load_vocab_set`; validator coverage can be extended as specific validator checks are added

`scripts/build_reference_snapshot.py`:

- Loads all 7 reference slices from DB (vocabularies, schema, rules+addenda, patch types, file patterns, label patterns, programme prose index)
- Emits JSON + optional MD view
- Regenerate at session start per the new `GR-LOAD-001`-equivalent step (AI session protocol)

## 6. Backups produced

- `bible_research_pre_M33_{ts}.db`
- `bible_research_pre_M34_{ts}.db`
- `bible_research_pre_M35_{ts}.db`

All retained 6+ months per backup discipline.

## 7. Remaining follow-ons

| Item | Scope | Owner |
|---|---|---|
| **Populate L2 programme prose** — 8 section types seeded empty; content (anchor verse definition, XREF architecture, validation standard, etc.) to be migrated from `wa-reference` + `wa-global-general-rules` via PROSE patches | Researcher + Claude AI draft prose; CC applies patches | After M32-M35 settle |
| **Deprecate `wa-reference` document** — once L2 prose is populated, the reference document becomes auto-generatable (markdown view already emitted by snapshot extractor). Document then marked superseded | CC | After L2 content migration |
| **Extend validator coverage** — currently DB-sourced for dimension + dominant_subject. Extend to QA_FLAG, MANUAL_OVERRIDE, DIMENSION_CONFIDENCE, patch types, label patterns as specific validation checks are added | CC | Incremental |
| **Session-start protocol update** — GR-LOAD-001 (or equivalent) should reference `wa-reference-snapshot-{YYYYMMDD}.json` as the canonical session-start reference load, rather than the markdown doc | Researcher direction needed | Next GR revision |

## 8. Cycle close

M33 + M34 + M35 CLOSED 2026-04-20. Schema at 3.13.0. Reference-as-DB 3-layer architecture fully operational.

Researcher can:

- Start populating L2 programme prose (PROSE patches for the 8 seeded section types) OR
- Tackle other programme work (C01 resubmission, Flags register review, FLAG-016 orphan audit, etc.)

---

*End of M33–M35 close record — 2026-04-20.*
