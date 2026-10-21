#!/usr/bin/env python
"""Produce a FULL markdown extract of a single registry word: every term and
every database row associated with it, traversed across all related tables.

Read-only. Usage:
    python scripts/_produce_registry_full_extract.py --registry 116 --out outputs/markdown/patience-full-db-extract-20260614.md
"""
import argparse, sqlite3, os, datetime

DB = os.path.join('database', 'bible_research.db')


def fetch(cur, sql, params=()):
    return cur.execute(sql, params).fetchall()


def render_rows(rows, drop_null=True):
    """Render a list of sqlite3.Row as markdown: one block per row, non-null fields only."""
    out = []
    for i, r in enumerate(rows, 1):
        d = dict(r)
        if drop_null:
            d = {k: v for k, v in d.items() if v not in (None, '')}
        out.append(f"**Row {i}**")
        for k, v in d.items():
            s = str(v).replace('\r\n', '\n')
            if '\n' in s or len(s) > 200:
                out.append(f"- `{k}`:\n\n  ```\n  " + s.replace('\n', '\n  ') + "\n  ```")
            else:
                out.append(f"- `{k}`: {s}")
        out.append("")
    return "\n".join(out)


def section(title, rows, note=""):
    parts = [f"\n## {title}", f"_Rows: {len(rows)}_{('  — ' + note) if note else ''}\n"]
    if rows:
        parts.append(render_rows(rows))
    else:
        parts.append("_(none)_\n")
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--registry', type=int, required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    reg = args.registry

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # ---- anchor id sets ----
    file_ids = [r['id'] for r in fetch(cur, "SELECT id FROM wa_file_index WHERE word_registry_fk=?", (reg,))]
    fp = ','.join('?' * len(file_ids)) or 'NULL'
    term_rows = fetch(cur, f"SELECT * FROM wa_term_inventory WHERE file_id IN ({fp})", file_ids)
    term_inv_ids = [r['id'] for r in term_rows]
    parsed_ids = [r['parsed_meaning_id'] for r in term_rows if r['parsed_meaning_id']]
    verse_rows = fetch(cur, f"SELECT * FROM wa_verse_records WHERE file_id IN ({fp})", file_ids)
    verse_ids = [r['id'] for r in verse_rows]
    mti_rows = fetch(cur, "SELECT * FROM mti_terms WHERE owning_registry_fk=?", (reg,))
    mti_ids = [r['id'] for r in mti_rows]
    # also any mti term referenced by these verse records (xref copies)
    vr_mti = sorted({r['mti_term_id'] for r in verse_rows if r['mti_term_id']})
    vc_rows = fetch(cur, f"SELECT * FROM verse_context WHERE verse_record_id IN ({','.join('?'*len(verse_ids)) or 'NULL'})", verse_ids)
    vc_ids = [r['id'] for r in vc_rows]
    group_ids = sorted({r['group_id'] for r in vc_rows if r['group_id']})

    def inq(ids):
        return ','.join('?' * len(ids)) or 'NULL', list(ids)

    L = []
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    wr = fetch(cur, "SELECT word FROM word_registry WHERE no=?", (reg,))
    word = wr[0]['word'] if wr else '?'
    L.append(f"# Full DB Extract — registry {reg} ({word})\n")
    L.append(f"_Generated {now} (read-only). Every term and every database row associated with registry {reg}._\n")
    L.append("## Anchor id sets")
    L.append(f"- file_ids: {file_ids}")
    L.append(f"- term_inventory ids: {len(term_inv_ids)} terms")
    L.append(f"- verse_record ids: {len(verse_ids)}")
    L.append(f"- mti_term ids (owned): {mti_ids}")
    L.append(f"- mti_term ids (referenced by verses): {vr_mti}")
    L.append(f"- verse_context ids: {len(vc_ids)}; group_ids: {group_ids}")
    L.append(f"- parsed_meaning ids: {sorted(set(parsed_ids))}")

    # ---- core registry ----
    L.append(section("word_registry", fetch(cur, "SELECT * FROM word_registry WHERE no=?", (reg,))))
    L.append(section("wa_file_index", fetch(cur, f"SELECT * FROM wa_file_index WHERE word_registry_fk=?", (reg,))))

    # ---- terms ----
    L.append(section("wa_term_inventory", term_rows))
    tq, tp = inq(term_inv_ids)
    L.append(section("wa_term_related_words", fetch(cur, f"SELECT * FROM wa_term_related_words WHERE term_inv_id IN ({tq})", tp)))
    L.append(section("wa_term_root_family", fetch(cur, f"SELECT * FROM wa_term_root_family WHERE term_inv_id IN ({tq})", tp)))
    L.append(section("wa_term_phase2_flags", fetch(cur, f"SELECT * FROM wa_term_phase2_flags WHERE term_inv_id IN ({tq})", tp)))
    L.append(section("wa_meaning_parsed", fetch(cur, f"SELECT * FROM wa_meaning_parsed WHERE term_inv_id IN ({tq})", tp)))
    L.append(section("wa_lsj_parsed", fetch(cur, f"SELECT * FROM wa_lsj_parsed WHERE term_inv_id IN ({tq})", tp)))
    pq, pp = inq(sorted(set(parsed_ids)))
    L.append(section("wa_meaning_sense", fetch(cur, f"SELECT * FROM wa_meaning_sense WHERE parsed_meaning_id IN ({pq})", pp)))
    L.append(section("wa_meaning_stem", fetch(cur, f"SELECT * FROM wa_meaning_stem WHERE parsed_meaning_id IN ({pq})", pp)))

    # ---- mti terms ----
    all_mti = sorted(set(mti_ids) | set(vr_mti))
    mq, mp = inq(all_mti)
    L.append(section("mti_terms (owned + referenced by verses)", fetch(cur, f"SELECT * FROM mti_terms WHERE id IN ({mq})", mp)))
    L.append(section("mti_term_flags", fetch(cur, f"SELECT * FROM mti_term_flags WHERE mti_term_id IN ({mq})", mp)))
    L.append(section("mti_term_cross_refs", fetch(cur, f"SELECT * FROM mti_term_cross_refs WHERE mti_term_id IN ({mq})", mp)))
    L.append(section("mti_term_subgroup", fetch(cur, f"SELECT * FROM mti_term_subgroup WHERE mti_term_id IN ({mq})", mp)))

    # ---- verses ----
    L.append(section("wa_verse_records", verse_rows, note="includes delete_flagged"))
    vq, vp = inq(verse_ids)
    L.append(section("wa_verse_term_links", fetch(cur, f"SELECT * FROM wa_verse_term_links WHERE verse_id IN ({vq})", vp)))
    L.append(section("finding_verse_link", fetch(cur, f"SELECT * FROM finding_verse_link WHERE verse_record_id IN ({vq})", vp)))

    # ---- verse context ----
    L.append(section("verse_context", vc_rows))
    gq, gp = inq(group_ids)
    L.append(section("verse_context_group", fetch(cur, f"SELECT * FROM verse_context_group WHERE id IN ({gq})", gp)))
    vcq, vcp = inq(vc_ids)
    L.append(section("finding (level=verse_context)", fetch(cur, f"SELECT * FROM finding WHERE verse_context_id IN ({vcq})", vcp)))
    L.append(section("finding (by mti_term_id)", fetch(cur, f"SELECT * FROM finding WHERE mti_term_id IN ({mq})", mp)))

    # ---- quality / research flags ----
    L.append(section("wa_data_quality_flags", fetch(cur, f"SELECT * FROM wa_data_quality_flags WHERE file_id IN ({fp})", file_ids)))
    L.append(section("wa_session_research_flags", fetch(cur, "SELECT * FROM wa_session_research_flags WHERE registry_id=?", (reg,))))
    L.append(section("wa_cross_registry_links", fetch(cur, f"SELECT * FROM wa_cross_registry_links WHERE file_id IN ({fp})", file_ids)))

    # ---- session B ----
    L.append(section("wa_session_b_dimensions", fetch(cur, "SELECT * FROM wa_session_b_dimensions WHERE registry_id=?", (reg,))))
    sbf = fetch(cur, "SELECT * FROM wa_session_b_findings WHERE registry_id=?", (reg,))
    L.append(section("wa_session_b_findings", sbf))
    sbf_ids = [r['finding_id'] for r in sbf if r['finding_id']]
    if sbf_ids:
        fq, fpp = inq(sbf_ids)
        L.append(section("wa_finding_entity_links", fetch(cur, f"SELECT * FROM wa_finding_entity_links WHERE finding_id IN ({fq})", fpp)))
        L.append(section("wa_finding_catalogue_links", fetch(cur, f"SELECT * FROM wa_finding_catalogue_links WHERE finding_id IN ({fq})", fpp)))

    # ---- dimension index ----
    L.append(section("wa_dimension_index", fetch(cur, f"SELECT * FROM wa_dimension_index WHERE verse_context_group_id IN ({gq}) OR owning_registry_no=?", gp + [reg])))

    # ---- prose ----
    L.append(section("prose_section", fetch(cur, "SELECT * FROM prose_section WHERE registry_id=?", (reg,))))

    # ---- engine audit trail ----
    L.append(section("word_run_state", fetch(cur, "SELECT * FROM word_run_state WHERE registry_id=?", (reg,))))
    L.append(section("term_fetch_log", fetch(cur, "SELECT * FROM term_fetch_log WHERE registry_id=?", (reg,))))

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write("\n".join(L))
    print("Wrote", args.out)
    print("Sections:", sum(1 for x in L if x.lstrip().startswith('## ')))


if __name__ == '__main__':
    main()
