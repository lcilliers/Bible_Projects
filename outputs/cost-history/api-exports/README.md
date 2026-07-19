# API usage exports — drop Console CSVs here

Direct Anthropic **API** usage (e.g. the IBA app's `read-passage` reading calls, or any
script that calls the Anthropic SDK) does **not** appear in Claude Code transcripts. It is
billed against your API account and is visible only in the **Anthropic Console**.

## How to feed it in

1. Go to **console.anthropic.com → Usage** (and **Cost**).
2. Export / download the usage as **CSV**.
3. Drop the CSV file(s) into this folder (`outputs/cost-history/api-exports/`).
4. Run `python scripts/cost_ledger.py`.

The ledger reads every `*.csv` here and folds it into the combined total.

## Columns the ledger understands

The reader is lenient about header names. It looks for (case-insensitive, common variants accepted):

| meaning | accepted header names |
|---|---|
| date | `date`, `day`, `usage_date`, `timestamp` |
| model | `model`, `model_id` |
| fresh input tokens | `input_tokens`, `input`, `uncached_input_tokens`, `prompt_tokens` |
| output tokens | `output_tokens`, `output`, `completion_tokens` |
| cache read tokens | `cache_read_input_tokens`, `cache_read`, `cache_read_tokens` |
| cache write tokens | `cache_creation_input_tokens`, `cache_write`, `cache_creation_tokens` |
| cost (optional) | `cost`, `cost_usd`, `amount`, `amount_usd` |

- If a **cost** column is present, the ledger uses it verbatim (that is your real billed cost).
- If not, it estimates cost from `scripts/token_cost_rates.json`, same as Claude Code.
- Missing token columns are treated as 0 — a partial export still contributes what it has.
