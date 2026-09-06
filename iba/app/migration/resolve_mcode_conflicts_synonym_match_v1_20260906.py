"""resolve_mcode_conflicts_synonym_match_v1_20260906.py — ONE-OFF. Escalation #1525. Researcher
spotted specific cases the title-exact-match method (#245) missed, verbatim: "you missed obedient,
devot(e) also I see similar meaning words e.g. amazement map to astonishment, anguish to despair,
answer to petition, silent with peace, upright with righteousness, wise with wisdom." Two distinct
gaps in #245's method: (1) stemming misses -- 'obedient'/'Obedience' and 'devote'/'Devotion' share
a root but aren't the identical token my exact-word matcher required; (2) genuine synonyms with no
shared root at all -- 'upright'/'righteousness', 'anguish'/'despair', 'amazement'/'astonishment',
'silent'/'peace' -- which no token-overlap method could ever catch without an explicit list.

Checked each named case against its ACTUAL two conflicting clusters (not assumed) -- two of the
three "answer" codes (`G0611`, `H6032`) pair with M24/M41, not M42/M41, so "answer -> petition"
doesn't apply to them; resolved those to M41 "Being Heard" instead (a judgement call, flagged as
mine, not a re-statement of the researcher's own instruction) since M42 isn't one of their two
options at all. "wise"/"wisdom" was checked against the live remaining set and found no matches --
not applicable, not silently dropped.

What this does, in iba.db, one transaction, direct write (same regime as #245): for each strong
below, retires its LOSING cluster's `cluster_strong` row (`rationale` appended); the winning
cluster's row is untouched. Neither cluster is merged/retired.

    python -m iba.app.migration.resolve_mcode_conflicts_synonym_match_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# (strong, winner, loser, note)
_DECIDED: list[tuple[str, str, str, str]] = [
    ("G0612", "M42", "M41", "answer -> Prayer & Petition, researcher instruction verbatim"),
    ("G0611", "M41", "M24", "to answer -> Being Heard (M42 not an option for this code; Claude's own call, not researcher's)"),
    ("H6032", "M41", "M24", "to answer -> Being Heard (M42 not an option for this code; Claude's own call, not researcher's)"),
    ("G1611", "M48", "M01", "amazement -> Astonishment & Wonder, researcher instruction verbatim"),
    ("G3716", "M12", "M13", "upright -> Righteousness & Integrity, researcher instruction verbatim"),
    ("G5255", "M54", "M30", "obedient -> Torah & Obedience, researcher instruction verbatim (stemming miss in #245)"),
    ("G8146", "M33", "M42", "silent -> Rest & Peace, researcher instruction verbatim"),
    ("H5535", "M33", "M42", "silent -> Rest & Peace, researcher instruction verbatim"),
    ("H2479", "M24", "M03", "anguish -> Faintness & Despair, researcher instruction verbatim"),
    ("H2763A", "M51", "M10", "to devote/destroy -> Love & Devotion, researcher instruction verbatim (stemming miss in #245)"),
    ("H2764A", "M51", "M28", "devoted thing -> Love & Devotion, researcher instruction verbatim (stemming miss in #245)"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        retired = 0
        for strong, winner, loser, note in _DECIDED:
            row = conn.execute(
                "SELECT id, rationale FROM cluster_strong WHERE strong=? AND cluster_code=? "
                "AND deleted=0", (strong, loser)).fetchone()
            if row is None:
                print(f"{strong}: no live {loser} row -- already resolved, skipping")
                continue
            new_rationale = (row["rationale"] or "") + (
                f" | retired 2026-09-06 (escalation #1525, synonym-match pass): {note}")
            conn.execute(
                "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                (new_rationale, row["id"]))
            retired += 1
            print(f"{strong}: retired {loser} (kept {winner}) -- {note}")
        conn.commit()
        print(f"\ntotal rows retired: {retired}")

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
