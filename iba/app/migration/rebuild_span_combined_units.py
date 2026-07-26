"""migration/rebuild_span_combined_units.py — ONE-OFF: regenerate `span` from
`verse.preview` using the corrected parse_spans() (one row per HTML <span>
tag, combined codes kept together - 2026-07-25 model fix; see
lib/stepapi.py, handlers/raw.py validate(), and the cfg_table/cfg_column
correction runs RUN-20260725_133709_153/133720_920/133735_587-CONFIGMAINT).

Background: the OLD parse_spans() emitted one row per Strong's CODE, even
when STEP's own HTML tagged several codes on ONE <span> (e.g.
strong='G1722 G0054' on "purity" - confirmed via a live STEP re-fetch of
2Cor.6.6, byte-identical to the stored preview, so this combination
originates in STEP's own data, not our pipeline). That misattributed the
OTHER codes' surface text onto the code with none of its own, and broke a
Hebrew word's attached particles off from the root they're semantically
bound to. The fix keeps a tag's full code/morph list together in one row.

No STEP re-fetch needed: every span row is re-derived from verse.preview,
already stored locally.

Full rebuild, not incremental: DELETEs every row in `span` and reinserts
from every non-deleted verse - the old rows are wrong at the model level
(split a combined unit), not just missing some, so there is nothing in the
old table worth keeping.

    python -m iba.app.migration.rebuild_span_combined_units            # dry-run: report only
    python -m iba.app.migration.rebuild_span_combined_units --apply     # do it
"""
from __future__ import annotations

import argparse
import datetime

from ..lib.cfg import Cfg
from ..lib.stepapi import Step


def _now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def build_new_rows(cur, step: Step):
    cur.execute("SELECT id, preview FROM verse WHERE deleted=0")
    verses = cur.fetchall()

    new_rows = []
    empty_preview = 0
    for v in verses:
        vid, preview = v["id"], v["preview"]
        if not preview:
            empty_preview += 1
            continue
        for sp in step.parse_spans(preview):
            new_rows.append((
                vid, sp["position"], sp["surface"], sp["strong_variant"],
                sp["morph_code"], sp["is_particle"], _now(), 0,
            ))
    return len(verses), empty_preview, new_rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    cfg = Cfg()
    step = Step(cfg)
    conn = cfg.conn
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM span")
    old_count = cur.fetchone()[0]

    n_verses, empty_preview, new_rows = build_new_rows(cur, step)

    print(f"verses considered: {n_verses}")
    print(f"verses with empty preview (skipped): {empty_preview}")
    print(f"old span rows: {old_count}")
    print(f"new span rows: {len(new_rows)}")

    if not args.apply:
        print("dry-run only - pass --apply to write")
        return

    cur.execute("DELETE FROM span")
    cur.executemany(
        "INSERT INTO span (verse_id, position, surface, strong_variant, morph_code, is_particle, built_at, deleted) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        new_rows,
    )
    conn.commit()
    print(f"span rebuilt: {old_count} -> {len(new_rows)} rows")


if __name__ == "__main__":
    main()
