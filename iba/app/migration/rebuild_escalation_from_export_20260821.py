"""rebuild_escalation_from_export_20260821.py — D1 (register v9): rebuild `escalation` from both
sources (the 2026-08-20 JSON export + this session's own live post-wipe rows), replayed through the
REAL validation engine (`_title_shape_error`, `_evaluate_transition`, `_check_requirements` — the
same functions `raise_new()`/`update()` call), in true chronological order, so numbering continues
from `escalations_old`'s max (735) and every #7xx citation in BUILD.md/GOVERNANCE.md stays
meaningful. `escalations_old` (735 rows) is untouched — this only concerns `escalation`/
`escalation_history`.

**TWO PHASES, per the register's own design — this script is PHASE 1 ONLY (dry run)**:
  --dry-run (default, the only mode this file implements): simulates every Raise/Update in memory,
      running the REAL business-rule functions against the LIVE config (cfg_escalation_transition/
      _requirement/_enum, read-only) but never calling `db.write()`/`db.update()` on `escalation`/
      `escalation_history` and never committing. Produces a reviewable proposed-conversion report.
  --execute: NOT IMPLEMENTED HERE. Per the register: "execute — only after the dry run is reviewed
      and corrected." That is a deliberate, separate, human-reviewed step — building and running it
      in the same pass as the dry run would erase the checkpoint the design exists to provide.

**Two output files, same computation** (researcher request, 2026-08-21): the `.md` report is prose
for reading; `escalation-rebuild-dry-run-20260821.json` alongside it is the same data as the EXACT
keyword arguments `raise_new()`/`update()` would be called with — every column named explicitly,
`null` where a version genuinely doesn't touch that field (matching `escalation_history`'s own delta
semantics), so it's directly readable AND directly hand-editable (e.g. to supply one of the 3 new
titles the dry run flags as still needed) ahead of whatever execute script eventually reads it.

**What this dry run actually reconstructs**:
  1. The 25 export rows (`escalation-export-20260820.json`), each with its full version history
     (`escalation_history-export-20260820.json`, 97 rows, FULL SNAPSHOTS under the retired design)
     — diffed here into true per-field DELTAS (comment/context/resolution/tried/short_description/
     related_activity: NULL unless that version's own transaction changed it vs. the previous
     version's snapshot).
  2. This session's own live rows (`escalation` as it stands now, ids #1-9, created after the wipe —
     not in the export) — replayed AFTER the export batch, unchanged in content.
  3. Chronological order = `raised_at` for the export's v1 rows (verified this pass: all 25 already
     fall in strict, non-overlapping raised_at order; the current live #1-9 all postdate every
     export row) — so a straight sequential replay, reseeded at 735, reproduces the ORIGINAL id
     numbers 736-759 exactly, with the export's one out-of-band item (JSON id=1, a
     configmaint.validate advisory raised chronologically LAST among the 25, at 11:39:53Z) landing
     on a fresh #760 rather than colliding with anything. The current live rows then become
     #761-769.
  4. `from_id` inference (D14): only possible WITHIN this replay batch (a from_id pointing at an
     `escalations_old` id, e.g. "carried over from escalations_old #650", can never resolve — that
     table is untouched, not merged into `escalation` — D1's own "not a copy, a conversion" framing
     covers exactly this: those stay related_activity prose, no from_id).

    python -m iba.app.migration.rebuild_escalation_from_export_20260821 --dry-run
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib import escalation as esc

EXPORT_DIR = pathlib.Path("iba/app/db/archive")
CONTENT_FIELDS = ("comment", "context", "resolution", "tried", "short_description",
                  "related_activity")
ENVELOPE_FIELDS = ("state", "next_action", "next_action_assigned_to", "originator")


def _load(name: str) -> dict:
    return json.loads((EXPORT_DIR / name).read_text(encoding="utf-8"))


class _Sim:
    """A synthetic escalation table for the dry run — id -> current merged row, in the shape
    _snapshot() would leave it. Never touches the real `escalation` table."""

    def __init__(self):
        self.rows: dict[int, dict] = {}
        self.next_id = 736                       # D1: reseeded to continue from escalations_old (735)

    def create(self, fields: dict) -> int:
        new_id = self.next_id
        self.next_id += 1
        self.rows[new_id] = dict(fields)
        return new_id

    def snapshot(self, sim_id: int, deltas: dict, envelope: dict) -> dict:
        cur = self.rows[sim_id]
        merged = dict(cur)
        for c in ("comment", "context"):
            if deltas.get(c):
                merged[c] = f"{cur[c]}\n{deltas[c]}" if cur.get(c) else deltas[c]
        for c in ("resolution", "related_activity", "tried", "short_description"):
            if deltas.get(c) is not None:
                merged[c] = deltas[c]
        merged.update(envelope)
        self.rows[sim_id] = merged
        return merged


def _diff_versions(prev: dict | None, cur: dict) -> dict:
    """The true delta a version's own transaction set, vs. the FULL-SNAPSHOT previous version
    (undoing the retired design's over-population — the whole reason D1 exists)."""
    delta = {}
    for f in CONTENT_FIELDS:
        pv = prev.get(f) if prev else None
        cv = cur.get(f)
        if cv != pv:
            delta[f] = cv
    return delta


def _from_id_candidates(text: str, batch_old_ids: set[int]) -> list[int]:
    """'#NNN' mentions in v1's comment/context that name ANOTHER item in THIS SAME 25-item batch —
    the only case from_id can resolve to post-replay (an escalations_old reference never can, that
    table isn't merged in)."""
    return sorted({int(m) for m in re.findall(r"#(\d+)", text or "") if int(m) in batch_old_ids})


def dry_run() -> tuple[list[str], list[str], dict]:
    """Returns (report_lines, hard_findings, json_doc). hard_findings is non-empty if ANY simulated
    call would be REFUSED by the real validation engine (title-shape/_check_requirements/
    _evaluate_transition) as it stands live today; these need a researcher decision before execute
    can be attempted, per D1's own two-phase gate. `json_doc` is the SAME computation, shaped as the
    exact keyword arguments raise_new()/update() would be called with — see module docstring."""
    cfg = Cfg()                                    # live, read-only for this whole run
    db = Db(cfg)

    export = _load("escalation-export-20260820.json")
    hist = _load("escalation_history-export-20260820.json")
    hist_by_id: dict[int, list[dict]] = {}
    for h in hist["rows"]:
        hist_by_id.setdefault(h["escalation_id"], []).append(h)
    for eid in hist_by_id:
        hist_by_id[eid].sort(key=lambda r: r["version"])

    batch_old_ids = {r["id"] for r in export["rows"]}
    old_to_new: dict[int, int] = {}                 # old export id -> synthetic new id (D1 sec: ids
                                                     # land back on their original numbers, but this
                                                     # mapping is kept explicit, not assumed, so a
                                                     # future out-of-order source doesn't silently
                                                     # mis-map)
    sim = _Sim()
    L: list[str] = ["# Escalation rebuild — dry run (D1, register v9)", "",
                    f"Reseeded at {sim.next_id - 1} (escalations_old's max). {len(export['rows'])} "
                    f"export item(s), {len(hist['rows'])} history version(s) total, replayed in "
                    f"raised_at order, followed by this session's {9} live post-wipe row(s). See "
                    f"the sibling .json in this same directory for the exact per-version column "
                    f"values (this prose report can't show every column, the json shows all of "
                    f"them, null where a version doesn't touch that field).", ""]
    findings: list[str] = []
    json_items: list[dict] = []

    ordered = sorted(export["rows"], key=lambda r: hist_by_id[r["id"]][0]["raised_at"])
    for r in ordered:
        old_id = r["id"]
        versions = hist_by_id[old_id]
        v1 = versions[0]
        cands = _from_id_candidates((v1["comment"] or "") + " " + (v1["context"] or ""),
                                    batch_old_ids - {old_id})
        from_id_new = old_to_new.get(cands[0]) if cands else None   # only usable if the target
                                                                     # was ALREADY replayed (earlier
                                                                     # in chronological order)

        title_err = esc._title_shape_error(v1["short_description"])
        L.append(f"## old #{old_id} -> new #{sim.next_id}  — {v1['short_description']}")
        if title_err:
            findings.append(f"old #{old_id} v1: title-shape violation — {title_err}")
            L.append(f"  ⚠ TITLE-SHAPE VIOLATION: {title_err}")
        if cands and from_id_new is None:
            L.append(f"  note: comment/context mentions old #{cands[0]} (same batch) but it hasn't "
                     f"been replayed yet at this point — from_id left unset, related_activity "
                     f"prose is the only carrier here")
        elif from_id_new:
            L.append(f"  from_id candidate: new #{from_id_new} (was old #{cands[0]})")

        new_id = sim.create({
            "state": v1["state"], "next_action": v1["next_action"],
            "next_action_assigned_to": v1["next_action_assigned_to"],
            "originator": v1["originator"], "type": v1["type"], "source": v1["source"],
            "at_step": v1["at_step"], "raised_at": v1["raised_at"],
            "comment": v1["comment"], "context": v1["context"], "resolution": v1["resolution"],
            "tried": v1["tried"], "related_activity": v1["related_activity"],
            "short_description": v1["short_description"], "from_id": from_id_new})
        old_to_new[old_id] = new_id
        L.append(f"  Raise: type={v1['type']} assigned_to={v1['next_action_assigned_to']} "
                 f"originator={v1['originator']}")

        # JSON: EXACTLY escalation.raise_new()'s own keyword arguments, one key per parameter —
        # editable in place (e.g. fix short_description here for #749/#751/#757-shaped items).
        item_json = {
            "old_id": old_id,
            "proposed_new_id": new_id,
            "raise_new_kwargs": {
                "short_description": v1["short_description"],
                "source": v1["source"],
                "etype": v1["type"],
                "comment": v1["comment"],
                "context": v1["context"],
                "related_activity": v1["related_activity"],
                "assigned_to": v1["next_action_assigned_to"],
                "from_id": from_id_new,
                "originator": v1["originator"],
            },
            "historical_reference_only": {
                "_note": "NOT passed to raise_new() -- raise_new() always sets raised_at=now() and "
                        "resolution/tried=None at creation. Shown so the original timing/values "
                        "are visible for review, not as fields an execute script should apply.",
                "raised_at": v1["raised_at"], "state": v1["state"],
                "next_action": v1["next_action"], "resolution": v1["resolution"],
                "tried": v1["tried"],
            },
            "title_shape_error": title_err,
            "from_id_candidate_old_id": cands[0] if cands else None,
            "updates": [],
        }

        prev_snapshot = v1
        for h in versions[1:]:
            delta = _diff_versions(prev_snapshot, h)
            env_changed = {f: h[f] for f in ("state", "next_action", "next_action_assigned_to")
                          if h[f] != prev_snapshot.get(f)}
            summary = ", ".join(f"{k}={v!r}" for k, v in delta.items()) or "(envelope only)"
            L.append(f"  v{h['version']} ({h['answered_at']}, {h['originator']}): {summary}"
                     + (f" | state {prev_snapshot.get('state')}->{h['state']}"
                        if h['state'] != prev_snapshot.get('state') else ""))

            # exercise the REAL validation for anything a live Update call would check —
            # title-shape (if short_description changed) and the two requirement/transition
            # engines, using the LIVE config (read-only) but never writing.
            update_title_err = None
            if delta.get("short_description"):
                update_title_err = esc._title_shape_error(delta["short_description"])
                if update_title_err:
                    findings.append(f"old #{old_id} v{h['version']}: title-shape violation on a "
                                    f"corrected short_description — {update_title_err}")
                    L.append(f"    ⚠ TITLE-SHAPE VIOLATION on corrected title: {update_title_err}")

            next_action_err = None
            if h["next_action"] and h["next_action"] != prev_snapshot.get("next_action"):
                try:
                    esc._check_next_action_manual(db, h["next_action"])
                except ValueError as e:
                    next_action_err = str(e)
                    findings.append(f"old #{old_id} v{h['version']}: {e}")
                    L.append(f"    ⚠ {e}")

            # JSON: EXACTLY escalation.update()'s own keyword arguments for this version — every
            # content column present (null = this version doesn't touch it, matching
            # escalation_history's own delta semantics), envelope fields only when changed.
            item_json["updates"].append({
                "version": h["version"],
                "update_kwargs": {
                    "next_action": h["next_action"] if "next_action" in env_changed else None,
                    "next_action_assigned_to": h["next_action_assigned_to"]
                        if "next_action_assigned_to" in env_changed else None,
                    "comment": delta.get("comment"),
                    "context": delta.get("context"),
                    "tried": delta.get("tried"),
                    "resolution": delta.get("resolution"),
                    "related_activity": delta.get("related_activity"),
                    "state": h["state"] if h["next_action"] == "reject" else None,
                    "originator": h["originator"],
                    # NOT a real update() parameter -- see "short_description_gap" below. Shown
                    # anyway because the historical data genuinely has this delta (e.g. #736 v2/v3,
                    # the #759 title-shape corrections) and hiding it would make the JSON silently
                    # incomplete for exactly the field a reviewer is most likely to need to edit.
                    "short_description": delta.get("short_description"),
                },
                "short_description_gap": (
                    "escalation.update() has NO short_description parameter today -- this delta is "
                    "real (present in the 2026-08-20 export) but CANNOT be applied by calling "
                    "update() as it currently exists. Raised as escalation #10, 2026-08-21."
                    if delta.get("short_description") else None),
                "historical_reference_only": {
                    "_note": "answered_at when this version was ORIGINALLY written -- update() "
                            "always sets answered_at=now() when replayed, not this value.",
                    "answered_at": h["answered_at"],
                    "state_became": h["state"] if "state" in env_changed else None,
                },
                "title_shape_error": update_title_err,
                "next_action_validation_error": next_action_err,
            })

            sim.snapshot(new_id, delta, env_changed)
            prev_snapshot = h
        L.append("")
        json_items.append(item_json)

    L.append(f"## This session's live rows (#1-9) — replayed unchanged, land as "
             f"#{sim.next_id}-#{sim.next_id + 8}")
    L.append("")
    json_live_rows = []
    for r in db.rows("SELECT * FROM escalation ORDER BY id"):
        L.append(f"  old (this session) #{r['id']} -> new #{sim.next_id}  — {r['short_description']}")
        json_live_rows.append({
            "old_id_this_session": r["id"], "proposed_new_id": sim.next_id,
            "short_description": r["short_description"],
            "note": "this session's live row (raised after the 2026-08-20 wipe, not in the "
                    "export) -- replayed unchanged, full row already matches today's rules"})
        sim.next_id += 1
    L.append("")

    L.append(f"## Summary")
    L.append(f"- {len(ordered)} export item(s) simulated, final synthetic id before the live-row "
            f"batch: {sim.next_id - 9 - 1}")
    L.append(f"- {len(findings)} finding(s) needing a decision before --execute" if findings
            else "- 0 findings — every simulated Raise/Update passed today's live validation "
                 "cleanly")
    if findings:
        L.append("")
        L.append("### Findings")
        for f in findings:
            L.append(f"- {f}")

    db.conn.rollback()          # this connection touched nothing but SELECTs, but explicit > implied
    db.conn.close()

    json_doc = {
        "_readme": "Same computation as the sibling .md report. 'raise_new_kwargs'/'update_kwargs' "
                  "are EXACTLY escalation.py's own function parameter names -- edit values here "
                  "(e.g. short_description for a title-shape finding) ahead of whatever execute "
                  "script eventually reads this file. 'historical_reference_only' blocks are NOT "
                  "passed to either function (raised_at/answered_at are always set to now() at "
                  "replay time) -- shown for review context only. EXCEPTION: "
                  "'update_kwargs.short_description' is NOT a real update() parameter either -- "
                  "update() has no way to correct a title after Raise today (escalation #10, "
                  "found 2026-08-21 reviewing this exact file). Shown because the historical delta "
                  "is real and a reviewer needs to see it, but applying it needs either a code fix "
                  "(add the parameter) or a different mechanism -- not a plain update() call.",
        "reseed_from": 735,
        "source_files": ["iba/app/db/archive/escalation-export-20260820.json",
                         "iba/app/db/archive/escalation_history-export-20260820.json"],
        "items": json_items,
        "live_rows_appended": json_live_rows,
        "findings": findings,
    }
    return L, findings, json_doc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", default=True)
    ap.add_argument("--execute", action="store_true",
                    help="NOT IMPLEMENTED — see module docstring: execute is a deliberate separate "
                        "step, built only after the dry run above is reviewed.")
    a = ap.parse_args()
    if a.execute:
        raise SystemExit("--execute is not implemented in this script — the dry run above is "
                         "PHASE 1 only, per D1's own two-phase gate ('execute — only after the dry "
                         "run is reviewed and corrected'). Review the report, then this needs a "
                         "second, separate script/pass.")

    lines, findings, json_doc = dry_run()
    out = pathlib.Path("iba/app/reports/escalation-rebuild-dry-run-20260821.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    json_out = pathlib.Path("iba/app/reports/escalation-rebuild-dry-run-20260821.json")
    json_out.write_text(json.dumps(json_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"dry run complete -> {out}")
    print(f"                 -> {json_out} (same data, per-version columns explicit, editable)")
    print(f"{len(findings)} finding(s) needing a decision before --execute")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
