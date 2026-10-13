"""temp_2138_add_gap_verses -- escalation #2138, one-off (2026-10-13).

Researcher, chat 2026-10-13 (verbatim): "2138  add the two verses to the verse table."
Psa 116:9 and 1Sa 17:19 are cited in the narrative (Ch 2, Ch 4) but had no `verse` row.
Each is fetched from STEP through the call3 route narrowed to the one verse, and written with
the same writer grant and the same verse/span rows as handlers/raw.py:verses_one. No
strong_verse rows: that table holds a word-onboarded strong's full concordance, and every code in
these two verses is meaning-only ('backfill') -- see #2138.

    python -m iba.app.tools.temp_2138_add_gap_verses [--live]
    python -m iba.app.tools.temp_2138_add_gap_verses --delete [--live]

--delete (researcher, chat 2026-10-13, verbatim: "soft delete and prepare the 2138 for approval"):
both verses were then removed from the narrative (register update 134), so their verse, span and
verse_lexical rows are soft-deleted, each under the grant that wrote it; verse_meta follows by the
trigger verse_meta_on_verse_deleted.
"""
from __future__ import annotations

import sys

from ..handlers.base import Ctx
from ..handlers.raw import _now, _write
from ..lib.db import Db
from ..lib.stepapi import Step, preview_to_text

# (osisId, a strong STEP tags in that verse, used only to narrow the call3 search to it)
VERSES = [("Ps.116.9", "H3068G"), ("1Sam.17.19", "H3478")]


def soft_delete(db: Db, live: bool) -> None:
    for osis, _ in VERSES:
        v = db.get("verse", osisId=osis)
        if not v or v["deleted"]:
            print(f"{osis}: no live verse row, skipped")
            continue
        for writer, table, col in (("lexical.build", "verse_lexical", "verse_id"),
                                   ("call3_strong", "span", "verse_id"), ("call3_strong", "verse", "id")):
            if table not in db.cfg.may_write(writer):
                raise PermissionError(f"write-grant violation: {writer!r} may not write {table!r}")
            n = db.conn.execute(f'SELECT COUNT(*) FROM "{table}" WHERE "{col}"=? AND deleted=0', (v["id"],)).fetchone()[0]
            print(f"{osis}: {table} {n} row(s) to soft-delete")
            if live:
                db.conn.execute(f'UPDATE "{table}" SET deleted=1 WHERE "{col}"=? AND deleted=0', (v["id"],))


def main() -> int:
    live = "--live" in sys.argv
    db = Db()
    if "--delete" in sys.argv:
        soft_delete(db, live)
        db.close()
        return 0
    step = Step(db.cfg)
    step.up()
    ctx = Ctx(db=db, cfg=db.cfg, step=step, run_id="temp_2138", word="", word_id=None, params={})
    route = db.cfg.route("call3_strong")
    for osis, code in VERSES:
        d = step._get(route.format(version=step.version, strong=code) + f"|reference={osis}")
        rows = [r for r in d.get("results", []) if r.get("osisId") == osis]
        if len(rows) != 1:
            raise SystemExit(f"{osis}: STEP returned {len(rows)} matching row(s), expected 1")
        r = rows[0]
        if db.get("verse", osisId=osis):
            print(f"{osis}: already in verse, skipped")
            continue
        spans = step.parse_spans(r.get("preview", ""))
        print(f"{osis} ({r.get('key')}): {preview_to_text(r.get('preview'))}  [{len(spans)} span(s)]")
        if not live:
            continue
        vid, _ = _write(ctx, "call3_strong", "verse", {
            "osisId": osis, "reference": r.get("key"), "preview": r.get("preview"),
            "text": preview_to_text(r.get("preview")),
            "step_version": step.version, "created_at": _now(), "deleted": 0})
        for sp in spans:
            _write(ctx, "call3_strong", "span", {
                "verse_id": vid, "position": sp["position"], "surface": sp["surface"],
                "strong_variant": sp["strong_variant"], "morph_code": sp["morph_code"],
                "is_particle": sp["is_particle"], "built_at": _now(), "deleted": 0})
        print(f"  written: verse id {vid}, {len(spans)} span(s)")
    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
