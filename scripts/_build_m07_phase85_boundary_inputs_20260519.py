"""M07 Phase 8.5 BOUNDARY-resolution inputs (per v2_8 §11A.1).

Produces:
1. BOUNDARY content report: per BOUNDARY term, verses + Pass A meanings
   + current cluster_subgroup_id + current group_id + the new VCG code.
2. Co-occurrence list: for every BOUNDARY verse, other-cluster terms
   at the same wa_verse_records.id (informational only, per §18.2).

Output paths:
  Sessions/Session_Clusters/M07/WA-M07-boundary-resolution-input-v1-20260519.md
  Sessions/Session_Clusters/M07/WA-M07-boundary-cooccurrence-list-v1-20260519.md
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
from pathlib import Path
from datetime import datetime
from collections import defaultdict

DB = Path('database/bible_research.db')
CONTENT_OUT = Path('Sessions/Session_Clusters/M07/WA-M07-boundary-resolution-input-v1-20260519.md')
COOC_OUT = Path('Sessions/Session_Clusters/M07/WA-M07-boundary-cooccurrence-list-v1-20260519.md')

# 5 BOUNDARY terms per Phase 3 v2 + Phase 5
BOUNDARY_TERMS = [
    (628, 'G2699', 'katatomē', 'mutilation'),
    (4905, 'H4893A', 'mish.chat', 'mutilation'),
    (5573, 'H5206', 'ni.dah', 'filth'),
    (244, 'H8213', 'sha.phel', 'to abase'),
    (4712, 'H8400', 'te.val.lul', 'defect'),
]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

NOW = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# ============================================================
# 1. BOUNDARY content report
# ============================================================
lines = []
lines.append("# M07 Phase 8.5 — BOUNDARY resolution input (content report)")
lines.append("")
lines.append(f"**Date:** {NOW}")
lines.append("**Cluster:** M07 — Shame, Disgrace and Humiliation")
lines.append("**Per:** v2_8 §11A.1 — input #1 (BOUNDARY content)")
lines.append("")
lines.append("Five BOUNDARY terms remain in M07 after Phase 3 v2. Each verse needs a per-verse disposition from §18.2: **SET-ASIDE** / **ROUTE-TO-CLUSTER** / **PROMOTE-TO-SUBGROUP** (existing target or new sub-group).")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append("| mti_id | Strong's | Translit | Gloss | Verses | Phase 3 question |")
lines.append("|---:|---|---|---|---:|---|")
total_verses = 0
for mti_id, strongs, translit, gloss in BOUNDARY_TERMS:
    n = cur.execute(
        "SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND is_relevant=1 AND COALESCE(delete_flagged,0)=0",
        (mti_id,),
    ).fetchone()[0]
    total_verses += n
    q_text = {
        628: "Cluster-membership undecided — single verse, minimal inner-being content",
        4905: "Cluster-membership undecided — outward physical disfigurement; no inner shame content named",
        5573: "Cluster-membership undecided — M07/M12 boundary; filth producing shame outcome",
        244: "Cluster-membership undecided — M07/M09 split (enforced humiliation of pride vs voluntary lowliness)",
        4712: "Data gap — no is_relevant verses (only an SA verse); CC verification needed",
    }[mti_id]
    lines.append(f"| {mti_id} | {strongs} | {translit} | {gloss} | {n} | {q_text} |")
lines.append(f"| | | | | **{total_verses}** | |")
lines.append("")
lines.append("---")
lines.append("")

# Per-term sections
for mti_id, strongs, translit, gloss in BOUNDARY_TERMS:
    lines.append(f"## {strongs} {translit} — {gloss} (mti_id={mti_id})")
    lines.append("")
    # Pull per-verse meanings + current sub-group + group_code
    rows = list(cur.execute("""
        SELECT vc.id AS vc_id, vr.reference, vr.verse_text,
               vc.analysis_note, vc.is_relevant,
               cs.subgroup_code, vcg.group_code
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        LEFT JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        LEFT JOIN verse_context_group vcg ON vcg.id = vc.group_id
        WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (mti_id,)).fetchall())

    if not rows:
        lines.append(f"**No verse_context rows.** Term is a data gap — CC to verify whether any verses should exist; if zero, term may be reassessed for removal from M07 entirely.")
        lines.append("")
        lines.append("---")
        lines.append("")
        continue

    n_rel = sum(1 for r in rows if r['is_relevant'] == 1)
    lines.append(f"**{len(rows)} verse_context rows** ({n_rel} is_relevant, {len(rows) - n_rel} set_aside).")
    lines.append(f"**Current sub-group routing:** all M07-BOUNDARY.")
    lines.append("")

    for r in rows:
        rel_tag = "is_relevant=1" if r['is_relevant'] == 1 else "set_aside"
        lines.append(f"### vc={r['vc_id']} — {r['reference']} ({rel_tag})")
        lines.append("")
        if r['verse_text']:
            text = r['verse_text'].strip()
            if len(text) > 600:
                text = text[:600] + ' …'
            lines.append(f"> {text}")
            lines.append("")
        if r['analysis_note']:
            lines.append(f"**Pass A meaning:** {r['analysis_note']}")
        else:
            lines.append(f"**Pass A meaning:** *(none — analysis_note is NULL)*")
        lines.append("")
        lines.append(f"**Current routing:** sub-group `{r['subgroup_code'] or '(none)'}` · VCG `{r['group_code'] or '(none)'}`")
        lines.append("")

    lines.append("---")
    lines.append("")

CONTENT_OUT.write_text("\n".join(lines), encoding='utf-8')
print(f"Wrote {CONTENT_OUT}")
print(f"Size: {CONTENT_OUT.stat().st_size:,} bytes")

# ============================================================
# 2. Co-occurrence list (informational, per §18.2)
# ============================================================
lines = []
lines.append("# M07 Phase 8.5 — BOUNDARY co-occurrence list (informational)")
lines.append("")
lines.append(f"**Date:** {NOW}")
lines.append("**Per:** v2_8 §11A.1 input #2 + §18.2 — informational input to disposition decisions; does not gate.")
lines.append("")
lines.append("For each BOUNDARY verse, other-cluster terms occurring at the same `wa_verse_records.id` (filter: cluster_code != 'M07' AND cluster_code IS NOT NULL).")
lines.append("")
lines.append("---")
lines.append("")

for mti_id, strongs, translit, gloss in BOUNDARY_TERMS:
    lines.append(f"## {strongs} {translit} (mti_id={mti_id})")
    lines.append("")
    vrs = list(cur.execute("""
        SELECT vc.id AS vc_id, vr.id AS vr_id, vr.reference, vc.is_relevant
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (mti_id,)).fetchall())

    if not vrs:
        lines.append("*(no verses)*")
        lines.append("")
        continue

    found_any = False
    for v in vrs:
        others = list(cur.execute("""
            SELECT mt.strongs_number, mt.transliteration, mt.cluster_code
            FROM verse_context vc2
            JOIN mti_terms mt ON mt.id = vc2.mti_term_id
            WHERE vc2.verse_record_id = ?
              AND vc2.mti_term_id != ?
              AND mt.cluster_code != 'M07'
              AND mt.cluster_code IS NOT NULL
              AND COALESCE(vc2.delete_flagged,0)=0
              AND COALESCE(mt.delete_flagged,0)=0
            ORDER BY mt.cluster_code, mt.strongs_number
        """, (v['vr_id'], mti_id)).fetchall())
        rel_tag = "is_relevant=1" if v['is_relevant'] == 1 else "set_aside"
        if others:
            found_any = True
            lines.append(f"- **vc={v['vc_id']} {v['reference']}** ({rel_tag}):")
            for o in others:
                lines.append(f"    - {o['cluster_code']} {o['strongs_number']} {o['transliteration']}")
        else:
            lines.append(f"- **vc={v['vc_id']} {v['reference']}** ({rel_tag}): *(no other-cluster terms)*")
    if not found_any:
        lines.append("")
        lines.append("*(no co-occurrences with other clusters across this term's verses)*")
    lines.append("")
    lines.append("---")
    lines.append("")

COOC_OUT.write_text("\n".join(lines), encoding='utf-8')
print(f"Wrote {COOC_OUT}")
print(f"Size: {COOC_OUT.stat().st_size:,} bytes")

conn.close()
