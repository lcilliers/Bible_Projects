"""_tmp_build_righteousness_audit_v1_20260502.py

Implements DIR-20260502-001 — Righteousness vocabulary programme-wide audit.

Read-only. No DB writes. Produces a single JSON output with 4 queries:

  Q1 — Programme-wide term inventory (mti_terms WHERE strongs IN target list,
       status IN ('extracted','extracted_thin'))
  Q2 — Registry ownership summary (Q1 grouped by owning registry)
  Q3 — Verse evidence footprint per term (vc_groups, dim_index rows, total
       verses, dominant_subject NULL count)
  Q4 — Cross-reference appearances per term (wa_term_inventory.term_owner_type
       = 'XREF' joined via file_id -> wa_file_index.word_registry_fk)

Output:
  data/exports/dimension_review/wa-dim-c10-righteousness-audit-20260502.json

Mirrored to:
  Sessions/Session_B/04_dimension_review_process input/
  Sessions/Session_B/words/139_righteousness/inputs/

Usage:
  python scripts/_tmp_build_righteousness_audit_v1_20260502.py
"""
from __future__ import annotations

import json
import os
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
TARGET_TERMS = [
    ("H6662", "tsaddiq", "righteous (adjective)"),
    ("H6663", "tsadaq", "to be righteous / to justify"),
    ("H6664", "tsedeq", "righteousness / justice"),
    ("H6665", "tsidqah", "righteousness (Aramaic)"),
    ("H6666", "tsedeqah", "righteousness"),
    ("G1342", "dikaios", "righteous (adjective)"),
    ("G1343", "dikaiosynē", "righteousness (noun)"),
    ("G1344", "dikaioō", "to justify / declare righteous"),
    ("G1345", "dikaiōma", "righteous requirement / act / decree"),
    ("G1346", "dikaiōs", "righteously (adverb)"),
    ("G1347", "dikaiōsis", "justification"),
    ("G1348", "dikastēs", "judge"),
    ("G1349", "dikē", "justice / penalty"),
]
TARGET_STRONGS = [t[0] for t in TARGET_TERMS]

OUT_NAME = "wa-dim-c10-righteousness-audit-20260502.json"
OUT_DEST = [
    os.path.join("data", "exports", "dimension_review", OUT_NAME),
    os.path.join("Sessions", "Session_B", "04_dimension_review_process input", OUT_NAME),
    os.path.join("Sessions", "Session_B", "words", "139_righteousness", "inputs", OUT_NAME),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def open_db() -> sqlite3.Connection:
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def expand_strongs(s: str) -> list[str]:
    """STEP commonly stores sub-letter variants (H6662G/H/I); the directive
    target list uses the bare canonical form. Look up all sub-variants too."""
    rows = []
    return rows  # Use a separate query in main; helper kept for clarity.


def query_term_inventory(conn) -> list:
    """Q1 — mti_terms rows for target Strong's family (incl. sub-letter
    variants H6662G, H6662H, etc., since STEP records them that way)."""
    # Match prefix-then-optional-letter
    rows = []
    for s in TARGET_STRONGS:
        for r in conn.execute("""
            SELECT mt.id AS mti_term_id, mt.strongs_number, mt.transliteration,
                   mt.gloss, mt.language, mt.status,
                   wr.no AS owning_registry_no, wr.word AS owning_registry_word,
                   wr.cluster_assignment, wr.session_b_status,
                   wr.verse_context_status, wr.dim_review_status
              FROM mti_terms mt
              LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
             WHERE (mt.strongs_number = ? OR mt.strongs_number GLOB ? || '[A-Z]')
               AND mt.status IN ('extracted', 'extracted_thin')
             ORDER BY mt.strongs_number, mt.id
        """, (s, s)).fetchall():
            rows.append(dict(r))
    return rows


def query_absent_strongs(conn) -> list:
    """Strong's from target list that returned 0 rows in Q1."""
    found = set()
    for s in TARGET_STRONGS:
        n = conn.execute("""
            SELECT COUNT(*) FROM mti_terms
             WHERE (strongs_number = ? OR strongs_number GLOB ? || '[A-Z]')
               AND status IN ('extracted','extracted_thin')
        """, (s, s)).fetchone()[0]
        if n > 0:
            found.add(s)
    absent = []
    for s, tr, gloss in TARGET_TERMS:
        if s not in found:
            absent.append({"strongs_number": s, "transliteration": tr,
                            "gloss": gloss,
                            "note": "No active mti_terms row found (extracted/extracted_thin). Term is absent from the programme."})
    return absent


def query_registry_summary(q1_rows: list) -> list:
    """Q2 — group Q1 by owning registry."""
    by_reg: dict = {}
    for r in q1_rows:
        no = r["owning_registry_no"]
        if no is None:
            continue
        if no not in by_reg:
            by_reg[no] = {
                "registry_no": no,
                "registry_word": r["owning_registry_word"],
                "cluster_assignment": r["cluster_assignment"],
                "session_b_status": r["session_b_status"],
                "verse_context_status": r["verse_context_status"],
                "dim_review_status": r["dim_review_status"],
                "owned_term_count": 0,
                "owned_strongs": [],
            }
        by_reg[no]["owned_term_count"] += 1
        by_reg[no]["owned_strongs"].append(r["strongs_number"])
    return [by_reg[k] for k in sorted(by_reg.keys())]


def query_verse_footprint(conn, q1_rows: list) -> list:
    """Q3 — per term: vc_groups + dim_index + total verse + dominant_subject NULL count."""
    out = []
    for r in q1_rows:
        mti = r["mti_term_id"]
        n_groups = conn.execute("""
            SELECT COUNT(*) FROM verse_context_group
             WHERE mti_term_id = ? AND (delete_flagged = 0 OR delete_flagged IS NULL)
        """, (mti,)).fetchone()[0]
        n_dim = conn.execute("""
            SELECT COUNT(*) FROM wa_dimension_index di
              JOIN verse_context_group vcg ON vcg.id = di.verse_context_group_id
             WHERE vcg.mti_term_id = ? AND (di.delete_flagged = 0 OR di.delete_flagged IS NULL)
               AND (vcg.delete_flagged = 0 OR vcg.delete_flagged IS NULL)
        """, (mti,)).fetchone()[0]
        total_verses = conn.execute("""
            SELECT COUNT(*) FROM verse_context
             WHERE mti_term_id = ? AND (delete_flagged = 0 OR delete_flagged IS NULL)
        """, (mti,)).fetchone()[0]
        n_ds_null = conn.execute("""
            SELECT COUNT(*) FROM wa_dimension_index di
              JOIN verse_context_group vcg ON vcg.id = di.verse_context_group_id
             WHERE vcg.mti_term_id = ? AND di.dominant_subject IS NULL
               AND (di.delete_flagged = 0 OR di.delete_flagged IS NULL)
               AND (vcg.delete_flagged = 0 OR vcg.delete_flagged IS NULL)
        """, (mti,)).fetchone()[0]
        out.append({
            "strongs_number": r["strongs_number"],
            "transliteration": r["transliteration"],
            "owning_registry_no": r["owning_registry_no"],
            "owning_registry_word": r["owning_registry_word"],
            "verse_context_group_count": n_groups,
            "wa_dimension_index_count": n_dim,
            "total_verse_count": total_verses,
            "dominant_subject_null_count": n_ds_null,
        })
    return out


def query_xref_appearances(conn, q1_rows: list) -> dict:
    """Q4 — XREF appearances per term.

    Schema mechanism: wa_term_inventory rows where term_owner_type='XREF'
    are joined to wa_file_index via file_id, and that gives the XREF
    registry via word_registry_fk -> word_registry.no.
    """
    schema_note = (
        "XREF mechanism: wa_term_inventory has one row per (term, file_id) "
        "occurrence. term_owner_type='OWNER' identifies the canonical home "
        "(file_id is on the owner registry's STEP extract file); "
        "term_owner_type='XREF' rows mark the term as in-scope for another "
        "registry's verse-context analysis without ownership. The XREF "
        "registry is derived via wa_file_index.word_registry_fk on the file "
        "the XREF row sits under."
    )
    rows_by_term: dict = {}
    for r in q1_rows:
        s = r["strongs_number"]
        if s not in rows_by_term:
            rows_by_term[s] = {
                "strongs_number": s,
                "transliteration": r["transliteration"],
                "owning_registry_no": r["owning_registry_no"],
                "owning_registry_word": r["owning_registry_word"],
                "xrefs": [],
            }
        for x in conn.execute("""
            SELECT DISTINCT wr.no AS xref_registry_no, wr.word AS xref_registry_word,
                   wr.cluster_assignment AS xref_cluster
              FROM wa_term_inventory ti
              JOIN wa_file_index wf ON wf.id = ti.file_id
              JOIN word_registry wr ON wr.id = wf.word_registry_fk
             WHERE ti.strongs_number = ?
               AND ti.term_owner_type = 'XREF'
               AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
               AND wr.no != ?
             ORDER BY wr.no
        """, (s, r["owning_registry_no"] or -1)).fetchall():
            rows_by_term[s]["xrefs"].append(dict(x))
    return {"schema_note": schema_note, "by_term": list(rows_by_term.values())}


def main() -> int:
    conn = open_db()
    ts = now_iso()

    q1 = query_term_inventory(conn)
    absent = query_absent_strongs(conn)
    q2 = query_registry_summary(q1)
    q3 = query_verse_footprint(conn, q1)
    q4 = query_xref_appearances(conn, q1)

    payload = {
        "meta": {
            "directive_id": "DIR-20260502-001",
            "produced_date": "2026-05-02",
            "produced_at": ts,
            "produced_by": "Claude Code (scripts/_tmp_build_righteousness_audit_v1_20260502.py)",
            "db_changes": "none",
            "target_strongs": [s for s, _, _ in TARGET_TERMS],
        },
        "completion_confirmation": {
            "queries_executed": ["Q1", "Q2", "Q3", "Q4"],
            "row_counts": {
                "Q1_term_inventory": len(q1),
                "Q2_registry_summary": len(q2),
                "Q3_verse_footprint": len(q3),
                "Q4_xref_appearances_terms": len(q4["by_term"]),
                "Q4_xref_appearances_total_xrefs": sum(len(t["xrefs"]) for t in q4["by_term"]),
            },
            "absent_target_strongs_in_Q1": [a["strongs_number"] for a in absent],
            "registries_outside_C10": sorted({
                r["owning_registry_no"]
                for r in q1
                if r["cluster_assignment"] and r["cluster_assignment"] != "C10"
            }),
            "schema_adaptations": [
                "Strongs lookup expanded to match sub-letter variants "
                "(H6662G/H/I etc.) via GLOB pattern, since STEP records sub-senses "
                "with letter suffixes; the directive target list uses bare canonical forms.",
                "XREF mechanism described in q_4 result schema_note: there is no "
                "dedicated xref join table; XREF associations live in "
                "wa_term_inventory.term_owner_type='XREF' joined via file_id -> "
                "wa_file_index -> word_registry.",
            ],
        },
        "query_1_term_inventory": q1,
        "query_1_absent_target_strongs": absent,
        "query_2_registry_summary": q2,
        "query_3_verse_footprint": q3,
        "query_4_xref_appearances": q4,
    }

    for path in OUT_DEST:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False, default=str)
        sz = os.path.getsize(path)
        print(f"Wrote: {path}  ({sz:,} bytes / {sz/1024:.1f} KB)")

    print()
    print("=== Completion confirmation ===")
    cc = payload["completion_confirmation"]
    print(f"  Q1 mti rows returned: {cc['row_counts']['Q1_term_inventory']}")
    print(f"  Q2 registries owning target terms: {cc['row_counts']['Q2_registry_summary']}")
    print(f"  Q3 verse footprint rows: {cc['row_counts']['Q3_verse_footprint']}")
    print(f"  Q4 terms surveyed: {cc['row_counts']['Q4_xref_appearances_terms']}; total XREF appearances: {cc['row_counts']['Q4_xref_appearances_total_xrefs']}")
    print(f"  Absent target Strongs (no extracted mti row): {cc['absent_target_strongs_in_Q1']}")
    print(f"  Registries outside C10 owning target terms: {cc['registries_outside_C10']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
