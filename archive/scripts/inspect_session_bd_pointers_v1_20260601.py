"""Read-only structural orientation for Session B & D pointers.

Dumps columns + row counts for the pointer/finding/observation tables, plus the
flag_code distribution, so the mapping-to-terms (and therefore clusters) can be
assessed on real structure rather than assumption.

  python scripts/inspect_session_bd_pointers_v1_20260601.py
"""
import sqlite3

DB = "database/bible_research.db"
TABLES = [
    "wa_session_research_flags",
    "wa_session_b_findings",
    "wa_finding_entity_links",
    "wa_session_b_dimensions",
    "session_d_runs",
    "session_d_observations",
    "session_d_term_links",
    "session_d_verse_links",
]


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    existing = {r["name"] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'")}

    for t in TABLES:
        if t not in existing:
            print(f"\n== {t} == (NOT PRESENT)")
            continue
        cols = [r["name"] for r in cur.execute(f"PRAGMA table_info({t})")]
        n = cur.execute(f"SELECT COUNT(1) FROM {t}").fetchone()[0]
        print(f"\n== {t} == rows={n}")
        print("  cols:", cols)

    # flag_code distribution (the SB_* / SD_* pointers live here)
    print("\n== wa_session_research_flags.flag_code distribution ==")
    for r in cur.execute("SELECT flag_code, COUNT(1) n FROM wa_session_research_flags GROUP BY flag_code ORDER BY n DESC"):
        print(f"  {r['flag_code']}: {r['n']}")

    # session_d_observations: any status/type columns + distribution if present
    if "session_d_observations" in existing:
        oc = [r["name"] for r in cur.execute("PRAGMA table_info(session_d_observations)")]
        for col in ("observation_type", "status", "pointer_type"):
            if col in oc:
                print(f"\n== session_d_observations.{col} ==")
                for r in cur.execute(f"SELECT {col} v, COUNT(1) n FROM session_d_observations GROUP BY {col} ORDER BY n DESC"):
                    print(f"  {r['v']}: {r['n']}")

    conn.close()


if __name__ == "__main__":
    main()
