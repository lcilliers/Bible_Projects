"""Rename cluster-folder top-level files to canonical form.

Canonical: wa-cluster-{CODE}-{kind}-v{n}-{date}.{ext}

Transformations applied (only to the first 2-3 segments):
  1. WA-{CODE}-{kind}-...   →  wa-cluster-{CODE}-{kind}-...
  2. WA-{CODE}-{CODE}-{X}-...   →  wa-cluster-{CODE}-{X}-...   (doubled-prefix bug)
  3. wa-cluster-m{NN}-...   →  wa-cluster-M{NN}-...   (case fix on cluster code)

Inner content (segments 4+) preserved as-is to keep the rename minimum-invasive.

Files skipped:
  - Any file inside a subfolder (inputs/, published/, files published/, files phase N/, archive/, etc.)
  - wa-obslog-{CODE}-* files (special category, retained)
  - Files not starting with wa- or WA-

Usage:
  python scripts/_rename_cluster_files_to_canonical_20260521.py            # dry-run
  python scripts/_rename_cluster_files_to_canonical_20260521.py --execute  # perform renames
"""
import argparse
import hashlib
import json
import re
import sys
import io
from pathlib import Path
from datetime import datetime, timezone

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REPO = Path(__file__).resolve().parent.parent
CLUSTER_BASE = REPO / 'Sessions' / 'Session_Clusters'
OUT_MAP = REPO / 'docs' / 'cluster-rename-map-20260521.json'


def compute_target(name: str) -> str | None:
    """Return canonical name if rename needed, else None."""
    # Match: {wa|WA}-{M??}-... or wa-cluster-{m??}-...
    # Case 3: lowercase cluster code in wa-cluster prefix
    m = re.match(r'^(wa-cluster-)(m)(\d+)(.*)$', name)
    if m:
        return f'{m.group(1)}M{m.group(3)}{m.group(4)}'

    # Case 1+2: CAPS WA- prefix
    m = re.match(r'^WA-(M\d+)-(.*)$', name)
    if m:
        code = m.group(1)
        rest = m.group(2)
        # Case 2: doubled-prefix bug (WA-M07-M07-...)
        m2 = re.match(rf'^{code}-(.*)$', rest)
        if m2:
            rest = m2.group(1)
        return f'wa-cluster-{code}-{rest}'

    # No rename needed
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--execute', action='store_true',
                    help='Actually perform the renames (default: dry-run)')
    args = ap.parse_args()

    mode = 'EXECUTE' if args.execute else 'DRY-RUN'
    print(f'=== Cluster-folder file rename to canonical ({mode}) ===')
    print(f'Base: {CLUSTER_BASE.relative_to(REPO)}')
    print()

    rename_map = []  # list of (cluster_code, old_path_rel, new_path_rel, status)
    collisions = []  # (cluster_code, old_path_rel, new_path_rel) where target already exists

    for cluster_dir in sorted(CLUSTER_BASE.iterdir()):
        if not cluster_dir.is_dir():
            continue
        if not re.match(r'^M\d+$', cluster_dir.name):
            continue
        for f in sorted(cluster_dir.iterdir()):
            if not f.is_file():
                continue  # skip subfolders
            name = f.name
            # Skip wa-obslog (retained)
            if name.startswith('wa-obslog-'):
                continue
            # Skip files that don't start with wa-/WA-
            if not name.lower().startswith('wa-'):
                continue
            target = compute_target(name)
            if not target or target == name:
                continue
            old_rel = str(f.relative_to(REPO)).replace('\\', '/')
            new_path = f.with_name(target)
            new_rel = str(new_path.relative_to(REPO)).replace('\\', '/')
            if new_path.exists():
                # Compare contents — if identical, the lowercase variant is a stale duplicate
                # that should be deleted (the CAPS-code version is canonical).
                try:
                    old_hash = hashlib.md5(f.read_bytes()).hexdigest()
                    new_hash = hashlib.md5(new_path.read_bytes()).hexdigest()
                    if old_hash == new_hash:
                        # Delete the stale duplicate
                        collisions.append((cluster_dir.name, old_rel, new_rel))
                        rename_map.append((cluster_dir.name, old_rel, new_rel, 'DELETE_DUPLICATE'))
                    else:
                        collisions.append((cluster_dir.name, old_rel, new_rel))
                        rename_map.append((cluster_dir.name, old_rel, new_rel, 'COLLISION_DIFFERENT'))
                except Exception:
                    rename_map.append((cluster_dir.name, old_rel, new_rel, 'COLLISION_ERROR'))
                continue
            rename_map.append((cluster_dir.name, old_rel, new_rel, 'pending'))

    # Per-cluster summary
    by_cluster = {}
    for cc, old, new, status in rename_map:
        by_cluster.setdefault(cc, []).append((old, new, status))

    print(f'Renames identified: {len(rename_map)} (collisions: {len(collisions)})')
    print()
    print(f'Per-cluster breakdown:')
    for cc in sorted(by_cluster):
        items = by_cluster[cc]
        pending = sum(1 for _,_,s in items if s == 'pending')
        coll = sum(1 for _,_,s in items if s == 'COLLISION')
        print(f'  {cc}: {pending} renames' + (f' + {coll} COLLISIONS' if coll else ''))

    # Dump the map for review
    OUT_MAP.parent.mkdir(parents=True, exist_ok=True)
    map_payload = {
        '_meta': {
            'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'mode': mode,
            'total': len(rename_map),
            'collisions': len(collisions),
            'canonical': 'wa-cluster-{CODE}-{kind}-v{n}-{date}',
        },
        'renames': [
            {'cluster': cc, 'old': old, 'new': new, 'status': status}
            for cc, old, new, status in rename_map
        ],
    }
    OUT_MAP.write_text(json.dumps(map_payload, indent=2), encoding='utf-8')
    print(f'\nWrote rename map: {OUT_MAP.relative_to(REPO)}')

    if collisions:
        print()
        print('=== COLLISIONS (will skip) ===')
        for cc, old, new in collisions[:30]:
            print(f'  {old} → {new} (target exists)')
        if len(collisions) > 30:
            print(f'  ... and {len(collisions)-30} more')

    if not args.execute:
        print()
        print('Dry-run only. Re-run with --execute to perform the renames.')
        return

    # Execute
    print()
    print('=== EXECUTING ===')
    renamed = 0
    deleted = 0
    failed = 0
    skipped = 0
    for cc, old, new, status in rename_map:
        old_p = REPO / old
        new_p = REPO / new
        if status == 'pending':
            try:
                old_p.rename(new_p)
                renamed += 1
            except Exception as e:
                print(f'  FAIL rename {old} → {new}: {e}')
                failed += 1
        elif status == 'DELETE_DUPLICATE':
            try:
                old_p.unlink()
                deleted += 1
            except Exception as e:
                print(f'  FAIL delete-dup {old}: {e}')
                failed += 1
        else:
            skipped += 1
    print(f'Renamed:  {renamed}')
    print(f'Deleted (duplicates): {deleted}')
    print(f'Skipped (real collisions / errors): {skipped}')
    print(f'Failed:   {failed}')


if __name__ == '__main__':
    main()
