# VE / lexical analysis — index (start here)

> The verse-extraction (VE) field work. **Reorganised 2026-06-18** into three classes: **instructions** (canonical, now in `Workflow/Instructions/`), **methodology findings** (`findings/`), and **exploratory/working** (`exploratory/`). Live state: schema **3.34.0**; VE field VALUES live in **`ve_lexical`** (mechanical `v2_engine_iter1` + read-resolved `*_read_api`); `finding` = real findings only. Corpus reads complete (location/cause/object-type/divine); **valence parked** for next-cluster eval.

---

## ★ Instructions — CANONICAL (binding) → `Workflow/Instructions/`
These govern generation; they were moved out of research into the programme instruction set.

| file | what it is |
|---|---|
| [01b — VE-field-reliability-and-rules](../../Workflow/Instructions/01b-VE-field-reliability-and-rules.md) | **The canonical VE generation spec.** Governing principles (mechanical-only, original-language-grounded, whole-verse-reset), the measure layer, the full item catalogue + rules, conflict register (C-1…C-6), validation notes (valence/divine/zero-pad fixes). |
| [01c — T2 treatment & API governance](../../Workflow/Instructions/01c-T2-treatment-and-API-governance.md) | **Binding:** T2 content/grammatical split + treatment in generation/JSON/reads; API governance (batched-by-verse, circuit-breaker, cost-cap, self-verify, residue-only). |

## Methodology findings → `findings/`
Settled design, model, mapping and audit results.

| file | what it is |
|---|---|
| [02 — what-is-in-the-database](findings/02-what-is-in-the-database.md) | the record-set model: unit = term-in-verse; columns vs findings. |
| [03 — data-model-redesign](findings/03-data-model-redesign.md) | the normalisation: `verse_context` + `ve_lexical`; finding = real-only. |
| [04 — verse-schema-current](findings/04-verse-schema-current.md) | the verse-related schema (tables/columns/FKs). |
| [05 — sense-operation](findings/05-sense-operation.md) | how sense works: subgloss floor; straight-through vs complex. |
| [06 — migration-to-ve-lexical](findings/06-migration-to-ve-lexical.md) | the VE→ve_lexical migration record. |
| [10 — catalogue-to-14-points](findings/10-catalogue-to-14-points.md) | catalogue questions ↔ the 14 VE points. |
| [11 — tier-catalogue-v3](findings/11-tier-catalogue-v3.md) | restructured T0–T7 tier catalogue (question-led). *(canonical tier docs live in `Workflow/Tiers/`)* |
| [12 — catalogue-extensions](findings/12-catalogue-extensions.md) | word-extension questions: coverage vs tiers + supersession. |
| [13 — catalogue-refit-principles](findings/13-catalogue-refit-principles.md) | the four governing refit principles. |
| [wa-ve-engine-compliance-audit-v1](findings/wa-ve-engine-compliance-audit-v1-20260617.md) | engine vs 01b spec — the compliance matrix. |
| [wa-ve-full-audit](findings/wa-ve-full-audit-20260617.md) | complete VE/engine/reads audit (integrity, coverage, outstanding items). |
| [wa-compound-and-cause-analysis](findings/wa-compound-and-cause-analysis-20260616.md) | compound + cause design analysis. |
| [wa-ve-templated-narration-first](findings/wa-ve-templated-narration-first-20260615.md) | the deterministic narration view (01b §1f). |

## Exploratory / working → `exploratory/`
Reviews, dumps, logs, registers, test-runs, dry-runs — transient process artefacts.

| file | what it is |
|---|---|
| [07 — sense-faculty-rerun-REVIEW](exploratory/07-sense-faculty-rerun-REVIEW.md) | sense/faculty rerun review. |
| [08 — working-set-50-verses](exploratory/08-working-set-50-verses.md) | 50 complex verses; signal-list seeds. |
| [09 — mode-field-visual](exploratory/09-mode-field-visual.md) | what the mode field looks like, by language. |
| [wa-ve-engine-v2-testrun](exploratory/wa-ve-engine-v2-testrun-20260616.md) · [wa-ve-rebuild-dryrun-review](exploratory/wa-ve-rebuild-dryrun-review-20260615.md) | engine test-run / dry-run reviews. |
| [wa-ve-corrective-actions-analysis](exploratory/wa-ve-corrective-actions-analysis-20260615.md) · [wa-ve-iteration2-action-register](exploratory/wa-ve-iteration2-action-register-20260615.md) · [wa-ve-narration-feedback-vc1630](exploratory/wa-ve-narration-feedback-vc1630-20260615.md) | iteration-2 review work-list, living register, worked example. |
| [wa-ve-corpus-rollout-plan-v1](exploratory/wa-ve-corpus-rollout-plan-v1-20260617.md) · [wa-autonomous-session-log](exploratory/wa-autonomous-session-log-20260617.md) | rollout plan (paused) + autonomous session log. |
| [wa-verse-records-status-by-cluster](exploratory/wa-verse-records-status-by-cluster-20260615.md) | per-cluster lexical/meaning status snapshot. |
| `wa-raw-dump-*-M01-M23-M46-*` (3) | raw verse-report + ve_lexical + narration dumps (cross-cluster). |

## Archive
- [`archive/01-THE-VE-DESIGN-spec-lists-rules.md`](archive/01-THE-VE-DESIGN-spec-lists-rules.md) — empty stub, superseded by 01b.

## Related (left in their integrity context)
- `research/investigations/` — XREF/verse-duplication, mode/language consistency checks, sense disambiguation.
- Per-cluster outputs live under `Sessions-v2/{CODE}-{Name}/` (Data/ + Analysis/).
