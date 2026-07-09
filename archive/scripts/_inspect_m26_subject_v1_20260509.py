"""_inspect_m26_subject_v1_20260509.py — render Step A meanings by subject.

Joins:
  - Step A JSONL  (m26-meanings-{model}-{date}.jsonl)
  - Subject JSONL (m26-subject-{model}-{sg}-{date}.jsonl)
  - DB (cluster_subgroup, mti_terms, wa_verse_records)

Output markdown structure:
  Sub-group A
    Subject: God
      Term G1342 *dikaios* (just) — N verses
        | ref | meaning | evidence | justification |
      Term G1343 ...
    Subject: man
      ...
    Subject: both
      ...
    Subject: neither
      ...
  Sub-group B
    ...

Records present in Step A but missing from Subject JSONL get rendered
under "(unclassified)" so they're visible.

NO API calls. NO DB writes.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")


CANONICAL_BOOKS = [
    "Gen", "Ex", "Lev", "Num", "Dt", "Jos", "Jdg", "Ru",
    "1Sa", "2Sa", "1Ki", "2Ki", "1Ch", "2Ch", "Ezr", "Ne",
    "Est", "Job", "Ps", "Pr", "Ec", "SS", "Is", "Je", "La",
    "Eze", "Da", "Hos", "Joel", "Am", "Ob", "Jon", "Mi",
    "Na", "Hab", "Zep", "Hag", "Zec", "Mal",
    "Mt", "Mk", "Lk", "Jn", "Ac", "Ro", "1Cor", "2Cor",
    "Ga", "Eph", "Php", "Col", "1Th", "2Th", "1Ti", "2Ti",
    "Tit", "Phm", "He", "Jas", "1Pe", "2Pe", "1Jn", "2Jn",
    "3Jn", "Jud", "Re",
]
BOOK_ORDER = {b: i for i, b in enumerate(CANONICAL_BOOKS)}

SUBJECT_ORDER = ["God", "man", "both", "neither", "(unclassified)"]


def ref_sort_key(ref: str):
    parts = ref.split(maxsplit=1)
    book = parts[0]
    rest = parts[1] if len(parts) > 1 else ""
    chap, _, vrs = rest.partition(":")
    try:
        c = int(chap)
    except ValueError:
        c = 0
    try:
        v = int(vrs.split()[0]) if vrs else 0
    except ValueError:
        v = 0
    return (BOOK_ORDER.get(book, 999), c, v)


def load_jsonl(path: str) -> list[dict]:
    out = []
    if not Path(path).exists():
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--meanings", required=True)
    ap.add_argument("--subjects", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    meanings = load_jsonl(args.meanings)
    subjects = load_jsonl(args.subjects)
    print(f"Meanings: {len(meanings)}")
    print(f"Subjects: {len(subjects)}")

    subj_by_key = {(s["vr_id"], s["mti_term_id"]): s for s in subjects}

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Term metadata (no sub-group here — that's per-verse post-M46)
    term_meta = {
        r["id"]: {
            "strong": r["strongs_number"],
            "translit": r["transliteration"],
            "gloss": r["gloss"],
        }
        for r in conn.execute("""
            SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss
              FROM mti_terms mt
             WHERE mt.cluster_code='M26'
               AND COALESCE(mt.delete_flagged,0)=0
        """)
    }

    # Sub-group metadata (id -> code/label/sort_order)
    sg_meta = {
        r["id"]: {
            "sg_code": r["subgroup_code"], "sg_label": r["label"],
            "sort_order": r["sort_order"],
        }
        for r in conn.execute("""
            SELECT id, subgroup_code, label, sort_order
              FROM cluster_subgroup
             WHERE cluster_code='M26'
               AND COALESCE(delete_flagged,0)=0
        """)
    }
    UNROUTED_KEY = -1
    sg_meta[UNROUTED_KEY] = {
        "sg_code": "M26-UNROUTED", "sg_label": "(no vc routing)",
        "sort_order": 999,
    }

    # vc routing: (vr_id, mti_term_id) -> list of cluster_subgroup_id
    # (list because 'both'-DEC-3 verses post-M26-A-apply have multiple)
    vc_routing: dict[tuple[int, int], list[int]] = defaultdict(list)
    for r in conn.execute("""
        SELECT vc.verse_record_id, vc.mti_term_id, vc.cluster_subgroup_id
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE mt.cluster_code='M26'
           AND COALESCE(vc.delete_flagged,0)=0
           AND vc.cluster_subgroup_id IS NOT NULL
    """):
        vc_routing[(r[0], r[1])].append(r[2])

    verse_refs = {
        r[0]: r[1] for r in conn.execute(
            "SELECT id, reference FROM wa_verse_records "
            " WHERE COALESCE(delete_flagged,0)=0"
        )
    }
    conn.close()

    # Restrict to sub-groups touched by the subjects file (any vc row whose
    # (vr_id, mti_term_id) appears in the subjects classification)
    sg_in_subjects = set()
    for s in subjects:
        for sg_id in vc_routing.get((s["vr_id"], s["mti_term_id"]), []):
            sg_in_subjects.add(sg_id)

    # bucket: cluster_subgroup_id -> subject -> mti_term_id -> [records]
    # A meaning record with N vc routings is rendered under each.
    bucket: dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for m in meanings:
        key = (m["vr_id"], m["mti_term_id"])
        sg_ids = vc_routing.get(key) or [UNROUTED_KEY]
        if sg_in_subjects:
            sg_ids = [s for s in sg_ids
                      if s == UNROUTED_KEY or s in sg_in_subjects]
            if not sg_ids:
                continue
        s = subj_by_key.get(key)
        subj = s["subject"] if s else "(unclassified)"
        rec = {**m, "justification": (s.get("justification") if s else "")}
        for sg_id in sg_ids:
            bucket[sg_id][subj][m["mti_term_id"]].append(rec)

    sg_ids_sorted = sorted(
        bucket.keys(),
        key=lambda sid: (sg_meta.get(sid, {}).get("sort_order", 998),
                         sg_meta.get(sid, {}).get("sg_code", "")),
    )
    out_path = args.out or args.subjects.replace(
        ".jsonl", "-by-subject.md"
    ).replace("m26-subject-", "m26-meanings-by-subject-")

    lines = [
        f"# M26 — meanings re-grouped by subject (God / man / both / neither)\n",
        f"Sources:",
        f"  - meanings: `{args.meanings}`",
        f"  - subjects: `{args.subjects}`",
        f"",
    ]

    # Top-line counts table
    lines.append("## Counts\n")
    lines.append("| sub-group | God | man | both | neither | (unclassified) | total |")
    lines.append("|-----------|-----|-----|------|---------|---------------:|------:|")
    grand = {s: 0 for s in SUBJECT_ORDER}
    for sg_id in sg_ids_sorted:
        sg_code = sg_meta.get(sg_id, {}).get("sg_code", "?")
        row = []
        total = 0
        for s in SUBJECT_ORDER:
            n = sum(len(v) for v in bucket[sg_id].get(s, {}).values())
            row.append(n)
            grand[s] += n
            total += n
        lines.append(
            f"| {sg_code} | {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {total} |"
        )
    grand_total = sum(grand.values())
    lines.append(
        f"| **all** | **{grand['God']}** | **{grand['man']}** | "
        f"**{grand['both']}** | **{grand['neither']}** | "
        f"**{grand['(unclassified)']}** | **{grand_total}** |"
    )
    lines.append("")

    # Detailed sections
    for sg_id in sg_ids_sorted:
        sg_code = sg_meta.get(sg_id, {}).get("sg_code", "?")
        sg_label = sg_meta.get(sg_id, {}).get("sg_label", "")
        lines.append(f"\n## {sg_code} — {sg_label}\n")

        for subj in SUBJECT_ORDER:
            if subj not in bucket[sg_id]:
                continue
            n = sum(len(v) for v in bucket[sg_id][subj].values())
            lines.append(f"\n### Subject: {subj}  ·  {n} verses")
            term_ids = sorted(
                bucket[sg_id][subj].keys(),
                key=lambda m: term_meta.get(m, {}).get("strong", "")
            )
            for tid in term_ids:
                meta = term_meta.get(tid, {})
                rows = bucket[sg_id][subj][tid]
                rows.sort(key=lambda r: ref_sort_key(
                    verse_refs.get(r["vr_id"], "Zzz 0:0")))
                lines.append(
                    f"\n**{meta.get('strong', '?')} "
                    f"*{meta.get('translit', '')}* "
                    f"({meta.get('gloss', '')})**  ·  {len(rows)} verses\n"
                )
                lines.append(
                    "| ref | meaning | evidence | cue |"
                )
                lines.append(
                    "|-----|---------|----------|-----|"
                )
                for r in rows:
                    ref = verse_refs.get(r["vr_id"], f"vr={r['vr_id']}")
                    m_ = (r.get("meaning") or "").replace("|", "\\|")
                    e_ = (r.get("evidence_quote") or "").replace("|", "\\|")
                    j_ = (r.get("justification") or "").replace("|", "\\|")
                    lines.append(f"| {ref} | {m_} | {e_} | {j_} |")
                lines.append("")

    Path(out_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
