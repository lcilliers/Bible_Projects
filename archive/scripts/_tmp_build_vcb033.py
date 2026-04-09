"""Build VCB-033 batch extract — Registry 48 (diligence) pipeline gap repair."""
import sqlite3, os, json

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
BATCH_ID = "VCB-033"
TODAY = "2026-04-09"
REGISTRY_FILTER = [48]

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

def build_term_json(mti_id):
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
    groups = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.context_description, vcg.notes, vcg.delete_flagged,
            (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id=vcg.id AND vc.is_anchor=1 AND vc.delete_flagged=0) as anchor_count,
            (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id=vcg.id AND vc.is_related=1 AND vc.delete_flagged=0) as related_count
        FROM verse_context_group vcg WHERE vcg.mti_term_id=?
    """, (mti_id,)).fetchall()
    existing_groups = [{"id": g["id"], "group_code": g["group_code"], "context_description": g["context_description"],
        "notes": g["notes"], "delete_flagged": g["delete_flagged"], "anchor_count": g["anchor_count"],
        "related_count": g["related_count"]} for g in groups]
    verses_rows = conn.execute("SELECT vr.id as verse_record_id, vr.reference, vr.verse_text, vr.target_word, vr.span_strong_match, vr.delete_flagged as verse_delete_flagged FROM wa_verse_records vr WHERE vr.term_inv_id=? ORDER BY vr.id", (term_inv_id,)).fetchall()
    verses_json, term_total, term_unclassified, prev, sa, anc = [], 0, 0, 0, 0, 0
    for vr in verses_rows:
        vc = conn.execute("SELECT vc.id, vc.group_id, vcg.group_code, vc.is_anchor, vc.is_relevant, vc.is_related, vc.notes, vc.delete_flagged FROM verse_context vc LEFT JOIN verse_context_group vcg ON vcg.id=vc.group_id WHERE vc.verse_record_id=? AND vc.mti_term_id=?", (vr["verse_record_id"], mti_id)).fetchone()
        vc_obj = None
        if vc:
            vc_obj = {"id": vc["id"], "group_id": vc["group_id"], "group_code": vc["group_code"], "is_anchor": vc["is_anchor"], "is_relevant": vc["is_relevant"], "is_related": vc["is_related"], "notes": vc["notes"], "delete_flagged": vc["delete_flagged"]}
            if vc["delete_flagged"] == 0:
                prev += 1
                if vc["is_relevant"] == 0: sa += 1
                if vc["is_anchor"] == 1: anc += 1
        verses_json.append({"verse_record_id": vr["verse_record_id"], "reference": vr["reference"], "verse_text": vr["verse_text"], "target_word": vr["target_word"], "span_strong_match": vr["span_strong_match"], "verse_delete_flagged": vr["verse_delete_flagged"], "verse_context": vc_obj})
        if vr["verse_delete_flagged"] == 0:
            term_total += 1
            if not vc or vc["delete_flagged"] == 1: term_unclassified += 1
    return {"term": {"mti_term_id": mti_id, "strongs_number": mt["strongs_number"], "transliteration": mt["transliteration"], "gloss": mt["gloss"], "language": mt["language"], "mti_status": mt["status"], "term_owner_type": "OWNER", "owning_registry_id": mt["registry_no"], "owning_registry_word": mt["registry_word"], "registry_verse_context_status": mt["verse_context_status"], "term_classification_complete": (term_unclassified == 0) and (term_total > 0), "total_verses": term_total, "unclassified_count": term_unclassified, "existing_groups": existing_groups, "verses": verses_json},
        "stats": {"total": term_total, "unclassified": term_unclassified, "previously_classified": prev, "set_aside": sa, "anchors_existing": anc}}

placeholders = ",".join("?" for _ in REGISTRY_FILTER)
term_rows = conn.execute(f"""
    SELECT mt.id as mti_term_id FROM mti_terms mt
    JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
    JOIN wa_file_index fi ON fi.id=ti.file_id JOIN word_registry wr ON wr.id=fi.word_registry_fk
    LEFT JOIN wa_verse_records vr ON vr.term_inv_id=ti.id AND vr.delete_flagged=0
    WHERE mt.status IN ('extracted','extracted_thin') AND wr.no IN ({placeholders})
    GROUP BY mt.id HAVING COUNT(vr.id) > 0
    ORDER BY wr.no, mt.strongs_number
""", REGISTRY_FILTER).fetchall()

all_mti_ids = [r["mti_term_id"] for r in term_rows]
print(f"Selected {len(all_mti_ids)} OWNER terms")

terms_json = []
totals = {"verses": 0, "unclassified": 0, "classified": 0, "set_aside": 0, "anchors": 0}
for mti_id in all_mti_ids:
    result = build_term_json(mti_id)
    if not result: continue
    terms_json.append(result["term"])
    totals["verses"] += result["stats"]["total"]
    totals["unclassified"] += result["stats"]["unclassified"]

terms_json.sort(key=lambda t: (t["owning_registry_id"], t["strongs_number"]))

batch_json = {"batch_id": BATCH_ID, "produced_date": TODAY,
    "produced_by": "Claude Code — WA-VerseContext-Instruction v2.5",
    "governing_instruction": "WA-VerseContext-Instruction-v2.5-20260409.md",
    "total_verse_count": totals["verses"], "total_term_count": len(terms_json),
    "unclassified_verse_count": totals["unclassified"],
    "verse_context_summary": {"total_verses_in_batch": totals["verses"], "previously_classified": totals["classified"],
        "unclassified": totals["unclassified"], "set_aside_in_prior_batches": totals["set_aside"],
        "anchor_verses_existing": totals["anchors"]},
    "terms": terms_json}

outpath = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "verse_context", f"wa-vcb-033-extract-{TODAY}.json")
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(batch_json, f, indent=2, ensure_ascii=False)
print(f"Written: {outpath}")
print(f"Terms: {len(terms_json)}, Verses: {totals['verses']}, Unclassified: {totals['unclassified']}")
conn.close()
