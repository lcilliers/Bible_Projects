"""temp_2354_surface_judge_tests.py -- the test plan of the surface judging tool (#2354, B:46), run against a COPY of
iba.db (argument 1) with a stub Ollama server for the deterministic cases and, when --real is given, the real
server for 3 surfaces. Throwaway test script: nothing here touches the live database or the live batch folder.

A copy is single-use: the handler cases commit their changes to it. Take a new one for each run (dbsnapshot --copy-to).

Usage:  python iba/app/staging/surface_judge_tests/temp_2354_surface_judge_tests.py <copy.db> <scratch-dir> [--real]
"""
import json
import pathlib
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "iba" / "app").is_dir())
sys.path.insert(0, str(ROOT))
from iba.app.handlers import surfacejudge as h  # noqa: E402
from iba.app.handlers.base import Ctx  # noqa: E402
from iba.app.lib import surfacejudge as sj  # noqa: E402
from iba.app.lib.cfg import Cfg  # noqa: E402

DB = pathlib.Path(sys.argv[1])
SCR = pathlib.Path(sys.argv[2])
REAL = "--real" in sys.argv
RESULTS = []


def case(cid, what, ok, detail=""):
    RESULTS.append((cid, what, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {cid}  {what}  {detail}")


# ---- stub server: the answer is chosen by the English in the prompt -------------------------------------------
MODEL_ON_STUB = "qwen3:30b"
SCRIPT = {}  # surface -> list of answers (strings) returned in turn; "DOWN" is not used (server stopped instead)
CALLS = []


DELAY = 0.0   # seconds the stub takes to answer a chat call


class Stub(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        out = json.dumps({"models": [{"name": MODEL_ON_STUB}]}).encode() if self.path == "/api/tags" else b"{}"
        self.send_response(200)
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        prompt = body["messages"][0]["content"]
        surface = prompt.split('English: "', 1)[1].split('"\n', 1)[0]
        CALLS.append(surface)
        time.sleep(DELAY)
        seq = SCRIPT.get(surface, ['{"group":"other","reason":"no bearing"}'])
        content = seq.pop(0) if len(seq) > 1 else seq[0]
        out = json.dumps({"message": {"content": content}, "eval_count": 5, "eval_duration": 1_000_000_000,
                          "prompt_eval_count": 50}).encode()
        self.send_response(200)
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)


srv = HTTPServer(("127.0.0.1", 0), Stub)
threading.Thread(target=srv.serve_forever, daemon=True).start()
HOST = f"http://127.0.0.1:{srv.server_port}"

cfg = Cfg(DB)
real = sj.settings(cfg)
stub = dict(real, host=HOST, timeout_seconds=5, tunnel_local_port=None)   # the stub is local: no tunnel to it
G = real["groups"]
SG = sj.stored_groups(real)

# ---- settings -----------------------------------------------------------------------------------------------
case("S1", "settings read from the copy: groups include other, every stored_as key is a group, prompt has {surface}",
     "other" in G and set(real["stored_as"]) <= set(G) and len(SG) == len(G) and "{surface}" in real["word_prompt"], str(G))


class Fake:
    def __init__(self, d):
        self.d = d

    def setting(self, k, default=None):
        return self.d.get(k)


full = {f"ollama.{k}": 1 for k in ("host", "model", "timeout_seconds", "keep_alive", "num_ctx", "temperature",
                                       "connect_timeout_seconds")}
full["surface_judge.max_consecutive_failures"] = 3
full["surface_judge.groups"] = ["a"]
full["surface_judge.word_prompt"] = "x {surface}"
try:
    sj.settings(Fake({k: v for k, v in full.items() if k != "ollama.model"}))
    case("S2", "a missing setting stops the run", False)
except sj.JudgeError as e:
    case("S2", "a missing setting stops the run", "ollama.model" in str(e), str(e))
try:
    sj.settings(Fake(dict(full, **{"surface_judge.groups": []})))
    case("S3", "empty groups stops the run", False)
except sj.JudgeError as e:
    case("S3", "empty groups stops the run", True, str(e))
try:
    sj.settings(Fake(dict(full, **{"surface_judge.group_stored_as": {"zzz": "being"}})))
    case("S6", "a group_stored_as key that is not a group stops the run", False)
except sj.JudgeError as e:
    case("S6", "a group_stored_as key that is not a group stops the run", "group_stored_as" in str(e), str(e)[:60])
try:
    sj.settings(Fake(dict(full, **{"surface_judge.word_prompt": "no place"})))
    case("S4", "a prompt without {surface} stops the run", False)
except sj.JudgeError as e:
    case("S4", "a prompt without {surface} stops the run", True, str(e))

# ---- check_word ---------------------------------------------------------------------------------------------
case("C1", "a valid group passes", sj.check_word({"group": "entity"}, G) == [])
case("C5", "the stored name being is not accepted from the model", sj.check_word({"group": "being"}, G) != [])
case("C2", "an unknown group is refused", sj.check_word({"group": "qualifier"}, G) != [])
case("C3", "a non-object is refused", sj.check_word(["being"], G) == ["not an object"])
case("C4", "a missing group is refused", sj.check_word({}, G) != [])

# ---- judge_word (stub) --------------------------------------------------------------------------------------
SCRIPT["love"] = ['{"group":"behaviour","reason":null}']
r = sj.judge_word(stub, "love")
case("J1", "a good answer is recorded", r["group"] == "behaviour" and r["errors"] == [] and r["judged_by"] == real["model"], str(r))
SCRIPT["heart"] = ['{"group":"nonsense"}', '{"group":"entity","reason":null}']
r = sj.judge_word(stub, "heart")
case("J2", "a bad group then a good one: retried once, recorded as the stored name being, the error kept",
     r["group"] == "being" and len(r["errors"]) == 1, str(r["errors"]))
SCRIPT["xyz"] = ['{"group":"bad1"}', '{"group":"bad2"}']
r = sj.judge_word(stub, "xyz")
case("J3", "two bad answers: group null, two errors, judged_by null",
     r["group"] is None and len(r["errors"]) == 2 and r["judged_by"] is None)
SCRIPT["junk"] = ["this is not json", "still not json"]
r = sj.judge_word(stub, "junk")
case("J4", "an answer that is not JSON: group null, call-failed errors", r["group"] is None and len(r["errors"]) == 2, str(r["errors"][:1]))
SCRIPT["and"] = ['{"group":"other","reason":"links words"}']
r = sj.judge_word(stub, "and")
case("J5", "other with its reason", r["group"] == "other" and r["reason"] == "links words")
SCRIPT['say "hi"'] = ['{"group":"behaviour","reason":null}']
r = sj.judge_word(stub, 'say "hi"')
case("J6", "a surface with a quote mark in it is sent whole", r["group"] == "behaviour")
dead = dict(stub, host="http://127.0.0.1:1")
r = sj.judge_word(dead, "love")
case("J7", "server unreachable: group null, no crash", r["group"] is None and len(r["errors"]) == 2, str(r["errors"][:1]))

# ---- the check before a run (preflight) and the halt ----------------------------------------------------------
import time  # noqa: E402

dead = dict(stub, host="http://127.0.0.1:1")

MODEL_ON_STUB = real["model"]
case("PF1", "preflight passes when the server answers and has the model", real["model"] in sj.preflight(stub))
t0 = time.time()
try:
    sj.preflight(dead)
    case("PF2", "preflight refuses when nothing is listening", False)
except sj.JudgeError as e:
    case("PF2", "preflight refuses when nothing is listening (message names the host and says nothing was run)",
         "did not answer" in str(e) and "nothing was run" in str(e) and dead["host"] in str(e), str(e)[:90])
try:
    sj.preflight(dict(dead, ssh_target="u@h", ssh_key="~/.ssh/k"))
    case("PF9", "the refusal names the configured ssh way in", False)
except sj.JudgeError as e:
    case("PF9", "the refusal names the configured ssh way in (key path and target, from settings)",
         "ssh -i ~/.ssh/k u@h" in str(e), str(e)[-110:])
try:
    sj.preflight(dict(dead, ssh_target=None, ssh_key=None))
except sj.JudgeError as e:
    case("PF10", "with no ssh settings the refusal still names the address and says nothing was run",
         "ssh -i" not in str(e) and "nothing was run" in str(e))
case("S7", "the ssh settings are read from the copy (path only, no key is read)",
     bool(real["ssh_target"]) and bool(real["ssh_key"]), str(real["ssh_key"]))
try:
    sj.preflight(dict(stub, model="nope:1b"))
    case("PF3", "preflight refuses a model the server does not have", False)
except sj.JudgeError as e:
    case("PF3", "preflight refuses a model the server does not have, and names the models it has",
         "no model" in str(e) and real["model"] in str(e), str(e)[:90])
ghost = SCR / "ghost-v1-20261103.jsonl"
if ghost.exists():
    ghost.unlink()
try:
    sj.run_words(dead, ["a", "b"], ghost)
    case("PF4", "a run against a dead server stops before the first surface", False)
except sj.JudgeError:
    case("PF4", "a run against a dead server stops before the first surface and writes no file", not ghost.exists())
slow = dict(dead, host="http://10.255.255.1:11434", connect_timeout_seconds=2)
t1 = time.time()
try:
    sj.preflight(slow)
except sj.JudgeError:
    pass
case("PF5", "preflight gives up within its timeout on an address that never answers (2 s set)",
     time.time() - t1 < 6, f"{time.time() - t1:.1f} s")
halt_out = SCR / "halt-v1-20261103.jsonl"
if halt_out.exists():
    halt_out.unlink()
SCRIPT.clear()
for w in "abcde":
    SCRIPT[w] = ['{"group":"x"}', '{"group":"x"}']
res = sj.run_words(stub, list("abcde"), halt_out)
case("PF7", "3 surfaces in a row with no answer halt the run (not 5 attempts)", res["halted"] and res["failed"] == 3
     and len(halt_out.read_text(encoding="utf-8").splitlines()) == 3, str(res))
seq_out = SCR / "seq-v1-20261103.jsonl"
if seq_out.exists():
    seq_out.unlink()
SCRIPT.clear()
for w in "ab":
    SCRIPT[w] = ['{"group":"x"}', '{"group":"x"}']
SCRIPT["c"] = ['{"group":"entity","reason":null}']
for w in "de":
    SCRIPT[w] = ['{"group":"x"}', '{"group":"x"}']
res = sj.run_words(stub, list("abcde"), seq_out)
case("PF8", "a good answer resets the count: 2 fail, 1 passes, 2 fail does not halt",
     not res["halted"] and res["judged"] == 1 and res["failed"] == 4, str(res))
SCRIPT.clear()

# ---- surface_list / status ----------------------------------------------------------------------------------
lst = sj.surface_list(cfg.conn)
names = [s for s, _ in lst]
exp = cfg.conn.execute("SELECT COUNT(DISTINCT surface) FROM surface_subgroup WHERE deleted=0 AND trim(surface)<>''").fetchone()[0]
case("L1", "the list is the distinct live non-blank surfaces of surface_subgroup (the 4 blank-surface rows are left out)", len(lst) == exp == len(set(names)), f"{len(lst)}")
case("L2", "most rows first, then alphabetical (every neighbouring pair)",
     all(a[1] > b[1] or (a[1] == b[1] and a[0] < b[0]) for a, b in zip(lst, lst[1:])), str(lst[:3]))
case("L3", "no empty or null surface", all(s and s.strip() for s in names))

out = SCR / "t-v1-20261102.jsonl"
if out.exists():
    out.unlink()
st = sj.status(cfg.conn, SG, out)
case("T1", "status with no file: nothing judged, all left", st["judged"] == 0 and st["left"] == len(lst) and st["failed"] == 0, str(st))

# ---- run_words (stub) ---------------------------------------------------------------------------------------
sub = names[:6]
SCRIPT.clear()
CALLS.clear()
res = sj.run_words(stub, sub, out, limit=4)
case("R1", "limit 4 judges 4 and writes 4 lines", res == {"judged": 4, "failed": 0, "stopped": False, "halted": False, "period_over": False}
     and len(out.read_text(encoding="utf-8").splitlines()) == 4, str(res))
res = sj.run_words(stub, sub, out)
case("R2", "run again: only the 2 not yet judged are sent", res["judged"] == 2 and CALLS[4:] == sub[4:], f"{res} {CALLS}")
res = sj.run_words(stub, sub, out)
case("R3", "run again when all done: nothing sent", res["judged"] == 0 and len(CALLS) == 6)
# failed word retried
bad = SCR / "t-v1-20261103.jsonl"
if bad.exists():
    bad.unlink()
SCRIPT[sub[0]] = ['{"group":"x"}', '{"group":"x"}']
res = sj.run_words(stub, sub[:2], bad)
case("R4", "a failed word is recorded (group null)", res == {"judged": 1, "failed": 1, "stopped": False, "halted": False, "period_over": False}, str(res))
SCRIPT[sub[0]] = ['{"group":"entity","reason":null}']
CALLS.clear()
res = sj.run_words(stub, sub[:2], bad)
case("R5", "next run tries only the failed word again", res["judged"] == 1 and CALLS == [sub[0]], str(CALLS))
last = sj.read_batch(bad)[sub[0]]
case("R6", "the last record of a word is the one read (stored as being)", last["group"] == "being")
# Ctrl+C
ctl = SCR / "t-v1-20261104.jsonl"
if ctl.exists():
    ctl.unlink()
n = {"i": 0}


def boom(msg):
    n["i"] += 1
    if n["i"] == 2:
        raise KeyboardInterrupt


res = sj.run_words(stub, sub, ctl, emit=boom)
case("R7", "Ctrl+C: stops, the word in hand is already written", res["stopped"] and
     len(ctl.read_text(encoding="utf-8").splitlines()) == 2, str(res))
st = sj.status(cfg.conn, SG, ctl)
case("T2", "status counts judged per group and what is left", st["judged"] == 2 and st["left"] == len(lst) - 2
     and sum(st["per_group"].values()) == 2, str(st))
case("T3", "status counts failed words separately", sj.status(cfg.conn, SG, bad)["failed"] == 0)

# ---- handler (stub, scratch batch folder) ---------------------------------------------------------------------
cfg.conn.execute("UPDATE cfg_setting SET value=? WHERE key='surface_judge.batch_dir'", (json.dumps(SCR.as_posix()),))
cfg.conn.execute("UPDATE cfg_setting SET value=? WHERE key='ollama.host'", (json.dumps(HOST),))
cfg.conn.execute("DELETE FROM cfg_setting WHERE key='ollama.tunnel_local_port'")   # the stub is local: no tunnel
cfg.conn.execute("UPDATE cfg_setting SET value=5 WHERE key='ollama.timeout_seconds'")


def ctx(**p):
    return Ctx(db=None, cfg=cfg, step=None, run_id="TEST", word="", word_id=None, params=p, step_id="x")


o = h.status(ctx())
case("H1", "status without -Batch is refused", o.condition == "refused" and "-Batch" in o.message, o.message)
for bad_name in ("First-Split-v1-20261102", "first_split-v1-20261102", "first-split-20261102", "first-split-v0-20261102",
                 "first-split-v1-2026", "../x-v1-20261102"):
    o = h.status(ctx(Batch=bad_name))
    case("H2", f"bad batch name {bad_name!r} is refused", o.condition == "refused", o.message[:60])
o = h.status(ctx(Batch="h-v1-20261102"))
case("H3", "status of a batch with no file says so", o.condition == "ok" and "no file yet" in o.message, o.message.splitlines()[0])
for lim in ("0", "-1", "abc", "1.5"):
    o = h.run(ctx(Batch="h-v1-20261102", Limit=lim))
    case("H4", f"-Limit {lim!r} is refused", o.condition == "refused", o.message[:60])
CALLS.clear()
o = h.run(ctx(Batch="h-v1-20261102", Limit="3"))
f = SCR / "h-v1-20261102.jsonl"
case("H5", "run -Limit 3 judges 3 and writes the file in batch_dir", o.condition == "ok" and o.counts["judged"] == 3
     and len(f.read_text(encoding="utf-8").splitlines()) == 3 and o.counts["left"] == len(lst) - 3, o.message)
o = h.run(ctx(Batch="h-v1-20261102", Limit="2"))
case("H6", "run again carries on from where it stopped", o.counts["judged"] == 2 and CALLS[3:] == names[3:5], str(CALLS))
o = h.status(ctx(Batch="h-v1-20261102"))
case("H7", "status after two runs: 5 judged", "judged: 5" in o.message, o.message.replace("\n", " | ")[:200])
cfg.conn.execute("UPDATE cfg_setting SET value=? WHERE key='ollama.host'", (json.dumps("http://127.0.0.1:1"),))
nofile = SCR / "dead-v1-20261103.jsonl"
if nofile.exists():
    nofile.unlink()
o = h.run(ctx(Batch="dead-v1-20261103", Limit="2"))
case("H9", "the handler refuses to run against a dead server, names it, and writes nothing",
     o.condition == "refused" and "did not answer" in o.message and not nofile.exists(), o.message[:90])
cfg.conn.execute("UPDATE cfg_setting SET value=? WHERE key='ollama.host'", (json.dumps(HOST),))
SCRIPT.clear()
for w in names[:6]:
    SCRIPT[w] = ['{"group":"x"}', '{"group":"x"}']
o = h.run(ctx(Batch="halt-v2-20261103", Limit="6"))
case("H10", "the handler reports a halt as the condition halted", o.condition == "halted" and o.counts["failed"] == 3, o.message[:110])
SCRIPT.clear()
cfg.conn.execute("DELETE FROM cfg_setting WHERE key='surface_judge.word_prompt'")
o = h.run(ctx(Batch="h-v1-20261102", Limit="1"))
case("H8", "a missing setting is refused, nothing written", o.condition == "refused" and
     len(f.read_text(encoding="utf-8").splitlines()) == 5, o.message[:80])
cfg.conn.rollback()

# ---- the ssh tunnel (ollama.tunnel_local_port) --------------------------------------------------------------------
import socket  # noqa: E402

with sj.server_route(stub) as r:
    case("TN1", "no tunnel port set: the values pass through unchanged", r is stub and r["host"] == HOST)
try:
    sj.settings(Fake(dict(full, **{"ollama.tunnel_local_port": 11435})))
    case("TN2", "a tunnel port without ssh_target and ssh_key stops the run", False)
except sj.JudgeError as e:
    case("TN2", "a tunnel port without ssh_target and ssh_key stops the run", "ssh_target" in str(e), str(e))
bad = dict(stub, tunnel_local_port=11437, ssh_target="nobody@127.0.0.1", ssh_key=str(SCR / "no-such-key"),
           connect_timeout_seconds=3)
try:
    with sj.server_route(bad):
        case("TN3", "a tunnel that cannot be opened refuses, naming the target and key", False)
except sj.JudgeError as e:
    case("TN3", "a tunnel that cannot be opened refuses, naming the target and key",
         "nobody@127.0.0.1" in str(e) and "nothing was run" in str(e), str(e)[:160])
with socket.socket() as s:
    case("TN4", "the failed tunnel left nothing listening on its local port", s.connect_ex(("127.0.0.1", 11437)) != 0)
res = None
try:
    res = sj.run_words(bad, ["a"], SCR / "tunnel-bad-v1-20261103.jsonl")
except sj.JudgeError:
    pass
case("TN5", "run_words with an unopenable tunnel writes nothing",
     res is None and not (SCR / "tunnel-bad-v1-20261103.jsonl").exists())

# ---- the cycle (run_cycle), its progress, stop and restart ---------------------------------------------------------
cyc_real = sj.cycle_settings(cfg)
case("CY0", "the four cycle settings are read from the copy as numbers",
     len(cyc_real) == 4 and all(isinstance(v, (int, float)) for v in cyc_real.values()), str(cyc_real))
for cid, what, bad in (("CY9a", "a missing cycle setting stops the cycle", None),
                       ("CY9b", "a work period of 0 minutes stops the cycle", 0),
                       ("CY9c", "a text value stops the cycle", "ten"),
                       ("CY9d", "true is not accepted as a number", True)):
    d = {f"surface_judge.{k}": 1 for k in ("cycle_work_minutes", "cycle_cooldown_minutes", "cycle_halt_wait_minutes",
                                            "cycle_max_halts_in_a_row")}
    d["surface_judge.cycle_work_minutes"] = bad
    try:
        sj.cycle_settings(Fake(d))
        case(cid, what, False)
    except sj.JudgeError as e:
        case(cid, what, "cycle_work_minutes" in str(e), str(e))
d0 = {f"surface_judge.{k}": 1 for k in ("cycle_work_minutes", "cycle_halt_wait_minutes", "cycle_max_halts_in_a_row")}
case("CY9e", "a cool-down of 0 is allowed", sj.cycle_settings(Fake(dict(d0, **{"surface_judge.cycle_cooldown_minutes": 0})))
     ["cycle_cooldown_minutes"] == 0)

CYC = {"cycle_work_minutes": 0.0075, "cycle_cooldown_minutes": 0.001, "cycle_halt_wait_minutes": 0.001,
       "cycle_max_halts_in_a_row": 2}   # 0.45 s of work, 60 ms of rest
cstub = dict(stub, max_consecutive_failures=3)
LIST = list("abcdefghij")


def cyc_out(name):
    p = SCR / f"{name}-v1-20261103.jsonl"
    for q in (p, sj.progress_path(p), sj.stop_path(p)):
        q.unlink(missing_ok=True)
    return p


DELAY_BEFORE = DELAY
DELAY = 0.05
# CY1 + CY2: the whole list across several work periods with rests, progress readable while it runs
o1 = cyc_out("cy1")
SCRIPT.clear()
CALLS.clear()
seen = []
res = sj.run_cycle(cstub, CYC, LIST, o1, emit=lambda m: seen.append((m, sj.read_progress(o1))))
final = sj.read_progress(o1)
case("CY1", "the whole list is judged across more than one work period, ending finished",
     res["state"] == "finished" and res["periods"] >= 2 and final["judged"] == 10 and final["left"] == 0
     and sorted(CALLS) == sorted(LIST), f"periods {res['periods']} state {res['state']} calls {len(CALLS)}")
mid = [p for m, p in seen if p and p["state"] == "running" and p["judged"] >= 2]
case("CY2", "while it runs the progress file moves: state running, judged counts, per group, speed and a finish estimate",
     bool(mid) and mid[0]["list"] == 10 and sum(mid[0]["per_group"].values()) == mid[0]["judged"]
     and mid[0]["mean_secs_last_50"] is not None and mid[0]["estimated_finish"], str(mid[0] if mid else None)[:200])
cool = [m for m, p in seen if m.startswith("cooling down")]
case("CY1b", "a rest is taken between periods (cooling down reported at least once)", len(cool) >= 1, str(cool[:1]))

# CY3: stop flag during work ends after the surface in hand; running it again resumes with no surface repeated
o3 = cyc_out("cy3")
CALLS.clear()
n = {"k": 0}


def stopper(m):
    n["k"] += 1
    if n["k"] == 3:
        sj.stop_path(o3).write_text("stop\n")


res = sj.run_cycle(cstub, dict(CYC, cycle_work_minutes=5), LIST, o3, emit=stopper)
got = sj.read_progress(o3)
case("CY3", "a stop flag ends the cycle after the surface in hand: state stopped, 3 or 4 judged",
     res["state"] == "stopped" and got["state"] == "stopped" and 3 <= got["judged"] <= 4, f"{got['state']} {got['judged']}")
first = list(CALLS)
res = sj.run_cycle(cstub, dict(CYC, cycle_work_minutes=5), LIST, o3, emit=None)
case("CY3b", "run again: the stale stop flag is cleared, it resumes and finishes with no surface judged twice",
     res["state"] == "finished" and res["judged"] == 10 and sorted(CALLS) == sorted(LIST) and not sj.stop_path(o3).exists(),
     f"{len(first)} then {len(CALLS) - len(first)}")

# CY4: stop during a rest
o4 = cyc_out("cy4")
slept = {"k": 0}


def sleeper(s):
    slept["k"] += 1
    sj.stop_path(o4).write_text("stop\n")
    time.sleep(min(s, 0.01))


res = sj.run_cycle(cstub, dict(CYC, cycle_cooldown_minutes=5), LIST, o4, sleep=sleeper)
case("CY4", "a stop flag during a rest ends the cycle at once: state stopped, not 5 minutes later",
     res["state"] == "stopped" and slept["k"] == 1 and res["judged"] < 10, f"{res['state']} judged {res['judged']}")

# CY5: the server never answers: waits, tries again, ends halted after the set number of periods; writes nothing
o5 = cyc_out("cy5")
res = sj.run_cycle(dict(cstub, host="http://127.0.0.1:1", connect_timeout_seconds=1), CYC, LIST, o5)
case("CY5", "no server: 2 periods in a row with no progress end the cycle halted, naming the address, nothing written",
     res["state"] == "halted" and res["halts_in_a_row"] == 2 and "127.0.0.1:1" in res["last_problem"]
     and not o5.exists(), f"{res['state']} {res['halts_in_a_row']}")

# CY6: the server comes back during the wait: the cycle carries on and finishes, the halt counter is cleared
o6 = cyc_out("cy6")
vv = dict(cstub, host="http://127.0.0.1:1", connect_timeout_seconds=1)


def revive(s):
    vv["host"] = HOST
    time.sleep(min(s, 0.01))


res = sj.run_cycle(vv, CYC, LIST, o6, sleep=revive)
case("CY6", "the server comes back after a halt: the cycle finishes and the halt count is back to 0",
     res["state"] == "finished" and res["judged"] == 10 and res["halts_in_a_row"] == 0, f"{res['state']} {res['halts_in_a_row']}")

# CY7: a second cycle on a live batch is refused; a stale progress file does not block
o7 = cyc_out("cy7")
sj.progress_path(o7).write_text(json.dumps({"state": "running", "updated_epoch": time.time()}))
try:
    sj.run_cycle(cstub, CYC, LIST, o7)
    case("CY7", "a second cycle on a batch whose progress is fresh is refused", False)
except sj.JudgeError as e:
    case("CY7", "a second cycle on a batch whose progress is fresh is refused", "is running" in str(e), str(e)[:90])
sj.progress_path(o7).write_text(json.dumps({"state": "running", "updated_epoch": time.time() - 3600}))
res = sj.run_cycle(cstub, CYC, LIST, o7)
case("CY7b", "a progress file not updated for an hour (an interrupted cycle) does not block a restart",
     res["state"] == "finished" and res["judged"] == 10)

# CY8: a surface that never gets a usable answer: the rest are judged, then the cycle ends halted
o8 = cyc_out("cy8")
SCRIPT.clear()
SCRIPT["z"] = ["not json"]
res = sj.run_cycle(cstub, CYC, ["a", "b", "z"], o8)
case("CY8", "a surface that never answers: the others are judged, the cycle ends halted, 1 failed and listed as left",
     res["state"] == "halted" and res["judged"] == 2 and res["failed"] == 1 and res["left"] == 1, f"{res['state']} {res['judged']}")
SCRIPT.clear()
DELAY = DELAY_BEFORE

# CY10: the handlers (stub, scratch batch folder): Progress, Stop, Cycle
cfg.conn.execute("UPDATE cfg_setting SET value=? WHERE key='surface_judge.batch_dir'", (json.dumps(SCR.as_posix()),))
cfg.conn.execute("UPDATE cfg_setting SET value=? WHERE key='ollama.host'", (json.dumps(HOST),))
cfg.conn.execute("DELETE FROM cfg_setting WHERE key='ollama.tunnel_local_port'")
cfg.conn.execute("UPDATE cfg_setting SET value=0.0075 WHERE key='surface_judge.cycle_work_minutes'")
cfg.conn.execute("UPDATE cfg_setting SET value=0.001 WHERE key='surface_judge.cycle_cooldown_minutes'")
hb = "cy10-v1-20261103"
hp = SCR / f"{hb}.jsonl"
for q in (hp, sj.progress_path(hp), sj.stop_path(hp)):
    q.unlink(missing_ok=True)
o = h.progress(ctx(Batch=hb))
case("CY10a", "Progress with no cycle run says so", o.condition != "refused" and "no progress file" in o.message, o.message[:90])
o = h.stop(ctx(Batch=hb))
case("CY10b", "Stop with no cycle running says so and writes no flag",
     "no cycle is running" in o.message and not sj.stop_path(hp).exists(), o.message[:90])
sj.progress_path(hp).write_text(json.dumps({"batch": hb, "state": "running", "updated_epoch": time.time() - 3600,
                                            "updated_at": "2026-11-03T01:00:00Z", "list": 10, "judged": 4, "failed": 0,
                                            "untried": 6, "left": 6, "per_group": {"other": 4}, "periods": 1,
                                            "judged_this_cycle": 4, "started_at": "x", "mean_secs_last_50": 9.5,
                                            "halts_in_a_row": 0}))
o = h.progress(ctx(Batch=hb))
case("CY10c", "Progress on a progress file that stopped moving says NOT running and how to resume",
     "NOT running" in o.message and "judged 4 of 10 (40.0 percent)" in o.message, o.message[:140])
sj.progress_path(hp).write_text(json.dumps({"batch": hb, "state": "cooling", "updated_epoch": time.time(),
                                            "updated_at": "now", "list": 10, "judged": 4, "failed": 0, "untried": 6,
                                            "left": 6, "per_group": {"other": 4}, "periods": 1, "judged_this_cycle": 4,
                                            "started_at": "x", "mean_secs_last_50": 9.5, "halts_in_a_row": 0,
                                            "next_resume_at": "2026-11-03T09:00:00Z", "estimated_finish": "2026-11-04T01:00:00Z",
                                            "estimate_note": "n"}))
o = h.progress(ctx(Batch=hb))
case("CY10d", "Progress on a live cycle shows the resume time and the estimated finish",
     "NOT running" not in o.message and "resumes work at 2026-11-03T09:00:00Z" in o.message
     and "estimated finish 2026-11-04T01:00:00Z" in o.message, o.message[:140])
o = h.stop(ctx(Batch=hb))
case("CY10e", "Stop on a live cycle writes the flag", sj.stop_path(hp).exists() and "stop requested" in o.message, o.message[:80])
o = h.cycle(ctx(Batch=hb))
case("CY10f", "Cycle on a live batch is refused, nothing written", o.condition == "refused" and "is running" in o.message,
     o.message[:90])
sj.progress_path(hp).unlink()
sj.stop_path(hp).unlink(missing_ok=True)
_real_list = sj.surface_list
sj.surface_list = lambda conn: [(x, 1) for x in LIST]   # the test list, not the 6,069 live surfaces
DELAY = 0.01
o = h.cycle(ctx(Batch=hb))
sj.surface_list = _real_list
DELAY = DELAY_BEFORE
case("CY10g", "Cycle through the handler judges the list across periods and reports finished",
     o.condition == "ok" and "finished" in o.message, o.message[:120])
case("CY10h", "the handler's cycle left a finished progress file with all 10 judged",
     sj.read_progress(hp)["state"] == "finished" and sj.read_progress(hp)["judged"] == 10)
cfg.conn.rollback()

# ---- the real server ----------------------------------------------------------------------------------------------
if REAL:
    tp = real.get("tunnel_local_port")
    case("TN6", "the copy carries ollama.tunnel_local_port", tp is not None, str(tp))
    with sj.server_route(real) as r:
        models = sj.preflight(r)
        case("TN7", "the real server answers through the tunnel and has the model", real["model"] in models,
             r["host"])
    with socket.socket() as s:
        case("TN8", "the tunnel is closed after the block", s.connect_ex(("127.0.0.1", int(tp))) != 0)
    cyc_out_real = SCR / "cyr-v1-20261103.jsonl"
    for q in (cyc_out_real, sj.progress_path(cyc_out_real), sj.stop_path(cyc_out_real)):
        q.unlink(missing_ok=True)
    pr = sj.run_cycle(real, {"cycle_work_minutes": 5, "cycle_cooldown_minutes": 0, "cycle_halt_wait_minutes": 0.01,
                             "cycle_max_halts_in_a_row": 2}, ["good", "fear", "heart"], cyc_out_real, emit=print)
    recs = sj.read_batch(cyc_out_real)
    case("CYR1", "the cycle on the real server through the tunnel judges 3 surfaces with a valid group and the "
         "server's own counts, and finishes",
         pr["state"] == "finished" and pr["judged"] == 3 and all(r["group"] in SG and "out_tokens" in r
                                                                  for r in recs.values()), str(pr["per_group"]))

fails = [r for r in RESULTS if not r[2]]
print(f"\n{len(RESULTS)} cases, {len(RESULTS) - len(fails)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)
