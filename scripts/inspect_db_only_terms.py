"""Detail query for DB_ONLY terms flagged during soul audit."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analytics.db_client import get_connection

conn = get_connection()
codes = ("H4578", "H5397", "G5590")

for code in codes:
    print(f"\n{'='*60}")
    print(f"  {code}")
    print(f"{'='*60}")

    ti = conn.execute(
        "SELECT * FROM wa_term_inventory WHERE strongs_number=? AND file_id=36",
        (code,)
    ).fetchone()
    if not ti:
        print("  NOT FOUND in wa_term_inventory (file_id=36)")
        continue

    ti = dict(ti)
    print(f"  id                  : {ti['id']}")
    print(f"  term_id             : {ti['term_id']}")
    print(f"  transliteration     : {ti['transliteration']}")
    print(f"  step_search_gloss   : {ti['step_search_gloss']}")
    print(f"  word_analysis_gloss : {ti['word_analysis_gloss']}")
    print(f"  occurrence_count    : {ti['occurrence_count']}")
    print(f"  testament           : {ti['testament']}")
    print(f"  delete_flagged      : {ti['delete_flagged']}")
    print(f"  meaning (truncated) : {str(ti.get('meaning') or '')[:120]}")
    print(f"  parsed_meaning_id   : {ti.get('parsed_meaning_id')}")
    print(f"  lsj_entry (trunc)   : {str(ti.get('lsj_entry') or '')[:80]}")

    # verse count
    vc = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_verse_records WHERE term_inv_id=? AND (delete_flagged=0 OR delete_flagged IS NULL)",
        (ti['id'],)
    ).fetchone()["c"]
    print(f"  active verse records: {vc}")

    # related words
    rw = conn.execute(
        "SELECT strongs_number, gloss FROM wa_term_related_words WHERE term_inv_id=? AND (delete_flagged=0 OR delete_flagged IS NULL)",
        (ti['id'],)
    ).fetchall()
    if rw:
        print(f"  related words ({len(rw)}): {', '.join(r['strongs_number'] or '?' for r in rw[:6])}")

    # root family
    rf = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_term_root_family WHERE term_inv_id=?",
        (ti['id'],)
    ).fetchone()["c"]
    print(f"  root_family rows    : {rf}")

    # mti_terms
    mti = conn.execute(
        "SELECT id, gloss, owning_registry, extraction_date FROM mti_terms WHERE strongs_number=?",
        (code,)
    ).fetchone()
    if mti:
        print(f"  mti_terms row       : id={mti['id']} gloss={mti['gloss']} owning={mti['owning_registry']}")
    else:
        print(f"  mti_terms row       : NONE")

    # cross_registry_links
    xl = conn.execute(
        "SELECT COUNT(*) AS c FROM wa_cross_registry_links WHERE file_id=36 AND connecting_term=?",
        (code,)
    ).fetchone()["c"]
    print(f"  cross_registry_links: {xl}")

    # wa_meaning_parsed
    mp = conn.execute(
        "SELECT id, parse_version FROM wa_meaning_parsed WHERE term_inv_id=?",
        (ti['id'],)
    ).fetchone()
    if mp:
        sc = conn.execute(
            "SELECT COUNT(*) AS c FROM wa_meaning_sense WHERE parsed_meaning_id=?", (mp['id'],)
        ).fetchone()["c"]
        print(f"  meaning_parsed id   : {mp['id']}  ({sc} senses)")
    else:
        print(f"  meaning_parsed      : NONE")

    # quality flags
    qf = conn.execute(
        "SELECT qft.flag_code, qft.flag_group "
        "FROM wa_data_quality_flags qf "
        "LEFT JOIN wa_quality_flag_types qft ON qft.id = qf.flag_id "
        "WHERE qf.file_id=36 AND qf.term_id=?",
        (ti['term_id'],)
    ).fetchall()
    if qf:
        flag_str = ", ".join(f"{r['flag_code']}({r['flag_group']})" for r in qf)
        print(f"  quality flags       : {flag_str}")
    else:
        print(f"  quality flags       : none")

print("\n\n--- Cross-registry reference check (are any other files using these terms?) ---")
for code in codes:
    other = conn.execute(
        "SELECT ti.file_id, fi.registry_id, wr.word FROM wa_term_inventory ti "
        "JOIN wa_file_index fi ON fi.id = ti.file_id "
        "LEFT JOIN word_registry wr ON wr.id = fi.word_registry_fk "
        "WHERE ti.strongs_number=? AND ti.file_id != 36",
        (code,)
    ).fetchall()
    if other:
        print(f"  {code} also appears in: {[(r['file_id'], r['registry_id'], r['word']) for r in other]}")
    else:
        print(f"  {code}: only appears in file_id=36 (soul)")
