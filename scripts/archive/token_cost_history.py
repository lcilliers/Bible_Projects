"""token_cost_history.py — an auditable history of token consumption and estimated cost.

WHY THIS EXISTS
    So there is a durable, verifiable record on disk of what every session cost.
    Claude cannot introspect its own live token use, and made-up numbers would be
    worthless. But Claude Code writes every turn of every session to disk as a
    transcript (~/.claude/projects/<project>/*.jsonl), and each assistant message
    in it carries the EXACT usage the billing layer saw. This script reads those
    transcripts and reports them. Every number traces to a recorded message.

WHAT IS EXACT vs ESTIMATED
    TOKENS  — exact. Read straight from the transcript's `usage` object.
    COST    — an estimate: tokens x the rates in scripts/token_cost_rates.json,
              which you control. Edit that file to match your actual bill.

GROUPING
    A "session" = one Claude Code conversation (one .jsonl / one sessionId) — the
    closest thing to a "cycle". The report aggregates per session, per day, and a
    grand total.

IDEMPOTENT
    Rebuilds the whole ledger from the transcripts on every run, deduped by
    requestId, so re-running is always safe and always gives the complete picture.

READ-ONLY
    Only reads transcripts and the rates file. Writes only its own report files.

    python scripts/token_cost_history.py
    python scripts/token_cost_history.py --projects-dir "C:/Users/.../<project>"
    python scripts/token_cost_history.py --out-dir outputs/cost-history
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import pathlib
import sys
from collections import defaultdict

DEFAULT_PROJECTS_DIR = pathlib.Path.home() / ".claude" / "projects" / "c--Bible-study-projects"
DEFAULT_RATES = pathlib.Path("scripts/token_cost_rates.json")
DEFAULT_OUT = pathlib.Path("outputs/cost-history")

BUCKETS = ["input", "output", "cache_read", "cache_write_5m", "cache_write_1h"]


def load_rates(path: pathlib.Path) -> dict:
    d = json.loads(path.read_text(encoding="utf-8"))
    return d


def usage_buckets(u: dict) -> dict:
    """Split a transcript usage object into the five priced buckets (exact tokens)."""
    cc = u.get("cache_creation") or {}
    w1h = cc.get("ephemeral_1h_input_tokens")
    w5m = cc.get("ephemeral_5m_input_tokens")
    total_write = u.get("cache_creation_input_tokens", 0) or 0
    # If the fine split is present use it; else treat all cache-writes as 5m.
    if w1h is None and w5m is None:
        w5m, w1h = total_write, 0
    else:
        w1h = w1h or 0
        w5m = w5m or 0
    return {
        "input": u.get("input_tokens", 0) or 0,
        "output": u.get("output_tokens", 0) or 0,
        "cache_read": u.get("cache_read_input_tokens", 0) or 0,
        "cache_write_5m": w5m,
        "cache_write_1h": w1h,
    }


def cost_of(b: dict, rates: dict) -> float:
    pm = rates["per_million"]
    lc = rates.get("long_context", {})
    thr = lc.get("threshold_input_tokens", 0) or 0
    mult = lc.get("premium_multiplier", 1.0) or 1.0
    # Long-context premium applies to the whole request's input-side when the
    # request's total input (fresh + cache) crosses the threshold.
    input_side = b["input"] + b["cache_read"] + b["cache_write_5m"] + b["cache_write_1h"]
    factor = mult if (thr and input_side > thr) else 1.0
    c = 0.0
    for k in BUCKETS:
        rate = pm.get(k, 0.0) / 1_000_000.0
        f = factor if k != "output" else 1.0
        c += b[k] * rate * f
    return c


def scan(projects_dir: pathlib.Path):
    """Yield one deduped record per API request across all transcripts."""
    seen = set()
    for jf in sorted(projects_dir.glob("*.jsonl")):
        with jf.open(encoding="utf-8") as f:
            for line in f:
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
                if not u:
                    continue
                model = msg.get("model", "")
                if model == "<synthetic>":
                    continue
                rid = r.get("requestId") or msg.get("id")
                key = (jf.name, rid)
                if rid and key in seen:
                    continue
                if rid:
                    seen.add(key)
                ts = r.get("timestamp", "")
                yield {
                    "session": r.get("sessionId") or jf.stem,
                    "file": jf.name,
                    "ts": ts,
                    "date": ts[:10] if ts else "",
                    "model": model,
                    "buckets": usage_buckets(u),
                }


def add(dst: dict, b: dict):
    for k in BUCKETS:
        dst[k] += b[k]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--projects-dir", type=pathlib.Path, default=DEFAULT_PROJECTS_DIR)
    ap.add_argument("--rates", type=pathlib.Path, default=DEFAULT_RATES)
    ap.add_argument("--out-dir", type=pathlib.Path, default=DEFAULT_OUT)
    a = ap.parse_args()

    if not a.projects_dir.exists():
        print(f"projects dir not found: {a.projects_dir}", file=sys.stderr)
        return 2
    rates = load_rates(a.rates)

    per_session = defaultdict(lambda: {k: 0 for k in BUCKETS})
    sess_meta = {}          # session -> {first, last, model, file, requests}
    per_day = defaultdict(lambda: {k: 0 for k in BUCKETS})
    grand = {k: 0 for k in BUCKETS}
    n = 0

    for rec in scan(a.projects_dir):
        s = rec["session"]
        add(per_session[s], rec["buckets"])
        if rec["date"]:
            add(per_day[rec["date"]], rec["buckets"])
        add(grand, rec["buckets"])
        m = sess_meta.setdefault(s, {"first": rec["ts"], "last": rec["ts"],
                                     "model": rec["model"], "file": rec["file"], "requests": 0})
        m["requests"] += 1
        if rec["ts"]:
            if not m["first"] or rec["ts"] < m["first"]:
                m["first"] = rec["ts"]
            if not m["last"] or rec["ts"] > m["last"]:
                m["last"] = rec["ts"]
        n += 1

    a.out_dir.mkdir(parents=True, exist_ok=True)
    run_stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def tok(b):  # total tokens in a bucket dict
        return sum(b[k] for k in BUCKETS)

    # ---- machine-readable ledger: one row per session ----
    csv_path = a.out_dir / "token-ledger.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["session", "first_ts", "last_ts", "model", "requests",
                    "input", "output", "cache_read", "cache_write_5m", "cache_write_1h",
                    "total_tokens", "est_cost_usd"])
        for s in sorted(per_session, key=lambda x: sess_meta[x]["first"]):
            b = per_session[s]
            meta = sess_meta[s]
            w.writerow([s, meta["first"], meta["last"], meta["model"], meta["requests"],
                        b["input"], b["output"], b["cache_read"], b["cache_write_5m"], b["cache_write_1h"],
                        tok(b), f"{cost_of(b, rates):.4f}"])

    # ---- machine-readable per-day ledger ----
    day_csv = a.out_dir / "token-ledger-daily.csv"
    with day_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "input", "output", "cache_read", "cache_write_5m", "cache_write_1h",
                    "total_tokens", "est_cost_usd"])
        for d in sorted(per_day):
            b = per_day[d]
            w.writerow([d, b["input"], b["output"], b["cache_read"], b["cache_write_5m"], b["cache_write_1h"],
                        tok(b), f"{cost_of(b, rates):.4f}"])

    # ---- human-readable history ----
    cur = rates.get("currency", "USD")
    pm = rates["per_million"]
    grand_cost = sum(cost_of(per_day[d], rates) for d in per_day)
    L = []
    L.append("# Token consumption & estimated cost — history")
    L.append("")
    L.append(f"> Rebuilt {run_stamp} from {n} recorded API requests across "
             f"{len(sess_meta)} sessions in `{a.projects_dir}`.")
    L.append("> **Tokens are exact** (read from Claude Code's session transcripts). "
             "**Cost is an estimate** at the rates in `scripts/token_cost_rates.json` — edit it to match your bill.")
    L.append("")
    L.append(f"**Grand total: {tok(grand):,} tokens · est. {cur} {grand_cost:,.2f}**")
    L.append("")
    L.append(f"Rates used ({cur}/M): input {pm['input']} · output {pm['output']} · "
             f"cache-read {pm['cache_read']} · cache-write-5m {pm['cache_write_5m']} · "
             f"cache-write-1h {pm['cache_write_1h']}.")
    lc = rates.get("long_context", {})
    if (lc.get("premium_multiplier", 1.0) or 1.0) != 1.0:
        L.append(f"Long-context premium x{lc['premium_multiplier']} over "
                 f"{lc['threshold_input_tokens']:,} input tokens/request.")
    L.append("")
    L.append("## Where the cost goes (by bucket)")
    L.append("")
    L.append(f"| bucket | tokens | est. {cur} | share of cost |")
    L.append("| --- | --: | --: | --: |")
    bucket_cost = {}
    for k in BUCKETS:
        one = {kk: (grand[k] if kk == k else 0) for kk in BUCKETS}
        bucket_cost[k] = cost_of(one, rates)
    tot_c = sum(bucket_cost.values()) or 1.0
    for k in BUCKETS:
        L.append(f"| {k} | {grand[k]:,} | {bucket_cost[k]:,.2f} | {100*bucket_cost[k]/tot_c:.0f}% |")
    L.append("")
    L.append("## Token buckets — what they mean")
    L.append("")
    L.append("- **input** — fresh (uncached) prompt tokens. Full price.")
    L.append("- **cache_read** — prompt tokens served from cache. ~10% of input price. "
             "Long conversations lean heavily on this — it is where most tokens sit, cheaply.")
    L.append("- **cache_write_5m / _1h** — writing the prompt into the cache. 1.25x / 2x input.")
    L.append("- **output** — tokens Claude generated. Most expensive per token.")
    L.append("")
    L.append("## By day")
    L.append("")
    L.append(f"| date | input | cache-read | cache-write | output | total | est. {cur} |")
    L.append("| --- | --: | --: | --: | --: | --: | --: |")
    for d in sorted(per_day):
        b = per_day[d]
        cw = b["cache_write_5m"] + b["cache_write_1h"]
        L.append(f"| {d} | {b['input']:,} | {b['cache_read']:,} | {cw:,} | {b['output']:,} "
                 f"| {tok(b):,} | {cost_of(b, rates):,.2f} |")
    L.append(f"| **total** | | | | | **{tok(grand):,}** | **{grand_cost:,.2f}** |")
    L.append("")
    L.append("## By session (a session ≈ one cycle)")
    L.append("")
    L.append(f"| first seen | requests | input | cache-read | cache-write | output | total | est. {cur} | session |")
    L.append("| --- | --: | --: | --: | --: | --: | --: | --: | --- |")
    for s in sorted(per_session, key=lambda x: sess_meta[x]["first"]):
        b = per_session[s]
        meta = sess_meta[s]
        cw = b["cache_write_5m"] + b["cache_write_1h"]
        L.append(f"| {meta['first'][:16].replace('T',' ')} | {meta['requests']} "
                 f"| {b['input']:,} | {b['cache_read']:,} | {cw:,} | {b['output']:,} "
                 f"| {tok(b):,} | {cost_of(b, rates):,.2f} | `{s[:8]}` |")
    L.append("")
    L.append("---")
    L.append("*Machine-readable: `token-ledger.csv` (per session), `token-ledger-daily.csv` (per day).*")

    md_path = a.out_dir / "token-history.md"
    md_path.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"{n} requests · {len(sess_meta)} sessions · {tok(grand):,} tokens · "
          f"est. {cur} {grand_cost:,.2f}")
    print(f"  {md_path}")
    print(f"  {csv_path}")
    print(f"  {day_csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
