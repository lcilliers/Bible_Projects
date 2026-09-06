"""resolved_sense_mcode_only_v1_20260906.py — ONE-OFF. Escalation #1527, researcher instruction
verbatim, 2026-09-06: `resolved_sense` is only relevant for cluster M-codes, not cluster T-codes
("what I do not want to happen is that layer 1 arrives at a resolved_sense that is compromised,
that gives layer 2 an answer that is not dependable") — plus, separately, drop the redundant raw
`stepGloss` dictionary dump that was being prepended to every row regardless (root cause of the
size problem #1526 surfaced: 51MB/75,350 rows for a single Very-Large cluster's Layer-1 extract).
Both fixes are in `iba/app/lib/lexical.py` itself now (`load_mcode_strongs`, `resolve_code`'s
sense construction, `build_for_verse`'s M-code gate) — this script re-runs the corrected code
against the full existing corpus so the live `verse_lexical` table reflects it, using the exact
same identity-stable production write path (`write_readings_for_span`, #1520) rather than a
bespoke SQL patch — the same validation approach BUILD.md #225 used for its own backfill.

Also applies decision (a) from the same escalation, previously made by the researcher and
confirmed this session: `gloss_consistent_in_verse` is keyed on `surface` (the aligned translation
word), not `resolved_sense` (a pure function of (strong, morph_code) that can never vary by
occurrence) — `_apply_gloss_consistency` in `lexical.py` already carries this fix; re-running
`build_for_verse` recomputes it for every row under the corrected logic.

Validated small first, not run blind: Dan 1:8 (H0834A's two occurrences, 'that'/'allow', now
correctly gloss_consistent_in_verse=0) and the full M46 cluster (591 verses — resolved_sense
population dropped from 100% to 19.9%, gloss_consistent_in_verse now genuinely varies) — both
checked live before this full-corpus run.

    python -m iba.app.migration.resolved_sense_mcode_only_v1_20260906
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
    print(f"resolved_sense_mcode_only_v1_20260906: rebuilding {len(verse_ids)} verses...")

    totals = lexical.build_for_verse_ids(conn, verse_ids, step=None)
    conn.commit()
    conn.close()

    print("resolved_sense_mcode_only_v1_20260906:")
    for k, v in totals.items():
        print(f"  - {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
