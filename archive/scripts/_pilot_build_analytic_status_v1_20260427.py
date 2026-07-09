"""_pilot_build_analytic_status_v1_20260427.py — analytic status .md generator skeleton.

Produces a per-registry Analytic Status `.md` for use as the SECOND input
in revision sessions (alongside the readiness `.md`). Per architecture
v1 §11.6 — two-input model:

  Readiness `.md`  → "here is the data as it stands now"
  Analytic Status `.md` → "here is what we previously concluded, with provenance"

For initial analyses: only the readiness .md is needed (analytic status has nothing).
For revisions: both inputs feed AI.

Sources from DB:
  - wa_session_b_findings (lifecycle journal)
  - wa_finding_catalogue_links (Q&A pairs + coverage)
  - wa_finding_entity_links (term/verse/group/dimension links)
  - wa_session_research_flags (SD pointers + flags)
  - prose_section (chapters)
  - wa_prose_section_citations (chapter↔findings linkage)
  - verse_context.analysis_note (anchor-verse analytical commentary)

Usage:
  python scripts/_pilot_build_analytic_status_v1_20260427.py --registry 67

Output:
  Sessions/Session_B/09_Analysis_output_logs/words/wa-{NNN}-{word}-analytic-status-v1-{date}.md  (+ .json)
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

DB_PATH = os.path.join("database", "bible_research.db")
# Analytic status outputs go to Sessions/Session_B/07_Analysis_Readiness_Status/
# (paired with the readiness output, both consumed by AI at session start).
OUT_DIR = os.path.join("Sessions", "Session_B", "07_Analysis_Readiness_Status")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def open_db(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def get_registry(conn, no: int):
    return conn.execute("SELECT id, no, word, session_b_status FROM word_registry WHERE no = ?", (no,)).fetchone()


def lifecycle_summary(conn, registry_id: int) -> dict:
    rows = conn.execute("""
        SELECT status, COUNT(*) AS n
          FROM wa_session_b_findings
         WHERE registry_id = ?
           AND (delete_flag = 0 OR delete_flag IS NULL)
         GROUP BY status
    """, (registry_id,)).fetchall()
    return {r['status'] or '(legacy_null)': r['n'] for r in rows}


def coverage_summary(conn, registry_id: int) -> dict:
    """Per-registry coverage counts for catalogue questions."""
    # Generic questions (Sections 1-5)
    n_universal = conn.execute("""
        SELECT COUNT(*) FROM wa_obs_question_catalogue
         WHERE (deleted = 0 OR deleted IS NULL) AND section LIKE 'Section %'
    """).fetchone()[0]
    # Catalogue links scoped to this registry's findings
    rows = conn.execute("""
        SELECT l.coverage, COUNT(*) AS n
          FROM wa_finding_catalogue_links l
          LEFT JOIN wa_session_b_findings f ON f.id = l.finding_id
         WHERE (l.finding_id IS NULL OR f.registry_id = ?)
           AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
         GROUP BY l.coverage
    """, (registry_id,)).fetchall()
    return {
        "universal_total": n_universal,
        "by_coverage": {r['coverage'] or '(unset)': r['n'] for r in rows},
    }


def get_resolved_qa(conn, registry_id: int) -> list:
    """Q&A pairs (resolved findings + their catalogue links)."""
    rows = conn.execute("""
        SELECT f.id AS finding_id, f.finding_id AS finding_label, f.finding,
               f.raised_date, f.term_id,
               l.id AS link_id, l.coverage, l.session_b_note AS answer,
               l.validated_date,
               q.obs_id, q.question_code, q.section, q.question_text
          FROM wa_session_b_findings f
          JOIN wa_finding_catalogue_links l ON l.finding_id = f.id
          JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
         WHERE f.registry_id = ?
           AND f.status = 'resolved_qa'
           AND (f.delete_flag = 0 OR f.delete_flag IS NULL)
           AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
         ORDER BY q.section, q.obs_id
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_resolved_sd(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT f.id AS finding_id, f.finding_id AS finding_label, f.finding,
               f.related_finding_id, f.raised_date,
               srf.flag_label, srf.priority, srf.description AS sd_text
          FROM wa_session_b_findings f
          LEFT JOIN wa_session_research_flags srf ON srf.id = f.related_finding_id
                                                  AND srf.flag_code = 'SD_POINTER'
         WHERE f.registry_id = ?
           AND f.status = 'resolved_sd'
           AND (f.delete_flag = 0 OR f.delete_flag IS NULL)
         ORDER BY f.raised_date
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_not_relevant(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT id, finding_id, finding_type, finding, obsolete_reason,
               raised_date, obsolete_date
          FROM wa_session_b_findings
         WHERE registry_id = ?
           AND status = 'not_relevant'
           AND (delete_flag = 0 OR delete_flag IS NULL)
         ORDER BY raised_date
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_chapters(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT ps.id, ps.heading, ps.body, ps.version, ps.author, ps.created_at,
               pst.code, pst.label
          FROM prose_section ps
          JOIN prose_section_type pst ON pst.id = ps.section_type_id
         WHERE ps.registry_id = ?
           AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
           AND pst.code LIKE 'sb_s2c_%'
         ORDER BY pst.code
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_anchor_analyses(conn, registry_id: int) -> list:
    """verse_context rows with analysis_note populated, for OWNER terms in this registry."""
    rows = conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vc.verse_record_id, vc.analysis_note,
               vc.is_anchor, vc.is_relevant, g.group_code,
               vr.reference, mt.strongs_number
          FROM verse_context vc
          JOIN verse_context_group g ON g.id = vc.group_id
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND vc.delete_flagged = 0
           AND vc.analysis_note IS NOT NULL
         ORDER BY mt.strongs_number, g.group_code, vr.book_id, vr.chapter, vr.verse_num
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_open_items(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT id, finding_id, finding_type, finding, raised_date, status, term_id
          FROM wa_session_b_findings
         WHERE registry_id = ?
           AND status = 'open'
           AND (delete_flag = 0 OR delete_flag IS NULL)
         ORDER BY raised_date DESC
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def fmt_blockquote(text: str) -> list:
    L = []
    for line in (text or "").split("\n"):
        L.append(f"> {line}" if line else ">")
    return L


def build(conn, registry_no: int) -> tuple:
    reg = get_registry(conn, registry_no)
    if not reg:
        raise SystemExit(f"Registry {registry_no} not found")
    registry_id = reg['id']
    word = reg['word']

    lifecycle = lifecycle_summary(conn, registry_id)
    coverage = coverage_summary(conn, registry_id)
    resolved_qa = get_resolved_qa(conn, registry_id)
    resolved_sd = get_resolved_sd(conn, registry_id)
    not_relevant = get_not_relevant(conn, registry_id)
    chapters = get_chapters(conn, registry_id)
    anchor_analyses = get_anchor_analyses(conn, registry_id)
    open_items = get_open_items(conn, registry_id)
    ts = now_iso()

    L = []
    L.append(f"# wa-{registry_no:03d}-{word} — Analytic Status (revision input)")
    L.append("")
    L.append(f"_Generated {ts}_")
    L.append("")
    L.append("This document is the second input for **revision sessions** (alongside the readiness `.md`). "
             "It captures previously-concluded analytical content with provenance.")
    L.append("")
    L.append("---")
    L.append("")

    # Section 1 — Lifecycle summary
    L.append("## 1. Lifecycle summary")
    L.append("")
    L.append(f"- **Session B status:** `{reg['session_b_status'] or 'NULL'}`")
    L.append(f"- **Resolved QA findings:** {lifecycle.get('resolved_qa', 0)}")
    L.append(f"- **Resolved SD findings:** {lifecycle.get('resolved_sd', 0)}")
    L.append(f"- **Open findings (must address this session):** {lifecycle.get('open', 0)}")
    L.append(f"- **Not-relevant (closed):** {lifecycle.get('not_relevant', 0)}")
    L.append(f"- **Superseded:** {lifecycle.get('superseded', 0)}")
    legacy = lifecycle.get('(legacy_null)', 0)
    if legacy:
        L.append(f"- **Legacy (status=NULL — pre-architecture):** {legacy}")
    L.append("")
    L.append(f"### Catalogue coverage (universal questions)")
    L.append("")
    L.append(f"- **Universal questions in catalogue:** {coverage['universal_total']}")
    for cov, n in coverage['by_coverage'].items():
        L.append(f"- `{cov}`: {n}")
    L.append("")
    L.append("---")
    L.append("")

    # Section 2 — Resolved QA findings
    L.append(f"## 2. Resolved findings — Q&A pairs ({len(resolved_qa)})")
    L.append("")
    if not resolved_qa:
        L.append("_None._")
        L.append("")
    else:
        # Group by section
        by_section = defaultdict(list)
        for r in resolved_qa:
            by_section[r['section'] or '(no section)'].append(r)
        for section, items in sorted(by_section.items()):
            L.append(f"### {section} ({len(items)})")
            L.append("")
            for r in items:
                L.append(f"#### `{r['question_code']}` — {r['question_text']}")
                L.append("")
                L.append(f"- **Coverage:** `{r['coverage']}` · **Validated:** {r['validated_date'] or '-'}")
                L.append(f"- **Source finding:** `{r['finding_label']}` (raised {r['raised_date']})")
                L.append("")
                L.append("**Answer:**")
                L.append("")
                L += fmt_blockquote(r['answer'])
                L.append("")
                if r.get('finding'):
                    L.append("**Source observation:**")
                    L.append("")
                    L += fmt_blockquote(r['finding'][:400] + ("…" if len(r.get('finding') or '') > 400 else ""))
                    L.append("")
    L.append("---")
    L.append("")

    # Section 3 — Resolved SD pointers
    L.append(f"## 3. Resolved findings — SD pointers ({len(resolved_sd)})")
    L.append("")
    if not resolved_sd:
        L.append("_None._")
        L.append("")
    else:
        for r in resolved_sd:
            L.append(f"### `{r['flag_label'] or 'unknown'}`")
            L.append("")
            L.append(f"- **Priority:** {r['priority'] or '-'} · **Source finding:** `{r['finding_label']}`")
            if r.get('sd_text'):
                L += fmt_blockquote(r['sd_text'])
                L.append("")
    L.append("---")
    L.append("")

    # Section 4 — Not-relevant
    L.append(f"## 4. Not-relevant findings ({len(not_relevant)})")
    L.append("")
    if not not_relevant:
        L.append("_None._")
        L.append("")
    else:
        L.append("| finding_id | type | reason | closed |")
        L.append("|---|---|---|---|")
        for r in not_relevant:
            L.append(f"| `{r['finding_id']}` | {r['finding_type']} | {r['obsolete_reason'] or '-'} | {r['obsolete_date'] or '-'} |")
        L.append("")
    L.append("---")
    L.append("")

    # Section 5 — Chapters
    L.append(f"## 5. Stage 2c chapters ({len(chapters)})")
    L.append("")
    if not chapters:
        L.append("_None._")
        L.append("")
    else:
        for ch in chapters:
            L.append(f"### {ch['label']} (v{ch['version']})")
            L.append("")
            L.append(f"- **Section type code:** `{ch['code']}` · **Author:** {ch['author']} · **Created:** {ch['created_at']}")
            L.append("")
            if ch.get('heading'):
                L.append(f"**Heading:** {ch['heading']}")
                L.append("")
            L.append("**Body:**")
            L.append("")
            L += fmt_blockquote(ch['body'])
            L.append("")
    L.append("---")
    L.append("")

    # Section 6 — Anchor verse analyses
    L.append(f"## 6. Anchor verse analytical notes ({len(anchor_analyses)})")
    L.append("")
    if not anchor_analyses:
        L.append("_None._")
        L.append("")
    else:
        # Group by term
        by_term = defaultdict(list)
        for a in anchor_analyses:
            by_term[a['strongs_number']].append(a)
        for strongs, items in by_term.items():
            L.append(f"### `{strongs}` ({len(items)} notes)")
            L.append("")
            for a in items:
                anchor_marker = " 🔵" if a['is_anchor'] else ""
                L.append(f"- **{a['reference']}**{anchor_marker} (`{a['group_code']}`):")
                L.append(f"  > {a['analysis_note']}")
            L.append("")
    L.append("---")
    L.append("")

    # Section 7 — Open items (carried forward)
    L.append(f"## 7. Open items carried forward ({len(open_items)})")
    L.append("")
    L.append("These must be resolved in the upcoming session — see also §N of the readiness `.md`.")
    L.append("")
    if not open_items:
        L.append("_None._")
        L.append("")
    else:
        L.append("| finding_id | type | raised | item (preview) |")
        L.append("|---|---|---|---|")
        for o in open_items:
            preview = ((o['finding'] or '')[:120].replace('|', '\\|').replace('\n', ' '))
            L.append(f"| `{o['finding_id']}` | {o['finding_type']} | {o['raised_date'] or '-'} | {preview} |")
        L.append("")
    L.append("---")
    L.append("")

    L.append(f"*End of analytic status — wa-{registry_no:03d}-{word}.*")

    payload = {
        "meta": {"generated_at": ts, "registry_no": registry_no, "word": word, "version": "v1"},
        "lifecycle": lifecycle,
        "coverage": coverage,
        "resolved_qa": resolved_qa,
        "resolved_sd": resolved_sd,
        "not_relevant": not_relevant,
        "chapters_count": len(chapters),
        "anchor_analyses_count": len(anchor_analyses),
        "open_items": open_items,
    }
    return "\n".join(L), payload


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    conn = open_db(args.db)
    md, payload = build(conn, args.registry)
    reg = get_registry(conn, args.registry)

    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = f"wa-{args.registry:03d}-{reg['word']}-analytic-status-v1-{today_compact()}"
    md_path = out_dir / f"{base}.md"
    json_path = out_dir / f"{base}.json"

    md_path.write_text(md, encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    print(f"Wrote: {md_path}  ({md_path.stat().st_size:,} bytes)")
    print(f"Wrote: {json_path}  ({json_path.stat().st_size:,} bytes)")
    print(f"\nLifecycle: {payload['lifecycle']}")
    print(f"Coverage: {payload['coverage']}")
    print(f"Resolved QA: {len(payload['resolved_qa'])} · Resolved SD: {len(payload['resolved_sd'])}")
    print(f"Chapters: {payload['chapters_count']} · Anchor analyses: {payload['anchor_analyses_count']}")
    print(f"Open items: {len(payload['open_items'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
