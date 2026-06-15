# Sense (#1) — operation setup: the gloss tables that must be related

> Researcher (2026-06-15): *"sense works with the gloss/subgloss — the table for all glosses must be related to the operation."* This maps the gloss/sense data landscape so the sense operation connects real tables, not free text. Setup only; no writes yet.

## The three layers sense must relate (with live population)

| layer | table.column | population | role |
|---|---|---|---|
| **per-occurrence subgloss** (mechanical floor) | `wa_verse_term_links.step_subgloss_label` (+`_code`) | **227,194 / 227,288 (100%)** · 2,563 distinct values | STEP's sense tag for *this term in this verse* — the mechanical sense we resolve FROM (per [[project_l1l2_field_reliability_direction]]) |
| **canonical sense inventory** ("all glosses") | `wa_meaning_sense.sense_text` (via `wa_term_inventory.parsed_meaning_id`) | **16,005 senses / 7,456 parsed-meanings**; inventory link 6,770/6,846 | the term's full parsed sense set — **this is the "table for all glosses"** the operation must relate to |
| **where sense lands per verse** | `verse_context.sense_id` · `step_meaning_applied` · `sense_multiplicity` | `sense_id` **0 / 42,704** (the gap) · `step_meaning_applied` 27,794 (free text) | the resolved sense recorded against the verse — currently free-text only, **not linked** to a canonical sense |

## The operation (what "relate the gloss table" means here)
1. Each verse-occurrence already has a **per-occurrence subgloss** (100% coverage) — the mechanical sense.
2. **Relate** that subgloss to a **canonical sense row** in `wa_meaning_sense` (the term's parsed senses).
3. **Record** the chosen canonical sense on `verse_context.sense_id` (today **0/42,704** — the gap to fill).
4. The **sense finding** then references `sense_id`, so the verse-meaning is traceable to a named sense and **searchable across clusters/terms** — the whole point of the field-reliability work.

## The open design question (resolve first, before populating sense_id)
There are **two sense vocabularies** that aren't yet reconciled:
- the **STEP subgloss** vocabulary (2,563 distinct `step_subgloss_label`, per-occurrence), and
- the **parsed-meaning** senses (`wa_meaning_sense.sense_text`, from parsing the term's definition).

Do they map 1:1, partially, or are they orthogonal? The sense operation needs a **reconciliation rule** between them (subgloss → canonical sense), or a decision to treat the STEP subgloss itself as the canonical sense and build `sense_id` off a subgloss inventory. (A per-term check on *nephesh* H5315 was inconclusive — its data is under sub-entries H5315G/H/I/J, a base/sub-entry join detail to handle.)

## Next steps (sense work proper)
1. Resolve the subgloss↔parsed-sense mapping (pick the canonical sense source + the relation rule), handling sub-entry term keys.
2. Build the mechanical sense pass: per-occurrence subgloss → canonical `sense_id` on `verse_context` (the 79% mono-sense are trivial; poly-sense read the per-occurrence subgloss; coarse-ceiling residue → signal-rule or `indeterminate`/`UNRESOLVED`).
3. Emit the sense **finding** referencing `sense_id`.
4. Then **type (#2)**, which supersedes to sense.
