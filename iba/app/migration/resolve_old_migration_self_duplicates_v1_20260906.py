"""resolve_old_migration_self_duplicates_v1_20260906.py — ONE-OFF. Escalation #1525, researcher
instruction verbatim, 2026-09-06: for the 21 strongs where both conflicting M-code tags trace to
the identical `old-system-migration` source (no newer tag to break the tie by provenance, unlike
the 413 resolved in `retire_old_migration_mcode_conflicts_v1_20260906.py`), the researcher reviewed
the full list directly and gave an explicit per-strong ruling: keep "cluster B" (the second cluster
listed for each strong) in every case except `G4993`, which keeps "cluster A" instead. "The
duplicate in the other cluster must be removed."

`_KEEP` below is that exact ruling — for each strong, which cluster_code stays live; the strong's
OTHER live M-code cluster_strong row (whatever it is) gets soft-deleted.

What this does, in iba.db, one transaction, direct write (`cluster_strong` is a `category='data'`
table with `writer='migration'` grants): for each of the 21 strongs, soft-deletes the M-code
`cluster_strong` row whose `cluster_code` is NOT the kept one (`deleted=1`, `rationale` appended,
never overwritten). Leaves the kept row untouched. Idempotent — a strong already down to one live
M-code row is a no-op.

    python -m iba.app.migration.resolve_old_migration_self_duplicates_v1_20260906
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

# strong -> cluster_code to KEEP (researcher's explicit ruling, this chat, 2026-09-06)
_KEEP: dict[str, str] = {
    "G0019": "M46",   # goodness: Gift&Favor / Wealth&Riches -> keep Wealth&Riches
    "G0929": "M35",   # torment: Grief&Lament / Being Tested -> keep Being Tested
    "G0930": "M27",   # torturer: Grief&Lament / Evil -> keep Evil
    "G2347": "M24",   # pressure: Fear&Awe / Faintness&Despair -> keep Faintness&Despair
    "G4730": "M24",   # hardship: Fear&Awe / Faintness&Despair -> keep Faintness&Despair
    "G4993": "M15",   # be of sound mind: Knowing&Understanding / Inner Seat -> keep Knowing&Understanding (EXCEPTION)
    "H0014": "M30",   # be willing: Desire / Rebellion&Stubbornness -> keep Rebellion&Stubbornness
    "H1361": "M08",   # to exult: Joy&Gladness / Pride&Arrogance -> keep Pride&Arrogance
    "H1793A": "M11",  # contrite: Humility&Lowliness / Turning&Repentance -> keep Turning&Repentance
    "H1984I": "M16",  # to boast/rave madly: Pride&Arrogance / Wisdom&Folly -> keep Wisdom&Folly
    "H2102": "M08",   # to boil: Anger&Wrath / Pride&Arrogance -> keep Pride&Arrogance
    "H2616B": "M07",  # to shame: Kindness&Friendship / Shame&Confusion -> keep Shame&Confusion
    "H2617B": "M07",  # shame: Kindness&Friendship / Shame&Confusion -> keep Shame&Confusion
    "H2750": "M02",   # burning: Fear&Awe / Anger&Wrath -> keep Anger&Wrath
    "H3520B": "M46",  # riches: Praise&Song / Wealth&Riches -> keep Wealth&Riches
    "H4164": "M24",   # constraint: Fear&Awe / Faintness&Despair -> keep Faintness&Despair
    "H4712": "M24",   # terror: Fear&Awe / Faintness&Despair -> keep Faintness&Despair
    "H4843": "M03",   # to provoke: Anger&Wrath / Grief&Lament -> keep Grief&Lament
    "H6869C": "M24",  # vexer: Anger&Wrath / Faintness&Despair -> keep Faintness&Despair
    "H6887E": "M28",  # to rival: Malice&Enmity / Envy&Greed -> keep Envy&Greed
    "H7600": "M46",   # secure: Trust&Refuge / Wealth&Riches -> keep Wealth&Riches
}

_NOTE = (
    " | retired 2026-09-06 (escalation #1525): researcher's own explicit per-strong ruling on the "
    "21 old-system-migration self-duplicates (both tags shared the same unverified source, no "
    "provenance signal to break the tie automatically) -- this cluster was the one NOT kept."
)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        retired = 0
        skipped = []
        for strong, keep_code in _KEEP.items():
            rows = conn.execute(
                "SELECT id, cluster_code, rationale FROM cluster_strong WHERE strong=? "
                "AND deleted=0 AND cluster_code LIKE 'M%'", (strong,)).fetchall()
            live_codes = {r["cluster_code"] for r in rows}
            if keep_code not in live_codes:
                skipped.append((strong, keep_code, sorted(live_codes)))
                continue
            for r in rows:
                if r["cluster_code"] == keep_code:
                    continue
                conn.execute(
                    "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                    ((r["rationale"] or "") + _NOTE, r["id"]))
                retired += 1
                print(f"{strong}: retired {r['cluster_code']} (kept {keep_code})")
        conn.commit()

        print(f"\nrows retired: {retired}")
        if skipped:
            print(f"SKIPPED (kept cluster not found live -- check manually): {skipped}")

        still_multi = conn.execute(
            "SELECT strong FROM cluster_strong WHERE deleted=0 AND cluster_code LIKE 'M%' "
            "AND strong IN ({}) GROUP BY strong HAVING COUNT(DISTINCT cluster_code)>1".format(
                ",".join("?" * len(_KEEP)))
        , tuple(_KEEP)).fetchall()
        print(f"of these 21 strongs, still multi-tagged after this run: {len(still_multi)}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
