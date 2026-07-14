#!/usr/bin/env python
"""Retrofit-authoring apply for the new/reinstated dimensions (v1, 2026-07-14).

Writes intensity(109)/specifier(110)/effect(111)/device(117)/direction(118) rows to ve_lexical
for read-2026 characteristics, from values authored off the saved reading prose. Values are
SELF-INTERPRETABLE (readable without the verse). device may carry a VEHICLE span (typed pair).
Idempotent: soft-deletes any prior reread row for the same (span, ve_nr) before inserting.

The caller supplies ROWS = { span_id: {109:v, 110:v, 111:v, 117:(v[, vehicle_span]), 118:v} }.
Missing dims default to 'none' (assessed-none, never ABSENT — per the anti-ABSENT rule).

Usage: import and call apply(ROWS, prov, live=True), or run a per-chapter _tmp_retrofit_*.py.
"""
import sqlite3, os, datetime

DB = os.path.join('database', 'bible_research.db')
LABELS = {109:'intensity', 110:'specifier', 111:'effect', 117:'device', 118:'direction'}
KINDS  = {109:'flag', 110:'flag', 111:'flag', 117:'value', 118:'value'}
MAND = (109, 110, 111, 117, 118)

def apply(ROWS, prov, live=False):
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    now = c.execute("SELECT COALESCE(MAX(created_at),'2026-07-14T00:00:00Z') FROM ve_lexical").fetchone()[0]
    ins = dele = veh = 0
    for sid, dims in ROWS.items():
        # verse_context_id for the span (carry it, like the reread apply)
        vc = c.execute("SELECT verse_context_id FROM ve_lexical WHERE verse_span_id=? AND verse_context_id IS NOT NULL LIMIT 1", (sid,)).fetchone()
        vcid = vc['verse_context_id'] if vc else None
        for ve in MAND:
            raw = dims.get(ve, 'none')
            vehicle = None
            if ve == 117 and isinstance(raw, (tuple, list)):
                raw, vehicle = raw[0], (raw[1] if len(raw) > 1 else None)
            val = raw if raw else 'none'
            # soft-delete prior reread row for this (span, ve_nr)
            d = c.execute("UPDATE ve_lexical SET delete_flagged=1 WHERE verse_span_id=? AND ve_nr=? AND source_provenance=? AND delete_flagged=0", (sid, ve, prov))
            dele += d.rowcount
            pk = 'pair' if vehicle else KINDS[ve]
            res = 'span' if vehicle else ('none' if str(val).lower() == 'none' else 'inferred')
            direction = val if ve == 118 else None
            c.execute("""INSERT INTO ve_lexical
                (verse_context_id, verse_span_id, ve_nr, ve_label, value, source_provenance, delete_flagged,
                 created_at, from_span, to_span, direction, resolution, pair_kind)
                VALUES (?,?,?,?,?,?,0,?,?,?,?,?,?)""",
                (vcid, sid, ve, LABELS[ve], val, prov, now,
                 sid if vehicle else None, vehicle, direction, res, pk))
            ins += 1
            if vehicle: veh += 1
    if live:
        c.commit(); print(f"LIVE: inserted {ins} dim rows ({veh} device-vehicle pairs); soft-deleted {dele} prior.")
    else:
        c.rollback(); print(f"[dry-run] would insert {ins} rows ({veh} vehicle pairs); soft-delete {dele}. --live to write.")
    c.close()
