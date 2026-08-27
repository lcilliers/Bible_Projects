---
name: project_api_reads_budget_bounded_small_batches
description: "API verse-reads must be small bounded batches with a pre-run cost estimate — never a full-corpus push; ~$15 credit, top-up at $5."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7a3d6e48-d97f-407e-83ba-ecef211af3af
---

The API (verse-reading / lexical read-passage phase) is pay-as-you-go, SEPARATE from the Pro subscription. Budget is tight: ~**$15 credit, auto top-up when it hits $5**. This works for smallish units but MUST NOT be used for a bulk push of thousands of reads at once.

**Why:** a full-corpus run would cost ~$600–900 on Sonnet (17,824 passages × ~$0.03–0.05 each; ~5× on Opus) — it would exhaust credit and hammer the top-up. The researcher explicitly wants reads structured around small units.

**How to apply — the `read-passage` operation must be budget-bounded by design:**
1. **Scope small** — per book, or `--limit N`; one run = a few hundred reads max (~$10 headroom ≈ 200–300 Sonnet reads).
2. **Estimate before spending** — dry-run prints "≈ $X for N passages" before any API call; never run blind.
3. **Checkpoint + resume** — store each read as it completes (same resumable pattern as the base build); a batch can stop and continue without re-reading.
4. **Stop on budget** — configurable ceiling halts the run before credit is exhausted, not after.
5. **Model choice is the cost dial** — Sonnet ≈ 1/5 of Opus per token. Default reads to the cheaper model unless depth demands Opus; the cost ledger prices per-model.

Fold this into `iba/app/docs/lexical-phase-plan-v1-20260719.md` when the operation is built. Related: [[feedback_token_cost_history_required]], [[feedback_simple_steps_not_engineered_designs]], [[project_per_book_corrective_pipeline]].
