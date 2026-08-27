# M09 Phase 9 — Synthesis completion (missing 99 prompts) — brief

**Cluster:** M09 — Humility, Meekness and Submission
**Phase:** 9 cluster-synthesis completion (gap-fill)
**Task date:** 2026-05-22
**Audience:** Claude AI session

---

## Context — why this brief exists

The first M09 cluster-synthesis AI session (2026-05-22) produced 90 of 189 expected `[CLUSTER]` prompt blocks. It dropped the .2/.3 follow-up prompts across tiers T2-T7 — likely a working-memory issue (could not hold the full 189-prompt × 6-char matrix at once). T0 and T1 are fully complete (36 / 36 prompts ✓). The prose appendix is also complete.

Your task: **author cluster-scope findings ONLY for the 99 missing prompts listed below.** The 90 prompts already authored are not in scope — do not re-author or revise them.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-synthesis-missing-brief-v1-20260522.md` | Primary task instructions |
| 2 | **Structural input (gap-fill)** — `Sessions/Session_Clusters/M09/wa-cluster-M09-phase9-synthesis-missing-input-v1-20260522.md` | The 99 missing prompts, each with its 6 per-characteristic findings stacked |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |
| 4 | **Science extract** — `Workflow/Sciences/wa-m09-humility-scienceextract-v1_0-20260513.md` | Programme-curated scientific lens for T7.3 prompts |
| 5 | **Existing synthesis (reference only)** — `Sessions/Session_Clusters/M09/files phase 9/wa-cluster-m09-phase9-cluster-synthesis-findings-v1-20260522.md` | Read T0/T1 + the 90 already-authored prompts for context if needed; do NOT re-author |
| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Missing prompts (the 99 in scope) — by tier

**T2** (17 prompts): T2.10.2, T2.10.3, T2.2.2, T2.2.3, T2.3.3, T2.4.2, T2.4.3, T2.5.2, T2.5.3, T2.6.2, T2.6.3, T2.7.2, T2.7.3, T2.8.2, T2.8.3, T2.9.2, T2.9.3

**T3** (20 prompts): T3.1.3, T3.10.2, T3.10.3, T3.11.2, T3.11.3, T3.2.2, T3.2.3, T3.3.2, T3.3.3, T3.4.3, T3.5.2, T3.5.3, T3.6.2, T3.6.3, T3.7.2, T3.7.3, T3.8.2, T3.8.3, T3.9.2, T3.9.3

**T4** (17 prompts): T4.1.3, T4.1.4, T4.2.2, T4.2.3, T4.2.4, T4.3.2, T4.3.3, T4.3.4, T4.4.2, T4.4.3, T4.4.4, T4.5.1, T4.5.3, T4.5.4, T4.6.2, T4.6.3, T4.6.4

**T5** (14 prompts): T5.1.3, T5.2.1, T5.2.2, T5.2.3, T5.3.2, T5.3.3, T5.4.2, T5.4.3, T5.5.2, T5.5.3, T5.6.2, T5.6.3, T5.7.2, T5.7.3

**T6** (17 prompts): T6.1.2, T6.1.3, T6.2.2, T6.2.3, T6.3.2, T6.3.3, T6.3.4, T6.4.2, T6.4.3, T6.4.4, T6.5.2, T6.5.3, T6.5.4, T6.6.2, T6.6.3, T6.7.2, T6.7.3

**T7** (14 prompts): T7.1.2, T7.1.3, T7.1.4, T7.1.5, T7.1.6, T7.1.7, T7.1.10, T7.2.1, T7.2.2, T7.2.3, T7.2.4, T7.2.5, T7.2.6, T7.3.2

---

## What you are producing

For each of the 99 missing prompts, author ONE cluster-scope finding examining what surfaces when the 6 characteristics' findings are compared.

### Output format

Use the SAME parser-safe format as the cluster-synthesis session:

```
**T#.#.# — question text excerpt (optional)**

**[CLUSTER]** E — Cluster-scope finding text. Cite specific characteristics by name and the specific patterns/divergences/anchors they reveal when compared.

---
```

**Scope marker** is `**[CLUSTER]**` (CC's loader sets characteristic_id=NULL, finding_status='cluster_synthesis'). Do NOT use [CHAR-N] markers in the output.

**Outcome codes:**
- **E** — evidenced; comparative pattern across chars supports a cluster-scope answer
- **S** — silent; no meaningful cluster-level pattern beyond per-char answers
- **G** — gap; cluster-level pattern would require evidence the 6 chars' findings don't supply

---

## ⚠️ TIER-BY-TIER STAGED EXECUTION — MANDATORY ⚠️

**Known prior failure:** the prior synthesis session dropped 99 of 189 prompts when trying to hold the whole matrix in working memory. **Do not repeat that pattern.** This narrowed brief is exactly the gap-fill — proceed tier-by-tier with self-evaluation between.

### Hard procedural sequence (per tier)

Tiers to process: T2 → T3 → T4 → T5 → T6 → T7 (T0/T1 already complete; not in scope).

For each tier in this brief's missing-prompt scope, you MUST:

1. **OPEN TIER** — announce: *"Starting Tier T{N} — {missing prompt count} missing prompts to author."*
2. **READ THE STACKED FINDINGS** — for each missing prompt in this tier, re-read the 6 stacked per-characteristic findings in §3 of the structural input. Do not rely on memorised summaries from prior tiers.
3. **AUTHOR THIS TIER'S MISSING PROMPTS** — one cluster-scope finding per missing prompt. No skipping. No "I'll come back later".
4. **WRITE TO DISK** — emit the tier's complete missing-prompt section as a contiguous markdown block. Each block has a `## T{N} — gap-fill` header (or similar) and the missing prompts with their findings below.
5. **SELF-EVALUATE** — run the gate (see below).
6. **PROCEED or ALERT** — if PASS, immediately begin next tier in the same response; if FAIL, announce ALERT and STOP.

### Self-evaluation gate (per tier)

| # | Check | PASS criterion | If FAIL |
|---|---|---|---|
| 1 | **Prompt count** | All missing prompts in this tier authored | ALERT — name the still-missing prompts |
| 2 | **Scope marker** | Every block uses `**[CLUSTER]**` (no `[CHAR-N]`) | ALERT |
| 3 | **Citation discipline** | Every E finding names which characteristics contribute what; ideally also names specific verses where relevant | ALERT |
| 4 | **No re-authoring** | Did not author or revise any of the 90 already-present prompts | ALERT |
| 5 | **Distinct findings** | No two prompts share an identical 80-char opening | ALERT |

Document the self-evaluation inline at the end of each tier block.

---

## Output structure

Write your output as a single markdown file at:

`Sessions/Session_Clusters/M09/files phase 9/wa-cluster-M09-phase9-synthesis-missing-findings-v1-20260522.md`

Suggested document structure:

```markdown
# M09 Phase 9 — Synthesis gap-fill — findings

**Date:** 2026-05-22
**Scope:** 99 missing prompts (T2-T7 follow-up subprompts)
**Prompts authored:** 99 / 99

## T2 — gap-fill (17 prompts)

**T2.2.2 — [question text]**

**[CLUSTER]** E — finding text comparing how the 6 characteristics answer this...

---

[... rest of T2 missing prompts ...]

T2 self-evaluation: 17/17 ✓ scope-clean ✓ ... → PASS. Proceeding to T3.

## T3 — gap-fill (20 prompts)
...
```

At the end of T7, after the last self-evaluation passes, post a final Self-check:

```markdown
## Self-check

- Missing prompts authored: 99 / 99 ✓
- All blocks use **[CLUSTER]** scope marker ✓
- Per-tier evaluations: T2 ✓ T3 ✓ T4 ✓ T5 ✓ T6 ✓ T7 ✓
- No re-authoring of the 90 existing prompts ✓
```

---

## After T7 + Self-check

1. Confirm the gap-fill findings file is on disk.
2. Ping CC: "M09 synthesis gap-fill ready".
3. CC merges the gap-fill into the existing 90-prompt synthesis file, validates the merged 189-row total, applies to `cluster_finding` (finding_status='cluster_synthesis').

---

*End of brief. Load the structural input (#2) and begin **Tier T2** in your first response.*