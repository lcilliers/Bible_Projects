"""run.py — the dispatcher and run-state machine. Config-governed.

The step's handler, its scope, the sequence order — all read from the config store
(cfg_step). The handler returns a CONDITION; this dispatcher looks it up in cfg_on_fail
to get the PATH. The code decides nothing: config maps condition -> path.

    python -m iba.app.run <work_package> --step <id> --run-id <id> --param Name=Value

Exit codes let PowerShell branch: 0 ok/continue · 2 paused · 3 stop.
"""

from __future__ import annotations

import argparse
import datetime
import importlib
import json
import sys

from .lib.cfg import Cfg
from .lib.db import Db
from .lib.stepapi import Step
from .lib.words import normalise
from .lib import dbsnapshot
from .lib.escalation import word_source, raise_ as esc_raise
from .handlers.base import Ctx, Outcome

# path -> what the run does + the process exit code
PATH_EXIT = {"ok": 0, "report-continue": 0, "self-heal": 0, "pause-continue": 2, "report-stop": 3}


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resolve(handler: str):
    mod, fn = handler.split(":")
    return getattr(importlib.import_module(mod), fn)


def _grant(cfg: Cfg, table: str):
    """The dispatcher writes control tables under the 'run' write grant — config-governed."""
    if table not in cfg.may_write("run"):
        raise PermissionError(f"write-grant violation: 'run' may not write {table!r} (cfg_write_grant)")


# ── escalation-reset 2026-08-16 (iba-table-review-response-v1) — this dispatcher writes the
# `escalation` table directly (three sites below), NOT via lib/escalation.py's raise_()/
# raise_manual() -- so the column renames + new required columns from that reset had to be applied
# here too, or every crash/pause/report-stop write in the app would have broken outright.
def _source_for_step(step_id: str) -> str:
    """cfg_escalation.source_classification: a code-generated row's source is the generating
    module name -- the same convention the reset's migration backfilled from at_step."""
    return step_id.split(".", 1)[0] if "." in step_id else "code"


def _escalation_type_for(step_id: str, word: str) -> str:
    """Same classification the migration used to backfill 634 historical rows (escalation_reset_v1
    _retrofit_escalation) -- kept in sync deliberately, not reinvented here."""
    if step_id.startswith("configmaint.propose"):
        return "config"
    if step_id.endswith(".validate"):
        return "issue"
    if word:
        return "task"
    if step_id in ("candidate.curate", "candidate.load"):
        return "issue"
    return "issue"


def _snapshot(db: Db, cfg: Cfg, run_id: str, word: str, phase: str):
    """Record a row-count of every data table as the run's pre/post baseline. Written
    under the 'run' grant into validation_result; delta = post - pre = what the run did."""
    _grant(cfg, "validation_result")
    for t in cfg.tables():
        n = db.rows(f'SELECT COUNT(*) n FROM "{t}"')[0]["n"]
        db.write("validation_result", {
            "run_id": run_id, "word": word, "step": "snapshot",
            "check_name": f"{phase}:{t}", "result": "count", "detail": str(n),
            "ran_at": _now(), "deleted": 0})


def _scope(params: dict) -> str:
    """The run's scope value — a word, a book, or whatever the work package runs over."""
    return params.get("Word") or params.get("Book") or ""


def _ensure_run(db: Db, cfg: Cfg, package: str, params: dict, run_id: str):
    if db.get("run", run_id=run_id):
        return
    # a real DB file snapshot, once per NEW run (not on resume) — the pre-write rollback point
    # this app didn't have until a candidate.load bug found the gap the hard way, 2026-07-22.
    # IBA_NO_SNAPSHOT=1 skips it for a tight loop (e.g. a book-by-book sweep), same escape hatch
    # the legacy engine's own _apply_* snapshotting uses.
    dbsnapshot.snapshot(f"{package}-{run_id}")
    _grant(cfg, "run")
    db.write("run", {
        "run_id": run_id, "work_package": package, "params": json.dumps(params),
        "runs_over": _scope(params), "config_version": cfg.config_version(),
        "state": "running", "resume_point": "", "started_at": _now()})
    if _scope(params):                                   # skip for scope-less runs (e.g. seed refresh)
        _snapshot(db, cfg, run_id, _scope(params), "pre")


def run_step(package: str, step_id: str, params: dict, run_id: str) -> dict:
    cfg = Cfg()
    # Dispatch gate (escalation #334, 2026-07-29) — checked FIRST, before _ensure_run/any DB
    # write, so a refusal is clean and has no partial effect. Before this, `inactive` was
    # validator-only metadata: nothing stopped `Set-Candidates.ps1 -Book Obad` (a retired work
    # package) from actually running. Raised as PermissionError, uncaught, the same convention
    # every `_grant()`/`_may()` write-grant check in this app already uses for "the config
    # forbids this" — see BUILD.md sec37.
    if cfg.work_package_inactive(package):
        cfg.close()
        raise PermissionError(
            f"work package {package!r} is inactive (retired) or unknown — refusing to dispatch "
            f"step {step_id!r} (cfg_work_package.inactive)")
    if cfg.step_inactive(package, step_id):
        cfg.close()
        raise PermissionError(
            f"step {step_id!r} in work package {package!r} is inactive (retired) or unknown — "
            f"refusing to dispatch (cfg_step.inactive)")
    # Second gate, 2026-07-30 (the researcher's own operations/utility model — "routines not in
    # the table[s] need special permission to be used"): a step with no cfg_step.kind classification
    # is refused too, not silently run. "Special permission" = the same configmaint.propose
    # approval gate every other cfg_* change goes through — there is no separate bypass.
    if cfg.step_kind(package, step_id) is None:
        cfg.close()
        raise PermissionError(
            f"step {step_id!r} in work package {package!r} has no cfg_step.kind classification "
            f"(operations|utility) — refusing to dispatch. Classify it first: "
            f"Config-Maintenance.ps1 -Step Propose -Table cfg_step -Op update "
            f"-Where '{{\"work_package\":\"{package}\",\"step\":\"{step_id}\"}}' "
            f"-Set '{{\"kind\":\"operations\"}}' (or \"utility\") -Question \"...\"")
    # Third gate — `cfg_escalation.module_blocking` (escalation #646, 2026-08-17) — DISABLED
    # 2026-08-26, escalation #859, researcher's direct instruction, verbatim: "this module blocker
    # was added in an attempt to ensure that you do not run code with errors in the pipeline. but
    # because the errors was ignored and just bypast in the pass, there is now such an
    # accumulation of errors and bugs that this control is null not fulfilling its function. and
    # because you get some type of work around every time it is defunct." Concrete trigger: the
    # `source=?` clause below collapses configmaint.validate/.propose/.report to one string via
    # `_source_for_step()`'s first-dot split, so an advisory finding raised by .validate blocked
    # .propose outright. That bug is one symptom; the deeper problem is the accumulated backlog of
    # raised/re-assigned escalations means this gate now blocks routine dispatch often enough that
    # routing around it, not resolving the module, had become the normal response — the opposite
    # of what the gate exists to enforce. Commented out, not deleted or fixed in place, pending a
    # real redesign (#859) — do not re-enable this block without that redesign being resolved.
    # _module = _source_for_step(step_id)
    # _blocker = cfg.conn.execute(
    #     "SELECT id, short_description FROM escalation "
    #     "WHERE state IN ('raised','re-assigned') AND (at_step=? OR source=?) "
    #     "ORDER BY id LIMIT 1", (step_id, _module)).fetchone()
    # if _blocker:
    #     cfg.close()
    #     raise PermissionError(
    #         f"step {step_id!r} in work package {package!r} is blocked by unresolved escalation "
    #         f"#{_blocker['id']} ({_blocker['short_description'][:100]!r}) — resolve it "
    #         f"(Escalation.ps1 -Action AnswerRun) before dispatching (cfg_escalation.module_blocking)")
    db = Db(cfg)
    if "Word" in params:                                  # normalise once, at the boundary
        params["Word"] = normalise(params["Word"], cfg)
    step_cfg = cfg.step(package, step_id)                 # <- handler, scope from config
    handler = _resolve(step_cfg["handler"])
    _ensure_run(db, cfg, package, params, run_id)
    wrow = db.get("word_registry", word=params["Word"]) if "Word" in params else None

    ctx = Ctx(db=db, cfg=cfg, step=Step(cfg), run_id=run_id, word=_scope(params),
              word_id=wrow["id"] if wrow else None, params=params, step_id=step_id)

    # Researcher's standing rule, 2026-07-30: "if a validation runs for a module operation, or an
    # error takes place in a module operation, then it would escalate and record an escalation
    # report. It is that simple." Before this, an uncaught exception in a handler propagated as a
    # bare crash — no record, nothing in `escalation`, nothing an Escalation.ps1 -Action List would
    # ever show. Caught here, recorded, then RE-RAISED — this adds a permanent record, it does not
    # soften or hide the failure (the traceback still surfaces exactly as before).
    try:
        outcome: Outcome = handler(ctx)
    except Exception as exc:
        import traceback
        # 2026-08-06: a real bug, found live (passage.build crashed mid-write on a verse_passage
        # UNIQUE-constraint collision, ROOT-CAUSED and fixed in handlers/passage.py separately —
        # but investigating IT surfaced this second, independent, cross-cutting bug: db.close()
        # below unconditionally commits, so whatever the crashed handler partially wrote BEFORE
        # raising was landing in the live DB as committed, inconsistent state (a `passage` row
        # with a `verse_count` that didn't match its actual, incomplete `verse_passage` rows —
        # confirmed live, not hypothetical). The disaster-recovery guarantee documented for this
        # app ("a hard kill commits nothing, since nothing commits until the handler's own single
        # final commit()") is genuinely true for a hard kill (the process is just gone, this
        # except block never runs) — but was FALSE for an in-process exception, because this
        # except block's own recovery writes shared the crashed handler's own still-open
        # transaction. Roll back FIRST, discarding the crashed handler's partial work, before
        # writing the escalation/run-state record in a fresh transaction — the crash gets a
        # permanent, visible record either way (that part was already correct); it just no longer
        # drags the crash's own half-finished writes in with it.
        db.conn.rollback()
        # escalation #798/#799 SS4: "pure coding logic" (researcher, 2026-08-22) -- an uncaught
        # exception is always self_correctable at raise time; escalate_to_decision() converts it
        # if Claude's fix attempt reveals a genuine new decision is needed.
        try:
            esc_raise(db, run_id, _source_for_step(step_id), step_id,
                     f"{step_id} crashed: {exc}",
                     {"traceback": traceback.format_exc()},
                     "uncaught exception — not a routed fail()/escalate() Outcome",
                     etype="run_error", assigned_to="Claude",
                     resolution_kind="self_correctable")
        except Exception as record_exc:
            # SS7 fix: never let a secondary failure here replace the original crash's clean
            # traceback -- log it, don't let it propagate over the `raise` below.
            print(f"[WARN] failed to record crash escalation: {record_exc!r}", file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(),
                  outcome=f"crashed: {exc}")
        db.close()
        raise

    # resolve the CONDITION to a PATH via config (cfg_on_fail); 'ok' has no rule
    if outcome.condition == "ok":
        path, message = "ok", outcome.message
    else:
        rule = cfg.on_fail(step_id, outcome.condition)
        path = rule["path"] if rule else "report-stop"
        message = (rule["message"] + " — " if rule and rule["message"] else "") + outcome.message

    # escalation #798/#799 SS5: a decision_required escalation is always terminal -- reassign
    # `path` itself (not just internal behaviour) so the exit code this process returns (via
    # PATH_EXIT below) and anything else keyed on `path` correctly say "stopped", not "paused
    # resumably". Content is still built from the handler's own escalate() call, not this
    # generic report-stop reassignment -- see the branch below, which keeps using
    # outcome.escalation's question/preset/tried rather than falling into the plain report-stop
    # block's message+counts synthesis (meant for fail()-shaped outcomes, would lose detail here).
    if (path == "pause-continue" and outcome.escalation
            and outcome.escalation.get("resolution_kind", "decision_required") == "decision_required"):
        path = "report-stop"

    # act on the path
    if path == "pause-continue" and outcome.escalation:
        # Only reachable for self_correctable now -- decision_required was reassigned to
        # report-stop above, before this dispatch, precisely so it's handled by that branch
        # instead (same content-building, correct terminal exit code).
        e = outcome.escalation
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            source = word_source(ctx.word) if ctx.word else _source_for_step(step_id)
            try:
                esc_raise(db, run_id, source, step_id, e["question"], e["preset"], e["tried"],
                         etype=_escalation_type_for(step_id, ctx.word),
                         assigned_to="Researcher", resolution_kind="self_correctable")
            except Exception as record_exc:
                print(f"[WARN] failed to record self_correctable escalation: {record_exc!r}",
                     file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="paused", resume_point=step_id)
    elif path == "report-stop":
        # Added 2026-07-30 (the same standing rule): report-stop used to only flip run.state to
        # 'failed' — no escalation row, invisible to Escalation.ps1 -Action List. A hard error is
        # still an error; it now leaves the same permanent, visible record a pause-continue
        # finding does, even though (unlike pause-continue) answering it doesn't resume anything —
        # the run is already terminal. Same idempotency guard as the pause-continue block above.
        # escalation #798/#799 SS4/SS5: two ways to land here now --
        #   (a) a genuine fail()-shaped outcome (outcome.escalation is None) -- always
        #       self_correctable at raise time ("pure coding logic"); escalate_to_decision()
        #       converts it if a fix attempt reveals a real decision is needed.
        #   (b) a handler's own escalate() call whose resolution_kind was decision_required,
        #       reassigned here from pause-continue above -- keeps ITS OWN question/preset/tried
        #       (richer than the generic message+counts synthesis below) and decision_required.
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            if outcome.escalation:
                e = outcome.escalation
                question, preset, tried, kind, whom = (
                    e["question"], e["preset"], e["tried"], "decision_required", "Researcher")
            else:
                # Found 2026-07-30 (escalation #383, "it is unclear what the issue is"): `message`
                # here is often just a bare count (e.g. fail()'s own message arg, "1 coherence
                # error(s)") — the actual error text lives in `outcome.counts` (e.g.
                # counts["errors"]). Append it so the question is self-contained — full detail
                # also still in `preset` for programmatic use.
                detail = "; ".join(f"{k}: {v}" for k, v in outcome.counts.items() if v)
                question = f"{message} — {detail}" if detail else message
                preset = outcome.counts if outcome.counts else {}
                tried = ("hard error (report-stop) — recorded for visibility; answering this "
                        "does not resume the run, which is already terminal")
                kind, whom = "self_correctable", "Claude"
            source = word_source(ctx.word) if ctx.word else _source_for_step(step_id)
            try:
                esc_raise(db, run_id, source, step_id, question, preset, tried,
                         etype=_escalation_type_for(step_id, ctx.word), assigned_to=whom,
                         resolution_kind=kind)
            except Exception as record_exc:
                print(f"[WARN] failed to record report-stop escalation: {record_exc!r}",
                     file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(), outcome=message)
    else:
        db.update("run", {"run_id": run_id}, resume_point=step_id)
        # Close the run when it's actually finished. For a CHAINED work package (every step runs
        # under one run_id in one PS invocation — new-word, set-candidates, build-passages), that
        # means the LAST step in the cfg_step sequence. For a NON-chained package (each step
        # invoked independently, one per run_id — configuration-maintenance, reports, candidate-
        # quality, passage-quality, candidate-curation), a standalone step can never BE the last
        # step of a multi-step registration it only ever partially executes — it is done as soon
        # as IT resolves on a continue path. Found 2026-07-22: the old "last-in-sequence-only"
        # rule left 185 runs stuck 'paused'/'running' forever despite being fully resolved — see
        # cfg_work_package.chained / migration/add_work_package_chained_column.py.
        seq = [r["step"] for r in cfg.sequence(package)]
        if not cfg.is_chained(package) or (seq and step_id == seq[-1]):
            db.update("run", {"run_id": run_id}, state="done", ended_at=_now(),
                      outcome=message or "complete")
            if ctx.word:                                   # post-delta only for scoped runs
                _snapshot(db, cfg, run_id, ctx.word, "post")

    db.close()
    return {"step": step_id, "condition": outcome.condition, "path": path,
            "message": message, "counts": outcome.counts}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--step", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--param", action="append", default=[])
    a = ap.parse_args()
    params = dict(p.split("=", 1) for p in a.param)
    r = run_step(a.package, a.step, params, a.run_id)
    print(json.dumps(r))
    return PATH_EXIT.get(r["path"], 0)


if __name__ == "__main__":
    sys.exit(main())
