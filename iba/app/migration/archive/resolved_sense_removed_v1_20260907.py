"""resolved_sense_removed_v1_20260907.py — ONE-OFF. Escalations #1575/#1527-continued, researcher
instruction verbatim, 2026-09-07: "there [is] still data in the sense column that does not serve a
purpose... can you kindly remove it from the column for all the lexicals." #1527 (2026-09-06)
already removed the raw stepGloss dictionary-dump prefix and scoped resolved_sense to M-code words
only; building #1549's Layer-2-LLM payload work this session found the remaining M-code-scoped
values were STILL a generic dump for 277 strongs — a stem/voice narrowing that falls back to
joining every gloss when no stem structure exists, PLUS an unconditional full strong_lsj_parsed +
strong_mounce_parsed lexicon append for every Greek code regardless of need (up to 3,938 chars,
G2192 "have" alone: 2,652 chars, 62 LSJ rows). Neither is per-occurrence (#1527 v2's own diagnosis:
resolved_sense is a pure function of (strong, morph_code), nothing reads the verse) and, per this
direct instruction, resolved_sense now serves no purpose in this table at all.

`resolve_code()` in `iba/app/lib/lexical.py` no longer writes `resolved_sense` in either branch —
role/status/ambiguity_note are UNCHANGED (ambiguity_note's own sense_rows computation is untouched,
only the final resolved_sense assignment is gone). `build_for_verse`'s #1527 M-code gate is now a
no-op (nothing left to null) and left in place, not ripped out, as a smaller separate cleanup.
This script re-runs the corrected code against the full existing corpus via the same identity-
stable production write path (`write_readings_for_span`, #1520) used for #1527's own migration,
rather than a bespoke SQL patch.

Validated small first: Rev.17.4 (the G2192 case itself, 5/26 codes updated, all resolved_sense now
NULL) and Dan.1.8 (H0834A's two occurrences, ambiguity_note logic unaffected) — both checked live
before this full-corpus run. `iba.db` backed up first
(`iba.db.pre-1575-resolved-sense-removed-20260907.bak`).

    python -m iba.app.migration.resolved_sense_removed_v1_20260907
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib import lexical
from ..lib.cfg import DB_PATH


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    verse_ids = [r["id"] for r in conn.execute(
        "SELECT DISTINCT verse_id AS id FROM verse_lexical WHERE deleted=0")]
    print(f"resolved_sense_removed_v1_20260907: rebuilding {len(verse_ids)} verses...")

    totals = lexical.build_for_verse_ids(conn, verse_ids, step=None)
    conn.commit()

    remaining = conn.execute(
        "SELECT COUNT(*) c FROM verse_lexical WHERE deleted=0 AND resolved_sense IS NOT NULL"
    ).fetchone()["c"]
    conn.close()

    print("resolved_sense_removed_v1_20260907:")
    for k, v in totals.items():
        print(f"  - {k}: {v}")
    print(f"  - rows with non-null resolved_sense remaining: {remaining}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
