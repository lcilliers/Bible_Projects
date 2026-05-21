# M08 Phase 9 — Bundle (char2+3+4+5) — brief

**Cluster:** M08 — Pride, Arrogance and Boasting
**Characteristics in this bundle:** 2 (Presumptuous defiance), 3 (Boasting and self-display), 4 (Vain conceit), 5 (Pride of power and position)
**Total verses across the bundle:** ~144
**Total prompts to author:** 756 (= 189 × 4 separate passes)
**Task date:** 2026-05-21
**Audience:** Claude AI session

**Read this brief first.** Structural input is in a separate file referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M08/wa-cluster-M08-phase9-bundle-char2+3+4+5-brief-v1-20260521.md` | Primary task instructions |
| 2 | **Structural input** — `Sessions/Session_Clusters/M08/wa-cluster-M08-phase9-bundle-char2+3+4+5-input-v1-20260521.md` | Per-characteristic data blocks + shared 189-prompt catalogue + carry-forward observations |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |
| 4 | **Science extract** — `Workflow/Sciences/wa-m08-pride-scienceextract-v1_0-20260513.md` | Programme-curated scientific lens for T7.3 (human science framework) prompts — ensures consistent framing across clusters and reviewers |
| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |
| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

> The full 189-prompt T0–T7 catalogue is reproduced inside the structural input. No separate catalogue file required.

---

## Why this is a bundle (not a single characteristic)

This package covers **multiple characteristics** to save on session setup overhead. The data for each characteristic is kept distinct in the structural input — sub-groups, VCGs, and verses are grouped under their own characteristic block (§2.A, §2.B, …). **Do not pool evidence across characteristics.** Each 189-prompt pass uses ONLY that characteristic's evidence.

> Per researcher direction 2026-05-19: *"you can combine more than one characteristic in the dataset, but keep the grouping of the sub group distinctly separate into characteristics, and be clear in the guide to do separate batches of going through the catalogue."*

---

## ⚠️ STAGED EXECUTION PROTOCOL — MANDATORY ⚠️

**Known prior failure mode (M07 bundle, 2026-05-20):** the AI attempted to hold all 4 characteristics × 189 prompts in working memory and answer them as a continuous stream. It fell over twice — lost track of which batch was active, mixed evidence across characteristics, and produced inconsistent CHAR-N scope markers. **Do not repeat that pattern.**

This bundle is **a series of independent batches**, not a single 4×189 pass. Each batch must be **completed, written to disk, and confirmed** before the next batch begins.

### Hard procedural sequence

**For each batch, in the order listed below, you MUST:**

1. **OPEN BATCH** — announce: *"Starting Batch N — Characteristic N (<name>)"*.
2. **READ EVIDENCE** — read **every** verse-meaning in §3.{letter} of the structural input for THIS batch's characteristic. Do not look at any other §3 section.
3. **AUTHOR 189 PROMPTS** — work through T0..T7 in order. If a single response can't hold the whole batch, split by tier pair (T0+T1 → T2+T3 → T4+T5 → T6+T7) — but the batch is not finished until all 189 prompts have a finding row.
4. **WRITE THE FILE** — emit the complete findings document as a single contiguous markdown block, with the exact filename from the table below. Include the Self-check at the end.
5. **CONFIRM WRITTEN** — announce: *"Batch N file written: wa-cluster-M08-phase9-charN-<name>-findings-v1-20260521.md, 189/189 prompts, [CHAR-N] markers verified"*.
6. **STOP** — do not begin Batch N+1 in the same response. Wait for the next prompt from CC or the user. CC needs to validate Batch N's file before you start Batch N+1.

**Between batches, your working memory must reset.** Do not carry verse-citation patterns, finding language, or evidence summaries from one batch into another. The next batch starts fresh from §3.{next-letter}.

### Recovery if you find yourself drifting mid-batch

If at any point you notice you have:

- Cited evidence from another characteristic's §3 block,
- Mixed `[CHAR-N]` scope markers within one findings file,
- Skipped prompts "to come back later",
- Begun a second characteristic before the first file is written,

then: **STOP** the current response, announce the issue, abandon the half-written batch, and restart that batch from scratch (re-read §3.{letter}, re-author from T0.1.1). It is faster to restart cleanly than to patch a contaminated batch.

---

## Batch sequence

You will do **4 separate 189-prompt batches**, one per characteristic, in the order listed below. Each batch is fully bounded to its own characteristic.

| Batch | Characteristic | Sub-groups | Verses | §3 section | Output file (you produce) |
|---|---|---|---:|---|---|
| 1 | Char 2 — Presumptuous defiance | M08-B | ~45 | §3.A | `Sessions/Session_Clusters/M08/wa-cluster-M08-phase9-char2-Presumptuous-defiance-findings-v1-20260521.md` |
| 2 | Char 3 — Boasting and self-display | M08-C | ~70 | §3.B | `Sessions/Session_Clusters/M08/wa-cluster-M08-phase9-char3-Boasting-and-self-display-findings-v1-20260521.md` |
| 3 | Char 4 — Vain conceit | M08-D | ~12 | §3.C | `Sessions/Session_Clusters/M08/wa-cluster-M08-phase9-char4-Vain-conceit-findings-v1-20260521.md` |
| 4 | Char 5 — Pride of power and position | M08-E | ~17 | §3.D | `Sessions/Session_Clusters/M08/wa-cluster-M08-phase9-char5-Pride-of-power-and-position-findings-v1-20260521.md` |

**The batch is not finished until the file is on disk.** CC validates each file (parser-safe form, completeness, CHAR-N scope marker consistency) before Batch N+1 begins.

---

## Output format (applies to every batch)

Per prompt, one block; parser-safe form per v2_8 §12.4:

```
**T#.#.# — question text excerpt (optional)**

**[CHAR-N]** E — Finding text. Cite specific verses / VCGs / sub-groups from the characteristic's evidence block. Quote verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.

---
```

**Scope marker** is `**[CHAR-N]**` where **N is the characteristic number for that batch** (e.g., `**[CHAR-2]**` for the Presumptuous-defiance batch, `**[CHAR-3]**` for the Boasting batch). CC's loader uses this to set characteristic_id on each row, so it MUST match the current batch's characteristic — and never reference a characteristic that isn't this bundle's set (M08 has only CHAR-1..CHAR-5; CHAR-1 is a separate session, not in this bundle).

**Outcome codes:**
- **E** — evidenced; cite specific verses / VCGs
- **S** — silent; describe the analytical significance of the absence
- **G** — gap; describe what data would be needed to answer

---

## Discipline (per v2_8 §12)

1. **One batch per response (or one tier-pair segment per response for an oversized batch).** Never start a second characteristic in the same response that finished the first. The STOP gate is structural — it's how you avoid the prior-failure mode.
2. **Read every verse-meaning in the structural input for the current batch.** No sampling. The Pass A meanings condense each verse's inner-being content — read them all for the batch's characteristic.
3. **Per prompt, ground in specific evidence.** Every E finding names verses, VCGs, or sub-groups. The test for a good answer is *can I name what evidences this?*
4. **Fluency is not a quality signal** (v2_8 §2.4). Plausible-sounding text without specific citations is rejected.
5. **No sub-group-scope findings.** All findings at characteristic scope. Where evidence differs by sub-group within a characteristic, the finding text names the sub-group(s) inline.
6. **No cross-characteristic mixing.** Evidence from another characteristic's block is OFF-LIMITS for the current batch. If a cross-characteristic observation is significant, note it in the Self-check for that batch — do NOT embed cross-batch findings.
7. **No cluster-scope findings.** Cluster synthesis runs after all 5 characteristics finish.
8. **Self-check before submitting each batch** — confirm 189 prompts have rows; confirm every E names evidence; confirm every `[CHAR-N]` marker matches the batch's characteristic number, not another batch's.

---

## Carry-forward observations (apply per-batch)

These analytical hints were raised at characteristic-mapping time. Two statuses are shown: **OPEN** means action and flag at end of batch; **CONFIRMED** means already validated by an earlier Phase 9 batch — included here as context that may matter for the current batch's evidence selection.

### For Characteristic 3 (Boasting and self-display)

**INTER_RELATIONSHIP — M08-C boasting ↔ M22 praise/glory as register-adjacent through shared vocabulary** — **OPEN**

> Phase 3 cross-register analysis (per v2_7 §6.3.2 verse-level relationship test) confirmed the kauchaomai family (kauchaomai/kauchēma/kauchēsis) and ha.lal verb carry three distinct registers within M08-C's 70-verse corpus: (a) condemned self-directed boasting (M08-C-VCG-01); (b) Pauline examined-boasting discourse — boasting only in the Lord / in weakness / in the cross (M08-C-VCG-02); (c) God-directed glorying / praise (M08-C-VCG-03, the M22 register). The same lexemes express both M08 (self-boasting) and M22 (praise-of-God) inner-being content; the register-distinction is verse-level. Phase 9 T6 (Structural Relationships with Other Characteristics) should articulate the M08 ↔ M22 register-adjacency: praise becomes boasting when self-directed; boasting becomes praise when God-directed. When M22 opens, the M08-C-VCG-03 verses (~20-23 verses) and the relevant ha.lal verses may be picked up as cross-cluster contributions to M22's praise vocabulary.

At end of this batch, flag whether the observation surfaced as expected.

### For Characteristic 5 (Pride of power and position)

**INTER_RELATIONSHIP — M08-E pride-of-power ↔ M23 strength/dominion as misuse-of-faculty register** — **OPEN**

> Phase 3 cross-register analysis confirmed several M08-E terms (ga.on proud-might, archō domineering-authority, hupsēlofroneō wealth-pride, ma.rom fortified-elevation, shal.le.tet imperious self-will, a.din voluptuous ease, qo.mah Eze 19:11) carry their primary register in M23 (strength/power/dominion); they remain in M08 because their verses evidence strength-misused-as-self-exaltation. The pride-of-power register is structurally the M23 faculty turned inward toward self-aggrandisement. Phase 9 T6 should articulate the M08 ↔ M23 misuse-of-faculty pairing: M23 carries strength/capacity as the inner-being faculty; M08-E carries the corruption of that faculty when it becomes the ground for arrogance. When M23 opens, the M08-E sub-group's term list informs which strength terms have a documented misuse-pole at the verse level.

At end of this batch, flag whether the observation surfaced as expected.

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

## After you finish each batch — the STOP gate

1. **Write the batch's findings to its own file** using the exact filename from the batch sequence table.
2. **Self-check inside the file** — confirm 189 prompts have rows; confirm every E names evidence; confirm every `[CHAR-N]` marker matches the batch's characteristic number.
3. **Announce file written** — *"Batch N file written: <filename>, 189/189 prompts, [CHAR-N] markers verified"*.
4. **STOP**. Do not begin Batch N+1 in the same response. Wait for the next prompt.
5. CC validates and applies the batch's findings to `cluster_finding` with the right characteristic_id.
6. When CC confirms validation, you may begin Batch N+1 in a new response — starting from step 1 of the staged execution protocol (re-read §3.{next-letter} fresh).

If a single batch is too large to fit in one response, split that batch's authorship by tier-pair (T0+T1 → T2+T3 → T4+T5 → T6+T7) — but the batch is still ONE file with ONE filename. Don't fragment one batch across multiple files.

---

*End of brief. Load the structural input (#2) and begin Batch 1 (and only Batch 1).*