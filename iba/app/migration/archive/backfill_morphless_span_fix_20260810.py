"""backfill_morphless_span_fix_20260810.py — ONE-OFF: re-parse `span` for every verse affected by
the `step.span_html` regex bug fixed this same session (2026-08-10, `configmaint.propose` run
RUN-20260810_160133_776-CONFIGMAINT).

The bug: `step.span_html` required a `morph='...'` attribute on every `<span>` tag. STEP sometimes
emits a content span with `strong='...'` and NO `morph=` attribute at all (confirmed live, e.g.
John 4:18's `<span strong='G2192'>have</span>`) — the old regex silently dropped these tags
entirely, so the Strong's occurrence was asserted in `strong_verse` (a separate STEP call) but
never got a `span` row. Found via `raw.validate`'s parse-check failing for the new `receive` word
("G2192:2 missed"); measured project-wide before fixing: 824 verses / 1,077 spans / 24 codes.

This migration does NOT re-fetch anything from STEP — every affected verse's `preview` HTML is
already stored in `verse.preview`; it just re-runs `Step.parse_spans()` (now reading the FIXED
regex from `cfg_setting`, applied earlier this session) against the stored text and compares the
fresh result to what's currently in `span`. Note this is a REPLACE, not an append: because the
extra recovered tags fall at various positions within a verse, EVERY tag after the first newly-
recovered one shifts its `position` index — a verse whose parse changes at all gets its whole
active span set soft-deleted and re-inserted fresh (same convention `verse_lexical` already uses
for a superseded row: soft-delete, never overwrite in place).

`Step(cfg)` is constructed directly — no network call in `__init__`/`parse_spans`/`is_particle`.

    python -m iba.app.migration.backfill_morphless_span_fix_20260810           # dry-run
    python -m iba.app.migration.backfill_morphless_span_fix_20260810 --apply
"""

from __future__ import annotations

import argparse
import datetime
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db
from ..lib.stepapi import Step


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _current_spans(db: Db, verse_id: int) -> list[tuple]:
    rows = db.rows(
        "SELECT position, surface, strong_variant, morph_code, is_particle FROM span "
        "WHERE verse_id=? AND deleted=0 ORDER BY position", (verse_id,))
    return [(r["position"], r["surface"], r["strong_variant"], r["morph_code"], r["is_particle"])
            for r in rows]


def _fresh_spans(step: Step, preview: str) -> list[tuple]:
    return [(s["position"], s["surface"], s["strong_variant"], s["morph_code"], s["is_particle"])
            for s in step.parse_spans(preview or "")]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="apply (default is dry-run)")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)
    if "span" not in cfg.may_write("migration"):
        print("write-grant violation: 'migration' may not write 'span'", file=sys.stderr)
        db.close(); cfg.close()
        return 1

    step = Step(cfg)  # local-only construction: reads config, no network call

    verses = db.rows("SELECT id, osisId, preview FROM verse WHERE deleted=0")
    changed: list[tuple[int, str, int, int]] = []  # (verse_id, osisId, old_count, new_count)
    for v in verses:
        old = _current_spans(db, v["id"])
        new = _fresh_spans(step, v["preview"])
        if old != new:
            changed.append((v["id"], v["osisId"], len(old), len(new)))

    print(f"{len(verses)} active verse(s) scanned; {len(changed)} need a span rebuild "
          f"(fresh parse differs from what's stored).")
    net_new_spans = sum(n - o for _, _, o, n in changed)
    print(f"net span rows added across those verses: +{net_new_spans}")
    for vid, osis, o, n in changed[:15]:
        print(f"  {osis:16} {o:3} -> {n:3} span(s)")
    if len(changed) > 15:
        print(f"  ... and {len(changed) - 15} more")

    if not a.apply:
        print("\nDRY-RUN — re-run with --apply to rewrite these verses' span rows.")
        db.close(); cfg.close()
        return 0

    total_deleted, total_inserted = 0, 0
    for vid, osis, _, _ in changed:
        # The table carries an UNCONDITIONAL UNIQUE(verse_id, position) constraint (not just the
        # partial live-only index idx_span_live_unique) — a plain `deleted=1` leaves the old rows
        # still occupying their (verse_id, position) slots, so the fresh insert below collides
        # (confirmed live: UNIQUE constraint failed on the very first verse). Bump position out of
        # the live range in the SAME update that soft-deletes, so the old rows stay soft-deleted
        # (auditable) but no longer block the reinsert.
        db.conn.execute(
            "UPDATE span SET deleted=1, position=position+1000000 WHERE verse_id=? AND deleted=0",
            (vid,))
        total_deleted += db.conn.execute("SELECT changes()").fetchone()[0]
        v = db.get("verse", id=vid)
        for sp in step.parse_spans(v["preview"] or ""):
            db.write("span", {
                "verse_id": vid, "position": sp["position"], "surface": sp["surface"],
                "strong_variant": sp["strong_variant"], "morph_code": sp["morph_code"],
                "is_particle": sp["is_particle"], "built_at": _now(), "deleted": 0})
            total_inserted += 1
    db.conn.commit()
    db.close()
    cfg.close()
    print(f"\napplied: {len(changed)} verse(s) rebuilt — {total_deleted} old span row(s) "
          f"soft-deleted, {total_inserted} new span row(s) inserted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
