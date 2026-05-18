"""Build a researcher-review document for M04's 75 terse set-asides.

Step 2 of the M04 v2_5 retrofit (per researcher direction 2026-05-18):
list every M04 verse set aside with the terse reasons 'physical_only' or
'no_inner_being' so the researcher can decide per verse:
  - CONFIRM SET-ASIDE (rewrite reason with §4.5.1-valid evidence-based ground)
  - RESCUE (re-classify is_relevant=1; Pass A meaning + downstream cascade)

Read-only. Output: Sessions/Session_Clusters/M04/WA-M04-terse-setaside-review-v1-{date}.md
"""
from __future__ import annotations
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
OUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-terse-setaside-review-v1-{TODAY}.md")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, mt.strongs_number, mt.transliteration, mt.gloss,
               vc.set_aside_reason,
               vr.reference, vr.verse_text, vr.context_before, vr.context_after,
               vr.translation
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE mt.cluster_code = 'M04'
          AND vc.is_relevant = 0
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.set_aside_reason IN ('physical_only', 'no_inner_being')
        ORDER BY vc.set_aside_reason, mt.strongs_number, vr.reference
        """
    ).fetchall()
    conn.close()

    by_reason = defaultdict(list)
    for r in rows:
        by_reason[r["set_aside_reason"]].append(r)

    L = []
    L.append("# M04 terse set-aside review — researcher decision required")
    L.append("")
    L.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    L.append(f"**Purpose:** Step 2 of the M04 v2_5 retrofit. The audit flagged 75 set-aside verses with terse reasons ('physical_only', 'no_inner_being') that may be bias-driven under v2_5 §1.1.")
    L.append(f"**Total verses to review:** {len(rows)}")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## How to use this document")
    L.append("")
    L.append("For each verse, mark a decision in the **Decision** column:")
    L.append("")
    L.append("- **CONFIRM** — Set-aside is correct; the verse genuinely lacks any inner-being state (the term refers to a physical/literal thing, not an inner state). In the **Rationale** column write a verse-specific evidence-based reason per §4.5.1 (e.g., \"tov as 'good land' — geographical descriptor, no inner state evidenced\").")
    L.append("- **RESCUE** — The verse DOES evidence an inner-being state under v2_5 §1.1's full scope (horizontal, sensory, evaluative, etc.); it was wrongly set aside under bias. CC will re-classify `is_relevant=1` and the verse cascades through Pass A → sub-group review → VCG → findings.")
    L.append("- **HOLD** — Uncertain; researcher needs more time / cross-reference; defer decision.")
    L.append("")
    L.append("Annotations may be added inline (e.g., `vc=18001 → RESCUE: this is moral-evaluative inner-being content`).")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Summary")
    L.append("")
    L.append("| Set-aside reason | Count |")
    L.append("|---|---:|")
    for reason in sorted(by_reason.keys()):
        L.append(f"| `{reason}` | {len(by_reason[reason])} |")
    L.append(f"| **Total** | **{len(rows)}** |")
    L.append("")
    L.append("All 75 are H2896A tov (good/pleasant). This reflects v2_4's tov-specific BOUNDARY work which split tov senses across multiple registers — some of which v2_5 §1.1 now brings into substantive scope.")
    L.append("")
    L.append("---")
    L.append("")

    for reason in ("no_inner_being", "physical_only"):
        verses = by_reason.get(reason, [])
        if not verses:
            continue
        L.append(f"## Set-aside reason: `{reason}` ({len(verses)} verses)")
        L.append("")
        for v in verses:
            L.append(f"### vc={v['vc_id']} — {v['reference']}")
            L.append("")
            L.append(f"**Term:** {v['strongs_number']} {v['transliteration']} — {v['gloss']}")
            L.append("")
            ctx_before = (v["context_before"] or "").strip()
            ctx_after = (v["context_after"] or "").strip()
            text = (v["verse_text"] or "").strip()
            if ctx_before:
                L.append(f"> _… {ctx_before}_")
            L.append(f"> **{text}**")
            if ctx_after:
                L.append(f"> _{ctx_after} …_")
            L.append("")
            L.append(f"**Current set_aside_reason:** `{v['set_aside_reason']}`")
            L.append("")
            L.append("**Decision:** _[CONFIRM / RESCUE / HOLD]_")
            L.append("**Rationale:** _[verse-specific evidence-based reason per §4.5.1 if CONFIRM; or analytical note if RESCUE]_")
            L.append("")
            L.append("---")
            L.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote: {OUT}")
    print(f"Total verses: {len(rows)}")
    for reason, verses in by_reason.items():
        print(f"  {reason}: {len(verses)}")


if __name__ == "__main__":
    main()
