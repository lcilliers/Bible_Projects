"""_apply_obslog_finisher_v1_20260427.py

Fill the remaining DB entries from the goodness obslog work:

  1. Chapter citations — parse the 5 chapter bodies for OBS-NNN, Q###,
     SP-NNN, DIM-... references and write rows to wa_prose_section_citations.
  2. Anchor verse analyses — find any anchor verse without analysis_note
     and re-extract from obslog v2 Unit 7 prose with a relaxed regex.
  3. Catalogue completeness sweep — any universal question with no link
     row at all for this registry → insert no_finding row.
  4. Audit report — chapter-vs-findings coherence; prose-vs-data audit.

Run --dry-run first; commits only with --live.
"""
from __future__ import annotations
import argparse
import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone


DB_PATH = os.path.join("data", "bible_research.db")
BACKUP_DIR = "backups"
OBSLOG_V2_PATH = os.path.join("data", "imports", "WA", "Patches",
                              "wa-obslog-ro-067-goodness-anlys-v2-20260426.md")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


# ── Chapter citation extraction ────────────────────────────────────────────


CITATION_PATTERNS = [
    # OBS-NNN-OBS-NNN (full finding label) or OBS-NNN (short)
    (re.compile(r"\bOBS-(?:\d+-OBS-)?(\d+)\b"), "observation"),
    # Q&A-NNN or just Q### inline
    (re.compile(r"\bQ&A-(\d+)\b"), "qa_seq"),
    (re.compile(r"\bQ(\d{3})\b"), "q_code"),
    # SD pointers SP-NNN or SP-NNN-NNN
    (re.compile(r"\b(SP-\d+(?:-\d+)?)\b"), "sd_pointer"),
    # Existing finding IDs DIM-NN-NNN or SBF-...
    (re.compile(r"\b(DIM-\d+-\d+|SBF-\w+(?:-\w+)*)\b"), "finding_id"),
]


def extract_citations_from_body(body: str) -> list:
    """Extract citation tokens with paragraph index."""
    citations = []
    paragraphs = re.split(r"\n\s*\n", body)  # split on blank lines
    for para_no, para in enumerate(paragraphs, start=1):
        for pat, kind in CITATION_PATTERNS:
            for m in pat.finditer(para):
                citations.append({
                    "kind": kind,
                    "raw": m.group(0),
                    "captured": m.group(1),
                    "paragraph_no": para_no,
                })
    # Dedup within paragraph (same citation_form mentioned twice in same para)
    seen = set()
    deduped = []
    for c in citations:
        key = (c["paragraph_no"], c["raw"])
        if key not in seen:
            seen.add(key)
            deduped.append(c)
    return deduped


def resolve_citation(conn, c: dict, registry_id: int) -> dict:
    """Resolve citation token to DB row IDs. Returns dict with resolved fields."""
    out = {
        "cited_finding_id": None,
        "cited_qa_link_id": None,
        "cited_sd_pointer_id": None,
        "cited_observation_seq": None,
        "citation_form": c["raw"],
        "paragraph_no": c["paragraph_no"],
    }
    if c["kind"] == "observation":
        # OBS-NNN — look up by suffix in finding_id
        seq = c["captured"]
        r = conn.execute(
            "SELECT id FROM wa_session_b_findings "
            "WHERE registry_id = ? AND finding_id LIKE ? "
            "AND (delete_flag = 0 OR delete_flag IS NULL) LIMIT 1",
            (registry_id, f"OBS-%-OBS-{seq.zfill(3)}"),
        ).fetchone()
        if r:
            out["cited_finding_id"] = r[0]
        out["cited_observation_seq"] = f"OBS-{seq.zfill(3)}"
    elif c["kind"] == "q_code":
        q_code = "Q" + c["captured"]
        r = conn.execute(
            "SELECT l.id FROM wa_finding_catalogue_links l "
            "JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id "
            "LEFT JOIN wa_session_b_findings f ON f.id = l.finding_id "
            "WHERE q.question_code = ? "
            "AND (f.registry_id = ? OR l.finding_id IS NULL) "
            "AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL) LIMIT 1",
            (q_code, registry_id),
        ).fetchone()
        if r:
            out["cited_qa_link_id"] = r[0]
    elif c["kind"] == "qa_seq":
        # Q&A-NNN — these are obslog-internal sequence numbers, no direct DB id;
        # only useful if we can map back, but we rely on Q### refs instead
        pass
    elif c["kind"] == "sd_pointer":
        sp_label = c["captured"]
        # Normalise: SP-NNN → SP-{reg}-NNN if no registry prefix
        if not re.match(r"SP-\d+-\d+", sp_label):
            # Add registry prefix
            m = re.match(r"SP-(\d+)", sp_label)
            if m:
                sp_label = f"SP-067-{m.group(1).zfill(3)}"
        r = conn.execute(
            "SELECT id FROM wa_session_research_flags "
            "WHERE registry_id = ? AND flag_code = 'SD_POINTER' AND flag_label = ? LIMIT 1",
            (registry_id, sp_label),
        ).fetchone()
        if r:
            out["cited_sd_pointer_id"] = r[0]
    elif c["kind"] == "finding_id":
        r = conn.execute(
            "SELECT id FROM wa_session_b_findings "
            "WHERE finding_id = ? AND (delete_flag = 0 OR delete_flag IS NULL) LIMIT 1",
            (c["captured"],),
        ).fetchone()
        if r:
            out["cited_finding_id"] = r[0]
    return out


def write_chapter_citations(conn, registry_id: int, ts: str, dry: bool) -> dict:
    """For each prose_section row (Stage 2c chapters), extract + write citations."""
    rows = conn.execute("""
        SELECT ps.id, ps.body, pst.code, pst.label
          FROM prose_section ps
          JOIN prose_section_type pst ON pst.id = ps.section_type_id
         WHERE ps.registry_id = ?
           AND pst.code LIKE 'sb_s2c_%'
           AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
    """, (registry_id,)).fetchall()
    written = skipped = 0
    unresolved = 0
    by_chapter = {}
    for ps_id, body, code, label in rows:
        cits = extract_citations_from_body(body or "")
        chapter_resolved = 0
        chapter_unresolved = 0
        for c in cits:
            resolved = resolve_citation(conn, c, registry_id)
            # Idempotency: don't insert duplicate (prose_section_id, citation_form, paragraph_no)
            existing = conn.execute(
                "SELECT id FROM wa_prose_section_citations "
                "WHERE prose_section_id = ? AND citation_form = ? AND paragraph_no = ? "
                "AND (delete_flagged = 0 OR delete_flagged IS NULL) LIMIT 1",
                (ps_id, resolved["citation_form"], resolved["paragraph_no"]),
            ).fetchone()
            if existing:
                skipped += 1
                continue
            if not dry:
                conn.execute("""
                    INSERT INTO wa_prose_section_citations
                        (prose_section_id, cited_finding_id, cited_qa_link_id,
                         cited_sd_pointer_id, cited_observation_seq, citation_form,
                         paragraph_no, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (ps_id, resolved["cited_finding_id"], resolved["cited_qa_link_id"],
                      resolved["cited_sd_pointer_id"], resolved["cited_observation_seq"],
                      resolved["citation_form"], resolved["paragraph_no"], ts))
            written += 1
            # Count "resolved" if any of the FK fields populated
            any_resolved = any([
                resolved["cited_finding_id"], resolved["cited_qa_link_id"],
                resolved["cited_sd_pointer_id"]
            ])
            if any_resolved:
                chapter_resolved += 1
            else:
                chapter_unresolved += 1
                unresolved += 1
        by_chapter[code] = {
            "label": label, "total": len(cits),
            "resolved": chapter_resolved, "unresolved": chapter_unresolved,
        }
    return {"written": written, "skipped": skipped, "unresolved": unresolved,
            "by_chapter": by_chapter}


# ── Anchor verse analyses (re-extraction) ──────────────────────────────────


def fill_missing_anchor_analyses(conn, registry_id: int, obslog_text: str,
                                 ts: str, dry: bool) -> dict:
    """Find anchor verses without analysis_note, re-extract from Unit 7 with relaxed regex."""
    missing = conn.execute("""
        SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id, vc.group_id,
               mt.strongs_number, vr.reference, g.group_code
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN verse_context_group g ON g.id = vc.group_id
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
         WHERE fi.word_registry_fk = ?
           AND vc.is_anchor = 1
           AND vc.delete_flagged = 0
           AND (vc.analysis_note IS NULL OR vc.analysis_note = '')
    """, (registry_id,)).fetchall()
    written = 0
    errors = []
    for row in missing:
        vc_id, vr_id, mti_id, gid, strongs, ref, gc = row
        # Try to find the verse block in Unit 7 with relaxed regex
        # Pattern: **{ref}** [optional emoji/marker] ... commentary until next anchor or sign-off
        pat = re.compile(
            re.escape(f"**{ref}**") + r"[^\n]*\n((?:.|\n)*?)(?=\n\*\*[A-Z][a-z]{2,3}\s+\d+:\d+(?:-\d+)?\*\*|\n\*\*Group\s+\d{3,4}-\d{3}\s+SIGN-OFF|\n###|\n##|\Z)",
        )
        m = pat.search(obslog_text)
        if not m:
            errors.append(f"{ref} (group {gc}, mti {mti_id}): no Unit 7 prose found")
            continue
        commentary = m.group(1).strip()
        if not commentary:
            errors.append(f"{ref}: matched but empty commentary")
            continue
        if not dry:
            conn.execute(
                "UPDATE verse_context SET analysis_note = ? WHERE id = ?",
                (commentary, vc_id),
            )
        written += 1
    return {"written": written, "errors": errors,
            "missing_count": len(missing)}


# ── Catalogue completeness sweep ───────────────────────────────────────────


def sweep_catalogue_completeness(conn, registry_id: int, ts: str, dry: bool) -> dict:
    """For every universal question with NO link record (linked to this reg or NULL),
    insert a coverage='no_finding' row with finding_id=NULL."""
    universal = conn.execute("""
        SELECT obs_id, question_code FROM wa_obs_question_catalogue
         WHERE (deleted = 0 OR deleted IS NULL) AND section LIKE 'Section %'
    """).fetchall()
    written = skipped = 0
    for q_obs_id, q_code in universal:
        existing = conn.execute("""
            SELECT l.id FROM wa_finding_catalogue_links l
              LEFT JOIN wa_session_b_findings f ON f.id = l.finding_id
             WHERE l.question_id = ?
               AND (f.registry_id = ? OR l.finding_id IS NULL)
               AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
             LIMIT 1
        """, (q_obs_id, registry_id)).fetchone()
        if existing:
            skipped += 1
            continue
        if not dry:
            conn.execute("""
                INSERT INTO wa_finding_catalogue_links
                    (finding_id, question_id, coverage, status,
                     mapped_date, session_b_note)
                VALUES (NULL, ?, 'no_finding', 'validated', ?, ?)
            """, (q_obs_id, ts[:10],
                  f"Question not surfaced in goodness analysis (R067)."))
        written += 1
    return {"written": written, "skipped": skipped}


# ── Audit ─────────────────────────────────────────────────────────────────


def audit(conn, registry_id: int) -> dict:
    """Prose-vs-findings audit per architecture v1 §10.4."""
    # Findings cited in no chapter
    findings_uncited = conn.execute("""
        SELECT f.id, f.finding_id, f.finding_type, SUBSTR(f.finding, 1, 80) AS preview
          FROM wa_session_b_findings f
         WHERE f.registry_id = ?
           AND f.status IN ('resolved_qa', 'resolved_sd')
           AND (f.delete_flag = 0 OR f.delete_flag IS NULL)
           AND NOT EXISTS (
              SELECT 1 FROM wa_prose_section_citations c
               WHERE c.cited_finding_id = f.id
                 AND (c.delete_flagged = 0 OR c.delete_flagged IS NULL)
          )
    """, (registry_id,)).fetchall()
    # Citations that don't resolve to any FK
    unresolved_citations = conn.execute("""
        SELECT c.id, c.citation_form, c.paragraph_no, ps.id AS prose_id
          FROM wa_prose_section_citations c
          JOIN prose_section ps ON ps.id = c.prose_section_id
         WHERE ps.registry_id = ?
           AND (c.delete_flagged = 0 OR c.delete_flagged IS NULL)
           AND c.cited_finding_id IS NULL
           AND c.cited_qa_link_id IS NULL
           AND c.cited_sd_pointer_id IS NULL
    """, (registry_id,)).fetchall()
    # Per-chapter coverage
    per_chapter = conn.execute("""
        SELECT pst.code, pst.label,
               COUNT(c.id) AS cite_count,
               SUM(CASE WHEN c.cited_finding_id IS NOT NULL THEN 1 ELSE 0 END) AS finding_links,
               SUM(CASE WHEN c.cited_qa_link_id IS NOT NULL THEN 1 ELSE 0 END) AS qa_links,
               SUM(CASE WHEN c.cited_sd_pointer_id IS NOT NULL THEN 1 ELSE 0 END) AS sd_links
          FROM prose_section ps
          JOIN prose_section_type pst ON pst.id = ps.section_type_id
          LEFT JOIN wa_prose_section_citations c ON c.prose_section_id = ps.id
                                                  AND (c.delete_flagged = 0 OR c.delete_flagged IS NULL)
         WHERE ps.registry_id = ?
           AND pst.code LIKE 'sb_s2c_%'
           AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
         GROUP BY pst.code, pst.label
         ORDER BY pst.code
    """, (registry_id,)).fetchall()
    return {
        "findings_uncited": [dict(zip(("id", "finding_id", "type", "preview"), r)) for r in findings_uncited],
        "unresolved_citations": [dict(zip(("id", "form", "para", "prose_id"), r)) for r in unresolved_citations],
        "per_chapter": [dict(zip(("code", "label", "cites", "f_links", "q_links", "s_links"), r)) for r in per_chapter],
    }


# ── Main ──────────────────────────────────────────────────────────────────


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, default=67)
    ap.add_argument("--obslog-v2", default=OBSLOG_V2_PATH)
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR,
                              f"bible_research_pre_obslog_finisher_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA foreign_keys = ON")
    reg_row = conn.execute("SELECT id, word FROM word_registry WHERE no = ?",
                          (args.registry,)).fetchone()
    registry_id = reg_row[0]
    word = reg_row[1]
    ts = now_iso()

    with open(args.obslog_v2, encoding="utf-8") as f:
        obslog_text = f.read()

    try:
        if args.live:
            conn.execute("BEGIN")

        cit_result = write_chapter_citations(conn, registry_id, ts, dry=not args.live)
        anchor_result = fill_missing_anchor_analyses(conn, registry_id, obslog_text, ts, dry=not args.live)
        cat_result = sweep_catalogue_completeness(conn, registry_id, ts, dry=not args.live)

        if args.live:
            conn.commit()
            print("[LIVE] committed.\n")
        else:
            print("[DRY-RUN] no writes attempted.\n")

        audit_result = audit(conn, registry_id)
    finally:
        conn.close()

    print("--- Citations ---")
    print(f"  written: {cit_result['written']}  skipped: {cit_result['skipped']}  unresolved: {cit_result['unresolved']}")
    for code, info in cit_result["by_chapter"].items():
        print(f"  {code} ({info['label']}): {info['total']} cites · {info['resolved']} resolved · {info['unresolved']} unresolved")
    print()
    print("--- Anchor analyses ---")
    print(f"  missing before: {anchor_result['missing_count']} · written now: {anchor_result['written']}")
    if anchor_result['errors']:
        for e in anchor_result['errors']:
            print(f"  ! {e}")
    print()
    print("--- Catalogue completeness sweep ---")
    print(f"  no_finding rows written: {cat_result['written']}  skipped (already linked): {cat_result['skipped']}")
    print()
    print("--- Audit ---")
    print(f"  Findings uncited in any chapter: {len(audit_result['findings_uncited'])}")
    print(f"  Unresolved citations (no FK populated): {len(audit_result['unresolved_citations'])}")
    print(f"  Per-chapter:")
    for ch in audit_result["per_chapter"]:
        print(f"    {ch['code']:12s} cites={ch['cites']:3d}  f={ch['f_links']:3d}  q={ch['q_links']:3d}  s={ch['s_links']:3d}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
