"""Trace the 3 M15 VC-coverage gap terms: H8637, G1231, G3312.
For each: ownership, verse evidence, placement history, vc_status journey,
and any verse_context rows (active or soft-deleted) that may exist."""
import sqlite3, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

TERMS = [
    ("H8637", "tir.gal", "to teach"),
    ("G1231", "diaginōskō", "to decide"),
    ("G3312", "meristēs", "arbiter"),
]


def banner(s):
    print("\n" + "=" * 80 + f"\n  {s}\n" + "=" * 80)


def kv(label, value, indent=2):
    pad = " " * indent
    if isinstance(value, str) and len(value) > 200:
        value = value[:200] + "…"
    if value is None or value == "":
        value = "(none)"
    print(f"{pad}{label:30s} {value}")


for strongs, translit, gloss in TERMS:
    banner(f"{strongs} — {translit} ({gloss})")

    # ---- 1. mti_terms canonical ----
    mt = conn.execute("""
        SELECT id, strongs_number, transliteration, gloss, language,
               owning_word, owning_registry_fk, status, cluster_code,
               vc_status, vc_status_note, vc_status_updated_at, anchor_note,
               extraction_date, last_changed
          FROM mti_terms WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0
    """, (strongs,)).fetchone()
    if not mt:
        print("  (no mti_terms row)")
        continue

    print("\n[1] mti_terms canonical row")
    for k in ("id","owning_word","owning_registry_fk","status","cluster_code",
              "vc_status","vc_status_note","vc_status_updated_at","anchor_note",
              "extraction_date","last_changed"):
        kv(k, mt[k])

    # ---- 2. wa_term_inventory occurrences (which registries pulled it) ----
    print("\n[2] Inventory rows (registries that pulled this term)")
    inv = list(conn.execute("""
        SELECT ti.id, ti.term_owner_type,
               ti.term_introduction_source, ti.term_introduction_rationale,
               ti.term_introduction_date,
               wr.no AS reg_no, wr.word AS reg_word
          FROM wa_term_inventory ti
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE ti.strongs_number=? AND COALESCE(ti.delete_flagged,0)=0
         ORDER BY wr.no
    """, (strongs,)).fetchall())
    print(f"  {len(inv)} row(s):")
    for r in inv:
        intro = (r["term_introduction_source"] or "")[:50]
        rationale = (r["term_introduction_rationale"] or "")[:60]
        print(f"    - reg {r['reg_no']:>3d} ({r['reg_word']:25s}) owner={r['term_owner_type']:6s}  "
              f"intro={intro}")
        if rationale:
            print(f"      rationale: {rationale}")

    # ---- 3. wa_verse_records: how many verses ----
    print("\n[3] Verse evidence (wa_verse_records)")
    v_total = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE term_id=?", (strongs,)).fetchone()[0]
    v_active = conn.execute("SELECT COUNT(*) FROM wa_verse_records WHERE term_id=? AND COALESCE(delete_flagged,0)=0", (strongs,)).fetchone()[0]
    v_flagged = v_total - v_active
    print(f"  total verse records:  {v_total}  (active {v_active}, soft-deleted {v_flagged})")

    # Sample verses (active only)
    if v_active > 0:
        sample = list(conn.execute("""
            SELECT vr.reference, SUBSTR(vr.verse_text,1,80) AS vt,
                   wr.no AS owner_reg, wr.word AS owner_word
              FROM wa_verse_records vr
              JOIN wa_file_index fi ON fi.id = vr.file_id
              JOIN word_registry wr ON wr.id = fi.word_registry_fk
             WHERE vr.term_id=? AND COALESCE(vr.delete_flagged,0)=0
             ORDER BY vr.book_id, vr.chapter, vr.verse_num
             LIMIT 5
        """, (strongs,)).fetchall())
        print(f"  Sample verses (under owning registries):")
        for s in sample:
            print(f"    {s['reference']:>12s} (owner: reg {s['owner_reg']} {s['owner_word']})")
            print(f"      > {s['vt']}…")

    # ---- 4. verse_context: any rows at all (active or flagged) ----
    print("\n[4] verse_context rows for this mti_term_id (any state)")
    vc_total = conn.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=?", (mt["id"],)).fetchone()[0]
    vc_active = conn.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (mt["id"],)).fetchone()[0]
    print(f"  total vc rows:  {vc_total}  (active {vc_active}, soft-deleted {vc_total - vc_active})")

    # ---- 5. mti_term_subgroup placement (which clusters) ----
    print("\n[5] Sub-group placements")
    placements = list(conn.execute("""
        SELECT cs.cluster_code, cs.subgroup_code, cs.label,
               mts.placement_note, mts.created_at, mts.last_updated_date
          FROM mti_term_subgroup mts
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
         WHERE mts.mti_term_id=? AND COALESCE(mts.delete_flagged,0)=0
         ORDER BY cs.cluster_code, cs.subgroup_code
    """, (mt["id"],)).fetchall())
    for p in placements:
        print(f"    {p['cluster_code']}.{p['subgroup_code']:14s}  {p['label']}")
        kv("placement_note", p["placement_note"], indent=8)
        kv("created_at", p["created_at"], indent=8)

    # Soft-deleted placements (history)
    print("\n  Soft-deleted placements (history):")
    deleted_placements = list(conn.execute("""
        SELECT cs.cluster_code, cs.subgroup_code, cs.label,
               mts.placement_note, mts.created_at, mts.last_updated_date
          FROM mti_term_subgroup mts
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
         WHERE mts.mti_term_id=? AND mts.delete_flagged=1
         ORDER BY cs.cluster_code, cs.subgroup_code
    """, (mt["id"],)).fetchall())
    if deleted_placements:
        for p in deleted_placements:
            print(f"    {p['cluster_code']}.{p['subgroup_code']:14s}  {p['label']}  (deleted)")
            kv("placement_note", p["placement_note"], indent=8)
    else:
        print("    (none)")

    # ---- 6. What did STEP say about this term? ----
    print("\n[6] STEP source (short_def_mounce / meaning preview)")
    if inv:
        ti_id = inv[0]["id"]
        ti = conn.execute("""
            SELECT short_def_mounce, meaning, lsj_entry, parsed_meaning_id
              FROM wa_term_inventory WHERE id=?
        """, (ti_id,)).fetchone()
        if ti["short_def_mounce"]:
            print(f"  short_def_mounce: {ti['short_def_mounce'][:300]}…")
        if ti["meaning"]:
            print(f"  meaning: {ti['meaning'][:200]}…")

conn.close()
