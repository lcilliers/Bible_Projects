"""
Try to get the remaining 29 results using different pagination approaches.
Also inspect V1Controller for an external API that might give more.
"""
import requests, json, re, struct, os

base = 'http://localhost:8989'
strong = 'H8057'

# ── Attempt 1: paging tokens in different positions ──────────────────────────
print('=== Try different token positions for pagination ===')
for fmt in [
    f'strong={strong}|version=ESV_th|page=2',
    f'strong={strong}|version=ESV_th|start=60',
    f'strong={strong}|version=ESV_th|offset=60',
    f'version=ESV_th|strong={strong}|pageNumber=2',
]:
    r = requests.get(f'{base}/rest/search/masterSearch/{fmt}', timeout=20)
    try:
        d = r.json()
        results = d.get('results', [])
        total = d.get('total')
        pn = d.get('pageNumber')
        first = results[0]['key'] if results else 'none'
        print(f'  {fmt[:60]} -> pn={pn} total={total} n={len(results)} first={first}')
    except Exception as e:
        print(f'  ERROR: {e}')

# ── Attempt 2: Use search endpoint with pagination as query params ────────────
print('\n=== Query-param pagination ===')
for params in [
    {'q': f'strong={strong}', 'version': 'ESV_th', 'pageNumber': 2},
    {'q': f'strong={strong}|version=ESV_th', 'pageNumber': 2},
]:
    r = requests.get(f'{base}/rest/search/search', params=params, timeout=20)
    try:
        d = r.json()
        n = len(d.get('results', []))
        print(f'  params={params} -> {n} results, error={d.get("errorMessage","none")}')
    except Exception as e:
        print(f'  ERROR: {e}')

# ── Attempt 3: Read V1Controller class for its URL path ──────────────────────
print('\n=== V1Controller class analysis ===')
v1_path = r"C:\Program Files (x86)\STEP\step-web\WEB-INF\classes\com\tyndalehouse\step\rest\controllers\external\V1Controller.class"

def read_utf8_strings(class_bytes):
    if class_bytes[:4] != b'\xca\xfe\xba\xbe':
        return []
    pos = 8
    constant_pool_count = struct.unpack('>H', class_bytes[pos:pos+2])[0]
    pos += 2
    strings = []
    i = 1
    while i < constant_pool_count:
        tag = class_bytes[pos]
        pos += 1
        if tag == 1:
            length = struct.unpack('>H', class_bytes[pos:pos+2])[0]
            pos += 2
            s = class_bytes[pos:pos+length].decode('utf-8', errors='replace')
            strings.append(s)
            pos += length
        elif tag in (7, 8, 16, 19, 20):
            pos += 2
        elif tag in (9, 10, 11, 12, 17, 18):
            pos += 4
        elif tag in (3, 4):
            pos += 4
        elif tag in (5, 6):
            pos += 8
            i += 1
        elif tag == 15:
            pos += 3
        else:
            break
        i += 1
    return strings

with open(v1_path, 'rb') as f:
    data = f.read()
strings = read_utf8_strings(data)
interesting = [s for s in strings if 2 < len(s) < 120 and '\n' not in s and not s.startswith('[') and not s.startswith('(')]
print('V1Controller strings:')
for s in interesting:
    print(f'  {repr(s)}')

# ── Attempt 4: Try V1Controller endpoints ────────────────────────────────────
print('\n=== V1Controller REST endpoints ===')
for ep in [
    f'/rest/search/masterSearch/strong={strong}|version=ESV_th|context=2',
    f'/rest/search/masterSearch/strong={strong}|version=ESV_th|sort=ASC',
    # Try alternative search methods from SearchController
]:
    r = requests.get(f'{base}{ep}', timeout=20)
    try:
        d = r.json()
        total = d.get('total')
        n = len(d.get('results', []))
        last = d['results'][-1]['key'] if d.get('results') else 'none'
        print(f'{ep[:60]} -> total={total} n={n} last={last}')
    except Exception as e:
        print(f'{ep}: ERROR {e}')
