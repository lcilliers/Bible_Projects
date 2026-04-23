# wa-prose-draft-preamble-v1-20260421

> Framework B Soul Word Analysis Programme — Programme Prose Preamble (Draft)
> Session reference: prose
> Session date: 2026-04-21
> Previous output: wa-prose-framework-review-v1-20260421
> Governed by: wa-global-general-rules [current]
> Proposed home: new `prose_section_type` row — `prog_preamble` with `chapter_no = 0`, `sort_order = 0` (see §Placement decision below)

---

## Change Control — v1

| Change | Section |
|---|---|
| New document. First draft of the preamble prose for the programme-prose corpus, authored in response to researcher message 6 with starter text supplied. Three length variants produced — short, medium, long — for researcher selection. | All |

---

## Drafting notes — read first

Researcher message 6 provided a starter sentence and asked for a preamble paragraph to "set the tone and scope for the program prose section as a whole". The starter establishes: (a) the prose describes the whole programme — what it is, how it fits, how it unfolds; (b) the prose is *not* detailed instructions — those live elsewhere.

I have produced three length variants. Shortest is closest to the researcher's starter in feel — one paragraph, boundary-stating. Medium expands into a second paragraph that covers what the corpus specifically contains (linking to the six framework areas without naming them rigidly). Long adds a third paragraph on how the prose relates to the other authoritative layers (rules, schema).

All three variants honour the starter's opening — first sentence is preserved almost verbatim; second sentence keeps the researcher's boundary framing and sharpens the phrasing.

Confidence markers: since this is original composition from the framework and programme orientation — not from recall of existing wa-reference content — I am not using the [M] / [M?] / [GAP] system. Instead, each variant is fully authored from the framework review and Claude AI's orientation to the programme. Researcher review is the quality gate.

---

## Variant A — Short (one paragraph, ~100 words)

**Programme Prose — Preamble**

> The programme prose describes the entire research programme — what it is, how it fits together, and how it intends to unfold. It is not the place for detailed instructions on how to perform specific elements; those live in the instruction documents and in the global rules. The prose covers the programme's purpose and governing question, its research methodology and pipeline, the disciplines and tools it operates by, the shape of the data it produces, the governance that keeps that data correct, and the instruction corpus that binds the work. It is the programme's self-description, written so that a reader encountering it for the first time can understand what the programme is and what it is for.

---

## Variant B — Medium (two paragraphs, ~180 words)

**Programme Prose — Preamble**

> The programme prose describes the entire research programme — what it is, how it fits together, and how it intends to unfold. It is not the place for detailed instructions on how to perform specific elements; those live in the instruction documents and in the global rules, which are binding in ways the prose is not. The prose is descriptive: it tells the programme's own story.
>
> The corpus covers six broad areas: the programme's purpose and governing question; the research methodology and the pipeline through which work moves; the disciplines, tools, and evidential principles by which the programme operates; the shape of the data it produces and the architecture that holds it; the governance that keeps that data correct over time; and the instruction corpus that binds the work, together with the discipline of how instructions are versioned, referenced, and updated. Within each area, individual prose records describe specific components in enough detail that a reader can understand the component without reading its underlying rules, instructions, or schema — though those remain the authoritative sources when questions about binding or exact structure arise.

---

## Variant C — Long (three paragraphs, ~280 words)

**Programme Prose — Preamble**

> The programme prose describes the entire research programme — what it is, how it fits together, and how it intends to unfold. It is not the place for detailed instructions on how to perform specific elements; those live in the instruction documents and in the global rules, which are binding in ways the prose is not. The prose is descriptive: it tells the programme's own story.
>
> The corpus covers six broad areas: the programme's purpose and governing question; the research methodology and the pipeline through which work moves; the disciplines, tools, and evidential principles by which the programme operates; the shape of the data it produces and the architecture that holds it; the governance that keeps that data correct over time; and the instruction corpus that binds the work, together with the discipline of how instructions are versioned, referenced, and updated. Within each area, individual prose records describe specific components in enough detail that a reader can understand the component without reading its underlying rules, instructions, or schema.
>
> The prose sits alongside two other authoritative layers. The global rules are the programme's binding discipline — what must be done, under what conditions, at what sequence — and they are enforced without exception. The database schema is the programme's structural memory — the tables, fields, and relationships by which data is held. The prose is the programme's narrative memory — the account of why the programme exists, how the rules and the schema came to be, what the data means, and how the pieces operate together. Each layer stands on its own; together they constitute the programme's full self-description. This prose corpus is a living document, growing as the programme itself grows, and kept current as rules and schema change.

---

## Placement decision — where the preamble lives

Three options:

| Option | Description | Arguments for | Arguments against |
|---|---|---|---|
| **(a) Own `prose_section_type`** | New type `prog_preamble` with `chapter_no = 0`, `sort_order = 0`. Sits above the six macro areas in the extract. | Preamble becomes a first-class prose record; travels with the corpus wherever it is extracted; the chapter_no = 0 convention is clean. | Adds one more type to the seed — minor. |
| **(b) In the structure design only** | Preamble lives in `programme-prose-structure-design-v2` as the opening narrative; not a DB row. | Lighter-weight; avoids a "special" section type. | Preamble doesn't travel with the prose corpus — a reader pulling the prose extract sees content without the framing. Runs counter to the authoritative-memory principle (the DB should hold the prose, not just describe where it isn't). |
| **(c) Both** | Preamble is a `prose_section` row **and** reproduced as the opening of the structure design. | Researcher convenience — both contexts have the preamble visible. | Mirror risk — the structure design's copy can drift from the DB row over time. |

**Authorship view:** **Option (a)**. The preamble belongs in the DB because the prose corpus is the authoritative narrative memory; having the preamble elsewhere only makes the corpus extract read as if it starts mid-conversation. Chapter_no = 0 is a clean convention that matches how the framework already uses chapter_no for macro areas 1–6.

One implication: adopting (a) increases the seed count. Current framework plans 52 section types (6 macro + 46 sub). With a preamble type, 53. With the additions I recommended in the framework review (researcher role, session lifecycle, findings, and any other accepted), it rises further. Worth noting; not an objection.

---

## What the researcher needs to decide

1. **Variant A, B, or C** — which length serves the purpose? A is closest to your starter in feel; B adds the six-area map; C adds the three-layer (rules / schema / prose) framing.
2. **Placement — (a), (b), or (c)?** My recommendation: (a).
3. **Edits to the chosen variant** — wording, emphasis, any sentence to add or remove. The second sentence in all three variants ("those live in the instruction documents and in the global rules, which are binding in ways the prose is not") is my sharpening of your starter; if "which are binding in ways the prose is not" feels heavier than the register wants, it can come out without loss.
4. **Any drafting element I should flag separately?** For example: variant C's third paragraph introduces the phrase "narrative memory" in contrast to "binding discipline" and "structural memory" — this is my framing and may or may not match how you describe the programme. If it is the wrong register, I can rework.

---

## Reflection on the preamble's role

The preamble will be read more often than any individual prose record — it sets expectations for everything that follows. Two consequences worth thinking through before finalising:

**On what the preamble promises.** If the preamble says the prose "tells the programme's own story" (Variant B), then every sub-section body is implicitly a chapter of that story. Drafting style, tone, and voice should align with that promise. This disciplines the drafting work positively — it gives future drafters a target register.

**On what the preamble excludes.** By saying "not detailed instructions", the preamble rules out a large class of content. This is useful: it protects the prose from inflation (drafters adding procedural detail because "it might as well go here") and it protects the instructions from duplication (the instruction documents remain the binding procedural source). But the line is not perfectly sharp — "how the VC pass classifies verses" is procedural, while "what the VC pass is and why it exists" is descriptive. The preamble's boundary will need to be honoured by authorship judgement on a case-by-case basis; it is not a mechanical filter.

Flagging so the consequence is visible: the preamble commits the prose to a register. If the register proves too constraining for specific records, the preamble itself can be revised — but ideally after drafting has tested the register rather than before.

---

*wa-prose-draft-preamble-v1-20260421 | First draft, three variants, per researcher message 6 of session `prose`*
