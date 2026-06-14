"""_tmp_assemble_chapter_prototype.py

Prototype: assemble Ch1 (Meaning) for a registry directly from DB content,
no AI prose generation. Validates the data is sufficient and that the
structure reads coherently.

Usage:
  python scripts/_tmp_assemble_chapter_prototype.py --registry 67 --chapter 1
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("research", "investigations", "chapter_assembly_prototype")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def fetch_qa_for_components(conn, registry_no, components):
    """Return Q&A entries (full answer body) for the given component codes,
    filtered to OBSERVATION-type findings (not synthesis-source breadcrumbs)."""
    placeholders = ",".join("?" for _ in components)
    rows = conn.execute(
        f"""
        SELECT q.component_code, q.component_title, q.prompt_seq,
               q.question_text, l.coverage,
               l.session_b_note AS answer,
               f.finding_id
        FROM wa_finding_catalogue_links l
        JOIN wa_obs_question_catalogue q ON q.obs_id = l.question_id
        JOIN wa_session_b_findings f ON f.id = l.finding_id
        WHERE f.registry_id = ?
        AND l.validated_by = 'claude_ai_v1_8'
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
    # Group by (component_code, prompt_seq) — pick the longest answer if multiple
    by_prompt: dict[tuple[str, int], dict] = {}
    for r in rows:
        key = (r["component_code"], r["prompt_seq"])
        if key not in by_prompt or len(r["answer"] or "") > len(by_prompt[key]["answer"] or ""):
            by_prompt[key] = dict(r)
    return sorted(by_prompt.values(), key=lambda x: (x["component_code"], x["prompt_seq"]))


def fetch_synthesis_for_chapter(conn, registry_no, chapter):
    """Return synthesis findings tagged for this Session C chapter."""
    rows = conn.execute(
        """
        SELECT finding_id, finding_type, synthesis_outcome, tiers_engaged,
               structural_relationship, finding
        FROM wa_session_b_findings
        WHERE registry_id = ?
        AND finding_type LIKE 'SYNTHESIS_%'
        AND delete_flag = 0
        AND synthesis_outcome = 'D'
        AND (',' || REPLACE(session_c_chapter, ' ', '') || ',') LIKE ?
        ORDER BY finding_type DESC, finding_id
        """,
        (registry_no, f"%,{chapter},%"),
    ).fetchall()
    return rows


def fetch_owner_term_inventory(conn, registry_no):
    rows = conn.execute(
        """
        SELECT ti.term_id, ti.transliteration, ti.language, ti.step_search_gloss,
               ti.short_def_mounce, ti.occurrence_count, ti.parsed_meaning_id,
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


def fetch_anchor_verses(conn, registry_no):
    """Fetch all anchor verses for the registry, with verse text, group context,
    and analysis_note (containing the 5 cross-registry vision questions)."""
    rows = conn.execute(
        """
        SELECT vr.id AS verse_id, vr.reference, vr.verse_text,
               vr.term_id, vr.transliteration,
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
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
        """,
        (registry_no,),
    ).fetchall()
    return rows


def assemble_ch1_meaning(conn, registry_no) -> str:
    """Ch1 — Meaning. Sources: registry.description, T1.1-T1.8, T7.1, SYN-INTRA-T1,
    term inventory, anchor verses with cross-registry vision analysis."""
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    word = reg["word"]
    word_title = word.title()

    parts: list[str] = []
    P = parts.append

    P(f"# Chapter 1 — Meaning")
    P(f"\n**Registry {registry_no:03d} — {word_title}** · *Word Characteristic Summary*\n")
    P(f"_Generated {now_iso()} from database — assembled from Stage 2b Q&A, Stage 2c synthesis, term inventory, and Stage 2a anchor-verse readings under v1.8._\n")
    P("---\n")

    # === Section 1: Working description ===
    P("## What it is\n")
    if reg["description"]:
        P(f"> {reg['description']}\n")
    qa = fetch_qa_for_components(conn, registry_no, ["T1.2"])
    t1_2_3 = next((q for q in qa if q["prompt_seq"] == 3), None)
    if t1_2_3:
        P(f"\n**Working description:** {t1_2_3['answer']}\n")

    # === Section 2: Name and naming ===
    P("\n## Name and naming\n")
    for q in fetch_qa_for_components(conn, registry_no, ["T1.1"]):
        P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
        P(f"{q['answer']}\n")

    # === Section 3: Kind ===
    P("\n## Kind\n")
    for q in fetch_qa_for_components(conn, registry_no, ["T1.2"]):
        if q["prompt_seq"] == 3:
            continue
        P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
        P(f"{q['answer']}\n")

    # === Section 4: Boundary ===
    P("\n## Boundary — what it is not\n")
    for q in fetch_qa_for_components(conn, registry_no, ["T1.3"]):
        P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
        P(f"{q['answer']}\n")

    # === Section 5: Modes of operation ===
    P("\n## Modes of operation\n")
    for q in fetch_qa_for_components(conn, registry_no, ["T1.4"]):
        P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
        P(f"{q['answer']}\n")

    # === Section 6: Immediate response (T1.5) ===
    t1_5 = fetch_qa_for_components(conn, registry_no, ["T1.5"])
    if t1_5:
        P("\n## Immediate response\n")
        for q in t1_5:
            P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
            P(f"{q['answer']}\n")

    # === Section 7: Sustained effect (T1.6) ===
    t1_6 = fetch_qa_for_components(conn, registry_no, ["T1.6"])
    if t1_6:
        P("\n## Sustained effect\n")
        for q in t1_6:
            P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
            P(f"{q['answer']}\n")

    # === Section 8: Conditions of reception (T1.7) ===
    t1_7 = fetch_qa_for_components(conn, registry_no, ["T1.7"])
    if t1_7:
        P("\n## Conditions of reception\n")
        for q in t1_7:
            P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
            P(f"{q['answer']}\n")

    # === Section 9: Dimension classification (T1.8) ===
    t1_8 = fetch_qa_for_components(conn, registry_no, ["T1.8"])
    if t1_8:
        P("\n## Dimension classification\n")
        for q in t1_8:
            P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
            P(f"{q['answer']}\n")

    # === Section 10: Anchor verses with the 5 cross-registry vision answers ===
    anchors = fetch_anchor_verses(conn, registry_no)
    if anchors:
        P(f"\n## Anchor verses\n")
        P(f"The {len(anchors)} anchor verses define this characteristic across its OWNER groups. Each anchor carries the full verse text, group context, and the Stage 2a analysis from `verse_context.analysis_note` — including the five cross-registry vision answers and any inline observations or SD pointers raised at this verse.\n")
        # Group by (term_id, group_code)
        cur_group = None
        for a in anchors:
            g_key = (a["strongs_number"], a["group_code"])
            if g_key != cur_group:
                P(f"\n### {a['strongs_number']} ({a['transliteration'] or ''}) · group {a['group_code']}\n")
                P(f"*{a['group_desc']}*\n")
                cur_group = g_key
            verse_text = (a["verse_text"] or "").replace("\n", " ").strip()
            P(f"\n**{a['reference']}** — {verse_text}\n")
            if a["analysis_note"]:
                P(f"*Stage 2a analysis (5 cross-registry vision questions + inline observations):*\n")
                P(a["analysis_note"])
                P("")

    # === Section 11: T1 synthesis (intra-tier) ===
    syn = fetch_synthesis_for_chapter(conn, registry_no, "Ch1")
    if syn:
        P("\n## Synthesis — what T1 reveals as a whole\n")
        for s in syn:
            tiers = s["tiers_engaged"] or ""
            P(f"**{s['finding_id']} | {tiers}** *(outcome: {s['synthesis_outcome']})*\n")
            P(f"{s['finding']}\n")

    # === Section 12: Lexical foundation (T7.1 + term inventory) ===
    P("\n## Lexical foundation\n")
    terms = fetch_owner_term_inventory(conn, registry_no)
    if terms:
        P("**OWNER terms:**\n")
        P("| Strong's | Translit | Language | Active verses | Gloss |")
        P("| --- | --- | --- | ---: | --- |")
        for t in terms:
            gloss = (t["step_search_gloss"] or "").replace("|", "/")[:60]
            P(f"| {t['term_id']} | {t['transliteration'] or ''} | {t['language']} | {t['active_v']} | {gloss} |")
        P("")
    lex_qa = fetch_qa_for_components(conn, registry_no, ["T7.1"])
    if lex_qa:
        P("\n**Vocabulary analysis (T7.1):**\n")
        for q in lex_qa:
            P(f"**{q['component_code']}.{q['prompt_seq']} — {q['question_text']}**\n")
            P(f"{q['answer']}\n")

    P("\n---")
    P(f"*Assembled by `scripts/_tmp_assemble_chapter_prototype.py` from `database/bible_research.db` at {now_iso()}.*")

    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--chapter", type=int, default=1, choices=[1])
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    reg = conn.execute("SELECT word FROM word_registry WHERE no = ?", (args.registry,)).fetchone()
    if not reg:
        print(f"ERROR: registry {args.registry} not found")
        return 1

    if args.chapter == 1:
        out = assemble_ch1_meaning(conn, args.registry)
    else:
        print(f"Chapter {args.chapter} not implemented in prototype")
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(
        OUT_DIR,
        f"R{args.registry:03d}-{reg['word']}-ch{args.chapter}-assembled-prototype.md"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {out_path} ({len(out):,} chars / {out.count(chr(10))} lines)")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
