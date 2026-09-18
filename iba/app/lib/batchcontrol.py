"""batchcontrol.py — the single writer for `run_batch` (escalation #1756, researcher-approved
design 2026-09-18). Every long-running LLM-calling step wraps its own API-call-plus-write unit
with `start_batch()` before the call and `commit_batch()`/`fail_batch()` after, and checks
`already_committed()` before spending on a batch a prior run may have already paid for.

**Resume/skip**: `already_committed(conn, step, selector_key, content_key)` is keyed on
`(step, selector_key, batch_content_key)` — deliberately NOT `run_id`-scoped, so a brand-new run
can see and skip work a PRIOR, unrelated run_id already committed. `content_key()` hashes the
batch's own actual item list (verse ids, member strongs, whatever the caller is batching), not
its ordinal position — a resume stays correct even if the selector's underlying item list shifts
between runs (e.g. a `cluster_strong` reassignment changes which verses belong to a cluster).

**Crash safeguard**: `start_batch()` writes `status='running'` and commits immediately, before the
API call — so a process that dies mid-batch (crash, kill, power loss) leaves that row visibly
`running` with no later `committed`/`failed` update. That is itself the evidence of a dead run;
nothing else needs to detect it separately.

**Progress monitor**: because every batch's `running`/`committed`/`failed` transition is its own
committed row, `run_batch` can be queried live, mid-run, from a separate connection (as
`BatchProgress.ps1` does) without waiting for the run to finish or reading process stdout.

**The resume/skip key above is an APPLICATION-level guarantee, not a schema one** — found live
minutes after this shipped (escalation #1758, `fix_run_batch_unique_constraint_v1_20260918.py`):
a `UNIQUE(step, selector_key, batch_content_key)` constraint on the table was tried first, but it
blocked a legitimate retry after a transient failure (the same content_key, a genuine second
attempt) with an `IntegrityError`, not just a genuine duplicate. `already_committed()`'s own
`WHERE status='committed'` check, consulted BEFORE `start_batch()` runs, is what actually prevents
re-paying for already-committed work — `start_batch()` itself always inserts a fresh row per
attempt, on purpose, so a retry history stays visible in the table rather than being blocked.
"""

from __future__ import annotations

import datetime
import hashlib


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def content_key(items: list[str]) -> str:
    """Stable hash of a batch's own item list (e.g. verse ids as strings, or member strongs).
    Order-independent (sorted before hashing) -- the same set of items always hashes the same,
    regardless of the order the caller happened to build the list in. Truncated to 16 hex chars:
    collision risk is irrelevant here (the UNIQUE constraint is (step, selector_key,
    batch_content_key) together, not this alone; a false-positive skip would need a genuine
    SHA-256 collision within one step+selector's own batch history, not a real-world risk at this
    scale)."""
    joined = ",".join(sorted(str(i) for i in items))
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()[:16]


def already_committed(conn, step: str, selector_key: str, batch_content_key: str) -> bool:
    """True if this exact batch (by content, not position) already has a committed row under this
    step+selector, from ANY run_id. The caller should skip the API call entirely when this is
    true."""
    row = conn.execute(
        "SELECT 1 FROM run_batch WHERE step=? AND selector_key=? AND batch_content_key=? "
        "AND status='committed'",
        (step, selector_key, batch_content_key)).fetchone()
    return row is not None


def start_batch(conn, run_id: str, work_package: str, step: str, selector_key: str,
                batch_ordinal: int, batch_content_key: str) -> int:
    """Writes status='running' and commits immediately -- deliberately a separate commit from the
    caller's own transaction, so this row is visible to a concurrent monitor query and survives a
    crash in the API call or the write that follows, which is the whole point of writing it
    BEFORE the risky work starts, not after."""
    cur = conn.execute(
        "INSERT INTO run_batch (run_id, work_package, step, selector_key, batch_ordinal, "
        "batch_content_key, status, started_at) VALUES (?,?,?,?,?,?,?,?)",
        (run_id, work_package, step, selector_key, batch_ordinal, batch_content_key, "running",
         _now()))
    conn.commit()
    return cur.lastrowid


def commit_batch(conn, batch_id: int, cost_usd: float | None = None) -> None:
    conn.execute(
        "UPDATE run_batch SET status='committed', ended_at=?, cost_usd=? WHERE id=?",
        (_now(), cost_usd, batch_id))
    conn.commit()


def fail_batch(conn, batch_id: int, error_message: str) -> None:
    conn.execute(
        "UPDATE run_batch SET status='failed', ended_at=?, error_message=? WHERE id=?",
        (_now(), error_message, batch_id))
    conn.commit()
