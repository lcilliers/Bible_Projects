# File Cleanup Plan — 2026-04-23

**Purpose:** audit of file placement vs [docs/file-organisation-rules.md](../../docs/file-organisation-rules.md), proposing moves tiered by risk and decision-weight. Nothing moves until the researcher approves the tier.

**Status:** AWAITING APPROVAL. Tier 1 is mechanical and safe to execute on approval. Tier 2 is mechanical but bulk. Tier 3 needs researcher decisions before any action.

---

## Summary of findings

| Tier | Issue | Count | Risk |
|---|---|---:|---|
| 1 | Files at `outputs/` root (subfolder exists for their type) | 10 | Low |
| 1 | Corrective: do NOT delete `~$` Word lock files (they are live) | 3 | — |
| 2 | Superseded-by-date STEP Extracts (older dated files per word) | ~80 pairs | Low-Medium |
| 2 | Uppercase-prefix `.docx` extracts in `outputs/docx/` | 2 | Low |
| 2 | Orphaned session logs in `Logs/` root with non-standard names | ~12 | Low-Medium |
| 3 | `data/imports/WA/Prose/` — folder not in rules (active workspace) | 45 files | Needs decision |
| 3 | `data/imports/WA/Word_Data/` — folder not in rules (legacy research) | ~100 files | Needs decision |
| 3 | Investigation files with `WA-` uppercase prefix (not governing docs) | ~5 | Needs decision |

Total files in scope: ~245. Most are archive moves; none are deletions.

---

## Tier 1 — Mechanical moves (safe to execute on approval)

### 1.1 Move 10 files out of `outputs/` root

Per §3.10, `outputs/` root must be empty of files. Everything goes in a subfolder.

| Source | Target | Rationale |
|---|---|---|
| `outputs/dim-label-noncanonical-rows-20260420.json` | `outputs/investigations/dim-label-noncanonical-rows-20260420.json` | Ad-hoc investigation artefact |
| `outputs/dim-label-verse-evidence-extract-20260420.json` | `outputs/investigations/dim-label-verse-evidence-extract-20260420.json` | Ad-hoc investigation artefact |
| `outputs/term-introduction-classification-proposals-20260420.md` | `outputs/investigations/term-introduction-classification-proposals-20260420.md` | Investigation artefact |
| `outputs/wa-183-heart-dirresult-001-phaseb-verify-v1-20260420.md` | `outputs/reports/programme/wa-183-heart-dirresult-001-phaseb-verify-v1-20260420.md` | Directive result report |
| `outputs/wa-global-databasereview-rd-v1-20260419.md` | `outputs/reports/programme/wa-global-databasereview-rd-v1-20260419.md` | Programme-level report |
| `outputs/wa-global-dirresult-002-dim-label-proposals-v1-20260420.json` | `outputs/reports/programme/wa-global-dirresult-002-dim-label-proposals-v1-20260420.json` | Directive result report |
| `outputs/wa-global-dirresult-002-dim-label-proposals-v1-20260420.md` | `outputs/reports/programme/wa-global-dirresult-002-dim-label-proposals-v1-20260420.md` | Directive result report |
| `outputs/wa-global-first-pass-close-v1-20260420.md` | `outputs/reports/programme/wa-global-first-pass-close-v1-20260420.md` | Programme-level report |
| `outputs/wa-global-outstanding-tasks-v1-20260419.md` | `outputs/reports/programme/wa-global-outstanding-tasks-v1-20260419.md` | Programme-level report |
| `outputs/wa-global-programme-control-v1-20260420.md` | `outputs/reports/programme/wa-global-programme-control-v1-20260420.md` | Programme-level report |

### 1.2 Lock files — NO action

Do **NOT** touch `outputs/docx/~$-*.docx`. These are Word's live-edit lock files (you currently have those .docx files open). They'll vanish when Word closes. Flagging only so the Explore-agent's "delete" recommendation is formally rejected.

---

## Tier 2 — Bulk mechanical archiving (approve one line to do all)

### 2.1 STEP Extracts — archive older-dated versions per word

§3.1 rule: _"When a new day's export supersedes a prior day's, the prior day's file is moved to `data/exports/archive/`."_

Current state in `data/exports/STEP Extracts/` is a mix: ~100 words have one or more dated exports each; many words have 2–5 files where older dates are superseded by a later date for the same word.

Example (Soul):

| File | Keep? | Reason |
|---|---|---|
| `Soul_182_full_20260324.json` | archive | superseded by 20260404 |
| `Soul_182_full_20260328_v1.json` | archive | superseded by 20260404 |
| `Soul_182_full_20260328_v2.json` | archive | superseded by 20260404 |
| `Soul_182_final_20260328_v1.json` | archive | "final" scope, superseded by 20260404 full |
| `Soul_182_full_20260404_v1.json` | **keep** | latest |

I estimate ~80 archive-moves across the folder. Automated by a script that groups by `{word}_{reg}_{scope}` and keeps only the latest `{date}_v{n}`.

**Proposed action:** I write a short dry-run script that lists every proposed move. You spot-check 5–10, approve, I then execute.

Target location: `data/exports/archive/STEP Extracts/` (new folder, mirrors source structure).

### 2.2 `.docx` extracts with uppercase prefix

Per naming rule §2.1 (lowercase, hyphenated), two files violate:

| Source | Target |
|---|---|
| `outputs/docx/ANGER-full-extract-2026-03-16.docx` | `outputs/archive/ANGER-full-extract-2026-03-16.docx` |
| `outputs/docx/LOVE-full-extract-2026-03-16.docx` | `outputs/archive/LOVE-full-extract-2026-03-16.docx` |

These are pre-framework exports from mid-March. Dated hyphen-format (`2026-03-16`) rather than compact (`20260316`). Easier to archive as historical than rename in place — they won't be regenerated and their names are unique enough that git history preserves them.

### 2.3 `Logs/` root — non-standard names

`Logs/` root has ~12 files that don't match `wa-session-log-{YYYYMMDD}-{topic}.md`. All dated March or early April. Two options:

- **(a)** Rename-in-place to the standard pattern (preserves location).
- **(b)** Archive to `archive/Logs/` as historical, rename optional.

Per §3.12 _"old session logs stay in their folder (historical records). Only move to `archive/Logs/` if explicitly superseded or no longer topically relevant."_ — option (a) is closer to the spirit of the rule.

**Proposed:** option (a) — I list the renames; you approve; I execute. Non-ASCII and mixed-case get normalised, `.docx` session logs (there are two) converted or archived on your call.

---

## Tier 3 — Decisions needed before any action

### 3.1 `data/imports/WA/Prose/` — not in the rules

**What's there:** 45 files — draft prose (`wa-prose-draft-*.md`), obslogs, session logs, catalogue patches, prose-programme JSON outputs, framework review, style/approach docs. Created 2026-04-21 and 2026-04-22. You committed all 45 in yesterday's session-snapshot commit.

**The situation:** this is an **active authoring workspace** for programme prose, not a misfiled folder. It did not exist when the rules were written.

**Options:**

1. **Extend the rules** — add §3.16 covering `data/imports/WA/Prose/` with subfolders: `drafts/` (v1/v2/v3 .md), `patches/` (catalogue + PROSE JSON), `logs/` (obslog + session log), `reference/` (framework review, style doc). This matches how you actually use it. _My recommendation._
2. **Route contents into existing folders** — drafts → `Session_B_Analysis` (wrong stage, don't do this), patches → `Patches/` (possibly), logs → `Logs/`. Splits the workspace and makes it harder to work inside.
3. **Keep as-is, undocumented** — technically drifts but you know what's there.

Recommendation: **Option 1**, and we write it up when the chapters you're authoring finish.

### 3.2 `data/imports/WA/Word_Data/` — legacy research

**What's there:** ~100 files. Old naming (`Word Anger.md`, `word_flesh_Part1.md`, `word_joy_Part1_2.md` duplicates), some `.txt` fragments with broken names (`"Flesh 185  there is no heading, to.txt"`, `"next word love 103  header.txt"`), pre-framework `.json` files (`WA-061-fear-data-part1-2026-03-11.json`). Mostly from March 2026.

**What it is:** the pre-framework research source material that seeded the programme. Registries were built from these notes; they're historical.

**Options:**

1. **Move entire folder to `archive/data/imports/WA/Word_Data/`** — signals "historical source, preserved but out of active scope". Git history preserves location. _My recommendation._
2. **Keep it as active but document it** — adds a rule, but no current pipeline reads from it.
3. **Clean individual duplicates** (`_2`, ` (1)` files, broken `.txt`) and leave the rest — halfway house.

Recommendation: **Option 1**. These files were input to the registry and Session A; nothing in the current pipeline reads them. Archive preserves access via the file manifest.

### 3.3 Investigation files with `WA-` uppercase prefix

§2.2: _"Governing documents retain their established `WA-` uppercase prefix for continuity. All other files use lowercase `wa-`."_

Non-governing files violating this rule (a handful in `outputs/investigations/` and `outputs/reports/`):

- `outputs/investigations/WA-InstructionGaps-v2_2-20260330.md`
- `outputs/investigations/WA-InstructionGaps-v2-20260330_1 researcher comments.md` (also has space in filename)
- `outputs/reports/WA-PipelineStatusReview-v2-20260330.md` (also in wrong subfolder per §3.10)
- `outputs/investigations/CLAUDE-MD-Update-Audit-20260330.md`

**Options:**

1. **Rename** to lowercase `wa-` (small git history impact).
2. **Archive** — these are March-dated; most are superseded by later work.
3. **Leave** — violation is minor and historical.

Recommendation: **Option 2** for anything dated before 2026-04-01 that has a known successor; otherwise **Option 1**.

---

## Not included / deliberately skipped

- **Governing instruction archive** in `data/imports/WA/Workflow/Framework_B/Session_B/archive/` — verified clean, prior versions correctly placed, nothing to do here.
- **Scripts hygiene** — survey agent flagged a few `_check_*` scripts as possibly stale, but the boundary between one-off and reusable is subjective. Better handled as a researcher-led pass.
- **Session-log version formatting** (e.g. `v1.0` vs `v1_0`) — minor; affects manifest search but not pipeline. Defer until you want a global rename pass.
- **`Session_D_Synthesis/` sub-organisation** — folder is fine, just big. Organise only if it grows further.
- **`data/exports/archive/`** — doesn't exist yet; will be created as needed during Tier 2 execution.

---

## Proposed sequence

1. **You approve Tier 1.** I execute the 10 moves. Update manifest. Commit.
2. **You approve Tier 2.** I write a dry-run script for STEP archiving, you spot-check the output, I execute. Handle docx-uppercase and Logs-root as the same commit or separate.
3. **You decide Tier 3 questions.** Tier 3.1 (Prose folder) probably just wants a rule addition, no moves. Tier 3.2 (Word_Data) is the biggest single action. Tier 3.3 is cleanup-on-top.
4. **File manifest rebuild** — run `python scripts/build_file_manifest.py` after each tier lands.

Nothing moves until each tier is approved. Each tier ends with a commit.

---

*Plan produced 2026-04-23 to audit file placement against `docs/file-organisation-rules.md`.*
