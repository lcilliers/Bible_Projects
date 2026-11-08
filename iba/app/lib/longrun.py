"""longrun -- the progress control every long job against the Ollama server uses (researcher, #2388, 2026-11-08: "the ollama processes should always have a
proper progress control method to check on progress").

A long job keeps three files under Logs/longrun/, named by the job: <job>.progress.json (rewritten after every step and every 30 s while it waits or
works, so a reader can tell a live job from a dead one), <job>.stop (the flag a stop asks by) and <job>.log. `Progress` reads the first, `Stop` writes the
second, and a job started again with the same name resumes from what the progress file records as done. The machine is kept from idle sleep while the
job runs (Windows SetThreadExecutionState; the display may still sleep). Closing the lid or sleeping the machine by hand still ends it.

Used by iba/app/tools/collection_batch_run.py; any later Ollama job calls the same functions."""
from __future__ import annotations

import json
import os
import pathlib
import threading
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
DIR = ROOT / "Logs" / "longrun"
LIVE_STATES = ("starting", "running", "waiting")


def iso(t: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(t))


def paths(job: str) -> dict:
    DIR.mkdir(parents=True, exist_ok=True)
    return {"progress": DIR / f"{job}.progress.json", "stop": DIR / f"{job}.stop", "log": DIR / f"{job}.log"}


def read(job: str) -> dict | None:
    p = paths(job)["progress"]
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):  # being replaced at this moment
        return None


def alive(prog: dict | None, stale_after: float = 120) -> bool:
    """Running when the file says a live state and moved within stale_after seconds (a step in hand can take longer, so the job beats every 30 s)."""
    return bool(prog) and prog.get("state") in LIVE_STATES and time.time() - prog.get("updated_epoch", 0) < stale_after


def keep_awake(on: bool) -> None:
    if os.name == "nt":
        import ctypes
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000001 if on else 0x80000000)


class Job:
    """with Job(name, total) as j: j.write(current=..); j.step_done(..); j.stop_asked(). The progress file always carries pid, state, counts, the item in
    hand, a mean and an ETA. Set j.prog['state'] to finished, stopped or halted before leaving the block."""

    def __init__(self, job: str, total: int, done: int = 0, extra: dict | None = None):
        self.job, self.p = job, paths(job)
        self.prog = {"job": job, "pid": os.getpid(), "started_at": iso(time.time()), "total": total, "done": done, "skipped": 0, "failed": 0,
                     "current": None, "current_since": None, "last_error": None, "state": "starting"}
        self.prog.update(extra or {})
        self.secs: list[float] = []
        self._lock = threading.Lock()
        self._end_beat = threading.Event()

    def __enter__(self):
        if alive(read(self.job)):
            raise RuntimeError(f"job {self.job} is running (its progress moved less than 120 s ago): stop it first with Stop, or wait")
        self.p["stop"].unlink(missing_ok=True)
        keep_awake(True)
        self.write("running")
        threading.Thread(target=self._beat, daemon=True).start()
        return self

    def __exit__(self, *exc):
        self._end_beat.set()
        keep_awake(False)
        self.prog["current"] = None
        self.write(self.prog["state"] if self.prog["state"] in ("finished", "stopped", "halted") else "stopped")
        return False

    def _beat(self):
        while not self._end_beat.wait(30):
            self.write()

    def stop_asked(self) -> bool:
        return self.p["stop"].exists()

    def step_done(self, secs: float, ok_: bool = True, skipped: bool = False, error: str | None = None):
        with self._lock:
            if skipped:
                self.prog["skipped"] += 1
            elif ok_:
                self.prog["done"] += 1
                self.secs.append(secs)
            else:
                self.prog["failed"] += 1
                self.prog["last_error"] = error
        self.write()

    def write(self, state: str | None = None, **kw):
        with self._lock:
            pr = self.prog
            if state:
                pr["state"] = state
            pr.update(kw)
            now = time.time()
            recent = self.secs[-20:]
            mean = sum(recent) / len(recent) if recent else None
            left = pr["total"] - pr["done"] - pr["skipped"] - pr["failed"]
            pr.update(updated_at=iso(now), updated_epoch=now, left=left, mean_secs_last_20=round(mean, 1) if mean else None,
                      estimated_finish=iso(now + left * mean) if mean and left else None,
                      estimate_note="items left at the recent mean seconds per item; the first items may run faster or slower than later ones")
            tmp = self.p["progress"].with_suffix(".tmp")
            try:
                tmp.write_text(json.dumps(pr, indent=1), encoding="utf-8")
                os.replace(tmp, self.p["progress"])
            except OSError:  # a reader has the file this instant; the next write succeeds
                pass


def summary(job: str) -> str:
    p = read(job)
    if not p:
        return f"no progress file for job {job}: it has not been started (Logs/longrun/{job}.progress.json)"
    live = alive(p)
    head = f"{job}: {p['state']}"
    if not live and p["state"] in LIVE_STATES:
        head += " -- NOT running: the file has not moved for over 2 minutes (the job was interrupted, for example by the machine sleeping); start it again to resume"
    lines = [head, f"done {p['done']} of {p['total']}, skipped {p['skipped']}, failed {p['failed']}, left {p.get('left')}",
             f"in hand: {p.get('current')} since {p.get('current_since')}",
             f"mean seconds per item (last 20): {p.get('mean_secs_last_20')}; estimated finish: {p.get('estimated_finish')}",
             f"started {p['started_at']}, last update {p['updated_at']}, process id {p['pid']}"]
    if p.get("last_error"):
        lines.append(f"last problem: {p['last_error']}")
    return "\n".join(lines)
