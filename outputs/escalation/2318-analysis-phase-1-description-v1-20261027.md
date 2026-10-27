# Analysis_phase_1: what the code does and which config it reads

> Escalation #2318 (rebuild reading steps 1 to 3). Version 1, 2026-10-27. Written in Developer Mode. Every code block below is quoted by script from the live files at git HEAD `c40d2878` (working tree at the time of writing); nothing is retyped. This describes the code **as it is today**, not as it should be. It is the first output of #2318 (B:105, B:44); no code has been changed.

## 1. The rule that applies to this file

Researcher, chat 2026-10-27 (verbatim): *"if you in future, when you are running Analysis_phase_1 do anything that is not in this description it will be regarded as a failure."* This file is therefore the whole of what a run of Analysis_phase_1 may do. What a run does that is not here is a failure; what this file says that the code does not do is a defect of this file, corrected by a new version, not worked around.

## 2. The name and its three steps

**Analysis_phase_1** is proposed by the researcher as the name of the three steps. They are run with `iba/app/ps/Reading.ps1`:

| Step | Reading.ps1 -Step | Gate afterwards | Written to the tables | Sections below |
|---|---|---|---|---|
| 1 | `Open` (0.C) | none | `reading`, `reading_verse`; files `<label>-gaps.json`, `<label>-collation.json` | 5 |
| 2 | `Gather` (0.GAP pre), then `Check` (pre gate) | pre: `open` -> `gathered` | `ib_observation`, `ib_node`, `ib_observation_change`, `reading_strand_hit`, thread items and responses, `reading` | 6 |
| 3 | `Observe`, then `Record`, then `Check` (observe gate) | observe: `gathered` -> `observed`; verses marked `analysed` | `Observe`: `reading` and `<label>-observe.json`; `Record`: `ib_observation`, `ib_node`, `ib_observation_change`, thread items; `Check`: `reading`, `verse_meta` | 7 and 8 |

**Question Q1 for the researcher.** I have put `Record` and the observe `Check` inside step 3, because you said step 3 ends in the rows of `ib_observation` and `ib_node` (chat 2026-10-27, recorded on #2316 v8). `Observe` itself writes only the observe file and two columns of the `reading` row. If step 3 is to be `Observe` alone, sections 7 and 8 move out. Please confirm.

**Question Q2.** The name Analysis_phase_1 exists nowhere in the code or config today. Registering it (a work package or a step grouping in `cfg_*`) is a design decision, not done here.

**Question Q3.** I have included the shared machinery (dispatcher, Cfg, Db, the Writer, the escalation update used for open items) as section 4, because a run cannot happen without it and your rule covers everything a run does. Please confirm that is the boundary you want.

## 3. How to read an element

Each element is one function (or one class, or a block of fixed values) that a run can execute. It has: where it is; its code, quoted whole; what it does; the config it reads; the data tables it reads and writes; and what it uses that is fixed in the code and not config. The **config** and **data** lines are found by a script scanning the quoted code for `required_setting`, `setting`, `enum`, `connection`, any `cfg_*` table name and any table in SQL; a function that reaches config by calling other functions is shown with the config of every function below it that has an element of its own (calls on objects such as `r.cluster(...)` or `w.insert(...)` are not followed by the script; those classes have their own elements). Where an element says *found in its code: none directly*, it reads no config itself.

## 4. Common to every step

Every step passes through the same chain: `Reading.ps1` -> `Notify.ps1` -> `run.py` -> the step's handler -> the Writer. Config governs it through `cfg_work_package`, `cfg_step` (handler, kind, inactive), `cfg_on_fail`, `cfg_write_grant`, `cfg_setting` and `cfg_enum`; appendix A lists the rows.

### 4.1 Elements C01 to C56



#### C01 — Reading.ps1 (the one door)

`iba/app/ps/Reading.ps1:1-85`

```powershell
<#
.SYNOPSIS
    The reading process (escalations #2228, #2273): a reading of one scope with its objective, on the
    phases of the analytic process, through four gates -- pre, observe, claims, narrate -- then published.
    Every step dispatches through run.py, work package reading.

.DESCRIPTION
    Claude reads and writes in the session; the app resolves the scope, gives everything already known,
    writes the findings as rows (one observation per finding, applied by its nodes) and checks each gate
    from the tables. One reading per scope:

      Open     -Label anger-bosom -Escalation 2172 -Home M02 -Objective "..." <scope selectors, as
               Verse-Scope.ps1>   0.C: the scope resolved (above 2,500 verses held until -Reviewed), its
               verses kept, the scope collated, and the pre-gap JSON written, one section per gap type of
               phase pre -> outputs/reading/<label>/<label>-gaps.json (and -collation.json)
      Gather   -Label <label> [-File <pre-gap JSON>]   0.GAP pre written: each item's record ({"finding"},
               {"table", "id"}, {"reason"}, a face, a response), new open items; ids written back
      Observe  -Label <label>    the observe JSON built from the tables: per verse its passage, every finding
               applied to it, the words in focus (qualifiers included), the claims, the prompts by kind
      Record   -Label <label> [-File <observe JSON>]   the findings written (a live description gains
               nodes), withdrawals with their reasons, each word's open item or reason
      Check    -Label <label>    the gate the reading is at: pre (open -> gathered), observe (gathered ->
               observed: every word in focus has a node of this reading, an open item or a reason; the
               verses are marked analysed), claims (observed -> synergised: every node disposed, every
               claim resting on a finding, every matched open item settled; the narrate JSON built), narrate
               (synergised -> narrated: every claim told or held, every cited verse recorded)
      Synergy  -Label <label>    the synergy JSON, built from the tables (never memory)
      Apply    -Label <label> [-File <synergy JSON>]   claims, each node's disposition, open items settled
      Narrate  -Label <label> [-File <narrate JSON>]   tellings, holds, blocks rewritten; nodes told
      Publish  -Label <label>    the touched chapters published, copied to the learning4comfort inbox
               and checked byte-identical
      Account  -Label <label>    the reading from the tables: its state and the gaps at its gate

    The JSON shapes are in lib/reading.py, lib/observationrecord.py and each file's "how". Write steps
    (all but Account) need -By Claude|Researcher. The escalation that anchors a reading cannot reach
    completed or closed while the reading is not published.

.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Open -Label anger-bosom -Escalation 2172 -Home M02 -Objective "what the bosom shows of anger" -Strong H2436 -By Claude
.EXAMPLE
    iba\app\ps\Reading.ps1 -Step Record -Label anger-bosom -By Claude
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('Open', 'Gather', 'Observe', 'Record', 'Check', 'Synergy', 'Apply', 'Narrate', 'Publish', 'Account')]
    [string] $Step,
    [Parameter(Mandatory = $true)] [string] $Label,
    [ValidateSet('Claude', 'Researcher')] [string] $By,
    # -Home is an alias of HomeCluster: a variable named Home would be PowerShell's read-only HOME (#2248)
    [string] $Escalation, [Alias('Home')] [string] $HomeCluster, [string] $Objective, [string] $Note, [string] $File,
    [string] $Cluster, [string] $Subgroup, [string] $Strand, [string] $Word, [string] $Strong,
    [string] $Verse, [string] $Chapter, [string] $Section, [string] $Claim, [string] $Observation,
    [string] $Item, [string] $Thread, [string] $OnlyStrong, [string] $Reviewed,
    [switch] $Trace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
if ($Trace) { $env:IBA_TRACE = '1' }

$RepoRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
Set-Location $RepoRoot
. $PSScriptRoot\_lib\Notify.ps1

$stepId = "reading.$($Step.ToLower())"
$runId = "RUN-$(Get-Date -Format 'yyyyMMdd_HHmmss_fff')-READING"

$paramArgs = @()
foreach ($name in @('Label', 'By', 'Escalation', 'HomeCluster', 'Objective', 'Note', 'File', 'Cluster', 'Subgroup', 'Strand', 'Word',
                    'Strong', 'Verse', 'Chapter', 'Section', 'Claim', 'Observation', 'Item', 'Thread', 'OnlyStrong',
                    'Reviewed')) {
    $value = Get-Variable -Name $name -ValueOnly
    $key = if ($name -eq 'HomeCluster') { 'Home' } else { $name }   # run.py's parameter stays Home
    if ($PSBoundParameters.ContainsKey($name)) { $paramArgs += @('--param', "$key=$value") }
}

Write-IbaRunHeader -WorkPackage 'reading' -Step $stepId -RunId $runId
$json = python -m iba.app.run reading --step $stepId --run-id $runId @paramArgs
$code = $LASTEXITCODE
$res = $json | ConvertFrom-Json
Write-IbaStepResult -Step $stepId -Path $res.path -Message $res.message -Code $code
exit $code
```

**What it does.** Takes -Step, -Label and every selector. Sets PYTHONUTF8=1 (and IBA_TRACE=1 with -Trace, which makes Cfg print every config read to stderr), moves to the repository root, loads Notify.ps1, and forms the step id `reading.<step>` and the run id `RUN-<yyyyMMdd_HHmmss_fff>-READING`. Every parameter you bound is passed on as `--param Name=Value` (-Home is passed as `Home`). It prints the run header, runs `python -m iba.app.run reading --step <id> --run-id <id> --param ...`, reads the single JSON line python prints, prints the result line and exits with python's exit code (0 ok or report-continue, 1 error, 2 pause, 3 stop). The script itself reads no config; the wording it prints comes from Notify.ps1.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The list of parameter names forwarded, the step names allowed (ValidateSet), the run-id format, `-Home` renamed `Home`.

#### C02 — Notify.ps1: header and result wording

`iba/app/ps/_lib/Notify.ps1:24-39`

```powershell
function _IbaLoadNotifications {
    if ($null -ne $script:_ibaNotif) { return }
    $json = python -c @'
import json
from iba.app.lib.cfg import Cfg
c = Cfg()
keys = ["notification.not_initialised", "notification.header_work_package",
        "notification.header_step", "notification.header_run_id",
        "notification.header_runs_over", "notification.step_result_line",
        "notification.paused_banner_guided", "notification.paused_banner_passthrough",
        "notification.stopped_banner"]
print(json.dumps({k: c.setting(k) for k in keys}))
c.close()
'@
    $script:_ibaNotif = $json | ConvertFrom-Json
}
```

**What it does.** Fetched once per process through one `python -c` call: opens Cfg and reads nine `notification.*` settings with `Cfg.setting` (no default: a missing row returns nothing).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The list of nine keys.

#### C03 — Notify.ps1: template filler

`iba/app/ps/_lib/Notify.ps1:56-60`

```powershell
function _IbaFormat([string] $Template, [hashtable] $Vars) {
    $out = $Template
    foreach ($k in $Vars.Keys) { $out = $out.Replace("{$k}", [string]$Vars[$k]) }
    return $out
}
```

**What it does.** Replaces `{name}` in a template by a value.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C04 — Notify.ps1: run header

`iba/app/ps/_lib/Notify.ps1:75-93`

```powershell
function Write-IbaRunHeader {
    param(
        [Parameter(Mandatory)] [string] $WorkPackage,
        [string] $Step,
        [Parameter(Mandatory)] [string] $RunId,
        [string] $RunsOver
    )
    _IbaLoadNotifications
    Write-Host ""
    Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_work_package' @{ work_package = $WorkPackage })
    if ($Step) {
        Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_step' @{ step = $Step })
    }
    Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_run_id' @{ run_id = $RunId })
    if ($RunsOver) {
        Write-Host (_IbaFormat $script:_ibaNotif.'notification.header_runs_over' @{ runs_over = $RunsOver })
    }
    Write-Host ""
}
```

**What it does.** Prints the work package, step and run id lines from the `notification.header_*` templates. Reading.ps1 passes no RunsOver, so the `header_runs_over` line is not printed.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C05 — Notify.ps1: result line

`iba/app/ps/_lib/Notify.ps1:95-111`

```powershell
function Write-IbaStepResult {
    param(
        [Parameter(Mandatory)] [string] $Step,
        [string] $Path,
        [string] $Message,
        [Parameter(Mandatory)] [int] $Code
    )
    _IbaLoadNotifications
    # 1 = 'DarkRed' added 2026-08-30 (escalation #1058) alongside run.py's new PATH_EXIT["error"]
    # -- a dispatch-level crash (retired work package/step, write-grant violation, etc.) now
    # returns a clean JSON result instead of a bare traceback, but this map didn't have an entry
    # for its exit code either, so `-ForegroundColor $null` crashed here instead -- same class of
    # bug, one layer in. The ?? fallback guards any FUTURE new code the same way, rather than
    # waiting to find the next one live.
    $colour = (@{ 0 = 'Green'; 1 = 'DarkRed'; 2 = 'Yellow'; 3 = 'Red' }[$Code]) ?? 'White'
    Write-Host ($script:_ibaNotif.'notification.step_result_line' -f $Step, $Path, $Message) -ForegroundColor $colour
}
```

**What it does.** Prints the `notification.step_result_line` template with step, path and message, coloured by the exit code.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The colour map by exit code (0 Green, 1 DarkRed, 2 Yellow, 3 Red, else White).

#### C06 — run.py: path-to-exit-code map and entry

`iba/app/run.py:29-30`

```python
PATH_EXIT = {"ok": 0, "report-continue": 0, "self-heal": 0, "pause-continue": 2, "report-stop": 3,
            "error": 1}
```

**What it does.** Maps the path chosen for a run to the process exit code Reading.ps1 returns.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The map itself.

#### C07 — run.py: main

`iba/app/run.py:258-277`

```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--step", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--param", action="append", default=[])
    a = ap.parse_args()
    params = dict(p.split("=", 1) for p in a.param)
    try:
        r = run_step(a.package, a.step, params, a.run_id)
    except Exception as exc:
        # The CLI boundary always prints one JSON line with a `path` key, which every iba/app/ps/*.ps1
        # wrapper reads: an uncaught exception from run_step() (dispatch gates, write-grant checks) is
        # turned into an "error" result here (#1058). Direct Python callers of run_step() still get the
        # raw exception.
        print(json.dumps({"step": a.step, "condition": "error", "path": "error",
                          "message": f"{type(exc).__name__}: {exc}", "counts": {}}))
        return PATH_EXIT["error"]
    print(json.dumps(r))
    return PATH_EXIT.get(r["path"], 0)
```

**What it does.** Reads the package, `--step`, `--run-id` and `--param Name=Value` pairs, calls `run_step`, and prints one JSON line with the result. Any uncaught exception becomes a JSON line with path `error` and exit code 1.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** C19 (setting retention.snapshot_keep_count)

**Data (found in its code).** none directly.

#### C08 — run.py: run_step (the dispatcher)

`iba/app/run.py:101-255`

```python
def run_step(package: str, step_id: str, params: dict, run_id: str) -> dict:
    cfg = Cfg()
    # Dispatch gate (#334), checked first, before any DB write: an inactive work package or step is
    # refused with PermissionError (uncaught, the convention of every _grant()/_may() check).
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
    # Second gate: a step with no cfg_step.kind is refused; classifying it goes through the
    # configmaint.propose approval gate.
    if cfg.step_kind(package, step_id) is None:
        cfg.close()
        raise PermissionError(
            f"step {step_id!r} in work package {package!r} has no cfg_step.kind classification "
            f"(operations|utility) — refusing to dispatch. Classify it first: "
            f"Config-Maintenance.ps1 -Step Propose -Table cfg_step -Op update "
            f"-Where '{{\"work_package\":\"{package}\",\"step\":\"{step_id}\"}}' "
            f"-Set '{{\"kind\":\"operations\"}}' (or \"utility\") -Question \"...\"")
    # Third gate, cfg_escalation.module_blocking: DISABLED (#859) pending a redesign; do not re-enable
    # without it.
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

    # an uncaught handler exception is recorded as an escalation, then re-raised: the traceback
    # still surfaces as before
    try:
        outcome: Outcome = handler(ctx)
    except Exception as exc:
        import traceback
        # roll back first: db.close() commits, so the crashed handler's partial writes must be discarded
        # before the escalation/run-state record is written in a fresh transaction
        db.conn.rollback()
        # an uncaught exception is self_correctable at raise time; escalate_to_decision() converts it
        # if the fix needs a new decision
        try:
            esc_raise(db, run_id, _source_for_step(step_id), step_id,
                     f"{step_id} crashed: {exc}",
                     {"traceback": traceback.format_exc()},
                     "uncaught exception — not a routed fail()/escalate() Outcome",
                     etype="run_error", assigned_to="Claude",
                     resolution_kind="self_correctable")
        except Exception as record_exc:
            # a secondary failure here is logged, never allowed to replace the original traceback
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

    # a decision_required escalation is always terminal: `path` becomes report-stop, so the exit code
    # says "stopped"; its content still comes from the handler's own escalate() call (below)
    if (path == "pause-continue" and outcome.escalation
            and outcome.escalation.get("resolution_kind", "decision_required") == "decision_required"):
        path = "report-stop"

    # act on the path
    if path == "pause-continue" and outcome.escalation:
        # only self_correctable reaches here (decision_required was moved to report-stop above)
        e = outcome.escalation
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            source = word_source(ctx.word) if ctx.word else _source_for_step(step_id)
            try:
                esc_raise(db, run_id, source, step_id, e["question"], e["preset"], e["tried"],
                         etype=_escalation_type_for(step_id, ctx.word),
                         assigned_to="Researcher", resolution_kind="self_correctable",
                         title=e.get("title"))
            except Exception as record_exc:
                print(f"[WARN] failed to record self_correctable escalation: {record_exc!r}",
                     file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="paused", resume_point=step_id)
    elif path == "report-stop":
        # report-stop leaves a visible escalation, like pause-continue (the run is already terminal).
        # Two ways to land here:
        #   (a) a fail()-shaped outcome (outcome.escalation is None): self_correctable at raise time.
        #   (b) a handler's escalate() with resolution_kind decision_required: keeps its own
        #       question/preset/tried and decision_required.
        already = db.rows("SELECT id FROM escalation WHERE run_id=? AND at_step=? "
                          "AND state='raised'", (run_id, step_id))
        if not already:
            if outcome.escalation:
                e = outcome.escalation
                question, preset, tried, kind, whom = (
                    e["question"], e["preset"], e["tried"], "decision_required", "Researcher")
                needs_followup = e.get("needs_followup", False)
                title = e.get("title")
            else:
                # `message` is often only a count; append the error text from `outcome.counts` so the question is
                # self-contained (full detail also in `preset`)
                detail = "; ".join(f"{k}: {v}" for k, v in outcome.counts.items() if v)
                question = f"{message} — {detail}" if detail else message
                preset = outcome.counts if outcome.counts else {}
                tried = ("hard error (report-stop) — recorded for visibility; answering this "
                        "does not resume the run, which is already terminal")
                kind, whom = "self_correctable", "Claude"
                needs_followup = False
                title = None
            source = word_source(ctx.word) if ctx.word else _source_for_step(step_id)
            try:
                esc_raise(db, run_id, source, step_id, question, preset, tried,
                         etype=_escalation_type_for(step_id, ctx.word), assigned_to=whom,
                         resolution_kind=kind, needs_followup=needs_followup, title=title)
            except Exception as record_exc:
                print(f"[WARN] failed to record report-stop escalation: {record_exc!r}",
                     file=sys.stderr)
        db.update("run", {"run_id": run_id}, state="failed", ended_at=_now(), outcome=message)
    else:
        db.update("run", {"run_id": run_id}, resume_point=step_id)
        # Close the run when it is finished: for a CHAINED work package (every step under one run_id),
        # at the last step in the cfg_step sequence; for a non-chained package (one step per run_id), as
        # soon as the step resolves on a continue path (cfg_work_package.chained).
        seq = [r["step"] for r in cfg.sequence(package)]
        if not cfg.is_chained(package) or (seq and step_id == seq[-1]):
            db.update("run", {"run_id": run_id}, state="done", ended_at=_now(),
                      outcome=message or "complete")
            if ctx.word:                                   # post-delta only for scoped runs
                _snapshot(db, cfg, run_id, ctx.word, "post")

    db.close()
    return {"step": step_id, "condition": outcome.condition, "path": path,
            "message": message, "counts": outcome.counts}
```

**What it does.** In order: (1) opens Cfg; (2) refuses an inactive or unknown work package (`cfg_work_package.inactive`) or step (`cfg_step.inactive`), and a step with no `cfg_step.kind`; (3) opens Db; (4) if a `Word` parameter was given, normalises it (`words.normalise`, C16) and looks it up in `word_registry`; (5) reads the step's row (`cfg_step`) and imports its handler (`iba.app.handlers.reading:<name>`); (6) `_ensure_run` for a new run id (snapshot, run row); (7) builds the context (Ctx) with a STEP object (`stepapi.Step`, C12); (8) calls the handler; (9) if the handler returned `ok`, path `ok`; otherwise looks the condition up in `cfg_on_fail` (reading steps have a `refused` row = `report-continue`, exit 0); (10) `report-continue` (and `ok`) update the run row (`resume_point`), and because `cfg_work_package.chained` is 0 for reading, the run is closed `done` at once, and if a `Word` was given the post row-count snapshot is written; (11) closes Db (commits). If the handler raises, the dispatcher rolls back, raises an escalation of type run_error assigned to Claude, marks the run failed and re-raises. The `report-stop` and `pause-continue` branches exist but no reading handler returns a condition that reaches them.

**Config read by this element (found in its code).** config tables named: `cfg_escalation`, `cfg_on_fail`, `cfg_step`, `cfg_work_package`

**Config read below it, through the functions it calls (all levels; each has its own element).** C19 (setting retention.snapshot_keep_count)

**Data (found in its code).** reads data table(s) `escalation`, `word_registry`; writes `run`

**Fixed in the code, not config.** The exit-code map, the gate order, the crash handling, `report-stop` as the default when a condition has no `cfg_on_fail` row.

#### C09 — run.py: run row and snapshot

`iba/app/run.py:86-98`

```python
def _ensure_run(db: Db, cfg: Cfg, package: str, params: dict, run_id: str):
    if db.get("run", run_id=run_id):
        return
    # a DB snapshot once per NEW run (not on resume): the pre-write rollback point.
    # IBA_NO_SNAPSHOT=1 skips it for a tight loop (e.g. a book-by-book sweep).
    dbsnapshot.snapshot(f"{package}-{run_id}")
    _grant(cfg, "run")
    db.write("run", {
        "run_id": run_id, "work_package": package, "params": json.dumps(params),
        "runs_over": _scope(params), "config_version": cfg.config_version(),
        "state": "running", "resume_point": "", "started_at": _now()})
    if _scope(params):                                   # skip for scope-less runs (e.g. seed refresh)
        _snapshot(db, cfg, run_id, _scope(params), "pre")
```

**What it does.** Skipped when the run id already has a row. For a new run id: takes a database snapshot (C10), checks the `run` write grant, writes the `run` row (work package, params, `config_version`, state running), and, only if the run has a scope (a `Word` or `Book` parameter), writes the pre row-count snapshot.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** C19 (setting retention.snapshot_keep_count)

**Data (found in its code).** reads data table(s) `run`; writes `run`

#### C10 — run.py: write-grant check

`iba/app/run.py:42-45`

```python
def _grant(cfg: Cfg, table: str):
    """The dispatcher writes control tables under the 'run' write grant — config-governed."""
    if table not in cfg.may_write("run"):
        raise PermissionError(f"write-grant violation: 'run' may not write {table!r} (cfg_write_grant)")
```

**What it does.** Refuses a write to a table the writer `run` has no `cfg_write_grant` row for.

**Config read by this element (found in its code).** config tables named: `cfg_write_grant`

**Data (found in its code).** none directly.

#### C12 — stepapi.Step: constructed for every run

`iba/app/lib/stepapi.py:38-50`

```python
    def __init__(self, cfg: Cfg):
        self.cfg = cfg
        self.base = cfg.connection("base_url").rstrip("/")
        self.version = cfg.connection("version")
        self.timeout = int(cfg.connection("timeout_seconds"))
        self.cap = int(cfg.setting("step.cap", 60))
        self.walk_start = cfg.required_setting("step.walk_start")
        self.walk_end = cfg.required_setting("step.walk_end")
        self.walk_max = int(cfg.setting("step.walk_max_iter", 400))
        self.particle_re = re.compile(cfg.setting("discovery.particle_pattern", r"^[HG]9\d{3}$"))
        # book order and the span-HTML pattern now come from config, not the code
        self.book_idx = cfg.book_order()
        self.span_re = re.compile(cfg.setting("step.span_html"))
```

**What it does.** Reads the STEP connection (`base_url`, `version`, `timeout_seconds`) and settings `step.cap`, `step.walk_start`, `step.walk_end`, `step.walk_max_iter`, `discovery.particle_pattern`, `step.span_html`, and the book order. It makes no network call here; the reading steps do not call STEP afterwards.

**Config read by this element (found in its code).** setting: `discovery.particle_pattern`, `step.cap`, `step.span_html`, `step.walk_end`, `step.walk_max_iter`, `step.walk_start`; connection: `base_url`, `timeout_seconds`, `version`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The defaults 60, 400 and `^[HG]9\d{3}$` when a setting is absent.

#### C13 — run.py: row-count snapshot (only when a Word or Book scope is given)

`iba/app/run.py:69-78`

```python
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
```

**What it does.** Writes, for every table `cfg.tables()` lists, a `validation_result` row with its current row count (phase pre or post). Reached only when `_scope(params)` is not empty; Reading.ps1 can pass `-Word`, so Open or any step given `-Word` takes this path. Otherwise it is skipped.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** writes `validation_result`

#### C14 — run.py: scope of a run

`iba/app/run.py:81-83`

```python
def _scope(params: dict) -> str:
    """The run's scope value — a word, a book, or whatever the work package runs over."""
    return params.get("Word") or params.get("Book") or ""
```

**What it does.** The `Word` parameter, else the `Book` parameter, else empty.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C15 — run.py: handler import

`iba/app/run.py:37-39`

```python
def _resolve(handler: str):
    mod, fn = handler.split(":")
    return getattr(importlib.import_module(mod), fn)
```

**What it does.** Splits `module:function` from `cfg_step.handler` and imports it.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C16 — words.normalise (only when -Word is given)

`iba/app/lib/words.py:34-43`

```python
def normalise(word: str, cfg: Cfg) -> str:
    strip = cfg.setting("registry.strip_ends_pattern", r"[^A-Za-z]")
    w = re.sub(r"\s+", " ", word or "").strip()
    w = re.sub(rf"^(?:{strip})+", "", w)
    m = re.search(rf"(?:{strip})+$", w)
    if m:
        candidate = w[:m.start()]
        if not _closes_open_bracket(candidate):
            w = candidate
    return w
```

**What it does.** Trims and cleans the word; reads `registry.strip_ends_pattern` with `Cfg.setting` (default `[^A-Za-z]`).

**Config read by this element (found in its code).** setting: `registry.strip_ends_pattern`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The default pattern.

#### C17 — dbsnapshot: snapshot, copy and prune

`iba/app/lib/dbsnapshot.py:53-65`

```python
def snapshot(reason: str = "run", keep: int | None = None) -> Path | None:
    """Copy iba.db to a timestamped snapshot, then prune. Returns the new path, or None if
    IBA_NO_SNAPSHOT=1 (the loop escape hatch) or the DB doesn't exist yet."""
    import os
    if os.environ.get("IBA_NO_SNAPSHOT") == "1":
        return None
    if not DB_PATH.exists():
        return None

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = copy_db(SNAPSHOT_DIR / f"iba-{ts}-{_slug(reason)}.db")
    prune(keep)
    return dest
```

**What it does.** Skipped when the environment variable IBA_NO_SNAPSHOT is 1. Otherwise copies iba.db with the SQLite backup API to `iba/app/db/snapshots/iba-<UTC timestamp>-<reason>.db` (reason `reading-<run id>`) and prunes (C18). One snapshot per NEW run id, so every Reading.ps1 call takes one.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** C19 (setting retention.snapshot_keep_count)

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The snapshot folder and file-name shape; the environment variable.

#### C18 — dbsnapshot: copy_db

`iba/app/lib/dbsnapshot.py:37-50`

```python
def copy_db(dest: Path | str, src: Path | str = DB_PATH) -> Path:
    """Copy `src` to `dest` with the SQLite backup API; returns `dest`. Refuses to overwrite."""
    dest = Path(dest)
    if dest.exists():
        raise FileExistsError(f"{dest} already exists")
    dest.parent.mkdir(parents=True, exist_ok=True)
    source = sqlite3.connect(f"file:{Path(src).as_posix()}?mode=ro", uri=True, timeout=30.0)
    target = sqlite3.connect(dest)
    try:
        source.backup(target)
    finally:
        target.close()
        source.close()
    return dest
```

**What it does.** Consistent copy by the SQLite online backup API; refuses to overwrite.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C19 — dbsnapshot: prune

`iba/app/lib/dbsnapshot.py:68-87`

```python
def prune(keep: int | None = None) -> int:
    """Delete the oldest snapshots beyond `keep` (config-driven default if not passed
    explicitly — read lazily here, not at import time, so this module has no hard Cfg
    dependency for callers that just want a quick snapshot)."""
    if keep is None:
        try:
            from .cfg import Cfg
            c = Cfg()
            keep = int(c.setting("retention.snapshot_keep_count", 20))
            c.close()
        except Exception:
            keep = 20
    if not SNAPSHOT_DIR.exists():
        return 0
    files = sorted(SNAPSHOT_DIR.glob("iba-*.db"), key=lambda p: p.stat().st_mtime, reverse=True)
    removed = 0
    for f in files[keep:]:
        f.unlink()
        removed += 1
    return removed
```

**What it does.** Keeps the newest `retention.snapshot_keep_count` snapshots (read with `Cfg.setting`) and deletes the older `iba-*.db` files in the folder, including named pre-run snapshots (see escalation #2301).

**Config read by this element (found in its code).** setting: `retention.snapshot_keep_count`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** Default 20 if the setting is absent or Cfg fails.

#### C20 — dbsnapshot: file-name slug

`iba/app/lib/dbsnapshot.py:32-34`

```python
def _slug(reason: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", reason or "run").strip("-").lower()
    return s[:40] or "run"
```

**What it does.** Lowercases the reason and keeps 40 characters.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The 40-character limit.

#### C21 — Cfg: opening the config store

`iba/app/lib/cfg.py:44-53`

```python
    def __init__(self, db_path: pathlib.Path = DB_PATH):
        self.conn = sqlite3.connect(db_path, timeout=30.0)
        self.conn.row_factory = sqlite3.Row
        # WAL + a real busy-timeout: readers don't block writers, and brief lock
        # contention waits instead of failing instantly with 'database is locked'.
        try:
            self.conn.execute("PRAGMA journal_mode=WAL")
            self.conn.execute("PRAGMA busy_timeout=30000")
        except sqlite3.Error:
            pass
```

**What it does.** Opens iba.db (WAL mode, 30-second busy timeout). Every config read in this description goes through this object.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The timeout.

#### C22 — Cfg: the readers the steps use (1/3)

`iba/app/lib/cfg.py:56-62`

```python
    def setting(self, key: str, default=None):
        # inactive rows are never read (#334)
        r = self.conn.execute(
            "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
        val = json.loads(r["value"]) if r else default
        _trace(f"setting {key}", val)
        return val
```

**What it does.** Reads `cfg_setting` (active rows only); returns the default when the key is missing.

**Config read by this element (found in its code).** config tables named: `cfg_setting`

**Data (found in its code).** none directly.

#### C23 — Cfg: the readers the steps use (2/3)

`iba/app/lib/cfg.py:64-76`

```python
    def required_setting(self, key: str):
        """Same lookup as `.setting()`, but with NO default parameter: raises if the key is missing or
        inactive. Used for report/output paths and any value that must have a single live config source,
        so a missing, renamed or deactivated setting fails loudly instead of falling back to a literal."""
        r = self.conn.execute(
            "SELECT value FROM cfg_setting WHERE key=? AND inactive=0", (key,)).fetchone()
        if r is None:
            raise KeyError(f"no active cfg_setting {key!r} -- every output location/value that "
                          f"must be config-driven needs a live row, not a hardcoded fallback in "
                          f"the calling code (governance.rules_must_be_config_driven)")
        val = json.loads(r["value"])
        _trace(f"required_setting {key}", val)
        return val
```

**What it does.** Reads `cfg_setting` (active rows only); raises KeyError when the key is missing or inactive.

**Config read by this element (found in its code).** config tables named: `cfg_setting`

**Data (found in its code).** none directly.

#### C24 — Cfg: the readers the steps use (3/3)

`iba/app/lib/cfg.py:179-183`

```python
    def enum(self, name: str) -> list[str]:
        rows = [r["value"] for r in self.conn.execute(
            "SELECT value FROM cfg_enum WHERE name=? AND inactive=0 ORDER BY ordinal", (name,))]
        _trace(f"enum({name})", rows)
        return rows
```

**What it does.** Reads active `cfg_enum` values of one name in ordinal order.

**Config read by this element (found in its code).** config tables named: `cfg_enum`

**Data (found in its code).** none directly.

#### C25 — Cfg: connection values

`iba/app/lib/cfg.py:186-190`

```python
    def connection(self, key: str):
        r = self.conn.execute(
            "SELECT value FROM cfg_connection WHERE key=? AND inactive=0", (key,)).fetchone()
        _trace(f"connection {key}", r["value"] if r else None)
        return r["value"] if r else None
```

**What it does.** Reads one active `cfg_connection` value (used by Step).

**Config read by this element (found in its code).** config tables named: `cfg_connection`

**Data (found in its code).** none directly.

#### C26 — Cfg: write grants

`iba/app/lib/cfg.py:212-219`

```python
    def may_write(self, writer: str, database: str = "iba") -> set[str]:
        """Which tables this writer (an api, a step, or 'run') is granted to write. `database` defaults
        to 'iba' (the two databases share table names)."""
        rows = {r["table_name"] for r in self.conn.execute(
            "SELECT table_name FROM cfg_write_grant WHERE writer=? AND database=? AND inactive=0",
            (writer, database))}
        _trace(f"may_write({writer}, database={database!r})", rows)
        return rows
```

**What it does.** The tables a writer (`run`, or a step id) may write: active `cfg_write_grant` rows.

**Config read by this element (found in its code).** config tables named: `cfg_write_grant`

**Data (found in its code).** none directly.

#### C27 — Cfg: book order

`iba/app/lib/cfg.py:265-269`

```python
    def book_order(self) -> dict[str, int]:
        rows = {r["book"]: r["ordinal"] for r in self.conn.execute(
            "SELECT book, ordinal FROM cfg_book_order WHERE inactive=0")}
        _trace("book_order()", rows)
        return rows
```

**What it does.** Reads `cfg_book_order` (used by Step).

**Config read by this element (found in its code).** config tables named: `cfg_book_order`

**Data (found in its code).** none directly.

#### C28 — Cfg: the dispatch gates

`iba/app/lib/cfg.py:244-249`

```python
    def work_package_inactive(self, work_package: str) -> bool:
        """True if `work_package` has an inactive `cfg_work_package` row, or no row at all. Used by
        `run.py`'s dispatch gate (#334)."""
        r = self.conn.execute("SELECT inactive FROM cfg_work_package WHERE name=?",
                              (work_package,)).fetchone()
        return True if r is None else bool(r["inactive"])
```

**What it does.** Reads `cfg_work_package.inactive`; a missing row counts as inactive.

**Config read by this element (found in its code).** config tables named: `cfg_work_package`

**Data (found in its code).** none directly.

#### C29 — Cfg: step gate

`iba/app/lib/cfg.py:251-256`

```python
    def step_inactive(self, work_package: str, step: str) -> bool:
        """True if `(work_package, step)` has a `cfg_step` row and it is `inactive=1`, OR no such
        row exists at all. Same reasoning as `work_package_inactive()`."""
        r = self.conn.execute("SELECT inactive FROM cfg_step WHERE work_package=? AND step=?",
                              (work_package, step)).fetchone()
        return True if r is None else bool(r["inactive"])
```

**What it does.** Reads `cfg_step.inactive`; a missing row counts as inactive.

**Config read by this element (found in its code).** config tables named: `cfg_step`

**Data (found in its code).** none directly.

#### C30 — Cfg: step kind gate

`iba/app/lib/cfg.py:258-263`

```python
    def step_kind(self, work_package: str, step: str) -> str | None:
        """`cfg_step.kind` (`'operations'` | `'utility'`) for `(work_package, step)`, or `None` if unset.
        `run.py` refuses a step with no kind."""
        r = self.conn.execute("SELECT kind FROM cfg_step WHERE work_package=? AND step=?",
                              (work_package, step)).fetchone()
        return r["kind"] if r else None
```

**What it does.** Reads `cfg_step.kind`; none means the step is refused.

**Config read by this element (found in its code).** config tables named: `cfg_step`

**Data (found in its code).** none directly.

#### C31 — Cfg: the step row

`iba/app/lib/cfg.py:229-234`

```python
    def step(self, work_package: str, step: str) -> sqlite3.Row:
        r = self.conn.execute(
            "SELECT * FROM cfg_step WHERE work_package=? AND step=? AND inactive=0",
            (work_package, step)).fetchone()
        _trace(f"step {step}", r["handler"] if r else None)
        return r
```

**What it does.** Reads the active `cfg_step` row (handler, scope).

**Config read by this element (found in its code).** config tables named: `cfg_step`

**Data (found in its code).** none directly.

#### C32 — Cfg: config version

`iba/app/lib/cfg.py:278-290`

```python
    def config_version(self) -> str:
        """The config version: computed live from the content of every active cfg_* rule table
        (_VERSION_TABLES_SQL), so it changes the moment the config does. 'app-0.1.0' is the
        human-readable major-version prefix."""
        base = self.conn.execute(
            "SELECT value FROM cfg_meta WHERE key='config_version'").fetchone()
        prefix = base["value"] if base else "app"
        h = hashlib.sha256()
        for (t,) in self.conn.execute(_VERSION_TABLES_SQL).fetchall():
            for row in self.conn.execute(f'SELECT * FROM "{t}" ORDER BY rowid'):
                h.update("|".join("" if v is None else str(v) for v in row).encode("utf-8"))
            h.update(b"\x00")
        return f"{prefix}+{h.hexdigest()[:12]}"
```

**What it does.** Hashes every row of every active rule table listed in `cfg_table` (plus `cfg_meta.config_version`); written into the run row.

**Config read by this element (found in its code).** config tables named: `cfg_meta`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The hash length (12).

#### C33 — Cfg: chained and sequence

`iba/app/lib/cfg.py:236-242`

```python
    def is_chained(self, work_package: str) -> bool:
        """True if every step of this work package runs under one run_id in one PS invocation ('done'
        waits for the last step); False if each step runs independently ('done' fires on that step's own
        continue path). cfg_work_package.chained. Only called for an active package (run.py's gate)."""
        r = self.conn.execute("SELECT chained FROM cfg_work_package WHERE name=?",
                              (work_package,)).fetchone()
        return bool(r["chained"]) if r else True   # default chained=True: the old, safer behaviour
```

**What it does.** Reads `cfg_work_package.chained` (0 for reading, so a run is closed at its own step).

**Config read by this element (found in its code).** config tables named: `cfg_work_package`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** Default chained when no row.

#### C34 — Cfg: step sequence

`iba/app/lib/cfg.py:222-227`

```python
    def sequence(self, work_package: str) -> list[sqlite3.Row]:
        rows = self.conn.execute(
            "SELECT * FROM cfg_step WHERE work_package=? AND inactive=0 ORDER BY ordinal",
            (work_package,)).fetchall()
        _trace(f"sequence({work_package})", rows)
        return rows
```

**What it does.** Reads the active `cfg_step` rows of the package in order (used by `run_step` after the handler).

**Config read by this element (found in its code).** config tables named: `cfg_step`

**Data (found in its code).** none directly.

#### C35 — Cfg: failure routing

`iba/app/lib/cfg.py:293-298`

```python
    def on_fail(self, step: str, condition: str) -> sqlite3.Row | None:
        r = self.conn.execute(
            "SELECT * FROM cfg_on_fail WHERE step=? AND condition=? AND inactive=0",
            (step, condition)).fetchone()
        _trace(f"on_fail({step}/{condition})", r["path"] if r else "ok")
        return r
```

**What it does.** Reads the `cfg_on_fail` row for (step, condition).

**Config read by this element (found in its code).** config tables named: `cfg_on_fail`

**Data (found in its code).** none directly.

#### C36 — Cfg: column names (used by Db.write)

`iba/app/lib/cfg.py:135-136`

```python
    def column_names(self, table: str) -> set[str]:
        return {r["name"] for r in self.columns(table)}
```

**What it does.** From `cfg_column`; Db.write refuses a column not in it.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C37 — Cfg: columns

`iba/app/lib/cfg.py:128-133`

```python
    def columns(self, table: str) -> list[sqlite3.Row]:
        rows = self.conn.execute(
            "SELECT * FROM cfg_column WHERE database='iba' AND table_name=? ORDER BY ordinal",
            (table,)).fetchall()
        _trace(f"columns({table})", rows)
        return rows
```

**What it does.** Reads `cfg_column` for one table of database iba.

**Config read by this element (found in its code).** config tables named: `cfg_column`

**Data (found in its code).** none directly.

#### C38 — Cfg: table list

`iba/app/lib/cfg.py:122-126`

```python
    def tables(self) -> list[str]:
        rows = [r["name"] for r in self.conn.execute(
            "SELECT name FROM cfg_table WHERE database='iba' ORDER BY rowid")]
        _trace("tables()", rows)
        return rows
```

**What it does.** Reads `cfg_table` for database iba (used by the row-count snapshot).

**Config read by this element (found in its code).** config tables named: `cfg_table`

**Data (found in its code).** none directly.

#### C39 — Cfg: trace line

`iba/app/lib/cfg.py:30-33`

```python
def _trace(what: str, value) -> None:
    if TRACE:
        v = value if isinstance(value, (str, int, float, bool, type(None))) else f"<{len(value)} rows>"
        print(f"    [cfg] {what:44} = {v}", file=sys.stderr)
```

**What it does.** With IBA_TRACE=1, prints each config read to stderr.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C40 — Db: opening and closing

`iba/app/lib/db.py:108-115`

```python
    def __init__(self, cfg: Cfg | None = None, path: pathlib.Path = DB_PATH):
        self.cfg = cfg or Cfg(path)
        self._own_cfg = cfg is None
        # ONE connection per process — the data layer SHARES the config handle's
        # connection, so a write transaction and a config read never self-contend
        # ('database is locked'). FKs declared in DDL but NOT hard-enforced — the raw
        # model references before its referent (word_strong before strong).
        self.conn = self.cfg.conn
```

**What it does.** Shares the Cfg connection.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C41 — Db: close

`iba/app/lib/db.py:117-120`

```python
    def close(self):
        self.conn.commit()
        if self._own_cfg:          # the shared connection is closed by whoever owns the Cfg
            self.cfg.close()
```

**What it does.** Commits the connection.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C42 — Db: get / write / update / rows

`iba/app/lib/db.py:152-155`

```python
    def get(self, table: str, **where):
        clause = " AND ".join(f'"{k}"=?' for k in where)
        return self.conn.execute(
            f'SELECT * FROM "{table}" WHERE {clause}', list(where.values())).fetchone()
```

**What it does.** Reads one row by column values.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C43 — Db.write

`iba/app/lib/db.py:122-132`

```python
    def write(self, table: str, row: dict) -> int:
        allowed = self.cfg.column_names(table)      # <- config decides the columns
        bad = set(row) - allowed
        if bad:
            raise ValueError(f"{table}: columns not in config schema: {sorted(bad)}")
        keys = list(row)
        ph = ",".join("?" * len(keys))
        cur = self.conn.execute(
            f'INSERT INTO "{table}" ({",".join(chr(34)+k+chr(34) for k in keys)}) VALUES ({ph})',
            [row[k] for k in keys])
        return cur.lastrowid
```

**What it does.** Inserts a row after checking its columns against `cfg_column`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C44 — Db.update

`iba/app/lib/db.py:157-161`

```python
    def update(self, table: str, where: dict, **sets):
        s = ", ".join(f'"{k}"=?' for k in sets)
        w = " AND ".join(f'"{k}"=?' for k in where)
        self.conn.execute(f'UPDATE "{table}" SET {s} WHERE {w}',
                          list(sets.values()) + list(where.values()))
```

**What it does.** Updates rows by column values.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C45 — Db.rows

`iba/app/lib/db.py:170-171`

```python
    def rows(self, sql: str, params=()):
        return self.conn.execute(sql, list(params)).fetchall()
```

**What it does.** Runs a query and returns all rows.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C46 — handlers.base: context and outcome

`iba/app/handlers/base.py:19-28`

```python
@dataclass
class Ctx:
    db: "object"        # lib.db.Db
    cfg: "object"       # lib.cfg.Cfg
    step: "object"      # lib.stepapi.Step
    run_id: str
    word: str
    word_id: int | None
    params: dict
    step_id: str = ""
```

**What it does.** The object a handler receives: db, cfg, step, run id, word, params, step id.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C47 — handlers.base: outcome

`iba/app/handlers/base.py:31-36`

```python
@dataclass
class Outcome:
    condition: str = "ok"       # named by the handler; resolved to a path by cfg_on_fail
    message: str = ""
    counts: dict = field(default_factory=dict)
    escalation: dict | None = None
```

**What it does.** A condition, a message, counts and an optional escalation.

**Config read by this element (found in its code).** config tables named: `cfg_on_fail`

**Data (found in its code).** none directly.

#### C48 — handlers.base: ok and fail

`iba/app/handlers/base.py:39-40`

```python
def ok(message="", **counts) -> Outcome:
    return Outcome("ok", message, counts)
```

**What it does.** `ok` names the condition `ok`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C49 — handlers.base: fail

`iba/app/handlers/base.py:43-46`

```python
def fail(condition: str, message="", **counts) -> Outcome:
    """Name a non-ok condition. The dispatcher reads cfg_on_fail[step, condition] for
    the path — the handler does not choose report-stop vs pause vs continue."""
    return Outcome(condition, message, counts)
```

**What it does.** `fail('refused', text)` names the condition `refused`; the config (`cfg_on_fail`) decides the path.

**Config read by this element (found in its code).** config tables named: `cfg_on_fail`

**Data (found in its code).** none directly.

#### C50 — handlers.reading: the writer

`iba/app/handlers/reading.py:20-24`

```python
def _writer(ctx: Ctx) -> nr.Writer:
    who = ctx.params.get("By")
    if who not in ("Claude", "Researcher"):
        raise nr.Refused("-By Claude|Researcher is required for a write step (who made the change)")
    return nr.Writer(ctx.cfg.conn, ctx.step_id, who)
```

**What it does.** A write step needs `-By Claude` or `-By Researcher`; builds the Writer (C52) for the step id.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The two allowed values of -By.

#### C51 — handlers.reading: the write wrapper

`iba/app/handlers/reading.py:27-39`

```python
def _write(ctx: Ctx, fn, export: bool = False) -> Outcome:
    try:
        w = _writer(ctx)
        message = fn(w)
    except nr.Refused as exc:
        return fail("refused", str(exc))
    if w.unresolved:                     # an unresolved reference is an error (#2134)
        eid = nr.raise_unresolved(ctx.cfg, ctx.db, w)
        message += "".join(f"\n  unresolved: {u}" for u in w.unresolved)
        message += f"\n  escalation #{eid} raised for {len(w.unresolved)} unresolved reference(s)"
    if export:
        message += f"\n  published: {', '.join(p.name for p in nr.export(ctx.cfg))}"
    return ok(message)
```

**What it does.** Runs the step function; a Refused becomes the condition `refused`. If the Writer collected unresolved verse references it would raise an escalation; the reading steps never record any, so that branch is not reached. `export` is False for these steps, so no chapter file is written.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C52 — narrativeregister.Writer

`iba/app/lib/narrativeregister.py:63-68`

```python
    def __init__(self, conn: sqlite3.Connection, step: str, who: str):
        self.conn, self.step, self.who = conn, step, who
        self.allowed = {r[0] for r in conn.execute(
            "SELECT table_name FROM cfg_write_grant WHERE writer=? AND database='iba' AND inactive=0",
            (step,))}
        self.unresolved: list[str] = []        # references written that match no verse (#2134)
```

**What it does.** Reads the tables this step id may write from `cfg_write_grant` (writer = the step id, e.g. `reading.open`).

**Config read by this element (found in its code).** config tables named: `cfg_write_grant`

**Data (found in its code).** none directly.

#### C53 — Writer._grant

`iba/app/lib/narrativeregister.py:70-72`

```python
    def _grant(self, table: str) -> None:
        if table not in self.allowed:
            raise PermissionError(f"write-grant violation: {self.step!r} may not write {table!r}")
```

**What it does.** Refuses a table the step has no write grant for.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C54 — Writer.insert

`iba/app/lib/narrativeregister.py:74-82`

```python
    def insert(self, table: str, row: dict) -> int:
        self._grant(table)
        row = {**row}
        row.setdefault("created_by", self.who)
        cols = list(row)
        cur = self.conn.execute(
            f'INSERT INTO "{table}" ({",".join(chr(34) + c + chr(34) for c in cols)}) '
            f'VALUES ({",".join("?" * len(cols))})', [row[c] for c in cols])
        return cur.lastrowid
```

**What it does.** Checks the grant, inserts the row and stamps `created_by` with the `-By` value.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C55 — Writer.update

`iba/app/lib/narrativeregister.py:84-89`

```python
    def update(self, table: str, where: dict, sets: dict) -> int:
        self._grant(table)
        s = ", ".join(f'"{k}"=?' for k in sets)
        w = " AND ".join(f'"{k}"=?' for k in where)
        return self.conn.execute(f'UPDATE "{table}" SET {s} WHERE {w}',
                                 list(sets.values()) + list(where.values())).rowcount
```

**What it does.** Checks the grant and updates rows by the where-columns.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### C56 — narrativeregister._atomic

`iba/app/lib/narrativeregister.py:117-127`

```python
def _atomic(conn: sqlite3.Connection, fn):
    """Run fn() inside a savepoint; a Refused (or any error) rolls back to it and re-raises."""
    conn.execute("SAVEPOINT narrative_register")
    try:
        result = fn()
    except BaseException:
        conn.execute("ROLLBACK TO narrative_register")
        conn.execute("RELEASE narrative_register")
        raise
    conn.execute("RELEASE narrative_register")
    return result
```

**What it does.** Runs a function inside a savepoint; on any error rolls back to it and re-raises, so a step writes all or nothing.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

## 5. Step 1 — Open (0.C)

`Reading.ps1 -Step Open -Label <label> -Escalation <id> -Home <cluster> -Objective "..." <selectors> -By Claude|Researcher`. Handler `iba.app.handlers.reading:open`. Resolves the scope, collects what is known for each verse, and writes the gap file.

### 5.1 Elements O01 to O26



#### O01 — handlers.reading.open

`iba/app/handlers/reading.py:42-53`

```python
def open(ctx: Ctx) -> Outcome:  # noqa: A001 -- the step's name
    file_request = None
    if ctx.params.get("File"):
        f = pathlib.Path(ctx.params["File"])
        f = f if f.is_absolute() else PROJECT_ROOT / f
        if not f.is_file():
            return fail("refused", f"request file not found: {f.as_posix()}")
        try:
            file_request = {k.lower(): v for k, v in json.loads(f.read_text(encoding="utf-8")).items()}
        except (ValueError, AttributeError) as exc:
            return fail("refused", f"request file {f.as_posix()} is not a JSON object: {exc}")
    return _write(ctx, lambda w: rd.open_(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT, file_request))
```

**What it does.** If `-File` is given, loads that JSON request file (relative paths from the repository root; keys lower-cased); then calls `reading.open_` through the write wrapper.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** O03 (setting reading.gap_types, enum reading_gap_type); O05 (setting reading.output_dir); O20 (setting verse_scope.max_seconds, setting verse_scope.max_verses); O22 (setting verse_collate.max_seconds)

**Data (found in its code).** none directly.

#### O02 — reading.open_ (the step)

`iba/app/lib/reading.py:216-293`

```python
def open_(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path, file_request: dict | None) -> str:
    """-Label -Escalation -Home -Objective <scope selectors as Verse-Scope.ps1> [-Reviewed] [-File request]."""
    conn = cfg.conn
    label = (p.get("Label") or "").strip()
    if not label or label != label.lower() or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", label):
        raise Refused("-Label is the reading's name, lowercase-hyphenated (e.g. anger-bosom)")
    if conn.execute("SELECT 1 FROM reading WHERE label=?", (label,)).fetchone():
        raise Refused(f"reading {label} already exists")
    objective = (p.get("Objective") or "").strip()
    if len(objective) < 10:
        raise Refused("-Objective is the scope's objective, in words (0.C: it defines the home of what is recorded)")
    try:
        eid = int(str(p.get("Escalation") or "").lstrip("#"))
    except ValueError:
        raise Refused("-Escalation (the task or issue that anchors the reading) is required") from None
    e = conn.execute("SELECT type, state FROM escalation e WHERE id=? AND version=(SELECT MAX(version) FROM escalation "
                     "x WHERE x.id=e.id)", (eid,)).fetchone()
    if e is None or e["type"] not in ("task", "issue") or e["state"] in ("completed", "closed", "withdrawn"):
        raise Refused(f"escalation #{eid} is not an open task or issue")
    home = (p.get("Home") or "").strip()
    if not conn.execute("SELECT 1 FROM cluster WHERE cluster_code=?", (home,)).fetchone():
        raise Refused(f"-Home {home!r} is not a cluster (the cluster the scope is anchored on)")
    unmapped = surfacemap.reading_refusal(conn, home)
    if unmapped:
        raise Refused(unmapped)
    types = gap_types(cfg)
    request = vs.normalise_request({k: v for k, v in p.items() if k not in NOT_SCOPE}, file_request)
    # the home (B:120): the request's subgroups of the home cluster, else the home cluster itself
    request["home"] = [s for s in request.get("subgroup", []) if conn.execute(
        "SELECT 1 FROM cluster_subgroup WHERE subgroup_code=? AND cluster_code=?", (s, home)).fetchone()] or [home]
    try:
        col = vc.collate(cfg, request, root)
    except (vs.ScopeError, vc.CollateError) as exc:
        raise Refused(str(exc)) from exc
    acc: dict = {}
    pre = [t for t, x in types.items() if x["phase"] == "pre"]
    for v in col["verses"]:
        for t in pre:
            if t in PRE:
                PRE[t](col, v, acc)
    sections = {}
    for t in pre:
        items = acc.get(t, [])
        if isinstance(items, dict):
            items = list(items.values())
        if t == "open_item":
            for it in items:
                row = _thread_item(conn, it["item"])[1]
                it["read_for"] = row["read_for"]
                it["subgroups"] = _item_subgroups(conn, row)
        sections[t] = {"guide": types[t]["guide"], "records_in": types[t]["records_in"], "items": items}
    folder = out_dir(cfg, root, label)
    gap_path = folder / f"{label}-gaps.json"
    if gap_path.exists():
        raise Refused(f"{_rel(root, gap_path)} is already on disk")

    def go():
        rid = w.insert("reading", {"label": label, "escalation_id": eid, "home_cluster": home, "objective": objective,
                                   "request": json.dumps(col["scope"]["request"], ensure_ascii=False),
                                   "gap_file": _rel(root, gap_path), "note": p.get("Note"), "run_id": run_id})
        for v in col["verses"]:
            w.insert("reading_verse", {"reading_id": rid, "verse_id": v["verse_id"],
                                       "routes": json.dumps(v["routes"], ensure_ascii=False)})
        return rid
    rid = nr._atomic(conn, go)
    data = {"reading": label, "reading_id": rid, "escalation": eid, "home": home, "objective": objective,
            "opened": _now(), "scope": col["scope"]["selectors"],
            "how": "Fill each item's `record` with one of {\"finding\": <a finding: observationrecord's shape>}, "
                   "{\"table\": \"...\", \"id\": n} or {\"reason\": \"...\"}; a face_not_gathered item may take "
                   "{\"face\", \"parties\", \"observation\"}; an open_item may take {\"response\": what the reading "
                   "found}. Then Reading.ps1 -Step Gather -Label " + label + ". New open items go in `new_items` (the "
                   "Open-Item.ps1 -Action Add shape).",
            "new_items": [], "sections": sections}
    _save(gap_path, data)
    _save(folder / f"{label}-collation.json", {"label": label, "run_id": run_id, **col})
    n = {k: len(s["items"]) for k, s in sections.items()}
    return (f"reading {label} opened (#{eid}, home {home}): {len(col['verses'])} verse(s); pre-gaps "
            + ", ".join(f"{k} {v}" for k, v in n.items()) + f"\n  -> {_rel(root, gap_path)}")
```

**What it does.** Order of work: (1) label must be lowercase-hyphenated and unused; (2) objective at least 10 characters; (3) `-Escalation` must be an open task or issue; (4) `-Home` must be a cluster; (5) `surfacemap.reading_refusal(home)` refuses an M cluster with unallocated or stale surface pairs; (6) `gap_types` (config) and the list of pre-phase gap types; (7) `versescope.normalise_request` turns the selectors (everything not in NOT_SCOPE) and the request file into one request; the home is the request's subgroups that belong to the home cluster, else the home cluster; (8) `versecollate.collate` resolves the scope and collects what is known for every verse (O20 to O24); (9) for each pre-phase gap type that has a detector (`PRE`), runs it over every verse; (10) builds one section per pre gap type with the `guide` and `records_in` from `reading.gap_types`; for the `open_item` section, reads each item's `read_for` and its subgroups; (11) refuses if the gap file already exists; (12) in one savepoint writes the `reading` row and one `reading_verse` row per verse; (13) writes `<label>-gaps.json` and `<label>-collation.json` into `reading.output_dir/<label>/`. It writes no observation, no node and no open item. Writer grants for `reading.open`: `reading`, `reading_verse`.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** O03 (setting reading.gap_types, enum reading_gap_type); O05 (setting reading.output_dir); O20 (setting verse_scope.max_seconds, setting verse_scope.max_verses); O22 (setting verse_collate.max_seconds)

**Data (found in its code).** reads data table(s) `cluster`, `cluster_subgroup`, `escalation`, `reading`; writes `reading`, `reading_verse`

**Fixed in the code, not config.** Label pattern; objective minimum of 10 characters; the three states refused for the escalation (completed, closed, withdrawn); the word `M` as the test of an M cluster (in surfacemap); the set NOT_SCOPE; the text of the `how` field in the gap file; the file names `<label>-gaps.json` and `<label>-collation.json`; the 2,500 verse guard is config (verse_scope.max_verses).

#### O03 — reading.gap_types

`iba/app/lib/reading.py:71-78`

```python
def gap_types(cfg) -> dict:
    """{type: {"phase", "records_in", "guide"}} in enum order; every enum value has its entry and no more."""
    spec = _setting(cfg, "reading.gap_types")
    names = cfg.enum("reading_gap_type")
    if set(names) != set(spec):
        raise Refused(f"cfg_enum reading_gap_type {sorted(names)} and cfg_setting reading.gap_types "
                      f"{sorted(spec)} disagree")
    return {n: spec[n] for n in names}
```

**What it does.** Reads setting `reading.gap_types` (phase, records_in, guide per gap type) and the enum `reading_gap_type`; refuses if the two disagree.

**Config read by this element (found in its code).** setting: `reading.gap_types`; enum: `reading_gap_type`; config tables named: `cfg_enum`, `cfg_setting`

**Data (found in its code).** none directly.

#### O04 — reading._setting

`iba/app/lib/reading.py:66-68`

```python
def _setting(cfg, key: str):
    v = cfg.required_setting(key)
    return json.loads(v) if isinstance(v, str) else v
```

**What it does.** `Cfg.required_setting` and, if the value is a string, `json.loads`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O05 — reading.out_dir

`iba/app/lib/reading.py:97-98`

```python
def out_dir(cfg, root: pathlib.Path, label: str) -> pathlib.Path:
    return root / cfg.required_setting("reading.output_dir") / label
```

**What it does.** `<repo>/<reading.output_dir>/<label>` (setting `reading.output_dir`).

**Config read by this element (found in its code).** setting: `reading.output_dir`

**Data (found in its code).** none directly.

#### O06 — reading._rel / _save / _now

`iba/app/lib/reading.py:120-122`

```python
def _save(path: pathlib.Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
```

**What it does.** Writes a JSON file (UTF-8, indent 1), creating the folder.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O07 — reading._rel

`iba/app/lib/reading.py:101-102`

```python
def _rel(root: pathlib.Path, p: pathlib.Path) -> str:
    return p.relative_to(root).as_posix() if p.is_relative_to(root) else p.as_posix()
```

**What it does.** Repository-relative path text.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O08 — reading._now

`iba/app/lib/reading.py:61-62`

```python
def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

**What it does.** UTC timestamp text.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O09 — pre detector: face_not_gathered

`iba/app/lib/reading.py:168-175`

```python
def _pre_face_not_gathered(col, v, acc):
    for h in v["strand_hits"]:
        gathered = any(o["tag"] == "face" and any(n["strong"] == h["strong"] and n["surface"] in (None, h["surface"])
                                                  for n in o["nodes"]) for o in v["observations"])
        if not gathered and not h["observation_id"] and not h["reason"]:      # its face is held by no finding
            acc.setdefault("face_not_gathered", []).append({"verse": v["reference"], "strand": h["strand"],
                                                           "strong": h["strong"], "surface": h["surface"],
                                                           "record": None})
```

**What it does.** For each strand hit of a verse (the `strand_hits` of the collation) that has no face on any observation node of the same Strong (and surface), no `observation_id` and no `reason`, adds an item to the section `face_not_gathered`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O10 — pre detector: meaning_missing

`iba/app/lib/reading.py:178-187`

```python
def _pre_meaning_missing(col, v, acc):
    found = acc.setdefault("meaning_missing", {})
    for x in v["words"]:
        lx = col["lexicon"].get(x["strong"], {})
        miss = [m for m, gone in (("meaning senses", not lx.get("meaning")),
                                  ("Mounce", x["strong"].startswith("G") and not lx.get("mounce"))) if gone]
        if miss:
            found.setdefault(x["strong"], {"strong": x["strong"], "missing": miss, "verses": [], "record": None})
            if v["reference"] not in found[x["strong"]]["verses"]:
                found[x["strong"]]["verses"].append(v["reference"])
```

**What it does.** For each word of a verse, looks at the collation's lexicon for that Strong: missing meaning senses, and for Greek missing Mounce. Adds one item per Strong with the verses it appears in.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** Greek is told by the code starting with G; the two source names.

#### O11 — pre detector: open_item

`iba/app/lib/reading.py:190-196`

```python
def _pre_open_item(col, v, acc):
    found = acc.setdefault("open_item", {})
    for o in v["open_items"]:
        it = found.setdefault(o["item"], {"item": o["item"], "value": o["value"], "read_for": None,
                                          "note": o["note"], "verses": [], "record": None})
        if v["reference"] not in it["verses"]:
            it["verses"].append(v["reference"])
```

**What it does.** For each open thread item matched to a verse (collation `open_items`), adds one item per thread item with the verses it appears in.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O12 — pre detector registry

`iba/app/lib/reading.py:200-201`

```python
PRE = {"face_not_gathered": _pre_face_not_gathered, "meaning_missing": _pre_meaning_missing,
       "open_item": _pre_open_item}
```

**What it does.** Maps gap type name to detector. A pre gap type with no detector gets an empty section: `term_cluster`, `base_missing` and `term_reading_missing` are pre types in the config and have no detector (checked below under 'What is not covered').

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The registry is in code, not config.

#### O13 — reading._thread_item

`iba/app/lib/reading.py:136-148`

```python
def _thread_item(conn, ref: str):
    """'OT-nn.n' -> (thread row, item row), the thread open or not."""
    m = re.fullmatch(r"(OT-\d+)\.(\d+)", (ref or "").strip(), re.I)
    if not m:
        raise Refused(f"{ref!r} is not a thread item (OT-nn.n)")
    t = conn.execute("SELECT * FROM escalation e WHERE type='thread' AND CAST(substr(alias, 4) AS INTEGER)=? AND "
                     "version=(SELECT MAX(version) FROM escalation x WHERE x.id=e.id)",
                     (int(m.group(1)[3:]),)).fetchone()
    it = t and conn.execute("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                            (t["id"], int(m.group(2)))).fetchone()
    if not it:
        raise Refused(f"thread item {ref} does not exist")
    return t, it
```

**What it does.** Resolves `OT-nn.n` to its thread and item rows (any thread state).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`, `escalation_thread_item`

#### O14 — reading._item_subgroups

`iba/app/lib/reading.py:204-213`

```python
def _item_subgroups(conn, item) -> list[dict]:
    """The subgroups a worded open item reaches: its target cluster and target terms through surface_subgroup (#2310).
    A cluster, strong, verse or escalation item names no target terms and reaches none."""
    terms = [t for t in (item["target_terms"] or "").split(",") if t]
    if not item["target_cluster"] or not terms:
        return []
    return [{"subgroup": r["subgroup_code"], "label": r["label"]} for r in conn.execute(
        "SELECT DISTINCT g.subgroup_code, g.label FROM surface_subgroup s JOIN cluster_subgroup g ON "
        f"g.id=s.cluster_subgroup_id WHERE s.deleted=0 AND s.cluster_code=? AND s.strong IN ({','.join('?' * len(terms))}) "
        "ORDER BY g.subgroup_code", [item["target_cluster"], *terms])]
```

**What it does.** For a worded open item, the subgroups its target cluster and target terms reach through `surface_subgroup` (live rows) and `cluster_subgroup`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `cluster_subgroup`, `surface_subgroup`

#### O15 — surfacemap.reading_refusal

`iba/app/lib/surfacemap.py:402-412`

```python
def reading_refusal(conn, cluster: str) -> str | None:
    """The reason reading.open refuses this home cluster, or None (B:118, #2294 G-a): an M cluster with unallocated
    or stale pairs is not read until they are."""
    if not cluster.startswith("M"):
        return None
    n, s = unallocated(conn, cluster), len(stale(conn, cluster))
    if not n and not s:
        return None
    return (f"-Home {cluster}: {n} unallocated and {s} stale (code, surface) pair(s). A cluster with unallocated or "
            f"stale pairs is not read until they are (behaviour rule surface-mapping-conditions). Map it first: "
            f"iba\\app\\ps\\Surface-Map.ps1 -Step Pairs -Cluster {cluster}, then Apply, Tail and Check.")
```

**What it does.** Only for a home starting with `M`: counts unallocated pairs and stale pairs; refuses when either is not zero.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The letter M and the wording of the refusal.

#### O16 — surfacemap.unallocated

`iba/app/lib/surfacemap.py:379-384`

```python
def unallocated(conn, cluster: str) -> int:
    return conn.execute(
        "SELECT count(*) FROM (SELECT DISTINCT l.strong, lower(trim(coalesce(l.surface,''))) AS s FROM verse_lexical l "
        "JOIN cluster_strong cs ON cs.strong=l.strong AND cs.deleted=0 AND cs.cluster_code=? WHERE l.deleted=0) p "
        "WHERE NOT EXISTS (SELECT 1 FROM surface_subgroup ss WHERE ss.cluster_code=? AND ss.strong=p.strong "
        "AND ss.surface=p.s AND ss.deleted=0)", (cluster, cluster)).fetchone()[0]
```

**What it does.** Counts the distinct (Strong, surface) pairs that occur in `verse_lexical` for the cluster's Strongs and have no live `surface_subgroup` row in that cluster.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `cluster_strong`, `surface_subgroup`, `verse_lexical`

#### O17 — surfacemap.stale

`iba/app/lib/surfacemap.py:373-376`

```python
def stale(conn, cluster: str | None = None) -> list[dict]:
    """Live pairs whose code has left the cluster or whose surface no longer occurs (C5)."""
    where, args = ("AND ss.cluster_code=?", (cluster,)) if cluster else ("", ())
    return [dict(r) for r in conn.execute(_STALE.format(where=where), args)]
```

**What it does.** Lists live pairs whose code has left the cluster or whose surface no longer occurs (the query text is the module constant `_STALE`).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O17b — surfacemap._STALE (the query)

`iba/app/lib/surfacemap.py:363-370`

```python
_STALE = ("SELECT ss.id, ss.cluster_code, ss.strong, ss.surface, ss.reason, "
          "CASE WHEN NOT EXISTS (SELECT 1 FROM cluster_strong cs WHERE cs.cluster_code=ss.cluster_code "
          "AND cs.strong=ss.strong AND cs.deleted=0) THEN 'the code is no longer in the cluster' "
          "ELSE 'the surface no longer occurs for the code' END AS why "
          "FROM surface_subgroup ss WHERE ss.deleted=0 {where} AND (NOT EXISTS (SELECT 1 FROM cluster_strong cs "
          "WHERE cs.cluster_code=ss.cluster_code AND cs.strong=ss.strong AND cs.deleted=0) OR NOT EXISTS "
          "(SELECT 1 FROM verse_lexical l WHERE l.strong=ss.strong AND l.deleted=0 "
          "AND lower(trim(coalesce(l.surface,'')))=ss.surface))")
```

**What it does.** The query that finds stale pairs.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `cluster_strong`, `surface_subgroup`, `verse_lexical`

**Fixed in the code, not config.** The query.

#### O18 — versescope.normalise_request

`iba/app/lib/versescope.py:552-574`

```python
def normalise_request(params: dict, file_request: dict | None = None) -> dict:
    """Command-line parameters (PS names, any case) and a request file merged into one request: a list per
    selector, and the home. A chapter is {'chapter': '10.1', 'section': heading or None}. Verse text is kept
    whole (it may hold ';' and ',')."""
    req: dict = {k: [] for k in SELECTORS}
    req["only_strong"] = []
    req["home"] = []
    for src in (file_request or {}, {k.lower(): v for k, v in params.items()}):
        for k in ("cluster", "subgroup", "strand", "word", "strong", "claim", "observation", "item", "thread", "home"):
            req[k] += _split(src.get(k))
        req["only_strong"] += _split(src.get("only_strong") or src.get("onlystrong"))
        if src.get("reviewed"):
            req["reviewed"] = str(src["reviewed"]).strip()
        v = src.get("verse")
        req["verse"] += [str(x) for x in (v if isinstance(v, list) else [v]) if x and str(x).strip()]
        ch = src.get("chapter")
        for c in (ch if isinstance(ch, list) else [ch]):
            if isinstance(c, dict):
                req["chapter"].append({"chapter": str(c.get("chapter")), "section": c.get("section")})
            elif c:
                for x in _split(c):
                    req["chapter"].append({"chapter": x, "section": src.get("section")})
    return {k: v for k, v in req.items() if v}
```

**What it does.** Merges the request file and the command-line parameters into one request: a list for each selector (cluster, subgroup, strand, word, strong, verse, chapter, claim, observation, item, thread), `home`, `only_strong`, and `reviewed`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `verse`

**Fixed in the code, not config.** The selector names (SELECTORS).

#### O19 — versescope: constants and small helpers

`iba/app/lib/versescope.py:49-49`, `iba/app/lib/versescope.py:50-51`, `iba/app/lib/versescope.py:52-52`, `iba/app/lib/versescope.py:53-53`, `iba/app/lib/versescope.py:54-54`

```python
SHAPE_VERSION = 2

SELECTORS = ("cluster", "subgroup", "strand", "word", "strong", "verse", "chapter", "claim",
             "observation", "item", "thread")

NO_VERSE_ROW = "no verse row (by design: governance.verse_gap_by_design)"

SETTLEMENT_TAG = "subgroup-settlement"

_CODE = re.compile(r"([HG])0*(\d{1,4})([A-Za-z]*)")
```

**What it does.** Fixed values: answer shape version 2, the selector list, the 'no verse row' wording, the tag `subgroup-settlement`, and the pattern of a Strong's code.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All of them.

#### O19b — versescope._split / _ids / _chapter_key

`iba/app/lib/versescope.py:65-74`

```python
def _split(v) -> list[str]:
    """A command-line value ('M02,M01') or a request-file list, as a list of trimmed strings."""
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        out = []
        for x in v:
            out += _split(x) if isinstance(x, str) else [str(x)]
        return out
    return [x.strip() for x in str(v).split(",") if x.strip()]
```

**What it does.** Splits a comma list into trimmed items.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O19c — versescope._ids

`iba/app/lib/versescope.py:61-62`

```python
def _ids(xs) -> str:
    return json.dumps(sorted(set(xs)))
```

**What it does.** A sorted JSON list of ids, for SQL json_each.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O19d — versescope._chapter_key

`iba/app/lib/versescope.py:77-82`

```python
def _chapter_key(v: str) -> str:
    """'02' and '2' are the same chapter; '10.1' stays '10.1' (as threadaudit reads it)."""
    head, _, rest = str(v).strip().partition(".")
    if head.isdigit():
        head = head.lstrip("0") or "0"
    return f"{head}.{rest}" if rest else head
```

**What it does.** '02' and '2' are the same chapter.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O19e — versescope.settlements

`iba/app/lib/versescope.py:85-92`

```python
def settlements(conn) -> dict[int, tuple[int, int]]:
    """verse_lexical id -> (subgroup id, observation id) for every current subgroup-settlement observation
    (rule 122): not withdrawn and not superseded by a live observation. Its nodes name their occurrence."""
    return {vl: (sg, oid) for vl, sg, oid in conn.execute(
        "SELECT n.verse_lexical_id, o.cluster_subgroup_id, o.id FROM ib_observation o JOIN ib_node n "
        "ON n.observation_id=o.id WHERE o.tag=? AND o.status<>'withdrawn' AND o.cluster_subgroup_id IS NOT NULL "
        "AND n.verse_lexical_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM ib_observation s WHERE "
        "s.supersedes_observation_id=o.id AND s.status<>'withdrawn') ORDER BY o.id", (SETTLEMENT_TAG,))}
```

**What it does.** For every current `subgroup-settlement` observation, the occurrence it places in a subgroup.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `ib_node`, `ib_observation`

**Fixed in the code, not config.** The tag name.

#### O19f — versescope.node_occurrences

`iba/app/lib/versescope.py:95-107`

```python
def node_occurrences(conn, where: str, args) -> list[tuple]:
    """(node id, verse id, osis, the occurrence or None, candidate occurrences) for the nodes `where` selects:
    the node's verse_lexical_id, else the one occurrence of its code and surface in its verse. A node matching
    several occurrences is placed on none (rule 121: it goes to its cluster's anomaly group, #2296)."""
    out = []
    for nid, vid, osis, vl, cand in conn.execute(
            "SELECT n.id, v.id, n.verse_reference, n.verse_lexical_id, (SELECT group_concat(x.id) FROM verse_lexical x "
            "WHERE x.deleted=0 AND x.verse_id=v.id AND x.strong=n.strong AND coalesce(x.surface,'')=coalesce("
            "n.surface,'')) FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference AND v.deleted=0 WHERE "
            + where + " ORDER BY n.id", args):
        match = [int(x) for x in (cand or "").split(",") if x]
        out.append((nid, vid, osis, vl if vl is not None else (match[0] if len(match) == 1 else None), match))
    return out
```

**What it does.** For observation or claim selectors: the occurrence a node names, else the one occurrence of its Strong and surface in its verse.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `ib_node`, `verse`, `verse_lexical`

#### O19g — versescope.ScopeError

`iba/app/lib/versescope.py:57-58`

```python
class ScopeError(ValueError):
    """A request that cannot be answered as given (an unknown cluster, a code that occurs nowhere)."""
```

**What it does.** The error for a request that cannot be answered.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O20 — versescope.resolve

`iba/app/lib/versescope.py:590-649`

```python
def resolve(cfg, request: dict) -> dict:
    """The verse collection for a normalised request (see normalise_request): the selectors, the verses with
    their routes and occurrences in canonical order, the home, what was not resolved, and counts. Raises
    ScopeError on a request that cannot be answered as given, or that is too wide: more verses than
    verse_scope.max_verses, or still resolving after verse_scope.max_seconds. Reads only."""
    if not any(request.get(k) for k in SELECTORS):
        raise ScopeError("the request has no selector (-Cluster, -Subgroup, -Strand, -Word, -Strong, -Verse, "
                         "-Chapter, -Claim, -Observation, -Item, -Thread or -File)")
    max_verses = int(cfg.required_setting("verse_scope.max_verses"))
    max_seconds = float(cfg.required_setting("verse_scope.max_seconds"))
    t0 = time.monotonic()
    r = Resolver(cfg)
    for h in request.get("home", []):
        r.home(h)

    def check_time():
        s = time.monotonic() - t0
        if s > max_seconds:
            raise _too_wide(r, int(s), int(max_seconds), "still resolving after the time limit, seconds")

    for k in ("cluster", "subgroup", "strand", "word", "strong", "verse", "claim", "observation"):
        for v in request.get(k, []):
            getattr(r, k)(str(v))
            check_time()
    for c in request.get("chapter", []):
        r.chapter(c["chapter"], c.get("section"))
        check_time()
    for v in request.get("item", []):
        r.item(v)
        check_time()
    for v in request.get("thread", []):
        r.thread(v)
        check_time()
    if not request.get("home"):                 # the home is what the request names (rule 120)
        for s in r.selectors:
            if s["kind"] == "subgroup" and not s.get("item"):
                r.home_sg |= {k for k, g in r.subgroups().items() if g["code"] == s["value"]}
            elif s["kind"] == "cluster" and not s.get("item") and s["value"].upper().startswith("M"):
                r.home_cl.add(s["value"])
    filt = r.only_strong(request["only_strong"]) if request.get("only_strong") else None
    if len(r.routes) > max_verses and not request.get("reviewed"):
        raise _too_wide(r, len(r.routes), max_verses, "verses in the result"
                        + (" after -OnlyStrong" if filt else ""))
    verses = r.verses()
    sgs = r.subgroups()
    occ = [o for v in verses for o in v["occurrences"]]
    ctx = [o for v in verses for o in v["context"]]
    out = {"version": SHAPE_VERSION, "request": request,
           "home": sorted(sgs[s]["code"] for s in r.home_sg) + sorted(r.home_cl),
           "selectors": r.selectors, "verses": verses, "not_resolved": r.not_resolved,
           "counts": {"verses": len(verses), "selectors": len(r.selectors), "not_resolved": len(r.not_resolved),
                      "occurrences": len(occ), "context": len(ctx),
                      "in_scope": sum(o["in_scope"] for o in occ + ctx),
                      "home": sum(o["home"] for o in occ),
                      "other_subgroups": len({o["subgroup"] for o in occ if o["subgroup"] and not o["home"]})}}
    if len(verses) > max_verses:
        out["reviewed"] = request["reviewed"]       # passed the size guard only on a recorded review
    if filt is not None:
        out["only_strong"] = filt
    return out
```

**What it does.** Refuses a request with no selector. Reads settings `verse_scope.max_verses` (2500) and `verse_scope.max_seconds` (30). Builds a Resolver, sets the home, runs each selector (cluster, subgroup, strand, word, strong, verse, claim, observation; then chapter, item, thread), checks the time limit after each, sets the home from the request when none was named, applies `only_strong`, refuses more verses than the limit unless `-Reviewed` was given, and returns the verses with routes, occurrences and counts. Reads only.

**Config read by this element (found in its code).** setting: `verse_scope.max_seconds`, `verse_scope.max_verses`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The order of the selectors; the home rule.

#### O20b — versescope._too_wide

`iba/app/lib/versescope.py:577-587`

```python
def _too_wide(r: Resolver, n: int, limit: int, what: str) -> ScopeError:
    """The refusal for a request past a guard: the selectors and their verse counts, widest first, so the
    request can be reformed (researcher 2026-10-23, #2228)."""
    parts = sorted(r.selectors, key=lambda s: -s["verses"])
    listed = "; ".join(f"{s['kind']} {s['value']}{' (' + s['item'] + ')' if s.get('item') else ''}: {s['verses']}"
                       for s in parts[:12])
    hold = ("it is held for review: reform it to a narrower scope, or, once the researcher has reviewed it, "
            "re-run with -Reviewed \"<the review>\"" if "verses" in what else "reform it to a narrower scope")
    return ScopeError(f"the request is too wide -- {what} ({n} against the limit {limit}); {hold}. "
                      f"Verses by selector, widest first: {listed}"
                      + (f"; and {len(parts) - 12} more" if len(parts) > 12 else ""))
```

**What it does.** The refusal text for a request past a limit.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The wording.

#### O21 — versescope.Resolver (class, whole)

`iba/app/lib/versescope.py:110-549`

```python
class Resolver:
    def __init__(self, cfg):
        self.conn: sqlite3.Connection = cfg.conn
        self.vx = nr.VerseIndex(cfg)
        self.routes: dict[int, list[dict]] = {}
        self.focus: dict[int, set[int]] = {}           # verse id -> the occurrences that brought it in
        self.not_resolved: list[dict] = []
        self.selectors: list[dict] = []
        self.home_sg: set[int] = set()
        self.home_cl: set[str] = set()
        self._codes: set[str] | None = None
        self._pairs: dict | None = None
        self._sg: dict | None = None
        self._settled: dict | None = None

    # ── shared ────────────────────────────────────────────────────────────────────────────────
    def occurring_codes(self) -> set[str]:
        if self._codes is None:
            self._codes = {r[0] for r in self.conn.execute(
                "SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0")}
        return self._codes

    def pairs(self) -> dict[tuple[str, str], tuple[int, int]]:
        """(code, surface) -> (subgroup id, two-sense flag) for every live surface_subgroup row; a pair's surface is
        held trimmed and lower-cased (surfacemap.norm)."""
        if self._pairs is None:
            self._pairs = {(r[0], r[1]): (r[2], r[3]) for r in self.conn.execute(
                "SELECT strong, surface, cluster_subgroup_id, two_sense FROM surface_subgroup WHERE deleted=0")}
        return self._pairs

    def subgroups(self) -> dict[int, dict]:
        if self._sg is None:
            self._sg = {r[0]: {"code": r[1], "cluster": r[2], "kind": r[3] or "group"} for r in self.conn.execute(
                "SELECT id, subgroup_code, cluster_code, kind FROM cluster_subgroup WHERE coalesce(delete_flagged,0)=0")}
        return self._sg

    def settled(self) -> dict[int, tuple[int, int]]:
        if self._settled is None:
            self._settled = settlements(self.conn)
        return self._settled

    def placed(self, vl_id: int, strong: str, surface: str) -> tuple[int | None, int, int | None]:
        """An occurrence's subgroup: (subgroup id, two-sense flag, settling observation id or None)."""
        sg, two = self.pairs().get((strong, norm(surface)), (None, 0))
        s = self.settled().get(vl_id)
        return (s[0], two, s[1]) if s else (sg, two, None)

    def _derived(self, base: str) -> list[str]:
        return sorted(c for c in self.occurring_codes() if c.startswith(base) and c[len(base):].isalpha())

    def decompose(self, given: str) -> list[str]:
        """One Strong's code as the codes it stands for (rule bare-strong-decomposed-to-derivatives)."""
        m = _CODE.fullmatch(given.strip())
        if not m:
            raise ScopeError(f"{given!r} is not a Strong's code")
        base = f"{m.group(1)}{m.group(2).zfill(4)}"
        if m.group(3):
            code = base + m.group(3)
            if code not in self.occurring_codes():
                hint = self._derived(base)
                raise ScopeError(f"{given!r} occurs in no verse"
                                 + (f" -- did you mean {', '.join(hint)}?" if hint else ""))
            return [code]
        if base in self.occurring_codes():
            return [base]
        derived = self._derived(base)
        if not derived:
            raise ScopeError(f"{given!r} occurs in no verse and has no derivative that does")
        return derived

    def senses(self, codes) -> dict[str, str]:
        return {r[0]: r[1] for r in self.conn.execute(
            "SELECT strong, head FROM strong_sense WHERE deleted=0 AND strong IN "
            "(SELECT value FROM json_each(?))", (_ids(codes),))}

    def add(self, verse_id: int, route: dict, occurrence: int | None = None) -> None:
        if route not in self.routes.get(verse_id, []):
            self.routes.setdefault(verse_id, []).append(route)
        else:
            self.routes.setdefault(verse_id, [])
        if occurrence is not None:
            self.focus.setdefault(verse_id, set()).add(occurrence)

    def miss(self, kind: str, value, reason: str) -> None:
        self.not_resolved.append({"kind": kind, "value": value, "reason": reason})

    def _expand_codes(self, raw: list[str], kind: str | None = None, value: str | None = None) -> list[str]:
        """Codes from a grouping table (kind/value given): one that occurs nowhere is reported, not raised,
        so a stale code does not refuse the whole grouping. Codes the request names itself raise."""
        out: list[str] = []
        for c in raw:
            try:
                out += self.decompose(c)
            except ScopeError as exc:
                if kind is None:
                    raise
                self.miss(kind, f"{value}: {c}", str(exc))
        return list(dict.fromkeys(out))

    def _by_occurrences(self, kind: str, value: str, rows, name: str | None = None, extra: dict | None = None,
                        route_kind: str | None = None, route_value: str | None = None) -> int:
        """Every verse of the occurrences `rows` (verse_lexical id, verse id, code, surface): each brings its
        verse in, routed by its code, and is marked in scope. The selector names the subgroups the occurrences
        fall in (rule 120: where one code falls in several, all are read). Returns the verse count."""
        seen, codes, sgs = set(), set(), set()
        for vl, vid, code, surface in rows:
            self.add(vid, {"kind": route_kind or kind, "value": route_value or value, "via": code}, vl)
            seen.add(vid)
            codes.add(code)
            sgs.add(self.placed(vl, code, surface)[0])
        sense = self.senses(codes)
        known = self.subgroups()
        self.selectors.append({"kind": kind, "value": value, **({"name": name} if name else {}),
                               "strongs": [{"code": c, "sense": sense.get(c)} for c in sorted(codes)],
                               "subgroups": sorted(known[s]["code"] for s in sgs if s in known),
                               "occurrences": len(rows), "verses": len(seen), **(extra or {})})
        return len(seen)

    def _code_rows(self, codes: list[str]) -> list[tuple]:
        return self.conn.execute(
            "SELECT id, verse_id, strong, coalesce(surface,'') FROM verse_lexical WHERE deleted=0 AND strong IN "
            "(SELECT value FROM json_each(?)) ORDER BY id", (_ids(codes),)).fetchall()

    def _by_codes(self, kind: str, value: str, codes: list[str], name: str | None = None,
                  route_kind: str | None = None, route_value: str | None = None) -> int:
        """Every occurrence of one of `codes` (one set-based query); returns the verse count."""
        return self._by_occurrences(kind, value, self._code_rows(codes), name, None, route_kind, route_value)

    def _pair_rows(self, where: str, arg) -> list[tuple]:
        return self.conn.execute(
            "SELECT v.id, v.verse_id, v.strong, coalesce(v.surface,'') FROM surface_subgroup s JOIN verse_lexical v "
            "ON v.strong=s.strong AND lower(trim(coalesce(v.surface,'')))=s.surface AND v.deleted=0 WHERE s.deleted=0 AND "
            + where + " ORDER BY v.id", (arg,)).fetchall()

    def home(self, code: str) -> None:
        """A code the request names as its home (rule 120): a subgroup that is not a qualifier group, or an
        M cluster."""
        sg = [k for k, g in self.subgroups().items() if g["code"] == code]
        if sg:
            if self.subgroups()[sg[0]]["kind"] == "qualifier":
                raise ScopeError(f"subgroup {code} is a qualifier group: a qualifying word is read for what it gives "
                                 f"the characteristic it qualifies, never as a home (cfg_behaviour_rule 120)")
            self.home_sg.add(sg[0])
            return
        row = self.conn.execute("SELECT cluster_code FROM cluster WHERE cluster_code=? AND coalesce(deleted,0)=0",
                                (code,)).fetchone()
        if row is None:
            raise ScopeError(f"home {code!r} is neither a live subgroup nor a live cluster")
        if not row[0].upper().startswith("M"):
            raise ScopeError(f"home {code} is not an M cluster: only an M cluster or one of its subgroups is a home "
                             f"(a T cluster is never a work unit of its own, cfg_behaviour_rule 120)")
        self.home_cl.add(row[0])

    # ── selectors ─────────────────────────────────────────────────────────────────────────────
    def cluster(self, code: str, **route) -> int:
        row = self.conn.execute("SELECT cluster_code, short_name FROM cluster WHERE cluster_code=? "
                                "AND coalesce(deleted,0)=0", (code,)).fetchone()
        if row is None:
            raise ScopeError(f"cluster {code!r} is not a live cluster")
        raw = [r[0] for r in self.conn.execute(
            "SELECT DISTINCT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0", (code,))]
        codes = self._expand_codes(raw, "cluster", code)
        if not self.conn.execute("SELECT 1 FROM surface_subgroup WHERE cluster_code=? AND deleted=0",
                                 (row[0],)).fetchone():
            return self._by_occurrences("cluster", code, self._code_rows(codes), row[1], {"entered_by": "codes"},
                                        **route)
        rows = self._pair_rows("s.cluster_code=?", row[0])
        got = {r[0] for r in rows}
        loose = sum(1 for r in self._code_rows(codes) if r[0] not in got)
        if loose:
            self.miss("cluster", code, f"{loose} occurrence(s) of its codes have no surface pair, so they are not "
                                       f"in the scope (Surface-Map.ps1 -Step Check -Cluster {row[0]})")
        return self._by_occurrences("cluster", code, rows, row[1], {"entered_by": "surface pairs"}, **route)

    def subgroup(self, code: str, **route) -> int:
        row = self.conn.execute("SELECT id, label, kind FROM cluster_subgroup WHERE subgroup_code=? AND "
                                "coalesce(delete_flagged,0)=0", (code,)).fetchone()
        if row is None:
            raise ScopeError(f"subgroup {code!r} is not a live cluster subgroup")
        if row[2] == "qualifier":
            raise ScopeError(f"subgroup {code} is a qualifier group and is never a work unit of its own: its words "
                             f"are read in the verses of what they qualify (cfg_behaviour_rule 120)")
        rows = [r for r in self._pair_rows("s.cluster_subgroup_id=?", row[0])
                if self.placed(r[0], r[2], r[3])[0] == row[0]]          # less those settled elsewhere
        have = {r[0] for r in rows}
        moved_in = [vl for vl, (sg, _o) in self.settled().items() if sg == row[0] and vl not in have]
        if moved_in:
            rows += self.conn.execute(
                "SELECT id, verse_id, strong, coalesce(surface,'') FROM verse_lexical WHERE deleted=0 AND id IN "
                "(SELECT value FROM json_each(?)) ORDER BY id", (_ids(moved_in),)).fetchall()
        if not rows:
            self.miss("subgroup", code, "the subgroup has no (code, surface) pair that occurs")
        return self._by_occurrences("subgroup", code, rows, row[1], {"entered_by": "surface pairs"}, **route)

    def strand(self, code: str, **route) -> int:
        row = self.conn.execute("SELECT id, title FROM reading_strand WHERE code=?", (code,)).fetchone()
        if row is None:
            raise ScopeError(f"strand {code!r} is not a defined strand (reading_strand)")
        raw = [r[0] for r in self.conn.execute(
            "SELECT strong FROM reading_strand_strong WHERE strand_id=?", (row[0],))]
        return self._by_codes("strand", code, self._expand_codes(raw, "strand", code), row[1], **route)

    def word(self, word: str, **route) -> int:
        """The occurrences whose surface is the word, case aside (rule 119); never word_strong. Surfaces that
        hold the word among other words are listed in the selector, not taken in."""
        w = word.strip()
        rows = self.conn.execute(
            "SELECT id, verse_id, strong, coalesce(surface,'') FROM verse_lexical WHERE deleted=0 AND "
            "lower(trim(surface))=lower(?) ORDER BY id", (w,)).fetchall()
        near = [f"{s} ({n})" for s, n in self.conn.execute(
            "SELECT surface, COUNT(*) FROM verse_lexical WHERE deleted=0 AND lower(trim(surface))<>lower(?) AND "
            "(' ' || lower(surface) || ' ') LIKE '% ' || lower(?) || ' %' GROUP BY surface ORDER BY 2 DESC, 1 "
            "LIMIT 12", (w, w))]
        if not rows:
            raise ScopeError(f"word {w!r} is no surface in verse_lexical (a word enters through its surface, "
                             f"cfg_behaviour_rule 119)" + (f"; surfaces holding it: {', '.join(near)}" if near else ""))
        return self._by_occurrences("word", w, rows, None, {"entered_by": "surface", "near_surfaces_not_taken": near},
                                    **route)

    def strong(self, given: str, **route) -> int:
        return self._by_codes("strong", given, self.decompose(given), None, **route)

    def verse(self, text: str, route_kind: str | None = None, route_value: str | None = None) -> int:
        refs = nr.parse_refs(text, self.vx)
        if not refs:
            self.miss("verse", text, "no verse reference found in the text")
            return 0
        seen = set()
        for r in refs:
            rk = {"kind": route_kind or "verse", "value": route_value or text, "via": r.normalised}
            if r.verse_id is not None:
                self.add(r.verse_id, rk)
                seen.add(r.verse_id)
            elif r.kind == "whole chapter" and not nr.unresolved(self.vx, r.normalised, None):
                book, ch = r.normalised.split(" ")
                for (b, c, _v), vid in self.vx.ids.items():
                    if b == book and c == int(ch):
                        self.add(vid, rk)
                        seen.add(vid)
            else:
                self.miss("verse", r.normalised, NO_VERSE_ROW if r.kind == "verse"
                          else "the book has no such chapter")
        self.selectors.append({"kind": "verse", "value": text, "verses": len(seen)})
        return len(seen)

    def chapter(self, chapter: str, section: str | None = None, route_kind: str | None = None,
                route_value: str | None = None) -> int:
        key = _chapter_key(chapter)
        rows = [r for r in self.conn.execute(
            "SELECT id, chapter_no, title FROM narrative_chapter WHERE inactive=0")
            if _chapter_key(r[1]) == key]
        if not rows:
            raise ScopeError(f"chapter {chapter!r} is not an active narrative chapter")
        cid, cno, title = rows[0]
        blocks = self.conn.execute(
            "SELECT id, heading FROM narrative_section WHERE chapter_id=? AND last_version IS NULL "
            "ORDER BY ordinal", (cid,)).fetchall()
        if section:
            blocks = [b for b in blocks if (b[1] or "").strip().lower() == section.strip().lower()]
            if not blocks:
                raise ScopeError(f"chapter {cno} has no current block headed {section!r}")
            if len(blocks) > 1:
                raise ScopeError(f"chapter {cno} has {len(blocks)} current blocks headed {section!r}")
        value = cno + (f" / {section}" if section else "")
        heading = {b[0]: b[1] for b in blocks}
        cited = {b[0]: 0 for b in blocks}
        seen = set()
        for sid, vid, written in self.conn.execute(
                "SELECT section_id, verse_id, ref_as_written FROM narrative_citation WHERE last_version IS NULL "
                "AND section_id IN (SELECT value FROM json_each(?))", (_ids(cited),)):
            if vid is None:
                self.miss("citation", f"{cno} / {heading[sid]}: {written}", "citation does not resolve to a verse")
                continue
            cited[sid] += 1
            self.add(vid, {"kind": route_kind or "chapter", "value": route_value or value, "via": heading[sid]})
            seen.add(vid)
        for sid, n in cited.items():
            if not n:
                self.miss("block", f"{cno} / {heading[sid]}", "block cites no verse")
        self.selectors.append({"kind": "chapter", "value": value, "name": title, "blocks": len(blocks),
                               "verses": len(seen)})
        return len(seen)

    def claim(self, ref: str) -> int:
        row = self.conn.execute("SELECT id, claim_ref, claim_text, status FROM narrative_claim WHERE claim_ref=? "
                                "OR CAST(id AS TEXT)=?", (ref, ref)).fetchone()
        if row is None:
            raise ScopeError(f"claim {ref!r} is not in the register")
        seen = set()
        for kind, vid, written, oid in self.conn.execute(
                "SELECT source_kind, verse_id, ref_as_written, observation_id FROM narrative_claim_source "
                "WHERE claim_id=?", (row[0],)):
            if kind == "observation" and oid is not None:      # path e through f (#2287)
                for _n, v, _osis, vl, _c in node_occurrences(self.conn, "n.observation_id=?", (oid,)):
                    self.add(v, {"kind": "claim", "value": row[1], "via": f"observation {oid}"}, vl)
                    seen.add(v)
            elif kind != "verse":
                self.miss("claim source", f"{row[1]}: {written or kind}", f"source is a {kind}, not a verse")
            elif vid is None:
                self.miss("claim source", f"{row[1]}: {written}", "source does not resolve to a verse")
            else:
                self.add(vid, {"kind": "claim", "value": row[1], "via": written})
                seen.add(vid)
        if not seen:
            self.miss("claim", row[1], "claim has no verse source")
        self.selectors.append({"kind": "claim", "value": row[1], "name": row[2], "status": row[3],
                               "verses": len(seen)})
        return len(seen)

    def observation(self, oid: str) -> int:
        row = self.conn.execute("SELECT id, status FROM ib_observation WHERE id=?", (oid,)).fetchone()
        if row is None:
            raise ScopeError(f"observation {oid!r} does not exist")
        seen = set()
        for _n, vid, osis, vl, _c in node_occurrences(self.conn, "n.observation_id=?", (row[0],)):
            self.add(vid, {"kind": "observation", "value": str(row[0]), "via": osis}, vl)
            seen.add(vid)
        if not seen:
            self.miss("observation", str(row[0]), "observation is grounded on no verse")
        self.selectors.append({"kind": "observation", "value": str(row[0]), "status": row[1],
                               "verses": len(seen)})
        return len(seen)

    def _thread(self, alias: str):
        m = re.fullmatch(r"OT-0*(\d+)", alias.strip(), re.I)
        if not m:
            raise ScopeError(f"{alias!r} is not a thread (OT-nn)")
        row = self.conn.execute("SELECT id, alias FROM escalation WHERE type='thread' AND "
                                "CAST(substr(alias, 4) AS INTEGER)=?", (int(m.group(1)),)).fetchone()
        if row is None:
            raise ScopeError(f"thread {alias!r} does not exist")
        return row

    def _item(self, kind: str, value: str, label: str, item_id: int | None = None) -> None:
        """One thread item, resolved by its kind; a kind that names no verse, or a value that does not
        resolve, is reported, not raised (a thread may hold items of every kind). A scope item gives its
        stored verses (escalation_thread_item_verse, #2287)."""
        route = {"route_kind": "item", "route_value": f"{label} {kind}:{value}"}
        before = len(self.selectors)
        try:
            if kind == "verse":
                self.verse(value, **route)
            elif kind == "cluster":
                self.cluster(value, **route)
            elif kind == "strong":
                self.strong(value, **route)
            elif kind == "chapter":
                self.chapter(value, **route)
            elif kind == "strand":
                self.strand(value, **route)
            elif kind == "scope" and item_id is not None:
                vids = [r[0] for r in self.conn.execute(
                    "SELECT verse_id FROM escalation_thread_item_verse WHERE item_id=? AND deleted=0", (item_id,))]
                for vid in vids:
                    self.add(vid, {"kind": "item", "value": route["route_value"], "via": "stored verse"})
                self.selectors.append({"kind": "scope", "value": value, "verses": len(set(vids))})
                if not vids:
                    self.miss("item", label, "scope item has no stored verse")
            else:
                self.miss("item", label, f"kind {kind!r} names no verse")
        except ScopeError as exc:
            self.miss("item", f"{label} {kind}:{value}", str(exc))
        for s in self.selectors[before:]:
            s["item"] = label

    def item(self, ref: str) -> None:
        m = re.fullmatch(r"(OT-\d+)\.(\d+)", ref.strip(), re.I)
        if not m:
            raise ScopeError(f"{ref!r} is not a thread item (OT-nn.n)")
        tid, alias = self._thread(m.group(1))
        it = self.conn.execute("SELECT kind, value, id FROM escalation_thread_item WHERE escalation_id=? AND "
                               "item_no=?", (tid, int(m.group(2)))).fetchone()
        if it is None:
            raise ScopeError(f"thread item {ref!r} does not exist")
        self._item(it[0], (it[1] or "").strip(), f"{alias}.{int(m.group(2))}", it[2])

    def thread(self, ref: str) -> None:
        tid, alias = self._thread(ref)
        items = self.conn.execute("SELECT item_no, kind, value, id FROM escalation_thread_item WHERE escalation_id=? "
                                  "AND status='open' ORDER BY item_no", (tid,)).fetchall()
        if not items:
            self.miss("thread", alias, "thread has no open item")
        for no, kind, value, iid in items:
            self._item(kind, (value or "").strip(), f"{alias}.{no}", iid)

    # ── filter and answer ─────────────────────────────────────────────────────────────────────
    def only_strong(self, raw: list[str]) -> dict:
        codes = self._expand_codes(raw)
        keep = {r[0] for r in self.conn.execute(
            "SELECT DISTINCT verse_id FROM verse_lexical WHERE deleted=0 AND strong IN (SELECT value FROM json_each(?)) "
            "AND verse_id IN (SELECT value FROM json_each(?))", (_ids(codes), _ids(self.routes)))}
        dropped = len(self.routes) - len(keep)
        self.routes = {v: r for v, r in self.routes.items() if v in keep}
        sense = self.senses(codes)
        return {"strongs": [{"code": c, "sense": sense.get(c)} for c in codes], "verses_dropped": dropped}

    def occurrences(self, vids) -> dict[int, dict]:
        """Per verse: its M-coded occurrences placed in their subgroups (an M-coded one with no pair is marked
        unplaced), and its other clustered occurrences as context (T-b)."""
        clusters: dict[str, list[str]] = {}
        for s, cl in self.conn.execute("SELECT DISTINCT strong, cluster_code FROM cluster_strong WHERE deleted=0 "
                                       "ORDER BY cluster_code"):
            clusters.setdefault(s, []).append(cl)
        sgs = self.subgroups()
        out = {v: {"occurrences": [], "context": []} for v in vids}
        for vl, vid, pos, code, surface in self.conn.execute(
                "SELECT id, verse_id, position, strong, coalesce(surface,'') FROM verse_lexical WHERE deleted=0 AND "
                "verse_id IN (SELECT value FROM json_each(?)) ORDER BY verse_id, position, id", (_ids(vids),)):
            cls = clusters.get(code, [])
            m = [c for c in cls if c.upper().startswith("M")]
            sg, two, by = self.placed(vl, code, surface)
            in_scope = vl in self.focus.get(vid, ())
            if sg in sgs:
                g = sgs[sg]
                out[vid]["occurrences"].append({
                    "id": vl, "position": pos, "strong": code, "surface": surface, "cluster": g["cluster"],
                    "subgroup": g["code"], "kind": g["kind"], "two_sense": bool(two),
                    **({"settled_by": by} if by else {}), "in_scope": in_scope,
                    "home": sg in self.home_sg or g["cluster"] in self.home_cl})
            elif m:
                out[vid]["occurrences"].append({
                    "id": vl, "position": pos, "strong": code, "surface": surface, "cluster": m[0], "subgroup": None,
                    "kind": None, "two_sense": False, "unplaced": True, "in_scope": in_scope,
                    "home": m[0] in self.home_cl})
            elif cls or in_scope:
                out[vid]["context"].append({"id": vl, "position": pos, "strong": code, "surface": surface,
                                            "clusters": cls, "in_scope": in_scope})
        return out

    def verses(self) -> list[dict]:
        rank = {osis: self.vx.book_rank.get(code, 999) for code, osis in self.vx.osis.items()}
        rows = self.conn.execute("SELECT id, osisId, reference FROM verse WHERE id IN (SELECT value FROM json_each(?))",
                                 (_ids(self.routes),)).fetchall()
        occ = self.occurrences([r[0] for r in rows])

        def key(r):
            b, c, v = (r[1].split(".") + ["0", "0"])[:3]
            return (rank.get(b, 999), int(c), int(v))
        return [{"verse_id": r[0], "osis": r[1], "reference": r[2], "routes": self.routes[r[0]], **occ[r[0]]}
                for r in sorted(rows, key=key)]
```

**What it does.** Which method runs depends on the selectors you give. `__init__` builds a VerseIndex (which reads `narrative.book_alias_map`). `home` accepts a non-qualifier subgroup or an M cluster. `cluster`, `subgroup`, `strand`, `word`, `strong`, `verse`, `chapter`, `claim`, `observation`, `item`, `thread` bring verses in by that selector (`_by_occurrences`, `_by_codes`, `_pair_rows`, `_code_rows`, `_expand_codes`, `decompose`, `_derived`, `occurring_codes`, `pairs`, `subgroups`, `settled`, `placed`, `senses`, `add`, `miss`). `only_strong` filters; `occurrences` and `verses` build the answer. It reads data tables only (listed beside the code); it reads no config setting except through VerseIndex.

**Config read by this element (found in its code).** config tables named: `cfg_behaviour_rule`

**Data (found in its code).** reads data table(s) `cluster`, `cluster_strong`, `cluster_subgroup`, `escalation`, `escalation_thread_item`, `escalation_thread_item_verse`, `ib_observation`, `narrative_chapter`, `narrative_citation`, `narrative_claim`, `narrative_claim_source`, `narrative_section`, `reading_strand`, `reading_strand_strong`, `strong_sense`, `surface_subgroup`, `verse`, `verse_lexical`

**Fixed in the code, not config.** The rules coded in it: a qualifier subgroup is never a home; a T cluster is never a home; a bare Strong's code stands for its lettered derivatives; a word enters by its surface; 12 near surfaces listed; `status='open'` for thread items.

#### O22 — versecollate.collate

`iba/app/lib/versecollate.py:41-226`

```python
def collate(cfg, request: dict, root: pathlib.Path) -> dict:
    """The collation for a normalised request (versescope.normalise_request). Raises vs.ScopeError (the scope)
    or CollateError (past verse_collate.max_seconds)."""
    t0 = time.monotonic()
    max_seconds = float(cfg.required_setting("verse_collate.max_seconds"))

    def check(step: str):
        if time.monotonic() - t0 > max_seconds:
            raise CollateError(f"collating stopped at the time limit (verse_collate.max_seconds {max_seconds:g}) "
                               f"while {step}; reform the scope to a narrower one")

    scope = vs.resolve(cfg, request)
    conn = cfg.conn
    vids = [v["verse_id"] for v in scope["verses"]]
    J = _ids(vids)
    rec = {v["verse_id"]: {"verse_id": v["verse_id"], "reference": v["reference"], "osis": v["osis"],
                           "routes": v["routes"], "occurrences": v["occurrences"], "text": None, "status": None,
                           "words": [], "surfaces": [], "observations": [],
                           "strand_hits": [], "claims": [], "narrative": [], "open_items": [], "file_lines": [],
                           "gaps": []} for v in scope["verses"]}

    for vid, text, status in conn.execute(
            "SELECT v.id, v.text, m.status FROM verse v LEFT JOIN verse_meta m ON m.verse_id=v.id "
            "WHERE v.id IN (SELECT value FROM json_each(?))", (J,)):
        rec[vid]["text"], rec[vid]["status"] = text, status

    strongs: set[str] = set()
    clusters: set[str] = set()
    for vid, surface, strong, cl, name in conn.execute(
            "SELECT vl.verse_id, vl.surface, vl.strong, cs.cluster_code, c.short_name FROM verse_lexical vl "
            "JOIN cluster_strong cs ON cs.strong=vl.strong AND cs.deleted=0 AND cs.cluster_code LIKE 'M%' "
            "LEFT JOIN cluster c ON c.cluster_code=cs.cluster_code "
            "WHERE vl.deleted=0 AND vl.verse_id IN (SELECT value FROM json_each(?)) ORDER BY vl.verse_id, vl.position",
            (J,)):
        rec[vid]["words"].append({"surface": surface, "strong": strong, "cluster": cl, "cluster_name": name})
        strongs.add(strong)
        clusters.add(cl)
    # every surface occurrence of the verse (the path verse_lexical -> cluster_strong -> surface_subgroup ->
    # cluster_subgroup, #2312): its clusters and its subgroups
    cl_of = collections.defaultdict(set)
    for strong, cl in conn.execute("SELECT strong, cluster_code FROM cluster_strong WHERE deleted=0"):
        cl_of[strong].add(cl)
    sub_of = collections.defaultdict(set)
    for cl, strong, surface, sg in conn.execute(
            "SELECT s.cluster_code, s.strong, s.surface, g.subgroup_code FROM surface_subgroup s JOIN cluster_subgroup g "
            "ON g.id=s.cluster_subgroup_id WHERE s.deleted=0"):
        sub_of[(strong, surface)].add(sg)
    for vid, vlid, pos, surface, strong, morph in conn.execute(
            "SELECT verse_id, id, position, surface, strong, morph_code FROM verse_lexical WHERE deleted=0 AND "
            "verse_id IN (SELECT value FROM json_each(?)) ORDER BY verse_id, position, id", (J,)):
        rec[vid]["surfaces"].append({"occurrence": vlid, "position": pos, "surface": surface, "strong": strong,
                                     "morph": morph, "clusters": sorted(cl_of.get(strong, ())),
                                     "subgroups": sorted(sub_of.get((strong, surface), ()))})
    check("reading the words")

    # every observation of the verse that is not withdrawn (any stage, any status), with the nodes that apply it to
    # this verse: the surface occurrence (verse_lexical_id), its role and its subgroup (#2312, #2276)
    obs_at: dict = {}
    for vid, oid, stage, tag, text, basis, note, status in conn.execute(
            "SELECT DISTINCT v.id, o.id, o.stage, o.tag, coalesce(o.meaning, o.obs_text), o.basis, o.revisit_note, "
            "o.status FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference JOIN ib_observation o ON "
            "o.id=n.observation_id AND o.status<>'withdrawn' WHERE v.id IN (SELECT value FROM json_each(?)) "
            "ORDER BY v.id, o.id", (J,)):
        obs_at[(vid, oid)] = {"id": oid, "stage": stage, "tag": tag, "status": status, "text": text, "basis": basis,
                              "october_disposition": _disposition(note), "nodes": []}
        rec[vid]["observations"].append(obs_at[(vid, oid)])
    for vid, oid, nid, strong, surface, role, vlid, sg in conn.execute(
            "SELECT v.id, n.observation_id, n.id, n.strong, n.surface, n.role, n.verse_lexical_id, "
            "n.cluster_subgroup_code FROM ib_node n JOIN verse v ON v.osisId=n.verse_reference WHERE v.id IN "
            "(SELECT value FROM json_each(?)) AND (n.disposition IS NULL OR n.disposition<>'withdrawn') "
            "ORDER BY n.id", (J,)):
        if (vid, oid) in obs_at:
            obs_at[(vid, oid)]["nodes"].append({"node": nid, "strong": strong, "surface": surface, "role": role,
                                                "verse_lexical_id": vlid, "subgroup": sg})
    for vid, code, strong, surface, face, reason, oid in conn.execute(
            "SELECT h.verse_id, s.code, h.strong, h.surface, h.face, h.reason, h.observation_id FROM reading_strand_hit h "
            "JOIN reading_strand s ON s.id=h.strand_id WHERE h.verse_id IN (SELECT value FROM json_each(?))", (J,)):
        rec[vid]["strand_hits"].append({"strand": code, "strong": strong, "surface": surface, "face": face,
                                        "reason": reason, "observation_id": oid})
    check("reading observations and strand hits")

    tellings = collections.defaultdict(list)
    for cid, chap, head in conn.execute(
            "SELECT t.claim_id, ch.chapter_no, s.heading FROM narrative_claim_telling t "
            "JOIN narrative_section s ON s.id=t.section_id AND s.last_version IS NULL "
            "JOIN narrative_chapter ch ON ch.id=s.chapter_id AND ch.inactive=0 WHERE t.status='current' AND t.claim_id IN "
            "(SELECT claim_id FROM narrative_claim_source WHERE verse_id IN (SELECT value FROM json_each(?)))", (J,)):
        tellings[cid].append(f"{chap} / {head}")
    for vid, cid, ref, text, status in conn.execute(
            "SELECT DISTINCT s.verse_id, c.id, c.claim_ref, c.claim_text, c.status FROM narrative_claim_source s "
            "JOIN narrative_claim c ON c.id=s.claim_id WHERE s.verse_id IN (SELECT value FROM json_each(?)) "
            "AND c.status IN ('current', 'held') ORDER BY s.verse_id, c.id", (J,)):
        rec[vid]["claims"].append({"claim": ref, "text": text, "status": status, "told_in": tellings.get(cid, [])})
    for vid, chap, head in conn.execute(
            "SELECT DISTINCT ci.verse_id, ch.chapter_no, s.heading FROM narrative_citation ci "
            "JOIN narrative_section s ON s.id=ci.section_id AND s.last_version IS NULL "
            "JOIN narrative_chapter ch ON ch.id=s.chapter_id AND ch.inactive=0 "
            "WHERE ci.last_version IS NULL AND ci.verse_id IN (SELECT value FROM json_each(?))", (J,)):
        rec[vid]["narrative"].append(f"{chap} / {head}")
    check("reading claims and the narrative")

    by_ref = {r["reference"]: vid for vid, r in rec.items()}
    by_strong = collections.defaultdict(set)
    by_cluster = collections.defaultdict(set)
    for vid, r in rec.items():                          # open items reach a verse through its surfaces (#2312)
        for w in r["surfaces"]:
            by_strong[w["strong"]].add(vid)
            for cl in w["clusters"]:
                by_cluster[cl].add(vid)
    seen = set()
    for t, it, qv in escalation.match_open_items(Db(cfg), clusters=sorted(by_cluster), strongs=sorted(by_strong),
                                                 verses=sorted(by_ref), home=False):   # worded items: verses only
        targets = {by_ref[qv]} if qv in by_ref else by_strong.get(qv) or by_cluster.get(qv) or set()
        for vid in targets:
            if (vid, it["id"]) in seen:
                continue
            seen.add((vid, it["id"]))
            rec[vid]["open_items"].append({"item": f"{t['alias']}.{it['item_no']}", "kind": it["kind"],
                                           "value": it["value"], "matched_on": qv, "note": it["note"]})
    check("matching open items")

    files: dict[str, list] = collections.defaultdict(list)
    for vid, path, sha, imported, head, line_no, line_kind, found_by, written in conn.execute(
            "SELECT x.verse_id, f.path, f.sha256, f.imported_observations, s.heading, x.line_no, x.line_kind, x.found_by, "
            "x.ref_as_written "
            "FROM reading_ref x JOIN reading_file f ON f.id=x.file_id AND f.removed=0 "
            "JOIN reading_section s ON s.id=x.section_id WHERE x.deleted=0 "
            "AND x.verse_id IN (SELECT value FROM json_each(?)) ORDER BY f.path, x.line_no", (J,)):
        files[path].append((vid, sha, imported, head, line_no, line_kind, found_by, written))
    stale = []
    for path, hits in files.items():
        p = root / path
        data = p.read_bytes() if p.is_file() else b""
        if hashlib.sha256(data).hexdigest() != hits[0][1]:
            stale.append(path)
        lines = data.decode("utf-8", errors="replace").replace("\r\n", "\n").split("\n")
        for vid, _sha, imported, head, line_no, line_kind, found_by, written in hits:
            rec[vid]["file_lines"].append({"file": path, "section": head, "line": line_no, "line_kind": line_kind,
                                           "found_by": found_by, "as_written": written, "imported": bool(imported),
                                           "text": lines[line_no - 1] if 0 < line_no <= len(lines) else None})
        check("extracting file lines")

    lexicon = {}
    for strong, head in conn.execute("SELECT strong, head FROM strong_sense WHERE deleted=0 AND strong IN "
                                     "(SELECT value FROM json_each(?))", (_ids(strongs),)):
        lexicon[strong] = {"sense": head, "meaning": [], "mounce": None, "lsj_chars": None}
    for strong, text in conn.execute("SELECT strong_variant, sense_text FROM strong_meaning_tree WHERE deleted=0 AND "
                                     "strong_variant IN (SELECT value FROM json_each(?)) ORDER BY strong_variant, sort",
                                     (_ids(strongs),)):
        lexicon.setdefault(strong, {"sense": None, "meaning": [], "mounce": None, "lsj_chars": None})["meaning"].append(text)
    for strong, mounce, lsj in conn.execute("SELECT strong, mounce, length(lsj) FROM strong_lexicon WHERE deleted=0 AND "
                                            "strong IN (SELECT value FROM json_each(?))", (_ids(strongs),)):
        lexicon.setdefault(strong, {"sense": None, "meaning": [], "mounce": None, "lsj_chars": None})
        lexicon[strong]["mounce"], lexicon[strong]["lsj_chars"] = mounce, lsj

    counts = collections.Counter()
    for r in rec.values():
        g = r["gaps"]
        read = bool(r["observations"]) or any(h["face"] for h in r["strand_hits"])
        if not read:
            g.append("not read")
        if r["file_lines"] and not r["observations"]:
            g.append("read in files only")
        if any(not h["face"] and not h["reason"] for h in r["strand_hits"]):
            g.append("hit unread")
        if r["observations"] and not any(c["status"] == "current" for c in r["claims"]):
            g.append("observed, no claim")
        if any(c["status"] == "current" and not c["told_in"] for c in r["claims"]):
            g.append("claim not told")
        if r["open_items"]:
            g.append("open item")
        if any(not lexicon.get(w["strong"], {}).get("meaning") or
               (w["strong"].startswith("G") and not lexicon.get(w["strong"], {}).get("mounce")) for w in r["words"]):
            g.append("meaning missing")
        counts.update(g)
    verses = [rec[v] for v in vids]
    return {"scope": {k: scope[k] for k in ("version", "request", "home", "selectors", "not_resolved", "counts")},
            "verses": verses, "lexicon": lexicon,
            "gaps": {k: counts.get(k, 0) for k in GAPS},
            "files_changed_since_indexed": stale,
            "counts": {"verses": len(verses), "with_a_gap": sum(1 for r in verses if r["gaps"]),
                       "observations": sum(len(r["observations"]) for r in verses),
                       "claims": len({c["claim"] for r in verses for c in r["claims"]}),
                       "file_lines": sum(len(r["file_lines"]) for r in verses),
                       "open_items": len({o["item"] for r in verses for o in r["open_items"]}),
                       "seconds": round(time.monotonic() - t0, 1)}}
```

**What it does.** Reads setting `verse_collate.max_seconds` (120). Resolves the scope (O20), then per verse by set-based queries: text and `verse_meta.status`; its M-coded words; every surface occurrence with its clusters and subgroups; every non-withdrawn observation with its nodes; strand hits; claims and tellings; narrative citations; open thread items matched through `escalation.match_open_items`; lines of the study files from `reading_ref`/`reading_file` (only those lines; a file is re-hashed to see if it changed since indexing); the lexicon per Strong (`strong_sense`, `strong_meaning_tree`, `strong_lexicon`); then the gaps per verse. Stops with CollateError if it runs past the time limit. Reads only.

**Config read by this element (found in its code).** setting: `verse_collate.max_seconds`

**Config read below it, through the functions it calls (all levels; each has its own element).** O20 (setting verse_scope.max_seconds, setting verse_scope.max_verses)

**Data (found in its code).** reads data table(s) `cluster`, `cluster_strong`, `cluster_subgroup`, `ib_node`, `ib_observation`, `narrative_chapter`, `narrative_citation`, `narrative_claim`, `narrative_claim_source`, `narrative_claim_telling`, `narrative_section`, `reading_file`, `reading_ref`, `reading_section`, `reading_strand`, `reading_strand_hit`, `strong_lexicon`, `strong_meaning_tree`, `strong_sense`, `surface_subgroup`, `verse`, `verse_lexical`, `verse_meta`

**Fixed in the code, not config.** The gap names (GAPS); the rules that decide a gap (read = any observation or any strand face; 'meaning missing' when the meaning tree is empty or, for Greek, Mounce is missing); only clusters whose code starts with M count as 'words'.

#### O22b — versecollate: constants, error, helpers

`iba/app/lib/versecollate.py:24-25`

```python
GAPS = ("not read", "read in files only", "hit unread", "observed, no claim", "claim not told", "open item",
        "meaning missing")
```

**What it does.** The seven gap names of the collation.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### O22c — versecollate._ids

`iba/app/lib/versecollate.py:32-33`

```python
def _ids(xs) -> str:
    return json.dumps(sorted(set(xs)))
```

**What it does.** A sorted JSON list of ids.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O22d — versecollate._disposition

`iba/app/lib/versecollate.py:36-38`

```python
def _disposition(note: str | None) -> str | None:
    m = re.search(r"October disposition:\s*([^;.(]+)", note or "")
    return m.group(1).strip() if m else None
```

**What it does.** Reads the text 'October disposition: ...' from a revisit note.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The pattern.

#### O22e — versecollate.CollateError

`iba/app/lib/versecollate.py:28-29`

```python
class CollateError(ValueError):
    """Stopped by the guard: the scope is too wide to collate in the time allowed."""
```

**What it does.** The error for a scope too wide for the time allowed.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O23 — escalation.match_open_items

`iba/app/lib/escalation.py:801-830`

```python
def match_open_items(db: Db, *, clusters=(), strongs=(), verses=(), strands=(), home=True) -> list[tuple]:
    """(thread, item, query) for every open item of every thread not completed that matches: a
    cluster or Strong's by code (_code_match), a verse inside a range or chapter, a strand by its
    code. One matcher for Match, Verse-Collate and a reading (#2219, #2228). A worded item (kind 'scope',
    #2236) matches a verse on its target verses only, and a cluster only on its target cluster (its
    home) when `home` is true; never a whole cluster's verses."""
    ph = ",".join("?" * len(_THREAD_OPEN_STATES))
    threads = db.rows(f"SELECT * FROM escalation WHERE type='thread' AND state IN ({ph}) "
                      f"ORDER BY CAST(substr(alias, 4) AS INTEGER)", _THREAD_OPEN_STATES)
    out = []
    for t in threads:
        for it in _thread_items(db, t["id"], "open"):
            v = it["value"]
            if it["kind"] == "scope":
                if verses:
                    refs = {r[0] for r in db.rows(
                        "SELECT v.reference FROM escalation_thread_item_verse x JOIN verse v ON v.id=x.verse_id "
                        "WHERE x.item_id=? AND x.deleted=0", (it["id"],))}
                    out += [(t, it, q) for q in verses if any(_verse_match(ref, q) for ref in refs)]
                if home and it["target_cluster"]:
                    out += [(t, it, q) for q in clusters if _code_match(it["target_cluster"], q, _CLUSTER_CODE)]
            elif it["kind"] == "cluster":
                out += [(t, it, q) for q in clusters if _code_match(v, q, _CLUSTER_CODE)]
            elif it["kind"] == "strong":
                out += [(t, it, q) for q in strongs if _code_match(v, q, _STRONG_CODE, _strong_norm)]
            elif it["kind"] == "verse":
                out += [(t, it, q) for q in verses if _verse_match(v, q)]
            elif it["kind"] == "strand":
                out += [(t, it, q) for q in strands if v.strip().lower() == q.strip().lower()]
    return out
```

**What it does.** Reads the open threads (`state` on-hold or in-progress) and their open items, and matches each to the clusters, Strong's codes, verses and strands asked: a cluster or Strong's by code, a verse inside a range or chapter, a strand by code; a worded (`scope`) item matches a verse on its stored target verses and a cluster on its target cluster.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`, `escalation_thread_item_verse`, `verse`

**Fixed in the code, not config.** The thread open states; the code patterns for cluster and Strong's codes.

#### O23b — escalation: matching constants

`iba/app/lib/escalation.py:60-60`, `iba/app/lib/escalation.py:797-797`, `iba/app/lib/escalation.py:798-798`, `iba/app/lib/escalation.py:755-756`

```python
_THREAD_OPEN_STATES = ("on-hold", "in-progress")    # a thread never sits at raised (T2)

_CLUSTER_CODE = r"^([MT]\d+)([a-z]*)$"

_STRONG_CODE = r"^([HG]\d+)([A-Z]*)$"

_VERSE_RE = _re.compile(r"^\s*(?P<book>\d?\s*[A-Za-z]+)\.?\s+(?P<ch>\d+)"
                        r"(?::(?P<v1>\d+)(?:\s*[-–—]\s*(?P<v2>\d+))?)?\s*$")
```

**What it does.** The two thread states, the cluster-code and Strong's-code patterns, and the verse pattern.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### O23c — escalation._thread_items

`iba/app/lib/escalation.py:497-502`

```python
def _thread_items(db: Db, escalation_id: int, status: str | None = None):
    if status:
        return db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND status=? "
                       "ORDER BY item_no", (escalation_id, status))
    return db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? ORDER BY item_no",
                   (escalation_id,))
```

**What it does.** A thread's items, optionally of one status.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation_thread_item`

#### O23d — escalation._verse_match

`iba/app/lib/escalation.py:786-794`

```python
def _verse_match(item_value: str, query: str) -> bool:
    """A verse matches inside a range (either side may be a range), and a whole-chapter item
    ('Rom 8') matches any verse of that chapter."""
    a, b = _parse_verse(item_value), _parse_verse(query)
    if not a or not b or a[0] != b[0] or a[1] != b[1]:
        return False
    if a[2] is None or b[2] is None:
        return True
    return a[2] <= b[3] and b[2] <= a[3]
```

**What it does.** A verse inside a range matches; a whole-chapter item matches any verse of the chapter.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O23e — escalation._parse_verse

`iba/app/lib/escalation.py:759-765`

```python
def _parse_verse(s: str):
    m = _VERSE_RE.match(s)
    if not m:
        return None
    v1 = int(m["v1"]) if m["v1"] else None
    v2 = int(m["v2"]) if m["v2"] else v1
    return (m["book"].replace(" ", "").lower(), int(m["ch"]), v1, v2)
```

**What it does.** Splits a verse reference into book, chapter, verse range.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O23f — escalation._code_match

`iba/app/lib/escalation.py:773-779`

```python
def _code_match(item_value: str, query: str, pattern: str, norm=lambda b: b) -> bool:
    """Exact code, else the same base when either side has no suffix (M10 <-> M10c,
    H7067 <-> H7067G); two different suffixes never match."""
    a, b = _code_parts(item_value, pattern), _code_parts(query, pattern)
    if not a or not b or norm(a[0]) != norm(b[0]):
        return False
    return a[1] == b[1] or not a[1] or not b[1]
```

**What it does.** Exact code, else same base when either side has no suffix.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O23g — escalation._code_parts

`iba/app/lib/escalation.py:768-770`

```python
def _code_parts(code: str, pattern: str):
    m = _re.match(pattern, code.strip(), _re.IGNORECASE)
    return (m.group(1).upper(), (m.group(2) or "").lower()) if m else None
```

**What it does.** Splits a code into base and suffix.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O23h — escalation._strong_norm

`iba/app/lib/escalation.py:782-783`

```python
def _strong_norm(base: str) -> str:
    return base[0] + base[1:].zfill(4)       # reference_strongs_zero_padded_4digit_in_db
```

**What it does.** Zero-pads a Strong's number to four digits.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O24 — narrativeregister.VerseIndex

`iba/app/lib/narrativeregister.py:143-166`

```python
    def __init__(self, cfg):
        conn = cfg.conn
        self.alias = dict(cfg.setting("narrative.book_alias_map"))
        self.ids: dict[tuple[str, int, int], int] = {}
        self.last_verse: dict[tuple[str, int], int] = {}
        self.max_chapter: dict[str, int] = {}
        self.osis: dict[str, str] = {}
        self.no_chapter: set[str] = set()      # single-chapter books: verse.reference is 'Obd 12'
        for vid, ref, osis in conn.execute(
                "SELECT id, reference, osisId FROM verse WHERE deleted=0"):
            m = re.fullmatch(r"(\S+) (?:(\d+):)?(\d+)", ref or "")
            o = re.fullmatch(r"[^.]+\.(\d+)\.(\d+)", osis or "")
            if not m or not o:
                continue
            b, c, v = m.group(1), int(o.group(1)), int(o.group(2))
            if m.group(2) is None:
                self.no_chapter.add(b)
            self.ids[(b, c, v)] = vid
            self.last_verse[(b, c)] = max(self.last_verse.get((b, c), 0), v)
            self.max_chapter[b] = max(self.max_chapter.get(b, 0), c)
            if osis:
                self.osis.setdefault(b, osis.split(".")[0])
        order = {r[0]: r[1] for r in conn.execute("SELECT book, ordinal FROM cfg_book_order")}
        self.book_rank = {b: order.get(o, 999) for b, o in self.osis.items()}
```

**What it does.** Reads setting `narrative.book_alias_map`, the `verse` table and `cfg_book_order`.

**Config read by this element (found in its code).** setting: `narrative.book_alias_map`; config tables named: `cfg_book_order`

**Data (found in its code).** reads data table(s) `verse`

#### O24b — VerseIndex: book / single_chapter / ref

`iba/app/lib/narrativeregister.py:168-169`

```python
    def book(self, token: str) -> str | None:
        return self.alias.get(token.lower().replace(" ", "").replace(".", ""))
```

**What it does.** Book alias to code.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O24c — VerseIndex.single_chapter

`iba/app/lib/narrativeregister.py:171-172`

```python
    def single_chapter(self, code: str) -> bool:
        return code in self.no_chapter or self.max_chapter.get(code, 0) == 1
```

**What it does.** Whether a book has one chapter.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O24d — VerseIndex.ref

`iba/app/lib/narrativeregister.py:174-176`

```python
    def ref(self, code: str, c: int, v: int) -> str:
        """verse.reference form: '1Sa 24:5'; 'Jude 6' for a single-chapter book."""
        return f"{code} {v}" if code in self.no_chapter else f"{code} {c}:{v}"
```

**What it does.** The reference form `1Sa 24:5` (or `Jude 6`).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O25 — narrativeregister.parse_refs

`iba/app/lib/narrativeregister.py:275-314`

```python
def parse_refs(text: str, vx: VerseIndex, follow_ons: bool = True, bare_follow_ons: bool = True) -> list[Ref]:
    """Every verse reference in `text` (a passage or a source list), expanded to one Ref per verse.
    A capitalised word that is not a book alias is not a reference and is skipped. Bare follow-ons
    in parentheses -- '(8:12)', '(5)' -- take book (and chapter) from the reference before them in
    the same text (test plan 3.9, 3.10). bare_follow_ons=False skips a follow-on that is only a
    number, '(5)', and keeps '(v. 5)': in study files a bare number is mostly a word count (#2228)."""
    hits: list[tuple[int, int, str, list]] = []          # (start, end, as_written, rows)
    last_book, last_ch, last_end = None, None, -1
    events = []
    for m in _REF_RX.finditer(text):
        code = vx.book(m.group("book"))
        if code:
            events.append(("ref", m.start(), m.end(), m, code))
    if follow_ons:
        for rx, kind in ((_FOLLOW_CV, "cv"), (_FOLLOW_V, "v")):
            for m in rx.finditer(text):
                events.append((kind, m.start(), m.end(), m, None))
    events.sort(key=lambda e: e[1])
    taken: list[tuple[int, int]] = []
    for kind, s, e, m, code in events:
        if any(a <= s < b for a, b in taken):
            continue
        if kind == "ref":
            rows, last_ch = _expand(vx, code, m.group("body"), None)
            last_book = code
        elif last_book is None:
            continue
        elif kind == "cv":
            rows, last_ch = _expand(vx, last_book, m.group("body"), last_ch)
        else:
            if last_ch is None or (not bare_follow_ons and not re.match(r"\(\s*vv?\.?", m.group(0))):
                continue
            rows, last_ch = _expand(vx, last_book, m.group("body"), last_ch)
        taken.append((s, e))
        hits.append((s, e, m.group(0).strip("()"), rows))
    out: list[Ref] = []
    for s, e, written, rows in hits:
        for normalised, vid, k in rows:
            out.append(Ref(written, normalised, vid, k, s))
    return out
```

**What it does.** Finds verse references in text, expanding ranges and lists to one reference per verse (Resolver.verse uses it).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The reference patterns.

#### O25b — narrativeregister._expand

`iba/app/lib/narrativeregister.py:222-258`

```python
def _expand(vx: VerseIndex, code: str, body: str, ctx_ch: int | None) -> tuple[list[tuple[str, int | None, str]], int | None]:
    """body like '24:5', '2:20–22, 29', '11:1–4; 12:9', '2:17–3:2', '6', '8–9', '1'.
    ctx_ch: the chapter in force before body (for a bare follow-on). Returns
    ([(normalised, verse_id, kind)], last chapter)."""
    out: list[tuple[str, int | None, str]] = []
    ch = ctx_ch
    single = vx.single_chapter(code)
    first = True
    for sep, part in re.findall(r"(^|,\s?|;\s)(" + _PART + r")", body):
        part = part.replace(" ", "")
        a, b = re.split(r"[–-]", part, maxsplit=1) if re.search(r"[–-]", part) else (part, "")
        if ":" in a:
            c1, v1 = (int(x) for x in a.split(":"))
            ch = c1
            if not b:
                out.append(_one(vx, code, c1, v1))
            elif ":" in b:                      # across chapters: 2:17–3:2
                c2, v2 = (int(x) for x in b.split(":"))
                out.extend(_span(vx, code, c1, v1, c2, v2))
                ch = c2
            else:
                out.extend(_span(vx, code, c1, v1, c1, int(b)))
        else:
            n1 = int(a)
            n2 = int(b) if b else None
            plain_chapter = (first and ctx_ch is None) or sep.startswith(";")
            if single and (ch is None or plain_chapter):
                ch = 1
                out.extend(_span(vx, code, 1, n1, 1, n2 or n1))
            elif plain_chapter or ch is None:
                for c in range(n1, (n2 or n1) + 1):
                    out.append((f"{code} {c}", None, "whole chapter"))
                ch = n2 or n1
            else:
                out.extend(_span(vx, code, ch, n1, ch, n2 or n1))
        first = False
    return out, ch
```

**What it does.** Expands the number part of a reference.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O25c — narrativeregister._one

`iba/app/lib/narrativeregister.py:261-262`

```python
def _one(vx: VerseIndex, code: str, c: int, v: int):
    return (vx.ref(code, c, v), vx.ids.get((code, c, v)), "verse")
```

**What it does.** One verse and its id.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O25d — narrativeregister._span

`iba/app/lib/narrativeregister.py:265-272`

```python
def _span(vx: VerseIndex, code: str, c1: int, v1: int, c2: int, v2: int):
    rows = []
    for c in range(c1, c2 + 1):
        lo = v1 if c == c1 else 1
        hi = v2 if c == c2 else max(vx.last_verse.get((code, c), v1 if c == c1 else 0), lo)
        for v in range(lo, hi + 1):
            rows.append(_one(vx, code, c, v))
    return rows
```

**What it does.** A run of verses.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O25e — narrativeregister.unresolved

`iba/app/lib/narrativeregister.py:195-202`

```python
def unresolved(vx: VerseIndex, normalised: str, verse_id: int | None) -> bool:
    """A reference that matches no verse row: a verse with no verse_id, or a whole chapter the book
    does not have. An unresolved reference in the narrative is an error and raises an escalation
    (#2134)."""
    if verse_id is not None:
        return False
    m = re.fullmatch(r"(\S+) (\d+)", normalised)
    return not (m and m.group(1) not in vx.no_chapter and (m.group(1), int(m.group(2))) in vx.last_verse)
```

**What it does.** True when a reference matches no verse row.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O25f — narrativeregister: reference patterns and Ref

`iba/app/lib/narrativeregister.py:185-185`, `iba/app/lib/narrativeregister.py:186-186`, `iba/app/lib/narrativeregister.py:189-189`, `iba/app/lib/narrativeregister.py:190-190`, `iba/app/lib/narrativeregister.py:191-191`, `iba/app/lib/narrativeregister.py:192-192`

```python
_BOOK = r"(?P<book>Song\sof\s(?:Songs|Solomon)|(?:[123]\s?)?[A-Z][a-z]+)\.?"

_PART = r"\d+(?::\d+)?(?:\s?[–-]\s?\d+(?::\d+)?)?"

_BODY = rf"(?P<body>{_PART}(?:(?:,\s?|;\s)(?:{_PART})(?![A-Za-z\d]|\s[A-Z][a-z]|\.\d))*)"

_REF_RX = re.compile(rf"(?<![\w.]){_BOOK}\s{_BODY}(?![\d:])")

_FOLLOW_CV = re.compile(r"\((?P<body>\d+:\d+(?:\s?[–-]\s?\d+(?::\d+)?)?(?:,\s?\d+(?::\d+)?)*)\)")

_FOLLOW_V = re.compile(r"\((?:v\.?\s?|vv\.?\s?)?(?P<body>\d+(?:\s?[–-]\s?\d+)?(?:,\s?\d+)*)\)")
```

**What it does.** The regular expressions.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### O25g — narrativeregister.Ref

`iba/app/lib/narrativeregister.py:131-137`

```python
@dataclasses.dataclass
class Ref:
    as_written: str            # the reference text as it stands
    normalised: str            # verse.reference form: '1Sa 24:5', or 'Isa 1' for a whole chapter
    verse_id: int | None
    kind: str                  # 'verse' | 'whole chapter'
    start: int = 0             # offset in the parsed text
```

**What it does.** One parsed reference.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### O26 — surfacemap.norm

`iba/app/lib/surfacemap.py:38-39`

```python
def norm(surface) -> str:
    return (surface or "").strip().lower()
```

**What it does.** Trim and lower-case a surface for matching.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

## 6. Step 2 — Gather (0.GAP pre) and the pre gate

`Reading.ps1 -Step Gather -Label <label> [-File <gap file>] -By ...`, then `Reading.ps1 -Step Check -Label <label> -By ...` (reading at `open`). Handlers `reading:gather` and `reading:check`.

### 6.1 Elements G01 to G51



#### G01 — handlers.reading.gather

`iba/app/handlers/reading.py:56-57`

```python
def gather(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.gather(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT))
```

**What it does.** Calls `reading.gather` through the write wrapper (C51).

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** G13 (enum ib_observation.basis, enum observation_role, enum observation_route); G14 (setting reading.observation_parts, enum ib_observation.tag); G21 (setting narrative.quote_min_words); G33 (enum escalation_assignee); G34 (enum escalation_next_action_manual); G35 (enum escalation_thread_item_kind); G36 (enum escalation_thread_item_response_kind, enum escalation_thread_item_status); G37 (enum escalation_thread_item_kind); G45 (enum escalation_state); O03 (setting reading.gap_types, enum reading_gap_type)

**Data (found in its code).** none directly.

#### G02 — reading.gather (the step)

`iba/app/lib/reading.py:334-448`

```python
def gather(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """-Label [-File <pre-gap JSON>]: every filled `record` written or checked; nothing is written if any is wrong."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "open")
    path = _path(root, p.get("File") or r["gap_file"])
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"]:
        raise Refused(f"the file is the pre-gap JSON of reading {data.get('reading')!r} (id {data.get('reading_id')}), "
                      f"not {r['label']} (id {r['id']})")
    types = gap_types(cfg)
    items = _ReadingItems(cfg, w)
    errors, quotes, plan, specs = [], [], [], []
    for sec, i, it in _items_of(data):
        rec, at = it.get("record"), f"{sec}[{i}] ({it.get('verse') or it.get('strong') or it.get('item')})"
        if rec is None or (isinstance(rec, dict) and rec.get("run_id") and rec.get("id") is not None):
            continue                                   # not yet, or written by an earlier Gather (checked at Check)
        kinds_given = [k for k in ("finding", "reason", "table", "response", "face") if rec.get(k)] \
            if isinstance(rec, dict) else []
        if sec == "face_not_gathered" and isinstance(rec, dict) and rec.get("reason") and not rec.get("face"):
            kinds_given = ["face"]                     # a strand hit's reason is the hit's own record
        if len(kinds_given) != 1:
            errors.append(f"{at}: record is one of {{\"finding\": ...}}, {{\"table\", \"id\"}} or {{\"reason\"}} "
                          f"(face_not_gathered: or a face; open_item: or a response)")
            continue
        how = kinds_given[0]
        if how == "reason":
            if len(rec["reason"].strip()) < 10:
                errors.append(f"{at}: a reason says why, in words (10 characters or more)")
            continue
        if how == "table":
            if rec["table"] not in types[sec]["records_in"]:
                errors.append(f"{at}: {sec} records into {types[sec]['records_in']}, not {rec['table']}")
            elif not _row_exists(conn, rec["table"], rec.get("id")):
                errors.append(f"{at}: {rec['table']} {rec.get('id')} does not exist")
            continue
        if how == "finding":
            if "ib_observation" not in types[sec]["records_in"]:
                errors.append(f"{at}: {sec} does not record into a finding")
                continue
            key = f"{sec}:{i}"
            specs.append((at, {**rec["finding"], "key": key}))
            plan.append(("finding", it, key))
        elif how == "response":
            if sec != "open_item" or len(rec["response"].strip()) < 10:
                errors.append(f"{at}: a response is what the reading found, on an open item (10 characters or more)")
                continue
            try:
                _thread_item(conn, it["item"])
            except Refused as exc:
                errors.append(f"{at}: {exc}")
                continue
            plan.append(("touch", it, rec["response"].strip()))
        else:                                          # a face on a strand hit
            if sec != "face_not_gathered":
                errors.append(f"{at}: a face is recorded on a face_not_gathered item")
                continue
            hit = conn.execute("SELECT h.id FROM reading_strand_hit h JOIN reading_strand s ON s.id=h.strand_id JOIN "
                               "verse v ON v.id=h.verse_id WHERE s.code=? AND h.strong=? AND v.reference=?",
                               (it.get("strand"), it.get("strong"), it.get("verse"))).fetchone()
            if hit is None:
                errors.append(f"{at}: no strand hit {it.get('strand')} {it.get('strong')} at {it.get('verse')}")
                continue
            if bool((rec.get("face") or "").strip()) == bool((rec.get("reason") or "").strip()):
                errors.append(f"{at}: give a face or a reason, one of them")
            ob = rec.get("observation")
            if ob is not None and not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'",
                                                   (ob,)).fetchone():
                errors.append(f"{at}: observation {ob} is not a live observation")
            plan.append(("hit", it, (hit["id"], rec)))
    fplan = orec.check(cfg, specs, errors, quotes) if specs else []
    new_items = _new_items(items, data, errors)
    if errors or quotes:
        raise Refused("\n  ".join(["the pre-gaps are not gathered:"] + errors + (
            ["quotation(s) not found in the ESV text:"] + quotes if quotes else [])))
    if not plan and not new_items:
        raise Refused("nothing to gather: no item has a new record, and no new item is listed")

    def go():
        _grant_findings(w)
        written = orec.write(conn, fplan, r["id"], run_id) if fplan else {}
        for kind, it, x in plan:
            rec = it["record"]
            if kind == "finding":
                it["record"] = {**rec, "table": "ib_observation", "id": written[x]["observation"],
                                "nodes": written[x]["nodes"], "run_id": run_id}
            elif kind == "touch":
                t, row = _thread_item(conn, it["item"])
                try:
                    escalation.update(cfg, Db(cfg), t["id"], item_refs=[str(row["item_no"])], response_kind="touched",
                                      respond=f"{x} (reading {r['label']}, pre gate)", via=r["escalation_id"],
                                      originator=w.who)
                except ValueError as exc:
                    raise Refused(f"{it['item']}: {exc}") from exc
                resp = conn.execute("SELECT MAX(id) FROM escalation_thread_item_response WHERE item_id=?",
                                    (row["id"],)).fetchone()[0]
                it["record"] = {**rec, "table": "escalation_thread_item_response", "id": resp, "run_id": run_id}
            else:
                hid, h = x
                w.update("reading_strand_hit", {"id": hid}, {"face": h.get("face"), "reason": h.get("reason"),
                                                             "parties": h.get("parties"),
                                                             "observation_id": h.get("observation"), "run_id": run_id})
                it["record"] = {**rec, "table": "reading_strand_hit", "id": hid, "run_id": run_id}
        added = []
        for at, spec in new_items:
            spec["added"] = items.raise_(spec, f"{at} (reading {r['label']})")
            added.append(spec["added"])
        w.update("reading", {"id": r["id"]}, {"run_id": run_id})
        return written, added
    written, added = nr._atomic(conn, go)
    _save(path, data)
    left = sum(1 for _, _, it in _items_of(data) if it.get("record") is None)
    return (f"reading {r['label']}: {len(plan)} record(s) written ({sum(1 for x in written.values() if x['new'])} "
            f"finding(s) new, {sum(len(x['nodes']) for x in written.values())} node(s)); {len(added)} open item(s) "
            f"added ({', '.join(added) or '-'}); {left} item(s) still without a record\n  ids written back to "
            f"{_rel(root, path)}")
```

**What it does.** Needs the reading to be at state `open`. Loads the gap file (`-File`, else the reading's `gap_file`) and refuses it if its `reading_id` is another reading's. For every item whose `record` is filled and not yet written (a record already carrying `run_id` and `id` is skipped): the record must be exactly one of `finding`, `reason`, `table`+`id`, `response` (open_item only) or `face` (face_not_gathered only; a `reason` on a face_not_gathered item counts as its face record). A `reason` must be 10 characters or more. A `table` must be one of that gap type's `records_in` (config) and the row must exist. A `finding` is allowed only where the gap type's `records_in` holds `ib_observation`; it is checked by `observationrecord.check` (G13 to G17) and written by `observationrecord.write`. A `response` becomes a `touched` response on the thread item, through `escalation.update` (G30). A `face` is written to the strand hit (`reading_strand_hit`: face, reason, parties, observation_id). `new_items` are checked with the open-item rules (G23 to G27) and added. Nothing is written if any record, quotation or new item is wrong; otherwise everything is written in one savepoint, then the gap file is saved with the ids written back. Writer grants for `reading.gather`: `escalation_thread_item`, `escalation_thread_item_verse`, `ib_node`, `ib_observation`, `ib_observation_change`, `reading`, `reading_strand_hit` (and the thread tables the escalation module writes under its own grants, see G30).

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** G13 (enum ib_observation.basis, enum observation_role, enum observation_route); G14 (setting reading.observation_parts, enum ib_observation.tag); G21 (setting narrative.quote_min_words); G33 (enum escalation_assignee); G34 (enum escalation_next_action_manual); G35 (enum escalation_thread_item_kind); G36 (enum escalation_thread_item_response_kind, enum escalation_thread_item_status); G37 (enum escalation_thread_item_kind); G45 (enum escalation_state); O03 (setting reading.gap_types, enum reading_gap_type)

**Data (found in its code).** reads data table(s) `escalation_thread_item_response`, `ib_observation`, `reading_strand`, `reading_strand_hit`, `strong`, `verse`; writes `reading`, `reading_strand_hit`

**Fixed in the code, not config.** The five record kinds; the minimum of 10 characters for a reason or response; the list of tables the grant helper opens (`ib_observation`, `ib_node`, `ib_observation_change`); the key `<gap type>:<index>` given to each finding; the 60-line cap on a refusal text.

#### G03 — reading._at

`iba/app/lib/reading.py:90-94`

```python
def _at(conn, label, state: str):
    r = reading(conn, label)
    if r["state"] != state:
        raise Refused(f"reading {r['label']} is {r['state']}; this step needs it {state}")
    return r
```

**What it does.** Refuses a step when the reading is not at the state it needs.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The state names (STATES).

#### G04 — reading.reading (lookup)

`iba/app/lib/reading.py:81-87`

```python
def reading(conn, label: str | None):
    if not (label or "").strip():
        raise Refused("-Label (the reading's name) is required")
    r = conn.execute("SELECT * FROM reading WHERE label=?", (label.strip(),)).fetchone()
    if r is None:
        raise Refused(f"reading {label!r} does not exist (Reading.ps1 -Step Open)")
    return r
```

**What it does.** Reads the `reading` row by label.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `reading`

#### G05 — reading._path / _load

`iba/app/lib/reading.py:105-107`

```python
def _path(root: pathlib.Path, path: str | None) -> pathlib.Path:
    f = pathlib.Path(path or "")
    return f if f.is_absolute() else root / f
```

**What it does.** Resolves a file path against the repository root.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G06 — reading._load

`iba/app/lib/reading.py:110-117`

```python
def _load(root: pathlib.Path, path: str | None, what: str) -> dict:
    f = _path(root, path)
    if not path or not f.is_file():
        raise Refused(f"{what} {path!r} not found")
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Refused(f"{what} is not valid JSON: {exc}") from exc
```

**What it does.** Loads a JSON file or refuses with the reason.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G07 — reading._items_of

`iba/app/lib/reading.py:129-133`

```python
def _items_of(data: dict):
    """(section, index, item) for every item of the pre-gap JSON."""
    for sec, s in (data.get("sections") or {}).items():
        for i, it in enumerate(s.get("items") or []):
            yield sec, i, it
```

**What it does.** Yields every item of the gap file with its section and index.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G08 — reading._row_exists

`iba/app/lib/reading.py:151-159`

```python
def _row_exists(conn, table: str, rid) -> bool:
    if not re.fullmatch(r"[a-z_]+", table or ""):
        return False
    if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone():
        return False
    try:
        return conn.execute(f'SELECT 1 FROM "{table}" WHERE id=?', (rid,)).fetchone() is not None
    except Exception:  # noqa: BLE001 -- a table with no id column cannot hold the record
        return False
```

**What it does.** True if the named table has a row with that id (table name restricted to letters and underscores).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The name pattern.

#### G09 — reading._grant_findings

`iba/app/lib/reading.py:329-331`

```python
def _grant_findings(w: nr.Writer) -> None:
    for t in ("ib_observation", "ib_node", "ib_observation_change"):
        w._grant(t)
```

**What it does.** Asks the Writer for the grants on `ib_observation`, `ib_node` and `ib_observation_change` (a refusal if the step has none).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The three table names.

#### G10 — reading constants

`iba/app/lib/reading.py:53-53`, `iba/app/lib/reading.py:54-54`, `iba/app/lib/reading.py:55-55`, `iba/app/lib/reading.py:56-56`, `iba/app/lib/reading.py:57-57`, `iba/app/lib/reading.py:58-58`

```python
Refused = nr.Refused

STATES = ("open", "gathered", "observed", "synergised", "narrated", "published")

NOT_SCOPE = ("Label", "Escalation", "Home", "By", "File", "Note", "Objective")

SETTLE = ("closed", "withdrawn", "superseded", "forward", "touched")

PART_MARK = "read in part"      # a gate 2 `touched` response: the item reaches past the reading (#2250 option A)

DISPOSE = ("claim", "held", "data", "context", "withdrawn")   # set at Apply; 'told' is set at Narrate
```

**What it does.** Fixed values: the six reading states in order; the parameter names that are not scope selectors; the settlement and disposition lists used by later steps.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### G11 — reading._ReadingItems

`iba/app/lib/reading.py:297-321`

```python
class _ReadingItems:
    """New open items (D-b): the Open-Item.ps1 -Action Add shape, through openitem.add."""

    def __init__(self, cfg, w):
        self.cfg, self.w = cfg, w

    def check(self, spec, at: str, errors: list):
        if not isinstance(spec, dict) or not spec.get("thread"):
            errors.append(f"{at}: a new item is the Open-Item add shape (thread, origin, anchor, a target, read_for, "
                          f"why, comes_back_when)")
            return None
        try:
            openitem._validate(self.cfg, openitem.spec_from(spec), vs.Resolver(self.cfg))
            openitem.resolve_target(self.cfg, openitem.spec_from(spec))
        except (openitem.ItemError, vs.ScopeError) as exc:
            errors.append(f"{at}: {exc}")
            return None
        return spec

    def raise_(self, spec, where: str) -> str:
        try:
            out = openitem.add(self.cfg, Db(self.cfg), self.w, openitem.spec_from(spec), self.w.who)
        except (openitem.ItemError, vs.ScopeError, ValueError) as exc:
            raise Refused(f"{where}: the open item could not be added: {exc}") from exc
        return out.split(" ", 1)[0]
```

**What it does.** `check` validates a new open item with `openitem._validate` and `openitem.resolve_target`; `raise_` adds it with `openitem.add`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G12 — reading._new_items

`iba/app/lib/reading.py:324-326`

```python
def _new_items(items: _ReadingItems, data: dict, errors: list) -> list:
    return [(f"new_items[{i}]", items.check(s, f"new_items[{i}]", errors))
            for i, s in enumerate(data.get("new_items") or []) if not (isinstance(s, dict) and s.get("added"))]
```

**What it does.** Checks every `new_items` entry not already added.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G13 — observationrecord.check

`iba/app/lib/observationrecord.py:62-169`

```python
def check(cfg, specs: list[tuple[str, dict]], errors: list, quotes: list) -> list[dict]:
    """[(where, spec)] -> the plan write() takes. Problems go to `errors`, quotations not in the ESV to `quotes`."""
    conn = cfg.conn
    vx = nr.VerseIndex(cfg)
    kinds_ = kinds(cfg)
    bases, routes, roles = cfg.enum("ib_observation.basis"), cfg.enum("observation_route"), cfg.enum("observation_role")
    keys, texts, plan = set(), {}, []
    for where, s in specs:
        if not isinstance(s, dict):
            errors.append(f"{where}: a finding is an object (key, kind, text, basis, nodes)")
            continue
        key = s.get("key")
        if not key or key in keys:
            errors.append(f"{where}: a unique key is required")
        keys.add(key)
        existing = s.get("existing")
        kind = s.get("kind")
        p = {"key": key, "where": where, "existing": None, "nodes": []}
        if existing is not None:
            row = conn.execute("SELECT id, tag, status FROM ib_observation WHERE id=?", (existing,)).fetchone()
            if row is None or row["status"] == "withdrawn":
                errors.append(f"{where}: existing {existing} is not a live observation")
                continue
            if any(s.get(k) for k in ("text", "meaning", "implication", "basis", "route")):
                errors.append(f"{where}: an existing finding takes nodes only (a changed description is a new finding, "
                              f"and the old one withdrawn with its reason)")
            p["existing"], kind = row["id"], row["tag"]
        else:
            if kind not in kinds_:
                errors.append(f"{where}: kind must be one of {kinds_}")
            text = (s.get("text") or "").strip()
            if not text:
                errors.append(f"{where}: text is required")
            else:
                try:
                    recordingpass._validate_obs_text(conn, text)
                except recordingpass.InvalidObservationText as exc:
                    errors.append(f"{where}: {exc}")
                dup = live_text(conn, text)
                if dup:
                    errors.append(f"{where}: this description is already live as observation {dup['id']} -- name it "
                                  f"as existing and give the nodes (one finding, many nodes)")
                if text in texts:
                    errors.append(f"{where}: the same text as {texts[text]} -- one finding, many nodes")
                texts[text] = where
            if s.get("basis") not in bases:
                errors.append(f"{where}: basis must be one of {bases}")
            route = s.get("route")
            if kind in ROUTE_REQUIRED and route not in routes:
                errors.append(f"{where}: a {kind} finding carries its route, one of {routes}")
            elif route is not None and (kind not in ROUTE_ALLOWED or route not in routes):
                errors.append(f"{where}: route ({routes}) is held only on a party or link finding")
            quotes += sr._quote_check(conn, cfg, [s.get(k) for k in ("text", "meaning", "implication")], where)
            p.update({"kind": kind, "text": text, "meaning": s.get("meaning"), "implication": s.get("implication"),
                      "basis": s.get("basis"), "route": route})
        nodes = s.get("nodes") or []
        if not nodes:
            errors.append(f"{where}: at least one node (what the finding applies to)")
        for j, n in enumerate(nodes):
            at = f"{where} nodes[{j}]"
            if not isinstance(n, dict):
                errors.append(f"{at}: a node is an object")
                continue
            if n.get("traced") is not None and not n.get("strong"):
                p["nodes"].append({"traced": n["traced"], "at": at})
                continue
            strong = n.get("strong")
            if not strong:
                errors.append(f"{at}: a node names the word (strong), or the finding it is about (traced)")
                continue
            clusters = word_clusters(conn, strong)
            cluster = n.get("cluster") or (clusters[0] if len(clusters) == 1 else None)
            if not clusters:
                errors.append(f"{at}: {strong} has no cluster (an untagged word): a node is a classification, so carry "
                              f"the word in the finding's text")
                continue
            if cluster not in clusters:
                errors.append(f"{at}: cluster must be one of {strong}'s own clusters {clusters}")
                continue
            if n.get("role") not in roles:
                errors.append(f"{at}: role must be one of {roles} (the word's role in this finding)")
            occ = {"verse_reference": None, "surface": n.get("surface"), "morph_code": None, "verse_lexical_id": None}
            if n.get("verse"):
                try:
                    vr = sr._verse(conn, vx, n["verse"])
                    occ = recordingpass.resolve_occurrence(conn, strong, vr["osisId"], n.get("surface"), None)
                except (Refused, recordingpass.UnresolvedOccurrence) as exc:
                    errors.append(f"{at}: {exc}")
                    continue
            elif kind != "term":
                errors.append(f"{at}: only a term finding applies to a word with no verse")
            p["nodes"].append({"strong": strong, "cluster": cluster, "role": n.get("role"),
                               "question": n.get("question"), "traced": n.get("traced"), "at": at,
                               **{k: occ[k] for k in ("verse_reference", "surface", "morph_code", "verse_lexical_id")}})
        if kind == "qualification":
            got = {n.get("role") for n in p["nodes"]}
            if not {"qualifier", "characteristic"} <= got:
                errors.append(f"{where}: a qualification finding applies to its qualifier (role qualifier) and the "
                              f"characteristic it binds to (role characteristic)")
        plan.append(p)
    for p in plan:
        for n in p["nodes"]:
            t = n.get("traced")
            if t is None or t in keys:
                continue
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'", (t,)).fetchone():
                errors.append(f"{n['at']}: traced {t!r} is neither a live observation nor a finding key in this file")
    return plan
```

**What it does.** Validates a list of finding specs and returns the plan, writing nothing. Per finding: a unique key; either `existing` (a live observation id; then only nodes may be given) or a new description: `kind` one of the eight kinds, `text` required and not a bare negation, not already live, not repeated in the file; `basis` one of the `ib_observation.basis` enum; `route` required on a party finding and allowed only on party or link; every quotation in text, meaning or implication found in the ESV (`narrative.quote_min_words`). Per node: a Strong's code with at least one cluster and the `cluster` among its clusters (if the code has exactly one, it is taken); `role` one of the `observation_role` enum; with a `verse`, the occurrence is resolved fresh from `verse_lexical` by `recordingpass.resolve_occurrence` (the first row wins if the Strong occurs more than once and neither surface nor morph matches); without a verse only a `term` finding may apply to a word; a `traced` node names a finding about a finding. A qualification finding must carry both a qualifier node and a characteristic node. The `question`, `meaning`, `implication` are carried as given; the check does not compare the content of any field to a requirement beyond the above.

**Config read by this element (found in its code).** enum: `ib_observation.basis`, `observation_role`, `observation_route`

**Config read below it, through the functions it calls (all levels; each has its own element).** G14 (setting reading.observation_parts, enum ib_observation.tag); G21 (setting narrative.quote_min_words)

**Data (found in its code).** reads data table(s) `cluster`, `ib_observation`, `strong`, `verse`

**Fixed in the code, not config.** The route rule (party required; party/link allowed); the qualification rule; the rule that a word with no cluster cannot be a node; the message wording.

#### G14 — observationrecord: constants and kinds

`iba/app/lib/observationrecord.py:41-48`

```python
def kinds(cfg) -> list[str]:
    """The eight kinds of finding (cfg_setting reading.observation_parts), each a live ib_observation.tag value."""
    parts = cfg.required_setting("reading.observation_parts")
    out = list((json.loads(parts) if isinstance(parts, str) else parts)["kinds"])
    missing = set(out) - set(cfg.enum("ib_observation.tag"))
    if missing:
        raise Refused(f"kinds {sorted(missing)} are not ib_observation.tag values")
    return out
```

**What it does.** Reads setting `reading.observation_parts` (`kinds`) and checks each kind is a value of enum `ib_observation.tag`.

**Config read by this element (found in its code).** setting: `reading.observation_parts`; enum: `ib_observation.tag`; config tables named: `cfg_setting`

**Data (found in its code).** none directly.

#### G14b — observationrecord constants

`iba/app/lib/observationrecord.py:33-33`, `iba/app/lib/observationrecord.py:34-34`, `iba/app/lib/observationrecord.py:34-34`

```python
STAGE = "reading"

ROUTE_REQUIRED, ROUTE_ALLOWED = ("party",), ("party", "link")

ROUTE_REQUIRED, ROUTE_ALLOWED = ("party",), ("party", "link")
```

**What it does.** Stage `reading`; the route rules.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### G15 — observationrecord.word_clusters

`iba/app/lib/observationrecord.py:51-53`

```python
def word_clusters(conn, strong: str) -> list[str]:
    return [r[0] for r in conn.execute("SELECT cluster_code FROM cluster_strong WHERE strong=? AND deleted=0 "
                                       "ORDER BY cluster_code", (strong,))]
```

**What it does.** The live clusters of a Strong's code from `cluster_strong`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `cluster_strong`

#### G16 — observationrecord.live_text

`iba/app/lib/observationrecord.py:56-59`

```python
def live_text(conn, text: str):
    """The live observation holding this exact description, if any."""
    return conn.execute("SELECT id, tag FROM ib_observation WHERE trim(obs_text)=? AND status<>'withdrawn' "
                        "ORDER BY id LIMIT 1", ((text or "").strip(),)).fetchone()
```

**What it does.** The live observation holding exactly this description.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `ib_observation`

#### G17 — observationrecord.write

`iba/app/lib/observationrecord.py:172-209`

```python
def write(conn, plan: list[dict], reading_id: int | None, run_id: str) -> dict:
    """Write a checked plan. Returns {key: {"observation": id, "nodes": [ids], "new": bool}}. Caller commits."""
    out, now = {}, _now()
    for p in plan:
        if p["existing"] is not None:
            oid, new = p["existing"], False
        else:
            oid = conn.execute(
                "INSERT INTO ib_observation (cluster_code, stage, tag, obs_text, meaning, implication, basis, route, "
                "meaning_source, status, run_id, created_at) VALUES (NULL,?,?,?,?,?,?,?,'verse-text','draft',?,?)",
                (STAGE, p["kind"], p["text"], p.get("meaning"), p.get("implication"), p["basis"], p.get("route"),
                 run_id, now)).lastrowid
            new = True
        out[p["key"]] = {"observation": oid, "nodes": [], "new": new}
    for p in plan:
        oid = out[p["key"]]["observation"]
        seq = conn.execute("SELECT COALESCE(MAX(seq), 0) FROM ib_node WHERE observation_id=?", (oid,)).fetchone()[0]
        for n in p["nodes"]:
            traced = n.get("traced")
            traced = out[traced]["observation"] if traced in out else traced
            if n.get("strong") and conn.execute(
                    "SELECT 1 FROM ib_node WHERE observation_id=? AND strong=? AND verse_reference IS ? AND "
                    "reading_id IS ? AND role IS ? AND verse_lexical_id IS ?",
                    (oid, n["strong"], n["verse_reference"], reading_id, n["role"], n.get("verse_lexical_id"))).fetchone():
                continue                                  # the same application, already written
            seq += 1
            cluster = n.get("cluster") or conn.execute(
                "SELECT cluster_code FROM ib_node WHERE observation_id=? AND cluster_code IS NOT NULL LIMIT 1",
                (traced,)).fetchone()[0]
            nid = conn.execute(
                "INSERT INTO ib_node (observation_id, cluster_code, strong, verse_reference, surface, morph_code, "
                "question_code, traced_observation_id, source_stage, seq, role, reading_id, created_at, verse_lexical_id) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (oid, cluster, n.get("strong"), n.get("verse_reference"), n.get("surface"), n.get("morph_code"),
                 n.get("question"), traced, STAGE, seq, n.get("role"), reading_id, now,
                 n.get("verse_lexical_id"))).lastrowid
            out[p["key"]]["nodes"].append(nid)
    return out
```

**What it does.** Writes a checked plan. A new finding becomes one `ib_observation` row (`cluster_code` NULL, `stage` `reading`, `tag` = kind, `meaning_source` `verse-text`, `status` `draft`). Each node becomes one `ib_node` row with: the observation, cluster, Strong, verse reference, surface, morph, question code, traced observation, `source_stage` `reading`, a sequence number, role, reading id, time, and the occurrence id (`verse_lexical_id`). A node already written for the same observation, Strong, verse, reading, role and occurrence is skipped. `ib_node.cluster_subgroup_code` is not among the columns inserted, so it stays empty.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `cluster`, `ib_node`, `strong`; writes `ib_node`, `ib_observation`

**Fixed in the code, not config.** The status `draft`, the stage and `meaning_source` literals, the duplicate-node test.

#### G18 — recordingpass._validate_obs_text

`iba/app/lib/recordingpass.py:301-305`

```python
def _validate_obs_text(conn, obs_text: str) -> None:
    if _DEGENERATE_OBS_TEXT.match(obs_text or ""):
        raise InvalidObservationText(
            f"obs_text {obs_text!r} is a bare negation with no actual content -- refusing to "
            f"write a content-less observation")
```

**What it does.** Refuses a text that is only 'none', 'n/a', 'null', 'nothing' or '-'.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The word list (below).

#### G18b — recordingpass: degenerate-text pattern and error

`iba/app/lib/recordingpass.py:293-293`

```python
_DEGENERATE_OBS_TEXT = re.compile(r"^\s*(none|n/?a|null|nothing|-)\s*\.?\s*$", re.I)
```

**What it does.** The pattern.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### G18c — recordingpass.InvalidObservationText

`iba/app/lib/recordingpass.py:296-298`

```python
class InvalidObservationText(Exception):
    """obs_text is a bare negation with no content, e.g. "none" alone ("none -- <explanation>" is
    allowed). Refused: a content-less row looks answered while adding nothing (#1723)."""
```

**What it does.** The error.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G19 — recordingpass.resolve_occurrence

`iba/app/lib/recordingpass.py:48-67`

```python
def resolve_occurrence(conn, strong: str, claimed_verse: str, claimed_surface: str | None,
                       claimed_morph: str | None) -> dict:
    """Rule 0.5: resolve fresh from iba.db, never trust the LLM's own verse string. Matches on
    strong + verse.osisId, disambiguating by surface/morph when a strong occurs more than once in
    the same verse. Raises UnresolvedOccurrence rather than writing an unverified node."""
    rows = conn.execute(
        """SELECT vl.id AS verse_lexical_id, vl.strong, vl.surface, vl.morph_code, v.osisId, v.id AS verse_id
           FROM verse_lexical vl JOIN verse v ON v.id=vl.verse_id
           WHERE vl.strong=? AND v.osisId=? AND vl.deleted=0 ORDER BY vl.position, vl.id""",
        (strong, claimed_verse)).fetchall()
    if not rows:
        raise UnresolvedOccurrence(
            f"strong {strong!r} claimed at {claimed_verse!r} has no matching live verse_lexical row")
    if len(rows) == 1:
        r = rows[0]
    else:
        exact = [r for r in rows if r["surface"] == claimed_surface or r["morph_code"] == claimed_morph]
        r = exact[0] if exact else rows[0]
    return {"verse_reference": r["osisId"], "verse_id": r["verse_id"], "surface": r["surface"],
           "morph_code": r["morph_code"], "verse_lexical_id": r["verse_lexical_id"]}
```

**What it does.** Looks up the live `verse_lexical` rows for the Strong in the verse. None: refuses. One: that row. Several: the first whose surface or morph equals the one claimed, else the first by position. Returns verse reference, surface, morph and `verse_lexical_id`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `verse`, `verse_lexical`

**Fixed in the code, not config.** The tie-break rule (first row).

#### G19b — recordingpass.UnresolvedOccurrence

`iba/app/lib/recordingpass.py:31-33`

```python
class UnresolvedOccurrence(Exception):
    """An occurrence the model claimed doesn't resolve against live verse_lexical data -- never
    written as a phantom node."""
```

**What it does.** The error.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G20 — strandreading._verse

`iba/app/lib/strandreading.py:85-95`

```python
def _verse(conn, vx, ref: str | None):
    """A verse named as osisId ('Gen.6.5') or as written in the narrative ('Gen 6:5')."""
    if not ref:
        raise Refused("a verse reference is required")
    r = conn.execute("SELECT id, osisId, reference FROM verse WHERE osisId=? AND deleted=0", (ref,)).fetchone()
    if r:
        return r
    refs = nr.parse_refs(ref, vx, follow_ons=False)
    if len(refs) != 1 or refs[0].verse_id is None:
        raise Refused(f"{ref!r} is not one verse")
    return conn.execute("SELECT id, osisId, reference FROM verse WHERE id=?", (refs[0].verse_id,)).fetchone()
```

**What it does.** A verse given as osisId or as written (`Gen 6:5`); refuses anything that is not one verse.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `verse`

#### G21 — strandreading._quote_check

`iba/app/lib/strandreading.py:112-116`

```python
def _quote_check(conn, cfg, texts: list[str], where: str) -> list[str]:
    corpus = quotecheck.Corpus(conn)
    _, bad = quotecheck.check_lines(corpus, [t for x in texts if x for t in x.split("\n")],
                                    int(cfg.required_setting("narrative.quote_min_words")), quotecheck.titles(conn))
    return [f"{where}: \"{b}\"" for b in bad]
```

**What it does.** Builds the ESV corpus (`quotecheck.Corpus`), reads `narrative.quote_min_words` and returns the quoted parts of the given texts that are not found in the ESV.

**Config read by this element (found in its code).** setting: `narrative.quote_min_words`

**Data (found in its code).** none directly.

#### G22 — quotecheck.Corpus

`iba/app/lib/quotecheck.py:25-37`

```python
class Corpus:
    """The ESV text, normalised and joined in canonical order. Build once per run."""

    def __init__(self, conn):
        order = {b: o for b, o in conn.execute("SELECT book, ordinal FROM cfg_book_order")}
        rows = []
        for osis, text in conn.execute("SELECT osisId, text FROM verse WHERE deleted=0"):
            b, ch, v = osis.rsplit(".", 2)
            rows.append((order.get(b, 999), int(ch), int(v), norm(text or "")))
        self.text = " " + " ".join(r[3] for r in sorted(rows)) + " "

    def has(self, part: str) -> bool:
        return f" {norm(part)} " in self.text
```

**What it does.** The ESV text of every live verse, normalised and joined in canonical order (`cfg_book_order`).

**Config read by this element (found in its code).** config tables named: `cfg_book_order`

**Data (found in its code).** reads data table(s) `verse`

#### G22b — quotecheck.norm and pattern

`iba/app/lib/quotecheck.py:21-22`

```python
def norm(s: str) -> str:
    return re.sub(r"\s+", " ", _NORM_RX.sub(" ", s or "")).strip().lower()
```

**What it does.** Strips quote marks and punctuation, collapses spaces, lower-cases.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The punctuation set.

#### G22c — quotecheck.parts_of

`iba/app/lib/quotecheck.py:43-60`

```python
def parts_of(line: str, min_words: int, skip: set[str] | None = None) -> list[str]:
    """The quoted parts of one line. Quote marks are paired in order (so a short quote such as
    "I" does not shift the pairing). Not checked: a gloss (a quote straight after an italic
    transliteration, *nephesh* ("soul") or *lun*, "to grumble"), a quote that is a section or
    chapter title (`skip`, normalised), and parts under min_words words."""
    out = []
    pos = [i for i, ch in enumerate(line) if ch == '"']
    for a, b in zip(pos[0::2], pos[1::2]):
        q = line[a + 1:b]
        if _GLOSS_RX.search(line[max(0, a - 60):a]):
            continue
        if skip and norm(q) in skip:
            continue
        for p in _ELLIPSIS_RX.split(q):
            p = re.sub(r"\[[^\]]*\]", " ", p)
            if len(norm(p).split()) >= min_words:
                out.append(p.strip())
    return out
```

**What it does.** The quoted parts of one line (paired double quotes), not a gloss, not a title, at least `min_words` words.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G22d — quotecheck.titles

`iba/app/lib/quotecheck.py:63-66`

```python
def titles(conn) -> set[str]:
    """Section headings and chapter titles, normalised: a quote of one is not a verse quote."""
    t = {norm(h) for (h,) in conn.execute("SELECT heading FROM narrative_section")}
    return t | {norm(x) for (x,) in conn.execute("SELECT title FROM narrative_chapter")}
```

**What it does.** Section headings and chapter titles (not verse quotes).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `narrative_chapter`, `narrative_section`

#### G22e — quotecheck.check_lines

`iba/app/lib/quotecheck.py:78-87`

```python
def check_lines(corpus: Corpus, lines: list[str], min_words: int,
                skip: set[str] | None = None) -> tuple[int, list[str]]:
    """(parts checked, failing parts)."""
    n, bad = 0, []
    for line in lines:
        for p in parts_of(line, min_words, skip):
            n += 1
            if not corpus.has(p):
                bad.append(p)
    return n, bad
```

**What it does.** The quoted parts that are not in the corpus.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G22f — quotecheck constants

`iba/app/lib/quotecheck.py:17-17`, `iba/app/lib/quotecheck.py:18-18`, `iba/app/lib/quotecheck.py:40-40`

```python
_NORM_RX = re.compile(r"[“”‘’\"'—–,;:.!?()\[\]*_-]")

_ELLIPSIS_RX = re.compile(r"\s*(?:…|\.\.\.)\s*")

_GLOSS_RX = re.compile(r'\*[^*\n]+\*\*?\s*[,(:]?\s*$')
```

**What it does.** The patterns.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### G23 — openitem.spec_from

`iba/app/lib/openitem.py:44-51`

```python
def spec_from(params: dict) -> dict:
    """PS parameters (any case) or a request-file object as one item spec."""
    p = {k.lower(): v for k, v in params.items()}
    return {"thread": p.get("thread"), "item": p.get("item"), "origin": p.get("origin"), "anchor": p.get("anchor"),
            "source": _list(p.get("source")), "target_cluster": (p.get("targetcluster") or p.get("target_cluster") or "").strip() or None,
            "target_terms": _list(p.get("targetterms") or p.get("target_terms")), "verse": p.get("verse"),
            "read_for": (p.get("readfor") or p.get("read_for") or "").strip(), "why": (p.get("why") or "").strip(),
            "comes_back_when": (p.get("comesbackwhen") or p.get("comes_back_when") or "").strip()}
```

**What it does.** Turns parameters or a request object into one item spec.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `verse`

#### G23b — openitem._list

`iba/app/lib/openitem.py:36-41`

```python
def _list(v) -> list[str]:
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip() for x in str(v).split(",") if x.strip()]
```

**What it does.** A comma list as trimmed items.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G24 — openitem._validate

`iba/app/lib/openitem.py:171-180`

```python
def _validate(cfg, spec: dict, r: vs.Resolver) -> tuple[str, int]:
    for f in TEXT_FIELDS:
        if len(spec.get(f) or "") < 15:
            raise ItemError(f"-{ {'read_for': 'ReadFor', 'why': 'Why', 'comes_back_when': 'ComesBackWhen'}[f] } is "
                            f"required and states it in words (an item without a clear purpose is refused)")
    origin = str(spec.get("origin") or "").lstrip("#")
    if not origin.isdigit() or not cfg.conn.execute("SELECT 1 FROM escalation WHERE id=? AND type IN ('task','issue')",
                                                    (int(origin),)).fetchone():
        raise ItemError(f"-Origin {spec.get('origin')!r} must be the task or issue of the analysis that raises the item")
    return _check_anchor(cfg, r, spec.get("anchor")), int(origin)
```

**What it does.** Each of read_for, why, comes_back_when must be 15 characters or more; the origin must be an existing task or issue; the anchor is checked (G25).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`

**Fixed in the code, not config.** The 15-character minimum.

#### G25 — openitem._check_anchor

`iba/app/lib/openitem.py:81-104`

```python
def _check_anchor(cfg, r: vs.Resolver, anchor: str) -> str:
    kind, _, value = (anchor or "").partition(":")
    kind, value = kind.strip().lower(), value.strip()
    if kind not in ANCHOR_KINDS or not value:
        raise ItemError(f"-Anchor {anchor!r} must be one of {', '.join(k + ':<value>' for k in ANCHOR_KINDS)}")
    conn = cfg.conn
    if kind == "strong":
        value = ",".join(r.decompose(value))
    elif kind == "verse":
        if not [x for x in vs.nr.parse_refs(value, r.vx) if x.verse_id]:
            raise ItemError(f"-Anchor verse {value!r} does not resolve to a verse")
    elif kind == "observation":
        if not conn.execute("SELECT 1 FROM ib_observation WHERE id=?", (value,)).fetchone():
            raise ItemError(f"-Anchor observation {value} does not exist")
    elif kind == "claim":
        if not conn.execute("SELECT 1 FROM narrative_claim WHERE claim_ref=?", (value,)).fetchone():
            raise ItemError(f"-Anchor claim {value} is not in the register")
    else:
        ch, _, head = value.partition("/")
        try:
            r.chapter(ch.strip(), head.strip() or None)
        except vs.ScopeError as exc:
            raise ItemError(f"-Anchor block {value!r}: {exc}") from exc
    return f"{kind}:{value}"
```

**What it does.** Checks the anchor kind (strong, verse, observation, claim, block) resolves.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `ib_observation`, `narrative_claim`

**Fixed in the code, not config.** ANCHOR_KINDS.

#### G26 — openitem.resolve_target

`iba/app/lib/openitem.py:107-168`

```python
def resolve_target(cfg, spec: dict) -> dict:
    """The item's target: verse ids and how they were found. Refused when it does not resolve, holds no verse,
    or is wider than open_item.max_verses."""
    r = vs.Resolver(cfg)
    limit = int(cfg.required_setting("open_item.max_verses"))
    conn = cfg.conn
    with_terms = bool(spec.get("target_cluster") or spec.get("target_terms"))
    if spec.get("verse") and with_terms and not (spec.get("source") and spec.get("target_cluster") and spec.get("target_terms")):
        raise ItemError("-Verse with a cluster target needs all of -Source, -TargetCluster and -TargetTerms")
    if spec.get("verse"):
        try:
            r.verse(str(spec["verse"]))
        except vs.ScopeError as exc:
            raise ItemError(str(exc)) from exc
        verses, label = sorted(r.routes), str(spec["verse"]).strip()
        if len(label) > 60:                # a long list is labelled by its first reference and its size
            label = f"{re.split(r'[;,]', label)[0].strip()} and {len(verses) - 1} more verses"
        out = {"source_terms": None, "target_cluster": None, "target_terms": None}
        if with_terms:     # a purpose's own verses, read for its source and target terms (#2236)
            try:
                src, tgt = r._expand_codes(spec["source"]), r._expand_codes(spec["target_terms"])
            except vs.ScopeError as exc:
                raise ItemError(str(exc)) from exc
            cl = spec["target_cluster"]
            members = {x[0] for x in conn.execute("SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0", (cl,))}
            outside = [t for t in tgt if t not in members]
            if not members or outside:
                raise ItemError(f"-TargetCluster {cl!r} is not a live cluster" if not members
                                else f"target term(s) {outside} are not in cluster {cl}")
            short = lambda xs: "+".join(xs[:3]) + ("+..." if len(xs) > 3 else "")  # noqa: E731
            label = f"{cl}: {short(src)} x {short(tgt)} ({len(verses)} verses)"
            out = {"source_terms": ",".join(src), "target_cluster": cl, "target_terms": ",".join(tgt)}
    else:
        if not (spec.get("source") and spec.get("target_cluster") and spec.get("target_terms")):
            raise ItemError("a cluster item needs -Source (the source analysis's strong), -TargetCluster and "
                            "-TargetTerms (the related term(s) in that cluster); or give -Verse")
        try:
            src = r._expand_codes(spec["source"])
            tgt = r._expand_codes(spec["target_terms"])
        except vs.ScopeError as exc:
            raise ItemError(str(exc)) from exc
        cl = spec["target_cluster"]
        members = {x[0] for x in conn.execute("SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0",
                                              (cl,))}
        if not members:
            raise ItemError(f"-TargetCluster {cl!r} is not a live cluster")
        outside = [t for t in tgt if t not in members]
        if outside:
            raise ItemError(f"target term(s) {outside} are not in cluster {cl}")
        verses = sorted({x[0] for x in conn.execute(
            "SELECT DISTINCT a.verse_id FROM verse_lexical a JOIN verse_lexical b ON b.verse_id=a.verse_id AND b.deleted=0 "
            "AND b.strong IN (SELECT value FROM json_each(?)) WHERE a.deleted=0 AND a.strong IN (SELECT value FROM json_each(?))",
            (json.dumps(tgt), json.dumps(src)))})
        label = f"{cl}: {'+'.join(src)} x {'+'.join(tgt)}"
        out = {"source_terms": ",".join(src), "target_cluster": cl, "target_terms": ",".join(tgt)}
    if not verses:
        raise ItemError(f"the target {label!r} holds no verse" + ("" if spec.get("verse") else
                        " (the source and target terms never stand in the same verse)"))
    if len(verses) > limit:
        raise ItemError(f"the target {label!r} holds {len(verses)} verses, over open_item.max_verses {limit}: "
                        f"split it into separate items, one purpose each")
    return {**out, "verses": verses, "label": label}
```

**What it does.** Reads setting `open_item.max_verses` (200). Resolves the item's target: either a verse list (optionally with source, target cluster and target terms) or a cluster item (verses where a source Strong and a target term share a verse); refuses a target with no verse or past the limit.

**Config read by this element (found in its code).** setting: `open_item.max_verses`

**Data (found in its code).** reads data table(s) `cluster_strong`, `verse`, `verse_lexical`

**Fixed in the code, not config.** The rules of the two target shapes.

#### G27 — openitem.add

`iba/app/lib/openitem.py:205-221`

```python
def add(cfg, db, w, spec: dict, who: str) -> str:
    conn = cfg.conn
    t = _thread(conn, spec.get("thread"))
    r = vs.Resolver(cfg)
    anchor, origin = _validate(cfg, spec, r)
    tgt = resolve_target(cfg, spec)
    if _duplicate(conn, t["id"], tgt["label"], spec["read_for"]):
        raise ItemError(f"{t['alias']} already has an open item on {tgt['label']!r} reading for the same thing")
    if conn.execute("SELECT 1 FROM escalation_thread_item WHERE escalation_id=? AND kind='scope' AND value=? COLLATE NOCASE",
                    (t["id"], tgt["label"])).fetchone():
        tgt["label"] = f"{tgt['label']} ({spec['read_for'][:40]})"     # same target, another purpose
    escalation.update(cfg, db, t["id"], originator=who, add_items=[("scope", tgt["label"], spec["read_for"])],
                      via=origin)
    it = conn.execute("SELECT id, item_no FROM escalation_thread_item WHERE escalation_id=? AND kind='scope' AND value=?",
                      (t["id"], tgt["label"])).fetchone()
    _write_worded(w, conn, it["id"], spec, anchor, origin, tgt)
    return f"{t['alias']}.{it['item_no']} added: {_shown(tgt)}"
```

**What it does.** Finds the open thread, validates the spec, resolves the target, refuses a duplicate, and adds the item with `escalation.update(add_items=...)` (G33), then writes the worded fields and the target verses (`escalation_thread_item`, `escalation_thread_item_verse`) through the Writer.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** G26 (setting open_item.max_verses); G33 (enum escalation_assignee); G34 (enum escalation_next_action_manual); G35 (enum escalation_thread_item_kind); G36 (enum escalation_thread_item_response_kind, enum escalation_thread_item_status); G37 (enum escalation_thread_item_kind); G45 (enum escalation_state)

**Data (found in its code).** reads data table(s) `escalation_thread_item`

**Fixed in the code, not config.** The label suffix rule for a same-target item.

#### G27b — openitem._thread

`iba/app/lib/openitem.py:54-64`

```python
def _thread(conn, ref: str):
    m = re.fullmatch(r"OT-0*(\d+)", (ref or "").strip(), re.I)
    if not m:
        raise ItemError(f"-Thread {ref!r} is not a thread (OT-nn)")
    row = conn.execute("SELECT * FROM escalation WHERE type='thread' AND CAST(substr(alias, 4) AS INTEGER)=?",
                       (int(m.group(1)),)).fetchone()
    if row is None:
        raise ItemError(f"thread {ref!r} does not exist")
    if row["state"] not in ("on-hold", "in-progress"):
        raise ItemError(f"thread {row['alias']} is {row['state']}; an item goes on an open thread")
    return row
```

**What it does.** The open thread (on-hold or in-progress) for `OT-nn`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`

**Fixed in the code, not config.** The two states.

#### G27c — openitem._duplicate

`iba/app/lib/openitem.py:199-202`

```python
def _duplicate(conn, thread_id: int, label: str, read_for: str, skip: int | None = None):
    return conn.execute("SELECT item_no FROM escalation_thread_item WHERE escalation_id=? AND status='open' AND "
                        "kind='scope' AND value=? AND read_for=? AND id<>?",
                        (thread_id, label, read_for, skip or -1)).fetchone()
```

**What it does.** An open worded item with the same target and purpose.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation_thread_item`

#### G27d — openitem._shown

`iba/app/lib/openitem.py:194-196`

```python
def _shown(tgt: dict) -> str:
    n = f"({len(tgt['verses'])} verses)"
    return tgt["label"] if tgt["label"].endswith(n) else f"{tgt['label']} {n}"
```

**What it does.** Label with verse count.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G27e — openitem._write_worded

`iba/app/lib/openitem.py:183-191`

```python
def _write_worded(w, conn, item_id: int, spec: dict, anchor: str, origin: int, tgt: dict) -> None:
    w.update("escalation_thread_item", {"id": item_id}, {
        "kind": "scope", "value": tgt["label"], "note": spec["read_for"], "origin_escalation_id": origin,
        "anchor": anchor, "source_terms": tgt["source_terms"], "target_cluster": tgt["target_cluster"],
        "target_terms": tgt["target_terms"], "read_for": spec["read_for"], "why": spec["why"],
        "comes_back_when": spec["comes_back_when"], "target_verses": len(tgt["verses"]), "worded_at": _now()})
    w.update("escalation_thread_item_verse", {"item_id": item_id, "deleted": 0}, {"deleted": 1})
    for vid in tgt["verses"]:
        w.insert("escalation_thread_item_verse", {"item_id": item_id, "verse_id": vid})
```

**What it does.** Writes the worded fields and replaces the item's target verses.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** writes `escalation_thread_item`, `escalation_thread_item_verse`

#### G27f — openitem._now / constants / ItemError

`iba/app/lib/openitem.py:32-33`

```python
def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

**What it does.** UTC timestamp.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G27g — openitem constants

`iba/app/lib/openitem.py:25-25`

```python
TEXT_FIELDS = ("read_for", "why", "comes_back_when")
```

**What it does.** The three purpose fields.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G27h — openitem.ItemError

`iba/app/lib/openitem.py:28-29`

```python
class ItemError(ValueError):
    """An item that cannot be registered as given."""
```

**What it does.** The error.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G30 — escalation.update (thread path: touched response, added item)

`iba/app/lib/escalation.py:1167-1329`

```python
def update(cfg: Cfg, db: Db, escalation_id: int, *, next_action: str | None = None,
          next_action_assigned_to: str | None = None, comment: str | None = None,
          context: str | None = None, tried: str | None = None, resolution: str | None = None,
          state: str | None = None, needs_followup: bool | None = None, originator: str,
          comes_back_when: str | None = None,
          add_items: list[tuple[str, str, str | None]] | None = None,
          item_refs: list[str] | None = None, respond: str | None = None,
          response_kind: str | None = None, via=None, files: list | None = None,
          superseded_by=None) -> str:
    """Update -- every later change to a MANUAL item. `originator` is required.

    `needs_followup`: None carries the current flag forward; True/False sets or clears it.

    A dispatcher-tied item is refused unless it is decision_required, which always uses the manual
    ready_for_approval/approved vocabulary. A dispatcher-tied self_correctable item closes through
    resolve_self_correctable() / escalate_to_decision().

    Threads: `item_refs` + `response_kind` + `respond` (+ `via`, `files`) record one response per
    named item; `closed`/`withdrawn`/`superseded` settle an item, `reopened` opens it, and `forward`
    needs at least one `add_items` entry. `add_items` alone adds items. Each such Update writes the
    responses in full into the thread's history. The thread's state follows the priority-0 transition
    rows; completed/closed is refused while any item is open (T6), and when the last item settles
    the thread completes with a generated resolution. Withdrawing a thread withdraws its open items;
    superseding (`superseded_by` OT-nn) moves them to the successor. After any change to a task or
    issue, every thread referencing it is brought into line (`_sync_threads_for`)."""
    cur = _current(db, escalation_id)
    if not cur["run_id"].startswith("MANUAL-") and cur["resolution_kind"] != "decision_required":
        return (f"escalation #{escalation_id} is dispatcher-tied (run_id {cur['run_id']!r}), not "
               f"manual -- answer it via AnswerRun, not Update")
    if cur["state"] not in live_states(db):
        return f"escalation #{escalation_id} is not open (state={cur['state']!r})"

    who = _check_assignee(db, originator)
    checked_action = _check_next_action_manual(db, next_action)
    new_resolution = resolution if resolution is not None else cur["resolution"]
    resolved_assignee = _check_assignee(db, next_action_assigned_to, required=False) or cur["next_action_assigned_to"]
    resolved_needs_followup = (int(needs_followup) if needs_followup is not None
                               else cur["needs_claude_followup"])

    # An approval that still needs follow-up goes back to Claude, overriding any -AssignedTo.
    if checked_action == "approved" and resolved_needs_followup:
        resolved_assignee = "Claude"

    # D25: approval is an authority check -- only the party ready_for_approval assigned the item to
    # may approve or note a decision_required item (#851 for noted). self_correctable items close
    # through resolve_self_correctable().
    if checked_action in ("approved", "noted") and cur["resolution_kind"] == "decision_required":
        rfa_assigned_to = _last_next_action_assigned_to(db, escalation_id, "ready_for_approval")
        if rfa_assigned_to and who != rfa_assigned_to:
            return (f"escalation #{escalation_id}: {who} cannot set {checked_action!r} -- "
                   f"'ready_for_approval' assigned this to {rfa_assigned_to!r}; only "
                   f"{rfa_assigned_to} may close it (authority check, not identity -- D25).")

    if checked_action == "ready_for_approval":
        _check_requirements(db, "ready_for_approval", originator=who, checked_action=checked_action,
                            values={"resolution": new_resolution,
                                    "next_action_assigned_to": resolved_assignee},
                            self_id=escalation_id)
    if checked_action == "approved":
        _check_requirements(db, "approved", originator=who, checked_action=checked_action,
                            values={"resolution": new_resolution}, self_id=escalation_id)
    if checked_action == "noted":
        _check_requirements(db, "noted", originator=who, checked_action=checked_action,
                            values={}, self_id=escalation_id)
    if checked_action == "reject":
        _check_requirements(db, "reject", originator=who, checked_action=checked_action,
                            values={"state": state, "type": cur["type"],
                                    "superseded_by": superseded_by})
    if checked_action == "revise":
        _check_requirements(db, "revise", originator=who, checked_action=checked_action,
                            values={"tried": tried})

    # thread items and responses: written before the state is derived, in the same transaction,
    # so the transition rows and the T6 check see this call's changes.
    is_thread = cur["type"] == "thread"
    thread_facts, item_summary = None, []
    succ_lines: list[str] = []          # what a supersede did on the successor thread
    if (add_items or item_refs or respond or response_kind or superseded_by) and not is_thread:
        raise ValueError("-Item/-AddItem/-Respond/-ResponseKind/-SupersededBy are for type thread "
                         "only")
    if superseded_by and not (checked_action == "reject" and state == "supersede"):
        raise ValueError("-SupersededBy goes with -NextAction reject -State supersede")
    if is_thread:
        if (item_refs or respond or response_kind) and not (item_refs and respond and response_kind):
            raise ValueError("an item response needs all three: -Item, -ResponseKind and -Respond "
                             "(a response about the whole thread is a plain -Comment)")
        if response_kind == "forward" and not add_items:
            raise ValueError("a forward response adds the forward mark as a new item: give "
                             "-AddItem kind:value (e.g. cluster:M03) with it")
        via_id = resolve_id(db, via) if via is not None else None
        now = _now()
        targets = [_resolve_item(db, cur, r) for r in item_refs or []]
        for it in targets:
            _respond(cfg, db, it, response_kind, respond, via=via_id, by=who, files=files, at=now)
            item_summary.append(f"item {it['item_no']} ({it['kind']}:{it['value']}) "
                                f"{response_kind}")
        for kind, value, note in add_items or []:
            new_item = _add_item(cfg, db, escalation_id, kind, value, note, opened_by=via_id, at=now)
            item_summary.append(f"item {new_item['item_no']} {kind}:{value} added")
        if checked_action == "reject":
            item_summary += _settle_thread_on_reject(cfg, db, cur, state, superseded_by,
                                                     reason=comment, who=who, at=now,
                                                     succ_lines=succ_lines)
        changed = bool(add_items) or response_kind in _SETTLE_KINDS + ("reopened",)
        thread_facts = _thread_facts(db, escalation_id, items_changed=changed,
                                     closed_some=response_kind in _SETTLE_KINDS)
        if item_summary:
            # the response itself, in full, to history
            line = (f"{cur['alias'] or '#' + str(escalation_id)}: " + "; ".join(item_summary)
                    + (f" (via #{via_id})" if via_id else ""))
            if respond:
                line += f" -- {response_kind} by {who}: {respond}"
                if files:
                    line += f" [files: {', '.join(files)}]"
            comment = f"{comment}\n{line}" if comment else line

    assignee_changed = bool(next_action_assigned_to) and next_action_assigned_to != cur["next_action_assigned_to"]
    new_state = _evaluate_transition(db, "manual", checked_action, has_resolution=bool(new_resolution),
                                     assignee_changed=assignee_changed, explicit_state=state,
                                     cur_state=cur["state"], needs_followup=bool(resolved_needs_followup),
                                     cur_next_action=cur["next_action"], thread=thread_facts)

    if (is_thread and new_state == "completed" and thread_facts and thread_facts["all_settled"]
            and not new_resolution):                        # last item settled
        resolution = new_resolution = _thread_completion_resolution(db, cur)

    # D26: comment/context/tried cannot land on a `raised` item (check_kind not_raised_with_content)
    _check_requirements(db, "update", originator=who, checked_action=checked_action,
                        values={"state": new_state, "comment": comment, "context": context,
                               "tried": tried, "next_action": next_action,
                               "next_action_assigned_to": resolved_assignee,
                               "type": cur["type"]},
                        self_id=escalation_id)

    merged = _snapshot(cfg, db, escalation_id,
                       deltas={"comment": comment, "context": context, "tried": tried,
                              "resolution": resolution, "comes_back_when": comes_back_when},
                       envelope={
                           "next_action": checked_action if checked_action is not None else cur["next_action"],
                           "next_action_assigned_to": resolved_assignee,
                           "state": _check_state(db, new_state),
                           "resolution_kind": cur["resolution_kind"],
                           "needs_claude_followup": resolved_needs_followup},
                       originator=who)
    msg = (f"escalation #{escalation_id} v{merged['version']} -> "
           f"state={new_state!r}, next_action={merged['next_action']!r}, "
           f"assigned_to={merged['next_action_assigned_to']!r}")
    if item_summary:
        msg += "\n  " + "; ".join(item_summary)
    if not is_thread:
        synced = _sync_threads_for(cfg, db, escalation_id, who=who)
        if synced:
            msg += "\n  threads: " + "; ".join(synced)
    elif superseded_by:
        succ = _current(db, resolve_id(db, superseded_by))
        st = _restate_thread(cfg, db, succ["id"],
                             f"{succ['alias']}: received the open items of "
                             f"{cur['alias'] or '#' + str(escalation_id)}, superseded by {who}: "
                             f"{comment}"
                             + (f"\n{succ['alias']}: " + "; ".join(succ_lines) if succ_lines
                                else ""), who=who, closed_some=False)
        msg += f"\n  successor {succ['alias']} (#{succ['id']}) -> {st}"
    return msg
```

**What it does.** Gather reaches this only to record a `touched` response on a thread item (an open_item `response`) or, through `openitem.add`, to add an item. In both the target is a thread, `next_action` is not given, and these lines run: load the current row (`_current`); refuse if the thread is not live (`live_states`: `cfg_enum` escalation_state_open/parked); check the originator (`escalation_assignee` enum); for a response, resolve the item (`_resolve_item`), write the response row (`_respond`, enums `escalation_thread_item_response_kind` and `escalation_thread_item_status`), add items (`_add_item`, enum `escalation_thread_item_kind`); derive the thread facts (`_thread_facts`) and the new state from `cfg_escalation_transition` (`_evaluate_transition`, `cfg_status_flow`); run the `update` requirements from `cfg_escalation_requirement` (`_check_requirements`); write a new history version (`_snapshot`). The branches for approval, reject, supersede, `_sync_threads_for` and `_restate_thread` are not reached on this path. The escalation module writes under the writer `escalation` (`cfg_write_grant`).

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** G33 (enum escalation_assignee); G34 (enum escalation_next_action_manual); G35 (enum escalation_thread_item_kind); G36 (enum escalation_thread_item_response_kind, enum escalation_thread_item_status); G37 (enum escalation_thread_item_kind); G45 (enum escalation_state)

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The condition vocabulary of the transition and requirement engines (fixed in code; which rule uses it is config).

#### G31 — escalation.live_states / state_group

`iba/app/lib/escalation.py:74-76`

```python
def live_states(db) -> tuple[str, ...]:
    """Not yet closed: open + parked."""
    return state_group(db, "open") + state_group(db, "parked")
```

**What it does.** Open plus parked states from `cfg_enum`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G31b — escalation.state_group

`iba/app/lib/escalation.py:63-71`

```python
def state_group(db, group: str) -> tuple[str, ...]:
    """The states in one group ('open' | 'parked' | 'terminal'), from cfg_enum. `db` is a Db or a
    sqlite3 connection. Missing config is an error, never a silent default."""
    conn = getattr(db, "conn", db)
    rows = conn.execute(_STATE_GROUP_SQL[group]).fetchall()
    if not rows:
        raise RuntimeError(f"cfg_enum {_STATE_GROUP_ENUM[group]!r} has no active values -- the "
                           f"escalation state groups are config (#2173 G1)")
    return tuple(r[0] for r in rows)
```

**What it does.** One group from `cfg_enum` escalation_state_open/_parked/_terminal; refuses if empty.

**Config read by this element (found in its code).** config tables named: `cfg_enum`

**Data (found in its code).** none directly.

#### G31c — escalation state-group constants

`iba/app/lib/escalation.py:53-54`, `iba/app/lib/escalation.py:55-59`, `iba/app/lib/escalation.py:80-81`, `iba/app/lib/escalation.py:82-82`, `iba/app/lib/escalation.py:83-83`, `iba/app/lib/escalation.py:84-84`, `iba/app/lib/escalation.py:85-85`

```python
_STATE_GROUP_ENUM = {"open": "escalation_state_open", "parked": "escalation_state_parked",
                     "terminal": "escalation_state_terminal"}

_STATE_GROUP_SQL = {   # literal names, so configmaint's orphan check sees each group's reader
    "open": "SELECT value FROM cfg_enum WHERE name='escalation_state_open' AND inactive=0 ORDER BY ordinal",
    "parked": "SELECT value FROM cfg_enum WHERE name='escalation_state_parked' AND inactive=0 ORDER BY ordinal",
    "terminal": "SELECT value FROM cfg_enum WHERE name='escalation_state_terminal' AND inactive=0 ORDER BY ordinal",
}

_ENVELOPE_COLS = ("state", "next_action", "next_action_assigned_to", "originator", "answered_at",
                 "resolution_kind", "needs_claude_followup")

_APPEND_COLS = ("comment", "context")            # escalation: cumulative. history: raw increment.

_REPLACE_COLS = ("resolution", "tried", "short_description", "comes_back_when")

_IMMUTABLE_COLS = ("run_id", "source", "at_step", "type", "raised_at", "alias")

_COLS = _ENVELOPE_COLS + _APPEND_COLS + _REPLACE_COLS + _IMMUTABLE_COLS
```

**What it does.** Names of the enums and the escalation columns.

**Config read by this element (found in its code).** config tables named: `cfg_enum`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### G32 — escalation._current

`iba/app/lib/escalation.py:379-383`

```python
def _current(db: Db, escalation_id: int) -> dict:
    rows = db.rows("SELECT * FROM escalation WHERE id=?", (escalation_id,))
    if not rows:
        raise ValueError(f"no escalation #{escalation_id}")
    return dict(rows[0])
```

**What it does.** The escalation row.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`

#### G33 — escalation._check_assignee

`iba/app/lib/escalation.py:142-153`

```python
def _check_assignee(db: Db, who: str | None, required: bool = True) -> str | None:
    if who is None:
        if required:
            raise ValueError("originator is required — must be 'Claude' or 'Researcher'. No "
                             "default (escalation rebuild 2026-08-20): a silent 'Researcher' "
                             "default previously misattributed >=39 history rows in one session.")
        return None
    normalised = who.strip().capitalize()
    valid = db.cfg.enum("escalation_assignee")
    if normalised not in valid:
        raise ValueError(f"{who!r} is not a member of cfg_enum 'escalation_assignee' ({valid!r})")
    return normalised
```

**What it does.** The originator must be a value of enum `escalation_assignee`.

**Config read by this element (found in its code).** enum: `escalation_assignee`; config tables named: `cfg_enum`

**Data (found in its code).** none directly.

#### G34 — escalation._check_next_action_manual

`iba/app/lib/escalation.py:124-131`

```python
def _check_next_action_manual(db: Db, next_action: str | None) -> str | None:
    if next_action is None:
        return None
    valid = db.cfg.enum("escalation_next_action_manual")
    if next_action not in valid:
        raise ValueError(f"{next_action!r} is not a member of cfg_enum "
                         f"'escalation_next_action_manual' ({valid!r})")
    return next_action
```

**What it does.** Not reached with a value on this path (None returns None).

**Config read by this element (found in its code).** enum: `escalation_next_action_manual`; config tables named: `cfg_enum`

**Data (found in its code).** none directly.

#### G35 — escalation._resolve_item

`iba/app/lib/escalation.py:527-549`

```python
def _resolve_item(db: Db, thread: dict, ref: str):
    """An item of `thread` from `ref`: 'OT-16.1' (alias must be this thread's), '1' (the item
    number), 'kind:value', or the value alone (unique within the thread)."""
    s = ref.strip()
    alias = thread["alias"] or ""
    if alias and s.upper().startswith(alias.upper() + "."):
        s = s[len(alias) + 1:]
    elif s.upper().startswith("OT-") and "." in s:
        raise ValueError(f"item {ref!r} does not belong to {alias or '#' + str(thread['id'])}")
    if s.isdigit():
        rows = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                       (thread["id"], int(s)))
    elif ":" in s and s.split(":", 1)[0].lower() in db.cfg.enum("escalation_thread_item_kind"):
        kind, value = s.split(":", 1)
        rows = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND kind=? "
                       "AND value=? COLLATE NOCASE", (thread["id"], kind.lower(), value.strip()))
    else:
        rows = db.rows("SELECT * FROM escalation_thread_item WHERE escalation_id=? AND "
                       "value=? COLLATE NOCASE", (thread["id"], s))
    if len(rows) != 1:
        raise ValueError(f"item {ref!r} on {alias or '#' + str(thread['id'])}: "
                         f"{'not found' if not rows else 'ambiguous -- use the item number'}")
    return dict(rows[0])
```

**What it does.** An item of the thread from `OT-nn.n`, a number, `kind:value` or a value.

**Config read by this element (found in its code).** enum: `escalation_thread_item_kind`

**Data (found in its code).** reads data table(s) `escalation_thread_item`

#### G36 — escalation._respond

`iba/app/lib/escalation.py:556-591`

```python
def _respond(cfg: Cfg, db: Db, item: dict, kind: str, text: str, *, via: int | None, by: str,
             files: list | None, at: str) -> None:
    """One response row. A settling kind (closed, withdrawn, superseded) needs an open item and
    sets its status to that kind; 'reopened' opens a settled item again. 'superseded' must name
    what carries the item on (OT-nn, OT-nn.n or #nnnn) in its text."""
    _grant(cfg, "escalation_thread_item_response")
    if kind not in db.cfg.enum("escalation_thread_item_response_kind"):
        raise ValueError(f"{kind!r} is not a member of cfg_enum "
                         f"'escalation_thread_item_response_kind' "
                         f"({db.cfg.enum('escalation_thread_item_response_kind')!r})")
    if not text:
        raise ValueError("a response needs its text (-Respond); a researcher's response is quoted "
                         "verbatim (cfg_escalation 5)")
    statuses = db.cfg.enum("escalation_thread_item_status")   # open/closed/withdrawn/superseded
    if item["status"] not in statuses:
        raise ValueError(f"item {item['item_no']} has status {item['status']!r}, not a member of "
                         f"cfg_enum 'escalation_thread_item_status' ({statuses!r})")
    if kind in _SETTLE_KINDS:
        if item["status"] != "open":
            raise ValueError(f"item {item['item_no']} ({item['kind']}:{item['value']}) is already "
                             f"{item['status']} -- reopen it first")
        if kind == "superseded" and not _SUCCESSOR_RE.search(text):
            raise ValueError("a superseded response names what carries the item on (OT-nn, "
                             "OT-nn.n or #nnnn) in -Respond")
        db.update("escalation_thread_item", {"id": item["id"]}, status=kind)
        item["status"] = kind
    elif kind == "reopened":
        if item["status"] == "open":
            raise ValueError(f"item {item['item_no']} ({item['kind']}:{item['value']}) is already "
                             f"open")
        db.update("escalation_thread_item", {"id": item["id"]}, status="open")
        item["status"] = "open"
    db.write("escalation_thread_item_response", {
        "item_id": item["id"], "escalation_id": item["escalation_id"], "kind": kind, "text": text,
        "via_escalation": via, "responded_by": by, "responded_at": at,
        "files": json.dumps(files, ensure_ascii=False) if files else None})
```

**What it does.** One response row; checks the kind and status against enums; a settling kind changes the item's status (not used for `touched`).

**Config read by this element (found in its code).** enum: `escalation_thread_item_response_kind`, `escalation_thread_item_status`; config tables named: `cfg_enum`, `cfg_escalation`

**Data (found in its code).** writes `escalation_thread_item`, `escalation_thread_item_response`

**Fixed in the code, not config.** The settle kinds.

#### G36b — escalation: settle kinds

`iba/app/lib/escalation.py:552-552`, `iba/app/lib/escalation.py:553-553`

```python
_SETTLE_KINDS = ("closed", "withdrawn", "superseded")   # response kinds that settle an item

_SUCCESSOR_RE = re.compile(r"\bOT-\d+(?:\.\d+)?\b|#\d+")
```

**What it does.** closed, withdrawn, superseded; the successor pattern.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### G37 — escalation._add_item

`iba/app/lib/escalation.py:505-524`

```python
def _add_item(cfg: Cfg, db: Db, escalation_id: int, kind: str, value: str, note: str | None,
              *, opened_by: int | None, at: str) -> dict:
    _grant(cfg, "escalation_thread_item")
    if kind not in db.cfg.enum("escalation_thread_item_kind"):
        raise ValueError(f"{kind!r} is not a member of cfg_enum 'escalation_thread_item_kind' "
                         f"({db.cfg.enum('escalation_thread_item_kind')!r})")
    if not value:
        raise ValueError("an item needs a value (kind:value)")
    dup = db.rows("SELECT item_no, status FROM escalation_thread_item WHERE escalation_id=? AND "
                  "kind=? AND value=? COLLATE NOCASE", (escalation_id, kind, value))
    if dup:
        raise ValueError(f"item {kind}:{value} already exists on #{escalation_id} as item "
                         f"{dup[0]['item_no']} ({dup[0]['status']}) -- respond to it instead "
                         f"(-ResponseKind reopened if it is closed)")
    n = db.rows("SELECT COALESCE(MAX(item_no), 0) + 1 AS n FROM escalation_thread_item "
                "WHERE escalation_id=?", (escalation_id,))[0]["n"]
    row = {"escalation_id": escalation_id, "item_no": n, "kind": kind, "value": value,
           "status": "open", "note": note, "opened_at": at, "opened_by": opened_by}
    row["id"] = db.write("escalation_thread_item", row)
    return row
```

**What it does.** A new open item; kind must be in enum `escalation_thread_item_kind`; refuses a duplicate kind and value.

**Config read by this element (found in its code).** enum: `escalation_thread_item_kind`; config tables named: `cfg_enum`

**Data (found in its code).** reads data table(s) `escalation_thread_item`; writes `escalation_thread_item`

#### G38 — escalation._thread_facts

`iba/app/lib/escalation.py:661-666`

```python
def _thread_facts(db: Db, escalation_id: int, *, items_changed: bool, closed_some: bool) -> dict:
    n_open = len(_thread_items(db, escalation_id, "open"))
    return {"items_changed": items_changed, "closed_some": closed_some,
            "open_remaining": n_open,
            "all_settled": n_open == 0 and bool(_thread_items(db, escalation_id)),
            "referenced": _thread_referenced(db, escalation_id)}
```

**What it does.** Counts open items and whether the thread is referenced.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G39 — escalation._thread_referenced

`iba/app/lib/escalation.py:646-658`

```python
def _thread_referenced(db: Db, escalation_id: int) -> bool:
    """T5: an open 'escalation' item points at a task or issue that is itself in-progress."""
    for it in _thread_items(db, escalation_id, "open"):
        if it["kind"] != "escalation":
            continue
        try:
            ref_id = resolve_id(db, it["value"])
        except ValueError:
            continue
        rows = db.rows("SELECT state FROM escalation WHERE id=?", (ref_id,))
        if rows and rows[0]["state"] == "in-progress":
            return True
    return False
```

**What it does.** True when an open `escalation` item points at a task or issue in-progress.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`

#### G40 — escalation._evaluate_transition

`iba/app/lib/escalation.py:224-258`

```python
def _evaluate_transition(db: Db, shape: str, next_action: str | None, *, has_resolution: bool,
                         assignee_changed: bool, explicit_state: str | None,
                         cur_state: str, needs_followup: bool = False,
                         cur_next_action: str | None = None, thread: dict | None = None) -> str:
    """Reads cfg_escalation_transition for `shape`, in priority order, first match wins.
    `resulting_status_key` `__explicit__` is the reject branch: the caller's own state, validated
    here (withdraw|supersede only). `__unchanged__` carries the state forward (or the caller's
    -State). The caller's explicit -State outranks an inferred assignee_changed result (#762)."""
    rows = db.rows(
        "SELECT priority, next_action, condition_key, resulting_status_key FROM "
        "cfg_escalation_transition WHERE shape=? AND active=1 ORDER BY priority", (shape,))
    if not rows:
        raise ValueError(f"cfg_escalation_transition has no active rows for shape={shape!r} -- "
                         f"run migration/rebuild_escalation_rules_config_20260820")
    for r in rows:
        if r["next_action"] is not None and r["next_action"] != next_action:
            continue
        if not _condition_true(r["condition_key"], next_action=next_action,
                               has_resolution=has_resolution, assignee_changed=assignee_changed,
                               has_explicit_state=explicit_state is not None,
                               needs_followup=needs_followup, cur_next_action=cur_next_action,
                               thread=thread):
            continue
        key = r["resulting_status_key"]
        if key == "__explicit__":
            if explicit_state not in ("withdraw", "supersede"):
                raise ValueError("next_action='reject' requires state='withdraw' or 'supersede', "
                                 "chosen explicitly by the caller")
            return explicit_state
        if key == "__unchanged__":
            return explicit_state or cur_state
        return _status_for(db, key, cur_state)
    raise ValueError(f"no cfg_escalation_transition rule matched shape={shape!r} "
                     f"next_action={next_action!r} -- the priority-last 'always' rule should have "
                     f"caught this; check the seed data")
```

**What it does.** The new state from `cfg_escalation_transition` rows in priority order; first match wins.

**Config read by this element (found in its code).** config tables named: `cfg_escalation_transition`

**Data (found in its code).** none directly.

#### G41 — escalation._condition_true

`iba/app/lib/escalation.py:186-221`

```python
def _condition_true(condition_key: str, *, next_action: str | None, has_resolution: bool,
                    assignee_changed: bool, has_explicit_state: bool = False,
                    needs_followup: bool = False, cur_next_action: str | None = None,
                    thread: dict | None = None) -> bool:
    """The fixed vocabulary cfg_escalation_transition.condition_key draws from. A new condition
    needs a code change here; which rule consumes it, in what priority, with what result, is config.

    `thread` is None for every non-thread item, so the thread conditions are false for them. For
    a thread it carries: items_changed (an item added, closed or reopened this call, or the state
    of the work an 'escalation' item references changed), closed_some, open_remaining, all_settled
    and referenced (an open 'escalation' item points at a task/issue at state in-progress)."""
    if condition_key == "always":
        return True
    if condition_key == "thread_items_changed_and_referenced":          # T3/T5
        return bool(thread and thread["items_changed"] and thread["referenced"])
    if condition_key == "thread_items_changed_partly_closed":           # T6, partial completion
        return bool(thread and thread["closed_some"] and thread["open_remaining"]
                    and not thread["referenced"])
    if condition_key == "has_resolution":
        return bool(has_resolution)
    if condition_key == "thread_items_all_settled":           # last open item settled: the
        return bool(thread and thread["items_changed"]         # thread completes; never on
                    and thread["all_settled"]                  # reject (withdraw/supersede
                    and next_action != "reject")               # settles its items itself)
    if condition_key == "thread_reassigned":                  # reassigning a thread keeps its
        return bool(thread is not None and assignee_changed)   # state (#2000 D1)
    if condition_key == "assignee_changed":
        return bool(assignee_changed)
    if condition_key == "explicit_state_given":               # an explicit -State outranks
        return bool(has_explicit_state)                        # assignee_changed (#762)
    if condition_key == "needs_followup":                      # approved but flagged: back to
        return bool(needs_followup)                            # Claude, not completed (#1075)
    if condition_key == "followup_cleared_was_approved":
        # Approved, resolution on file, follow-up now cleared: completed, without a second approval.
        return not needs_followup and has_resolution and cur_next_action == "approved"
    raise ValueError(f"unknown cfg_escalation_transition.condition_key {condition_key!r}")
```

**What it does.** The condition vocabulary of the transition engine.

**Config read by this element (found in its code).** config tables named: `cfg_escalation_transition`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The vocabulary.

#### G42 — escalation._status_for

`iba/app/lib/escalation.py:176-182`

```python
def _status_for(db: Db, set_by_substr: str, fallback: str) -> str:
    """cfg_status_flow lookup for entity='escalation'. `fallback` only covers a missing row."""
    for r in db.conn.execute(
            "SELECT status FROM cfg_status_flow WHERE entity='escalation' AND set_by LIKE ?",
            (f"%{set_by_substr}%",)):
        return r["status"]
    return fallback
```

**What it does.** Status from `cfg_status_flow`.

**Config read by this element (found in its code).** config tables named: `cfg_status_flow`

**Data (found in its code).** none directly.

#### G43 — escalation._check_requirements

`iba/app/lib/escalation.py:279-375`

```python
def _check_requirements(db: Db, action: str, *, originator: str, checked_action: str | None,
                        values: dict, self_id: int | None = None) -> None:
    """Raises ValueError on the first unmet requirement. `values` = the field->value the caller is
    supplying this transaction (already merged where relevant). `check_kind` selects the
    comparison. `self_id` is the item's own id (None at Raise)."""
    rows = db.rows(
        "SELECT field, condition_key, check_kind, message FROM cfg_escalation_requirement "
        "WHERE action=? AND active=1", (action,))
    for r in rows:
        if not _requirement_condition_true(r["condition_key"], originator=originator,
                                           checked_action=checked_action, values=values):
            continue
        kind = r["check_kind"] or "field_required"
        field_val = values.get(r["field"])
        if kind == "field_required":
            if not field_val:
                raise ValueError(r["message"])
        elif kind == "not_raised_with_content":                # D26
            if field_val == "raised":
                raise ValueError(r["message"])
        elif kind == "requires_current_ready_for_approval_if_decision_required":
            # A decision_required item may be approved only while it sits at ready_for_approval (#851).
            if self_id is not None:
                row = db.rows("SELECT resolution_kind, next_action FROM escalation WHERE id=?",
                              (self_id,))
                if (row and row[0]["resolution_kind"] == "decision_required"
                        and row[0]["next_action"] != "ready_for_approval"):
                    raise ValueError(r["message"])
        elif kind == "actor_must_be_assignee":
            # Inactive: no active cfg_escalation_requirement row uses this check_kind (rows 17-19 set
            # active=0); kept so it can be re-enabled by one row update. The D25 authority
            # check in update() is separate and stays.
            if self_id is not None:
                row = db.rows("SELECT next_action_assigned_to FROM escalation WHERE id=?", (self_id,))
                cur_assignee = row[0]["next_action_assigned_to"] if row else None
                if cur_assignee and originator != cur_assignee:
                    raise ValueError(
                        f"escalation #{self_id} is currently assigned to {cur_assignee!r} -- only "
                        f"{cur_assignee} may act on it (got originator={originator!r}). "
                        f"{cur_assignee} must process it first (even just to reassign it onward).")
        elif kind == "decision_required_approval_requires_researcher":
            # Only the researcher may approve a decision_required item, whoever it was assigned to.
            if self_id is not None:
                row = db.rows("SELECT resolution_kind FROM escalation WHERE id=?", (self_id,))
                if (row and row[0]["resolution_kind"] == "decision_required"
                        and originator != "Researcher"):
                    raise ValueError(r["message"])
        elif kind == "ready_for_approval_not_assignable_to_claude":
            # A task or issue can never be put at ready_for_approval assigned to Claude.
            if self_id is not None and values.get("next_action_assigned_to") == "Claude":
                row = db.rows("SELECT type FROM escalation WHERE id=?", (self_id,))
                if row and row[0]["type"] in ("task", "issue"):
                    raise ValueError(r["message"])
        elif kind == "reassign_to_researcher_requires_ready_for_approval":
            # Claude hands a decision_required item to the researcher only by setting
            # next_action=ready_for_approval in the same call; no bare reassignment (rule 63).
            if self_id is not None:
                row = db.rows("SELECT resolution_kind, next_action_assigned_to FROM escalation "
                              "WHERE id=?", (self_id,))
                if row:
                    cur_assignee = row[0]["next_action_assigned_to"]
                    new_assignee = values.get("next_action_assigned_to")
                    new_next_action = values.get("next_action")
                    if (row[0]["resolution_kind"] == "decision_required" and originator == "Claude"
                            and cur_assignee == "Claude" and new_assignee == "Researcher"
                            and new_next_action != "ready_for_approval"):
                        raise ValueError(r["message"])
        elif kind == "must_be_self_correctable":
            # every thread is raised self_correctable (T4)
            if field_val != "self_correctable":
                raise ValueError(r["message"])
        elif kind == "no_open_thread_items":
            # T6: a thread reaches completed/closed only when every item is closed. `field` is 'state',
            # the state this call would land on; items written earlier in the same call are visible here.
            if self_id is not None and field_val in ("completed", "closed"):
                n_open = db.rows("SELECT COUNT(*) AS n FROM escalation_thread_item WHERE "
                                 "escalation_id=? AND status='open'", (self_id,))[0]["n"]
                if n_open:
                    raise ValueError(f"{r['message']} ({n_open} open item(s) on #{self_id})")
        elif kind == "strand_account_clean":
            # #2172 safeguard 5: the escalation that records a strand reaches completed/closed only when
            # every hit has a face or a reason and every observation a disposition (strandreading).
            if self_id is not None and field_val in ("completed", "closed"):
                from . import strandreading
                gaps = strandreading.gate_message(db.conn, self_id)
                if gaps:
                    raise ValueError(f"{r['message']} ({gaps})")
        elif kind == "readings_published":
            # #2228: the escalation that anchors a reading reaches completed/closed only when each of its
            # readings is published or withdrawn (lib/reading).
            if self_id is not None and field_val in ("completed", "closed"):
                from . import reading
                gaps = reading.gate_message(db.conn, self_id)
                if gaps:
                    raise ValueError(f"{r['message']} ({gaps})")
        else:
            raise ValueError(f"unknown cfg_escalation_requirement.check_kind {kind!r}")
```

**What it does.** Applies `cfg_escalation_requirement` rows for the action; for `update` the rows listed in config (appendix).

**Config read by this element (found in its code).** config tables named: `cfg_escalation_requirement`

**Data (found in its code).** reads data table(s) `escalation`, `escalation_thread_item`

**Fixed in the code, not config.** The check kinds.

#### G44 — escalation._requirement_condition_true

`iba/app/lib/escalation.py:262-276`

```python
def _requirement_condition_true(condition_key: str, *, originator: str, checked_action: str | None,
                                values: dict) -> bool:
    """`values` -- some conditions need to look at what the caller is actually supplying this
    transaction, not just who they are / what action they're taking."""
    if condition_key == "always":
        return True
    if condition_key == "claude_revising":
        return originator == "Claude" and checked_action == "revise"
    if condition_key == "has_content":                         # D26
        return bool(values.get("comment") or values.get("context") or values.get("tried"))
    if condition_key == "thread_type":                         # escalation #2000 (T4/T6/T7)
        return values.get("type") == "thread"
    if condition_key == "thread_superseding":
        return values.get("type") == "thread" and values.get("state") == "supersede"
    raise ValueError(f"unknown cfg_escalation_requirement.condition_key {condition_key!r}")
```

**What it does.** The condition vocabulary of the requirement engine.

**Config read by this element (found in its code).** config tables named: `cfg_escalation_requirement`

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The vocabulary.

#### G45 — escalation._check_state

`iba/app/lib/escalation.py:101-105`

```python
def _check_state(db: Db, state: str) -> str:
    valid = db.cfg.enum("escalation_state")
    if state not in valid:
        raise ValueError(f"{state!r} is not a member of cfg_enum 'escalation_state' ({valid!r})")
    return state
```

**What it does.** The state must be a value of enum `escalation_state`.

**Config read by this element (found in its code).** enum: `escalation_state`; config tables named: `cfg_enum`

**Data (found in its code).** none directly.

#### G46 — escalation._snapshot

`iba/app/lib/escalation.py:401-434`

```python
def _snapshot(cfg: Cfg, db: Db, escalation_id: int, deltas: dict, envelope: dict,
              originator: str) -> dict:
    """`deltas` = what the caller sets THIS transaction for append/replace columns (None/absent =
    untouched). `envelope` = state/next_action/next_action_assigned_to, already resolved. The
    history row gets the deltas as given (NULL where not supplied) plus the envelope; `escalation`
    gets append columns merged onto the running text and replace columns updated or carried."""
    _grant_both(cfg)
    cur = _current(db, escalation_id)
    version = cur["version"] + 1
    now = _now()

    hist_row = {c: None for c in _APPEND_COLS + _REPLACE_COLS + _IMMUTABLE_COLS}
    for c in _APPEND_COLS + _REPLACE_COLS:
        if deltas.get(c):
            hist_row[c] = deltas[c]
    hist_row.update(envelope)
    hist_row["originator"] = originator
    hist_row["answered_at"] = now
    db.write("escalation_history", {"escalation_id": escalation_id, "version": version, **hist_row})

    merged = dict(cur)
    for c in _APPEND_COLS:
        if deltas.get(c):
            merged[c] = _append(cur[c], deltas[c])
    for c in _REPLACE_COLS:
        if deltas.get(c) is not None:
            merged[c] = deltas[c]
    merged.update(envelope)
    merged["originator"] = originator
    merged["answered_at"] = now
    merged["version"] = version
    db.update("escalation", {"id": escalation_id}, version=version,
             **{k: merged[k] for k in _COLS})
    return merged
```

**What it does.** Writes the new history version and updates the escalation row (comment/context appended, resolution/tried replaced).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** writes `escalation`, `escalation_history`

#### G47 — escalation._append / _grant / _grant_both / _now

`iba/app/lib/escalation.py:437-440`

```python
def _append(current: str | None, addition: str | None) -> str | None:
    if not addition:
        return current
    return f"{current}\n{addition}" if current else addition
```

**What it does.** Append text with a newline.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G47b — escalation._grant

`iba/app/lib/escalation.py:92-94`

```python
def _grant(cfg: Cfg, table: str):
    if table not in cfg.may_write("escalation"):
        raise PermissionError(f"write-grant violation: 'escalation' may not write {table!r}")
```

**What it does.** The `escalation` writer's grants (`cfg_write_grant`).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G47c — escalation._grant_both

`iba/app/lib/escalation.py:386-388`

```python
def _grant_both(cfg: Cfg) -> None:
    _grant(cfg, "escalation")
    _grant(cfg, "escalation_history")
```

**What it does.** Grants on `escalation` and `escalation_history`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G47d — escalation._now

`iba/app/lib/escalation.py:88-89`

```python
def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

**What it does.** UTC timestamp.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G48 — escalation.resolve_id

`iba/app/lib/escalation.py:466-476`

```python
def resolve_id(db: Db, ref) -> int:
    """An escalation id from `ref`: 2000, '2000', '#2000', or a thread alias 'OT-16' (any case)."""
    s = str(ref).strip()
    if s.startswith("#"):
        s = s[1:]
    if s.isdigit():
        return int(s)
    rows = db.rows("SELECT id FROM escalation WHERE alias=? COLLATE NOCASE", (s,))
    if not rows:
        raise ValueError(f"no escalation with id or alias {ref!r}")
    return rows[0]["id"]
```

**What it does.** An escalation id from `2000`, `#2000` or `OT-16`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`

#### G49 — reading.check (pre gate, state open)

`iba/app/lib/reading.py:1183-1220`

```python
def check(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = reading(conn, p.get("Label"))
    if r["state"] == "open":
        gaps = gate_pre(conn, root, r)
        if gaps:
            _gate_fail(r, "pre", gaps)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "gathered", "gathered_at": _now(),
                                                                      "run_id": run_id}))
        return f"reading {r['label']}: pre gate passed -- gathered (Reading.ps1 -Step Observe next)"
    if r["state"] == "gathered":
        gaps = gate_observe(cfg, root, r)
        if gaps:
            _gate_fail(r, "observe", gaps)

        def go():
            w.update("reading", {"id": r["id"]}, {"state": "observed", "observed_at": _now(), "run_id": run_id})
            w._grant("verse_meta")
            return versemeta.mark(conn, verse_ids(conn, r["id"]), "analysed")
        marked = nr._atomic(conn, go)
        return f"reading {r['label']}: observe gate passed -- observed; {marked} verse(s) marked analysed"
    if r["state"] == "observed":
        gaps = gate_post(cfg, root, r)
        if gaps:
            _gate_fail(r, "claims", gaps)
        path = _build_narrate(cfg, root, r)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {
            "state": "synergised", "synergised_at": _now(), "narrate_file": _rel(root, path), "run_id": run_id}))
        return (f"reading {r['label']}: claims gate passed -- synergised; narrate JSON built from the tables\n  -> "
                f"{_rel(root, path)}")
    if r["state"] == "synergised":
        gaps = gate_narrate(cfg, r)
        if gaps:
            _gate_fail(r, "narrate", gaps)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "narrated", "narrated_at": _now(),
                                                                      "run_id": run_id}))
        return f"reading {r['label']}: narrate gate passed -- narrated (Reading.ps1 -Step Publish next)"
    raise Refused(f"reading {r['label']} is {r['state']}; Check runs at open, gathered, observed or synergised")
```

**What it does.** Runs the gate for the state the reading is at. At `open`: `gate_pre` (G50); if no gaps, sets the reading to `gathered` with the time. (The other states belong to later steps: see 'Not in Analysis_phase_1'.)

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** B04 (setting reading.focus_words, setting reading.non_characteristic_strongs, setting reading.surface_requirements)

**Data (found in its code).** writes `reading`, `verse_meta`

**Fixed in the code, not config.** The state names.

#### G50 — reading.gate_pre

`iba/app/lib/reading.py:451-465`

```python
def gate_pre(conn, root: pathlib.Path, r) -> list[str]:
    data = _load(root, r["gap_file"], "the pre-gap JSON")
    out = []
    for sec, i, it in _items_of(data):
        rec, at = it.get("record"), f"{sec}[{i}] {it.get('verse') or it.get('strong') or it.get('item')}"
        if not isinstance(rec, dict):
            out.append(f"{at}: no record")
        elif rec.get("reason") and not rec.get("id"):
            continue
        elif not rec.get("table") or not _row_exists(conn, rec["table"], rec.get("id")):
            out.append(f"{at}: record {rec.get('table')} {rec.get('id')} is not a row that exists (run Gather)")
    for i, s in enumerate(data.get("new_items") or []):
        if not (isinstance(s, dict) and s.get("added")):
            out.append(f"new_items[{i}]: not added (run Gather)")
    return out
```

**What it does.** Loads the gap file. Every item must have a `record`: a reason (no id needed), or a `table`+`id` that exists. Every `new_items` entry must have been added. It does not compare a record to the item it answers.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### G51 — reading._gate_fail

`iba/app/lib/reading.py:162-164`

```python
def _gate_fail(r, name: str, gaps: list[str]):
    raise Refused("\n  ".join([f"reading {r['label']} is not past the {name} gate ({len(gaps)} gap(s)):"] + gaps[:60]
                              + ([f"... and {len(gaps) - 60} more"] if len(gaps) > 60 else [])))
```

**What it does.** Refuses with up to 60 gap lines.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** The 60-line cap.

## 7. Step 3 — Observe and Record

`Reading.ps1 -Step Observe -Label <label> -By ...` builds `<label>-observe.json` from the tables. `Reading.ps1 -Step Record -Label <label> [-File <observe file>] -By ...` writes what is in that file. Handlers `reading:observe` and `reading:record`. Elements of `Gather` that `Record` reuses (G13 to G27) are not repeated.

### 7.1 Observe: elements B01 to B12



#### B01 — handlers.reading.observe

`iba/app/handlers/reading.py:60-61`

```python
def observe(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.observe(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT))
```

**What it does.** Calls `reading.observe` through the write wrapper.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** B02 (setting reading.observe_prompts); B04 (setting reading.focus_words, setting reading.non_characteristic_strongs, setting reading.surface_requirements); G14 (setting reading.observation_parts, enum ib_observation.tag); O05 (setting reading.output_dir)

**Data (found in its code).** none directly.

#### B02 — reading.observe (the step)

`iba/app/lib/reading.py:599-647`

```python
def observe(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """The observe JSON, built from the tables once the reading is gathered (RO2: every finding into focus)."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "gathered")
    V = []
    vids = verse_ids(conn, r["id"])
    refs = [(vid, conn.execute("SELECT reference FROM verse WHERE id=?", (vid,)).fetchone()[0]) for vid in vids]
    items_on = _open_items_for(cfg, conn, refs)
    for vid in vids:
        v = conn.execute("SELECT osisId, reference, text FROM verse WHERE id=?", (vid,)).fetchone()
        state = surfaces_state(cfg, conn, vid)
        V.append({"verse": v["reference"], "osis": v["osisId"], "text": v["text"], "passage": _passage(conn, v["osisId"]),
                  "findings_in_focus": _findings_on(conn, v["osisId"]), "open_items": items_on[vid],
                  "surfaces_in_focus": len(state), "surfaces_complete": sum(1 for s in state if not s["missing"]),
                  "words": [s for s in state if s["missing"]]})
    in_focus = sorted({f["observation"] for v in V for f in v["findings_in_focus"]})
    C = [{"claim": c["claim_ref"], "status": c["status"], "text": c["claim_text"]}
         for c in scope_claims(conn, r["id"], in_focus)]
    prompts = {}
    for kind, codes in _setting(cfg, "reading.observe_prompts").items():
        prompts[kind] = [{"code": q, "question": t} for q, t in conn.execute(
            f"SELECT question_code, question_text FROM wa_obs_question_catalogue WHERE deleted=0 AND question_code IN "
            f"({','.join('?' * len(codes)) or 'NULL'}) ORDER BY prompt_seq", codes)]
    built = _now()
    data = {"reading": r["label"], "reading_id": r["id"], "objective": r["objective"], "built_at": built,
            "built_from": "the tables (B:114)",
            "how": "Read each verse in its passage with every finding in focus (RO1, RO2). Record findings in "
                   "`findings` (observationrecord's shape: key, kind, text, meaning, implication, basis, route on a "
                   "party or link finding, nodes [{verse, strong, surface, cluster, role}]; the surface names the "
                   "occurrence; a description already live is named as existing and gains nodes). `words` lists only "
                   "the surfaces of the verse (a surface is a word as written with its Strong) that lack what "
                   "reading.surface_requirements asks, as `missing`: add only that. A surface lacking nothing is not "
                   "listed (`surfaces_complete`). `open_items` are the open items for the verse, whatever their "
                   "subgroup. A surface that cannot be completed takes its `record`: "
                   "{\"reason\": ...}, {\"item\": \"OT-nn.n|#n\"} or {\"new_item\": <Open-Item add shape>}. A finding "
                   "no longer supported: `withdraw` [{\"node\": id, \"reason\"} | {\"observation\": id, \"reason\"}]. "
                   "The prompts are the catalogue's questions by kind: a prompt that does not apply is not answered "
                   "(RG-17). Then Reading.ps1 -Step Record -Label " + r["label"] + ".",
            "kinds": orec.kinds(cfg), "prompts": prompts, "claims": C, "verses": V,
            "findings": [], "withdraw": []}
    path = out_dir(cfg, root, r["label"]) / f"{r['label']}-observe.json"
    if path.exists():
        path.replace(path.with_name(f"{r['label']}-observe-{built.replace(':', '').replace('-', '')}.json"))
    _save(path, data)
    nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {
        "observe_file": _rel(root, path), "observe_built_at": built, "run_id": run_id}))
    n_words = sum(len(v["words"]) for v in V)
    return (f"reading {r['label']}: observe JSON built from the tables -- {len(V)} verse(s), {n_words} word(s) in "
            f"focus, {len(in_focus)} finding(s) in focus, {len(C)} claim(s)\n  -> {_rel(root, path)}")
```

**What it does.** Needs the reading at `gathered`. Reads the verse ids of the reading, then per verse: its text; `surfaces_state` (B04); the passage (the verse and two before and after); every live finding on it with its nodes (`_findings_on`); the open items matched to it (`_open_items_for`). Collects the claims on the scope (`scope_claims`, current or held). Reads the catalogue questions named in setting `reading.observe_prompts` from `wa_obs_question_catalogue`. Reads the kinds (`observationrecord.kinds`). Writes `<label>-observe.json` (an earlier file with that name is renamed with a time stamp), sets `observe_file` and `observe_built_at` on the `reading` row, and returns the counts. It writes no observation and no node. Writer grant: `reading`.

**Config read by this element (found in its code).** setting: `reading.observe_prompts`

**Config read below it, through the functions it calls (all levels; each has its own element).** B04 (setting reading.focus_words, setting reading.non_characteristic_strongs, setting reading.surface_requirements); G14 (setting reading.observation_parts, enum ib_observation.tag); O05 (setting reading.output_dir)

**Data (found in its code).** reads data table(s) `verse`, `wa_obs_question_catalogue`; writes `reading`

**Fixed in the code, not config.** The state `gathered`; the passage window of two verses either side; the file name; the `how` text; claims of status current or held.

#### B03 — reading.verse_ids

`iba/app/lib/reading.py:125-126`

```python
def verse_ids(conn, rid: int) -> list[int]:
    return [r[0] for r in conn.execute("SELECT verse_id FROM reading_verse WHERE reading_id=? ORDER BY verse_id", (rid,))]
```

**What it does.** The reading's verses (`reading_verse`).

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `reading_verse`

#### B04 — reading.surfaces_state

`iba/app/lib/reading.py:502-543`

```python
def surfaces_state(cfg, conn, vid: int) -> list[dict]:
    """The surfaces of one verse that need observations, and what each already has and lacks (#2312). A surface is a
    verse_lexical occurrence (surface with its Strong). In focus (reading.focus_words): every content word (a function
    word is left out by its morph), the kept tags (negators, connectives), every M-coded word and the words in
    reading.non_characteristic_strongs. Required of each (reading.surface_requirements): a node with a role, and the
    kinds listed, or a silence finding in their place. Missing = required and not yet on a live finding."""
    spec = _setting(cfg, "reading.focus_words")
    req = _setting(cfg, "reading.surface_requirements")
    never = set(_setting(cfg, "reading.non_characteristic_strongs"))
    osis = conn.execute("SELECT osisId FROM verse WHERE id=?", (vid,)).fetchone()[0]
    rows = conn.execute("SELECT id, position, surface, strong, morph_code, testament, is_negator FROM verse_lexical "
                        "WHERE verse_id=? AND deleted=0 ORDER BY position, id", (vid,)).fetchall()
    sub = _subgroups_of(conn)
    have = _has_on_surfaces(conn, osis, rows)
    out = []
    for r in rows:
        clusters = orec.word_clusters(conn, r["strong"])
        prefix = (r["morph_code"] or "")[:2] if r["testament"] == "OT" else (r["morph_code"] or "").split("-")[0]
        function = prefix in spec["function_word_morph"].get(r["testament"], [])
        why = []
        if any(c.startswith("M") for c in clusters):
            why.append("M-code")
        if r["strong"] in never:
            why.append("never a characteristic (RG-23)")
        if r["is_negator"] or any(t in clusters for t in spec["keep_tags"]):
            why.append("negator or connective (RG-22)")
        if not function and not why:
            why.append("content word (RG-22)")
        if not why:
            continue
        got = have[r["id"]]
        kinds = {t for _, t in got}
        silent = "silence" in kinds
        missing = []
        if req["role"] and not any(role for role, _ in got):
            missing.append("role")
        missing += [k for k in req["kinds"] if k not in kinds and not (silent and k in req["silence_instead_of"])]
        out.append({"word": f"{r['surface']} ({r['strong']})", "strong": r["strong"], "surface": r["surface"],
                    "morph": r["morph_code"], "position": r["position"], "occurrence": r["id"], "clusters": clusters,
                    "subgroups": sub.get((r["strong"], r["surface"]), []), "in_focus_as": why,
                    "has": sorted(kinds), "missing": missing, "record": None})
    return out
```

**What it does.** Decides, for each word occurrence (`verse_lexical` row) of a verse, whether it is in focus and what it lacks. Reads settings `reading.focus_words`, `reading.surface_requirements` and `reading.non_characteristic_strongs`. In focus when: it has an M-coded cluster; or its Strong is in `non_characteristic_strongs`; or it is a negator or has a cluster in `keep_tags` (T5, T6); or it is a content word (its morph prefix is not in `function_word_morph` for its testament). It lacks `role` if no live node of it has a role, and each kind in `surface_requirements.kinds` (face, term) that no live finding on it has, unless a `silence` finding is on it (`silence_instead_of`). A live node belongs to an occurrence by its `verse_lexical_id`; a node without one belongs to the occurrence only when its Strong and surface match exactly one occurrence in the verse.

**Config read by this element (found in its code).** setting: `reading.focus_words`, `reading.non_characteristic_strongs`, `reading.surface_requirements`

**Data (found in its code).** reads data table(s) `verse`, `verse_lexical`

**Fixed in the code, not config.** The morph-prefix rule (first two letters for OT, text before the first hyphen for NT); the word 'content word'; the labels RG-22, RG-23, RG-22; the rule that a node with no occurrence id counts only on a unique match.

#### B05 — reading._subgroups_of

`iba/app/lib/reading.py:469-476`

```python
def _subgroups_of(conn) -> dict:
    """{(strong, surface): [subgroup codes]} through surface_subgroup (the surface's own subgroup, #2312)."""
    out: dict = {}
    for strong, surface, sg in conn.execute(
            "SELECT s.strong, s.surface, g.subgroup_code FROM surface_subgroup s JOIN cluster_subgroup g ON "
            "g.id=s.cluster_subgroup_id WHERE s.deleted=0 ORDER BY g.subgroup_code"):
        out.setdefault((strong, surface), []).append(sg)
    return out
```

**What it does.** (Strong, surface) to subgroup codes from `surface_subgroup` and `cluster_subgroup`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `cluster_subgroup`, `surface_subgroup`

#### B06 — reading._has_on_surfaces

`iba/app/lib/reading.py:479-499`

```python
def _has_on_surfaces(conn, osis: str, rows: list) -> dict:
    """{verse_lexical id: [(node role, observation tag)]}: the live nodes of live findings on each surface occurrence
    of one verse. A node belongs to an occurrence by its verse_lexical_id; one without it by verse, Strong and
    surface when that match is unique in the verse; any other node is set aside (it names a verse and no surface)."""
    key = {}
    for r in rows:
        key.setdefault((r["strong"], r["surface"]), []).append(r["id"])
    out: dict = {r["id"]: [] for r in rows}
    for n in conn.execute(
            "SELECT n.verse_lexical_id, n.strong, n.surface, n.role, o.tag FROM ib_node n JOIN ib_observation o ON "
            "o.id=n.observation_id WHERE n.verse_reference=? AND o.status<>'withdrawn' AND "
            "(n.disposition IS NULL OR n.disposition<>'withdrawn')", (osis,)):
        if n["verse_lexical_id"] in out:
            out[n["verse_lexical_id"]].append((n["role"], n["tag"]))
        elif n["verse_lexical_id"] is None and n["strong"]:
            same = key.get((n["strong"], n["surface"])) if n["surface"] else None
            if same is None and not n["surface"]:
                same = [i for (s, _), ids in key.items() if s == n["strong"] for i in ids]
            if same and len(same) == 1:
                out[same[0]].append((n["role"], n["tag"]))
    return out
```

**What it does.** For each occurrence of the verse, the (role, kind) pairs of the live nodes of live findings that belong to it.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `ib_node`, `ib_observation`

#### B08 — reading._open_items_for

`iba/app/lib/reading.py:551-574`

```python
def _open_items_for(cfg, conn, verses: list[tuple]) -> dict:
    """{verse id: [open item, ...]}: the open thread items for each verse, by the verse and through its surfaces' Strongs
    and clusters (a scope item by its own verses only), each with the subgroups it reaches (#2312). `verses` is
    [(verse id, reference)]."""
    by_ref = {ref: vid for vid, ref in verses}
    by_strong, by_cluster = {}, {}
    for vid, _ in verses:
        for r in conn.execute("SELECT strong FROM verse_lexical WHERE verse_id=? AND deleted=0", (vid,)):
            by_strong.setdefault(r["strong"], set()).add(vid)
            for cl in orec.word_clusters(conn, r["strong"]):
                by_cluster.setdefault(cl, set()).add(vid)
    out: dict = {vid: [] for vid, _ in verses}
    seen = set()
    for t, it, qv in escalation.match_open_items(Db(cfg), clusters=sorted(by_cluster), strongs=sorted(by_strong),
                                                 verses=sorted(by_ref), home=False):
        for vid in ({by_ref[qv]} if qv in by_ref else by_strong.get(qv) or by_cluster.get(qv) or set()):
            if (vid, it["id"]) in seen:
                continue
            seen.add((vid, it["id"]))
            row = conn.execute("SELECT * FROM escalation_thread_item WHERE id=?", (it["id"],)).fetchone()
            out[vid].append({"item": f"{t['alias']}.{it['item_no']}", "kind": it["kind"], "value": it["value"],
                             "matched_on": qv, "note": it["note"], "read_for": row["read_for"],
                             "subgroups": _item_subgroups(conn, row)})
    return out
```

**What it does.** For the reading's verses, the open thread items matched by verse, by the Strongs and clusters of the verse's words (`escalation.match_open_items`, home false), each with its read_for and the subgroups it reaches.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation_thread_item`, `verse_lexical`

#### B09 — reading._passage

`iba/app/lib/reading.py:577-582`

```python
def _passage(conn, osis: str) -> list[dict]:
    book, ch, v = osis.split(".")
    want = [f"{book}.{ch}.{n}" for n in range(max(1, int(v) - 2), int(v) + 3)]
    rows = {r[0]: r for r in conn.execute("SELECT osisId, reference, text FROM verse WHERE deleted=0 AND osisId IN "
                                          f"({','.join('?' * len(want))})", want)}
    return [{"verse": rows[o][1], "text": rows[o][2]} for o in want if o in rows]
```

**What it does.** The verse and the two before and after it in the same chapter.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `verse`

**Fixed in the code, not config.** The window of two.

#### B10 — reading._findings_on

`iba/app/lib/reading.py:585-596`

```python
def _findings_on(conn, osis: str) -> list[dict]:
    out = []
    for o in conn.execute("SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE "
                          "n.verse_reference=? AND o.status<>'withdrawn' ORDER BY o.id", (osis,)):
        nodes = [dict(n) for n in conn.execute(
            "SELECT id node, strong, surface, verse_lexical_id occurrence, cluster_code cluster, cluster_subgroup_code "
            "subgroup, role, reading_id, disposition FROM ib_node WHERE "
            "observation_id=? AND verse_reference=? AND (disposition IS NULL OR disposition<>'withdrawn')",
            (o["id"], osis))]
        out.append({"observation": o["id"], "stage": o["stage"], "kind": o["tag"], "text": o["obs_text"],
                    "meaning": o["meaning"], "basis": o["basis"], "route": o["route"], "nodes": nodes})
    return out
```

**What it does.** Each non-withdrawn observation with a node in the verse, with its live nodes there.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `ib_node`, `ib_observation`

#### B11 — reading.scope_claims

`iba/app/lib/reading.py:787-792`

```python
def scope_claims(conn, rid: int, obs_ids: list[int]) -> list:
    return conn.execute(
        f"SELECT DISTINCT c.* FROM narrative_claim c JOIN narrative_claim_source cs ON cs.claim_id=c.id WHERE "
        f"c.status IN ('current', 'held') AND (cs.verse_id IN (SELECT verse_id FROM reading_verse WHERE reading_id=?) "
        f"OR cs.observation_id IN ({','.join('?' * len(obs_ids)) or 'NULL'})) ORDER BY c.id",
        (rid, *obs_ids)).fetchall()
```

**What it does.** Current or held claims whose source is a verse of the reading or a finding in focus.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `narrative_claim`, `narrative_claim_source`, `reading_verse`

#### B12 — observationrecord.kinds

`iba/app/lib/observationrecord.py:41-48`

```python
def kinds(cfg) -> list[str]:
    """The eight kinds of finding (cfg_setting reading.observation_parts), each a live ib_observation.tag value."""
    parts = cfg.required_setting("reading.observation_parts")
    out = list((json.loads(parts) if isinstance(parts, str) else parts)["kinds"])
    missing = set(out) - set(cfg.enum("ib_observation.tag"))
    if missing:
        raise Refused(f"kinds {sorted(missing)} are not ib_observation.tag values")
    return out
```

**What it does.** (shown at G14)

**Config read by this element (found in its code).** setting: `reading.observation_parts`; enum: `ib_observation.tag`; config tables named: `cfg_setting`

**Data (found in its code).** none directly.

### 7.2 Record: elements R01 to R08



#### R01 — handlers.reading.record

`iba/app/handlers/reading.py:64-65`

```python
def record(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.record(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT))
```

**What it does.** Calls `reading.record` through the write wrapper.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** G13 (enum ib_observation.basis, enum observation_role, enum observation_route); G14 (setting reading.observation_parts, enum ib_observation.tag); G21 (setting narrative.quote_min_words)

**Data (found in its code).** none directly.

#### R02 — reading.record (the step)

`iba/app/lib/reading.py:657-738`

```python
def record(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    """-Label [-File <observe JSON>]: the findings, withdrawals and word records written; nothing if any is wrong."""
    conn = cfg.conn
    r = _at(conn, p.get("Label"), "gathered")
    path = _path(root, p.get("File") or r["observe_file"] or "")
    data = _load(root, str(path), "-File")
    if data.get("reading_id") != r["id"] or not r["observe_built_at"] or data.get("built_at") != r["observe_built_at"]:
        raise Refused(f"the file is not the observe JSON built from the tables for reading {r['label']} "
                      f"(built_at {data.get('built_at')!r}, the reading's {r['observe_built_at']!r}): run Observe")
    items = _ReadingItems(cfg, w)
    errors, quotes = [], []
    todo = [(f"findings[{i}] ({f.get('key')})", f) for i, f in enumerate(data.get("findings") or [])
            if isinstance(f, dict) and not f.get("written")]
    fplan = orec.check(cfg, todo, errors, quotes) if todo else []
    raise_words = []
    for v in data.get("verses") or []:
        for j, wd in enumerate(v.get("words") or []):
            rec, at = wd.get("record"), f"{v['verse']} words[{j}] {wd.get('word')}"
            if not rec or (isinstance(rec, dict) and rec.get("added")):
                continue
            if not isinstance(rec, dict) or len([k for k in ("reason", "item", "new_item") if rec.get(k)]) != 1:
                errors.append(f"{at}: record is one of {{\"reason\"}}, {{\"item\"}} or {{\"new_item\"}}")
            elif rec.get("reason") and len(rec["reason"].strip()) < 10:
                errors.append(f"{at}: a reason says why, in words (10 characters or more)")
            elif rec.get("item") and not _item_exists(conn, rec["item"]):
                errors.append(f"{at}: item {rec['item']} does not exist")
            elif rec.get("new_item"):
                if items.check(rec["new_item"], at, errors):
                    raise_words.append((at, wd))
    wd_plan = []
    for i, x in enumerate(data.get("withdraw") or []):
        at = f"withdraw[{i}]"
        if not isinstance(x, dict) or x.get("done"):
            continue
        if len((x.get("reason") or "").strip()) < 10:
            errors.append(f"{at}: a withdrawal needs its reason, in words (RW-01)")
        elif x.get("node") is not None:
            if not conn.execute("SELECT 1 FROM ib_node WHERE id=? AND (disposition IS NULL OR disposition<>'withdrawn')",
                                (x["node"],)).fetchone():
                errors.append(f"{at}: node {x['node']} is not a live node")
            else:
                wd_plan.append(x)
        elif x.get("observation") is not None:
            if not conn.execute("SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'",
                                (x["observation"],)).fetchone():
                errors.append(f"{at}: observation {x['observation']} is not a live observation")
            else:
                wd_plan.append(x)
        else:
            errors.append(f"{at}: name the node or the observation withdrawn")
    if errors or quotes:
        raise Refused("\n  ".join(["the reading is not recorded:"] + errors + (
            ["quotation(s) not found in the ESV text:"] + quotes if quotes else [])))
    if not fplan and not raise_words and not wd_plan:
        raise Refused("nothing to record: no new finding, no word with a new item, no withdrawal")

    def go():
        _grant_findings(w)
        written = orec.write(conn, fplan, r["id"], run_id) if fplan else {}
        for x in wd_plan:
            if x.get("node") is not None:
                orec.set_disposition(conn, x["node"], "withdrawn", x["reason"].strip(), r["id"], run_id, w.who)
            else:
                orec.withdraw_observation(conn, x["observation"], x["reason"].strip(), r["id"], run_id, w.who)
        added = []
        for at, wd in raise_words:
            wd["record"]["added"] = items.raise_(wd["record"]["new_item"], f"{at} (reading {r['label']})")
            added.append(wd["record"]["added"])
        w.update("reading", {"id": r["id"]}, {"run_id": run_id})
        return written, added
    written, added = nr._atomic(conn, go)
    for f in data.get("findings") or []:
        if isinstance(f, dict) and f.get("key") in written:
            f["written"] = {"observation": written[f["key"]]["observation"], "nodes": written[f["key"]]["nodes"],
                            "run_id": run_id}
    for x in wd_plan:
        x["done"] = run_id
    _save(path, data)
    return (f"reading {r['label']}: {sum(1 for x in written.values() if x['new'])} finding(s) new, "
            f"{sum(1 for x in written.values() if not x['new'])} existing applied, "
            f"{sum(len(x['nodes']) for x in written.values())} node(s); {len(wd_plan)} withdrawal(s); {len(added)} open "
            f"item(s) added ({', '.join(added) or '-'})\n  ids written back to {_rel(root, path)}")
```

**What it does.** Needs the reading at `gathered` and the observe file to be the one built for it (the `built_at` stamp must match). Checks: each new finding in `findings` (not yet written) by `observationrecord.check` (G13); each verse's `words[].record` is exactly one of `reason` (10 characters or more), `item` (an existing escalation or thread item) or `new_item` (open-item rules); each `withdraw` entry has a reason of 10 characters or more and names a live node or a live observation. Refuses all if anything is wrong, or if there is nothing to record. Otherwise in one savepoint: writes the findings (`observationrecord.write`), applies each withdrawal (`set_disposition` to `withdrawn` for a node, `withdraw_observation` for a finding; each change logged with its reason in `ib_observation_change`), adds the new items; then saves the file with the ids written back. Writer grants for `reading.record`: `escalation_thread_item`, `escalation_thread_item_verse`, `ib_node`, `ib_observation`, `ib_observation_change`, `reading`.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** G13 (enum ib_observation.basis, enum observation_role, enum observation_route); G14 (setting reading.observation_parts, enum ib_observation.tag); G21 (setting narrative.quote_min_words)

**Data (found in its code).** reads data table(s) `ib_node`, `ib_observation`; writes `reading`

**Fixed in the code, not config.** The 10-character minimum; the three record kinds; the `written` and `done` marks in the file.

#### R03 — reading._item_exists

`iba/app/lib/reading.py:651-654`

```python
def _item_exists(conn, ref: str) -> bool:
    ref = str(ref or "")
    kind = "escalation" if ref.startswith("#") else "thread item" if "." in ref else "thread"
    return bool(ref) and nr._escalation_exists(conn, kind, ref)
```

**What it does.** An escalation (`#n`), thread item (`OT-nn.n`) or thread (`OT-nn`) exists.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

#### R04 — narrativeregister._escalation_exists

`iba/app/lib/narrativeregister.py:890-900`

```python
def _escalation_exists(conn, kind: str, value: str) -> bool:
    if kind == "escalation":
        return conn.execute("SELECT 1 FROM escalation WHERE id=?", (int(value.lstrip("#")),)).fetchone() is not None
    alias, _, item = value.partition(".")
    e = conn.execute("SELECT id FROM escalation WHERE alias=?", (alias,)).fetchone()
    if e is None:
        return False
    if kind == "thread item":
        return conn.execute("SELECT 1 FROM escalation_thread_item WHERE escalation_id=? AND item_no=?",
                            (e[0], int(item or 0))).fetchone() is not None
    return True
```

**What it does.** The existence test for the three forms.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `escalation`, `escalation_thread_item`

#### R05 — observationrecord.set_disposition

`iba/app/lib/observationrecord.py:223-232`

```python
def set_disposition(conn, node_id: int, disposition: str, note: str, reading_id, run_id: str, who: str) -> None:
    """Where this verse ends up for the finding (cfg_enum observation_disposition), the change kept."""
    n = conn.execute("SELECT observation_id, disposition, disposition_note FROM ib_node WHERE id=?",
                     (node_id,)).fetchone()
    if n is None:
        raise Refused(f"node {node_id} does not exist")
    if (n["disposition"], n["disposition_note"]) == (disposition, note):
        return
    log(conn, n["observation_id"], node_id, "disposition", n["disposition"], disposition, note, reading_id, run_id, who)
    conn.execute("UPDATE ib_node SET disposition=?, disposition_note=? WHERE id=?", (disposition, note, node_id))
```

**What it does.** Sets a node's disposition and note, logging the change with its reason.

**Config read by this element (found in its code).** config tables named: `cfg_enum`

**Data (found in its code).** reads data table(s) `ib_node`; writes `ib_node`

#### R06 — observationrecord.withdraw_observation

`iba/app/lib/observationrecord.py:235-241`

```python
def withdraw_observation(conn, observation_id: int, reason: str, reading_id, run_id: str, who: str) -> None:
    """The finding is wrong everywhere: its status withdrawn, the change kept (nothing overwritten)."""
    o = conn.execute("SELECT status FROM ib_observation WHERE id=?", (observation_id,)).fetchone()
    if o is None or o["status"] == "withdrawn":
        raise Refused(f"observation {observation_id} is not a live observation")
    log(conn, observation_id, None, "status", o["status"], "withdrawn", reason, reading_id, run_id, who)
    conn.execute("UPDATE ib_observation SET status='withdrawn', updated_at=? WHERE id=?", (_now(), observation_id))
```

**What it does.** Sets an observation's status to `withdrawn`, logging the change with its reason.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `ib_observation`; writes `ib_observation`

#### R07 — observationrecord.log

`iba/app/lib/observationrecord.py:213-220`

```python
def log(conn, observation_id: int, node_id: int | None, column: str, old, new, reason: str, reading_id, run_id: str,
        who: str) -> None:
    if len((reason or "").strip()) < 10:
        raise Refused(f"a change to observation {observation_id} needs its reason, in words (10 characters or more)")
    conn.execute("INSERT INTO ib_observation_change (observation_id, node_id, column_name, old_value, new_value, "
                 "reason, reading_id, run_id, created_by) VALUES (?,?,?,?,?,?,?,?,?)",
                 (observation_id, node_id, column, None if old is None else str(old),
                  None if new is None else str(new), reason.strip(), reading_id, run_id, who))
```

**What it does.** Writes `ib_observation_change`; refuses a reason under 10 characters.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** writes `ib_observation_change`

**Fixed in the code, not config.** The 10-character minimum.

#### R08 — observationrecord._now

`iba/app/lib/observationrecord.py:37-38`

```python
def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

**What it does.** UTC timestamp.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

## 8. Step 3 — the observe gate

`Reading.ps1 -Step Check -Label <label> -By ...` with the reading at `gathered`. Handler `reading:check`. G49 (the function `check`) is the same function quoted in step 2; here its second branch applies.

### 8.1 Elements K01 to K06



#### K01 — handlers.reading.check

`iba/app/handlers/reading.py:68-69`

```python
def check(ctx: Ctx) -> Outcome:
    return _write(ctx, lambda w: rd.check(ctx.cfg, w, ctx.params, ctx.run_id, PROJECT_ROOT))
```

**What it does.** Calls `reading.check` through the write wrapper.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** B04 (setting reading.focus_words, setting reading.non_characteristic_strongs, setting reading.surface_requirements)

**Data (found in its code).** none directly.

#### K02 — reading.check (observe gate, state gathered)

`iba/app/lib/reading.py:1183-1220`

```python
def check(cfg, w: nr.Writer, p: dict, run_id: str, root: pathlib.Path) -> str:
    conn = cfg.conn
    r = reading(conn, p.get("Label"))
    if r["state"] == "open":
        gaps = gate_pre(conn, root, r)
        if gaps:
            _gate_fail(r, "pre", gaps)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "gathered", "gathered_at": _now(),
                                                                      "run_id": run_id}))
        return f"reading {r['label']}: pre gate passed -- gathered (Reading.ps1 -Step Observe next)"
    if r["state"] == "gathered":
        gaps = gate_observe(cfg, root, r)
        if gaps:
            _gate_fail(r, "observe", gaps)

        def go():
            w.update("reading", {"id": r["id"]}, {"state": "observed", "observed_at": _now(), "run_id": run_id})
            w._grant("verse_meta")
            return versemeta.mark(conn, verse_ids(conn, r["id"]), "analysed")
        marked = nr._atomic(conn, go)
        return f"reading {r['label']}: observe gate passed -- observed; {marked} verse(s) marked analysed"
    if r["state"] == "observed":
        gaps = gate_post(cfg, root, r)
        if gaps:
            _gate_fail(r, "claims", gaps)
        path = _build_narrate(cfg, root, r)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {
            "state": "synergised", "synergised_at": _now(), "narrate_file": _rel(root, path), "run_id": run_id}))
        return (f"reading {r['label']}: claims gate passed -- synergised; narrate JSON built from the tables\n  -> "
                f"{_rel(root, path)}")
    if r["state"] == "synergised":
        gaps = gate_narrate(cfg, r)
        if gaps:
            _gate_fail(r, "narrate", gaps)
        nr._atomic(conn, lambda: w.update("reading", {"id": r["id"]}, {"state": "narrated", "narrated_at": _now(),
                                                                      "run_id": run_id}))
        return f"reading {r['label']}: narrate gate passed -- narrated (Reading.ps1 -Step Publish next)"
    raise Refused(f"reading {r['label']} is {r['state']}; Check runs at open, gathered, observed or synergised")
```

**What it does.** At `gathered`: runs `gate_observe` (K03); if no gaps, sets the reading to `observed` with the time, takes the grant on `verse_meta` and marks the reading's verses `analysed` (`versemeta.mark`). Writer grants for `reading.check`: `reading`, `verse_meta`.

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** B04 (setting reading.focus_words, setting reading.non_characteristic_strongs, setting reading.surface_requirements)

**Data (found in its code).** writes `reading`, `verse_meta`

#### K03 — reading.gate_observe

`iba/app/lib/reading.py:741-769`

```python
def gate_observe(cfg, root: pathlib.Path, r) -> list[str]:
    """Every surface in focus has what reading.surface_requirements asks (on a live finding, of this reading or an
    earlier one), or an open item or a reason (#2312); every finding in the file written; every node of this reading on
    a word holds its role."""
    if not r["observe_file"]:
        return ["no observe JSON yet (Reading.ps1 -Step Observe, then Record)"]
    data = _load(root, r["observe_file"], "the observe JSON")
    out = []
    conn = cfg.conn
    for v in data.get("verses") or []:
        vid = conn.execute("SELECT id FROM verse WHERE osisId=?", (v["osis"],)).fetchone()[0]
        by_occ = {}
        for wd in v.get("words") or []:
            by_occ[wd.get("occurrence")] = wd
        for s in surfaces_state(cfg, conn, vid):
            if not s["missing"]:
                continue
            rec = (by_occ.get(s["occurrence"]) or {}).get("record") or {}
            if (rec.get("reason") and len(rec["reason"].strip()) >= 10) or rec.get("item") or rec.get("added"):
                continue
            out.append(f"{v['verse']} {s['word']} ({', '.join(s['in_focus_as'])}): missing {', '.join(s['missing'])}; "
                       f"no open item, no reason (not_read)")
    for i, f in enumerate(data.get("findings") or []):
        if isinstance(f, dict) and not f.get("written"):
            out.append(f"findings[{i}] ({f.get('key')}): not written (run Record)")
    for n in conn.execute("SELECT id, observation_id FROM ib_node WHERE reading_id=? AND strong IS NOT NULL AND "
                          "verse_reference IS NOT NULL AND role IS NULL", (r["id"],)):
        out.append(f"node {n['id']} (observation {n['observation_id']}): no role (observation_part_missing)")
    return out
```

**What it does.** Needs an observe file. For each verse in it, recomputes `surfaces_state` from the tables (B04) and, for each surface still missing something, accepts a `reason` of 10 characters or more, an `item`, or an `added` mark in that word's `record` in the file; otherwise the gap `not_read`. Also a gap for every finding in the file not yet written, and for every node of this reading on a word with no role (`observation_part_missing`).

**Config read by this element (found in its code).** none directly.

**Config read below it, through the functions it calls (all levels; each has its own element).** B04 (setting reading.focus_words, setting reading.non_characteristic_strongs, setting reading.surface_requirements)

**Data (found in its code).** reads data table(s) `ib_node`, `verse`

**Fixed in the code, not config.** The 10-character minimum; the gap names `not_read` and `observation_part_missing`.

#### K04 — versemeta.mark

`iba/app/lib/versemeta.py:31-45`

```python
def mark(conn, verse_ids, status: str) -> int:
    """The reading process's coverage marks (#2172, build decision 3): a verse read is 'analysed', a
    verse the narrative cites is 'citated'; 'citated' replaces 'analysed' and is never stepped back,
    and 'exclude' is never overwritten. No commit (the caller's unit of work). Returns rows changed."""
    if status not in ("analysed", "citated"):
        raise ValueError(f"mark() sets analysed or citated, not {status!r}")
    now, n = _now(), 0
    for vid in set(verse_ids):
        r = conn.execute("SELECT status FROM verse_meta WHERE verse_id=? AND deleted=0", (vid,)).fetchone()
        if r is None or r[0] == "exclude" or _RANK.get(r[0], 3) >= _RANK[status]:
            continue
        conn.execute("UPDATE verse_meta SET status=?, status_changed_at=?, updated_at=? WHERE verse_id=?",
                     (status, now, now, vid))
        n += 1
    return n
```

**What it does.** Sets `verse_meta.status` to `analysed` for verses with no status; never steps back from `citated`; never overwrites `exclude`.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** reads data table(s) `verse_meta`; writes `verse_meta`

**Fixed in the code, not config.** The rank order.

#### K05 — versemeta: rank and now

`iba/app/lib/versemeta.py:28-28`

```python
_RANK = {None: 0, "analysed": 1, "citated": 2}
```

**What it does.** None < analysed < citated.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

**Fixed in the code, not config.** All.

#### K06 — versemeta._now

`iba/app/lib/versemeta.py:13-14`

```python
def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

**What it does.** UTC timestamp.

**Config read by this element (found in its code).** none directly.

**Data (found in its code).** none directly.

## 9. Not in Analysis_phase_1

- Reading.ps1 steps `Synergy`, `Apply`, `Narrate`, `Publish` and `Account`, and the `Check` branches for the states `observed` and `synergised` (`gate_post`, `_build_narrate`, `gate_narrate`). They are later steps. A `Check` run on a reading that is not at `open` or `gathered` is outside Analysis_phase_1.
- `narrativeregister.export` and `raise_unresolved`: the handlers call them only when asked to export or when a Writer holds unresolved references; none of the five steps does either.
- `escalation.update` branches for approval, reject, supersede, `_sync_threads_for`, `_restate_thread`, `_settle_thread_on_reject`: not reached by the thread update that Gather performs.
- `run.py` branches `report-stop` and `pause-continue`, and the crash escalation: reached only if a handler raises an uncaught exception or returns a condition other than `ok` or `refused`.
- Pre gap types in `reading.gap_types` with **no detector in the code**: `term_cluster`, `base_missing`, `term_reading_missing`. Open writes an empty section for each; no step checks them.
- Observe-phase gap types in `reading.gap_types` that no code in `iba/app/lib/reading.py` names: `observation_unsupported`.

## Appendix A — the config rows these steps read, as they stand on 2026-10-27

### A1 Work package and steps (`cfg_work_package`, `cfg_step`)

`reading`: ps_script `iba/app/ps/Reading.ps1`, chained 0, inactive 0.

| step | handler | kind | scope | inactive |
|---|---|---|---|---|
| reading.open | iba.app.handlers.reading:open | utility | none | 0 |
| reading.gather | iba.app.handlers.reading:gather | utility | none | 0 |
| reading.observe | iba.app.handlers.reading:observe | utility | none | 0 |
| reading.record | iba.app.handlers.reading:record | utility | none | 0 |
| reading.check | iba.app.handlers.reading:check | utility | none | 0 |

### A2 Failure routing (`cfg_on_fail`)

| step | condition | path |
|---|---|---|
| reading.check | refused | report-continue |
| reading.gather | refused | report-continue |
| reading.observe | refused | report-continue |
| reading.open | refused | report-continue |
| reading.record | refused | report-continue |

### A3 Write grants (`cfg_write_grant`)

| writer | tables |
|---|---|
| run | run, validation_result, word_registry |
| reading.open | reading, reading_verse |
| reading.gather | escalation_thread_item, escalation_thread_item_verse, ib_node, ib_observation, ib_observation_change, reading, reading_strand_hit |
| reading.observe | reading |
| reading.record | escalation_thread_item, escalation_thread_item_verse, ib_node, ib_observation, ib_observation_change, reading |
| reading.check | reading, verse_meta |
| escalation | escalation, escalation_history, escalation_thread_item, escalation_thread_item_response |

### A4 Settings (`cfg_setting`)

- `reading.output_dir`: `"outputs/reading"`

- `reading.gap_types`:

  - `term_cluster` — phase pre; records in ['cluster_strong']; guide: A term in scope with no cluster (term-cluster). Route it to the cluster assignment's recovery (Cluster-Assign.ps1) and name the row, or give the reason.
  - `meaning_missing` — phase pre; records in ['strong_meaning_tree', 'strong_lexicon']; guide: A term in scope with no meaning in one of the three sources (meaning tree; for Greek, Mounce and LSJ). Pull it through the spine route and name the row, or give the reason it is not needed.
  - `base_missing` — phase pre; records in ['span', 'strong']; guide: A verse or term in scope with a missing base datum (span, Strong's). Route it to its recovery (New-Word, raw.backfill_meaning, the spine); never work round it.
  - `term_reading_missing` — phase pre; records in ['ib_observation']; guide: A term in a verse of the scope with no term reading result: meaning in context, surface variants, related terms. Record it as an observation, measured against what is expected, not by presence.
  - `face_not_gathered` — phase pre; records in ['ib_observation', 'reading_strand_hit']; guide: A face recorded on a ledger strand hit that no face finding holds on that surface. Link it to the finding that holds it (the face with its observation), write the face finding, or give the reason. The face story is built in the claims.
  - `open_item` — phase pre; records in ['ib_observation', 'escalation_thread_item_response']; guide: An open item for the verse, found by the verse and through its surfaces' Strongs and clusters, whatever its subgroup; the item shows the subgroups it reaches. Read for what it asks, and record what the reading found. It is settled at the claim step.
  - `not_read` — phase observe; records in ['ib_observation']; guide: A word in focus (reading.focus_words: every M-code word, every qualifier, every negator) with no finding of this reading applied to it. Read the verse in its passage with every finding already applied to it in focus; apply a finding (an existing one, or a new one) to the word, raise an open item, or give the reason.
  - `observation_part_missing` — phase observe; records in ['ib_observation']; guide: A finding without what its kind needs: a node without the word's role; a party finding without its route; a qualification finding without both its qualifier and its characteristic. Presence of something that is not the right thing is not a resolved gap.
  - `observation_unsupported` — phase observe; records in ['ib_observation']; guide: A finding the verse no longer supports. Withdraw its node for this verse, or the finding everywhere, with the reason (ib_observation_change).
  - `observed_no_claim` — phase post; records in ['narrative_claim', 'ib_observation']; guide: A node of this reading with no disposition: carry its finding by a claim, hold it on an item, or dispose of it (data, context, withdrawn) with a reason. Checked against the claims (0.GAP post).
  - `claim_not_told` — phase narrate; records in ['narrative_claim_telling']; guide: A current claim no block tells: tell it in a block that fits its chapter's story, or hold it with a reason.
  - `claim_without_observation` — phase post; records in ['narrative_claim_source']; guide: A claim resting on verses only, with no observation behind it: give it its observation source.
  - `citation_without_record` — phase narrate; records in ['ib_observation', 'narrative_claim']; guide: A verse cited in a block with no observation and no claim behind it: record them.

- `reading.focus_words`: `{"function_word_morph": {"OT": ["HR", "HS", "HT", "HP", "HC", "AR", "AS", "AT", "AP", "AC"], "NT": ["P", "PREP", "R", "D", "I", "COND", "X", "F", "S", "PRT", "K", "C", "T", "CONJ"]}, "keep_tags": ["T5", "T6"], "applies": "the surfaces in focus at the Observe step (#2312): a surface is a word as written in the verse with its Strong (a verse_lexical occurrence). In focus: every content word; a function word is left out by its morph (function_word_morph: OT, the first two letters of the morph code; NT, the part before the first hyphen); negators and connectives (keep_tags) are kept; every M-coded word and every word in reading.non_characteristic_strongs is in focus (RG-03, RG-07, RG-22, RG-23, RG-24)."}`

- `reading.surface_requirements`: `{"role": true, "kinds": ["face", "term"], "silence_instead_of": ["face", "term"]}`

- `reading.non_characteristic_strongs`: `{"H4210": "superscription: 'Psalm' (mizmor)", "H7892": "superscription: 'Song' (shir)", "H5329": "superscription: 'to the choirmaster' (menatseach)", "H0341": "external adversary: 'enemy'", "H6862": "external adversary: 'foe, adversary'"}`

- `reading.observe_prompts`: `{"face": ["M0.1.1", "M0.1.3", "M0.4.1", "M0.5.1", "M0.5.2", "M0.5.3", "M0.5.4", "M0.5.11"], "qualification": ["M0.8.1"], "party": ["D5.2.1", "D7.1.1", "D7.2.1", "D7.3.1", "D7.4.1", "D7.5.1", "D7.6.1", "D7.7.1", "M0.7.9", "M0.7.11", "M0.7.12", "M0.7.13", "M0.7.14", "M0.7.15", "M0.7.16"], "statement": ["D1.1.1", "D2.1.1", "D3.1.1", "D6.1.1", "D10.1.1", "D10.2.1", "D10.3.1", "D10.4.1", "D10.6.1", "F0.1.1", "M0.7.1", "M0.7.2", "M0.7.3", "M0.7.4", "M0.7.6", "M0.7.7", "M0.7.8", "M0.7.10"], "link": ["D10.5.1", "M0.6.5", "M0.6.6", "M0.7.5"], "use": ["M0.6.1"], "term": ["M0.1.2", "M0.5.5", "M0.5.6", "M0.5.7", "M0.5.8", "M0.5.9"], "silence": []}`

- `reading.observation_parts`: `{"kinds": ["face", "qualification", "party", "statement", "link", "use", "term", "silence"], "finding": ["obs_text", "meaning", "implication", "basis", "tag", "route"], "node": ["verse_reference", "strong", "surface", "morph_code", "cluster_code", "role", "reading_id", "disposition", "disposition_note", "traced_observation_id", "question_code"], "rule": "one finding per description, applied by its nodes (#2273); the face, the qualification, the parties and the operation (statement) are findings, not columns"}`

- `verse_scope.max_verses`: `2500`

- `verse_scope.max_seconds`: `30`

- `verse_collate.max_seconds`: `120`

- `open_item.max_verses`: `200`

- `narrative.quote_min_words`: `2`

- `retention.snapshot_keep_count`: `5`

- `registry.strip_ends_pattern`: `"[^A-Za-z]"`

- `step.cap`: `60`

- `step.walk_start`: `"Gen.1.1"`

- `step.walk_end`: `"Rev.22.21"`

- `step.walk_max_iter`: `400`

- `discovery.particle_pattern`: `"^[HG]9\\d{3}$"`

- `step.span_html`: `"<span(?: var='[^']*')?(?: morph='([^']*)')? strong='([^']*)'>([^<]*)</span>"`

- `notification.header_run_id`: `"run_id       : {run_id}"`

- `notification.header_runs_over`: `"runs over    : {runs_over}"`

- `notification.header_step`: `"step         : {step}"`

- `notification.header_work_package`: `"work package : {work_package}"`

- `notification.not_initialised`: `"The app is not initialised. Run first:  iba\\app\\ps\\Start-Iba.ps1"`

- `notification.paused_banner_guided`: `"PAUSED — awaiting your decision. Answer with:\n  .\\Escalation.ps1 -Action AnswerRun -RunId {run_id} -Decision <Approve|Reject|Revise|Hold|Noted> [-Comment ...]\nthen re-run this exact command with -RunId {run_id} to act on the answer."`

- `notification.paused_banner_passthrough`: `"PAUSED — {message}"`

- `notification.step_result_line`: `"  {0,-20} {1,-14} {2}"`

- `notification.stopped_banner`: `"STOPPED — {message}"`

- `narrative.book_alias_map`: 194 aliases (read by VerseIndex)

### A5 Enums (`cfg_enum`)

- `reading_gap_type`: term_cluster, meaning_missing, base_missing, term_reading_missing, face_not_gathered, open_item, not_read, observation_part_missing, observation_unsupported, observed_no_claim, claim_not_told, claim_without_observation, citation_without_record
- `ib_observation.tag`: verse-grouping, difference-inference, surface-gloss-divergence, no-human-context, data-error, alternative-meaning, could-not-resolve, answered-no-flag, tightly-related, no-direct-connection, qualifier-for-term, no-impact, not-related-to-meaningful-word, sole-mcode-in-verse, cluster-pole-negative, cluster-pole-positive, attested-pre-nt, nt-coinage, needs_adjacent_verse_context, elevation-candidate, key-statement, face, link, party, qualification, silence, statement, term, use, subgroup-settlement, unfitted
- `ib_observation.basis`: read, stated
- `observation_route`: A, B, C
- `observation_role`: characteristic, qualifier, standalone
- `escalation_state`: raised, on-hold, closed, withdraw, completed, in-progress, supersede, re-assigned
- `escalation_state_open`: raised, in-progress, re-assigned
- `escalation_state_parked`: on-hold
- `escalation_state_terminal`: completed, closed, withdraw, supersede
- `escalation_assignee`: Claude, Researcher
- `escalation_thread_item_kind`: cluster, strong, verse, strand, chapter, event, researcher, escalation, scope
- `escalation_thread_item_response_kind`: touched, narrowed, forward, ruling, note, closed, reopened, withdrawn, superseded
- `escalation_thread_item_status`: open, closed, withdrawn, superseded
- `escalation_next_action_manual`: ready_for_approval, approved, reject, revise, noted, review

### A6 Escalation engines used by `escalation.update` (thread path)

`cfg_escalation_requirement`, action `update`, active rows:

- field `state`, condition `has_content`, check `not_raised_with_content`
- field `next_action_assigned_to`, condition `always`, check `reassign_to_researcher_requires_ready_for_approval`
- field `state`, condition `thread_type`, check `no_open_thread_items`
- field `state`, condition `always`, check `readings_published`

`cfg_escalation_transition`, shape `manual`, active rows in priority order:

- priority 0: next_action None, condition `thread_items_changed_and_referenced` -> `thread, T3/T5`
- priority 0: next_action None, condition `thread_items_changed_partly_closed` -> `thread, T6`
- priority 0: next_action None, condition `thread_items_all_settled` -> `thread: every item settled`
- priority 1: next_action approved, condition `needs_followup` -> `next_action=approved+needs_claude_followup`
- priority 2: next_action approved, condition `has_resolution` -> `next_action=approved`
- priority 2: next_action reject, condition `always` -> `__explicit__`
- priority 3: next_action revise, condition `always` -> `next_action=revise`
- priority 4: next_action noted, condition `always` -> `next_action=noted`
- priority 5: next_action ready_for_approval, condition `always` -> `no more specific rule`
- priority 5: next_action None, condition `followup_cleared_was_approved` -> `next_action=approved`
- priority 6: next_action None, condition `explicit_state_given` -> `__unchanged__`
- priority 6: next_action None, condition `thread_reassigned` -> `__unchanged__`
- priority 7: next_action None, condition `assignee_changed` -> `no more specific rule`
- priority 8: next_action None, condition `always` -> `__unchanged__`

## 10. Facts this description exposes (stated from the code above; nothing changed)

These are for the requirements sheet that follows. They are facts about the code, not proposals.

1. `observationrecord.write` inserts `ib_node` rows without the column `cluster_subgroup_code` (element G17), so it stays empty on every node a run writes.
2. `observationrecord.check` (G13) is the whole validation of a finding. It checks form: kind, text present and not a bare negation, basis, route, role, cluster, quotations found in the ESV. No code compares the *content* of a finding to a requirement (for example that a term finding takes its meaning from the meaning sources, or that a face finding says what differs from the word's other occurrences).
3. `gate_pre` (G50) checks that every item has a record that exists, or a reason. It does not check that the record answers the item.
4. When a verse holds two occurrences with the same Strong and the same surface, `resolve_occurrence` (G19) returns the first, so every node written for that pair names the first occurrence; the second occurrence can never receive a node from these steps. `_has_on_surfaces` (B06) matches a node without an occurrence id only when the match in the verse is unique.
5. `recordingpass.py`'s own header says only that module writes `ib_observation` and `ib_node`; `observationrecord.write` (G17) inserts into both directly.
6. Values fixed in code and not in config appear under 'Fixed in the code' on each element; among them the minimum of 10 characters for a reason or response, 15 for an open item's purpose fields, the passage window of two verses, the bare-negation word list, the 60-line cap on a refusal, the 20-snapshot fallback, and the registry of pre detectors.
7. Each Reading.ps1 call takes a database snapshot (C09, C17) and prunes to `retention.snapshot_keep_count`. This is the behaviour behind escalation #2301.
8. `reading.open_` (O02) refuses an anchoring escalation whose state is `completed`, `closed` or `withdrawn`. The terminal states in `cfg_enum` `escalation_state_terminal` are `completed`, `closed`, `withdraw` and `supersede` (appendix A5): a state `withdraw` or `supersede` is not refused by that test.

## 11. What I need from the researcher

Q1, Q2 and Q3 above. Then the requirements sheet: for each of the three steps, what it must check and write into `ib_observation` and `ib_node`, with sources, to be brought as a decision (B:105). I will not start it until Q1 to Q3 are answered.

