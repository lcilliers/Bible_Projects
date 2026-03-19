"""
Merge GAP_FILL_SINGLE and BULK_GAP_FILL into a single GAP_FILL mode.
- BULK_GAP_FILL entries represent the actual code; keep all meaningful entries from both.
- Mode order becomes: REGISTER, NEW_WORD, GAP_FILL, AUDIT_WORD.
- Replace all text references to either old name with GAP_FILL.
"""
import json

NOT_WRITTEN_ENTRY = {"stage": "—", "operation": "NOT_WRITTEN", "condition": "—", "value": "—"}

def is_not_written(entry):
    return entry.get("operation") in ("NOT_WRITTEN", "") or (
        entry.get("stage") == "—" and entry.get("value") == "—"
    )

def merge_entries(single, bulk):
    meaningful = [e for e in single + bulk if not is_not_written(e)]
    if not meaningful:
        return [NOT_WRITTEN_ENTRY]
    # Deduplicate by (stage, operation, value prefix)
    seen = set()
    deduped = []
    for e in meaningful:
        key = (e.get("stage", ""), e.get("operation", ""), e.get("value", "")[:60])
        if key not in seen:
            seen.add(key)
            deduped.append(e)
    return deduped

def fix_text(s):
    if not isinstance(s, str):
        return s
    s = s.replace("BULK_GAP_FILL", "GAP_FILL")
    s = s.replace("GAP_FILL_SINGLE", "GAP_FILL")
    return s

with open("docs/field-data-flow-mapping.json", encoding="utf-8") as f:
    data = json.load(f)

for tbl in data["tables"]:
    # modes_that_write
    seen_gf = False
    new_mw = []
    for m in tbl.get("modes_that_write", []):
        if m in ("GAP_FILL_SINGLE", "BULK_GAP_FILL"):
            if not seen_gf:
                new_mw.append("GAP_FILL")
                seen_gf = True
        else:
            new_mw.append(m)
    tbl["modes_that_write"] = new_mw

    # table_spec_rules
    tbl["table_spec_rules"] = [fix_text(r) for r in tbl.get("table_spec_rules", [])]

    for fld in tbl["fields"]:
        modes = fld.get("modes", {})
        single = modes.get("GAP_FILL_SINGLE", [])
        bulk   = modes.get("BULK_GAP_FILL", [])
        merged = merge_entries(single, bulk)

        new_modes = {}
        for m in ("REGISTER", "NEW_WORD", "GAP_FILL", "AUDIT_WORD"):
            if m == "GAP_FILL":
                new_modes[m] = merged
            elif m in modes:
                new_modes[m] = modes[m]
        fld["modes"] = new_modes

        for key in ("spec_section", "spec_rule", "data_source", "spec_match"):
            if key in fld:
                fld[key] = fix_text(fld[key])

with open("docs/field-data-flow-mapping.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done — GAP_FILL_SINGLE + BULK_GAP_FILL merged into GAP_FILL.")
