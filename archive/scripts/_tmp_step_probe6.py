"""Parse the full masterSearch response structure and deduce a STEP extractor."""
import requests, json, re
from html import unescape

base = 'http://localhost:8989'
strong = 'H8057'

# ── 1. Get full vocab info ──────────────────────────────────────────────────
r1 = requests.get(f'{base}/rest/module/getInfo/ESV_th//{strong}//', timeout=15)
d1 = r1.json()
vocab = d1['vocabInfos'][0]

print('=== VOCAB INFO ===')
print(f'strongNumber       : {vocab["strongNumber"]}')
print(f'accentedUnicode    : {vocab["accentedUnicode"]}')
print(f'stepGloss          : {vocab["stepGloss"]}')
print(f'stepTransliteration: {vocab["stepTransliteration"]}')
print(f'count              : {vocab["count"]}')
print(f'mediumDef          : {vocab["mediumDef"]}')
print(f'rawRelatedNumbers  : {vocab["rawRelatedNumbers"]}')
print(f'relatedNos ({len(vocab["relatedNos"])}):')
for r in vocab['relatedNos']:
    print(f'  {r["strongNumber"]}  {r.get("matchingForm","")}  "{r.get("gloss","")}"  ({r.get("stepTransliteration","")})')

# ── 2. Get full masterSearch and parse verses ─────────────────────────────────
print('\n\n=== SEARCH RESULTS ===')
r2 = requests.get(f'{base}/rest/search/masterSearch/strong={strong}|version=ESV_th', timeout=30)
d2 = r2.json()

print(f'searchType  : {d2.get("searchType")}')
print(f'Total chars : {len(r2.text)}')
print('All top-level keys:', list(d2.keys()))

# The value field is HTML - let's look at what other keys might have verse list
for k in d2.keys():
    v = d2[k]
    if isinstance(v, list) and len(v) > 5:
        print(f'\nKey [{k}]: list of {len(v)} items, first:')
        print(f'  {json.dumps(v[0], ensure_ascii=False)[:200]}')
    elif isinstance(v, dict):
        print(f'\nKey [{k}]: dict with keys {list(v.keys())[:6]}')
    elif isinstance(v, str) and len(v) > 100:
        print(f'\nKey [{k}]: str ({len(v)} chars), starts: {v[:100]}')

# The 'value' key is likely the HTML with all verse data
value = d2.get('value', '')
print(f'\n--- value field ({len(value)} chars):')
# Extract verse refs from the HTML
# STEP HTML: <span class="verse ..."><a name="Gen.8.8">...</a>...verse text
verse_anchors = re.findall(r'<a name=["\']([A-Z][a-z]+\.\d+\.\d+)["\']', value)
print(f'Verse anchors found: {len(verse_anchors)}')
print('First 20:', verse_anchors[:20])

# Extract "osisId" or similar from value
osisids = re.findall(r'osisId["\']?\s*[:=]\s*["\']([^"\']+)', value)  
print(f'osisIds in value: {osisids[:10]}')

# Also look at reference field
print(f'\nreference : {d2.get("reference", "N/A")}')
print(f'osisId    : {d2.get("osisId", "N/A")}')
print(f'fragment  : {str(d2.get("fragment",""))[:100]}')
print(f'multipleRanges: {d2.get("multipleRanges")}')
print(f'startRange: {d2.get("startRange")}')
print(f'endRange  : {d2.get("endRange")}')
