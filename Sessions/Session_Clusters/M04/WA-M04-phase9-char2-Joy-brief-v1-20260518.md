# M04 Phase 9 — Characteristic 2 (Joy) — brief

**Cluster:** M04 — Joy, Gladness and Delight
**Characteristic:** 2 — Joy
**Verses in scope:** ~469 across 4 sub-group(s)
**Task date:** 2026-05-18
**Audience:** Claude AI session

**Read this brief first.** Structural input is in a separate file referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M04/WA-M04-phase9-char2-Joy-brief-v1-20260518.md` | Primary task instructions |
| 2 | **Structural input** — `Sessions/Session_Clusters/M04/WA-M04-phase9-char2-Joy-input-v1-20260518.md` | Characteristic definition + sub-groups + VCGs + verses + 189 prompts + carry-forward observations |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |
| 4 | **Tier catalogue** — `Workflow/Tiers/wa-obs-catalogue-tiered-v{N}-{date}.md` (latest) | Full prompt catalogue T0–T7 (verses are also reproduced in §3 of the structural input for self-containment) |
| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |
| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M04 has 7 inner-being characteristics. You are processing **Characteristic 2 (Joy)**. Per researcher direction 2026-05-18:

> *"sub groups is purely a capacity organiser, the evaluating unit is the characteristic or group of sub groups."*

All your findings author at **characteristic scope** — NOT at sub-group scope. Sub-groups organise the evidence for navigation; they don't carry the analytical unit.

Cluster-scope synthesis (across all 7 characteristics) happens in a separate session at the end. **Don't author cluster-scope findings here.**

---

## Characteristic 2 — Joy: definition

> The active inner experience of rejoicing — the soul's engaged, participatory delight in what is worth celebrating. Joy is less surging than Exultation and more active than Gladness. It is the inner being rejoicing in something: in the Lord, in community, in shared celebration, in what is promised and coming. The commanded 'rejoice in the Lord always' is Joy — an active inner disposition of engagement, not merely a warm background feeling.

---

## Your task

For each of the **189 catalogue prompts** (T0–T7), author a finding at characteristic scope for Characteristic 2 (Joy). Use the verse evidence in the structural input.

Output format per prompt (one block per prompt; parser-safe form per v2_5 §12.4):

```
**T#.#.# — question text excerpt (optional)**

**[CHAR-2]** E — Finding text. Cite specific verses / VCGs / sub-groups from the evidence in §3 of the structural input. Quote the specific verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.

---
```

Outcome codes:

- **E** — evidenced; cite specific verses / VCGs
- **S** — silent; describe the analytical significance of the absence
- **G** — gap; describe what data would be needed to answer

Scope marker is `**[CHAR-2]**` (CC's loader maps this to characteristic_id=2 for this characteristic).

---

## Discipline (per v2_5 §12)

1. **Read every verse-meaning in the structural input.** No sampling. The Pass A meanings condense each verse's inner-being content — read them all.
2. **Per prompt, ground in specific evidence.** Every E finding names verses, VCGs, or sub-groups. The test for a good answer is *can I name what evidences this?*
3. **Fluency is not a quality signal** (v2_5 §2.4). Plausible-sounding text without specific citations is rejected.
4. **No sub-group-scope findings.** All findings at characteristic scope. Where evidence differs by sub-group, the finding text names the sub-group(s) inline (e.g., "primarily evidenced in M04-A; with M04-G's affective register confirming...").
5. **No cluster-scope findings.** Cluster synthesis runs after all 7 characteristics finish.
6. **Self-check before submitting** — confirm each of the 189 prompts has a row; confirm every E names evidence; confirm no row was bulk-classified from a sample.

---

## Carry-forward observations (apply to this characteristic)

These analytical hints were raised at characteristic-mapping time and are queued for Phase 9 attention:

### INTER_RELATIONSHIP — Joy/Gladness inter-relationship within M04-B and M04-C

> M04-B (Communal/Festive Rejoicing) and M04-C (NT Joy in Christ) carry BOTH the active-rejoicing register (Joy, Characteristic 2) and the settled-warm register (Gladness, Characteristic 3) within their verse corpora. The characteristic map assigns these sub-groups to Joy as their dominant phenomenon; the Gladness dimension within them is expected to emerge from VCG-level analysis. This inter-relationship between Joy and Gladness is anticipated as one of the significant findings of Phase 9 for M04.

**At Phase 9 end:** flag whether this observation surfaced in the findings as expected; mark in your final summary so CC can update status open → confirmed/refined.

### SPLIT_SUBGROUP — M04-E serves both Characteristic 2 (Joy) and Characteristic 7 (Suffering-Joy)

> M04-E (Promised and Eschatological Joy) carries two distinct registers within its 35-verse corpus. Its eschatological forward-rejoicing register (sa.s.von — gladness promised as reversal of sorrow) belongs under Characteristic 2 — Joy. Its NT suffering-paradox register (agalliao — rejoicing in trials; joy that suffering itself occasions) belongs under Characteristic 7 — Suffering-Joy. The VCG structure within M04-E will show which VCGs serve which characteristic. Phase 9 should apply the 189 prompts to M04-E under both Characteristic 2 and Characteristic 7 separately, where the evidence permits.

**At Phase 9 end:** flag whether this observation surfaced in the findings as expected; mark in your final summary so CC can update status open → confirmed/refined.

---

## Output structure

Write your output as a single markdown document. Suggested structure:

```markdown
# M04 Phase 9 — Characteristic 2 (Joy) — findings

**Date:** 2026-05-18
**Characteristic_id:** 2
**Prompts answered:** 189 / 189

## T0 — Divine Image and Created Design

**T0.1.1 — [question]**

**[CHAR-2]** E — finding text with verse citations...

---

**T0.1.2 — [question]**

...
```

End the document with a **self-check** block:

```markdown
## Self-check

- Prompts answered: 189 / 189 ✓
- E findings naming specific evidence: <count>
- S findings: <count>
- G findings: <count>
- Carry-forward observations addressed: <list>
- Unexpected analytical patterns surfaced: <list>
```

---

## After you finish

1. Drop the output in `Sessions/Session_Clusters/M04/WA-M04-phase9-char2-Joy-findings-v1-20260518.md`
2. Ping CC: "M04 Char 2 (Joy) Phase 9 findings ready"
3. CC parses, validates evidence-grounding + completeness, applies to cluster_finding with characteristic_id set.
4. Move to next characteristic (Char 3).

---

*End of brief. Load the structural input (#2) and begin.*