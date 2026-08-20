"""fix_escalation_titles_v2_20260820.py — one-off data repair, escalation #759, round 2.

The first pass (fix_escalation_short_description_and_columns_20260820.py) got the column split
right (comment/context/resolution) but got the TITLE wrong — researcher, live: "if you take my
title in 753 as an example, it would help. It looks like you just cut what ever was there previous
to 57 chars, its not a title or subject." Correct: round 1's "titles" were compressed sentences
(verb-predicate, colons dragging in stats/paths) under 60 chars, not composed noun-phrase titles
like #753's own "Escalation utility Refinement".

This pass ONLY touches short_description, on top of round 1's already-correct comment/context/
resolution split — those aren't touched again. Same mechanism as round 1: a new escalation_history
snapshot (version+1), nothing in any prior version altered.
"""

from __future__ import annotations

import datetime

from ..lib.cfg import Cfg
from ..lib.db import Db

_NOW = lambda: datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

_COLS = ("run_id", "source", "at_step", "type", "short_description", "context", "comment", "tried",
        "state", "next_action", "next_action_assigned_to", "originator", "resolution",
        "related_activity", "raised_at", "answered_at")

_REPAIR_NOTE = ("[title corrected 2026-08-20, escalation #759 round 2: round 1's short_description "
               "was a compressed sentence, not a composed title -- researcher: \"it looks like you "
               "just cut whatever was there previous to 57 chars\". Redone as an actual noun-"
               "phrase title, matching #753's own style. comment/context/resolution from round 1 "
               "are unchanged.]")

TITLES: dict[int, str] = {
 736: "Main-Project / IBA Filing Consolidation",
 737: "IBA Debate-Pipeline to research_db Migration (Gated)",
 738: "Cluster-Assignment Backfill Exceptions",
 739: "Programme Prose Realignment (Ch. 4-6)",
 740: "Configmaint Orphan-Config Advisory",
 741: "Manual Raise/Update Flow Smoke Test",
 742: "Approve-Without-Resolution Smoke Test",
 743: "Escalation.ps1 Manual-Verb Wrapper Gap",
 744: "GOVERNANCE.md / USER-GUIDE.md Escalation Drift",
 745: "escalation_history Write-Grant Gap",
 746: "cfg_escalation Rule-Table Staleness",
 747: "write_history_report() Entry-Point Gap",
 748: "Escalation #735 Orphan-Config Follow-Up",
 749: "Escalation #677 Formal Closure",
 750: "cfg_write_grant Orphan (writer=run)",
 751: "Escalation #745 Fix Verification",
 752: "Escalation.ps1 Manual-Verb Live Test",
 754: "Escalation.ps1 Positional-Binding Bug",
 755: "Escalation-Module Config Review",
 756: "cfg_write_grant Orphan (escalation to word_registry)",
 757: "C: Drive Zero-Free-Space Incident",
 758: "content_index Size / DB-Bloat Investigation",
 759: "escalation.short_description Column-Spec Violation",
}


def _current(db: Db, escalation_id: int) -> dict:
    rows = db.rows("SELECT * FROM escalation WHERE id=?", (escalation_id,))
    if not rows:
        raise ValueError(f"no escalation #{escalation_id}")
    return dict(rows[0])


def main() -> None:
    cfg = Cfg()
    db = Db(cfg)
    if "escalation" not in cfg.may_write("escalation") or "escalation_history" not in cfg.may_write("escalation"):
        raise PermissionError("write-grant violation: 'escalation' may not write escalation/escalation_history")

    overflow = {eid: t for eid, t in TITLES.items() if len(t) > 60}
    if overflow:
        for eid, t in overflow.items():
            print(f"  OVER 60: #{eid} ({len(t)} chars): {t!r}")
        raise AssertionError(f"{len(overflow)} title(s) over 60 chars -- fix TITLES before running")

    fixed = 0
    for eid, new_sd in sorted(TITLES.items()):
        cur = _current(db, eid)
        merged = dict(cur)
        merged["short_description"] = new_sd
        merged["comment"] = f"{cur['comment']}\n\n{_REPAIR_NOTE}"
        merged["version"] = cur["version"] + 1
        merged["originator"] = "Claude"
        merged["answered_at"] = _NOW()

        db.write("escalation_history", {"escalation_id": eid, "version": merged["version"],
                                        **{k: merged[k] for k in _COLS}})
        db.update("escalation", {"id": eid}, version=merged["version"],
                 **{k: merged[k] for k in _COLS})
        fixed += 1
        print(f"  #{eid} v{merged['version']}: {new_sd!r} ({len(new_sd)} chars)")

    db.close()
    cfg.close()
    print(f"\n{fixed} titles corrected.")


if __name__ == "__main__":
    main()
