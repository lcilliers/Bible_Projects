# VE / lexical analysis — index (start here)

> The verse-extraction (VE) field work, filed in one place (2026-06-15). Read in number order; each file's old scattered name is noted for traceability. Live state: schema **3.33.0**; VE field VALUES live in **`ve_lexical`**, `finding` = real findings only.

## The model & design (read first)
| # | file | what it is |
|---|---|---|
| **01** | **[THE-VE-DESIGN-spec-lists-rules](01-THE-VE-DESIGN-spec-lists-rules.md)** | **★ THE design doc** — the verse-level extraction record: every VE field with its **explicit option-list** + the **M/R (mechanical vs read) split** + which tier it feeds. This is where the VEs + lists + rules were created. *(was wa-verse-level-extraction-spec-v1)* |
| 01b | [VE-field-reliability-and-rules](01b-VE-field-reliability-and-rules.md) | the reliability elaboration on 01 — reliable measures, signal-lists, the list/rules/states table, faculty R1–R5. *(was wa-l1l2-field-reliability-measures-v1)* |
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

## Current state of each VE (as of 2026-06-15)
- **Mode (#4)** = `morph_code`/`stem` **column** — done for ALL verses.
- **Sense (VE1)** — re-derived to per-occurrence subgloss (analysed set; 725 UNRESOLVED).
- **Faculty (VE7)** — re-derived v1 against signal-lists (7,694 direct + 17,460 indirect = review).
- **Type (VE2)** — migrated as-is (bundles type + simple/compound; needs split + morph-derive).
- **VE3 compound, VE5 location, VE6 origin, VE8 attributed-God** — migrated as-is; mechanical/signal re-derive pending.
- **VE9 purpose, VE10 typology, VE11 response, VE12 produces** — the **read VEs** (free-text/interpretive); pending.
- **Coverage:** 30,103 of 41,657 units analysed; the ~2,333 M-cluster gap is M47-heavy; the rest (~9,215) is T2 (correctly not standalone-analysed).

## Related — supporting foundation (left in their integrity context)
- Grounding/integrity that made this possible: [`research/investigations/wa-xref-verse-duplication-blocker-v1-20260615.md`](../investigations/wa-xref-verse-duplication-blocker-v1-20260615.md) · [`wa-mode-consistency-check-v1-20260615.md`](../investigations/wa-mode-consistency-check-v1-20260615.md) · [`wa-language-testament-consistency-check-v1-20260615.md`](../investigations/wa-language-testament-consistency-check-v1-20260615.md).
- Background sense investigations (older): `research/investigations/wa-step-morphology-sense-disambiguation-v1-20260607.md` · `wa-termsense-ranking-v1-20260609.md` · `sense-sampling-walkthrough-20260328.md`.
