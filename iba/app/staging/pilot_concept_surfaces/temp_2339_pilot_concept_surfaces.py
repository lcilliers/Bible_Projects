"""Throwaway pilot for escalation #2339 (approved 2026-10-31, v4 design): classify surfaces by
content with the local model, with no subgroup, cluster or concept label as input. Read-only on
iba/app/db/iba.db; results go to outputs/concept-mapping/. Not part of the app.

Stages (each resumable): sample, run, repeat, group, report.
  python -I iba/app/staging/pilot_concept_surfaces/temp_2339_pilot_concept_surfaces.py <stage>
"""
import json
import random
import re
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DB = ROOT / "iba/app/db/iba.db"
SPEC = ROOT / "iba/docs/concept-mapping-spec-v1-20261031.json"
OUT = ROOT / "outputs/concept-mapping"
SAMPLE = OUT / "pilot-surfaces-sample-v1-20261031.json"
RUN = OUT / "pilot-surfaces-run-v1-20261031.jsonl"
REPEAT = OUT / "pilot-surfaces-repeat-v1-20261031.jsonl"
GROUPS = OUT / "pilot-surfaces-groups-v1-20261031.json"
REPORT = OUT / "pilot-surfaces-result-v1-20261031.md"
MODEL = "qwen2.5:7b-instruct"
URL = "http://localhost:11434/api/generate"
SEED = 20261031


def con():
    return sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)


def definition(c, strong):
    g = c.execute("SELECT stepGloss FROM strong WHERE strongNumber=? AND deleted=0", (strong,)).fetchone()
    senses = [re.sub(r"<[^>]+>", "", t[0]).strip()[:90] for t in c.execute(
        "SELECT sense_text FROM strong_meaning_tree WHERE lemma_key=? AND deleted=0 ORDER BY sort LIMIT 3",
        (strong,))]
    return (g[0] if g and g[0] else ""), [s for s in senses if s]


def stage_sample():
    c = con()
    spec = json.load(open(SPEC, encoding="utf-8"))
    feel = [i for d in spec["domains"][:4] for k in d["concepts"] for i in k["subgroup_ids"]]
    base = "SELECT id, strong, surface, cluster_code FROM surface_subgroup WHERE deleted=0 AND "
    rnd = random.Random(SEED)
    f = c.execute(base + f"cluster_subgroup_id IN ({','.join(map(str, feel))})").fetchall()
    m46 = c.execute(base + "cluster_code='M46'").fetchall()
    m72 = c.execute(base + "cluster_code='M72'").fetchall()
    taken = {r[0] for r in f} | {r[0] for r in m46} | {r[0] for r in m72}
    rest = [r for r in c.execute(base + "1=1") if r[0] not in taken]
    pick = ([("feeling", r) for r in rnd.sample(f, 100)] + [("wealth_M46", r) for r in rnd.sample(m46, 20)]
            + [("authority_M72", r) for r in rnd.sample(m72, 20)] + [("other", r) for r in rnd.sample(rest, 60)])
    out = []
    for stratum, (sid, strong, surface, cl) in pick:
        gloss, senses = definition(c, strong)
        out.append({"id": sid, "strong": strong, "surface": surface, "stratum": stratum,
                    "gloss": gloss, "senses": senses})
    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(SAMPLE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("sample", len(out), "no definition senses:", sum(1 for r in out if not r["senses"]))


PROMPT = (
    "You classify words of the Bible by what they are about.\n"
    "English word as translated: \"{surface}\"\n"
    "Original-language word {strong}, glossed \"{gloss}\". Senses: {senses}\n"
    "In 2 to 5 words, say what this word is about (its subject matter), in your own words. "
    "Do not repeat the word itself unless nothing else fits.\n"
    "Answer only JSON: {{\"about\": \"...\"}}"
)


def ask(prompt, temperature, num_predict=60, num_ctx=2048):
    body = json.dumps({"model": MODEL, "prompt": prompt, "stream": False, "format": "json",
                       "options": {"temperature": temperature, "num_predict": num_predict,
                                   "num_ctx": num_ctx}}).encode()
    req = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
    t = time.time()
    with urllib.request.urlopen(req, timeout=900) as r:
        txt = json.loads(r.read())["response"]
    return txt, time.time() - t


def classify(row, temperature):
    p = PROMPT.format(surface=row["surface"], strong=row["strong"], gloss=row["gloss"],
                      senses="; ".join(row["senses"]) or "none recorded")
    try:
        txt, secs = ask(p, temperature)
    except Exception as e:  # recorded, not hidden
        return {"id": row["id"], "valid": False, "error": repr(e), "secs": 0, "about": ""}
    try:
        about = str(json.loads(txt)["about"]).strip()
        valid = bool(about)
    except Exception:
        about, valid = "", False
    return {"id": row["id"], "valid": valid, "about": about, "secs": round(secs, 1), "raw": txt}


def done(path):
    if not path.exists():
        return set()
    return {json.loads(ln)["id"] for ln in open(path, encoding="utf-8") if ln.strip()}


def stage_run(path, rows, temperature):
    have = done(path)
    with open(path, "a", encoding="utf-8") as f:
        for i, row in enumerate(rows):
            if row["id"] in have:
                continue
            f.write(json.dumps(classify(row, temperature), ensure_ascii=False) + "\n")
            f.flush()
            print(path.name, i + 1, "of", len(rows), flush=True)


def norm(s):
    return re.sub(r"[^a-z ]", "", s.lower()).strip()


def stage_group():
    run = [json.loads(ln) for ln in open(RUN, encoding="utf-8") if ln.strip()]
    phrases = sorted({norm(r["about"]) for r in run if r["valid"]})
    listing = "\n".join(f"{i}: {p}" for i, p in enumerate(phrases))
    prompt = ("Below are numbered short phrases, each saying what a Bible word is about. Group phrases "
              "that are about the same subject. Name each group in 2 to 4 words. Every number must be in "
              "exactly one group. Answer only JSON: {\"groups\": [{\"name\": \"...\", \"members\": [0, 1]}]}\n\n"
              + listing)
    txt, secs = ask(prompt, 0, num_predict=3000, num_ctx=8192)
    try:
        g = json.loads(txt)["groups"]
    except Exception:
        g = []
    placed = {m for x in g for m in x.get("members", []) if isinstance(m, int)}
    json.dump({"phrases": phrases, "groups": g, "unplaced": [i for i in range(len(phrases)) if i not in placed],
               "secs": round(secs, 1), "raw_valid": bool(g)}, open(GROUPS, "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("groups", len(g), "unplaced", len(phrases) - len(placed), "secs", round(secs))


def stage_report():
    sample = {r["id"]: r for r in json.load(open(SAMPLE, encoding="utf-8"))}
    run = {r["id"]: r for r in (json.loads(ln) for ln in open(RUN, encoding="utf-8") if ln.strip())}
    rep = {r["id"]: r for r in (json.loads(ln) for ln in open(REPEAT, encoding="utf-8") if ln.strip())} \
        if REPEAT.exists() else {}
    g = json.load(open(GROUPS, encoding="utf-8")) if GROUPS.exists() else {"phrases": [], "groups": [], "unplaced": []}
    v = [r for r in run.values() if r["valid"]]
    secs = [r["secs"] for r in v]
    L = ["# Pilot: surfaces classified by the local model (#2339)", "",
         f"Model {MODEL}, Ollama, CPU only. Read-only; nothing written to iba/app/db/iba.db. "
         "Phrases and group names are the model's output: inferential (B:4), not confirmed.", "",
         "## Measures", f"- rows run: {len(run)} of {len(sample)}; valid output: {len(v)} ({100*len(v)//max(1,len(run))}%)",
         f"- seconds per surface: mean {sum(secs)/max(1,len(secs)):.1f}, max {max(secs, default=0):.1f}; "
         f"sum {sum(secs)/60:.0f} min for {len(v)} rows"]
    if rep:
        both = [i for i in rep if rep[i]["valid"] and i in run and run[i]["valid"]]
        exact = [i for i in both if norm(rep[i]["about"]) == norm(run[i]["about"])]
        share = [i for i in both if set(norm(rep[i]["about"]).split()) & set(norm(run[i]["about"]).split())]
        L.append(f"- repeat (temperature 0.5 against the temperature 0 run), {len(both)} rows: identical phrase {len(exact)}, "
                 f"at least one word shared {len(share)}")
    L += ["", f"## Groups ({len(g['groups'])} named; phrases {len(g['phrases'])}; unplaced {len(g['unplaced'])})"]
    ph = g["phrases"]
    inv = {}
    for r in run.values():
        if r["valid"]:
            inv.setdefault(norm(r["about"]), []).append(r["id"])
    for x in g["groups"]:
        mem = [ph[m] for m in x.get("members", []) if isinstance(m, int) and m < len(ph)]
        ids = [i for p in mem for i in inv.get(p, [])]
        strata = {}
        for i in ids:
            strata[sample[i]["stratum"]] = strata.get(sample[i]["stratum"], 0) + 1
        L.append(f"- **{x.get('name')}** ({len(ids)} surfaces; {strata}): " + "; ".join(
            f"{sample[i]['surface']} ({sample[i]['strong']})" for i in ids[:12]))
    L += ["", "## Every sampled row (stratum, surface, strong, model phrase)", "",
          "| stratum | surface | strong | model phrase | secs |", "|---|---|---|---|---|"]
    for i, s in sample.items():
        r = run.get(i)
        L.append(f"| {s['stratum']} | {s['surface']} | {s['strong']} | {(r or {}).get('about', 'not run')} | {(r or {}).get('secs', '')} |")
    open(REPORT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("report written")


if __name__ == "__main__":
    st = sys.argv[1]
    if st == "sample":
        stage_sample()
    elif st == "run":
        stage_run(RUN, json.load(open(SAMPLE, encoding="utf-8")), 0)
    elif st == "repeat":
        rows = json.load(open(SAMPLE, encoding="utf-8"))
        pick = random.Random(SEED + 1).sample(rows, 20)
        stage_run(REPEAT, pick, 0.5)
    elif st == "group":
        stage_group()
    elif st == "report":
        stage_report()
