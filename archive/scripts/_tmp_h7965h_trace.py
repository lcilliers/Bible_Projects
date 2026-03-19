"""Detailed trace of get_verse_records_with_html for H7965H."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from analytics.step_client import StepClient

client = StepClient()
strong = "H7965H"

# Step 1: resolved
resolved = client._resolved_strong(strong)
print(f"_resolved_strong({strong!r}) = {resolved!r}")

# Step 2: first search
first = client._search_range(resolved)
total = first.get("total", 0)
print(f"_search_range({resolved!r}): total={total}")

# Step 3: base fallback check
_base_m = re.match(r'^([HG]\d+)[A-Za-z]$', resolved)
print(f"base_m on {resolved!r}: {_base_m}")
if _base_m:
    base_code = _base_m.group(1)
    print(f"base_code = {base_code!r}")
    base_first = client._search_range(base_code)
    base_total = base_first.get("total", 0)
    print(f"base search {base_code!r}: total={base_total}")
else:
    print("No base match — regex did not match resolved code")
