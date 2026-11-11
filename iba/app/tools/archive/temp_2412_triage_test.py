"""temp_2412_triage_test.py -- proof of the Ollama triage question (escalation #2412, design D) against the items Claude assessed.

    python -m iba.app.tools.temp_2412_triage_test --sample                 # build the stratified sample from the assessment files (read-only)
    python -m iba.app.tools.temp_2412_triage_test --run [--limit n]        # ask both prompts of every sample item not yet answered (resumable, progress control)
    python -m iba.app.tools.temp_2412_triage_test --report                 # agreement of the model with Claude, and of the two prompts, to a .md file

Truth: the evaluations of the assessment files of the seven engaged collections, with the reopen decisions of the review files applied. none = not_relevant
and not reopened; every other result is bearing (relevant: characteristic or qualifier; bears_on: object, relational_target or enactment). The model's
answer is read back from ai_call (module engagementask, step triage), so the run writes no other table. Every answer is inferential (B:4)."""
from __future__ import annotations

import argparse
import collections
import glob
import json
import random
import sys
import time

from ..lib import aiclient as ai
from ..lib import engagementask as ea
from ..lib import longrun as lr
from ..lib.cfg import Cfg

ROOT = lr.ROOT
DB = ROOT / "iba" / "app" / "db" / "iba.db"
WORK = ROOT / "_analytics" / "surfaces" / "working_files" / "engagement"
COLS = ["aloud", "call", "deal", "new", "anger", "godly", "choose"]
SAMPLE = WORK / "2412-triage-sample-v1-20261110.json"
REPORT = ROOT / "outputs" / "escalation" / "2412-engagement-ollama-triage-test-v1-20261110.md"
JOB = "engagement-triage-test"
PER_CELL = 15
SEED = 2412


def truth() -> dict:
    out = {}
    for c in COLS:
        reopened = set()
        for f in glob.glob(str(WORK / f"engagement-{c}-review-assessment-*.json")):
            for d in json.load(open(f, encoding="utf-8"))["decisions"]:
                if d["decision"] == "reopen":
                    reopened.add(d["vl_id"])
        for f in sorted(glob.glob(str(WORK / f"engagement-{c}-assessment-*.json"))):
            for e in json.load(open(f, encoding="utf-8"))["evaluations"]:
                cls = "none" if e["result"] == "not_relevant" and e["vl_id"] not in reopened else (
                    "relevant" if e["result"] == "relevant" else "bears_on" if e["result"] == "bears_on" else "reopened")
                out.setdefault(e["vl_id"], {"vl_id": e["vl_id"], "collection": c, "surface": e["surface"], "truth": cls, "role": e.get("role"),
                                            "reason": e["reason"]})
    return out


def build_sample() -> dict:
    t = truth()
    rnd = random.Random(SEED)
    cells = collections.defaultdict(list)
    for v in t.values():
        cells[(v["collection"], v["truth"])].append(v)
    items = []
    for key in sorted(cells):
        pool = sorted(cells[key], key=lambda x: x["vl_id"])
        items += rnd.sample(pool, min(PER_CELL, len(pool)))
    data = {"seed": SEED, "per_cell": PER_CELL, "truth_items": len(t), "items": items}
    SAMPLE.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    cnt = collections.Counter(i["truth"] for i in items)
    print(f"truth items {len(t)}; sample {len(items)} -> {SAMPLE.as_posix()}; by truth {dict(cnt)}")
    return data


def answered(conn, vl_id: int, prompt_id: int) -> bool:
    return conn.execute("SELECT 1 FROM ai_call WHERE module=? AND step='triage' AND subject_id=? AND prompt_id=? AND outcome='answered' AND deleted=0 LIMIT 1",
                        (ea.MODULE, vl_id, prompt_id)).fetchone() is not None


def run(limit: int | None) -> None:
    items = json.load(open(SAMPLE, encoding="utf-8"))["items"]
    cfg = Cfg(DB)
    conn = cfg.conn
    client = ai.AiClient(cfg, ea.MODULE, "triage", f"RUN-{time.strftime('%Y%m%d_%H%M%S')}-ENGAGEMENTASK")
    pids = {k: client.prompt(k)[0] for k in ea.PROMPT_KEYS}
    todo = [(i, k) for i in items for k in ea.PROMPT_KEYS if not answered(conn, i["vl_id"], pids[k])]
    if limit:
        todo = todo[:limit]
    print(f"{len(items)} items, {len(todo)} questions to ask", flush=True)
    with lr.Job(JOB, len(todo)) as job, client.session(["judge"]):
        try:
            for it, key in todo:
                if job.stop_asked():
                    job.prog["state"] = "stopped"
                    break
                job.write(current=f"{key} vl {it['vl_id']} {it['surface']}", current_since=lr.iso(time.time()))
                t0 = time.time()
                r = ea.ask_triage(conn, client, it["vl_id"], key)
                job.step_done(time.time() - t0, ok_=r["outcome"] == "answered", error=r["error"])
            else:
                job.prog["state"] = "finished"
        except ai.AiHalted as exc:
            job.prog["state"] = "halted"
            job.prog["last_error"] = str(exc)
            print("HALTED:", exc)


def latest(conn, vl_id: int, key: str):
    r = conn.execute("SELECT c.result, c.answer FROM ai_call c JOIN cfg_ai_prompt p ON p.id=c.prompt_id WHERE c.module=? AND c.step='triage' AND c.subject_id=? "
                     "AND p.prompt_key=? AND c.outcome='answered' AND c.deleted=0 ORDER BY c.id DESC LIMIT 1", (ea.MODULE, vl_id, key)).fetchone()
    if not r:
        return None, None
    try:
        return r[0], json.loads(r[1]).get("quote")
    except (TypeError, ValueError):
        return r[0], None


def pct(a, b):
    return f"{a} of {b} ({100 * a / b:.0f}%)" if b else "0 of 0"


def report() -> None:
    data = json.load(open(SAMPLE, encoding="utf-8"))
    cfg = Cfg(DB)
    conn = cfg.conn
    rows = []
    for it in data["items"]:
        a, qa = latest(conn, it["vl_id"], "engagement.triage")
        b, qb = latest(conn, it["vl_id"], "engagement.triage_b")
        rows.append(dict(it, a=a, b=b, qa=qa, qb=qb))
    have = [r for r in rows if r["a"] and r["b"]]
    bearing = lambda x: x != "none"
    L = ["# #2412 — Ollama triage test v1 (model against Claude's reading)", "",
         f"Basis: sample of {len(rows)} items (seed {data['seed']}, up to {data['per_cell']} for each collection and truth class) from the {data['truth_items']} items Claude assessed "
         f"in seven collections ({', '.join(COLS)}), reopen decisions applied. Prompts engagement.triage v1 (A) and engagement.triage_b v1 (B), model qwen3:30b, "
         "`ai_call` rows module engagementask. All model answers are inferential (B:4). Items answered by both prompts: " + pct(len(have), len(rows)) + ".", ""]
    if not have:
        L.append("No item has an answer from both prompts yet.")
        REPORT.write_text("\n".join(L), encoding="utf-8")
        return

    def block(title, getter):
        tp = sum(1 for r in have if r["truth"] != "none" and bearing(getter(r)))
        fn = sum(1 for r in have if r["truth"] != "none" and not bearing(getter(r)))
        tn = sum(1 for r in have if r["truth"] == "none" and not bearing(getter(r)))
        fp = sum(1 for r in have if r["truth"] == "none" and bearing(getter(r)))
        L.extend([f"## {title}", "", f"- Claude bearing, model bearing: {tp}; Claude bearing, model none (a miss): {fn}",
                  f"- Claude none, model none: {tn}; Claude none, model bearing (an over-read): {fp}",
                  f"- agreement on bearing versus none: {pct(tp + tn, len(have))}; misses {pct(fn, tp + fn)} of Claude's bearing items; "
                  f"over-reads {pct(fp, tn + fp)} of Claude's none items", ""])
    block("Prompt A alone", lambda r: r["a"])
    block("Prompt B alone", lambda r: r["b"])
    agree = [r for r in have if r["a"] == r["b"]]
    agree_bin = [r for r in have if bearing(r["a"]) == bearing(r["b"])]
    L.extend(["## The two prompts together", "", f"- same three-way answer: {pct(len(agree), len(have))}; same bearing-or-none: {pct(len(agree_bin), len(have))}"])
    ok = sum(1 for r in agree_bin if bearing(r["a"]) == (r["truth"] != "none"))
    L.append(f"- where they agree on bearing-or-none, the answer matches Claude: {pct(ok, len(agree_bin))}")
    n_none = [r for r in agree_bin if not bearing(r["a"])]
    L.append(f"- where both say none, Claude also says none: {pct(sum(1 for r in n_none if r['truth'] == 'none'), len(n_none))}")
    L.extend([f"- the {len(have) - len(agree_bin)} items they differ on would go to Claude's reading", ""])
    L.extend(["## By Claude's class (prompt A answers)", "", "| Claude | inner_being | outward_act | none |", "|---|---|---|---|"])
    for tr in ("relevant", "bears_on", "reopened", "none"):
        sub = [r for r in have if r["truth"] == tr]
        if sub:
            c = collections.Counter(r["a"] for r in sub)
            L.append(f"| {tr} ({len(sub)}) | {c['inner_being']} | {c['outward_act']} | {c['none']} |")
    L.extend(["", "## By collection (bearing versus none, prompt A)", "", "| collection | items | agree |", "|---|---|---|"])
    for c in COLS:
        sub = [r for r in have if r["collection"] == c]
        if sub:
            L.append(f"| {c} | {len(sub)} | {pct(sum(1 for r in sub if bearing(r['a']) == (r['truth'] != 'none')), len(sub))} |")
    mism = [r for r in have if bearing(r["a"]) != (r["truth"] != "none") or bearing(r["b"]) != (r["truth"] != "none")]
    L.extend(["", f"## Disagreements with Claude ({len(mism)} items; first 60)", "",
              "| collection | surface | vl_id | Claude | A | B | Claude's reason | model's quote (A) |", "|---|---|---|---|---|---|---|---|"])
    for r in mism[:60]:
        esc = lambda s: (s or "").replace("|", "/").replace("\n", " ")[:160]
        L.append(f"| {r['collection']} | {r['surface']} | {r['vl_id']} | {r['truth']} | {r['a']} | {r['b']} | {esc(r['reason'])} | {esc(r['qa'])} |")
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"report -> {REPORT.as_posix()}; items with both answers {len(have)} of {len(rows)}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sample", action="store_true")
    p.add_argument("--run", action="store_true")
    p.add_argument("--report", action="store_true")
    p.add_argument("--limit", type=int)
    a = p.parse_args()
    if a.sample:
        build_sample()
    if a.run:
        run(a.limit)
    if a.report:
        report()


if __name__ == "__main__":
    sys.exit(main())
