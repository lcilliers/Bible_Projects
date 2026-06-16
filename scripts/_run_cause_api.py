"""_run_cause_api.py (2026-06-16) — run the focused cause-resolution API package and save the output.
Tracks wall-time + token usage + estimated cost. Reads ANTHROPIC_API_KEY from .env (never printed).

  python scripts/_run_cause_api.py --input <package.json> --out <output.json> [--model claude-sonnet-4-6]
"""
import argparse, json, os, re, sys, time
sys.stdout.reconfigure(encoding="utf-8")

# load key from .env without printing it
if not os.getenv("ANTHROPIC_API_KEY") and os.path.exists(".env"):
    for line in open(".env", encoding="utf-8"):
        if line.strip().startswith("ANTHROPIC_API_KEY="):
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
import anthropic

# approx published per-MTok rates (USD) for cost estimate
RATES = {"claude-sonnet-4-6": (3.0, 15.0), "claude-haiku-4-5-20251001": (1.0, 5.0), "claude-opus-4-8": (15.0, 75.0)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="claude-sonnet-4-6")
    a = ap.parse_args()
    pkg = json.load(open(a.input, encoding="utf-8"))
    prompt = pkg["meta"]["instruction"]
    items = pkg["items"]
    content = prompt + "\n\nITEMS (resolve every one):\n" + json.dumps(items, ensure_ascii=False)

    client = anthropic.Anthropic()
    t0 = time.time()
    resp = client.messages.create(model=a.model, max_tokens=8000,
                                  messages=[{"role": "user", "content": content}])
    dt = time.time() - t0
    text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    m = re.search(r"\[.*\]", text, re.S)
    results = json.loads(m.group(0)) if m else []
    json.dump(results, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    it, ot = resp.usage.input_tokens, resp.usage.output_tokens
    ri, ro = RATES.get(a.model, (3.0, 15.0))
    cost = it / 1e6 * ri + ot / 1e6 * ro
    print(f"model: {a.model}")
    print(f"items in: {len(items)}  ·  results out: {len(results)}")
    print(f"time: {dt:.1f}s  ({dt/max(1,len(items))*1000:.0f} ms/item)")
    print(f"tokens: input {it:,} · output {ot:,}")
    print(f"est. cost: ${cost:.4f}  (@ ${ri}/${ro} per MTok in/out)")
    print(f"wrote: {a.out}")
    if results[:2]:
        print("sample:", json.dumps(results[:2], ensure_ascii=False))


if __name__ == "__main__":
    main()
