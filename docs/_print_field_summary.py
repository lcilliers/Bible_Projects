import json

MODES = ["NEW_WORD", "GAP_FILL", "AUDIT_WORD"]

def mode_summary(entries):
    """Return a short label: blank if NOT_WRITTEN/—, otherwise the operation + value."""
    if not entries:
        return "—"
    ops = []
    for e in entries:
        op = e.get("operation", "")
        val = e.get("value", "")
        if op in ("NOT_WRITTEN", "") or val in ("—", ""):
            ops.append("—")
        else:
            # Show operation and a short value
            short_val = val[:40] + "..." if len(val) > 40 else val
            ops.append(f"{op}: {short_val}")
    # Deduplicate while preserving order
    seen = []
    for o in ops:
        if o not in seen:
            seen.append(o)
    return " | ".join(seen)

with open('docs/field-data-flow-mapping.json', encoding='utf-8') as f:
    data = json.load(f)

for tbl in data['tables']:
    required_fields = [f for f in tbl['fields'] if not f.get('optional', True)]
    if not required_fields:
        continue
    print(f"\n{'='*120}")
    print(f"TABLE: {tbl['table']}  (required fields only)")
    print(f"{'='*120}")
    hdr = f"{'Field':<30} {'Spec Match':<14} {'NEW_WORD':<40} {'GAP_FILL':<40} {'AUDIT_WORD':<40}"
    print(hdr)
    print("-"*180)
    for fld in required_fields:
        match = fld.get('spec_match', '')
        icon = match.split(' ')[0] if match else '—'
        modes = fld.get('modes', {})
        cols = [mode_summary(modes.get(m, [])) for m in MODES]
        row = f"{fld['field']:<30} {icon:<14} {cols[0]:<40} {cols[1]:<40} {cols[2]:<40}"
        print(row)

