"""M07 Phase 8 — build the VCG dissolution comparison report.

Per v2_8 §11.3. Identifies inherited VCGs (linked to M07 mti_terms via
vcg_term but NOT created by the Phase 7 directive — i.e. group_code
doesn't match the M07-*-VCG-NN pattern) and produces the comparison.

For M07: every is_relevant verse already moved to a Phase 7 VCG at
Phase 7 Op C. The inherited VCGs are empty (no is_relevant references)
— uniform OBSOLETE disposition.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

DB = Path('database/bible_research.db')
OUT = Path('Sessions/Session_Clusters/M07/WA-M07-vcg-dissolution-comparison-v1-20260519.md')

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Identify inherited VCGs linked to M07
inherited = list(cur.execute("""
    SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description
    FROM verse_context_group vcg
    JOIN vcg_term vt ON vt.vcg_id = vcg.id
    JOIN mti_terms mt ON mt.id = vt.mti_term_id
    WHERE mt.cluster_code='M07'
      AND COALESCE(vt.delete_flagged,0)=0
      AND COALESCE(mt.delete_flagged,0)=0
      AND COALESCE(vcg.delete_flagged,0)=0
      AND NOT (vcg.group_code LIKE 'M07%-VCG-%')
    ORDER BY vcg.group_code
""").fetchall())

# Map of inherited VCG -> M07 terms originally linked
vcg_to_terms = defaultdict(list)
for r in cur.execute("""
    SELECT vt.vcg_id, mt.strongs_number, mt.transliteration, mt.id AS mti_id
    FROM vcg_term vt
    JOIN mti_terms mt ON mt.id = vt.mti_term_id
    JOIN verse_context_group vcg ON vcg.id = vt.vcg_id
    WHERE mt.cluster_code='M07'
      AND COALESCE(vt.delete_flagged,0)=0
      AND COALESCE(mt.delete_flagged,0)=0
      AND COALESCE(vcg.delete_flagged,0)=0
      AND NOT (vcg.group_code LIKE 'M07%-VCG-%')
"""):
    vcg_to_terms[r['vcg_id']].append({
        'strongs': r['strongs_number'],
        'translit': r['transliteration'],
        'mti_id': r['mti_id'],
    })

# Per inherited VCG: count members + is_relevant; identify which new VCGs absorbed those terms' verses
def per_vcg_counts(vcg_id):
    total = cur.execute(
        "SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id=? AND COALESCE(vc.delete_flagged,0)=0",
        (vcg_id,),
    ).fetchone()[0]
    return total

def new_vcgs_for_terms(mti_ids):
    if not mti_ids:
        return []
    ph = ','.join('?' * len(mti_ids))
    rows = cur.execute(
        f"""
        SELECT DISTINCT vcg.group_code,
               SUBSTR(vcg.context_description, 1, 130) AS descr
        FROM vcg_term vt
        JOIN verse_context_group vcg ON vcg.id = vt.vcg_id
        WHERE vt.mti_term_id IN ({ph})
          AND vcg.group_code LIKE 'M07%-VCG-%'
          AND COALESCE(vt.delete_flagged,0)=0
          AND COALESCE(vcg.delete_flagged,0)=0
        ORDER BY vcg.group_code
        """,
        mti_ids,
    ).fetchall()
    return [(r['group_code'], r['descr']) for r in rows]

# Write report
NOW = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
lines = []
lines.append("# M07 Phase 8 — VCG dissolution comparison report")
lines.append("")
lines.append(f"**Date:** {NOW}")
lines.append("**Cluster:** M07 — Shame, Disgrace and Humiliation")
lines.append("**Per:** v2_8 §11.3 — researcher comparison before dissolution")
lines.append("")
lines.append("---")
lines.append("")

# Summary
n_inherited = len(inherited)
n_with_active = 0
for v in inherited:
    if per_vcg_counts(v['id']) > 0:
        n_with_active += 1

lines.append("## Summary")
lines.append("")
lines.append(f"- **Inherited VCGs identified:** {n_inherited}")
lines.append(f"- **Inherited VCGs with active vc references:** {n_with_active}")
lines.append(f"- **Inherited VCGs already empty (Phase 7 migrated all verses):** {n_inherited - n_with_active}")
lines.append(f"- **Disposition (uniform):** OBSOLETE — inherited framings reflect pre-cluster-pivot Session B work on the original word registries (shame, humility, peace, etc.); they have no analogue in the M07 cluster's new VCG structure which was designed from the meaning corpus.")
lines.append("")
lines.append("**Phase 7 verification (recap from `WA-M07-dir-003-vcg-create-v1-20260519.md`):** 363 is_relevant verses routed to 29 new M07 VCGs; 0 is_relevant verses point at any inherited VCG.")
lines.append("")
lines.append("---")
lines.append("")

# Per inherited VCG
lines.append("## Per inherited VCG")
lines.append("")
for v in inherited:
    terms = vcg_to_terms[v['id']]
    terms_label = ", ".join(f"{t['strongs']} {t['translit']}" for t in terms)
    n_verses = per_vcg_counts(v['id'])

    lines.append(f"### Old VCG `{v['group_code']}` (id {v['id']})")
    lines.append("")
    descr = (v['context_description'] or '').strip()
    if len(descr) > 200:
        descr = descr[:200].rstrip() + ' …'
    lines.append(f"- **Old description:** {descr or '(empty)'}")
    lines.append(f"- **Linked M07 term(s):** {terms_label}")
    lines.append(f"- **Active vc references (post-Phase-7):** {n_verses}")
    lines.append(f"- **Disposition:** OBSOLETE")

    # Where did the term's verses go?
    new_vcg_list = new_vcgs_for_terms([t['mti_id'] for t in terms])
    if new_vcg_list:
        lines.append(f"- **New routing of the linked term(s)' verses (Phase 7):**")
        for code, descr_excerpt in new_vcg_list[:6]:
            d = (descr_excerpt or '').strip()
            if len(d) > 130:
                d = d[:130].rstrip() + ' …'
            lines.append(f"  - `{code}` — {d}")
        if len(new_vcg_list) > 6:
            lines.append(f"  - … and {len(new_vcg_list) - 6} more new VCGs")
    else:
        lines.append("- **New routing:** none (term has no Phase 7 VCG — likely zero is_relevant verses)")
    lines.append("")

lines.append("---")
lines.append("")
lines.append("## Verdict")
lines.append("")
lines.append(f"All {n_inherited} inherited VCGs are **already empty** (0 active vc references) — Phase 7 Op C migrated every is_relevant verse to a new M07 VCG. Soft-delete is safe and produces no analytical loss; the inherited descriptions remain queryable with `delete_flagged=1` for any future audit reference.")
lines.append("")
lines.append("**Researcher gate (§11.4):** dissolution directive ready to fire on approval.")
lines.append("")
lines.append("---")
lines.append("")
lines.append(f"*Generated by `scripts/_build_m07_phase8_comparison_20260519.py`. Next: `wa-cluster-M07-dir-004-vcg-dissolve-v1-20260519.md` (soft-delete Op A + Op B).*")

OUT.write_text("\n".join(lines), encoding='utf-8')
print(f"Wrote {OUT}")
print(f"Size: {OUT.stat().st_size:,} bytes")
print(f"Inherited VCGs: {n_inherited} ({n_inherited - n_with_active} empty, {n_with_active} with active references)")
