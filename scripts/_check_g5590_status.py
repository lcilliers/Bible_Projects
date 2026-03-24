"""One-off: read and patch G5590 status_note for WR-08."""
import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
PHRASE = " No separate verse record."

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

row = conn.execute(
    "SELECT id, strongs_number, status_note FROM wa_term_inventory WHERE strongs_number = 'G5590'"
).fetchone()

if not row:
    print("G5590 NOT FOUND in wa_term_inventory")
    conn.close()
    raise SystemExit(1)

print(f"id={row['id']}  strongs={row['strongs_number']}")
print(f"status_note={row['status_note']!r}")

if PHRASE in (row["status_note"] or ""):
    print("Already contains target phrase — no action needed.")
else:
    new_note = (row["status_note"] or "") + PHRASE
    conn.execute(
        "UPDATE wa_term_inventory SET status_note = ? WHERE id = ?",
        (new_note, row["id"]),
    )
    conn.commit()
    print(f"Updated status_note to: {new_note!r}")

conn.close()
