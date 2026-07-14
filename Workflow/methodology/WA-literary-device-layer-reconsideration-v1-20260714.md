# WA — The literary-device layer: reconsidering how meaning-enriching devices are captured (v1, 2026-07-14)

- **Date:** 2026-07-14
- **Trigger (researcher):** analogy/allegory are only two of a large family of meaning-enriching devices (metaphor, simile, symbolism, typology, parable, personification, paradox, hyperbole, litotes, irony, metonymy, parallelism, chiasm, motif, imagery, …). "Take this for further consideration."
- **Status:** design reconsideration — needs the researcher's steer on scope. Builds on the qualifier-model reconsideration (`WA-qualifier-model-reconsideration-analogy-and-rhetorical-typology-v1`).

## 1. The systematic finding — the reads PERCEIVE devices but RECORD none as structure
The analogy gap is not analogy-specific. Searching the `reading`(114) prose of the two re-read books, the reads are **saturated with device-language that is never captured as queryable data**:

| device-language in the reading prose | readings | structural capture today |
|---|--:|---|
| **imagery / image** | **3,261** | none — the reads think in images throughout |
| personification / personified | 101 | none (73 chars have Wisdom/Folly as bearer) |
| antithesis / contrast | 60 | ◑ partial via `coupling` "set against" |
| simile / like… | 59 | ✗ vehicle `standalone` |
| irony / ironic | 21 | none |
| emphatic / doubled (intensity/hyperbole) | 13 | ✗ dropped to standalone |
| metaphor | 9 | none |
| paradox | 8 | none |
| litotes / understatement | 2 | ✗ (e.g. 24:23 "not good" read in prose) |

**The device is *read* — it is right there in the prose ("personified", "the image of", "ironic", "the paradox") — but it is not *recorded*.** So an analyst cannot ask "which characteristics are taught by metaphor vs literally? where is personification used? what are the paradoxes of the inner life? how does the imagery cluster?" This is the same gap as analogy, generalised across the whole family.

## 2. Organise the family by GRAIN — because they do not all attach to a characteristic
The devices operate at three different levels; capturing them means three different homes:

- **A. Per-characteristic (the DEVICE MODE of a reading)** — *how this characteristic is expressed:* `literal · metaphor · simile · analogy · personification · paradox · hyperbole · litotes · metonymy · synecdoche · irony · symbolism · typology`. A tag (multi-valued) on the reading; for the comparison devices it also carries a **typed edge** to the vehicle (from the qualifier model).
- **B. Per-passage (STRUCTURAL form)** — *the shape of the unit:* `parallelism (synonymous / antithetic / synthetic) · chiasm · repetition · parable · allegory`. **Parallelism is the master device of Hebrew poetry** — and antithetic parallelism is exactly the antithesis the reads half-capture via `coupling`. A passage-level tag, not per-char.
- **C. Corpus (CROSS-reading)** — *patterns across the book/canon:* `motif (light/darkness…) · archetype · allusion · typology(cross-corpus)`. A cross-reading layer over the whole projection.

## 3. Relevance filter — capture what serves the study's OBJECT (inner-being movements), not all 25
Not every device is load-bearing for reading the inner being. Recommended tiers:

- **Load-bearing (capture):** metaphor, simile, analogy, personification, paradox, litotes, metonymy, hyperbole (per-char); parallelism-type + chiasm (per-passage); motif + typology (corpus). These *shape how an inner-being truth means* — "the fear of the LORD is a **fountain** of life" (metaphor), "**Wisdom cries out**" (personification), "whoever **loses** his life will **find** it" (paradox).
- **Secondary (tag if cheap):** irony, symbolism, synecdoche, allusion, archetype, repetition.
- **Low relevance here (skip):** fable, myth, oxymoron, emblem — rare in Psalms/Proverbs per-char inner-being reading.

## 4. The proposed model — a `device` layer integrated with the qualifier-typing
1. **`device` dimension** on each reading — a controlled, multi-valued vocabulary (tier-A list), with **`literal`** as the honest default (assessed, not blank — same anti-`ABSENT` principle).
2. **Typed edges** for the devices that have a counterpart span — `analogy/simile/metaphor` → the **vehicle**; `antithesis` → the opposing pole; `metonymy` → the stood-for. (This *is* the qualifier-typing layer; device-tag and typed-edge are two facets of one enrichment.)
3. **Passage-level device tags** (parallelism-type, chiasm) on the passage/segment.
4. **Corpus device layer** — motif/archetype/allusion as cross-reading annotations over the projection.

The projection then gains: a `device` column (reading_view); `edge_type ∈ {…, analogy, antithesis, metonymy}` (edges); passage `parallelism_type`; a motif index. Vehicles become first-class nodes.

## 5. Feasibility — much is bootstrappable, because the prose already names it
- **Mechanical first-pass** (like `translit`): the reading prose already contains "personified / simile / metaphor / paradox / ironic / image" — extract a provisional `device` tag from it, then confirm by reading. Signals: simile = `like`/`as…so`; personification = non-human bearer (Wisdom/Folly/an object) + human verb; litotes = `not` + positive; parallelism = the poetic line-pair; antithesis = `but`.
- **Reading judgment** for metaphor, paradox, symbolism, typology (no clean signal).
So the retrofit is a **device-typing pass** seeded from the existing prose — not a re-read.

## 6. Scope decision (researcher to steer) — integrated with the qualifier scope
| option | what it adds | effort |
|---|---|---|
| **D1** | per-char `device` tag (load-bearing list) + analogy/antithesis edges + the modifying trio | bounded — the highest-value structure; provable on 1 chapter each |
| **D2** | D1 + passage parallelism/chiasm tags | + the poetic backbone |
| **D3** | D2 + corpus motif/typology/allusion layer | the full literary map |

Each applies to **Psalms + Proverbs (retrofit) AND future reads (bake-in)**. This subsumes the earlier qualifier scope (S1/S2): the modifying + relational + rhetorical + device work is **one integrated enrichment — "record the structure of how each characteristic means."**

**Recommendation:** **D1 now** — it captures the meaning-bearing devices (metaphor/simile/analogy/personification/paradox/litotes/metonymy) + their edges + intensity/specifier/effect, is bounded and provable, and delivers the biggest analytical gain (imagery, personification, paradox become queryable). Add D2 (parallelism) next — it is the poetic backbone and cheap to detect. D3 (corpus motifs) is a later, standalone cross-reading pass.

**One caution worth stating:** device-tagging is interpretive. To stay evidence-bound, each tag should point at its trigger (the vehicle span, the connective, the parallel line) and default to `literal` — so a `device` is always *shown from the text*, never asserted. That keeps this consistent with the study's rule that meaning is read off the verse, not imported.
