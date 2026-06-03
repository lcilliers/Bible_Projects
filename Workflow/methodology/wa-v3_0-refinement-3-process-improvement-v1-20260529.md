# v3_0 refinement — 3. Process improvement

**Date:** 2026-05-29
**Status:** Discussion document. No instruction-doc changes yet.
**Reading time:** ~25 minutes
**Index:** [wa-v3_0-refinement-0-index-v1-20260529.md](wa-v3_0-refinement-0-index-v1-20260529.md)

---

## The problem, deeper

M38 had repeated re-run cycles that the original document treated as a single problem. They're actually several distinct problems with related but different fixes. Each cost real time and money; together they account for a significant slice of M38's wall clock and cost.

Looking at the M38 failure history:

| Phase | Failure | Root cause | Fix used | Time lost | Cost lost |
|---|---|---|---|---:|---:|
| B.2 design | 46 dups + 15 missing + 1 spurious | AI placed verses in multiple sub-groups; missed some | Repair API call with affected verses | ~25 min | ~$0.10 |
| B.3 M38-A | JSON truncation at 121 verses | Output exceeded max_tokens | Partial parse + targeted repair | ~30 min | ~$0.15 |
| B.3 E/F/G | Small coverage gaps | Coverage drift in design call | Targeted API repair | ~15 min | ~$0.05 |
| D.A chars 1/2/4/5/7 | q_code drift | AI numbered T0.1.1, T0.1.2… instead of using catalogue q_codes | Order-based remapping + re-run | ~45 min | ~$1.20 |
| D.B 4-segment | max_tokens truncation on every segment | Output volume across 4 segments × 7 chars exceeded limits | Switched to per-tier (8 calls) | ~60 min (abandoned segments) | ~$0.80 (sunk) |
| D.B T2/T3/T7 | Partial truncation on re-run | Output volume still high | Re-ran with max_tokens=24000 | ~20 min | ~$0.30 |

Total: ~3 hours 15 min and ~$2.60 in re-run cycles. Roughly half the Phase D Stage A and Stage B cost.

There are three distinct root causes here, and each calls for a different fix:

**Root cause 1: No output-volume budgeting up-front.** Each API call set `max_tokens` by guess. When the input had 121 verses requiring per-verse output, the response truncated. When the 4-segment approach asked for 28 prompts × ~350 words per response, it truncated on every segment.

**Root cause 2: Free-text output for structured data.** The AI was asked to produce verse assignments in markdown or loose JSON. Drift in formatting, q_code numbering, and field names was the result. Schema-constrained output via tool-use or response_format would have prevented this entirely.

**Root cause 3: No failure log.** Each failure was handled in conversation context, then forgotten. There's no place where "B.2 fails on coverage gaps in ~30% of runs" is recorded. We can't see whether the failure rate is improving across clusters. We can't refine the v3_0 instruction based on accumulated evidence.

There's also a fourth, larger-frame issue worth naming separately: the division of labour between CC, AI chat, and API isn't formalised in v3_0. M38 made on-the-fly choices about which work went where, leading to the cost-doubling problem you flagged (paying for subscription + paying for API). This is a methodological gap that deserves attention before M36.

---

## The model

### Each AI call has a budget — name it up-front

Every API call has three implicit budgets that should be explicit:

| Budget | What it measures | What happens when exceeded |
|---|---|---|
| **Input tokens** | Size of prompt + context | Cost increases; may exceed model limits |
| **Output tokens** | Expected response length | Truncation; rework |
| **Wall-clock time** | How long the call takes | Pipeline delay; researcher attention drift |

For a given task — say, designing VCGs for a 121-verse sub-group — you can estimate the output tokens before making the call:

```
expected_output_tokens =
    (num_verses × avg_tokens_per_verse_assignment)
  + (num_sub_groups × avg_tokens_per_sub_group_metadata)
  + structural_overhead
```

For VCG design, empirically: ~25 tokens per verse assignment (vc_id, sub-group code, brief reason) + ~80 tokens per VCG metadata + ~200 token overhead. A 121-verse sub-group needing 10 VCGs = 121×25 + 10×80 + 200 = 4,025 tokens. Set max_tokens = 6,000 (50% headroom). If the budget exceeds the model's limit, **split before calling**, not after truncation.

This is the budgeting discipline that M38 didn't have. Every API call in v3_0 should declare its expected output tokens and set max_tokens with stated headroom.

### Failures are data; capture them

When a call fails (truncation, schema drift, coverage gap, q_code drift), three things should happen:

1. The failure is logged with structured detail.
2. An automated recovery is attempted (propose-validate-repair).
3. If recovery succeeds, the success path becomes the validation step for future calls.

The current pipeline does (2) ad-hoc but doesn't do (1) or (3). Without (1), failures are forgotten. Without (3), the same kind of failure recurs cluster after cluster.

The failure log is the cheapest and highest-value addition. It's a markdown file per cluster with one entry per failure. Aggregated across clusters, it surfaces patterns: "B.2 coverage gaps occur in 60% of clusters; the design call needs schema constraint".

### Division of labour is a methodological decision, not an on-the-fly choice

The M38 cost-doubling problem (subscription paid + API costs incurred) wasn't a billing accident. It was the consequence of making per-task choices about CC vs API vs chat without an overall principle. The principle that emerged from M38's verdict:

- **API** is for high-volume atomic work that won't fit in chat — and where output quality at Sonnet-level is acceptable for the task.
- **Chat (Opus)** is for tasks where holistic context, judgment, and integrated voice matter — most prose work; complex AI decisions where the conversational refinement is itself part of the value.
- **CC** is for deterministic structural work, validation, file generation, DB writes, audit running.

For v3_0 each phase should declare its work split. The same task should not be done both via API and via chat duplicate; the choice should be made once per phase and documented.

---

## Concrete proposals

### A. Output-volume budgeting

Every API runner script declares its expected output volume before making the call, and sets `max_tokens` accordingly.

**The pattern in pseudo-code:**

```python
def estimate_output_tokens(task_shape):
    """Return expected output token count for a given task shape."""
    if task_shape.kind == "vcg_design":
        per_verse = 25
        per_vcg_meta = 80
        overhead = 200
        return (task_shape.num_verses * per_verse
                + task_shape.estimated_num_vcgs * per_vcg_meta
                + overhead)
    elif task_shape.kind == "subgroup_design":
        per_verse_assignment = 30
        per_subgroup_meta = 150
        return (task_shape.num_verses * per_verse_assignment
                + task_shape.num_subgroups * per_subgroup_meta
                + 300)
    # ... per task kind

def make_api_call(task_shape, system_prompt, user_message):
    estimated = estimate_output_tokens(task_shape)
    max_tokens = min(int(estimated * 1.5), MODEL_MAX_OUTPUT)  # 50% headroom
    if estimated * 1.5 > MODEL_MAX_OUTPUT:
        # Split the task before calling
        return split_and_call(task_shape, system_prompt, user_message)
    # Make the call with the budgeted max_tokens
    return client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
```

The constants per task kind (tokens per verse assignment, tokens per VCG metadata, etc.) are calibrated empirically from M38's outputs. Updated as more clusters run.

**Calibrated constants from M38 (initial estimates):**

| Task kind | Per-item tokens | Overhead |
|---|---:|---:|
| Sub-group design (per verse) | 30 | 300 |
| VCG design (per verse) | 25 | 200 + 80 per VCG |
| Constitution debate (per term) | 80 | 400 |
| Stage A finding (per prompt) | 350 | 200 |
| Stage B synthesis (per prompt) | 400 | 300 |
| Pass A meaning (per verse) | 120 | 200 |

These are starting points. As M36 runs, actual outputs feed back into the constants.

### B. Propose-validate-repair loop

Every analytical API call is wrapped in a standard loop:

```python
def propose_validate_repair(
    task_shape, system_prompt, user_message,
    validator, max_repair_iterations=2,
):
    """Make AI call, validate output, repair if needed, cap retries."""
    iteration = 0
    response = make_api_call(task_shape, system_prompt, user_message)
    while True:
        validation_result = validator(response)
        if validation_result.passed:
            return response
        if iteration >= max_repair_iterations:
            log_failure(task_shape, validation_result, "exceeded_retry_cap")
            raise FailureRequiresJudgmentGate(validation_result)
        # Build a repair user message
        repair_message = build_repair_message(
            original=user_message,
            response=response,
            gaps=validation_result.gaps,
        )
        response = make_api_call(task_shape, system_prompt, repair_message)
        iteration += 1
    log_failure(task_shape, validation_result, "succeeded_after_repair", iteration)
```

The validator is task-specific. For sub-group design: every relevant verse has exactly one assignment, all assignments are to known sub-groups, no duplicates. For VCG design: every verse has a group_id, all VCG metadata is complete, sub-group constraints respected. For Stage A findings: every prompt has a response, every response has a valid outcome code, q_codes match catalogue.

The repair_message tells the AI specifically what went wrong: "These 15 verses (list) have no assignment. These 46 verses (list) are assigned to multiple sub-groups (with conflicts). Provide a single assignment per verse for these 61 verses only."

After 2 failed repair attempts, the loop escalates to a judgment gate. You inspect the failure detail and decide whether to override, retry manually, or fix something upstream.

### C. The failure log

A markdown file per cluster, written to by every phase script.

**Path:** `Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-failure-log-v1-{date}.md`

**Format:**

```markdown
# M36 Service — Failure Log

This file records every API call failure and recovery during M36's pipeline run. Used for cross-cluster pattern analysis.

---

## Entry 1 — Pass A truncation
- **Timestamp:** 2026-05-30 08:42:13
- **Phase:** A — Pass A
- **Task shape:** 4 verses (of 312 total) — high-density meanings
- **Failure type:** output_truncation
- **Detected by:** schema validator (verses 145, 167, 198, 234 had no meaning text)
- **Root cause:** estimated 38400 tokens for 312 verses; actual output ran longer than budget on dense verses
- **Recovery:** propose-validate-repair iteration 1 (target the 4 truncated verses); succeeded in 28 seconds, cost $0.04
- **Cost lost:** $0.04 repair
- **Time lost:** 42 seconds

## Entry 2 — B.1 forbidden vocabulary
- **Timestamp:** 2026-05-30 09:23:45
- **Phase:** B.1 — Constitution debate
- **Task shape:** 7 terms
- **Failure type:** forbidden_vocabulary_in_reasoning
- **Detected by:** hygiene check (BOUNDARY reason for "diakonia" used "this is too vague" — not a valid §4.5.1 ground)
- **Root cause:** AI defaulted to imprecise language
- **Recovery:** propose-validate-repair iteration 1 with explicit ground list; succeeded
- **Cost lost:** $0.02
- **Time lost:** 38 seconds

[entries appended chronologically]
```

At cluster close, CC summarises the failure log into stats:

```markdown
## Summary

- Total entries: 12
- Failure types: output_truncation (4), forbidden_vocabulary (3), coverage_gap (3), q_code_drift (1), other (1)
- Total time lost: 4 min 12 sec
- Total cost lost: $0.28
- Recovery rate: 12/12 succeeded within 2 iterations
```

The per-cluster log feeds the cross-cluster analysis (proposal D).

### D. Cross-cluster failure pattern analysis

A script that reads all clusters' failure logs and produces:

**Path:** `outputs/markdown/wa-cluster-failure-analysis-v1-{date}.md`

**Content:**

- Failure rate by type, per phase, across clusters
- Recovery rate (1-iteration, 2-iteration, escalated-to-judgment)
- Failure types that appear in >50% of clusters → candidates for v3_0 instruction tightening
- Cost-of-failure as a percentage of total cost
- Time-of-failure as a percentage of total time

Run periodically (every 3–5 clusters) to inform v3_0 instruction refinement. The point: failures become data, and the data tells us what to fix structurally vs what to tolerate.

### E. Division of labour — formal declaration

Each phase in v3_0 declares its workload split:

| Phase | Work | Done by | Why |
|---|---|---|---|
| Pre-Phase A | Cluster scope verification, pre-analysis notes | Researcher + CC | Curatorial; needs your knowledge |
| Phase A — UT | Verse-level classification (IB-relevant vs set-aside) | **API (Sonnet)** | High-volume atomic; Sonnet quality acceptable |
| Phase A — Pass A | Meaning + keyword extraction per verse | **API (Sonnet)** | Same |
| Phase A — analytics | Keyword counts, summary statistics | **CC** | Deterministic |
| Phase B.1 — Constitution | Per-term inclusion debate | **Chat (Opus)** OR **API (Sonnet)** | Borderline. Chat for nuanced clusters, API for volume |
| Phase B.2 — Sub-groups | Sub-group design + verse assignment | **API (Sonnet)** with propose-validate-repair | High-volume; structured output; API acceptable |
| Phase B.3 — VCGs | Per-sub-group VCG design | **API (Sonnet)** per sub-group, parallel | High-volume; structured; API acceptable |
| Phase C | Apply structural decisions to DB | **CC** | Deterministic SQL transaction |
| Phase D Stage A — Char findings | 7 chars × catalogue prompts | **API (Sonnet)** with hygiene checks | High-volume; Sonnet quality acceptable for analytical findings |
| Phase D Stage B — Cluster synthesis | Cluster-scope synthesis findings | **API (Sonnet)** with hygiene checks | Same |
| Phase E.0 — Vision | Compose internal model of cluster | **Chat (Opus)** | Holistic; Opus quality essential |
| Phase E.1 — Chapter authoring | Per-chapter prose | **Chat (Opus)** | Same |
| Phase E.2 — Consistency | Cross-chapter edit list | **Chat (Opus)** | Same |
| Phase E.3 — Integration | Closing observation | **Chat (Opus)** | Same |
| Phase E.4 — Assembly + DOCX | Combine + render | **CC** | Deterministic |
| End-of-D audit | Hygiene + structural checks | **CC** | SQL + script |

The principle: API for volume where Sonnet is good enough; Chat (Opus) for prose and holistic judgment; CC for deterministic work. **No task is done by both API and chat.** This is what addresses the cost-doubling.

For M38, the table above would have moved nothing — the only place chat was used was the M38 essay drafting, and that's the same in the proposal. But it formalises the decision and prevents future drift.

### F. Memory and accumulated learning

Memory entries already accumulate (we're at 48+ entries in MEMORY.md). They're surfaced into context for every conversation. Their value compounds as more clusters complete.

The refinement: be more deliberate about what's a memory vs what's an instruction edit.

| Type | Goes where | Example |
|---|---|---|
| **Researcher preference** | Memory (feedback_*) | "Use markdown for all workings" |
| **Cluster-specific context** | Memory (project_*) | "M11 paused at Phase 9" |
| **Generally-applicable methodology rule** | v3_0 instruction edit | "Per-phase hygiene checks required" |
| **Pattern that's emerging across clusters** | Cross-cluster failure analysis → eventual instruction edit | "B.2 coverage gaps in 60% of clusters → schema constraint" |

The current memory directory has feedback memories that are really methodology rules ("phase 3 verse-level relationship test", "phase 5 sub-groups represent characteristics", "phase 9 tier-by-tier mandatory"). These are valuable but should migrate into v3_0 instruction proper, leaving memory for genuine researcher preferences and cluster-specific context.

Migration is not urgent. It can happen as v3_0 gets a v3_1 edit.

---

## Open uncertainties

1. **Whether the calibrated constants for output budgeting are right.** They're based on M38's actual outputs but only one cluster's worth. M36's actuals will refine them. They might be off by 30% in either direction.

2. **Whether schema-constrained output (tool-use or response_format) would be simpler than propose-validate-repair.** The proposal defers schema-constrained output because tool-use is more complex to wire and the propose-validate-repair pattern works. But if drift remains across 3+ clusters, schema constraint is worth the investment.

3. **Whether the 2-iteration repair cap is right.** Too few and we escalate to judgment unnecessarily; too many and we burn API spend in loops. 2 is a guess. Calibrate after M36.

4. **Whether the failure log will actually get used for cross-cluster analysis.** The log is cheap to write. Running the analysis is also cheap. But if nobody reviews the analysis output, the discipline degrades. Worth committing to a "review cadence" (e.g. every 3 clusters) up-front.

5. **Whether B.1 belongs in API or Chat.** B.1 has nuanced theological judgments. M38 ran it via API and one BOUNDARY (Act 27:34) was a mis-classification per the inner-being-full-scope memory. Maybe B.1 quality benefits from chat. But B.1 is also small enough (per-term debate) that the cost difference is marginal. Worth deciding.

6. **Whether the memory-vs-instruction division will hold.** Memories accumulate naturally; instructions require deliberate editing. The risk is that memory becomes a parallel methodology repository that's never folded into instructions. Counter-discipline: review memory monthly and migrate appropriate entries.

---

## Questions for your review

1. **Output volume budgeting** — does the principle hold? Are the calibrated constants close enough to be a starting point, or do you want them validated empirically on M36 before they're trusted?

2. **Propose-validate-repair with 2-iteration cap** — does 2 feel right? Higher? Lower? Configurable per phase?

3. **The failure log** — does the markdown format work, or would you prefer structured JSON / DB rows? Markdown is human-readable but harder to analyse; DB is the opposite.

4. **Cross-cluster failure analysis cadence** — every 3 clusters? Every batch (7)? On request?

5. **Division of labour table** — is the API/Chat/CC split correct as proposed? Specifically: B.1 in chat or API? Pass A in chat or API (volume suggests API but quality might suggest chat for some clusters)?

6. **Schema-constrained output** — defer (as proposed) or invest in it now? It's a real engineering project but it solves several drift problems at once.

7. **Memory-vs-instruction migration** — when to do it? Before M36? After this batch? Never (treat memories as the live methodology repository)?

---

## What changes in v3_0 instruction if this is adopted

- New §X.6 "Output volume budgeting" — declare expected output, set max_tokens with headroom, split if budget exceeds limit.
- New §X.7 "Propose-validate-repair loop" — the standard wrapper for analytical AI calls.
- New §X.8 "Failure log" — per-cluster log file and what goes in it.
- New §X.9 "Division of labour" — formal declaration per phase of who does what work.
- Minor edits to phase sections to reference the new sections.

## What CC needs to build

- Output-volume estimator (per-task-kind constants, helper function).
- Propose-validate-repair wrapper (Python function used by every API runner).
- Failure-log writer (called from every script that can fail).
- Cross-cluster failure analysis script (read all logs, produce report).

Estimated build time:
- Estimator + propose-validate-repair: ~2 hours.
- Failure log writer: ~30 minutes.
- Cross-cluster analysis: ~1 hour.

Total: ~3.5 hours of CC engineering. Recoups itself in M36 if it prevents even one major re-run cycle.

---

*Document 3 of 4. Next: [Document 4 — Quality control](wa-v3_0-refinement-4-quality-control-v1-20260529.md).*
