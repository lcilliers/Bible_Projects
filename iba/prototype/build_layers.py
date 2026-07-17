"""build_layers.py — the STEP pull as SEARCH LAYERS, one table per layer.

PROTOTYPE. Each layer is exactly one kind of STEP call, and the table is exactly what
that call returned. Nothing is interpreted, nothing is dropped, nothing is renamed.

    layer 1   word   -> strong      masterSearch  version=<v>|meanings=<word>
    layer 2   strong -> detail      module.getInfo/<v>//<strong>//

Repeating groups inside a response become their own table with an FK, because a
repeating group is not a column. Nothing else is changed.

Every field STEP returned is kept, including the ones the study does not use — the
point is to see what is on offer, not what we chose.

Usage:
    python iba/prototype/build_layers.py --word hypocrisy
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

import requests

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "analytics"))

from analytics.step_client import StepClient  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--word", required=True)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    c = StepClient()
    c.preflight()
    out = pathlib.Path(a.out) if a.out else (ROOT / "iba" / "prototype" / "layers" / a.word)
    out.mkdir(parents=True, exist_ok=True)

    def get(path):
        return requests.get(f"{c.base}/{path}", timeout=c.timeout).json()

    # ── LAYER 1 — word -> strong ────────────────────────────────────────────
    route1 = c._route("search.masterSearch.meanings", text=a.word)
    r1 = get(route1)

    layer1_search = [{
        "search_id": 1,
        "word": a.word,
        "route": route1,
        # every scalar the response carried about the search itself
        **{k: v for k, v in r1.items()
           if k not in ("definitions", "results", "searchTokens", "strongHighlights")
           and not isinstance(v, (list, dict))},
        "strongHighlights": r1.get("strongHighlights"),
        "definitions_returned": len(r1.get("definitions", [])),
        "results_returned": len(r1.get("results", [])),
    }]

    # one row per returned definition — ALL its fields, unaltered
    layer1_strong = []
    for i, d in enumerate(r1.get("definitions", []), 1):
        layer1_strong.append({"l1_id": i, "search_id": 1, "word": a.word, **d})

    # the verses this layer-1 search itself returned (it answers with verses too)
    layer1_verse = [{"l1v_id": i, "search_id": 1,
                     **{k: v for k, v in row.items() if k != "preview"},
                     "preview": row.get("preview")}
                    for i, row in enumerate(r1.get("results", []), 1)]

    print(f"[layer 1]  {route1}")
    print(f"           total={r1.get('total')}  searchType={r1.get('searchType')}  "
          f"definitions={len(layer1_strong)}  results={len(layer1_verse)}")
    for d in layer1_strong:
        print(f"             {d.get('strongNumber'):9} {str(d.get('gloss','')):26} "
              f"pop={d.get('popularity')}")
    print(f"           fields per definition: {sorted(layer1_strong[0].keys()) if layer1_strong else '—'}")

    # ── LAYER 2 — strong -> detail ──────────────────────────────────────────
    layer2_strong = []
    layer2_related = []          # relatedNos is a repeating group -> its own table
    layer2_morph = []            # morphInfos likewise

    print()
    for i, d in enumerate(layer1_strong, 1):
        code = d.get("strongNumber")
        route2 = c._route("module.getInfo", strong=code)
        r2 = get(route2)
        vocabs = r2.get("vocabInfos", []) or []
        print(f"[layer 2]  {code:9} -> vocabInfos={len(vocabs)}  morphInfos={len(r2.get('morphInfos',[]))}")
        for v in vocabs:
            row = {"l2_id": len(layer2_strong) + 1,
                   "l1_id": d["l1_id"],                 # FK -> layer 1
                   "requested_strong": code,            # what we asked for
                   **{k: val for k, val in v.items() if k != "relatedNos"}}
            layer2_strong.append(row)
            if row.get("strongNumber") != code:
                print(f"             ⚠ requested {code}, STEP answered {row.get('strongNumber')}")
            for j, rn in enumerate(v.get("relatedNos", []) or [], 1):
                layer2_related.append({"l2r_id": len(layer2_related) + 1,
                                       "l2_id": row["l2_id"],   # FK -> layer 2
                                       "of_strong": row.get("strongNumber"), **rn})
        for m in r2.get("morphInfos", []) or []:
            layer2_morph.append({"l2m_id": len(layer2_morph) + 1,
                                 "requested_strong": code, **m})

    tables = {
        "layer1_search": layer1_search,
        "layer1_strong": layer1_strong,
        "layer1_verse": layer1_verse,
        "layer2_strong": layer2_strong,
        "layer2_related": layer2_related,
        "layer2_morph": layer2_morph,
    }
    for name, rows in tables.items():
        (out / f"{name}.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False),
                                          encoding="utf-8")

    (out / "_layers.json").write_text(json.dumps({
        "word": a.word,
        "principle": "one table per SEARCH LAYER. The table is what the call returned — "
                     "nothing interpreted, nothing dropped, nothing renamed.",
        "layers": [
            {"layer": 1, "call": "masterSearch  version=<v>|meanings=<word>",
             "route": route1, "answers": "which strongs does this English word map to",
             "tables": {"layer1_search": "the search itself",
                        "layer1_strong": "one row per returned definition — word -> strong",
                        "layer1_verse": "the verses this same call returned"}},
            {"layer": 2, "call": "module.getInfo/<v>//<strong>//",
             "answers": "the detail of one strong",
             "tables": {"layer2_strong": "one row per returned vocabInfo",
                        "layer2_related": "relatedNos — a repeating group, so its own table",
                        "layer2_morph": "morphInfos — likewise"}},
        ],
        "foreign_keys": [
            {"from": "layer1_strong.search_id", "to": "layer1_search.search_id"},
            {"from": "layer1_verse.search_id", "to": "layer1_search.search_id"},
            {"from": "layer2_strong.l1_id", "to": "layer1_strong.l1_id"},
            {"from": "layer2_related.l2_id", "to": "layer2_strong.l2_id"},
        ],
        "counts": {k: len(v) for k, v in tables.items()},
        "fields_returned": {k: sorted({f for row in v for f in row}) for k, v in tables.items()},
    }, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n{'='*66}")
    for k, v in tables.items():
        print(f"  {k:18} {len(v):>4} row(s)")
    print(f"  -> {out.relative_to(ROOT)}")
    print(f"{'='*66}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
