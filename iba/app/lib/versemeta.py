"""versemeta.py — verse_meta.status maintenance (#1661): sets the status (cfg_enum
verse_meta_status: exclude/citated/analysed) for a list of verse references and stamps the change.
The passage anchor is its own column (verse_meta.is_passage_anchor). Run as step
verse_meta.set_status (handlers/versemeta.py), behind VerseMeta.ps1.
"""
from __future__ import annotations

import datetime

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


_RANK = {None: 0, "analysed": 1, "citated": 2}


def mark(conn, verse_ids, status: str) -> int:
    """The reading process's coverage marks (#2172, build decision 3): a verse read is 'analysed', a
    verse the narrative cites is 'citated'; 'citated' replaces 'analysed' and is never stepped back,
    and 'exclude' is never overwritten. No commit (the caller's unit of work). Returns rows changed."""
    if status not in ("analysed", "citated"):
        raise ValueError(f"mark() sets analysed or citated, not {status!r}")
    now, n = _now(), 0
    for vid in set(verse_ids):
        r = conn.execute("SELECT status FROM verse_meta WHERE verse_id=? AND deleted=0", (vid,)).fetchone()
        if r is None or r[0] == "exclude" or _RANK.get(r[0], 3) >= _RANK[status]:
            continue
        conn.execute("UPDATE verse_meta SET status=?, status_changed_at=?, updated_at=? WHERE verse_id=?",
                     (status, now, now, vid))
        n += 1
    return n


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
    if status == "analysed":
        raise ValueError("'analysed' is set only at gate 1 of a reading (Reading.ps1 -Step Check; #2228 D-c), "
                         "never by hand")

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
