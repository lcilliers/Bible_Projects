# v2_9 vs v3_0 — Cycle Comparison

> **SUPERSEDED (2026-06-14)** by the v3_2 cluster-rollup model — `wa-cluster-rollup-design.md` / `wa-cluster-rollup-instruction-v3_2-DRAFT-20260607.md`. Retained for reference (v3_0 design phase); see `outputs/markdown/project-reconstruction/04-open-loops-and-incomplete-methodology-20260614.md` §4. Archiving pending the cleanup register.

**Date:** 2026-05-27
**Status:** Pre-write analysis for v3_0 instruction. Quantifies the cycle / re-read reduction.
**Sources:**
- `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_9-20260526.md` (1,813 lines)
- `Workflow/Instructions/wa-sessionc-cluster-overview-v1_0-20260513.md`
- `Workflow/Instructions/wa-v3_0-final-review-v1-20260527.md` (with researcher §3 amendments)

Working assumption: **N = 7 characteristics per cluster** (the M03/M15/M01/M05/M06 norm; M20=4 / M39=2 / M46=4 are below median, M10/M11=2-3 are split clusters).

---

## §1. Phase-by-phase side-by-side

| v2_9 phase | v2_9 cycle | v3_0 phase | v3_0 cycle | Net change |
|---|---|---|---|---|
| **P1** UT verse review | CC API · 1 op | **A.1** UT verse review | CC API · 1 op | Same |
| **P2** Pass A meaning + keywords | CC API · 1 op | **A.2** Pass A meaning + keywords | CC API · 1 op | Same (already collapsed under v2_9) |
| **P3** Constitution debate | AI chat · 1 session, reads corpus | **B.1** Constitution debate | folded into Phase B single corpus read | -1 corpus read |
| **P4** Apply term transfers + BOUNDARY | CC · 1 op | **C.1** Apply transfers + BOUNDARY | CC · 1 op (folded with C.2/C.3) | -1 ceremonial op |
| **P5** Sub-group formation | AI chat · 1 session, reads Pass-A meanings | **B.2** Sub-group formation | folded into Phase B single AI session | -1 AI session |
| **P6** Verse → sub-group routing | CC · 1 op | **C.2** Sub-group structural apply | CC · 1 op (folded into C) | -1 ceremonial op |
| **P7** VCG design within sub-groups | AI chat · 1 session, reads Pass-A meanings | **B.3** VCG design | folded into Phase B single AI session | -1 AI session |
| **P8** Silent VCG dissolution | CC · 1 op | **C.3** Inherited-VCG cleanup | CC · no-op for post-split clusters; bulk-soft-delete already applied 2026-05-27 | -1 ceremonial op |
| **P8.5** BOUNDARY resolution (conditional) | AI chat · 0–1 session | **C.4** BOUNDARY resolution (conditional) | AI chat · 0–1 session | Same (conditional) |
| **P8.7** Characteristic load | CC silent (v2_8+) | **C.5** Characteristic load | CC silent | Same |
| **P9** Catalogue prompts — per-char + synthesis | AI chat · N+1 = **8 sessions** | **D** Analytics findings — per-char + synthesis | AI chat · N+1 = **8 sessions** | Same count, but no embedded prose |
| *(Session C ch1–ch7)* | AI chat · **7 chapter sessions** + 1 appendix = 8 sessions | **E** Publication prose — per-char tier prose + cluster synthesis prose | AI chat · N+1 = **8 sessions**, reads findings table not corpus | Same session count; corpus re-reads → 0 |
| **P10** Inherited-finding reconciliation | AI chat · 1 session (conditional, mostly no-op for post-v2_6) | **F.1** Inherited-finding fold (conditional) | CC · 1 op + optional AI; folds into F | -1 AI session in normal case |
| **P11** Inherited-finding fold + validation | CC · 1 op | **F.2** Validation (11-check) | CC · 1 op | Same |
| **P12** Cluster closure | CC · 1 op | **F.3** Closure (status flip) | CC · 1 op | Same |
| *(Session C assembly)* | CC · 1 op | **Pub** CC assembly from `prose_section` | CC · 1 op | Same |

---

## §2. Cycle totals per cluster (N=7 characteristics)

### §2.1 AI chat sessions

| Layer | v2_9 | v3_0 | Δ |
|---|---:|---:|---:|
| Phase 3 / Phase 5 / Phase 7 (grouping work) | 3 | 1 *(Phase B, segmented if needed)* | **−2** |
| Phase 8.5 BOUNDARY (conditional) | 0–1 | 0–1 | 0 |
| Phase 9 / Phase D (per-char + synthesis) | 8 | 8 | 0 |
| Phase 10 reconciliation (conditional) | 0–1 | 0 *(folded into F)* | **−0 to −1** |
| Session C / Phase E publication prose | 8 | 8 *(but no verse re-read)* | 0 |
| Session C → CC assembly | — | — | 0 |
| **Total AI chat sessions** | **19–21** | **17–18** | **−2 to −3** |

Note: the headline AI-session reduction is modest. The session count of Phase E mirrors Session C's chapter+appendix count. **The dramatic savings are elsewhere — see §2.2 and §2.3.**

### §2.2 AI verse-corpus reads (the heavy-cost reads)

A "verse-corpus read" is an AI session that must ingest the cluster's verse evidence (Pass A meanings + verse text) into its working memory. These dominate AI cost.

| Layer | v2_9 | v3_0 | Δ |
|---|---:|---:|---:|
| Phase 3 (constitution debate reads corpus) | 1 | 0 *(folded into B)* | **−1** |
| Phase 5 (sub-group formation reads Pass-A meanings) | 1 | 0 *(folded into B)* | **−1** |
| Phase 7 (VCG design reads Pass-A meanings) | 1 | 0 *(folded into B)* | **−1** |
| Phase B (single corpus read for grouping) | — | 1 | **+1** |
| Phase 9 / Phase D (8 sessions reading characteristic verse evidence) | 8 | 8 | 0 |
| Session C chapters 1–7 (7 sessions each reading curated verse evidence) | 7 | 0 *(replaced by Phase E reading findings table)* | **−7** |
| Phase E (8 sessions reading **findings table only** — no verse re-read) | — | 0 corpus-reads (lightweight finding-row reads instead) | 0 (cheap reads) |
| **Total verse-corpus reads** | **18** | **9** | **−9 (50% reduction)** |

This is the single biggest win in v3_0 — **half the verse re-reads disappear**, because:
1. Phases 3+5+7 read the corpus three times under v2_9; Phase B reads it once.
2. Session C's seven chapter sessions each re-read the verse corpus from a different angle; Phase E reads only the `cluster_finding` table (which is the same data flattened into rows of analytical text — much smaller, no need to read raw verses).

### §2.3 CC mechanical operations

| Layer | v2_9 | v3_0 | Δ |
|---|---:|---:|---:|
| Phase 1 / A.1 — UT review | 1 | 1 | 0 |
| Phase 2 / A.2 — Pass A | 1 | 1 | 0 |
| Phase 4 — Term transfers + BOUNDARY directives | 1 | folded into C | **−1** |
| Phase 6 — Sub-group routing | 1 | folded into C | **−1** |
| Phase 8 — VCG dissolution | 1 | folded into C | **−1** |
| Phase 8.7 — Characteristic load | 1 | folded into C | **−1** |
| Phase C — Structural cleanup (one consolidated op) | — | 1 | **+1** |
| Phase 11 — Fold + validation | 1 | folded into F | **−1** |
| Phase 12 — Closure | 1 | folded into F | **−1** |
| Phase F — Validation + closure (one consolidated op) | — | 1 | **+1** |
| Session C → CC assembly | 1 | 1 | 0 |
| **Total CC ops** | **8** | **4** | **−4 (50% reduction)** |

Half the ceremonial CC ops disappear by phase consolidation.

### §2.4 Decision-cycle round-trips (researcher review gates)

| Layer | v2_9 | v3_0 |
|---|---:|---:|
| After P3 constitution debate (researcher reviews transfers) | 1 | — *(B integrated)* |
| After P5 sub-group design (researcher reviews) | 1 | — *(B integrated)* |
| After P7 VCG design (researcher reviews) | 1 | 1 *(at end of B)* |
| After P8.5 BOUNDARY (conditional) | 0–1 | 0–1 |
| After P8.7 characteristic map (under v2_8+ silent) | 0 | 0 |
| Per Phase 9 / D batch (researcher reviews findings) | 8 | 8 |
| After Phase 9 / D synthesis (researcher reviews) | 1 | 1 |
| After Phase E tier-prose / chapter draft (per char) | 7 | 7 |
| After Phase E cluster prose | 1 | 1 |
| After validation + closure | 1 | 1 |
| **Researcher review gates** | **21–22** | **20–21** | 

Net: −1 review gate. The big benefit isn't fewer gates, it's that the gates that remain see CLEANER artefacts (consolidated Phase B output instead of three separate review docs).

---

## §3. Re-read elimination — the v3_0 publication pipeline

The Session C → Phase E shift is worth unpacking. Under v2_9:

```
Phase 9 batch (AI session 1): reads char's verse corpus, writes 189 findings
                              [findings live in cluster_finding table]
                                       ↓
                              [days / weeks later]
                                       ↓
Session C Ch1 (AI session A): reads char's verse evidence (T0+T1 lens) — corpus re-read
Session C Ch3 (AI session B): reads char's verse evidence (T0 spine) — corpus re-read
Session C Ch4 (AI session C): reads char's verse evidence (T2+T3 lens) — corpus re-read
Session C Ch5 (AI session D): reads char's verse evidence (T4+T5 lens) — corpus re-read
Session C Ch6 (AI session E): reads char's verse evidence (T6 lens) — corpus re-read
Session C Ch7 (AI session F): reads char's verse evidence (T7 lens) — corpus re-read
                              [each session re-derives analytical context AI already produced]
```

Under v3_0:

```
Phase D batch (AI session 1): reads char's verse corpus, writes 189 findings to cluster_finding
                                       ↓
                              [days / weeks later]
                                       ↓
Phase E batch (AI session A): reads the char's 189 findings from cluster_finding,
                              writes T0 / T1 / ... / T7 tier-prose to prose_section
                              [no verse re-read; the findings ARE the analytical content]
                                       ↓
CC assembly: per-chapter mapping (see §2.3 of publication-pipeline-design)
             joins tier-prose blocks into chapter-shaped Markdown
             writes combined publication output
```

**Quantification.** A typical Phase 9 batch sees ~150–400 verses in its characteristic. Each verse in the corpus carries ~150–400 tokens of Pass-A meaning + raw text + cross-refs. So one batch ingests roughly 30k–150k tokens of verse evidence. Seven Session C chapters per characteristic would re-ingest similar volumes seven times — **roughly 200k–1M tokens of redundant verse re-read per characteristic, per cluster**.

Across the programme's remaining ~30 clusters × 7 characteristics × 7 chapters: **~40M–200M tokens of verse re-read avoided** by switching to the findings-driven Phase E + CC assembly.

That is the v3_0 productivity headline. AI session *count* drops modestly; the *cost per session* drops sharply because Phase E sessions read findings (small, structured) not verses (large, prose).

---

## §4. Where v3_0 keeps the cycle count instead of reducing it

Honest accounting — not everything shrinks:

1. **Phase D = Phase 9.** Same 8 AI sessions per cluster. The characteristic-scoped batch model is unchanged. v3_0 doesn't shrink it because the per-prompt × per-characteristic structure is the analytical unit.

2. **Phase E ≈ Session C session count.** 7 per-char tier-prose sessions + 1 cluster-synthesis prose session ≈ 7 Session C chapters + 1 appendices session. Session count is conserved; the saving is in read cost (corpus → findings).

3. **Phase B is larger than P3 alone.** Phase B consolidates 3 v2_9 phases (P3+P5+P7) into one session. The corpus read is single, but the AI session is heavier. Researcher direction (§3.1 of final review): segment Phase B internally to avoid AI overload; emit progressive obslog. Cycle reduction is real, but session length grows.

4. **Conditional phases remain conditional.** P8.5 BOUNDARY resolution is still conditional under Phase C; if a cluster has unresolved BOUNDARY, the AI session is still needed.

---

## §5. Summary scoreboard

For a typical N=7 cluster going through the full pipeline end-to-end:

| Dimension | v2_9 | v3_0 | Δ | % |
|---|---:|---:|---:|---:|
| AI chat sessions | 19–21 | 17–18 | −2 to −3 | ~10–14% |
| **AI verse-corpus reads** | **18** | **9** | **−9** | **−50%** |
| CC mechanical ops | 8 | 4 | −4 | −50% |
| Researcher review gates | 21–22 | 20–21 | −1 | ~5% |
| Session C AI sessions | 8 | 0–1 | −7 to −8 | −88% to −100% |

**The headline number is the corpus re-read reduction (−50%) and the Session C collapse (−88% to −100%).** Other dimensions move modestly.

---

*v1 — 2026-05-27. Quantification basis for v3_0 §20 "Why v3_0 — the changes from v2_9".*

---

## §6. Corrigendum (2026-05-27, post Phase B control design)

After researcher raised the Phase B procedural anomaly (control gates within the consolidated phase), the design was tightened — see [`wa-v3_0-phase-b-control-design-v1-20260527.md`](wa-v3_0-phase-b-control-design-v1-20260527.md).

Conclusion: **AI session count for the grouping work is unchanged between v2_9 (P3+P5+P7) and v3_0 (B.1+B.2+B.3) — three AI sessions in both.** The §2.1 row labelled "Phase 3 / Phase 5 / Phase 7 (grouping work)" claiming a v3_0 reduction to "1 session" is incorrect.

Revised §2.1 AI session totals for an N=7 cluster:

| Layer | v2_9 | v3_0 (revised) |
|---|---:|---:|
| Grouping work (B/P3+5+7) | 3 | **3** (not 1) |
| Phase 8.5 BOUNDARY (conditional) | 0–1 | 0–1 |
| Phase D/9 (per-char + synthesis) | 8 | 8 |
| Phase 10 reconciliation (conditional) | 0–1 | 0 |
| Phase E / Session C publication prose | 8 | 8 |
| **Total AI sessions** | **19–21** | **19–20** | 

Net AI session reduction is **0–1 per cluster** (not −2 to −3 as claimed in §5).

**The Phase B savings are real but not in session count:**

- **Three CC structural applies → one (Phase C)** — directives consolidate.
- **Three input pack builds → one shared input scaffolding** — constitution report, keyword analytics, Pass A meaning corpus load once and are referenced across B.1/B.2/B.3.
- **Analytical context builds progressively** — AI does not cold-start three times.
- **One v3_0 phase boundary** in obslog and status discipline instead of three v2_9 phase boundaries.

**The headline reductions in §2.2 (verse-corpus reads) and §2.3 (CC ops) and the Session C collapse remain correct and unchanged.** They are the substantive v3_0 win — Phase B contributes structural cleanliness, not cycle count.

This corrigendum is incorporated in [`wa-sessionb-cluster-instruction-v3_0-20260527.md`](wa-sessionb-cluster-instruction-v3_0-20260527.md) §21.5.
