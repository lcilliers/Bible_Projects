"""
_build_tables_7_9.py
Appends tables 7-9 to field-data-flow-mapping.json.

Tables:
  7. wa_term_root_family    — researcher-assigned root families; DEFERRED; engine never writes
  8. phase2_flag_types      — reference/lookup table; seeded by migration; no run mode writes
  9. wa_term_phase2_flags   — junction: terms ↔ phase2 flags; spec says engine writes at N16/S5;
                              code (run_flag_engine) never INSERTs here → ✗ Diverges

Source files examined:
  engine/flag_engine.py     — run_flag_engine() only writes wa_data_quality_flags; no wa_term_phase2_flags INSERT
  data/schema/create_tables.sql — schema for all three tables
  docs/Session-A-v9-Architecture-v4-Final-20260318.md — §9 field mapping, §14 schema summary,
      §6.1 S5, §7.2 N16, §8.1 WR-13/WR-16
"""

import json, pathlib


def nw():
    return [{"stage": "—", "operation": "NOT_WRITTEN", "condition": "—", "value": "—"}]


tables = [

# ════════════════════════════════════════════════════════════════════════════
# TABLE 7 — wa_term_root_family
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "wa_term_root_family",
  "part": "Part 2 — Core Word Data Tables",
  "description": "Root family labels assigned to each term from wa_term_inventory. One row per root family membership per term — a term may belong to multiple families. Entirely researcher-assigned. The engine never writes to this table. All rows null for automation terms (v9). WR-13 explicitly excludes root_code from the undocumented-null check.",
  "spec_sections": ["§9", "§14", "§8.1 WR-13"],
  "modes_that_write": [],
  "table_spec_rules": [
    "§9: wa_term_root_family.root_code — Researcher judgment | null until assigned | DEFERRED. Not written by engine. Expected null for all automation terms. Not flagged by WR-13.",
    "§14: Content | Researcher (deferred) | Unchanged — populated by researcher, not engine.",
    "§8.1 WR-13: wa_term_root_family.root_code is explicitly excluded from the undocumented-null quality flag check.",
    "No engine mode (NEW_WORD, GAP_FILL, AUDIT_WORD) writes to this table. Rows appear only when a researcher assigns root families to a term (next-phase work).",
    "~640 rows in DB baseline — all written by researcher during earlier manual processing phases."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§14",
      "spec_rule": "AUTOINCREMENT PK. Not assigned by engine — researcher writes these rows.",
      "data_source": "NOT_WRITTEN — researcher-assigned",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "— Not written by engine (DEFERRED)"
    },
    {
      "field": "term_inv_id",
      "spec_section": "§9 · §14",
      "spec_rule": "FK to wa_term_inventory.id. Links root family row to its owning term. Assigned by researcher.",
      "data_source": "NOT_WRITTEN — researcher-assigned",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "— Not written by engine (DEFERRED)"
    },
    {
      "field": "root_code",
      "spec_section": "§9",
      "spec_rule": "Root family identifier, e.g. 'TSR', 'CHARAH', 'LUPE'. Researcher judgment — null until assigned. DEFERRED. WR-13 explicitly excludes from undocumented-null check.",
      "data_source": "NOT_WRITTEN — researcher judgment",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "— Not written by engine (DEFERRED)"
    },
    {
      "field": "root_language",
      "spec_section": "§14",
      "spec_rule": "'Hebrew', 'Greek', or 'Aramaic'. Researcher-assigned. Not written by engine.",
      "data_source": "NOT_WRITTEN — researcher-assigned",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "— Not written by engine (DEFERRED)"
    },
    {
      "field": "root_gloss",
      "spec_section": "§14",
      "spec_rule": "Brief English gloss for the root, e.g. 'to be angry', 'inner peace'. Researcher-assigned. Not written by engine.",
      "data_source": "NOT_WRITTEN — researcher-assigned",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "— Not written by engine (DEFERRED)"
    },
    {
      "field": "note",
      "spec_section": "§14",
      "spec_rule": "Additional researcher note about this root family membership. Not written by engine.",
      "data_source": "NOT_WRITTEN — researcher annotation",
      "py_file": "—",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "— Not written by engine (DEFERRED)"
    }
  ]
},

# ════════════════════════════════════════════════════════════════════════════
# TABLE 8 — phase2_flag_types
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "phase2_flag_types",
  "part": "Part 3 — Phase-2 Flags (shared lookup)",
  "description": "Lookup table for Phase 2 analytical flags. 25 rows. Seeded historically by migration scripts and patch imports — not written by any run mode. Both wa_term_phase2_flags and mti_term_flags FK to this single table. All 25 flags are researcher judgment flags; none are written by the v9 engine. Spec §14 classifies this table as Reference with no mode.",
  "spec_sections": ["§14", "§12.2 migration history"],
  "modes_that_write": [],
  "table_spec_rules": [
    "§14: Reference | — | Unchanged. No run mode writes to this table.",
    "25 rows populated via historical migration (migrate_flag_tables.py consolidated wa_phase2_flag_types into this table at normalisation).",
    "All 25 phase2_flag_types entries represent researcher judgment flags — none are derivable by the engine. Spec §13 (checklist): 'Judgment-deferred fields confirmed: wa_term_root_family, god_as_subject, somatic_link, mti_term_flags, all 25 phase2_flag_types judgment flags.'",
    "flag_engine.py does not reference this table when writing flags — only wa_quality_flag_types is used for derivable flags."
  ],
  "fields": [
    {
      "field": "id",
      "spec_section": "§14",
      "spec_rule": "AUTOINCREMENT PK. Seeded by migration; read only at runtime.",
      "data_source": "Seeded by migration — read only by run modes",
      "py_file": "scripts/migrate_flag_tables.py (historical seeding only)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "— Reference table (seeded by migration; no run mode writes)"
    },
    {
      "field": "flag_code",
      "spec_section": "§14",
      "spec_rule": "25 analytical flag codes, e.g. 'GOD_AS_SUBJECT', 'SOMATIC_INNER_LINK', 'THEOLOGICAL_ANCHOR'. UNIQUE constraint. Seeded by migration.",
      "data_source": "Seeded by migration — read only at runtime. Run modes FK-reference via wa_term_phase2_flags.flag_id.",
      "py_file": "scripts/migrate_flag_tables.py (historical seeding only)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "— Reference table (seeded by migration; no run mode writes)"
    },
    {
      "field": "description",
      "spec_section": "§14",
      "spec_rule": "Human-readable description of the flag. Seeded by migration.",
      "data_source": "Seeded by migration — read only at runtime",
      "py_file": "scripts/migrate_flag_tables.py (historical seeding only)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   nw(),
        "GAP_FILL":   nw(),
        "AUDIT_WORD": nw()
      },
      "optional": True,
      "spec_match": "— Reference table (seeded by migration; no run mode writes)"
    }
  ]
},

# ════════════════════════════════════════════════════════════════════════════
# TABLE 9 — wa_term_phase2_flags
# ════════════════════════════════════════════════════════════════════════════
{
  "table": "wa_term_phase2_flags",
  "part": "Part 3 — Phase-2 Flags (shared lookup)",
  "description": "Junction table: wa_term_inventory ↔ phase2_flag_types (many-to-many). Composite PK (term_inv_id, flag_id) — no separate id column. Spec says engine writes 'derivable flags' here at NEW_WORD N16 and GAP_FILL S5. However, flag_engine.py's run_flag_engine() writes ONLY to wa_data_quality_flags and never INSERTs to this table. No INSERT INTO wa_term_phase2_flags exists anywhere in engine/ code. In practice, all rows written to this table come from manual DB patch imports, not from engine runs.",
  "spec_sections": ["§6.1 S5", "§7.2 N16", "§14"],
  "modes_that_write": [],
  "table_spec_rules": [
    "§7.2 N16: 'Run flag engine. Evaluate derivable flags. INSERT wa_term_phase2_flags, wa_data_quality_flags (including SPAN_RESOLUTION_CONFLICT for any span-conflict terms).'",
    "§6.1 S5: 'FLAG_ENGINE | Terms written in S4 | wa_term_phase2_flags (derivable flags); wa_data_quality_flags including SPAN_RESOLUTION_CONFLICT where applicable.'",
    "§14: 'Content | Engine (derivable) | Unchanged' — spec intent is engine-written.",
    "CODE REALITY: flag_engine.py run_flag_engine() docstring says 'Writes rows to wa_term_phase2_flags and wa_data_quality_flags' but implementation only writes to wa_data_quality_flags. No INSERT INTO wa_term_phase2_flags anywhere in engine/ code.",
    "CODE REALITY: flag_engine.py comment: 'All other phase2_flag_types are judgment flags deferred to the researcher.' Derivable quality flags go to wa_data_quality_flags (HIGH_FREQUENCY_ANCHOR, THIN_DATA, SMALL_VERSE_SAMPLE, NO_WORD_ANALYSIS, NO_VERSES, SPAN_RESOLUTION_CONFLICT).",
    "AUDIT_WORD has no explicit flag engine step in its step sequence — wa_term_phase2_flags is not touched.",
    "Impact: Terms processed by v9 automation engine have zero rows in wa_term_phase2_flags. The table has rows only for terms processed before v9 (manual patches).",
    "COMPOSITE PK — no separate id column. Fields are term_inv_id and flag_id only."
  ],
  "fields": [
    {
      "field": "term_inv_id",
      "spec_section": "§6.1 S5 · §7.2 N16",
      "spec_rule": "FK to wa_term_inventory.id. Part of composite PK. Spec: written by engine at N16 (NEW_WORD) and S5 (GAP_FILL). Code: never set — run_flag_engine() does not INSERT to this table.",
      "data_source": "NOT_WRITTEN by engine — rows written only via manual DB patch imports",
      "py_file": "engine/flag_engine.py (listed in docstring but not implemented)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [
          {"stage": "N16", "operation": "NOT_WRITTEN",
           "condition": "Spec says 'INSERT wa_term_phase2_flags (derivable flags)' at N16; code run_flag_engine() never INSERTs to this table",
           "value": "— ✗ Diverges from spec §7.2 N16"}
        ],
        "GAP_FILL":   [
          {"stage": "S5", "operation": "NOT_WRITTEN",
           "condition": "Spec says FLAG_ENGINE writes wa_term_phase2_flags at S5; code run_flag_engine() never INSERTs to this table",
           "value": "— ✗ Diverges from spec §6.1 S5"}
        ],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✗ Diverges — spec §7.2 N16 and §6.1 S5 specify engine writes derivable flags to wa_term_phase2_flags; run_flag_engine() in code only writes to wa_data_quality_flags; no INSERT INTO wa_term_phase2_flags exists in engine/ code; rows written only by manual DB patch imports for pre-v9 terms"
    },
    {
      "field": "flag_id",
      "spec_section": "§6.1 S5 · §7.2 N16",
      "spec_rule": "FK to phase2_flag_types.id. Part of composite PK. Spec: derivable flags written by engine. Code: never written by engine.",
      "data_source": "NOT_WRITTEN by engine — rows written only via manual DB patch imports",
      "py_file": "engine/flag_engine.py (listed in docstring but not implemented)",
      "modes": {
        "REGISTER":   nw(),
        "NEW_WORD":   [
          {"stage": "N16", "operation": "NOT_WRITTEN",
           "condition": "Same divergence as term_inv_id — no INSERT to wa_term_phase2_flags",
           "value": "—"}
        ],
        "GAP_FILL":   [
          {"stage": "S5", "operation": "NOT_WRITTEN",
           "condition": "Same divergence as term_inv_id — no INSERT to wa_term_phase2_flags",
           "value": "—"}
        ],
        "AUDIT_WORD": nw()
      },
      "optional": False,
      "spec_match": "✗ Diverges — same as term_inv_id; the entire table is not written by v9 engine despite spec §7.2 N16 and §6.1 S5 intent"
    }
  ]
}

]  # end tables list


# ── Append to existing JSON ───────────────────────────────────────────────────
src = pathlib.Path("docs/field-data-flow-mapping.json")
existing = json.loads(src.read_text(encoding="utf-8"))
existing["tables"].extend(tables)
src.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
total_fields = sum(len(t["fields"]) for t in existing["tables"])
print(f"Total tables now: {len(existing['tables'])}  ({total_fields} fields total)")
print(f"New tables: {[t['table'] for t in tables]}")
