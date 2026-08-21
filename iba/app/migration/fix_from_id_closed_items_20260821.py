"""One-off data repair, escalation #767 v3. Researcher, verbatim: "I notice that you recently
created new and changed items where you entered in the related_activity details that indicate that
it should have 753 as From_id. The fact that you did not do it, tells me that you are not reading
the configs for the column requirements. that is a serious omission. what you now need to do is to
work through every instance where related_activity is not null, and check if you can find the
correct from_id. if you can, do a update for the item."

Full audit run first (not this script -- see escalation #767 v4/#772 investigation): 39 live rows
carry related_activity; 9 already had a correct from_id; 30 did not. Of those 30, 10 have a genuine,
identifiable single spawn parent, discoverable from the item's own recorded text -- this script
corrects those 10. The other 20 (19 with no discoverable parent + this correction) are handled
separately: #8 (the one OPEN item in the real-parent group) went through the normal update() front
door directly. The 19 "no parent found" rows are NOT touched here -- writing from_id=0 as the
researcher's proposed "checked, none" sentinel was found to be indistinguishable from NULL
throughout escalation.py (every from_id check -- _find_dangling/_find_cycles/_find_mismatched_
pairing/the paired-requirement test -- uses a plain truthy `if r["from_id"]`, and bool(0) is
False), so it would not achieve what the researcher asked for. Raised back to the researcher rather
than written silently; a real fix (a genuinely non-falsy sentinel, or explicit `IS NOT NULL` checks
throughout) needs their decision first.

WHY A DIRECT SCRIPT, not `update()`: 9 of these 10 items are `closed`/`completed`, and `update()`
structurally refuses to touch any item outside `_OPEN_STATES` ("raised"/"re-assigned"/"on-hold"/
"in-progress") -- confirmed live, itself a real gap (there is currently no sanctioned front-door
path to retroactively correct a closed record's from_id at all). Same class of exception already
established and used in this project for exactly this situation:
`fix_escalation_short_description_and_columns_20260820.py` (escalation #759) -- "writes directly,
the same way escalation.py's own _snapshot() does... allows changing [a column update() excludes],
which update()'s caller never does." This script calls `_snapshot()` (the actual, current,
already-tested mechanism -- not a hand-rolled reimplementation of its delta/append logic) directly,
bypassing only `update()`'s open-state gate, envelope UNCHANGED (state/next_action/assigned_to all
carried forward exactly as they are -- this is a field correction, not a state transition).

Determinations, each grounded in the item's OWN recorded text, not assumed:
  #6   -> 753  short_description itself says "per #753"; v1: "This item stands in #753's place"
  #10  -> 5    CORRECTION from the wrong value it was raised with (6): its own related_activity
               says "(found reviewing D1's dry-run JSON, see #5)" -- #5 is the item whose dry-run
               work this was found reviewing, not #6.
  #743 -> 6    #6 v8: "PS front door entirely missing from the design" -- matches #743's own
               content ("Escalation.ps1 has no PS wrapper for the new manual verbs") exactly.
  #744 -> 6    #6 v1: "GOVERNANCE.md never updated across the entire redesign lineage despite the
               original 2026-08-16 instruction" -- matches #744 exactly.
  #745 -> 6    Sibling finding from the same #6-driven design-plan review pass as #743/#744/#747.
  #747 -> 6    "Closed alongside #743 -- same PS-wrapper build covered both" -- same review pass.
  #750 -> 753  related_activity is literally "#753" -- the researcher's own named example.
  #754 -> 753  related_activity: "escalation-utility-refinement, related #753" -- researcher's
               own named example.
  #755 -> 753  related_activity: "escalation-utility-refinement, related #753"; content: "Config
               review requested in #753 v2" -- direct confirmation.
  #759 -> 753  related_activity: "escalation-utility-refinement, related #753" -- same pattern as
               #754/#755.

Run: python -m iba.app.migration.fix_from_id_closed_items_20260821
"""
from __future__ import annotations

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.escalation import _snapshot, _current  # the real, current, tested mechanism

FIXES: dict[int, int] = {
    6: 753,
    10: 5,
    743: 6,
    744: 6,
    745: 6,
    747: 6,
    750: 753,
    754: 753,
    755: 753,
    759: 753,
}

_REPAIR_NOTE = (
    "[from_id corrected 2026-08-21, escalation #767 v3 -- researcher's direct instruction after "
    "spotting the omission: 'you are not reading the configs for the column requirements'. Set to "
    "the genuine spawn parent identified from this item's own recorded text (see migration/"
    "fix_from_id_closed_items_20260821.py for the specific reasoning). No prior escalation_history "
    "row altered -- this is a new version on top, not a rewrite of history.]"
)


def main() -> None:
    cfg = Cfg()
    db = Db(cfg)
    if "escalation" not in cfg.may_write("escalation") or \
            "escalation_history" not in cfg.may_write("escalation"):
        raise PermissionError(
            "write-grant violation: 'escalation' may not write escalation/escalation_history")

    fixed = 0
    for eid, new_from_id in sorted(FIXES.items()):
        cur = _current(db, eid)
        target = _current(db, new_from_id)  # confirms the target genuinely exists, fails loudly if not
        deltas = {"from_id": new_from_id, "comment": _REPAIR_NOTE}
        envelope = {
            "state": cur["state"],
            "next_action": cur["next_action"],
            "next_action_assigned_to": cur["next_action_assigned_to"],
        }
        merged = _snapshot(cfg, db, eid, deltas, envelope, originator="Claude")
        fixed += 1
        print(f"  #{eid} v{merged['version']}: from_id {cur['from_id']!r} -> {new_from_id} "
              f"(target #{new_from_id} exists: {target['short_description']!r})")

    db.close()
    cfg.close()
    print(f"\n{fixed} rows corrected.")


if __name__ == "__main__":
    main()
