# Cluster Folder File Naming — Assessment + Canonical Proposal

**Date:** 2026-05-21
**Author:** CC
**Purpose:** Identify the inconsistencies the researcher flagged in `Sessions/Session_Clusters/M0X/` filenames, propose a canonical convention, and scope the rename work.

---

## 1. The problem

`Sessions/Session_Clusters/M0X/` folders carry **two distinct first-three-segment conventions** for cluster-scoped artefacts. The split is roughly 50/50 across 660+ files at the cluster top level:

| Shape | Count | Examples |
|---|---:|---|
| `wa-cluster-{CODE}-{kind}-v{n}-{date}.{ext}` (lowercase, with `cluster` prefix) | 346 | `wa-cluster-M03-detail-v2-20260506.md`, `wa-cluster-M08-constitution-v2-20260520.md` |
| `WA-{CODE}-{kind}-v{n}-{date}.{ext}` (CAPS, no `cluster` prefix) | 312 | `WA-M07-dir-001-term-transfer-v1-20260519.md`, `WA-M08-phase9-char1-Arrogant-self-elevation-brief-v1-20260521.md` |
| `wa-obslog-{CODE}-{kind}-...` (special category — observation logs) | 10 | `wa-obslog-M08-phase1-ut-v1-20260520.md` |
| Lowercase cluster code: `wa-cluster-m06-...`, `wa-cluster-m05-...` | 3 | `wa-cluster-m05-coverage-v1-20260505.md` |
| Doubled prefix: `WA-M07-M07-...`, `WA-M02-M02-...` | 15 | `WA-M07-M07-A-vcg-design-v1-20260519.md` — **clearly a bug** |
| Other (`wa-global-...`, `wa-sessionlog-...` etc.) | ~10 | |

### Where the divergence came from

The dominant `wa-cluster-{CODE}-*` shape is what generator scripts (constitution report, subgroup meanings, complete extract) produce. The CAPS shape was adopted by:

1. **AI-authored artefacts** (Phase 5 design, Phase 7 VCG designs, Phase 9 findings) — AI sessions pick their own filenames; if not given an exact target, they default to `WA-{CODE}-...`.
2. **CC-built directive files** — I authored these as `WA-{CODE}-dir-NNN-*.md` matching the M01..M07 precedent set in earlier sessions.
3. **Phase 9 builder scripts** — `_build_m07_*phase9*.py` and the M08 clones use `WA-M07/M08-phase9-...` filename templates.

`docs/file-organisation-rules.md` §2.1 states: *"All non-code files produced by or for the programme follow these rules: **Case** — All lowercase"*. The CAPS convention violates this; the carve-out in §2.2 explicitly says "Governing documents retain their established `WA-` uppercase prefix for continuity. **All other files use lowercase `wa-`.**"

So the lowercase `wa-cluster-{CODE}-...` shape is the rules-compliant canonical.

---

## 2. Proposed canonical

**`wa-cluster-{CODE}-{kind}-v{n}-{YYYYMMDD}.{ext}`**

Where:

- **`wa-cluster-`** — lowercase prefix; literal `cluster` segment scopes the artefact as cluster-level
- **`{CODE}`** — cluster code in CAPS (`M01`, `M07`, `M46`). Cluster codes are conventionally CAPS per the DB; the file convention preserves that.
- **`{kind}`** — lowercase, hyphenated descriptor of artefact (`constitution`, `dir-001-term-transfer`, `phase9-char1-arrogant-self-elevation-brief`, `subgroup-design`, `vcg-creation`, etc.)
- **`v{n}`** — integer version, no leading zero
- **`{YYYYMMDD}`** — compact date

Special-case retention:

- **`wa-obslog-{CODE}-{kind}-...`** — keep as-is. Observation logs are a distinct artefact category and this naming is consistent across all clusters that have them.
- Subfolders like `inputs/`, `published/`, `files phase N/` are unchanged.

---

## 3. Scope of the rename

### Files to rename (cluster top-level files only)

| Current shape | Files | Action |
|---|---:|---|
| `WA-{CODE}-{kind}-...` → `wa-cluster-{CODE}-{kind}-...` | ~312 | Lowercase prefix + insert `cluster` segment |
| `WA-{CODE}-{CODE}-{X}-vcg-design-...` (doubled prefix bug) | ~15 | Drop the doubled `{CODE}` segment, then apply the above |
| `wa-cluster-m{NN}-...` (lowercase code) | 3 | Uppercase the code |
| `wa-obslog-{CODE}-...` (10 files) | 0 | Keep as-is |

**Total: ~330 files** at cluster top level across 13 clusters (M01-M08, M15, M20, M26, M39, M46).

### Renames NOT in scope (this pass)

- Files **inside** `inputs/`, `published/`, `files published/`, `files phase N/`, `archive/` subfolders. These are AI-output staging areas; their internal contents reference their own canonical names. Leave them alone.
- Filename references **inside** existing markdown documents (e.g. directives that reference each other by filename). These markdown references will resolve to either the renamed target or the missing old name; we accept this minor breakage in superseded directives since they are historical records, not active inputs.
- Files in `Sessions/Session_A`, `Sessions/Session_B`, `Sessions/Session_C/Session_C_Words/` — different naming domains entirely (per-word and per-batch artefacts).

### Scripts to fix (so future files are correct)

The scripts that hardcode the CAPS pattern in filename templates:

| Script | Hits | Action |
|---|---:|---|
| `_build_m07_characteristic_phase9_package_20260520.py` | 2 | Update to `wa-cluster-M07-...` template |
| `_build_m07_characteristic_phase9_bundle_20260520.py` | 2 | Update |
| `_build_m07_phase9_cluster_synthesis_20260520.py` | 2 | Update |
| `_build_m08_characteristic_phase9_package_20260521.py` | 2 | Update |
| `_build_m08_characteristic_phase9_bundle_20260521.py` | 2 | Update |
| `_build_m08_phase9_cluster_synthesis_20260521.py` | 2 | Update |
| Several M0X-specific apply scripts referencing CAPS output filenames in print statements / source notes | ~10 | Update narrative references |

### Manifest

Rebuild `database/file_manifest.json` after the rename via `python scripts/build_file_manifest.py`.

---

## 4. Implementation plan

If approved:

1. **Build a rename map** — programmatically transform every `WA-{CODE}-...` filename to `wa-cluster-{CODE}-...`. Dump the proposed map to `docs/cluster-rename-map-20260521.json` for review.
2. **Execute renames** in a single transaction (Python script that does `Path.rename` for each pair, logs to console + a result file).
3. **Update scripts** — patch the 6 phase9 builders to emit the canonical filename template.
4. **Rebuild manifest** — `python scripts/build_file_manifest.py`.
5. **Update memory** — note the canonical naming so future sessions don't drift back.
6. **Commit** — single commit with all renames + script fixes + manifest rebuild.

---

## 5. Risks

| Risk | Mitigation |
|---|---|
| Existing markdown documents reference old filenames internally | Acceptable — these are historical records. Active references that matter (in instruction docs, current briefs) will be updated separately if needed. |
| Git history shows files as deleted + re-added | Git tracks renames automatically when the content is identical; the diff will show as `R` (rename) rather than `D + A`. |
| AI sessions in flight (M08 Phase 9) reference old filenames | M08 Phase 9 briefs have not yet been executed by AI. Rename the in-flight files at the same time as everything else; AI will read the new names. |
| Inputs/published/files-phase-N subfolders may have internal cross-refs | Subfolder contents are out of scope for this rename pass. |

---

*End of assessment. Awaiting researcher confirmation of the canonical form before executing.*
