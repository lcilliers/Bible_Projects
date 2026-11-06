"""ai handlers -- work package `ai-control` (#2361, stage 4), one step per Ai-Control.ps1 action.

Status shows the registers (models by role, prompts by key) and the calls made (by module, step, prompt, model and outcome); -Live also asks
the server which models it holds. Prompts lists every version of every prompt. PromptAdd makes a NEW version of a prompt (append-only: the text of a
version never changes), records the change note and, with -Activate, retires the version that was active. Replay sends a stored request again and
reports whether the answer is the same. Compare reports, per prompt version and model, how a step did: answered, refused, failed, seconds and
tokens. Everything is read from the tables; only PromptAdd and Replay write (cfg_ai_prompt through configmaint.apply_logged, and ai_call)."""
from __future__ import annotations

import datetime
import json

from ..lib import aiclient as ai
from ..lib import surfacejudge as sj
from .base import Ctx, Outcome, fail, ok
from .configmaint import apply_logged


def status(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    lines = ["models (cfg_ai_model): role, name, status"]
    for name, role, st in conn.execute("SELECT name, role, status FROM cfg_ai_model WHERE inactive=0 ORDER BY role, name"):
        lines.append(f"  {role:<11} {name}  {st}")
    lines.append("prompts (cfg_ai_prompt): key, active version, versions")
    for key, n, act in conn.execute("SELECT prompt_key, count(*), MAX(CASE WHEN status='active' THEN version END) FROM cfg_ai_prompt GROUP BY 1 ORDER BY 1"):
        lines.append(f"  {key:<28} active v{act if act else '-'} of {n}")
    lines.append("calls (ai_call): module, step, outcome, count")
    for m, s, o, n in conn.execute("SELECT module, step, outcome, count(*) FROM ai_call WHERE deleted=0 GROUP BY 1,2,3 ORDER BY 1,2,3"):
        lines.append(f"  {m}/{s}  {o}  {n}")
    if str(ctx.params.get("Live", "")).lower() in ("1", "true", "yes"):
        try:
            client = ai.AiClient(ctx.cfg, "ai", "status", ctx.run_id)
            with sj.server_route(client.vals_for_route()) as route:
                have = sj.preflight(dict(route, model=client.model("judge")[1]))
            reg = {r[0] for r in conn.execute("SELECT name FROM cfg_ai_model WHERE inactive=0")}
            lines.append("server: answers; models on it: " + ", ".join(sorted(m for m in have if m)))
            lines.append("registered but not on the server: " + (", ".join(sorted(reg - set(have))) or "none"))
        except (ai.AiError, sj.JudgeError) as exc:
            lines.append(f"server: {exc}")
    return ok("\n  ".join(lines))


def prompts(ctx: Ctx) -> Outcome:
    key = (ctx.params.get("Key") or "").strip()
    rows = ctx.cfg.conn.execute("SELECT prompt_key, version, status, role, hash, created_by, activated_at, change_note, length(text) FROM cfg_ai_prompt "
                                + ("WHERE prompt_key=? " if key else "") + "ORDER BY prompt_key, version", (key,) if key else ()).fetchall()
    if key and not rows:
        return fail("refused", f"no prompt with the key {key!r}")
    return ok("\n  ".join(f"{r[0]} v{r[1]} {r[2]} ({r[3]}, hash {r[4]}, {r[8]} characters, by {r[5]}): {r[7]}" for r in rows), versions=len(rows))


def prompt_add(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    key, text, note = ((ctx.params.get(k) or "").strip() for k in ("Key", "Text", "Note"))
    role = (ctx.params.get("Role") or "").strip()
    if not (key and text and note):
        return fail("refused", "-Key, -Text and -Note are required (the change note says why the new version exists)")
    prev = conn.execute("SELECT id, version, role, status, hash FROM cfg_ai_prompt WHERE prompt_key=? ORDER BY version DESC", (key,)).fetchall()
    if not prev and not role:
        return fail("refused", f"{key!r} is a new key: -Role is required (judge, embed, embed_fast, quick or reviewer)")
    if prev and role and role != prev[0][2]:
        return fail("refused", f"{key!r} is a prompt for role {prev[0][2]!r}, not {role!r}")
    role = role or prev[0][2]
    if not conn.execute("SELECT 1 FROM cfg_ai_model WHERE role=? AND inactive=0", (role,)).fetchone():
        return fail("refused", f"no model of role {role!r} in cfg_ai_model")
    h = ai.text_hash(text)
    if any(p[4] == h for p in prev):
        return fail("refused", f"this text is already a version of {key!r}")
    activate = str(ctx.params.get("Activate", "")).lower() in ("1", "true", "yes")
    purpose = conn.execute("SELECT purpose FROM cfg_ai_prompt WHERE prompt_key=? ORDER BY version DESC", (key,)).fetchone()
    ver = (prev[0][1] + 1) if prev else 1
    apply_logged(conn, ctx.run_id, "cfg_ai_prompt", "insert", {}, {
        "prompt_key": key, "version": ver, "text": text, "hash": h, "role": role, "purpose": purpose[0] if purpose else (ctx.params.get("Purpose") or note),
        "expected_output": None, "status": "draft", "parent_id": prev[0][0] if prev else None, "change_note": note, "created_by": "prompt step",
        "activated_at": None})
    if activate:
        for pid, v, _, st, _ in prev:
            if st == "active":
                apply_logged(conn, ctx.run_id, "cfg_ai_prompt", "update", {"id": pid}, {"status": "retired"})
        new_id = conn.execute("SELECT id FROM cfg_ai_prompt WHERE prompt_key=? AND version=?", (key, ver)).fetchone()[0]
        apply_logged(conn, ctx.run_id, "cfg_ai_prompt", "update", {"id": new_id}, {"status": "active", "activated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    conn.commit()
    return ok(f"{key} v{ver} added ({'active' if activate else 'draft: not used until activated'}; hash {h}): {note}", version=ver, active=int(activate))


def replay(ctx: Ctx) -> Outcome:
    cid = str(ctx.params.get("Call") or "").strip()
    if not cid.isdigit():
        return fail("refused", "-Call is required: the id of an ai_call row")
    try:
        client = ai.AiClient(ctx.cfg, "ai", "replay", ctx.run_id)
        ctx.cfg.conn.commit()
        with client.session(["judge"]):
            r = client.replay(int(cid))
    except (ai.AiError, sj.JudgeError) as exc:
        return fail("refused", str(exc))
    msg = f"call {cid}: the new answer is {'the same' if r['same'] else 'DIFFERENT'}"
    if not r["same"]:
        msg += f"\n  before {json.dumps(r['before'], ensure_ascii=False)[:200]}\n  after  {json.dumps(r['after'], ensure_ascii=False)[:200]}"
    return ok(msg, same=int(r["same"]))


def compare(ctx: Ctx) -> Outcome:
    step = (ctx.params.get("Step") or "").strip()
    if not step:
        return fail("refused", "-Step is required: an ai_call step such as base or group")
    rows = ctx.cfg.conn.execute(
        "SELECT p.prompt_key, p.version, m.name, c.outcome, count(*), round(avg(c.secs),1), round(avg(c.tokens_out),0) FROM ai_call c "
        "LEFT JOIN cfg_ai_prompt p ON p.id=c.prompt_id JOIN cfg_ai_model m ON m.id=c.model_id WHERE c.step=? AND c.deleted=0 GROUP BY 1,2,3,4 ORDER BY 1,2,3,4",
        (step,)).fetchall()
    if not rows:
        return fail("refused", f"no ai_call rows with step {step!r}")
    cases = ctx.cfg.conn.execute("SELECT standing, count(*) FROM surface_eval_case WHERE step=? AND deleted=0 GROUP BY 1", (step,)).fetchall()
    lines = [f"step {step}: prompt version, model, outcome, calls, average seconds, average tokens out"]
    lines += [f"  {r[0] or '(no prompt)'} v{r[1] or '-'}  {r[2]}  {r[3]}  {r[4]}  {r[5]}  {r[6]}" for r in rows]
    lines.append("cases for this step (surface_eval_case): " + (", ".join(f"{s} {n}" for s, n in cases) or "none")
                 + ("; any agreement with them is 'against provisional cases'" if cases else ""))
    return ok("\n  ".join(lines), rows=len(rows))
