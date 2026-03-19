"""
_build_tables_4_6.py
Appends tables 4-6 to field-data-flow-mapping.json.
Based on verified source code reading of:
  engine/new_word.py (N11, N12, N14, N18)
  engine/gap_fill.py (S2 Phase C, S3, S4)
  engine/audit_word.py (A3a, A4, A5)
"""
import json, pathlib

def nw():
    return [{"stage": "—", "operation": "NOT_WRITTEN", "condition": "—", "value": "—"}]

tables = [

# ════════════════════════════════════════════════════════════════════════════
# TABLE 4 — wa_term_inventory
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "wa_term_inventory",
  "part": "Part 2 — Core Word Data Tables",
  "description": "One row per Strong's number per word. Holds all per-term metadata: glosses, meaning, occurrence counts, testament coverage, parsed meaning FK. Written at N11 (NEW_WORD) and S2 Phase C (GAP_FILL). Refreshed non-destructively at A4 (AUDIT_WORD).",
  "spec_sections": ["§7.2 N11", "§9 Field-Level Mapping", "§4 M03", "§4 M04"],
  "modes_that_write": ["NEW_WORD", "GAP_FILL", "AUDIT_WORD"],
  "table_spec_rules": [
    "§7.2 N11: INSERT per NEW term inside atomic transaction N9–N15. id=MAX(id)+1 queried live.",
    "§9: god_as_subject=0, somatic_link=0 — DEFERRED. Next-phase judgment fields.",
    "§9: also_spelled and occurrence_count_qualifier — DEFERRED-INTERACTIVE. Filled at field-fill N18/A8/S8. null until researcher provides value or confirms null.",
    "§9: testament — derived from confirmed verse records after verse insert (span_strong_match=1). Derived per term at N14. GAP_FILL and AUDIT_WORD do not re-derive this field after verse changes.",
    "§4 M04: short_def_mounce and parsed_meaning_id are new columns added in migration M04.",
    "AUDIT_WORD A4: non-destructive COALESCE update — fills only null/empty fields. Never overwrites existing values.",
    "GAP_FILL S4: meaning gap-fill — fills meaning, meaning_numbered, step_search_gloss, word_analysis_gloss, lsj_entry if null. Also fills via COALESCE.",
    "WR-11: transliteration must be non-null — STOP condition.",
    "WR-12: language must be 'Hebrew' or 'Greek' — STOP condition."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§7.2 N11 · §4 M03",
      "spec_rule": "Sequential integer. Must query MAX(id) live before insert.",
      "data_source": "engine/db.py get_max_id(conn, 'wa_term_inventory') → SELECT MAX(id) FROM wa_term_inventory → result + 1",
      "py_file": "engine/db.py · engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of atomic transaction N9–N15; one row per NEW term", "value": "get_max_id(conn, 'wa_term_inventory') + 1"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "One row per NEW term; idempotent within transaction", "value": "get_max_id(conn, 'wa_term_inventory') + 1"}],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "Refreshes existing rows; never INSERTs new rows (new terms are handled at A6 gap-fill)", "value": "COALESCE update — no new id assigned"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "file_id",
      "spec_section": "§7.2 N11",
      "spec_rule": "FK to wa_file_index.id. Links this term row to the file anchor for this word.",
      "data_source": "wa_file_index.id assigned at N9/S2 Phase A",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction; file_id from N9", "value": "file_id (wa_file_index.id from N9)"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "file_id from Phase A", "value": "file_id (wa_file_index.id from Phase A)"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "language",
      "spec_section": "§9 · §7.2 N12 WR-12",
      "spec_rule": "H-prefix Strong's → 'Hebrew'; G-prefix → 'Greek'. WR-12 STOP if not one of these two values.",
      "data_source": "vocab.get('language', 'Hebrew') from STEP API",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('language', 'Hebrew')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('language', 'Hebrew')"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "term_id",
      "spec_section": "§9",
      "spec_rule": "STEP internal code — stores resolved Strong's number. Same as strongs_number at write time.",
      "data_source": "vocab['strong_number'] (resolved form)",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "resolved (vocab['strong_number'])"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "resolved (vocab['strong_number'])"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "strongs_number",
      "spec_section": "§9",
      "spec_rule": "Canonical resolved Strong's number. H2428 → H2428A. Same as term_id at write time.",
      "data_source": "vocab['strong_number'] (resolved form)",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "resolved (vocab['strong_number'])"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "resolved (vocab['strong_number'])"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "transliteration",
      "spec_section": "§9 · §8.1 WR-11",
      "spec_rule": "Required — WR-11 STOP if null. From STEP vocab API.",
      "data_source": "vocab.get('transliteration', '') from STEP API",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('transliteration', '')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('transliteration', '')"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "step_search_gloss",
      "spec_section": "§9",
      "spec_rule": "English gloss label from STEP search heading (vocabInfos[0].stepGloss). COALESCE-filled in S4 and A4 — never overwrites existing non-empty value.",
      "data_source": "vocab.get('gloss', '') from STEP API",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('gloss', '')"}],
        "GAP_FILL":   [
          {"stage": "S2 Phase C", "operation": "INSERT",  "condition": "Part of transaction", "value": "vocab.get('gloss', '')"},
          {"stage": "S4",         "operation": "UPDATE",  "condition": "COALESCE(step_search_gloss, ?) — fills only if null", "value": "UPDATE wa_term_inventory SET step_search_gloss=COALESCE(step_search_gloss,?) WHERE id=?"}
        ],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "COALESCE(NULLIF(step_search_gloss,''),?) — fills only if null or empty string", "value": "UPDATE wa_term_inventory SET step_search_gloss=COALESCE(NULLIF(step_search_gloss,''),?) WHERE id=?"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "word_analysis_gloss",
      "spec_section": "§9",
      "spec_rule": "Gloss from STEP word analysis block. Same as step_search_gloss at write time. Researcher may update in review. COALESCE-filled in S4 and A4.",
      "data_source": "vocab.get('gloss', '') from STEP API",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('gloss', '')"}],
        "GAP_FILL":   [
          {"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('gloss', '')"},
          {"stage": "S4",         "operation": "UPDATE", "condition": "COALESCE fill if null", "value": "UPDATE wa_term_inventory SET word_analysis_gloss=COALESCE(word_analysis_gloss,?) WHERE id=?"}
        ],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "COALESCE fill if null/empty", "value": "UPDATE wa_term_inventory SET word_analysis_gloss=COALESCE(NULLIF(word_analysis_gloss,''),?) WHERE id=?"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "occurrence_count",
      "spec_section": "§9",
      "spec_rule": "Token occurrence count from STEP API. Null if API does not return it — triggers DATA_GAP quality flag. COALESCE-filled by AUDIT_WORD A4.",
      "data_source": "vocab.get('occurrence_count') from STEP API — may be null",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction; null if API returns no value", "value": "vocab.get('occurrence_count')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('occurrence_count')"}],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "COALESCE(occurrence_count, ?) — fills only if currently null", "value": "UPDATE wa_term_inventory SET occurrence_count=COALESCE(occurrence_count,?) WHERE id=?"}]
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "occurrence_count_qualifier",
      "spec_section": "§9",
      "spec_rule": "DEFERRED-INTERACTIVE. 'about', 'exactly', etc. Not available from API. Filled at field-fill N18/A8/S8 with researcher input or confirmed null. Only NEW_WORD N18 implements the interactive field-fill; GAP_FILL has no S8 equivalent in code; AUDIT_WORD A8 in code writes SPAN_BACK_POPULATED flag (not field-fill).",
      "data_source": "Researcher input at N18 field-fill — not from API",
      "py_file": "engine/new_word.py (_run_field_fill)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N18", "operation": "UPDATE", "condition": "Interactive: presented only if null; researcher types value or presses Enter to confirm null", "value": "UPDATE wa_term_inventory SET occurrence_count_qualifier=? WHERE id=?"}],
        "GAP_FILL":   [{"stage": "—", "operation": "NOT_WRITTEN", "condition": "GAP_FILL has no S8 field-fill stream implemented; field remains null for words processed by BULK_GAP_FILL without a subsequent NEW_WORD run", "value": "—"}],
        "AUDIT_WORD": [{"stage": "A8", "operation": "NOT_WRITTEN", "condition": "A8 in code writes SPAN_BACK_POPULATED quality flag — not field-fill; occurrence_count_qualifier not updated by AUDIT_WORD", "value": "—"}]
      },
      "optional": True,
      "spec_match": "⚠ Partial — only NEW_WORD N18 implements the interactive field-fill; GAP_FILL has no S8 equivalent in code; AUDIT_WORD A8 writes SPAN_BACK_POPULATED flag instead of field-fill; words processed only through GAP_FILL will have occurrence_count_qualifier=null indefinitely"
    },
    {
      "field": "meaning",
      "spec_section": "§9",
      "spec_rule": "Full meaning block from STEP vocab.medium_def. HTML-stripped; newlines preserved. Null if API returns none — triggers NO_WORD_ANALYSIS flag. Gap-filled in S4; refreshed in A4.",
      "data_source": "vocab.get('medium_def') from STEP API",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('medium_def')"}],
        "GAP_FILL":   [
          {"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('medium_def')"},
          {"stage": "S4",         "operation": "UPDATE", "condition": "Fills if meaning IS NULL or empty", "value": "UPDATE wa_term_inventory SET meaning=?,meaning_numbered=? WHERE id=?"}
        ],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "COALESCE(NULLIF(meaning,''),?) — non-destructive", "value": "UPDATE wa_term_inventory SET meaning=COALESCE(NULLIF(meaning,''),?) WHERE id=?"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "meaning_numbered",
      "spec_section": "§9",
      "spec_rule": "Same content as meaning at write time. Mirrors meaning text. Researcher-distinguishable numbered form for future structured parsing. Gap-filled and refreshed same as meaning.",
      "data_source": "vocab.get('medium_def') — same value as meaning at write",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction; mirrors meaning", "value": "vocab.get('medium_def')"}],
        "GAP_FILL":   [
          {"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('medium_def')"},
          {"stage": "S4",         "operation": "UPDATE", "condition": "Updated alongside meaning", "value": "UPDATE wa_term_inventory SET meaning_numbered=? WHERE id=?"}
        ],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "COALESCE fill if null/empty", "value": "UPDATE wa_term_inventory SET meaning_numbered=COALESCE(NULLIF(meaning_numbered,''),?) WHERE id=?"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "also_spelled",
      "spec_section": "§9",
      "spec_rule": "DEFERRED-INTERACTIVE. Hebrew only. Alternate spelling / Strong's variant (JSON). Filled at field-fill N18/A8/S8. null until researcher provides value or confirms null. Same gap as occurrence_count_qualifier — only NEW_WORD N18 implements field-fill.",
      "data_source": "Researcher input at N18 field-fill — Hebrew terms only; not from API",
      "py_file": "engine/new_word.py (_run_field_fill)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N18", "operation": "UPDATE", "condition": "Hebrew terms only; presented if null; researcher types value or confirms null", "value": "UPDATE wa_term_inventory SET also_spelled=? WHERE id=?"}],
        "GAP_FILL":   [{"stage": "—", "operation": "NOT_WRITTEN", "condition": "No S8 field-fill in GAP_FILL code", "value": "—"}],
        "AUDIT_WORD": [{"stage": "—", "operation": "NOT_WRITTEN", "condition": "A8 in code writes quality flag, not field-fill", "value": "—"}]
      },
      "optional": True,
      "spec_match": "⚠ Partial — only NEW_WORD N18 implements the field-fill; GAP_FILL and AUDIT_WORD do not prompt for also_spelled; Hebrew words processed only through GAP_FILL will have also_spelled=null indefinitely"
    },
    {
      "field": "lsj_entry",
      "spec_section": "§9",
      "spec_rule": "Greek only. Full LSJ lexicon text from STEP vocab API. Null for Hebrew. COALESCE-filled by S4 and A4.",
      "data_source": "vocab.get('lsj_entry') from STEP API — null for Hebrew",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction; null for Hebrew", "value": "vocab.get('lsj_entry') or None"}],
        "GAP_FILL":   [
          {"stage": "S2 Phase C", "operation": "INSERT", "condition": "null for Hebrew", "value": "vocab.get('lsj_entry') or None"},
          {"stage": "S4",         "operation": "UPDATE", "condition": "COALESCE fill if null", "value": "UPDATE wa_term_inventory SET lsj_entry=COALESCE(lsj_entry,?) WHERE id=?"}
        ],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "COALESCE(NULLIF(lsj_entry,''),?) — Greek only; null for Hebrew", "value": "UPDATE wa_term_inventory SET lsj_entry=COALESCE(NULLIF(lsj_entry,''),?) WHERE id=?"}]
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "short_def_mounce",
      "spec_section": "§9 · §4 M04",
      "spec_rule": "Greek only. Mounce short definition. New column added in M04. Null for Hebrew. COALESCE-filled by A4.",
      "data_source": "vocab.get('short_def_mounce') from STEP API — null for Hebrew",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction; null for Hebrew", "value": "vocab.get('short_def_mounce') or None"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "null for Hebrew", "value": "vocab.get('short_def_mounce') or None"}],
        "AUDIT_WORD": [{"stage": "A4", "operation": "UPDATE", "condition": "COALESCE(NULLIF(short_def_mounce,''),?) — Greek only", "value": "UPDATE wa_term_inventory SET short_def_mounce=COALESCE(NULLIF(short_def_mounce,''),?) WHERE id=?"}]
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "testament",
      "spec_section": "§9",
      "spec_rule": "OT/NT/both derived per term from confirmed verse records (span_strong_match=1). Derived at NEW_WORD N14 post-transaction. GAP_FILL inserts verses at S3 but has no per-term testament derivation step. AUDIT_WORD A9 updates wa_file_index.testament_coverage only — not wa_term_inventory.testament.",
      "data_source": "SELECT DISTINCT testament FROM wa_verse_records WHERE term_inv_id=? AND span_strong_match=1",
      "py_file": "engine/new_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [
          {"stage": "N11", "operation": "INSERT",  "condition": "Part of transaction", "value": "NULL — placeholder; derived post-transaction at N14"},
          {"stage": "N14", "operation": "UPDATE",  "condition": "After verse records committed", "value": "SELECT DISTINCT testament FROM wa_verse_records WHERE term_inv_id=? AND span_strong_match=1 → OT/NT/both → UPDATE wa_term_inventory SET testament=? WHERE id=?"}
        ],
        "GAP_FILL":   [
          {"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "NULL — placeholder"},
          {"stage": "—",          "operation": "NOT_WRITTEN", "condition": "S3 inserts verse records but no step derives per-term testament for wa_term_inventory in GAP_FILL", "value": "— GAP: field remains NULL after GAP_FILL verse insert (S3)"}
        ],
        "AUDIT_WORD": [
          {"stage": "A9", "operation": "NOT_WRITTEN", "condition": "A9 updates wa_file_index.testament_coverage only; wa_term_inventory.testament is not updated", "value": "— GAP: per-term testament not re-derived after A3a verse sync"}
        ]
      },
      "optional": False,
      "spec_match": "⚠ Partial — only NEW_WORD N14 derives per-term testament from confirmed verse records; GAP_FILL (S3) and AUDIT_WORD (A3a/A9) do not update wa_term_inventory.testament after verse changes"
    },
    {
      "field": "god_as_subject",
      "spec_section": "§9",
      "spec_rule": "DEFERRED. Default 0 (schema DEFAULT). Next-phase judgment — whether the term is applied to God or Holy Spirit. Never set by engine; researcher assigns in next phase.",
      "data_source": "Schema DEFAULT 0 — not written by engine INSERT column list",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Not in INSERT column list; schema DEFAULT 0 applies", "value": "0 — schema default"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Not in column list; schema DEFAULT 0", "value": "0 — schema default"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "somatic_link",
      "spec_section": "§9",
      "spec_rule": "DEFERRED. Default 0 (schema DEFAULT). Inner state linked to bodily expression — next-phase judgment. Never set by engine.",
      "data_source": "Schema DEFAULT 0 — not written by engine INSERT column list",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Not in INSERT column list; schema DEFAULT 0 applies", "value": "0 — schema default"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Schema DEFAULT 0", "value": "0 — schema default"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "causative_form_present",
      "spec_section": "§9",
      "spec_rule": "1 if medium_def contains Hiphil or Piel (Hebrew) or causative sense. Derived at INSERT from vocab API response.",
      "data_source": "1 if vocab.get('causative_form_present') else 0",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "1 if vocab.get('causative_form_present') else 0"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "1 if vocab.get('causative_form_present') else 0"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "status_note",
      "spec_section": "§9",
      "spec_rule": "step_client warnings for this term. Null if no warnings. Populated at INSERT from any errors accumulated during pre-transaction fetch.",
      "data_source": "'; '.join(errors[-3:]) if errors else None",
      "py_file": "engine/new_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction; null if no errors", "value": "'; '.join(errors[-3:]) if errors else None"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Always NULL in GAP_FILL Phase C", "value": "NULL — hardcoded in GAP_FILL INSERT"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "parsed_meaning_id",
      "spec_section": "§9 · §4 M04 · §7.2 N15",
      "spec_rule": "FK to wa_meaning_parsed.id. Null until meaning parser runs. Set by run_parser_for_file() at N15 (NEW_WORD), S4 (GAP_FILL), A5 (AUDIT_WORD).",
      "data_source": "engine/meaning_parser.py run_parser_for_file() → INSERT wa_meaning_parsed → UPDATE wa_term_inventory SET parsed_meaning_id=?",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py · engine/meaning_parser.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [
          {"stage": "N11", "operation": "INSERT",  "condition": "Part of transaction", "value": "NULL — not yet set"},
          {"stage": "N15", "operation": "UPDATE",  "condition": "After meaning parser runs", "value": "run_parser_for_file() → UPDATE wa_term_inventory SET parsed_meaning_id=wa_meaning_parsed.id WHERE id=?"}
        ],
        "GAP_FILL":   [
          {"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "NULL — not yet set"},
          {"stage": "S4",         "operation": "UPDATE", "condition": "run_parser_for_file() called after meaning gap-fill", "value": "run_parser_for_file() → UPDATE wa_term_inventory SET parsed_meaning_id=?"}
        ],
        "AUDIT_WORD": [{"stage": "A5", "operation": "UPDATE", "condition": "Always — re-parses all terms", "value": "run_parser_for_file() → UPDATE wa_term_inventory SET parsed_meaning_id=?"}]
      },
      "optional": True,
      "spec_match": "✓ Match"
    }
  ]
},

# ════════════════════════════════════════════════════════════════════════════
# TABLE 5 — wa_term_related_words
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "wa_term_related_words",
  "part": "Part 2 — Core Word Data Tables",
  "description": "Related words cluster for each term from the STEP word analysis block. One row per related word per term. Written at N11 (NEW_WORD) and S2 Phase C (GAP_FILL). AUDIT_WORD does not refresh or add related words — if the STEP API returns new related words in a re-fetch, they are not captured.",
  "spec_sections": ["§7.2 N11", "§9"],
  "modes_that_write": ["NEW_WORD", "GAP_FILL"],
  "table_spec_rules": [
    "§7.2 N11: INSERT per related word per NEW term inside atomic transaction N9–N15.",
    "Related words are written inside the same transaction as wa_term_inventory (Phase C in GAP_FILL).",
    "AUDIT_WORD A4 re-fetches vocab and does COALESCE UPDATEs on wa_term_inventory but does not INSERT new wa_term_related_words rows. If the STEP API returns new related words, they are silently dropped.",
    "relationship_note column exists in schema but is not written by any engine mode — researcher annotation field."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§7.2 N11 · §4 M03",
      "spec_rule": "Sequential integer. AUTOINCREMENT in schema — no explicit MAX query required.",
      "data_source": "SQLite AUTOINCREMENT — engine does not explicitly set id for related_words rows",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "One row per related word per NEW term", "value": "AUTOINCREMENT — not explicitly set in INSERT"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "One row per related word per NEW term", "value": "AUTOINCREMENT"}],
        "AUDIT_WORD": [{"stage": "—", "operation": "NOT_WRITTEN", "condition": "A4 re-fetches vocab but does not INSERT new related_words rows; new related words from STEP API are not captured", "value": "— GAP: AUDIT_WORD silently drops new related words from re-fetch"}]
      },
      "optional": False,
      "spec_match": "⚠ Partial — AUDIT_WORD does not INSERT new related word rows even when re-fetching vocab at A4; related words added to STEP API after the initial write are never captured"
    },
    {
      "field": "term_inv_id",
      "spec_section": "§7.2 N11",
      "spec_rule": "FK to wa_term_inventory.id. Links related word row to its owning term.",
      "data_source": "ti_id — wa_term_inventory.id from concurrent N11/S2-Phase-C INSERT",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Part of transaction", "value": "ti_id (wa_term_inventory.id from N11)"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Part of transaction", "value": "ti_id (wa_term_inventory.id from Phase C)"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "gloss",
      "spec_section": "§9",
      "spec_rule": "English gloss for the related word, from STEP vocab related_words array.",
      "data_source": "rw.get('gloss') from vocab['related_words'][i]",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Per related word", "value": "rw.get('gloss')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Per related word", "value": "rw.get('gloss')"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "transliteration",
      "spec_section": "§9",
      "spec_rule": "Transliteration of the related word. From STEP vocab related_words array.",
      "data_source": "rw.get('translit') from vocab['related_words'][i]",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Per related word", "value": "rw.get('translit')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Per related word", "value": "rw.get('translit')"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "strongs_number",
      "spec_section": "§9",
      "spec_rule": "Strong's number of the related word. From STEP vocab related_words array.",
      "data_source": "rw.get('strong') from vocab['related_words'][i]",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N11", "operation": "INSERT", "condition": "Per related word", "value": "rw.get('strong')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Per related word", "value": "rw.get('strong')"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "relationship_note",
      "spec_section": "— Not in spec §9 field mapping",
      "spec_rule": "Schema column for researcher annotation of how related words relate to the term. Never written by any engine mode. Researcher-only field.",
      "data_source": "NOT_WRITTEN — researcher annotation",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "— Not specified"
    }
  ]
},

# ════════════════════════════════════════════════════════════════════════════
# TABLE 6 — wa_verse_records
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "wa_verse_records",
  "part": "Part 2 — Core Word Data Tables",
  "description": "Core research table. One row per confirmed term occurrence in a verse (span_strong_match=1 at write time). All v9 engine modes write or modify this table. NEW_WORD N12 and GAP_FILL S3 INSERT span-confirmed rows only. AUDIT_WORD A3a INSERTs missing rows, UPDATEs existing rows with latest STEP data, and marks orphan rows (span_strong_match=-1) for verses in DB but absent from current STEP API response.",
  "spec_sections": ["§7.2 N12", "§5.2 Span Filter", "§5.5 AUDIT A3a", "§9", "§4 M05"],
  "modes_that_write": ["NEW_WORD", "GAP_FILL", "AUDIT_WORD"],
  "table_spec_rules": [
    "§5.2: Span filter — only verses where queried Strong's appears in the strong= attribute of the target-word span are stored. span_strong_match=1 at write time for all v9 INSERTs.",
    "§5.5 A3a: AUDIT_WORD verse sync — INSERT missing (in STEP not in DB), UPDATE existing (overwrite span fields), mark orphans span_strong_match=-1 (in DB not in STEP). -1 is a code extension not in the spec's defined value set (spec: 1/0/NULL only).",
    "§4 M05: target_word, span_strong_match, context_before, context_after added in migration M05.",
    "§5.6: context_before, context_after, note, claude_output — Phase 2 reserved. Always NULL in Phase 1. Not written by v9 engine.",
    "§9: translation hardcoded 'ESV' in all INSERT statements.",
    "§9: book_id derived from book_code via book_code_variants lookup — WR error if not found."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§7.2 N12 · §4 M03",
      "spec_rule": "Sequential integer. Must query MAX(id) live before insert.",
      "data_source": "engine/db.py get_max_id(conn, 'wa_verse_records') → SELECT MAX(id) → result + 1",
      "py_file": "engine/db.py · engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12", "operation": "INSERT", "condition": "One row per span-confirmed verse per term", "value": "get_max_id(conn, 'wa_verse_records') + 1"}],
        "GAP_FILL":   [{"stage": "S3",  "operation": "INSERT", "condition": "Terms with zero verse records; span-confirmed only", "value": "get_max_id(conn, 'wa_verse_records') + 1"}],
        "AUDIT_WORD": [{"stage": "A3a", "operation": "INSERT", "condition": "Verses in STEP response but absent from DB", "value": "get_max_id(conn, 'wa_verse_records') + 1"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "file_id",
      "spec_section": "§7.2 N12",
      "spec_rule": "FK to wa_file_index.id.",
      "data_source": "file_id from wa_file_index INSERT at N9/S2 Phase A",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "file_id from N9"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Part of S3 loop", "value": "ti_row['file_id']"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "fid (from file_ids loop)"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "term_inv_id",
      "spec_section": "§7.2 N12",
      "spec_rule": "FK to wa_term_inventory.id.",
      "data_source": "ti_id from wa_term_inventory INSERT at N11/S2 Phase C",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "ti_id from term_inv_ids[strongs]"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Part of S3 loop", "value": "ti_id from gap row"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "ti_id from term_rows loop"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "term_id",
      "spec_section": "§9",
      "spec_rule": "Strong's / STEP code for the term this verse belongs to.",
      "data_source": "strongs variable (resolved Strong's number)",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "strongs (vocab key)"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Part of S3 loop", "value": "strongs from gap row"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "strongs (ti['strongs_number'] or ti['term_id'])"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "transliteration",
      "spec_section": "§9",
      "spec_rule": "Transliteration of the term. From vocab at write time.",
      "data_source": "vocab_map.get(strongs, {}).get('transliteration', '')",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "vocab_map.get(strongs, {}).get('transliteration', '')"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Part of S3 loop", "value": "ti_row['transliteration'] or ''"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "ti['transliteration'] or ''"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "book_id",
      "spec_section": "§9",
      "spec_rule": "FK to books.id. Derived from book_code via SELECT book_id FROM book_code_variants WHERE code=?. STOP if not found.",
      "data_source": "engine/db.py get_book_id(conn, rec['book_code']) → SELECT book_id FROM book_code_variants WHERE code=?",
      "py_file": "engine/db.py · engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "None → error logged; row skipped", "value": "get_book_id(conn, rec['book_code'])"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "None → error logged; row skipped", "value": "get_book_id(conn, rec['book_code'])"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "None → book_misses list; row skipped", "value": "get_book_id(conn, rec['book_code'])"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "reference",
      "spec_section": "§9",
      "spec_rule": "STEP verse reference string as returned, e.g. 'Gen 31:27'.",
      "data_source": "rec['ref'] from STEP masterSearch response",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "rec['ref']"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "S3 loop", "value": "rec['ref']"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "rec['ref'] — used as match key for INSERT vs UPDATE decision"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "chapter",
      "spec_section": "§9",
      "spec_rule": "Integer chapter number. Single-chapter books always 1. Parsed from STEP verse record.",
      "data_source": "rec['chapter'] from STEP masterSearch response",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "rec['chapter']"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "S3 loop", "value": "rec['chapter']"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "rec['chapter']"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "verse_num",
      "spec_section": "§9",
      "spec_rule": "Integer verse number. Parsed from STEP verse record.",
      "data_source": "rec['verse_num'] from STEP masterSearch response",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "rec['verse_num']"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "S3 loop", "value": "rec['verse_num']"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "rec['verse_num']"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "testament",
      "spec_section": "§9",
      "spec_rule": "'OT' or 'NT' — derived from book_code vs NT_BOOKS list in step_client.",
      "data_source": "rec['testament'] from STEP verse record (derived by step_client)",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py · analytics/step_client.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "rec['testament']"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "S3 loop", "value": "rec['testament']"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "rec['testament']"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "translation",
      "spec_section": "§9",
      "spec_rule": "Hardcoded 'ESV' for all v9 engine runs.",
      "data_source": "hardcoded: 'ESV' in all INSERT statements",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Always", "value": "'ESV' — hardcoded"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Always", "value": "'ESV' — hardcoded"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT", "value": "'ESV' — hardcoded"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "verse_text",
      "spec_section": "§9",
      "spec_rule": "HTML-stripped ESV verse text from STEP masterSearch preview.",
      "data_source": "rec['esv_text'] from STEP masterSearch; HTML-stripped by step_client",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py · analytics/step_client.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "rec['esv_text']"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "S3 loop", "value": "rec['esv_text']"}],
        "AUDIT_WORD": [
          {"stage": "A3a", "operation": "INSERT", "condition": "Missing verse INSERT", "value": "rec['esv_text']"},
          {"stage": "A3a", "operation": "UPDATE",  "condition": "Existing verse: always overwritten with latest STEP text", "value": "UPDATE wa_verse_records SET verse_text=? WHERE id=?"}
        ]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "target_word",
      "spec_section": "§9 · §5.2 · §4 M05",
      "spec_rule": "English rendering of target Strong's from span text. Null if span extraction fails. Set at INSERT for all v9 writes. AUDIT_WORD A3a also UPDATEs if new value available from re-fetch.",
      "data_source": "rec.get('target_word', '') — extracted by span_filter.py from strong= attribute span text",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py · engine/span_filter.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Part of transaction", "value": "rec.get('target_word', '')"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "S3 loop", "value": "rec.get('target_word', '')"}],
        "AUDIT_WORD": [
          {"stage": "A3a", "operation": "INSERT", "condition": "Missing verse INSERT", "value": "rec.get('target_word', '')"},
          {"stage": "A3a", "operation": "UPDATE",  "condition": "Existing verse: if rec.get('target_word') is truthy", "value": "UPDATE wa_verse_records SET target_word=? WHERE id=?"}
        ]
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "span_strong_match",
      "spec_section": "§5.2 · §5.5 · §9 · §4 M05",
      "spec_rule": "1 = queried Strong's confirmed in span. 0 = only sibling/prefix form (AUDIT back-pop). NULL = pre-v9 not yet assessed. Code also uses -1 for orphan rows (in DB but not in current STEP API response) — this value is not in the spec's defined set.",
      "data_source": "rec.get('span_strong_match', 1) at INSERT; span_filter.py derived; AUDIT A3a: 1 or -1 on UPDATE",
      "py_file": "engine/span_filter.py · engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Span-confirmed rows only — all inserted rows have span_strong_match=1", "value": "rec.get('span_strong_match', 1) — always 1 for v9 INSERTs"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Span-confirmed rows only", "value": "rec.get('span_strong_match', 1) — always 1 for S3 INSERTs"}],
        "AUDIT_WORD": [
          {"stage": "A3a", "operation": "INSERT", "condition": "Missing verse INSERT", "value": "rec.get('span_strong_match', 1) — 1 for confirmed"},
          {"stage": "A3a", "operation": "UPDATE",  "condition": "Existing verse: always overwritten", "value": "span_strong_match = rec.get('span_strong_match', 1)"},
          {"stage": "A3a", "operation": "UPDATE",  "condition": "Orphan: verse in DB but absent from STEP API response", "value": "UPDATE wa_verse_records SET span_strong_match=-1 WHERE id=?  — NOTE: -1 is code-only; spec defines 1/0/NULL"}
        ]
      },
      "optional": False,
      "spec_match": "⚠ Partial — INSERT correctly sets span_strong_match=1 per spec §5.2; AUDIT_WORD A3a uses span_strong_match=-1 for orphan rows (verses in DB but absent from STEP response); spec §5.2/§5.5 only defines 1 (confirmed), 0 (sibling/back-pop), NULL (pre-v9 unassessed); -1 is a code extension"
    },
    {
      "field": "context_before",
      "spec_section": "§5.6 · §4 M05",
      "spec_rule": "Phase 2 reserved. Always NULL in Phase 1. AUDIT_WORD A3a may UPDATE if STEP API returns a value (conditional write), but STEP never returns this — effectively always NULL.",
      "data_source": "NULL — Phase 2 reserved. Not written in Phase 1.",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Always", "value": "NULL — Phase 2 reserved; hardcoded in INSERT"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Always", "value": "NULL — Phase 2 reserved; hardcoded in INSERT"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "Missing verse INSERT: NULL; UPDATE: conditional on rec.get('context_before') is not None — never triggered in Phase 1", "value": "NULL for Phase 1 — STEP API does not return context_before"}]
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "context_after",
      "spec_section": "§5.6 · §4 M05",
      "spec_rule": "Phase 2 reserved. Always NULL in Phase 1. Same logic as context_before.",
      "data_source": "NULL — Phase 2 reserved. Not written in Phase 1.",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N12",  "operation": "INSERT", "condition": "Always", "value": "NULL — Phase 2 reserved"}],
        "GAP_FILL":   [{"stage": "S3",   "operation": "INSERT", "condition": "Always", "value": "NULL — Phase 2 reserved"}],
        "AUDIT_WORD": [{"stage": "A3a",  "operation": "INSERT", "condition": "NULL; conditional UPDATE never triggered in Phase 1", "value": "NULL for Phase 1"}]
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "note",
      "spec_section": "§5.6",
      "spec_rule": "Phase 2 reserved. Researcher annotation at verse level. Never written by v9 engine. NULL for all Phase 1 records.",
      "data_source": "NOT_WRITTEN — Phase 2 reserved, researcher annotation",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "claude_output",
      "spec_section": "§5.6",
      "spec_rule": "Phase 2 reserved. AI-assisted analysis output for specific verse. Never written by v9 engine. NULL for all Phase 1 records.",
      "data_source": "NOT_WRITTEN — Phase 2 reserved",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    }
  ]
}

]  # end tables list

# ── Append new tables to existing JSON ───────────────────────────────────────
src = pathlib.Path("docs/field-data-flow-mapping.json")
existing = json.loads(src.read_text(encoding="utf-8"))
existing["tables"].extend(tables)
src.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
total = sum(len(t["fields"]) for t in existing["tables"])
print(f"Total tables now: {len(existing['tables'])}  ({total} fields total)")
print(f"New tables: {[t['table'] for t in tables]}")
