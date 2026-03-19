"""Deep-read the two working STEP endpoints for H8057 (simkhah/gladness)."""
import requests, json

base = 'http://localhost:8989'
strong = 'H8057'

# ── Endpoint 1: module.getInfo (vocab/lexicon data) ──────────────────────────
print('=== module/getInfo ===')
r1 = requests.get(f'{base}/rest/module/getInfo/ESV_th//{strong}///', timeout=15)
d1 = r1.json()
print(json.dumps(d1, indent=2, ensure_ascii=False)[:5000])

print('\n\n=== search/masterSearch (verse occurrences) ===')
r2 = requests.get(f'{base}/rest/search/masterSearch/{strong}|version=ESV_th', timeout=30)
d2 = r2.json()

# Show structure - top-level keys and sizes
print('Top-level keys:', list(d2.keys()))
print('searchType:', d2.get('searchType'))
print('masterVersion:', d2.get('masterVersion'))

# How many results?
if 'searchResults' in d2:
    sr = d2['searchResults']
    print(f'searchResults type: {type(sr).__name__}')
    if isinstance(sr, list):
        print(f'Total verses: {len(sr)}')
        # Show first 3
        for v in sr[:3]:
            print(f'  {json.dumps(v, ensure_ascii=False)[:300]}')
elif 'results' in d2:
    print(f'results: {len(d2["results"])} items')

# Show first 2000 chars of the raw response to understand structure
print('\n--- Raw start (2000 chars):')
print(r2.text[:2000])
