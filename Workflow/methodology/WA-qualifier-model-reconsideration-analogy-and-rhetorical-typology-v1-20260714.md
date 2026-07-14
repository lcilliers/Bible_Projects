# WA — Reconsidering the qualifier model: the qualifier is a TYPED RELATIONSHIP (analogy, and the rhetorical typology)

- **Date:** 2026-07-14
- **Trigger (researcher):** "all qualifiers will not necessarily be captured in the three edges… I would not be surprised if we find we have underestimated the significance of the qualifiers. For instance: how did we surface analogy and allegory?"
- **Verdict:** confirmed and material. Below is the evidence, the fuller typology, and a proposed model. **This is a methodological reconsideration, not a backfill — it needs the researcher's steer on scope before execution.**

## 1. The finding — analogy is structurally lost, and it is not alone
Checked live: in **every** analogy the **vehicle is discarded as `standalone`** and the comparison survives only in the `reading` prose. There is **no analogy marker anywhere** in the ledger (`pair_kind ∈ {value,flag,event,pair,note}`; no "vehicle"/"simile"; no dimension for it).

| proverb | the characteristic | the vehicle (the meaning) | how it was stored |
|---|---|---|---|
| 26:14 | sluggard | door turning on its hinges | vehicle `standalone`; analogy in prose |
| 25:12 | wise reprover | a gold ring / ornament | vehicle `standalone`; analogy in prose |
| 27:8 | the man who strays | a bird strayed from its nest | vehicle `standalone`; analogy in prose |
| 26:11 | the fool who repeats folly | a dog returning to its vomit | vehicle `standalone`; analogy in prose |

The vehicle *is* the interpretation — and an analyst cannot query it: "which characteristics are taught by analogy? what imagery illuminates wisdom vs folly? how does the vehicle-set cluster?" — none of it is answerable from the structured data.

## 2. The fuller typology — qualifiers/connectives carry MANY typed relationships (both books, 2,136 read verses)
| relationship | verses | % | current capture |
|---|--:|--:|---|
| **analogy / simile** (like / as…so) | 104 | 5% | ✗ vehicle standalone; prose-only |
| **causation** (for/because/so-that) | 513 | 24% | ✗ mostly prose |
| **antithesis** (but) | 346 | 16% | ◑ partial via `coupling` "set against" |
| **condition** (if/lest/when) | 196 | 9% | ✗ mostly prose |
| **comparison** (better/than) | 54 | 2% | ◑ partial ("better" sometimes a char) |
| intensity / specifier / effect (modifying) | (per prior note) | — | ✗ dropped to standalone |
| relational (coupling/target/bearer/source/manner) | — | — | ✓ captured as pairs |

So the model captures the **relational** qualifiers (the movement graph) and the **antithesis** partially, but the **rhetorical/logical** layer — analogy, causation, condition, comparison — and the **modifying** layer (intensity/specifier/effect) are largely **not structural**. This is the underestimation.

## 3. The reframe — a qualifier is a **typed relationship**, not a standalone or a bare relational endpoint
Every span around a characteristic that *does something to how it means* is a **typed edge** from the characteristic:

- **relational:** `coupling · target · bearer · source · manner` (have these)
- **modifying:** `intensity · specifier · effect` (the prior fix)
- **rhetorical / logical:** `analogy(vehicle) · comparison · condition · causation · antithesis` (the new layer)

Each typed edge links the characteristic to its qualifying span (the vehicle, the condition, the cause…) and, where it carries a value (degree, the specifier text, the vehicle image), fills a dimension too. This is precisely the **relational web** the RESET method is after ("movements, associations, interlocking, emergence") — analogy and causation are *associations* the current data cannot express.

**Worked target (26:14):** characteristic `sluggard` —`analogy`→ vehicle `door/hinges` (image: "turns and turns, never rises"); the analogy becomes a queryable edge, the vehicle a first-class node, the imagery clusterable — instead of a sentence in a prose field.

## 4. Scope options (researcher to steer — this expands the read + retrofit)
- **S1 — analogy first (recommended start).** Add `edge_type=analogy` (vehicle→char) + the modifying trio (intensity/specifier/effect) already agreed. Highest value (104 analogies + the imagery), bounded.
- **S2 — analogy + the full rhetorical layer.** Also `causation / condition / comparison / antithesis` as typed edges. Richest (the whole logical scaffold, ~900+ verse-relationships) — but a larger read.
- **S3 — full reframe.** Treat *every* structurally-significant qualifier as a typed edge, corpus-wide, and make "qualifier-typing" a standing part of the per-char decomposition.

Each option applies **to Psalms + Proverbs (retrofit) AND bakes into future book reads** (per the standing instruction). The retrofit is a **qualifier-typing pass** (the spans exist; the read connects + types them) — not a full re-read.

## 5. Implications
- **Method:** the per-char decomposition gains a step — *"type each surrounding qualifier's relationship to the characteristic"* — updating the ve-lexical catalogue + ledger-lib + the edge model (`pair_kind`/`ve_label` or a new `edge_type`).
- **Projection:** the edge-list gains `edge_type ∈ {…relational…, intensity, specifier, effect, analogy, …}`; the reading_view gains the modifying-dimension columns; vehicles become nodes. Movement/imagery analysis becomes possible.
- **This may be the most consequential single enrichment** for the AI-analysis goal, because analogy + causation are how wisdom literature *argues*, and they are currently invisible to the data.

**Decision needed:** which scope (S1 / S2 / S3)? I recommend **S1 now** (analogy + the modifying trio — bounded, highest-value, provable on one chapter each), with S2 as the next increment once S1's typing rules are validated.
