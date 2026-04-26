"""build_obs_catalogue_export.py — generic Observation Question Catalogue export.

Programme-wide reference file. Carries the 147 generic questions in Sections 1-5
(plus the section summary). Word-specific Extensions and Evidence-Flag questions
are NOT included — those belong inline in each word's readiness output (when
the registry being analysed is the source registry).

Source of truth: wa_obs_question_catalogue (in DB).

Output:
  data/imports/WA/Workflow/Framework_B/Session_B/wa-obs-catalogue-generic-v{n}-{YYYYMMDD}.json

Usage:
  python scripts/build_obs_catalogue_export.py
  python scripts/build_obs_catalogue_export.py --version 2  # for v2, v3, ...
"""
from __future__ import annotations
import argparse
import json
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("data", "bible_research.db")
OUT_DIR = os.path.join("data", "imports", "WA", "Workflow", "Framework_B", "Session_B")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--version", default="1", help="version number for filename suffix")
    ap.add_argument("--out", default=None, help="override output path")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT obs_id, question_code, section, source_word, source_registry_no,
               question_text, pattern_type, scope, status
          FROM wa_obs_question_catalogue
         WHERE (deleted = 0 OR deleted IS NULL)
           AND section LIKE 'Section %'
         ORDER BY section, obs_id
    """).fetchall()
    rows = [dict(r) for r in rows]

    by_section: dict = defaultdict(list)
    for r in rows:
        by_section[r['section']].append(r)

    schema_v = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    schema_version = schema_v[0] if schema_v else "unknown"

    payload = {
        "meta": {
            "title": "WA Observation Question Catalogue — Generic Questions (Sections 1-5)",
            "description": (
                "Programme-wide chapter questions used by Stage 2b. The 5 sections "
                "are the chapter structure of Stage 2b — analysts work through one "
                "section at a time. Apply to every word's readiness analysis."
            ),
            "generated_at": now_iso(),
            "schema_version": schema_version,
            "source_table": "wa_obs_question_catalogue",
            "filter": "section LIKE 'Section %' AND (deleted=0 OR deleted IS NULL)",
            "scope_note": (
                "Does NOT include word-specific Extensions (Compassion / Mercy / "
                "Love / Forgiveness Extensions) or Evidence-Flag Research Questions. "
                "Those are surfaced inline in each word's readiness output where "
                "applicable (per source_registry_no match or flag presence)."
            ),
            "version": f"v{args.version}",
            "total_questions": len(rows),
            "section_count": len(by_section),
        },
        "section_summary": [
            {"section": s, "n_questions": len(qs)}
            for s, qs in sorted(by_section.items())
        ],
        "sections": {
            s: [
                {
                    "obs_id": q['obs_id'],
                    "question_code": q['question_code'],
                    "section": q['section'],
                    "source_word": q['source_word'],
                    "source_registry_no": q['source_registry_no'],
                    "question_text": q['question_text'],
                    "pattern_type": q['pattern_type'],
                    "scope": q['scope'],
                    "status": q['status'],
                }
                for q in qs
            ]
            for s, qs in sorted(by_section.items())
        },
    }

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = (args.out or
             f"wa-obs-catalogue-generic-v{args.version}-{today_compact()}.json")
    out_path = out_dir / fname
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    sz = out_path.stat().st_size
    print(f"Wrote: {out_path}")
    print(f"  Size: {sz:,} bytes ({sz/1024:.1f} KB)")
    print(f"  Questions: {len(rows)} across {len(by_section)} sections:")
    for s, qs in sorted(by_section.items()):
        print(f"    {s}: {len(qs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
