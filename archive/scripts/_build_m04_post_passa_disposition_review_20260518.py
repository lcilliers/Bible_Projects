"""Build the post-Pass-A disposition review document for M04 retrofit.

After the 75-verse reset + Pass A re-run + 4 special-case fixes, 77 verses have
fresh per-verse meanings. Researcher now decides per verse:

- **PROMOTE-TO-SUBGROUP** — assign to an existing M04 sub-group (A-J) or propose new
- **CONFIRM-SET-ASIDE** — re-set-aside with a §4.5.1-valid evidence-based reason
- **HOLD** — defer decision

The document groups verses by their fresh meaning's apparent register (heuristic
keyword scan) so the researcher can review cohesively.

Output: Sessions/Session_Clusters/M04/WA-M04-post-passa-disposition-review-v1-{date}.md
"""
from __future__ import annotations
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
OUT = Path(f"Sessions/Session_Clusters/M04/WA-M04-post-passa-disposition-review-v1-{TODAY}.md")

# Heuristic register grouping (keyword scan of analysis_note). Lets the
# researcher review cohesively rather than verse-by-verse alphabetically.
REGISTER_HEURISTICS = [
    ("vertical_god_directed", ["god is good", "yhwh", "lord is", "lord's", "divine", "god's character", "god's goodness"]),
    ("evaluative_moral", ["moral", "evaluat", "judge", "what is good", "right or wrong", "righteous", "ethical"]),
    ("communal_festive", ["celebrat", "feast", "festal", "community", "communal", "corporate", "assembly"]),
    ("wellbeing_circumstantial", ["it may be well", "wellbeing", "well-being", "circumstance", "prosperity", "thrive", "flourish"]),
    ("material_property", ["good land", "good thing", "abundance", "material", "wealth", "possession"]),
    ("sensory_aesthetic", ["beautiful", "pleasant smell", "sweetness", "aroma", "appearance", "form"]),
    ("relational_horizontal", ["between people", "marital", "parental", "neighbor", "neighbour", "friend"]),
    ("volitional_evaluative", ["seems good", "seems fitting", "what pleases", "deference", "decision"]),
    ("news_speech", ["good news", "good word", "good report", "speech", "tongue", "lips"]),
    ("ill_inner_being", ["no inner", "no inner-being", "not an inner state", "literal", "place", "geographic"]),
]


def classify_register(note: str) -> str:
    note_low = (note or "").lower()
    for label, kws in REGISTER_HEURISTICS:
        for kw in kws:
            if kw in note_low:
                return label
    return "uncategorised"


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Pull all verses currently is_relevant=1 + analysis_note populated + recently audit-fixed
    # We identify these by the notes field containing the audit-fix marker.
    rows = conn.execute(
        """
        SELECT vc.id AS vc_id, vc.is_relevant, vc.analysis_note, vc.notes,
               vc.cluster_subgroup_id, vc.group_id,
               mt.strongs_number, mt.transliteration, mt.gloss,
               vr.reference, vr.verse_text, vr.context_before, vr.context_after,
               cs.subgroup_code
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        LEFT JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        WHERE mt.cluster_code = 'M04'
          AND vc.is_relevant = 1
          AND COALESCE(vc.delete_flagged, 0) = 0
          AND vc.analysis_note IS NOT NULL
          AND vc.notes LIKE '%audit-fix v2_5%2026-05-18%'
        ORDER BY mt.strongs_number, vr.book_id, vr.chapter, vr.verse_num
        """
    ).fetchall()

    print(f"Audit-fix verses with fresh Pass A: {len(rows)}")

    by_register = defaultdict(list)
    for r in rows:
        by_register[classify_register(r["analysis_note"])].append(r)

    L = []
    L.append("# M04 post-Pass-A disposition review")
    L.append("")
    L.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    L.append(f"**Total verses with fresh meanings:** {len(rows)}")
    L.append("")
    L.append("**Context:** the 75 terse-set-aside verses (all H2896A tov) were reset on 2026-05-18 per researcher direction (\"these verses must all be reset to UT and re-introduced, meaning generated, and re-evaluated\"), plus 2 special-case orphans (2Sa 23:1 na.im, Ezr 6:16 ched.vah) had their wa_verse_records restored. Pass A re-authored a fresh per-verse meaning for each. This document is the disposition review.")
    L.append("")
    L.append("**Per-verse decision required:**")
    L.append("")
    L.append("- **PROMOTE-{subgroup_code}** — assign to an M04 sub-group (e.g. `PROMOTE-M04-A`, `PROMOTE-M04-J`). Existing sub-groups: M04-A (Exultation in YHWH), M04-B (Communal/Festive), M04-C (NT Joy in Christ), M04-D (Shared Communal), M04-E (Promised/Eschatological), M04-F (Cheerfulness under Adversity), M04-G (Delight in God's Word), M04-H (Volitional Delight), M04-I (Wonder), M04-J (Pleasantness/Relational).")
    L.append("- **PROMOTE-NEW-{label}** — propose a new sub-group (e.g. `PROMOTE-NEW-EvaluativeGoodness`).")
    L.append("- **CONFIRM-SET-ASIDE** — re-set-aside with a §4.5.1-valid evidence-based reason in the Rationale block.")
    L.append("- **HOLD** — defer.")
    L.append("")
    L.append("Mark decisions inline. After saving, ping me ('M04 disposition review marked') and I'll process.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Summary by heuristic register grouping")
    L.append("")
    L.append("| Register heuristic | Count |")
    L.append("|---|---:|")
    for reg in sorted(by_register.keys()):
        L.append(f"| `{reg}` | {len(by_register[reg])} |")
    L.append("")
    L.append("*Heuristic only — keyword-based; use as a navigation aid, not as the disposition.*")
    L.append("")
    L.append("---")
    L.append("")

    for reg in sorted(by_register.keys()):
        verses = by_register[reg]
        L.append(f"## Register heuristic: `{reg}` ({len(verses)} verses)")
        L.append("")
        for v in verses:
            current_sg = v["subgroup_code"] or "—"
            L.append(f"### vc={v['vc_id']} — {v['reference']} ({v['strongs_number']} {v['transliteration']})")
            L.append("")
            L.append(f"**Current sub-group:** {current_sg}  |  **gloss:** {v['gloss']}")
            L.append("")
            text = (v["verse_text"] or "").strip()
            ctx_before = (v["context_before"] or "").strip()
            ctx_after = (v["context_after"] or "").strip()
            if ctx_before:
                L.append(f"> _… {ctx_before}_")
            L.append(f"> **{text}**")
            if ctx_after:
                L.append(f"> _{ctx_after} …_")
            L.append("")
            L.append(f"**Pass A meaning (fresh, authored 2026-05-18):**")
            L.append("")
            L.append(f"> {v['analysis_note']}")
            L.append("")
            L.append(f"**Decision:** _[PROMOTE-M04-X / PROMOTE-NEW-Label / CONFIRM-SET-ASIDE / HOLD]_")
            L.append(f"**Rationale:** _[for CONFIRM-SET-ASIDE: §4.5.1-valid evidence-based reason; for PROMOTE: analytical note]_")
            L.append("")
            L.append("---")
            L.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
