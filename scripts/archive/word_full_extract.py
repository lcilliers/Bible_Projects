"""
word_full_extract.py
────────────────────
Export all database records related to a word.

Default (--flat): single mega-join query → one CSV with all columns.
                  Produces a wide, denormalised Cartesian-product result.
                  Row count = terms × related_words × root_family × verse_records
                              × quality_flags × cross_links × mti_terms
                              × meaning_senses × meaning_stems × …
                  This is intentional — the user wants one flat file.

--sections: one CSV per section (normalised, no Cartesian explosion).

Usage:
    python scripts/word_full_extract.py peace
    python scripts/word_full_extract.py love
    python scripts/word_full_extract.py 117            # registry ID
"""

import argparse
import csv
import os
import sys

# Allow running from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analytics.db_client import get_connection


# ── Full flat JOIN query ──────────────────────────────────────────────────────

FLAT_SQL = """
SELECT
    -- S2  word_registry (key identity + status fields)
    wr.id                       AS wr_id,
    wr.word                     AS wr_word,
    wr.phase1_status            AS wr_phase1_status,
    wr.automation_eligible      AS wr_automation_eligible,
    wr.strongs_list             AS wr_strongs_list,
    wr.phase1_term_count        AS wr_phase1_term_count,
    wr.phase1_verse_count       AS wr_phase1_verse_count,

    -- S3  wa_file_index (key identity + coverage fields)
    wfi.id                      AS wfi_id,
    wfi.filename                AS wfi_filename,
    wfi.part_number             AS wfi_part_number,
    wfi.phase                   AS wfi_phase,
    wfi.testament_coverage      AS wfi_testament_coverage,
    wfi.translation_used        AS wfi_translation_used,

    -- S4a  wa_term_inventory (key identity + core definition fields)
    wti.id                      AS wti_id,
    wti.term_id                 AS wti_term_id,
    wti.strongs_number          AS wti_strongs_number,
    wti.transliteration         AS wti_transliteration,
    wti.language                AS wti_language,
    wti.step_search_gloss       AS wti_step_search_gloss,
    wti.short_def_mounce        AS wti_short_def_mounce,
    wti.occurrence_count        AS wti_occurrence_count,
    wti.testament               AS wti_testament,
    wti.god_as_subject          AS wti_god_as_subject,
    wti.causative_form_present  AS wti_causative_form_present,

    -- S4b  wa_term_related_words (key identity + relationship)
    rw.id                       AS rw_id,
    rw.gloss                    AS rw_gloss,
    rw.strongs_number           AS rw_strongs_number,
    rw.relationship_note        AS rw_relationship_note,

    -- S4c  wa_term_root_family (key identity + root label)
    rf.id                       AS rf_id,
    rf.root_code                AS rf_root_code,
    rf.root_language            AS rf_root_language,
    rf.root_gloss               AS rf_root_gloss,

    -- S5  wa_term_phase2_flags + phase2_flag_types
    pft.flag_code               AS p2f_flag_code,
    pft.description             AS p2f_flag_description,

    -- S6  wa_data_quality_flags + wa_quality_flag_types
    dqf.id                      AS dqf_id,
    qft.flag_group              AS dqf_flag_group,
    qft.flag_code               AS dqf_flag_code,
    dqf.description             AS dqf_note,

    -- S7  wa_cross_registry_links + wa_crosslink_type
    crl.id                      AS crl_id,
    crl.linked_word             AS crl_linked_word,
    wr2.word                    AS crl_linked_word_resolved,
    ct.type_code                AS crl_connection_type_code,
    crl.connecting_term         AS crl_connecting_term,

    -- S8  wa_verse_records + books
    vr.id                       AS vr_id,
    vr.reference                AS vr_reference,
    b.name                      AS vr_book_name,
    vr.chapter                  AS vr_chapter,
    vr.verse_num                AS vr_verse_num,
    vr.testament                AS vr_testament,
    vr.translation              AS vr_translation,
    vr.target_word              AS vr_target_word,
    vr.span_strong_match        AS vr_span_strong_match,

    -- S9  mti_terms (key identity + status)
    mt.id                       AS mt_id,
    mt.strongs_number           AS mt_strongs_number,
    mt.transliteration          AS mt_transliteration,
    mt.gloss                    AS mt_gloss,
    mt.language                 AS mt_language,
    mt.status                   AS mt_status,
    mt.owning_part              AS mt_owning_part,

    -- S9b  mti_term_flags + phase2_flag_types (mti)
    pft_mt.flag_code            AS mtf_flag_code,

    -- S9c  mti_term_cross_refs (key identity + target)
    mcr.id                      AS mcr_id,
    mcr.word                    AS mcr_word,
    mcr.word_data_reference     AS mcr_word_data_reference,

    -- S11a  wa_meaning_parsed (summary counts)
    mp.id                       AS mp_id,
    mp.top_sense_count          AS mp_top_sense_count,
    mp.stem_count               AS mp_stem_count,
    mp.parse_version            AS mp_parse_version,
    mp.parse_warnings           AS mp_parse_warnings,

    -- S11b  wa_meaning_sense (key sense label + text)
    ms.id                       AS ms_id,
    ms.level_code               AS ms_level_code,
    ms.level_depth              AS ms_level_depth,
    ms.sense_text               AS ms_sense_text,
    ms.domain_tag               AS ms_domain_tag,

    -- S11c  wa_meaning_stem (stem label + top sense)
    mst.id                      AS mst_id,
    mst.stem_name               AS mst_stem_name,
    mst.stem_type               AS mst_stem_type,
    mst.top_sense_text          AS mst_top_sense_text,

    -- S11d  wa_lsj_parsed (gloss + domains only; raw text excluded)
    lsj.id                      AS lsj_id,
    lsj.lsj_gloss               AS lsj_gloss,
    lsj.lsj_domains             AS lsj_domains,
    lsj.parse_version           AS lsj_parse_version

FROM word_registry wr

-- S3
LEFT JOIN wa_file_index wfi
       ON wfi.word_registry_fk = wr.id

-- S4a
LEFT JOIN wa_term_inventory wti
       ON wti.file_id = wfi.id

-- S4b
LEFT JOIN wa_term_related_words rw
       ON rw.term_inv_id = wti.id

-- S4c
LEFT JOIN wa_term_root_family rf
       ON rf.term_inv_id = wti.id

-- S5
LEFT JOIN wa_term_phase2_flags p2f
       ON p2f.term_inv_id = wti.id
LEFT JOIN phase2_flag_types pft
       ON pft.id = p2f.flag_id

-- S6
LEFT JOIN wa_data_quality_flags dqf
       ON dqf.file_id = wfi.id
LEFT JOIN wa_quality_flag_types qft
       ON qft.id = dqf.flag_id

-- S7
LEFT JOIN wa_cross_registry_links crl
       ON crl.file_id = wfi.id
LEFT JOIN wa_crosslink_type ct
       ON ct.id = crl.connection_type_id
LEFT JOIN word_registry wr2
       ON wr2.id = crl.linked_registry_id

-- S8
LEFT JOIN wa_verse_records vr
       ON vr.term_inv_id = wti.id
LEFT JOIN books b
       ON b.id = vr.book_id

-- S9
LEFT JOIN mti_terms mt
       ON CAST(mt.owning_registry AS INTEGER) = wr.id
LEFT JOIN mti_term_flags mtf
       ON mtf.mti_term_id = mt.id
LEFT JOIN phase2_flag_types pft_mt
       ON pft_mt.id = mtf.flag_id
LEFT JOIN mti_term_cross_refs mcr
       ON mcr.mti_term_id = mt.id

-- S11
LEFT JOIN wa_meaning_parsed mp
       ON mp.term_inv_id = wti.id
LEFT JOIN wa_meaning_sense ms
       ON ms.parsed_meaning_id = mp.id
LEFT JOIN wa_meaning_stem mst
       ON mst.parsed_meaning_id = mp.id
LEFT JOIN wa_lsj_parsed lsj
       ON lsj.term_inv_id = wti.id

WHERE wr.id = ?
ORDER BY wfi.part_number, wti.term_id, b.book_order, vr.chapter, vr.verse_num
"""
Let me read both the review doc and check what the extract run actually produced.

Read audit_word_refactor_review.md, lines 1 to 150

The extract ran successfully (exit code 0). Now let me lay out what I'm seeing across both issues so we can make a clear decision.

What the review doc tells us
From your Section 1 & 2 responses — confirmed design gaps
1. No soft-delete on any table.
Every table is insert/update only. Your requirement: flag for deletion, physical delete as a separate archive operation. This is a schema change — new column (e.g. deleted_at or delete_flag) needed on all content tables. That has to land in create_tables.sql and a new migration.

2. A2–A6 needs a complete redesign — and you've asked for a debate.
Your core objection: the current design reads the DB first, calls STEP, then compares. You want it inverted:

STEP first, all calls complete, results held in memory
Then compare everything against DB tables in one pass
Then apply INSERT / UPDATE / SET DELETE FLAG in a single atomic transaction
This is a fundamentally different architecture — not a patch on the current code.
3. Meaning field migration (~33 records).
Those 33 terms have meaning data sitting in wti.meaning / wti.meaning_numbered instead of the wa_meaning_* tables. Before audit_word can re-parse meaning cleanly, those need to be migrated. This is a one-off data migration task, separable from the design debate.

4. A10 is incomplete — strongs_list and word-level notes/anomalies not being written.

What the word_full_extract test revealed
Two problems surfaced immediately:

wa_term_phase2_flags and mti_term_flags are pure junction tables with no id column — any code that assumes a surrogate key on flags will break
The Cartesian product from the flat join is large — relationship integrity questions (do all terms have verses? do all mti_terms link correctly?) are hidden in the noise. Love had data, but we don't yet know what's missing or duplicated




# ── Helpers ───────────────────────────────────────────────────────────────────

def resolve_registry_id(conn, word: str | None, registry_id: int | None) -> tuple[int, str]:
    if registry_id is not None:
        row = conn.execute(
            "SELECT id, word FROM word_registry WHERE id = ?", (registry_id,)
        ).fetchone()
        if not row:
            raise SystemExit(f"No word_registry row with id={registry_id}")
        return row[0], row[1]
    row = conn.execute(
        "SELECT id, word FROM word_registry WHERE LOWER(word) = LOWER(?)", (word,)
    ).fetchone()
    if not row:
        raise SystemExit(f"No word_registry row with word='{word}'")
    return row[0], row[1]


# ── Main ──────────────────────────────────────────────────────────────────────

def run(word: str | None, registry_id: int | None, output_dir: str) -> None:
    conn = get_connection()
    rid, rword = resolve_registry_id(conn, word, registry_id)

    safe_word = (rword.replace(" ", "_").replace("/", "_")
                 .replace("(", "").replace(")", ""))
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, f"{safe_word}_full_extract.csv")

    print(f"\nWord extract: [{rid}] {rword}")
    print(f"Running full flat join query across all sections …")

    cur = conn.execute(FLAT_SQL.strip(), (rid,))
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()

    print(f"Rows returned  : {len(rows):,}")
    print(f"Columns        : {len(cols)}")
    print(f"Writing CSV    : {csv_path}")

    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(cols)
        writer.writerows(rows)

    conn.close()
    print(f"Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Full word extract — single flat JOIN across all sections → CSV"
    )
    parser.add_argument(
        "word",
        type=str,
        help="Word label (e.g. 'peace') or numeric registry ID (e.g. '117')"
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             "outputs", "word_reports"),
        help="Base output directory (default: outputs/word_reports/)"
    )
    args = parser.parse_args()
    # Accept either a numeric registry ID or a word label
    if args.word.isdigit():
        run(None, int(args.word), args.output_dir)
    else:
        run(args.word, None, args.output_dir)
