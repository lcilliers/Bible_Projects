# Combined cost ledger — Claude Code · API · Claude AI

> Rebuilt 2026-07-19T05:06:49Z. Tokens are exact where they exist; cost is estimated at the rates in `scripts/token_cost_rates.json` unless a source supplies real cost.
> **Claude Code billing detected: subscription [claude pro] (+extra-usage overage enabled).**

## ACTUAL MONEY (est.) — USD 117.95

> Claude Code runs on your **Claude subscription** — the same plan as claude.ai chat. Its per-token list value is shown below as a **reference only** and is **NOT** added to the money total; the flat subscription fee (record it in `cost_subscriptions.json`) is what covers it, plus any extra-usage overage. Only the **API** column is real pay-as-you-go spend.

| surface | tokens | USD | counts toward money? | fidelity |
| --- | --: | --: | --- | --- |
| Claude Code | 6,337,231,156 | 15,398.03 | no — subscription | exact tokens · list-price reference |
| Anthropic API (pay-as-you-go) | 17,928,204 | 117.95 | yes | estimated (per-model) |
| Subscription fees (Claude Code + chat) | n/a | 0.00 | yes | flat fee you recorded |
| **ACTUAL MONEY** | | **117.95** | | |

*Reference: Claude Code consumed USD 15,398.03 of usage at API list prices — the value you got from the subscription, not a charge.*

## 1. Claude Code — by project folder

| project folder | tokens | list value USD |
| --- | --: | --: |
| `c--Bible-study-projects` | 6,162,678,932 | 14,691.05 |
| `subagents` | 174,244,437 | 698.48 |
| `g--My-Drive-Bible-study-projects` | 256,680 | 6.95 |
| `G--My-Drive-Bible-study-projects--claude-worktrees-reverent-swanson-3a3822` | 51,107 | 1.55 |
| **all Claude Code** | **6,337,231,156** | **15,398.03** |

*This USD column is list-price VALUE, not a bill — Claude Code is on your subscription.*

Buckets: input 1,406,854 · cache-read 6,158,648,462 · cache-write 152,947,969 · output 24,227,871. For per-session/per-day Claude Code detail run `token_cost_history.py`.

## 2. Anthropic API — from Console exports (real pay-as-you-go)

Read 25 rows from 2 export file(s) spanning 2026-05-03 … 2026-06-19: `claude_api_tokens_2026_05.csv`, `claude_api_tokens_2026_06.csv`.

| model | input | output | cache-read | cache-write | est. USD |
| --- | --: | --: | --: | --: | --: |
| sonnet | 11,145,339 | 5,481,198 | 914,743 | 353,250 | 117.25 |
| opus | 30,529 | 3,145 | 0 | 0 | 0.69 |
| **total** | 11,175,868 | 5,484,343 | 914,743 | 353,250 | **117.95** |

Cost estimated (per-model). This IS separate pay-as-you-go spend, on top of the subscription. The upcoming lexical read-passage phase will add to this table.

## 3. Claude AI chat — subscription (flat)

claude.ai chat is not billed per token and has no usage export. Its cost is the monthly fee, recorded in `scripts/cost_subscriptions.json`.

| service | plan | USD/mo | months | subtotal | note |
| --- | --- | --: | --: | --: | --- |
| claude.ai chat |  | 0.00 | 0 | 0.00 | fill in your claude.ai subscription (Pro/Max/Team) and how many months you have paid |
| Claude Code / API plan |  | 0.00 | 0 | 0.00 | any flat plan fee, if applicable (leave 0 if you pay per-token API only) |
| **total** | | | | **0.00** | |

*(All zero — fill in `scripts/cost_subscriptions.json` with what you actually pay.)*

---
*Claude Code detail: `token-history.md`. This file is the roll-up across all three surfaces.*
