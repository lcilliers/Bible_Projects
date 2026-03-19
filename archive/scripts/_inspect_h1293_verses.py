"""Append verses for Strong's H1293 to inspect_peace_registry.md."""
import sqlite3

DB  = r"g:\My Drive\Bible_study_projects\data\bible_research.db"
OUT = r"g:\My Drive\Bible_study_projects\outputs\markdown\inspect_peace_registry.md"

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

# Find the mti_terms row for H1293
term = con.execute(
    "SELECT * FROM mti_terms WHERE strongs_number = 'H1293'"
).fetchone()

if not term:
    print("H1293 not found in mti_terms")
    con.close()
    raise SystemExit(1)

term_id = term["id"]
print(f"mti_terms id={term_id}, gloss={term['gloss']}, owning_registry={term['owning_registry']}")

# Check wa_verse_records columns
cols = [r[1] for r in con.execute("PRAGMA table_info(wa_verse_records)")]
print("wa_verse_records columns:", cols)

# Find term_inventory id(s) for this mti_term
# wa_term_inventory links to mti_terms via mti_term_id or similar
inv_cols = [r[1] for r in con.execute("PRAGMA table_info(wa_term_inventory)")]
print("wa_term_inventory columns:", inv_cols)

inv_rows = con.execute(
    "SELECT * FROM wa_term_inventory WHERE mti_term_id = ?", (term_id,)
).fetchall()
print(f"wa_term_inventory rows for mti_term_id={term_id}: {len(inv_rows)}")
for r in inv_rows:
    print(dict(r))

# Get verses
if inv_rows:
    inv_ids = [r["id"] for r in inv_rows]
    placeholders = ",".join("?" * len(inv_ids))
    verse_rows = con.execute(
        f"SELECT * FROM wa_verse_records WHERE term_inv_id IN ({placeholders}) ORDER BY id",
        inv_ids
    ).fetchall()
else:
    verse_rows = []

print(f"Verses found: {len(verse_rows)}")

con.close()

# Build markdown
def md_table(rows):
    if not rows:
        return "_No rows found._\n"
    c = rows[0].keys()
    header = "| " + " | ".join(c) + " |"
    sep    = "| " + " | ".join("---" for _ in c) + " |"
    lines  = [header, sep]
    for r in rows:
        lines.append("| " + " | ".join(str(r[col]) if r[col] is not None else "" for col in c) + " |")
    return "\n".join(lines) + "\n"

with open(OUT, "a", encoding="utf-8") as f:
    f.write(f"\n---\n\n## wa_verse_records — H1293 ({term['gloss'] or 'n/a'})\n\n")
    f.write(f"**mti_terms id:** {term_id}  \n")
    f.write(f"**gloss:** {term['gloss']}  \n")
    f.write(f"**owning_registry:** {term['owning_registry']}  \n\n")
    f.write(md_table(verse_rows))
    f.write(f"\n_({len(verse_rows)} verse(s))_\n")

print(f"Appended {len(verse_rows)} verses to {OUT}")
