"""Update cluster_observation status open->confirmed for the two observations
that Char 2 (Joy) Phase 9 explicitly addressed.

Per the Char 2 findings self-check:
- INTER_RELATIONSHIP (Joy/Gladness within M04-B and M04-C): CONFIRMED
- SPLIT_SUBGROUP (M04-E serves Char 2 + Char 7): CONFIRMED

The carry-forward resolution text from the self-check is copied verbatim
into cluster_observation.resolution_note for traceability.
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path('database/bible_research.db')
NOW_UTC = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SOURCE_FILE = 'Sessions/Session_Clusters/M04/WA-M04-phase9-char2-Joy-findings-v1-20260518.md'

UPDATES = [
    (1, 'CONFIRMED via Char 2 Phase 9 self-check. The Joy/Gladness boundary '
        'surfaces as one of the most significant analytical findings of '
        "Characteristic 2's Phase 9. Evidence: (a) sa.mach and sim.chah appear "
        'in close synonymous parallelism throughout M04-B; (b) the formulaic '
        '"joy and gladness" pairing is the most common co-occurrence pattern; '
        '(c) the boundary is clearest at the extremes (Hab 3:18 type Joy is '
        'not Gladness; Lam 3:26 type Gladness is not Joy) and most porous in '
        'the middle register. To be primary finding in Session D cluster-scope '
        'synthesis.'),
    (2, 'CONFIRMED via Char 2 Phase 9 self-check. The split is validated by '
        'the evidence: M04-E-VCG-01 (sa.s.von corpus - OT restoration joy) '
        'belongs to Char 2 as eschatological-Joy register; M04-E-VCG-02 '
        '(agalliao - NT exulting-beyond-circumstance) belongs to Char 7 '
        '(Suffering-Joy) in its paradox-of-joy-in-suffering register. Several '
        'verses (1Pe 1:8; Mat 5:12; Rev 19:7) carry evidence for both '
        'characteristics simultaneously. Char 7 Phase 9 should treat '
        'M04-E-VCG-02 as primary evidence base.'),
]


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('BEGIN')
    try:
        for obs_id, note in UPDATES:
            row = cur.execute(
                'SELECT status, title FROM cluster_observation WHERE id=?',
                (obs_id,),
            ).fetchone()
            if not row:
                raise SystemExit(f"cluster_observation id={obs_id} not found")
            print(f"obs#{obs_id} ({row[1]}) — current status: {row[0]}")
            cur.execute(
                "UPDATE cluster_observation "
                "SET status='confirmed', resolution_note=?, resolved_date=?, "
                "last_updated_date=?, source_file=? "
                "WHERE id=?",
                (note, NOW_UTC, NOW_UTC, SOURCE_FILE, obs_id),
            )
        conn.commit()
        print("\nCommitted: 2 observation status updates.")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise

    # Verify
    print("\n=== Post-update cluster_observation status for M04 ===")
    for r in cur.execute(
        "SELECT id, characteristic_id, observation_type, status, "
        "       SUBSTR(resolution_note, 1, 60) "
        "FROM cluster_observation WHERE cluster_code='M04' ORDER BY id"
    ).fetchall():
        print(r)
    conn.close()


if __name__ == '__main__':
    main()
