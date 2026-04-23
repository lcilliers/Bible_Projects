# wa-prose-draft-preamble-v2-20260421

> Framework B Soul Word Analysis Programme — Programme Prose Preamble (Committed Draft)
> Session reference: prose
> Session date: 2026-04-21
> Previous output: wa-prose-draft-preamble-v1-20260421 (three variants); wa-prose-obslog-v1-20260421
> Governed by: wa-global-general-rules [current]
> Target section_type: new row — `code = preamble`, `label = Programme Preamble`, `source_stage = programme`, `chapter_no = 0`, `sort_order = 1`

---

## Change Control — v2

| Change | Section |
|---|---|
| v1 presented three variants (A/B/C) and three placement options (a/b/c). Researcher selected Variant B and placement (a), and gave authorship mode: commit and let researcher edit. | Drafting approach |
| Variant B rewritten with boundary discipline strengthened to address the drafter audience explicitly; closed-corpus principle honoured (researcher message 8 — "nothing exists outside the prose sections + metadata"); sharpening clause "binding in ways the prose is not" removed; label spelling silently corrected from "Preable" to "Preamble". | Body |
| Section-type metadata confirmed; section-type `description` field drafted. | Patch record envelope |

---

## Preamble body — committed

**Heading:** `Programme Preamble`

**Body:**

> The programme prose describes the entire research programme — what it is, how it fits together, and how it intends to unfold. It is the programme's narrative memory: the account that a reader encountering the work for the first time can use to understand what the programme is, what it produces, and the disciplines by which it operates.
>
> This prose is not the place for detailed instructions on how to perform specific elements of the work. Procedural content — the exact format of a patch, the step sequence for executing a directive, the completeness tests applied at an inflection point — lives in the instruction documents and the global rules, which are the programme's binding and procedural sources. The prose describes; the instructions bind. A drafter who finds themselves specifying how a task is performed, rather than what the task is and why it exists, has crossed into territory that belongs to an instruction document. This boundary is deliberate and load-bearing: the prose corpus is intended to stand on its own as a coherent description, and instructions are intended to stand on their own as the working procedures. Neither is a substitute for the other.
>
> The corpus covers six broad areas. It begins with the programme's purpose — the governing question, how inner being is defined, where this study sits within the researcher's wider work, and what a successful outcome would look like. It then describes the research methodology and the pipeline through which work moves, from word selection to publication. It sets out the disciplines, tools, and evidential principles by which the programme operates — how findings are distinguished from hypotheses, how the two-AI division of responsibility functions, how memory is managed across sessions. It describes the shape of the data the programme produces and the architecture that holds it — the registry, the terms, the verse groups, the dimensional profiles, the question catalogue. It covers the governance that keeps that data correct over time — the soft-delete discipline, validation standards, backup regime, patch-failure protocol. And it describes the instruction corpus itself: how rules and instructions are versioned, referenced, and updated, and how the programme's authority structure operates.
>
> Within each area, individual prose records describe specific components in enough detail that a reader can understand the component without leaving the prose corpus. The corpus is designed to be self-sufficient as a narrative account of the programme — every piece of information a reader needs to understand what the programme is should be present here. Where a record points outward to a rule, an instruction, or a schema table, the pointer exists to allow the reader to reach the binding source, not to substitute for content the prose should itself contain.

---

## Body metrics

Approximate word count: **365 words**. `word_count` calculated at patch apply time.

Four paragraphs. Structure:
- §1 — What the prose is (narrative memory; reader orientation).
- §2 — What the prose is not (procedural content); the boundary made explicit for drafters.
- §3 — What the corpus contains (the six-area map, expressed as reader navigation).
- §4 — How the records inside each area are designed (self-sufficient; pointers vs. substitutes).

---

## Authorship notes

Three substantive changes from variant B:

1. **Narrative memory surfaced earlier.** Variant B delayed this framing to the closing sentence of its first paragraph. v2 leads with it — the reader knows immediately what role this corpus plays.

2. **Boundary discipline given its own paragraph.** Variant B carried the "not detailed instructions" clause in a subordinate position. v2 gives it a full paragraph (§2) because the researcher identified it as load-bearing for future drafters. The paragraph names the drafter audience implicitly by describing the failure mode ("A drafter who finds themselves specifying how a task is performed…") so a future drafter reading this paragraph recognises themselves.

3. **Closed-corpus principle surfaced in §4.** Variant B said "a reader can understand the component without reading its underlying rules, instructions, or schema". v2 sharpens: "without leaving the prose corpus". This reflects the researcher's design principle that the prose + metadata must be self-sufficient for compiling an automated document. External references are explicitly framed as pointers, not substitutes.

Removed: the "binding in ways the prose is not" sharpening clause from v1 variants — not because it was wrong, but because the longer §2 now carries the boundary work, and keeping the clause would have been belt-and-braces.

Did not carry forward: the three-layer framing (rules = binding / schema = structural / prose = narrative memory) from variant C. That framing is useful but belongs in its own prose record — likely under the instruction corpus area or as a framing paragraph to the macro area 6 — rather than in the preamble where it would compete with §2's boundary work.

---

## Proposed `prose_section_type.description`

The section-type description is the stub text that appears in the prose extract alongside the label, before any body exists. For the preamble:

> Opening orientation for the programme prose corpus. Sets the tone for readers, makes the boundary between descriptive prose and procedural instruction explicit for drafters, and maps the six-area structure that follows.

---

## Patch record envelope — full field values for the eventual PROSE patch

For the `prose_section_type` insert (part of the seeding patch):

| Field | Value |
|---|---|
| `code` | `preamble` |
| `label` | `Programme Preamble` |
| `source_stage` | `programme` |
| `lifecycle_tag` | `null` |
| `chapter_no` | `0` |
| `description` | (as §Proposed description above) |
| `expected_length_min` | `300` |
| `expected_length_max` | `500` |
| `sort_order` | `1` |
| `delete_flagged` | `0` |

For the `prose_section` insert (the body, post schema-enablement-directive):

| Field | Value |
|---|---|
| `registry_id` | `null` (requires schema enablement directive applied first) |
| `section_type_id` | `{lookup from code = 'preamble'}` — CC resolves at patch apply time |
| `heading` | `Programme Preamble` |
| `body` | (the four-paragraph body above) |
| `word_count` | `365` (validated at apply) |
| `status` | `draft` |
| `version` | `1` |
| `author` | `claude_ai` |
| `source_file` | `wa-prose-draft-preamble-v2-20260421.md` |

Note: `expected_length_min` and `expected_length_max` on the section-type row are my judgement (a preamble of this kind sits naturally between 300 and 500 words). These bounds will enforce discipline on future supersedences — a v2 body growing to 800 words would flag as outside range. If researcher prefers to leave these null on the section-type row, that is fine; they are hints, not constraints.

---

## What the researcher needs to do

Read the committed body. Edit where it wants changing. That is all — no options to select, no decisions required from my end. Researcher's commitment in message 8 was "I will definitely make changes"; that is the expected next step.

---

*wa-prose-draft-preamble-v2-20260421 | Committed draft per researcher message 8 — authorship mode: commit-and-edit*
