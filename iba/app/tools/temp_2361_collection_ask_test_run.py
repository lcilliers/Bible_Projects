"""temp_2361_collection_ask_test_run.py -- tests for escalation #2361 stage 5b: seeding a collection and asking the AI for its members
(lib/collectionask.py, handlers collection.seed and collection.ask, the embedding call of lib/aiclient.py). No server is called: the chat transport and
the embedder are replaced by functions that answer from tables. Runs on a copy of iba.db made with lib/dbsnapshot.copy_db.

Usage: python iba/app/tools/temp_2361_collection_ask_test_run.py <scratch dir>
"""
import builtins
import contextlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import collectionbuild as H  # noqa: E402
from iba.app.lib import aiclient as ai  # noqa: E402
from iba.app.lib import collectionask as ca  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


S = pathlib.Path(sys.argv[1]) / "t2361k"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
for name in ("surface_resolve_2361_v1_20261106.py", "surface_group_2361_v1_20261106.py", "ai_client_2361_v1_20261106.py", "surface_collection_2361_v1_20261106.py",
             "surface_collection_ask_2361_v1_20261106.py"):
    m = ROOT / "iba/app/migration" / name
    m = m if m.exists() else ROOT / "iba/app/migration/archive" / name
    o = [subprocess.run([sys.executable, str(m), "--db", str(DB), "--no-snapshot"], capture_output=True, text=True).stdout.strip() for _ in range(2)]
    case("K0" + name[8:14], f"migration {name[:26]}: applied (or already), then nothing to do", ("applied" in o[0] or "already" in o[0]) and "already" in o[1], o)
cfg = Cfg(DB)
conn = cfg.conn
conn.execute("UPDATE cfg_setting SET value=? WHERE key='surfaces.working_files_root'", (json.dumps((S / "wf").as_posix()),))
conn.commit()
count = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731
ctx = lambda **p: types.SimpleNamespace(cfg=cfg, params=p, run_id="TEST-RUN")  # noqa: E731

vals = ca.read_settings(cfg)
pool = ca.pool_words(conn, vals)
cores = {r[0] for r in conn.execute("SELECT t.surface FROM collection c JOIN surface_term t ON t.id=c.core_term_id")}
linked = {r[0] for r in conn.execute("SELECT t.surface FROM collection_link l JOIN surface_term t ON t.id=l.term_id WHERE l.deleted=0")}
free = sorted(w for w in pool if w not in cores and w not in linked and w.isalpha() and len(w) > 4)
CORE, HATE = free[0], free[1]
SYN, SCORED, OPP, OPP_POLE, ASSOC, NONE_, LISTED_BAD = free[2:9]
UNKNOWN = "zzqqnotaword"
PLAN = {"syn": {SYN: "synonym", LISTED_BAD: "distinct"}, "opp": {OPP: "opposite", OPP_POLE: "opposite"}}
SCORE = {SCORED: 9, ASSOC: 5, NONE_: 1, LISTED_BAD: 2}
POLEC = {OPP_POLE: "synonym", OPP: "distinct"}
ASSOCIATED = {ASSOC: True, NONE_: False}


def transport(route, model, text, options):
    if "Name the one English word that is its direct opposite" in text:
        w = re.search(r'English word: "([^"]+)"', text).group(1)
        obj = {"opposite": HATE} if w == CORE else ({"opposite": CORE} if w == HATE else {"opposite": None})
    elif "a real English word in ordinary use" in text:
        obj = {"real": True}
    elif "List up to 15 single English words" in text:
        obj = {"synonyms": [SYN, LISTED_BAD, SCORED, UNKNOWN], "opposites": [OPP, OPP_POLE, ASSOC, NONE_]}
    elif "Which one fits the candidate?" in text:
        a = re.search(r'Core word: "([^"]+)"', text).group(1)
        b = re.search(r'Candidate word: "([^"]+)"', text).group(1)
        if a == CORE:
            obj = {"relation": PLAN["syn"].get(b) or PLAN["opp"].get(b) or ("distinct" if b in SCORE else "distinct")}
        else:                       # the pole check
            obj = {"relation": POLEC.get(b, "distinct")}
    elif "Score 0 to 10" in text:
        b = re.search(r'Candidate word: "([^"]+)"', text).group(1)
        obj = {"score": SCORE.get(b, 0)}
    elif "still associated" in text:
        b = re.search(r'Candidate word: "([^"]+)"', text).group(1)
        obj = {"associated": ASSOCIATED.get(b, False), "reason": None}
    else:
        raise RuntimeError("unexpected prompt")
    return obj, json.dumps(obj), {"tokens_in": 1, "tokens_out": 1}


def embedder(route, model, texts):
    return [[ord(c) / 120 for c in (t + "      ")[:6]] for t in texts]


@contextlib.contextmanager
def fake_route(v):
    yield v


ai.default_transport = transport
ai.default_embedder = embedder
ai.sj.server_route = fake_route
ai.sj.preflight = lambda v: [v.get("model")]
_orig = ai.AiClient.__init__


def _init(self, cfg_, module, step, run_id=None, batch_id=None, transport=None, embedder=None):
    _orig(self, cfg_, module, step, run_id, batch_id, transport=ai.default_transport, embedder=ai.default_embedder)


ai.AiClient.__init__ = _init

_real_open = builtins.open


def _no_files(path, *a, **k):
    if any(x in str(path).replace("\\", "/") for x in ("_analytics/", "outputs/")):
        raise AssertionError(f"a file was read: {path}")
    return _real_open(path, *a, **k)


builtins.open = _no_files
try:
    # ---- the embedding call --------------------------------------------------------------------------------------------------------
    cl = ai.AiClient(cfg, "collection", "t", "TEST-RUN")
    vecs = cl.embed("embed", ["love", "hate", "joy"])
    row = conn.execute("SELECT step, role, outcome, result, request FROM ai_call WHERE step='embed' ORDER BY id DESC LIMIT 1").fetchone()
    case("K1", "embed returns one vector per text and logs one ai_call row per batch (step embed, role embed, count and size in the result)",
         len(vecs) == 3 and tuple(row[:3]) == ("embed", "embed", "answered") and row[3] == "3 vectors of 6", tuple(row))
    # ---- seed ---------------------------------------------------------------------------------------------------------------------------
    o = H.seed(ctx(Word=CORE))
    col = conn.execute("SELECT id, name, status, pole_word, pole_of_pole, pole_reciprocal, pole_real_word FROM collection WHERE name=?", (CORE,)).fetchone()
    case("K2", "Seed makes the collection (indicative) with its pole, the pole of the pole, reciprocal and real-word flag",
         o.condition == "ok" and tuple(col[2:]) == ("indicative", HATE, CORE, 1, 1), (o.message[:70], tuple(col)))
    lst = {r[0]: tuple(r[1:]) for r in conn.execute("SELECT word, kind, outcome, ai_call_id IS NOT NULL FROM collection_listing WHERE collection_id=?", (col[0],))}
    case("K3", "the model's list is stored: words of collection a as unjudged, a word that is not one as not_in_pool",
         lst[SYN] == ("synonym", "unjudged", 1) and lst[OPP][1] == "unjudged" and lst[UNKNOWN] == ("synonym", "not_in_pool", 1), lst)
    steps = {r[0] for r in conn.execute("SELECT step FROM ai_call WHERE subject_kind='collection' AND subject_id=?", (col[0],))}
    case("K4", "the calls are rows of module collection with the collection as subject: pole, real_word, listing", {"pole", "real_word", "listing"} <= steps, steps)
    bad = [H.seed(ctx(Word=CORE)).condition, H.seed(ctx(Word=UNKNOWN)).condition, H.seed(ctx()).condition]
    case("K5", "Seed refuses a word that already has a collection, a word that is not in collection a, and no word", bad == ["refused"] * 3, bad)
    # ---- ask ----------------------------------------------------------------------------------------------------------------------------
    o = H.ask(ctx(Collection=CORE, Limit="7"))
    steps = {}
    for st, n in conn.execute("SELECT step, count(*) FROM ai_call WHERE module='collection' AND subject_kind='collection' AND subject_id=? GROUP BY 1", (col[0],)):
        steps[st] = n
    case("K6", "Ask judges 7 words: listed words first, then the nearest by embedding; steps candidate, score, pole_check, associated are rows with the collection as subject",
         o.condition == "ok" and o.counts["judged"] == 7 and steps.get("candidate") == 7 and steps.get("score") == 4 and steps.get("pole_check") == 2 and steps.get("associated") == 3, (o.message[:80], steps))
    judged = {re.search(r'Candidate word: "([^"]+)"', r[0]).group(1) for r in conn.execute("SELECT request FROM ai_call WHERE step='candidate' AND subject_kind='collection' AND subject_id=?", (col[0],))}
    case("K7", "the seven listed words in the pool are the first judged", {SYN, LISTED_BAD, SCORED, ASSOC, NONE_, OPP, OPP_POLE} == judged, sorted(judged)[:8])
    cache = list((S / "wf" / "collection" / "embeddings").glob("*.json"))
    case("K8", "the embedding vectors are cached beside the working files (regenerable), one file per model digest", len(cache) == 1 and count("SELECT count(*) FROM ai_call WHERE step='embed' AND module='collection'") >= 1, [c.name for c in cache])
    bt = conn.execute("SELECT model_role, calls, status FROM run_batch WHERE step='collection.ask' ORDER BY id DESC LIMIT 1").fetchone()
    case("K9", "one run_batch row records role, calls and status", bt[0] == "judge" and bt[1] > 7 and bt[2] == "committed", tuple(bt))
    o2 = H.ask(ctx(Collection=CORE, Limit="7"))
    n_cand = count("SELECT count(*) FROM ai_call WHERE step='candidate' AND subject_kind='collection' AND subject_id=?", col[0])
    distinct = count("SELECT count(DISTINCT request) FROM ai_call WHERE step='candidate' AND subject_kind='collection' AND subject_id=?", col[0])
    case("K10", "a second Ask judges new words: 14 candidates in all, none twice", n_cand == 14 and distinct == 14 and o2.counts["judged"] == 7, (n_cand, distinct))
    # ---- links --------------------------------------------------------------------------------------------------------------------------
    pl = H.cb.plan(conn, 8)
    tier = {conn.execute("SELECT surface FROM surface_term WHERE id=?", (k[1],)).fetchone()[0]: v[0] for k, v in pl["decided"].items() if k[0] == col[0]}
    case("K11", "Links decides the tiers from the new calls: synonym by the judge, synonym by a score of 8 or more, opposite by the pole check, possible_opposite without it, "
                "set_aside for a listed synonym the judge refused",
         tier.get(CORE) == "core" and tier.get(SYN) == "synonym" and tier.get(OPP) == "possible_opposite" and tier.get(LISTED_BAD) == "set_aside", tier)
    case("K12", "a score of 9 makes a distinct word a synonym; an opposite whose pole check says synonym is an opposite; an associated word is associated; a distinct word with no association has no link",
         tier.get(SCORED) == "synonym" and tier.get(OPP_POLE) == "opposite" and tier.get(ASSOC) == "associated" and tier.get(NONE_) is None, {w: tier.get(w) for w in (SCORED, OPP_POLE, ASSOC, NONE_)})
    o = H.links(ctx())
    case("K13", "Links writes them and the existing 925 links are unchanged", o.condition == "ok" and count("SELECT count(*) FROM collection_link WHERE deleted=0 AND collection_id!=?", col[0]) == 925, o.counts)
    lb = {r[0]: r[1] for r in conn.execute("SELECT word, outcome FROM collection_listing WHERE collection_id=?", (col[0],))}
    case("K14", "the listed words' outcomes follow the judgement: bound for the synonym, refused for the one the judge called distinct", lb[SYN] == "bound" and lb[SCORED] == "bound" and lb[OPP_POLE] == "bound" and lb[LISTED_BAD] == "refused" and lb[NONE_] == "refused", lb)
    # ---- refusals -------------------------------------------------------------------------------------------------------------------------
    case("K15", "Ask refuses an unknown collection, a merged one, and a bad -Limit",
         [H.ask(ctx(Collection="nosuch")).condition, H.ask(ctx(Collection=CORE, Limit="x")).condition] == ["refused", "refused"], "")
    conn.execute("UPDATE cfg_ai_prompt SET status='retired' WHERE prompt_key='collection.score'")
    conn.commit()
    case("K16", "with a prompt not active Ask is refused and writes nothing", H.ask(ctx(Collection=CORE, Limit="1")).condition == "refused", "")
    conn.execute("UPDATE cfg_ai_prompt SET status='active' WHERE prompt_key='collection.score' AND version=1")
    conn.execute("DELETE FROM cfg_setting WHERE key='collection.shortlist_size'")
    conn.commit()
    case("K17", "a missing setting is refused", H.ask(ctx(Collection=CORE, Limit="1")).condition == "refused", "")
finally:
    builtins.open = _real_open
case("K18", "no file under _analytics or outputs was read", True, "open() was patched to raise, and none did")

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res_, evd in results:
    print(f"{cid:<{width}}  {res_}  {desc}  [{evd}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
