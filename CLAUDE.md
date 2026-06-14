# CLAUDE.md — Claude Code Project Reference

> Compact reference loaded into every conversation. Authoritative detail lives in `Workflow/Instructions/` (the `[current]` versions per GR-REF-002). Last refresh: 2026-04-27 (folder restructure: paths updated for the new top-level layout; pre-restructure refresh was 2026-04-26).
>
> ⚠ **Orientation (2026-06-14):** this file is the entry point but is **drift-stale** on schema/architecture — live schema is **3.31.0** (not the 3.11/3.17 cited below), and the live model is finding-centric (the `finding`/`cluster`/`characteristic` tables). **Start each session at [`docs/project-orientation-core-memory-map.md`](docs/project-orientation-core-memory-map.md)**, which fans out to the current-truth reconstruction in [`outputs/markdown/project-reconstruction/`](outputs/markdown/project-reconstruction/) (files 01–04). Until this file is refreshed, that reconstruction is the corrected current state.

---

## 1. What This Project Is

A structured academic Bible research platform centred on **~214 English words** for the inner life of mankind. Each word maps to Hebrew (OT) and Greek (NT) terms via Strong's numbers, captured in a SQLite database processed by a custom Python automation engine.

**Owner:** le Roux Cilliers — sole researcher; final authority on scope and methodology.

**AI roles:**

- **Claude Code** — DB engine: patch application, JSON export, schema migrations, validation queries, programme state, Verse Context batch construction, pool dataset assembly.
- **Claude AI** — analytical: term classification, verse analysis, scope judgements, narrative production, JSON extraction, Verse Context classification.

**Governing documents:** `Workflow/Instructions/`. All operational cross-refs use `[current]` (GR-REF-002) → resolve to highest-numbered version at read time. Authoritative CC instruction: `wa-claudecode-instruction [current]`.

---

## 2. Directory Map

```text
Bible_study_projects/             ← working dir (C:\Bible_study_projects — moved off Google Drive 2026-06-03)
├── CLAUDE.md, README.md, tasks.md, .gitignore, .env
├── engine/                       ← Python automation engine (`python -m engine.engine`)
├── scripts/                      ← Utility/maintenance scripts (see §6 for prefix conventions)
│   └── analytics/                ← STEP/Zotero clients, db_client, word_export
├── database/
│   ├── bible_research.db         ← SQLite (~165 MB, NOT in Git)
│   └── file_manifest.json        ← Machine-readable file index
├── Sessions-v2/                  ← **per-cluster working tree (cluster-rework phase from 2026-06-05) — HOME for ALL new cluster output**
│   └── {CODE}-{Name}/            ← one folder per cluster (M01-Fear … M46-Abundance, FLAG, T2); see README + file-organisation-rules §3.0
├── Sessions/                     ← Session-staged inputs and outputs (now READ-ONLY cross-reference)
│   ├── Patches/                  ← JSON patches (per-session-stage); applied → archive/patches/
│   ├── Session_A/                ← STEP Extracts, terms, Word_Data, registry, Data_Prose
│   ├── Session_B/                ← 12 numbered sub-stages (01_Verse_Context_Process_input … 12_Session_B_Status)
│   ├── Session_C/                ← Session C and Session_C_Words (word studies)
│   └── Session_D/                ← Session_D_Synthesis + session_d (cluster outputs)
├── Workflow/                     ← Programme governance
│   ├── Instructions/             ← Authoritative instruction docs (wa-*-vN_M-YYYYMMDD.md)
│   ├── Global_rules/             ← wa-global-rules-all-vN, -startup-vN, extract.json
│   ├── Catalogue/                ← Observation question catalogue extracts
│   ├── reference/                ← Reference snapshots, file/label/patch patterns
│   ├── registry/                 ← Registry-management guide + overview
│   ├── schema/                   ← create_tables.sql + database-schema-v*.json
│   ├── Programme/                ← programme_prose, programme_analysis, Program_reports
│   ├── methodology/              ← Methodology session logs and design notes
│   ├── Sessionlogs/              ← Cross-stage session logs
│   └── archive/                  ← Superseded instruction-doc versions
├── outputs/                      ← Generated artefacts (docx, markdown, pdf, session-logs)
├── research/                     ← discovery/ (STEP raw output), investigations/, notes/, templates/
├── docs/                         ← file-organisation-rules.md, interaction-preferences.md, *_setup.md
├── Logs/                         ← Pre-restructure session logs (historical)
├── archive/                      ← patches/, scripts/, docs/, Sessions/, References/, Programme_prose/, Logs/
└── backups/                      ← DB snapshots (NOT in Git)
```

For exact file lookup use `python scripts/build_file_manifest.py --search "..."`.

---

## 3. The Database — Schema v3.17.0

**File:** `database/bible_research.db` (SQLite, ~165 MB, excluded from Git). Connection pattern: `sqlite3.connect('database/bible_research.db')`; set `row_factory = sqlite3.Row` for dict-like access.

### Table Groups

| Group | Tables | Purpose |
| --- | --- | --- |
| Reference | `books`, `themes`, `sources` | Static (66 books, code aliases) |
| Registry | `word_registry` | The 214-word anchor; carries `phase1_status`, `verse_context_status`, `session_b_status` |
| WA core | `wa_file_index`, `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family` | Per-term metadata; `term_owner_type` = OWNER \| XREF |
| MTI | `mti_terms`, `mti_term_flags`, `mti_term_cross_refs` | One row per Strong's; `owning_registry_fk` = canonical home |
| Verse data | `wa_verse_records`, `wa_verse_term_links` | One row per term-in-verse occurrence (~130k active) |
| Verse Context | `verse_context_group`, `verse_context` | Contextual meaning groups + per-verse classification (M18) |
| Quality flags | `wa_quality_flag_types`, `wa_data_quality_flags` | Engine-derived; v3.11.0 evidence-flag family |
| Session research | `wa_session_research_flags` | PH2_*, SB_FINDING, SB_DIMENSION, SD_POINTER |
| Cross-registry | `wa_crosslink_type`, `wa_cross_registry_links` | Semantic links between registries |
| Session B | `wa_session_b_dimensions`, `wa_session_b_findings`, `wa_finding_entity_links` | Dimensional profiles + findings |
| Session D | `session_d_runs`, `session_d_verse_links`, `session_d_term_links`, `session_d_observations` | Cross-registry synthesis |
| Observation | `wa_obs_question_catalogue`, `wa_finding_catalogue_links`, `wa_flag_type_question_link` | 194 + 12 Q-COV catalogue + flag→question routing (M31) |
| Prose store | `prose_section_type`, `prose_section`, `prose_section_fts` (FTS5), link tables | DB-canonical prose (M20) |
| Engine control | `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log` | Audit trail |
| Meaning parse | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | Structured meaning text |
| Metadata | `schema_version` | Migration history |

### Key Relationships

```text
word_registry (no = registry_id)
  └─ wa_file_index ─ wa_term_inventory ─ wa_verse_records ─ verse_context
      └─ mti_terms (owning_registry_fk → word_registry.id)
          └─ verse_context_group (mti_term_id) — group_id consumed by verse_context
```

### XREF Architecture

- One `mti_terms` row per Strong's, programme-wide.
- `wa_term_inventory.term_owner_type`: **OWNER** = canonical home (verses active, VC processed); **XREF** = cross-reference copy (verses delete_flagged; VC derived from OWNER).
- `verse_context.mti_term_id` is shared across OWNER/XREF copies.
- Scale: ~5,500 OWNER + ~1,500 XREF terms; ~133k active OWNER verses.

### Conventions

- **Strong's:** `H` Hebrew, `G` Greek; suffix letters (e.g. `H7965H`) = sub-entries.
- **Language:** `"Hebrew"` or `"Greek"` (capitalised).
- **Dates:** ISO-8601 UTC (`2026-03-19T18:08:49Z`).
- **Booleans:** INTEGER 1/0.
- **Soft deletes:** `delete_flagged = 1`; no physical deletes in automated flows.

---

## 4. The Engine

Invocation: `python -m engine.engine [options]`. Source: `engine/`. Audit pipeline runs `audit.py` (WR-01..WR-20: outcome PASS / REVIEW / STOP).

| Mode | Command | Purpose |
| --- | --- | --- |
| AUDIT_WORD | `--mode=audit_word --registry=N` | Unified pipeline: ingest Step 1 JSON, sync DB, run audit (new + existing words) |
| MIGRATE | `--migrate [--dry-run]` | Apply pending schema migrations |
| REGISTER | `--register --word="..." --source="..."` | Add new word to `word_registry` |
| REPORT | `--report --registry=N` | Word overview |
| EXPORT | `--export-word --registry=N` | Export full word JSON |
| EXPORT_REGISTRY | `--export-registry` | Export `word_registry` JSON |

NEW_WORD and GAP_FILL modes are superseded — AUDIT_WORD handles both paths.

**Common flags:** `--dry-run`, `--force`, `--interactive`, `--skip-span-backpop`, `--extract-file=PATH`.

**Constants (`engine/constants.py`):** `EXPECTED_SCHEMA_VERSION = "3.17.0"` · `LOCK_SENTINEL = "In Progress"` (title case, matches stored data) · `HIGH_FREQ_THRESHOLD = 500` · `THIN_DATA_THRESHOLD = 20` · `BACKUP_RETENTION = 10` · `STALE_LOCK_SECONDS = 7200`.

Detailed engine architecture and audit-check enumeration: `docs/Session-A-v9-Architecture-*.md`.

---

## 5. STEP API Client

`scripts/analytics/step_client.py` against local STEP server (`http://localhost:8989`). Methods: `get_vocab_info`, `get_verse_records`, `get_verse_records_with_html`, `get_strongs_for_word`, `get_related_term_cluster`, `extract_word_data`. STEP caps results at 60; client uses canonical section splits (Torah/History/Poetry/Prophets/NT, halved if needed) for full coverage. Detail: `docs/step_setup.md`.

---

## 6. Script Conventions

| Prefix | Behaviour | Safe? |
| --- | --- | --- |
| `_assess_*`, `_check_*`, `_discover_*`, `_explore_*`, `_probe_*`, `verify_*`, `inspect_*` | Read-only diagnostics | Yes |
| `_apply_*`, `_repair_*`, `_realign_*`, `_reset_*`, `_extract_*`, `_batch_extract.py` | Modify DB | **No** |
| `_delete_*` | Remove rows | **No** (destructive) |
| `_tmp_*` | Throwaway ad-hoc | Varies |
| `apply_session_patch.py` | Apply Session/VC/REPAIR JSON patches | **No** |
| `build_*`, `generate_*`, `export_*`, `_produce_*`, `_generate_*`, `word_*_extract.py`, `_exploratory_*` | Read-only reports/exports | Yes |

For full file lookup: `python scripts/build_file_manifest.py --search "..."`.

---

## 7. Word Study Pipeline

Three-phase term workflow (Phase 1 discover → Phase 2 decisions → Phase 3 DB sync): `_discover_word_terms.py` → `_apply_term_decisions.py` → `_extract_word_terms.py`. For a quick STEP pull without the full pipeline: `word_study_extract.py --word <english> [--anchors H1234,G5678]`.

---

## 8. Data Flow

```text
Phase 1 (STEP + audit_word) → Verse Context → Session B (DataPrep → pool Analysis → Extraction) → Session C → Session D
```

All Claude AI output → JSON patch → `python scripts/apply_session_patch.py` (validates and writes). **Never import raw Claude output directly.**

**Patch types:** PREANALYSIS · SESSIONB · SESSIONB-COMPLETE · ANALYSIS · VERSECONTEXT · VCGROUP · VCVERSE · SDPOINTERS · REPAIR · SESSIOND · CLUSTERING · DIMREVIEW.

**Engine export** (STEP format): `python -m engine.engine --export-word --registry=N` → `Sessions/Session_A/STEP Extracts/...`.
**Complete extract** (Session B/C format, 9 layers): `python scripts/build_complete_extract.py --registry=N` → `Sessions/Session_C/Session C/...`. Scope `full` (pre-analysis) or `final` (post-analysis); version auto-increments per day.

Detail: `wa-patch-instruction [current]` (patch ops, REPAIR catalogue, failure protocol) · `wa-versecontext-instruction [current]` (VC batch construction, R1–R4 validation, status advancement) · `wa-sessionb-analysis-readiness [current]` and `wa-sessionb-analysis-output [current]` (Session B Stage 1/2) · `wa-registry-management-guide [current]` §7a (pool IDs and pool-readiness logic) · `wa-sessiond-orientation [current]`.

---

## 9. Interaction Protocols (`docs/interaction-preferences.md`)

1. **Instruction Confirmation:** Before non-trivial tasks — summarise, state approach, WAIT for approval.
2. **Output & Workings → `.md` Always.** All outputs and workings (analysis, plans, decisions, intermediate results, reports) must be written to a `.md` file in `docs/`, `outputs/`, or a relevant subfolder. Chat is for **alerts and brief summaries only** — every substantive deliverable in chat must include a link to the `.md` file that holds the full content. Never present final output only in chat.
3. **Factual Discipline:** Work with explicit facts. Don't guess. Stop and ask if unclear.
4. **File Organisation & Versioning:** Follow `docs/file-organisation-rules.md`. **Same-name = version bump:** if a file with the same base name already exists (regardless of date), the new file must carry an incremented `-v{n}` suffix (integer, no leading zero). This applies even within the same day — a revised report produced later the same day becomes `-v2-`, the next revision `-v3-`, and so on. Archive superseded versions promptly. Never overwrite a prior version in place.
5. **Manifest Maintenance:** Run `python scripts/build_file_manifest.py` after session-log processing or batch file moves.
6. **Cost Awareness:** Cost is a real constraint. Where a task can be done more cheaply without sacrificing the outcome, advise the cheaper path **before** acting. Flag: (a) Opus on routine pipeline work; (b) whole-file reads when targeted Read/Grep would suffice; (c) subagents when a direct query is enough; (d) duplicate artefacts; (e) `--dry-run` then `--live` for routine patches; (f) ad-hoc scripts duplicating existing reports. Detail: [`outputs/markdown/cost management 20260426.md`](outputs/markdown/cost%20management%2020260426.md).

---

## 10. Document Architecture

Documents in `Workflow/Instructions/`. **All operational cross-references use the `[current]` token (GR-REF-002)** — resolve to highest-numbered version at read time. Pin specific versions only for provenance (Supersedes fields, patch metadata).

| Document | Audience | Purpose |
| --- | --- | --- |
| wa-claudecode-instruction | Claude Code | CC responsibilities: patch/directive execution, VC batch ops, extracts |
| wa-patch-instruction | Claude Code | Patch preparation + execution: ops, REPAIR catalogue, failure protocol, validation |
| wa-directive-instruction | Both | Directive specification (5 required elements, validation, execution) |
| wa-global-general-rules | Both | Programme governance (GR-REF-002, GR-FILE-003, GR-OBS-001, etc.) |
| wa-global-flags | Both | Standalone flag tracking (FLAG-010 = blocking gate) |
| wa-reference | Both | Controlled vocabulary, schema reference, file naming, validation standard |
| wa-registry-management-guide | Both | Registry structure, OWNER/XREF, dual status, clusters, pools (§7a) |
| wa-sessionb-analysis-readiness | Both | Session B Stage 1: data audit + remediation. Hard gates: VC/DimReview/B-target |
| wa-sessionb-analysis-output | Both | Session B Stage 2: 2a analysis · 2b Q&A + Type b patch · 2c analytic word output |
| wa-sessionc-instruction | Claude AI | *(superseded by cluster model — see wa-sessionc-cluster-overview)* Per-word Session C, retired 2026-05-12 |
| wa-sessionc-cluster-overview | Both | Session C cluster publication: end-to-end process, shared style, 7 chapter instructions, appendices instruction, assembler. Entry point for cluster publication |
| wa-sessiond-orientation | Both | Session D: pointer clustering, question formulation, evidence retrieval, analysis |
| wa-dimensionreview-instruction | Both | Dimension review (Phase A/B/C) |
| wa-versecontext-instruction | Both | Verse Context: batch construction, classification, validation, status advancement |
| wa-word-study-template | Claude AI | Word study output template |

### Current Programme State (2026-04-26)

- Schema **v3.11.0** (M29–M31 evidence-flag redesign applied 2026-04-20).
- 214 registries · 182 VC Complete · 2 In Progress (grace 68, suffering 214) · 30 NULL (excluded).
- All clusters C01–C22 dimension-reviewed.
- 6 registries reset to `Verse Context Reset` (2026-04-19, Q12): compassion (23), fellowship (62), forgiveness (64), grace (68), love (103), mercy (111). Prior Session B narratives retained as historical `.md`.
- 5 registries BANKED on scorecard v2 (2026-04-20): covetousness (35), fellowship (62), renewal (134), vulnerability (206), blindness spiritual (207).
- Observation Catalogue: 194 + 12 Q-COV questions (Q-COV-01..12 added 2026-04-20 for evidence-flag routing).
- Prose store operational (26 seeded section types; FTS5).
- Evidence flags (informational, never gating): `VERSE_EVIDENCE_MINIMAL` · `_CONCENTRATED` · `_HIGH` · `_BREADTH_NOTE`.
- FLAG-010: blocking gate — no new word analysis until all instructions audited against GR v2.8+.
- Open HIGH OT: OT-DBR-009 (mti_terms dedup) — designed (Action R), awaiting approval.

---

## 11. Common Operations

```bash
# Engine
python -m engine.engine --db-status
python -m engine.engine --migrate
python -m engine.engine --check-locks
python -m engine.engine --clear-lock --registry=N
python -m engine.engine --mode=audit_word --registry=N
python -m engine.engine --report --registry=N
python -m engine.engine --export-word --registry=N
python -m engine.engine --export-registry

# Patches
python scripts/apply_session_patch.py [--dry-run] <patch.json>

# Reports & extracts (read-only)
python scripts/_generate_programme_report.py
python scripts/generate_registry_overview.py
python scripts/generate_programme_snapshot.py [--registry-only|--strongs-only] [--out PATH] [--date YYYYMMDD]
python scripts/build_complete_extract.py --registry=N [--complete-only|--owner-only]
python scripts/build_correlation_extract.py
python scripts/build_dimension_extract.py --cluster|--pointers|--rootfamily C17
python scripts/_exploratory_sessionb_export_v1_20260415.py --registry=N
python scripts/export_database_schema.py

# File manifest (rebuild + search)
python scripts/build_file_manifest.py
python scripts/build_file_manifest.py --search "grace"
python scripts/build_file_manifest.py --search "registry:068"
python scripts/build_file_manifest.py --search "type:observations"

# STEP discovery (no DB writes)
python scripts/word_study_extract.py --word anger --anchors H2734

# Integrity
python scripts/_integrity_full_check.py
```

DB connection pattern for ad-hoc scripts:

```python
import sqlite3, os
conn = sqlite3.connect(os.path.join('data', 'bible_research.db'))
conn.row_factory = sqlite3.Row
```

Programme-state SQL queries (Session B progress, VC progress, OWNER terms needing VC, pool readiness, cluster progress, ownership distribution): `wa-claudecode-instruction [current]` §6.6.

---

## 12. Git

- Excluded: `database/bible_research.db`, `backups/`.
- Committed: `Sessions/Patches/*.json`.
- Commit message: `session YYYYMMDD: brief description`. Branch: `main`. Remote: `github.com/lcilliers/Bible_Projects`.

---

## 13. Environment

- Windows 11; working directory `C:\Bible_study_projects` (moved off Google Drive 2026-06-03 after a Drive sync event corrupted the DB + `.git`; see `outputs/markdown/wa-db-loss-incident-20260603.md`). Off-Drive backups to NAS `\\LSUK-SYNRACK\HomeMedia\bible_study_projects\`: (a) **DB** → `db_backups\` (daily 18:00 task `BibleResearch DB Backup to NAS`; `scripts/backup_db_to_nas.py`); (b) **full folder + memory mirror** → `mirror\` + `claude-backup\` (daily 18:30 task `BibleResearch Full Mirror to NAS`; `scripts/mirror_to_nas.ps1`, robocopy /MIR). Project memory is also committed to git under `memory/` (mirror of the `.claude` memory). Old `G:\My Drive\Bible_study_projects` retained as a fallback only.
- Python 3.14.0 · PowerShell 7+ (`$env:PYTHONUTF8="1"`).
- STEP Bible local server at `http://localhost:8989`.
- Secrets in `.env` (ZOTERO_API_KEY, ZOTERO_USER_ID, STEP_BASE_URL).

---

## 14. Controlled Vocabulary (most-referenced)

**`word_registry.session_b_status`:** NULL · `Verse Context Reset` · `Ready for Analysis` · `Pre-Analysis Complete` · `Analysis Complete` · `Session B Complete`.

**`word_registry.verse_context_status`:** NULL · `In Progress` · `Complete`.

**`wa_term_inventory.term_owner_type`:** `OWNER` | `XREF`.

**`mti_terms.status`:** `extracted` · `extracted_thin` · `extracted_theological_anchor` · `candidate_delete` · `delete` · `excluded` · NULL.

**`wa_session_research_flags.flag_code`:** `PH2_*` · `SB_FINDING` · `SB_DIMENSION` · `SB_INNER_BEING` · `SD_POINTER` · `SD_CLUSTER` · `CANDIDATE_REGISTRY_WORD` · `VOLUME_LIMITATION`.

**Evidence flags (post-M29, informational only):** `VERSE_EVIDENCE_MINIMAL` · `_CONCENTRATED` · `_HIGH` · `_BREADTH_NOTE`.

**Researcher-authored fields (pipeline must not overwrite):** `word_registry.inference_note` · `word_registry.word_synopsis`.

Full vocabulary, schema reference, evidential-status enum, dimensional-weight enum, dropped/retained-fields catalogue, full patch operation list: `wa-reference [current]` and `wa-patch-instruction [current]`.
