"""Proverbs Stage-1 onboarding (registry path) — the 30 candidate terms absent from
`mti_terms` (worklist: verse-analysis/proverbs/_reread/wa-proverbs-stage1-onboarding-worklist-v1).

COMPLIANT: reuses `process_registry` from `_run_gate1_onboard_batch_v1` — the
`word_study_extract --anchors` -> curate -> `audit_word --add-terms` -> stamp ->
verse_context path. It does NOT hand-write mti_terms / wa_verse_records; every term
and verse addition goes through `audit_word` (per wa-term-add-update-AUTHORITATIVE-
pipeline-v1, 2026-07-12 amendment). Requires the STEP server up (http://localhost:8989).

Usage:
  python scripts/_run_proverbs_stage1_onboard_v1_20260712.py --list
  python scripts/_run_proverbs_stage1_onboard_v1_20260712.py --dry-curate [--registries strife,contempt]
  python scripts/_run_proverbs_stage1_onboard_v1_20260712.py --live       [--registries strife]
Default (no --live) = dry-curate (no DB writes). Idempotent (skips already-stamped terms).
"""
import sys, os, argparse, importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
g1 = importlib.import_module('_run_gate1_onboard_batch_v1_20260706')

# strong -> (registry_word, cluster). Cluster deferred (None) — set post-read; the
# registry association is the point at this stage. From the Stage-1 worklist.
WORK = {
    'H0159': ('love', None),       'H0404': ('desire', None),
    'H0936': ('contempt', None),   'H4426': ('contempt', None),  'H3944': ('contempt', None),
    'H1566': ('strife', None),     'H4079': ('strife', None),    'H4090': ('strife', None),
    'H5916': ('strife', None),
    'H2054': ('guilt', None),
    'H2134': ('purity', None),     'H6337': ('purity', None),
    'H2502': ('salvation', None),
    'H2904': ('rejection', None),
    'H3093': ('pride', None),
    'H3832': ('corruption', None), 'H4072': ('corruption', None), 'H7703': ('corruption', None),
    'H3994': ('cursing', None),    'H6895': ('cursing', None),
    'H4860': ('deceit', None),
    'H5889': ('weakness', None),
    'H7189': ('worship', None),
    'H7390': ('compassion', None),
    'H7456': ('appetite', None),
    'H4878': ('rebellion', None),
    'H8367': ('peace', None),      'H4832': ('peace', None),      'H7500': ('peace', None),
    'H3856': ('despair', None),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--registries')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--dry-curate', action='store_true')
    ap.add_argument('--live', action='store_true')
    a = ap.parse_args()

    byreg = {}
    for strong, (rw, cl) in WORK.items():
        byreg.setdefault(rw, []).append((strong, cl))

    if a.list:
        for rw in sorted(byreg):
            print(f"  {rw:12} {[s for s, _ in byreg[rw]]}")
        print(f"total: {len(WORK)} terms, {len(byreg)} registries")
        return

    sel = set(byreg)
    if a.registries:
        sel = {x.strip().lower() for x in a.registries.split(',')}
    todo = sorted(rw for rw in byreg if rw.lower() in {s.lower() for s in sel})

    dry = not a.live or a.dry_curate
    print(f"{'DRY-CURATE (no DB writes)' if dry else 'LIVE (audit_word)'}: {len(todo)} registries: {todo}")
    done = fail = 0
    for rw in todo:
        res = g1.process_registry(rw, byreg[rw], dry_curate=dry)
        ok = res['status'] in ('DONE', 'DRY_CURATE', 'ALREADY_DONE')
        done += ok
        fail += (not ok)
        flag = '' if ok else '  <-- CHECK'
        print(f"  [{res['status']:12}] {rw:12} kept={res.get('kept')} "
              f"unresolved={res.get('unresolved')} vr={res.get('verse_records','-')}{flag}")
    print(f"\n{done} ok, {fail} need attention.")


if __name__ == '__main__':
    main()
