# File Organisation Assessment — 2026-04-14

> Produced by Claude Code at leRoux's request. This is a read-only assessment — no files have been moved or renamed.

---

## 1. Project Scale

| Area | Files | Notes |
|------|-------|-------|
| **data/imports/WA/** | 919 | Session B analysis, VC, dim review, workflow docs, patches |
| **data/exports/** | 577 | STEP extracts (416), Session C (32), dim review (75), VC (38), session_d (7), vertical_pass (8) |
| **data/discovery/** | 385 | STEP discovery JSON + markdown pairs |
| **archive/** | 373 | patches (211), scripts (123), docs (22), logs (17) |
| **outputs/** | 246 | reports/words (157), investigations (34), reports/programme (32), archive (18), docx (3), pdf (1) |
| **scripts/** | 87 | Active utility and maintenance scripts |
| **Logs/** | 51 | Root-level session logs |
| **engine/** | 32 | Core automation engine modules |
| **docs/** | 29 | Reference documents |
| **analytics/** | 8 | Python library (plus 7,890 in venv — excluded) |
| **research/** | 6 | Templates only (placeholder) |
| **Total (excl. venv/backups/.git)** | **~3,500** | |

---

## 2. Problems Identified

### 2.1 Two Conflicting Organisation Documents

The project has two file organisation documents that contradict each other:

| Document | Created | Scope |
|----------|---------|-------|
| [file_organization.md](docs/file_organization.md) | Early project | Two-tier Google Drive / Git model with numbered folders (00_Admin, 01_Primary_Sources, etc.) |
| [file-organisation-rules.md](docs/file-organisation-rules.md) | 2026-03-30 | Framework B rules — current naming patterns, subfolder placement |

**Impact:** `file_organization.md` references a folder structure (00_Admin, 01_Primary_Sources, 04_Claude_Research, etc.) that was never implemented. It also references GitHub Copilot as the coding tool. It is obsolete but still present in `docs/`, creating confusion about which rules apply.

**Recommendation:** Archive `file_organization.md` to `archive/docs/`. The Framework B rules document is authoritative.

---

### 2.2 Naming Inconsistencies

The single biggest source of confusion. Four distinct problems:

#### a) Date format split

| Format | Count | Examples |
|--------|-------|---------|
| Hyphenated `2026-04-12` | ~193 files | `wa-064-forgiveness-sessionB-brief-v1-2026-04-12.md` |
| Compact `20260412` | ~348 files | `wa-dim-C17-observations-v1.2-20260413.md` |

Both formats are used **within the same folder** and sometimes for the **same word's files**.

#### b) Case inconsistency

Same cluster, same folder, different case:
```
wa-dim-C17-observations-v1.2-20260413.md    (uppercase C17)
wa-dim-c17-session-log-v1-2026-04-10.md     (lowercase c17)
```

Also: `WA-VCB-001-SessionLog-RegistryB-20260330.md` vs `wa-vcb-002-sessionlog-001-20260330.md`

#### c) Separator inconsistency

- Some files: `WA-001-abomination-analysis-2026-03-07.md` (hyphens)
- Some files: `contrition_30_full_20260413_v1.json` (underscores)
- The file-organisation-rules.md itself says "use underscores" in one section but all its naming patterns use hyphens.

#### d) Prefix inconsistency

Files in `Session_B_Analysis/` use at least three prefix styles:
```
FrameworkB-SessionB-Registry111-Mercy-20260326.docx   (old Framework style)
WA-001-abomination-analysis-2026-03-07.md             (WA uppercase)
wa-068-grace-sessionB-observations-v1-20260410.md     (wa lowercase)
```

**Recommendation:** Standardise on a single pattern project-wide. Proposed: `wa-{nnn}-{word}-{type}-v{n}-{YYYYMMDD}.md` (lowercase, hyphens, compact date). Then rename in bulk.

---

### 2.3 Cross-Placed Files

Files sitting in the wrong folder per the organisation rules:

| File(s) | Current location | Should be in |
|---------|-----------------|-------------|
| 4 Session C notes (`wa-*-sessionC-*`) | `Session_B_Analysis/` | `Session_C_Words/` |
| 3 dimension review files (`wa-dim-c13-*`) | `Session_B_Verse_Context/` | `Session_B_Dimension_Review/` |
| `wa-session-log-2026-04-13.md`, `wa-session-log-2026-04-13-b.md` | `Session_B_Dimension_Review/` | Ambiguous — generic session logs without cluster/word scoping |
| CC directives (`CC-DIRECTIVE-062-*`) | `archive/patches/` | Should these be in a directives folder? |
| Several `.docx` instruction files | `Session_B_Analysis/` | `Workflow/Framework_B/Session_B/archive/` |

**Impact:** When looking for all Session C materials for a word, you must search multiple folders. Dimension review observations for C13 are split across two folders.

---

### 2.4 Version Proliferation Without Archiving

The archiving rules say "old versions move to archive". In practice, all versions accumulate:

| Example | Versions in folder |
|---------|-------------------|
| compassion Session B observations | 7 versions (v1 through v7) |
| C17 dimension review session logs | 11 versions (v1 through v11) |
| love Session B observations | 4+ versions (v1, v2, v5, v8) |
| forgiveness word study | 3 versions (v1, v2, v3) |

**Total:** `data/imports/WA/Session_B_Verse_Context/` alone has **323 files**, many of which are intermediate versions.

**Impact:** When you need the current observations for a word, you must scan through all versions to find the latest. There's no way to distinguish "current" from "superseded" without opening files or parsing version numbers.

**Recommendation:** Either (a) move all-but-latest versions to an `archive/` subfolder within each imports directory, or (b) adopt a convention where only the latest version is present (prior versions tracked by Git history).

---

### 2.5 The "Framework_B" Typo

```
data/imports/WA/Workflow/Framework_B/    ← typo: should be "Framework_B"
data/imports/WA/Workflow/Framework_A/    ← correct
```

This typo is embedded in 136 files' paths and referenced in CLAUDE.md, file-organisation-rules.md, and multiple scripts. It has been there since the folder was created.

**Impact:** Cosmetic, but creates confusion when referencing paths. Git rename would preserve history.

---

### 2.6 Flat Patch Archive (211 files)

`archive/patches/` contains 211 applied patch files with no sub-organisation:
- VC batch patches (`wa-vcb-*`)
- Session B patches (`wa-*-sessionB-*`, `PATCH-*-ANALYSIS-*`, `PATCH-*-PREANALYSIS-*`)
- Dimension review patches (`wa-dim-*`)
- REPAIR patches
- SD pointer patches
- CC directives mixed in with JSON patches

**Recommendation:** Subdivide by type:
```
archive/patches/
  verse_context/        ← VCB patches
  session_b/            ← PREANALYSIS, ANALYSIS, SESSIONB, SESSIONB-COMPLETE
  dimension_review/     ← dim patches
  repair/               ← REPAIR patches
  sd_pointers/          ← SD pointer enrichment
  directives/           ← CC directive markdown files
```

---

### 2.7 Duplicate Report Versions in outputs/

`outputs/reports/words/` has **157 files**, including multiple date-stamped versions of the same VC report:
```
vc-report-004-anger-20260331.docx
vc-report-004-anger-20260402.docx
vc-report-004-anger-20260404.docx
```

`outputs/reports/programme/` has 6 database schema snapshots from different dates.

**Recommendation:** Keep only the latest version in the active folder; move older versions to `outputs/archive/`.

---

### 2.8 scripts/ Contains Obsolete One-Off Scripts

87 scripts in `scripts/`, including:
- 6 `_check_stupor*.py` / `_check_sorrow*.py` variants (one-off investigations)
- 3 `_probe_*.py` scripts
- 2 `_orphan_check*.py` scripts
- `_check_empty_fi.py` and `_check_empty_fi2.py`
- Multiple `_check_mti_*.py` variants

Many of these were single-use investigation scripts that should have been archived after use.

**Recommendation:** Review each `_check_*` and `_probe_*` script. If it was a one-off investigation (not reusable), move to `archive/scripts/`.

---

### 2.9 Logs/ Root Folder vs Other Log Locations

Session logs are scattered across four locations:

| Location | Files | Content |
|----------|-------|---------|
| `Logs/` (root) | 51 | Mixed: old session logs, instruction docs, pipeline reviews |
| `data/imports/WA/Session_B_Verse_Context/` | ~60 session logs | VC batch session logs |
| `data/imports/WA/Session_B_Analysis/` | ~20 session logs | Session B analysis logs |
| `data/imports/WA/Session_B_Dimension_Review/` | ~25 session logs | Dim review session logs |
| `data/imports/WA/Workflow/Sessionlogs/` | ~15 | Workflow session logs |

**Impact:** To reconstruct what happened on a given date, you must check 5+ folders.

---

### 2.10 docs/ Contains Stale Documents

| File | Status |
|------|--------|
| `file_organization.md` | Obsolete (see 2.1) |
| `Corrective action for Table relatio.txt` | Truncated filename, likely one-off |
| `general observations.md` | Vague title, likely stale |
| `patch_specification.md` | Superseded by `patch_specification_v1_10` in Workflow |
| `orphan_flags_audit.csv` | One-off investigation output |
| `soul_phase2_root_cause_analysis.md` | One-off investigation |
| `post_fix_script_review.md` | One-off review |
| `db_preflight_findings.md` | One-off findings |
| `engine_dml_audit_20260322.md` | One-off audit |

**Recommendation:** Move one-off investigation outputs to `outputs/investigations/`. Archive obsolete docs. Keep only current reference documents in `docs/`.

---

## 3. Summary of Recommendations

### Quick wins (low risk, high impact)

| # | Action | Files affected |
|---|--------|---------------|
| 1 | Archive `docs/file_organization.md` | 1 |
| 2 | Move cross-placed files to correct folders (2.3) | ~10 |
| 3 | Move one-off docs to `outputs/investigations/` (2.10) | ~6 |
| 4 | Move older VC report versions to `outputs/archive/` (2.7) | ~100 |
| 5 | Archive one-off scripts (2.8) | ~15-20 |

### Medium effort (some coordination needed)

| # | Action | Files affected |
|---|--------|---------------|
| 6 | Subdivide `archive/patches/` by type (2.6) | 211 |
| 7 | Move superseded import versions to archive subfolders (2.4) | ~200+ |
| 8 | Standardise date format in new files going forward | Policy change |
| 9 | Standardise case convention in new files going forward | Policy change |

### Larger effort (needs planning)

| # | Action | Notes |
|---|--------|-------|
| 10 | Bulk rename existing files to consistent pattern | Could be scripted; Git tracks renames |
| 11 | Rename `Framework_B` to `Framework_B` | Affects 136 paths + references in CLAUDE.md and docs |
| 12 | Build a file index/manifest | A machine-readable JSON index mapping each file to its type, word, session, date, and current-vs-superseded status |

### Structural suggestion: File Manifest

The most impactful long-term improvement would be a **machine-readable file manifest** — a JSON file (e.g., `data/file_manifest.json`) that indexes every non-code file with metadata:

```json
{
  "files": [
    {
      "path": "data/imports/WA/Session_B_Analysis/wa-068-grace-sessionB-observations-v5-20260410.md",
      "type": "session_b_observations",
      "registry": 68,
      "word": "grace",
      "version": 5,
      "date": "2026-04-10",
      "status": "superseded",
      "superseded_by": "wa-068-grace-sessionB-observations-v6-20260411.md"
    }
  ]
}
```

This would allow:
- Programmatic lookup: "give me the latest observations for grace"
- Stale file detection: "which files are superseded but not archived?"
- Cross-reference: "all files related to registry 68"
- Consistency audit: "which files don't match the naming convention?"

Claude Code could maintain this manifest automatically as files are created or moved.

---

## 4. Proposed Naming Standard (for discussion)

If you want to standardise going forward:

```
Pattern:  wa-{NNN}-{word}-{type}-v{n}-{YYYYMMDD}.{ext}
Case:     all lowercase
Seps:     hyphens (-)
Date:     compact YYYYMMDD
Version:  v{n} (integer, no leading zero)

Examples:
  wa-068-grace-sessionb-observations-v5-20260410.md
  wa-dim-c17-session-log-v1-20260413.md
  wa-vcb-034-term-observations-v1-20260412.md
  patch-20260412-068-sdenrich-v1.json
```

Types: `observations`, `session-log`, `brief`, `word-study`, `cc-directive`, `patch`, `extract`, `report`

---

*Assessment complete. No files moved. Awaiting your direction on which recommendations to pursue.*
