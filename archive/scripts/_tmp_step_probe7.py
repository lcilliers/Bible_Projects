"""Parse full STEP verse data and determine pagination needed for H8057 (94 occurrences)."""
import requests, json, re
from html import unescape

base = 'http://localhost:8989'
strong = 'H8057'

# Get first page
r2 = requests.get(f'{base}/rest/search/masterSearch/strong={strong}|version=ESV_th', timeout=30)
d2 = r2.json()

print(f'total     : {d2.get("total")}')
print(f'pageSize  : {d2.get("pageSize")}')
print(f'pageNumber: {d2.get("pageNumber")}')
print(f'results   : {len(d2.get("results", []))}')

# Show full structure of a single result
result0 = d2['results'][0]
print(f'\nFirst result keys: {list(result0.keys())}')
print(f'key   : {result0["key"]}')
print(f'osisId: {result0["osisId"]}')

# Strip HTML tags from preview to get plain text
preview_html = result0['preview']
preview_text = re.sub(r'<[^>]+>', ' ', preview_html)
preview_text = re.sub(r'\s+', ' ', preview_text).strip()
print(f'preview (plain): {preview_text[:200]}')

# Check definitions key
defs = d2.get('definitions', {})
print(f'\ndefinitions type: {type(defs).__name__}')
if isinstance(defs, dict):
    print(f'  keys: {list(defs.keys())[:10]}')
    for k, v in list(defs.items())[:2]:
        print(f'  [{k}]: {json.dumps(v, ensure_ascii=False)[:200]}')

# Check strongHighlights
sh = d2.get('strongHighlights', {})
print(f'\nstrongHighlights type: {type(sh).__name__}')
if isinstance(sh, dict):
    print(f'  keys: {list(sh.keys())[:5]}')

# ── Gather ALL results (paginate) ─────────────────────────────────────────────
print('\n\n=== PAGINATION ===')
page_size = d2.get('pageSize', 60)
total = d2.get('total', 0)
print(f'Need {total} results, page_size={page_size}')

all_results = list(d2['results'])

page = 1
while len(all_results) < total and page < 10:
    r_p = requests.get(
        f'{base}/rest/search/masterSearch/strong={strong}|version=ESV_th|pageNumber={page}|pageSize={page_size}',
        timeout=30
    )
    try:
        d_p = r_p.json()
    except:
        print(f'Page {page}: parse error')
        break
    new_results = d_p.get('results', [])
    if not new_results:
        print(f'Page {page}: empty results')
        break
    print(f'Page {page}: got {len(new_results)} more results (total so far: {len(all_results)+len(new_results)})')
    all_results.extend(new_results)
    page += 1

print(f'\nTotal results gathered: {len(all_results)}')

# ── Show all verse references ────────────────────────────────────────────────
print('\n=== All verse references for H8057 ===')
for i, r in enumerate(all_results):
    print(f'  {i+1:3d}. {r["key"]:25s}  ({r["osisId"]})')
