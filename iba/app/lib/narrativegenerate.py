"""narrativegenerate.py — registers `narrative.generate` as a real report step: assembles a book's
filled passage debates + the two governing instruction docs into one package, submits it to the
Anthropic Messages API, and writes the result as the book's inner-being narrative. Matches the
pattern `passagedebatereport.py`/`wholebookread.py` set — the discovery/assembly/filing plumbing is
mechanised; the actual writing is not done by this module, it is done by the model on the other end
of the API call, working strictly from the instructions and source material this module assembles
(same "consistent package in, consistent quality out" intent the researcher asked for 2026-07-30).

**Cost is real money, not a subscription.** Every `key` this reads is `cfg_setting` (module
`narrative`) so the model, the token budget, and the per-run cost cap are all changeable via
`configmaint.propose`, never hard-coded here. Before ever calling the API, the package is assembled
and its cost is ESTIMATED (character-count heuristic, ~4 chars/token) and checked against `narrative.
generate_max_cost` — over the cap is a hard refusal (`cost-cap-exceeded`, report-stop), not a
silent overspend. Below the cap, the run PAUSES for researcher approval (`needs-approval`,
pause-continue) exactly like every other spend/write-worthy step in this app (`registry.create`,
`configmaint.propose`) — the same run_id is re-run once approved, and only then is the live call
made. Every live call's REAL token/cost (from the API response's own `usage` block, not the
estimate) is appended to `narrative.usage_log_path` — an on-disk, append-only audit trail, since
`scripts/cost_ledger.py` (repo root) only ingests Console CSV exports, not this app's own live
calls.

Uses `requests` directly against the Messages API rather than the `anthropic` SDK — this app has
exactly one Python dependency (`requests`, see `USER-GUIDE.md` §1) and the Messages API is a plain
JSON POST, so a second dependency isn't needed for one endpoint.
"""

from __future__ import annotations

import csv
import datetime
import os
import pathlib
import sqlite3

import requests

from . import passagetrack, reportkit

API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"
CHARS_PER_TOKEN = 4  # rough estimate only — the real count comes back in the API response's usage


class NoDebatesFound(Exception):
    """No `debate_status='filled'` passage row exists yet for this book."""


class MethodDocMissing(Exception):
    """A method.* cfg_setting points at a file that isn't on disk."""


class ApiKeyMissing(Exception):
    """ANTHROPIC_API_KEY not found in the environment or repo-root .env."""


class CostCapExceeded(Exception):
    """The pre-call cost estimate exceeds narrative.generate_max_cost."""


class ApiCallFailed(Exception):
    """The Messages API returned a non-2xx response."""


def _method_doc(cfg, key: str) -> pathlib.Path:
    raw = cfg.setting(key)
    if not raw:
        raise MethodDocMissing(f"{key!r} has no cfg_setting value — run the bootstrap migration")
    path = pathlib.Path(raw)
    if not path.exists():
        raise MethodDocMissing(f"{key!r} points to {path} which does not exist on disk — "
                               f"the config is stale relative to iba/docs/")
    return path


def _api_key() -> str:
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
                        "repo root — add it there (never commit it)")


def gather_book(conn: sqlite3.Connection, book: str) -> list[dict]:
    """Every filled debate for `book`, in reading order, with its full text read off disk."""
    rows = passagetrack.all_debated_ranges(conn, book)
    if not rows:
        raise NoDebatesFound(
            f"no debate_status='filled' passage row exists for book {book!r} — run at least one "
            f"report.passage_debate pass and fill it in before a narrative makes sense")
    out = []
    for r in rows:
        path = pathlib.Path(r["debate_path"])
        out.append({"ref": r["ref"], "path": r["debate_path"], "exists": path.exists(),
                    "text": path.read_text(encoding="utf-8") if path.exists() else ""})
    return out


def assemble_package(cfg, book: str, book_label: str) -> dict:
    """Resolve the two governing docs + every filled debate for `book` into one instructions/content
    pair, and estimate its token count/cost. Raises NoDebatesFound/MethodDocMissing before ever
    touching the network.

    Checked for compliance first (escalation #648, 2026-08-17) — this module's own API_URL/
    API_VERSION/CHARS_PER_TOKEN are hardcoded, flagged NON-COMPLIANT in cfg_utility; using it now
    signals (via cfg.assert_utility_compliant) that it needs revision before this is called again."""
    cfg.assert_utility_compliant("iba/app/lib/narrativegenerate.py")
    conn: sqlite3.Connection = cfg.conn
    constraints_path = _method_doc(cfg, "method.narrative_hard_constraints_path")
    guidance_path = _method_doc(cfg, "method.inner_being_narrative_guidance_path")
    entries = gather_book(conn, book)
    missing = [e["ref"] for e in entries if not e["exists"]]

    instructions = (
        constraints_path.read_text(encoding="utf-8") + "\n\n---\n\n" +
        guidance_path.read_text(encoding="utf-8") + "\n\n---\n\n" +
        f"The book is **{book_label}**. Write the narrative now, for this book, from the passage "
        f"debates supplied below. Output the finished narrative in Markdown ONLY — no preamble, no "
        f"acknowledgement of these instructions, no meta-commentary before or after the piece "
        f"itself. Start directly with a title (`# ...`) and end with the required `## Scope "
        f"self-check` section."
    )
    content = "\n\n".join(
        f"=== {e['ref']} (`{e['path']}`) ===\n\n{e['text']}" for e in entries if e["exists"])

    est_input_tokens = (len(instructions) + len(content)) // CHARS_PER_TOKEN
    max_output_tokens = int(cfg.setting("narrative.generate_max_output_tokens", 16000))
    rate_in = float(cfg.setting("narrative.rate_input_per_million", 3.00))
    rate_out = float(cfg.setting("narrative.rate_output_per_million", 15.00))
    est_cost = (est_input_tokens / 1_000_000 * rate_in) + (max_output_tokens / 1_000_000 * rate_out)

    return {
        "instructions": instructions, "content": content, "entries": entries,
        "missing_debates": missing, "constraints_path": str(constraints_path),
        "guidance_path": str(guidance_path), "est_input_tokens": est_input_tokens,
        "max_output_tokens": max_output_tokens, "est_cost_usd": round(est_cost, 4),
        "model": cfg.required_setting("narrative.generate_model"),
    }


def call_api(package: dict) -> dict:
    """One live Messages API call. Returns {"text": str, "input_tokens": int, "output_tokens": int,
    "cost_usd": float}. Raises ApiCallFailed on a non-2xx response."""
    key = _api_key()
    resp = requests.post(
        API_URL,
        headers={"x-api-key": key, "anthropic-version": API_VERSION,
                "content-type": "application/json"},
        json={"model": package["model"], "max_tokens": package["max_output_tokens"],
             "system": package["instructions"],
             "messages": [{"role": "user", "content": package["content"]}]},
        timeout=600)
    if resp.status_code != 200:
        raise ApiCallFailed(f"Messages API returned {resp.status_code}: {resp.text[:500]}")
    data = resp.json()
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    usage = data.get("usage", {})
    it, ot = usage.get("input_tokens", 0), usage.get("output_tokens", 0)
    return {"text": text, "input_tokens": it, "output_tokens": ot}


def log_usage(cfg, run_id: str, book: str, model: str, input_tokens: int, output_tokens: int,
             cost_usd: float, path: str) -> pathlib.Path:
    log_path = pathlib.Path(cfg.required_setting("narrative.usage_log_path"))
    log_path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not log_path.exists()
    with log_path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["run_id", "book", "model", "input_tokens", "output_tokens", "cost_usd",
                       "path", "generated_at"])
        w.writerow([run_id, book, model, input_tokens, output_tokens, f"{cost_usd:.4f}", path,
                   datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")])
    return log_path


def write_narrative(cfg, book: str, book_label: str, text: str) -> pathlib.Path:
    """File the model's finished narrative under report.verse_analysis_output_dir/<book_label>/,
    same folder its source debates live in, archiving any prior version first — reportkit's shared
    convention, not a one-off writer."""
    conn: sqlite3.Connection = cfg.conn
    output_dir = pathlib.Path(cfg.required_setting("report.verse_analysis_output_dir"))
    pattern = cfg.required_setting("narrative.output_pattern")
    filename = pattern.format(book=book.lower())
    path = output_dir / book_label / filename

    rep = conn.execute("SELECT title, footer_text, archive_dir FROM cfg_report WHERE step=?",
                       ("report.book_narrative_generate",)).fetchone()
    lines = [text.rstrip()]
    if rep and rep["footer_text"]:
        lines += ["", rep["footer_text"]]
    archive_dir = (rep["archive_dir"] if rep else None) or "archive"
    reportkit.archive_before_write(path, archive_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    out_text = "\n".join(lines)
    if not out_text.endswith("\n"):
        out_text += "\n"
    path.write_text(out_text, encoding="utf-8")
    return path
