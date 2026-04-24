"""Render per-word Session A prose as a self-contained `.md` for Verse Context input.

Deterministic render from the database. No analytics. No AI. The `.md` contains
only STEP-sourced data plus lexical parse, organised under the six seeded
`prose_section_type` handles (sa_s1_d1 … sa_s1_d6).

Usage:
    # One registry
    python scripts/build_session_a_prose.py --registry=35

    # Several registries
    python scripts/build_session_a_prose.py --registries=35,62,134,206,207

    # The five BANKED registries (shortcut)
    python scripts/build_session_a_prose.py --banked

Output:
    data/exports/session_a/wa-{NNN}-{word}-session_a-{YYYYMMDD}.md

Flags:
    --no-filter-reminder   Omit the "Method reminder" block quoting the VC filter.
    --no-prior-vc          Do not include existing verse_context state even where present.
    --output-dir PATH      Override default output folder.
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from textwrap import dedent

DB_PATH = Path("data/bible_research.db")
OUTPUT_DIR = Path("data/exports/session_a")
TERM_OUTPUT_DIR = Path("data/exports/session_a/terms")

BANKED_REGISTRIES = [35, 62, 134, 206, 207]


# ─── Method reminder (embedded in every .md per design decision B) ───────────
FILTER_REMINDER = dedent("""\
    > **Governing filter (VC Instruction §3).** For each verse, ask:
    > *Does this verse, through the use of this term, say something about the
    > inner being — the non-physical, internal states, capacities, and
    > expressions that constitute a person's invisible life: how a person
    > thinks, feels, chooses, relates, and orients themselves toward meaning,
    > others, and God?*
    > If yes → classify the contextual meaning. If no → set aside
    > (`is_relevant = 0`, with a `set_aside_reason` from the controlled
    > vocabulary: `no_inner_being` / `physical_only` / `spatial_only` /
    > `wrong_face` / `other`).
    >
    > **Grouping model (VC Instruction §6.2 Step 3 — characteristic-perspective).**
    > Groups are formed from the perspective of the inner-being characteristic
    > the verse cluster is primarily about — not from the perspective of what
    > the term does. For property terms especially, name the characteristic
    > being served (seat / channel / expression / mechanism / obstacle /
    > counterpart), not just the term's function. Reuse existing groups where
    > they fit; create a new group only when the inner-being characteristic is
    > materially different, or the same characteristic is engaged in a
    > materially different way.
    >
    > **Anchor designation (VC Instruction §4).** 1–2 anchor verses per group,
    > each making the contextual meaning evident without surrounding context.
    > Every term must have at least one active anchor (Rule R4).
""")


# ─── SQL helpers ──────────────────────────────────────────────────────────────
def _rows(conn: sqlite3.Connection, sql: str, params=()) -> list[sqlite3.Row]:
    return list(conn.execute(sql, params))


def _row(conn: sqlite3.Connection, sql: str, params=()) -> sqlite3.Row | None:
    return conn.execute(sql, params).fetchone()


def get_registry(conn, registry_no: int) -> sqlite3.Row:
    r = _row(conn, """
        SELECT * FROM word_registry WHERE no = ?
    """, (registry_no,))
    if not r:
        raise SystemExit(f"Registry {registry_no} not found")
    return r


def get_file_ids(conn, registry_id: int) -> list[int]:
    rows = _rows(conn, """
        SELECT id FROM wa_file_index WHERE word_registry_fk = ?
        ORDER BY id
    """, (registry_id,))
    return [r["id"] for r in rows]


def get_terms(conn, file_ids: list[int], term_owner_type: str) -> list[sqlite3.Row]:
    if not file_ids:
        return []
    placeholders = ",".join("?" * len(file_ids))
    return _rows(conn, f"""
        SELECT ti.*,
               mt.id AS mti_term_id,
               mt.status AS mti_status,
               mt.owning_registry_fk,
               mt.owning_word,
               mt.gloss AS mti_gloss
        FROM wa_term_inventory ti
        LEFT JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
        WHERE ti.file_id IN ({placeholders})
          AND ti.delete_flagged = 0
          AND ti.term_owner_type = ?
        ORDER BY ti.language, ti.strongs_number
    """, (*file_ids, term_owner_type))


def get_verses(conn, term_inv_id: int, include_deleted: bool = False) -> list[sqlite3.Row]:
    where = "term_inv_id = ?"
    if not include_deleted:
        where += " AND delete_flagged = 0"
    return _rows(conn, f"""
        SELECT id, reference, verse_text, target_word, span_strong_match,
               delete_flagged, testament, book_id, chapter, verse_num
        FROM wa_verse_records
        WHERE {where}
        ORDER BY book_id, chapter, verse_num
    """, (term_inv_id,))


def get_meaning(conn, term_inv_id: int) -> tuple[sqlite3.Row | None, list[sqlite3.Row], list[sqlite3.Row]]:
    parsed = _row(conn, """
        SELECT * FROM wa_meaning_parsed WHERE term_inv_id = ?
    """, (term_inv_id,))
    if not parsed:
        return None, [], []
    senses = _rows(conn, """
        SELECT level_code, sense_text, is_stem_label, stem_label, sort_order
        FROM wa_meaning_sense WHERE parsed_meaning_id = ?
        ORDER BY sort_order, level_code
    """, (parsed["id"],))
    stems = _rows(conn, """
        SELECT stem_name, stem_type, sense_count, top_sense_text
        FROM wa_meaning_stem WHERE parsed_meaning_id = ?
        ORDER BY stem_name
    """, (parsed["id"],))
    return parsed, senses, stems


def get_lsj(conn, term_inv_id: int) -> sqlite3.Row | None:
    return _row(conn, """
        SELECT lsj_gloss, lsj_domains, lsj_philosophical_note,
               lsj_etymology_note, lsj_cognate_forms
        FROM wa_lsj_parsed WHERE term_inv_id = ?
    """, (term_inv_id,))


def get_related_words(conn, term_inv_id: int) -> list[sqlite3.Row]:
    return _rows(conn, """
        SELECT strongs_number, transliteration, gloss, relationship_note
        FROM wa_term_related_words
        WHERE term_inv_id = ? AND delete_flagged = 0
        ORDER BY strongs_number
    """, (term_inv_id,))


def get_root_family(conn, term_inv_id: int) -> list[sqlite3.Row]:
    return _rows(conn, """
        SELECT root_code, root_language, root_gloss, note
        FROM wa_term_root_family
        WHERE term_inv_id = ? AND delete_flagged = 0
        ORDER BY root_code
    """, (term_inv_id,))


def get_quality_flags(conn, file_id: int, strongs: str) -> list[sqlite3.Row]:
    return _rows(conn, """
        SELECT qft.flag_code, qft.category, qf.description
        FROM wa_data_quality_flags qf
        JOIN wa_quality_flag_types qft ON qft.id = qf.flag_id
        WHERE qf.file_id = ? AND qf.term_id = ?
          AND qft.deprecated = 0
        ORDER BY qft.flag_code
    """, (file_id, strongs))


def get_prior_vc(conn, mti_term_id: int) -> tuple[list[sqlite3.Row], dict[int, sqlite3.Row]]:
    """Return (groups_for_term, verse_context_by_verse_record_id)."""
    groups = _rows(conn, """
        SELECT id, group_code, context_description, notes, delete_flagged
        FROM verse_context_group WHERE mti_term_id = ?
        ORDER BY id
    """, (mti_term_id,))
    vc_rows = _rows(conn, """
        SELECT verse_record_id, group_id, is_anchor, is_relevant, is_related,
               set_aside_reason, notes, delete_flagged
        FROM verse_context WHERE mti_term_id = ?
    """, (mti_term_id,))
    vc_map = {r["verse_record_id"]: r for r in vc_rows}
    return groups, vc_map


def get_cross_registry_links(conn, file_ids: list[int]) -> list[sqlite3.Row]:
    if not file_ids:
        return []
    placeholders = ",".join("?" * len(file_ids))
    return _rows(conn, f"""
        SELECT linked_word, linked_registry_id, connection_type_id,
               connecting_term, note
        FROM wa_cross_registry_links
        WHERE file_id IN ({placeholders})
        ORDER BY linked_registry_id
    """, tuple(file_ids))


def get_questions(conn, registry_no: int, flag_codes: set[str]) -> list[sqlite3.Row]:
    """Questions linked to this registry's quality-flag codes via flag→question map."""
    if not flag_codes:
        return []
    placeholders = ",".join("?" * len(flag_codes))
    return _rows(conn, f"""
        SELECT DISTINCT q.obs_id, q.question_code, q.section, q.question_text,
               q.pattern_type, q.scope, qft.flag_code
        FROM wa_obs_question_catalogue q
        JOIN wa_flag_type_question_link link ON link.question_id = q.obs_id
        JOIN wa_quality_flag_types qft ON qft.id = link.flag_type_id
        WHERE qft.flag_code IN ({placeholders})
          AND (q.deleted = 0 OR q.deleted IS NULL)
          AND link.active = 1
        ORDER BY q.question_code
    """, tuple(flag_codes))


# ─── Rendering ────────────────────────────────────────────────────────────────
def _bullet_if(items, none_msg="_None._") -> str:
    if not items:
        return f"{none_msg}\n"
    return "\n".join(items) + "\n"


def render_header(registry, generated_at: str, include_filter: bool,
                  n_active_prior_groups: int, n_dissolved_prior_groups: int,
                  n_terms_with_prior_records: int, n_total_owner_terms: int) -> str:
    parts = [f"# Session A — Registry {registry['no']:03d} {registry['word']}"]
    parts.append("")
    parts.append(f"**Generated:** {generated_at}  ")
    parts.append(f"**Source:** `data/bible_research.db` (deterministic render, no analytics)  ")
    parts.append("**Governing instruction:** wa-versecontext-instruction [current]  ")
    parts.append("**Produced by:** `scripts/build_session_a_prose.py`")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## About this document")
    parts.append("")
    parts.append(dedent(f"""\
        This document is the Session A input for **Verse Context classification** of
        registry {registry['no']:03d} {registry['word']}. It contains all STEP-sourced data for this
        registry's OWNER terms and is self-sufficient for the VC classification task.

        Read the VC instruction in full before beginning (see `wa-versecontext-instruction [current]`).
        This document is the **data**; the instruction is the **method**. The `.md`
        carries no analytical content from downstream stages (no Session B findings,
        no dimensional placements, no Session C prose, no Session D synthesis) —
        that content is a product of later stages and must not bleed back into VC.
    """))
    # Prior-state posture (B.14 — added 2026-04-24)
    parts.append("### Prior-state posture")
    parts.append("")
    if n_active_prior_groups == 0 and n_terms_with_prior_records == 0:
        parts.append(dedent(f"""\
            This registry has **no** active prior `verse_context` groups across its
            OWNER terms ({n_dissolved_prior_groups} dissolved). **Approach this as a
            FRESH classification.** No re-evaluation obligations apply; no orphan-group
            disposition required at term close.
        """))
    else:
        parts.append(dedent(f"""\
            This registry has **{n_active_prior_groups} active** prior
            `verse_context` groups across its OWNER terms
            ({n_dissolved_prior_groups} dissolved); {n_terms_with_prior_records}
            of {n_total_owner_terms} OWNER terms carry prior classifications.
            **Approach this as a RE-EVALUATION** — every prior classification will be
            reviewed under the current filter and grouping model; every pre-existing
            active group must be retained (with verses), dissolved, or
            documented-retained at term close. No silent pass-through. See VC
            Instruction §6.1 (prior-state posture declaration) and §6.2 Step 6
            (re-evaluation self-check + orphan-group check).
        """))
    if include_filter:
        parts.append("### Method reminder")
        parts.append("")
        parts.append(FILTER_REMINDER)
    parts.append("---")
    parts.append("")
    return "\n".join(parts)


def render_word_summary(registry, owner_count, xref_count, owner_verse_count, owner_flag_summary) -> str:
    p = [f"## {1}. Word Summary"]
    p.append("")
    p.append("| Field | Value |")
    p.append("|---|---|")
    p.append(f"| Registry | {registry['no']:03d} |")
    p.append(f"| Word | {registry['word']} |")
    p.append(f"| Cluster | {registry['cluster_assignment'] or '—'} |")
    p.append(f"| Phase 1 status | {registry['phase1_status'] or 'NULL'} |")
    p.append(f"| Phase 1 term count | {registry['phase1_term_count'] if 'phase1_term_count' in registry.keys() else '—'} |")
    p.append(f"| Verse Context status | {registry['verse_context_status'] or 'NULL'} |")
    p.append(f"| Session B status | {registry['session_b_status'] or 'NULL'} |")
    p.append(f"| OWNER terms | {owner_count} |")
    p.append(f"| XREF terms | {xref_count} |")
    p.append(f"| Active OWNER verses (total) | {owner_verse_count} |")
    p.append("")

    synopsis = registry["word_synopsis"] if "word_synopsis" in registry.keys() else None
    if synopsis:
        p.append("### Word synopsis (researcher-authored)")
        p.append("")
        p.append(f"> {synopsis}")
        p.append("")
    inference = registry["inference_note"] if "inference_note" in registry.keys() else None
    if inference:
        p.append("### Inference note (researcher-authored)")
        p.append("")
        p.append(f"> {inference}")
        p.append("")

    if owner_flag_summary:
        p.append("### Data-quality flag summary (informational, post-M29)")
        p.append("")
        p.append("| Flag | Terms affected |")
        p.append("|---|---:|")
        for flag_code, count in sorted(owner_flag_summary.items()):
            p.append(f"| `{flag_code}` | {count} |")
        p.append("")
    p.append("---")
    p.append("")
    return "\n".join(p)


def render_meaning_section(owner_terms_data: list[dict]) -> str:
    p = ["## 2. Meaning"]
    p.append("")
    p.append(dedent("""\
        Per-OWNER-term lexical context, STEP-sourced and mechanically parsed. Read
        this section before filtering verses — understand what the term means in
        its lexical range before assessing each verse's inner-being engagement.
    """))
    p.append("")
    for td in owner_terms_data:
        t = td["term"]
        p.append(f"### {t['strongs_number']} · *{t['transliteration'] or '—'}* · {t['step_search_gloss'] or t['mti_gloss'] or '—'}")
        p.append("")
        p.append(f"- **Language:** {t['language']}")
        p.append(f"- **mti_term_id:** {t['mti_term_id']}")
        p.append(f"- **STEP gloss:** {t['step_search_gloss'] or '—'}")
        if t["word_analysis_gloss"]:
            p.append(f"- **Word-analysis gloss:** {t['word_analysis_gloss']}")
        if t["short_def_mounce"]:
            p.append(f"- **Mounce short def:** {t['short_def_mounce']}")
        p.append(f"- **Occurrence count:** {t['occurrence_count'] or 0}"
                 + (f" ({t['occurrence_count_qualifier']})" if t["occurrence_count_qualifier"] else ""))
        if t["also_spelled"]:
            p.append(f"- **Also spelled:** {t['also_spelled']}")
        p.append("")

        if t["meaning"]:
            p.append("**Meaning (STEP):**")
            p.append("")
            p.append("> " + t["meaning"].strip().replace("\n", "\n> "))
            p.append("")

        if t["meaning_numbered"]:
            p.append("**Meaning (numbered form):**")
            p.append("")
            p.append("```")
            p.append(t["meaning_numbered"].strip())
            p.append("```")
            p.append("")

        parsed = td["meaning_parsed"]
        if parsed and td["senses"]:
            p.append("**Parsed senses:**")
            p.append("")
            for s in td["senses"]:
                marker = f"{s['level_code']}"
                label = f" *(stem label: {s['stem_label']})*" if s["is_stem_label"] else ""
                p.append(f"- `{marker}`{label} {s['sense_text']}")
            p.append("")

        if td["stems"]:
            p.append("**Stems (Hebrew binyanim / Greek forms):**")
            p.append("")
            for st in td["stems"]:
                p.append(f"- `{st['stem_name']}` ({st['stem_type'] or '—'}) — {st['sense_count']} sense(s); top: {st['top_sense_text'] or '—'}")
            p.append("")

        lsj = td["lsj"]
        if lsj:
            p.append("**LSJ (Greek lexicon):**")
            p.append("")
            if lsj["lsj_gloss"]:
                p.append(f"- Gloss: {lsj['lsj_gloss']}")
            if lsj["lsj_domains"]:
                p.append(f"- Domains: {lsj['lsj_domains']}")
            if lsj["lsj_etymology_note"]:
                p.append(f"- Etymology: {lsj['lsj_etymology_note']}")
            if lsj["lsj_cognate_forms"]:
                p.append(f"- Cognate forms: {lsj['lsj_cognate_forms']}")
            if lsj["lsj_philosophical_note"]:
                p.append(f"- Philosophical note: {lsj['lsj_philosophical_note']}")
            p.append("")

        if td["related_words"]:
            p.append("**Related words:**")
            p.append("")
            for rw in td["related_words"]:
                p.append(f"- `{rw['strongs_number']}` *{rw['transliteration'] or '—'}* — {rw['gloss'] or '—'}"
                         + (f" ({rw['relationship_note']})" if rw["relationship_note"] else ""))
            p.append("")

        if td["root_family"]:
            p.append("**Root family:**")
            p.append("")
            for rf in td["root_family"]:
                p.append(f"- `{rf['root_code']}` ({rf['root_language']}) — {rf['root_gloss'] or '—'}"
                         + (f" — {rf['note']}" if rf["note"] else ""))
            p.append("")

        if td["quality_flags"]:
            p.append("**Data-quality flags (informational):**")
            p.append("")
            for qf in td["quality_flags"]:
                p.append(f"- `{qf['flag_code']}` — {qf['description']}")
            p.append("")

        p.append("")
    p.append("---")
    p.append("")
    return "\n".join(p)


def render_verses_section(owner_terms_data: list[dict], include_prior_vc: bool) -> str:
    p = ["## 3. Verses"]
    p.append("")
    p.append(dedent("""\
        The complete verse corpus for each OWNER term. This is the object of
        classification. Every active verse (`delete_flagged = 0`) must be assessed
        against the governing filter. Any existing `verse_context` state is shown
        per verse as **Prior classification** — review, and revise only where
        clearly warranted (VC Instruction §6.2 Step 2).
    """))
    p.append("")
    for td in owner_terms_data:
        t = td["term"]
        verses = td["verses"]
        prior_groups = td["prior_groups"]
        prior_vc = td["prior_vc"]
        active_verses = [v for v in verses if not v["delete_flagged"]]
        historical_verses = [v for v in verses if v["delete_flagged"]]

        p.append(f"### {t['strongs_number']} · *{t['transliteration'] or '—'}* — {len(active_verses)} active verse(s)")
        p.append("")
        p.append(f"- **mti_term_id:** {t['mti_term_id']}")
        p.append(f"- **Language:** {t['language']}")
        p.append(f"- **Gloss:** {t['step_search_gloss'] or t['mti_gloss'] or '—'}")
        p.append(f"- **Total verses:** {len(verses)} ({len(active_verses)} active, {len(historical_verses)} delete_flagged)")
        if include_prior_vc and prior_groups:
            active_groups = [g for g in prior_groups if not g["delete_flagged"]]
            dissolved = [g for g in prior_groups if g["delete_flagged"]]
            p.append(f"- **Prior verse_context groups:** {len(active_groups)} active"
                     + (f", {len(dissolved)} dissolved" if dissolved else ""))
        p.append("")

        if include_prior_vc and prior_groups:
            p.append("**Existing verse_context groups for this term:**")
            p.append("")
            p.append("| group_code | description | state |")
            p.append("|---|---|---|")
            for g in prior_groups:
                state = "dissolved" if g["delete_flagged"] else "active"
                desc = (g["context_description"] or "").replace("|", "\\|")
                p.append(f"| `{g['group_code']}` | {desc} | {state} |")
            p.append("")

        p.append("**Verses:**")
        p.append("")
        for v in active_verses:
            span_marker = "" if v["span_strong_match"] else " *(no span match)*"
            p.append(f"**vid={v['id']}** — `{v['reference']}`{span_marker}")
            if v["target_word"]:
                p.append(f"*target word in verse:* `{v['target_word']}`")
            p.append("")
            p.append(f"> {v['verse_text']}")
            p.append("")
            if include_prior_vc and v["id"] in prior_vc:
                vc = prior_vc[v["id"]]
                status_parts = []
                if vc["is_relevant"]:
                    status_parts.append("**relevant**")
                    if vc["is_anchor"]:
                        status_parts.append("**anchor**")
                    elif vc["is_related"]:
                        status_parts.append("related")
                else:
                    status_parts.append(f"*set aside — reason: `{vc['set_aside_reason'] or '(not set)'}`*")
                if vc["group_id"]:
                    # find the group_code for this group_id
                    gc = next((g["group_code"] for g in prior_groups if g["id"] == vc["group_id"]), f"gid={vc['group_id']}")
                    status_parts.append(f"group=`{gc}`")
                state_marker = " [deleted]" if vc["delete_flagged"] else ""
                p.append(f"_Prior classification: {' · '.join(status_parts)}{state_marker}_")
                if vc["notes"]:
                    p.append(f"_Notes: {vc['notes']}_")
                p.append("")
            p.append("")

        if historical_verses:
            p.append(f"<details><summary>Historical verses ({len(historical_verses)} `delete_flagged = 1`)</summary>")
            p.append("")
            for v in historical_verses:
                p.append(f"- vid={v['id']} `{v['reference']}` — {v['verse_text'][:120]}…")
            p.append("")
            p.append("</details>")
            p.append("")
        p.append("")
    p.append("---")
    p.append("")
    return "\n".join(p)


def render_terms_section(owner_terms: list, xref_terms: list) -> str:
    p = ["## 4. Terms"]
    p.append("")
    p.append(dedent("""\
        The full term landscape of this registry. OWNER terms are classified in
        Verse Context; XREF terms are not — their classification is inherited
        programme-wide from the OWNER's VC records (VC Instruction §0.2).
    """))
    p.append("")

    p.append("### OWNER terms")
    p.append("")
    if owner_terms:
        p.append("| mti_id | Strong's | Translit. | Gloss | Language | mti_status | Occurrence |")
        p.append("|---:|---|---|---|---|---|---:|")
        for t in owner_terms:
            p.append(f"| {t['mti_term_id']} | `{t['strongs_number']}` | {t['transliteration'] or '—'} | "
                     f"{t['step_search_gloss'] or t['mti_gloss'] or '—'} | {t['language']} | "
                     f"{t['mti_status'] or '—'} | {t['occurrence_count'] or 0} |")
    else:
        p.append("_None._")
    p.append("")

    p.append("### XREF terms")
    p.append("")
    if xref_terms:
        p.append(dedent("""\
            _These terms appear in this registry's term inventory but their primary
            analytical home (OWNER) is in a different registry. Their verse records
            are `delete_flagged = 1` here. Do not classify them in this session —
            VC records for them (if any) are held at the OWNER._
        """))
        p.append("")
        p.append("| Strong's | Translit. | Gloss | Language | OWNER registry | OWNER word |")
        p.append("|---|---|---|---|---:|---|")
        for t in xref_terms:
            owner_reg = t["owning_registry_fk"] or "—"
            owner_word = t["owning_word"] or "—"
            p.append(f"| `{t['strongs_number']}` | {t['transliteration'] or '—'} | "
                     f"{t['step_search_gloss'] or t['mti_gloss'] or '—'} | {t['language']} | "
                     f"{owner_reg} | {owner_word} |")
    else:
        p.append("_None._")
    p.append("")
    p.append("---")
    p.append("")
    return "\n".join(p)


def render_pointers_section(cross_links: list, xref_terms: list) -> str:
    p = ["## 5. Pointers"]
    p.append("")
    p.append(dedent("""\
        Structural pointers — what other parts of the programme this registry
        connects to. Informational only; not required for classification.
        No Session D synthesis content here.
    """))
    p.append("")

    p.append("### Cross-registry links")
    p.append("")
    if cross_links:
        p.append("| Linked registry | Linked word | Connection | Connecting term | Note |")
        p.append("|---:|---|---|---|---|")
        for cl in cross_links:
            p.append(f"| {cl['linked_registry_id']} | {cl['linked_word'] or '—'} | "
                     f"{cl['connection_type_id'] or '—'} | {cl['connecting_term'] or '—'} | "
                     f"{(cl['note'] or '').replace('|', '\\\\|')} |")
    else:
        p.append("_None recorded._")
    p.append("")

    p.append("### Terms borrowed as XREF from other registries")
    p.append("")
    if xref_terms:
        p.append("Each XREF term's OWNER registry is its primary analytical home.")
        p.append("")
        for t in xref_terms:
            p.append(f"- `{t['strongs_number']}` *{t['transliteration'] or '—'}* — "
                     f"OWNER: registry {t['owning_registry_fk'] or '—'} "
                     f"({t['owning_word'] or '—'})")
    else:
        p.append("_None._")
    p.append("")
    p.append("---")
    p.append("")
    return "\n".join(p)


def render_questions_section(questions: list) -> str:
    p = ["## 6. Questions"]
    p.append("")
    p.append(dedent("""\
        Open questions from the programme's observation catalogue linked to the
        data-quality flags present on this registry. These are for awareness —
        classification work may surface answers; many will be addressed in
        Session B. Do not try to answer them here.
    """))
    p.append("")
    if questions:
        p.append("| obs_id | code | triggering flag | question |")
        p.append("|---:|---|---|---|")
        for q in questions:
            qtext = (q["question_text"] or "").replace("\n", " ").replace("|", "\\|")
            p.append(f"| {q['obs_id']} | `{q['question_code']}` | `{q['flag_code']}` | {qtext} |")
    else:
        p.append("_No open catalogue questions linked to this registry's flags._")
    p.append("")
    p.append("---")
    p.append("")
    return "\n".join(p)


def render_footer(registry) -> str:
    return dedent(f"""\
        ## Footer — what happens next

        When a Claude AI Verse Context session consumes this document, it produces a
        `VERSECONTEXT` patch populating `verse_context_group` and `verse_context`
        for each OWNER term. The patch is applied via
        `scripts/apply_session_patch.py`; Claude Code then advances this registry's
        `verse_context_status` to Complete (subject to XREF coverage rules per
        VC Instruction §0.2) and a fresh Session A `.md` can be regenerated.

        *End of Session A prose for registry {registry['no']:03d} {registry['word']}.*
    """)


# ─── Per-term build (VC-5 — alignment analysis v4 §8, §7.9 hybrid) ───────────

def _fetch_term_by_mti_id(conn, mti_term_id: int) -> sqlite3.Row:
    """Fetch a single OWNER term by mti_term_id, joining to its inventory row
    so the term-bundle shape matches what get_terms() returns."""
    r = _row(conn, """
        SELECT ti.*, mt.id AS mti_term_id, mt.status AS mti_status,
               mt.owning_registry_fk, mt.owning_word, mt.gloss AS mti_gloss,
               mt.vc_status, mt.vc_instruction_version,
               mt.vc_status_updated_at, mt.vc_status_note,
               mt.md_version
        FROM mti_terms mt
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
        WHERE mt.id = ?
          AND ti.term_owner_type = 'OWNER'
          AND ti.delete_flagged = 0
          AND ti.file_id IN (
              SELECT id FROM wa_file_index WHERE word_registry_fk = mt.owning_registry_fk
          )
        LIMIT 1
    """, (mti_term_id,))
    if not r:
        raise SystemExit(f"OWNER term with mti_term_id={mti_term_id} not found")
    return r


def render_term_header(registry, term, generated_at: str, include_filter: bool,
                       has_prior_records: bool, n_active_groups: int,
                       n_dissolved_groups: int) -> str:
    strongs = term["strongs_number"]
    trans = term["transliteration"] or "—"
    gloss = term["step_search_gloss"] or term["mti_gloss"] or "—"
    # A-03: md_version must be stamped into the header — the patch's
    # input_version gate compares this value to mti_terms.md_version at apply.
    md_version = term["md_version"] if "md_version" in term.keys() else 1
    parts = [f"# Session A — Term `{strongs}` *{trans}* — {gloss}"]
    parts.append("")
    parts.append(f"**Registry:** {registry['no']:03d} {registry['word']}  ")
    parts.append(f"**mti_term_id:** {term['mti_term_id']}  ")
    parts.append(f"**Language:** {term['language']}  ")
    parts.append(f"**md_version:** `v{md_version}`  ⚠ the patch's `_patch_meta.input_versions[{term['mti_term_id']}]` must equal `{md_version}` at submission time or the applicator will reject it as stale (A-03 version gate).  ")
    parts.append(f"**Generated:** {generated_at}  ")
    parts.append(f"**Current vc_status:** `{term['vc_status']}`"
                 + (f" — {term['vc_status_note']}" if term['vc_status_note'] else "") + "  ")
    parts.append(f"**Source:** `data/bible_research.db` (deterministic render, no analytics)  ")
    parts.append("**Governing instruction:** wa-versecontext-instruction [current]  ")
    parts.append("**Produced by:** `scripts/build_session_a_prose.py --term`")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## About this document")
    parts.append("")
    parts.append(dedent(f"""\
        This document is the Session A input for **Verse Context classification** of
        a single OWNER term — `{strongs}` *{trans}* ({gloss}) from registry
        {registry['no']:03d} {registry['word']}. It contains the STEP-sourced data for this one term only.
        Per alignment analysis v4 §7 and §8, the term is the atomic unit of VC
        classification; this document presents the term in the scope the method
        actually operates on.

        Read the VC instruction in full before beginning. This document is the
        **data**; the instruction is the **method**. The `.md` carries no analytical
        content from downstream stages (no Session B findings, no dimensional
        placements, no Session C prose, no Session D synthesis).
    """))
    parts.append("### Prior-state posture (this term)")
    parts.append("")
    if not has_prior_records and n_active_groups == 0:
        parts.append(dedent("""\
            This term has **no** active prior `verse_context` records. Approach this
            as a **FRESH** classification for this term. No orphan-group disposition
            required at term close.
        """))
    else:
        parts.append(dedent(f"""\
            This term has **{n_active_groups} active** prior `verse_context_group`
            rows ({n_dissolved_groups} dissolved). Approach this as a
            **RE-EVALUATION** — every prior classification will be reviewed under
            the current filter and grouping model; every pre-existing active group
            must be retained (with verses), dissolved, or documented-retained at
            term close. No silent pass-through. See VC Instruction §6.1
            (prior-state posture declaration) and §6.2 Step 6 (re-evaluation
            self-check + orphan-group check).
        """))
    if include_filter:
        parts.append("### Method reminder")
        parts.append("")
        parts.append(FILTER_REMINDER)
    parts.append("---")
    parts.append("")
    return "\n".join(parts)


def render_term_other_terms(registry_owner_terms: list, registry_xref_terms: list,
                            current_term_id: int) -> str:
    """Short pointer table: what other terms exist in this registry. For wrong-face
    awareness without loading their data."""
    p = ["## 4. Other terms in this registry"]
    p.append("")
    p.append(dedent("""\
        A pointer-only list of the other terms in this registry, so that
        wrong-face set-asides can reference them accurately (VC Instruction §3.6).
        **Do not classify these terms here** — each is handled in its own Session A
        per-term document.
    """))
    p.append("")
    others_owner = [t for t in registry_owner_terms if t["mti_term_id"] != current_term_id]
    if others_owner:
        p.append("### Other OWNER terms")
        p.append("")
        p.append("| Strong's | Translit. | Gloss | Language |")
        p.append("|---|---|---|---|")
        for t in others_owner:
            p.append(f"| `{t['strongs_number']}` | {t['transliteration'] or '—'} | "
                     f"{t['step_search_gloss'] or t['mti_gloss'] or '—'} | {t['language']} |")
        p.append("")
    if registry_xref_terms:
        p.append("### XREF terms (OWNER elsewhere)")
        p.append("")
        p.append("| Strong's | Translit. | Gloss | OWNER registry | OWNER word |")
        p.append("|---|---|---|---:|---|")
        for t in registry_xref_terms:
            p.append(f"| `{t['strongs_number']}` | {t['transliteration'] or '—'} | "
                     f"{t['step_search_gloss'] or t['mti_gloss'] or '—'} | "
                     f"{t['owning_registry_fk'] or '—'} | {t['owning_word'] or '—'} |")
        p.append("")
    if not others_owner and not registry_xref_terms:
        p.append("_This registry has no other terms besides the one classified here._")
        p.append("")
    p.append("---")
    p.append("")
    return "\n".join(p)


def build_one_term(conn, mti_term_id: int, include_filter: bool,
                   include_prior_vc: bool) -> tuple[str, str]:
    """Render a per-term Session A .md for a single OWNER term."""
    term = _fetch_term_by_mti_id(conn, mti_term_id)
    registry = _row(conn, "SELECT * FROM word_registry WHERE id = ?",
                    (term["owning_registry_fk"],))
    if not registry:
        raise SystemExit(f"Owning registry not found for mti_term_id={mti_term_id}")

    # Term bundle (same shape as build_one's owner_terms_data entries)
    verses = get_verses(conn, term["id"], include_deleted=True)
    parsed, senses, stems = get_meaning(conn, term["id"])
    lsj = get_lsj(conn, term["id"]) if term["language"].lower().startswith("greek") else None
    related = get_related_words(conn, term["id"])
    root = get_root_family(conn, term["id"])
    qflags = get_quality_flags(conn, term["file_id"], term["strongs_number"])

    prior_groups, prior_vc = ([], {})
    if include_prior_vc:
        prior_groups, prior_vc = get_prior_vc(conn, term["mti_term_id"])

    term_data = {
        "term": term,
        "verses": verses,
        "meaning_parsed": parsed,
        "senses": senses,
        "stems": stems,
        "lsj": lsj,
        "related_words": related,
        "root_family": root,
        "quality_flags": qflags,
        "prior_groups": prior_groups,
        "prior_vc": prior_vc,
    }

    # Prior-state counts for this single term
    n_active_groups = sum(1 for g in prior_groups if not g["delete_flagged"])
    n_dissolved_groups = sum(1 for g in prior_groups if g["delete_flagged"])
    has_prior_records = bool(prior_vc) or n_active_groups > 0

    # Registry-wide term listing for the "Other terms" pointer section
    file_ids = get_file_ids(conn, registry["id"])
    registry_owner_terms = get_terms(conn, file_ids, "OWNER")
    registry_xref_terms = get_terms(conn, file_ids, "XREF")
    questions = get_questions(conn, registry["no"],
                              {qf["flag_code"] for qf in qflags})

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    parts = [
        render_term_header(registry, term, generated_at, include_filter,
                           has_prior_records, n_active_groups, n_dissolved_groups),
        render_meaning_section([term_data]),
        render_verses_section([term_data], include_prior_vc),
        render_term_other_terms(registry_owner_terms, registry_xref_terms,
                                term["mti_term_id"]),
        render_pointers_section(
            get_cross_registry_links(conn, file_ids),
            [t for t in registry_xref_terms
             if t["strongs_number"] == term["strongs_number"]],
        ),
        render_questions_section(questions),
        dedent(f"""\
            ## Footer — what happens next

            A Claude AI Verse Context session produces a `VERSECONTEXT` patch
            covering this term (and any others classified in the same session).
            The patch must declare `_patch_meta.terms_covered` including
            `mti_term_id = {term['mti_term_id']}`. On apply, Claude Code flips
            this term's `mti_terms.vc_status` to `complete` and re-derives the
            owning registry's `verse_context_status` from the aggregate of all
            its OWNER + XREF-via-OWNER term statuses (VC-2 in the applicator;
            alignment analysis v4 §8.2).

            *End of Session A prose for term {term['strongs_number']}
            ({registry['no']:03d} {registry['word']}).*
        """)
    ]
    content = "\n".join(parts)

    word_slug = registry["word"].replace(" ", "-").replace("(", "").replace(")", "")
    filename = (f"wa-{registry['no']:03d}-{word_slug}-{term['strongs_number']}"
                f"-session_a-{datetime.now().strftime('%Y%m%d')}.md")
    return filename, content


# ─── Per-registry build ───────────────────────────────────────────────────────
def build_one(conn, registry_no: int, include_filter: bool, include_prior_vc: bool) -> tuple[str, str]:
    registry = get_registry(conn, registry_no)
    file_ids = get_file_ids(conn, registry["id"])
    owner_terms = get_terms(conn, file_ids, "OWNER")
    xref_terms = get_terms(conn, file_ids, "XREF")

    # Build per-term data bundles for OWNER
    owner_terms_data = []
    all_flag_codes: set[str] = set()
    flag_summary: dict[str, int] = {}
    total_owner_verses = 0

    for t in owner_terms:
        verses = get_verses(conn, t["id"], include_deleted=True)
        active_verses = [v for v in verses if not v["delete_flagged"]]
        total_owner_verses += len(active_verses)
        parsed, senses, stems = get_meaning(conn, t["id"])
        lsj = get_lsj(conn, t["id"]) if t["language"].lower().startswith("greek") else None
        related = get_related_words(conn, t["id"])
        root = get_root_family(conn, t["id"])
        qflags = get_quality_flags(conn, t["file_id"], t["strongs_number"])
        for qf in qflags:
            all_flag_codes.add(qf["flag_code"])
            flag_summary[qf["flag_code"]] = flag_summary.get(qf["flag_code"], 0) + 1
        prior_groups, prior_vc = ([], {})
        if include_prior_vc and t["mti_term_id"]:
            prior_groups, prior_vc = get_prior_vc(conn, t["mti_term_id"])

        owner_terms_data.append({
            "term": t,
            "verses": verses,
            "meaning_parsed": parsed,
            "senses": senses,
            "stems": stems,
            "lsj": lsj,
            "related_words": related,
            "root_family": root,
            "quality_flags": qflags,
            "prior_groups": prior_groups,
            "prior_vc": prior_vc,
        })

    cross_links = get_cross_registry_links(conn, file_ids)
    questions = get_questions(conn, registry_no, all_flag_codes)

    # Prior-state posture counts for header (B.14)
    n_active_prior_groups = 0
    n_dissolved_prior_groups = 0
    n_terms_with_prior_records = 0
    for td in owner_terms_data:
        has_prior = False
        for g in td["prior_groups"]:
            if g["delete_flagged"]:
                n_dissolved_prior_groups += 1
            else:
                n_active_prior_groups += 1
                has_prior = True
        if td["prior_vc"]:
            has_prior = True
        if has_prior:
            n_terms_with_prior_records += 1

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    parts = [
        render_header(registry, generated_at, include_filter,
                      n_active_prior_groups, n_dissolved_prior_groups,
                      n_terms_with_prior_records, len(owner_terms)),
        render_word_summary(registry, len(owner_terms), len(xref_terms),
                            total_owner_verses, flag_summary),
        render_meaning_section(owner_terms_data),
        render_verses_section(owner_terms_data, include_prior_vc),
        render_terms_section(owner_terms, xref_terms),
        render_pointers_section(cross_links, xref_terms),
        render_questions_section(questions),
        render_footer(registry),
    ]
    content = "\n".join(parts)

    word_slug = registry["word"].replace(" ", "-").replace("(", "").replace(")", "")
    filename = f"wa-{registry['no']:03d}-{word_slug}-session_a-{datetime.now().strftime('%Y%m%d')}.md"
    return filename, content


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--registry", type=int, help="Single registry number (renders per-registry .md)")
    g.add_argument("--registries", type=str, help="Comma-separated registry numbers")
    g.add_argument("--banked", action="store_true", help="Render the 5 BANKED registries")
    g.add_argument("--term", type=int, metavar="MTI_TERM_ID",
                   help="Render a single OWNER term's .md (VC-5 — per-term mode)")
    g.add_argument("--terms", type=str, metavar="IDS",
                   help="Comma-separated mti_term_ids (per-term .md each)")
    g.add_argument("--registry-per-term", type=int, metavar="N",
                   help="Render one per-term .md for every OWNER term of registry N")
    ap.add_argument("--no-filter-reminder", action="store_true")
    ap.add_argument("--no-prior-vc", action="store_true")
    ap.add_argument("--output-dir", type=str, default=None,
                    help="Override output folder (default: data/exports/session_a for "
                         "registry mode, data/exports/session_a/terms for per-term mode)")
    args = ap.parse_args()

    # Determine mode and output set
    term_mode = bool(args.term or args.terms or args.registry_per_term)

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    if term_mode:
        out_dir = Path(args.output_dir) if args.output_dir else TERM_OUTPUT_DIR
        out_dir.mkdir(parents=True, exist_ok=True)
        # Resolve term id list
        if args.term:
            term_ids = [args.term]
        elif args.terms:
            term_ids = [int(x.strip()) for x in args.terms.split(",") if x.strip()]
        else:
            # --registry-per-term: fan out to every OWNER term of the registry
            reg = _row(conn, "SELECT id FROM word_registry WHERE no = ?",
                       (args.registry_per_term,))
            if not reg:
                raise SystemExit(f"Registry {args.registry_per_term} not found")
            term_ids = [
                r[0] for r in conn.execute(
                    """SELECT mt.id FROM mti_terms mt
                        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                       WHERE mt.owning_registry_fk = ?
                         AND mt.delete_flagged = 0
                         AND mt.status IN ('extracted', 'extracted_thin')
                         AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
                         AND ti.file_id IN (
                            SELECT id FROM wa_file_index WHERE word_registry_fk = ?
                         )
                       GROUP BY mt.id
                       ORDER BY mt.strongs_number""",
                    (reg["id"], reg["id"]),
                ).fetchall()
            ]
            print(f"  [per-term] registry {args.registry_per_term}: {len(term_ids)} OWNER terms")
        for term_id in term_ids:
            try:
                filename, content = build_one_term(
                    conn, term_id,
                    include_filter=not args.no_filter_reminder,
                    include_prior_vc=not args.no_prior_vc,
                )
                out_path = out_dir / filename
                out_path.write_text(content, encoding="utf-8")
                size_kb = out_path.stat().st_size / 1024
                print(f"  wrote {filename}  ({size_kb:.1f} KB)")
            except SystemExit as e:
                print(f"  SKIP term {term_id}: {e}", file=sys.stderr)
                continue
    else:
        # Per-registry mode (original)
        out_dir = Path(args.output_dir) if args.output_dir else OUTPUT_DIR
        out_dir.mkdir(parents=True, exist_ok=True)
        if args.banked:
            regs = list(BANKED_REGISTRIES)
        elif args.registries:
            regs = [int(x.strip()) for x in args.registries.split(",") if x.strip()]
        else:
            regs = [args.registry]
        for r_no in regs:
            try:
                filename, content = build_one(
                    conn, r_no,
                    include_filter=not args.no_filter_reminder,
                    include_prior_vc=not args.no_prior_vc,
                )
                out_path = out_dir / filename
                out_path.write_text(content, encoding="utf-8")
                size_kb = out_path.stat().st_size / 1024
                print(f"  wrote {filename}  ({size_kb:.1f} KB)")
            except SystemExit as e:
                print(f"  SKIP registry {r_no}: {e}", file=sys.stderr)
                continue


if __name__ == "__main__":
    main()
