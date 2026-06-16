# VE / lexical analysis — index (start here)

> The verse-extraction (VE) field work, filed in one place (2026-06-15). Read in number order; each file's old scattered name is noted for traceability. Live state: schema **3.33.0**; VE field VALUES live in **`ve_lexical`**, `finding` = real findings only.

## The model & design (read first)
| # | file | what it is |
|---|---|---|
| ~~01~~ | [THE-VE-DESIGN-spec-lists-rules](01-THE-VE-DESIGN-spec-lists-rules.md) | ⛔ **EMPTY / SUPERSEDED — do not use.** The canonical design+rules are in **01b** (below). Stub only. |
| **01b** | **[VE-field-reliability-and-rules](01b-VE-field-reliability-and-rules.md)** | **★ CANONICAL generation spec (v2 · 2026-06-16 — design SETTLED; Q1–Q14 + C-1…C-6 decided; remaining = list-building + build).** Part A = the mechanical rules: governing principles (mechanical-only, original-language-grounded, whole-verse-reset), the measure layer, full item catalogue (revised + new predicate-argument VEs), conflict register (C-1…C-6 decided 2026-06-16), §7 open questions Q1–Q14. Part B = the v1 reliability analysis (retained). *(was wa-l1l2-field-reliability-measures-v1)* |
| 13 | [catalogue-refit-principles](13-catalogue-refit-principles.md) | the four governing principles behind the refit (characteristic = typed-term-in-verse, etc.). *(was wa-catalogue-refit-two-layer)* |
| 02 | [what-is-in-the-database](02-what-is-in-the-database.md) | the record-set model: unit = term-in-verse; bedrock=columns vs interpretive=findings; why mode≠sense storage. *(was wa-finding-recordset-model-orientation)* |
| 03 | [data-model-redesign](03-data-model-redesign.md) | the normalisation: verse-level (`verse_context`) + items (`ve_lexical`); cardinality split; finding=real-only. *(was wa-ve-lexical-data-model-redesign)* |
| 04 | [verse-schema-current](04-verse-schema-current.md) | the actual CURRENT schema of all 17 verse-related tables (columns/types/FKs). *(was wa-verse-schema-current)* |

## Sense, mode & the build
| # | file | what it is |
|---|---|---|
| 05 | [sense-operation](05-sense-operation.md) | how sense works: subgloss floor, two-level (83% straight-through / 17% complex), span reliability. *(was wa-sense-operation-setup)* |
| 06 | [migration-to-ve-lexical](06-migration-to-ve-lexical.md) | the migration: 298k VE findings → 212k `ve_lexical` rows; the field→VE-nr map; finding cleaned. *(was wa-ve-lexical-migration-complete)* |
| 07 | **[sense-faculty-rerun-REVIEW](07-sense-faculty-rerun-REVIEW.md)** | **← REVIEW THIS** — sense fixed to subgloss; faculty re-derived against signal-lists (direct vs indirect); what to check. *(was wa-sense-faculty-rerun-for-review)* |
| 09 | [mode-field-visual](09-mode-field-visual.md) | what the mode (`morph_code`/`stem`) field looks like, by language. *(was wa-mode-field-visual)* |

## Catalogue ↔ VE mapping
| # | file | what it is |
|---|---|---|
| 10 | [catalogue-to-14-points](10-catalogue-to-14-points.md) | the catalogue questions mapped to the 14 VE points. *(was wa-catalogue-vs-L1L2-14-points)* |
| 11 | [tier-catalogue-v3](11-tier-catalogue-v3.md) | the restructured T0–T7 tier catalogue (question-led). *(was wa-tier-catalogue-restructured-v3)* |
| 12 | [catalogue-extensions](12-catalogue-extensions.md) | word-extension questions: coverage vs tiers + supersession. *(was wa-catalogue-extensions-coverage)* |

## Working data
| # | file | what it is |
|---|---|---|
| 08 | [working-set-50-verses](08-working-set-50-verses.md) | 50 complex multi-term/cluster verses; mode assessment; signal-list seeds. *(was wa-l1l2-50complex-verses)* |

## Current state of each VE (as of 2026-06-15 — POST WIPE + MECHANICAL REBUILD)
> The migrated value layer was judged corrupt and **wiped** (237,397 rows hard-deleted), then **rebuilt mechanically per 01b**. Scripts: `_apply_wipe_ve_lexical_v1.py` · `_apply_ve_rebuild_mechanical_v1.py` · `_produce_ve_narration_v1.py` · `_apply_persist_narration_finding_v1.py`.
- **Mode (#4)** = `morph_code`/`stem` **column** — done for ALL verses (not in ve_lexical).
- **VE 1,2,3,5,6,7,8,13 REBUILT** (`source_provenance='mechanical_v1'`): 247,899 rows over 40,739 units, strictly per 01b §1d. Attachment proxy = the term neighbourhood; doubt → `UNRESOLVED`. Faculty false-positives fixed.
- **Templated narration PERSISTED** as the single `l2_meaning` finding (30,571 M-cluster; old prose soft-deleted). Composer = deterministic view.
- **VE9/10/11/12/14** — read/deferred; not built.
- **ITERATION-2 review DONE (5 verses); CATEGORISED ANALYSIS READY** — researcher verdict: not one verse-lexical complete. **➤ Work-list: [wa-ve-corrective-actions-analysis-20260615.md](wa-ve-corrective-actions-analysis-20260615.md)** (error corrections · rule changes · VE extensions · new VEs + sequence + decisions). Running log: [wa-ve-iteration2-action-register-20260615.md](wa-ve-iteration2-action-register-20260615.md); first example [wa-ve-narration-feedback-vc1630-20260615.md](wa-ve-narration-feedback-vc1630-20260615.md). Meta-pattern: [[project_ve_proposition_gap]] — the pass captures the term, not the proposition.
- **Review/dump artefacts (today):** `wa-verse-records-status-by-cluster-20260615.md` · `wa-raw-dump-with-narration-M01-M23-M46-20260615.md` · `wa-ve-rebuild-dryrun-review-20260615.md` · `wa-ve-templated-narration-first-20260615.md`.

## Related — supporting foundation (left in their integrity context)
- Grounding/integrity that made this possible: [`research/investigations/wa-xref-verse-duplication-blocker-v1-20260615.md`](../investigations/wa-xref-verse-duplication-blocker-v1-20260615.md) · [`wa-mode-consistency-check-v1-20260615.md`](../investigations/wa-mode-consistency-check-v1-20260615.md) · [`wa-language-testament-consistency-check-v1-20260615.md`](../investigations/wa-language-testament-consistency-check-v1-20260615.md).
- Background sense investigations (older): `research/investigations/wa-step-morphology-sense-disambiguation-v1-20260607.md` · `wa-termsense-ranking-v1-20260609.md` · `sense-sampling-walkthrough-20260328.md`.
