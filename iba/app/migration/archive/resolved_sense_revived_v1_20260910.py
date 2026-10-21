"""resolved_sense_revived_v1_20260910.py — ONE-OFF, corpus-wide. Escalation #1596/#1663-cont.,
researcher instruction verbatim, 2026-09-10: "my intent is that the lexical will carry the
strong_meaning_parse ord = 0 row as resolved_sense and the surface. the gloss_consistent_in_verse
flag should be retained. I know I have gone around the block several times about
strong_meaning_parse but the work we did earlier today finally brought me around to settle on the
ord=0."

Reverses (in substance, not mechanically) escalation #1575 (2026-09-07), which stopped
`resolve_code()` writing `resolved_sense` at all — that removal targeted a genuinely bad value (an
unconditional stem/voice-narrow-then-append-every-LSJ/Mounce-row dump, up to 3,938 chars per code).
This is a DIFFERENT, much narrower value: `strong_meaning_parsed`'s own sort=0 row (confirmed live,
escalation #1663, 2026-09-10: `sort` is 0-indexed — MIN(sort)=0 for every live strong_variant/
lemma_key group, no exceptions) — the same exact-variant/base-fallback `sense_rows` list
`resolve_code()` already computes for `ambiguity_note`, first element. See `resolve_code()`'s own
docstring in `lib/lexical.py` for the full reasoning (including why this revival carries no
M-code restriction, unlike #1527's original scoping).

`gloss_consistent_in_verse` needed NO code change — confirmed live, it has been keyed on `surface`
(not `resolved_sense`) since escalation #1527 (2026-09-06), a day before #1575 even removed
resolved_sense. Its 106,658 stale `=0` flags (escalation #1596's own finding) predate that #1527
surface-keying fix and were simply never recomputed since — this migration's ordinary rebuild path
(`build_for_verse` always calls `_apply_gloss_consistency` per verse) refreshes them as a side
effect, no separate step required. The researcher's "should be retained" = keep the column and its
current (already-correct) formula, not a request to change it.

Validated small first, live, before this full-corpus run (see escalation #1596 chat record):
  - Rev.17.4 (the G2192 "have" case #1575 itself was about) — 26/26 codes updated, G2192 now
    carries the single clean ord=0 gloss ("(tr.) to have, hold, keep; (intr.) to be"), not the old
    2,652-char LSJ dump.
  - G2071 (one of #1663's 250 zero-strong_meaning_parsed-row codes) — resolved_sense correctly
    stays None, not guessed from stepGloss.
  - G0004 (one of #1663's 347 duplicate-sort=0 codes, two rows both sort=0: "weightless" and "not
    burdensome") — deterministic tie-break confirmed: lowest `strong_meaning_parsed.id` wins
    ("weightless").

`iba.db` snapshotted first via `lib/dbsnapshot.snapshot()` (WAL-checkpointed copy under the
project's existing snapshot convention), same discipline as #1575's own migration.

    python -m iba.app.migration.resolved_sense_revived_v1_20260910
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib import dbsnapshot, lexical
from ..lib.cfg import DB_PATH


def main() -> int:
    snap = dbsnapshot.snapshot("pre-1596-resolved-sense-revived")
    print(f"snapshot: {snap}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    verse_ids = [r["id"] for r in conn.execute(
        "SELECT DISTINCT verse_id AS id FROM verse_lexical WHERE deleted=0")]
    print(f"resolved_sense_revived_v1_20260910: rebuilding {len(verse_ids)} verses...")

    totals = lexical.build_for_verse_ids(conn, verse_ids, step=None)
    conn.commit()

    n_total = conn.execute(
        "SELECT COUNT(*) c FROM verse_lexical WHERE deleted=0").fetchone()["c"]
    n_sense = conn.execute(
        "SELECT COUNT(*) c FROM verse_lexical WHERE deleted=0 AND resolved_sense IS NOT NULL"
    ).fetchone()["c"]
    n_null = n_total - n_sense
    n_flag0 = conn.execute(
        "SELECT COUNT(*) c FROM verse_lexical WHERE deleted=0 AND gloss_consistent_in_verse=0"
    ).fetchone()["c"]
    conn.close()

    print("resolved_sense_revived_v1_20260910:")
    for k, v in totals.items():
        print(f"  - {k}: {v}")
    print(f"  - live verse_lexical rows: {n_total}")
    print(f"  - resolved_sense populated: {n_sense}")
    print(f"  - resolved_sense still NULL (no strong_meaning_parsed row, exact or base): {n_null}")
    print(f"  - gloss_consistent_in_verse=0 after refresh: {n_flag0}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
