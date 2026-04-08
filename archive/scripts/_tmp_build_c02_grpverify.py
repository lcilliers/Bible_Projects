"""Build consolidated group verification extract for C02 Phase C — 28 QA-REVIEW groups."""
import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "dimension_review")

# Groups from the directive with their vcg IDs and issues
GROUPS = [
    # Registry 32 (counsel)
    ("2110-001", 401, "Dual inner-being engagements — plotter's will and victim's shaped inner life"),
    ("748-001", 416, "Bidirectional compression at 50 verses"),
    ("749-001", 405, "Bidirectional compression at 37 verses"),
    ("751-001", 410, "Relational-spiritual dimension — divine intimate friendship"),
    ("751-002", 411, "Membership in divine council — covenantal access"),
    ("751-004", 413, "Trustworthiness in keeping confidence"),
    ("753-003", 421, "Names site (mouth) rather than inner act of vow"),
    ("753-004", 422, "God's mouth as authoritative pronouncement"),
    # Registry 85 (imagination)
    ("916-001", 1292, "Possible conflation — fanciful inner content and false image of security"),
    # Registry 100 (knowledge)
    ("955-001", 1504, "Generic description for 49 verses"),
    ("958-005", 1513, "God's revelatory knowledge — human reception implicit"),
    ("959-001", 1502, "Divine attribute named; human inner-being engagement absent"),
    ("961-002", 1501, "Measure of divine perfection opaque"),
    ("963-004", 1498, "Covers divine and human knowing"),
    # Registry 126 (purpose)
    ("3373-001", 2097, "Dual use — governance foresight vs. provision for fleshly desire"),
    # Registry 160 (thought)
    ("1175-001", 2294, "Broad — intending, planning, aspiration, design"),
    ("3445-001", 2296, "Divine giving of thought — human reception implicit"),
    ("3459-001", 2292, "Holds positive prudence and self-deceiving pride together"),
    # Registry 166 (understanding)
    ("1203-001", 2346, "God hears — Spiritual/God-ward vs Theological/Divine-Human"),
    ("1203-004", 2349, "Broad response range — fear, grief, anger, joy, worship, courage"),
    ("1204-001", 2344, "Too compressed — divinely given inner capacity"),
    # Registry 174 (wisdom)
    ("518-001", 2483, "Inner devotional origin implied; names external act (song)"),
    ("519-002", 2491, "Outer result (success) named rather than inner dimension"),
    ("523-001", 2471, "Divine attribute only — human inner-being absent"),
    ("524-001", 2484, "Same as 523-001"),
    ("527-001", 2495, "Same as 523-001"),
    ("532-001", 2488, "Divine attribute only — candidate QA-EXTERNALISED"),
    ("532-002", 2489, "Christological — wisdom as person of Christ"),
    ("6670-001", 2479, "Physical condition leads; inner recognition at endpoint"),
    ("6672-001", 2481, "Physical mark named; inner pride as cause"),
    ("6672-002", 2482, "Physical feature named; inner desire as subordinate clause"),
]

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

groups_out = []

for group_code, vcg_id, issue in GROUPS:
    # Group metadata
    vcg = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.context_description, vcg.notes
        FROM verse_context_group vcg WHERE vcg.id = ?
    """, (vcg_id,)).fetchone()

    if not vcg:
        print(f"  WARNING: vcg_id={vcg_id} ({group_code}) not found")
        continue

    # Dimension index data
    di = conn.execute("""
        SELECT dimension, dimension_confidence
        FROM wa_dimension_index WHERE group_code = ? AND delete_flagged = 0
    """, (group_code,)).fetchone()

    # Anchor verses
    anchors = conn.execute("""
        SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
               vr.reference, vr.verse_text, vc.is_anchor, vc.is_related
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN books b ON b.id = vr.book_id
        WHERE vc.group_id = ? AND vc.is_anchor = 1 AND vc.delete_flagged = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (vcg_id,)).fetchall()

    # Related verses
    related = conn.execute("""
        SELECT vc.verse_record_id, b.name as book, vr.chapter, vr.verse_num as verse,
               vr.reference, vr.verse_text, vc.is_anchor, vc.is_related
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN books b ON b.id = vr.book_id
        WHERE vc.group_id = ? AND vc.is_related = 1 AND vc.is_anchor = 0 AND vc.delete_flagged = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (vcg_id,)).fetchall()

    groups_out.append({
        "group_code": group_code,
        "verse_context_group_id": vcg_id,
        "context_description": vcg["context_description"],
        "dimension": di["dimension"] if di else None,
        "dimension_confidence": di["dimension_confidence"] if di else None,
        "issue": issue,
        "anchor_verses": [dict(r) for r in anchors],
        "related_verses": [dict(r) for r in related],
    })

    print(f"  {group_code}: {len(anchors)} anchors, {len(related)} related")

result = {
    "extract_meta": {
        "extract_type": "group_verification_batch",
        "cluster": "C02",
        "batch": "anchor-review-phase-c",
        "produced_date": "2026-04-07",
        "total_groups": len(groups_out),
    },
    "groups": groups_out,
}

os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "wa-dim-grpverify-C02-batch1-v1-2026-04-07.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

fsize = os.path.getsize(out_path)
print(f"\nWritten: {out_path}")
print(f"Groups: {len(groups_out)}, Size: {fsize / 1024:.0f} KB")

conn.close()
