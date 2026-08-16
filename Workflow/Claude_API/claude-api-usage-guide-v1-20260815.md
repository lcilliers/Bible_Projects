# Claude API — Usage Guide

> Reference doc for using the **Claude API** (the raw `POST /v1/messages` endpoint — distinct from
> this Claude Code chat) in this project. Written 2026-08-15 because the researcher stated the
> Claude API will be used **extensively in the new analytic phase** and will be **integrated into
> the IBA App**. This doc is the technical "how" — model IDs, request shapes, cost mechanics. The
> project's binding governance for any step that spends real money through it is
> [`iba/app/GOVERNANCE.md`](../../iba/app/GOVERNANCE.md) §30/§31 (below); this doc doesn't restate
> that as a rule, it points to it.
>
> Related: [`outputs/markdown/project-review-response-2-20260815.md`](../../outputs/markdown/project-review-response-2-20260815.md)
> §1 covers *when* to reach for the API vs. Claude Code chat vs. Managed Agents — read that first if
> the question is "which surface." This doc assumes the answer is already "the API" and covers *how*.

---

## 1. There is already a live, working integration — start there, not from scratch

Before this doc existed, one real Claude-API-calling step was already built, governed, and running:
`report.book_narrative_generate` (`iba/app/lib/narrativegenerate.py`, registered by
`iba/app/migration/bootstrap_book_narrative_generate.py`, governed by `GOVERNANCE.md` §30). Any new
analytic-phase work that calls the API should follow the same shape unless there's a specific reason
not to — it's already been through the researcher's approval and one config-maintenance cycle.

**The established pattern, in order:**

1. **Assemble the package** (instructions + content) entirely from files/DB — no network call yet.
2. **Estimate cost** before touching the network (character-count heuristic in the existing code;
   §5 below has the exact `count_tokens` endpoint to upgrade that estimate with).
3. **Hard-refuse over a configured cap** (`cost-cap-exceeded`) — no call, no escalation, nothing spent.
4. **Escalate for approval below the cap** (`needs-approval`, pause-continue) — the same escalation
   shape every other spend/write step in this app uses (`registry.create`, `configmaint.propose`).
   The live call only happens once that run_id comes back `approve`.
5. **Make the one live call.**
6. **Log the REAL usage** (from the response's own `usage` block, not the estimate) to an append-only
   CSV audit trail — `narrative.usage_log_path` is the precedent field name.

Every value that shapes the call — model, output-token ceiling, both cost rates, the cost cap, the
output path/filename pattern, the usage-log path — is a `cfg_setting` (module `narrative` in the
precedent), never a literal in the handler. That's not a style preference; it's
`governance.rules_must_be_config_driven` (`iba/app/GOVERNANCE.md`) applied to this specific case.
**A new analytic-phase step that calls the API needs its own `cfg_setting` rows and its own
`bootstrap_*` migration, following this same precedent — not a hand-rolled call inline in a
handler.**

## 2. Why this codebase uses raw `requests`, not the `anthropic` SDK

`iba/app/lib/narrativegenerate.py`'s own docstring states the reason: the IBA app has **exactly one
Python dependency** (`requests` — see `USER-GUIDE.md` §1), and the Messages API is a plain JSON
POST, so a second dependency isn't justified for one endpoint. This is a deliberate, already-made
architectural decision, not an oversight — **don't add the `anthropic` SDK as a dependency without
raising that as its own decision first.** Everything in this doc is written against the raw HTTP
shape for that reason, even where the general Claude API skill's default guidance is "use the
official SDK."

**The shape, unchanged from the existing code:**

```python
import requests

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"

resp = requests.post(
    API_URL,
    headers={
        "x-api-key": api_key,
        "anthropic-version": API_VERSION,
        "content-type": "application/json",
    },
    json={
        "model": model,               # cfg_setting, never a literal
        "max_tokens": max_output_tokens,
        "system": instructions,
        "messages": [{"role": "user", "content": content}],
    },
    timeout=600,
)
if resp.status_code != 200:
    raise ApiCallFailed(f"Messages API returned {resp.status_code}: {resp.text[:500]}")
data = resp.json()
text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
usage = data.get("usage", {})
```

**Auth.** `ANTHROPIC_API_KEY` is read from the environment, falling back to the repo-root `.env`
(never committed — `.gitignore` already excludes it). Per `GOVERNANCE.md` §30, this is the one
deliberate exception to the IBA app's own "no secrets, no `.env`" boundary, and it's not a new key —
it's the same key the legacy (non-IBA) pipeline's `scripts/_run_ve_reads_governed.py` and
`_apply_*_via_api_*.py` scripts already use. **Never log, print, or write the key's value anywhere**
— not in a report, not in an escalation payload, not in a commit.

## 3. Current models and pricing (accurate as of this doc's date)

| Model | Model ID | Input $/1M | Output $/1M | Context | Notes |
|---|---|---|---|---|---|
| Claude Opus 5 | `claude-opus-5` | $5.00 | $25.00 | 1M | Deep reasoning, hardest analytic judgment calls |
| Claude Sonnet 5 | `claude-sonnet-5` | $3.00 (**$2.00 intro through 2026-08-31**) | $15.00 (**$10.00 intro**) | 1M | Already the default in `narrative.generate_model` — the right default for most analytic-phase work: near-Opus quality on structured/classification work at a fraction of the cost |
| Claude Haiku 4.5 | `claude-haiku-4-5` | $1.00 | $5.00 | 200K | Simple, high-volume, speed-critical classification only |

**The Sonnet 5 intro price expires 2026-08-31** — re-check `shared/models.md` in the `claude-api`
skill (or `https://platform.claude.com/docs/en/pricing.md`) after that date before trusting a cost
estimate against the discounted rate. Never guess a model ID — copy it verbatim from this table or
re-derive it via the `claude-api` skill; a wrong ID 404s.

**Routing rule** (from the project-review-response-2 doc, restated here for the technical context):
same rules/input/output shape every run, no per-run human judgment → Claude API call, config-driven,
`output_config.format` for the shape guarantee. A genuine investigation or judgment call stays in
Claude Code chat.

## 4. Building blocks relevant to the analytic phase

The existing `report.book_narrative_generate` step uses only the bare minimum (system + messages +
`max_tokens`). The features below are what the *new* analytic-phase work is likely to actually need
— each is a plain addition to the same JSON body, no SDK required.

### 4.1 Structured outputs — the direct fix for "consistency and quality could not be achieved"

This is the mechanism the project-review-response-2 doc pointed at as the fix for the old method's
free-form-question inconsistency. Add `output_config.format` to the request body; the response is
then *guaranteed* to match the schema — no free-text parsing, no drift between runs:

```python
"output_config": {
    "format": {
        "type": "json_schema",
        "schema": {
            "type": "object",
            "properties": {
                "finding": {"type": "string"},
                "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
            },
            "required": ["finding", "confidence"],
            "additionalProperties": False,
        },
    }
},
```

Parse `resp.json()["content"][0]["text"]` as JSON — `output_config.format` guarantees it's valid
JSON matching the schema, so no retry-on-parse-failure loop is needed (unlike the old prefill-based
approach). Incompatible with citations; fine with everything else used here.

### 4.2 Effort — the cost/quality dial

`output_config.effort`: `low` / `medium` / `high` / `xhigh` / `max`, default `high`. For
high-volume, per-verse-level classification work (structured, narrow, repeatable), start at `low` or
`medium` and measure — `narrative.generate_max_output_tokens`-style config already exists for output
ceilings; add an `effort` setting alongside it per step, same pattern.

### 4.3 Thinking

`thinking: {"type": "adaptive"}` — on Claude Sonnet 5 this is the default even if omitted. For
narrow, structured, single-shot classification calls (the bulk of what an analytic phase does),
thinking usually isn't needed and can be left off (`{"type": "disabled"}`) to save cost — but note
Sonnet 5 respects `disabled` only when paired with `effort` at `high` or below (Opus-5-specific rule;
irrelevant on Sonnet 5, but worth knowing if a step later moves to Opus).

### 4.4 Prompt caching — cost reduction for repeated instructions

Every analytic-phase call that reuses the same instructions doc (a hard-constraints file, a method
doc, a catalogue) across many verses/terms is a caching candidate. Add `cache_control` to the stable
`system` block:

```python
"system": [
    {"type": "text", "text": instructions, "cache_control": {"type": "ephemeral"}}
],
```

Cache reads cost ~0.1× the base input price. **Minimum cacheable prefix is 1024 tokens on Sonnet 5**
— a short instructions doc won't cache; check `usage.cache_read_input_tokens` in the response to
confirm it's actually hitting, not silently missing. This is the highest-leverage single change for
"extensive" analytic-phase usage, since the same governing docs get resubmitted on every call today
(`narrativegenerate.py`'s `assemble_package` rebuilds the full instructions string every time with
no cache marker).

### 4.5 Batch API — the right shape for bulk analytic runs

If the analytic phase's shape is "run the same kind of call over many verses/terms, not
latency-sensitive" (which most of it plausibly is, per `feedback_iba_no_synthesis_small_units_only`
and `project_api_reads_budget_bounded_small_batches` — small bounded batches, not a full-corpus
push), the Batch API is the better fit than one-call-per-verse:

- `POST /v1/messages/batches` — up to 100,000 requests or 256 MB per batch, **50% off standard
  pricing**, results within an hour typically (max 24h).
- Poll `processing_status` until `"ended"`, then stream `batches.results(id)` — results arrive in
  any order, keyed by `custom_id`, never by position.
- Still raw HTTP-compatible: the batch endpoints are plain JSON POST/GET, same auth header, no SDK
  needed — the "one dependency" constraint doesn't force one-call-at-a-time.

Given the project's own bounded-batch discipline, this is worth a real evaluation before the
analytic phase scales up: batching + caching together could cut the per-verse cost substantially
below today's single-call approach.

### 4.6 Token counting — a real pre-call estimate, not the char/4 heuristic

`narrativegenerate.py`'s cost estimate is `(len(instructions) + len(content)) // 4` — a rough
heuristic the code's own comment flags as such. The real endpoint:

```python
resp = requests.post(
    "https://api.anthropic.com/v1/messages/count_tokens",
    headers={"x-api-key": api_key, "anthropic-version": API_VERSION, "content-type": "application/json"},
    json={"model": model, "system": instructions, "messages": [{"role": "user", "content": content}]},
)
input_tokens = resp.json()["input_tokens"]
```

Free to call, no `max_tokens` billing. Worth adopting for any new cost-cap check — it replaces a
rough estimate with the actual pre-call number, tightening the `cost-cap-exceeded` gate.

## 5. What NOT to do

- **Don't add the `anthropic` SDK dependency** without raising it as its own decision — the
  single-dependency policy is deliberate (§2).
- **Don't hardcode model IDs, rates, paths, or caps** in a handler — every one of them is a
  `cfg_setting`, changeable via `configmaint.propose`, per `governance.rules_must_be_config_driven`.
- **Don't call the API before a pre-call cost estimate and cap check** — the hard-refuse-over-cap /
  escalate-under-cap two-step (§1, steps 2–4) is the governed pattern for every spend step in this
  app, not just the narrative one.
- **Don't skip the usage-log write** — every live call's real `usage` block goes to an append-only
  CSV, same as `narrative.usage_log_path`. Without it, `scripts/cost_ledger.py` (which only ingests
  Console CSV exports) has no record of this app's own live calls.
- **Don't use `claude-opus-5` as a default** for high-volume structured work without a specific
  reason — Sonnet 5 is already the established default (`narrative.generate_model`) and is
  substantially cheaper for near-equivalent quality on structured/classification tasks.
- **Never write the API key's value into a file, report, escalation payload, or commit.**

## 6. Pointers

- **Live implementation:** [`iba/app/lib/narrativegenerate.py`](../../iba/app/lib/narrativegenerate.py)
- **Registration migration (the `bootstrap_*` pattern to copy for a new step):**
  [`iba/app/migration/bootstrap_book_narrative_generate.py`](../../iba/app/migration/bootstrap_book_narrative_generate.py)
- **Binding governance:** `iba/app/GOVERNANCE.md` §30 ("the first step that spends real money, and
  how config governs that") and §31 (session-pacing guidance as config, token-consumption
  diagnostic).
- **Session-cost precedent:** `iba/app/reports/token-consumption-diagnostic-20260802.md` — ≈1.13M
  tokens moved through one large session; the reason `passage.debate_session_chapter_guideline`
  exists as a paced-batch config value.
- **The Claude Code vs Claude API routing question:**
  [`outputs/markdown/project-review-response-2-20260815.md`](../../outputs/markdown/project-review-response-2-20260815.md) §1.
- **Full API reference** (models, structured outputs, batches, caching, effort, thinking, error
  codes): the `claude-api` skill available in this Claude Code environment — invoke it for anything
  not covered above, rather than working from memory of the API shape.
