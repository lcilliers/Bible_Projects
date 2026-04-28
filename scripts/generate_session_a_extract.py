"""generate_session_a_extract.py — Mechanical Session A extract generator.

Produces a Session A extract for a registry: 6 markdown sections rendered
directly from the live database. Follows the specification in
research/investigations/session-a-extract-section-types-advice-v1-20260419.md.

Sections (by chapter_no in prose_section_type where source_stage='session_a'):
  1. Summary           — registry orientation + word_synopsis + counts
  2. Meaning           — parsed meaning, senses, stems, LSJ (Greek)
  3. Terms             — OWNER + XREF with MTI status, flags, quality flags,
                         root family, related words, verse counts
  4. Verses            — group-first rendering with dimensions + verse records
  5. Pointers          — SB findings, SD pointers, cross-registry links,
                         phase2 flags, research flags
  6. Questions         — universal catalogue questions + registry extensions

Usage:
  python scripts/generate_session_a_extract.py --registry=N
  python scripts/generate_session_a_extract.py --registry=N --out-dir=Sessions/Session_A/Data_Prose
  python scripts/generate_session_a_extract.py --registry=N --apply          # also write to DB
  python scripts/generate_session_a_extract.py --registry=N --emit-patch=FILE # JSON patch only

Output:
  Default: <out-dir>/wa-{NNN}-{word}-sessiona-{YYYYMMDD}.md
           Markdown file with PROSE_SECTION markers, ready for import via
           the round-trip tooling (or direct DB application via --apply).

--apply mode:
  Builds a PROSE patch with `insert` (first generation) or `session_a_replace`
  (regeneration) operations and applies it via scripts/apply_session_patch.py.

--emit-patch=FILE:
  Writes the PROSE patch to the given JSON path without applying it. The
  researcher can review then apply via apply_session_patch.py --patch-file=...

Author: Claude Code (mechanical extract — no analytical judgement).
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sqlite3
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.stdout.reconfigure(encoding="utf-8")  # Windows console compatibility

DB_PATH = os.path.join("database", "bible_research.db")
SOURCE_STAGE = "session_a"
AUTHOR = "claude_code"
STATUS = "approved"

# Semantic section order per Session A advice §5 (researcher-approved 2026-04-19).
# Keyed by label-keyword — robust to DB seed chapter_no/sort_order ordering.
# Labels in prose_section_type for session_a contain these keywords unambiguously.
SECTION_ORDER = [
    ("summary",  "Summary"),
    ("meaning",  "Meaning"),
    ("terms",    "Terms"),
    ("verses",   "Verses"),
    ("pointers", "Pointers"),
    ("questions", "Questions"),
]


# --------------------------------------------------------------------------
# DB helpers
# --------------------------------------------------------------------------

def open_db(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_one(conn: sqlite3.Connection, sql: str, params=()) -> sqlite3.Row | None:
    cur = conn.execute(sql, params)
    return cur.fetchone()


def fetch_all(conn: sqlite3.Connection, sql: str, params=()) -> list[sqlite3.Row]:
    cur = conn.execute(sql, params)
    return list(cur.fetchall())


def scalar(conn: sqlite3.Connection, sql: str, params=()) -> Any:
    cur = conn.execute(sql, params)
    row = cur.fetchone()
    return row[0] if row else None


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def load_section_types(conn: sqlite3.Connection) -> list[dict]:
    """Return session_a section types in semantic order per SECTION_ORDER.

    Matches by label keyword (case-insensitive), not chapter_no, so the
    generator is robust to DB seed chapter_no/sort_order issues. Returns a
    list preserving SECTION_ORDER; raises if any slot cannot be matched or
    if a DB row remains unmatched (detects seed drift).
    """
    rows = fetch_all(conn, """
        SELECT id, code, label, chapter_no, sort_order
          FROM prose_section_type
         WHERE source_stage = ? AND delete_flagged = 0
         ORDER BY id
    """, (SOURCE_STAGE,))

    remaining = {r["id"]: r for r in rows}
    out: list[dict] = []
    for keyword, display_name in SECTION_ORDER:
        match = None
        for r in remaining.values():
            if keyword in (r["label"] or "").lower():
                match = r
                break
        if match is None:
            raise RuntimeError(
                f"prose_section_type: no session_a row matches keyword "
                f"'{keyword}' ({display_name}). Seed incomplete."
            )
        out.append(dict(
            id=match["id"],
            code=match["code"],
            label=match["label"],
            keyword=keyword,
            display_name=display_name,
            db_chapter_no=match["chapter_no"],  # retained for diagnostics
        ))
        remaining.pop(match["id"])
    if remaining:
        extras = ", ".join(f"id={r['id']} code={r['code']} label={r['label']!r}"
                           for r in remaining.values())
        raise RuntimeError(
            f"prose_section_type session_a has unmatched rows: {extras}. "
            "Update SECTION_ORDER or investigate seed drift."
        )
    return out


def load_registry_context(conn: sqlite3.Connection, no: int) -> dict:
    """Load word_registry + primary file_id + OWNER/XREF file_ids."""
    wr = fetch_one(conn, "SELECT * FROM word_registry WHERE no = ?", (no,))
    if wr is None:
        raise ValueError(f"registry {no} not found")
    wr_id = wr["id"]
    file_ids = [r["id"] for r in fetch_all(
        conn, "SELECT id FROM wa_file_index WHERE word_registry_fk = ?", (wr_id,)
    )]
    return dict(
        registry_id=wr_id,
        registry_no=no,
        word=wr["word"],
        row=dict(wr),
        file_ids=file_ids,
    )


# --------------------------------------------------------------------------
# Markdown helpers
# --------------------------------------------------------------------------

def fmt(v) -> str:
    """Render a scalar for a markdown table cell."""
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v).replace("\n", " ").replace("|", "\\|").strip()
    return s if s else "—"


def meta_block(
    section_label: str,
    sources: list[str],
    notes: str | None = None,
) -> str:
    """The 'meta block' every section opens with (per advice §3 design principle)."""
    lines: list[str] = []
    lines.append(f"## {section_label}")
    lines.append("")
    lines.append("**Section meta**")
    lines.append("")
    lines.append("| Aspect | Value |")
    lines.append("|---|---|")
    lines.append(f"| Generated | {now_iso()} |")
    lines.append(f"| Source stage | `session_a` (mechanical extract) |")
    lines.append(f"| Author | `claude_code` |")
    lines.append(f"| Source tables | {', '.join(f'`{t}`' for t in sources)} |")
    if notes:
        lines.append(f"| Notes | {notes} |")
    lines.append("")
    return "\n".join(lines)


def marker(
    section_type_code: str,
    registry_no: int,
    existing_id: int | None,
    version: int,
) -> str:
    """PROSE_SECTION marker block per prose-store design §5.1."""
    lines = ["<!-- PROSE_SECTION"]
    if existing_id is not None:
        lines.append(f"id: {existing_id}")
    lines.append(f"type: {section_type_code}")
    lines.append(f"registry: {registry_no}")
    lines.append(f"version: {version}")
    lines.append(f"status: {STATUS}")
    lines.append(f"author: {AUTHOR}")
    lines.append("-->")
    return "\n".join(lines)


def slugify_heading(text: str) -> str:
    """GitHub/Obsidian-compatible heading anchor slug."""
    import re
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def section_heading_for(keyword: str) -> str:
    """The H2 heading emitted by each section's meta_block()."""
    headings = {
        "summary":  "Section 1 — Summary (Registry Orientation)",
        "meaning":  "Section 2 — Meaning (Lexical / Semantic)",
        "terms":    "Section 3 — Terms (OWNER + XREF) with Analytical Metadata",
        "verses":   "Section 4 — Verses by Group (with Dimensions and Annotations)",
        "pointers": "Section 5 — Research Pointers, Findings, and Cross-Registry Links",
        "questions": "Section 6 — Analytic Questions (Catalogue + Registry Extensions)",
    }
    return headings[keyword]


# --------------------------------------------------------------------------
# Section 1 — Summary
# --------------------------------------------------------------------------

def render_summary(conn: sqlite3.Connection, ctx: dict) -> str:
    wr = ctx["row"]
    wr_id = ctx["registry_id"]
    file_ids = ctx["file_ids"]
    fid_ph = ",".join("?" * len(file_ids)) if file_ids else ""

    # Derived counts
    if file_ids:
        owner_count = scalar(conn, f"""
            SELECT COUNT(*) FROM wa_term_inventory
            WHERE file_id IN ({fid_ph})
              AND term_owner_type='OWNER' AND delete_flagged=0
        """, tuple(file_ids)) or 0
        xref_count = scalar(conn, f"""
            SELECT COUNT(*) FROM wa_term_inventory
            WHERE file_id IN ({fid_ph})
              AND term_owner_type='XREF' AND delete_flagged=0
        """, tuple(file_ids)) or 0
        verse_count = scalar(conn, f"""
            SELECT COUNT(*) FROM wa_verse_records
            WHERE file_id IN ({fid_ph}) AND delete_flagged=0
        """, tuple(file_ids)) or 0
    else:
        owner_count = xref_count = verse_count = 0

    group_count = scalar(conn, """
        SELECT COUNT(*) FROM verse_context_group vcg
        WHERE vcg.delete_flagged=0
          AND vcg.mti_term_id IN (SELECT id FROM mti_terms WHERE owning_registry_fk=?)
    """, (wr_id,)) or 0

    dim_count = scalar(conn, """
        SELECT COUNT(*) FROM wa_dimension_index wdi
        JOIN verse_context_group vcg ON vcg.id = wdi.verse_context_group_id
        WHERE wdi.delete_flagged=0
          AND vcg.mti_term_id IN (SELECT id FROM mti_terms WHERE owning_registry_fk=?)
    """, (wr_id,)) or 0

    body = [meta_block(
        "Section 1 — Summary (Registry Orientation)",
        sources=["word_registry", "wa_term_inventory", "wa_verse_records",
                 "verse_context_group", "wa_dimension_index"],
        notes="Word synopsis is researcher-authored (`word_registry.word_synopsis`, M21). "
              "NULL means authoring is pending — see Action S programme note.",
    )]

    # Word identity
    body.append("### 1.1 Word identity\n")
    body.append("| Field | Value |")
    body.append("|---|---|")
    body.append(f"| Word | **{fmt(wr['word'])}** |")
    body.append(f"| Registry no | {fmt(wr['no'])} |")
    body.append(f"| Cluster | {fmt(wr['cluster_assignment'])} |")
    body.append(f"| Carry forward | {fmt(wr['carry_forward'])} |")
    body.append("")

    # Word synopsis
    body.append("### 1.2 Word synopsis\n")
    synopsis = wr["word_synopsis"] if "word_synopsis" in wr.keys() else None
    if synopsis:
        body.append(synopsis.strip())
    else:
        body.append("_Word synopsis not yet authored. Researcher to populate "
                    "`word_registry.word_synopsis` (M21)._")
    body.append("")

    # Programme state
    body.append("### 1.3 Programme state\n")
    body.append("| Field | Value |")
    body.append("|---|---|")
    body.append(f"| session_b_status | {fmt(wr['session_b_status'])} |")
    body.append(f"| verse_context_status | {fmt(wr['verse_context_status'])} |")
    body.append(f"| dim_review_status | {fmt(wr['dim_review_status'])} |")
    if "dim_review_version" in wr.keys():
        body.append(f"| dim_review_version | {fmt(wr['dim_review_version'])} |")
    body.append(f"| phase1_status | {fmt(wr['phase1_status'])} |")
    body.append("")

    # Population counts (from word_registry)
    body.append("### 1.4 Term & verse population (registry-recorded)\n")
    body.append("| Field | Value |")
    body.append("|---|---|")
    for k in ("unique_term_count", "shared_term_count", "term_sharing_ratio",
              "phase1_term_count", "phase1_verse_count"):
        if k in wr.keys():
            body.append(f"| {k} | {fmt(wr[k])} |")
    body.append("")

    # Registry-level dimensions
    body.append("### 1.5 Registry-level dimension list\n")
    if "dimensions" in wr.keys() and wr["dimensions"]:
        body.append(f"`{wr['dimensions']}`")
    else:
        body.append("_No registry-level dimensions recorded._")
    body.append("")

    # Derived counts
    body.append("### 1.6 Derived counts (confirmatory)\n")
    body.append("| Field | Value |")
    body.append("|---|---|")
    body.append(f"| OWNER terms (active) | {owner_count} |")
    body.append(f"| XREF terms (active) | {xref_count} |")
    body.append(f"| Active verse records | {verse_count} |")
    body.append(f"| Active verse-context groups | {group_count} |")
    body.append(f"| Active dimension assignments | {dim_count} |")
    body.append("")

    return "\n".join(body)


# --------------------------------------------------------------------------
# Section 2 — Meaning
# --------------------------------------------------------------------------

def render_meaning(conn: sqlite3.Connection, ctx: dict) -> str:
    file_ids = ctx["file_ids"]
    fid_ph = ",".join("?" * len(file_ids)) if file_ids else ""

    # OWNER terms only (meaning is keyed to the OWNER record)
    terms = fetch_all(conn, f"""
        SELECT ti.id AS ti_id, ti.strongs_number, ti.transliteration,
               ti.step_search_gloss, ti.word_analysis_gloss, ti.language,
               ti.meaning, ti.meaning_numbered, ti.short_def_mounce,
               ti.lsj_entry, ti.parsed_meaning_id
          FROM wa_term_inventory ti
         WHERE ti.file_id IN ({fid_ph})
           AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
         ORDER BY ti.strongs_number
    """, tuple(file_ids)) if file_ids else []

    body = [meta_block(
        "Section 2 — Meaning (Lexical / Semantic)",
        sources=["wa_term_inventory.meaning", "wa_meaning_parsed",
                 "wa_meaning_sense", "wa_meaning_stem", "wa_lsj_parsed"],
        notes=f"Rendered per OWNER term ({len(terms)} terms). Raw meaning text "
              "lives in `wa_term_inventory.meaning`; structured parse "
              "in `wa_meaning_*` tables.",
    )]

    if not terms:
        body.append("_No OWNER terms with meaning data for this registry._")
        body.append("")
        return "\n".join(body)

    for t in terms:
        body.append(f"### 2.{t['strongs_number']} — {t['strongs_number']} "
                    f"({t['transliteration'] or '—'}) — {t['language'] or '—'}\n")
        body.append(f"_step gloss: {fmt(t['step_search_gloss'])} · "
                    f"analysis gloss: {fmt(t['word_analysis_gloss'])}_\n")

        # Raw meaning (stored on wa_term_inventory)
        raw = t["meaning"] or ""
        if raw:
            body.append("**Raw meaning text:**")
            body.append("")
            body.append("> " + raw.replace("\n", "\n> "))
            body.append("")
        else:
            body.append("_No raw meaning text for this term._")
            body.append("")

        if t["short_def_mounce"]:
            body.append(f"**Mounce short def:** {fmt(t['short_def_mounce'])}")
            body.append("")

        # Parsed meaning metadata
        parsed_id = t["parsed_meaning_id"]
        if not parsed_id:
            parsed = fetch_one(conn, """
                SELECT id, top_sense_count, stem_count, has_causative_stem,
                       has_domain_tags, parsed_at, parse_version, parse_warnings
                  FROM wa_meaning_parsed
                 WHERE term_inv_id = ?
            """, (t["ti_id"],))
        else:
            parsed = fetch_one(conn, """
                SELECT id, top_sense_count, stem_count, has_causative_stem,
                       has_domain_tags, parsed_at, parse_version, parse_warnings
                  FROM wa_meaning_parsed
                 WHERE id = ?
            """, (parsed_id,))

        if not parsed:
            body.append("_Meaning not structured-parsed for this term._")
            body.append("")
            continue

        body.append(f"**Parse metadata:** senses={fmt(parsed['top_sense_count'])} · "
                    f"stems={fmt(parsed['stem_count'])} · "
                    f"causative={fmt(parsed['has_causative_stem'])} · "
                    f"domain_tags={fmt(parsed['has_domain_tags'])} · "
                    f"parser={fmt(parsed['parse_version'])}")
        body.append("")

        # Senses
        senses = fetch_all(conn, """
            SELECT level_code, level_depth, parent_level_code,
                   sense_text, is_stem_label, stem_label, domain_tag, sort_order
              FROM wa_meaning_sense
             WHERE parsed_meaning_id = ?
             ORDER BY sort_order, id
        """, (parsed["id"],))
        if senses:
            body.append("**Senses:**\n")
            body.append("| # | Level | Stem? | Stem label | Domain | Sense text |")
            body.append("|---|---|---|---|---|---|")
            for s in senses:
                body.append(
                    f"| {fmt(s['sort_order'])} | {fmt(s['level_code'])} "
                    f"(d{fmt(s['level_depth'])}) | {fmt(s['is_stem_label'])} | "
                    f"{fmt(s['stem_label'])} | {fmt(s['domain_tag'])} | "
                    f"{fmt(s['sense_text'])} |"
                )
            body.append("")

        # Stems
        stems = fetch_all(conn, """
            SELECT stem_name, stem_type, sense_count, top_sense_text
              FROM wa_meaning_stem
             WHERE parsed_meaning_id = ?
             ORDER BY id
        """, (parsed["id"],))
        if stems:
            body.append("**Stems (verbal forms):**\n")
            body.append("| Stem | Type | # senses | Top sense |")
            body.append("|---|---|---|---|")
            for s in stems:
                body.append(f"| {fmt(s['stem_name'])} | {fmt(s['stem_type'])} | "
                            f"{fmt(s['sense_count'])} | {fmt(s['top_sense_text'])} |")
            body.append("")

        # LSJ (Greek only)
        if (t["language"] or "").lower() == "greek":
            lsj = fetch_one(conn, """
                SELECT raw_lsj, lsj_gloss, lsj_domains, lsj_philosophical_note,
                       lsj_etymology_note, lsj_cognate_forms
                  FROM wa_lsj_parsed
                 WHERE term_inv_id = ?
            """, (t["ti_id"],))
            if lsj:
                body.append("**LSJ lexicon:**\n")
                body.append(f"- Gloss: {fmt(lsj['lsj_gloss'])}")
                body.append(f"- Domains: {fmt(lsj['lsj_domains'])}")
                if lsj["lsj_etymology_note"]:
                    body.append(f"- Etymology: {fmt(lsj['lsj_etymology_note'])}")
                if lsj["lsj_philosophical_note"]:
                    body.append(f"- Philosophical note: {fmt(lsj['lsj_philosophical_note'])}")
                if lsj["lsj_cognate_forms"]:
                    body.append(f"- Cognate forms: {fmt(lsj['lsj_cognate_forms'])}")
                if lsj["raw_lsj"]:
                    body.append("")
                    body.append("> " + (lsj["raw_lsj"] or "").replace("\n", "\n> "))
                body.append("")

    return "\n".join(body)


# --------------------------------------------------------------------------
# Section 3 — Terms (OWNER + XREF)
# --------------------------------------------------------------------------

def render_terms(conn: sqlite3.Connection, ctx: dict) -> str:
    file_ids = ctx["file_ids"]
    fid_ph = ",".join("?" * len(file_ids)) if file_ids else ""
    wr_id = ctx["registry_id"]

    terms = fetch_all(conn, f"""
        SELECT ti.id AS ti_id, ti.strongs_number, ti.transliteration,
               ti.step_search_gloss, ti.word_analysis_gloss, ti.language,
               ti.term_owner_type, ti.evidential_status, ti.retention_note,
               ti.causative_form_present, ti.occurrence_count
          FROM wa_term_inventory ti
         WHERE ti.file_id IN ({fid_ph}) AND ti.delete_flagged = 0
         ORDER BY CASE ti.term_owner_type WHEN 'OWNER' THEN 0 ELSE 1 END,
                  ti.strongs_number
    """, tuple(file_ids)) if file_ids else []

    body = [meta_block(
        "Section 3 — Terms (OWNER + XREF) with Analytical Metadata",
        sources=["wa_term_inventory", "mti_terms", "mti_term_flags",
                 "wa_data_quality_flags", "wa_term_root_family",
                 "wa_term_related_words", "wa_verse_records"],
        notes=f"Total active terms: {len(terms)}. OWNER listed first, then XREF.",
    )]

    if not terms:
        body.append("_No active terms for this registry._")
        body.append("")
        return "\n".join(body)

    for t in terms:
        body.append(f"### 3.{t['term_owner_type']}.{t['strongs_number']} — "
                    f"{t['strongs_number']} ({t['transliteration'] or '—'}) — "
                    f"{t['term_owner_type']}\n")

        # Identity
        body.append("| Field | Value |")
        body.append("|---|---|")
        body.append(f"| Language | {fmt(t['language'])} |")
        body.append(f"| STEP gloss | {fmt(t['step_search_gloss'])} |")
        body.append(f"| Analysis gloss | {fmt(t['word_analysis_gloss'])} |")
        body.append(f"| Occurrence count | {fmt(t['occurrence_count'])} |")
        body.append(f"| Causative form present | {fmt(t['causative_form_present'])} |")
        body.append(f"| Evidential status | {fmt(t['evidential_status'])} |")
        if t["retention_note"]:
            body.append(f"| Retention note | {fmt(t['retention_note'])} |")
        body.append("")

        # MTI status
        mti = fetch_one(conn, """
            SELECT id, status, owning_registry_fk, owning_word, owning_part,
                   exclusion_reason, anchor_note
              FROM mti_terms
             WHERE strongs_number = ? AND delete_flagged = 0
             ORDER BY CASE WHEN status IN ('extracted','extracted_thin') THEN 0 ELSE 1 END,
                      owning_registry_fk IS NULL, id
             LIMIT 1
        """, (t["strongs_number"],))
        if mti:
            body.append("**MTI (Mounce Term Index) canonical row:**\n")
            body.append("| Field | Value |")
            body.append("|---|---|")
            body.append(f"| status | `{fmt(mti['status'])}` |")
            body.append(f"| owning_registry_fk | {fmt(mti['owning_registry_fk'])} "
                        f"({'this registry' if mti['owning_registry_fk']==wr_id else 'other'}) |")
            body.append(f"| owning_word | {fmt(mti['owning_word'])} |")
            if mti["owning_part"]:
                body.append(f"| owning_part | {fmt(mti['owning_part'])} |")
            if mti["exclusion_reason"]:
                body.append(f"| exclusion_reason | {fmt(mti['exclusion_reason'])} |")
            if mti["anchor_note"]:
                body.append(f"| anchor_note | {fmt(mti['anchor_note'])} |")
            body.append("")

            # MTI flags (authoritative for somatic / god_as_subject per GR-DATA-003)
            flags = fetch_all(conn, """
                SELECT mtf.flag_id, qft.flag_code, qft.description
                  FROM mti_term_flags mtf
                  JOIN wa_quality_flag_types qft ON qft.id = mtf.flag_id
                 WHERE mtf.mti_term_id = ?
            """, (mti["id"],))
            if flags:
                body.append("**MTI flags:**")
                for f in flags:
                    body.append(f"- `{f['flag_code']}` — {fmt(f['description'])[:120]}")
                body.append("")

        # Term-level data quality flags
        quality = fetch_all(conn, """
            SELECT qft.flag_code, qft.research_actions, dqf.description, dqf.last_changed
              FROM wa_data_quality_flags dqf
              JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
             WHERE dqf.term_id = ?
        """, (t["strongs_number"],))
        if quality:
            body.append("**Data quality flags:**\n")
            body.append("| Flag | Research actions | Description | Last changed |")
            body.append("|---|---|---|---|")
            for q in quality:
                body.append(f"| `{q['flag_code']}` | {fmt(q['research_actions'])} | "
                            f"{fmt(q['description'])} | {fmt(q['last_changed'])} |")
            body.append("")

            # Inline linked Q-COV catalogue questions for any evidence-family flag
            # per coverage-flags-redesign-v1 §12.4 methodology (prose carries the
            # questions; answers land as findings later).
            flag_codes_here = [q["flag_code"] for q in quality]
            linked_questions = fetch_all(conn, f"""
                SELECT qft.flag_code, oqc.question_code, oqc.question_text
                  FROM wa_flag_type_question_link ftql
                  JOIN wa_quality_flag_types qft ON qft.id = ftql.flag_type_id
                  JOIN wa_obs_question_catalogue oqc ON oqc.obs_id = ftql.question_id
                 WHERE ftql.active = 1
                   AND qft.flag_code IN ({','.join('?' * len(flag_codes_here))})
                   AND COALESCE(oqc.deleted, 0) = 0
                 ORDER BY qft.flag_code, oqc.question_code
            """, tuple(flag_codes_here)) if flag_codes_here else []
            if linked_questions:
                body.append("**Open research questions (from catalogue, driven by flags above):**\n")
                current_flag = None
                for lq in linked_questions:
                    if lq["flag_code"] != current_flag:
                        current_flag = lq["flag_code"]
                        body.append(f"_Via `{current_flag}`:_")
                    body.append(f"- **{lq['question_code']}** — {lq['question_text']}")
                body.append("")

        # Term-level dimension (aggregated from groups via mti_term_id)
        if mti:
            dims = fetch_all(conn, """
                SELECT wdi.dimension, wdi.dimension_confidence, COUNT(*) c
                  FROM wa_dimension_index wdi
                  JOIN verse_context_group vcg ON vcg.id = wdi.verse_context_group_id
                 WHERE vcg.mti_term_id = ? AND wdi.delete_flagged = 0
                 GROUP BY wdi.dimension, wdi.dimension_confidence
                 ORDER BY c DESC
            """, (mti["id"],))
            if dims:
                body.append("**Term-level dimension signal (aggregated across this term's groups):**\n")
                body.append("| Dimension | Confidence | Group count |")
                body.append("|---|---|---|")
                for d in dims:
                    body.append(f"| {fmt(d['dimension'])} | {fmt(d['dimension_confidence'])} | {d['c']} |")
                body.append("")

        # Root family
        roots = fetch_all(conn, """
            SELECT root_code, root_language, root_gloss, note
              FROM wa_term_root_family
             WHERE term_inv_id = ? AND delete_flagged = 0
             ORDER BY id
        """, (t["ti_id"],))
        if roots:
            body.append("**Root family:**\n")
            body.append("| Root | Language | Gloss | Note |")
            body.append("|---|---|---|---|")
            for r in roots:
                body.append(f"| `{fmt(r['root_code'])}` | {fmt(r['root_language'])} | "
                            f"{fmt(r['root_gloss'])} | {fmt(r['note'])} |")
            body.append("")

        # Related words
        related = fetch_all(conn, """
            SELECT strongs_number, gloss, transliteration, relationship_note
              FROM wa_term_related_words
             WHERE term_inv_id = ? AND delete_flagged = 0
             ORDER BY id
        """, (t["ti_id"],))
        if related:
            body.append("**Related words:**\n")
            body.append("| Strongs | Transliteration | Gloss | Relationship |")
            body.append("|---|---|---|---|")
            for r in related:
                body.append(f"| {fmt(r['strongs_number'])} | {fmt(r['transliteration'])} | "
                            f"{fmt(r['gloss'])} | {fmt(r['relationship_note'])} |")
            body.append("")

        # Verse counts for this term
        vc_total = scalar(conn, "SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id=?",
                          (t["ti_id"],)) or 0
        vc_active = scalar(conn, "SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id=? AND delete_flagged=0",
                           (t["ti_id"],)) or 0
        body.append(f"**Verse record counts:** total={vc_total}, active={vc_active}, "
                    f"delete_flagged={vc_total - vc_active}.")
        body.append("")

    return "\n".join(body)


# --------------------------------------------------------------------------
# Section 4 — Verses (group-first)
# --------------------------------------------------------------------------

def render_verses(conn: sqlite3.Connection, ctx: dict) -> str:
    wr_id = ctx["registry_id"]

    groups = fetch_all(conn, """
        SELECT vcg.id AS gid, vcg.group_code, vcg.context_description,
               vcg.mti_term_id, mt.strongs_number, mt.owning_word,
               wdi.dimension, wdi.dimension_confidence, wdi.dominant_subject,
               wdi.manual_override, wdi.anchor_count, wdi.related_count,
               wdi.set_aside_count, wdi.notes
          FROM verse_context_group vcg
          JOIN mti_terms mt ON mt.id = vcg.mti_term_id
     LEFT JOIN wa_dimension_index wdi
            ON wdi.verse_context_group_id = vcg.id AND wdi.delete_flagged = 0
         WHERE vcg.delete_flagged = 0
           AND mt.owning_registry_fk = ?
         ORDER BY mt.strongs_number, vcg.group_code
    """, (wr_id,))

    body = [meta_block(
        "Section 4 — Verses by Group (with Dimensions and Annotations)",
        sources=["verse_context_group", "wa_dimension_index",
                 "wa_verse_records", "verse_context", "mti_terms"],
        notes=f"Active groups: {len(groups)}. Verses within each group rendered "
              "as anchor → related → set-aside.",
    )]

    if not groups:
        body.append("_No active verse-context groups for this registry._")
        body.append("")
        return "\n".join(body)

    for g in groups:
        body.append(f"### 4.{g['strongs_number']}.{g['group_code']} — "
                    f"{g['strongs_number']} · group `{g['group_code']}`\n")

        body.append("| Field | Value |")
        body.append("|---|---|")
        body.append(f"| context_description | {fmt(g['context_description'])} |")
        body.append(f"| dimension | {fmt(g['dimension'])} |")
        body.append(f"| dimension_confidence | {fmt(g['dimension_confidence'])} |")
        body.append(f"| dominant_subject | {fmt(g['dominant_subject'])} |")
        body.append(f"| manual_override | {fmt(g['manual_override'])} |")
        body.append(f"| anchor / related / set-aside | "
                    f"{fmt(g['anchor_count'])} / {fmt(g['related_count'])} / {fmt(g['set_aside_count'])} |")
        if g["notes"]:
            body.append(f"| notes | {fmt(g['notes'])} |")
        body.append("")

        # Verses in this group
        verses = fetch_all(conn, """
            SELECT vr.id AS vrid, vr.reference, vr.verse_text, vr.translation,
                   vr.span_strong_match,
                   vc.is_relevant, vc.is_anchor, vc.is_related, vc.set_aside_reason
              FROM verse_context vc
              JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
             WHERE vc.group_id = ? AND vc.delete_flagged = 0 AND vr.delete_flagged = 0
             ORDER BY CASE
                        WHEN vc.is_anchor=1 THEN 0
                        WHEN vc.is_related=1 THEN 1
                        ELSE 2 END,
                      vr.id
        """, (g["gid"],))
        if not verses:
            body.append("_No verses in this group._")
            body.append("")
            continue

        body.append("| Role | Reference | Translation | Span match | Text |")
        body.append("|---|---|---|---|---|")
        for v in verses:
            if v["is_anchor"]:
                role = "**anchor**"
            elif v["is_related"]:
                role = "related"
            else:
                role = f"set-aside: {fmt(v['set_aside_reason'])}" if v['set_aside_reason'] else "set-aside"
            text = (v["verse_text"] or "")
            # Truncate long verses for readability but don't lose them
            if len(text) > 350:
                text = text[:347] + "…"
            body.append(f"| {role} | {fmt(v['reference'])} | "
                        f"{fmt(v['translation'])} | {fmt(v['span_strong_match'])} | {fmt(text)} |")
        body.append("")

    return "\n".join(body)


# --------------------------------------------------------------------------
# Section 5 — Pointers
# --------------------------------------------------------------------------

def render_pointers(conn: sqlite3.Connection, ctx: dict) -> str:
    wr_id = ctx["registry_id"]
    reg_no = ctx["registry_no"]

    body = [meta_block(
        "Section 5 — Research Pointers, Findings, and Cross-Registry Links",
        sources=["wa_session_b_findings", "wa_finding_catalogue_links",
                 "wa_obs_question_catalogue", "wa_session_research_flags",
                 "wa_term_phase2_flags", "wa_cross_registry_links",
                 "wa_crosslink_type"],
        notes="Four sub-blocks: 5a SB findings + SB pointers · 5b SD pointers · "
              "5c cross-registry links · 5d correlation summary.",
    )]

    # 5a — Session B findings and pointers
    body.append("### 5a — Session B Pointers and Findings\n")
    findings = fetch_all(conn, """
        SELECT id, finding_id, finding_type, finding, status, anchor_verses,
               raised_date, pass_ref, study_segment, term_id, thin_evidence
          FROM wa_session_b_findings
         WHERE registry_id = ? AND COALESCE(delete_flag, 0) = 0
         ORDER BY finding_id
    """, (wr_id,))
    if findings:
        body.append("**Structured findings:**\n")
        body.append("| Code | Type | Status | Anchor verses | Finding text |")
        body.append("|---|---|---|---|---|")
        for f in findings:
            body.append(f"| `{fmt(f['finding_id'])}` | {fmt(f['finding_type'])} | "
                        f"{fmt(f['status'])} | {fmt(f['anchor_verses'])[:60]} | "
                        f"{fmt(f['finding'])[:200]} |")
        body.append("")

        # Catalogue links per finding — use the internal row.id as the link target
        finding_row_ids = [f["id"] for f in findings]
        fid_ph = ",".join("?" * len(finding_row_ids))
        fclinks = fetch_all(conn, f"""
            SELECT fcl.finding_id, fcl.question_id, fcl.coverage, fcl.status,
                   oqc.question_code, oqc.question_text, oqc.section
              FROM wa_finding_catalogue_links fcl
              JOIN wa_obs_question_catalogue oqc ON oqc.obs_id = fcl.question_id
             WHERE fcl.finding_id IN ({fid_ph})
               AND COALESCE(fcl.delete_flagged, 0) = 0
             ORDER BY fcl.finding_id, oqc.question_code
        """, tuple(finding_row_ids))
        if fclinks:
            body.append("**Finding → catalogue question mapping:**\n")
            body.append("| Finding row | Question code | Section | Coverage | Status | Question text |")
            body.append("|---|---|---|---|---|---|")
            for x in fclinks:
                body.append(f"| {x['finding_id']} | `{fmt(x['question_code'])}` | "
                            f"{fmt(x['section'])} | {fmt(x['coverage'])} | "
                            f"{fmt(x['status'])} | {fmt(x['question_text'])[:90]} |")
            body.append("")
    else:
        body.append("_No Session B findings recorded for this registry._\n")

    # Session B research flags
    sb_flags = fetch_all(conn, """
        SELECT flag_code, flag_label, description, priority, resolved, resolved_note
          FROM wa_session_research_flags
         WHERE registry_id = ? AND session_target = 'B'
         ORDER BY COALESCE(priority,'') DESC, flag_code
    """, (wr_id,))
    if sb_flags:
        body.append("**Session B research flags:**\n")
        body.append("| Code | Priority | Resolved | Description |")
        body.append("|---|---|---|---|")
        for f in sb_flags:
            body.append(f"| `{fmt(f['flag_code'])}` | {fmt(f['priority'])} | "
                        f"{fmt(f['resolved'])} | {fmt(f['description'])[:150]} |")
        body.append("")

    # Phase2 term advisories — join with wa_quality_flag_types for the flag_code
    ph2 = fetch_all(conn, """
        SELECT tp.term_inv_id, ti.strongs_number,
               qft.flag_code, tp.description, tp.source
          FROM wa_term_phase2_flags tp
          JOIN wa_term_inventory ti ON ti.id = tp.term_inv_id
          LEFT JOIN wa_quality_flag_types qft ON qft.id = tp.flag_id
         WHERE ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk=?)
           AND COALESCE(tp.delete_flagged, 0) = 0
         ORDER BY ti.strongs_number
    """, (wr_id,))
    if ph2:
        body.append("**Phase 2 term advisories:**\n")
        body.append("| Strongs | Flag | Source | Description |")
        body.append("|---|---|---|---|")
        for p in ph2:
            body.append(f"| {fmt(p['strongs_number'])} | `{fmt(p['flag_code'])}` | "
                        f"{fmt(p['source'])} | {fmt(p['description'])[:150]} |")
        body.append("")

    # 5b — Session D pointers
    body.append("### 5b — Session D Pointers (cross-registry synthesis queue)\n")
    sd_flags = fetch_all(conn, """
        SELECT flag_code, flag_label, description, priority, resolved, strongs_reference
          FROM wa_session_research_flags
         WHERE registry_id = ? AND session_target = 'D'
         ORDER BY COALESCE(priority,'') DESC, flag_code
    """, (wr_id,))
    if sd_flags:
        body.append("| Code | Strongs ref | Priority | Resolved | Description |")
        body.append("|---|---|---|---|---|")
        for f in sd_flags:
            body.append(f"| `{fmt(f['flag_code'])}` | {fmt(f['strongs_reference'])} | "
                        f"{fmt(f['priority'])} | {fmt(f['resolved'])} | "
                        f"{fmt(f['description'])[:150]} |")
        body.append("")
    else:
        body.append("_No Session D pointers for this registry._\n")

    # 5c — Cross-registry links — keyed by file_id → wa_file_index → registry
    body.append("### 5c — Cross-Registry Links\n")
    xl = fetch_all(conn, """
        SELECT crl.id, crl.linked_word, crl.linked_registry_id,
               ct.type_code, ct.description AS type_description,
               crl.connecting_term, crl.note,
               wr.word AS linked_registry_word, wr.no AS linked_registry_no
          FROM wa_cross_registry_links crl
     LEFT JOIN wa_crosslink_type ct ON ct.id = crl.connection_type_id
     LEFT JOIN word_registry wr ON wr.id = crl.linked_registry_id
         WHERE crl.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
         ORDER BY crl.id
    """, (wr_id,))
    if xl:
        body.append("| Linked registry | Word | Type | Connecting term | Note |")
        body.append("|---|---|---|---|---|")
        for x in xl:
            body.append(f"| {fmt(x['linked_registry_no'])} "
                        f"(id={fmt(x['linked_registry_id'])}) | "
                        f"{fmt(x['linked_registry_word'] or x['linked_word'])} | "
                        f"`{fmt(x['type_code'])}` | {fmt(x['connecting_term'])} | "
                        f"{fmt(x['note'])[:150]} |")
        body.append("")
    else:
        body.append("_No cross-registry links recorded for this registry._\n")

    # 5d — Correlation summary (brief per advice §3)
    body.append("### 5d — Correlation signals\n")
    body.append("_Full programme-wide correlation data is not inlined here — see "
                "`scripts/build_correlation_extract.py` output. This section reserved "
                "for a brief registry-specific summary once correlations are integrated._")
    body.append("")

    return "\n".join(body)


# --------------------------------------------------------------------------
# Section 6 — Analytic Questions
# --------------------------------------------------------------------------

def render_questions(conn: sqlite3.Connection, ctx: dict) -> str:
    reg_no = ctx["registry_no"]
    word = ctx["word"]

    body = [meta_block(
        "Section 6 — Analytic Questions (Catalogue + Registry Extensions)",
        sources=["wa_obs_question_catalogue"],
        notes="Universal catalogue questions (scope='universal') + any registry-specific "
              "extensions (source_registry_no or source_word match). Grouped by "
              "catalogue `section`.",
    )]

    # Universal questions
    universal = fetch_all(conn, """
        SELECT obs_id, question_code, section, question_text, pattern_type, scope, status
          FROM wa_obs_question_catalogue
         WHERE scope = 'universal' AND COALESCE(deleted, 0) = 0
         ORDER BY section, question_code
    """)

    body.append(f"### 6.1 Universal catalogue ({len(universal)} questions)\n")
    if universal:
        by_section: dict = {}
        for r in universal:
            sec = r["section"] or "(no section)"
            by_section.setdefault(sec, []).append(r)
        for sec in sorted(by_section.keys()):
            body.append(f"#### {sec}\n")
            body.append("| Code | Pattern | Question |")
            body.append("|---|---|---|")
            for r in by_section[sec]:
                body.append(f"| `{fmt(r['question_code'])}` | "
                            f"{fmt(r['pattern_type'])} | {fmt(r['question_text'])} |")
            body.append("")
    else:
        body.append("_No universal questions found in catalogue._\n")

    # Registry-specific extensions
    exts = fetch_all(conn, """
        SELECT obs_id, question_code, section, question_text, pattern_type,
               scope, source_registry_no, source_word
          FROM wa_obs_question_catalogue
         WHERE (source_registry_no = ? OR source_word = ?)
           AND COALESCE(deleted, 0) = 0
           AND COALESCE(scope, '') != 'universal'
         ORDER BY section, question_code
    """, (reg_no, word))

    body.append(f"### 6.2 Registry-specific extensions ({len(exts)} questions)\n")
    if exts:
        body.append("| Code | Section | Scope | Pattern | Question |")
        body.append("|---|---|---|---|---|")
        for r in exts:
            body.append(f"| `{fmt(r['question_code'])}` | {fmt(r['section'])} | "
                        f"{fmt(r['scope'])} | {fmt(r['pattern_type'])} | "
                        f"{fmt(r['question_text'])} |")
        body.append("")
    else:
        body.append("_No registry-specific extensions for this word._\n")

    return "\n".join(body)


# --------------------------------------------------------------------------
# Section dispatch
# --------------------------------------------------------------------------

SECTION_RENDERERS = {
    "summary":  render_summary,
    "meaning":  render_meaning,
    "terms":    render_terms,
    "verses":   render_verses,
    "pointers": render_pointers,
    "questions": render_questions,
}


def lookup_existing_prose(
    conn: sqlite3.Connection, registry_id: int, section_type_id: int
) -> sqlite3.Row | None:
    return fetch_one(conn, """
        SELECT id, version
          FROM prose_section
         WHERE registry_id = ? AND section_type_id = ?
           AND delete_flagged = 0
         ORDER BY version DESC LIMIT 1
    """, (registry_id, section_type_id))


def build_extract(conn: sqlite3.Connection, registry_no: int) -> dict:
    """Returns dict with per-section rendered markdown bodies + metadata."""
    ctx = load_registry_context(conn, registry_no)
    section_types = load_section_types(conn)  # list in semantic SECTION_ORDER
    parts = []
    for idx, st in enumerate(section_types, start=1):
        renderer = SECTION_RENDERERS[st["keyword"]]
        body = renderer(conn, ctx)
        existing = lookup_existing_prose(conn, ctx["registry_id"], st["id"])
        parts.append(dict(
            semantic_order=idx,
            keyword=st["keyword"],
            section_type_id=st["id"],
            section_type_code=st["code"],
            section_label=st["label"],
            db_chapter_no=st["db_chapter_no"],
            body=body,
            word_count=len(body.split()),
            existing_id=existing["id"] if existing else None,
            existing_version=existing["version"] if existing else None,
        ))
    return dict(
        registry_no=registry_no,
        registry_id=ctx["registry_id"],
        word=ctx["word"],
        generated_at=now_iso(),
        parts=parts,
    )


def assemble_markdown_file(extract: dict) -> str:
    """Build a single .md file with PROSE_SECTION markers for all 6 sections.

    Structure:
      # Header
      _metadata lines_
      ## Table of Contents     <- human navigation; ignored by round-trip import
      ---                       <- visual separator (still preamble from parser's POV)
      <!-- PROSE_SECTION ... --> <- first marker; import starts here
      ## Section 1 ...
      ...
    """
    out = io.StringIO()
    out.write(f"# Session A Extract — r{extract['registry_no']:03d} {extract['word']}\n\n")
    out.write(f"_Generated: {extract['generated_at']}_\n")
    out.write(f"_Mechanical extract — do not hand-edit body; edit schema and regenerate._\n\n")

    # Table of Contents (file preamble — ignored by round-trip import per design §5.6)
    out.write("## Table of Contents\n\n")
    for p in extract["parts"]:
        heading = section_heading_for(p["keyword"])
        anchor = slugify_heading(heading)
        out.write(f"- [{heading}](#{anchor})\n")
    out.write("\n---\n\n")

    for p in extract["parts"]:
        version = (p["existing_version"] or 0) + 1
        out.write(marker(
            section_type_code=p["section_type_code"],
            registry_no=extract["registry_no"],
            existing_id=p["existing_id"],
            version=version,
        ))
        out.write("\n\n")
        out.write(p["body"])
        out.write("\n")
    return out.getvalue()


def build_prose_patch(extract: dict) -> dict:
    """Build a JSON PROSE patch with insert / session_a_replace operations."""
    today = today_stamp()
    patch_id = f"PATCH-{today}-SESSIONA-R{extract['registry_no']:03d}-V1"
    ops = []
    for p in extract["parts"]:
        op_id = f"SA-R{extract['registry_no']:03d}-{p['keyword'].upper()}"
        metadata = json.dumps({
            "generator": "generate_session_a_extract.py",
            "generator_version": "1.0",
            "semantic_order": p["semantic_order"],
            "keyword": p["keyword"],
            "db_chapter_no": p["db_chapter_no"],
        })
        if p["existing_id"] is not None:
            ops.append(dict(
                op_id=op_id,
                table="prose_section",
                operation="session_a_replace",
                id=p["existing_id"],
                record=dict(
                    body=p["body"],
                    word_count=p["word_count"],
                    heading=p["section_label"],
                    metadata_json=metadata,
                    source_file=f"wa-{extract['registry_no']:03d}-{extract['word']}-sessiona-{today}.md",
                ),
            ))
        else:
            ops.append(dict(
                op_id=op_id,
                table="prose_section",
                operation="insert",
                record=dict(
                    registry_id=extract["registry_id"],
                    section_type_id=p["section_type_id"],
                    heading=p["section_label"],
                    body=p["body"],
                    word_count=p["word_count"],
                    status=STATUS,
                    author=AUTHOR,
                    approved_at=extract["generated_at"],
                    approved_by=AUTHOR,
                    metadata_json=metadata,
                    source_file=f"wa-{extract['registry_no']:03d}-{extract['word']}-sessiona-{today}.md",
                ),
            ))
    # Patch envelope per applicator contract: top-level metadata under
    # _patch_meta (apply_session_patch.py reads `meta = patch.get("_patch_meta", {})`).
    # `registry_id` in _patch_meta carries the registry no — see _validate().
    return dict(
        _patch_meta=dict(
            patch_id=patch_id,
            patch_type="PROSE",
            produced_at=extract["generated_at"],
            registry_id=extract["registry_no"],
            session_b_status=None,
        ),
        operations=ops,
    )


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Generate Session A mechanical extract")
    ap.add_argument("--registry", type=int, required=True, help="registry no")
    ap.add_argument("--out-dir", type=str, default="Sessions/Session_A/Data_Prose",
                    help="where to write the .md file")
    ap.add_argument("--emit-patch", type=str, default=None,
                    help="write JSON PROSE patch to this path (no DB write)")
    ap.add_argument("--apply", action="store_true",
                    help="apply the patch directly via apply_session_patch.py after write")
    ap.add_argument("--no-md", action="store_true",
                    help="skip writing the .md file (only emit patch if --emit-patch given)")
    ap.add_argument("--db", type=str, default=DB_PATH, help="database path")
    args = ap.parse_args()

    conn = open_db(args.db)
    extract = build_extract(conn, args.registry)
    word_slug = extract["word"].replace(" ", "_").replace("(", "").replace(")", "")

    if not args.no_md:
        out_dir = Path(args.out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        md_path = out_dir / f"wa-{extract['registry_no']:03d}-{word_slug}-sessiona-{today_stamp()}.md"
        md_path.write_text(assemble_markdown_file(extract), encoding="utf-8")
        print(f"Wrote markdown: {md_path}")

    if args.emit_patch:
        patch = build_prose_patch(extract)
        patch_path = Path(args.emit_patch)
        patch_path.parent.mkdir(parents=True, exist_ok=True)
        patch_path.write_text(json.dumps(patch, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote patch: {patch_path}")

    if args.apply:
        if not args.emit_patch:
            # Auto-write patch to Sessions/Patches/
            patch = build_prose_patch(extract)
            default_patch_path = Path("Sessions/Patches") / \
                f"wa-{extract['registry_no']:03d}-{word_slug}-sessiona-patch-{today_stamp()}.json"
            default_patch_path.parent.mkdir(parents=True, exist_ok=True)
            default_patch_path.write_text(json.dumps(patch, indent=2, ensure_ascii=False),
                                          encoding="utf-8")
            patch_path = default_patch_path
            print(f"Wrote patch: {patch_path}")
        else:
            patch_path = Path(args.emit_patch)
        # Apply via subprocess (apply_session_patch.py takes the patch file as
        # a positional argument, not a --patch-file flag).
        import subprocess
        cmd = [sys.executable, "scripts/apply_session_patch.py", str(patch_path)]
        print(f"Applying: {' '.join(cmd)}")
        res = subprocess.run(cmd, check=False)
        return res.returncode

    print(f"OK — registry {args.registry} ({extract['word']}) — "
          f"{len(extract['parts'])} sections rendered. "
          f"Total word count: {sum(p['word_count'] for p in extract['parts']):,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
