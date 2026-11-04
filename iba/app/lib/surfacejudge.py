"""surfacejudge.py -- the first split of the surfaces of the concepts into behaviour, state, being or other
(escalation #2354, researcher 2026-11-02).

The list is the distinct surface of surface_subgroup (the surfaces the concepts are built on). Each surface is put to
the Ollama server on its own, one call per string, with no Hebrew or Greek code, no verse and no neighbouring word.
The model answers one group of cfg_setting surface_judge.groups; a surface goes to the first three only when it
definitely belongs there, otherwise to `other`, the residue the researcher cleans up in a later pass. The answers are
appended to a batch file, one JSON line per surface, as each finishes; nothing here writes the database. Every
verdict is inferential (B:4) until the researcher confirms it.

Server and limits come from cfg_setting modules `ollama` and `surface_judge`; the prompt text and the groups are
cfg_setting rows too (surface_judge.word_prompt, surface_judge.groups).
"""
from __future__ import annotations

import contextlib
import json
import os
import pathlib
import socket
import subprocess
import time
import urllib.parse
import urllib.request

from .cfg import Cfg


class JudgeError(Exception):
    pass


def settings(cfg: Cfg) -> dict:
    """The server, the limits, the groups and the prompt; stops when a setting is missing."""
    keys = ["ollama.host", "ollama.model", "ollama.timeout_seconds", "ollama.keep_alive", "ollama.num_ctx",
            "ollama.temperature", "ollama.connect_timeout_seconds", "surface_judge.groups",
            "surface_judge.word_prompt", "surface_judge.max_consecutive_failures"]
    got = {k.split(".", 1)[1]: cfg.setting(k) for k in keys}
    missing = [k for k, v in zip(keys, got.values()) if v is None]
    if missing:
        raise JudgeError(f"cfg_setting missing: {missing}")
    # how the machine is reached over ssh, named when the server check fails (optional)
    got["ssh_target"], got["ssh_key"] = cfg.setting("ollama.ssh_target"), cfg.setting("ollama.ssh_key")
    # when the server's own port is not reachable from this machine: the local port of the ssh tunnel the run opens
    # to ssh_target with ssh_key (optional; none means the server is called at ollama.host directly)
    got["tunnel_local_port"] = cfg.setting("ollama.tunnel_local_port")
    if got["tunnel_local_port"] is not None and not (got["ssh_target"] and got["ssh_key"]):
        raise JudgeError("cfg_setting ollama.tunnel_local_port needs ollama.ssh_target and ollama.ssh_key")
    # the names the model is given for the groups, where they differ from the names stored (optional)
    got["stored_as"] = cfg.setting("surface_judge.group_stored_as") or {}
    if not isinstance(got["stored_as"], dict) or any(k not in got["groups"] for k in got["stored_as"]):
        raise JudgeError("cfg_setting surface_judge.group_stored_as is a JSON object of {group named to the model: "
                         "group stored}, each key one of surface_judge.groups")
    if not isinstance(got["groups"], list) or not got["groups"]:
        raise JudgeError("cfg_setting surface_judge.groups is a JSON list of the groups")
    if "{surface}" not in got["word_prompt"]:
        raise JudgeError("cfg_setting surface_judge.word_prompt has no {surface} place")
    return got


def preflight(vals: dict) -> list[str]:
    """Before any surface is sent: the server answers within ollama.connect_timeout_seconds and has the configured
    model. Returns the names of the models on the server; raises JudgeError (nothing run) when it cannot."""
    url = vals["host"] + "/api/tags"
    way_in = (f" The configured way in over ssh: ssh -i {vals['ssh_key']} {vals['ssh_target']} "
              "(cfg_setting ollama.ssh_key, ollama.ssh_target)." if vals.get("ssh_target") and vals.get("ssh_key") else "")
    try:
        with urllib.request.urlopen(url, timeout=vals["connect_timeout_seconds"]) as r:
            models = [m.get("name") for m in json.loads(r.read()).get("models", [])]
    except Exception as exc:  # unreachable, refused, timed out, not an Ollama answer
        raise JudgeError(f"the Ollama server at {vals['host']} did not answer within "
                         f"{vals['connect_timeout_seconds']} s ({exc}); nothing was run. Check that the server is "
                         "on and that cfg_setting ollama.host is its address." + way_in) from None
    if vals["model"] not in models:
        raise JudgeError(f"the server at {vals['host']} answers but has no model {vals['model']!r} (cfg_setting "
                         f"ollama.model); it has: {', '.join(m for m in models if m) or 'none'}")
    return models


@contextlib.contextmanager
def server_route(vals: dict):
    """The values to call the server with. Without ollama.tunnel_local_port these are `vals` as they are. With it,
    an ssh tunnel is opened for the length of the block (unattended: ssh_key must have no passphrase, BatchMode),
    from 127.0.0.1:<tunnel_local_port> to the server's own 127.0.0.1:<port of ollama.host>, and `host` is the local
    end. The tunnel is closed on leaving the block. JudgeError, nothing run, when it cannot be opened."""
    port = vals.get("tunnel_local_port")
    if port is None:
        yield vals
        return
    remote_port = urllib.parse.urlparse(vals["host"]).port or 11434
    wait = vals["connect_timeout_seconds"]
    cmd = ["ssh", "-i", os.path.expanduser(vals["ssh_key"]), "-o", "BatchMode=yes", "-o", "ExitOnForwardFailure=yes",
           "-o", f"ConnectTimeout={int(wait)}", "-N", "-L", f"127.0.0.1:{int(port)}:127.0.0.1:{remote_port}",
           vals["ssh_target"]]
    proc = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    try:
        end = time.time() + wait + 5
        while time.time() < end and proc.poll() is None and not _port_open(int(port)):
            time.sleep(0.3)
        if proc.poll() is not None or not _port_open(int(port)):
            err = proc.stderr.read().strip() if proc.poll() is not None else "no answer on the local port"
            raise JudgeError(f"the ssh tunnel to {vals['ssh_target']} could not be opened with {vals['ssh_key']} "
                             f"({err[:300]}); nothing was run (cfg_setting ollama.ssh_target, ollama.ssh_key, "
                             "ollama.tunnel_local_port).")
        yield dict(vals, host=f"http://127.0.0.1:{int(port)}")
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()


def _port_open(port: int) -> bool:
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=1):
            return True
    except OSError:
        return False


def ask(vals: dict, prompt: str) -> tuple[dict, dict]:
    """One call to the server; the parsed JSON answer and the server's own counts."""
    body = {"model": vals["model"], "stream": False, "think": False, "format": "json",
            "keep_alive": vals["keep_alive"],
            "options": {"temperature": vals["temperature"], "num_ctx": vals["num_ctx"]},
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(vals["host"] + "/api/chat", json.dumps(body).encode(),
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=vals["timeout_seconds"]) as r:
        resp = json.loads(r.read())
    return json.loads(resp["message"]["content"]), {
        "out_tokens": resp.get("eval_count"), "prompt_tokens": resp.get("prompt_eval_count"),
        "tok_s": round(resp["eval_count"] / (resp["eval_duration"] / 1e9), 1) if resp.get("eval_duration") else None}


def check_word(ans: dict, groups: list[str]) -> list[str]:
    """Reasons the answer is not usable (empty list when it is)."""
    if not isinstance(ans, dict):
        return ["not an object"]
    if ans.get("group") not in groups:
        return [f"group {ans.get('group')!r}"]
    return []


def judge_word(vals: dict, surface: str) -> dict:
    """One surface string, one call (one retry). A failed word is recorded with group null and is tried again on
    the next run."""
    t0 = time.time()
    prompt = vals["word_prompt"].replace("{surface}", surface)
    errors, ans, meta = [], None, {}
    for attempt in (1, 2):
        try:
            got, meta = ask(vals, prompt)
        except Exception as exc:  # network, timeout or unparsable JSON
            errors.append(f"call failed: {exc}")
            continue
        bad = check_word(got, vals["groups"])
        if not bad:
            ans = got
            break
        errors.append(f"attempt {attempt}: " + "; ".join(bad))
    rec = {"surface": surface, "group": vals["stored_as"].get(ans["group"], ans["group"]) if ans else None,
           "reason": (ans.get("reason") or None) if ans else None,
           "judged_by": vals["model"] if ans else None, "errors": errors, "secs": round(time.time() - t0, 1)}
    rec.update({k: v for k, v in meta.items() if v is not None})
    return rec


def surface_list(conn) -> list[tuple[str, int]]:
    """The distinct surfaces of the live rows of surface_subgroup (stored lower-cased and trimmed), most rows
    first, with their row counts."""
    return [(r[0], r[1]) for r in conn.execute(
        "SELECT surface, COUNT(*) FROM surface_subgroup WHERE deleted=0 AND surface IS NOT NULL "
        "AND trim(surface)<>'' GROUP BY surface ORDER BY COUNT(*) DESC, surface")]


def read_batch(out: pathlib.Path) -> dict[str, dict]:
    """The last record of each surface in a batch file (empty when there is no file)."""
    got: dict[str, dict] = {}
    if out.exists():
        for line in out.read_text(encoding="utf-8").splitlines():
            if line:
                r = json.loads(line)
                got[r["surface"]] = r
    return got


def run_words(vals: dict, surfaces: list[str], out: pathlib.Path, limit: int | None = None,
              emit=None, deadline: float | None = None, should_stop=None, on_surface=None) -> dict:
    """Judge each surface once, appending one JSON line per word as it finishes (flushed). Resumable: a word
    already judged (group not null) is skipped, a word that failed is tried again. `limit` is the most words
    judged in this run. The server is checked first (preflight: JudgeError, nothing written, when it does not
    answer); the run halts after surface_judge.max_consecutive_failures surfaces in a row with no usable answer
    (the server went away part-way). Ctrl+C stops after the word in hand is written. Returns what this run did.
    When ollama.tunnel_local_port is set the ssh tunnel is open for the whole run (see server_route).
    For the cycle (run_cycle): `deadline` (epoch seconds) ends the run after the surface in hand (period_over),
    `should_stop()` true stops it the same way (stopped), and `on_surface(rec)` is called with each record written."""
    with server_route(vals) as route:
        return _run_words(route, surfaces, out, limit, emit, deadline, should_stop, on_surface)


def _run_words(vals: dict, surfaces: list[str], out: pathlib.Path, limit: int | None, emit, deadline, should_stop,
               on_surface) -> dict:
    preflight(vals)
    done = {s for s, r in read_batch(out).items() if r.get("group")}
    out.parent.mkdir(parents=True, exist_ok=True)
    did = failed = streak = 0
    stopped = halted = period_over = False
    try:
        for s in surfaces:
            if s in done:
                continue
            if limit is not None and did + failed >= limit:
                break
            if should_stop is not None and should_stop():
                stopped = True
                break
            if deadline is not None and time.time() >= deadline:
                period_over = True
                break
            rec = judge_word(vals, s)
            with out.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                f.flush()
            if rec["group"]:
                did += 1
                streak = 0
            else:
                failed += 1
                streak += 1
            if emit:
                emit(f"{s!r}: {rec['group']} {rec['secs']} s" + (f"  {rec['errors'][-1][:120]}" if not rec["group"] else ""))
            if on_surface is not None:
                on_surface(rec)
            if streak >= int(vals["max_consecutive_failures"]):
                halted = True
                break
    except KeyboardInterrupt:
        stopped = True
    return {"judged": did, "failed": failed, "stopped": stopped, "halted": halted, "period_over": period_over}


def stored_groups(vals: dict) -> list[str]:
    """The groups as stored in the batch file: the names given to the model, mapped where they differ."""
    return [vals["stored_as"].get(g, g) for g in vals["groups"]]


def status(conn, groups: list[str], out: pathlib.Path) -> dict:
    """How far a batch file has got against the list: judged per group (the stored names, see stored_groups),
    failed (tried, no answer) and left."""
    surfaces = [s for s, _ in surface_list(conn)]
    got = read_batch(out)
    per = {g: 0 for g in groups}
    failed = 0
    for s in surfaces:
        r = got.get(s)
        if r is None:
            continue
        if r.get("group") in per:
            per[r["group"]] += 1
        else:
            failed += 1
    judged = sum(per.values())
    return {"list": len(surfaces), "judged": judged, "per_group": per, "failed": failed,
            "left": len(surfaces) - judged - failed, "not_on_list": len(set(got) - set(surfaces))}


# ---- the cycle: the whole list, unattended, in work periods with a cool-down between ----------------------------

def cycle_settings(cfg: Cfg) -> dict:
    """The cycle's timings and limits (cfg_setting module surface_judge); stops when one is missing or not a number."""
    keys = ["surface_judge.cycle_work_minutes", "surface_judge.cycle_cooldown_minutes",
            "surface_judge.cycle_halt_wait_minutes", "surface_judge.cycle_max_halts_in_a_row"]
    got = {k.split(".", 1)[1]: cfg.setting(k) for k in keys}
    missing = [k for k, v in zip(keys, got.values()) if v is None]
    if missing:
        raise JudgeError(f"cfg_setting missing: {missing}")
    for k, v in got.items():
        if isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0 or (k != "cycle_cooldown_minutes" and v == 0):
            raise JudgeError(f"cfg_setting surface_judge.{k} is a number above 0 (the cool-down may be 0), not {v!r}")
    got["cycle_max_halts_in_a_row"] = int(got["cycle_max_halts_in_a_row"])
    return got


def progress_path(out: pathlib.Path) -> pathlib.Path:
    """The progress file of a batch: rewritten after every surface while a cycle runs."""
    return out.with_name(out.stem + ".progress.json")


def stop_path(out: pathlib.Path) -> pathlib.Path:
    """The stop flag of a batch: while it exists a cycle stops after the surface in hand."""
    return out.with_name(out.stem + ".stop")


def _iso(epoch: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch))


def read_progress(out: pathlib.Path) -> dict | None:
    p = progress_path(out)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):  # being replaced at this moment
        return None


def cycle_alive(prog: dict | None, stale_after: float) -> bool:
    """A cycle is running when its progress file says so and was updated within `stale_after` seconds."""
    if not prog or prog.get("state") not in ("running", "cooling", "waiting_after_halt", "starting"):
        return False
    return time.time() - prog.get("updated_epoch", 0) < stale_after


def _keep_awake(on: bool) -> None:
    """Windows: keep the machine from sleeping while a cycle runs (the display may still sleep)."""
    if os.name == "nt":
        import ctypes
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000001 if on else 0x80000000)


def run_cycle(vals: dict, cyc: dict, surfaces: list[str], out: pathlib.Path, emit=None, sleep=time.sleep) -> dict:
    """Judge the whole list, unattended. Work periods of cycle_work_minutes (the ssh tunnel is opened for a period
    and closed at its end), then cycle_cooldown_minutes of rest (the server's CPUs cool), until every surface has an
    answer. A period that ends with the server not answering (or surfaces that keep failing) is a halt: wait
    cycle_halt_wait_minutes and try again; cycle_max_halts_in_a_row periods in a row with no progress end the cycle
    (state halted). Progress is written to progress_path(out) after every surface and during every wait; a stop flag
    (stop_path(out)) or Ctrl+C ends it after the surface in hand (state stopped); run it again to resume. Refuses
    (JudgeError) when a cycle on this batch is already alive. Returns the last progress record."""
    sp, flag = progress_path(out), stop_path(out)
    stale_after = float(vals["timeout_seconds"]) + 120
    if cycle_alive(read_progress(out), stale_after):
        raise JudgeError(f"a cycle on batch {out.stem} is running (its progress was updated less than "
                         f"{int(stale_after)} s ago); stop it with -Action Stop, or wait")
    flag.unlink(missing_ok=True)
    surface_set = set(surfaces)
    known = {s: r.get("group") for s, r in read_batch(out).items() if s in surface_set}
    recent: list[float] = []
    prog = {"batch": out.stem, "started_at": _iso(time.time()), "periods": 0, "halts_in_a_row": 0,
            "last_problem": None, "period_started_at": None, "next_resume_at": None}
    counted = {"judged_this_cycle": 0}

    def judged_count() -> int:
        return sum(1 for g in known.values() if g)

    def refresh(state: str) -> None:
        per = {g: 0 for g in stored_groups(vals)}
        for g in known.values():
            if g in per:
                per[g] += 1
        judged = sum(per.values())
        failed = sum(1 for g in known.values() if not g)
        todo = len(surfaces) - judged
        mean = (sum(recent[-50:]) / len(recent[-50:])) if recent else None
        eta = None
        if mean is not None:
            active = todo * mean
            periods_left = -(-active // (cyc["cycle_work_minutes"] * 60)) if active else 0
            eta = _iso(time.time() + active + max(periods_left - 1, 0) * cyc["cycle_cooldown_minutes"] * 60)
        now = time.time()
        prog.update(state=state, updated_at=_iso(now), updated_epoch=now, list=len(surfaces), judged=judged,
                    per_group=per, failed=failed, left=todo, untried=todo - failed,
                    mean_secs_last_50=round(mean, 1) if mean is not None else None,
                    judged_this_cycle=counted["judged_this_cycle"], estimated_finish=eta,
                    estimate_note="work time left at the recent mean per surface plus the cool-downs between periods")
        tmp = sp.with_suffix(".tmp")
        try:
            tmp.write_text(json.dumps(prog, indent=1), encoding="utf-8")
            os.replace(tmp, sp)
        except OSError:  # a reader has the file this instant; the next write succeeds
            pass

    def on_surface(rec: dict) -> None:
        known[rec["surface"]] = rec["group"]
        if rec["group"]:
            recent.append(rec["secs"])
            counted["judged_this_cycle"] += 1
        refresh("running")

    def wait(minutes: float, state: str) -> bool:
        """Sleep in short slices, keeping the progress file alive; False when a stop was asked for."""
        end = time.time() + minutes * 60
        prog["next_resume_at"] = _iso(end)
        refresh(state)
        last = time.time()
        while time.time() < end:
            if flag.exists():
                return False
            sleep(min(5, max(end - time.time(), 0)))
            if time.time() - last >= 30:
                refresh(state)
                last = time.time()
        return True

    _keep_awake(True)
    state = "finished"
    try:
        refresh("starting")
        while True:
            if judged_count() >= len(surfaces):
                state = "finished"
                break
            judged_before = judged_count()
            prog["periods"] += 1
            prog["period_started_at"], prog["next_resume_at"] = _iso(time.time()), None
            refresh("running")
            problem = None
            try:
                res = run_words(vals, surfaces, out, None, emit, deadline=time.time() + cyc["cycle_work_minutes"] * 60,
                                should_stop=flag.exists, on_surface=on_surface)
            except JudgeError as exc:  # the tunnel or the server check: nothing was run in this period
                res, problem = None, str(exc)
            known.update({s: r.get("group") for s, r in read_batch(out).items() if s in surface_set})
            if flag.exists() or (res and res["stopped"]):
                state = "stopped"
                break
            if judged_count() >= len(surfaces):
                state = "finished"
                break
            if res and res["halted"]:
                problem = f"halted after {vals['max_consecutive_failures']} surfaces in a row with no usable answer"
            elif res and not res["period_over"]:
                problem = f"the pass ended with {len(surfaces) - judged_count()} surfaces that got no usable answer"
            if problem is None or judged_count() > judged_before:
                prog["halts_in_a_row"] = 0 if problem is None else 1
            else:
                prog["halts_in_a_row"] += 1
            prog["last_problem"] = problem or prog["last_problem"]
            if problem and prog["halts_in_a_row"] >= cyc["cycle_max_halts_in_a_row"]:
                state = "halted"
                break
            if emit:
                emit(("cooling down" if problem is None else "waiting after a halt") + f" ({problem or 'work period over'})")
            minutes = cyc["cycle_cooldown_minutes"] if problem is None else cyc["cycle_halt_wait_minutes"]
            if not wait(minutes, "cooling" if problem is None else "waiting_after_halt"):
                state = "stopped"
                break
    except KeyboardInterrupt:
        state = "stopped"
    finally:
        _keep_awake(False)
        prog["next_resume_at"] = None
        refresh(state)
    return prog
