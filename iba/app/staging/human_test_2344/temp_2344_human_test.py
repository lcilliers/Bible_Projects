"""Throwaway (#2344): the researcher's human test on each live surface pair of the concept query.
Read-only on iba/app/db/iba.db. Verdicts are the local model's, inferential (B:4)."""
import sqlite3, json, csv, sys, time, urllib.request, os
ROOT = "C:/Bible_study_projects/"
DB = ROOT + "iba/app/db/iba.db"
OUT = ROOT + "outputs/concept-mapping/"
MODEL = "qwen2.5:7b-instruct"
URL = "http://localhost:11434/api/generate"
JSONL = OUT + "surface-human-test-progress-v1-20261031.jsonl"
CSV = OUT + "surface-human-test-v1-20261031.csv"
Q = """SELECT d.id,d.name,c.id,c.name,cs.cluster_code,cs.label,s.id,s.strong,s.surface,s.reason,s.allocated_by
FROM concept_subgroup cg JOIN concept c ON cg.concept_id=c.id AND c.deleted=0
JOIN concept_domain d ON c.domain_id=d.id AND d.deleted=0
JOIN cluster_subgroup cs ON cg.cluster_subgroup_id=cs.id
JOIN surface_subgroup s ON cs.id=s.cluster_subgroup_id AND s.deleted=0
WHERE cg.deleted=0 ORDER BY d.ordinal,c.ordinal,cs.cluster_code,s.id"""
HEAD = ["domain_id","domain_name","concept_id","concept_name","cluster_code","cluster_subgroup_name",
        "surface_subgroup_id","strong","surface","reason","allocated_by"]
KEYS = ["be","do","experience","express","get"]

def ask(word):
    p = (f'The English word is "{word}". Answer each question about a human being with true or false, '
         'taking the word in its ordinary Bible-translation sense.\n'
         f'be: can a human be {word} (a state or quality a person can be)?\n'
         f'do: can a human do {word} (an act a person can do)?\n'
         f'experience: can a human experience {word}?\n'
         f'express: can a human express {word}?\n'
         f'get: can a human get {word}?\n'
         'Reply with JSON only: {"be":bool,"do":bool,"experience":bool,"express":bool,"get":bool}')
    body = json.dumps({"model": MODEL, "prompt": p, "stream": False, "format": "json",
                       "options": {"temperature": 0, "num_predict": 60, "num_ctx": 1024}}).encode()
    req = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        t = json.loads(r.read())["response"]
    try:
        j = json.loads(t); return {k: bool(j.get(k)) for k in KEYS}
    except Exception:
        return None

def main(limit=None):
    c = sqlite3.connect("file:" + DB + "?mode=ro", uri=True)
    rows = c.execute(Q).fetchall()
    words = sorted({r[8] for r in rows})
    have = {}
    if os.path.exists(JSONL):
        for l in open(JSONL, encoding="utf-8"):
            j = json.loads(l); have[j["w"]] = j["v"]
    todo = [w for w in words if w not in have]
    if limit: todo = todo[:limit]
    t0 = time.time()
    with open(JSONL, "a", encoding="utf-8") as f:
        for i, w in enumerate(todo):
            v = ask(w); have[w] = v
            f.write(json.dumps({"w": w, "v": v}) + "\n"); f.flush()
            if i % 50 == 0: print(i, len(todo), round(time.time() - t0), "s", flush=True)
    print("words", len(words), "done", len(have), "secs", round(time.time() - t0))

def build():
    c = sqlite3.connect("file:" + DB + "?mode=ro", uri=True)
    rows = c.execute(Q).fetchall()
    have = {}
    for l in open(JSONL, encoding="utf-8"):
        j = json.loads(l); have[j["w"]] = j["v"]
    with open(CSV, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(HEAD + ["human_be","human_do","human_experience","human_express","human_get","human_test_verdict"])
        for r in rows:
            v = have.get(r[8])
            if v is None: w.writerow(list(r) + ["","","","","","not_run"]); continue
            w.writerow(list(r) + [int(v[k]) for k in KEYS] + ["pass" if any(v.values()) else "fail"])
    print("wrote", CSV, len(rows))

if __name__ == "__main__":
    a = sys.argv[1]
    if a == "run": main(int(sys.argv[2]) if len(sys.argv) > 2 else None)
    else: build()
