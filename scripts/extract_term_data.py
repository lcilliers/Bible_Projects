"""
extract_term_data.py
────────────────────
Explore the database through the lens of a single Strong's number.

Shows:
1. The term itself — gloss, meaning, senses, status
2. Every registry it connects to (OWNER and XREF)
3. For each registry — the full term/gloss landscape of that registry,
   so you can see how this term sits within the vocabulary of each word
4. Verse context groups and classifications where they exist

Usage:
    python scripts/extract_term_data.py H2734
    python scripts/extract_term_data.py G5590 --output data/exports/term_G5590.json
    python scripts/extract_term_data.py H7965 --include-deleted
"""
import sqlite3
import json
import argparse
import os
from datetime import date

DB_PATH = os.path.join('data', 'bible_research.db')


def extract(conn, strongs, include_deleted=False):
    """Extract all data for a Strong's number, expanding through registries."""
    df = "" if include_deleted else "AND delete_flagged = 0"
    df_mt = "" if include_deleted else "AND mt.delete_flagged = 0"
    df_ti = "" if include_deleted else "AND ti.delete_flagged = 0"
    df_vr = "" if include_deleted else "AND vr.delete_flagged = 0"
    df_vc = "" if include_deleted else "AND vc.delete_flagged = 0"
    df_vcg = "" if include_deleted else "AND vcg.delete_flagged = 0"

    result = {
        "strongs_number": strongs,
        "extracted_date": date.today().isoformat(),
        "include_deleted": include_deleted,
    }

    # ── 1. The term itself ───────────────────────────────────────────────
    mt = conn.execute(f"""
        SELECT mt.*, wr.no as owning_registry_no, wr.word as owning_registry_word
        FROM mti_terms mt
        LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
        WHERE mt.strongs_number = ? {df_mt}
    """, (strongs,)).fetchone()

    if not mt:
        result["error"] = f"No active mti_terms record for {strongs}"
        return result

    result["term"] = {k: mt[k] for k in mt.keys()}

    # Flags on the mti term
    result["term"]["mti_flags"] = [
        {k: r[k] for k in r.keys()}
        for r in conn.execute(
            "SELECT * FROM mti_term_flags WHERE mti_term_id = ?", (mt['id'],)
        ).fetchall()
    ]

    # Cross refs
    result["term"]["mti_cross_refs"] = [
        {k: r[k] for k in r.keys()}
        for r in conn.execute(
            "SELECT * FROM mti_term_cross_refs WHERE mti_term_id = ?", (mt['id'],)
        ).fetchall()
    ]

    # ── 2. Verse context for this term (programme-wide) ──────────────────
    vcg_rows = conn.execute(f"""
        SELECT vcg.* FROM verse_context_group vcg
        WHERE vcg.mti_term_id = ? {df_vcg}
        ORDER BY vcg.group_code
    """, (mt['id'],)).fetchall()

    result["verse_context"] = {
        "groups": [],
        "set_aside_count": 0,
    }

    for vcg in vcg_rows:
        group = {k: vcg[k] for k in vcg.keys()}
        group["anchors"] = [
            {"reference": r["reference"], "verse_text": r["verse_text"],
             "target_word": r["target_word"]}
            for r in conn.execute(f"""
                SELECT vr.reference, vr.verse_text, vr.target_word
                FROM verse_context vc
                JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                WHERE vc.group_id = ? AND vc.is_anchor = 1 {df_vc}
                ORDER BY vr.book_id, vr.chapter, vr.verse_num
            """, (vcg['id'],)).fetchall()
        ]
        group["related_count"] = conn.execute(f"""
            SELECT COUNT(*) FROM verse_context vc
            WHERE vc.group_id = ? AND vc.is_related = 1 {df_vc}
        """, (vcg['id'],)).fetchone()[0]
        result["verse_context"]["groups"].append(group)

    result["verse_context"]["set_aside_count"] = conn.execute(f"""
        SELECT COUNT(*) FROM verse_context vc
        WHERE vc.mti_term_id = ? AND vc.is_relevant = 0 {df_vc}
    """, (mt['id'],)).fetchone()[0]

    # ── 3. Every registry this term appears in ───────────────────────────
    ti_rows = conn.execute(f"""
        SELECT ti.id as ti_id, ti.strongs_number, ti.step_search_gloss,
               ti.term_owner_type, ti.occurrence_count,
               ti.evidential_status, ti.meaning,
               wr.no as reg_no, wr.word as reg_word,
               wr.verse_context_status, wr.session_b_status,
               wr.cluster_assignment,
               fi.id as file_id
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE ti.strongs_number = ? {df_ti}
        ORDER BY wr.no
    """, (strongs,)).fetchall()

    result["registries"] = []

    for ti in ti_rows:
        reg_entry = {
            "registry_no": ti["reg_no"],
            "registry_word": ti["reg_word"],
            "term_owner_type": ti["term_owner_type"],
            "cluster": ti["cluster_assignment"],
            "verse_context_status": ti["verse_context_status"],
            "session_b_status": ti["session_b_status"],
            "occurrence_count": ti["occurrence_count"],
            "evidential_status": ti["evidential_status"],
            "active_verses_for_this_term": conn.execute(
                "SELECT COUNT(*) FROM wa_verse_records WHERE term_inv_id = ? AND delete_flagged = 0",
                (ti["ti_id"],)
            ).fetchone()[0],
        }

        # Meaning senses for this term in this registry
        mp = conn.execute(
            "SELECT id FROM wa_meaning_parsed WHERE term_inv_id = ?", (ti["ti_id"],)
        ).fetchone()
        if mp:
            reg_entry["meaning_senses"] = [
                {"code": s["level_code"], "text": s["sense_text"],
                 "stem": s["stem_label"]}
                for s in conn.execute(
                    "SELECT level_code, sense_text, stem_label FROM wa_meaning_sense "
                    "WHERE parsed_meaning_id = ? ORDER BY sort_order", (mp["id"],)
                ).fetchall()
            ]
        else:
            reg_entry["meaning_senses"] = []

        # LSJ
        lsj = conn.execute(
            "SELECT lsj_gloss, lsj_domains FROM wa_lsj_parsed WHERE term_inv_id = ?",
            (ti["ti_id"],)
        ).fetchone()
        if lsj and lsj["lsj_gloss"]:
            reg_entry["lsj"] = {"gloss": lsj["lsj_gloss"], "domains": lsj["lsj_domains"]}

        # ── 3a. All other terms in this registry (the gloss landscape) ───
        sibling_terms = conn.execute(f"""
            SELECT ti2.strongs_number, ti2.step_search_gloss, ti2.term_owner_type,
                   ti2.occurrence_count, ti2.evidential_status,
                   mt2.id as mti_id, mt2.gloss as mti_gloss, mt2.status as mti_status,
                   (SELECT COUNT(*) FROM verse_context_group vcg
                    WHERE vcg.mti_term_id = mt2.id {df_vcg}) as vc_group_count
            FROM wa_term_inventory ti2
            JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
            LEFT JOIN mti_terms mt2 ON mt2.strongs_number = ti2.strongs_number
              AND mt2.delete_flagged = 0
            WHERE fi2.word_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
              AND ti2.strongs_number != ?
              {df_ti.replace('ti.', 'ti2.')}
            ORDER BY ti2.term_owner_type DESC, ti2.strongs_number
        """, (ti["reg_no"], strongs)).fetchall()

        reg_entry["registry_terms"] = []
        for sib in sibling_terms:
            sib_entry = {
                "strongs_number": sib["strongs_number"],
                "gloss": sib["step_search_gloss"] or sib["mti_gloss"] or "",
                "term_owner_type": sib["term_owner_type"],
                "mti_status": sib["mti_status"],
                "occurrence_count": sib["occurrence_count"],
                "vc_group_count": sib["vc_group_count"],
            }
            # If this sibling has verse context groups, include descriptions
            if sib["mti_id"] and sib["vc_group_count"] > 0:
                sib_entry["context_descriptions"] = [
                    r["context_description"]
                    for r in conn.execute(f"""
                        SELECT context_description FROM verse_context_group vcg
                        WHERE vcg.mti_term_id = ? {df_vcg}
                        ORDER BY group_code
                    """, (sib["mti_id"],)).fetchall()
                ]
            reg_entry["registry_terms"].append(sib_entry)

        reg_entry["registry_term_count"] = len(sibling_terms)
        reg_entry["registry_owner_count"] = sum(
            1 for s in sibling_terms if s["term_owner_type"] == "OWNER"
        )
        reg_entry["registry_xref_count"] = sum(
            1 for s in sibling_terms if s["term_owner_type"] == "XREF"
        )

        result["registries"].append(reg_entry)

    # ── 4. Cross-registry links ──────────────────────────────────────────
    result["cross_registry_links"] = [
        {k: r[k] for k in r.keys()}
        for r in conn.execute("""
            SELECT cl.*, wr.no as from_registry_no, wr.word as from_registry_word
            FROM wa_cross_registry_links cl
            JOIN wa_file_index fi ON fi.id = cl.file_id
            JOIN word_registry wr ON wr.id = fi.word_registry_fk
            WHERE cl.connecting_term = ?
            ORDER BY wr.no
        """, (strongs,)).fetchall()
    ]

    # ── 5. Session research flags ────────────────────────────────────────
    result["research_flags"] = [
        {k: r[k] for k in r.keys()}
        for r in conn.execute(
            "SELECT * FROM wa_session_research_flags WHERE strongs_reference = ? ORDER BY registry_id",
            (strongs,)
        ).fetchall()
    ]

    # ── 6. Summary ───────────────────────────────────────────────────────
    result["summary"] = {
        "registries_connected": len(result["registries"]),
        "owner_in": [
            {"no": r["registry_no"], "word": r["registry_word"]}
            for r in result["registries"] if r["term_owner_type"] == "OWNER"
        ],
        "xref_in": [
            {"no": r["registry_no"], "word": r["registry_word"]}
            for r in result["registries"] if r["term_owner_type"] == "XREF"
        ],
        "verse_context_groups": len(result["verse_context"]["groups"]),
        "set_aside_count": result["verse_context"]["set_aside_count"],
        "total_sibling_terms": sum(r["registry_term_count"] for r in result["registries"]),
    }

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Extract all DB records for a Strong's number — viewed through the term lens")
    parser.add_argument('strongs', help="Strong's number (e.g. H2734, G5590)")
    parser.add_argument('--output', '-o', help='Output JSON path (default: stdout)')
    parser.add_argument('--include-deleted', action='store_true',
                        help='Include delete_flagged records')
    parser.add_argument('--md', action='store_true',
                        help='Also produce a readable .md report alongside the JSON')
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    data = extract(conn, args.strongs, include_deleted=args.include_deleted)
    conn.close()

    output = json.dumps(data, indent=2, ensure_ascii=False, default=str)

    if args.output:
        os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        s = data.get("summary", {})
        owner_list = ', '.join(str(r['no']) + '-' + r['word'] for r in s.get('owner_in', []))
        xref_list = ', '.join(str(r['no']) + '-' + r['word'] for r in s.get('xref_in', []))
        gloss = data.get('term', {}).get('gloss', '?')
        print(f"Written: {args.output}")
        print(f"  Term: {data['strongs_number']} -- {gloss}")
        print(f"  OWNER in: {owner_list}")
        print(f"  XREF in: {xref_list}")
        print(f"  VC groups: {s.get('verse_context_groups', 0)} | Set aside: {s.get('set_aside_count', 0)}")
        print(f"  Sibling terms across registries: {s.get('total_sibling_terms', 0)}")

        if args.md:
            md_path = args.output.rsplit('.', 1)[0] + '.md'
            md = render_markdown(data)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md)
            print(f"  Markdown: {md_path}")
    else:
        print(output)


def render_markdown(data):
    """Render extracted term data as a readable markdown report."""
    lines = []
    def p(s=''): lines.append(s)

    term = data.get("term", {})
    s = data.get("summary", {})
    strongs = data["strongs_number"]

    p(f"# Term Exploration: {strongs} -- {term.get('gloss', '?')}")
    p()
    p(f"> Transliteration: {term.get('transliteration', '?')}  |  "
      f"Language: {term.get('language', '?')}  |  "
      f"Status: {term.get('status', '?')}")
    p(f"> Owning registry: {term.get('owning_registry_no', '?')}-{term.get('owning_registry_word', '?')}  |  "
      f"Extracted: {data['extracted_date']}")
    p()

    # Summary
    owner_list = ', '.join(str(r['no']) + '-' + r['word'] for r in s.get('owner_in', []))
    xref_list = ', '.join(str(r['no']) + '-' + r['word'] for r in s.get('xref_in', []))
    p("## Summary")
    p()
    p(f"- **OWNER in:** {owner_list or 'none'}")
    p(f"- **XREF in:** {xref_list or 'none'}")
    p(f"- **Verse context groups:** {s.get('verse_context_groups', 0)}")
    p(f"- **Set aside verses:** {s.get('set_aside_count', 0)}")
    p(f"- **Sibling terms across registries:** {s.get('total_sibling_terms', 0)}")
    p()

    # MTI flags
    if term.get("mti_flags"):
        p("## Term Flags")
        p()
        for f_item in term["mti_flags"]:
            p(f"- {f_item.get('flag_code', '?')}: {f_item.get('description', '')}")
        p()

    # Verse Context
    vc = data.get("verse_context", {})
    if vc.get("groups"):
        p("## Verse Context Classification")
        p()
        for g in vc["groups"]:
            p(f"### Group {g.get('group_code', '?')}: {g.get('context_description', '?')}")
            if g.get("notes"):
                p(f"*Note: {g['notes']}*")
            p()
            if g.get("anchors"):
                p("**Anchor verses:**")
                for a in g["anchors"]:
                    p(f"- **{a['reference']}** -- {a['verse_text']}")
                p()
            p(f"Related verses: {g.get('related_count', 0)}")
            p()
        p(f"**Set aside:** {vc.get('set_aside_count', 0)} verses")
        p()

    # Per registry
    p("## Registry Connections")
    p()
    for reg in data.get("registries", []):
        reg_label = f"{reg['registry_no']}-{reg['registry_word']}"
        p(f"### Registry {reg_label}  [{reg['term_owner_type']}]")
        p()
        p(f"- Cluster: {reg.get('cluster', '?')}")
        p(f"- VC status: {reg.get('verse_context_status', '?')}  |  SB status: {reg.get('session_b_status', '?')}")
        p(f"- Verses for {strongs} in this registry: {reg.get('active_verses_for_this_term', 0)}")
        p(f"- Total terms in registry: {reg.get('registry_term_count', 0)} "
          f"(OWNER: {reg.get('registry_owner_count', 0)}, XREF: {reg.get('registry_xref_count', 0)})")
        p()

        # Meaning senses
        if reg.get("meaning_senses"):
            p("**Meaning senses:**")
            for ms in reg["meaning_senses"]:
                stem = f"  [{ms['stem']}]" if ms.get('stem') else ""
                p(f"- {ms.get('code', '')}: {ms.get('text', '')}{stem}")
            p()

        if reg.get("lsj"):
            p(f"**LSJ:** {reg['lsj'].get('gloss', '')}  Domains: {reg['lsj'].get('domains', '')}")
            p()

        # Registry gloss landscape
        if reg.get("registry_terms"):
            p("**Registry term landscape** (all other terms in this word):")
            p()
            p("| Strong | Gloss | Type | Status | VC groups |")
            p("|--------|-------|------|--------|-----------|")
            for sib in reg["registry_terms"]:
                vc_count = sib.get("vc_group_count", 0)
                p(f"| {sib['strongs_number']} | {sib['gloss']} | {sib['term_owner_type']} | "
                  f"{sib.get('mti_status', '')} | {vc_count} |")
            p()

            # Show context descriptions for classified siblings
            classified_sibs = [
                sib for sib in reg["registry_terms"]
                if sib.get("context_descriptions")
            ]
            if classified_sibs:
                p("**Classified term contextual meanings:**")
                p()
                for sib in classified_sibs:
                    p(f"- **{sib['strongs_number']}** ({sib['gloss']}):")
                    for desc in sib["context_descriptions"]:
                        p(f"  - {desc}")
                p()

    # Research flags
    if data.get("research_flags"):
        p("## Research Flags")
        p()
        for fl in data["research_flags"]:
            p(f"- [{fl.get('flag_code', '')}] {fl.get('flag_label', '')}: {fl.get('description', '')}")
        p()

    p("---")
    p(f"*Produced {data['extracted_date']} by extract_term_data.py*")

    return '\n'.join(lines)


if __name__ == '__main__':
    main()
