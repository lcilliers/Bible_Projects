"""Build VCB-027 batch extract JSON.

Registries 197 (authority) + 199 (dominion) — C20 pair.
Includes already-classified terms from these registries as context.
"""
import sqlite3
import os
import json
from collections import Counter

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
BATCH_ID = "VCB-027"
TODAY = "2026-04-06"
REGISTRY_FILTER = [197, 199]

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row


def build_term_json(mti_id):
    """Build the full term JSON object for a given mti_term_id."""
    mt = conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss, mt.language, mt.status,
               wr.no as registry_no, wr.word as registry_word, wr.verse_context_status,
               ti.id as term_inv_id
        FROM mti_terms mt
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE mt.id = ?
    """, (mti_id,)).fetchone()

    if not mt:
        return None

    term_inv_id = mt["term_inv_id"]

    # Existing groups (ALL including delete_flagged)
    groups = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.context_description, vcg.notes, vcg.delete_flagged,
            (SELECT COUNT(*) FROM verse_context vc
             WHERE vc.group_id = vcg.id AND vc.is_anchor = 1 AND vc.delete_flagged = 0) as anchor_count,
            (SELECT COUNT(*) FROM verse_context vc
             WHERE vc.group_id = vcg.id AND vc.is_related = 1 AND vc.delete_flagged = 0) as related_count
        FROM verse_context_group vcg
        WHERE vcg.mti_term_id = ?
    """, (mti_id,)).fetchall()

    existing_groups = [
        {
            "id": g["id"],
            "group_code": g["group_code"],
            "context_description": g["context_description"],
            "notes": g["notes"],
            "delete_flagged": g["delete_flagged"],
            "anchor_count": g["anchor_count"],
            "related_count": g["related_count"],
        }
        for g in groups
    ]

    # ALL verses (including delete_flagged for revision history)
    verses_rows = conn.execute("""
        SELECT vr.id as verse_record_id, vr.reference, vr.verse_text, vr.target_word,
               vr.span_strong_match, vr.delete_flagged as verse_delete_flagged
        FROM wa_verse_records vr
        WHERE vr.term_inv_id = ?
        ORDER BY vr.id
    """, (term_inv_id,)).fetchall()

    verses_json = []
    term_total = 0
    term_unclassified = 0
    previously_classified = 0
    set_aside = 0
    anchors_existing = 0

    for vr in verses_rows:
        vc = conn.execute("""
            SELECT vc.id, vc.group_id, vcg.group_code, vc.is_anchor, vc.is_relevant,
                   vc.is_related, vc.notes, vc.delete_flagged
            FROM verse_context vc
            LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
            WHERE vc.verse_record_id = ? AND vc.mti_term_id = ?
        """, (vr["verse_record_id"], mti_id)).fetchone()

        vc_obj = None
        if vc:
            vc_obj = {
                "id": vc["id"],
                "group_id": vc["group_id"],
                "group_code": vc["group_code"],
                "is_anchor": vc["is_anchor"],
                "is_relevant": vc["is_relevant"],
                "is_related": vc["is_related"],
                "notes": vc["notes"],
                "delete_flagged": vc["delete_flagged"],
            }
            if vc["delete_flagged"] == 0:
                previously_classified += 1
                if vc["is_relevant"] == 0:
                    set_aside += 1
                if vc["is_anchor"] == 1:
                    anchors_existing += 1

        verses_json.append({
            "verse_record_id": vr["verse_record_id"],
            "reference": vr["reference"],
            "verse_text": vr["verse_text"],
            "target_word": vr["target_word"],
            "span_strong_match": vr["span_strong_match"],
            "verse_delete_flagged": vr["verse_delete_flagged"],
            "verse_context": vc_obj,
        })

        if vr["verse_delete_flagged"] == 0:
            term_total += 1
            if not vc or vc["delete_flagged"] == 1:
                term_unclassified += 1

    term_classification_complete = (term_unclassified == 0) and (term_total > 0)

    return {
        "term": {
            "mti_term_id": mti_id,
            "strongs_number": mt["strongs_number"],
            "transliteration": mt["transliteration"],
            "gloss": mt["gloss"],
            "language": mt["language"],
            "mti_status": mt["status"],
            "term_owner_type": "OWNER",
            "owning_registry_id": mt["registry_no"],
            "owning_registry_word": mt["registry_word"],
            "registry_verse_context_status": mt["verse_context_status"],
            "term_classification_complete": term_classification_complete,
            "total_verses": term_total,
            "unclassified_count": term_unclassified,
            "existing_groups": existing_groups,
            "verses": verses_json,
        },
        "stats": {
            "total": term_total,
            "unclassified": term_unclassified,
            "previously_classified": previously_classified,
            "set_aside": set_aside,
            "anchors_existing": anchors_existing,
        },
    }


# ── Step 1: Select OWNER terms for target registries ──

placeholders = ",".join("?" for _ in REGISTRY_FILTER)
term_rows = conn.execute(f"""
SELECT mt.id as mti_term_id, mt.strongs_number, wr.no as reg,
       COUNT(vr.id) as total_verses
FROM mti_terms mt
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
  AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
LEFT JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
WHERE mt.status IN ('extracted', 'extracted_thin')
  AND wr.no IN ({placeholders})
GROUP BY mt.id
HAVING total_verses > 0
ORDER BY wr.no ASC, mt.strongs_number ASC
""", REGISTRY_FILTER).fetchall()

all_mti_ids = [r["mti_term_id"] for r in term_rows]
print(f"Selected {len(all_mti_ids)} OWNER terms from registries {REGISTRY_FILTER}")

# ── Step 2: Build JSON ──

terms_json = []
totals = {"verses": 0, "unclassified": 0, "classified": 0, "set_aside": 0, "anchors": 0}

for mti_id in all_mti_ids:
    result = build_term_json(mti_id)
    if not result:
        print(f"  SKIP mti_term_id={mti_id}: no OWNER inventory path")
        continue
    terms_json.append(result["term"])
    totals["verses"] += result["stats"]["total"]
    totals["unclassified"] += result["stats"]["unclassified"]
    totals["classified"] += result["stats"]["previously_classified"]
    totals["set_aside"] += result["stats"]["set_aside"]
    totals["anchors"] += result["stats"]["anchors_existing"]

# Sort by registry then strongs
terms_json.sort(key=lambda t: (t["owning_registry_id"], t["strongs_number"]))

# Deduplicate by mti_term_id
seen = set()
deduped = []
for t in terms_json:
    if t["mti_term_id"] not in seen:
        seen.add(t["mti_term_id"])
        deduped.append(t)
terms_json = deduped

batch_json = {
    "batch_id": BATCH_ID,
    "produced_date": TODAY,
    "produced_by": "Claude Code \u2014 WA-VerseContext-Instruction v2.4",
    "governing_instruction": "WA-VerseContext-Instruction-v2.4-20260403.md",
    "total_verse_count": totals["verses"],
    "total_term_count": len(terms_json),
    "unclassified_verse_count": totals["unclassified"],
    "verse_context_summary": {
        "total_verses_in_batch": totals["verses"],
        "previously_classified": totals["classified"],
        "unclassified": totals["unclassified"],
        "set_aside_in_prior_batches": totals["set_aside"],
        "anchor_verses_existing": totals["anchors"],
    },
    "terms": terms_json,
}

outpath = os.path.join(
    os.path.dirname(__file__), "..", "data", "exports", "verse_context",
    f"wa-vcb-027-extract-{TODAY}.json",
)
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(batch_json, f, indent=2, ensure_ascii=False)

fsize = os.path.getsize(outpath)
print(f"\nWritten: {outpath}")
print(f"File size: {fsize / 1024:.0f} KB ({fsize / (1024*1024):.1f} MB)")
print(f"Terms: {len(terms_json)}")
print(f"Total verses: {totals['verses']}")
print(f"Unclassified: {totals['unclassified']}")
print(f"Previously classified: {totals['classified']}")

# Registry breakdown
reg_terms = Counter()
reg_verses = Counter()
for t in terms_json:
    key = f"{t['owning_registry_id']} ({t['owning_registry_word']})"
    reg_terms[key] += 1
    reg_verses[key] += t["unclassified_count"]

print("\nRegistry breakdown:")
for reg in sorted(reg_terms.keys(), key=lambda x: int(x.split()[0])):
    print(f"  {reg}: {reg_terms[reg]} terms, {reg_verses[reg]} unclassified verses")

conn.close()
