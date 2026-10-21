# Filing system for the verse-fanout method — design proposal (for approval)

- **File:** docs/verse-analysis-filing-design-proposal-v1-20260627.md · 2026-06-27 · Author: Claude Code.
- **Problem:** every new-method artefact is landing in `outputs/markdown/validation/`, mixed with old cluster-method and ad-hoc files. The method is **verse-centric and will grow to thousands of verses**; without a structure we lose the raw source collections (which hold irreplaceable researcher-added Logos/Claude material) and can't tell input from regenerable output.
- **Status:** proposal — **nothing moved yet.** Confirm §5 decisions and I implement.

## 1. Design principles
1. **The DB is the single source of truth** (`ib_observation`, `verse_analysis_progress`). Files are either **inputs** (raw fan-out collections) or **regenerable exports** (extracts/reports) — never the record of findings.
2. **Verse-centric, grouped by book** so it scales across the canon (66 book folders, verses within).
3. **Separate the three kinds of artefact:** raw INPUT (irreplaceable) · regenerable EXPORT · method/governance.
4. **Consistent with the existing standard** — mirrors how `Sessions-v2/{CODE}-{Name}/` gave clusters a dedicated tree (file-organisation-rules §3.0).

## 2. Proposed structure — a new top-level tree `verse-analysis/`
```
verse-analysis/                       ← home for ALL verse-fanout work products
  README.md                           ← orientation: method, structure, how to find a verse; links to method docs
  _reports/                           ← cross-verse roll-ups (progress, worklist exports) — snapshots
  {Book}/                             ← DB short_code: Gen, Exo, Lev, Psa, Mar …
    {Book}-{CCC}-{VVV}/               ← one folder per ANALYSED verse, zero-padded chapter/verse
      wa-{book}-{ccc}-{vvv}-fanout-v{n}-{date}.md        ← RAW source collection  (INPUT — preserve, version)
      wa-{book}-{ccc}-{vvv}-observations-v{n}-{date}.md  ← verse+observations extract (EXPORT — regenerable)
      wa-{book}-{ccc}-{vvv}-raw-{contributor}-v{n}-{date}.md  ← (optional) separate Logos/Claude raw drops
```
- **A folder is created only when a verse is actually analysed.** In-focus verses live only in the `verse_analysis_progress` anchor (DB) until worked — the tree never balloons with empty folders.
- **Method/governance docs stay in `Workflow/`** (the governance home) — `Workflow/methodology/` (operating model, dimension definitions, master synthesis) and `Workflow/Catalogue/` (dimensions catalogue). `verse-analysis/README.md` links to them. *(Alternative: move them under `verse-analysis/_method/`. Recommend NOT — keeps all governance consolidated in `Workflow/`.)*
- **Loader/builder scripts stay in `scripts/`** per §3.13, named per-verse (`_apply_load_ib_observations_{book}_{c}_{v}_*`).

## 3. Naming — zero-padded for canon-wide sort
Chapter and verse padded to **3 digits** so the whole canon sorts correctly (handles Psa 119:176):
- folder `Exo-001-013`, files `wa-exo-001-013-fanout-v1-20260627.md`.
- DB reference (`Exo 1:13`) stays canonical; the padded form is just the sortable file encoding.
- *(Alternative: readable `Exo-1-13` / `wa-exo-1-13-…` — but sorts wrongly past chapter 9. Recommend padded.)*

## 4. Migration map (what moves where)
| current file (outputs/markdown/validation/) | disposition |
|---|---|
| `wa-exo-1-13-fanout-v1-20260627.md` | → `verse-analysis/Exo/Exo-001-013/wa-exo-001-013-fanout-v1-20260627.md` (RAW) |
| `wa-exo-1-13-verse-and-observations-v2-20260627.md` | → `verse-analysis/Exo/Exo-001-013/wa-exo-001-013-observations-v2-20260627.md` (EXPORT) |
| `wa-exo-1-13-verse-and-observations-v1-…` | superseded by v2 → `outputs/archive/` |
| `wa-exo-1-13-ib-observations-v1-…` | superseded by v2 → `outputs/archive/` |
| `wa-gen-6-5-fanout-v1-20260627.md` | → `verse-analysis/Gen/Gen-006-005/wa-gen-006-005-fanout-v1-20260627.md` (RAW) |
| `wa-gen-6-5-ib-observations-v1-20260627.md` | → `verse-analysis/Gen/Gen-006-005/wa-gen-006-005-observations-v1-20260627.md` (EXPORT) |
| `wa-lev-25-44-45-corroboration-reading-v1-…` | **RETRACTED** → `outputs/archive/` (kept for provenance) |
| `wa-verse-analysis-progress-anchor-proposal-v1-…` | → `verse-analysis/_reports/` |
| `wa-verse-meaning-fanout-index-design-v1-20260626.md` | method/design → `Workflow/methodology/` |
| `wa-m10-validation-…-v1-20260624.md` | **old cluster method** (not new) → leave / `outputs/archive/` |

**Side-effects of renaming** (only if §5.3 = padded rename is approved):
- update `ib_observation.raw_file` (currently `wa-exo-1-13-fanout-v1-20260627.md` etc.) to the new names;
- update the in-file cross-reference pointers (extract → fanout);
- update the `RAW=` constant in the loader scripts;
- add a new section to `docs/file-organisation-rules.md` (a `§3.0b verse-analysis/` tree);
- `python scripts/build_file_manifest.py` to re-index.

## 5. Decisions needed before I implement
1. **Top-level home** = `verse-analysis/`? (or your preferred name)
2. **Per-verse folder** (`{Book}/{Book-CCC-VVV}/`) — yes? (vs flat files within each book folder)
3. **Naming** = zero-padded `Exo-001-013` (sorts canon-wide) — yes? (vs readable `Exo-1-13`)
4. **Method docs** stay in `Workflow/` — yes? (vs move under `verse-analysis/_method/`)
5. **Rename existing files** to the new convention (I update `raw_file` + cross-refs), or **keep current filenames** inside the new folders (no DB/cross-ref edits)?
