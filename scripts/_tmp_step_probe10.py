"""
Strategy: Since masterSearch caps at 60, use book-by-book restrictions OR
use getSubjectVerses / different endpoints to get all 89 verses.

Ecc 5:20 is verse #60 (last one returned). The remaining 29 start somewhere after Ecclesiastes.
Let's check: what comes canonically after Ecc? Song, Isa, Jer, ...

Let's try restriction to books after Ecc using OSIS range.
"""
import requests, json

base = 'http://localhost:8989'
strong = 'H8057'

def search(query, label=''):
    r = requests.get(f'{base}/rest/search/masterSearch/{query}', timeout=30)
    try:
        d = r.json()
        results = d.get('results', [])
        total = d.get('total')
        err = d.get('errorMessage')
        if err:
            print(f'  ERROR [{label}]: {err[:60]}')
            return []
        print(f'  OK [{label}]: total={total} n={len(results)} first={results[0]["key"] if results else "none"} last={results[-1]["key"] if results else "none"}')
        return results
    except Exception as e:
        print(f'  EXCEPT [{label}]: {e}')
        return []

# Restrict to different book ranges using context/scope
print('=== Book range restrictions ===')
# After Ecc 5:20 in the OT: Ecc 5:21+ through Mal would have 29 more
all_results = search(f'strong={strong}|version=ESV_th', 'all (baseline)')

# Try OSIS range restriction
for scope_fmt in [
    f'strong={strong}|version=ESV_th|range=Song.1.1-Mal.4.6',
    f'strong={strong}|version=ESV_th|scope=Song.1.1-Mal.4.6',
    f'strong={strong}|version=ESV_th|context=Song.1.1-Mal.4.6',
]:
    search(scope_fmt, scope_fmt[-30:])

# Try book filter
for bk in ['Song', 'Isa', 'Jer']:
    res = search(f'strong={strong}|version=ESV_th|reference={bk}.1.1-{bk}.100.100', f'ref={bk}')
    for r in res:
        print(f'    {r["key"]}')

# Check if there's a searchRestriction parameter 
r = requests.get(f'{base}/rest/search/masterSearch/strong={strong}|version=ESV_th', timeout=30)
d = r.json()
print(f'\nsearchRestriction: {d.get("searchRestriction")}')
print(f'searchTokens types: {[t.get("tokenType") for t in d.get("searchTokens", [])]}')

# Maybe we need to specify the Testament?
print('\n=== Testament/book filter ===')
for filt in [
    f'strong={strong}|version=ESV_th|testament=OT',
    f'strong={strong}|version=ESV_th|filter=OT',
]:
    r2 = requests.get(f'{base}/rest/search/masterSearch/{filt}', timeout=20)
    try:
        d2 = r2.json()
        n = len(d2.get('results', []))
        total = d2.get('total')
        print(f'  {filt}: total={total} n={n}')
    except:
        pass

# Try getSubjectVerses
print('\n=== getSubjectVerses / getExactForms ===')
for ep, label in [
    (f'/rest/search/getSubjectVerses/{strong}', 'getSubjectVerses'),
    (f'/rest/search/getSubjectVerses/strong={strong}', 'getSubjectVerses q-style'),
    (f'/rest/search/suggest/{strong}/ESV_th', 'suggest'),
]:
    r = requests.get(f'{base}{ep}', timeout=20)
    try:
        d = r.json()
        n = len(d.get('results', d) if isinstance(d, dict) else d)
        print(f'  {label}: {str(d)[:200]}')
    except Exception as e:
        print(f'  {label}: ERROR {e}')
