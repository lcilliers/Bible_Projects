"""
build_tables_1_3.py
Writes fresh JSON for tables 1-3 into field-data-flow-mapping.json,
replacing the existing tables array completely.
Based on verified source code reading of:
  engine/new_word.py, engine/gap_fill.py, engine/audit_word.py, engine/register.py
and spec: docs/Session-A-v9-Architecture-v4-Final-20260318.md
"""
import json, pathlib

NW = "NOT_WRITTEN"

def nw():
    return [{"stage": "—", "operation": "NOT_WRITTEN", "condition": "—", "value": "—"}]

tables = [

# ════════════════════════════════════════════════════════════════════════════
# TABLE 1 — word_registry
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "word_registry",
  "part": "Part 1 — Registration Tables",
  "description": "Master word anchor. One row per English word under research. First and last table touched by every engine run.",
  "spec_sections": ["§1.2", "§7.1", "§7.4", "§7.2 N19", "§6.1 S7", "§7.5 A10"],
  "modes_that_write": ["REGISTER", "NEW_WORD", "GAP_FILL", "AUDIT_WORD"],
  "table_spec_rules": [
    "§1.2: The registry is the anchor. Every run begins and ends with a confirmed word_registry row.",
    "§7.1: --register inserts a new row: no=MAX(no)+1, phase1_status=Pending, automation_eligible=1. Validates: no duplicate word; lowercase and hyphens only; source_list non-empty.",
    "§7.4: last_automation_run is the run-lock. LOCK_SENTINEL ('IN_PROGRESS') written before any API call; replaced with UTC timestamp at run end. --clear-lock sets to NULL.",
    "§4 M03: All sequential IDs must use SELECT MAX(id)+1 queried live — never hardcoded."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§7.1 · §4 M03",
      "spec_rule": "Auto-assigned sequential integer at registration. Never modified after INSERT.",
      "data_source": "SELECT MAX(id) AS m FROM word_registry → (m or 0) + 1",
      "py_file": "engine/register.py",
      "modes": {
        "REGISTER":   [{"stage": "--register", "operation": "INSERT", "condition": "Always — new row only", "value": "SELECT MAX(id) AS m FROM word_registry → (m or 0) + 1"}],
        "NEW_WORD":   [{"stage": "N1",  "operation": "READ", "condition": "SELECT * FROM word_registry WHERE no=?", "value": "read only"}],
        "GAP_FILL":   [{"stage": "S1",  "operation": "READ", "condition": "SELECT * FROM word_registry WHERE no=?", "value": "read only"}],
        "AUDIT_WORD": [{"stage": "A1",  "operation": "READ", "condition": "SELECT * FROM word_registry WHERE no=?", "value": "read only"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "no",
      "spec_section": "§7.1 · §4 M03",
      "spec_rule": "Sequential registry number. MAX(no)+1, queried live. Used as the primary lookup key by all engine modes.",
      "data_source": "SELECT MAX(no) AS m FROM word_registry → (m or 0) + 1",
      "py_file": "engine/register.py",
      "modes": {
        "REGISTER":   [{"stage": "--register", "operation": "INSERT", "condition": "Always", "value": "SELECT MAX(no) AS m FROM word_registry → (m or 0) + 1"}],
        "NEW_WORD":   [{"stage": "N1",  "operation": "READ", "condition": "Used as WHERE key in all NEW_WORD queries", "value": "read only"}],
        "GAP_FILL":   [{"stage": "S1",  "operation": "READ", "condition": "Used as WHERE key per word loop", "value": "read only"}],
        "AUDIT_WORD": [{"stage": "A1",  "operation": "READ", "condition": "Used as WHERE key", "value": "read only"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "word",
      "spec_section": "§7.1",
      "spec_rule": "Lowercase English word label. Validated: lowercase and hyphens only; no duplicates allowed. Never modified after INSERT.",
      "data_source": "researcher-supplied CLI argument: --word=[value]",
      "py_file": "engine/register.py",
      "modes": {
        "REGISTER":   [{"stage": "--register", "operation": "INSERT", "condition": "Validated lowercase; duplicate check", "value": "CLI arg --word as-supplied"}],
        "NEW_WORD":   [{"stage": "N1",  "operation": "READ", "condition": "Loaded from reg_row", "value": "read only"}],
        "GAP_FILL":   [{"stage": "S1",  "operation": "READ", "condition": "Loaded from reg row", "value": "read only"}],
        "AUDIT_WORD": [{"stage": "A1",  "operation": "READ", "condition": "Loaded from reg_row", "value": "read only"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "source_list",
      "spec_section": "§7.1",
      "spec_rule": "Researcher-supplied source list label. Required non-empty at registration. Copied to wa_file_index and mti_terms at write time.",
      "data_source": "researcher-supplied CLI argument: --source=[value]",
      "py_file": "engine/register.py",
      "modes": {
        "REGISTER":   [{"stage": "--register", "operation": "INSERT", "condition": "Non-empty validated", "value": "CLI arg --source"}],
        "NEW_WORD":   [{"stage": "N9",  "operation": "READ", "condition": "reg_row['source_list'] propagated to wa_file_index INSERT", "value": "read only — propagated downstream"}],
        "GAP_FILL":   [{"stage": "S2",  "operation": "READ", "condition": "reg['source_list'] propagated to wa_file_index INSERT", "value": "read only — propagated downstream"}],
        "AUDIT_WORD": [{"stage": "—",   "operation": "NOT_WRITTEN", "condition": "AUDIT_WORD reads reg_row but does not modify source_list", "value": "—"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "category_hint",
      "spec_section": "§7.1",
      "spec_rule": "Optional researcher category hint. Set at registration only. No engine mode modifies it.",
      "data_source": "researcher-supplied CLI argument: --category=[value] (optional)",
      "py_file": "engine/register.py",
      "modes": {
        "REGISTER":   [{"stage": "--register", "operation": "INSERT", "condition": "Optional — NULL if not supplied", "value": "CLI arg --category or NULL"}],
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "phase1_status",
      "spec_section": "§7.1 · §7.2 N19 · §6.1 S2/S7 · §7.5 A10",
      "spec_rule": "Pending at --register. NEW_WORD N19: 'Complete' if PASS else 'In Progress'. GAP_FILL S2: 'In Progress' at wa_file_index write; S7: final status. AUDIT_WORD A10: does NOT update phase1_status — retains current value.",
      "data_source": "NEW_WORD N19/GAP_FILL S7: audit_result → 'Complete' if PASS else 'In Progress'",
      "py_file": "engine/register.py · engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   [{"stage": "--register", "operation": "INSERT", "condition": "Always", "value": "hardcoded: 'Pending'"}],
        "NEW_WORD":   [
          {"stage": "N1",  "operation": "READ",   "condition": "STOP if != 'Pending'", "value": "read only"},
          {"stage": "N19", "operation": "UPDATE", "condition": "Always at run end", "value": "audit PASS → 'Complete'; else → 'In Progress'  |  UPDATE word_registry SET phase1_status=? WHERE no=?"}
        ],
        "GAP_FILL": [
          {"stage": "S1",  "operation": "READ",   "condition": "Filter: WHERE phase1_status='Pending'", "value": "read only"},
          {"stage": "S2",  "operation": "UPDATE", "condition": "At wa_file_index write (per word)", "value": "hardcoded: 'In Progress'  |  UPDATE word_registry SET phase1_status='In Progress' ... WHERE no=?"},
          {"stage": "S7",  "operation": "UPDATE", "condition": "After audit per word", "value": "audit PASS → retain existing; STOP/REVIEW → 'In Progress'  |  UPDATE word_registry SET phase1_status=? WHERE no=?"}
        ],
        "AUDIT_WORD": [
          {"stage": "A1",  "operation": "READ", "condition": "Read for context only", "value": "read only"},
          {"stage": "A10", "operation": "NOT_WRITTEN", "condition": "A10 UPDATE does not include phase1_status — field is not set by audit mode", "value": "— GAP: spec §7.5 A10 implies status update but code omits it"}
        ]
      },
      "optional": False,
      "spec_match": "⚠ Partial — AUDIT_WORD A10 does not update phase1_status; the field retains its pre-audit value even if audit result changes"
    },
    {
      "field": "automation_eligible",
      "spec_section": "§7.1 · §7.2 N1",
      "spec_rule": "Set 1 at registration. NEW_WORD reads at N1 to confirm eligibility (0 → STOP). GAP_FILL S1 uses in WHERE filter. Never modified by any engine mode.",
      "data_source": "hardcoded: 1 at INSERT",
      "py_file": "engine/register.py",
      "modes": {
        "REGISTER":   [{"stage": "--register", "operation": "INSERT", "condition": "Always", "value": "hardcoded: 1"}],
        "NEW_WORD":   [{"stage": "N1",  "operation": "READ", "condition": "automation_eligible=0 → STOP", "value": "read only"}],
        "GAP_FILL":   [{"stage": "S1",  "operation": "READ", "condition": "WHERE automation_eligible=1 filter in SELECT", "value": "read only"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "last_automation_run",
      "spec_section": "§7.4 · §7.2 N6/N19 · §6.1 S2/S7 · §7.5 A10",
      "spec_rule": "Run-lock field. LOCK_SENTINEL='IN_PROGRESS' must be written before any API call; replaced with UTC timestamp at run end. --clear-lock sets to NULL. Only NEW_WORD follows this protocol fully (N6: sentinel, N19: timestamp). GAP_FILL (S2) and AUDIT_WORD (A10) both write the completion timestamp directly without first setting the IN_PROGRESS sentinel.",
      "data_source": "lock: hardcoded 'IN_PROGRESS'; completion: _now() → datetime.now(utc).strftime('%Y-%m-%dT%H:%M:%S')",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER": nw(),
        "NEW_WORD": [
          {"stage": "N6",  "operation": "UPDATE", "condition": "Before any API call — stale lock check", "value": "UPDATE word_registry SET last_automation_run='IN_PROGRESS' WHERE no=?"},
          {"stage": "N19", "operation": "UPDATE", "condition": "Always at run end", "value": "UPDATE word_registry SET last_automation_run=_now() WHERE no=?"}
        ],
        "GAP_FILL": [
          {"stage": "S2",  "operation": "UPDATE", "condition": "At wa_file_index write — no prior sentinel step", "value": "UPDATE word_registry SET ..., last_automation_run=_now() WHERE no=?"},
          {"stage": "S7",  "operation": "UPDATE", "condition": "At final registry update", "value": "UPDATE word_registry SET last_automation_run=_now() WHERE no=?"}
        ],
        "AUDIT_WORD": [
          {"stage": "A10", "operation": "UPDATE", "condition": "Always at audit end — no prior sentinel step", "value": "UPDATE word_registry SET last_automation_run=_now() WHERE no=?"}
        ]
      },
      "optional": False,
      "spec_match": "⚠ Partial — GAP_FILL and AUDIT_WORD write the completion timestamp but neither sets LOCK_SENTINEL='IN_PROGRESS' before starting work; §7.4 run-lock guarantee requires the sentinel to be set before any API call"
    },
    {
      "field": "automation_run_id",
      "spec_section": "§7.2 N19 · §6.1 S7 · §7.5 A10",
      "spec_rule": "FK to engine_run_log.run_id. Written at run completion by all three engine modes.",
      "data_source": "engine/run_log.py make_run_id(mode) → f'RUN-{datetime.now(utc).strftime(\"%Y%m%d_%H%M%S\")}-{mode}'",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER": nw(),
        "NEW_WORD":   [{"stage": "N19", "operation": "UPDATE", "condition": "Always", "value": "UPDATE word_registry SET automation_run_id=run_id WHERE no=?"}],
        "GAP_FILL":   [
          {"stage": "S2", "operation": "UPDATE", "condition": "At wa_file_index write (per word)", "value": "UPDATE word_registry SET automation_run_id=run_id WHERE no=?"},
          {"stage": "S7", "operation": "UPDATE", "condition": "At final registry update", "value": "UPDATE word_registry SET automation_run_id=run_id WHERE no=?"}
        ],
        "AUDIT_WORD": [{"stage": "A10", "operation": "UPDATE", "condition": "Always", "value": "UPDATE word_registry SET automation_run_id=run_id WHERE no=?"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "phase1_term_count",
      "spec_section": "§7.2 N19 · §6.1 S4/S7 · §7.5 A10",
      "spec_rule": "Count of wa_term_inventory rows for this word. Written at run completion by all three engine modes.",
      "data_source": "N19: counts['total_terms_new'] from run loop; GAP_FILL S4/S7 and AUDIT_WORD A10: SELECT COUNT(*) FROM wa_term_inventory WHERE file_id IN (...)",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER": nw(),
        "NEW_WORD":   [{"stage": "N19", "operation": "UPDATE", "condition": "Always", "value": "UPDATE word_registry SET phase1_term_count=counts['total_terms_new'] WHERE no=?"}],
        "GAP_FILL":   [
          {"stage": "S4", "operation": "UPDATE", "condition": "Per word after audit", "value": "UPDATE word_registry SET phase1_term_count=SELECT COUNT(*) FROM wa_term_inventory WHERE file_id=? WHERE no=?"},
          {"stage": "S7", "operation": "UPDATE", "condition": "Final recount at registry update", "value": "UPDATE word_registry SET phase1_term_count=term_count WHERE no=?"}
        ],
        "AUDIT_WORD": [{"stage": "A10", "operation": "UPDATE", "condition": "Always", "value": "UPDATE word_registry SET phase1_term_count=SELECT COUNT(*) FROM wa_term_inventory WHERE file_id IN (...) WHERE no=?"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "phase1_verse_count",
      "spec_section": "§7.2 N19 · §6.1 S4/S7 · §7.5 A10",
      "spec_rule": "Count of span-confirmed verse records (span_strong_match=1 OR IS NULL). Written at run completion by all three engine modes.",
      "data_source": "N19: counts['total_verses_inserted']; GAP_FILL S4/S7 and AUDIT_WORD A10: SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN (...) AND (span_strong_match=1 OR IS NULL)",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py",
      "modes": {
        "REGISTER": nw(),
        "NEW_WORD":   [{"stage": "N19", "operation": "UPDATE", "condition": "Always", "value": "UPDATE word_registry SET phase1_verse_count=counts['total_verses_inserted'] WHERE no=?"}],
        "GAP_FILL":   [
          {"stage": "S4", "operation": "UPDATE", "condition": "Per word after audit", "value": "UPDATE word_registry SET phase1_verse_count=SELECT COUNT(*) FROM wa_verse_records WHERE file_id=? AND (span_strong_match=1 OR IS NULL) WHERE no=?"},
          {"stage": "S7", "operation": "UPDATE", "condition": "Final recount at registry update", "value": "UPDATE word_registry SET phase1_verse_count=verse_count WHERE no=?"}
        ],
        "AUDIT_WORD": [{"stage": "A10", "operation": "UPDATE", "condition": "Always", "value": "UPDATE word_registry SET phase1_verse_count=SELECT COUNT(*) FROM wa_verse_records WHERE file_id IN (...) AND (span_strong_match=1 OR IS NULL) WHERE no=?"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "phase1_input_file",
      "spec_section": "§9 Field-Level Mapping",
      "spec_rule": "Stores the run_id of the NEW_WORD run that created the word's data. Written only by NEW_WORD N19. GAP_FILL and AUDIT_WORD do not write this field.",
      "data_source": "engine/run_log.py make_run_id('NEW_WORD') → e.g. 'RUN-20260319_143022-NEW_WORD'",
      "py_file": "engine/new_word.py",
      "modes": {
        "REGISTER": nw(),
        "NEW_WORD":   [{"stage": "N19", "operation": "UPDATE", "condition": "Always", "value": "UPDATE word_registry SET phase1_input_file=run_id WHERE no=?"}],
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "⚠ Partial — GAP_FILL and AUDIT_WORD do not write phase1_input_file; field remains NULL or retains NEW_WORD value; spec §9 implies it should record the originating run for any mode that creates the word's Phase 1 data"
    },
    {
      "field": "strongs_list",
      "spec_section": "— Not in spec",
      "spec_rule": "No spec rule — field exists in DB schema and engine code (GAP_FILL S1 UPDATE) but is not referenced anywhere in the v9 Architecture specification.",
      "data_source": "STEP REST API text search via StepClient.get_strongs_for_word(word) → JSON array e.g. [{\"strong\":\"H7965\",\"count\":148},...]",
      "py_file": "analytics/step_client.py · engine/gap_fill.py",
      "modes": {
        "REGISTER": nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   [{"stage": "S1", "operation": "UPDATE", "condition": "Only if strongs_list IS NULL", "value": "UPDATE word_registry SET strongs_list=json_array WHERE no=?"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "— Not specified"
    },
    {
      "field": "notes",
      "spec_section": "§7.5 A10",
      "spec_rule": "AUDIT_WORD A10 is specified to update last_automation_run, automation_run_id, and notes. Researcher annotation field. However, A10 UPDATE in code only sets phase1_term_count, phase1_verse_count, last_automation_run, automation_run_id — notes is absent.",
      "data_source": "Not implemented — A10 UPDATE in audit_word.py does not include notes column",
      "py_file": "engine/audit_word.py",
      "modes": {
        "REGISTER": nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": [{"stage": "A10", "operation": "NOT_WRITTEN", "condition": "Spec says update — code does not implement it", "value": "— DIVERGES: UPDATE word_registry SET notes=? WHERE no=? is absent from A10"}]
      },
      "optional": False,
      "spec_match": "✗ Diverges — spec §7.5 A10 lists notes in the update statement but audit_word.py A10 UPDATE does not include the notes column; field is never written by any engine mode"
    }
  ]
},

# ════════════════════════════════════════════════════════════════════════════
# TABLE 2 — wa_file_index
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "wa_file_index",
  "part": "Part 2 — Core Word Data Tables",
  "description": "One row per word. Anchor connecting word_registry to all term and verse data. Created by NEW_WORD N9 or GAP_FILL S2. AUDIT_WORD reads it at A1 and updates testament_coverage at A9; never re-creates it.",
  "spec_sections": ["§7.2 N9", "§7.3", "§9 Field-Level Mapping", "§4 M03", "§7.5 A9"],
  "modes_that_write": ["NEW_WORD", "GAP_FILL", "AUDIT_WORD"],
  "table_spec_rules": [
    "§7.2 N9: INSERT one row inside atomic transaction N9-N15. id=MAX(id)+1. testament_coverage=NULL at insert; derived at N14.",
    "§7.3: part_number, total_parts, is_split, root_families_in_prior_parts are legacy columns from the manual multi-part pipeline. v9 always writes NULL/0 for these. Retained in schema for backward compatibility.",
    "§9: specification constant = 'Session A v9 Automation'. phase = 'Phase 1'. translation_used = 'ESV'. All hardcoded.",
    "§4 M03: id must be queried live via SELECT MAX(id)+1 — never hardcoded.",
    "§7.5 A9: AUDIT_WORD re-derives testament_coverage from confirmed verse rows and updates wa_file_index."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§7.2 N9 · §4 M03",
      "spec_rule": "Sequential integer. Must query MAX(id) live before insert.",
      "data_source": "engine/db.py get_max_id(conn, 'wa_file_index') → SELECT MAX(id) FROM wa_file_index → result + 1",
      "py_file": "engine/db.py · engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9",  "operation": "INSERT", "condition": "Part of atomic transaction N9-N15", "value": "get_max_id(conn, 'wa_file_index') + 1"}],
        "GAP_FILL":   [{"stage": "S2",  "operation": "INSERT", "condition": "Phase A, per word — idempotent; skipped if already exists", "value": "get_max_id(conn, 'wa_file_index') + 1"}],
        "AUDIT_WORD": [{"stage": "A1",  "operation": "READ",   "condition": "SELECT id FROM wa_file_index WHERE registry_id=? — no row → STOP", "value": "read only"}]
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "filename",
      "spec_section": "§9 Field-Level Mapping",
      "spec_rule": "Stores run_id — not a filesystem path. v9 replaced the prior .md filename convention with run_id.",
      "data_source": "engine/run_log.py make_run_id(mode) → f'RUN-{timestamp}-{mode}'",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Part of transaction", "value": "run_id string"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Phase A, per word", "value": "run_id string"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "registry_id",
      "spec_section": "§7.2 N9",
      "spec_rule": "word_registry.no value stored as TEXT. Links file_index row back to registry.",
      "data_source": "CLI arg registry_id (word_registry.no) → str(registry_id)",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Part of transaction", "value": "str(registry_id)"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Phase A, per word", "value": "str(registry_no)"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "word_registry_fk",
      "spec_section": "§7.2 N9",
      "spec_rule": "word_registry.id (PK integer, not .no). FK constraint to word_registry.",
      "data_source": "SELECT * FROM word_registry WHERE no=? → reg_row['id']",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Part of transaction", "value": "reg_row['id']"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Phase A, per word", "value": "reg['id']"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "word",
      "spec_section": "§9",
      "spec_rule": "English word label copied from word_registry.word.",
      "data_source": "SELECT word FROM word_registry WHERE no=? → reg_row['word']",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Part of transaction", "value": "reg_row['word']"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Phase A, per word", "value": "reg['word']"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "part_number",
      "spec_section": "§7.3 Multi-Part Legacy",
      "spec_rule": "Legacy column from v3-v8 manual multi-part pipeline. v9 always writes NULL. Column retained for backward compatibility.",
      "data_source": "hardcoded: NULL",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "NULL — hardcoded"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Always", "value": "NULL — hardcoded"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "total_parts",
      "spec_section": "§7.3 Multi-Part Legacy",
      "spec_rule": "Legacy column. v9 always writes NULL.",
      "data_source": "hardcoded: NULL",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "NULL — hardcoded"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Always", "value": "NULL — hardcoded"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "is_split",
      "spec_section": "§7.3 Multi-Part Legacy",
      "spec_rule": "Legacy column. v9 always writes 0.",
      "data_source": "hardcoded: 0",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "0 — hardcoded"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Always", "value": "0 — hardcoded"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "specification",
      "spec_section": "§9",
      "spec_rule": "Constant string identifying the automation spec version. Written from engine/constants.py.",
      "data_source": "engine/constants.py → SPECIFICATION constant = 'Session A v9 Automation'",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/constants.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "SPECIFICATION constant from engine/constants.py"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Always", "value": "SPECIFICATION constant"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "phase",
      "spec_section": "§9",
      "spec_rule": "Constant 'Phase 1'. Hardcoded for all v9 engine runs.",
      "data_source": "hardcoded: 'Phase 1'",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "'Phase 1'"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Always", "value": "'Phase 1'"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "produced_date",
      "spec_section": "§9",
      "spec_rule": "UTC date of the run that created this row. YYYY-MM-DD format.",
      "data_source": "_today() → datetime.now(utc).strftime('%Y-%m-%d')",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "_today() → UTC date string"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Always", "value": "_today()"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "translation_used",
      "spec_section": "§9",
      "spec_rule": "Constant 'ESV'. Hardcoded for all v9 engine runs.",
      "data_source": "hardcoded: 'ESV'",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "'ESV'"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Always", "value": "'ESV'"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "source_list",
      "spec_section": "§9",
      "spec_rule": "Copied from word_registry.source_list at file_index creation.",
      "data_source": "SELECT source_list FROM word_registry WHERE no=? → reg_row['source_list']",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N9", "operation": "INSERT", "condition": "Always", "value": "reg_row['source_list']"}],
        "GAP_FILL":   [{"stage": "S2", "operation": "INSERT", "condition": "Per word", "value": "reg['source_list']"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "testament_coverage",
      "spec_section": "§7.2 N14 · §9 · §7.5 A9",
      "spec_rule": "NULL at INSERT. Derived after verse records are committed by querying distinct testament values from confirmed verse rows (span_strong_match=1). Re-derived in AUDIT_WORD A9 from span_strong_match=1 OR IS NULL rows.",
      "data_source": "SELECT DISTINCT testament FROM wa_verse_records WHERE file_id=? AND span_strong_match=1 → 'OT_only' / 'NT_only' / 'both' / NULL",
      "py_file": "engine/new_word.py · engine/audit_word.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD": [
          {"stage": "N9",  "operation": "INSERT",  "condition": "Part of transaction", "value": "NULL — placeholder; derived post-transaction at N14"},
          {"stage": "N14", "operation": "UPDATE",  "condition": "After verse records committed", "value": "SELECT DISTINCT testament FROM wa_verse_records WHERE file_id=? AND span_strong_match=1 → UPDATE wa_file_index SET testament_coverage=? WHERE id=?"}
        ],
        "GAP_FILL": [
          {"stage": "S2",  "operation": "INSERT",  "condition": "Phase A", "value": "NULL — placeholder; no derivation step in GAP_FILL"},
          {"stage": "—",   "operation": "NOT_WRITTEN", "condition": "GAP_FILL has no testament_coverage derivation step after S3 verse insert — field remains NULL", "value": "— GAP: no equivalent of N14 in GAP_FILL stream"}
        ],
        "AUDIT_WORD": [
          {"stage": "A9",  "operation": "UPDATE",  "condition": "Always — re-derives from confirmed verses post-audit", "value": "SELECT DISTINCT testament FROM wa_verse_records WHERE file_id=? AND (span_strong_match=1 OR IS NULL) → UPDATE wa_file_index SET testament_coverage=? WHERE id=?"}
        ]
      },
      "optional": False,
      "spec_match": "⚠ Partial — GAP_FILL inserts the row with testament_coverage=NULL at S2 but has no derivation step; the field is never updated after verses are written by GAP_FILL (S3). AUDIT_WORD A9 corrects this for words it processes."
    },
    {
      "field": "root_families_in_prior_parts",
      "spec_section": "§7.3 Multi-Part Legacy",
      "spec_rule": "Legacy multi-part column. Never written by v9 engine. Retained in schema for backward compatibility only.",
      "data_source": "NOT_WRITTEN — legacy column",
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
},

# ════════════════════════════════════════════════════════════════════════════
# TABLE 3 — mti_terms
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "mti_terms",
  "part": "Part 2 — Core Word Data Tables",
  "description": "Master term index. One row per Strong's number processed. Created by NEW_WORD N10 or GAP_FILL S2 Phase C. Idempotent — re-checks existence before INSERT. AUDIT_WORD spec intent: INSERT any term returned by STEP API that is missing from mti_terms; flag as redundant any row in mti_terms not returned by STEP. Code currently does not implement either action.",
  "spec_sections": ["§7.2 N10", "§9 Field-Level Mapping", "§4 M03"],
  "modes_that_write": ["NEW_WORD", "GAP_FILL", "AUDIT_WORD (spec intent — not yet implemented)"],
  "table_spec_rules": [
    "§7.2 N10: INSERT per NEW term inside atomic transaction N9-N15.",
    "§9: status hardcoded 'extracted'. extraction_date = run date. strongs_reconciled = 1 if suffix was resolved (input != resolved), else 0.",
    "§4 M03: id must be queried live via SELECT MAX(id)+1.",
    "owning_part is a legacy multi-part column — always NULL in v9.",
    "Idempotent: both NEW_WORD and GAP_FILL re-check SELECT id FROM mti_terms WHERE strongs_number=? before INSERT.",
    "AUDIT_WORD spec intent (not yet implemented): (1) For each strongs_number returned by STEP API for this word — if not present in mti_terms, INSERT the row (same columns as NEW_WORD N10). (2) For each row already in mti_terms for this word — if its strongs_number is NOT in the STEP API response, UPDATE status='REDUNDANT'."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§7.2 N10 · §4 M03",
      "spec_rule": "Sequential integer. Must query MAX(id) live before insert.",
      "data_source": "engine/db.py get_max_id(conn, 'mti_terms') → SELECT MAX(id) FROM mti_terms → result + 1",
      "py_file": "engine/db.py · engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of atomic transaction N9-N15; only if strongs_number not already in mti_terms", "value": "get_max_id(conn, 'mti_terms') + 1"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent: only if SELECT id FROM mti_terms WHERE strongs_number=? returns no row", "value": "get_max_id(conn, 'mti_terms') + 1"}],
        "AUDIT_WORD": [
          {"stage": "A1",  "operation": "READ",        "condition": "Loads existing mti_terms rows for this word", "value": "read only"},
          {"stage": "A-x", "operation": "NOT_WRITTEN", "condition": "Should INSERT for each strongs_number in STEP response not already in mti_terms — not yet implemented", "value": "— DIVERGES: code never calls get_max_id(conn, 'mti_terms') or INSERT in audit_word.py"}
        ]
      },
      "optional": False,
      "spec_match": "✗ Diverges — AUDIT_WORD spec intent requires INSERT of missing term rows (terms in STEP API but absent from mti_terms); code does not implement this; all mti_terms fields are unset by AUDIT_WORD"
    },
    {
      "field": "strongs_number",
      "spec_section": "§7.2 N10 · §9",
      "spec_rule": "Resolved Strong's number (e.g. H7965). If input had a suffix that was resolved, stores the resolved form.",
      "data_source": "StepClient.get_vocab_info(strongs) → vocab['strong_number'] (resolved)",
      "py_file": "engine/new_word.py · engine/gap_fill.py · analytics/step_client.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab['strong_number'] — resolved strongs string"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent INSERT", "value": "vocab['strong_number'] — resolved strongs string"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "transliteration",
      "spec_section": "§9",
      "spec_rule": "Transliteration of the Strong's term. From STEP vocab API response.",
      "data_source": "STEP REST API GET /vocab?strong={x} → vocab['transliteration']",
      "py_file": "engine/new_word.py · engine/gap_fill.py · analytics/step_client.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('transliteration', '')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent INSERT", "value": "vocab.get('transliteration', '')"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "gloss",
      "spec_section": "§9",
      "spec_rule": "Primary gloss for the term. From STEP vocab API response.",
      "data_source": "STEP REST API → vocab['gloss']",
      "py_file": "engine/new_word.py · engine/gap_fill.py · analytics/step_client.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('gloss', '')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent INSERT", "value": "vocab.get('gloss', '')"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "language",
      "spec_section": "§9",
      "spec_rule": "Derived from STEP vocab API 'language' field. 'Hebrew' or 'Greek'.",
      "data_source": "vocab.get('language', 'Hebrew')",
      "py_file": "engine/new_word.py · engine/gap_fill.py · analytics/step_client.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of transaction", "value": "vocab.get('language', 'Hebrew')"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent INSERT", "value": "vocab.get('language', 'Hebrew')"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "owning_registry",
      "spec_section": "§9",
      "spec_rule": "word_registry.no stored as string. Links this term to its registry entry.",
      "data_source": "str(registry_id) — CLI arg word_registry.no",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of transaction", "value": "str(registry_id)"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent INSERT", "value": "str(registry_no)"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "owning_word",
      "spec_section": "§9",
      "spec_rule": "English word label from word_registry. Denormalised copy for query convenience.",
      "data_source": "SELECT word FROM word_registry WHERE no=? → reg_row['word']",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of transaction", "value": "reg_row['word']  (word variable)"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent INSERT", "value": "word variable"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "owning_part",
      "spec_section": "§7.3 Multi-Part Legacy",
      "spec_rule": "Legacy multi-part column. v9 always writes NULL.",
      "data_source": "hardcoded: NULL",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Always", "value": "NULL — hardcoded"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Always", "value": "NULL — hardcoded"}],
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "✓ Match"
    },
    {
      "field": "word_data_reference",
      "spec_section": "§9",
      "spec_rule": "Stores wa_file_index.id as a string. Links mti_terms row to its file index entry.",
      "data_source": "str(file_id) — wa_file_index.id just inserted at N9/S2",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Part of transaction; file_id available from N9", "value": "str(file_id)"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Idempotent INSERT; file_id from Phase A", "value": "str(file_id)"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "status",
      "spec_section": "§9",
      "spec_rule": "'extracted' at INSERT (hardcoded). AUDIT_WORD spec intent: UPDATE status='REDUNDANT' for any row whose strongs_number is not returned by the STEP API for this word.",
      "data_source": "INSERT: hardcoded 'extracted' | AUDIT_WORD UPDATE: 'REDUNDANT' (confirmed flag value)",
      "py_file": "engine/new_word.py · engine/gap_fill.py · engine/audit_word.py (pending)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10",      "operation": "INSERT",        "condition": "Always",                                                                              "value": "'extracted' — hardcoded"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT",      "condition": "Always",                                                                              "value": "'extracted' — hardcoded"}],
        "AUDIT_WORD": [{"stage": "A-x",      "operation": "NOT_WRITTEN",  "condition": "Should UPDATE status='REDUNDANT' for any row whose strongs_number is absent from STEP API response — not yet implemented", "value": "— DIVERGES: UPDATE mti_terms SET status='REDUNDANT' WHERE id=? not present in audit_word.py"}]
      },
      "optional": False,
      "spec_match": "⚠ Partial — INSERT correctly sets 'extracted'; AUDIT_WORD should UPDATE status='REDUNDANT' for stale term rows (strongs_number absent from STEP API response) but code does not implement it"
    },
    {
      "field": "extraction_date",
      "spec_section": "§9",
      "spec_rule": "UTC date of the run that created this term row. YYYY-MM-DD format.",
      "data_source": "_today() → datetime.now(utc).strftime('%Y-%m-%d')",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Always", "value": "_today()"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Always", "value": "_today()"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    },
    {
      "field": "strongs_reconciled",
      "spec_section": "§9",
      "spec_rule": "1 if the resolved strongs_number differs from the input (suffix stripped/mapped); 0 otherwise.",
      "data_source": "1 if resolved != strong else 0",
      "py_file": "engine/new_word.py · engine/gap_fill.py",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [{"stage": "N10", "operation": "INSERT", "condition": "Always", "value": "1 if resolved != strongs_input else 0"}],
        "GAP_FILL":   [{"stage": "S2 Phase C", "operation": "INSERT", "condition": "Always", "value": "1 if resolved != strong else 0"}],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✓ Match"
    }
  ]
}

]  # end tables list

# ── Load existing JSON, replace tables array, write back ──────────────────
src = pathlib.Path("docs/field-data-flow-mapping.json")
existing = json.loads(src.read_text(encoding="utf-8"))
existing["tables"] = tables
src.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Written {len(tables)} tables ({sum(len(t['fields']) for t in tables)} fields total).")
