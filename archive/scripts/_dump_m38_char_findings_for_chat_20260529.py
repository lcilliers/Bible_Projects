"""Dump M38 per-characteristic findings to a single markdown file for AI-chat hand-off.

Companion to outputs/markdown/_tmp_m38_synthesis_dump.md (cluster-scope).
Produces outputs/markdown/_tmp_m38_charscope_dump.md.
"""
from __future__ import annotations
import sqlite3, sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

DB = "database/bible_research.db"
OUT = Path("outputs/markdown/_tmp_m38_charscope_dump.md")

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row

chars = list(conn.execute("""
    SELECT id, char_seq, short_name, definition
    FROM characteristic
    WHERE cluster_code='M38' AND COALESCE(delete_flagged,0)=0
    ORDER BY char_seq
"""))

parts = ["# M38 per-characteristic findings (1,323 rows across 7 characteristics)", ""]

for ch in chars:
    rows = list(conn.execute("""
        SELECT cf.id, cf.finding_text, cf.finding_status, q.question_code, q.tier, q.component_title, q.question_text
        FROM cluster_finding cf
        JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
        WHERE cf.cluster_code='M38' AND cf.characteristic_id=? AND COALESCE(cf.delete_flagged,0)=0
        ORDER BY q.tier, q.prompt_seq, cf.id
    """, (ch["id"],)))
    parts.append(f"## Characteristic {ch['char_seq']} — {ch['short_name']}")
    parts.append("")
    parts.append(f"**Definition:** {ch['definition'] or '(no definition stored)'}")
    parts.append("")
    parts.append(f"**Findings:** {len(rows)}")
    parts.append("")
    parts.append("---")
    parts.append("")
    for r in rows:
        parts.append(f"### {r['question_code']} {r['component_title']}")
        parts.append(f"**Q:** {r['question_text']}")
        parts.append("")
        parts.append(r["finding_text"] or "(empty)")
        parts.append("")
        parts.append("---")
        parts.append("")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(parts), encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
