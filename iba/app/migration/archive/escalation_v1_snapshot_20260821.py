"""escalation_v1_snapshot_20260821.py — D1, STRATEGY CHANGED 2026-08-21 (researcher, direct
instruction, replacing `rebuild_escalation_from_export_20260821.py`'s versioned-replay approach):
"trying to fix all the issues and use versioning will create more problems. lets change the D1
strategy. add the current values of each item as v1."

**What changed and why.** The versioned-replay dry run (raise v1, then replay every historical
`escalation_history` version as its own `update()` call) surfaced two real, escalating problems
before any data was written: (1) `update()` cannot correct `short_description` at all (escalation
#10); (2) 22 of the 25 items have at least one point where `comment`/`context` was genuinely
REPLACED, not appended to (the #759 "column-spec correction" wave) — `update()` has no replace mode
for those fields either, so a literal increment-by-increment replay would permanently contaminate
the final `comment`/`context` with stale pre-correction text. Chasing a byte-perfect version-by-
version reconstruction through mechanisms that don't support it was creating MORE problems than it
solved. New strategy: each item becomes ONE v1 row, holding its CURRENT (already-final) values --
no replay, no delta reconstruction, no append/replace ambiguity. The full historical journey is not
lost: `escalation-export-20260820.json` + `escalation_history-export-20260820.json` remain archived
verbatim, permanently, as the complete narrative record for anyone who needs it.

**Source**: `escalation-export-20260820.json` ONLY (25 rows) -- this is the `escalation` table's own
CURRENT-STATE-ONLY snapshot at export time (2026-08-20T11:34:34Z), already holding every field's
FINAL value (e.g. #736's `short_description` is already `'Main-Project / IBA Filing
Consolidation'`, the fully-corrected title, not the original 324-char text) -- confirmed directly,
not assumed. `escalation_history-export-20260820.json` (97 rows) is NOT read by this script at all;
it stays archived for provenance only. This session's own live rows (`escalation` as it stands now,
`#1`-`#9`) are appended after, read directly from the live table -- also single-row, no history
concern.

**Output**: `escalation-v1-snapshot-20260821.json` -- one row per item, EVERY `escalation` column
named explicitly, ready for the researcher to choose between (their own words): "the standard
system to process corrections" (raise_new() + whatever update() call(s) reach the target
state/resolution -- `standard_system_note` on each item names what that would take, since
raise_new() alone can only produce `state='raised'`/`next_action='review'` or the `notice` special
case) or "straight edits in the json to prepare the data" (hand-edit the `row` dict directly).
Nothing is written to the DB by this script -- read-only, same discipline as the dry run it
replaces.

    python -m iba.app.migration.escalation_v1_snapshot_20260821
"""

from __future__ import annotations

import json
import pathlib

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib import escalation as esc

EXPORT_PATH = pathlib.Path("iba/app/db/archive/escalation-export-20260820.json")

# escalation columns raise_new() CAN set directly, one call, at creation.
_RAISE_NEW_SETTABLE = ("short_description", "source", "type", "comment", "context",
                       "related_activity", "next_action_assigned_to", "from_id")
# escalation columns raise_new() CANNOT set -- always fixed at creation (state='raised'/
# next_action='review', or the notice special case; resolution/tried always None).
_RAISE_NEW_FIXED = ("state", "next_action", "resolution", "tried")


def _standard_system_note(row: dict) -> str | None:
    """What, beyond a single raise_new() call, 'the standard system' would need to reach this
    item's actual current state/resolution/tried -- None if raise_new() alone already produces it
    (a plain raised/review item, or a notice)."""
    if row["type"] == "notice":
        if row["state"] == "closed" and row["next_action"] is None:
            return None
        return (f"type=notice but state={row['state']!r}/next_action={row['next_action']!r} -- "
               f"raise_new() would create it closed/None; does not match this row as exported, "
               f"needs a look")
    if row["state"] == "raised" and row["next_action"] == "review" and not row["resolution"] \
            and not row["tried"]:
        return None                                     # exactly what raise_new() produces
    needs = []
    if row["resolution"]:
        needs.append(f"resolution={row['resolution']!r} (raise_new() always sets None)")
    if row["tried"]:
        needs.append(f"tried={row['tried']!r} (raise_new() always sets None)")
    if row["state"] != "raised" or row["next_action"] not in ("review", None):
        needs.append(f"state={row['state']!r}/next_action={row['next_action']!r} -- reached via "
                    f"a follow-up update() call (e.g. next_action='approved' with resolution "
                    f"present -> completed; 'noted' -> closed; 'reject'+state='withdraw'/"
                    f"'supersede' -> that state; 'ready_for_approval' -> re-assigned)")
    return "; ".join(needs) if needs else None


def build_snapshot() -> dict:
    export = json.loads(EXPORT_PATH.read_text(encoding="utf-8"))
    cfg = Cfg()
    db = Db(cfg)

    next_id = 736
    items = []
    for r in sorted(export["rows"], key=lambda r: r["raised_at"]):
        row = {
            "short_description": r["short_description"], "source": r["source"],
            "type": r["type"], "context": r["context"], "comment": r["comment"],
            "tried": r["tried"], "state": r["state"], "next_action": r["next_action"],
            "next_action_assigned_to": r["next_action_assigned_to"],
            "originator": r["originator"], "resolution": r["resolution"],
            "related_activity": r["related_activity"], "from_id": None,
        }
        title_err = esc._title_shape_error(row["short_description"])
        raise_new_kwargs = {
            "short_description": row["short_description"], "source": row["source"],
            "etype": row["type"], "comment": row["comment"], "context": row["context"],
            "related_activity": row["related_activity"],
            "assigned_to": row["next_action_assigned_to"], "from_id": row["from_id"],
            "originator": row["originator"],
        }
        items.append({
            "old_id": r["id"],
            "proposed_new_id": next_id,
            "title_shape_error": title_err,
            "row": row,
            "raise_new_kwargs": raise_new_kwargs,
            "standard_system_note": _standard_system_note(row),
        })
        next_id += 1

    live_rows = []
    for r in db.rows("SELECT * FROM escalation ORDER BY id"):
        row = {k: r[k] for k in ("short_description", "source", "type", "context", "comment",
                                 "tried", "state", "next_action", "next_action_assigned_to",
                                 "originator", "resolution", "related_activity", "from_id")}
        live_rows.append({
            "old_id_this_session": r["id"],
            "proposed_new_id": next_id,
            "title_shape_error": esc._title_shape_error(row["short_description"]),
            "row": row,
            "raise_new_kwargs": {
                "short_description": row["short_description"], "source": row["source"],
                "etype": row["type"], "comment": row["comment"], "context": row["context"],
                "related_activity": row["related_activity"],
                "assigned_to": row["next_action_assigned_to"], "from_id": row["from_id"],
                "originator": row["originator"],
            },
            "standard_system_note": _standard_system_note(row),
        })
        next_id += 1

    db.conn.rollback()
    db.conn.close()

    return {
        "_readme": (
            "D1, strategy changed 2026-08-21 (researcher direct instruction) -- ONE row per item, "
            "its CURRENT/FINAL values only, no history replay. Two ways forward, your choice: "
            "(a) 'standard system' -- raise_new() using 'raise_new_kwargs', then whatever update() "
            "call 'standard_system_note' describes to reach the real state/resolution (None means "
            "raise_new() alone already produces it). (b) 'straight json edits' -- hand-edit 'row' "
            "directly (e.g. short_description for a title_shape_error), then a future script "
            "reads this file and writes the DB rows directly (bypassing raise_new()'s narrower "
            "constraints), the same direct-write precedent this module's own prior rebuilds used "
            "under direct researcher direction. The full version-by-version history is NOT lost -- "
            "escalation-export-20260820.json + escalation_history-export-20260820.json stay "
            "archived verbatim as the permanent narrative record."),
        "reseed_from": 735,
        "source_file": str(EXPORT_PATH.as_posix()),
        "items": items,
        "live_rows_appended": live_rows,
    }


def main() -> int:
    doc = build_snapshot()
    out = pathlib.Path("iba/app/reports/escalation-v1-snapshot-20260821.json")
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n_title_errs = sum(1 for i in doc["items"] if i["title_shape_error"])
    n_needs_followup = sum(1 for i in doc["items"] if i["standard_system_note"])
    print(f"-> {out}")
    print(f"{len(doc['items'])} export item(s) + {len(doc['live_rows_appended'])} live row(s)")
    print(f"{n_title_errs} title-shape violation(s), {n_needs_followup} item(s) needing a "
         f"follow-up update() call under the 'standard system' path")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
