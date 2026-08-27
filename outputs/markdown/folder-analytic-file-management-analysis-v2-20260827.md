# Folder analysis — analytic-file management across the project (v2: full census)

Prepared for escalation #929 v4: *"This is a good extract, now combine the actual files in folders
of the entire project and map it to this what is should be."* Supersedes v1's sample-based survey
with a real census — every directory in the project walked, every file counted, filtered to
analytic-file extensions (`.md .json .docx .pdf .txt` — code and raw CSV data-table exports
excluded, matching v1's original scope statement), then mapped against v1's 13-group taxonomy
(A–M). **713 directories hold 12,331 analytic files.** New patterns v1's sampling missed are
called out explicitly, not folded in silently.

---

## 1. Totals by top-level area

| area | dirs | files | maps to group(s) |
|---|---|---|---|
| `Sessions/` | 245 | 3,455 | H, **plus a newly-found sub-pattern (see §3)** |
| `verse-analysis/` | 109 | 2,835 | G |
| `archive/` | 15 | 1,565 | J |
| `iba/` | 105 | 1,351 | I, **plus 4 new locations (see §4)** |
| `research/` | 11 | 1,052 | E |
| `Sessions-v2/` | 97 | 641 | F |
| `Workflow/` | 32 | 528 | A, K |
| `outputs/` | 21 | 319 | D |
| `memory/` | 1 | 241 | M |
| `Logs/` | 2 | 198 | C |
| `scripts/` | 68 | 83 | not analytic — code folder with a handful of stray `.md` notes, not a real analytic-file location |
| `docs/` | 1 | 36 | ungrouped in v1 — top-level `docs/` itself, mixed design docs (see §5) |
| `data/`, `scratchpad_tmp/`, `.` , `InnerBeingStudy/`, `database/` | 6 | 27 | incidental, not a real pattern |

---

## 2. Sessions-v2 — all 49 clusters, actual counts (group F)

Confirms F's structural convention (`Analysis/`/`Data/`/`essays/`/`findings/` per cluster) holds
uniformly, but the **population is wildly uneven** — something v1's single-sample description
could not show:

| cluster | files | cluster | files | cluster | files |
|---|---|---|---|---|---|
| M01-Fear | 106 | M12-Purity | 32 | M25-Life | 1 |
| M10-Sin | 134 | M07-Shame | 59 | M26-Righteousness | 1 |
| M02-Anger | 44 | M06-Hate | 26 | M27-Evil | 1 |
| M04-Joy | 44 | M08-Pride | 26 | M28-Envy | 1 |
| M03-Grief | 40 | M09-Humility | 26 | M29-Desire | 1 |
| M05-Love | 38 | M11-Repentance | 11 | M30-Obedience | 1 |
| M31-Faith, M37, M44, M47 | 2 each | M10b-Wickedness | 5 | remaining 26 clusters (M13–M46, excl. above) | 1–3 each |
| M10c-Defilement | 2 | | | | |

45 of 49 clusters carry 1–3 files (a `.gitkeep` plus a stub at most); 4 clusters (M01, M02–M05,
M07, M09–M10) hold the actual working volume. The folder structure is uniform; the content behind
it is not — a real fact about the state of cluster-rework, not a filing inconsistency, but relevant
to "what should be" if the aim includes knowing what's actually populated.

---

## 3. `Sessions/` (the pre-`Sessions-v2` tree, group H) — the volume v1 undercounted

| subsystem | files | note |
|---|---|---|
| `Session_Clusters/` | **2,006** | **Not named in v1 at all.** M-code folders (`FLAG`, `M01`…`M47`, bare codes, no descriptive suffix) — a parallel structure to `Sessions-v2/{code}-{Name}/`, under the old tree, holding more analytic files than every other single area in the project bar none. |
| `Session_B/` | 974 | The 12 numbered-stage folders v1 described |
| `Session_A/` | 415 | `STEP Extracts`, `terms`, `Word_Data`, `registry`, `Data_Prose` |
| `Session_C/` | 42 | |
| `Session_D/` | 14 | |
| `Patches/` | 4 | (most patches live in `Sessions/Patches/` proper, group A) |

`Session_Clusters` is the single largest concentration of analytic files anywhere in the project —
larger than `Sessions-v2` (641), `research/` (1,052), and `iba/` (1,351) each on their own, and
close to `verse-analysis`'s 2,835. It was invisible to v1's sampling because v1 sampled
`Sessions/Session_A/`, `_B/`, `_C/`, `_D/` (named in `CLAUDE.md`'s own directory map) but
`Session_Clusters/` is not named there at all.

---

## 4. `iba/` — four locations v1's sample of `iba/docs/` and `iba/app/reports/` missed

| location | files | what it is |
|---|---|---|
| `iba/app/verse-analysis/` | 308 | **A second, separate per-book folder tree**, parallel to the top-level `verse-analysis/` (group G) — but keyed on Title-Case/abbreviated book names (`1 Chronicles`, `1Cor`, `1Pet`) where the top-level tree uses lowercase full names (`daniel`, `psalms`, `hosea`). Two book-keyed analytic trees, two different naming conventions for the same 66-book set, coexisting. |
| `iba/app/config/` | 310 | `CONFIG-REPORT.md`/`CONFIG-REPORT-v{N}-{date}.md` snapshots + its own `archive/` and `export/` subfolders — a config-report-specific instance of group I's pattern, not previously listed as its own location |
| `iba/app/staging/operations/` | 16 | Unsurveyed in v1; a working/staging area, not yet characterised further here |
| `iba/config/` (`DBSchema/`, `archive/`, `process/`, `utility/`, `wide/`) | 26 | The parallel, not-yet-loadable configurator design named in `GOVERNANCE.md` §6 — its own small document set, distinct from `iba/app/config/`'s live config-report output |

---

## 5. Remaining areas, real subfolder counts

**`archive/`** (top-level, group J): `Sessions/` 999, `patches/` 391, `Clusters/` 86, `Programme_prose/` 37, `docs/` 30, `References/` 13, `Logs/` 5, `verse-analysis-state-20260704/` 4.

**`research/`** (group E): `discovery/` 637, `investigations/` 380, `VE-lexical/` 31, `templates/` 3, `notes/` 1.

**`Workflow/`** (groups A/K): `methodology/` 131, `archive/` 87, `Programme/` 67, `Sessionlogs/` 61, `Instructions/` 57, `Clusters/` 33, `Tiers/` 36, `schema/` 18, `Sciences/` 10, `reference/` 8, `Chat_responses/` 6, `Global_rules/` 5, `registry/` 4, `Catalogue/` 2, `Claude_API/` 1, `Obsidian/` 1, `SQLite/` 1.

**`outputs/`** (group D): `markdown/` 202, `integrity/` 43, `archive/` 40, `projections/` 9, `docx/` 7, `reports/` 4, `step-api-probe-20260716/` 5, `pdf/` 3, `cost-history/` 3, `cc/` 2, `json/` 1.

**`docs/`** (top-level, 36 files) — **not assigned to any group in v1.** A flat folder, no subfolders, no archive, mixing architecture docs, design reviews, one `.xlsx` (the escalation worksheet), and a `Session-A-v9-*` doc pair in both `.docx` and `.md`. Closest analogue is group B (`iba/docs/`) in spirit — design/planning docs — but `docs/` has no versioning convention applied consistently and no archive at all; it is its own, fourteenth pattern, not a fit for B.

---

## 6. What v1 got right, unchanged by this census

The 7 naming conventions and archiving-shape analysis in v1 §2 stand — the census confirms rather
than revises them; `Session_Clusters`, `iba/app/verse-analysis`, `iba/app/config`, `iba/app/staging`,
`iba/config/*`, and `docs/` are additions to the map, not corrections to what was already there.

## 7. Not attempted here

This document maps what exists and its real scale; it still does not recommend which convention
should become the standard, or what should happen to the 2,006-file `Session_Clusters` volume or
the two parallel `verse-analysis` trees — those are the "what it should be" decisions the
researcher's instruction points at, and they need the researcher's judgement on intent (is
`Session_Clusters` superseded by `Sessions-v2` and archivable outright? are the two
`verse-analysis` trees serving different purposes or is one stale?) that a file census alone cannot
answer.
