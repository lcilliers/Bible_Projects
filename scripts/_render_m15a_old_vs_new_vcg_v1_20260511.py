"""_render_m15a_old_vs_new_vcg_v1_20260511.py — read-only.

Produce a markdown review of M15-A verses comparing OLD DB VCG assignments
to NEW authoritative assignments from wa-m15a-vcg-groups-v2 (loaded into
v9 of the baseline). Includes the 10 new VCGs (with anchors), the 39
set-asides, and the 5 M15-E reroutes.

Source: m15-baseline-verses-v9-20260511.json
Output: m15-M15A-old-vs-new-vcg-v1-20260511.md
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
IN_PATH = os.path.join(M15_DIR, "m15-baseline-verses-v9-20260511.json")
OUT_PATH = os.path.join(M15_DIR, "m15-M15A-old-vs-new-vcg-v1-20260511.md")

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
    return (BOOK_INDEX.get(m.group(1), 99), int(m.group(2)), int(m.group(3)))


def short(s: str | None, limit: int = 320) -> str:
    if not s:
        return ""
    s = s.replace("\n", " ").strip()
    return s if len(s) <= limit else s[:limit].rstrip() + "…"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(IN_PATH, "r", encoding="utf-8") as f:
        d = json.load(f)

    # Filter M15-A verses (effective sub-group, before reroute)
    # We want all 307 verses that were in M15-A per the input. Use the
    # m15a_vcg_merge metadata which set assignments for exactly those.
    # Practical filter: any verse with new_vcg.code starting M15-A-VCG,
    # or proposed_set_aside, or new_subgroup._origin starting with
    # 'manual_reroute_2026-05-11_M15A_input'.
    m15a_verses = []
    for v in d["verses"]:
        nv = v.get("new_vcg") or {}
        if nv.get("code", "").startswith("M15-A-VCG"):
            v["_bucket"] = ("vcg", nv["code"])
            m15a_verses.append(v)
            continue
        if "proposed_set_aside" in v:
            # Only consider set-asides from the M15-A pass (others may
            # exist in DB). Filter by source_file.
            sa = v.get("proposed_set_aside") or {}
            if sa.get("source_file") == "wa-m15a-vcg-v1-20260511.json":
                v["_bucket"] = ("setaside", "SETASIDE")
                m15a_verses.append(v)
                continue
        ns = v.get("new_subgroup") or {}
        if ns.get("_origin") == "manual_reroute_2026-05-11_M15A_input":
            v["_bucket"] = ("reroute", "REROUTE-M15-E")
            m15a_verses.append(v)
            continue

    print(f"M15-A verses found: {len(m15a_verses)}")
    by_bucket = Counter(v["_bucket"][0] for v in m15a_verses)
    print(f"  by bucket: {dict(by_bucket)}")

    # Group by new VCG (or SETASIDE / REROUTE)
    grouped: dict[str, list] = defaultdict(list)
    for v in m15a_verses:
        grouped[v["_bucket"][1]].append(v)
    # Sort each group's verses: strongs, then canonical ref
    for code in grouped:
        grouped[code].sort(key=lambda v: (v["term"]["strongs"],
                                          ref_sort_key(v.get("reference"))))

    # Build cross-map: old VCG → new VCG counts
    cross = Counter()
    for v in m15a_verses:
        old = (v.get("current") or {}).get("group_code") or "(none)"
        new_code = v["_bucket"][1]
        cross[(old, new_code)] += 1

    out: list[str] = []
    w = out.append

    w("# M15-A — old vs new VCG assignments review")
    w("")
    w(f"_Source:_ `{os.path.relpath(IN_PATH, ROOT)}`")
    w(f"_Rendered:_ {now_iso()}")
    w("")
    w("**Sub-group:** `M15-A` — *Wisdom as holistic inner character and orientation*")
    w("")
    w("Three buckets for M15-A's 307 verses:")
    w("")
    w(f"- **10 new VCGs** (M15-A-VCG01..10) covering **{by_bucket.get('vcg', 0)} verses** — each with a designated anchor")
    w(f"- **{by_bucket.get('setaside', 0)} verses proposed set-aside** (no inner-being phenomenon carried by the term in that verse)")
    w(f"- **{by_bucket.get('reroute', 0)} verses proposed re-route to M15-E** (deliberative planning — wrong sub-group)")
    w("")

    # Cross-map summary
    w("## 1. DB old VCG → new VCG flow")
    w("")
    w("_Each row: how many M15-A verses in the DB's existing VCG code (left) are being routed to which new VCG / bucket (right)._")
    w("")
    w("| Old VCG | New VCG / bucket | Verses |")
    w("|---|---|---:|")
    for (old, new_code), n in sorted(cross.items(), key=lambda x: (-x[1], x[0])):
        w(f"| `{old}` | `{new_code}` | {n} |")
    w("")

    # 2. Per new VCG section
    w("## 2. New VCG sections — anchor + assigned verses")
    w("")
    w(
        "_Each verse line: `[vr_id]` · reference · "
        "`Strong's translit` (gloss) · old VCG · meaning · assignment note._"
    )
    w("")
    vcg_codes_sorted = sorted(
        [c for c in grouped if c.startswith("M15-A-VCG")],
        key=lambda c: int(c.split("VCG")[-1])
    )
    for code in vcg_codes_sorted:
        rows = grouped[code]
        # Pull VCG meta from the first row's new_vcg
        meta = rows[0].get("new_vcg") or {}
        label = meta.get("label") or ""
        descr = meta.get("context_description") or ""
        # Find anchor row in this VCG
        anchor_row = next((r for r in rows
                           if (r.get("new_vcg") or {}).get("is_anchor")), None)

        w(f"### {code} — {label}")
        w("")
        w(f"_{descr}_")
        w("")
        if anchor_row:
            t = anchor_row["term"]
            anv = anchor_row.get("new_vcg") or {}
            w(f"**Anchor:** `[{anchor_row['vr_id']}]` "
              f"**{anchor_row['reference']}** · "
              f"`{t['strongs']} {t['translit']}` ({t.get('gloss', '')})")
            w("")
            w(f"> {short(anchor_row.get('verse_text'), 500)}")
            w(f"> ")
            w(f"> **Anchor rationale:** {short(anv.get('anchor_rationale'), 600)}")
            w("")
        else:
            w(f"_No anchor designated._")
            w("")
        w(f"**Verses in this VCG ({len(rows)}):**")
        w("")
        for r in rows:
            t = r["term"]
            old = (r.get("current") or {}).get("group_code") or "(none)"
            anchor_mark = " 🎯 ANCHOR" if r is anchor_row else ""
            anv = r.get("new_vcg") or {}
            note = anv.get("assignment_note") or ""
            meaning = (r.get("meaning") or {}).get("text") or ""
            w(
                f"- `[{r['vr_id']}]` · **{r['reference']}** · "
                f"`{t['strongs']} {t['translit']}` ({t.get('gloss', '')}) · "
                f"old VCG `{old}`{anchor_mark}"
            )
            w(f"  > {short(r.get('verse_text'), 320)}")
            if meaning:
                w(f"  > _Meaning:_ {short(meaning, 320)}")
            if note:
                w(f"  > _Assignment:_ {short(note, 220)}")
            w("")
        w("---")
        w("")

    # 3. Set-asides
    sa_rows = grouped.get("SETASIDE", [])
    w(f"## 3. Proposed set-aside — {len(sa_rows)} verses")
    w("")
    if sa_rows:
        first_sa = sa_rows[0].get("proposed_set_aside") or {}
        w(f"_Reason: `{first_sa.get('reason')}`._")
        w(f"_{short(first_sa.get('context_description'), 600)}_")
        w("")
        for r in sa_rows:
            t = r["term"]
            old = (r.get("current") or {}).get("group_code") or "(none)"
            sa = r.get("proposed_set_aside") or {}
            note = sa.get("assignment_note") or ""
            meaning = (r.get("meaning") or {}).get("text") or ""
            w(
                f"- `[{r['vr_id']}]` · **{r['reference']}** · "
                f"`{t['strongs']} {t['translit']}` ({t.get('gloss', '')}) · "
                f"old VCG `{old}`"
            )
            w(f"  > {short(r.get('verse_text'), 320)}")
            if meaning:
                w(f"  > _Meaning:_ {short(meaning, 320)}")
            if note:
                w(f"  > _Reason here:_ {short(note, 220)}")
            w("")
    w("---")
    w("")

    # 4. Reroutes
    rr_rows = grouped.get("REROUTE-M15-E", [])
    w(f"## 4. Proposed re-route to M15-E — {len(rr_rows)} verses")
    w("")
    if rr_rows:
        first_rr = rr_rows[0].get("new_subgroup") or {}
        w(
            f"_Target sub-group: `M15-E` — "
            f"{first_rr.get('label') or 'Deliberative planning, counsel, and purposive intent'}_"
        )
        w(f"_Reason: {short(first_rr.get('_reroute_reason'), 600)}_")
        w("")
        for r in rr_rows:
            t = r["term"]
            old = (r.get("current") or {}).get("group_code") or "(none)"
            ns = r.get("new_subgroup") or {}
            note = ns.get("_reroute_note") or ""
            meaning = (r.get("meaning") or {}).get("text") or ""
            w(
                f"- `[{r['vr_id']}]` · **{r['reference']}** · "
                f"`{t['strongs']} {t['translit']}` ({t.get('gloss', '')}) · "
                f"old VCG `{old}` → new SG `M15-E`"
            )
            w(f"  > {short(r.get('verse_text'), 320)}")
            if meaning:
                w(f"  > _Meaning:_ {short(meaning, 320)}")
            if note:
                w(f"  > _Reroute note:_ {short(note, 220)}")
            w("")

    text = "\n".join(out) + "\n"
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Written: {OUT_PATH}")
    print(f"  size: {os.path.getsize(OUT_PATH):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
