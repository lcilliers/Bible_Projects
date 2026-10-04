"""narrativecopy.py — copy the current inner-being narrative files to the learning4comfort inbox.

Escalation #1941 (researcher, 2026-10-04): "A) this project (bible_study_projects) does not publish
directly to github b) on completion of a section of work or on request, the current
...inner-being-narrative files are copied to C:\\learning4comfort\\publication-inbox\\... c)
session-close trigger the copy in b)". Inbox folder: the_inner_being (researcher, same day).

What it does:
- Source = cfg_setting narrative.copy_source_dir. Only the TOP-LEVEL .md files are copied
  (the current version of each chapter, plus the index). The archive/ subfolder is never copied.
- Target = cfg_setting narrative.learning4comfort_inbox_dir (created if missing; local-only
  staging in the learning4comfort repo, which owns preparation and publishing).
- In the target, an .md file whose base name (without -vN-YYYYMMDD) matches a current source file
  but whose name differs is an earlier version of that file: it is removed, then replaced.
  Every other file in the target is left untouched.
- A file already present with identical content is left as is ("unchanged").
- Never runs git, in either repository.

Usage (from the repo root):
  python -m iba.app.lib.narrativecopy [--dry-run] [--source DIR --target DIR]
--source/--target override the config, for testing only.
"""
import argparse, hashlib, os, re, shutil, sys

_VERSIONED = re.compile(r'^(?P<base>.+)-v\d+-\d{8}\.md$')


def base_name(fname: str) -> str:
    m = _VERSIONED.match(fname)
    return m.group('base') if m else fname[:-3] if fname.endswith('.md') else fname


def _hash(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def plan(source: str, target: str):
    """Return (copy, unchanged, remove, untouched) lists of file names."""
    current = sorted(f for f in os.listdir(source)
                     if f.endswith('.md') and os.path.isfile(os.path.join(source, f)))
    cur_by_base = {base_name(f): f for f in current}
    existing = sorted(f for f in os.listdir(target)
                      if os.path.isfile(os.path.join(target, f))) if os.path.isdir(target) else []
    remove = [f for f in existing
              if f.endswith('.md') and base_name(f) in cur_by_base and cur_by_base[base_name(f)] != f]
    copy, unchanged = [], []
    for f in current:
        t = os.path.join(target, f)
        if os.path.isfile(t) and _hash(t) == _hash(os.path.join(source, f)):
            unchanged.append(f)
        else:
            copy.append(f)
    untouched = [f for f in existing if f not in remove and f not in current]
    return current, copy, unchanged, remove, untouched


def run(source: str, target: str, dry_run: bool) -> int:
    if not os.path.isdir(source):
        print(f'ERROR: source folder not found: {source}')
        return 1
    current, copy, unchanged, remove, untouched = plan(source, target)
    mode = 'DRY RUN (nothing written)' if dry_run else 'COPY'
    print(f'narrative copy — {mode}')
    print(f'  source : {source}  ({len(current)} current files)')
    print(f'  target : {target}')
    if not dry_run:
        os.makedirs(target, exist_ok=True)
        for f in remove:
            os.remove(os.path.join(target, f))
        for f in copy:
            shutil.copy2(os.path.join(source, f), os.path.join(target, f))
        bad = [f for f in current if _hash(os.path.join(source, f)) != _hash(os.path.join(target, f))]
        if bad:
            print(f'ERROR: content check failed for {bad}')
            return 1
    print(f'  copied (new or changed) : {len(copy)}' + ('' if not copy else '  ' + ', '.join(copy)))
    print(f'  unchanged               : {len(unchanged)}')
    print(f'  earlier versions removed: {len(remove)}' + ('' if not remove else '  ' + ', '.join(remove)))
    print(f'  other files left as is  : {len(untouched)}' + ('' if not untouched else '  ' + ', '.join(untouched)))
    if not dry_run:
        print(f'  verified: all {len(current)} current files in the target match the source')
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--source')
    ap.add_argument('--target')
    a = ap.parse_args(argv)
    if a.source and a.target:
        source, target = a.source, a.target
    else:
        from iba.app.lib.cfg import Cfg
        cfg = Cfg()
        source = cfg.required_setting('narrative.copy_source_dir')
        target = cfg.required_setting('narrative.learning4comfort_inbox_dir')
    return run(source, target, a.dry_run)


if __name__ == '__main__':
    sys.exit(main())
