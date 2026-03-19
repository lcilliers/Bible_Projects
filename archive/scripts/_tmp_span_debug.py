"""Debug span filter for H7965H."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from analytics.step_client import StepClient
from engine.span_filter import filter_verse_records, apply_span_filter, _base_prefix

strong = "H7965H"
print(f"base_prefix for {strong!r}: {_base_prefix(strong)!r}")

client = StepClient()
print(f"Fetching from STEP for {strong}...")
raw_records, html_map = client.get_verse_records_with_html(strong)
print(f"STEP returned {len(raw_records)} raw records, {len(html_map)} html entries")

if raw_records:
    result = filter_verse_records(raw_records, strong, html_map)
    print(f"stored={len(result['stored'])}  filtered={len(result['filtered'])}  conflict={result['conflict']}")

    # Show first 5 stored with their ref
    print("\nFirst 5 stored refs:")
    for r in result['stored'][:5]:
        print(f"  {r['ref']}  span_strong_match={r['span_strong_match']}  target_word={r.get('target_word','')!r}")

    # Show one filtered example with its html
    if result['filtered']:
        ex = result['filtered'][0]
        osisId = ex['osisId']
        html = html_map.get(osisId, '')
        print(f"\nExample filtered: {ex['ref']}")
        # Show spans in html
        import re
        spans = re.findall(r"<span[^>]*\bstrong=['\"]([^'\"]+)['\"][^>]*>", html)
        print(f"  spans strong attrs: {spans}")
else:
    print("No records returned from STEP")
