"""Build the goodness (R067) Analytic-Readiness data-layer report.

One-shot script. Reads the database and produces a single markdown file
under research/investigations/word_deep_dive/goodness/. Produces the
"complete data layer" view — every piece of structured data the analysis
sits on top of, with no narrative interpretation.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

OUT = "research/investigations/word_deep_dive/goodness/goodness-2-analytic-readiness.md"


def main() -> int:
    conn = sqlite3.connect(os.path.join("database", "bible_research.db"))
    conn.row_factory = sqlite3.Row

    parts: list[str] = []
    P = parts.append

    # --- Header ---
    reg = conn.execute("SELECT * FROM word_registry WHERE no = 67").fetchone()
    P(f"# Goodness — Analytic-Readiness (R067)\n")
    P(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
    P(f"**Source:** SQLite `database/bible_research.db` (schema v3.17.0).\n")
    P(f"**Purpose:** the complete structured data layer for goodness — every term, group, dimension assignment, verse-classification count, anchor verse, quality flag, and cross-registry shared anchor that the analysis is built on. No narrative; the prose interpretation lives in [goodness-1-prose.md](goodness-1-prose.md).\n\n")

    # --- 1. Registry header ---
    P("## 1. Registry header\n")
    P("| Field | Value |\n| --- | --- |")
    P(f"| `no` | {reg['no']} |")
    P(f"| `id` (FK) | {reg['id']} |")
    P(f"| `word` | {reg['word']} |")
    P(f"| `category_hint` | {reg['category_hint']} |")
    P(f"| `dimensions` (registry-level label) | {reg['dimensions']} |")
    P(f"| `cluster_assignment` | {reg['cluster_assignment']} |")
    P(f"| `sb_classification` | {reg['sb_classification']} |")
    P(f"| `phase1_status` | {reg['phase1_status']} |")
    P(f"| `verse_context_status` | {reg['verse_context_status']} |")
    P(f"| `session_b_status` | {reg['session_b_status']} |")
    P(f"| `dim_review_status` | {reg['dim_review_status']} |")
    P(f"| `dim_review_version` | {reg['dim_review_version']} |")
    P(f"| `phase1_term_count` | {reg['phase1_term_count']} |")
    P(f"| `phase1_verse_count` | {reg['phase1_verse_count']} |")
    P(f"| `unique_term_count` | {reg['unique_term_count']} |")
    P(f"| `shared_term_count` | {reg['shared_term_count']} |")
    P(f"| `term_sharing_ratio` | {reg['term_sharing_ratio']} |")
    P(f"| `strongs_list` | {reg['strongs_list']} |")
    P("")
    P("**Description (researcher-authored, do not pipeline-overwrite):**\n")
    P(f"> {reg['description']}")
    P("")
    P(f"**`inference_note`:** {reg['inference_note'] or '(none)'}\n")
    if reg["word_synopsis"]:
        P(f"**`word_synopsis`:**\n\n> {reg['word_synopsis']}\n")
    P("")

    # --- 2. Term inventory ---
    P("## 2. Term inventory\n")
    rows = conn.execute(
        """
        SELECT ti.term_owner_type, ti.term_id, ti.transliteration, ti.language,
               ti.evidential_status, ti.term_introduction_rationale,
               ti.step_search_gloss, ti.occurrence_count,
               ti.term_introduction_source, ti.term_introduction_date,
               (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id AND (vr.delete_flagged = 0 OR vr.delete_flagged IS NULL)) AS active_v,
               (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id) AS total_v
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.registry_id = 67
        AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
        ORDER BY ti.term_owner_type DESC, ti.language, ti.term_id
        """,
    ).fetchall()
    n_owner = sum(1 for r in rows if r["term_owner_type"] == "OWNER")
    n_xref = sum(1 for r in rows if r["term_owner_type"] == "XREF")
    owner_active = sum(r["active_v"] for r in rows if r["term_owner_type"] == "OWNER")
    P(f"**Counts:** {n_owner} OWNER + {n_xref} XREF = {len(rows)} total. OWNER active verses = **{owner_active}**.\n")
    P("XREF rows show `active=0` because XREF verse copies are `delete_flagged=1` by design (verses live on the OWNER side; XREF rows are reference-only). The `total_v` column shows the verse count carried into the file when the term was first ingested.\n")
    P("\n### 2.1 OWNER terms\n")
    P("| Strong's | Translit | Lang | active | total | step_search_gloss | occ_count |")
    P("| --- | --- | --- | ---: | ---: | --- | ---: |")
    for r in rows:
        if r["term_owner_type"] != "OWNER":
            continue
        gloss = (r["step_search_gloss"] or "")[:60].replace("|", "/")
        P(f"| {r['term_id']} | {r['transliteration'] or ''} | {r['language']} | {r['active_v']} | {r['total_v']} | {gloss} | {r['occurrence_count'] or ''} |")
    P("\n### 2.2 XREF terms\n")
    P("| Strong's | Translit | Lang | total | step_search_gloss | occ_count | source |")
    P("| --- | --- | --- | ---: | --- | ---: | --- |")
    for r in rows:
        if r["term_owner_type"] != "XREF":
            continue
        gloss = (r["step_search_gloss"] or "")[:60].replace("|", "/")
        src = (r["term_introduction_source"] or "")[:30]
        P(f"| {r['term_id']} | {r['transliteration'] or ''} | {r['language']} | {r['total_v']} | {gloss} | {r['occurrence_count'] or ''} | {src} |")
    P("")

    # --- 3. Verse Context groups ---
    P("## 3. Verse Context groups (OWNER terms)\n")
    rows = conn.execute(
        """
        SELECT g.id, g.group_code, g.context_description, g.notes,
               mt.strongs_number,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = g.id AND vc.is_relevant = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)) AS rel_v,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = g.id AND vc.is_anchor = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)) AS anchor_v,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = g.id AND vc.is_related = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)) AS rel_related
        FROM verse_context_group g
        JOIN mti_terms mt ON mt.id = g.mti_term_id
        WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = 67)
        AND (g.delete_flagged = 0 OR g.delete_flagged IS NULL)
        ORDER BY g.group_code
        """,
    ).fetchall()
    P(f"**Total groups:** {len(rows)}.\n")
    for r in rows:
        P(f"### {r['group_code']} (Strong's {r['strongs_number']})\n")
        P(f"- **Relevant verses:** {r['rel_v']}  ·  **Anchor verses:** {r['anchor_v']}  ·  **Related verses:** {r['rel_related']}")
        P(f"- **Description:** {r['context_description']}")
        if r['notes']:
            P(f"- **Notes:** {r['notes']}")
        # Anchor verses list
        anchors = conn.execute(
            """
            SELECT vr.reference, vr.verse_text
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            WHERE vc.group_id = ? AND vc.is_anchor = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)
            ORDER BY vr.book_id, vr.chapter, vr.verse_num
            """,
            (r["id"],),
        ).fetchall()
        if anchors:
            P("- **Anchors:**")
            for a in anchors:
                txt = (a['verse_text'] or '').replace('\n', ' ').strip()
                P(f"  - **{a['reference']}** — {txt}")
        P("")

    # --- 4. Verse classification summary ---
    P("## 4. Verse classification summary\n")
    rows = conn.execute(
        """
        SELECT
          SUM(CASE WHEN vc.is_anchor = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS anchors,
          SUM(CASE WHEN vc.is_relevant = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS relevant,
          SUM(CASE WHEN vc.is_related = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS related,
          SUM(CASE WHEN vc.set_aside_reason IS NOT NULL AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS set_aside,
          COUNT(*) AS total_rows
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = 67)
        """,
    ).fetchone()
    P("| Metric | Count |\n| --- | ---: |")
    P(f"| Anchor verses | {rows['anchors']} |")
    P(f"| Relevant (in-group) | {rows['relevant']} |")
    P(f"| Related (cross-reference) | {rows['related']} |")
    P(f"| Set-aside (with reason) | {rows['set_aside']} |")
    P(f"| Total verse_context rows | {rows['total_rows']} |\n")

    # Set-aside reason breakdown
    sa = conn.execute(
        """
        SELECT vc.set_aside_reason, COUNT(*) AS n
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = 67)
        AND vc.set_aside_reason IS NOT NULL
        GROUP BY vc.set_aside_reason
        ORDER BY n DESC
        """,
    ).fetchall()
    if sa:
        P("**Set-aside reason breakdown:**\n")
        P("| Reason | Count |\n| --- | ---: |")
        for r in sa:
            P(f"| {r['set_aside_reason']} | {r['n']} |")
        P("")

    # --- 5. Cluster + dimension review state ---
    P("## 5. Cluster and dimension review\n")
    P(f"- **Cluster assignment:** `{reg['cluster_assignment']}`")
    P(f"- **`dim_review_status`:** `{reg['dim_review_status']}`  ·  **version:** `{reg['dim_review_version']}`")
    P(f"- **registry-level dimension label (`word_registry.dimensions`):** `{reg['dimensions']}`\n")
    sb_dim = conn.execute(
        "SELECT * FROM wa_session_b_dimensions WHERE registry_id = 67",
    ).fetchall()
    if sb_dim:
        P(f"**`wa_session_b_dimensions` rows:** {len(sb_dim)}")
        for d in sb_dim:
            P(f"\n#### Dimensions row id={d['id']} (raised {d['raised_date']}, instr `{d['session_b_instruction']}`)")
            for k in ("relational_environment", "spirit_soul_body", "inner_operations", "being"):
                v = d[k]
                if v:
                    P(f"- **{k}:** {v}")
                if d[k + "_note"]:
                    P(f"  - note: {d[k + '_note']}")
        P("")

    # --- 6. Dimension assignments per group (from prose; check via Session B findings) ---
    P("## 6. Group → dimension mapping (per Session B obslog v3)\n")
    P("The 12 OWNER groups carry the following dimension assignments per the goodness Session B Stage 2 work. Three are tagged provisional pending dimension review (SP-067-014, -016, and the GAP-N-related dimensions for 884-007 and 884-009).\n")
    P("| Group | Strong's | Dimension | Status |")
    P("| --- | --- | --- | --- |")
    P("| 884-001 | H2896A | 11 — Divine-Human Correspondence | confirmed |")
    P("| 884-002 | H2896A | 05 — Moral Character | confirmed |")
    P("| 884-003 | H2896A | 05 — Moral Character | provisional (SP-067-014: may belong to Dependence/Creatureliness 08) |")
    P("| 884-004 | H2896A | 03 — Cognition | confirmed |")
    P("| 884-005 | H2896A | 05 — Moral Character | provisional (SP-067-016: may be 11 — divine faithfulness focus) |")
    P("| 884-006 | H2896A | 03 — Cognition | confirmed |")
    P("| 884-007 | H2896A | 11 provisional | needs sub-category for ontological-creative pronouncement (GAP-N-003 → SP-067-026 substream) |")
    P("| 884-008 | H2896A | 04 — Volition | confirmed |")
    P("| 884-009 | H2896A | dimension uncertain | no current label fits cleanly (GAP-N-001/002 → SP-067-019/020 substream) |")
    P("| 885-001 | G0019 | 04 — Volition | confirmed |")
    P("| 886-001 | G5544 | 11 — Divine-Human Correspondence | confirmed (divine chrēstotēs) |")
    P("| 886-002 | G5544 | 05 — Moral Character | confirmed (Spirit-produced kindness) |")
    P("\n_Note: dimension assignments are not currently stored as a structured field per group in the schema — they are recorded in the obslog narrative and reflected in `wa_session_research_flags` SP-067-014/-016 and the migrated GAP-N pointers. This table is reproduced here for data-layer completeness; it is not derived from the DB._\n")

    # --- 7. Co-occurrence with other registries ---
    P("## 7. Co-occurrence with other registries (via shared verse references)\n")
    P("Other registries that share verse references with R067's OWNER active verses. Counts are distinct (book, chapter, verse) tuples; the same verse may appear across multiple R067 OWNER terms but is counted once. OWNER-only on both sides.\n")
    rows = conn.execute(
        """
        WITH r67_verses AS (
            SELECT DISTINCT vr.book_id, vr.chapter, vr.verse_num
            FROM wa_verse_records vr
            JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
            JOIN wa_file_index fi ON fi.id = ti.file_id
            WHERE fi.registry_id = 67
            AND ti.term_owner_type = 'OWNER'
            AND (vr.delete_flagged = 0 OR vr.delete_flagged IS NULL)
        )
        SELECT fi.registry_id AS reg_no, wr.word, COUNT(DISTINCT vr.book_id || '|' || vr.chapter || '|' || vr.verse_num) AS shared
        FROM wa_verse_records vr
        JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        JOIN r67_verses r67 ON r67.book_id = vr.book_id AND r67.chapter = vr.chapter AND r67.verse_num = vr.verse_num
        WHERE fi.registry_id != 67
        AND ti.term_owner_type = 'OWNER'
        AND (vr.delete_flagged = 0 OR vr.delete_flagged IS NULL)
        GROUP BY fi.registry_id, wr.word
        ORDER BY shared DESC
        LIMIT 25
        """,
    ).fetchall()
    P("| Registry | Word | Shared verses |")
    P("| ---: | --- | ---: |")
    for r in rows:
        try:
            reg_no = int(r["reg_no"])
            P(f"| R{reg_no:03d} | {r['word']} | {r['shared']} |")
        except (TypeError, ValueError):
            P(f"| R{r['reg_no']} | {r['word']} | {r['shared']} |")
    P("")

    # --- 8. Cross-registry links (explicit, in wa_cross_registry_links) ---
    P("## 8. Explicit cross-registry links (`wa_cross_registry_links`)\n")
    rows = conn.execute(
        """
        SELECT crl.linked_word, crl.linked_registry_id, ct.type_code, crl.connecting_term, crl.note
        FROM wa_cross_registry_links crl
        LEFT JOIN wa_crosslink_type ct ON ct.id = crl.connection_type_id
        JOIN wa_file_index fi ON fi.id = crl.file_id
        WHERE fi.registry_id = 67
        ORDER BY crl.linked_word
        """,
    ).fetchall()
    if rows:
        P("| Linked word | Reg | Type | Connecting term | Note |")
        P("| --- | --- | --- | --- | --- |")
        for r in rows:
            note = (r["note"] or "")[:80].replace("|", "/")
            P(f"| {r['linked_word']} | R{r['linked_registry_id']} | {r['type_code']} | {r['connecting_term']} | {note} |")
    else:
        P("_No explicit `wa_cross_registry_links` rows. Cross-registry connections in the prose are derived from shared anchor verses (see §7 above and §9 below) and recorded as SD pointers, not as structured link rows. This is a known data-layer gap._\n")
    P("")

    # --- 9. Shared anchor verses ---
    P("## 9. Shared anchor verses (verses anchoring multiple registries)\n")
    P("Verses where the same (book, chapter, verse) appears as an anchor in another registry's OWNER VC group.\n")
    rows = conn.execute(
        """
        WITH r67_anchors AS (
            SELECT DISTINCT vr.id AS verse_record_id, vr.reference, vr.book_id, vr.chapter, vr.verse_num
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = 67)
            AND vc.is_anchor = 1
            AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)
        )
        SELECT a.reference,
               GROUP_CONCAT(wr.word || '/R' || fi.registry_id, '; ') AS other_registries
        FROM r67_anchors a
        JOIN wa_verse_records vr ON vr.book_id = a.book_id AND vr.chapter = a.chapter AND vr.verse_num = a.verse_num
        JOIN verse_context vc2 ON vc2.verse_record_id = vr.id AND vc2.is_anchor = 1 AND (vc2.delete_flagged = 0 OR vc2.delete_flagged IS NULL)
        JOIN mti_terms mt ON mt.id = vc2.mti_term_id
        JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
        WHERE wr.no != 67
        GROUP BY a.reference
        ORDER BY a.book_id, a.chapter, a.verse_num
        """,
    ).fetchall()
    if rows:
        P("| Reference | Also anchored in |")
        P("| --- | --- |")
        for r in rows:
            others = r["other_registries"] or ""
            # Dedup
            seen = set()
            kept = []
            for piece in others.split("; "):
                if piece and piece not in seen:
                    seen.add(piece)
                    kept.append(piece)
            P(f"| {r['reference']} | {'; '.join(kept)} |")
    else:
        P("_None._\n")
    P("")

    # --- 10. Quality flags ---
    P("## 10. Quality flags (`wa_data_quality_flags`)\n")
    summary = conn.execute(
        """
        SELECT ft.flag_code, COUNT(*) AS n
        FROM wa_data_quality_flags qf
        LEFT JOIN wa_quality_flag_types ft ON ft.id = qf.flag_id
        JOIN wa_file_index fi ON fi.id = qf.file_id
        WHERE fi.registry_id = 67
        GROUP BY ft.flag_code
        ORDER BY n DESC
        """,
    ).fetchall()
    P("| flag_code | count |")
    P("| --- | ---: |")
    for r in summary:
        P(f"| {r['flag_code']} | {r['n']} |")
    P("")
    # Detail for the small / interesting flags
    detail = conn.execute(
        """
        SELECT ft.flag_code, qf.term_id, qf.description
        FROM wa_data_quality_flags qf
        LEFT JOIN wa_quality_flag_types ft ON ft.id = qf.flag_id
        JOIN wa_file_index fi ON fi.id = qf.file_id
        WHERE fi.registry_id = 67
        AND ft.flag_code IN ('VERSE_EVIDENCE_MINIMAL','VERSE_EVIDENCE_CONCENTRATED','VERSE_EVIDENCE_HIGH','VERSE_EVIDENCE_BREADTH_NOTE')
        ORDER BY ft.flag_code, qf.term_id
        """,
    ).fetchall()
    if detail:
        P("\n**Evidence-flag detail (informational, never gating per M29):**\n")
        P("| flag_code | term_id | description |")
        P("| --- | --- | --- |")
        for r in detail:
            desc = (r["description"] or "")[:140].replace("|", "/")
            P(f"| {r['flag_code']} | {r['term_id']} | {desc} |")
    P("")

    # --- 11. Counts of analytical artefacts ---
    P("## 11. Analytical artefact counts (Session B onward)\n")
    P("| Artefact | Count |\n| --- | ---: |")
    n = conn.execute("SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id = 67 AND delete_flag = 0").fetchone()[0]
    P(f"| Active Session B findings (`wa_session_b_findings`) | {n} |")
    n = conn.execute("SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id = 67 AND delete_flag = 0 AND finding_type = 'OBSERVATION'").fetchone()[0]
    P(f"| · of which OBSERVATION type | {n} |")
    n = conn.execute("SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id = 67 AND delete_flag = 0 AND finding_type LIKE 'DATA_ANOMALY%'").fetchone()[0]
    P(f"| · of which DATA_ANOMALY_* | {n} |")
    n = conn.execute("SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id = 67 AND delete_flag = 0 AND finding_type = 'DIMENSION_REVIEW'").fetchone()[0]
    P(f"| · of which DIMENSION_REVIEW | {n} |")
    n = conn.execute(
        """
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = 67)
        AND (resolved = 0 OR resolved IS NULL)
        """,
    ).fetchone()[0]
    P(f"| Open `wa_session_research_flags` (any type) | {n} |")
    n = conn.execute(
        """
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = 67)
        AND flag_code = 'SD_POINTER' AND (resolved = 0 OR resolved IS NULL)
        """,
    ).fetchone()[0]
    P(f"| · of which SD_POINTER (Session D) | {n} |")
    n = conn.execute(
        """
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = 67)
        AND flag_code = 'SB_FINDING' AND (resolved = 0 OR resolved IS NULL)
        """,
    ).fetchone()[0]
    P(f"| · of which SB_FINDING | {n} |")
    n = conn.execute(
        """
        SELECT COUNT(*) FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        WHERE f.registry_id = 67 AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        """,
    ).fetchone()[0]
    P(f"| Q&A finding-catalogue links | {n} |")
    n = conn.execute(
        """
        SELECT COUNT(DISTINCT entity_id) FROM wa_finding_entity_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        WHERE f.registry_id = 67 AND l.entity_type = 'verse'
        AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        """,
    ).fetchone()[0]
    P(f"| Distinct cited verses (`wa_finding_entity_links`, type=verse) | {n} |")
    n = conn.execute(
        """
        SELECT COUNT(DISTINCT entity_id) FROM wa_finding_entity_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        WHERE f.registry_id = 67 AND l.entity_type = 'group'
        AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        """,
    ).fetchone()[0]
    P(f"| Distinct cited groups (`wa_finding_entity_links`, type=group) | {n} |")
    P("\nThe linked detail of each finding lives in [goodness-3-open-flags.md](goodness-3-open-flags.md), [goodness-4-qa-list.md](goodness-4-qa-list.md), and [goodness-5-citations.md](goodness-5-citations.md).\n")

    out_path = OUT
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"Wrote {out_path} ({sum(len(p) for p in parts):,} chars / {len(parts)} lines)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
