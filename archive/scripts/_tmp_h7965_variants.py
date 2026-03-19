"""Test what STEP returns for H7965 (base, no suffix) vs H7965H."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from analytics.step_client import StepClient

client = StepClient()

for code in ['H7965', 'H7965H', 'H7965A', 'H7965B']:
    raw_records, html_map = client.get_verse_records_with_html(code)
    print(f"{code}: {len(raw_records)} verses returned")
    if raw_records:
        import re
        # Show first span strong attrs from first verse
        first_html = html_map.get(raw_records[0]['osisId'], '')
        spans = re.findall(r"<span[^>]*\bstrong=['\"]([^'\"]+)['\"]", first_html)
        print(f"  first verse {raw_records[0]['ref']!r}, spans: {spans[:3]}")
