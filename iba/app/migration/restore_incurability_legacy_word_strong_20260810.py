"""restore_incurability_legacy_word_strong_20260810.py — ONE-OFF: correction to
`repurpose_incurability_to_suffering_20260810.py`.

That script soft-deleted the 7 legacy 'Incurability' `word_strong` links (G2983, G6103, G6345,
G7474, H0605, H2470I, H5375J) when the word was renamed to 'Suffering', reasoning that none of
them fit the new word. The researcher's follow-up instruction (2026-08-10, same day) corrected
this: the old links are to be RETAINED, not retired — the 8 new curated suffering/affliction codes
are ADDED alongside them, not a replacement of them. This script undoes the soft-delete on exactly
those 7 rows (restores `deleted=0`) and corrects `word_registry.source` to stop claiming a
replacement that didn't happen. The 8 new rows added by the prior script are untouched (already
correct).

    python -m iba.app.migration.restore_incurability_legacy_word_strong_20260810           # dry-run
    python -m iba.app.migration.restore_incurability_legacy_word_strong_20260810 --apply
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db

WORD = "Suffering"
LEGACY_CODES = ["G2983", "G6103", "G6345", "G7474", "H0605", "H2470I", "H5375J"]
NEW_SOURCE = (
    "repurposed 2026-08-10 from legacy registry word 'Incurability' (id 177; main-project "
    "verse-fanout orphan id 218) to 'Suffering' — the researcher's own curated Hebrew "
    "suffering/affliction list (8 codes) added ALONGSIDE the word's pre-existing 7 STEP-"
    "masterSearch-derived word_strong links, which are retained, not replaced (corrected "
    "2026-08-10, same day: the first pass had wrongly soft-deleted them)"
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="apply (default is dry-run)")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)
    for t in ("word_registry", "word_strong"):
        if t not in cfg.may_write("migration"):
            print(f"write-grant violation: 'migration' may not write {t!r}", file=sys.stderr)
            db.close(); cfg.close()
            return 1

    wrow = db.get("word_registry", word=WORD)
    if not wrow or wrow["deleted"]:
        print(f"{WORD!r} not found in word_registry (or deleted).", file=sys.stderr)
        db.close(); cfg.close()
        return 1
    wid = wrow["id"]

    to_restore = [r["strong"] for r in db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? AND deleted=1 AND strong IN "
        f"({','.join('?' * len(LEGACY_CODES))})", (wid, *LEGACY_CODES))]

    print(f"word_registry id {wid} ({WORD!r})")
    print(f"restoring {len(to_restore)} legacy link(s): {', '.join(to_restore) or '(none — already active)'}")
    if not a.apply:
        print("\nDRY-RUN — re-run with --apply to write these changes.")
        db.close(); cfg.close()
        return 0

    db.update("word_registry", {"id": wid}, source=NEW_SOURCE)
    n = 0
    for s in to_restore:
        db.update("word_strong", {"word_id": wid, "strong": s}, deleted=0)
        n += 1
    db.conn.commit()
    db.close()
    cfg.close()
    print(f"\napplied: {n} legacy link(s) restored to active, source corrected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
