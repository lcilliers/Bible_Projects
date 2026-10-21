"""withdraw_stale_word_level_observations_v1_20260923.py — ONE-OFF migration, escalation #1856.

Researcher's own decision (v3, verbatim): "my expectation is that a rerun will automatically reset
all the items that is wrong. As long as the code doesn't automatically skip some stuff that should
be revisited." Verified (v4): as coded, it WOULD skip them -- `fully_covered_verse_ids`
(stage1coverage.py) treats a verse as fully covered purely on "does a live, non-withdrawn node
exist," with no concept of whether that node predates the 2026-09-23 span-grounding fix. This
migration makes the researcher's own stated condition true: withdraw every stale pre-fix word-level
(M0.1.x/M0.5.x, excluding M0.5.11 which is a correctly-behaved per-occurrence question, not
word-level) observation, so the SAME existing coverage-check machinery correctly treats them as
not-yet-answered -- a normal (non-Force) future rerun then naturally re-derives them under the
corrected mechanism. No code change, no new mechanism -- a status correction that lets the already-
approved design actually do what it was approved to do.

Soft-delete only (status='withdrawn'), matching the project's own no-physical-delete convention --
fully reversible, no ib_node rows touched (coverage checks already join through ib_observation.status,
so withdrawing the observation alone is sufficient).

Idempotent (only touches non-withdrawn rows) -- a second run is a no-op.

    python -m iba.app.migration.withdraw_stale_word_level_observations_v1_20260923
"""
from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

from ..lib.cfg import DB_PATH

_WHERE = (
    "(question_code LIKE 'M0.1%' OR question_code LIKE 'M0.5%') "
    "AND question_code != 'M0.5.11' AND status != 'withdrawn'"
)


def apply_fix(conn: sqlite3.Connection) -> list[str]:
    before = conn.execute(f"SELECT COUNT(*) FROM ib_observation WHERE {_WHERE}").fetchone()[0]
    if before == 0:
        return ["no-op -- 0 stale word-level observations found (already applied)"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute(f"UPDATE ib_observation SET status='withdrawn', updated_at=? WHERE {_WHERE}", (now,))
    after = conn.execute(f"SELECT COUNT(*) FROM ib_observation WHERE {_WHERE}").fetchone()[0]
    m5_11_untouched = conn.execute(
        "SELECT COUNT(*) FROM ib_observation WHERE question_code='M0.5.11' AND status != 'withdrawn'"
    ).fetchone()[0]
    return [
        f"withdrawn: {before} stale word-level observations",
        f"remaining non-withdrawn (should be 0): {after}",
        f"M0.5.11 untouched, still live (should be unchanged): {m5_11_untouched}",
    ]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_fix(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
