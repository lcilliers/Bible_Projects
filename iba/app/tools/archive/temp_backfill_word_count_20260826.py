"""temp_backfill_word_count_20260826.py -- escalation #832 item 2, approved by the researcher.

One-off correction: 25 `prose_section` rows have `word_count=0` despite holding real body text
(word_count was never computed for them by whichever write path created them). Recomputes each
using the same formula already used live elsewhere in the codebase
(`scripts/apply_session_patch.py`: `word_count = rec.get("word_count") or len(body.split())`),
through the same `record_change_log` choke-point every other prose_section write already goes
through (`cfg_behaviour_rule` 'record-change-log-choke-point' / 'record-change-log-version-is-
pointer') -- snapshot prior state, write the change-log row, UPDATE with the log id as `version`.

Per governance.scripts_and_routines: temporary script, one-time use, `temp_` prefix -- delete or
archive after running (docs/file-organisation-rules.md sec3.13's equivalent for IBA scripts).
"""
import gzip
import json
import sqlite3
from datetime import datetime, timezone

DB = "database/bible_research.db"


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> None:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT id, heading, body, word_count, status, author, approved_at, approved_by, "
        "metadata_json, created_at FROM prose_section WHERE word_count=0 AND length(body)>50"
    ).fetchall()
    print(f"{len(rows)} rows to fix")
    fixed = []
    for r in rows:
        correct = len(r["body"].split())
        prior = {k: r[k] for k in r.keys()}
        payload = gzip.compress(json.dumps(prior, default=str).encode("utf-8"))
        cur = conn.execute(
            """INSERT INTO record_change_log
               (target_table, target_id, change_type, change_datetime, change_source,
                change_reason, changed_by, status, payload)
               VALUES ('prose_section', ?, 'change', ?, 'temp_backfill_word_count_20260826',
                       'escalation #832 item 2 -- word_count was never computed for this row',
                       'claude_code', 'change_applied', ?)""",
            (r["id"], now(), payload),
        )
        log_id = cur.lastrowid
        conn.execute(
            "UPDATE prose_section SET word_count = ?, version = ?, updated_at = ? WHERE id = ?",
            (correct, log_id, now(), r["id"]),
        )
        fixed.append((r["id"], r["word_count"], correct, log_id))
    conn.commit()
    for row_id, old, new, log_id in fixed:
        print(f"  id={row_id}: word_count {old} -> {new} (record_change_log id={log_id})")
    # verify
    remaining = conn.execute(
        "SELECT count(*) c FROM prose_section WHERE word_count=0 AND length(body)>50"
    ).fetchone()["c"]
    print(f"remaining word_count=0-with-real-body rows: {remaining}")
    conn.close()


if __name__ == "__main__":
    main()
