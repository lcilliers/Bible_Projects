"""versemeta.py — verse_meta.status maintenance, escalation #1661.

Researcher instruction, verbatim: "Add an additional column to verse_meta to set the status of
the verse. Status values: exclude; anchor; citated; analysed. ... create a ps routine whereby
researcher can update the status for a range of verses by comma delimited refences. Ignore the
status anchor, it is already included as a separate column [that's verse_meta.is_passage_anchor].
Updated column must be stamped if the status change."

Column + `cfg_enum verse_meta_status` domain (exclude/citated/analysed) built by
migration/add_verse_meta_status_column_v1_20260910.py. This module is the ongoing write path —
a standalone utility (like lib/escalation.py), not a run.py dispatcher step, since it's a direct
researcher-driven maintenance action, not a repeatable pipeline stage.

CLI:
    python -m iba.app.lib.versemeta set-status --references "Gen.1.1,Rom 1:1,Rom.1.2" --status analysed [--db PATH]
"""
from __future__ import annotations

import argparse
import datetime
import sys

from .cfg import Cfg


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _find_verse(conn, ref: str):
    """A reference token may be typed as osisId ('Rom.1.1') or the human display form
    ('Rom 1:1') -- try osisId first (the app's canonical key elsewhere), then reference."""
    row = conn.execute(
        "SELECT id, osisId, reference FROM verse WHERE osisId=? AND deleted=0", (ref,)).fetchone()
    if row:
        return row
    return conn.execute(
        "SELECT id, osisId, reference FROM verse WHERE reference=? AND deleted=0", (ref,)).fetchone()


def run_set_status(cfg: Cfg, references: list[str], status: str) -> dict:
    """Set verse_meta.status for each verse named in `references` (comma-split by the caller).
    `status_changed_at` is stamped ONLY on an actual value change (the researcher's own "stamped
    if the status change" requirement) -- re-setting the same status again leaves the timestamp
    untouched. Returns a per-reference report; never raises for an individual not-found/duplicate
    reference, only for a bad `status` itself (checked once, up front)."""
    valid = cfg.enum("verse_meta_status")
    if status not in valid:
        raise ValueError(f"status {status!r} is not a live value of cfg_enum "
                          f"'verse_meta_status' ({valid!r})")

    conn = cfg.conn
    updated, unchanged, not_found = [], [], []
    now = _now()
    for raw in references:
        ref = raw.strip()
        if not ref:
            continue
        v = _find_verse(conn, ref)
        if not v:
            not_found.append(ref)
            continue
        meta = conn.execute(
            "SELECT status FROM verse_meta WHERE verse_id=? AND deleted=0", (v["id"],)).fetchone()
        if meta is None:
            not_found.append(f"{ref} (no verse_meta row for verse_id={v['id']})")
            continue
        if meta["status"] == status:
            unchanged.append(v["osisId"])
            continue
        conn.execute(
            "UPDATE verse_meta SET status=?, status_changed_at=?, updated_at=? WHERE verse_id=?",
            (status, now, now, v["id"]))
        updated.append(v["osisId"])
    conn.commit()
    return {"status": status, "updated": updated, "unchanged": unchanged, "not_found": not_found}


def main() -> int:
    ap = argparse.ArgumentParser(prog="python -m iba.app.lib.versemeta")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("set-status", help="set verse_meta.status for a comma-delimited list of "
                                          "verse references")
    p.add_argument("--references", required=True,
                    help="comma-delimited verse references, osisId ('Rom.1.1') or display form "
                         "('Rom 1:1') -- either is accepted per reference")
    p.add_argument("--status", required=True, help="one of cfg_enum verse_meta_status")
    p.add_argument("--db", default=None)

    args = ap.parse_args()
    cfg = Cfg(args.db) if args.db else Cfg()
    try:
        if args.cmd == "set-status":
            result = run_set_status(cfg, args.references.split(","), args.status)
            print(f"  status={result['status']!r}: {len(result['updated'])} updated, "
                  f"{len(result['unchanged'])} already set, {len(result['not_found'])} not found")
            if result["updated"]:
                print("  updated:", ", ".join(result["updated"]))
            if result["unchanged"]:
                print("  already set:", ", ".join(result["unchanged"]))
            if result["not_found"]:
                print("  NOT FOUND:", ", ".join(result["not_found"]))
            return 1 if result["not_found"] else 0
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    finally:
        cfg.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
