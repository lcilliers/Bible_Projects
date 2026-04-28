"""_apply_r030_chapter_citation_backfill_v1_20260428.py — One-off retrofit.

Extracts inline citations from the 5 R030 contrition chapters (sb_s2c_ch1..5)
and inserts them into wa_prose_section_citations. Forward-only: deduplicates
against existing citations for these prose_section.id rows.

Tokens recognised:
  OBS-030-NNN     → wa_session_b_findings.finding_id (OBS-NNN style)
  Q&A NNN | Q&A-NNN  → citation_form only (no FK)
  SP-030-NNN      → wa_session_research_flags.flag_label
  DIM-30-NNN      → wa_session_b_findings.finding_id

After v1_5 of the analysis-output instruction lands, the writer's
`write_chapters()` will do this on initial write. This one-off backfill
covers R030's chapters captured under v1_4 (2026-04-28).

Usage:
  python scripts/archive/_apply_r030_chapter_citation_backfill_v1_20260428.py
  python scripts/archive/_apply_r030_chapter_citation_backfill_v1_20260428.py --live
"""
from __future__ import annotations
import argparse
import os
import re
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
REGISTRY_NO = 30

# Order matters: OBS-NNN-NNN before bare OBS-NNN; SP-NNN-NNN before bare SP-NNN.
PATTERNS = [
    ("OBS_FULL",  re.compile(r"\bOBS-(\d{3})-OBS-(\d{3})\b")),  # R067 style
    ("OBS",       re.compile(r"\bOBS-(\d{3})-(\d{3})\b")),       # R030 style
    ("SP",        re.compile(r"\bSP-(\d{3})-(\d{3})\b")),
    ("DIM",       re.compile(r"\b(DIM-\d+-\d+)\b")),
    ("QA_HYPHEN", re.compile(r"\bQ&A-(\d{1,3})\b")),
    ("QA_SPACE",  re.compile(r"\bQ&A\s+(\d{1,3})\b")),
    ("Q_CODE",    re.compile(r"\bQ(\d{3})\b")),
    ("GAP",       re.compile(r"\b(GAP-N-\d{3}|GAP-S\d-\d{3})\b")),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def extract_citations(body: str, registry_no: int):
    """Walk body once, collect (token, ttype, position) preserving order; dedup later."""
    found = []
    for ttype, pat in PATTERNS:
        for m in pat.finditer(body):
            token = m.group(0)
            found.append((m.start(), ttype, token, m.groups()))
    found.sort(key=lambda x: x[0])
    return found


def resolve_token(conn, ttype: str, token: str, groups: tuple, registry_no: int):
    """Return (citation_form, cited_finding_id, cited_sd_pointer_id, cited_observation_seq)."""
    citation_form = token
    cited_finding_id = None
    cited_sd_pointer_id = None
    cited_observation_seq = None

    if ttype == "OBS_FULL":
        # Token like 'OBS-067-OBS-005'
        full_finding_id = token
        cited_observation_seq = full_finding_id
        r = conn.execute(
            "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
            (full_finding_id,),
        ).fetchone()
        if r:
            cited_finding_id = r[0]
    elif ttype == "OBS":
        # Token like 'OBS-030-007'
        full_finding_id = token  # same form
        cited_observation_seq = full_finding_id
        r = conn.execute(
            "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
            (full_finding_id,),
        ).fetchone()
        if r:
            cited_finding_id = r[0]
    elif ttype == "SP":
        flag_label = token  # 'SP-030-005'
        r = conn.execute(
            "SELECT id FROM wa_session_research_flags WHERE flag_label = ? AND flag_code = 'SD_POINTER'",
            (flag_label,),
        ).fetchone()
        if r:
            cited_sd_pointer_id = r[0]
    elif ttype == "DIM":
        # Token like 'DIM-30-001' or 'DIM-30-SD001'
        r = conn.execute(
            "SELECT id FROM wa_session_b_findings WHERE finding_id = ? AND (delete_flag=0 OR delete_flag IS NULL)",
            (token,),
        ).fetchone()
        if r:
            cited_finding_id = r[0]

    return citation_form, cited_finding_id, cited_sd_pointer_id, cited_observation_seq


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR, f"bible_research_pre_r030_citation_backfill_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"Backup: {backup}\n")

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    if args.live:
        conn.execute("BEGIN")

    try:
        # Get the 5 R030 chapters (current rows only)
        chapters = list(conn.execute("""
            SELECT ps.id, pst.code, ps.body, length(ps.body) AS len
              FROM prose_section ps
              JOIN prose_section_type pst ON pst.id = ps.section_type_id
             WHERE ps.registry_id = (SELECT id FROM word_registry WHERE no = ?)
               AND pst.source_stage = 'session_b'
               AND pst.code LIKE 'sb_s2c_ch%'
               AND ps.superseded_by_id IS NULL
               AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
             ORDER BY pst.sort_order
        """, (REGISTRY_NO,)))
        print(f"Chapters found: {len(chapters)}")
        if not chapters:
            print("ERROR: no chapters for R030.")
            return 1

        ts = now_iso()
        total_inserted = 0
        total_skipped_dup = 0
        total_unresolved = 0
        per_chapter = {}

        for ch in chapters:
            ps_id = ch["id"]
            code = ch["code"]
            body = ch["body"]

            tokens = extract_citations(body, REGISTRY_NO)
            # Dedup within chapter on (citation_form, ttype) — order preserved by first sighting
            seen = set()
            unique_tokens = []
            for pos, ttype, token, groups in tokens:
                key = (ttype, token)
                if key in seen:
                    continue
                seen.add(key)
                unique_tokens.append((ttype, token, groups))

            inserted = 0
            unresolved = 0
            for ttype, token, groups in unique_tokens:
                citation_form, fid, spid, obs_seq = resolve_token(conn, ttype, token, groups, REGISTRY_NO)

                # Idempotency check: skip if exact (prose_section_id, citation_form) already exists
                existing = conn.execute("""
                    SELECT id FROM wa_prose_section_citations
                     WHERE prose_section_id = ? AND citation_form = ?
                       AND (delete_flagged = 0 OR delete_flagged IS NULL)
                     LIMIT 1
                """, (ps_id, citation_form)).fetchone()
                if existing:
                    total_skipped_dup += 1
                    continue

                if not args.live:
                    inserted += 1
                else:
                    conn.execute("""
                        INSERT INTO wa_prose_section_citations
                            (prose_section_id, citation_form, cited_finding_id,
                             cited_sd_pointer_id, cited_observation_seq, paragraph_no, created_at)
                        VALUES (?, ?, ?, ?, ?, NULL, ?)
                    """, (ps_id, citation_form, fid, spid, obs_seq, ts))
                    inserted += 1

                if fid is None and spid is None and ttype in ("OBS", "OBS_FULL", "SP", "DIM"):
                    unresolved += 1
                    total_unresolved += 1

            per_chapter[code] = {"tokens": len(unique_tokens), "inserted": inserted, "unresolved": unresolved}
            total_inserted += inserted

        if args.live:
            conn.commit()
            print("[LIVE] committed.\n")
        else:
            print("[DRY-RUN] no writes.\n")

        # Summary
        print("=== Per-chapter summary ===")
        for code, d in per_chapter.items():
            print(f"  {code:14s} tokens={d['tokens']:3d}  inserted={d['inserted']:3d}  unresolved-FK={d['unresolved']}")
        print()
        print(f"Total inserted: {total_inserted}")
        print(f"Total skipped (already existed): {total_skipped_dup}")
        print(f"Total unresolved FKs (citation_form preserved, FK null): {total_unresolved}")

    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
