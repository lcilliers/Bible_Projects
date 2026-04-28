# wa-prose-draft-purp-scope-v1-20260421

> Framework B Soul Word Analysis Programme — Sub-section 1.2 Scope (Draft)
> Session reference: prose
> Session date: 2026-04-21
> Previous output: wa-prose-draft-purp-mission-v2-20260421 (approved); wa-prose-corpus-assembly-v1-20260421
> Governed by: wa-global-general-rules [current]; closed-corpus rule (session `prose` message 8)
> Target: `prose_section_type.code = prog_purp_scope` | `label = Scope` | `chapter_no = 1` | `sort_order = 3` (provisional)

---

## Change Control — v1

| Change | Section |
|---|---|
| New document. First committed draft of the Scope sub-section body, from researcher message 11 source material, under the closed-corpus rule and commit-and-edit authorship mode. | All |

---

## Heading

`Scope`

## Body

> The advent of the Framework A and Framework B documents did not close the work. By February 2026, with both studies in a readable state, it had become clear that each would benefit from further research and refinement — in style and in depth. Further reading into Framework B's subject made the sharper point: the study had only touched the surface of what the soul actually consists of. A cursory overview counted some twenty-eight distinct characteristics — an order of magnitude short of what a careful treatment of the biblical evidence plainly contains.
>
> That shortfall triggered a deliberate extension of scope: an in-depth exploration of the soul, set within the wider frame of the inner being so that soul, spirit, and body could be treated in their actual relation rather than in isolation. A thorough collation of Scripture's inner-being vocabulary was assembled — approximately two hundred English words, mapped to their Hebrew and Greek originals. That registry became the scope of the present focus of the programme. Every word in it is in scope; every word outside it is out of scope. The registry is the boundary, and the boundary is the basis on which everything downstream — verse selection, term classification, dimensional analysis, cross-registry synthesis — is defined.

---

## Body metrics

Approximate word count: **200 words**. Two paragraphs.

---

## Authorship notes

Two judgement calls worth naming:

1. **"An order of magnitude short" added to paragraph 1.** Your material says the cursory overview noted "about 28 distinct characteristics" and that this triggered the scope extension. You did not state what a complete treatment would look like, but the fact that twenty-eight triggered an extension to a ~200-word registry implies the original count was recognised as substantially incomplete. "An order of magnitude short" makes that implication visible without inventing a specific target figure. If this overreaches, the clause removes cleanly.

2. **Closing "the registry is the boundary, and the boundary is the basis" added to paragraph 2.** Your material says the registry "became the scope of this particular focus of the entire programme". I extended that to make the closed-corpus rule explicit in the prose: everything downstream (verse selection, term classification, analysis) is defined against the registry. This serves the preamble's promise that a reader understands each component without leaving the corpus — a reader of Scope now knows not just what the scope is but how it operates as a boundary. Removable if you find it pulls scope into territory that belongs to a later sub-section; my view is that the statement of operating consequence belongs with the statement of scope.

What I did not do: I held back any mention of the database, the two-AI architecture, the pipeline, or the current programme's methodology. These belong to 1.4 (this inner being programme) and to Area 2 and Area 3. Scope stops at the registry.

---

## Closed-corpus compliance check

- The February 2026 timing is given explicitly. A reader does not need external reference to place the scope-setting moment.
- The ~200-word figure is stated. The registry is identified as the boundary; the boundary is identified as operational. A reader finishes the record knowing what the scope is, when it was set, and that it functions as the downstream filter.
- No "see [document]" references. No offloaded content.

---

## Flag — figure consistency

The prose states "approximately two hundred" words, matching your source material. My in-context awareness carries a slightly different figure from programme-state memory (~212 words across 181 active registries). These are compatible:
- "Approximately two hundred" — the original collation count, which is what a scope record should carry because scope describes what was collated, not the current pipeline state.
- "212 / 181 active" — current counts after pipeline work has added, split, merged, or soft-deleted entries.

The distinction matters: scope is historical and bounding; current counts belong to methodology or data architecture. If you want the scope to carry the current active-registry figure instead, that is an edit.

---

## Patch record envelope (for PROSE patch when gates clear)

| Field | Value |
|---|---|
| `registry_id` | `null` |
| `section_type_id` | `{lookup from code = 'prog_purp_scope'}` |
| `heading` | `Scope` |
| `body` | (approved body text above) |
| `word_count` | `200` |
| `status` | `draft` |
| `version` | `1` |
| `author` | `claude_ai` |
| `source_file` | `wa-prose-draft-purp-scope-v1-20260421.md` |

For the `prose_section_type` row (part of the seeding patch):

| Field | Value |
|---|---|
| `code` | `prog_purp_scope` |
| `label` | `Scope` |
| `source_stage` | `programme` |
| `chapter_no` | `1` |
| `sort_order` | `3` (provisional — second sub-section of chapter 1; mission occupies sort_order 2) |
| `description` | `The programme's scope boundary — what it includes, what it excludes, and how the boundary was set. The ~200-word inner-being registry as the operational scope against which all downstream work is defined.` |
| `expected_length_min` | `150` |
| `expected_length_max` | `300` |

---

*wa-prose-draft-purp-scope-v1-20260421 | First committed draft, scope sub-section, from researcher message 11 source material*
