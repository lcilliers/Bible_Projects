"""Fix pagination and get all 89 verses for H8057.
Pagination: try pageNumber=2 (1-based? 0-based?)
"""
import requests, json, re

base = 'http://localhost:8989'
strong = 'H8057'

def get_page(page_num, page_size=60):
    """page_num: 0-based or 1-based? Try both."""
    url = f'{base}/rest/search/masterSearch/strong={strong}|version=ESV_th|pageNumber={page_num}|pageSize={page_size}'
    r = requests.get(url, timeout=30)
    d = r.json()
    total = d.get('total')
    pn = d.get('pageNumber')
    results = d.get('results', [])
    print(f'  pageNumber={page_num} -> server_pageNumber={pn}, total={total}, results={len(results)}, first={results[0]["key"] if results else "none"}, last={results[-1]["key"] if results else "none"}')
    return d

print('=== Testing pageNumber values ===')
for pn in [0, 1, 2, 3]:
    get_page(pn)

print('\n=== Testing pageSize smaller ===')
url = f'{base}/rest/search/masterSearch/strong={strong}|version=ESV_th|pageSize=100'
r = requests.get(url, timeout=30)
d = r.json()
print(f'pageSize=100: total={d.get("total")}, results={len(d.get("results",[]))}, pageNumber={d.get("pageNumber")}')

print('\n=== Just get everything with pageSize=200 ===')
url = f'{base}/rest/search/masterSearch/strong={strong}|version=ESV_th|pageSize=200'
r = requests.get(url, timeout=30)
d = r.json()
results = d.get('results', [])
print(f'pageSize=200: total={d.get("total")}, results={len(results)}')
for i, rv in enumerate(results):
    print(f'  {i+1:3d}. {rv["key"]:25s}  ({rv["osisId"]})')
