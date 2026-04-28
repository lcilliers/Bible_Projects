# Characteristic Layer Concept — Programme Architecture Note

**Date:** 2026-04-03
**Status:** Concept — for researcher + Claude AI discussion when Stage 1 nears completion
**Origin:** Researcher observation during term exploration (extract_term_data.py review of H2734)

---

## The Observation

The programme currently cuts the data two ways:
- **Registry** (212 English words) — the scope instrument
- **Term** (Strong's numbers) — the lexical instrument

A third cut is emerging from the Verse Context data: **characteristics** — what a term actually does to or in the inner being, regardless of which registry it belongs to. This cut is visible in the `verse_context_group.context_description` field, which Claude AI writes for every classified term.

Example: H2734 (charah, "to be incensed") in registry 4 (anger) has context descriptions like:
- "Term names the kindling of inner anger as the first act of moral rebellion"
- "Term names divine anger as inner response to covenant violation"
- "Term names the inner injunction against anger as spiritual counsel"

These descriptions classify the term's *function* in the inner being — not its lexical meaning, but what it reveals about how the inner life works. If you read all 1,700+ context descriptions programme-wide, patterns would emerge: terms that name inner states, terms that name capacities, terms that name orientations, terms that name expressions.

---

## The Problem

Session B Analysis works per pool (10-15 words). It can identify characteristics within its pool but cannot see cross-programme patterns. Session D is designed for cross-programme synthesis but comes after Session B.

The context descriptions being produced in Stage 1 contain a proto-taxonomy of inner-being functions. But no current pipeline stage aggregates them programme-wide.

---

## The Proposed Layer

**Layer 2 — Characteristic Mapping** sits between Verse Context (Layer 1) and Session B Analysis (Layer 3).

| Layer | Scope | Who | What |
|-------|-------|-----|------|
| 1. Verse Context | Per term | Claude AI + Claude Code | Classify verses, group by contextual meaning |
| **2. Characteristic Mapping** | **Programme-wide** | **Claude Code (mechanical) + Claude AI (validation)** | **Cluster context descriptions into characteristic families** |
| 3. Session B Analysis | Per pool | Claude AI | Analytical narrative per word |
| 4. Session D Synthesis | Cross-programme | Claude AI | Full synthesis |

Layer 2 is a **data organisation task**, not an analytical task:
1. Claude Code extracts all context_descriptions programme-wide
2. Mechanical grouping by key phrases (inner state, divine response, moral quality, volitional act, capacity, orientation, expression, etc.)
3. Produce characteristic families with their member terms and registries
4. Claude AI reviews and refines per pool — validating, not discovering

---

## What This Enables

- Session B receives a **pre-structured characteristic landscape** instead of discovering taxonomy from scratch
- Cross-pool patterns are visible before Session D begins
- The "super groups" the researcher identified — characteristics that span multiple registries — become a formal programme construct
- Pool processing order could be optimised by characteristic density, not just term sharing

---

## Prerequisites

- Stage 1 (Verse Context) substantially complete — need enough context_descriptions to cluster meaningfully
- Researcher + Claude AI agreement on the characteristic vocabulary
- Possible schema addition: a characteristic/capability table linking terms to characteristic families

---

## Next Steps

1. When Stage 1 reaches ~80% completion, extract all context_descriptions
2. Present to Claude AI for initial characteristic family identification
3. Researcher reviews and names the families
4. Assess whether this becomes a formal pipeline stage or an analytical tool

---

*Project note — not an instruction document. For discussion when Stage 1 nears completion.*
