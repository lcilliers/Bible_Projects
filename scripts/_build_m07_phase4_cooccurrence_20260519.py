"""M07 Phase 4 co-occurrence list (informational, per v2_7 §7.3.1).

For each verse where a TRANSFERRING term has a verse_context row, list
other active terms (and their clusters) that also have a verse_context
row at the same wa_verse_records.id. Output written as markdown for the
Phase 4 directive MOTIVATION reference.

Transfers in scope (per v2 verdicts):
- H2616B cha.sad (mti_id=338) -> M05 (2 verses)
- H2617B che.sed (mti_id=1633) -> M05 (162 verses)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import sqlite3
from pathlib import Path
from datetime import datetime
from collections import defaultdict

DB = Path('database/bible_research.db')
OUT = Path('Sessions/Session_Clusters/M07/WA-M07-phase4-cooccurrence-list-v1-20260519.md')

TRANSFERS = [
    (338, 'H2616B', 'cha.sad', 'M05', 'to shame -> steadfast love'),
    (1633, 'H2617B', 'che.sed', 'M05', 'shame -> steadfast love'),
]

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

lines = []
NOW = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
lines.append(f"# M07 Phase 4 co-occurrence list (informational)")
lines.append("")
lines.append(f"**Date:** {NOW}")
lines.append(f"**Source cluster:** M07")
lines.append(f"**Per:** v2_7 §7.3.1 — informational input to Phase 4 directive MOTIVATION.")
lines.append("")
lines.append("For each transferring term, every verse where the term has a `verse_context` row is checked for other-cluster terms with their own `verse_context` rows at the same `wa_verse_records.id`. **Informational only** — does not gate the transfer.")
lines.append("")
lines.append("---")
lines.append("")

for mti_id, strongs, translit, dest_cluster, label in TRANSFERS:
    lines.append(f"## {strongs} {translit} (mti_id={mti_id}) -> {dest_cluster}")
    lines.append(f"")
    lines.append(f"Label: {label}")
    lines.append("")

    # All verse_context rows for this term
    vcs = cur.execute(
        """
        SELECT vc.id AS vc_id, vc.verse_record_id, vr.reference, vc.is_relevant
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE vc.mti_term_id = ? AND COALESCE(vc.delete_flagged,0)=0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
        """,
        (mti_id,),
    ).fetchall()
    lines.append(f"Total verse_context rows: **{len(vcs)}** ({sum(1 for v in vcs if v['is_relevant']==1)} is_relevant)")
    lines.append("")

    cooccurrence_summary = defaultdict(int)
    per_verse = []
    for vc in vcs:
        others = cur.execute(
            """
            SELECT other_mt.strongs_number, other_mt.transliteration, other_mt.cluster_code,
                   other_vc.is_relevant
            FROM verse_context other_vc
            JOIN mti_terms other_mt ON other_mt.id = other_vc.mti_term_id
            WHERE other_vc.verse_record_id = ?
              AND other_vc.mti_term_id != ?
              AND other_mt.cluster_code != 'M07'
              AND other_mt.cluster_code IS NOT NULL
              AND COALESCE(other_vc.delete_flagged,0)=0
              AND COALESCE(other_mt.delete_flagged,0)=0
            ORDER BY other_mt.cluster_code, other_mt.strongs_number
            """,
            (vc['verse_record_id'], mti_id),
        ).fetchall()
        if others:
            cluster_set = set()
            for o in others:
                cluster_set.add(o['cluster_code'])
                cooccurrence_summary[o['cluster_code']] += 1
            per_verse.append((vc['reference'], sorted(cluster_set), len(others)))

    # Summary table
    lines.append("### Co-occurrence cluster frequency (other-cluster terms at the same verse)")
    lines.append("")
    if cooccurrence_summary:
        lines.append("| Cluster | Co-occurrence count |")
        lines.append("|---|---:|")
        for k, v in sorted(cooccurrence_summary.items(), key=lambda x: -x[1]):
            lines.append(f"| {k} | {v} |")
    else:
        lines.append("(no co-occurrences with other clusters)")
    lines.append("")

    lines.append(f"### Per-verse co-occurrence (top 30 of {len(per_verse)})")
    lines.append("")
    if per_verse:
        lines.append("| Reference | Co-occurring clusters | Term-count |")
        lines.append("|---|---|---:|")
        for ref, clusters, n in per_verse[:30]:
            lines.append(f"| {ref} | {', '.join(clusters)} | {n} |")
        if len(per_verse) > 30:
            lines.append(f"| ... | (and {len(per_verse) - 30} more) | |")
    else:
        lines.append("(no per-verse co-occurrences)")
    lines.append("")
    lines.append("---")
    lines.append("")

lines.append("*End of co-occurrence list. Informational input to Phase 4 directive.*")

OUT.write_text("\n".join(lines), encoding='utf-8')
print(f"Wrote {OUT}")
print(f"Size: {OUT.stat().st_size:,} bytes")
conn.close()
