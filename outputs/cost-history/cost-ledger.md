# Combined cost ledger — Claude Code · API · Claude AI

> Rebuilt 2026-07-19T05:25:50Z. Tokens are exact where they exist; cost is estimated at the rates in `scripts/token_cost_rates.json` unless a source supplies real cost.
> **Claude Code billing detected: subscription [claude pro] (+extra-usage overage enabled).**

## ACTUAL MONEY (est.) — GBP 859.82

> Real money you have paid, in GBP: your **invoices** (which already cover Claude Code + claude.ai chat + overage on the one plan) plus separate **pay-as-you-go API**. Claude Code's per-token list value is a **reference only** — NOT a charge — because it is on the subscription.

| surface | native | in GBP | counts as money? |
| --- | --: | --: | --- |
| Claude Code (value consumed) | USD 15,402.42 | (covered by invoices) | no — on subscription |
| Anthropic API (pay-as-you-go) | USD 117.95 | 92.87 | yes |
| Subscription invoices (chat + Code + overage) | GBP 766.95 | 766.95 | yes |
| **ACTUAL MONEY** | | **859.82** | |

*Reference: Claude Code consumed **USD 15,402.42** of usage at API list prices — the value you extracted from the subscription, not a bill. You actually paid GBP 766.95 in invoices for it (with chat) + the API above.*

*API converted at USD 1.27/GBP (edit `fx` in cost_subscriptions.json).*

## 1. Claude Code — by project folder

| project folder | tokens | list value USD |
| --- | --: | --: |
| `c--Bible-study-projects` | 6,164,438,615 | 14,695.44 |
| `subagents` | 174,244,437 | 698.48 |
| `g--My-Drive-Bible-study-projects` | 256,680 | 6.95 |
| `G--My-Drive-Bible-study-projects--claude-worktrees-reverent-swanson-3a3822` | 51,107 | 1.55 |
| **all Claude Code** | **6,338,990,839** | **15,402.42** |

*This USD column is list-price VALUE, not a bill — Claude Code is on your subscription.*

Buckets: input 1,406,877 · cache-read 6,160,371,218 · cache-write 152,969,354 · output 24,243,390. For per-session/per-day Claude Code detail run `token_cost_history.py`.

## 2. Anthropic API — from Console exports (real pay-as-you-go)

Read 25 rows from 2 export file(s) spanning 2026-05-03 … 2026-06-19: `claude_api_tokens_2026_05.csv`, `claude_api_tokens_2026_06.csv`.

| model | input | output | cache-read | cache-write | est. USD |
| --- | --: | --: | --: | --: | --: |
| sonnet | 11,145,339 | 5,481,198 | 914,743 | 353,250 | 117.25 |
| opus | 30,529 | 3,145 | 0 | 0 | 0.69 |
| **total** | 11,175,868 | 5,484,343 | 914,743 | 353,250 | **117.95** |

Cost estimated (per-model). This IS separate pay-as-you-go spend, on top of the subscription. The upcoming lexical read-passage phase will add to this table.

## 3. Subscription invoices — the real bill (chat + Claude Code + overage)

claude.ai / Claude Code share one subscription; there is no per-token export for it. These are the actual invoices, recorded in `scripts/cost_subscriptions.json`.

12 invoices spanning 2026-01-23 … 2026-07-15.

| date | amount (GBP) | status | note |
| --- | --: | --- | --- |
| 2026-07-15 | 180.00 | Paid | reconstructed pairing — verify |
| 2026-07-12 | 12.62 | Paid | likely extra-usage overage |
| 2026-07-12 | 12.56 | Paid | likely extra-usage overage |
| 2026-06-15 | 90.00 | Paid | monthly subscription |
| 2026-05-15 | 90.00 | Paid | monthly subscription |
| 2026-04-15 | 90.00 | Paid | monthly subscription |
| 2026-04-07 | 40.50 | Paid | prorated/partial |
| 2026-03-15 | 90.00 | Paid | monthly subscription |
| 2026-03-02 | 0.00 | Paid |  |
| 2026-02-15 | -78.73 | Paid | credit / refund |
| 2026-02-01 | 60.00 | Paid |  |
| 2026-01-23 | 180.00 | Paid | initial signup (subscription created 2026-01-23) |
| **total** | **766.95** | | |

*Reconstructed from a pasted billing page — the total is exact; correct any date↔amount row.*

---
*Claude Code detail: `token-history.md`. This file is the roll-up across all surfaces.*
