"""One-off migration: escalation #758 -- researcher's direct instruction on closing out the
content-index bloat investigation: "delete all the rows in the index table so that the size of the
database can reduce again." The current predefined-key concordance design (14.1M rows, ~3.45GB raw
payload before indexes) is judged unsupportable and is being decommissioned pending a redesign
(escalation #770, spawned from #758). Emptied to a clean slate, not a partial trim -- a future
redesign is expected to replace the mechanism, not resume where this left off.

Clears BOTH content_index and content_index_scan, not content_index alone: content_index_scan
records which .md files have already been scanned (by mtime). Leaving it populated while
content_index is empty would silently break contentindex.refresh() forever after -- it would see
every file as "already scanned, nothing changed" and never re-populate the index, with no error
raised anywhere. A true clean slate needs both tables emptied together.

Followed by VACUUM (run separately, not inside this script's own transaction -- VACUUM cannot run
inside a transaction) to actually reclaim the freed disk space; SQLite does not shrink the file on
DELETE alone.

Same class of migration as bootstrap_behaviour_rules_cycle4_v1_20260818.py -- one-off, direct
sqlite3, config_exempt in cfg_utility, registered in the same unit of work.
"""
import pathlib
import sqlite3
import sys

DB_PATH = pathlib.Path(__file__).resolve().parents[1] / "db" / "iba.db"


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM content_index")
    before_index = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM content_index_scan")
    before_scan = cur.fetchone()[0]

    cur.execute("DELETE FROM content_index")
    cur.execute("DELETE FROM content_index_scan")
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM content_index")
    after_index = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM content_index_scan")
    after_scan = cur.fetchone()[0]
    conn.close()

    print(f"content_index: {before_index} -> {after_index} rows")
    print(f"content_index_scan: {before_scan} -> {after_scan} rows")
    print("Run VACUUM separately (not inside this script) to reclaim disk space.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
