"""
Test the JS-discovered URL format with positional path args:
  masterSearch/<query>/HNVUG//////en?lang=en
and book-range restriction for >60 pagination.
"""
import requests, json

base = 'http://localhost:8989'
strong = 'H8057'

def s(url, label=''):
    r = requests.get(f'{base}{url}', timeout=30)
    try:
        d = r.json()
        err = d.get('errorMessage')
        res = d.get('results', [])
        total = d.get('total')
        first = res[0]['key'] if res else 'none'
        last = res[-1]['key'] if res else 'none'
        pn = d.get('pageNumber')
        print(f'  {"ERR" if err else "OK "}  [{label[:50]}]  total={total}  n={len(res)}  pn={pn}  first={first}  last={last}')
        if err:
            print(f'       err: {err[:80]}')
        return d
    except Exception as e:
        print(f'  FAIL [{label}]: {e}: {r.text[:100]}')
        return {}

# ── 1. JS URL format with HNVUG positional args ─────────────────────────────
print('=== 1. JS positional arg format ===')
s(f'/rest/search/masterSearch/strong={strong}|version=ESV_th/HNVUG//////en', 'HNVUG suffix')
s(f'/rest/search/masterSearch/strong={strong}|version=ESV_th/HNVUG//////en?lang=en', 'HNVUG+lang')
s(f'/rest/search/masterSearch/version=ESV_th|strong={strong}/HNVUG//////en', 'version first HNVUG')

# ── 2. Positional arg offsets (7 slashes -> 8 positions) ─────────────────────
# Format: query / options / ??? / ??? / ??? / ??? / pageNumber / pageSize / lang
print('\n=== 2. Page number as positional arg ===')
# Try putting pageNumber in each of the 7 positions after HNVUG
for pos_vals in [
    ('HNVUG', '',   '', '', '', '2', '', 'en'),   # pos6=pageNum
    ('HNVUG', '',   '', '', '2', '', '', 'en'),   # pos5=pageNum
    ('HNVUG', '2',  '', '', '',  '', '', 'en'),   # pos2=pageNum
    ('HNVUG', '',   '', '2', '', '', '', 'en'),   # pos4=pageNum
]:
    path = '/'.join(pos_vals)
    url = f'/rest/search/masterSearch/strong={strong}|version=ESV_th/{path}'
    s(url, f'pos={pos_vals}')

# ── 3. Book-range restriction to get pages 2+ ────────────────────────────────
# H8057 first 60 end at Ecc 5:20. Remaining should be from Song onwards.
print('\n=== 3. Book-range restriction pagination ===')

# First verify what books we're missing by checking a range
ranges = [
    ('Song.1.1-Mal.4.6', 'Song-Mal'),
    ('Ecc.1.1-Ecc.12.14', 'Ecc only'),
    ('Pro.1.1-Song.9.9', 'Pro-Song'),
    ('Isa.1.1-Mal.4.6', 'Isa-Mal'),
    ('Isa.1.1-Jer.52.34', 'Isa-Jer'),
    ('Ezek.1.1-Mal.4.6', 'Ezek-Mal'),
]
for ref_range, label in ranges:
    url = f'/rest/search/masterSearch/strong={strong}|version=ESV_th|reference={ref_range}'
    s(url, label)

# ── 4. Verify full coverage with two-part split ──────────────────────────────
print('\n=== 4. Two-pass full coverage test ===')
d1 = s(f'/rest/search/masterSearch/strong={strong}|version=ESV_th|reference=Gen.1.1-Ecc.12.14', 'OT first half')
d2 = s(f'/rest/search/masterSearch/strong={strong}|version=ESV_th|reference=Song.1.1-Mal.4.6', 'OT second half')
d3 = s(f'/rest/search/masterSearch/strong={strong}|version=ESV_th|reference=Matt.1.1-Rev.22.21', 'NT')

r1 = d1.get('results', [])
r2 = d2.get('results', [])
r3 = d3.get('results', [])
all_ids = set(r['osisId'] for r in r1+r2+r3)
print(f'\n  Combined unique verses: {len(all_ids)} (expected ~89)')
for x in sorted(all_ids)[-15:]:
    print(f'    {x}')
