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

## The span (the verse-link) + the two-level operation (added 2026-06-15)

**Where the span lives + reliability.** The span is **not** in `verse_context` — it's `span_strong_match` on `wa_verse_records` (and `wa_verse_term_links`), reached from a verse_context row via `verse_record_id`. It is **highly reliable**: `span_strong_match=1` on **61,844/61,846** verse-records and **227,026/227,288** links — **0 zeros**, only a handful NULL. So the term↔verse link (which word in the verse is this term) is authoritative for essentially every occurrence.

**The operation IS two-level — confirmed.** Over the 61,665 active clustered occurrences (span reliable + subgloss present for ~100%):

| level | definition | share |
|---|---|---|
| **STRAIGHT-THROUGH** | mono-sense term (one subgloss across its corpus) → span + subgloss resolve the sense **without doubt**; fully mechanical, no read | **51,085 · 83%** |
| **COMPLEX** | poly-sense term (>1 subgloss) → the per-occurrence subgloss still resolves most, but these need verification (the coarse-ceiling residue) | **10,580 · 17%** |

**The complexity is tiny and bounded:** all 17% comes from just **70 poly-sense terms** (54 with 2 subglosses, 14 with 3, 2 with 4). So the complex level is a *named, small* set — not a diffuse problem.

**→ This is exactly the two-level sense pipeline:**
1. **Straight-through (83%):** sense = the term's single subgloss (anchored by `span_strong_match=1`). Pure mechanical pass — emit `sense_id` + finding directly.
2. **Complex (17%, 70 terms):** take the **per-occurrence subgloss** (still mechanical for most); only the coarse-ceiling subset (e.g. *pneuma* "spirit" not separating Holy/human) needs a **signal-rule** or an `indeterminate`/`UNRESOLVED` verdict.

## CRITICAL: it's a FIX, not a create (2026-06-15)

The sense field is **already populated** — it is the **T7 'Lexical and Semantic Analysis'** finding. Two provenances hold it:
- **`l2_api`** (where the read ran, M01/M15) — a rich, read-derived contextual sense (e.g. *"astonishment and terror at the miraculous; awe"*). Good.
- **`l2_mechanical`** (145,720 VERSE findings, the bulk) — uses the **UNIFORM TERM GLOSS**, repeated for every occurrence: H2194 = *"to have indignation, be indignant…"* on every verse. **This is the impasse defect, confirmed in the data.** It ignored the per-occurrence subgloss.

So **"populate sense" = FIX the `l2_mechanical` sense findings** to carry the **per-occurrence subgloss** (`step_subgloss_label`, the real sense), not the uniform gloss — anchored by `span_strong_match=1`. Plus:
- **35,899** `l2_mechanical` findings **duplicate** an `l2_api` finding (same verse+term) — the read sense already exists there; the mechanical one is redundant and should defer to / be superseded by it.

## The build (sense fix) — proposed, needs sign-off before a large write
1. **Straight-through (83%):** for `l2_mechanical` sense findings on **mono-sense** terms, set `finding_value` = the per-occurrence `step_subgloss_label`; record/confirm via the gloss tables; set `verse_context.sense_id`.
2. **Complex (17%, 70 terms):** same per-occurrence subgloss, but flag the coarse-ceiling subset for a signal-rule / `indeterminate`.
3. **De-duplicate:** where an `l2_api` sense exists, the `l2_mechanical` one defers (soft-delete or mark superseded).
4. Confirm the subgloss↔canonical-sense (`wa_meaning_sense`) relation for `sense_id` (handle sub-entry term keys).
5. Then **type (#2)**, which supersedes to sense.

> This is a ~100k+ finding update + de-dup — destructive-ish and reversible-by-design, but it touches the finding model + the catalogue link, so **design sign-off first, dry-run before live**. Do NOT bulk-write sense values blind.
