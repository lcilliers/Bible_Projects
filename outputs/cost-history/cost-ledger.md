# Combined cost ledger — Claude Code · API · Claude AI

> Rebuilt 2026-07-19T04:51:58Z. Tokens are exact where they exist; cost is estimated at the rates in `scripts/token_cost_rates.json` unless a source supplies real cost.

## GRAND TOTAL — est. USD 15,392.70

| surface | tokens | est. USD | fidelity |
| --- | --: | --: | --- |
| Claude Code | 6,335,137,981 | 15,392.70 | exact tokens · estimated cost |
| Anthropic API | — | 0.00 | no export loaded |
| Claude AI chat | n/a | 0.00 | subscription-flat (no tokens exist) |
| **total** | | **15,392.70** | |

## 1. Claude Code — by project folder

| project folder | tokens | est. USD |
| --- | --: | --: |
| `c--Bible-study-projects` | 6,160,585,757 | 14,685.73 |
| `subagents` | 174,244,437 | 698.48 |
| `g--My-Drive-Bible-study-projects` | 256,680 | 6.95 |
| `G--My-Drive-Bible-study-projects--claude-worktrees-reverent-swanson-3a3822` | 51,107 | 1.55 |
| **all Claude Code** | **6,335,137,981** | **15,392.70** |

Buckets: input 1,406,823 · cache-read 6,156,602,214 · cache-write 152,919,997 · output 24,208,947. For per-session/per-day Claude Code detail run `token_cost_history.py`.

## 2. Anthropic API — from Console exports

**No API export loaded.** Direct API spend (e.g. the app's reading calls, the research subagent's monthly-limit spend) lives only in the Anthropic Console and is **NOT** counted above until you add it.

To include it: export CSV from **console.anthropic.com → Usage**, drop it in `outputs\cost-history\api-exports/`, re-run. See that folder's `README.md`.

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
