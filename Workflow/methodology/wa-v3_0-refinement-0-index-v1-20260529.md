# v3_0 refinement — review index

**Date:** 2026-05-29
**Status:** Discussion documents. No instruction-doc changes yet. Read in your own time.
**Supersedes the original combined document:** [wa-v3_0-refinement-discussion-v1-20260529.md](wa-v3_0-refinement-discussion-v1-20260529.md) (preserved as reference; the four below are the working set)

---

## Why four documents

The original combined document worked through five problems together. On reflection, the natural review structure is four focus areas, each addressing a coherent problem you can think about separately:

| Document | Problem it addresses | Read time |
|---|---|---:|
| [1 — Gate management](wa-v3_0-refinement-1-gate-management-v1-20260529.md) | Pipeline dead time and researcher attention. The 4-hour gap problem. | ~20 min |
| [2 — Prose generation](wa-v3_0-refinement-2-prose-generation-v1-20260529.md) | Phase E essay reads as sentence-by-sentence assembly, not integrated argument. | ~20 min |
| [3 — Process improvement](wa-v3_0-refinement-3-process-improvement-v1-20260529.md) | Re-run cycles in Phase B and D. Cost-time-quality tradeoffs. Division of labour between CC, AI chat, and API. | ~25 min |
| [4 — Quality control](wa-v3_0-refinement-4-quality-control-v1-20260529.md) | Per-phase hygiene gaps. Audit-after-prose. Bias-watch as discipline. | ~20 min |

Total: ~85 minutes across the four. The order isn't strict — Document 2 (prose) is the highest-impact for essay quality and can be read first. Document 1 (gates) is the one most likely to compress wall clock. Documents 3 and 4 are the supporting infrastructure that makes the first two reliable.

## What each document includes

Each is structured the same way:

1. **The problem, deeper.** What we actually saw in M38, with evidence. Where my original treatment was incomplete or surfaced thoughts without developing them.
2. **The model.** A way of thinking about the problem that makes the design choices follow naturally.
3. **Concrete proposals.** Specific artefacts, file formats, prompt sketches, code patterns — enough that you can imagine what it would look like, not just the principle.
4. **Open uncertainties.** What I'm not sure about. Where the proposal is a hypothesis rather than a known-good pattern.
5. **Questions for your review.** Not yes/no asks. Genuine decisions the design hangs on, framed for considered reflection rather than instant answer.

## How the four documents relate

The four problems are linked but the proposals can be adopted independently:

```text
            [Gate management]               [Prose generation]
                  │                                │
                  │                                │
              dashboard ──────────────────── vision document
              URGENT.md                       consistency pass
              gate-type taxonomy              integration pass
                  │                                │
                  │                                │
                  └─────► obslog ◄─────────────────┘
                              │
                              │
            [Process improvement]            [Quality control]
                  │                                │
            volume budgeting                  per-phase hygiene
            propose-validate-repair           anchor + verse-ref checks
            failure log                       end-of-D audit gate
            division of labour                bias-watch as discipline
            cost/time/quality                 forbidden vocabulary
                              │
                              │
                              ▼
                      ┌───────────────┐
                      │ v3_0 refined  │
                      └───────────────┘
```

The **obslog** is the cross-cutting artefact — every refinement writes to it or reads from it. The **gate-type taxonomy** (three types: mechanical, confirmation, judgment) underlies both the gate-management and quality-control documents. The **vision document** is specific to prose generation but loads into the obslog as one of the recorded artefacts.

The four can be adopted in any order. Document 2 (prose) gives the largest single quality lift; Documents 3 and 4 give the largest reliability and cost lift; Document 1 gives the largest wall-clock lift.

## What is NOT in any of these documents

- v3_0 instruction-doc edits themselves. Those come after you've decided what to adopt.
- Code to build any of this. The proposals describe what scripts would do, not the scripts themselves.
- Decisions about which clusters use which refinements. The refinements are designed to be opt-in per cluster.

## Your time-economic context

You have ~30–45 days of intense processing ahead to finish the analytic phase across the remaining clusters. M38 cost ~6 h 45 min active processing + ~5 h 45 min dead time and ~$9.40, producing a prose essay that the verdict called "not fluent" and a Phase D output that had 177 hygiene items.

If the refinements compress active processing by ~25%, eliminate the dead time, and produce integrated rather than sentence-by-sentence prose, the per-cluster economics shift substantially:

| Metric | M38 actual | Plausible after refinement |
|---|---:|---:|
| Active processing per cluster | 6 h 45 min | 4 h 30 min |
| Dead time per cluster | 5 h 45 min | < 30 min (if dashboard + auto-advance hold) |
| Wall clock per cluster | 12 h 30 min | 5 h |
| Cost per cluster | $9.40 | $7.50 (less rework) + ~$1.20 if E.0/E.2 go via API |
| Prose quality | sentence-by-sentence | integrated (vision document + consistency pass) |

Across 30 remaining clusters: ~225 hours of wall clock saved if these hold up. The cost of investment is the engineering time to build the supporting scripts — estimated at one full CC day distributed across M36 (~4–5 hours).

## Suggested review order

If you want to read in priority order:

1. **Document 2 (Prose)** first — the highest-leverage change. The vision document idea either resonates or it doesn't; that decision drives a lot.
2. **Document 4 (Quality)** second — the per-phase hygiene checks are the cheapest reliability gains and they're concrete.
3. **Document 1 (Gates)** third — the dashboard + URGENT.md + gate taxonomy. Wall-clock impact, modest engineering cost.
4. **Document 3 (Process)** last — the supporting infrastructure (volume budgeting, propose-validate-repair, failure log). Most engineering effort, slowest to show value, but compounds across the remaining clusters.

If you have less time and want to scan the questions only, each document's "questions for your review" section sits at the end.

---

*This index will be updated as you mark up the individual documents. Take your time. Nothing is committed until you tell me which refinements to adopt.*
