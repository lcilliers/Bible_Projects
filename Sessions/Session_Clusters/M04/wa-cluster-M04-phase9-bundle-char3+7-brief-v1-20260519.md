# M04 Phase 9 — Bundle (char3+7) — brief

**Cluster:** M04 — Joy, Gladness and Delight
**Characteristics in this bundle:** 3 (Gladness), 7 (Suffering-Joy)
**Total verses across the bundle:** ~172
**Total prompts to author:** 378 (= 189 × 2 separate passes)
**Task date:** 2026-05-19
**Audience:** Claude AI session

**Read this brief first.** Structural input is in a separate file referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M04/WA-M04-phase9-bundle-char3+7-brief-v1-20260519.md` | Primary task instructions |
| 2 | **Structural input** — `Sessions/Session_Clusters/M04/WA-M04-phase9-bundle-char3+7-input-v1-20260519.md` | Per-characteristic data blocks + shared 189-prompt catalogue + carry-forward observations |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |
| 4 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |
| 5 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

> The full 189-prompt T0–T7 catalogue is reproduced inside the structural input. No separate catalogue file required.

---

## Why this is a bundle (not a single characteristic)

This package covers **multiple characteristics** to save on session setup overhead. The data for each characteristic is kept distinct in the structural input — sub-groups, VCGs, and verses are grouped under their own characteristic block (§2.A, §2.B, …). **Do not pool evidence across characteristics.** Each 189-prompt pass uses ONLY that characteristic's evidence.

> Per researcher direction 2026-05-19: *"you can combine more than one characteristic in the dataset, but keep the grouping of the sub group distinctly separate into characteristics, and be clear in the guide to do separate batches of going through the catalogue."*

---

## How to work this bundle — separate batches

You will do **2 separate 189-prompt batches**, one per characteristic, in the order listed below. Each batch is fully bounded to its own characteristic — do not reuse another characteristic's evidence within a batch.

| Batch | Characteristic | Sub-groups | Verses | Output file (you produce) |
|---|---|---|---:|---|
| 3 | Gladness | M04-L, M04-O | ~133 | `Sessions/Session_Clusters/M04/WA-M04-phase9-char3-Gladness-findings-v1-20260519.md` |
| 7 | Suffering-Joy | M04-E, M04-F | ~39 | `Sessions/Session_Clusters/M04/WA-M04-phase9-char7-Suffering-Joy-findings-v1-20260519.md` |

Complete each batch fully (189 prompts + self-check) and check it against the discipline list BEFORE moving to the next batch. Each output is a standalone findings file.

---

## Output format (applies to every batch)

Per prompt, one block; parser-safe form per v2_5 §12.4:

```
**T#.#.# — question text excerpt (optional)**

**[CHAR-N]** E — Finding text. Cite specific verses / VCGs / sub-groups from the characteristic's evidence block. Quote verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.

---
```

**Scope marker** is `**[CHAR-N]**` where **N is the characteristic number for that batch** (e.g., `**[CHAR-3]**` for the Gladness batch, `**[CHAR-7]**` for the Suffering-Joy batch). CC's loader uses this to set characteristic_id on each row, so it MUST match the current batch's characteristic.

**Outcome codes:**
- **E** — evidenced; cite specific verses / VCGs
- **S** — silent; describe the analytical significance of the absence
- **G** — gap; describe what data would be needed to answer

---

## Discipline (per v2_5 §12)

1. **Read every verse-meaning in the structural input for the current batch.** No sampling. The Pass A meanings condense each verse's inner-being content — read them all for the batch's characteristic.
2. **Per prompt, ground in specific evidence.** Every E finding names verses, VCGs, or sub-groups. The test for a good answer is *can I name what evidences this?*
3. **Fluency is not a quality signal** (v2_5 §2.4). Plausible-sounding text without specific citations is rejected.
4. **No sub-group-scope findings.** All findings at characteristic scope. Where evidence differs by sub-group within a characteristic, the finding text names the sub-group(s) inline.
5. **No cross-characteristic mixing.** Evidence from another characteristic's block is OFF-LIMITS for the current batch. If a cross-characteristic observation is significant, note it in the Self-check for that batch — do NOT embed cross-batch findings.
6. **No cluster-scope findings.** Cluster synthesis runs after all 7 characteristics finish.
7. **Self-check before submitting each batch** — confirm 189 prompts have rows; confirm every E names evidence; confirm the `[CHAR-N]` marker matches the batch.

---

## Carry-forward observations (apply per-batch)

These analytical hints were raised at characteristic-mapping time. Two statuses are shown: **OPEN** means action and flag at end of batch; **CONFIRMED** means already validated by an earlier Phase 9 batch — included here as context that may matter for the current batch's evidence selection.

### For Characteristic 3 (Gladness)

**INTEGRATION_NOTE — M04-L evaluative-cognitive face integrates with M04-O circumstantial under Gladness** — **OPEN**

> M04-L (Evaluative Goodness) and M04-O (Circumstantial Gladness) together form Characteristic 3 — Gladness. M04-L is the cognitive face (the soul's inner appraisal that something is good — the assessment that produces and expresses gladness); M04-O is the experiential face (the warm inner response to beneficial circumstance). Phase 9 findings for M04-L should be integrated with M04-O's findings under Characteristic 3, recognising these together name the cognitive + experiential aspects of one inner-being characteristic.

At end of this batch, flag whether the observation surfaced as expected.

### For Characteristic 7 (Suffering-Joy)

**SPLIT_SUBGROUP — M04-E serves both Characteristic 2 (Joy) and Characteristic 7 (Suffering-Joy)** — **CONFIRMED (context only)**

> M04-E (Promised and Eschatological Joy) carries two distinct registers within its 35-verse corpus. Its eschatological forward-rejoicing register (sa.s.von — gladness promised as reversal of sorrow) belongs under Characteristic 2 — Joy. Its NT suffering-paradox register (agalliao — rejoicing in trials; joy that suffering itself occasions) belongs under Characteristic 7 — Suffering-Joy. The VCG structure within M04-E will show which VCGs serve which characteristic. Phase 9 should apply the 189 prompts to M04-E under both Characteristic 2 and Characteristic 7 separately, where the evidence permits.

_Earlier-batch resolution:_ CONFIRMED via Char 2 Phase 9 self-check. The split is validated by the evidence: M04-E-VCG-01 (sa.s.von corpus - OT restoration joy) belongs to Char 2 as eschatological-Joy register; M04-E-VCG-02 (agalliao - NT exulting-beyond-circumstance) belongs to Char 7 (Suffering-Joy) in its paradox-of-joy-in-suffering register. Several verses (1Pe 1:8; Mat 5:12; Rev 19:7) carry evidence for both characteristics simultaneously. Char 7 Phase 9 should treat M04-E-VCG-02 as primary evidence base.

---

## Self-check template (use at the end of EACH batch's findings file)

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

## After you finish each batch

1. Save the batch's findings to its own file (filename in the table above).
2. Ping CC: "M04 Char N (<name>) Phase 9 findings ready" — once per batch.
3. CC parses, validates, applies that file to cluster_finding with the right characteristic_id.
4. Begin the next batch.

If a batch is too large to fit in a single response, split it into segments by tier-pair (T0+T1, T2+T3, T4+T5, T6+T7) — same convention used for Char 2.

---

*End of brief. Load the structural input (#2) and begin Batch 1.*