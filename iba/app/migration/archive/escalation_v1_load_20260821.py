"""escalation_v1_load_20260821.py — D1 EXECUTE, run 2026-08-21. ALREADY RUN — this file is the
permanent record of what was done, per the project's own convention that every real DB mutation
has a committed script, not just a scratchpad one. Re-running it will fail its own guard (the id
sequence is no longer at 10) and must not be forced past that guard blindly.

Loads `iba/app/reports/escalation-v1-snapshot-20260821.json` (built by
`escalation_v1_snapshot_20260821.py`) through the REAL front door — `escalation.raise_new()` +
`escalation.update()`, the same functions `Escalation.ps1 -Action Raise/Update` call — reseeding
the id sequence 10 -> 735 first so all 25 items land on their EXACT original `escalations_old`-era
numbers (736-760), matching every `#7xx` citation already written across `BUILD.md`/
`GOVERNANCE.md`/this session's own commits.

**Judgement calls made this run** (researcher: "my aim is not necessarily to get these 25 items
perfect, just to ensure that we do not miss anything that still need attention"):
  - `#741`/`#742`/`#751`/`#752` — `type=notice` WITH a `resolution` already recorded (genuinely
    done). `raise_new()` auto-closes a notice and can't set `resolution` at creation, so the
    resolution text is folded into `comment` instead, not silently dropped.
  - `#749` — `type=notice`, NO resolution (genuinely still open/undecided). Raising it as `notice`
    would auto-close it, silently losing the fact it was never actually decided — the one thing
    this load exists to avoid. Raised as `task` instead, so it stays visibly open.
  - `#1`, `#756` — originally DISPATCHER-TIED pauses (`run_id` starts `RUN-`, not `MANUAL-`), both
    still unresolved. The runs they were tied to no longer exist, so `AnswerRun` can never reach
    them again — raised as manual `issue`s instead, so the substance stays visible and actionable.
  - `#750`/`#753` — `re-assigned`, no resolution. `ready_for_approval` now requires a resolution
    (this session's own D25 fix) — left at `raised`/`review` rather than forcing a state they can't
    legitimately reach.
  - `#1` also had no `originator` at all (a dispatcher pause only gets one at ANSWER time, never at
    raise) and no `comment` (dispatcher pauses carry their question in `context`, not `comment`).
    `originator` used `"Claude"` — the real originator of THIS load transaction, not a guess about
    who raised the original; `comment` derived from `context`'s own `full_message`.

**Result, verified with a fresh connection after commit** (not the same process's view): all 25
items present, every id exact (736-760), `configmaint.validate` clean (0 hard errors), 21 open
escalations live. `escalation.list`'s D15 sections show only the expected finding — `missing_link`
hits for historical `escalations_old` cross-references (`#650` etc.), which correctly can't resolve
since that table is untouched by design (D1's own "not a copy, a conversion" framing).

    python -m iba.app.migration.escalation_v1_load_20260821
"""

from __future__ import annotations

import json
import pathlib
import sqlite3

from ..lib.cfg import Cfg, DB_PATH
from ..lib.db import Db
from ..lib import escalation as esc

SNAPSHOT_PATH = pathlib.Path("iba/app/reports/escalation-v1-snapshot-20260821.json")

# old_id -> override type (notice -> something that stays open when there's genuinely no
# resolution yet; dispatcher-tied originals raised as manual issues since the runs they were
# tied to no longer exist).
TYPE_OVERRIDE = {749: "task", 1: "issue", 756: "config"}   # 756 unchanged, listed for clarity

# old_id -> the follow-up update() call needed to reach the item's real recorded state
# (raise_new() alone only ever produces raised/review or the notice special case).
FOLLOWUP: dict[int, dict] = {
    740: dict(next_action="noted"),
    743: dict(next_action="approved"),
    744: dict(next_action="approved"),
    745: dict(next_action="approved"),
    747: dict(next_action="approved"),
    754: dict(state="in-progress"),
    757: dict(next_action="approved"),
    759: dict(next_action="ready_for_approval"),
}
# 750/753 deliberately have NO follow-up entry -- see module docstring.
NOTICE_FOLD_RESOLUTION = (741, 742, 751, 752)
FOLD_TRIED_INTO_CONTEXT = (1, 756)


def main() -> None:
    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))

    conn_check = sqlite3.connect(DB_PATH)
    cur_seq = conn_check.execute(
        "SELECT seq FROM sqlite_sequence WHERE name='escalation'").fetchone()[0]
    conn_check.close()
    if cur_seq != 10:
        raise RuntimeError(
            f"expected escalation sqlite_sequence at 10 (this session's live #1-10, pre-load), "
            f"found {cur_seq} -- this script has already run, or the live table has moved since "
            f"this record was written. Refusing to run blindly a second time.")

    cfg = Cfg()
    db = Db(cfg)
    db.conn.execute("UPDATE sqlite_sequence SET seq=735 WHERE name='escalation'")
    print("reseeded escalation sqlite_sequence: 10 -> 735")

    results = []
    for item in snapshot["items"]:      # already in raised_at (chronological) order -- #1 is
                                        # LAST (built that way by escalation_v1_snapshot's own
                                        # sort). Do NOT re-sort by old_id -- that puts #1 first
                                        # and shifts every other item's id by one.
        old_id = item["old_id"]
        kw = dict(item["raise_new_kwargs"])
        etype = TYPE_OVERRIDE.get(old_id, kw.pop("etype"))
        kw.pop("etype", None)

        if old_id in NOTICE_FOLD_RESOLUTION:
            res = item["row"]["resolution"]
            if res:
                kw["comment"] = (f"{kw['comment']}\n\n[resolution, folded in at load time -- "
                                f"notice-type items can't carry a separate resolution column: "
                                f"{res}]")
        if old_id in FOLD_TRIED_INTO_CONTEXT:
            tried = item["row"]["tried"]
            if tried:
                ctx = kw.get("context") or ""
                kw["context"] = (f"{ctx}\n\n[tried, folded in at load time -- can't be set "
                                f"post-raise while the item stays open (D26): {tried}]").strip()

        if not kw.get("comment"):
            derived = None
            if kw.get("context"):
                try:
                    derived = json.loads(kw["context"]).get("full_message")
                except (json.JSONDecodeError, AttributeError):
                    pass
            kw["comment"] = derived or kw["short_description"]
            print(f"  (old #{old_id}: comment was empty, derived from context/short_description)")

        originator = kw["originator"]
        if not originator:
            originator = "Claude"
            print(f"  (old #{old_id}: originator was empty in the export -- using 'Claude' as "
                 f"this load transaction's real originator, not a guess about the original)")

        new_id = esc.raise_new(cfg, db, kw.pop("short_description"), kw.pop("source"),
                               etype=etype, comment=kw.get("comment"), context=kw.get("context"),
                               related_activity=kw.get("related_activity"),
                               assigned_to=kw.get("assigned_to"), from_id=kw.get("from_id"),
                               originator=originator)

        followup_msg = None
        if old_id in FOLLOWUP:
            f = FOLLOWUP[old_id]
            row = item["row"]
            upd_kwargs = dict(originator=row["originator"])
            if "next_action" in f:
                upd_kwargs["next_action"] = f["next_action"]
            if "state" in f:
                upd_kwargs["state"] = f["state"]
            if row["resolution"]:
                upd_kwargs["resolution"] = row["resolution"]
            if row["tried"] and old_id not in FOLD_TRIED_INTO_CONTEXT:
                upd_kwargs["tried"] = row["tried"]
            followup_msg = esc.update(cfg, db, new_id, **upd_kwargs)

        results.append((old_id, new_id, followup_msg))
        print(f"old #{old_id} -> new #{new_id}" + (f" | {followup_msg}" if followup_msg else ""))

    db.close()   # commits -- Db.close() commits then closes; Cfg.close() alone does NOT commit
    print(f"\n{len(results)} items loaded, committed for real.")


if __name__ == "__main__":
    main()
