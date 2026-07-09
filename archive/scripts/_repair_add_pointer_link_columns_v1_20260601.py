"""Add cluster-link columns to the Session B/D pointer tables (guarded, idempotent).

Adds (if missing) to wa_session_b_findings and wa_session_research_flags:
  - cluster_link        TEXT   (multi-value, comma-separated cluster codes)
  - cluster_link_basis  TEXT   ('strongs' / 'translit' / 'strongs+translit')

Same operation as a migration's _add_column_if_missing, but standalone — does NOT
touch schema_version (the engine's EXPECTED_SCHEMA_VERSION is a stale 3.27.0 vs the
DB's 3.28.0, so `--migrate` is deliberately avoided). Nullable columns → reversible.

DEFAULT IS DRY-RUN. Pass --apply to write.
"""
import argparse
import sqlite3

DB = "database/bible_research.db"
TARGETS = [
    ("wa_session_b_findings", "cluster_link", "TEXT"),
    ("wa_session_b_findings", "cluster_link_basis", "TEXT"),
    ("wa_session_research_flags", "cluster_link", "TEXT"),
    ("wa_session_research_flags", "cluster_link_basis", "TEXT"),
]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); a = ap.parse_args()
    conn = sqlite3.connect(DB, timeout=15)
    cur = conn.cursor()
    todo = []
    for table, col, typ in TARGETS:
        cols = {r[1] for r in cur.execute(f"PRAGMA table_info({table})")}
        if col not in cols:
            todo.append((table, col, typ))
    print(f"{'APPLY' if a.apply else 'DRY-RUN'}: columns to add: {len(todo)}")
    for t, c, ty in todo:
        print(f"  + {t}.{c} {ty}")
    if not todo:
        print("  (all already present — nothing to do)")
    if not a.apply or not todo:
        conn.close(); return
    cur.execute("BEGIN")
    try:
        for t, c, ty in todo:
            cur.execute(f"ALTER TABLE {t} ADD COLUMN {c} {ty}")
        conn.commit()
    except Exception:
        conn.rollback(); raise
    print(f"APPLIED: added {len(todo)} columns.")
    conn.close()


if __name__ == "__main__":
    main()
