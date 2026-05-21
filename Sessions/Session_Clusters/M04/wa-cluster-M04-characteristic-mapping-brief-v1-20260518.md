# M04 characteristic mapping — brief

**Cluster:** M04 — Joy, Gladness and Delight
**Task date:** 2026-05-18
**Audience:** Claude AI session
**Read this brief first.** Structural input is in a separate file referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M04/WA-M04-characteristic-mapping-brief-v1-20260518.md` | Primary task instructions |
| 2 | **Structural input** — `Sessions/Session_Clusters/M04/WA-M04-characteristic-mapping-input-v1-20260518.md` | M04 cluster description + 16 sub-groups (code, label, core_description, verse count, term count) |
| 3 | **Programme prose extract** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Chapter 1 'Defining Inner Being' | The canonical definition of an inner-being characteristic |
| 4 | **Structural-terms clarification** — `Workflow/methodology/WA-structural-terms-clarification-v1-20260518.md` | The corrected hierarchy: characteristic → registry → term → cluster → sub-group → VCG → tier |
| 5 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M04 (Joy, Gladness and Delight) has 16 substantive sub-groups. Per the programme's working definition, an inner-being characteristic is:

> *"the non-physical, internal states, capacities, and expressions that constitute a person's invisible life — encompassing how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God."*

Under the corrected hierarchy:

- A **cluster** groups *similar characteristics* for joint analysis.
- A **sub-group** within a cluster represents *a characteristic, or a sub-component of a characteristic*.
- Sub-groups may be split for verse-volume reasons; in that case, **multiple sub-groups can map to ONE characteristic**.
- The 189 Tier prompts apply per **characteristic** (across whatever sub-groups form it), not per sub-group individually.

Your task is to examine M04's 16 sub-groups and map them onto distinct characteristics.

---

## Your task

For each of the 16 M04 sub-groups in the structural input, decide:

- Does this sub-group represent **a distinct characteristic** in its own right?
- OR does it share a characteristic with one or more other M04 sub-groups (i.e., it is a sub-component, split for verse-volume reasons)?

Then produce a **characteristic map** for M04:

```
Characteristic 1 — <short name> — <one-paragraph definition tied to the inner-being scope>
  Sub-groups: M04-X, M04-Y, ...
  Rationale: why these sub-groups share this characteristic (and not others)

Characteristic 2 — <short name> — <one-paragraph definition>
  Sub-groups: M04-Z
  Rationale: ...

...
```

Each sub-group appears in exactly one characteristic. Every sub-group must be mapped (none left out).

### Quality expectations

1. **Each characteristic must be a true inner-being phenomenon** per the working definition — not just a register or stylistic variant. "Joy directed toward God" is a characteristic; "morning joy versus evening joy" is not. Test: can you state the characteristic as a distinct inner-being state/capacity/expression?
2. **Sub-groups grouped under one characteristic must share the same analytical phenomenon**, differing only by verse-volume / corpus-section / register-of-expression. If they differ in WHAT inner-being phenomenon they evidence, they're distinct characteristics.
3. **Cite specific sub-group features** in your rationale — quote from `core_description` to show why a grouping holds.
4. **Default to keeping sub-groups distinct.** Only group two or more sub-groups into one characteristic when the evidence forces it. The bias should be toward distinct characteristics; consolidation requires positive evidence of sub-component status.
5. **No more than ~10 characteristics for M04 likely**, but no upper or lower cap — let the analysis drive the count.

### Anti-patterns to avoid

- Don't group sub-groups together just because they share a Hebrew/Greek term family. Term overlap does not imply characteristic identity.
- Don't group sub-groups together just because they are in the same testament or have similar verse counts.
- Don't propose hyper-fine characteristics like "Joy at sunrise" — characteristics are analytical phenomena, not narrative details.
- Don't propose characteristics that don't match the inner-being-scope definition — every characteristic must be a non-physical internal state/capacity/expression.

---

## Output format

Write the characteristic map as a markdown document. Use this structure:

```markdown
# M04 characteristic map — proposed

## Summary

M04 represents N distinct inner-being characteristics, mapped across the 16 sub-groups as below.

## Characteristic 1 — <short name>

**Definition:** <one paragraph tying the characteristic to the inner-being working definition>

**Sub-groups in this characteristic:** M04-X, M04-Y, M04-Z

**Rationale:** <why these sub-groups share this characteristic — cite specific phrases from core_descriptions; explain whether grouping is for verse-volume reasons or analytical kinship>

## Characteristic 2 — ...
```

Then at the end:

```markdown
## Cross-check

All 16 sub-groups accounted for:
- M04-A → Characteristic <n>
- M04-B → Characteristic <n>
- ...
- M04-P → Characteristic <n>

## Observations and open questions

- <any sub-groups where the mapping is ambiguous and needs researcher decision>
- <any sub-groups that don't fit the M04 cluster analytically (rare)>
```

---

## After you finish

1. Drop the output in `Sessions/Session_Clusters/M04/` as `WA-M04-characteristic-map-v1-20260518.md`.
2. Ping CC: "M04 characteristic map ready: <path>".
3. CC presents the map to researcher for review.
4. If approved, the map drives Phase 9: the 189 prompts run per characteristic (across its sub-groups), not per sub-group individually.

---

*End of brief. Now load the structural input (#2 in Required inputs) and begin.*