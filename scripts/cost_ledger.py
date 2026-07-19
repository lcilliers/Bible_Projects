"""cost_ledger.py — ONE combined cost ledger across all three Claude surfaces.

Brings together, into a single on-disk report, the three ways this account spends:

  1. CLAUDE CODE  — every project folder under ~/.claude/projects. Exact tokens,
                    read automatically from the session transcripts. (Same source
                    as token_cost_history.py; this sweeps ALL projects, not one.)
  2. ANTHROPIC API — direct SDK/API calls (e.g. the app's read-passage reading).
                    NOT in any transcript. You export a CSV from the Anthropic
                    Console (console.anthropic.com -> Usage) and drop it in
                    outputs/cost-history/api-exports/ ; this reads it.
  3. CLAUDE AI CHAT — claude.ai Pro/Max/Team. A FLAT SUBSCRIPTION with no token or
                    cost export in existence. Its only honest cost is the monthly
                    fee, recorded by you in scripts/cost_subscriptions.json.

FIDELITY IS LABELLED per source so nothing is silently mixed:
  Claude Code  = EXACT tokens, ESTIMATED cost (tokens x your editable rates)
  API          = EXACT tokens; cost EXACT if the export has a cost column, else estimated
  Claude AI    = SUBSCRIPTION-FLAT (no tokens; the fee is the cost)

READ-ONLY on everything except its own report files.

    python scripts/cost_ledger.py
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import pathlib
import sys
from collections import defaultdict

# reuse the Claude Code engine
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_cost_history import BUCKETS, usage_buckets, cost_of, load_rates  # noqa: E402

DEFAULT_PROJECTS_ROOT = pathlib.Path.home() / ".claude" / "projects"
DEFAULT_RATES = pathlib.Path("scripts/token_cost_rates.json")
DEFAULT_SUBS = pathlib.Path("scripts/cost_subscriptions.json")
DEFAULT_OUT = pathlib.Path("outputs/cost-history")
API_EXPORT_DIR = DEFAULT_OUT / "api-exports"

# lenient CSV header mapping for API Console exports (real Console names first)
COL_ALIASES = {
    "date": ["usage_date_utc", "date", "day", "usage_date", "timestamp"],
    "model": ["model_version", "model", "model_id"],
    "input": ["usage_input_tokens_no_cache", "input_tokens", "input", "uncached_input_tokens", "prompt_tokens"],
    "output": ["usage_output_tokens", "output_tokens", "output", "completion_tokens"],
    "cache_read": ["usage_input_tokens_cache_read", "cache_read_input_tokens", "cache_read", "cache_read_tokens"],
    "cache_write_5m": ["usage_input_tokens_cache_write_5m", "cache_creation_input_tokens", "cache_write", "cache_creation_tokens"],
    "cache_write_1h": ["usage_input_tokens_cache_write_1h"],
    "cost": ["cost", "cost_usd", "amount", "amount_usd"],
}


def model_family(model: str) -> str:
    m = (model or "").lower()
    if "opus" in m:
        return "opus"
    if "sonnet" in m:
        return "sonnet"
    if "haiku" in m:
        return "haiku"
    return "_default"


def cost_pm(b: dict, pm: dict) -> float:
    """Cost of a bucket dict at an explicit per-million rate dict."""
    c = 0.0
    for k in BUCKETS:
        c += b[k] * (pm.get(k, 0.0) / 1_000_000.0)
    return c


def cc_billing_mode() -> str:
    """Detect how Claude Code is billed on this machine (subscription vs api-key)."""
    try:
        d = json.loads((pathlib.Path.home() / ".claude.json").read_text(encoding="utf-8"))
        oa = d.get("oauthAccount") or {}
        bt = oa.get("billingType")
        ot = oa.get("organizationType")
        if bt == "stripe_subscription" or (ot and "claude" in str(ot)):
            extra = " (+extra-usage overage enabled)" if oa.get("hasExtraUsageEnabled") else ""
            plan = str(ot or "subscription").replace("_", " ")
            return f"subscription [{plan}]{extra}"
    except Exception:
        pass
    return "unknown"


def _empty():
    return {k: 0 for k in BUCKETS}


def _add(dst, b):
    for k in BUCKETS:
        dst[k] += b[k]


def _tok(b):
    return sum(b[k] for k in BUCKETS)


# ---------------------------------------------------------------- Claude Code
def scan_claude_code(root: pathlib.Path):
    """Sweep every project folder; return {project_folder: buckets}, deduped by requestId."""
    per_project = defaultdict(_empty)
    seen = set()
    if not root.exists():
        return per_project
    for jf in sorted(root.rglob("*.jsonl")):
        project = jf.parent.name
        try:
            fh = jf.open(encoding="utf-8")
        except OSError:
            continue
        with fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if r.get("type") != "assistant":
                    continue
                msg = r.get("message") or {}
                u = msg.get("usage")
                if not u or msg.get("model") == "<synthetic>":
                    continue
                rid = r.get("requestId") or msg.get("id")
                key = (jf.name, rid)
                if rid and key in seen:
                    continue
                if rid:
                    seen.add(key)
                _add(per_project[project], usage_buckets(u))
    return per_project


# ---------------------------------------------------------------- API (Console CSV)
def _pick(header_map, keys):
    for k in keys:
        if k in header_map:
            return header_map[k]
    return None


def _num(s):
    if s is None:
        return 0.0
    s = str(s).replace(",", "").replace("$", "").strip()
    try:
        return float(s)
    except ValueError:
        return 0.0


def ingest_api(folder: pathlib.Path, rates: dict):
    """Read every CSV; return dict with per-model buckets, cost, files, rows, dates."""
    api_models = rates.get("api_models", {})
    default_pm = api_models.get("_default", rates.get("per_million", {}))
    per_model = defaultdict(_empty)
    total = _empty()
    cost = 0.0
    cost_from_file = 0.0
    saw_cost_col = False
    files = []
    n_rows = 0
    dates = []
    if not folder.exists():
        return {"total": total, "per_model": per_model, "cost": 0.0,
                "exact_cost": None, "files": files, "rows": 0, "dates": dates}
    for csvf in sorted(folder.glob("*.csv")):
        files.append(csvf.name)
        with csvf.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                continue
            hmap = {h.lower().strip(): h for h in reader.fieldnames}
            col = {m: _pick(hmap, al) for m, al in COL_ALIASES.items()}
            for row in reader:
                n_rows += 1
                if col["date"]:
                    dates.append(str(row.get(col["date"], ""))[:10])
                fam = model_family(row.get(col["model"]) if col["model"] else "")
                b = {
                    "input": int(_num(row.get(col["input"]))) if col["input"] else 0,
                    "output": int(_num(row.get(col["output"]))) if col["output"] else 0,
                    "cache_read": int(_num(row.get(col["cache_read"]))) if col["cache_read"] else 0,
                    "cache_write_5m": int(_num(row.get(col["cache_write_5m"]))) if col["cache_write_5m"] else 0,
                    "cache_write_1h": int(_num(row.get(col["cache_write_1h"]))) if col["cache_write_1h"] else 0,
                }
                _add(per_model[fam], b)
                _add(total, b)
                cost += cost_pm(b, api_models.get(fam, default_pm))
                if col["cost"]:
                    saw_cost_col = True
                    cost_from_file += _num(row.get(col["cost"]))
    return {"total": total, "per_model": per_model,
            "cost": (cost_from_file if saw_cost_col else cost),
            "exact_cost": (cost_from_file if saw_cost_col else None),
            "files": files, "rows": n_rows, "dates": [d for d in dates if d]}


# ---------------------------------------------------------------- subscriptions
def read_subs(path: pathlib.Path):
    if not path.exists():
        return "USD", []
    d = json.loads(path.read_text(encoding="utf-8"))
    return d.get("currency", "USD"), d.get("subscriptions", [])


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--projects-root", type=pathlib.Path, default=DEFAULT_PROJECTS_ROOT)
    ap.add_argument("--rates", type=pathlib.Path, default=DEFAULT_RATES)
    ap.add_argument("--subs", type=pathlib.Path, default=DEFAULT_SUBS)
    ap.add_argument("--api-dir", type=pathlib.Path, default=API_EXPORT_DIR)
    ap.add_argument("--out-dir", type=pathlib.Path, default=DEFAULT_OUT)
    a = ap.parse_args()

    rates = load_rates(a.rates)
    cur = rates.get("currency", "USD")
    cc_mode = cc_billing_mode()
    cc_is_sub = cc_mode.startswith("subscription")

    cc = scan_claude_code(a.projects_root)
    cc_total = _empty()
    for b in cc.values():
        _add(cc_total, b)
    cc_value = cost_of(cc_total, rates)   # list-price VALUE (reference)

    api = ingest_api(a.api_dir, rates)
    api_b = api["total"]
    api_cost = api["cost"]
    api_cost_kind = "EXACT (from export)" if api["exact_cost"] is not None else "estimated (per-model)"

    sub_cur, subs = read_subs(a.subs)
    sub_cost = sum(_num(s.get("monthly_usd")) * _num(s.get("months")) for s in subs)

    # ACTUAL MONEY = subscription (covers Claude Code + chat) + pay-as-you-go API.
    # Claude Code's list-price value is NOT added when it is subscription-billed.
    money = sub_cost + api_cost + (0.0 if cc_is_sub else cc_value)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    L = []
    L.append("# Combined cost ledger — Claude Code · API · Claude AI")
    L.append("")
    L.append(f"> Rebuilt {stamp}. Tokens are exact where they exist; cost is estimated at "
             f"the rates in `scripts/token_cost_rates.json` unless a source supplies real cost.")
    L.append(f"> **Claude Code billing detected: {cc_mode}.**")
    L.append("")
    L.append(f"## ACTUAL MONEY (est.) — {cur} {money:,.2f}")
    L.append("")
    if cc_is_sub:
        L.append("> Claude Code runs on your **Claude subscription** — the same plan as claude.ai chat. "
                 "Its per-token list value is shown below as a **reference only** and is **NOT** added to "
                 "the money total; the flat subscription fee (record it in `cost_subscriptions.json`) is "
                 "what covers it, plus any extra-usage overage. Only the **API** column is real pay-as-you-go spend.")
        L.append("")
    L.append(f"| surface | tokens | {cur} | counts toward money? | fidelity |")
    L.append("| --- | --: | --: | --- | --- |")
    cc_money_note = "no — subscription" if cc_is_sub else "yes"
    L.append(f"| Claude Code | {_tok(cc_total):,} | {cc_value:,.2f} | {cc_money_note} | exact tokens · list-price {'reference' if cc_is_sub else 'estimate'} |")
    api_tok = f"{_tok(api_b):,}" if api["files"] else "—"
    L.append(f"| Anthropic API (pay-as-you-go) | {api_tok} | {api_cost:,.2f} | yes | {api_cost_kind if api['files'] else 'no export loaded'} |")
    L.append(f"| Subscription fees (Claude Code + chat) | n/a | {sub_cost:,.2f} | yes | flat fee you recorded |")
    L.append(f"| **ACTUAL MONEY** | | **{money:,.2f}** | | |")
    L.append("")
    if cc_is_sub:
        L.append(f"*Reference: Claude Code consumed {cur} {cc_value:,.2f} of usage at API list prices — "
                 f"the value you got from the subscription, not a charge.*")
        L.append("")

    # Claude Code detail
    L.append("## 1. Claude Code — by project folder")
    L.append("")
    if cc:
        vlabel = "list value" if cc_is_sub else "est."
        L.append(f"| project folder | tokens | {vlabel} {cur} |")
        L.append("| --- | --: | --: |")
        for p in sorted(cc, key=lambda x: -_tok(cc[x])):
            L.append(f"| `{p}` | {_tok(cc[p]):,} | {cost_of(cc[p], rates):,.2f} |")
        L.append(f"| **all Claude Code** | **{_tok(cc_total):,}** | **{cc_value:,.2f}** |")
        L.append("")
        if cc_is_sub:
            L.append(f"*This {cur} column is list-price VALUE, not a bill — Claude Code is on your subscription.*")
            L.append("")
        cw = cc_total["cache_write_5m"] + cc_total["cache_write_1h"]
        L.append(f"Buckets: input {cc_total['input']:,} · cache-read {cc_total['cache_read']:,} · "
                 f"cache-write {cw:,} · output {cc_total['output']:,}. "
                 f"For per-session/per-day Claude Code detail run `token_cost_history.py`.")
    else:
        L.append(f"No Claude Code transcripts found under `{a.projects_root}`.")
    L.append("")

    # API detail
    L.append("## 2. Anthropic API — from Console exports (real pay-as-you-go)")
    L.append("")
    if api["files"]:
        drange = ""
        if api["dates"]:
            drange = f" spanning {min(api['dates'])} … {max(api['dates'])}"
        L.append(f"Read {api['rows']:,} rows from {len(api['files'])} export file(s){drange}: "
                 f"{', '.join('`'+f+'`' for f in api['files'])}.")
        L.append("")
        L.append(f"| model | input | output | cache-read | cache-write | est. {cur} |")
        L.append("| --- | --: | --: | --: | --: | --: |")
        api_models = rates.get("api_models", {})
        default_pm = api_models.get("_default", rates.get("per_million", {}))
        for fam in sorted(api["per_model"], key=lambda x: -_tok(api["per_model"][x])):
            b = api["per_model"][fam]
            cw = b["cache_write_5m"] + b["cache_write_1h"]
            fc = cost_pm(b, api_models.get(fam, default_pm))
            L.append(f"| {fam} | {b['input']:,} | {b['output']:,} | {b['cache_read']:,} | {cw:,} | {fc:,.2f} |")
        L.append(f"| **total** | {api_b['input']:,} | {api_b['output']:,} | {api_b['cache_read']:,} "
                 f"| {api_b['cache_write_5m']+api_b['cache_write_1h']:,} | **{api_cost:,.2f}** |")
        L.append("")
        L.append(f"Cost {api_cost_kind}. This IS separate pay-as-you-go spend, on top of the subscription. "
                 f"The upcoming lexical read-passage phase will add to this table.")
    else:
        L.append("**No API export loaded.** Direct API spend (e.g. the app's reading calls, "
                 "the research subagent's monthly-limit spend) lives only in the Anthropic "
                 "Console and is **NOT** counted above until you add it.")
        L.append("")
        L.append("To include it: export CSV from **console.anthropic.com → Usage**, drop it in "
                 f"`{a.api_dir}/`, re-run. See that folder's `README.md`.")
    L.append("")

    # Subscriptions detail
    L.append("## 3. Claude AI chat — subscription (flat)")
    L.append("")
    L.append("claude.ai chat is not billed per token and has no usage export. Its cost is the "
             "monthly fee, recorded in `scripts/cost_subscriptions.json`.")
    L.append("")
    if subs:
        L.append(f"| service | plan | {sub_cur}/mo | months | subtotal | note |")
        L.append("| --- | --- | --: | --: | --: | --- |")
        for s in subs:
            sub = _num(s.get("monthly_usd")) * _num(s.get("months"))
            L.append(f"| {s.get('service','')} | {s.get('plan','')} | {_num(s.get('monthly_usd')):,.2f} "
                     f"| {int(_num(s.get('months')))} | {sub:,.2f} | {s.get('note','')} |")
        L.append(f"| **total** | | | | **{sub_cost:,.2f}** | |")
        if sub_cost == 0:
            L.append("")
            L.append("*(All zero — fill in `scripts/cost_subscriptions.json` with what you actually pay.)*")
    L.append("")
    L.append("---")
    L.append("*Claude Code detail: `token-history.md`. This file is the roll-up across all three surfaces.*")

    a.out_dir.mkdir(parents=True, exist_ok=True)
    out = a.out_dir / "cost-ledger.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"Claude Code billing: {cc_mode}")
    print(f"Claude Code list-value {cur} {cc_value:,.2f} ({'NOT billed — subscription' if cc_is_sub else 'estimated'}) "
          f"· API pay-as-you-go {cur} {api_cost:,.2f} ({'loaded' if api['files'] else 'no export'}) "
          f"· subs {cur} {sub_cost:,.2f}")
    print(f"ACTUAL MONEY est. {cur} {money:,.2f}")
    print(f"  {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
