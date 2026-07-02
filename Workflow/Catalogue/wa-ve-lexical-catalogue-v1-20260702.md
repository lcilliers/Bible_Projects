# VE-lexical catalogue — v1 (the authoritative item list, 2026-07-02)

> **Supersedes** the tier catalogue (`wa-IB-verse-dimensions-catalogue-v2`) and the item framing of `01b-VE-field-reliability-and-rules` for the **verse-first / pair-model** lexical. The bedrock mechanics of 01b (measure layer, sense, mode) are retained. This is the live catalogue for the new model.

## 0. The model in one paragraph
The lexical is **verse-first**: a verse yields a **list of terms** (each with a full per-term lexical) **plus verse-level items** (not per-term). Each term is described across the **dimensions** below; a dimension value is a **PAIR** (`element1 → element2`, semantic direction, with a `resolution`), an **EVENT** (a predicate/chain), or a **FLAG**. The unit of work is a **passage** (a maximal run of consecutive verses); the lexical is derived on the passage's **first verse** (anchor) and spans all its terms. Processing is **term-driven** (an owner term's anchor first, then all its verses), **genre-aware**, **self-checking** (read-back → D11 notes on uncertainty), and marked complete on `verse.process_marker`.

## 1. Resolution states (every pair value)
`span` (element1 is an actual span) · `inferred` (deduced, not in the verse) · `unknown` (a value is expected but undeterminable — the worklist) · `none/silent` (the verse genuinely has none — never impute).

## 2. Per-term items (keyed on `verse_context`; stored in `ve_lexical`)
| dim | item | shape | definition | current rule (status) | converges legacy |
|---|---|---|---|---|---|
| **D1** | **sense** | value | the per-occurrence sense (STEP subgloss) | ✅ reliable | `sense`(1) |
| **D1** | **type** | value | action / status / quality (from POS) | ✅ reliable | `type`(2) |
| **D4** | **operation** | EVENT | the governing predicate — the act; for a manner-noun, the verb it qualifies | ✅ reliable | `how`(18) + `operation`(27) |
| **D2** | **source** | PAIR | driver/antecedent → term (span/inferred/unknown) | ⚠ **must distinguish DRIVER vs RESTRAINT** (else D11 role-uncertain) | `cause`(17) + `cause_clause`(22) + `from-source`(23) |
| **D3** | **seat** | PAIR | constitutional seat (heart/soul/spirit…) → term, via construct chain | ✅ reliable (construct-gated, not verse-wide) | `location`(5) |
| **D3** | **bearer** | PAIR | who bears it (experiencer/subject) → term | ❌ not yet derived (gap) | `experiencer`(20) |
| **D5** | **target** | PAIR | term → object (+ **object-type** person/God/group/thing/abstract/spiritual-being) | ⚠ partial (HTo object-marker; Hebrew word-order) | `object`+`object-type`(16) |
| **D6** | **manner** | PAIR | qualifier span → term (prep-marked adverbial); + **intensity** (me'od/kol) | ✅ reliable | `intensity`(19) + `compound`-qualifier(3) |
| **D8** | **effect** | PAIR | term → produced-state (a Piel/Hiphil result verb, adjacent, prose only) | ✅ narrative / ⚠ poetry | `immediate-response`(11) + produces-effect |
| **D9** | **coupling** | PAIR | the **morphological weld** only (construct/preposition binding to a co-term) — NOT every co-occurrence | ✅ reliable (no explosion) | `compound`(3) role |
| **D10** | **prohibition** | FLAG | a **mechanical** negation/prohibition particle on the term (moral framing) | ⚠ proximity-based | (valence remnant) |

## 3. Verse-level items (NOT per-term)
| dim | item | home | definition |
|---|---|---|---|
| **D14** | **passage** | `verse.passage_id` + `passage` table | the consecutive-run membership; anchor = first verse (`is_passage_anchor`) |
| **(new)** | **genre** | `verse.genre` | law/narrative · narrative · poetic/wisdom · prophetic · gospel-narrative · epistle — **feeds the passage treatment** |
| **D7** | **process** | passage-level | the escalation chain of the passage's affect/vice operations (prose narrative only) |
| **D11** | **discovery** | `ve_lexical` note (`discovery`(29)) | the **uncertainty / discovery notes channel** — when unsure, write here; also the span-completeness lookout |

## 4. Dropped (researcher decisions)
- **D10 valence** — DROPPED (was 99.3% AI-interpreted `valence_read_api`, all soft-deleted). Keep only the **mechanical prohibition** signal (above).
- **D12 hidden meaning** — DROPPED (not lexical-level).
- **D13 cohabitation** — DROPPED (implicit in the multi-term-in-verse principle — a verse already holds its co-terms).
- **related_tier (T0–T7)** — DEPRECATED (superseded tier scheme; 372,884 values retained for provenance, not used going forward).

## 5. Storage (schema 3.35.0)
- **Per-term values:** `ve_lexical` (`verse_context_id · ve_nr · ve_label · value · notes · source_provenance`) **+ the pair columns** `from_span · to_span · direction · resolution · pair_kind`.
- **Verse-level:** `verse.passage_id · is_passage_anchor · process_marker · genre`; `passage` table.
- **Measure layer (source of all derivation):** `verse_morphology` (spans) · `lexicon` · `verse`.

## 6. Pending (not yet built — need the finalised derivation)
- Physically **converge** the legacy items (col. "converges legacy") into the new pair items, with a per-pair convergence rule + old↔new result-parity check.
- **Convert `ib_observation`** (81 rows) into this shape, then **retire** the table.
- Allocate final `ve_nr`s for the new items (`process`, `genre`) — keep old numbers, add new (researcher).
- **Bearer (D3)** derivation; **source** driver/restraint split; **target** word-order; the **AFFECT/VICE cluster set** (seed) to firm.

## 7. Legacy handling (researcher, 2026-07-02)
Legacy is **left in place, not migrated, not retired** — cleaned up only after the verse analysis is done. It is **filterable / ignorable** now:
- **New-model `ve_lexical` rows** carry the pair columns (`pair_kind` / `resolution` NOT NULL) + a new-model `source_provenance` tag → reports select the new model by `pair_kind IS NOT NULL`; **legacy = the rest** (`v2_engine_iter1`, `*_read_api`, etc.).
- **`ib_observation`** is **completely ignored** — never joined in reports; converted nowhere; removed later with the rest of the redundant material.
