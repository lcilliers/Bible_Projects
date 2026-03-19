"""
extract_spec_match.py — Field compliance summary from field-data-flow-mapping.json.
Shows all fields with spec_match; for ⚠ and ✗ shows spec_rule beneath.
"""
import json, pathlib

MODES = ["REGISTER", "NEW_WORD", "GAP_FILL", "AUDIT_WORD"]

def mode_val(entries):
    """Return compact label for a mode's entries."""
    if not entries:
        return "—"
    ops = []
    for e in entries:
        op  = e.get("operation", "")
        val = e.get("value", "")
        stg = e.get("stage", "")
        if op in ("NOT_WRITTEN",) or (stg == "—" and val == "—"):
            ops.append("—")
        else:
            v = val[:35] + "…" if len(val) > 35 else val
            ops.append(f"{op}({stg}): {v}")
    deduped = list(dict.fromkeys(ops))
    return " | ".join(deduped)

d = json.loads(pathlib.Path(__file__).parent.joinpath("field-data-flow-mapping.json").read_text(encoding="utf-8"))
for t in d["tables"]:
    print(f"\nTABLE: {t['table']}")
    for fld in t["fields"]:
        sm   = fld.get("spec_match", "")
        req  = "REQ" if not fld.get("optional", True) else "opt"
        print(f"  [{req}] {fld['field']:<35} {sm}")
        if sm.startswith("⚠") or sm.startswith("✗") or sm.startswith("—"):
            print(f"         spec_rule : {fld.get('spec_rule','')}")
        if not fld.get("optional", True) and (sm.startswith("⚠") or sm.startswith("✗")):
            modes = fld.get("modes", {})
            for m in MODES:
                mv = mode_val(modes.get(m, []))
                if mv != "—":
                    print(f"         {m:<17}: {mv}")
        print()
