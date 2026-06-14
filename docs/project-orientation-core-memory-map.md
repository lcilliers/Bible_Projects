# Project Orientation — Core Memory Map

> **Start here every session.** This is the map of the guides and documents that direct continued work on this project. **CLAUDE.md is the core entry point; from there it fans out** (instructions → current-truth reconstruction → open-items → memory). Created 2026-06-14.
>
> ⚠ **Standing caveat:** CLAUDE.md (last refresh 2026-04-27) is currently **drift-stale** on schema version and architecture. It says schema v3.11/3.17 — the live DB is **3.31.0** — and it omits the finding-centric model. Until CLAUDE.md is refreshed, treat the **2026-06-14 reconstruction (Tier 2)** as the corrected current truth.

---

## How to orient (the routine)

1. **CLAUDE.md** loads automatically — compact reference: directory map, schema groups, engine, conventions, common operations. Read it for *structure and conventions*, but verify *schema/architecture/state* against Tier 2.
2. **Read this map.**
3. **Read the reconstruction (Tier 2)** for the true current state, the failure history, table relevancy, and what is still open.
4. **Resolve `[current]` cross-references** (GR-REF-002): an instruction cited as `[current]` means the highest-numbered version in `Workflow/Instructions/`.
5. **Scan memory** (`MEMORY.md` index) — note the governing entries flagged below.
6. **Establish any new facts from the written record, not the DB** — drive from `database/file_manifest.json` (rebuild with `scripts/build_file_manifest.py`), read dated docs in ascending order, cite sources, never reconstruct state from row counts. (memory: `feedback_source_of_truth_is_written_record`)

---

## The fan-out

### Tier 0 — Entry point
| Doc | Role | Status |
|---|---|---|
| `CLAUDE.md` | Compact project reference (loaded every session): directory map, schema v-groups, engine modes, script conventions, data flow, common ops, controlled vocab | ⚠ **drift-stale** on schema/architecture; refresh pending (approved Plan B) |

### Tier 1 — Governing instructions (`Workflow/Instructions/`, resolve `[current]`)
**Programme governance & reference**
- `wa-claudecode-instruction` — Claude Code responsibilities (patch/directive execution, VC batch ops, extracts)
- `wa-patch-instruction` — patch ops, REPAIR catalogue, failure protocol, validation
- `wa-directive-instruction` — directive spec
- `wa-global-general-rules`, `wa-global-flags` — programme governance + standalone flags
- `wa-reference` — controlled vocabulary, schema reference, file naming, validation standard
- `wa-registry-management-guide` — registry structure, OWNER/XREF, dual status, clusters, pools

**The LIVE analytical model (cluster / finding / verse-read — June 2026)**
- `wa-cluster-rollup-design.md` — **authoritative L1–L8 design** the live pipeline is built from
- `wa-cluster-rollup-instruction-v3_2-DRAFT-…` — the procedural instruction (**DRAFT; not finalised** — open item B3)
- `wa-verse-analysis-methodology.md` — span-focal verse analysis (**v4 DRAFT**)
- `wa-tier-catalogue-restructured-v2-…` — two-layer **VE (verse-extraction) + SYNTH** catalogue (approved; **DB not yet modified**)
- `wa-study-foundations.md` — the re-grounded study definition (focus, raw-data completeness, analysis rules, end point)
- `wa-cluster-audit-design-v1-…` — per-level compliance audit (L1 specified; L2–L8 stubbed)

**Earlier-stage instructions (still referenced; some superseded — see 04 §4)**
- `wa-versecontext-instruction`, `wa-sessionb-cluster-instruction-v3_0` *(superseded by v3_2)*, `wa-sessiond-orientation`, `wa-dimensionreview-instruction` *(dimension review eliminated 2026-05-04)*, `wa-word-study-template`

**Filing / file-organisation governance** (where files go, how they're named/versioned/archived)
- **`docs/file-organisation-rules.md`** — the governing filing doc: naming conventions (§2), **snapshot vs living-document versioning** (§2.3 / §2.3a — living docs carry no `-vN`, version in metadata + git), folder rules (§3, incl. §3.0 `Sessions-v2/` = home for all new cluster output), archiving (§4), CC obligations (§5), the manifest (§6)
- `Workflow/Global_rules/wa-global-rules-all-v2-…` — the **GR-FILE-*** rules (+ GR-PROC/GR-OBS governance)
- `wa-reference` `[current]` — file-naming patterns + labels; and the **DB-resident pattern registries** `wa_file_name_pattern` / `wa_label_pattern` / `wa_patch_type_registry` (M34)
- `database/file_manifest.json` (+ `scripts/build_file_manifest.py`) — the whole-tree index with a `currency` signal; **the reliable way to locate files** (folders alone are not reliable)
- ⚠ **The filing guidance is itself partly drifted from the restructured layout** (verified 2026-06-14): §3.9 `data/schema/` is gone (schema now at `Workflow/schema/`); a top-level `data/` exists but is absent from CLAUDE.md §2; exports have two homes (`Sessions/Session_A/STEP Extracts` and `data/exports`). **A filing audit (reconcile rules ↔ actual layout) is an open item** — see 02 and 04.

### Tier 2 — Current truth baseline (the 2026-06-14 reconstruction)
`outputs/markdown/project-reconstruction/`
| File | What it gives |
|---|---|
| `00-spine-index-ascending-…` | the 523-doc dated reading list (the narrative spine) |
| `01-project-status-reconstruction-…` | true status oldest→newest + current-state table + what's incomplete |
| `02-failures-oversights-rework-log-…` | ~55 cited failures/reworks + digested implications (two roots) |
| `03-table-data-relevancy-map-…` | every table by usage/last-write into current/foundation/stale-relevant/dead/empty + 4 issues to ratify |
| `04-open-loops-and-incomplete-methodology-…` | open actions, DRAFT/awaiting-approval work, silent supersession |

### Tier 3 — Open-items / worklist
- `Workflow/Programme/Program_reports/wa-programme-open-items.md` — **living register, 127 items (§A–§Q)**. ⚠ dated 2026-06-01, predates the 06-03 DB loss + 06-04 reset — **confirm currency** before working it.
- `Workflow/wa-workflow-cleanup-register.md` + `wa-archive-decisions-for-guidance-v1-…` — filing/archiving decisions awaiting researcher markup.

### Tier 4 — Memory (`.claude` project memory; mirrored to `memory/` in git)
Governing entries to read first:
- `reference-core-memory-orientation-map` → points here
- `source-of-truth-is-written-record` → the method (this section's rule 6)
- `project_reconstruction_baseline_20260614` → the drift finding + reconstruction
- plus the live-direction set: `project_l2_verse_read_meaning_live`, `project_meaning_duplicates_then_fabricates`, `project_column_wise_ve_hypothesis`, `project_cluster_rework_phase_started`, `feedback_characteristic_is_typed_term_in_verse`, `feedback_ontology_typed_relationships`, `feedback_all_study_work_in_db`.

---

## Keeping this map true (governance)

- **CLAUDE.md is the entry point but drifted.** When CLAUDE.md and the reconstruction disagree on schema/architecture/state, the reconstruction wins until CLAUDE.md is refreshed.
- **Silent supersession is a known hazard.** ~12 documents are replaced without a marker (04 §4). Before trusting an older doc, check it isn't superseded. Recommended fix: a one-line `> SUPERSEDED (date) by <doc>` header on replaced docs, or a DB-resident supersession ledger.
- **Method discipline:** establish truth from the written record via the manifest (ascending), cite every claim, treat DB row-counts as evidence not verdict, flag silences as open questions — never guess.
- **The drift root** (02 implications): over-structuring an integrated subject + decision↔artefact gap. The lasting fix is a single live "what is open / what is authoritative" surface, re-issued after each pivot — not more scattered docs.
