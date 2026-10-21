"""repurpose_incurability_to_suffering_20260810.py — ONE-OFF: repurpose registry word id 177 from
'Incurability' to 'Suffering', per the researcher's direct instruction (2026-08-10 chat).

'Incurability' was a legacy 'verse-fanout orphan' (main-project word_registry id 218, curated there
to ONE Strong's, H0605 'anash'/be incurable) but in THIS app's word_registry it had accumulated 7
word_strong links via raw.discover's STEP masterSearch(meanings="Incurability") — a bare English-
string search that returned several false positives (matched on one ESV verse span containing the
substring "incur", not on the term's actual meaning; see
iba/app/reports/incurability-strongs-origin-20260810.md-equivalent chat investigation). None of that
is worth carrying forward under the new word, so ALL prior links are retired, not selectively kept.

The new curated Hebrew list (researcher's own, verified against `strong` in this DB by exact
stepTransliteration + stepGloss match):

    H6869B  tsa.rah      distress    70x  (H6869C "vexer" 1x correctly NOT this one)
    H6040   o.ni         affliction  36x  (H0590  "fleet" 7x correctly NOT this one)
    H7185   qa.shah      to harden   28x
    H4341   makh.ov      pain        16x
    H3511   ke.ev        pain         6x
    H4251   ma.cha.luy   suffering    1x  — FLAGGED: only transliteration/gloss match in the DB, so
                                            unambiguous, but this DB's own count fields disagree with
                                            the researcher's 1x (strong.count=4, dictionary-wide; 0
                                            strong_verse rows — not yet pulled into any book build).
                                            Linked anyway per instruction; verse data still to come.
    H6039   e.nut        affliction   1x
    H6094   ats.tse.vet  injury       5x

Requires the 'migration' -> 'word_registry' write grant added via configmaint.propose (run
RUN-20260810_153409_045-CONFIGMAINT, researcher-approved 2026-08-10) alongside the pre-existing
'migration' -> 'word_strong' grant.

    python -m iba.app.migration.repurpose_incurability_to_suffering_20260810           # dry-run
    python -m iba.app.migration.repurpose_incurability_to_suffering_20260810 --apply
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db

OLD_WORD = "Incurability"
NEW_WORD = "Suffering"
NEW_SOURCE = (
    "repurposed 2026-08-10 from legacy registry word 'Incurability' (id 177; main-project "
    "verse-fanout orphan id 218) — researcher's own curated Hebrew suffering/affliction list, "
    "replacing the 7 STEP-masterSearch-derived word_strong links (3 of which were false positives "
    "from English-span text matches, not real term relationships)"
)

# (strong, gloss, translit, count) — for the printed plan; the write itself only needs the strong.
CODES: list[tuple[str, str, str, int]] = [
    ("H6869B", "distress", "tsa.rah", 70),
    ("H6040", "affliction", "o.ni", 36),
    ("H7185", "to harden", "qa.shah", 28),
    ("H4341", "pain", "makh.ov", 16),
    ("H3511", "pain", "ke.ev", 6),
    ("H4251", "suffering", "ma.cha.luy", 1),  # flagged in docstring — count mismatch vs strong.count
    ("H6039", "affliction", "e.nut", 1),
    ("H6094", "injury", "ats.tse.vet", 5),
]


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

    wrow = db.get("word_registry", word=OLD_WORD)
    if not wrow or wrow["deleted"]:
        print(f"{OLD_WORD!r} not found in word_registry (or already deleted) — nothing to repurpose.",
              file=sys.stderr)
        db.close(); cfg.close()
        return 1
    wid = wrow["id"]

    old_links = [r["strong"] for r in db.rows(
        "SELECT strong FROM word_strong WHERE word_id=? AND deleted=0", (wid,))]
    new_codes = [s for s, *_ in CODES]

    print(f"word_registry id {wid}: {OLD_WORD!r} -> {NEW_WORD!r}")
    print(f"retiring {len(old_links)} old word_strong link(s): {', '.join(old_links) or '(none)'}")
    print(f"adding {len(new_codes)} new word_strong link(s):")
    for s, g, t, c in CODES:
        print(f"  {s:8} {t:12} {g:12} {c}x")

    if not a.apply:
        print("\nDRY-RUN — re-run with --apply to write these changes.")
        db.close(); cfg.close()
        return 0

    db.update("word_registry", {"id": wid}, word=NEW_WORD, source=NEW_SOURCE)
    n_retired = 0
    for s in old_links:
        db.update("word_strong", {"word_id": wid, "strong": s}, deleted=1)
        n_retired += 1
    n_added = 0
    for s, *_ in CODES:
        db.upsert("word_strong", {"word_id": wid, "strong": s, "deleted": 0})
        n_added += 1
    db.conn.commit()
    db.close()
    cfg.close()
    print(f"\napplied: word {wid} renamed, {n_retired} old link(s) retired (deleted=1), "
          f"{n_added} new link(s) added under {NEW_WORD!r}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
