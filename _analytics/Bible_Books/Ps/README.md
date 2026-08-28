# Psalms — folder index & navigation map

> **The DB is the corpus.** Every reading lives in `database/bible_research.db`; the files here are governance records, regenerable views, or build provenance. If a file and the DB disagree, the DB wins.

## 📁 Folder map (where everything lives)

| subfolder | what's in it | regenerate with |
|---|---|---|
| **`_reread/`** | the corrected char-arc **re-read** process docs — baseline, snapshots v1–v6, discipline audit, intervention/pilot plans, the Screen-0 correction | — (governance records) |
| **`_base-sources/`** | the **47 per-family base-source JSONs** (+ `INDEX.md`) — complete lexical evidence per family for analysis | `scripts/_produce_family_base_source_json_20260711.py` |
| **`_lineage/`** | per-family **lineage JSONs** — the raw DB chain `ib_char → ve_lexical → passage` with FK documentation | `scripts/_produce_family_lineage_json_20260712.py --family <slug>` |
| **`_family-analyses/`** | the **47 in-depth family analyses** (+ `INDEX.md`) — source-only, cited, one per base source | subagents per `Workflow/methodology/wa-psalms-family-analysis-method-v1-20260711.md` |
| **`_model/`** | the **`ib_characteristic` model** work — table analysis, family grouping, family-vs-cluster comparison, grounded-state, restructure plan, 261-orphan evidence, investigations, + reversibility JSON exports | `scripts/_apply_ib_char_*`, `_produce_family_cluster_comparison_*` |
| **`readings/`** | *(superseded)* the 150 Phase-2 whole-chapter readings (`prose_section` id 104) | `scripts/_export_prose_to_md_v1_20260703.py` |
| **`phase1-views/`** | *(superseded)* Phase-1 lexical inspection dumps of the *old* `ve_lexical` | `scripts/_export_prose_to_md_v1_20260703.py` |
| **`_archive/`** | build provenance (per-psalm builder + role JSONs the read was applied from) — safe to delete | — |

**Method/governance docs are NOT here** (per file-organisation-rules §3.0b) — they live in `Workflow/Instructions/` and `Workflow/methodology/`.

---

## ★ Current authoritative state — the corrected char-arc re-read (2026-07-11)

**All 150 psalms have been re-read by char-arc under the corrected method, and are gate-clean.** This is the live Psalms analysis. It lives in the DB as `ve_lexical` rows stamped `source_provenance='reread-psalms-2026'` with `verse_span_index.role_provenance='read-2026'`.

- **Method (repeatable):** [`Workflow/Instructions/wa-corrected-charac-arc-reread-repeatable-process-v1-20260711.md`](../../Workflow/Instructions/wa-corrected-charac-arc-reread-repeatable-process-v1-20260711.md).
- **Lens correction:** [`_reread/wa-ib-relevance-screen-correction-20260709.md`](_reread/wa-ib-relevance-screen-correction-20260709.md) — Screen 0 (God-content → qualifier; human IB → characteristic).
- **Final state:** [`_reread/wa-psalms-reread-snapshot-v6-FINAL-20260711.md`](_reread/wa-psalms-reread-snapshot-v6-FINAL-20260711.md) — 150/150, every content gate at zero.

### Re-read progress trail (in `_reread/`)
`wa-psalms-reread-baseline-20260709` → `-snapshot-20260710` (51/150) → `-v2/-v3/-v4` (Book II/III/IV) → `-v5` (150/150) → `-v6-FINAL` (Book I remediated). Plus `-discipline-audit-20260710` and the planning/pilot docs (`wa-psalms-intervention-plan`, `wa-psalm-004-pilot-delta`, `wa-psalms-pilots-validation-and-scale`, `wa-reread-automation-worklist-design`).

## The `ib_characteristic` model layer (in `_model/`) — built 2026-07-11
On top of the read: the master char-spans were rolled into a **meaning-keyed `ib_characteristic` index** (877 records), grouped into **46 families**, and assigned **term-based clusters**. Key docs:
- `wa-ib-characteristic-table-analysis-20260711.md` — the index analysed
- `wa-ib-characteristic-family-grouping-20260711.md` — the 46 families
- `wa-ib-char-family-vs-cluster-comparison-20260711.md` — the two-lens cross-check
- `wa-psalms-characteristic-model-grounded-state-20260711.md` · `wa-psalms-db-integrity-grounded-state-20260711.md` — grounded state
- reversibility exports: `ib_characteristic_v2_book19_pre_v3rebuild_*.json`, `ib_characteristic_legacy_29_export_*.json`, `ib_char_877_meanings_for_family_*.json`, `char-seed-extension-read-emergent-19_*.json`

## The base-source analysis sweep (in `_base-sources/`, `_lineage/`, `_family-analyses/`) — 2026-07-11/12
Each family got a self-describing **base source** (`_base-sources/`), a **lineage view** (`_lineage/`), and an **in-depth analysis** (`_family-analyses/`). Start at [`_family-analyses/wa-family-analyses-INDEX-20260711.md`](_family-analyses/wa-family-analyses-INDEX-20260711.md) and [`_base-sources/INDEX.md`](_base-sources/INDEX.md).

## Cross-cutting outputs (in `../_reports/`, DB-canonical)
Psalter syntheses (`prose_section` id 580/581) + harvest grid — built on the **old** read; to be regenerated from the corrected read in the findings/narrative phase.
