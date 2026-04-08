# CC Directive — Group Description Verification Extract
**File:** wa-dim-cc-directive-grpverify-6427-6428-2026-04-07.md
**Issued by:** Claude AI — WA-DimensionReview-Instruction-v1.3-2026-04-07
**Date:** 2026-04-07
**Previous output:** wa-dim-patch-C05-v1-2026-04-07.json

---

## Purpose

During Phase B of the C05 Dimension Review, groups 6427-001 and 6428-001 (Registry 151, sorrow) were found to carry identical `context_description` values:

> *"The heart stricken/pierced as inner-being affliction — the language of wounding applied to the inner state of the afflicted person."*

The underlying terms differ:
- **6427-001**: mti_term_id 6427, H2490B cha.lal, gloss "to play flute", verse_context_group_id 2253, wa_dimension_index id 5541
- **6428-001**: mti_term_id 6428, H2490I cha.lal, gloss "to profane/begin: fruit", verse_context_group_id 2254, wa_dimension_index id 5543

Both groups have 1 anchor verse and 0 related verses. The descriptions cannot be differentiated as currently written, which means a reliable dimension cannot be assigned to 6428-001.

**Dimension assigned to 6427-001 in PATCH-20260407-DIMREVIEW-C05-V1:** Affective/Emotional (CLAUDE_AI, manual_override=0).
**Dimension for 6428-001:** deferred pending description correction.

---

## Instruction to Claude Code

Please construct a **group description verification extract** per WA-DimensionReview-Instruction-v1.3 Section 9.2 for both groups.

**Extract name:** `wa-dim-grpverify-6427-6428-2026-04-07.json`

**Scope:** Both groups together in a single extract file.

**Required fields per group:**

| JSON field | Source |
|---|---|
| `group.id` | wa_dimension_index.id |
| `group.group_code` | wa_dimension_index.group_code |
| `group.strongs_number` | mti_terms.strongs_number |
| `group.transliteration` | mti_terms.transliteration |
| `group.gloss` | mti_terms.gloss |
| `group.current_description` | verse_context_group.context_description |
| `group.notes` | verse_context_group.notes |
| `anchor_verses.verse_record_id` | verse_context.verse_record_id (is_anchor=1, delete_flagged=0) |
| `anchor_verses.book` | books.name via wa_verse_records.book_id |
| `anchor_verses.chapter` | wa_verse_records.chapter |
| `anchor_verses.verse` | wa_verse_records.verse |
| `anchor_verses.verse_text` | wa_verse_records.verse_text |
| `related_verses.*` | same as anchor_verses where is_related=1, is_anchor=0 |

**Group identifiers:**

| Field | Group 6427-001 | Group 6428-001 |
|---|---|---|
| wa_dimension_index.id | 5541 | 5543 |
| verse_context_group.id | 2253 | 2254 |
| mti_term_id | 6427 | 6428 |

---

## Post-extract action

Once this extract is returned to Claude AI, Claude AI will:
1. Read the verse texts for both groups
2. Determine whether the descriptions are genuinely identical in meaning or whether the verses reveal a distinguishable inner-being engagement
3. Propose revised descriptions for researcher confirmation
4. Encode the confirmed correction in a supplementary group description correction patch for Claude Code application

---

*WA-DimensionReview-Instruction-v1.3-2026-04-07 | Directive issued 2026-04-07*
