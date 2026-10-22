"""lexicalenrichgenerate.py — the shared Anthropic Messages API call layer of the LLM-calling
stages (#1549): the API key lookup, `call_api`, `log_usage` and their exceptions, imported by
`versereadinggenerate`, `subgroupgenerate`, `charreadinggenerate` and `charanswergenerate`.

**Config-driven**: URL, API version, model, token limits, rates, cost cap and log path are
`cfg_setting` rows (module `lexical`). The lexical.run Layer 2 package builder that once lived
here was retired with that step (#2207).
"""

from __future__ import annotations

import os
import pathlib


class ApiKeyMissing(Exception):
    """ANTHROPIC_API_KEY not found in the environment or repo-root .env."""


class ApiCallFailed(Exception):
    """The Messages API returned a non-2xx response."""


def _api_key() -> str:
    """ANTHROPIC_API_KEY from the environment, else from the repo-root .env (shared by every
    LLM-calling stage)."""
    key = os.getenv("ANTHROPIC_API_KEY")
    if key:
        return key
    env_path = pathlib.Path(".env")
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("ANTHROPIC_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                if key:
                    return key
    raise ApiKeyMissing("ANTHROPIC_API_KEY not set in the environment or found in .env at the "
                        "repo root -- add it there (never commit it)")


class CostCapExceeded(Exception):
    """A single batch's estimated cost exceeds lexical.llm_max_cost_per_batch."""


class BadModelResponse(Exception):
    """The model's reply doesn't contain a parseable JSON object with a 'notes' or 'remove' key."""


def call_api(ctx, package: dict) -> dict:
    """One live Messages API call. Returns {"text", "input_tokens", "output_tokens"}. URL/version are
    cfg_setting. Extended thinking is disabled explicitly (the API otherwise defaults to it and can
    spend the whole output budget on thinking), so `lexical.llm_max_output_tokens` is the answer's own
    budget, as the cost estimate assumes."""
    import requests
    key = _api_key()
    url = ctx.cfg.required_setting("lexical.llm_api_url")
    version = ctx.cfg.required_setting("lexical.llm_api_version")
    resp = requests.post(
        url,
        headers={"x-api-key": key, "anthropic-version": version, "content-type": "application/json"},
        json={"model": package["model"], "max_tokens": package["max_output_tokens"],
             "thinking": {"type": "disabled"},
             "system": package["instructions"],
             "messages": [{"role": "user", "content": package["content"]}]},
        timeout=600)
    if resp.status_code != 200:
        raise ApiCallFailed(f"Messages API returned {resp.status_code}: {resp.text[:500]}")
    data = resp.json()
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    usage = data.get("usage", {})
    if not text and data.get("stop_reason") == "max_tokens":
        raise ApiCallFailed(
            f"response hit max_tokens ({package['max_output_tokens']}) with no text content "
            f"produced (usage={usage}) -- the answer itself needs more room than "
            f"lexical.llm_max_output_tokens currently allows, raise it via configmaint.propose")
    return {"text": text, "input_tokens": usage.get("input_tokens", 0),
           "output_tokens": usage.get("output_tokens", 0)}


def log_usage(cfg, run_id: str, chunk_label: str, model: str, input_tokens: int,
             output_tokens: int, cost_usd: float) -> None:
    import csv
    import datetime
    import pathlib
    log_path = pathlib.Path(cfg.required_setting("lexical.llm_usage_log_path"))
    log_path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not log_path.exists()
    with log_path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["run_id", "chunk", "model", "input_tokens", "output_tokens", "cost_usd",
                       "called_at"])
        w.writerow([run_id, chunk_label, model, input_tokens, output_tokens, f"{cost_usd:.4f}",
                   datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")])
