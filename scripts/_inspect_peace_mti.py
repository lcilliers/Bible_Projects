"""Append MTI records for registry 117 (peace) to inspect_peace_registry.md."""
import sqlite3, os

DB = r"g:\My Drive\Bible_study_projects\data\bible_research.db"
OUT = r"g:\My Drive\Bible_study_projects\outputs\markdown\inspect_peace_registry.md"

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

# wa_file_index rows for registry 117
fi_rows = con.execute(
    "SELECT * FROM wa_file_index WHERE registry_id = '117' OR registry_id = 117 ORDER BY id"
).fetchall()

# mti_terms rows via owning_registry
mti_rows = con.execute("""
    SELECT *
    FROM mti_terms
    WHERE owning_registry = 117 OR owning_registry = '117'
    ORDER BY id
""").fetchall()

# wa_term_inventory rows
inv_rows = con.execute("""
    SELECT ti.*
    FROM wa_term_inventory ti
    JOIN wa_file_index fi ON fi.id = ti.file_id
    WHERE fi.registry_id = '117' OR fi.registry_id = 117
    ORDER BY ti.id
""").fetchall()

con.close()

def md_table(rows):
    if not rows:
        return "_No rows found._\n"
    cols = rows[0].keys()
    header = "| " + " | ".join(cols) + " |"
    sep    = "| " + " | ".join("---" for _ in cols) + " |"
    lines  = [header, sep]
    for r in rows:
        lines.append("| " + " | ".join(str(r[c]) if r[c] is not None else "" for c in cols) + " |")
    return "\n".join(lines) + "\n"

with open(OUT, "a", encoding="utf-8") as f:
    f.write("\n---\n\n## wa_file_index — registry_id 117\n\n")
    f.write(md_table(fi_rows))
    f.write(f"\n_({len(fi_rows)} row(s))_\n")

    f.write("\n---\n\n## mti_terms — via wa_file_index\n\n")
    f.write(md_table(mti_rows))
    f.write(f"\n_({len(mti_rows)} row(s))_\n")

    f.write("\n---\n\n## wa_term_inventory — via wa_file_index\n\n")
    f.write(md_table(inv_rows))
    f.write(f"\n_({len(inv_rows)} row(s))_\n")

print(f"Appended {len(fi_rows)} file_index, {len(mti_rows)} mti_terms, {len(inv_rows)} term_inventory rows.")
print(f"Written to {OUT}")
