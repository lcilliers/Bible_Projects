"""Append wa_verse_records WHERE file_id=48 to inspect_peace_registry.md."""
import sqlite3

DB  = r"g:\My Drive\Bible_study_projects\data\bible_research.db"
OUT = r"g:\My Drive\Bible_study_projects\outputs\markdown\inspect_peace_registry.md"

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

rows = con.execute(
    "SELECT * FROM wa_verse_records WHERE file_id = 48 ORDER BY id"
).fetchall()
con.close()

print(f"Rows found: {len(rows)}")

def md_table(rows):
    if not rows:
        return "_No rows found._\n"
    c = rows[0].keys()
    header = "| " + " | ".join(c) + " |"
    sep    = "| " + " | ".join("---" for _ in c) + " |"
    lines  = [header, sep]
    for r in rows:
        cell = str(r[col]).replace("\n", " ").replace("|", "\\|") if r[col] is not None else ""
        lines.append("| " + " | ".join(
            (str(r[col]).replace("\n", " ").replace("|", "\\|") if r[col] is not None else "")
            for col in c
        ) + " |")
    return "\n".join(lines) + "\n"

with open(OUT, "a", encoding="utf-8") as f:
    f.write(f"\n---\n\n## wa_verse_records — file_id=48\n\n")
    f.write(md_table(rows))
    f.write(f"\n_({len(rows)} row(s))_\n")

print(f"Written to {OUT}")
