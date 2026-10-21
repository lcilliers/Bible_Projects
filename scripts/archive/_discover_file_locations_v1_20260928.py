"""Read-only inventory of study files across locations (file-location inventory, step 1).

Walks each root, fingerprints every file (sha256; size-only above HASH_LIMIT) and writes:
  research/investigations/file-location-inventory-v1-20260928.csv  (one row per file)
  research/investigations/file-location-inventory-v1-20260928-data.json  (summary figures for the .md)
Nothing is moved, renamed or deleted.
"""
import csv, hashlib, json, os, sys, collections, datetime

AUTH = r'C:\Bible_study_projects'
ROOTS = {
    'AUTH': AUTH,
    'G_OLD': r'G:\My Drive\Bible_study_projects',
    'G_CLAUDE': r'G:\My Drive\Claude_Research',
    'G_SHARE': r'G:\My Drive\BibleStudyShare',
    'G_DOCS': r'G:\My Drive\Documents',
    'ZOTERO': os.path.expandvars(r'%USERPROFILE%\Zotero\storage'),
    'DOCS': os.path.expandvars(r'%USERPROFILE%\Documents'),
    'DESKTOP': os.path.expandvars(r'%USERPROFILE%\Desktop'),
}
SKIP_DIRS = {'.git', '.venv', 'venv', 'node_modules', '__pycache__', '.pytest_cache', '.mypy_cache'}
HASH_LIMIT = 300 * 1024 * 1024
OUT = os.path.join(AUTH, 'research', 'investigations')
STAMP = 'file-location-inventory-v1-20260928'


def sha(path, size):
    if size > HASH_LIMIT:
        return f'size:{size}'
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


rows = []
for key, root in ROOTS.items():
    if not os.path.isdir(root):
        print(f'{key}: missing {root}')
        continue
    n = 0
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for fn in files:
            p = os.path.join(d, fn)
            try:
                st = os.stat(p)
                h = sha(p, st.st_size)
            except OSError as e:
                h = f'error:{e.__class__.__name__}'
                st = None
            rows.append({
                'root': key, 'path': p, 'rel': os.path.relpath(p, root), 'name': fn,
                'ext': os.path.splitext(fn)[1].lower(),
                'size': st.st_size if st else '',
                'mtime': datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M') if st else '',
                'sha256': h,
            })
            n += 1
    print(f'{key}: {n} files')

# duplicate status per file
by_hash = collections.defaultdict(set)
by_name = collections.defaultdict(set)
for r in rows:
    by_hash[r['sha256']].add(r['root'])
    by_name[r['name'].lower()].add(r['root'])
for r in rows:
    hr = by_hash[r['sha256']]
    if r['sha256'].startswith('error'):
        s = 'READ_ERROR'
    elif 'AUTH' in hr and r['root'] != 'AUTH':
        s = 'DUP_OF_AUTH'
    elif 'ZOTERO' in hr and r['root'] != 'ZOTERO':
        s = 'DUP_OF_ZOTERO'
    elif r['root'] in ('AUTH', 'ZOTERO'):
        s = 'IN_' + r['root']
    elif 'AUTH' in by_name[r['name'].lower()] or 'ZOTERO' in by_name[r['name'].lower()]:
        s = 'SAME_NAME_DIFFERENT_CONTENT'
    else:
        s = 'UNIQUE_HERE'
    r['status'] = s

with open(os.path.join(OUT, STAMP + '.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=['root', 'status', 'rel', 'name', 'ext', 'size', 'mtime', 'sha256', 'path'])
    w.writeheader()
    w.writerows(sorted(rows, key=lambda r: (r['root'], r['status'], r['rel'])))

summary = collections.defaultdict(lambda: collections.Counter())
sizes = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    summary[r['root']][r['status']] += 1
    sizes[r['root']][r['status']] += r['size'] or 0
json.dump({'summary': summary, 'sizes': sizes, 'roots': ROOTS}, open(os.path.join(OUT, STAMP + '-data.json'), 'w'), indent=1, default=dict)
for k in summary:
    print(k, dict(summary[k]))
