#!/usr/bin/env python3
"""Full DB detail for H4578, H5397, G5590."""
import sqlite3, glob, os, json

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(_ROOT, "data", "bible_research.db")
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

for code in ["H4578", "H5397", "G5590"]:
    print(f"{'='*60}\nCODE: {code}\n{'='*60}")

    rows = conn.execute(
        "SELECT id, strongs_number, step_search_gloss, word_analysis_gloss, "
        "transliteration, language, occurrence_count, delete_flagged, testament, file_id "
        "FROM wa_term_inventory WHERE strongs_number=?", (code,)
    ).fetchall()
    print(f"[wa_term_inventory] rows={len(rows)}")
    for r in rows:
        print(f"  id={r['id']}  file_id={r['file_id']}  step_gloss='{r['step_search_gloss']}'  "
              f"wa_gloss='{r['word_analysis_gloss']}'  translit={r['transliteration']}  "
              f"lang={r['language']}  occur={r['occurrence_count']}  "
              f"testament={r['testament']}  delete_flagged={r['delete_flagged']}")

    if rows:
        ti_id   = rows[0]['id']
        file_id = rows[0]['file_id']

        vtl_count = conn.execute(
            "SELECT COUNT(*) FROM wa_verse_term_links WHERE term_inv_id=?",
            (ti_id,)
        ).fetchone()[0]
        print(f"  -> vtl_rows={vtl_count}")

        linked_verses = conn.execute(
            """SELECT COUNT(*) FROM wa_verse_records vr
               JOIN wa_verse_term_links vtl ON vtl.verse_id = vr.id
               WHERE vtl.term_inv_id=? AND vr.delete_flagged=0""", (ti_id,)
        ).fetchone()[0]
        print(f"  -> active linked verses={linked_verses}")

        mti = conn.execute(
            "SELECT id, strongs_number, gloss, owning_registry, owning_registry_fk, "
            "transliteration, extraction_date, status "
            "FROM mti_terms WHERE strongs_number=?", (code,)
        ).fetchone()
        if mti:
            print(f"\n[mti_terms] id={mti['id']}  gloss='{mti['gloss']}'  "
                  f"owning_registry={mti['owning_registry']}  "
                  f"owning_registry_fk={mti['owning_registry_fk']}  "
                  f"extraction_date={mti['extraction_date']}  status={mti['status']}")
        else:
            print("\n[mti_terms] NO ROW FOUND")

        # quality flags - wa_data_quality_flags uses term_id TEXT (strongs code)
        flags = conn.execute(
            """SELECT dqf.id, dqf.description, qft.flag_code, qft.flag_group
               FROM wa_data_quality_flags dqf
               JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
               WHERE dqf.file_id=? AND dqf.term_id=?""", (file_id, code)
        ).fetchall()
        print(f"\n[quality_flags] count={len(flags)}")
        for f in flags:
            print(f"  {f['flag_code']} [{f['flag_group']}]: {(f['description'] or '')[:110]}")

        # root family
        rf = conn.execute(
            "SELECT COUNT(*) FROM wa_term_root_family WHERE term_inv_id=?",
            (ti_id,)
        ).fetchone()[0]
        print(f"\n[root_family_rows]={rf}")

        # related words
        rw = conn.execute(
            "SELECT COUNT(*) FROM wa_term_related_words WHERE term_inv_id=?",
            (ti_id,)
        ).fetchone()[0]
        print(f"[related_word_rows]={rw}")

    print()

# JSON
disc_dir = os.path.join(_ROOT, "data", "discovery")
jfiles = sorted(glob.glob(os.path.join(disc_dir, "182_soul_step_data_*.json")))
if jfiles:
    jf = jfiles[-1]
    print(f"\n{'='*60}\nJSON FILE: {os.path.basename(jf)}\n{'='*60}")
    with open(jf) as fh:
        j = json.load(fh)
    print(f"anchors:      {j['meta']['anchor_codes']}")
    print(f"generated:    {j['meta']['generated']}")
    print(f"step_version: {j['meta']['step_version']}")
    print(f"total_terms:  {j['meta']['total_terms_evaluated']}")
    print(f"\ninclude_codes ({len(j['meta']['include_codes'])}):")
    for c in j['meta']['include_codes']:
        print(f"  {c}")
    print(f"\nexclude_codes ({len(j['meta']['exclude_codes'])}):")
    for c in j['meta']['exclude_codes']:
        print(f"  {c}")
    print("\nSearching terms[] for H4578, H5397, G5590:")
    found = [t for t in j["terms"] if t["code"] in ("H4578","H5397","G5590")]
    if found:
        for t in found:
            print(f"  FOUND: code={t['code']}  action={t['action']}  group={t['decision_group']}")
    else:
        print("  RESULT: NOT FOUND — none of these codes appear anywhere in j['terms']")

    print("\nAll terms in JSON:")
    print(f"{'CODE':<12}  {'GRP':<4}  {'ACTION':<8}  GLOSS")
    for t in j["terms"]:
        print(f"  {t['code']:<12}  {t['decision_group']:<4}  {t['action']:<8}  {t.get('gloss','')[:40]}")

conn.close()
