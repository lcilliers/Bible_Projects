# Session log — 2026-07-19 — Cost governance: an auditable token/cost ledger

> Handover record. Written at researcher instruction on session close.
>
> **State at close:** 4 commits · **nothing in either database was changed** — this session
> touched no DB at all. New tooling under `scripts/`, reports under `outputs/cost-history/`.
>
> **The whole session was one task: cost visibility.** The researcher opened with a serious
> grievance — thousands paid over ~6 months for little to show, no trust in self-reported token
> numbers. The session built a durable, auditable cost history from source-of-truth data, and in
> doing so **corrected a major misconception**: the scary five-figure "cost" was list-price
> *value*, not money paid. Real spend is ~**£860 over 6 months**.

---

## 1. The arc, in order

| # | what happened | outcome |
|---|---|---|
| 1 | *"Can I instruct you to write to disk a history of tokens/cost per cycle?"* | Yes — built it |
| 2 | Built `token_cost_history.py` — parses Claude Code transcripts (exact recorded usage) | **Done, committed** |
| 3 | *"does this cover API, Claude Code, and Claude chat?"* | Only Claude Code — surfaced the gap |
| 4 | Built `cost_ledger.py` — combined ledger across all 3 surfaces, per-source fidelity | **Done, committed** |
| 5 | *"does Claude Code consume the Claude AI chat subscription?"* | **Yes** — confirmed from local login |
| 6 | Detected billing: `stripe_subscription` / `claude_pro` → CC is on the subscription, not per-token | Corrected the model |
| 7 | Researcher supplied real API CSVs + made ledger subscription- & model-aware | **Done, committed** |
| 8 | Researcher pasted actual GBP invoices; ledger reworked to invoice model + GBP/USD combine | **Done, committed** |
| 9 | Decisions stated: one task/session · stay on Pro · use API for reading | Recorded to memory |
| 10 | Budget constraint: $15 credit, top-up at $5 → API reads must be small bounded batches | Recorded; folds into read-passage build |

---

## 2. Completed and committed

- **`scripts/token_cost_history.py`** — Claude Code detail (per-session / per-day / by-bucket) for this
  project. Tokens read straight from `~/.claude/projects/**/*.jsonl` (exact); cost = tokens × editable rates.
- **`scripts/cost_ledger.py`** — the roll-up across **all three surfaces**:
  1. Claude Code — auto, all project folders incl. `subagents` and the old Google-Drive folder.
  2. Anthropic API — ingests Console CSVs from `outputs/cost-history/api-exports/`, priced **per model**.
  3. Subscription — real **invoices** from `scripts/cost_subscriptions.json`, GBP, folded into the total via `fx`.
- **`scripts/token_cost_rates.json`** — editable rates; now carries per-model API rates (opus/sonnet/haiku).
- **`scripts/cost_subscriptions.json`** — the 12 real invoices (£766.95 total), reconstructed from the paste.
- **Reports** in `outputs/cost-history/`: `cost-ledger.md` (the roll-up), `token-history.md`, CSV ledgers.

Commits: token/cost history tool → combined ledger → subscription+model-aware → real GBP invoices.

---

## 3. The headline finding

| | amount | note |
|---|--:|---|
| **ACTUAL MONEY, ~6 months (Jan 23 – Jul 15)** | **£859.82** | the real, all-in figure |
| — subscription invoices (chat + Code + overage) | £766.95 | all Paid |
| — pay-as-you-go API (~$118, mostly Sonnet) | ~£93 | separate track |
| Claude Code "cost" at API list prices | **$15,402** | **VALUE consumed, NOT a bill** |

- **Claude Code is on the Pro subscription** (`billingType=stripe_subscription`, `organizationType=claude_pro`,
  `hasExtraUsageEnabled=True`). It shares the one plan with claude.ai chat. The $15k is list-price value —
  roughly **18× the value of what was actually paid**.
- **87% of Claude Code consumption is context** (cache-read 61% + cache-write-1h 26%), only ~12% is generated
  output. Cost scales with session length — every turn re-reads the whole conversation. Marathon sessions
  (1,500–2,000 requests) each consumed $2,000+ of list value.
- The two small **July 12 charges** (£12.62 + £12.56) are extra-usage **overage** above the plan limit.

---

## 4. Decisions & operating rules (recorded to memory)

- **One task per session** + `/clear` between tasks — kills the cache-read pileup, stays inside the flat Pro fee.
- **Stay on Pro**; **use the API for verse reading** (separate pay-as-you-go track).
- **API reads = small bounded batches** — `--limit`/per-book scope · pre-run cost estimate · checkpoint+resume ·
  budget-stop. **Never a full-corpus push** ($15 credit, top-up at $5; full corpus ≈ $600–900 Sonnet). Sonnet default.
- Memories written: `feedback_token_cost_history_required`, `project_api_reads_budget_bounded_small_batches`.

---

## 5. Open / next

- **Keep the ledger current:** export a fresh API CSV into `outputs/cost-history/api-exports/` periodically and
  re-run `python scripts/cost_ledger.py`. Add new invoice lines as they arrive. Correct any invoice date↔amount
  pairing (the £766.95 total is exact; the per-row dates are a reconstruction).
- **Before the reading run:** raise the **API spend limit** enough to complete a book.
- **Still awaiting confirmation (prior session):** the lexical-phase plan
  (`iba/app/docs/lexical-phase-plan-v1-20260719.md`) — its §9 open decisions. The `read-passage` operation, when
  built, must be **budget-bounded per §4** above.
- Outstanding registry item (unchanged): `blindness (spiritual` (malformed name, not built) — decision pending.
