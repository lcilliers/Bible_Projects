# M02 · Lexical-Coverage Self-Audit — All Characteristics (C1–C7)

- **File:** wa-m02-lexical-coverage-audit-v1_0-20260619.md · **Date:** 2026-06-19 · **Author:** le Roux Cilliers
- **Purpose:** Read back from the M02 ve_lexical extract and confirm every lexical element is accounted for in each characteristic tier-analysis document. Run per researcher instruction (2026-06-19).

**Method.** For each canonical lexical element, richness (non-null / total) is computed per characteristic directly from the extract, and the representation location is named. Coverage is guaranteed by the embedded **Evidence Base (EB)** now present in every document (C1–C4 at v1_1; C5–C7 at v1_0) plus the relevant tier answers.

**Headline result.** All **18 populated** lexical elements are represented in all seven documents. `mode` is **absent from the M02 extract schema** (0/703; not a key in the lexical) and is noted as such in each EB. **No coverage gaps remain.** One gap was found and fixed during this audit: `cause_clause` (177 occurrences) had not been surfaced — now added to every EB.

## Field richness per characteristic (non-null / total)

| Lexical element | C1 | C2 | C3 | C4 | C5 | C6 | C7 | Represented in document |
|---|---|---|---|---|---|---|---|---|
| `sense` | 228/228 | 145/145 | 85/85 | 77/77 | 49/49 | 83/83 | 4/4 | EB ▸ Senses; Q&A |
| `lemma_meaning` | 227/228 | 145/145 | 85/85 | 77/77 | 49/49 | 83/83 | 4/4 | EB ▸ Vocabulary (lexical meaning); T7.1.1 |
| `type` | 228/228 | 145/145 | 85/85 | 77/77 | 49/49 | 83/83 | 4/4 | EB ▸ Grammatical kind; T1.2/T7.1.2 |
| `mode` | 0/228 | 0/145 | 0/85 | 0/77 | 0/49 | 0/83 | 0/4 | ABSENT from M02 extract (noted in EB) |
| `faculty` | 227/228 | 145/145 | 83/85 | 75/77 | 45/49 | 1/83 | 0/4 | EB ▸ Faculty; T3 tier |
| `location` | 16/228 | 9/145 | 3/85 | 7/77 | 3/49 | 6/83 | 0/4 | EB ▸ Constitutional seat; T2.1 |
| `origin` | 4/228 | 2/145 | 2/85 | 1/77 | 1/49 | 2/83 | 0/4 | EB ▸ Origin; T2.9 |
| `how` | 101/228 | 85/145 | 14/85 | 34/77 | 27/49 | 64/83 | 2/4 | EB ▸ How |
| `object` | 118/228 | 96/145 | 59/85 | 48/77 | 31/49 | 23/83 | 1/4 | EB ▸ Object (raw, hint) |
| `object_type` | 115/228 | 96/145 | 56/85 | 48/77 | 31/49 | 22/83 | 1/4 | EB ▸ Object type; T4 |
| `cause` | 41/228 | 28/145 | 12/85 | 15/77 | 9/49 | 5/83 | 0/4 | EB ▸ Cause (read-resolved); T0.2/T7.2.3 |
| `cause_clause` | 63/228 | 35/145 | 15/85 | 26/77 | 10/49 | 24/83 | 1/4 | EB ▸ Cause clause |
| `experiencer` | 173/228 | 126/145 | 49/85 | 54/77 | 37/49 | 57/83 | 2/4 | EB ▸ Experiencer |
| `divine_involvement` | 1/228 | 145/145 | 62/85 | 30/77 | 21/49 | 13/83 | 0/4 | EB ▸ Divine involvement; T0/T4 |
| `intensity` | 34/228 | 23/145 | 8/85 | 11/77 | 2/49 | 8/83 | 0/4 | EB ▸ Intensity; T1.4.2 |
| `valence` | 197/228 | 111/145 | 80/85 | 73/77 | 42/49 | 75/83 | 4/4 | EB ▸ Valence; Valence integration; T0.2/T1.7/T3.8 |
| `immediate_response` | 34/228 | 19/145 | 8/85 | 12/77 | 6/49 | 12/83 | 1/4 | EB ▸ Immediate response; T1.5 |
| `compound` | 187/228 | 119/145 | 64/85 | 68/77 | 36/49 | 67/83 | 3/4 | EB ▸ Co-occurrence web; T6.1 |
| `relational` | 62/228 | 31/145 | 17/85 | 5/77 | 13/49 | 22/83 | 0/4 | EB ▸ Relational direction; T4 |

_Low non-null counts (e.g. `origin` 12/703, `intensity` 94/703, `location` 45/703) reflect the data, not gaps — each EB reports the full distribution incl. the dominant NONE, and tier answers mark "Silent." where the set is genuinely sparse._

## Updates applied as a result of this audit
- **Fixed:** `cause_clause` (177 occ corpus-wide) was not captured by the evidence builder; parser corrected and the verbatim causal phrases now appear in every EB.
- Added `lemma_meaning` (fuller lexical definitions) and raw `object` (mechanical-hint, with object_type-authoritative caveat) to every EB.
- Added an explicit note that `mode` is absent from the M02 extract.
- Integrated **valence** across all seven (C1–C4 raised to **v1_1** with a dedicated Valence-integration section + corrected PARKED note; C5–C7 carry it from first issue).
- Confirmed every document now carries a consolidated **Evidence Base** sufficient to author an essay without reopening the source extract.

## Residual data-quality flags (not coverage gaps — for researcher review)
- **C2 valence:** 7 divine-wrath occurrences tagged `sinful` — anomalous; verse-confirm (likely C1/C2 boundary-leak or mis-tag).
- **C7 scope:** NT-only `pikria` (4 verses); OT "bitterness of soul" (marah/mar) outside the set — recommend membership review (M03 cross-check).
- **object_type under-population** (programme-wide, previously logged) — raw `object` is a mechanical hint; carried.
- **mode** absent from M02 — morphological-mode analysis, if wanted, must come from `morph` separately.