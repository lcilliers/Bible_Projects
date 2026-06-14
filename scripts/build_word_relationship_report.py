#!/usr/bin/env python
"""build_word_relationship_report.py — READ-ONLY.

For one registry word, report (A) where it appears in the database (table → row count,
grouped by area) and (B) the trail of related words: lexical (term related-words + root
families), cross-registry/XREF (other registry words sharing its Strong's), cross-registry
links, and cluster siblings (C-code + M-code).

Usage:  python scripts/build_word_relationship_report.py --registry 116 [--out PATH]
"""
import argparse, os, sqlite3, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "database", "bible_research.db")


def base_strong(s):
    """Strip a trailing sub-entry letter: H7965H -> H7965, G0530 -> G0530."""
    if not s:
        return s
    return s[:-1] if (len(s) > 1 and s[-1].isalpha() and s[1:-1].isdigit()) else s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--out")
    args = ap.parse_args()
    reg = args.registry

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    wr = cur.execute("SELECT * FROM word_registry WHERE no=?", (reg,)).fetchone()
    if not wr:
        raise SystemExit(f"registry {reg} not found")
    word = wr["word"]

    file_ids = [r["id"] for r in cur.execute("SELECT id FROM wa_file_index WHERE word_registry_fk=?", (reg,))]
    fp = ",".join("?" * len(file_ids)) or "NULL"
    terms = cur.execute(f"SELECT * FROM wa_term_inventory WHERE file_id IN ({fp})", file_ids).fetchall()
    tids = [t["id"] for t in terms]
    tp = ",".join("?" * len(tids)) or "NULL"
    verse_ids = [r["id"] for r in cur.execute(f"SELECT id FROM wa_verse_records WHERE file_id IN ({fp})", file_ids)]
    vp = ",".join("?" * len(verse_ids)) or "NULL"
    mti = cur.execute("SELECT * FROM mti_terms WHERE owning_registry_fk=?", (reg,)).fetchall()
    mids = [m["id"] for m in mti]
    mp = ",".join("?" * len(mids)) or "NULL"

    def count(sql, params):
        return cur.execute(sql, params).fetchone()[0]

    L = []
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    L.append(f"# Word relationship report — registry {reg} ({word})\n")
    L.append(f"_Read-only, generated {now} from the live DB (`scripts/build_word_relationship_report.py`)._\n")

    # Identity
    L.append("## 1. Identity")
    for f in ["no", "word", "source_list", "dimensions", "cluster_assignment",
              "session_b_status", "verse_context_status", "description"]:
        v = wr[f] if f in wr.keys() else None
        if v not in (None, ""):
            L.append(f"- **{f}**: {v}")
    L.append("")

    # A. Where it appears
    L.append("## 2. Where *patience* appears in the database\n".replace("*patience*", f"*{word}*"))
    L.append("| Area | Table | Rows |")
    L.append("| --- | --- | --- |")
    rows = [
        ("Registry", "word_registry", count("SELECT COUNT(*) FROM word_registry WHERE no=?", (reg,))),
        ("Registry", "wa_file_index", count("SELECT COUNT(*) FROM wa_file_index WHERE word_registry_fk=?", (reg,))),
        ("Terms", "wa_term_inventory", len(terms)),
        ("Terms", "wa_term_related_words", count(f"SELECT COUNT(*) FROM wa_term_related_words WHERE term_inv_id IN ({tp})", tids)),
        ("Terms", "wa_term_root_family", count(f"SELECT COUNT(*) FROM wa_term_root_family WHERE term_inv_id IN ({tp})", tids)),
        ("Terms", "wa_term_phase2_flags", count(f"SELECT COUNT(*) FROM wa_term_phase2_flags WHERE term_inv_id IN ({tp})", tids)),
        ("Terms", "wa_meaning_parsed", count(f"SELECT COUNT(*) FROM wa_meaning_parsed WHERE term_inv_id IN ({tp})", tids)),
        ("MTI", "mti_terms (owned)", len(mti)),
        ("MTI", "mti_term_flags", count(f"SELECT COUNT(*) FROM mti_term_flags WHERE mti_term_id IN ({mp})", mids)),
        ("MTI", "mti_term_cross_refs", count(f"SELECT COUNT(*) FROM mti_term_cross_refs WHERE mti_term_id IN ({mp})", mids)),
        ("MTI", "mti_term_subgroup", count(f"SELECT COUNT(*) FROM mti_term_subgroup WHERE mti_term_id IN ({mp})", mids)),
        ("Verses", "wa_verse_records", len(verse_ids)),
        ("Verses", "wa_verse_term_links", count(f"SELECT COUNT(*) FROM wa_verse_term_links WHERE verse_id IN ({vp})", verse_ids)),
        ("Verse context", "verse_context", count(f"SELECT COUNT(*) FROM verse_context WHERE verse_record_id IN ({vp})", verse_ids)),
        ("Findings", "finding (by mti_term)", count(f"SELECT COUNT(*) FROM finding WHERE mti_term_id IN ({mp})", mids)),
        ("Findings", "wa_session_b_findings", count("SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id=?", (reg,))),
        ("Flags", "wa_data_quality_flags", count(f"SELECT COUNT(*) FROM wa_data_quality_flags WHERE file_id IN ({fp})", file_ids)),
        ("Flags", "wa_session_research_flags", count("SELECT COUNT(*) FROM wa_session_research_flags WHERE registry_id=?", (reg,))),
        ("Cross-registry", "wa_cross_registry_links", count(f"SELECT COUNT(*) FROM wa_cross_registry_links WHERE file_id IN ({fp})", file_ids)),
        ("Dimension review", "wa_dimension_index", count("SELECT COUNT(*) FROM wa_dimension_index WHERE owning_registry_no=?", (reg,))),
        ("Engine", "word_run_state", count("SELECT COUNT(*) FROM word_run_state WHERE registry_id=?", (reg,))),
    ]
    for area, tbl, n in rows:
        if n:
            L.append(f"| {area} | `{tbl}` | {n} |")
    L.append("")

    # B. Terms
    L.append("## 3. The terms (anchors)\n")
    for typ in ("OWNER", "XREF"):
        sub = [t for t in terms if t["term_owner_type"] == typ]
        if not sub:
            continue
        L.append(f"### {typ} terms ({len(sub)})")
        L.append("| Strong's | Lang | Translit | Gloss | Occ | del |")
        L.append("| --- | --- | --- | --- | --- | --- |")
        for t in sorted(sub, key=lambda r: (r["language"] or "", r["strongs_number"] or "")):
            gloss = (t["word_analysis_gloss"] or t["step_search_gloss"] or "")[:60]
            L.append(f"| {t['strongs_number']} | {t['language']} | {t['transliteration']} | {gloss} | {t['occurrence_count']} | {t['delete_flagged']} |")
        L.append("")

    # B1. lexical related words
    L.append("## 4. Related-words trail\n")
    L.append("### 4a. Lexical — related words per term (`wa_term_related_words`)\n")
    tmap = {t["id"]: t for t in terms}
    rw = cur.execute(f"SELECT * FROM wa_term_related_words WHERE term_inv_id IN ({tp}) AND COALESCE(delete_flagged,0)=0 ORDER BY term_inv_id", tids).fetchall()
    from collections import defaultdict
    by_term = defaultdict(list)
    for r in rw:
        by_term[r["term_inv_id"]].append(r)
    for tid, items in by_term.items():
        t = tmap[tid]
        rel = "; ".join(f"{i['transliteration'] or ''} ({i['strongs_number'] or '?'}) {i['gloss'] or ''}".strip() for i in items)
        L.append(f"- **{t['strongs_number']} {t['transliteration']}** → {rel}")
    if not rw:
        L.append("_(none)_")
    L.append("")

    # B2 root families
    L.append("### 4b. Root families (`wa_term_root_family`)\n")
    rf = cur.execute(f"SELECT * FROM wa_term_root_family WHERE term_inv_id IN ({tp}) AND COALESCE(delete_flagged,0)=0", tids).fetchall()
    seen = set()
    for r in rf:
        key = (r["root_code"], r["root_gloss"])
        if key in seen:
            continue
        seen.add(key)
        lang = f" ({r['root_language']})" if r["root_language"] else ""
        gl = f" — {r['root_gloss']}" if r["root_gloss"] else ""
        L.append(f"- root **{r['root_code']}**{lang}{gl}")
    if not rf:
        L.append("_(none)_")
    L.append("")

    # B3 cross-registry / XREF shared-term words
    L.append("### 4c. Cross-registry / XREF — other English words sharing these terms\n")
    base = sorted({base_strong(t["strongs_number"]) for t in terms if t["strongs_number"]})
    bp = ",".join("?" * len(base)) or "NULL"
    shared = cur.execute(f"""
        SELECT DISTINCT wr.no, wr.word, ti.strongs_number, ti.term_owner_type
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON ti.file_id = fi.id
        JOIN word_registry wr ON fi.word_registry_fk = wr.no
        WHERE (ti.strongs_number IN ({bp})
               OR substr(ti.strongs_number,1,length(ti.strongs_number)-1) IN ({bp}))
          AND wr.no != ?
        ORDER BY wr.word, ti.strongs_number
    """, base + base + [reg]).fetchall()
    sw = defaultdict(list)
    for r in shared:
        sw[(r["no"], r["word"])].append(f"{r['strongs_number']}({(r['term_owner_type'] or '?')[0]})")
    if sw:
        L.append("| Registry | Word | Shared Strong's |")
        L.append("| --- | --- | --- |")
        for (no, w), strs in sorted(sw.items(), key=lambda x: x[0][1]):
            L.append(f"| {no} | {w} | {', '.join(sorted(set(strs)))} |")
    else:
        L.append("_(no other registry shares these Strong's)_")
    L.append("")

    # B3b mti_term_cross_refs
    cr = cur.execute(f"SELECT DISTINCT registry, word FROM mti_term_cross_refs WHERE mti_term_id IN ({mp}) AND word IS NOT NULL ORDER BY word", mids).fetchall()
    L.append("**`mti_term_cross_refs` (recorded cross-references):** " +
             (", ".join(f"{r['word']} ({r['registry']})" for r in cr) if cr else "_(none)_"))
    L.append("")

    # B4 cross_registry_links
    L.append("### 4d. Cross-registry links (`wa_cross_registry_links`)\n")
    crl = cur.execute(f"""
        SELECT crl.linked_word, crl.linked_registry_id, crl.connecting_term, ct.type_code, ct.description
        FROM wa_cross_registry_links crl
        LEFT JOIN wa_crosslink_type ct ON crl.connection_type_id = ct.id
        WHERE crl.file_id IN ({fp})
    """, file_ids).fetchall()
    if crl:
        L.append("| Linked word | Reg | Type | Connecting term | Note |")
        L.append("| --- | --- | --- | --- | --- |")
        for r in crl:
            L.append(f"| {r['linked_word']} | {r['linked_registry_id']} | {r['type_code'] or ''} | {r['connecting_term'] or ''} | {(r['description'] or '')[:40]} |")
    else:
        L.append("_(none)_")
    L.append("")

    # B5 cluster trail
    L.append("### 4e. Cluster trail\n")
    cc = wr["cluster_assignment"]
    L.append(f"**C-code (dimension-review layer):** `{cc}`")
    if cc:
        sibs = cur.execute("SELECT no, word FROM word_registry WHERE cluster_assignment=? AND no!=? ORDER BY word", (cc, reg)).fetchall()
        L.append(f"- C-code siblings ({len(sibs)}): " + ", ".join(f"{s['word']}({s['no']})" for s in sibs))
    mcodes = sorted({m["cluster_code"] for m in mti if m["cluster_code"]})
    L.append("")
    L.append(f"**M-code cluster(s) of these terms:** " + (", ".join(mcodes) if mcodes else "_(none set)_"))
    for mc in mcodes:
        crow = cur.execute("SELECT short_name, status FROM cluster WHERE cluster_code=?", (mc,)).fetchone()
        nterms = cur.execute("SELECT COUNT(*) FROM mti_terms WHERE cluster_code=?", (mc,)).fetchone()[0]
        if crow:
            L.append(f"- `{mc}` — {crow['short_name']} (status: {crow['status']}; {nterms} terms total in this cluster)")
    L.append("")

    out = args.out or os.path.join(ROOT, "outputs", "markdown",
                                   f"{word}-db-appearance-and-related-words-{now.replace('-','')}.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print("Wrote", out)


if __name__ == "__main__":
    main()
