"""_render_m15_baseline_to_md_v2_20260511.py — read-only render of v4 JSON.

Per-verse render where every verse line carries the full text needed to
confirm its review_status: verse text, AI-generated meaning, current
sub-group code + description, new sub-group code + description, current
DB VCG code + description, new VCG code + title + description.

Layout:
  - Headline + status counts
  - Section 'For research' — verses missing data or data-integrity issues
  - Section 'For Review' — verses with conflict flags
  - Section 'Ready with changes' — verses with a clean proposal
  - Section 'No change' — researcher-confirmed final state (initially empty)
Within each status, grouped by sub-group; within sub-group ordered by
canonical book/chapter/verse where possible (here: by reference string).
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
BASELINE_IN = os.path.join(M15_DIR, "m15-baseline-verses-v5-20260511.json")
OUT_PATH = os.path.join(M15_DIR, "m15-baseline-render-v3-20260511.md")

STATUS_ORDER = ["For research", "For Review", "Ready with changes", "No change"]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def short(s: str | None, limit: int = 250) -> str:
    if not s:
        return ""
    s = s.replace("\n", " ").strip()
    if len(s) > limit:
        return s[:limit].rstrip() + "…"
    return s


def render_verse_card(v: dict, out: list[str], duplicate_vr_ids: set[int]) -> None:
    """Render one verse as a compact card with all text inline.

    Verse-line format: `[vr_id]` (or `[vr_id/vc_id]` for the duplicate
    rows) + reference + Strong's + transliteration + gloss + status.
    """
    t = v["term"]
    cur = v.get("current") or {}
    new_sg = v.get("new_subgroup") or {}
    nv = v.get("new_vcg") or {}
    meaning = (v.get("meaning") or {})
    vcmp = v.get("vcg_comparison") or {}
    flags = v.get("review_flags") or []

    # Identifier: vr_id (with vc_id for the 2 known duplicates)
    if v["vr_id"] in duplicate_vr_ids and cur.get("vc_id") is not None:
        ident = f"[{v['vr_id']}/{cur['vc_id']}]"
    else:
        ident = f"[{v['vr_id']}]"

    gloss = t.get("gloss") or ""
    header_parts = [
        f"`{ident}`",
        f"**{v['reference']}**",
        f"`{t['strongs']} {t['translit']}` ({gloss})",
    ]
    if cur.get("status"):
        header_parts.append(f"_{cur['status']}_")
    if flags:
        header_parts.append(f"flags: {', '.join(flags)}")

    out.append(" · ".join(header_parts))
    out.append("")

    # Verse text + meaning (and AI annotation if any)
    out.append(f"> **Verse:** {short(v.get('verse_text'), 400)}")
    m_text = meaning.get("text")
    if m_text:
        out.append(f"> **Meaning:** {short(m_text, 500)}")
    else:
        out.append("> **Meaning:** _(missing — no v1 meaning row)_")
    ann = nv.get("verse_annotation") if nv else None
    if ann:
        out.append(f"> **AI annotation:** `[{short(ann, 200)}]`")

    # Sub-group comparison
    cur_sg_code = cur.get("subgroup_code") or "(none)"
    cur_sg_label = cur.get("subgroup_label") or ""
    cur_sg_descr = short(cur.get("subgroup_description"), 220)
    new_sg_code = new_sg.get("code") if new_sg else None
    new_sg_label = (new_sg or {}).get("label") or ""
    new_sg_descr = short((new_sg or {}).get("description"), 220)
    if cur_sg_code and cur_sg_descr:
        out.append(
            f"> **Current SG** `{cur_sg_code}` — {cur_sg_label} — _{cur_sg_descr}_"
        )
    else:
        out.append(f"> **Current SG** `{cur_sg_code}`")
    if new_sg_code is None:
        out.append("> **New SG**     _(no proposal)_")
    else:
        same_sg = (cur_sg_code == new_sg_code)
        if same_sg:
            out.append(f"> **New SG**     `{new_sg_code}` — {new_sg_label} ✅ same")
        else:
            out.append(
                f"> **New SG**     `{new_sg_code}` — {new_sg_label} ⚠️ change"
                + (f" — _{new_sg_descr}_" if new_sg_descr else "")
            )

    # VCG comparison
    db_block = vcmp.get("db") or {}
    new_block = vcmp.get("new") or {}
    db_code = db_block.get("code")
    db_descr = short(db_block.get("description"), 260)
    new_vcg_code = new_block.get("code")
    new_vcg_title = new_block.get("title") or ""
    new_vcg_descr = short(new_block.get("description"), 260)
    if db_code:
        out.append(
            f"> **Current VCG** `{db_code}` — _{db_descr or '(no DB description)'}_"
        )
    else:
        out.append("> **Current VCG** _(no DB group_id)_")
    if new_vcg_code:
        out.append(
            f"> **New VCG**     `{new_vcg_code}` — {new_vcg_title} — _{new_vcg_descr or '(no description)'}_"
        )
    else:
        out.append("> **New VCG**     _(no proposal)_")
    out.append("")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    with open(BASELINE_IN, "r", encoding="utf-8") as f:
        data = json.load(f)
    md = data["metadata"]
    verses = data["verses"]
    duplicate_vr_ids = set(md.get("duplicate_vr_ids", []))

    # Bucket by status, then by sub-group
    bucket: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for v in verses:
        status = v.get("review_status", "For research")
        sg = (v.get("current") or {}).get("subgroup_code") or "(unrouted)"
        bucket[status][sg].append(v)

    # Sort within each (status, sg) by reference string (stable enough for review)
    for status in bucket:
        for sg in bucket[status]:
            bucket[status][sg].sort(key=lambda v: v.get("reference", ""))

    counts = {s: sum(len(lst) for lst in bucket[s].values())
              for s in STATUS_ORDER}

    out: list[str] = []
    w = out.append

    w(f"# M15 baseline — per-verse render (with review status)")
    w(f"")
    w(f"_Source:_ `{os.path.relpath(BASELINE_IN, ROOT)}`")
    w(f"_Rendered:_ {now_iso()}")
    w(f"")
    w(f"## Headline counts")
    w(f"")
    w(f"| Status | Verses |")
    w(f"|---|---:|")
    for s in STATUS_ORDER:
        w(f"| **{s}** | {counts[s]} |")
    w(f"| _Total_ | {sum(counts.values())} |")
    w(f"")
    w(f"### Status definitions")
    w(f"")
    sw = md.get("status_workflow", {})
    w(f"- **No change** — researcher/AI confirms the verse is correctly placed; no edit needed. Not auto-assigned.")
    w(f"- **Ready with changes** — clear new_vcg proposal, sub-group aligned, no conflict flags.")
    w(f"- **For Review** — proposal exists but carries one or more flags: `subgroup_fallback`, `multi_candidate`, `ai_annotation`, `meaning_vcg_mismatch`.")
    w(f"- **For research** — missing critical info: no new_vcg AND/OR no meaning, duplicate vr_id, status P/UT, or no current group_id.")
    w(f"")
    w(f"_Read each verse card below to confirm or override the status._")
    w(f"")

    # Section per status
    for status in STATUS_ORDER:
        sg_dict = bucket.get(status, {})
        total = sum(len(lst) for lst in sg_dict.values())
        w(f"---")
        w(f"")
        w(f"## {status} — {total} verses")
        w(f"")
        if total == 0:
            w(f"_(none)_")
            w(f"")
            continue
        # Per-sub-group breakdown
        for sg in sorted(sg_dict):
            rows = sg_dict[sg]
            w(f"### {sg} — {len(rows)} verses")
            w(f"")
            for v in rows:
                render_verse_card(v, out, duplicate_vr_ids)
            w(f"")

    text = "\n".join(out) + "\n"
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Written: {OUT_PATH}")
    print(f"  size: {os.path.getsize(OUT_PATH):,} bytes")
    print(f"  status counts: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
