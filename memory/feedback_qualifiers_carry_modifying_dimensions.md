---
name: feedback_qualifiers_carry_modifying_dimensions
description: Modifying qualifiers around a characteristic (intensity/specifier/effect) must be read into dimensions, not dropped to standalone.
metadata:
  type: feedback
---

The re-read reads qualifier spans only **relationally** — a `qualifier`-role span becomes the span-id endpoint of a characteristic's coupling(112)/source(103)/target(107)/manner(108)/seat/bearer/operation. That captures the movement graph well. **But the MODIFYING qualifiers are dropped:** intensity (`greatly`, `very`), specifier (a narrowing `this`/`of-X`), and effect (`so that…`, the result) fall to `role='standalone'` and survive only inside the `reading` prose, not as structured dimensions.

**Evidence:** Pro 23:24 "the father of the righteous GREATLY rejoices" — `rejoice` read as the characteristic, but **"greatly" (H1523) sits `standalone`, unlinked**. The old model *did* read intensity(109)=8,748 rows and specifier(110)=9,794 rows; the re-read stopped. So intensity/specifier/effect are **DEGRADED, not redundant** — the researcher's point (2026-07-14): they are *derivatives of reading the qualifier in context*, and that read was thinned.

**Why:** the reread narrowed qualifier-reading to relational qualifiers (the pair-endpoint model) and folded the modifying ones into prose.

**How to apply:**
- When a characteristic has a same-verse **modifying qualifier** — a degree adverb (intensity), a narrowing specifier, or a result clause (effect) — **read it into the corresponding dimension AND link the qualifier span to the char** (as coupling/target already do). The `standalone` modifying-qualifier spans are already present; the read must *connect* them.
- Do this in the method going forward AND retro to Psalms/Proverbs (researcher: "must be done for both books + built in").
- In the projection, this lets `intensity`/`specifier`/`effect` be filterable columns and the edge-list carry `edge_type ∈ {intensity, specifier, effect}`.
- Do NOT deprecate `specifier`: the old *content* ("of David") was low-value, but the *concept* (a qualifier that narrows the characteristic) is valid.

Related: [[project_ve_lexical_is_verse_first]], [[feedback_char_driven_read_not_span_sweep]], [[feedback_resist_grouping_preserve_distinctions]], [[feedback_read_completeness_is_verse_level_not_passage_level]].
