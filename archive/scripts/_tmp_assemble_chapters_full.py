"""_tmp_assemble_chapters_full.py

Full 6-chapter assembler — builds Session B Stage 2c prose for any registry
directly from DB content, no AI generation. Reads from:
  - word_registry (header, description)
  - wa_term_inventory + mti_terms + wa_meaning_parsed + wa_meaning_sense
  - verse_context_group + verse_context (anchors + analysis_note)
  - wa_verse_records (verse text)
  - wa_finding_catalogue_links (Q&A bodies, joined to wa_obs_question_catalogue)
  - wa_session_b_findings (synthesis findings with session_c_chapter routing)
  - wa_session_research_flags (SD pointers, RESEARCHER_DECISION items)

Produces 6 chapter files + 1 combined "extract" file under
research/investigations/chapter_assembly_prototype/.

Usage:
  python scripts/_tmp_assemble_chapters_full.py --registry 67
"""
from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
PER_WORD_BASE = os.path.join("Sessions", "Session_B", "words")
LEGACY_OUT_DIR = os.path.join("research", "investigations", "chapter_assembly_prototype")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


# --- Shared fetch helpers ---

def fetch_qa_for_components(conn, registry_no, components):
    """Return Q&A entries (full answer body) for the given component codes,
    filtered to OBSERVATION-type findings (not synthesis-source breadcrumbs).
    Multi-row dedupe: pick longest answer per (component, prompt_seq)."""
    if not components:
        return []
    placeholders = ",".join("?" for _ in components)
    rows = conn.execute(
        f"""
        SELECT q.tier, q.component_code, q.component_title, q.prompt_seq,
               q.question_text, l.coverage,
               l.session_b_note AS answer,
               f.finding_id, l.validated_by
        FROM wa_finding_catalogue_links l
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        WHERE f.registry_id = ?
        AND l.validated_by IN ('claude_ai_v1_8','claude_ai_2nd_tier_v1')
        AND f.finding_type IN ('OBSERVATION','THEOLOGICAL_NOTE','VERSE_ANNOTATION',
                               'SOMATIC_EVIDENCE','VERSE_PATTERN','MEANING_OBSERVATION',
                               'ETYMOLOGY','ROOT_FINDING','SPIRIT_SOUL_BODY','CROSS_REGISTRY')
        AND q.component_code IN ({placeholders})
        AND f.delete_flag = 0
        AND (l.delete_flagged = 0 OR l.delete_flagged IS NULL)
        ORDER BY q.component_code, q.prompt_seq, f.finding_id
        """,
        [registry_no] + list(components),
    ).fetchall()
    # Dedupe by (component_code, prompt_seq). Prefer claude_ai_v1_8 over
    # claude_ai_2nd_tier_v1 (v1.8 captures supersede v1.7-style); within the
    # same validated_by, pick the longest answer body.
    PRIORITY = {"claude_ai_v1_8": 1, "claude_ai_2nd_tier_v1": 2}
    by_prompt: dict[tuple[str, int], dict] = {}
    for r in rows:
        key = (r["component_code"], r["prompt_seq"])
        existing = by_prompt.get(key)
        rd = dict(r)
        if existing is None:
            by_prompt[key] = rd
            continue
        ex_p = PRIORITY.get(existing["validated_by"], 9)
        new_p = PRIORITY.get(rd["validated_by"], 9)
        if new_p < ex_p:
            by_prompt[key] = rd
        elif new_p == ex_p and len(rd["answer"] or "") > len(existing["answer"] or ""):
            by_prompt[key] = rd
    return sorted(by_prompt.values(), key=lambda x: (x["component_code"], x["prompt_seq"]))


def derive_chapter_from_tiers(tiers_str: str | None, finding_type: str) -> str:
    """Per v1.8 §10 chapter source mapping, route a synthesis finding to a
    Session C chapter based on its tiers_engaged when session_c_chapter is
    absent/N/A.

    Mapping (from §10):
      Ch1 (Meaning):           T1 intra; T1×T7 inter
      Ch2 (How It Works):      T2/T3/T4/T5 intra; T2×T3, T3×T5, T4×T5, T2×T4 inter
      Ch3 (Verses):            T7 literary intra; verse-grounded inter (rare)
      Ch4 (Language):          T7 lexical intra; T2×T7, T1×T7 inter
      Ch5 (Interrelationships): T6 intra; T6×T2, T6×T4, T6×T5 inter
    """
    if not tiers_str:
        return "Ch2"  # default
    tiers = {t.strip() for t in tiers_str.split(",") if t.strip()}
    if finding_type == "SYNTHESIS_INTRA_TIER":
        if "T1" in tiers:
            return "Ch1"
        if "T6" in tiers:
            return "Ch5"
        if "T7" in tiers:
            return "Ch4"
        if tiers & {"T2", "T3", "T4", "T5"}:
            return "Ch2"
        return "Ch2"
    # SYNTHESIS_INTER_TIER
    if "T6" in tiers:
        return "Ch5"
    if "T7" in tiers and ("T1" in tiers or "T2" in tiers):
        return "Ch4"
    if tiers & {"T2", "T3", "T4", "T5"}:
        return "Ch2"
    if "T1" in tiers:
        return "Ch1"
    return "Ch2"


def fetch_synthesis_for_chapter(conn, registry_no, chapter):
    """Return synthesis findings for a chapter, including all outcomes (D/F/N).
    When session_c_chapter is N/A or NULL, fall back to tier-based routing
    per v1.8 §10."""
    rows = conn.execute(
        """
        SELECT finding_id, finding_type, synthesis_outcome, tiers_engaged,
               structural_relationship, session_c_chapter, sd_pointer_ref, finding
        FROM wa_session_b_findings
        WHERE registry_id = ?
        AND finding_type LIKE 'SYNTHESIS_%'
        AND delete_flag = 0
        ORDER BY finding_type DESC, finding_id
        """,
        (registry_no,),
    ).fetchall()

    matched: list[sqlite3.Row] = []
    for r in rows:
        sc = (r["session_c_chapter"] or "").strip()
        if sc and sc != "N/A":
            # Multi-chapter values (e.g. "Ch2,Ch5") split on comma
            chapters_listed = {c.strip() for c in sc.replace(" ", "").split(",")}
            if chapter in chapters_listed:
                matched.append(r)
        else:
            # No explicit routing — derive from tiers
            derived = derive_chapter_from_tiers(r["tiers_engaged"], r["finding_type"])
            if derived == chapter:
                matched.append(r)
    return matched


def fetch_owner_term_inventory(conn, registry_no):
    rows = conn.execute(
        """
        SELECT ti.id AS inv_id, ti.term_id, ti.transliteration, ti.language,
               ti.step_search_gloss, ti.short_def_mounce, ti.occurrence_count,
               ti.parsed_meaning_id, ti.meaning,
               (SELECT COUNT(*) FROM wa_verse_records vr
                WHERE vr.term_inv_id = ti.id
                AND (vr.delete_flagged = 0 OR vr.delete_flagged IS NULL)) AS active_v
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.registry_id = ?
        AND ti.term_owner_type = 'OWNER'
        AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
        ORDER BY ti.language, ti.term_id
        """,
        (registry_no,),
    ).fetchall()
    return rows


def fetch_xref_inventory(conn, registry_no):
    rows = conn.execute(
        """
        SELECT ti.term_id, ti.transliteration, ti.language,
               ti.step_search_gloss, ti.occurrence_count
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        WHERE fi.registry_id = ?
        AND ti.term_owner_type = 'XREF'
        AND (ti.delete_flagged = 0 OR ti.delete_flagged IS NULL)
        ORDER BY ti.language, ti.term_id
        """,
        (registry_no,),
    ).fetchall()
    return rows


def fetch_anchor_verses(conn, registry_no, order="group"):
    """Fetch anchor verses with full context. order='group' (default) groups
    anchors by (strongs, group_code) so each group's H2 heading appears once;
    order='canonical' sorts by book/chapter/verse only."""
    if order == "canonical":
        order_by = "vr.book_id, vr.chapter, vr.verse_num"
    else:
        order_by = "mt.strongs_number, g.group_code, vr.book_id, vr.chapter, vr.verse_num"
    rows = conn.execute(
        f"""
        SELECT vr.id AS verse_id, vr.reference, vr.verse_text,
               vr.term_id, vr.transliteration, vr.book_id, vr.chapter, vr.verse_num,
               mt.strongs_number,
               g.group_code, g.context_description AS group_desc,
               vc.analysis_note
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN verse_context_group g ON g.id = vc.group_id
        WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
        AND vc.is_anchor = 1
        AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)
        ORDER BY {order_by}
        """,
        (registry_no,),
    ).fetchall()
    return rows


def fetch_vc_groups(conn, registry_no):
    rows = conn.execute(
        """
        SELECT g.group_code, g.context_description, g.notes,
               mt.strongs_number,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = g.id
                AND vc.is_relevant = 1 AND (vc.delete_flagged=0 OR vc.delete_flagged IS NULL)) AS rel_v,
               (SELECT COUNT(*) FROM verse_context vc WHERE vc.group_id = g.id
                AND vc.is_anchor = 1 AND (vc.delete_flagged=0 OR vc.delete_flagged IS NULL)) AS anchor_v
        FROM verse_context_group g
        JOIN mti_terms mt ON mt.id = g.mti_term_id
        WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
        AND (g.delete_flagged = 0 OR g.delete_flagged IS NULL)
        ORDER BY g.group_code
        """,
        (registry_no,),
    ).fetchall()
    return rows


def fetch_co_occurrence(conn, registry_no, top=25):
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
        LIMIT ?
        """,
        (registry_no, registry_no, top),
    ).fetchall()
    return rows


def fetch_shared_anchors(conn, registry_no):
    rows = conn.execute(
        """
        WITH r_anchors AS (
            SELECT DISTINCT vr.id AS verse_record_id, vr.reference, vr.book_id, vr.chapter, vr.verse_num
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            JOIN mti_terms mt ON mt.id = vc.mti_term_id
            WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
            AND vc.is_anchor = 1
            AND (vc.delete_flagged = 0 OR vc.delete_flagged IS NULL)
        )
        SELECT a.reference,
               GROUP_CONCAT(wr.word || '/R' || fi.registry_id, '; ') AS others
        FROM r_anchors a
        JOIN wa_verse_records vr ON vr.book_id = a.book_id AND vr.chapter = a.chapter AND vr.verse_num = a.verse_num
        JOIN verse_context vc2 ON vc2.verse_record_id = vr.id AND vc2.is_anchor = 1
            AND (vc2.delete_flagged = 0 OR vc2.delete_flagged IS NULL)
        JOIN mti_terms mt ON mt.id = vc2.mti_term_id
        JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        JOIN wa_file_index fi ON fi.word_registry_fk = wr.id
        WHERE wr.no != ?
        GROUP BY a.reference
        ORDER BY a.book_id, a.chapter, a.verse_num
        """,
        (registry_no, registry_no),
    ).fetchall()
    return rows


def fetch_sd_pointers(conn, registry_no):
    rows = conn.execute(
        """
        SELECT flag_label, priority, session_target, raised_date, session_raised, description, strongs_reference
        FROM wa_session_research_flags
        WHERE registry_id = (SELECT id FROM word_registry WHERE no = ?)
        AND flag_code = 'SD_POINTER'
        AND (resolved = 0 OR resolved IS NULL)
        ORDER BY
            CASE priority WHEN 'HIGH' THEN 0 WHEN 'MEDIUM' THEN 1 ELSE 2 END,
            flag_label
        """,
        (registry_no,),
    ).fetchall()
    return rows


def fetch_meaning_senses(conn, term_inv_id):
    """Fetch wa_meaning_parsed + wa_meaning_sense for an OWNER term."""
    parsed = conn.execute(
        "SELECT * FROM wa_meaning_parsed WHERE id = (SELECT parsed_meaning_id FROM wa_term_inventory WHERE id = ?)",
        (term_inv_id,),
    ).fetchone()
    if not parsed:
        return None, []
    senses = conn.execute(
        "SELECT * FROM wa_meaning_sense WHERE parsed_meaning_id = ? ORDER BY id",
        (parsed["id"],),
    ).fetchall()
    return parsed, senses


# --- Q&A printing helper ---

def render_qa_block(qa_entries):
    """Render a list of Q&A entries as a markdown sub-section."""
    out: list[str] = []
    for q in qa_entries:
        out.append(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
        out.append(f"{q['answer']}\n")
    return out


def render_synthesis_block(syntheses):
    """Render synthesis entries grouped by outcome (D / F / N).

    D — substantive finding, full text shown as the synthesis claim
    F — further research required, always paired with an SD pointer
    N — not applicable, one-sentence rationale shown briefly
    """
    out: list[str] = []
    by_outcome = {"D": [], "F": [], "N": []}
    other = []
    for s in syntheses:
        oc = (s["synthesis_outcome"] or "").upper()
        if oc in by_outcome:
            by_outcome[oc].append(s)
        else:
            other.append(s)

    # D — substantive findings
    for s in by_outcome["D"]:
        tiers = s["tiers_engaged"] or ""
        struct = s["structural_relationship"] or "N/A"
        out.append(f"**{s['finding_id']} | {tiers}** *(outcome: D; structural: {struct})*\n")
        out.append(f"{s['finding']}\n")

    # F — further research required
    if by_outcome["F"]:
        out.append("\n**Further-research items (F outcome)** — these synthesis pairs raise questions that cannot be resolved from the current evidence; each pairs with an SD pointer for Session D.\n")
        for s in by_outcome["F"]:
            tiers = s["tiers_engaged"] or ""
            sd = s["sd_pointer_ref"] or "(no SD pointer linked)"
            out.append(f"\n**{s['finding_id']} | {tiers}** *(outcome: F; SD pointer: {sd})*\n")
            out.append(f"{s['finding']}\n")

    # N — not applicable (brief)
    if by_outcome["N"]:
        out.append("\n**Not-applicable items (N outcome)** — these synthesis pairs do not produce a structural relationship for this word. Each carries a one-sentence rationale.\n")
        for s in by_outcome["N"]:
            tiers = s["tiers_engaged"] or ""
            out.append(f"- **{s['finding_id']} | {tiers}**: {s['finding']}")
        out.append("")

    if other:
        # Fallback for unexpected outcome values
        out.append("\n**Other outcome entries:**\n")
        for s in other:
            out.append(f"- {s['finding_id']} (outcome={s['synthesis_outcome']}): {s['finding'][:200]}…")

    return out


# --- Per-chapter assemblers ---

def assemble_ch1_meaning(conn, registry_no):
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    P: list[str] = []
    P.append(f"# Chapter 1 — Meaning")
    P.append(f"\n**Registry {registry_no:03d} — {reg['word'].title()}** · *Word Characteristic Summary*\n")
    P.append("---\n")

    P("## What it is\n") if False else None
    P.append("## What it is\n")
    if reg["description"]:
        P.append(f"> {reg['description']}\n")
    qa = fetch_qa_for_components(conn, registry_no, ["T1.2"])
    t1_2_3 = next((q for q in qa if q["prompt_seq"] == 3), None)
    if t1_2_3:
        P.append(f"\n**Working description:** {t1_2_3['answer']}\n")

    P.append("\n## Name and naming\n")
    P.extend(render_qa_block(fetch_qa_for_components(conn, registry_no, ["T1.1"])))

    P.append("\n## Kind\n")
    for q in fetch_qa_for_components(conn, registry_no, ["T1.2"]):
        if q["prompt_seq"] == 3:
            continue
        P.append(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
        P.append(f"{q['answer']}\n")

    P.append("\n## Boundary — what it is not\n")
    P.extend(render_qa_block(fetch_qa_for_components(conn, registry_no, ["T1.3"])))

    P.append("\n## Modes of operation\n")
    P.extend(render_qa_block(fetch_qa_for_components(conn, registry_no, ["T1.4"])))

    qa_t15 = fetch_qa_for_components(conn, registry_no, ["T1.5"])
    if qa_t15:
        P.append("\n## Immediate response\n")
        P.extend(render_qa_block(qa_t15))

    qa_t16 = fetch_qa_for_components(conn, registry_no, ["T1.6"])
    if qa_t16:
        P.append("\n## Sustained effect\n")
        P.extend(render_qa_block(qa_t16))

    qa_t17 = fetch_qa_for_components(conn, registry_no, ["T1.7"])
    if qa_t17:
        P.append("\n## Conditions of reception\n")
        P.extend(render_qa_block(qa_t17))

    qa_t18 = fetch_qa_for_components(conn, registry_no, ["T1.8"])
    if qa_t18:
        P.append("\n## Dimension classification\n")
        P.extend(render_qa_block(qa_t18))

    anchors = fetch_anchor_verses(conn, registry_no)
    if anchors:
        P.append(f"\n## Anchor verses\n")
        P.append(f"The {len(anchors)} anchor verses define this characteristic across its OWNER groups. Each anchor carries the full verse text, group context, and the Stage 2a analysis from `verse_context.analysis_note` — including the five cross-registry vision answers and any inline observations or SD pointers raised at this verse.\n")
        cur_group = None
        for a in anchors:
            g_key = (a["strongs_number"], a["group_code"])
            if g_key != cur_group:
                P.append(f"\n### {a['strongs_number']} ({a['transliteration'] or ''}) · group {a['group_code']}\n")
                P.append(f"*{a['group_desc']}*\n")
                cur_group = g_key
            verse_text = (a["verse_text"] or "").replace("\n", " ").strip()
            P.append(f"\n**{a['reference']}** — {verse_text}\n")
            if a["analysis_note"]:
                P.append("*Stage 2a analysis (5 cross-registry vision questions + inline observations):*\n")
                P.append(a["analysis_note"])
                P.append("")

    syn = fetch_synthesis_for_chapter(conn, registry_no, "Ch1")
    if syn:
        P.append("\n## Synthesis — what T1 reveals as a whole\n")
        P.extend(render_synthesis_block(syn))

    P.append("\n## Lexical foundation\n")
    terms = fetch_owner_term_inventory(conn, registry_no)
    if terms:
        P.append("**OWNER terms:**\n")
        P.append("| Strong's | Translit | Language | Active verses | Gloss |")
        P.append("| --- | --- | --- | ---: | --- |")
        for t in terms:
            gloss = (t["step_search_gloss"] or "").replace("|", "/")[:60]
            P.append(f"| {t['term_id']} | {t['transliteration'] or ''} | {t['language']} | {t['active_v']} | {gloss} |")
        P.append("")
    lex = fetch_qa_for_components(conn, registry_no, ["T7.1"])
    if lex:
        P.append("\n**Vocabulary analysis (T7.1):**\n")
        P.extend(render_qa_block(lex))

    return "\n".join(P)


def assemble_ch2_how_it_works(conn, registry_no):
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    P: list[str] = []
    P.append(f"# Chapter 2 — How It Works")
    P.append(f"\n**Registry {registry_no:03d} — {reg['word'].title()}** · *Word Impact Description*\n")
    P.append("Operations, faculties, constitutional location, relational axis, formative dimension. Drawn from T2 (Constitutional Location), T3 (Inner Faculties), T4 (Relational Interfaces), and T5 (Formative & Developmental).\n")
    P.append("---\n")

    # T2 — Constitutional Location
    t2_components = ["T2.1","T2.2","T2.3","T2.4","T2.5","T2.6","T2.7","T2.8","T2.9","T2.10"]
    qa_t2 = fetch_qa_for_components(conn, registry_no, t2_components)
    if qa_t2:
        P.append("## Constitutional location and boundaries\n")
        P.append("Where this characteristic operates within the spirit/soul/heart/mind/body structure.\n")
        cur_comp = None
        for q in qa_t2:
            if q["component_code"] != cur_comp:
                P.append(f"\n### {q['component_code']} — {q['component_title']}\n")
                cur_comp = q["component_code"]
            P.append(f"**Prompt {q['prompt_seq']}: {q['question_text']}**\n")
            P.append(f"{q['answer']}\n")

    # T3 — Inner Faculties
    t3_components = [f"T3.{i}" for i in range(1, 12)]
    qa_t3 = fetch_qa_for_components(conn, registry_no, t3_components)
    if qa_t3:
        P.append("\n## Inner faculties engaged\n")
        P.append("How this characteristic engages the eleven inner-being faculties: perception, cognition, memory, affect, creativity, volition, agency, moral evaluation, conscience, conscientiousness, and relational capacity.\n")
        cur_comp = None
        for q in qa_t3:
            if q["component_code"] != cur_comp:
                P.append(f"\n### {q['component_code']} — {q['component_title']}\n")
                cur_comp = q["component_code"]
            P.append(f"**Prompt {q['prompt_seq']}: {q['question_text']}**\n")
            P.append(f"{q['answer']}\n")

    # T4 — Relational Interfaces
    t4_components = [f"T4.{i}" for i in range(1, 7)]
    qa_t4 = fetch_qa_for_components(conn, registry_no, t4_components)
    if qa_t4:
        P.append("\n## Relational interfaces\n")
        P.append("How this characteristic operates across the relational interfaces of the human person — God-to-human, human-to-God, human-to-human (giving / receiving / boundaries), and the spiritual beings interface.\n")
        cur_comp = None
        for q in qa_t4:
            if q["component_code"] != cur_comp:
                P.append(f"\n### {q['component_code']} — {q['component_title']}\n")
                cur_comp = q["component_code"]
            P.append(f"**Prompt {q['prompt_seq']}: {q['question_text']}**\n")
            P.append(f"{q['answer']}\n")

    # T5 — Formative & Developmental
    t5_components = [f"T5.{i}" for i in range(1, 8)]
    qa_t5 = fetch_qa_for_components(conn, registry_no, t5_components)
    if qa_t5:
        P.append("\n## Formative and developmental dimension\n")
        P.append("How this characteristic shapes the person over time — nature of transformation, sequence of inner states, mechanism of change, suffering and affliction, formation and sanctification, eschatological trajectory, deposit consequence.\n")
        cur_comp = None
        for q in qa_t5:
            if q["component_code"] != cur_comp:
                P.append(f"\n### {q['component_code']} — {q['component_title']}\n")
                cur_comp = q["component_code"]
            P.append(f"**Prompt {q['prompt_seq']}: {q['question_text']}**\n")
            P.append(f"{q['answer']}\n")

    # Synthesis — Ch2
    syn = fetch_synthesis_for_chapter(conn, registry_no, "Ch2")
    if syn:
        P.append("\n## Synthesis — what T2 through T5 reveal as a whole\n")
        # split intra vs inter
        intra = [s for s in syn if s["finding_type"] == "SYNTHESIS_INTRA_TIER"]
        inter = [s for s in syn if s["finding_type"] == "SYNTHESIS_INTER_TIER"]
        if intra:
            P.append("\n### Intra-tier syntheses\n")
            P.extend(render_synthesis_block(intra))
        if inter:
            P.append("\n### Inter-tier syntheses\n")
            P.extend(render_synthesis_block(inter))

    return "\n".join(P)


def assemble_ch3_verses(conn, registry_no):
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    P: list[str] = []
    P.append(f"# Chapter 3 — Verses")
    P.append(f"\n**Registry {registry_no:03d} — {reg['word'].title()}** · *Annotated Verse Evidence*\n")
    P.append("---\n")

    anchors = fetch_anchor_verses(conn, registry_no)
    if not anchors:
        P.append("_No anchor verses recorded._")
        return "\n".join(P)

    P.append(f"This chapter walks the {len(anchors)} anchor verses for this registry in canonical order. Each anchor is presented with its full verse text, group context, dimension assignment, and the Stage 2a analysis (five cross-registry vision questions, inline observations, and any SD pointers raised at the verse) drawn from `verse_context.analysis_note`.\n")

    # Index by group
    cur_group = None
    for a in anchors:
        g_key = (a["strongs_number"], a["group_code"])
        if g_key != cur_group:
            P.append(f"\n## {a['strongs_number']} ({a['transliteration'] or ''}) — group {a['group_code']}\n")
            P.append(f"**Group context:** {a['group_desc']}\n")
            cur_group = g_key
        verse_text = (a["verse_text"] or "").replace("\n", " ").strip()
        P.append(f"\n### {a['reference']}\n")
        P.append(f"> {verse_text}\n")
        if a["analysis_note"]:
            P.append("\n**Stage 2a analysis (5 cross-registry vision questions + inline observations + any SD pointers raised at this verse):**\n")
            P.append(a["analysis_note"])
            P.append("")
        # Find Q&A entries that reference this verse in their anchor_verses field
        qa_for_verse = conn.execute(
            """
            SELECT q.component_code, q.component_title, q.prompt_seq, q.question_text,
                   l.session_b_note AS answer
            FROM wa_finding_catalogue_links l
            JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
            JOIN wa_session_b_findings f ON f.id = l.finding_id
            WHERE f.registry_id = ?
            AND l.validated_by IN ('claude_ai_v1_8','claude_ai_2nd_tier_v1')
            AND f.delete_flag = 0
            AND f.finding_type IN ('OBSERVATION','THEOLOGICAL_NOTE','VERSE_ANNOTATION',
                                   'SOMATIC_EVIDENCE','VERSE_PATTERN','MEANING_OBSERVATION',
                                   'ETYMOLOGY','ROOT_FINDING','SPIRIT_SOUL_BODY','CROSS_REGISTRY')
            AND f.anchor_verses LIKE ?
            ORDER BY q.tier, q.component_code, q.prompt_seq
            LIMIT 8
            """,
            (registry_no, f"%{a['reference']}%"),
        ).fetchall()
        if qa_for_verse:
            seen_ids = set()
            shown = []
            for q in qa_for_verse:
                k = (q["component_code"], q["prompt_seq"])
                if k in seen_ids:
                    continue
                seen_ids.add(k)
                shown.append(q)
            if shown:
                P.append(f"\n**Q&A entries citing this verse as anchor:**\n")
                for q in shown:
                    P.append(f"- *{q['component_code']}.{q['prompt_seq']} ({q['component_title']})*: {q['answer'][:280]}…")
                P.append("")

    return "\n".join(P)


def assemble_ch4_language(conn, registry_no):
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    P: list[str] = []
    P.append(f"# Chapter 4 — Language")
    P.append(f"\n**Registry {registry_no:03d} — {reg['word'].title()}** · *Original Language Vocabulary*\n")
    P.append("Hebrew and Greek precision, somatic dimension, what the English translation obscures.\n")
    P.append("---\n")

    # Term inventory + meaning senses
    terms = fetch_owner_term_inventory(conn, registry_no)
    if terms:
        P.append("## Term inventory\n")
        P.append("**OWNER terms:**\n")
        P.append("| Strong's | Translit | Language | Active verses | Total occurrences | Gloss |")
        P.append("| --- | --- | --- | ---: | ---: | --- |")
        for t in terms:
            gloss = (t["step_search_gloss"] or "").replace("|", "/")[:60]
            P.append(f"| {t['term_id']} | {t['transliteration'] or ''} | {t['language']} | {t['active_v']} | {t['occurrence_count'] or ''} | {gloss} |")
        P.append("")
        for t in terms:
            parsed, senses = fetch_meaning_senses(conn, t["inv_id"])
            if senses:
                P.append(f"\n**{t['term_id']} ({t['transliteration']}) — {len(senses)} sense(s):**\n")
                for s in senses:
                    sense_text = ""
                    for col in ("sense_label", "definition", "gloss", "text"):
                        if col in s.keys() and s[col]:
                            sense_text = s[col]
                            break
                    P.append(f"- {sense_text}")
                P.append("")
        # XREF brief
        xrefs = fetch_xref_inventory(conn, registry_no)
        if xrefs:
            P.append(f"**XREF terms ({len(xrefs)} total):** vocabulary borrowed from neighbouring registries; see data package §2.2 for full inventory.\n")

    # T7.1 — Lexical and Semantic Analysis
    qa_t71 = fetch_qa_for_components(conn, registry_no, ["T7.1"])
    if qa_t71:
        P.append("\n## Lexical and semantic analysis (T7.1)\n")
        P.extend(render_qa_block(qa_t71))

    # T7.2 — Verse and Literary Interpretation
    qa_t72 = fetch_qa_for_components(conn, registry_no, ["T7.2"])
    if qa_t72:
        P.append("\n## Verse and literary interpretation (T7.2)\n")
        P.extend(render_qa_block(qa_t72))

    # T2.6, T2.7, T2.8 — Body / Somatic Dimension
    qa_body = fetch_qa_for_components(conn, registry_no, ["T2.6","T2.7","T2.8"])
    if qa_body:
        P.append("\n## Somatic dimension — body significance, direction, deposit\n")
        P.append("How (and whether) the characteristic is grounded in the body — whether Scripture links it to specific body parts, the direction of body↔soul interaction, and any constitutional deposit produced over time.\n")
        cur_comp = None
        for q in qa_body:
            if q["component_code"] != cur_comp:
                P.append(f"\n### {q['component_code']} — {q['component_title']}\n")
                cur_comp = q["component_code"]
            P.append(f"**Prompt {q['prompt_seq']}: {q['question_text']}**\n")
            P.append(f"{q['answer']}\n")

    # Synthesis — Ch4
    syn = fetch_synthesis_for_chapter(conn, registry_no, "Ch4")
    if syn:
        P.append("\n## Synthesis — what the language reveals\n")
        intra = [s for s in syn if s["finding_type"] == "SYNTHESIS_INTRA_TIER"]
        inter = [s for s in syn if s["finding_type"] == "SYNTHESIS_INTER_TIER"]
        if intra:
            P.append("\n### Intra-tier syntheses\n")
            P.extend(render_synthesis_block(intra))
        if inter:
            P.append("\n### Inter-tier syntheses\n")
            P.extend(render_synthesis_block(inter))

    return "\n".join(P)


def assemble_ch5_interrelationships(conn, registry_no):
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    P: list[str] = []
    P.append(f"# Chapter 5 — Interrelationships")
    P.append(f"\n**Registry {registry_no:03d} — {reg['word'].title()}** · *Connections and Research Pointers*\n")
    P.append("Cross-registry connections, structural relationships, vocabulary sharing, and shared verse anchors.\n")
    P.append("---\n")

    # T6 — Structural Relationships
    t6_components = [f"T6.{i}" for i in range(1, 8)]
    qa_t6 = fetch_qa_for_components(conn, registry_no, t6_components)
    if qa_t6:
        P.append("## Structural relationships (T6)\n")
        cur_comp = None
        for q in qa_t6:
            if q["component_code"] != cur_comp:
                P.append(f"\n### {q['component_code']} — {q['component_title']}\n")
                cur_comp = q["component_code"]
            P.append(f"**Prompt {q['prompt_seq']}: {q['question_text']}**\n")
            P.append(f"{q['answer']}\n")

    # Co-occurrence top 25
    co = fetch_co_occurrence(conn, registry_no, top=25)
    if co:
        P.append(f"\n## Co-occurrence with other registries (top {len(co)})\n")
        P.append("Other registries that share verse references with this word's OWNER active verses. Counts are distinct (book, chapter, verse) tuples; the same verse is counted once.\n")
        P.append("| Registry | Word | Shared verses |")
        P.append("| ---: | --- | ---: |")
        for r in co:
            try:
                rn = int(r["reg_no"])
                P.append(f"| R{rn:03d} | {r['word']} | {r['shared']} |")
            except (TypeError, ValueError):
                P.append(f"| R{r['reg_no']} | {r['word']} | {r['shared']} |")

    # Shared anchor verses
    sa = fetch_shared_anchors(conn, registry_no)
    if sa:
        P.append(f"\n## Shared anchor verses\n")
        P.append("Verses where the same (book, chapter, verse) is anchor in another registry's OWNER VC group.\n")
        P.append("| Reference | Also anchored in |")
        P.append("| --- | --- |")
        for r in sa:
            others = r["others"] or ""
            seen, kept = set(), []
            for piece in others.split("; "):
                if piece and piece not in seen:
                    seen.add(piece)
                    kept.append(piece)
            P.append(f"| {r['reference']} | {'; '.join(kept)} |")

    # Synthesis — Ch5
    syn = fetch_synthesis_for_chapter(conn, registry_no, "Ch5")
    if syn:
        P.append("\n## Synthesis — what the cross-registry analysis reveals\n")
        intra = [s for s in syn if s["finding_type"] == "SYNTHESIS_INTRA_TIER"]
        inter = [s for s in syn if s["finding_type"] == "SYNTHESIS_INTER_TIER"]
        if intra:
            P.append("\n### Intra-tier syntheses\n")
            P.extend(render_synthesis_block(intra))
        if inter:
            P.append("\n### Inter-tier syntheses\n")
            P.extend(render_synthesis_block(inter))

    return "\n".join(P)


def assemble_ch6_open_questions(conn, registry_no):
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    P: list[str] = []
    P.append(f"# Chapter 6 — Open Questions")
    P.append(f"\n**Registry {registry_no:03d} — {reg['word'].title()}** · *Session D Pointer Compendium*\n")
    P.append("All open SD pointers for this registry, ordered by priority (HIGH first). This chapter is the Session D input from this word.\n")
    P.append("---\n")

    sd = fetch_sd_pointers(conn, registry_no)
    if not sd:
        P.append("_No open SD pointers._")
        return "\n".join(P)

    # Group by priority
    priority_order = ["HIGH", "MEDIUM", "LOW"]
    by_priority: dict[str, list] = {p: [] for p in priority_order}
    for s in sd:
        by_priority.setdefault(s["priority"] or "MEDIUM", []).append(s)

    counts = ", ".join(f"{p}: {len(by_priority[p])}" for p in priority_order if by_priority[p])
    P.append(f"**Total open SD pointers:** {len(sd)} ({counts})\n")

    for p in priority_order:
        items = by_priority.get(p) or []
        if not items:
            continue
        P.append(f"\n## {p} priority ({len(items)})\n")
        for s in items:
            P.append(f"\n### {s['flag_label']}\n")
            meta_bits = [f"priority: {s['priority']}", f"target session: {s['session_target']}"]
            if s["raised_date"]:
                meta_bits.append(f"raised: {s['raised_date']}")
            if s["strongs_reference"]:
                meta_bits.append(f"Strong's: {s['strongs_reference']}")
            P.append(f"_{' · '.join(meta_bits)}_\n")
            if s["session_raised"]:
                P.append(f"*Source:* {s['session_raised']}\n")
            P.append(s["description"] or "_(no description)_")
            P.append("")

    return "\n".join(P)


# --- Main ---

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    reg = conn.execute("SELECT word FROM word_registry WHERE no = ?", (args.registry,)).fetchone()
    if not reg:
        print(f"ERROR: registry {args.registry} not found")
        return 1
    word = reg["word"]

    # Per-word folder (default) — writes to Sessions/Session_B/words/{NNN}_{word}/chapters/
    word_folder = os.path.join(PER_WORD_BASE, f"{args.registry:03d}_{word}")
    OUT_DIR = os.path.join(word_folder, "chapters")
    if not os.path.exists(word_folder):
        # Fallback to legacy path if the per-word folder hasn't been created
        OUT_DIR = LEGACY_OUT_DIR
    os.makedirs(OUT_DIR, exist_ok=True)

    chapters = [
        (1, "Meaning", assemble_ch1_meaning),
        (2, "How It Works", assemble_ch2_how_it_works),
        (3, "Verses", assemble_ch3_verses),
        (4, "Language", assemble_ch4_language),
        (5, "Interrelationships", assemble_ch5_interrelationships),
        (6, "Open Questions", assemble_ch6_open_questions),
    ]

    chapter_outputs = []
    for n, title, fn in chapters:
        body = fn(conn, args.registry)
        out_path = os.path.join(OUT_DIR, f"R{args.registry:03d}-{word}-ch{n}-assembled.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(body)
        chapter_outputs.append((n, title, out_path, body))
        print(f"Wrote {out_path} ({len(body):,} chars / {body.count(chr(10))} lines)")

    # Combined extract
    combined_path = os.path.join(
        OUT_DIR, f"R{args.registry:03d}-{word}-assembled-prose-extract-20260501.md"
    )
    parts = [
        f"# {word.title()} (R{args.registry:03d}) — Assembled Prose Extract\n",
        f"**Generated:** {now_iso()} from `database/bible_research.db`",
        f"**Registry:** R{args.registry:03d} — {word}",
        f"**Source:** Stage 2a observations + Stage 2b Q&A + Stage 2c synthesis under v1.8 (capture script `_apply_v1_8_obslog_capture_v1_20260430.py`)",
        f"**Method:** Mechanical assembly from DB rows. No AI prose generation. Every sentence traces to a finding row, Q&A answer, or DB field.\n",
        "**Chapter structure (per legacy v1.5 model, content drawn from v1.8 captures):**\n",
        "1. *Meaning* — what it is, name, kind, boundary, modes, immediate response, sustained effect, conditions, dimensions, anchor verses with cross-registry vision analysis, lexical foundation",
        "2. *How It Works* — constitutional location, inner faculties, relational interfaces, formative dimension, synthesis",
        "3. *Verses* — annotated walk through every anchor verse with the Stage 2a analysis_note",
        "4. *Language* — term inventory, lexical/semantic analysis, verse and literary interpretation, somatic dimension",
        "5. *Interrelationships* — structural relationships, co-occurrence, shared anchors, cross-registry syntheses",
        "6. *Open Questions* — SD pointer compendium for Session D",
        "",
        "---\n",
    ]
    for n, title, _path, body in chapter_outputs:
        parts.append(body)
        parts.append("\n---\n")
    parts.append(f"\n*Combined extract assembled by `scripts/_tmp_assemble_chapters_full.py` at {now_iso()}.*")

    combined = "\n".join(parts)
    with open(combined_path, "w", encoding="utf-8") as f:
        f.write(combined)
    print(f"\nWrote combined: {combined_path} ({len(combined):,} chars / {combined.count(chr(10))} lines)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
