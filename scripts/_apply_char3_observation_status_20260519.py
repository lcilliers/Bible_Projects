"""Mark observation #4 (INTEGRATION_NOTE for Char 3 Gladness) as confirmed
per the Char 3 Phase 9 self-check.
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path('database/bible_research.db')
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SOURCE = 'Sessions/Session_Clusters/M04/WA-M04-phase9-char3-Gladness-findings-v1-20260519.md'

NOTE = (
    "CONFIRMED via Char 3 Phase 9 self-check. Integration surfaced as the "
    "structural key to Char 3: M04-L cognitive-evaluative (Mic 6:8, Gen 1:31 "
    "ontological baseline) + M04-O experiential-circumstantial together form "
    "Gladness. The evaluative act (M04-L) produces the cognitive recognition "
    "that enables and grounds the experiential warmth (M04-O). Char 3 is the "
    "most cognitively-constituted positive characteristic in M04 - "
    "distinguished from Joy / Exultation / Delight / Pleasure by its unique "
    "cognitive-evaluative primary dimension. Status: analytically validated."
)


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('BEGIN')
    try:
        row = cur.execute(
            'SELECT status, title FROM cluster_observation WHERE id=4'
        ).fetchone()
        if not row:
            raise SystemExit('obs#4 not found')
        print(f"obs#4 ({row[1]}) - current status: {row[0]}")
        cur.execute(
            "UPDATE cluster_observation "
            "SET status='confirmed', resolution_note=?, resolved_date=?, "
            "last_updated_date=?, source_file=? "
            "WHERE id=4",
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
