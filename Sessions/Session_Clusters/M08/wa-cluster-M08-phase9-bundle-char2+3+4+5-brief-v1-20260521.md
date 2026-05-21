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

## ⚠️ STAGED EXECUTION PROTOCOL — MANDATORY (two-level: batch and tier) ⚠️

**Known prior failure modes:** (a) M07 bundle (2026-05-20) — the AI tried to hold all 4 characteristics × 189 prompts in working memory and fell over twice (mixed evidence across characteristics, lost CHAR-N markers). (b) M08 CHAR-1 (2026-05-21) — the AI tried to process all 189 prompts in one pass and drifted (carried prior-tier reasoning into later tiers, performed analysis between tiers, substituted fluency for citation). **Do not repeat either pattern.**

This bundle is **two nested levels of staged execution**:

1. **Batch-level** — 4 batches, one per characteristic (Char 2 → Char 3 → Char 4 → Char 5). Each batch must be **completed, written to disk, and confirmed** before the next batch begins. CC needs to validate Batch N before you start Batch N+1.
2. **Tier-level (inside each batch)** — each batch's 189 prompts are split across 8 tiers (T0..T7). **One tier per response.** Each tier is announced, authored, appended to the batch's findings file, confirmed, and STOPPED before the next tier begins.

**Net effect:** ≈ 32 responses per bundle (4 batches × 8 tiers, plus Self-checks). That is the right cadence; you are not being asked to be fast. You are being asked to be correct.

### Tier breakdown (applies inside every batch)

Each batch's 189 prompts split across 8 tiers. Tier sizes: **T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20.** One tier per response.

### Hard procedural sequence — per BATCH

For each batch in order:

1. **OPEN BATCH** — *"Starting Batch N — Characteristic N (<name>). Tier T0 next."*
2. **READ EVIDENCE FRESH** — read **every** verse-meaning in §3.{letter} for THIS batch's characteristic. Do not look at any other §3 section.
3. **Run the per-tier sequence (T0 → T7)** — see next subsection.
4. **After T7 — Self-check response** — post the Self-check block for this batch.
5. **STOP** — do not begin Batch N+1 in the same response. CC validates Batch N's file before you start Batch N+1.

### Hard procedural sequence — per TIER (inside each batch)

For each tier T0 → T1 → … → T7 within the current batch:

1. **OPEN TIER** — *"Batch N · Tier T{N} — {tier title}."*
2. **RE-READ EVIDENCE** — re-read §3.{letter} for this tier's lens. Don't rely on memorised summaries from prior tiers.
3. **AUTHOR THIS TIER'S PROMPTS** — every prompt gets one finding block (parser-safe form below). No skipping. No "summarise the rest".
4. **WRITE TO FILE** — T0 CREATES the batch's findings file with the header + T0 section; T1..T7 APPEND each tier's `## T{N} — {title}` section. Each response shows the complete segment ready to be appended.
5. **CONFIRM WRITTEN** — *"Batch N · Tier T{N} written: <filename>, {n}/{n} prompts, [CHAR-N] markers verified."*
6. **STOP** — do not begin Tier T{N+1} in the same response.

**Between tiers, working memory must reset.** Do not carry prior-tier reasoning or finding patterns into the next tier. Each tier re-reads §3 fresh with its own analytical lens.

**Between batches, working memory must reset.** Don't carry verse-citation patterns, finding language, or evidence summaries from Batch N into Batch N+1. The next batch starts fresh from §3.{next-letter}.

### What NOT to do (each is a drift signal)

- Authoring prompts from a tier you have not announced as OPEN
- Holding multiple tiers' worth of unwritten findings in one response
- Skipping prompts "to come back later"
- Inter-tier or inter-batch analysis while a tier/batch is in flight — finish current, write, STOP. Cross-tier patterns belong in the batch Self-check; cross-batch patterns belong in the cluster-synthesis session.
- Substituting fluency for citation — every E must name verses / VCGs from §3
- Bulk-classifying prompts from a sample — each prompt is its own analytical pass
- Beginning Batch N+1 before Batch N's findings file is written and validated
- Citing evidence from another characteristic's §3 block in the current batch
- Mixing `[CHAR-N]` scope markers within one batch's findings file

### Recovery if you find yourself drifting

If at any point you notice any of the things in the "NOT to do" list:

- **STOP** the current response immediately and announce the issue.
- Identify the level of drift (mid-tier vs cross-batch) and abandon the contaminated work.
- Re-read §3.{letter} fresh and restart the affected tier from its first prompt (or the affected batch from T0 if the contamination is cross-batch).

It is faster to restart cleanly than to patch a contaminated batch or tier.

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

1. The batch's findings file is built incrementally by tier: T0 created the file with the header + T0 section; T1..T7 each appended their section.
2. **Post the batch Self-check** (separate response, after T7's STOP) — counts of E/S/G, carry-forward observations addressed, unexpected patterns.
3. **Announce batch complete** — *"Batch N complete: <filename>, 189/189 prompts, [CHAR-N] markers verified, Self-check posted."*
4. **STOP**. Do not begin Batch N+1 in the same response. Wait for the next prompt.
5. CC validates and applies the batch's findings to `cluster_finding` with the right characteristic_id.
6. When CC confirms validation, begin Batch N+1 in a new response — starting from the batch-level OPEN BATCH step.

**One batch = one file = 8 tier-segments + 1 Self-check segment (≈ 9 responses).** Bundle total: 4 × 9 ≈ 36 responses. That is the right cadence; you are being asked to be correct, not fast.

---

*End of brief. Load the structural input (#2) and begin **Batch 1 · Tier T0** (and only that) in your first response.*