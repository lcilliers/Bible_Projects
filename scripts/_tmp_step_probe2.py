"""Phase 2 STEP probe: browser headers + log/install discovery + JS template-literal scan."""
import requests, re, json, os, glob

base = 'http://localhost:8989'

# ── Test 1: Browser-like headers ──────────────────────────────────────────────
print('=== Test 1: Browser headers ===')
browser_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'http://localhost:8989/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120',
    'X-Requested-With': 'XMLHttpRequest',
}
for ep in [
    '/rest/definitions/definitions=H8057|version=ESV_th',
    '/rest/search/searchAllPassages/strong=H8057|version=ESV_th',
]:
    r = requests.get(f'{base}{ep}', headers=browser_headers, timeout=15)
    body = r.text[:300].replace('\n', ' ')
    print(f'{r.status_code}  {ep}')
    print(f'  {body}')

# ── Test 2: Scan JS bundle for template-literal rest URLs ─────────────────────
print('\n=== Test 2: JS bundle — template literal patterns ===')
rj = requests.get(f'{base}/js/step.26.1.2.min.js', timeout=30)
text = rj.text

# backtick segments
bt_patterns = re.findall(r'`(rest/[^`]{8,})`', text)
print(f'Backtick rest/ patterns: {len(bt_patterns)}')
for p in sorted(set(bt_patterns))[:60]:
    print(f'  {p}')

# also look for string concat patterns like "rest/" + something
concat = re.findall(r'"rest/([^"]{3,})"', text)
print(f'Double-quote rest/ segments: {len(concat)}')
for p in sorted(set(concat))[:40]:
    print(f'  rest/{p}')

# Also look for .get( or .post( calls with 'rest
http_calls = re.findall(r'\.(get|post|put)\(["\`]([^"\'`]{0,80})["\`]', text)
rest_calls = [(m,u) for m,u in http_calls if 'rest' in u.lower()]
print(f'\nHTTP calls with "rest": {len(rest_calls)}')
for m,u in rest_calls[:40]:
    print(f'  .{m}({u})')

# ── Test 3: Find STEP install dir and logs ────────────────────────────────────
print('\n=== Test 3: STEP install / Tomcat logs ===')
search_roots = [
    r'C:\Program Files\STEP Bible',
    r'C:\Program Files (x86)\STEP Bible',
    r'C:\STEP',
    r'C:\stepbible',
    os.path.expandvars(r'%LOCALAPPDATA%\STEP'),
    os.path.expandvars(r'%APPDATA%\STEP'),
    r'C:\Tomcat',
    r'C:\apache-tomcat*',
]
found_dirs = []
for root in search_roots:
    expanded = glob.glob(root)
    for d in expanded:
        if os.path.exists(d):
            found_dirs.append(d)
            print(f'  Found: {d}')

# Check common Tomcat log locations
log_locations = [
    r'C:\Program Files\STEP Bible\logs',
    r'C:\STEP\logs',
    r'C:\Tomcat\logs',
]
for loc in log_locations:
    if os.path.exists(loc):
        logs = os.listdir(loc)
        print(f'  Logs in {loc}: {logs[:10]}')
