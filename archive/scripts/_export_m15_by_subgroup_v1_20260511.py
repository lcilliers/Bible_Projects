"""_export_m15_by_subgroup_v1_20260511.py — read-only export.

Derivative JSON organised per sub-group, for AI evaluation in SG phases.

Schema per verse (deliberately lean):
  vr_id · reference · verse_text · strongs · translit · gloss · meaning

Schema per sub-group:
  code · label · description · verse_count · verses[]

Resolution rule for which sub-group a verse belongs to:
  effective_subgroup = new_subgroup.code if present else current.subgroup_code

Excluded by design:
  - any current or new VCG code or description
  - review_status, review_flags
  - meaning source / version metadata
  - dual-vc duplicate-row markers (kept as-is — same vr_id appears twice
    in its sub-group if the DB has two active vc rows for it)

Reads:  m15-baseline-verses-v7-20260511.json
Writes: m15-by-subgroup-v1-20260511.json
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
IN_PATH = os.path.join(M15_DIR, "m15-baseline-verses-v7-20260511.json")
OUT_PATH = os.path.join(M15_DIR, "m15-by-subgroup-v1-20260511.json")

SG_ORDER = ["M15-A", "M15-B", "M15-C", "M15-D", "M15-E", "M15-F", "M15-G",
            "M15-H", "BOUNDARY"]

# Canonical book order for verse sorting within each (sub-group × term)
BOOK_ORDER = [
    "Gen", "Exo", "Lev", "Num", "Deu",
    "Jos", "Judg", "Rut", "1Sa", "2Sa", "1Ki", "2Ki", "1Ch", "2Ch",
    "Ezr", "Neh", "Est", "Job", "Psa", "Pro", "Ecc", "Song",
    "Isa", "Jer", "Lam", "Eze", "Dan", "Hos", "Joel", "Amo", "Oba",
    "Jon", "Mic", "Nah", "Hab", "Zep", "Hag", "Zec", "Mal",
    "Mat", "Mar", "Luk", "Joh", "Act",
    "Rom", "1Cor", "2Cor", "Gal", "Eph", "Phili", "Col",
    "1Th", "2Th", "1Ti", "2Ti", "Tit", "Phlm", "Heb",
    "Jam", "1Pe", "2Pe", "1Jo", "2Jo", "3Jo", "Jud", "Rev",
]
BOOK_INDEX = {b: i for i, b in enumerate(BOOK_ORDER)}
REF_RE = re.compile(r"^([A-Za-z0-9]+)\s+(\d+):(\d+)")


def ref_sort_key(ref: str) -> tuple:
    m = REF_RE.match(ref or "")
    if not m:
        return (99, 99, 99)
    book, ch, vs = m.group(1), int(m.group(2)), int(m.group(3))
    return (BOOK_INDEX.get(book, 99), ch, vs)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(IN_PATH, "r", encoding="utf-8") as f:
        d = json.load(f)

    # Resolve sub-group label/description from the JSON's sub-group rows
    # (current.subgroup_* fields per verse give them) + new_subgroup_proposed
    sg_meta: dict[str, dict] = {}
    proposed = d["metadata"].get("new_subgroup_proposed")
    if proposed:
        sg_meta[proposed["code"]] = {
            "code": proposed["code"],
            "label": proposed["label"],
            "description": proposed["description"],
            "db_state": proposed.get("db_state"),
        }
    # Glean the rest from per-verse current.subgroup_* fields
    for v in d["verses"]:
        cur = v.get("current") or {}
        code = cur.get("subgroup_code")
        if code and code not in sg_meta:
            sg_meta[code] = {
                "code": code,
                "label": cur.get("subgroup_label"),
                "description": cur.get("subgroup_description"),
                "db_state": "in cluster_subgroup",
            }
        new_sg = v.get("new_subgroup") or {}
        ncode = new_sg.get("code")
        if ncode and ncode not in sg_meta:
            sg_meta[ncode] = {
                "code": ncode,
                "label": new_sg.get("label"),
                "description": new_sg.get("description"),
                "db_state": "proposed",
            }

    # Group verses by effective sub-group
    grouped: dict[str, list] = defaultdict(list)
    no_sg = 0
    for v in d["verses"]:
        new_sg = (v.get("new_subgroup") or {}).get("code")
        cur_sg = (v.get("current") or {}).get("subgroup_code")
        effective = new_sg or cur_sg
        if not effective:
            no_sg += 1
            effective = "(unrouted)"
        t = v["term"]
        slim = {
            "vr_id": v["vr_id"],
            "reference": v["reference"],
            "verse_text": (v.get("verse_text") or "").strip(),
            "strongs": t["strongs"],
            "translit": t["translit"],
            "gloss": t.get("gloss"),
            "meaning": (v.get("meaning") or {}).get("text"),
        }
        grouped[effective].append(slim)

    # Sort verses within each sub-group: by Strong's then canonical ref order
    for code in grouped:
        grouped[code].sort(key=lambda r: (r["strongs"], ref_sort_key(r["reference"])))

    # Build ordered output
    sgs_out = []
    seen = set()
    for code in SG_ORDER:
        if code in grouped:
            meta = sg_meta.get(code, {"code": code})
            sgs_out.append({
                "code": code,
                "label": meta.get("label"),
                "description": meta.get("description"),
                "db_state": meta.get("db_state"),
                "verse_count": len(grouped[code]),
                "verses": grouped[code],
            })
            seen.add(code)
    # Catch anything not in canonical order
    for code in sorted(grouped):
        if code in seen:
            continue
        meta = sg_meta.get(code, {"code": code})
        sgs_out.append({
            "code": code,
            "label": meta.get("label"),
            "description": meta.get("description"),
            "db_state": meta.get("db_state"),
            "verse_count": len(grouped[code]),
            "verses": grouped[code],
        })

    out = {
        "metadata": {
            "cluster_code": "M15",
            "generated_at": now_iso(),
            "source": os.path.relpath(IN_PATH, ROOT).replace("\\", "/"),
            "purpose": (
                "Per-sub-group view for AI evaluation in SG phases. "
                "Each sub-group carries its label + description and the "
                "lean per-verse rows (vr_id, reference, verse_text, "
                "strongs, translit, gloss, meaning). No VCG context, no "
                "review status — the input is the verses + the SG frame, "
                "and the question is whether the verses fit the SG."
            ),
            "effective_subgroup_rule": (
                "new_subgroup.code if present else current.subgroup_code; "
                "unrouted verses surface under '(unrouted)'."
            ),
            "subgroup_count": len(sgs_out),
            "row_count": sum(s["verse_count"] for s in sgs_out),
            "rows_without_effective_subgroup": no_sg,
        },
        "subgroups": sgs_out,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("Sub-group summary:")
    for s in sgs_out:
        print(f"  {s['code']:14s}  {s['verse_count']:>4d}  {s.get('label') or ''}")
    print(f"  TOTAL:        {sum(s['verse_count'] for s in sgs_out):>4d}")
    print()
    print(f"Written: {OUT_PATH}")
    print(f"Size: {os.path.getsize(OUT_PATH):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
