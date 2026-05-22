# M09 Phase 9 — Bundle (char2+3+4+5+6) — brief

**Cluster:** M09 — Humility, Meekness and Submission
**Characteristics in this bundle:** 2 (Submission), 3 (Contrition), 4 (Meekness and gentleness), 5 (Dignity), 6 (Willing-heartedness)
**Total verses across the bundle:** ~48
**Total prompts to author:** 945 (= 189 × 5 separate passes)
**Task date:** 2026-05-22
**Audience:** Claude AI session

**Read this brief first.** Structural input is in a separate file referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-bundle-char2+3+4+5+6-brief-v1-20260522.md` | Primary task instructions |
| 2 | **Structural input** — `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-bundle-char2+3+4+5+6-input-v1-20260522.md` | Per-characteristic data blocks + shared 189-prompt catalogue + carry-forward observations |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |
| 4 | **Science extract** — `Workflow/Sciences/wa-m09-humility-scienceextract-v1_0-20260513.md` | Programme-curated scientific lens for T7.3 (human science framework) prompts — ensures consistent framing across clusters and reviewers |
| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |
| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

> The full 189-prompt T0–T7 catalogue is reproduced inside the structural input. No separate catalogue file required.

---

## Why this is a bundle (not a single characteristic)

This package covers **multiple characteristics** to save on session setup overhead. The data for each characteristic is kept distinct in the structural input — sub-groups, VCGs, and verses are grouped under their own characteristic block (§2.A, §2.B, …). **Do not pool evidence across characteristics.** Each 189-prompt pass uses ONLY that characteristic's evidence.

> Per researcher direction 2026-05-19: *"you can combine more than one characteristic in the dataset, but keep the grouping of the sub group distinctly separate into characteristics, and be clear in the guide to do separate batches of going through the catalogue."*

---

## ⚠️ STAGED EXECUTION PROTOCOL — MANDATORY (two-level: batch and tier) ⚠️

**Known prior failure modes:** (a) M07 bundle (2026-05-20) — the AI tried to hold all 4 characteristics × 189 prompts in working memory and fell over twice (mixed evidence across characteristics, lost CHAR-N markers). (b) M09 CHAR-1 (2026-05-21) — the AI tried to process all 189 prompts in one pass and drifted (carried prior-tier reasoning into later tiers, performed analysis between tiers, substituted fluency for citation). **Do not repeat either pattern.**

This bundle is **two nested levels of staged execution**:

1. **Batch-level** — 4 batches, one per characteristic (Char 2 → Char 3 → Char 4 → Char 5). Each batch must be **completed, written to disk, and confirmed** before the next batch begins. CC needs to validate Batch N before you start Batch N+1.
2. **Tier-level (inside each batch)** — each batch's 189 prompts are split across 8 tiers (T0..T7). **One tier per response.** Each tier is announced, authored, appended to the batch's findings file, confirmed, and STOPPED before the next tier begins.

**Net effect:** ≈ 32 responses per bundle (4 batches × 8 tiers, plus Self-checks). That is the right cadence; you are not being asked to be fast. You are being asked to be correct.

### Tier breakdown (applies inside every batch)

Each batch's 189 prompts split across 8 tiers. Tier sizes: **T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20.** Tiers chain in one batch when self-evaluation passes; ALERT and stop only when self-evaluation surfaces an issue.

### Hard procedural sequence — per BATCH

For each batch in order:

1. **OPEN BATCH** — *"Starting Batch N — Characteristic N (<name>). Tier T0 next."*
2. **READ EVIDENCE FRESH** — read **every** verse-meaning in §3.{letter} for THIS batch's characteristic. Do not look at any other §3 section.
3. **Run the per-tier sequence (T0 → T7) with self-evaluation gates** — see next subsection.
4. **After T7's self-evaluation passes — final Self-check** — append the Self-check block for this batch.
5. **STOP at batch boundary** — do not begin Batch N+1 in the same response. CC validates Batch N's file before you start Batch N+1.

### Hard procedural sequence — per TIER (inside each batch)

For each tier T0 → T1 → … → T7 within the current batch:

1. **OPEN TIER** — *"Batch N · Tier T{N} — {tier title}."*
2. **RE-READ EVIDENCE** — re-read §3.{letter} for this tier's lens. Don't rely on memorised summaries from prior tiers.
3. **AUTHOR THIS TIER'S PROMPTS** — every prompt gets one finding block (parser-safe form below). No skipping. No "summarise the rest".
4. **WRITE TO FILE** — T0 CREATES the batch's findings file with the header + T0 section; T1..T7 APPEND each tier's `## T{N} — {title}` section. Each response shows the complete segment ready to be appended.
5. **SELF-EVALUATE the tier** — run the self-evaluation gate (see below).
6. **DECIDE: proceed or ALERT** —
   - If self-evaluation PASS: announce *"Batch N · Tier T{N} PASS — {n}/{n} prompts, [CHAR-N] markers verified. Proceeding to Tier T{N+1}."* Then immediately begin Tier T{N+1} in the SAME response.
   - If self-evaluation FAIL or surfaces a researcher-review item: announce *"Batch N · Tier T{N} ALERT — {issue}. Pausing for researcher review."* Then STOP. Wait for next prompt.

**Between tiers, working memory must reset.** Each tier re-reads §3 fresh with its own analytical lens. The chaining is procedural (same response); the analytical context is not.

**Between batches, working memory must reset.** Don't carry verse-citation patterns or finding language from Batch N into Batch N+1. The next batch starts fresh from §3.{next-letter}.

### Self-evaluation gate (run after every tier)

| # | Check | PASS criterion | If FAIL |
|---|---|---|---|
| 1 | **Prompt count** | Every prompt in the tier has a finding block (T0=12, T1=24, T2=31, T3=33, T4=24, T5=21, T6=24, T7=20) | ALERT — name the missing prompts |
| 2 | **Scope marker** | Every `[CHAR-N]` marker in this tier matches the current batch's characteristic | ALERT — name the wrong-marker prompts |
| 3 | **Citation discipline** | Every E finding cites at least one verse-ref or VCG code (e.g. `Pro 16:5`, `M09-C-VCG-01`) | ALERT — name the uncited E prompts |
| 4 | **No cross-tier mixing** | This tier's findings do not reference findings from a later tier | ALERT — name the cross-tier references |
| 5 | **Distinct evidence per prompt** | No two prompts share an identical 80-character opening | ALERT — name the shared-opening prompts |
| 6 | **Verse-corpus validity** | Verse references look like they belong to this characteristic's evidence corpus (cross-check from §3.{letter}); flag any cited verse that is not in §3.{letter} | ALERT — name the phantom-ref prompts |
| 7 | **No cross-batch mixing** | This tier's findings do not cite evidence from another characteristic's §3 block | ALERT — name the cross-batch references |

Document the self-evaluation result inline at the end of each tier section — one sentence per check, PASS or FAIL. If everything passes, the next tier follows immediately in the same response.

### What NOT to do (each is a drift signal)

- Authoring prompts from a tier you have not announced as OPEN
- Holding multiple tiers' worth of unwritten findings in your response (the file write is per-tier, even though tiers chain in one response)
- Skipping prompts "to come back later" — every prompt in a tier is answered before its self-evaluation
- Inter-tier or inter-batch analysis while a tier/batch is in flight — cross-tier patterns belong in the batch Self-check; cross-batch patterns belong in the cluster-synthesis session that runs after all batches finish
- Substituting fluency for citation — every E must name verses / VCGs from §3.{letter}
- Bulk-classifying prompts from a sample — each prompt is its own analytical pass
- Beginning Batch N+1 before Batch N's findings file is written and CC has validated
- Citing evidence from another characteristic's §3 block in the current batch
- Mixing `[CHAR-N]` scope markers within one batch's findings file

### Recovery if drift surfaces mid-tier

If during a tier you notice any of the drift signals above:

- **STOP** the current response immediately and announce the issue.
- Identify the level of drift (mid-tier vs cross-batch) and abandon the contaminated work.
- Re-read §3.{letter} fresh and restart the affected tier from its first prompt (or the affected batch from T0 if the contamination is cross-batch).

It is faster to restart cleanly than to patch a contaminated batch or tier.

---

## Batch sequence

You will do **5 separate 189-prompt batches**, one per characteristic, in the order listed below. Each batch is fully bounded to its own characteristic.

| Batch | Characteristic | Sub-groups | Verses | §3 section | Output file (you produce) |
|---|---|---|---:|---|---|
| 1 | Char 2 — Submission | M09-C, M09-D | ~36 | §3.A | `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-char2-Submission-findings-v1-20260522.md` |
| 2 | Char 3 — Contrition | M09-E | ~2 | §3.B | `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-char3-Contrition-findings-v1-20260522.md` |
| 3 | Char 4 — Meekness and gentleness | M09-F | ~2 | §3.C | `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-char4-Meekness-and-gentleness-findings-v1-20260522.md` |
| 4 | Char 5 — Dignity | M09-G | ~3 | §3.D | `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-char5-Dignity-findings-v1-20260522.md` |
| 5 | Char 6 — Willing-heartedness | M09-H | ~5 | §3.E | `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-char6-Willing-heartedness-findings-v1-20260522.md` |

**The batch is not finished until the file is on disk.** CC validates each file (parser-safe form, completeness, CHAR-N scope marker consistency) before Batch N+1 begins.

---

## Output format (applies to every batch)

Per prompt, one block; parser-safe form per v2_8 §12.4:

```
**T#.#.# — question text excerpt (optional)**

**[CHAR-N]** E — Finding text. Cite specific verses / VCGs / sub-groups from the characteristic's evidence block. Quote verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.

---
```

**Scope marker** is `**[CHAR-N]**` where **N is the characteristic number for that batch** (e.g., `**[CHAR-2]**` for the Submission batch, `**[CHAR-3]**` for the Boasting batch). CC's loader uses this to set characteristic_id on each row, so it MUST match the current batch's characteristic — and never reference a characteristic that isn't this bundle's set (M09 has only CHAR-1..CHAR-5; CHAR-1 is a separate session, not in this bundle).

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
7. **No cluster-scope findings.** Cluster synthesis runs after all 6 characteristics finish.
8. **Self-check before submitting each batch** — confirm 189 prompts have rows; confirm every E names evidence; confirm every `[CHAR-N]` marker matches the batch's characteristic number, not another batch's.

---

## Carry-forward observations (apply per-batch)

These analytical hints were raised at characteristic-mapping time. Two statuses are shown: **OPEN** means action and flag at end of batch; **CONFIRMED** means already validated by an earlier Phase 9 batch — included here as context that may matter for the current batch's evidence selection.

### For Characteristic 2 (Submission)

**INTER_RELATIONSHIP — M09 submission ↔ M30 (Obedience) register-adjacency** — **OPEN**

> CHAR-2 (Submission) is register-adjacent with the future M30 (Obedience/Disobedience) cluster. M09-C/D hupakoē/hupakouō/hupotagē/yiq.qe.hah carry the submission-of-will register; M30 will carry the broader obedience-as-action register. When M30 opens, M09-C/D evidence will inform M30's T6 relational findings. Cross-register flag carried forward.

At end of this batch, flag whether the observation surfaced as expected.

### For Characteristic 5 (Dignity)

**INTER_RELATIONSHIP — M09 dignity ↔ M08 pride as structural opposites** — **OPEN**

> CHAR-5 (Dignity, semnotēs) functions as the structural opposite of M08 (Pride) — grounded moral gravity vs proud self-display. The 3 semnotēs verses (1Ti 2:2, 1Ti 3:4, Tit 2:7) name the inner-grounded worth that does not require self-promotion. Phase 9 T6 should articulate the M09-G ↔ M08 polarity.

At end of this batch, flag whether the observation surfaced as expected.

### For Characteristic 6 (Willing-heartedness)

**INTER_RELATIONSHIP — M09 willing-heartedness ↔ M04 joy + M29 desire/will** — **OPEN**

> CHAR-6 (Willing-heartedness, na.div) overlaps with M04 (joy/delight — spontaneous generosity dimension) and M29 (desire/will — volitional readiness dimension). Psa 51:12 in particular pairs willing spirit with joy of salvation. When M04 / M29 open, the na.div corpus will inform their cross-cluster T6 findings.

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

1. The batch's findings file is built incrementally by tier: T0 created the file with the header + T0 section; T1..T7 each appended their section. Tiers chained automatically when their self-evaluations passed.
2. **After T7's self-evaluation passes** — append the final batch Self-check block — counts of E/S/G, carry-forward observations addressed, unexpected patterns, per-tier self-eval summary.
3. **Announce batch complete** — *"Batch N complete: <filename>, 189/189 prompts, [CHAR-N] markers verified, all per-tier evaluations PASS, Self-check posted."*
4. **STOP at batch boundary**. Do not begin Batch N+1 in the same response. Wait for the next prompt.
5. CC validates and applies the batch's findings to `cluster_finding` with the right characteristic_id.
6. When CC confirms validation, begin Batch N+1 in a new response — starting from the batch-level OPEN BATCH step.

**Cadence note:** One batch's 189 prompts may fit in one long response (if all per-tier self-evals pass and you chain straight through) or in 2-4 responses (if you split at tier boundaries to keep response length manageable). Either is fine. The hard constraints are: (a) per-tier self-evaluation gate; (b) per-tier file append; (c) no cross-batch chaining without CC validation. Bundle total: typically 4-8 responses for the authoring + 4 batch-Self-checks.

---

*End of brief. Load the structural input (#2) and begin **Batch 1 · Tier T0** in your first response. Chain tiers when self-evaluation passes; ALERT only on issues; STOP at batch boundaries.*