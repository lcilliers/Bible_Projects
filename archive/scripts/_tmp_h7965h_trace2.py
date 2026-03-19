"""Test get_verse_records_with_html directly with added trace."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Force reload to bypass pycache
import importlib
import analytics.step_client as sc_module
importlib.reload(sc_module)
StepClient = sc_module.StepClient

client = StepClient()

# Manually replicate the method with prints
import re as _re
strong = "H7965H"
resolved = client._resolved_strong(strong)
print(f"resolved: {resolved!r}")
first = client._search_range(resolved)
total = first.get("total", 0)
print(f"initial total: {total}")

if total <= 5:
    _base_m = _re.match(r'^([HG]\d+)[A-Za-z]$', resolved)
    print(f"base_m: {_base_m}")
    if _base_m:
        base_code = _base_m.group(1)
        print(f"base_code: {base_code!r}")
        for try_code in [base_code, base_code + 'A']:
            base_first = client._search_range(try_code)
            base_total = base_first.get("total", 0)
            print(f"  try_code={try_code!r} -> total={base_total}")
            if base_total > total:
                resolved = try_code
                first = base_first
                total = base_total
                print(f"  -> using {try_code!r}, total={total}")
                break

print(f"\nFinal resolved: {resolved!r}, total: {total}")
