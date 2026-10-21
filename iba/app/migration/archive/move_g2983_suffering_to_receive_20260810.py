"""move_g2983_suffering_to_receive_20260810.py — ONE-OFF: retire G2983 (lambano) under 'Suffering'
now that it has a proper home in the new registry word 'receive' (id 185, this same session).

G2983 was the flagged false positive in 'Suffering' (BUILD.md sec96/sec93-era note) — STEP's bare
masterSearch("Incurability") had matched it only on one ESV verse span's incidental use of the
English word "incur" (Rom 13:2), not on its actual meaning. Its real meaning ("to take, receive")
is what raw.discover for 'receive' picked it up on naturally (STEP masterSearch("receive") -> G2983
is one of the 64 seeds) — no manual add needed there, already active under word_id 185.

This script only does the other half: soft-delete the word_strong row under 'Suffering' (word_id
177). Idempotent — a no-op if already retired.

    python -m iba.app.migration.move_g2983_suffering_to_receive_20260810           # dry-run
    python -m iba.app.migration.move_g2983_suffering_to_receive_20260810 --apply
"""

from __future__ import annotations

import argparse
import sys

from ..lib.cfg import Cfg
from ..lib.db import Db

STRONG = "G2983"
FROM_WORD = "Suffering"
TO_WORD = "receive"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="apply (default is dry-run)")
    a = ap.parse_args()

    cfg = Cfg()
    db = Db(cfg)
    if "word_strong" not in cfg.may_write("migration"):
        print("write-grant violation: 'migration' may not write 'word_strong'", file=sys.stderr)
        db.close(); cfg.close()
        return 1

    from_row = db.get("word_registry", word=FROM_WORD)
    to_row = db.get("word_registry", word=TO_WORD)
    if not from_row or not to_row:
        print(f"{FROM_WORD!r} or {TO_WORD!r} not found in word_registry.", file=sys.stderr)
        db.close(); cfg.close()
        return 1

    from_link = db.get("word_strong", word_id=from_row["id"], strong=STRONG, deleted=0)
    to_link = db.get("word_strong", word_id=to_row["id"], strong=STRONG, deleted=0)

    print(f"{STRONG} under {FROM_WORD!r} (id {from_row['id']}): "
          f"{'active — will retire' if from_link else 'already retired'}")
    print(f"{STRONG} under {TO_WORD!r} (id {to_row['id']}): "
          f"{'already active — nothing to add' if to_link else 'MISSING (unexpected — not touched by this script)'}")

    if not a.apply:
        print("\nDRY-RUN — re-run with --apply to write this change.")
        db.close(); cfg.close()
        return 0

    if from_link:
        db.update("word_strong", {"word_id": from_row["id"], "strong": STRONG}, deleted=1)
        db.conn.commit()
        print(f"\napplied: {STRONG} retired under {FROM_WORD!r}.")
    else:
        print("\nnothing to apply.")
    db.close()
    cfg.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
