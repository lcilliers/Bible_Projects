"""Build VCB-024 batch extract JSON.

Includes:
  - Unclassified OWNER terms (the work items) — target 2000-2500 unclassified verses
  - Already-classified OWNER terms from the same registries (context for Claude AI)
    with term_classification_complete: true and full verse_context records
"""
import sqlite3
import os
import json
from collections import Counter

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
BATCH_ID = "VCB-024"
TODAY = "2026-04-05"
TARGET_MIN = 2000
TARGET_MAX = 2500

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


# ── Step 1: Select unclassified OWNER terms (the work items) ──

term_rows = conn.execute("""
SELECT mt.id as mti_term_id,
       wr.no as registry_no,
       COUNT(vr.id) as total_verses,
       SUM(CASE WHEN NOT EXISTS (
           SELECT 1 FROM verse_context vc
           WHERE vc.verse_record_id = vr.id AND vc.mti_term_id = mt.id AND vc.delete_flagged = 0
       ) THEN 1 ELSE 0 END) as unclassified_count
FROM mti_terms mt
JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
  AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
LEFT JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
WHERE mt.status IN ('extracted', 'extracted_thin')
  AND wr.verse_context_status = 'In Progress'
GROUP BY mt.id
HAVING unclassified_count > 0 AND total_verses > 0
ORDER BY wr.no ASC, mt.strongs_number ASC
""").fetchall()

# Accumulate to target
work_mti_ids = []
batch_unclassified = 0
for r in term_rows:
    uc = r["unclassified_count"]
    if batch_unclassified + uc > TARGET_MAX and batch_unclassified >= TARGET_MIN:
        break
    if batch_unclassified + uc > TARGET_MAX and batch_unclassified > 0:
        break
    work_mti_ids.append(r["mti_term_id"])
    batch_unclassified += uc

print(f"Work terms (unclassified): {len(work_mti_ids)}, {batch_unclassified} unclassified verses")

# ── Step 2: Identify registries touched, get already-classified terms ──

# Collect registries from work terms
work_registries = set()
for mid in work_mti_ids:
    r = conn.execute("""
        SELECT wr.no FROM mti_terms mt
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE mt.id = ?
    """, (mid,)).fetchone()
    if r:
        work_registries.add(r["no"])

print(f"Registries in batch: {sorted(work_registries)}")

# Get already-classified OWNER terms from these registries (with verses)
classified_mti_ids = []
for reg_no in sorted(work_registries):
    rows = conn.execute("""
        SELECT DISTINCT mt.id as mti_term_id
        FROM mti_terms mt
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
          AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged = 0
        WHERE wr.no = ?
          AND mt.status IN ('extracted', 'extracted_thin')
          AND mt.id NOT IN ({})
          AND EXISTS (
            SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
          )
        ORDER BY mt.strongs_number
    """.format(",".join(str(x) for x in work_mti_ids)), (reg_no,)).fetchall()
    for row in rows:
        classified_mti_ids.append(row["mti_term_id"])

# Deduplicate (a term might appear in multiple registries)
classified_mti_ids = list(dict.fromkeys(classified_mti_ids))
print(f"Already-classified terms to include: {len(classified_mti_ids)}")

# ── Step 3: Build full JSON ──

all_mti_ids = classified_mti_ids + work_mti_ids  # classified first, then work items
# Actually, order by registry then strongs within each — let's build all terms
# and sort by owning_registry_id then strongs_number

terms_json = []
totals = {"verses": 0, "unclassified": 0, "classified": 0, "set_aside": 0, "anchors": 0}
skipped = 0

for mti_id in all_mti_ids:
    result = build_term_json(mti_id)
    if not result:
        skipped += 1
        continue
    terms_json.append(result["term"])
    totals["verses"] += result["stats"]["total"]
    totals["unclassified"] += result["stats"]["unclassified"]
    totals["classified"] += result["stats"]["previously_classified"]
    totals["set_aside"] += result["stats"]["set_aside"]
    totals["anchors"] += result["stats"]["anchors_existing"]

if skipped:
    print(f"Skipped {skipped} terms (no OWNER inventory path)")

# Sort: by owning_registry_id ascending, then strongs_number
terms_json.sort(key=lambda t: (t["owning_registry_id"], t["strongs_number"]))

# Deduplicate by mti_term_id (safety check)
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
    f"wa-vcb-024-extract-{TODAY}.json",
)
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(batch_json, f, indent=2, ensure_ascii=False)

fsize = os.path.getsize(outpath)
print(f"\nWritten: {outpath}")
print(f"File size: {fsize / 1024:.0f} KB ({fsize / (1024*1024):.1f} MB)")
print(f"Terms: {len(terms_json)} ({len(classified_mti_ids)} classified + {len(work_mti_ids)} unclassified)")
print(f"Total verses in batch: {totals['verses']}")
print(f"Unclassified verses: {totals['unclassified']}")
print(f"Previously classified: {totals['classified']}")
print(f"Set aside (prior): {totals['set_aside']}")
print(f"Anchors existing: {totals['anchors']}")

# Registry breakdown
reg_terms_c = Counter()
reg_terms_u = Counter()
reg_verses_u = Counter()
for t in terms_json:
    key = f"{t['owning_registry_id']} ({t['owning_registry_word']})"
    if t["term_classification_complete"]:
        reg_terms_c[key] += 1
    else:
        reg_terms_u[key] += 1
        reg_verses_u[key] += t["unclassified_count"]

all_keys = sorted(set(list(reg_terms_c.keys()) + list(reg_terms_u.keys())),
                  key=lambda x: int(x.split()[0]))
print("\nRegistry breakdown:")
print(f"  {'Registry':<30} {'Classified':>10} {'Unclassified':>12} {'Uncl. verses':>12}")
for reg in all_keys:
    print(f"  {reg:<30} {reg_terms_c.get(reg, 0):>10} {reg_terms_u.get(reg, 0):>12} {reg_verses_u.get(reg, 0):>12}")

conn.close()
