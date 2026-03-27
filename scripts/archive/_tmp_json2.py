#!/usr/bin/env python3
import glob, os, json

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
disc_dir = os.path.join(_ROOT, "data", "discovery")
jfiles = sorted(glob.glob(os.path.join(disc_dir, "182_soul_step_data_*.json")))
jf = jfiles[-1]
print(f"JSON FILE: {os.path.basename(jf)}")
with open(jf, encoding="utf-8") as fh:
    j = json.load(fh)
print(f"anchors:      {j['meta']['anchor_codes']}")
print(f"generated:    {j['meta']['generated']}")
print(f"step_version: {j['meta']['step_version']}")
print(f"groups total: {j['meta']['total_terms_evaluated']}")
print(f"\ninclude_codes ({len(j['meta']['include_codes'])}):")
for c in j['meta']['include_codes']:
    print(f"  {c}")
print(f"\nexclude_codes ({len(j['meta']['exclude_codes'])}):")
for c in j['meta']['exclude_codes']:
    print(f"  {c}")
print(f"\nTotal terms[] records: {len(j['terms'])}")
print("\nSearching terms[] for H4578, H5397, G5590:")
found = [t for t in j["terms"] if t["code"] in ("H4578","H5397","G5590")]
print(f"  RESULT: {'FOUND '+str(len(found)) if found else 'NOT FOUND — completely absent from j[terms]'}")
print("\nAll terms in JSON:")
print(f"  {'CODE':<12}  {'GRP':<5}  {'ACTION':<9}  {'SECT_TYPE':<14}  GLOSS")
for t in j["terms"]:
    print(f"  {t['code']:<12}  {t['decision_group']:<5}  {t['action']:<9}  "
          f"{t['step_section_type']:<14}  {t.get('gloss','')[:35]}")
