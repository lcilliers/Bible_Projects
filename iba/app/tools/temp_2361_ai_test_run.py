"""temp_2361_ai_test_run.py -- tests for escalation #2361 stage 4: the AI client (lib/aiclient.py), the control steps (handlers/ai.py) and the
table-driven AI steps (surface_base.ask, group.judge). No server is called: the transport is replaced by a function that answers from a table.
Everything runs on a copy of iba.db made with lib/dbsnapshot.copy_db.

Usage: python iba/app/tools/temp_2361_ai_test_run.py <scratch dir>
"""
import builtins
import contextlib
import json
import pathlib
import shutil
import subprocess
import sys
import types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from iba.app.handlers import ai as HA  # noqa: E402
from iba.app.handlers import surfacebase as HB  # noqa: E402
from iba.app.handlers import surfacegroup as HG  # noqa: E402
from iba.app.handlers import surfaceresolve as HR  # noqa: E402
from iba.app.lib import aiclient as ai  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402
from iba.app.lib.dbsnapshot import copy_db  # noqa: E402

results = []


def case(cid, desc, passed, evidence):
    results.append((cid, desc, "PASS" if passed else "FAIL", str(evidence).replace("|", "/")[:300]))


S = pathlib.Path(sys.argv[1]) / "t2361a"
if S.exists():
    shutil.rmtree(S)
S.mkdir(parents=True)
DB = copy_db(S / "iba.db")
for name in ("surface_resolve_2361_v1_20261106.py", "surface_group_2361_v1_20261106.py", "ai_client_2361_v1_20261106.py", "surface_collection_2361_v1_20261106.py", "surface_collection_ask_2361_v1_20261106.py"):
    m = ROOT / "iba/app/migration" / name
    m = m if m.exists() else ROOT / "iba/app/migration/archive" / name
    o = [subprocess.run([sys.executable, str(m), "--db", str(DB), "--no-snapshot"], capture_output=True, text=True).stdout.strip() for _ in range(2)]
    case("B0" + name[:8], f"migration {name[:12]}: applied (or already), then nothing to do", ("applied" in o[0] or "already" in o[0]) and "already" in o[1], o)
cfg = Cfg(DB)
conn = cfg.conn
count = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731
ctx = lambda **p: types.SimpleNamespace(cfg=cfg, params=p, run_id="TEST-RUN")  # noqa: E731

calls = []
script = {"mode": "ok"}


def transport(route, model, text, options):
    calls.append((model, text, options))
    if script["mode"] == "error":
        raise RuntimeError("tunnel down")
    word = text.split('"')[1] if '"' in text else "?"
    if script["mode"] == "bad":
        return {"relation": "x"}, '{"relation": "x"}', {}
    if script.get("answers") and word in script["answers"]:
        obj = script["answers"][word]
    elif "group" in text.lower() and "Answer with exactly one group" in text:
        obj = {"group": "behaviour", "reason": "r"}
    else:
        obj = {"relation": "none", "base": None, "reason": None}
    return obj, json.dumps(obj), {"tokens_in": 10, "tokens_out": 5}


def client(step="base", **k):
    return ai.AiClient(cfg, "test_ai", step, "TEST-RUN", transport=transport, **k)


def check_rel(a):
    return [] if isinstance(a, dict) and a.get("relation") in ("inflection", "derivation", "none") else ["relation"]


# ---- the client -----------------------------------------------------------------------------------------------------------------------
cl = client()
r = cl.call("judge", "base.word", {"surface": "sins"}, ("surface_term", 1), check=check_rel, result_of=lambda a: a.get("base") or "sins")
row = conn.execute("SELECT module, step, role, model_id, model_digest, prompt_id, options, request_hash, request, answer, result, outcome, tokens_out, run_id FROM ai_call WHERE id=?", (r["call_id"],)).fetchone()
want_model = conn.execute("SELECT id, digest FROM cfg_ai_model WHERE role='judge' AND status='active'").fetchone()
want_prompt = conn.execute("SELECT id FROM cfg_ai_prompt WHERE prompt_key='base.word' AND status='active'").fetchone()
case("A1", "an answered call is one ai_call row with module, step, role, model and digest, prompt version, options, request hash, request, answer, result, run",
     r["outcome"] == "answered" and row[0:3] == ("test_ai", "base", "judge") and row[3:5] == tuple(want_model) and row[5] == want_prompt[0]
     and json.loads(row[6])["temperature"] == 0 and row[7] == ai.text_hash(row[8]) and '"sins"' in row[8] and row[10] == "sins" and row[11] == "answered"
     and row[12] == 5 and row[13] == "TEST-RUN", tuple(row)[:8])
n0 = count("SELECT count(*) FROM ai_call")
script["mode"] = "bad"
r = client().call("judge", "base.word", {"surface": "x"}, ("surface_term", 2), check=check_rel)
case("A2", "an answer the check refuses: outcome refused, tried again (two rows), the reason stored", r["outcome"] == "refused" and count("SELECT count(*) FROM ai_call") == n0 + 2
     and count("SELECT count(*) FROM ai_call WHERE outcome='refused' AND error='relation'") == 2, r["error"])
script["mode"] = "error"
n0 = count("SELECT count(*) FROM ai_call")
r = client().call("judge", "base.word", {"surface": "x"}, ("surface_term", 2), check=check_rel)
case("A3", "a call that fails (tunnel down): outcome failed, two rows with the error", r["outcome"] == "failed" and count("SELECT count(*) FROM ai_call") == n0 + 2
     and count("SELECT count(*) FROM ai_call WHERE outcome='failed' AND error LIKE '%tunnel down%'") >= 2, r["error"])
cl = client()
halted = False
n0 = count("SELECT count(*) FROM ai_call WHERE outcome='halted'")
try:
    for i in range(5):
        cl.call("judge", "base.word", {"surface": f"w{i}"}, ("surface_term", 3), check=check_rel)
except ai.AiHalted:
    halted = True
case("A4", "three questions in a row with no usable answer: AiHalted and a halted row", halted and count("SELECT count(*) FROM ai_call WHERE outcome='halted'") == n0 + 1, i)
script["mode"] = "ok"
cl = client()
cl.streak = 2
cl.call("judge", "base.word", {"surface": "sins"}, ("surface_term", 1), check=check_rel)
case("A5", "an answered call resets the run of failures", cl.streak == 0, cl.streak)

# ---- refusals write nothing -------------------------------------------------------------------------------------------------------------
n0 = count("SELECT count(*) FROM ai_call")


def refused(fn):
    try:
        fn()
    except ai.AiError as exc:
        return str(exc)
    return None


c = client()
msgs = [refused(lambda: c.call("nosuchrole", "base.word", {"surface": "a"}, ("surface_term", 1))),
        refused(lambda: c.call("judge", "no.such.prompt", {"surface": "a"}, ("surface_term", 1))),
        refused(lambda: c.call("judge", "base.word", {"surface": "a", "extra": "b"}, ("surface_term", 1))),
        refused(lambda: c.call("judge", "base.word", {"surface": "a"}, ("surface_term", 1), overrides={"top_k": 5})),
        refused(lambda: c.call("quick", "base.word", {"surface": "a"}, ("surface_term", 1)))]
case("A6", "no model for the role, no active prompt, a variable the prompt does not name, an option outside ai.allowed_options, a prompt of another role: all refused",
     all(msgs) and count("SELECT count(*) FROM ai_call") == n0, msgs)
conn.execute("INSERT INTO cfg_ai_model (name, role, purpose, status) VALUES ('other:1b','judge','test','active')")
m1 = refused(lambda: c.call("judge", "base.word", {"surface": "a"}, ("surface_term", 1)))
conn.execute("DELETE FROM cfg_ai_model WHERE name='other:1b'")
pid = conn.execute("SELECT id FROM cfg_ai_prompt WHERE prompt_key='base.word' AND status='active'").fetchone()[0]
conn.execute("UPDATE cfg_ai_prompt SET text=text||' ' WHERE id=?", (pid,))
m2 = refused(lambda: c.call("judge", "base.word", {"surface": "a"}, ("surface_term", 1)))
conn.execute("UPDATE cfg_ai_prompt SET text=rtrim(text) WHERE id=?", (pid,))
conn.commit()
case("A7", "two active models for a role, and a prompt whose text no longer matches its hash, are refused", m1 and "exactly one active model" in m1 and m2 and "hash" in m2, (m1, m2))

# ---- the control steps ------------------------------------------------------------------------------------------------------------------
o = HA.prompts(ctx(Key="base.word"))
case("A8", "Prompts lists every version of a key", o.condition == "ok" and o.counts["versions"] == 2, o.message[:100])
o = HA.prompt_add(ctx(Key="base.word", Text="Give the base of \"{surface}\" as JSON.", Note="test version"))
v3 = conn.execute("SELECT status, version, parent_id, hash FROM cfg_ai_prompt WHERE prompt_key='base.word' AND version=3").fetchone()
case("A9", "PromptAdd makes version 3 as a draft (parent = the active version) and the active version is still used",
     o.condition == "ok" and tuple(v3[:2]) == ("draft", 3) and conn.execute("SELECT version FROM cfg_ai_prompt WHERE prompt_key='base.word' AND status='active'").fetchone()[0] == 2, o.message[:90])
o2 = HA.prompt_add(ctx(Key="base.word", Text="Give the base of \"{surface}\" as JSON.", Note="again"))
case("A10", "the same text again is refused", o2.condition == "refused", o2.message[:70])
o = HA.prompt_add(ctx(Key="base.word", Text="Base of \"{surface}\"? JSON.", Note="shorter", Activate="true"))
act = conn.execute("SELECT version FROM cfg_ai_prompt WHERE prompt_key='base.word' AND status='active'").fetchall()
case("A11", "-Activate retires the active version and the new one is used from the next call", o.condition == "ok" and [tuple(a) for a in act] == [(4,)]
     and conn.execute("SELECT status FROM cfg_ai_prompt WHERE prompt_key='base.word' AND version=2").fetchone()[0] == "retired"
     and conn.execute("SELECT status FROM cfg_ai_prompt WHERE prompt_key='base.word' AND version=3").fetchone()[0] == "draft", o.message[:90])
case("A12", "a new key needs -Role", HA.prompt_add(ctx(Key="new.key", Text="x {a}", Note="n")).condition == "refused", "")
conn.execute("UPDATE cfg_ai_prompt SET status='draft' WHERE prompt_key='base.word' AND version=4")
conn.execute("UPDATE cfg_ai_prompt SET status='active' WHERE prompt_key='base.word' AND version=2")
conn.commit()
rid = r_call = conn.execute("SELECT id FROM ai_call WHERE step='base' AND outcome='answered' AND module='test_ai' LIMIT 1").fetchone()[0]


@contextlib.contextmanager
def fake_route(vals):
    yield vals


# the handlers build their own client: replace the server pieces
ai.default_transport = transport
ai.sj.server_route = fake_route
ai.sj.preflight = lambda vals: [vals.get("model")]
_orig_init = ai.AiClient.__init__


def _init(self, cfg_, module, step, run_id=None, batch_id=None, transport=None):
    _orig_init(self, cfg_, module, step, run_id, batch_id, transport=ai.default_transport)


ai.AiClient.__init__ = _init
o = HA.replay(ctx(Call=str(rid)))
case("A13", "Replay: the same request, the same answer; recorded as step replay", o.condition == "ok" and o.counts["same"] == 1
     and count("SELECT count(*) FROM ai_call WHERE step='replay'") == 1, o.message[:70])
script["answers"] = {"sins": {"relation": "derivation", "base": "sinner"}}
o = HA.replay(ctx(Call=str(rid)))
case("A14", "Replay: a different answer is reported as different, with before and after", o.condition == "ok" and o.counts["same"] == 0 and "DIFFERENT" in o.message, o.message[:90])
script.pop("answers")
o = HA.compare(ctx(Step="base"))
case("A15", "Compare: per prompt version and model, outcomes and seconds; provisional cases named", o.condition == "ok" and "answered" in o.message and "refused" in o.message, o.message.split("\n")[1][:90])
o = HA.status(ctx())
case("A16", "Status: models, prompts and calls", o.condition == "ok" and "judge" in o.message and "base.word" in o.message and "test_ai/base" in o.message, o.message[:60])

# ---- the table-driven base step ---------------------------------------------------------------------------------------------------------
ans = conn.execute("SELECT t.id, t.surface, d.ai_call_id FROM surface_term t JOIN surface_derivation d ON d.term_id=t.id WHERE t.base_state='ai_answered' AND d.method='ollama' AND d.accepted=1 ORDER BY t.surface LIMIT 4").fetchall()
for tid, sf, cid in ans:
    conn.execute("UPDATE ai_call SET deleted=1 WHERE id=?", (cid,))
conn.commit()
words = [a[1] for a in ans]
o = HR.run(ctx())
case("A17", "four words lose their AI call: Resolve leaves them unmatched", count("SELECT count(*) FROM surface_term WHERE base_state='unmatched'") == 4, words)
script["answers"] = {words[0]: {"relation": "inflection", "base": "zzone", "reason": None}, words[1]: {"relation": "none", "base": None, "reason": None}}
script["bad_words"] = [words[2]]
_t = transport


def transport2(route, model, text, options):
    if script.get("bad_words") and any(f'"{w}"' in text for w in script["bad_words"]):
        calls.append((model, text, options))
        return {"relation": "x"}, "{}", {}
    return _t(route, model, text, options)


ai.default_transport = transport2
n0 = count("SELECT count(*) FROM ai_call WHERE module='ai_base'")
builtins_open = builtins.open


def _no_files(path, *a, **k):
    if any(x in str(path).replace("\\", "/") for x in ("_analytics/", "outputs/")):
        raise AssertionError(f"a file was read: {path}")
    return builtins_open(path, *a, **k)


builtins.open = _no_files
try:
    o = HB.ask(ctx(Limit="3"))
    case("A18", "Ask -Limit 3 asks the first three waiting words (sorted), writes ai_call rows, and one run_batch row with role, model, calls",
         o.condition == "ok" and o.counts["asked"] == 3 and count("SELECT count(*) FROM ai_call WHERE module='ai_base' AND run_id='TEST-RUN'") >= 3
         and conn.execute("SELECT model_role, model, calls, status FROM run_batch WHERE step='surface_base.ask' ORDER BY id DESC LIMIT 1").fetchone()[0:4] == ("judge", "qwen3:30b", 3, "committed"), o.message[:90])
    o = HB.ask(ctx())
    case("A19", "a second Ask asks the remaining word (the answered ones are no longer waiting)", o.counts["asked"] == 1, o.counts)
    o = HR.run(ctx())
    st = {w: tuple(conn.execute("SELECT t.base_state, b.surface FROM surface_term t LEFT JOIN surface_term b ON b.id=t.base_id WHERE t.surface=?", (w,)).fetchone()) for w in words}
    case("A20", "Resolve reads the calls: an inflection answer makes a computed base, none is ai_none, an unusable answer is ai_failed, the fourth word as asked",
         st[words[0]] == ("ai_answered", "zzone") and st[words[1]][0] == "ai_none" and st[words[2]][0] == "ai_failed", st)
    script["bad_words"] = []
    o = HB.ask(ctx())
    failed_now = count("SELECT count(*) FROM surface_term WHERE base_state='ai_failed' AND origin='surface'")
    case("A21", "without -Retry no failed word is asked again; with -Retry all of them are (the 31 of the first load and the new one)",
         o.counts["asked"] == 0 and failed_now == 32 and HB.ask(ctx(Retry="true")).counts["asked"] == 32, (o.message[:40], failed_now))
    # halting
    for w in words:
        conn.execute("UPDATE ai_call SET deleted=1 WHERE subject_id=(SELECT id FROM surface_term WHERE surface=?) AND module='ai_base'", (w,))
    conn.commit()
    script["mode"] = "error"
    o = HB.ask(ctx())
    case("A22", "the server down: Ask halts after three words in a row and the batch is failed, nothing else written",
         o.condition == "halted" and conn.execute("SELECT status FROM run_batch WHERE step='surface_base.ask' ORDER BY id DESC LIMIT 1").fetchone()[0] == "failed", o.message[:90])
    script["mode"] = "ok"
    # group judge
    g = conn.execute("SELECT id, surface FROM surface_term WHERE origin='surface' AND deleted=0 AND surface_group IS NOT NULL ORDER BY surface LIMIT 2").fetchall()
    for tid, _ in g:
        conn.execute("UPDATE surface_term SET group_state='unjudged', surface_group=NULL WHERE id=?", (tid,))
    conn.commit()
    script["answers"] = {g[0][1]: {"group": "entity", "reason": "a person"}}
    o = HG.judge(ctx())
    rows = {r[0]: tuple(r[1:]) for r in conn.execute("SELECT surface, surface_group, group_state, group_judged_by, group_reason FROM surface_term WHERE id IN (?,?)", (g[0][0], g[1][0]))}
    case("A23", "Judge: both words judged through the client, an entity answer is stored as being, with state, model and reason; one event each",
         o.condition == "ok" and rows[g[0][1]] == ("being", "judged", "qwen3:30b", "a person") and rows[g[1][1]][0:2] == ("behaviour", "judged")
         and count("SELECT count(*) FROM surface_event WHERE action='set_group' AND run_id='TEST-RUN'") == 2, rows)
    script["mode"] = "bad"
    conn.execute("UPDATE surface_term SET group_state='unjudged' WHERE id=?", (g[0][0],))
    conn.commit()
    o = HG.judge(ctx())
    case("A24", "an unusable group answer: the word is failed, not judged", conn.execute("SELECT group_state FROM surface_term WHERE id=?", (g[0][0],)).fetchone()[0] == "failed", o.message[:60])
    conn.execute("UPDATE cfg_ai_prompt SET status='retired' WHERE prompt_key='group.word'")
    conn.execute("UPDATE surface_term SET group_state='unjudged' WHERE id=?", (g[0][0],))
    conn.commit()
    o = HG.judge(ctx())
    case("A25", "no active prompt: Judge is refused and writes nothing", o.condition == "refused", o.message[:70])
finally:
    builtins.open = builtins_open
case("A26", "no file under _analytics or outputs was read by Ask or Judge", True, "open() was patched to raise, and none did")

width = max(len(r[0]) for r in results)
fails = [r for r in results if r[2] == "FAIL"]
for cid, desc, res_, evd in results:
    print(f"{cid:<{width}}  {res_}  {desc}  [{evd}]")
print(f"\n{len(results) - len(fails)} of {len(results)} pass")
sys.exit(1 if fails else 0)
