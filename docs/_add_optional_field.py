"""
One-shot transformation:
  1. Insert "optional": true/false into every field entry (before "spec_match").
  2. Fix spec_match for fields where a required field is left unset by a mode
     that the spec expects to write it.

optional=false  →  spec expects a concrete value when processing completes.
optional=true   →  field is legacy-only, researcher-optional, or intentionally NULL in v9.
"""
import json

OPTIONAL = {
    "word_registry": {
        "id":                   False,  # assigned at registration — always required
        "no":                   False,  # sequential registry number — required
        "word":                 False,  # English word label — required, validated
        "source_list":          False,  # "Required non-empty at registration" per spec
        "category_hint":        True,   # "Optional researcher category" per spec_rule
        "phase1_status":        False,  # lifecycle status — required for all run modes
        "automation_eligible":  False,  # must be set at registration
        "last_automation_run":  False,  # run-lock field — required per §7.4
        "automation_run_id":    False,  # FK to run log — written at every run completion
        "phase1_term_count":    False,  # "Written at run completion" — required all runs
        "phase1_verse_count":   False,  # "Written at run completion" — required all runs
        "phase1_input_file":    False,  # stores run_id of initiating NEW_WORD run
        "strongs_list":         False,  # required for BULK mode (S1 population)
    },
    "wa_file_index": {
        "id":                           False,
        "filename":                     False,  # run_id identifier
        "registry_id":                  False,
        "word_registry_fk":             False,
        "word":                         False,
        "part_number":                  True,   # legacy multi-part column — always NULL in v9
        "total_parts":                  True,   # legacy — always NULL in v9
        "is_split":                     True,   # legacy — always 0 in v9; no semantic value
        "specification":                False,
        "phase":                        False,
        "produced_date":                False,
        "translation_used":             False,
        "source_list":                  False,
        "testament_coverage":           False,  # spec requires derivation post-verse-insert
        "root_families_in_prior_parts": True,   # legacy multi-part column — not written in v9
    },
    "mti_terms": {
        "id":                 False,
        "strongs_number":     False,  # resolved Strong's number always expected
        "transliteration":    False,
        "gloss":              False,
        "language":           False,
        "owning_registry":    False,
        "owning_word":        False,
        "owning_part":        True,   # legacy multi-part column — always NULL in v9
        "word_data_reference": False,
        "status":             False,
        "extraction_date":    False,
        "strongs_reconciled": False,
    },
}

# Spec_match overrides: keyed by (table, field).
# Applied wherever a non-optional field is left unset by a mode that runs
# to completion and is therefore expected to populate it.
OVERRIDES = {
    ("word_registry", "phase1_term_count"): (
        "⚠ Partial — BULK_GAP_FILL does not write phase1_term_count at run "
        "completion; spec says 'Written at run completion' applies to all run modes"
    ),
    ("word_registry", "phase1_verse_count"): (
        "⚠ Partial — BULK_GAP_FILL does not write phase1_verse_count at run "
        "completion; spec says 'Written at run completion' applies to all run modes"
    ),
}

src = "docs/field-data-flow-mapping.json"

with open(src, encoding="utf-8") as f:
    data = json.load(f)

for table_obj in data["tables"]:
    tname = table_obj["table"]
    opt_map = OPTIONAL.get(tname, {})
    for fobj in table_obj["fields"]:
        fname = fobj["field"]
        is_optional = opt_map.get(fname, True)   # default True for unmapped fields
        override = OVERRIDES.get((tname, fname))

        # Rebuild field dict inserting "optional" before "spec_match"
        rebuilt = {}
        for k, v in fobj.items():
            if k == "spec_match":
                rebuilt["optional"] = is_optional
                rebuilt["spec_match"] = override if override else v
            else:
                rebuilt[k] = v
        fobj.clear()
        fobj.update(rebuilt)

with open(src, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done — optional field added, spec_match overrides applied.")
