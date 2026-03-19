import requests, re, json, sys

base = 'http://localhost:8989'

# ── Phase 1: grab JS bundle and find all rest/ URL templates ──────────────────
print('=== Phase 1: REST patterns in JS bundle ===')
js_url = f'{base}/js/step.26.1.2.min.js'
rj = requests.get(js_url, timeout=30)
print(f'JS bundle: {rj.status_code}, {len(rj.text):,} chars')

patterns = re.findall(r'"(rest/[^"]{8,})"', rj.text)
unique = sorted(set(patterns))
print(f'Unique rest/ patterns: {len(unique)}')
for p in unique[:80]:
    print(f'  {p}')

# ── Phase 2: probe specific endpoints and dump full body ──────────────────────
print('\n=== Phase 2: Endpoint response bodies ===')
strong = 'H8057'
version = 'ESV_th'

tests = [
    f'/rest/definitions/definitions={strong}|version={version}',
    f'/rest/definitions/definitions={strong}',
    f'/rest/vocabs/getDefinition?strong={strong}',
    f'/rest/search/searchAllPassages/strong={strong}|version={version}',
    f'/rest/search/strong={strong}|version={version}',
    f'/rest/search?q=strong%3A{strong}&version=ESV',
    f'/rest/passage/find?q={strong}&version=ESV',
    f'/rest/word?strong={strong}',
    f'/rest/lexicon/{strong}',
    f'/rest/analysis?strong={strong}',
]
for ep in tests:
    try:
        rr = requests.get(f'{base}{ep}', timeout=15)
        body = rr.text[:600].strip()
        print(f'\n--- {ep}')
        print(f'    Status: {rr.status_code}  Content-Type: {rr.headers.get("Content-Type","?")}')
        print(f'    Body preview: {body[:400]}')
    except Exception as e:
        print(f'\n--- {ep}  ERROR: {e}')

