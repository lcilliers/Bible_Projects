# Plan for approval — (b) characteristic-table restructure + (c) integrity fixes

> **Nothing here is executed yet.** These are destructive (schema change, table clear-out, master-index repair) and turn on design choices the researcher only *suggested* ("amongst others"), so they need sign-off. Grounded in queries run 2026-07-11.

## First, an ambiguity to resolve: there are TWO characteristic tables
| table | rows | fits new approach? | dependents (inbound FK) |
|---|--:|---|---|
| `characteristic` | 277 | M-code cluster model (Exultation, Joy…); legacy | **YES — `characteristic_subgroup`, `cluster_observation`, `cluster_finding`** (clearing it orphans these) |
| `ib_characteristic` | 29 | "IB characteristic registry" (trust-refuge, fear-of-the-lord…); built 2026-07-03, pre-reread | **none** (safe to restructure) |

**Recommendation:** build the new "defined characteristic" on **`ib_characteristic`** (dependent-free, already the IB concept). Leave `characteristic` (M-code) untouched as legacy — clearing it would require first disposing of its 3 dependent tables, which is separate work. *(Confirm, or say if by "the characteristic table" you meant the M-code one.)*

## (b) Proposed structure for the defined-characteristic table
Each **row = one defined characteristic** (the recurring inner-being movement); the 2,168 span-instances link *into* it.

Columns (your three + the "amongst others"):
- **`ledger`** — the full description of the characteristic (its defining text: what it is, its colour-range/variants, its junctions). *(your a)*
- **`key_span_id`** + **`key_word`** — the anchoring representative span (FK → `verse_span_index.id`) and its word/Strong's. *(your b)*
- **`operation`** — the characteristic's core operation/movement. *(your c)*
- amongst others: `id`, `code`, `name`, `status`, `provenance`, `notes`, `created_at`, `updated_at`.

**Instance → characteristic linkage** (to satisfy integrity invariant **I7**): add **`verse_span_index.characteristic_id`** (FK → the defined-characteristic row). Each of the 2,168 char-spans gets its `characteristic_id` set when it is grouped. *(Alternative: a `char_span_link` junction table if a span can express >1 characteristic — say which you prefer.)*

**Clear-out (preserve first):** export the 29 current `ib_characteristic` rows to a legacy archive (a `_legacy` table or a JSON export) **before** clearing, so the old-read registry isn't lost. Then clear + restructure. *(Confirm.)*

## (c) Integrity fixes — the three gaps, with method
| gap | count | proposed fix | note |
|---|--:|---|---|
| **I2** master-index orphans | 261 | **Engine onboarding (per-book method step d), NOT a bypass INSERT** — memory records a prior Gate-1 bypass was **REJECTED**. Run the proper STEP/engine path so term + verses + links are built. | biggest piece; needs the engine + STEP; all 261 have a `verse_id`, so they trace to a verse already |
| **I4** passage-less spans | 18 | assign `passage_id` per the passage rule (step b rework) across 13 chapters | small, mechanical |
| **I7** unlinked instances | 2,168 | **a distinct analytical phase** — grouping the 2,168 instances into defined characteristics — done *after* (b) creates the table + link column | this is substantial (it is essentially the "findings"/definition work), not a quick fix |

## Sequence I propose (on approval)
1. **(b)** restructure `ib_characteristic` (export-then-clear + new columns) + add `verse_span_index.characteristic_id`. Integrity-gated (DB snapshot pre/post).
2. **(c) I4** — assign the 18 passages.
3. **(c) I2** — the 261 via engine onboarding (step d). *This may be its own working session given the engine/STEP dependency.*
4. Finalise integrity invariant **I7** in the definition doc (make it enforceable) once the table + link exist.
5. **I7 linkage** (grouping 2,168 → defined characteristics) — the next major phase, separate.

## Decisions I need before executing anything
1. Use **`ib_characteristic`** for the new structure (leave M-code `characteristic` as legacy)? Or did you mean the M-code table?
2. The columns above — confirmed / adjust?
3. Instance link = a **`characteristic_id` column on the span**, or a **junction table**?
4. Clear-out: export-then-clear the 29 old rows — OK?
5. The 261 orphans via **engine onboarding (step d)** — confirmed (no bypass)?

*Filed 2026-07-11. Awaiting sign-off; no DB mutation performed.*
