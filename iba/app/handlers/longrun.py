"""longrun handlers -- work package `long-run` (escalation #2388), one step per Long-Run.ps1 action: the progress control of every long job against the
Ollama server (lib/longrun.py).

Plan writes the job's plan (for collection-batch: one seed word per sub-group of the bases not yet in a collection). Start launches the job detached through
Windows' process service (rule B:125), so the Claude app closing does not end it; the job keeps the machine from idle sleep while it runs. Progress reads the
job's progress file (read-only). Stop writes the stop flag; the job ends after the item in hand and a Start resumes it. An unknown job, a job already running
or a bad -Limit is the routed condition 'refused' and nothing is started. No setting is read: the job's few fixed values are named in
iba/app/tools/collection_batch_run.py."""
from __future__ import annotations

import shutil
import subprocess
import sys

from ..lib import longrun as lr
from .base import Ctx, Outcome, fail, ok

JOBS = {"collection-batch": "iba.app.tools.collection_batch_run"}


def _pwsh() -> str:
    return shutil.which("pwsh") or r"C:\Program Files (x86)\PowerShell\7\pwsh.exe"


def _job(ctx: Ctx):
    job = str(ctx.params.get("Job") or "").strip()
    if job not in JOBS:
        return None, fail("refused", f"-Job {job!r} is not a known job: {', '.join(sorted(JOBS))}")
    return job, None


def plan(ctx: Ctx) -> Outcome:
    job, err = _job(ctx)
    if err:
        return err
    r = subprocess.run([sys.executable, "-m", JOBS[job], "--job", job, "--plan"], cwd=lr.ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return fail("refused", f"the plan could not be made: {(r.stderr or r.stdout).strip()[-300:]}")
    return ok(r.stdout.strip())


def start(ctx: Ctx) -> Outcome:
    job, err = _job(ctx)
    if err:
        return err
    if lr.alive(lr.read(job)):
        return fail("refused", f"job {job} is running (its progress moved less than 120 s ago): Progress shows it; Stop ends it")
    limit = str(ctx.params.get("Limit") or "").strip()
    if limit and not limit.isdigit():
        return fail("refused", f"-Limit is a whole number, not {limit!r}")
    lim = f" --limit {limit}" if limit else ""
    console = lr.paths(job)["log"].with_suffix(".console.log")
    inner = f"& '{sys.executable}' -m {JOBS[job]} --job {job} --run{lim} *> '{console}'"
    command_line = f'"{_pwsh()}" -NoProfile -Command "{inner}"'
    ps = ("$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{ CommandLine = '" + command_line.replace("'", "''")
          + "'; CurrentDirectory = '" + str(lr.ROOT) + "' }; \"$($r.ReturnValue) $($r.ProcessId)\"")
    r = subprocess.run([_pwsh(), "-NoProfile", "-Command", ps], capture_output=True, text=True, encoding="utf-8", errors="replace")
    parts = r.stdout.split()
    if r.returncode != 0 or len(parts) != 2 or parts[0] != "0":
        return fail("refused", f"the job could not be started: {(r.stderr or r.stdout).strip()[-300:]}")
    return ok(f"started job {job}, process id {parts[1]}; its console is {console}. Watch it with Long-Run.ps1 -Action Progress -Job {job}", pid=int(parts[1]))


def progress(ctx: Ctx) -> Outcome:
    job, err = _job(ctx)
    if err:
        return err
    return ok(lr.summary(job))


def stop(ctx: Ctx) -> Outcome:
    job, err = _job(ctx)
    if err:
        return err
    prog = lr.read(job)
    if not lr.alive(prog):
        return ok(f"job {job} is not running ({prog['state'] if prog else 'no progress file'}): nothing to stop")
    lr.paths(job)["stop"].write_text("stop", encoding="utf-8")
    return ok(f"stop asked for job {job}: it ends after the item in hand (a collection takes about 12 minutes). Start resumes it")
