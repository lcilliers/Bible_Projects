"""
Multi-purpose probe:
  1. Find >60 verse pagination by inspecting the JS bundle for the scroll-more mechanism
  2. Test non-canonical Strong's numbers (G9559, G9073, G6347)
  3. Test multi-gloss terms (ko.ach H3581, cha.yil H2428)
  4. Inspect a verse preview to understand the HTML structure
"""
import requests, json, re, struct

base = 'http://localhost:8989'

def search_master(query, label=''):
    r = requests.get(f'{base}/rest/search/masterSearch/{query}', timeout=30)
    d = r.json()
    err = d.get('errorMessage')
    results = d.get('results', [])
    total = d.get('total')
    print(f'\n  [{label}]  total={total}  n={len(results)}  err={err and err[:60]}')
    return d

def get_vocab(strong, label=''):
    r = requests.get(f'{base}/rest/module/getInfo/ESV_th//{strong}//', timeout=15)
    d = r.json()
    err = d.get('errorMessage')
    vocabs = d.get('vocabInfos', [])
    print(f'\n  [{label or strong}]  vocabs={len(vocabs)}  err={err and err[:60]}')
    for v in vocabs:
        print(f'    strong={v.get("strongNumber")}  gloss={v.get("stepGloss")}  count={v.get("count")}')
        print(f'    related: {v.get("rawRelatedNumbers")}')
        def_short = (v.get("mediumDef","") or "").replace("<br>"," | ")[:100]
        print(f'    def: {def_short}')
    return d

# ── 1. Pagination hunt in JS bundle ──────────────────────────────────────────
print('=== 1. JS pagination patterns ===')
rj = requests.get(f'{base}/js/step.26.1.2.min.js', timeout=30)
js = rj.text

# Search for "pageNumber" or "paginat" patterns near function calls
pn_contexts = [m.start() for m in re.finditer(r'pageNumber|paginat|loadMore|nextPage|scrollMore|appendResult', js, re.I)]
print(f'Hits for page/paginate/loadMore: {len(pn_contexts)}')
for pos in pn_contexts[:8]:
    snippet = js[max(0,pos-80):pos+120].replace('\n', ' ')
    print(f'  @{pos}: ...{snippet}...')

# Search for the search URL construction
url_build = [m.start() for m in re.finditer(r'masterSearch|searchAll|searchResult', js, re.I)]
print(f'\nmasterSearch/searchAll refs: {len(url_build)}')
for pos in url_build[:6]:
    snippet = js[max(0,pos-100):pos+150].replace('\n', ' ')
    print(f'  @{pos}: ...{snippet}...')

# ── 2. Non-canonical Strong's ─────────────────────────────────────────────────
print('\n\n=== 2. Non-canonical Strong\'s numbers ===')
for s in ['G9559', 'G9073', 'G6347', 'H9002', 'H9001']:
    get_vocab(s)
    search_master(f'strong={s}|version=ESV_th', s)

# ── 3. Multi-gloss terms ─────────────────────────────────────────────────────
print('\n\n=== 3. Multi-gloss terms ===')
for s, name in [('H3581', 'ko.ach'), ('H2428', 'cha.yil'), ('H5797', 'oz')]:
    get_vocab(s, name)

# ── 4. Parse a verse preview HTML ────────────────────────────────────────────
print('\n\n=== 4. Verse preview HTML structure ===')
r = requests.get(f'{base}/rest/search/masterSearch/strong=H8057|version=ESV_th', timeout=30)
d = r.json()
result = d['results'][0]
print(f'key: {result["key"]}   osisId: {result["osisId"]}')
html = result['preview']
print(f'Raw HTML ({len(html)} chars):')
print(html[:1200])
print('...')

# Strip to ESV text only
clean = re.sub(r'<[^>]+>', ' ', html)
clean = re.sub(r'\s+', ' ', clean).strip()
print(f'\nClean text: {clean[:300]}')

# Check if preview contains the strong-tagged word
strong_hits = re.findall(r"strong='([^']+)'[^>]*>([^<]+)<", html)
print(f'\nStrong-tagged words in preview:')
for s_num, word in strong_hits[:10]:
    print(f'  strong={s_num}  word={word}')
