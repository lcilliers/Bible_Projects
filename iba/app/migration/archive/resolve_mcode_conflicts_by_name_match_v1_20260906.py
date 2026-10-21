"""resolve_mcode_conflicts_by_name_match_v1_20260906.py — ONE-OFF. Escalation #1525. Researcher
observation, verbatim: "if the strong is song, and one of the m-codes has song in the title, and
the other not, then I don't understand why it is so difficult to decide where song should go" —
correct, and a flat bag-of-words score across each cluster's ENTIRE gloss corpus (this escalation's
own first-pass heuristic) was the wrong method: it weighed a word buried anywhere in a cluster's
gloss list the same as a literal hit on the cluster's own name, so M22 "Praise & Song" and M42
"Prayer & Petition" scored an artificial tie on the word "song" (M42 happens to independently carry
a few song-glossed legacy members of its own, unrelated to this specific block).

Two-tier fix, applied here: TIER 1 checks each block's own vocabulary against each cluster's
SHORT_NAME (title) alone first — a hit on exactly one side decides it outright, no corpus fuzz
involved. TIER 2 (only reached when neither/both titles match) falls back to the full corpus score,
but requires a real margin (winner's score >=2 with the loser at 0, or at least double the loser's
score) AND a block of 3+ strongs — a single-keyword 1-vs-0 score on a lone strong is not treated as
decisive.

This resolves 22 of the 95 conflicting M-code cluster-pairs found on escalation #1525 (63 of the
208 then-remaining multi-tagged strongs); 73 pairs (145 strongs) have no reliable signal under
either tier and stay open, unresolved by this script.

What this does, in iba.db, one transaction, direct write (`cluster_strong` is `category='data'`
with `writer='migration'` grants): for every strong in a decided block, soft-deletes its LOSING
cluster's `cluster_strong` row (`deleted=1`, `rationale` appended) — the winning cluster's own row
for that strong already exists live and is untouched. Neither cluster itself is merged or retired
here (unlike the M10b/M58, M29/M18, M38/M45, M17/M16, M27/M55 whole-cluster merges) — both clusters
in every pair stay live; only the individual strongs' double-tagging is resolved.

Idempotent: a strong with no live row under the losing cluster is a no-op for that entry.

    python -m iba.app.migration.resolve_mcode_conflicts_by_name_match_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# (winner, loser, [strongs]) -- winner keeps its tag, loser's tag on these specific strongs is retired
_DECIDED: list[tuple[str, str, list[str]]] = [
    # TIER 1 -- title match
    ("M22", "M42", ["G0103", "G5603", "H7891", "H7892A", "H7892B"]),
    ("M42", "M21", ["G2172", "G2428", "H1159", "H7596"]),
    ("M64", "M18", ["G2071", "G3801", "H0972"]),
    ("M12", "M26", ["G3717", "H4639H", "H6665"]),
    ("M18", "M28", ["G7410", "H0185", "H7904"]),
    ("M36", "M21", ["G4574", "H6282A"]),
    ("M10", "M55", ["H1500", "H7701"]),
    ("M24", "M20", ["H4523", "H4531A"]),
    ("M33", "M19", ["G1879"]),
    ("M36", "M22", ["G4573"]),
    ("M47", "M15", ["G7244"]),
    ("M65", "M23", ["G8156"]),
    ("M11", "M45", ["G8298"]),
    ("M37", "M70", ["H1069"]),
    ("M76", "M22", ["H2986"]),
    ("M84", "M15", ["H7452"]),
    # TIER 2 -- corpus-score margin, 3+ strongs
    ("M07", "M06", ["G0176", "G0685", "G2652", "G2671", "G3680", "G7906", "H3994", "H7045", "H8381"]),
    ("M37", "M42", ["G1951", "G2564H", "G4779", "G6285", "G7099", "G7115"]),
    ("M15", "M16", ["G1321", "G3809", "H2449", "H4561", "H5034A"]),
    ("M04", "M18", ["G0587", "G0699", "G7936", "H7470"]),
    ("M24", "M06", ["H2556C", "H3238", "H3905", "H8496"]),
    ("M34", "M23", ["G1476", "G7683", "G7686"]),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        total_retired = 0
        for winner, loser, members in _DECIDED:
            for s in members:
                row = conn.execute(
                    "SELECT id, rationale FROM cluster_strong WHERE strong=? AND cluster_code=? "
                    "AND deleted=0", (s, loser)).fetchone()
                if row is None:
                    print(f"{s}: no live {loser} row -- already resolved, skipping")
                    continue
                new_rationale = (row["rationale"] or "") + (
                    f" | retired 2026-09-06 (escalation #1525): resolved in favour of {winner} "
                    f"(title/corpus-score match, this strong's block-level bulk resolution)")
                conn.execute(
                    "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                    (new_rationale, row["id"]))
                total_retired += 1
                print(f"{s}: retired {loser} (kept {winner})")
        conn.commit()
        print(f"\ntotal rows retired: {total_retired}")

        remaining = conn.execute(
            "SELECT COUNT(*) c FROM ("
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "GROUP BY strong HAVING COUNT(DISTINCT cluster_code)>1)").fetchone()["c"]
        print(f"total multi-tagged M-code strongs remaining corpus-wide: {remaining}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
