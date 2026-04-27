"""_pilot_build_readiness_output_v2_20260426.py

v2 readiness-output generator — addresses AI feedback from
wa-obslog-ro-067-goodness-anlys-v1-20260426.md (14 issues + 10 SD pointers).

Sections aligned with `wa-sessionb-analysis-output-v1_1` reading units 1-9:

  A. Registry overview                       [Unit 1]
  B. Stage 1 Completion Record (synthesised) [Instruction S2 prerequisite]
  C. Term inventory                          [Unit 1 prep]
  D. OWNER terms — lexical foundation        [Unit 3] — meaning_parse, senses,
                                                       root family, related words,
                                                       LSJ where available
  E. XREF terms                              [Unit 2]
  F. Verse context groups landscape          [Unit 4] — adds dimension assignments
  G. Correlation signals                     [Unit 5] — XREF sharing, verse
                                                       co-occurrence, shared anchors
  H. Existing SD pointers + findings         [Units 6 + 9]
  I. Thin-evidence phase2 flags              [Unit 8]
  J. Anchor verse material                   [Unit 7] — full verse text with
                                                       clear 🔵 anchor markers
  K. Legacy-VC terms — UNVERIFIED            [v2 strategy §4 mandate]
  L. Stage 2b reference: catalogue questions [Stage 2b prep]
  M. Readiness verification

Usage:
  python scripts/_pilot_build_readiness_output_v2_20260426.py --registry 67

Output:
  outputs/reports/words/wa-{NNN}-{word}-readiness-output-v2-{YYYYMMDD}.md
"""
from __future__ import annotations
import argparse
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("data", "bible_research.db")
OUT_DIR = os.path.join("outputs", "reports", "words")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def open_db(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def get_registry(conn, no: int) -> dict:
    r = conn.execute("""
        SELECT id, no, word, verse_context_status, session_b_status,
               dim_review_status, dim_review_version, cluster_assignment,
               sb_classification, sb_classification_reasoning,
               carry_forward, inference_note, word_synopsis, description,
               dimensions, phase1_status, phase1_term_count, phase1_verse_count
          FROM word_registry WHERE no = ?
    """, (no,)).fetchone()
    if r is None:
        raise SystemExit(f"Registry {no} not found")
    return dict(r)


def get_owner_terms(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT mt.id AS mti, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status, mt.vc_status, mt.md_version,
               mt.anchor_note,
               ti.id AS ti_id
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND mt.delete_flagged = 0
           AND mt.status NOT IN ('delete', 'excluded')
         ORDER BY mt.language DESC, mt.strongs_number
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_xref_terms(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT mt.id AS mti, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status, mt.vc_status,
               ti.id AS ti_id,
               (SELECT wr2.no || ' ' || wr2.word FROM wa_term_inventory ti2
                  JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
                  JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
                 WHERE ti2.strongs_number = mt.strongs_number
                   AND ti2.term_owner_type = 'OWNER'
                   AND ti2.delete_flagged = 0 LIMIT 1) AS owner_registry,
               (SELECT COUNT(*) FROM wa_verse_records vr
                 WHERE vr.term_inv_id = (
                    SELECT id FROM wa_term_inventory
                     WHERE strongs_number = mt.strongs_number
                       AND term_owner_type = 'OWNER'
                       AND delete_flagged = 0 LIMIT 1)
                   AND vr.delete_flagged = 0) AS owner_verse_count
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'XREF'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = ?
           AND mt.delete_flagged = 0
           AND mt.status NOT IN ('delete', 'excluded')
         ORDER BY mt.strongs_number
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_term_state(conn, mti_id: int, ti_id: int) -> dict:
    counts = conn.execute("""
        SELECT
          (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id=? AND vr.delete_flagged=0) AS verses_active,
          (SELECT COUNT(*) FROM wa_verse_records vr WHERE vr.term_inv_id=? AND vr.delete_flagged=1) AS verses_deleted,
          (SELECT COUNT(*) FROM verse_context_group g WHERE g.mti_term_id=? AND g.delete_flagged=0) AS groups_active,
          (SELECT COUNT(*) FROM verse_context_group g WHERE g.mti_term_id=? AND g.delete_flagged=1) AS groups_dissolved,
          (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND vc.delete_flagged=0) AS vc_rows_active,
          (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND vc.delete_flagged=0 AND vc.is_relevant=1) AS vc_relevant,
          (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND vc.delete_flagged=0 AND vc.is_relevant=0 AND vc.set_aside_reason IS NOT NULL) AS vc_set_aside,
          (SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND vc.delete_flagged=0 AND vc.is_anchor=1) AS anchor_count
    """, (ti_id, ti_id, mti_id, mti_id, mti_id, mti_id, mti_id, mti_id)).fetchone()

    groups = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.context_description, vcg.notes,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = vcg.id AND vc.delete_flagged=0 AND vc.is_relevant=1) AS rel_n,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = vcg.id AND vc.delete_flagged=0 AND vc.is_anchor=1) AS anchor_n,
               di.dimension, di.cluster_assignment, di.dimension AS dim
          FROM verse_context_group vcg
          LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id AND di.delete_flagged = 0
         WHERE vcg.mti_term_id = ? AND vcg.delete_flagged = 0
         ORDER BY vcg.group_code
    """, (mti_id,)).fetchall()

    return {**dict(counts), "groups": [dict(g) for g in groups]}


def get_term_lexical(conn, ti_id: int, mti_id: int) -> dict:
    """Lexical foundation per Unit 3: meaning parse + senses + root family + related + LSJ."""
    parsed = conn.execute("""
        SELECT id, top_sense_count, stem_count, has_causative_stem, has_domain_tags,
               parsed_at, parse_version
          FROM wa_meaning_parsed WHERE term_inv_id = ? LIMIT 1
    """, (ti_id,)).fetchone()
    senses = []
    if parsed:
        senses = conn.execute("""
            SELECT level_code, level_depth, parent_level_code, sense_text,
                   is_stem_label, stem_label, domain_tag, sort_order
              FROM wa_meaning_sense
             WHERE parsed_meaning_id = ?
             ORDER BY sort_order
        """, (parsed['id'],)).fetchall()
        senses = [dict(s) for s in senses]
    stems = []
    if parsed:
        stems = conn.execute("""
            SELECT stem_name, stem_type, sense_count, top_sense_text
              FROM wa_meaning_stem WHERE parsed_meaning_id = ?
        """, (parsed['id'],)).fetchall()
        stems = [dict(s) for s in stems]
    root = conn.execute("""
        SELECT root_code, root_language, root_gloss, note
          FROM wa_term_root_family
         WHERE term_inv_id = ? AND delete_flagged = 0
         LIMIT 5
    """, (ti_id,)).fetchall()
    related = conn.execute("""
        SELECT strongs_number, transliteration, gloss, relationship_note
          FROM wa_term_related_words
         WHERE term_inv_id = ? AND delete_flagged = 0
         ORDER BY strongs_number
         LIMIT 30
    """, (ti_id,)).fetchall()
    related_total = conn.execute("""
        SELECT COUNT(*) FROM wa_term_related_words
         WHERE term_inv_id = ? AND delete_flagged = 0
    """, (ti_id,)).fetchone()[0]
    lsj = conn.execute("""
        SELECT lsj_gloss, lsj_domains, lsj_philosophical_note,
               lsj_etymology_note, lsj_cognate_forms, raw_lsj
          FROM wa_lsj_parsed WHERE term_inv_id = ? LIMIT 1
    """, (ti_id,)).fetchone()
    return {
        "parsed": dict(parsed) if parsed else None,
        "senses": senses,
        "stems": stems,
        "root_family": [dict(r) for r in root],
        "related_words": [dict(r) for r in related],
        "related_total": related_total,
        "lsj": dict(lsj) if lsj else None,
    }


def get_term_phase2_flags(conn, ti_id: int) -> list:
    rows = conn.execute("""
        SELECT pf.flag_id, pf.description, pf.source, pf.raised_date,
               qft.flag_code, qft.description AS flag_desc
          FROM wa_term_phase2_flags pf
          LEFT JOIN wa_quality_flag_types qft ON qft.id = pf.flag_id
         WHERE pf.term_inv_id = ? AND (pf.delete_flagged = 0 OR pf.delete_flagged IS NULL)
    """, (ti_id,)).fetchall()
    return [dict(r) for r in rows]


def get_term_verses(conn, ti_id: int, mti_id: int) -> list:
    rows = conn.execute("""
        SELECT vr.id AS vr_id, vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               vr.verse_text, vr.target_word, vr.span_strong_match,
               vc.id AS vc_id, vc.is_relevant, vc.is_anchor, vc.is_related,
               vc.set_aside_reason, vc.notes,
               g.group_code
          FROM wa_verse_records vr
          LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                    AND vc.mti_term_id = ?
                                    AND vc.delete_flagged = 0
          LEFT JOIN verse_context_group g ON g.id = vc.group_id
         WHERE vr.term_inv_id = ?
           AND vr.delete_flagged = 0
         ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (mti_id, ti_id)).fetchall()
    return [dict(r) for r in rows]


def get_open_flags(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT flag_code, flag_label, priority, session_target, raised_date,
               session_raised, description
          FROM wa_session_research_flags
         WHERE registry_id = ?
           AND (resolved = 0 OR resolved IS NULL)
         ORDER BY priority DESC, id
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_session_b_findings(conn, registry_id: int) -> list:
    rows = conn.execute("""
        SELECT id, finding_id, finding_type, finding, anchor_verses,
               raised_date, status, thin_evidence,
               session_b_instruction, pass_ref, study_segment,
               obsolete_reason, superseded_by_id, related_finding_id,
               resolution_note, term_id
          FROM wa_session_b_findings
         WHERE registry_id = ?
           AND (delete_flag = 0 OR delete_flag IS NULL)
         ORDER BY raised_date DESC, id
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def get_correlation_signals(conn, registry_id: int, owner_mti_ids: list) -> dict:
    """Compute correlation signals from XREF sharing + verse co-occurrence + shared anchors."""
    signals = {"xref_sharing": [], "verse_co_occurrence": [], "shared_anchors": []}
    if not owner_mti_ids:
        return signals
    placeholders = ",".join(["?"] * len(owner_mti_ids))

    # XREF sharing: registries that have XREF terms shared with our OWNER strongs
    xref_share = conn.execute(f"""
        SELECT wr2.no AS reg_no, wr2.word AS reg_word, COUNT(DISTINCT mt.strongs_number) AS shared_terms,
               GROUP_CONCAT(DISTINCT mt.strongs_number) AS strongs_list
          FROM mti_terms mt
          JOIN wa_term_inventory ti2 ON ti2.strongs_number = mt.strongs_number
                                    AND ti2.term_owner_type = 'XREF'
                                    AND ti2.delete_flagged = 0
          JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
          JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
         WHERE mt.id IN ({placeholders})
           AND wr2.id != ?
         GROUP BY wr2.no, wr2.word
         ORDER BY shared_terms DESC, wr2.no
    """, (*owner_mti_ids, registry_id)).fetchall()
    signals["xref_sharing"] = [dict(r) for r in xref_share]

    # Verse co-occurrence: same verse_record_id (same book+chap+verse) appears
    # as classified verse_context for terms in OTHER registries
    co_occur = conn.execute(f"""
        SELECT wr2.no AS reg_no, wr2.word AS reg_word,
               COUNT(DISTINCT vc.verse_record_id) AS shared_verses
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          JOIN wa_verse_records vr2 ON vr2.book_id = vr.book_id
                                    AND vr2.chapter = vr.chapter
                                    AND vr2.verse_num = vr.verse_num
                                    AND vr2.delete_flagged = 0
                                    AND vr2.id != vr.id
          JOIN wa_term_inventory ti2 ON ti2.id = vr2.term_inv_id
                                    AND ti2.delete_flagged = 0
                                    AND ti2.term_owner_type = 'OWNER'
          JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
          JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
          JOIN verse_context vc2 ON vc2.verse_record_id = vr2.id
                                AND vc2.delete_flagged = 0
                                AND vc2.is_relevant = 1
         WHERE vc.mti_term_id IN ({placeholders})
           AND vc.delete_flagged = 0
           AND vc.is_relevant = 1
           AND wr2.id != ?
         GROUP BY wr2.no, wr2.word
         HAVING shared_verses >= 3
         ORDER BY shared_verses DESC
         LIMIT 25
    """, (*owner_mti_ids, registry_id)).fetchall()
    signals["verse_co_occurrence"] = [dict(r) for r in co_occur]

    # Shared anchors: same verse reference is anchor in this registry AND another
    shared_anchors = conn.execute(f"""
        SELECT wr2.no AS reg_no, wr2.word AS reg_word,
               vr.reference AS verse_ref,
               COUNT(*) AS n
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          JOIN wa_verse_records vr2 ON vr2.book_id = vr.book_id
                                    AND vr2.chapter = vr.chapter
                                    AND vr2.verse_num = vr.verse_num
                                    AND vr2.delete_flagged = 0
                                    AND vr2.id != vr.id
          JOIN wa_term_inventory ti2 ON ti2.id = vr2.term_inv_id
                                    AND ti2.delete_flagged = 0
                                    AND ti2.term_owner_type = 'OWNER'
          JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
          JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
          JOIN verse_context vc2 ON vc2.verse_record_id = vr2.id
                                AND vc2.delete_flagged = 0
                                AND vc2.is_anchor = 1
         WHERE vc.mti_term_id IN ({placeholders})
           AND vc.is_anchor = 1
           AND vc.delete_flagged = 0
           AND wr2.id != ?
         GROUP BY wr2.no, wr2.word, vr.reference
         ORDER BY wr2.no, vr.reference
    """, (*owner_mti_ids, registry_id)).fetchall()
    signals["shared_anchors"] = [dict(r) for r in shared_anchors]

    return signals


def get_catalogue_questions(conn, registry_no: int) -> dict:
    """Return generic (Sections 1-5) + any registry-specific catalogue questions.

    Per researcher direction (2026-04-26):
      - Generic = the 147 chapter questions in Sections 1-5 (apply to every word).
      - Registry-specific = questions where source_registry_no = current registry
        (these are word-specific Extensions, included only when this is the word
        being analysed).
      - Word-specific Extensions for OTHER registries and Evidence-Flag questions
        are NOT included in the readiness output for this word.
    """
    generic = conn.execute("""
        SELECT obs_id, question_code, section, source_word, source_registry_no,
               question_text, pattern_type, scope, status
          FROM wa_obs_question_catalogue
         WHERE (deleted = 0 OR deleted IS NULL)
           AND section LIKE 'Section %'
         ORDER BY section, obs_id
    """).fetchall()
    generic = [dict(r) for r in generic]
    by_section = defaultdict(list)
    for r in generic:
        by_section[r['section'] or '(no section)'].append(r)
    # Registry-specific: questions whose source_registry_no matches current registry
    # (word-specific Extensions like 'Compassion Extensions' are sourced from reg 23 etc.)
    registry_specific = conn.execute("""
        SELECT obs_id, question_code, section, source_word, source_registry_no,
               question_text, pattern_type, scope, status
          FROM wa_obs_question_catalogue
         WHERE (deleted = 0 OR deleted IS NULL)
           AND source_registry_no = ?
           AND section NOT LIKE 'Section %'
         ORDER BY section, obs_id
    """, (registry_no,)).fetchall()
    return {
        "generic": generic,
        "generic_by_section": dict(by_section),
        "generic_section_summary": [(s, len(qs)) for s, qs in by_section.items()],
        "registry_specific": [dict(r) for r in registry_specific],
    }


def get_schema_version(conn) -> str:
    r = conn.execute(
        "SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1"
    ).fetchone()
    return r[0] if r else "unknown"


def fmt_blockquote(text: str) -> list:
    L = []
    for line in (text or "").split("\n"):
        L.append(f"> {line}" if line else ">")
    return L


# ---- Section renderers ---------------------------------------------------


def render_section_a_overview(reg: dict, owners: list, xrefs: list,
                              flags_count: int, findings_count: int) -> list:
    L = []
    L.append("## A. Registry Overview")
    L.append("")
    L.append(f"- **Registry no:** `{reg['no']}` · **word:** `{reg['word']}`")
    L.append(f"- **verse_context_status:** `{reg['verse_context_status'] or 'NULL'}`")
    L.append(f"- **session_b_status:** `{reg['session_b_status'] or 'NULL'}`")
    L.append(f"- **dim_review_status:** `{reg['dim_review_status'] or 'NULL'}` "
             f"(version `{reg['dim_review_version'] or '-'}`)")
    L.append(f"- **cluster_assignment:** `{reg['cluster_assignment'] or 'NULL'}`")
    L.append(f"- **sb_classification:** `{reg['sb_classification'] or 'NULL'}`")
    L.append(f"- **carry_forward:** `{reg['carry_forward']}`")
    L.append(f"- **dimensions (registry-level):** `{reg['dimensions'] or 'NULL'}`")
    L.append("")
    L.append(f"**Phase 1 (registry-scoped):**")
    L.append(f"- `phase1_status`: `{reg['phase1_status'] or 'NULL'}`")
    L.append(f"- `phase1_term_count`: {reg['phase1_term_count'] or 0}  "
             f"(programme-wide aggregate including XREF and historical terms — "
             f"current OWNER count is {len(owners)}, XREF {len(xrefs)})")
    L.append(f"- `phase1_verse_count`: {reg['phase1_verse_count'] or 0}  "
             f"(programme-wide aggregate; current registry verse counts shown per term in §C)")
    L.append("")
    L.append(f"**Open flags:** {flags_count} unresolved · "
             f"**Existing session_b_findings:** {findings_count}")
    L.append("")
    if reg['inference_note']:
        L.append("**Researcher inference_note (verbatim):**")
        L.append("")
        L += fmt_blockquote(reg['inference_note'])
        L.append("")
    if reg['word_synopsis']:
        L.append("**Researcher word_synopsis (verbatim):**")
        L.append("")
        L += fmt_blockquote(reg['word_synopsis'])
        L.append("")
    if reg['description']:
        L.append("**Description:**")
        L.append("")
        L += fmt_blockquote(reg['description'])
        L.append("")
    if reg['sb_classification_reasoning']:
        L.append("**sb_classification_reasoning:**")
        L.append("")
        L += fmt_blockquote(reg['sb_classification_reasoning'])
        L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_b_completion_record(reg: dict, owners: list,
                                       schema: str, ts: str) -> list:
    L = []
    L.append("## B. Stage 1 Completion Record (synthesised from DB state)")
    L.append("")
    L.append("_The Analysis Output instruction's S2 expects a Stage 1 Completion Record from the "
             "Analysis Readiness session. Under the v2 strategy the readiness `.md` IS that record. "
             "The synthesised confirmation below derives the seven-domain pass criteria from current "
             "DB state at generation time._")
    L.append("")
    md_versions = sorted({t['md_version'] for t in owners if t['md_version']})
    vc_completed = sum(1 for t in owners if t['vc_status'] == 'vc_completed')
    legacy = sum(1 for t in owners if (t['vc_status'] or 'not_done') in ('not_done', 'to_revise'))
    L.append(f"- **Generation timestamp:** `{ts}`")
    L.append(f"- **Schema version:** `{schema}`")
    L.append(f"- **OWNER term md_versions present:** `{md_versions or '(none / legacy)'}`")
    L.append(f"  (this is the project's audit equivalent of `meta.export_version`)")
    L.append(f"- **OWNER terms vc_completed:** {vc_completed} / {len(owners)}")
    L.append(f"- **OWNER terms legacy-VC (not_done):** {legacy} / {len(owners)}")
    L.append("")
    L.append("**Synthesised seven-domain pass status:**")
    L.append("")
    L.append("| Domain | Check | Status |")
    L.append("|---|---|---|")
    L.append(f"| A — Data completeness | Registry status fields populated | "
             f"{'✓' if (reg['verse_context_status'] or reg['session_b_status']) else '✗'} |")
    L.append(f"| A — Data completeness | OWNER terms have md_version | "
             f"{'✓' if md_versions else '✗ — legacy era'} |")
    L.append(f"| B — VC completeness | All OWNER terms vc_completed | "
             f"{'✓' if vc_completed == len(owners) else f'partial — {legacy} legacy-VC remain (handled per §K)'} |")
    L.append(f"| C — Group integrity | Active groups present per OWNER term | "
             f"{'✓ (see §F)'} |")
    L.append(f"| D — Verse coverage | All OWNER terms have ≥1 active verse | "
             f"{'see §C term inventory'} |")
    L.append(f"| E — Cross-registry | XREF terms documented (§E) | "
             f"{'✓'} |")
    L.append(f"| F — Flag closure | All resolved flags closed | "
             f"{'see §H open flags'} |")
    L.append(f"| G — Researcher fields | inference_note / word_synopsis preserved | "
             f"{'✓ — preserved verbatim in §A' if (reg['inference_note'] or reg['word_synopsis']) else '✗ — researcher narrative absent'} |")
    L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_c_inventory(owners: list, states: dict) -> list:
    L = []
    L.append("## C. Term Inventory — OWNER Terms")
    L.append("")
    L.append("| strongs | translit | gloss | lang | status | vc_status | md_v | verses | groups (a/d) | vc rel/sa | anchors |")
    L.append("|---|---|---|---|---|---|---:|---:|---:|---|---:|")
    for t in owners:
        s = states[t['mti']]
        L.append(f"| `{t['strongs_number']}` | {t['transliteration'] or ''} | "
                 f"{(t['gloss'] or '')[:30]} | {t['language'][:1]} | `{t['status']}` | "
                 f"**`{t['vc_status'] or 'NULL'}`** | {t['md_version'] or '-'} | "
                 f"{s['verses_active']} | {s['groups_active']}/{s['groups_dissolved']} | "
                 f"{s['vc_relevant']}/{s['vc_set_aside']} | {s['anchor_count']} |")
    L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_d_lexical(owners: list, lexical: dict) -> list:
    L = []
    L.append("## D. OWNER Terms — Lexical Foundation [Unit 3]")
    L.append("")
    L.append("Per term: structured meaning parse (`wa_meaning_parsed` / `wa_meaning_sense`), root family, related-words sample, and LSJ data where available.")
    L.append("")
    for t in owners:
        lex = lexical[t['mti']]
        L.append(f"### `{t['strongs_number']}` — {t['transliteration'] or ''} \"{t['gloss'] or ''}\"")
        L.append("")
        L.append(f"**Identity:** mti={t['mti']} · ti={t['ti_id']} · language={t['language']} · status=`{t['status']}` · md_v={t['md_version'] or '-'}")
        L.append("")
        if t.get('anchor_note'):
            L.append("**anchor_note:**")
            L.append("")
            L += fmt_blockquote(t['anchor_note'])
            L.append("")
        # Meaning parse
        if lex['parsed']:
            p = lex['parsed']
            L.append(f"**Meaning parse** (parser v{p['parse_version']}, parsed {p['parsed_at']}): "
                     f"{p['top_sense_count']} top senses · {p['stem_count']} stems · "
                     f"causative={bool(p['has_causative_stem'])} · domain_tags={bool(p['has_domain_tags'])}")
            L.append("")
            if lex['stems']:
                L.append("Stems:")
                for st in lex['stems']:
                    L.append(f"- `{st['stem_name']}` ({st['stem_type']}) — {st['sense_count']} senses · top: {st['top_sense_text']}")
                L.append("")
            if lex['senses']:
                L.append("Senses (top-level):")
                top = [s for s in lex['senses'] if s['level_depth'] == 1]
                for s in top[:30]:
                    tag = f" [{s['domain_tag']}]" if s['domain_tag'] else ""
                    L.append(f"- `{s['level_code']}`{tag}: {s['sense_text']}")
                if len(top) > 30:
                    L.append(f"- … and {len(top) - 30} more top senses (see DB).")
                L.append("")
                # Sub-senses
                subs = [s for s in lex['senses'] if s['level_depth'] > 1]
                if subs:
                    L.append(f"Sub-senses (depth > 1): {len(subs)} entries — present in DB; first 15:")
                    for s in subs[:15]:
                        L.append(f"  - `{s['level_code']}` (under `{s['parent_level_code']}`): {s['sense_text']}")
                    L.append("")
        else:
            L.append("**Meaning parse:** _no parsed meaning row found in `wa_meaning_parsed` for this term._ Lexical work proceeds from gloss + group descriptions + verse evidence.")
            L.append("")
        # Root family
        if lex['root_family']:
            L.append("**Root family:**")
            for r in lex['root_family']:
                note = f" — {r['note']}" if r['note'] else ""
                L.append(f"- `{r['root_code']}` ({r['root_language']}): {r['root_gloss'] or '-'}{note}")
            L.append("")
        # Related words (capped sample)
        if lex['related_words']:
            L.append(f"**Related words ({lex['related_total']} total; sample of {len(lex['related_words'])}):**")
            for r in lex['related_words'][:15]:
                note = f" — {r['relationship_note']}" if r['relationship_note'] else ""
                L.append(f"- `{r['strongs_number'] or '-'}` {r['transliteration'] or ''} \"{r['gloss'] or ''}\"{note}")
            if len(lex['related_words']) > 15:
                L.append(f"- … and {len(lex['related_words']) - 15} more shown of {lex['related_total']} total")
            L.append("")
        # LSJ
        if lex['lsj']:
            ls = lex['lsj']
            L.append("**LSJ (Greek lexicon):**")
            if ls['lsj_gloss']:
                L.append(f"- gloss: {ls['lsj_gloss']}")
            if ls['lsj_domains']:
                L.append(f"- domains: {ls['lsj_domains']}")
            if ls['lsj_etymology_note']:
                L.append(f"- etymology: {ls['lsj_etymology_note']}")
            if ls['lsj_philosophical_note']:
                L.append(f"- philosophical note: {ls['lsj_philosophical_note']}")
            if ls['lsj_cognate_forms']:
                L.append(f"- cognates: {ls['lsj_cognate_forms']}")
            L.append("")
        elif t['language'] == 'Greek':
            L.append("**LSJ:** _not parsed for this term (LSJ data is sparse — meaning work proceeds without it)._")
            L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_e_xrefs(xrefs: list) -> list:
    L = []
    L.append(f"## E. XREF Terms [Unit 2] ({len(xrefs)})")
    L.append("")
    if not xrefs:
        L.append("_None._")
        L.append("")
    else:
        L.append("| strongs | translit | gloss | lang | OWNER registry | status | OWNER verse count |")
        L.append("|---|---|---|---|---|---|---:|")
        for t in xrefs:
            L.append(f"| `{t['strongs_number']}` | {t['transliteration'] or ''} | "
                     f"{(t['gloss'] or '')[:30]} | {t['language'][:1]} | "
                     f"{t['owner_registry'] or '?'} | `{t['status']}` | "
                     f"{t['owner_verse_count']} |")
        L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_f_groups_landscape(owners: list, states: dict) -> list:
    L = []
    L.append("## F. Verse Context Groups — Landscape [Unit 4]")
    L.append("")
    L.append("Per OWNER term: all active groups with descriptions, **dimension assignments** "
             "(from `wa_dimension_index`), anchor counts, and relevant counts.")
    L.append("")
    for t in owners:
        s = states[t['mti']]
        L.append(f"### `{t['strongs_number']}` — {len(s['groups'])} groups")
        L.append("")
        if not s['groups']:
            L.append("_No active groups (term may be legacy-VC or set-aside-only)._")
            L.append("")
            continue
        for g in s['groups']:
            dim = f"`{g['dimension']}`" if g['dimension'] else "_NULL_"
            cluster = f"`{g['cluster_assignment']}`" if g['cluster_assignment'] else "_NULL_"
            L.append(f"- **`{g['group_code']}`** — {g['rel_n']} relevant · {g['anchor_n']} anchor verse(s) · "
                     f"dimension: {dim} · cluster: {cluster}")
            desc = (g['context_description'] or '').strip()
            if desc:
                L.append(f"  - *{desc}*")
            if g['notes']:
                L.append(f"  - notes: {g['notes']}")
        L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_g_correlation(signals: dict) -> list:
    L = []
    L.append("## G. Correlation Signals [Unit 5] (computed)")
    L.append("")
    L.append("Three signal types computed at generation time from DB state:")
    L.append("- **XREF sharing** — registries that own terms appearing as XREF in this registry")
    L.append("- **Verse co-occurrence** — same verse classified is_relevant=1 in this registry AND another (≥3 shared verses)")
    L.append("- **Shared anchors** — same verse appears as is_anchor=1 in this registry AND another")
    L.append("")
    L.append("### G.1 XREF sharing")
    L.append("")
    if signals["xref_sharing"]:
        L.append("| Other registry | shared OWNER strongs | strongs list |")
        L.append("|---|---:|---|")
        for r in signals["xref_sharing"]:
            L.append(f"| {r['reg_no']} {r['reg_word']} | {r['shared_terms']} | `{r['strongs_list']}` |")
    else:
        L.append("_No XREF sharing._")
    L.append("")
    L.append("### G.2 Verse co-occurrence (≥3 shared)")
    L.append("")
    if signals["verse_co_occurrence"]:
        L.append("| Other registry | shared verses |")
        L.append("|---|---:|")
        for r in signals["verse_co_occurrence"]:
            L.append(f"| {r['reg_no']} {r['reg_word']} | {r['shared_verses']} |")
    else:
        L.append("_No verse co-occurrence at threshold._")
    L.append("")
    L.append("### G.3 Shared anchors")
    L.append("")
    if signals["shared_anchors"]:
        L.append("| Other registry | shared anchor verse |")
        L.append("|---|---|")
        for r in signals["shared_anchors"]:
            L.append(f"| {r['reg_no']} {r['reg_word']} | {r['verse_ref']} |")
    else:
        L.append("_No shared anchor verses._")
    L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_h_findings_flags(findings: list, flags: list) -> list:
    L = []
    L.append("## H. Existing SD Pointers + session_b_findings [Units 6 + 9]")
    L.append("")
    L.append(f"### H.1 Existing session_b_findings ({len(findings)})")
    L.append("")
    if findings:
        for f in findings:
            L.append(f"#### `{f['finding_id']}` — `{f['finding_type']}`")
            L.append("")
            L.append(f"- **status:** `{f['status'] or 'NULL'}` · "
                     f"**thin_evidence:** {f['thin_evidence']} · "
                     f"**raised:** {f['raised_date']} · "
                     f"**term_id:** {f['term_id'] or '-'}")
            L.append("")
            if f['finding']:
                L += fmt_blockquote(f['finding'])
                L.append("")
            if f['anchor_verses']:
                L.append(f"**Anchor verses cited:** {f['anchor_verses']}")
                L.append("")
    else:
        L.append("_None._")
        L.append("")
    L.append(f"### H.2 Open SD pointers + research flags ({len(flags)})")
    L.append("")
    if not flags:
        L.append("_None._")
    else:
        L.append("| flag_code | label | priority | session | raised |")
        L.append("|---|---|---|---|---|")
        for f in flags:
            L.append(f"| `{f['flag_code']}` | {(f['flag_label'] or '')[:50]} | "
                     f"{f['priority'] or '-'} | {f['session_target'] or '-'} | "
                     f"{f['raised_date'] or '-'} |")
        L.append("")
        for f in flags:
            L.append(f"#### {f['flag_label'] or f['flag_code']}")
            L.append("")
            if f['description']:
                L += fmt_blockquote(f['description'])
            L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_i_phase2(owners: list, phase2: dict) -> list:
    L = []
    L.append("## I. Thin-Evidence Phase2 Flags [Unit 8]")
    L.append("")
    has_any = any(phase2.get(t['mti']) for t in owners)
    if not has_any:
        L.append("_No phase2 flags on any OWNER term._")
        L.append("")
    else:
        for t in owners:
            flags = phase2.get(t['mti'], [])
            if not flags:
                continue
            L.append(f"### `{t['strongs_number']}` ({len(flags)} flag(s))")
            L.append("")
            for f in flags:
                L.append(f"- **`{f['flag_code'] or f['flag_id']}`** — {f.get('flag_desc', '')}")
                if f['description']:
                    L.append(f"  - {f['description']}")
                L.append(f"  - source: {f['source'] or '-'} · raised: {f['raised_date'] or '-'}")
            L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_j_verses(owners: list, verses_by_term: dict) -> list:
    L = []
    L.append("## J. Anchor Verse Material — All Verbatim Verse Text [Unit 7]")
    L.append("")
    L.append("Each verse listed with: group code · `is_relevant` (✓/✗) · `is_anchor` (🔵 marker) · "
             "`set_aside_reason` if set aside · `target_word` · full verse text. **Anchor verses (🔵) are the primary reading targets per Unit 7.**")
    L.append("")
    for t in owners:
        verses = verses_by_term[t['mti']]
        anchor_count = sum(1 for v in verses if v.get('is_anchor'))
        classified = sum(1 for v in verses if v.get('vc_id'))
        L.append(f"### `{t['strongs_number']}` — {classified}/{len(verses)} classified · "
                 f"{anchor_count} anchor verse(s)")
        L.append("")
        if not verses:
            L.append("_No active verses._")
            L.append("")
            continue
        # Group by group_code
        by_group = defaultdict(list)
        for v in verses:
            key = v.get('group_code') or ('SET-ASIDE' if v.get('vc_id') and v['is_relevant'] == 0 else 'UNCLASSIFIED')
            by_group[key].append(v)

        def sort_key(k):
            if k == 'UNCLASSIFIED': return (2, k)
            if k == 'SET-ASIDE': return (1, k)
            return (0, k)

        for group_key in sorted(by_group.keys(), key=sort_key):
            items = by_group[group_key]
            anchors_here = [v['reference'] for v in items if v.get('is_anchor')]
            anchor_str = f" — anchors: {', '.join(anchors_here)}" if anchors_here else ""
            L.append(f"**Group `{group_key}`** ({len(items)} verse{'s' if len(items)!=1 else ''}{anchor_str})")
            L.append("")
            # Sort: anchors first, then by reference
            items_sorted = sorted(items, key=lambda v: (0 if v.get('is_anchor') else 1, v.get('book_id', 0), v.get('chapter', 0), v.get('verse_num', 0)))
            for v in items_sorted:
                anchor = " 🔵" if v.get('is_anchor') else ""
                relevant = "✓" if v.get('is_relevant') == 1 else ("✗" if v.get('is_relevant') == 0 else "—")
                sa = f" [set_aside: {v['set_aside_reason']}]" if v.get('set_aside_reason') else ""
                target = f" *target: {v['target_word']}*" if v.get('target_word') else ""
                L.append(f"- **{v['reference']}**{anchor} ({relevant}){sa}{target}")
                text = (v.get('verse_text') or '').strip().replace('\n', ' ')
                if text:
                    L.append(f"  > {text}")
                if v.get('notes'):
                    L.append(f"  - notes: {v['notes']}")
            L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_k_legacy_vc(owners: list, states: dict) -> list:
    L = []
    legacy = [t for t in owners if (t['vc_status'] or 'not_done') in ('not_done', 'to_revise')]
    L.append("## K. Legacy-VC Terms — UNVERIFIED UNDER v3 CONTRACTS")
    L.append("")
    if not legacy:
        L.append("**No legacy-VC terms.** All OWNER terms in this registry are `vc_status='vc_completed'` — classifications were performed under v3_x contracts.")
        L.append("")
    else:
        L.append(f"**{len(legacy)} term(s)** in this registry carry classification rows from pre-v3 work.")
        L.append("")
        L.append("> **Analytical instruction (per vc-corrective-strategy v2 §4):** these classifications are facts on the ground. The VC programme has not re-classified them under v3 contracts. If a finding depends *materially* on a verse classification, group description, or anchor designation from this section, emit an `ANALYSIS_VC_UNVERIFIED_MATERIAL` flag specifying the source term(s), verses, the alternative scenario, and the predicted change to the finding.")
        L.append("")
        L.append("| strongs | gloss | vc_status | verses | groups | vc_rows |")
        L.append("|---|---|---|---:|---:|---:|")
        for t in legacy:
            s = states[t['mti']]
            L.append(f"| `{t['strongs_number']}` | {(t['gloss'] or '')[:30]} | "
                     f"`{t['vc_status'] or 'NULL'}` | {s['verses_active']} | "
                     f"{s['groups_active']} | {s['vc_rows_active']} |")
        L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_l_catalogue(catalogue: dict, registry_no: int, registry_word: str) -> list:
    """Stage 2b foundational input — generic catalogue + any registry-specific questions.

    Per researcher direction (2026-04-26):
      - Generic = the 147 chapter questions in Sections 1-5. Apply to every word.
        Embedded as JSON; the section grouping IS the Stage 2b chapter structure.
      - Registry-specific = questions sourced from THIS registry (word-specific
        Extensions). Included only when this registry has any.
      - Other word-specific Extensions and Evidence-Flag questions are NOT
        included here.
    """
    import json
    L = []
    generic = catalogue['generic']
    generic_by_section = catalogue['generic_by_section']
    section_summary = catalogue['generic_section_summary']
    registry_specific = catalogue['registry_specific']
    L.append("## L. Stage 2b Foundational Input — Observation Question Catalogue")
    L.append("")
    L.append(f"**Generic questions: {len(generic)}** across {len(generic_by_section)} sections. The section grouping IS the Stage 2b chapter structure — Stage 2b works through the catalogue section-by-section, producing answers grouped by section.")
    L.append("")
    L.append("### Section summary (generic)")
    L.append("")
    L.append("| Section | n questions |")
    L.append("|---|---:|")
    for s, n in section_summary:
        L.append(f"| {s} | {n} |")
    L.append("")
    L.append("### Generic questions (JSON, grouped by section)")
    L.append("")
    L.append("Format: JSON. Structure: as-is from `wa_obs_question_catalogue`. Apply to every word.")
    L.append("")
    grouped_payload = {
        "total": len(generic),
        "section_count": len(generic_by_section),
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
            for s, qs in generic_by_section.items()
        }
    }
    L.append("```json")
    L.append(json.dumps(grouped_payload, indent=2, ensure_ascii=False))
    L.append("```")
    L.append("")
    # Registry-specific
    L.append(f"### Registry-specific questions for {registry_no:03d} {registry_word}")
    L.append("")
    if not registry_specific:
        L.append(f"_None._ No questions in `wa_obs_question_catalogue` are sourced from registry {registry_no} ({registry_word}).")
        L.append("")
    else:
        L.append(f"**{len(registry_specific)} question(s)** sourced from this registry's prior work. Include in Stage 2b alongside the generic questions.")
        L.append("")
        rs_payload = {
            "registry_no": registry_no,
            "registry_word": registry_word,
            "total": len(registry_specific),
            "questions": [
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
                for q in registry_specific
            ],
        }
        L.append("```json")
        L.append(json.dumps(rs_payload, indent=2, ensure_ascii=False))
        L.append("```")
        L.append("")
    L.append("---")
    L.append("")
    return L


def get_open_session_b_items(conn, registry_id: int) -> list:
    """Section N source — open Session B findings to be addressed this session.

    Per architecture v1 §11.4: every open finding must be resolved in this
    analytical session via one of the four resolution paths.
    """
    rows = conn.execute("""
        SELECT id, finding_id, finding_type, finding, anchor_verses,
               raised_date, status, thin_evidence, term_id,
               session_b_instruction, pass_ref
          FROM wa_session_b_findings
         WHERE registry_id = ?
           AND status = 'open'
           AND (delete_flag = 0 OR delete_flag IS NULL)
         ORDER BY raised_date DESC, id
    """, (registry_id,)).fetchall()
    return [dict(r) for r in rows]


def render_section_n_open_items(open_items: list, registry_no: int) -> list:
    """§N — Open Session B Items (must be resolved this session).

    Each item must have an outcome by session close:
      (a) Q&A answer (via wa_finding_catalogue_links)
      (b) Follow-up research question (new GAP)
      (c) SD pointer (cross-registry research target)
      (d) Marked no_longer_relevant with reason
    """
    L = []
    L.append(f"## N. Open Session B Items — must resolve this session")
    L.append("")
    if not open_items:
        L.append("**No open items.** This is either a first analytical session for the registry, "
                 "or all prior open items have been resolved.")
        L.append("")
        L.append("---")
        L.append("")
        return L
    L.append(f"**{len(open_items)} open item(s) carried forward.** Each must reach one of these outcomes "
             "by session close — recorded back on the Session B finding row:")
    L.append("")
    L.append("- **(a)** Resolve via Q&A: link to a catalogue question + record answer "
             "→ `wa_finding_catalogue_links` row + `wa_session_b_findings.status='resolved_qa'`")
    L.append("- **(b)** Raise follow-up research question (new GAP catalogue entry) "
             "→ inserts a new `wa_obs_question_catalogue` row + `status='resolved_qa'`")
    L.append("- **(c)** Convert to SD pointer (cross-registry research target) "
             "→ `wa_session_research_flags` insert + `status='resolved_sd'`")
    L.append("- **(d)** Mark no_longer_relevant with reason "
             "→ `wa_session_b_findings.status='not_relevant'` + `obsolete_reason`")
    L.append("")
    L.append("**Items below are not optional. Each must be addressed.**")
    L.append("")
    for item in open_items:
        finding_id = item.get('finding_id') or f"id={item['id']}"
        ftype = item.get('finding_type') or 'OBSERVATION'
        L.append(f"### `{finding_id}` — {ftype}")
        L.append("")
        L.append(f"- **Raised:** {item.get('raised_date') or '-'} · "
                 f"**Term context:** {item.get('term_id') or '-'} · "
                 f"**Source instruction:** {item.get('session_b_instruction') or '-'} · "
                 f"**Thin evidence:** {item.get('thin_evidence') or 0}")
        L.append("")
        if item.get('finding'):
            for line in (item['finding']).split('\n'):
                L.append(f"> {line}" if line else ">")
            L.append("")
        if item.get('anchor_verses'):
            L.append(f"**Anchor verses cited:** {item['anchor_verses']}")
            L.append("")
        L.append("**Required outcome (one of a/b/c/d above). Record on this finding row at session close.**")
        L.append("")
    L.append("---")
    L.append("")
    return L


def render_section_m_verification(owners: list, schema: str, ts: str,
                                  reg: dict, states: dict) -> list:
    L = []
    L.append("## M. Readiness Verification")
    L.append("")
    L.append(f"- **Generated at:** `{ts}`")
    L.append(f"- **Schema version:** `{schema}`")
    md_versions = sorted({t['md_version'] for t in owners if t['md_version']})
    L.append(f"- **OWNER term md_versions present:** `{md_versions or '(none / legacy)'}`")
    L.append("")
    L.append("**Stage 1 quick checks:**")
    L.append("")
    L.append(f"- Registry status fields populated: {'✓' if (reg['verse_context_status'] or reg['session_b_status']) else '✗'}")
    L.append(f"- OWNER term inventory non-empty: {'✓' if owners else '✗'}")
    L.append(f"- All OWNER terms have at least 1 verse: "
             f"{'✓' if all(states[t['mti']]['verses_active'] > 0 for t in owners) else '✗'}")
    L.append(f"- Researcher fields preserved: "
             f"{'present' if (reg['inference_note'] or reg['word_synopsis']) else 'absent — researcher narrative not yet written'}")
    L.append("")
    issues = []
    if reg['session_b_status'] == 'Verse Context Reset':
        issues.append("session_b_status='Verse Context Reset' — investigate whether this is current or stale post-VCB-13.")
    if reg['dim_review_status'] is None:
        issues.append("dim_review_status NULL — dimensional analysis in §F will be limited to dimensions actually populated in `wa_dimension_index` for individual groups.")
    if issues:
        L.append("**Notes / concerns:**")
        for i in issues:
            L.append(f"- {i}")
        L.append("")
    L.append("---")
    L.append("")
    return L


# ---- Main build ----------------------------------------------------------


def build(conn, registry_no: int) -> str:
    reg = get_registry(conn, registry_no)
    owners = get_owner_terms(conn, reg['id'])
    xrefs = get_xref_terms(conn, reg['id'])
    flags = get_open_flags(conn, reg['id'])
    findings = get_session_b_findings(conn, reg['id'])
    catalogue = get_catalogue_questions(conn, registry_no)
    schema = get_schema_version(conn)
    ts = now_iso()

    states = {t['mti']: get_term_state(conn, t['mti'], t['ti_id']) for t in owners}
    lexical = {t['mti']: get_term_lexical(conn, t['ti_id'], t['mti']) for t in owners}
    phase2 = {t['mti']: get_term_phase2_flags(conn, t['ti_id']) for t in owners}
    verses_by_term = {t['mti']: get_term_verses(conn, t['ti_id'], t['mti']) for t in owners}
    signals = get_correlation_signals(conn, reg['id'], [t['mti'] for t in owners])

    L: list[str] = []
    L.append(f"# wa-{registry_no:03d}-{reg['word']} — Analysis Readiness Output (v2)")
    L.append("")
    L.append(f"_Pilot v2 generation · {ts} · schema {schema}_")
    L.append("")
    L.append(f"_Strategy: vc-corrective-strategy-v2 §4 · sections aligned with `wa-sessionb-analysis-output-v1_1` reading units 1-9._")
    L.append("")
    L.append(f"_Source of truth: live DB at generation time. Regenerate to refresh._")
    L.append("")
    L.append("**Section map:**")
    L.append("")
    L.append("- A. Registry overview — Unit 1")
    L.append("- B. Stage 1 Completion Record (synthesised) — instruction S2 prerequisite")
    L.append("- C. Term inventory — Unit 1 prep")
    L.append("- D. OWNER terms — lexical foundation — Unit 3")
    L.append("- E. XREF terms — Unit 2")
    L.append("- F. Verse context groups landscape — Unit 4 (with dimension assignments)")
    L.append("- G. Correlation signals — Unit 5 (computed)")
    L.append("- H. Existing SD pointers + session_b_findings — Units 6 + 9")
    L.append("- I. Thin-evidence phase2 flags — Unit 8")
    L.append("- J. Anchor verse material — Unit 7 (full verbatim verse text)")
    L.append("- K. Legacy-VC terms — UNVERIFIED — v2 strategy mandate")
    L.append("- L. Stage 2b reference — observation question catalogue")
    L.append("- N. Open Session B items (carried forward; must resolve this session)")
    L.append("- M. Readiness verification")
    L.append("")
    L.append("---")
    L.append("")

    L += render_section_a_overview(reg, owners, xrefs, len(flags), len(findings))
    L += render_section_b_completion_record(reg, owners, schema, ts)
    L += render_section_c_inventory(owners, states)
    L += render_section_d_lexical(owners, lexical)
    L += render_section_e_xrefs(xrefs)
    L += render_section_f_groups_landscape(owners, states)
    L += render_section_g_correlation(signals)
    L += render_section_h_findings_flags(findings, flags)
    L += render_section_i_phase2(owners, phase2)
    L += render_section_j_verses(owners, verses_by_term)
    L += render_section_k_legacy_vc(owners, states)
    L += render_section_l_catalogue(catalogue, registry_no, reg['word'])
    open_items = get_open_session_b_items(conn, reg['id'])
    L += render_section_n_open_items(open_items, registry_no)
    L += render_section_m_verification(owners, schema, ts, reg, states)
    L.append(f"*End of readiness output v3 — wa-{registry_no:03d}-{reg['word']}.*")
    return "\n".join(L)


def build_json(conn, registry_no: int) -> dict:
    """Same data as build() but as a structured dict — for parallel .json output."""
    reg = get_registry(conn, registry_no)
    owners = get_owner_terms(conn, reg['id'])
    xrefs = get_xref_terms(conn, reg['id'])
    flags = get_open_flags(conn, reg['id'])
    findings = get_session_b_findings(conn, reg['id'])
    catalogue = get_catalogue_questions(conn, registry_no)
    schema = get_schema_version(conn)
    ts = now_iso()

    states = {t['mti']: get_term_state(conn, t['mti'], t['ti_id']) for t in owners}
    lexical = {t['mti']: get_term_lexical(conn, t['ti_id'], t['mti']) for t in owners}
    phase2 = {t['mti']: get_term_phase2_flags(conn, t['ti_id']) for t in owners}
    verses_by_term = {t['mti']: get_term_verses(conn, t['ti_id'], t['mti']) for t in owners}
    signals = get_correlation_signals(conn, reg['id'], [t['mti'] for t in owners])

    open_items = get_open_session_b_items(conn, reg['id'])

    return {
        "meta": {
            "generated_at": ts,
            "schema_version": schema,
            "registry_no": registry_no,
            "registry_word": reg['word'],
            "generator": "_pilot_build_readiness_output_v2_20260426.py",
            "strategy": "vc-corrective-strategy-v2-20260426.md",
            "version": "v5",
        },
        "registry": reg,
        "owner_terms": owners,
        "xref_terms": xrefs,
        "term_state": {str(k): v for k, v in states.items()},
        "term_lexical": {str(k): v for k, v in lexical.items()},
        "term_phase2_flags": {str(k): v for k, v in phase2.items()},
        "term_verses": {str(k): v for k, v in verses_by_term.items()},
        "correlation_signals": signals,
        "open_flags": flags,
        "session_b_findings": findings,
        "open_session_b_items": open_items,
        "catalogue": catalogue,
    }


def main() -> int:
    import json
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--out", default=None,
                    help="Override .md output path. JSON path is derived by .md→.json.")
    ap.add_argument("--md-only", action="store_true", help="suppress .json output")
    ap.add_argument("--json-only", action="store_true", help="suppress .md output")
    args = ap.parse_args()

    conn = open_db(args.db)
    reg = get_registry(conn, args.registry)
    out_dir = OUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    base = (args.out and os.path.splitext(args.out)[0]) or \
        f"wa-{args.registry:03d}-{reg['word']}-readiness-output-v5-{today_compact()}"

    if not args.json_only:
        md_text = build(conn, args.registry)
        md_path = os.path.join(out_dir, f"{base}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        sz = os.path.getsize(md_path)
        print(f"Wrote: {md_path}  ({sz:,} bytes / {sz/1024:.1f} KB)")

    if not args.md_only:
        data = build_json(conn, args.registry)
        json_path = os.path.join(out_dir, f"{base}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        sz = os.path.getsize(json_path)
        print(f"Wrote: {json_path}  ({sz:,} bytes / {sz/1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
