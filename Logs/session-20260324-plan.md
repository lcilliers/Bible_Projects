# Session Plan — 24 March 2026

## Pending Request: README pointer + memory playback

### What I understood
1. Create a workspace copy of the interaction preferences (`docs/interaction-preferences.md`) so it exists as a real, editable workspace file.
2. Add a pointer to it in `README.md`.
3. Read back all memory (interaction preferences + repo memory).

### Proposed approach
- **Create** `docs/interaction-preferences.md` — copied from current `/memories/interaction-preferences.md` content (Option A: workspace file, version-controlled, editable by researcher).
- **Update** `README.md` — add a section or reference in Section 2 (Participants and Roles) or Section 12 (Project Rules) pointing to `docs/interaction-preferences.md`.
- **Write** full memory playback to this file (see below).

**Awaiting explicit approval before making any changes.**

---

## Memory Playback — Current state

### `/memories/interaction-preferences.md`

#### Instruction Confirmation Protocol
Before executing ANY user instruction (except trivial single-step tasks):
1. Summarise the instruction as understood
2. State what I plan to do (approach, files affected, scope)
3. WAIT for explicit user approval before proceeding

Applies every new chat session, without exception.

#### Output & Workings Stream Protocol
All workings (reasoning, plans, steps) and all outputs must be streamed to `.md` files.
- Never present final output only in chat — always write it to a `.md` file first
- Workings (analysis steps, decisions made, intermediate results) also captured in `.md` format
- Files placed in a logical workspace location (`docs/`, `outputs/`, or relevant subfolder)
- User may edit these files to correct or contribute; those edits must be respected in subsequent steps

#### Factual Discipline Protocol
- Work only with facts and inputs explicitly provided
- Do not invent context, fill in gaps with assumptions, or speculate without being asked
- Opinions and recommendations only when explicitly requested
- If anything is unclear or information is missing — STOP and ask before proceeding

---

### `/memories/repo/engine-bugs-and-fixes.md` — UPDATED 2026-03-24

#### Infrastructure Notes

**SQLite on Google Drive — WAL mode unsafe**
Google Drive does not provide reliable file-locking for SQLite WAL mode. Large WAL transactions appear to succeed but produce a corrupted database unreadable by the next connection.
- Mitigation (2026-03-22): Database switched to DELETE journal mode before all repair scripts. All future scripts must verify DELETE mode before operating.
- Planned resolution: Migrate project folder to NAS after Fix 8b is complete. Google Drive then serves as backup only.

**Schema version (current):** v3.3.0 (M12 applied 2026-03-23, uncommitted)
- M12 adds: `delete_flagged INTEGER DEFAULT 0` on `wa_term_inventory`, `wa_verse_records`, `wa_term_related_words`, `wa_term_root_family`
- M12 adds: `wa_verse_term_links` junction table (verse × term span data; UNIQUE on verse_id+term_inv_id)
- Previous: v3.2.0 (M11 FK alignment, 2026-03-22)

**Fix 8a/8b status:** Parked — to be done alongside verse-related work in a future session.
- 53 orphan flags confirmed: 44 NOT_IN_DB, 6 NO_STRONG, 3 RELATED_SUFFIX, 0 WRONG_FILE
- `docs/orphan_flags_audit.csv` is the researcher input file for Fix 8b

#### Session 2026-03-23: Major Engine Redesign (uncommitted)

**1. New pipeline — `scripts/word_study_extract.py`**
Single script replaces three former scripts (`_discover_word_terms.py`, `_apply_term_decisions.py`, `_extract_word_terms.py`). Command: `python scripts/word_study_extract.py --word soul [--dry-run]`
- Runs six phases: DISCOVER → TRIAGE → DECIDE → FETCH → FILTER → EXPORT
- Auto-includes any codes from `mti_terms WHERE owning_registry=?` that are absent from the STEP cluster (e.g. H4578, H5397 for soul)
- G2r terms (root unverified) are INCLUDED with a `NOTE_ON_ROOT_FAMILY` quality flag (not excluded)
- Output: `data/discovery/{reg_no:03d}_{word}_step_data_{YYYYMMDD}.json`

**2. AUDIT_WORD v2 — complete redesign (`engine/audit_word.py`)**
- Old flow (A1–A10): Called STEP API directly
- New flow (Pre-A1 through A10): Reads Step 1 JSON from `data/discovery/`; no live API calls
- No physical deletes — rows flagged with `delete_flagged=1` (soft delete); archive mode handles actual deletion
- `word_registry.last_automation_run` set to `'AUDITED'` on successful completion (new `AUDITED_SENTINEL` constant)
- `word_run_state.approved_by` set to `'PROVISIONAL'`
- Discovery file auto-selected by date unless `--extract-file` supplied

**3. `engine/constants.py` changes**
- `EXPECTED_SCHEMA_VERSION` → `"3.3.0"`
- New: `AUDITED_SENTINEL = "AUDITED"`

**4. `engine/audit.py` — WR changes**
- WR-05: Downgraded from `_fail_stop` → `_fail_review` (ID gaps are not evidence of partial write)
- WR-19: Now accepts `NOTE`, `NOTE_ON_ROOT_FAMILY`, or `PROSE_ONLY_MEANING` flags (previously only `NOTE`)

**5. `engine/flag_engine.py` — pending fix (not yet applied)**
- When a term's `wa_meaning_parsed.parse_warnings` contains `PROSE_ONLY`, flag_engine should write a `NOTE`/`PROSE_ONLY_MEANING` quality flag automatically
- Until this is done, WR-19 will fire REVIEW on any word with low-frequency Greek G2 terms

#### Session 2026-03-19: Code Review Findings (still valid)

DB Integrity fixes applied:
1. `mti_terms.word_data_reference` — bad IDs for peace and gladness rows. Fixed via `scripts/_fix_mti_wdr.py`.
2. 37 NULL `word_data_reference` rows (joy, fear, strength). Fixed via `scripts/_fix_mti_null_fields.py`.
3. 1 NULL strongs_number — mti_terms id=354 (alupos, anxiety). Assigned G0253.
4. 2 duplicate strongs within registry (peace H7999A×2, shame G0150×2) — accepted, no action.

Engine bug fixes applied (still valid, but some superseded by v2 redesign):
- `engine/new_word.py`: N2 purge, N13 insert, N19 all-XREF status, classify_strongs `extracted_theological_anchor`
- `engine/flag_engine.py`: Duplicate flag idempotency
- `engine/audit_word.py`: A10 dead code fixed — superseded by v2 redesign
- `engine/gap_fill.py`: S7 and S4 `final_status` logic corrected

**WR-14 note:** Effectively dead check. Low priority.

**owning_part format inconsistency:** peace uses `'1'/'2'/'3'`; joy uses `'Part1'/'Part2'/'Part3'`. Engine writes NULL for single-part words. Queries must handle both formats.

---

## Outstanding items — FULLY CORRECTED (as at 2026-03-24, after reading all uncommitted changes)

### What was resolved during 2026-03-23 (already in uncommitted code)

**WR-19 — DONE.** `engine/flag_engine.py` already has the PROSE_ONLY_MEANING fix:
- `_ensure_flag_type` bootstraps the `PROSE_ONLY_MEANING` flag type on every run
- `PROSE_ONLY_MEANING` is in `_DERIVABLE_FLAGS` (cleared before re-evaluate)
- When `wa_meaning_parsed.parse_warnings` contains `PROSE_ONLY`, the flag is written automatically
- `engine/audit.py` WR-19 already accepts `PROSE_ONLY_MEANING` alongside `NOTE` and `NOTE_ON_ROOT_FAMILY`
- **No further code change needed. Will auto-resolve on next AUDIT_WORD v2 run.**

**AUDIT_WORD v2 — DONE.** Complete redesign is in `engine/audit_word.py`. Reads from `data/discovery/` Step 1 JSON — no live STEP API calls. CLI updated in `engine/engine.py` (`--interactive`, `--extract-file` flags).

**Pipeline script — DONE.** `scripts/word_study_extract.py` exists. Discovery files present:
- `data/discovery/182_soul_step_data_20260323.json` ✓
- `data/discovery/004_anger_step_data_20260323.json` ✓
- `data/discovery/love_step_data_20260323.json` ✓ (legacy naming — no registry prefix)

**Schema M12 — CODED but not yet applied to DB.** `engine/migrate.py` has M12 (v3.2.0 → v3.3.0). `engine/constants.py` requires v3.3.0. DB must be migrated before any engine run.

---

### What still needs to be done — based on actual engine report (2026-03-24)

**Soul current state (from `--report --registry=182` run at 05:53 UTC):**
- `phase1_status`: Complete, 24 terms, 757 verses
- `last_automation_run`: AUDITED (RUN-20260323_202200-AUDIT_WORD)
- Latest audit result: **REVIEW** — 3 non-pass checks remain

**WR-05 REVIEW** — ID gaps [(491,493), (493,1530)]: expected structural artefact from term expansion. No action required.

**WR-08 REVIEW** — Low verse/occurrence ratio on:
- H4578: 0 verses / 32 occurrences
- H5397: 0 verses / 24 occurrences  
- G5590: 0 verses / 825 occurrences
- G5590G: 46 verses / 825 occurrences (ratio 0.056 — below threshold)

Note: H4578, H5397 and G5590 (unsuffixed) are in the WR-08 report but **not** in term_inventory (file_id=36) — the report is resolving them from a different table or the audit reads strongs data differently. Requires investigation before any action.

**WR-19 REVIEW** — 17 terms have `parse_warnings` but no NOTE flag: G5590, H5317, H5314, G5590G-K, G5591, G1634, G1374, G0674, G0895, G2174, G2473, G3642, G4861. The PROSE_ONLY_MEANING flag IS being written correctly by flag_engine (confirmed in report — 14 PROSE_ONLY_MEANING flags present). WR-19 still fires because it checks for NOTE-group flags, not DATA_COVERAGE flags. The audit.py WR-19 check needs to also accept PROSE_ONLY_MEANING from DATA_COVERAGE group, or the flag_engine needs to write it to the NOTE group.

**Immediate next step:** Investigate WR-08 — understand why H4578, H5397, G5590 appear in the audit check when they are not in wa_term_inventory for file_id=36. Then resolve WR-19 flag-group issue.

### Other pending tasks (lower priority)
- ~~Create `docs/interaction-preferences.md`~~ — **DONE** (2026-03-24 this session)
- ~~Add pointer in `README.md`~~ — **DONE** (2026-03-24 this session)
- Commit all uncommitted work

---

## Pending Instruction: Commit All Uncommitted Changes

### Understood instruction
Commit all uncommitted changes to the local git repository.

### Scope — requires clarification before proceeding

There are two categories of uncommitted work:

**Category A — 12 modified tracked files (`git add -u`)**
These are files already known to git that have been changed:
- `README.md`
- `analytics/step_client.py`, `analytics/word_export.py`
- `data/schema/create_tables.sql`
- `docs/audit_word_refactor_review.md`
- `engine/audit.py`, `engine/audit_word.py`, `engine/constants.py`, `engine/engine.py`, `engine/flag_engine.py`, `engine/migrate.py`, `engine/span_filter.py`

**Category B — ~90 untracked new files (`??` in git status)**
These are files git has never tracked before. They include:
- `scripts/word_study_extract.py` ← main new pipeline script (should be committed)
- `docs/audit_word_design.md`, `docs/word_study_extract_design.md`, `docs/pipeline_decisions_20260323.md`, etc. ← design docs (should be committed)
- `data/discovery/` ← discovery JSONs (may or may not be committed — could be in .gitignore)
- `outputs/audit_diff_*.md`, `outputs/session-20260324-plan.md` ← session outputs
- `Logs/session-2026-03-23-soul-audit-recovery.md`
- `scripts/_tmp_*.py`, `scripts/_probe_*.py`, `scripts/_check_*.py`, `scripts/_repair_*.py` ← ~60 one-off diagnostic scripts

### Question for researcher
Does "all uncommitted changes" mean:
1. **Category A only** — just the 12 modified tracked files (the engine redesign)
2. **Everything** — all of A + all of B (`git add .`)
3. **A + selected B** — modified tracked files plus specific new files (e.g. exclude `_tmp_*.py` and `data/discovery/`)

Also: what commit message should be used? Suggested: `"2026-03-23: AI attempts to fix and correct and update, but largely fails. this brings all the repo up to date with all the endevours"`

**Awaiting approval before running any git commands.**

---

## Chronological Review — COMPLETE ✓
**Completed: 2026-03-24**

All modified files (12) and key untracked files read. `/memories/repo/engine-bugs-and-fixes.md` fully updated.

### Corrections to earlier memory notes

1. **`engine/flag_engine.py` PROSE_ONLY_MEANING** — was noted as "pending fix (not yet applied)". **CORRECTION: It IS already applied** in the uncommitted code. `_ensure_flag_type()` bootstraps the flag type; flag is written when `parse_warnings` contains "PROSE_ONLY"; added to `_DERIVABLE_FLAGS`.

2. **"True outstanding items" list in memory** — was a mid-session TO-DO list written before the 20:22 audit ran. The migrate (M12) DID run (schema check passed for the 20:22 run). The AUDIT_WORD v2 DID run (RUN-20260323_202200). Those items are DONE. Only WR-08 and WR-19 remain as researcher actions.

### Confirmed last action of 2026-03-23
`python -m engine.engine --audit_word --registry=182` (or equivalent) at approximately 20:22.  
Run ID: `RUN-20260323_202200-AUDIT_WORD`  
Result: 24 terms, 757 verses, `phase1_status=Complete`, `last_automation_run=AUDITED`, `audit_result=REVIEW` (3 items: WR-05, WR-08, WR-19).

### New files created during 2026-03-23 (untracked)
Key docs created post-crash in timestamp order:
- 15:07 `docs/pipeline_design_review_20260323.md` — pipeline architecture review
- 15:07 `docs/soul_phase2_root_cause_analysis.md` — root cause + fix plan for Soul Phase 2 issues
- 15:10 `docs/pipeline_decisions_20260323.md` — pipeline decisions agreed by researcher
- 17:19 `docs/audit_word_refactor_review.md` — updated (DB_ONLY_TERM + Section 6 wa_verse_term_links)
- 18:21 `docs/word_study_extract_design.md` — annotated JSON design reference
- 20:08 `docs/audit_word_design.md` — full AUDIT_WORD v2 design specification
- `data/discovery/love_step_data_20260323.json` + `.md` (18:16)
- `data/discovery/182_soul_step_data_20260323.json` + `.md` (18:25)
- `data/discovery/004_anger_step_data_20260323.json` + `.md` (18:27)
