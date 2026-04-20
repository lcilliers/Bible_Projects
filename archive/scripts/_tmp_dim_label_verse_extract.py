"""One-off: build a full verse-evidence extract for the 110 non-canonical dim-label rows.

Reads outputs/dim-label-noncanonical-rows-20260420.json (the 110 wdi_ids)
Emits: outputs/dim-label-verse-evidence-extract-20260420.json

Structure: registry → groups → full verse list (with anchor / related / set-aside
classification from verse_context + ESV text from wa_verse_records).

Purpose: enables Claude AI (or researcher) to do semantic dim-label classification
with verse evidence in hand, not just context_description text.
"""
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

DB_PATH = 'data/bible_research.db'
SOURCE = 'outputs/dim-label-noncanonical-rows-20260420.json'
OUT = 'outputs/dim-label-verse-evidence-extract-20260420.json'

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

with open(SOURCE, encoding='utf-8') as f:
    nc_rows = json.load(f)

# Group wdi_ids by registry for extract structure
wdi_by_reg: dict = {}
for r in nc_rows:
    wdi_by_reg.setdefault(r['registry_no'], []).append(r)

# Schema version
schema_version = conn.execute(
    "SELECT version_code FROM schema_version WHERE id=(SELECT MAX(id) FROM schema_version)"
).fetchone()[0]

out = {
    "meta": {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "schema_version": schema_version,
        "source": "DIR-20260420-002 scope — 110 non-canonical dimension-label rows",
        "purpose": "verse-evidence extract for dim-label canonicalisation; enables semantic analytical pass on the 47 LOW + 23 new-dim-candidate rows",
        "source_file": SOURCE,
        "registry_count": len(wdi_by_reg),
        "row_count": len(nc_rows),
    },
    "registries": {},
}

# Per-registry: fetch word_registry + groups + verses
for reg_no in sorted(wdi_by_reg.keys()):
    reg_row = conn.execute(
        "SELECT id, no, word, cluster_assignment, carry_forward, "
        "session_b_status, verse_context_status, dim_review_status "
        "FROM word_registry WHERE no = ?",
        (reg_no,),
    ).fetchone()
    if not reg_row:
        continue
    reg_entry = {
        "registry_no": reg_row["no"],
        "word": reg_row["word"],
        "cluster_assignment": reg_row["cluster_assignment"],
        "carry_forward": reg_row["carry_forward"],
        "session_b_status": reg_row["session_b_status"],
        "verse_context_status": reg_row["verse_context_status"],
        "dim_review_status": reg_row["dim_review_status"],
        "groups": [],
    }
    for nc in wdi_by_reg[reg_no]:
        wdi_id = nc["wdi_id"]
        # Fetch the wa_dimension_index row + its vcg
        wdi = conn.execute(
            "SELECT wdi.id, wdi.verse_context_group_id, wdi.dimension, "
            "wdi.dimension_confidence, wdi.manual_override, wdi.dominant_subject, "
            "wdi.notes, wdi.anchor_count, wdi.related_count, wdi.set_aside_count, "
            "wdi.total_verse_count, "
            "vcg.group_code, vcg.context_description, vcg.mti_term_id, "
            "mt.strongs_number, mt.transliteration, mt.gloss, mt.language, mt.owning_word "
            "FROM wa_dimension_index wdi "
            "JOIN verse_context_group vcg ON vcg.id = wdi.verse_context_group_id "
            "JOIN mti_terms mt ON mt.id = vcg.mti_term_id "
            "WHERE wdi.id = ?",
            (wdi_id,),
        ).fetchone()
        if not wdi:
            continue

        # Fetch all active verses in this group
        verses = conn.execute(
            "SELECT vr.reference, vr.book_id, vr.chapter, vr.verse_num, "
            "vr.verse_text, vr.translation, vr.span_strong_match, "
            "vc.is_anchor, vc.is_relevant, vc.is_related, vc.set_aside_reason, "
            "vc.notes AS vc_notes "
            "FROM verse_context vc "
            "JOIN wa_verse_records vr ON vr.id = vc.verse_record_id "
            "WHERE vc.group_id = ? AND vc.delete_flagged = 0 AND vr.delete_flagged = 0 "
            "ORDER BY CASE WHEN vc.is_anchor=1 THEN 0 WHEN vc.is_related=1 THEN 1 ELSE 2 END, "
            "         vr.book_id, vr.chapter, vr.verse_num",
            (wdi["verse_context_group_id"],),
        ).fetchall()

        verse_list = []
        anchor_count_actual = 0
        for v in verses:
            role = (
                "anchor" if v["is_anchor"] == 1
                else "related" if v["is_related"] == 1
                else "set-aside" if (v["is_relevant"] == 0 and v["is_anchor"] == 0 and v["is_related"] == 0)
                else "relevant"
            )
            if v["is_anchor"] == 1:
                anchor_count_actual += 1
            verse_list.append({
                "reference": v["reference"],
                "book_id": v["book_id"],
                "chapter": v["chapter"],
                "verse_num": v["verse_num"],
                "translation": v["translation"],
                "role": role,
                "is_anchor": v["is_anchor"],
                "is_relevant": v["is_relevant"],
                "is_related": v["is_related"],
                "set_aside_reason": v["set_aside_reason"],
                "verse_text": v["verse_text"],
                "span_strong_match": v["span_strong_match"],
                "vc_notes": v["vc_notes"],
            })

        # Pull the anchor verse(s) separately for easy consumption
        anchor_verses = [v for v in verse_list if v["is_anchor"] == 1]

        group_entry = {
            "wdi_id": wdi_id,
            "verse_context_group_id": wdi["verse_context_group_id"],
            "group_code": wdi["group_code"],
            "mti_term_id": wdi["mti_term_id"],
            "strongs_number": wdi["strongs_number"],
            "transliteration": wdi["transliteration"],
            "gloss": wdi["gloss"],
            "language": wdi["language"],
            "owning_word": wdi["owning_word"],
            "context_description": wdi["context_description"],
            "current_dim_state": {
                "legacy_label": nc["legacy_label"],
                "dimension_confidence": wdi["dimension_confidence"],
                "manual_override": wdi["manual_override"],
                "dominant_subject": wdi["dominant_subject"],
                "notes": wdi["notes"],
            },
            "counts": {
                "anchor_count_recorded": wdi["anchor_count"],
                "related_count_recorded": wdi["related_count"],
                "set_aside_count_recorded": wdi["set_aside_count"],
                "total_verse_count_recorded": wdi["total_verse_count"],
                "anchor_count_actual": anchor_count_actual,
                "verses_returned": len(verse_list),
            },
            "anchor_verses": anchor_verses,
            "all_verses": verse_list,
        }
        reg_entry["groups"].append(group_entry)

    out["registries"][str(reg_no)] = reg_entry

# Summary stats for meta
out["meta"]["groups_total"] = sum(len(r["groups"]) for r in out["registries"].values())
out["meta"]["verses_total"] = sum(
    g["counts"]["verses_returned"]
    for r in out["registries"].values()
    for g in r["groups"]
)
out["meta"]["anchor_verses_total"] = sum(
    len(g["anchor_verses"])
    for r in out["registries"].values()
    for g in r["groups"]
)

Path(OUT).write_text(
    json.dumps(out, indent=2, ensure_ascii=False),
    encoding='utf-8',
)
size_kb = Path(OUT).stat().st_size / 1024
print(f'Wrote: {OUT} ({size_kb:.1f} KB)')
print()
print(f'Registries: {out["meta"]["registry_count"]}')
print(f'Groups: {out["meta"]["groups_total"]}')
print(f'Verses: {out["meta"]["verses_total"]}')
print(f'Anchor verses: {out["meta"]["anchor_verses_total"]}')
print()
# Per-registry group count
reg_sizes = [(r, len(out["registries"][str(r)]["groups"])) for r in sorted(wdi_by_reg.keys(), key=int)]
print('Per-registry group counts:')
for r, n in reg_sizes:
    word = out["registries"][str(r)]["word"]
    print(f'  r{r:>3} {word:<22}  {n}')
