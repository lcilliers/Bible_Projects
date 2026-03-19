import requests, re

base = 'http://localhost:8989'

# Fetch the main JS bundle and grep for rest/ API patterns
r = requests.get(f'{base}/js/step.26.1.2.min.js', timeout=30)
print(f'JS bundle status: {r.status_code}, size: {len(r.text):,} chars')

js = r.text

# Find all rest/ URL patterns
patterns = re.findall(r'["\`](?:\.\./)?(rest/[^"\'`\s]{5,})["\`]', js)
print(f'\nFound {len(patterns)} rest/ patterns:')
for p in sorted(set(patterns))[:60]:
    print(f'  {p}')

# Also look for "definitions" and "search" context
print('\n--- search context ---')
idx = js.find('definitions/')
if idx > 0:
    print(js[idx-100:idx+200])
