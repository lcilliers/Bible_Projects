"""_tmp_build_word_data_package.py

Build a single comprehensive data-package markdown for a registry word.

For AI question-testing: the file aims to be self-contained — every piece of
analytical data the programme has on the word, in one document, with no
narrative interpretation. Reproduces (per word):

  · registry header
  · term inventory (OWNER + XREF)
  · verse context groups + anchor verses (with text)
  · verse classification summary + set-aside reasons
  · cluster + dimension review state
  · co-occurrence with other registries
  · shared anchor verses (verses that anchor multiple registries)
  · quality flag summary
  · all active findings (with: finding text, structured verse/group citations,
    Q&A back-refs, and text-scan recovery — DIM↔OBS chain, cross-finding
    refs, Strong's, transliterations, inline verse refs, inline group refs)
  · open flags (SD pointers + SB findings + others)
  · Q&A list — every active in-scope catalogue question with the registry's
    answer text or 'silent'

Usage:
  python scripts/_tmp_build_word_data_package.py --registry 67
  python scripts/_tmp_build_word_data_package.py --all
  python scripts/_tmp_build_word_data_package.py --registries 23,30,62,64,67,68,103,111
"""
from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_BASE = os.path.join("research", "investigations", "ai_question_test_bundle_20260429")

DEFAULT_8 = [23, 30, 62, 64, 67, 68, 103, 111]

STRONGS_RE = re.compile(r"\b([HG]\d{4}[A-Z]?)\b")
DIM_REF_RE = re.compile(r"\bDIM-\d+-\d+\b")
GROUP_CODE_RE = re.compile(r"\b\d{3,4}-\d{3}\b")


def find_verse_refs(text: str, book_codes: set[str]) -> list[str]:
    if not text:
        return []
    out: list[str] = []
    seen: set[str] = set()
    pat = re.compile(r"\b(\d?\s?[A-Z][a-z]{2})\s+(\d+):(\d+)(?:[–—\-]\d+)?\b")
    for m in pat.finditer(text):
        code, ch, vs = m.group(1).strip(), m.group(2), m.group(3)
        code_norm = code.replace(" ", "")
        if code_norm in book_codes:
            ref = f"{code_norm} {ch}:{vs}"
            if ref not in seen:
                seen.add(ref)
                out.append(ref)
    return out


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def build_word(conn: sqlite3.Connection, no: int, book_codes: set[str]) -> tuple[str, str]:
    """Return (slug, markdown content) for one registry word."""
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (no,)).fetchone()
    if not reg:
        return ("", f"# Registry {no} — not found\n")
    word = reg["word"]
    word_slug = slug(word)

    parts: list[str] = []
    P = parts.append

    P(f"# {word.title()} — Data Package (R{no:03d})\n")
    P(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
    P("**Source:** SQLite `database/bible_research.db` (schema v3.17.0).\n")
    P("**Purpose:** complete data package for AI question-testing — every term, group, anchor verse, finding, flag, Q&A link, and citation the programme has on this word, in one document. No narrative interpretation. Companion to similar packages for the other 7 words in this bundle.\n\n")

    # === 1. Registry header ===
    P("## 1. Registry header\n")
    P("| Field | Value |\n| --- | --- |")
    for k in ("no", "id", "word", "category_hint", "dimensions", "cluster_assignment",
              "sb_classification", "phase1_status", "verse_context_status",
              "session_b_status", "dim_review_status", "dim_review_version",
              "phase1_term_count", "phase1_verse_count",
              "unique_term_count", "shared_term_count", "term_sharing_ratio"):
        P(f"| `{k}` | {reg[k]} |")
    P("\n**Description:**\n")
    P(f"> {reg['description'] or '_(empty)_'}\n")
    if reg["inference_note"]:
        P(f"\n**`inference_note`:** {reg['inference_note']}\n")
    if reg["word_synopsis"]:
        P(f"\n**`word_synopsis`:**\n\n> {reg['word_synopsis']}\n")
    P("")

    # === 2. Term inventory ===
    P("## 2. Term inventory\n")
    rows = conn.execute(
        """
        SELECT ti.term_owner_type, ti.term_id, ti.transliteration, ti.language,
               ti.evidential_status, ti.term_introduction_rationale,
               ti.step_search_gloss, ti.occurrence_count,
               ti.term_introduction_source,
               (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id AND (vr.delete_flagged = 0 OR vr.delete_flagged IS NULL)) AS active_v,
               (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id = ti.id) AS total_v
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.registry_id = ?
        AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
        ORDER BY ti.term_owner_type DESC, ti.language, ti.term_id
        """,
        (no,),
    ).fetchall()
    n_owner = sum(1 for r in rows if r["term_owner_type"] == "OWNER")
    n_xref = sum(1 for r in rows if r["term_owner_type"] == "XREF")
    owner_active = sum(r["active_v"] for r in rows if r["term_owner_type"] == "OWNER")
    P(f"**Counts:** {n_owner} OWNER + {n_xref} XREF = {len(rows)} total. OWNER active verses = **{owner_active}**.\n")

    if rows:
        P("\n### 2.1 OWNER terms\n")
        P("| Strong's | Translit | Lang | active | total | step_search_gloss | occ_count |")
        P("| --- | --- | --- | ---: | ---: | --- | ---: |")
        for r in rows:
            if r["term_owner_type"] != "OWNER":
                continue
            gloss = (r["step_search_gloss"] or "")[:60].replace("|", "/")
            P(f"| {r['term_id']} | {r['transliteration'] or ''} | {r['language']} | {r['active_v']} | {r['total_v']} | {gloss} | {r['occurrence_count'] or ''} |")

        if any(r["term_owner_type"] == "XREF" for r in rows):
            P("\n### 2.2 XREF terms\n")
            P("| Strong's | Translit | Lang | total | step_search_gloss | occ_count |")
            P("| --- | --- | --- | ---: | --- | ---: |")
            for r in rows:
                if r["term_owner_type"] != "XREF":
                    continue
                gloss = (r["step_search_gloss"] or "")[:60].replace("|", "/")
                P(f"| {r['term_id']} | {r['transliteration'] or ''} | {r['language']} | {r['total_v']} | {gloss} | {r['occurrence_count'] or ''} |")
    P("")

    # === 3. Verse Context groups + anchors ===
    P("## 3. Verse Context groups (OWNER terms)\n")
    groups = conn.execute(
        """
        SELECT g.id, g.group_code, g.context_description, g.notes,
               mt.strongs_number,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = g.id AND vc.is_relevant = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)) AS rel_v,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = g.id AND vc.is_anchor = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)) AS anchor_v
        FROM verse_context_group g
        JOIN mti_terms mt ON mt.id = g.mti_term_id
        WHERE mt.owning_registry_fk = ?
        AND (g.delete_flagged = 0 OR g.delete_flagged IS NULL)
        ORDER BY g.group_code
        """,
        (reg["id"],),
    ).fetchall()
    P(f"**Total groups:** {len(groups)}.\n")
    for g in groups:
        P(f"### {g['group_code']} (Strong's {g['strongs_number']})\n")
        P(f"- Relevant: {g['rel_v']} · Anchor: {g['anchor_v']}")
        P(f"- **Description:** {g['context_description']}")
        if g["notes"]:
            P(f"- **Notes:** {g['notes']}")
        anchors = conn.execute(
            """
            SELECT vr.reference, vr.verse_text
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            WHERE vc.group_id = ? AND vc.is_anchor = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)
            ORDER BY vr.book_id, vr.chapter, vr.verse_num
            """,
            (g["id"],),
        ).fetchall()
        if anchors:
            P("- **Anchors:**")
            for a in anchors:
                txt = (a["verse_text"] or "").replace("\n", " ").strip()
                P(f"  - **{a['reference']}** — {txt}")
        P("")

    # === 4. Verse classification summary ===
    P("## 4. Verse classification summary\n")
    summary = conn.execute(
        """
        SELECT
          SUM(CASE WHEN vc.is_anchor = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS anchors,
          SUM(CASE WHEN vc.is_relevant = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS relevant,
          SUM(CASE WHEN vc.is_related = 1 AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS related,
          SUM(CASE WHEN vc.set_aside_reason IS NOT NULL AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL) THEN 1 ELSE 0 END) AS set_aside,
          COUNT(*) AS total_rows
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.owning_registry_fk = ?
        """,
        (reg["id"],),
    ).fetchone()
    P("| Metric | Count |\n| --- | ---: |")
    P(f"| Anchor verses | {summary['anchors'] or 0} |")
    P(f"| Relevant (in-group) | {summary['relevant'] or 0} |")
    P(f"| Related (cross-reference) | {summary['related'] or 0} |")
    P(f"| Set-aside (with reason) | {summary['set_aside'] or 0} |")
    P(f"| Total verse_context rows | {summary['total_rows'] or 0} |")
    sa = conn.execute(
        """
        SELECT vc.set_aside_reason, COUNT(*) AS n
        FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.owning_registry_fk = ?
        AND vc.set_aside_reason IS NOT NULL
        GROUP BY vc.set_aside_reason
        ORDER BY n DESC
        """,
        (reg["id"],),
    ).fetchall()
    if sa:
        P("\n**Set-aside breakdown:**\n")
        P("| Reason | Count |\n| --- | ---: |")
        for r in sa:
            P(f"| {r['set_aside_reason']} | {r['n']} |")
    P("")

    # === 5. Co-occurrence with other registries ===
    P("## 5. Co-occurrence with other registries (top 25)\n")
    P("Other registries that share verse references with this word's OWNER active verses.\n")
    rows = conn.execute(
        """
        WITH r_verses AS (
            SELECT DISTINCT vr.book_id, vr.chapter, vr.verse_num
            FROM wa_verse_records vr
            JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
            JOIN wa_file_index fi ON fi.id = ti.file_id
            WHERE fi.registry_id = ?
            AND ti.term_owner_type = 'OWNER'
            AND (vr.delete_flagged = 0 OR vr.delete_flagged IS NULL)
        )
        SELECT fi.registry_id AS reg_no, wr.word,
               COUNT(DISTINCT vr.book_id || '|' || vr.chapter || '|' || vr.verse_num) AS shared
        FROM wa_verse_records vr
        JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        JOIN r_verses r0 ON r0.book_id = vr.book_id AND r0.chapter = vr.chapter AND r0.verse_num = vr.verse_num
        WHERE fi.registry_id != ?
        AND ti.term_owner_type = 'OWNER'
        AND (vr.delete_flagged = 0 OR vr.delete_flagged IS NULL)
        GROUP BY fi.registry_id, wr.word
        ORDER BY shared DESC
        LIMIT 25
        """,
        (no, no),
    ).fetchall()
    if rows:
        P("| Registry | Word | Shared verses |")
        P("| ---: | --- | ---: |")
        for r in rows:
            try:
                rn = int(r["reg_no"])
                P(f"| R{rn:03d} | {r['word']} | {r['shared']} |")
            except (TypeError, ValueError):
                P(f"| R{r['reg_no']} | {r['word']} | {r['shared']} |")
    else:
        P("_None._\n")
    P("")

    # === 6. Shared anchor verses ===
    P("## 6. Shared anchor verses (anchored in multiple registries)\n")
    rows = conn.execute(
        """
        WITH r_anchors AS (
            SELECT DISTINCT vr.id AS verse_record_id, vr.reference, vr.book_id, vr.chapter, vr.verse_num
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.owning_registry_fk = ?
            AND vc.is_anchor = 1
            AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)
        )
        SELECT a.reference,
               GROUP_CONCAT(wr.word || '/R' || fi.registry_id, '; ') AS others
        FROM r_anchors a
        JOIN wa_verse_records vr ON vr.book_id = a.book_id AND vr.chapter = a.chapter AND vr.verse_num = a.verse_num
        JOIN verse_context vc2 ON vc2.verse_record_id = vr.id AND vc2.is_anchor = 1 AND (vc2.delete_flagged = 0 OR vc2.delete_flagged IS NULL)
        JOIN mti_terms mt ON mt.id = vc2.mti_term_id
        JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
        WHERE wr.no != ?
        GROUP BY a.reference
        ORDER BY a.book_id, a.chapter, a.verse_num
        """,
        (reg["id"], no),
    ).fetchall()
    if rows:
        P("| Reference | Also anchored in |")
        P("| --- | --- |")
        for r in rows:
            others = r["others"] or ""
            seen, kept = set(), []
            for piece in others.split("; "):
                if piece and piece not in seen:
                    seen.add(piece)
                    kept.append(piece)
            P(f"| {r['reference']} | {'; '.join(kept)} |")
    else:
        P("_None._\n")
    P("")

    # === 7. Quality flags summary ===
    P("## 7. Quality flags summary\n")
    qf = conn.execute(
        """
        SELECT ft.flag_code, COUNT(*) AS n
        FROM wa_data_quality_flags qf
        LEFT JOIN wa_quality_flag_types ft ON ft.id = qf.flag_id
        JOIN wa_file_index fi ON fi.id = qf.file_id
        WHERE fi.registry_id = ?
        GROUP BY ft.flag_code
        ORDER BY n DESC
        """,
        (no,),
    ).fetchall()
    if qf:
        P("| flag_code | count |\n| --- | ---: |")
        for r in qf:
            P(f"| {r['flag_code']} | {r['n']} |")
    else:
        P("_None._")
    P("")

    # === 8. Findings (with full citation recovery) ===
    P("## 8. Findings (with all support categories)\n")
    findings = conn.execute(
        """
        SELECT id, finding_id, finding_type, status, raised_date, finding,
               anchor_verses, thin_evidence, session_b_instruction
        FROM wa_session_b_findings
        WHERE registry_id = ? AND delete_flag = 0
        ORDER BY
            CASE finding_type
                WHEN 'DIMENSION_REVIEW' THEN 0
                WHEN 'OBSERVATION' THEN 1
                ELSE 2
            END,
            finding_id
        """,
        (no,),
    ).fetchall()
    P(f"**Total active findings:** {len(findings)}.\n")
    if findings:
        # Pre-build registry's term transliteration whitelist
        term_translits = conn.execute(
            """
            SELECT DISTINCT ti.term_id, ti.transliteration
            FROM wa_term_inventory ti
            JOIN wa_file_index fi ON fi.id = ti.file_id
            WHERE fi.registry_id = ?
            AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
            AND ti.transliteration IS NOT NULL AND ti.transliteration != ''
            """,
            (no,),
        ).fetchall()
        translit_map = {
            r["transliteration"]: r["term_id"] for r in term_translits
            if r["transliteration"] and len(r["transliteration"]) >= 4
        }
        # Group code whitelist
        group_codes = {g["group_code"] for g in groups}
        # Finding-id map for cross-ref
        by_fid = {f["finding_id"]: f for f in findings}

        truly_orphan: list[str] = []

        for f in findings:
            P(f"### {f['finding_id']}  ·  {f['finding_type']}  ·  status `{f['status']}`")
            meta = f"_Raised {f['raised_date']}._"
            if f["thin_evidence"]:
                meta += "  **thin_evidence=1**"
            if f["session_b_instruction"]:
                meta += f"  Instr: `{f['session_b_instruction']}`"
            P(meta + "\n")

            P("**Finding.**\n")
            P("> " + (f["finding"] or "_(empty)_").replace("\n", "\n> "))
            P("")

            if f["anchor_verses"]:
                P(f"**`anchor_verses` field:** `{f['anchor_verses']}`\n")

            verses = conn.execute(
                """
                SELECT vr.id, vr.reference, vr.verse_text, vr.term_id, vr.transliteration
                FROM wa_finding_entity_links l
                JOIN wa_verse_records vr ON vr.id = l.entity_id
                WHERE l.finding_id = ? AND l.entity_type = 'verse'
                AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
                ORDER BY vr.book_id, vr.chapter, vr.verse_num
                """,
                (f["id"],),
            ).fetchall()
            if verses:
                P(f"**Cited verses ({len(verses)}):**\n")
                seen_refs = set()
                for v in verses:
                    if v["reference"] in seen_refs:
                        continue
                    seen_refs.add(v["reference"])
                    txt = (v["verse_text"] or "").replace("\n", " ").strip()
                    P(f"- **{v['reference']}** ({v['term_id']} *{v['transliteration']}*) — {txt}")
                P("")

            cited_groups = conn.execute(
                """
                SELECT g.group_code, g.context_description, mt.strongs_number
                FROM wa_finding_entity_links l
                JOIN verse_context_group g ON g.id = l.entity_id
                JOIN mti_terms mt ON mt.id = g.mti_term_id
                WHERE l.finding_id = ? AND l.entity_type = 'group'
                AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
                ORDER BY g.group_code
                """,
                (f["id"],),
            ).fetchall()
            if cited_groups:
                P(f"**Cited groups ({len(cited_groups)}):**\n")
                for g in cited_groups:
                    P(f"- **{g['group_code']}** ({g['strongs_number']}) — {g['context_description']}")
                P("")

            qa = conn.execute(
                """
                SELECT q.question_code, q.question_text, l.coverage, l.section_b_note AS sbn,
                       q.section, q.deleted
                FROM wa_finding_catalogue_links l
                JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
                WHERE l.finding_id = ?
                AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
                ORDER BY q.question_code
                """,
                (f["id"],),
            ).fetchall() if False else conn.execute(
                """
                SELECT q.question_code, q.question_text, l.coverage, l.session_b_note AS sbn,
                       q.section, q.deleted
                FROM wa_finding_catalogue_links l
                JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
                WHERE l.finding_id = ?
                AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
                ORDER BY q.question_code
                """,
                (f["id"],),
            ).fetchall()
            if qa:
                P(f"**Catalogue Q&A links ({len(qa)}):**\n")
                for q in qa:
                    tag = " *(catalogue row soft-deleted)*" if q["deleted"] else ""
                    P(f"- **{q['question_code']}** [{q['coverage']}]{tag} — {(q['question_text'] or '')[:160]}")
                P("")

            # Text-scan recovery
            resolves_chain: list[str] = []
            if f["finding_type"] == "DIMENSION_REVIEW" and f["finding_id"]:
                for ofid, oth in by_fid.items():
                    if ofid == f["finding_id"]:
                        continue
                    if oth["finding_type"] != "OBSERVATION":
                        continue
                    if oth["finding"] and f["finding_id"] in oth["finding"]:
                        resolves_chain.append(ofid)
            resolves_dim: list[str] = []
            if f["finding_type"] == "OBSERVATION" and f["finding"]:
                for dim_ref in DIM_REF_RE.findall(f["finding"]):
                    if dim_ref in by_fid and dim_ref != f["finding_id"]:
                        resolves_dim.append(dim_ref)
            if resolves_chain:
                P(f"**Resolved by ({len(resolves_chain)} OBS):** " + ", ".join(resolves_chain) + "\n")
            if resolves_dim:
                P(f"**Resolves DIM:** " + ", ".join(sorted(set(resolves_dim))) + "\n")

            cross_refs_in: list[str] = []
            if f["finding_id"]:
                for ofid, oth in by_fid.items():
                    if ofid == f["finding_id"] or ofid in resolves_chain:
                        continue
                    if oth["finding"] and f["finding_id"] in oth["finding"]:
                        cross_refs_in.append(ofid)
            if cross_refs_in:
                P(f"**Referenced by ({len(cross_refs_in)} other finding(s)):** " + ", ".join(cross_refs_in[:20]) + "\n")

            cross_refs_out: list[str] = []
            if f["finding"]:
                for ofid in by_fid:
                    if ofid == f["finding_id"] or ofid in resolves_dim:
                        continue
                    if ofid in f["finding"]:
                        cross_refs_out.append(ofid)
            if cross_refs_out:
                P(f"**References ({len(cross_refs_out)} other finding(s)):** " + ", ".join(cross_refs_out[:20]) + "\n")

            body_strongs: list[str] = []
            if f["finding"]:
                seen_s: set[str] = set()
                for m in STRONGS_RE.findall(f["finding"]):
                    if m not in seen_s:
                        seen_s.add(m)
                        body_strongs.append(m)
            if body_strongs:
                P(f"**Strong's references in body:** " + ", ".join(body_strongs) + "\n")

            body_translits: list[str] = []
            if f["finding"]:
                for tl, tid in translit_map.items():
                    if tl in f["finding"] and tid not in body_strongs:
                        body_translits.append(f"{tl} ({tid})")
            if body_translits:
                P(f"**Term transliterations in body:** " + ", ".join(body_translits) + "\n")

            cited_refs_set = {v["reference"] for v in verses}
            inline_verses = [v for v in find_verse_refs(f["finding"] or "", book_codes) if v not in cited_refs_set]
            if inline_verses:
                P(f"**Verse references in body (not in entity_links):** " + ", ".join(inline_verses) + "\n")

            cited_groups_set = {g["group_code"] for g in cited_groups}
            inline_groups: list[str] = []
            if f["finding"]:
                seen_g: set[str] = set()
                for m in GROUP_CODE_RE.findall(f["finding"]):
                    if m in group_codes and m not in cited_groups_set and m not in seen_g:
                        seen_g.add(m)
                        inline_groups.append(m)
            if inline_groups:
                P(f"**Group references in body (not in entity_links):** " + ", ".join(inline_groups) + "\n")

            any_support = (
                verses or cited_groups or qa or resolves_chain or resolves_dim
                or cross_refs_in or cross_refs_out or body_strongs
                or body_translits or inline_verses or inline_groups
            )
            if not any_support:
                P("_(no support — orphan)_\n")
                truly_orphan.append(f["finding_id"])
            P("---\n")

        if truly_orphan:
            P(f"\n**Orphan findings ({len(truly_orphan)}):** " + ", ".join(truly_orphan) + "\n")

    # === 9. Open flags ===
    P("\n## 9. Open flags (Session B + Session D)\n")
    flags = conn.execute(
        """
        SELECT flag_code, flag_label, priority, session_target, raised_date,
               session_raised, description, strongs_reference
        FROM wa_session_research_flags
        WHERE registry_id = ?
        AND (resolved = 0 OR resolved IS NULL)
        ORDER BY flag_code, flag_label
        """,
        (reg["id"],),
    ).fetchall()
    P(f"**Total open flags:** {len(flags)}.\n")
    if flags:
        by_code: dict[str, list] = {}
        for r in flags:
            by_code.setdefault(r["flag_code"], []).append(r)
        for code in sorted(by_code):
            items = by_code[code]
            P(f"\n### {code} — {len(items)}\n")
            for r in items:
                P(f"#### {r['flag_label']}  ·  {r['priority']}  ·  target: {r['session_target']}")
                meta = f"_Raised {r['raised_date']}._"
                if r["strongs_reference"]:
                    meta += f"  Strong's: {r['strongs_reference']}."
                if r["session_raised"]:
                    meta += f"  Source: {r['session_raised']}."
                P(meta + "\n")
                P(r["description"] or "_(no description)_")
                P("")

    # === 10. v2 prompts (tier-and-component structure) ===
    P("\n## 10. v2 prompts — observation framework T0-T7\n")
    P("Catalogue v2 prompts (189 total across 56 components in 8 tiers). The v1 generic catalogue was retired on 2026-04-30 (`status='redundant_v1'`); historical v1 Q&A links to findings are preserved and surfaced separately in §11.\n")
    P("**Supporting data within this package:** for every component, the section pointers below tell the AI where in this file to look for evidence to answer the prompt. The pointers reflect the data-adequacy assessment ([data-adequacy-assessment-v2-20260430.md](../../investigations/ai_question_test_bundle_20260429/data-adequacy-assessment-v2-20260430.md)). Adequacy codes: ✅ adequate · ⚠️ partial · 🚧 gap.\n")

    TIER_DATA_POINTERS = {
        "T0": ("✅⚠️", "§3 (VC groups + anchor verses), §6 (shared anchors), §8 (findings)"),
        "T1": ("✅⚠️", "§1 (registry description), §2 (term inventory), §3 (groups), §4 (classification summary), §8 (findings)"),
        "T2": ("⚠️🚧", "§3 (anchor verse text), §5 (co-occurrence — look for spirit/soul/heart/mind registries), §8 (findings); body-part links are not structurally captured"),
        "T3": ("⚠️", "§5 (co-occurrence with faculty registries — perception/cognition/volition/etc.), §8 (findings); no structured engaged-faculty flag"),
        "T4": ("✅⚠️🚧", "§3 (verse text), §5 (co-occurrence), §6 (shared anchors), §8 (findings), §9 (open flags); spiritual-beings interface is a known sparse area"),
        "T5": ("⚠️🚧", "§3 (verse text), §8 (findings); sequence/mechanism/trajectory are interpretive — no structured capture"),
        "T6": ("✅⚠️", "§5 (co-occurrence), §6 (shared anchors), §2 (term inventory + transliterations); per-group dimension assignment is a partial gap"),
        "T7": ("⚠️🚧", "§2 (term inventory + Strong's + glosses); literary-form and human-science framing are not stored"),
    }

    # Active v2 prompts for this word
    v2_q = conn.execute(
        """
        SELECT obs_id, question_code, question_text, tier, component_code,
               component_title, prompt_seq, section
        FROM wa_obs_question_catalogue
        WHERE (deleted=0 OR deleted IS NULL)
        AND tier IS NOT NULL
        ORDER BY tier, component_code, prompt_seq, question_code
        """,
    ).fetchall()

    P(f"**Total v2 prompts:** {len(v2_q)}.  No findings are linked to v2 prompts yet — this is the new analytical surface against which AI will run the next round of Session B work.\n")

    by_tier: dict[str, dict[str, list]] = {}
    tier_titles: dict[str, str] = {}
    for q in v2_q:
        tier_titles[q["tier"]] = q["section"]
        by_tier.setdefault(q["tier"], {}).setdefault(q["component_code"], []).append(q)

    for tier_code in sorted(by_tier):
        tier_title = tier_titles[tier_code]
        adeq, pointer = TIER_DATA_POINTERS.get(tier_code, ("⚠️", ""))
        n_prompts = sum(len(prompts) for prompts in by_tier[tier_code].values())
        P(f"\n### {tier_title}  ({adeq})\n")
        P(f"_{len(by_tier[tier_code])} components · {n_prompts} prompts._\n")
        P(f"**Supporting data:** {pointer}\n")

        for comp_code in sorted(by_tier[tier_code]):
            prompts = by_tier[tier_code][comp_code]
            comp_title = prompts[0]["component_title"]
            P(f"\n#### {comp_code} — {comp_title}\n")
            for p in prompts:
                P(f"{p['prompt_seq']}. {p['question_text']}")
            P("")

    # === 11. Word-specific Extensions (if any) ===
    own_ext_section = f"{word.title()} Extensions"
    ext_questions = conn.execute(
        """SELECT obs_id, question_code, question_text
           FROM wa_obs_question_catalogue
           WHERE section = ? AND (deleted=0 OR deleted IS NULL)
           ORDER BY question_code, obs_id""",
        (own_ext_section,),
    ).fetchall()
    if ext_questions:
        P(f"\n## 11. Word-specific Extensions ({own_ext_section})\n")
        P(f"_{len(ext_questions)} questions specific to this word, retained from catalogue v1._\n")
        for q in ext_questions:
            P(f"\n### {q['question_code']} (obs_id={q['obs_id']})")
            P(f"**Q.** {q['question_text']}\n")
            links = conn.execute(
                """SELECT l.coverage, l.session_b_note, f.finding_id
                   FROM wa_finding_catalogue_links l
                   JOIN wa_session_b_findings f ON f.id = l.finding_id
                   WHERE f.registry_id = ? AND l.question_id = ?
                   AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)
                   ORDER BY l.coverage DESC, f.finding_id""",
                (no, q["obs_id"]),
            ).fetchall()
            if not links:
                P(f"**R{no:03d} answer:** _silent_")
                continue
            by_cov: dict[str, list] = {}
            for l in links:
                by_cov.setdefault(l["coverage"], []).append(l)
            for cov in ("full", "partial"):
                if cov not in by_cov:
                    continue
                items = by_cov[cov]
                notes = {l["session_b_note"] for l in items if l["session_b_note"]}
                if len(notes) == 1:
                    P(f"**R{no:03d} answer ({cov}):**\n")
                    P("> " + (notes.pop() or "").replace("\n", "\n> "))
                    P(f"\n_Sourced from: " + ", ".join(l["finding_id"] for l in items) + "_")

    # === 12. Historical v1 Q&A (preserved as analytic history) ===
    P(f"\n## 12. Historical v1 Q&A links (analytic provenance)\n")
    P("v1 generic catalogue questions were retired on 2026-04-30 (`status='redundant_v1'`). The Q&A links to findings under v1 are preserved here as analytic provenance — they show what was asked of the v1 catalogue and what was answered. This section will not grow; new analytic work runs against v2.\n")
    v1_links = conn.execute(
        """
        SELECT q.question_code, q.section AS old_section, q.question_text,
               l.coverage, l.session_b_note, f.finding_id
        FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        WHERE f.registry_id = ?
        AND q.status = 'redundant_v1'
        AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)
        ORDER BY q.question_code, f.finding_id
        """,
        (no,),
    ).fetchall()
    P(f"**Total v1 historical links for R{no:03d}:** {len(v1_links)}.\n")
    if v1_links:
        # Group by question
        by_q: dict[str, list] = {}
        q_text: dict[str, str] = {}
        q_section: dict[str, str] = {}
        for r in v1_links:
            by_q.setdefault(r["question_code"], []).append(r)
            q_text[r["question_code"]] = r["question_text"]
            q_section[r["question_code"]] = r["old_section"]
        for qc in sorted(by_q):
            P(f"\n### v1 {qc} (section: {q_section[qc]})")
            P(f"**Q.** {q_text[qc]}\n")
            items = by_q[qc]
            notes = {r["session_b_note"] for r in items if r["session_b_note"]}
            if len(notes) == 1:
                cov = items[0]["coverage"]
                P(f"**R{no:03d} answer ({cov}):**\n")
                P("> " + (notes.pop() or "").replace("\n", "\n> "))
                P(f"\n_Sourced from: " + ", ".join(r["finding_id"] for r in items) + "_")
            elif notes:
                for r in items:
                    if r["session_b_note"]:
                        P(f"\n_From {r['finding_id']} ({r['coverage']}):_")
                        P("> " + (r["session_b_note"] or "").replace("\n", "\n> "))

    return (word_slug, "\n".join(parts))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, help="Single registry no")
    ap.add_argument("--registries", type=str, help="Comma-separated registry nos")
    ap.add_argument("--all", action="store_true", help="All 8 default words")
    args = ap.parse_args()

    if args.all:
        regs = DEFAULT_8
    elif args.registries:
        regs = [int(x) for x in args.registries.split(",")]
    elif args.registry:
        regs = [args.registry]
    else:
        ap.error("must specify --registry, --registries, or --all")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book_codes = {r["short_code"] for r in conn.execute("SELECT short_code FROM books").fetchall()}
    book_codes |= {r["abbreviation"] for r in conn.execute("SELECT abbreviation FROM books").fetchall()}

    os.makedirs(OUT_BASE, exist_ok=True)
    summary: list[tuple[int, str, int, int, int]] = []

    for no in regs:
        word_slug, content = build_word(conn, no, book_codes)
        if not content:
            print(f"R{no}: build returned empty — skipped")
            continue
        out_path = os.path.join(OUT_BASE, f"R{no:03d}-{word_slug}-data.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        n_findings = conn.execute("SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id = ? AND delete_flag = 0", (no,)).fetchone()[0]
        n_flags = conn.execute("SELECT COUNT(*) FROM wa_session_research_flags WHERE registry_id = (SELECT id FROM word_registry WHERE no = ?) AND (resolved=0 OR resolved IS NULL)", (no,)).fetchone()[0]
        summary.append((no, word_slug, len(content), n_findings, n_flags))
        print(f"R{no:03d} {word_slug:30s} -> {os.path.basename(out_path)}  ({len(content):>7,} chars, {n_findings} findings, {n_flags} flags)")

    # Index
    if len(summary) > 1:
        index_lines = [
            "# AI Question-Test Bundle — 8 Words\n",
            f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n",
            "**Purpose:** complete data per word for AI testing of new questions.  Each file contains every term, group, anchor verse (with text), finding (with all citation categories — structured links + text-recovered support), open flag (Session B + Session D), and Q&A link (where present), plus co-occurrence, shared anchors, quality flags, and verse classification summary.\n",
            "**Schema:** v3.17.0 SQLite at `database/bible_research.db` — DB is the source of truth.\n",
            "",
            "## Files\n",
            "| Reg | Word | File | Size | Findings | Open flags |",
            "| ---: | --- | --- | ---: | ---: | ---: |",
        ]
        for no, ws, sz, nf, ng in summary:
            fname = f"R{no:03d}-{ws}-data.md"
            index_lines.append(f"| R{no:03d} | {ws} | [{fname}]({fname}) | {sz:,} chars | {nf} | {ng} |")
        index_lines.append("\n## Notes on completeness\n")
        index_lines.append("Words at v2 `Analysis Complete` carry the richest Q&A coverage (forgiveness, goodness, contrition).  Fellowship is at `Pre-Analysis Complete` — has v2 findings but no Q&A links yet.  Compassion, grace, love, and mercy are at `Verse Context Reset` — they carry pre-v2 findings (often only 1–2 per registry) and rich SD-pointer flags but no Q&A coverage under the current catalogue.\n")
        index_lines.append("Citation completeness varies: where structured `wa_finding_entity_links` rows are sparse, the report falls back to text-scan recovery (DIM↔OBS resolution chain, cross-finding refs, inline Strong's, term transliterations, inline verse refs, inline group-code refs).  Findings with no support in any of the seven categories are tagged orphan at the end of §8.\n")
        index_path = os.path.join(OUT_BASE, "_index.md")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write("\n".join(index_lines))
        print(f"\nIndex: {index_path}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
