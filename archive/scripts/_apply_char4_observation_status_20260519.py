"""Mark observation #3 (INTER_RELATIONSHIP for Char 4 Delight) as confirmed
per the Char 4 Phase 9 self-check.
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SOURCE = 'Sessions/Session_Clusters/M04/WA-M04-phase9-char4-Delight-findings-v1-20260519.md'

NOTE = (
    "CONFIRMED via Char 4 Phase 9 self-check; the breadth-integration "
    "surfaced as the central analytical finding of the batch. "
    "(a) M04-G affective and M04-H volitional are not separate but the "
    "affective and volitional faces of a single orientation-toward-object "
    "(Psa 37:4; 40:8; Rom 7:22 show the integration in single instances). "
    "(b) M04-M obedience is M04-H's directed will operating in the "
    "obedience-toward-God register (Joh 8:29 fully integrates M04-H and "
    "M04-M in Christ). (c) M04-P corrupt operates through the same "
    "faculty as the healthy registers (Isa 66:3 nephesh + cha.phets) - "
    "corruption is a question of object, not faculty. Delight is the "
    "most volitionally-constituted and agentively-powerful characteristic "
    "in M04; Isa 53:10's cha.phets makes divine Delight the inner "
    "mechanism of the atonement."
)


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('BEGIN')
    try:
        row = cur.execute('SELECT status, title FROM cluster_observation WHERE id=3').fetchone()
        if not row:
            raise SystemExit('obs#3 not found')
        print(f"obs#3 ({row[1]}) - current status: {row[0]}")
        cur.execute(
            "UPDATE cluster_observation "
            "SET status='confirmed', resolution_note=?, resolved_date=?, "
            "last_updated_date=?, source_file=? "
            "WHERE id=3",
            (NOTE, NOW, NOW, SOURCE),
        )
        conn.commit()
        print("Committed: 1 observation status update.")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise

    print()
    print("=== M04 cluster_observation status ===")
    for r in cur.execute(
        "SELECT id, characteristic_id, observation_type, status "
        "FROM cluster_observation WHERE cluster_code='M04' ORDER BY id"
    ).fetchall():
        print(r)
    conn.close()


if __name__ == '__main__':
    main()
