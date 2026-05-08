"""_generate_cluster_prose_extract_v1_20260507.py — read-only.

Builds a candidate "prose-extract" report for a cluster: the data set we
think might feed end-of-analysis prose generation. Three sections:

  1. Findings  — sorted by tier (T0 → T7), then sub-group, then
                 question_code. Includes finding_status and finding_text.
  2. Anchor verses  — one row per is_anchor=1 vc row, with group + sub-
                      group + Strong's + gloss + verse text.
  3. Terms  — one row per active mti_terms row, with sub-group, gloss,
              transliteration, structured senses (wa_meaning_sense),
              Mounce short-def, and an LSJ excerpt.

Auto-bumps version if a file with the same base name already exists.

Usage:
  python scripts/_generate_cluster_prose_extract_v1_20260507.py --m-cluster M06
"""
from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from datetime import date

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR_TMPL = os.path.join("Sessions", "Session_Clusters", "{code}")


def next_version(out_dir: str, basename: str) -> int:
    if not os.path.isdir(out_dir):
        return 1
    rx = re.compile(re.escape(basename) + r"-v(\d+)-\d{8}\.md$")
    n = 0
    for fn in os.listdir(out_dir):
        m = rx.match(fn)
        if m:
            n = max(n, int(m.group(1)))
    return n + 1


def ref_label(book_short, chap, verse):
    return f"{book_short} {chap}:{verse}"


def md_escape(s: str) -> str:
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ")


def trim(s: str, n: int) -> str:
    if s is None:
        return ""
    s = re.sub(r"\s+", " ", str(s)).strip()
    if len(s) <= n:
        return s
    return s[: n - 1] + "…"


def load_cluster(conn, code):
    row = conn.execute(
        "SELECT cluster_code, description, gloss, status FROM cluster "
        " WHERE cluster_code=?", (code,)
    ).fetchone()
    return row


def load_subgroups(conn, code):
    return list(conn.execute(
        "SELECT id, subgroup_code, label, core_description "
        "  FROM cluster_subgroup WHERE cluster_code=? "
        "   AND COALESCE(delete_flagged,0)=0 "
        " ORDER BY COALESCE(sort_order, id)", (code,)
    ))


def load_terms(conn, code):
    return list(conn.execute(
        """
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration,
               mt.gloss, mt.language, mt.cluster_subgroup_id,
               mt.anchor_note, mt.md_version,
               cs.subgroup_code, cs.label AS sg_label,
               ti.short_def_mounce, ti.lsj_entry, ti.meaning,
               ti.parsed_meaning_id, ti.occurrence_count,
               ti.occurrence_count_qualifier, ti.testament
          FROM mti_terms mt
          LEFT JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id
          LEFT JOIN wa_term_inventory ti
                 ON ti.strongs_number=mt.strongs_number
                AND COALESCE(ti.delete_flagged,0)=0
                AND COALESCE(ti.term_owner_type,'OWNER')='OWNER'
         WHERE mt.cluster_code=?
           AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(cs.delete_flagged,0)=0
         ORDER BY mt.cluster_subgroup_id, mt.language, mt.strongs_number
        """, (code,)
    ))


def load_senses_for(conn, parsed_meaning_id):
    if not parsed_meaning_id:
        return []
    return list(conn.execute(
        "SELECT level_code, level_depth, sense_text "
        "  FROM wa_meaning_sense "
        " WHERE parsed_meaning_id=? "
        " ORDER BY sort_order, id", (parsed_meaning_id,)
    ))


def load_findings(conn, code):
    """Findings ordered by question_code → sub-group; placeholders dropped.

    Excludes:
      - cf.delete_flagged=1
      - q.deleted=1 (catalogue rows retired)
      - cs.delete_flagged=1 (sub-groups retired)
      - placeholder text "[Sub-group not separately addressed in source...]"
      - empty finding_text
    """
    return list(conn.execute(
        """
        SELECT cf.id AS finding_id, cf.finding_status, cf.finding_text,
               cf.cluster_subgroup_id, cf.obs_id,
               q.tier, q.question_code, q.question_text,
               q.component_code, q.component_title, q.prompt_seq,
               cs.subgroup_code, cs.label AS sg_label
          FROM cluster_finding cf
          LEFT JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code=?
           AND COALESCE(cf.delete_flagged,0)=0
           AND COALESCE(q.deleted,0)=0
           AND COALESCE(cs.delete_flagged,0)=0
           AND COALESCE(cf.finding_text,'')!=''
           AND cf.finding_text NOT LIKE '[Sub-group not separately%'
         ORDER BY q.question_code, cs.subgroup_code, cf.id
        """, (code,)
    ))


def load_anchors(conn, code):
    return list(conn.execute(
        """
        SELECT vc.id AS vc_id, vc.verse_record_id, vc.group_id,
               vc.notes AS vc_notes, vc.set_aside_reason,
               vcg.group_code, vcg.context_description,
               vcg.notes AS group_notes,
               vr.book_id, vr.chapter, vr.verse_num, vr.verse_text,
               b.short_code AS book_short, b.name AS book_name,
               mt.id AS mti_id, mt.strongs_number, mt.transliteration,
               mt.gloss, mt.language, mt.anchor_note,
               cs.subgroup_code, cs.label AS sg_label
          FROM verse_context vc
          JOIN verse_context_group vcg ON vcg.id=vc.group_id
          JOIN mti_terms mt           ON mt.id=vcg.mti_term_id
          JOIN wa_verse_records vr    ON vr.id=vc.verse_record_id
          JOIN books b                ON b.id=vr.book_id
          LEFT JOIN cluster_subgroup cs ON cs.id=mt.cluster_subgroup_id
         WHERE mt.cluster_code=?
           AND vc.is_anchor=1
           AND COALESCE(vc.delete_flagged,0)=0
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(cs.delete_flagged,0)=0
         ORDER BY cs.subgroup_code, mt.strongs_number, vcg.group_code
        """, (code,)
    ))


# --------------------- writers ---------------------

def write_header(f, cl, sgs, n_terms, n_anchors, n_findings, tier_counts):
    today = date.today().strftime("%Y-%m-%d")
    f.write(f"# Cluster Prose Extract — {cl['cluster_code']}: "
            f"{cl['description'] or cl['gloss'] or ''}\n\n")
    f.write(f"_Generated: {today}_\n\n")
    f.write(f"_Cluster status_: **{cl['status']}**\n\n")
    f.write("## At a glance\n\n")
    f.write(f"- Active terms (mti_terms): **{n_terms}**\n")
    f.write(f"- Anchor verses (is_anchor=1, active): **{n_anchors}**\n")
    f.write(f"- Findings (cluster_finding, non-empty): **{n_findings}**\n")
    f.write("- Findings by tier: " + ", ".join(
        f"{t or '—'}={n}" for t, n in tier_counts) + "\n\n")

    f.write("### Sub-groups\n\n")
    f.write("| Code | Label | Definition |\n")
    f.write("|---|---|---|\n")
    for sg in sgs:
        f.write(
            f"| {md_escape(sg['subgroup_code'])} "
            f"| {md_escape(sg['label'])} "
            f"| {md_escape(trim(sg['core_description'] or '', 200))} |\n"
        )
    f.write("\n---\n\n")


def write_findings_section(f, findings):
    f.write("## 1. Findings (grouped by Q-code)\n\n")
    f.write(
        "_Placeholder rows ('[Sub-group not separately addressed…]') are "
        "filtered out. Each Q-code section shows all sub-group responses "
        "for that question together._\n\n"
    )
    if not findings:
        f.write("_No findings recorded._\n\n---\n\n")
        return

    # Group by question_code; within each, all sub-group rows.
    cur_qc = object()
    first = True
    for r in findings:
        qc = r["question_code"] or "—"
        if qc != cur_qc:
            cur_qc = qc
            tier = r["tier"] or "—"
            if not first:
                f.write("\n")
            first = False
            f.write(f"### {qc}  ·  Tier {tier}\n\n")
            qtext = trim(r["question_text"] or "", 400)
            if qtext:
                f.write(f"> {md_escape(qtext)}\n\n")
            f.write("| Sub-group | Status | Finding |\n")
            f.write("|---|---|---|\n")
        f.write(
            f"| {md_escape(r['subgroup_code'] or '—')} "
            f"| {md_escape(r['finding_status'] or '')} "
            f"| {md_escape(trim(r['finding_text'] or '', 800))} |\n"
        )
    f.write("\n---\n\n")


def write_anchors_section(f, anchors):
    f.write("## 2. Anchor verses\n\n")
    if not anchors:
        f.write("_No anchors set._\n\n---\n\n")
        return

    cur_sg = object()
    for r in anchors:
        sg_key = r["subgroup_code"] or "—"
        if sg_key != cur_sg:
            cur_sg = sg_key
            f.write(f"### Sub-group {sg_key} — {r['sg_label'] or ''}\n\n")

        ref = ref_label(r["book_short"], r["chapter"], r["verse_num"])
        translit = r["transliteration"] or ""
        gloss = r["gloss"] or ""
        f.write(
            f"**Group {r['group_code']}** — "
            f"{r['strongs_number']} *{translit}* "
            f"({r['language']}, “{gloss}”)\n\n"
        )
        if r["context_description"]:
            f.write(
                f"- _Group context_: "
                f"{trim(r['context_description'], 1200)}\n"
            )
        if r["group_notes"]:
            f.write(
                f"- _Group notes_: "
                f"{trim(r['group_notes'], 400)}\n"
            )
        verse_text = trim(r["verse_text"] or "", 800)
        f.write(f"- _Anchor verse_ — **{ref}**: {verse_text}\n")
        anc_note = r["anchor_note"] or r["vc_notes"] or ""
        if anc_note:
            f.write(f"- _Anchor note_: {trim(anc_note, 400)}\n")
        f.write("\n")
    f.write("\n---\n\n")


def write_terms_section(f, conn, terms):
    f.write("## 3. Terms — meaning detail\n\n")
    if not terms:
        f.write("_No active terms._\n\n---\n\n")
        return

    cur_sg = object()
    for t in terms:
        sg_key = t["subgroup_code"] or "—"
        if sg_key != cur_sg:
            cur_sg = sg_key
            f.write(f"### Sub-group {sg_key} — {t['sg_label'] or ''}\n\n")

        occ = t["occurrence_count"]
        occ_q = t["occurrence_count_qualifier"] or ""
        if occ:
            occ_str = f"{occ_q} {occ}".strip()
        else:
            occ_str = "—"

        f.write(
            f"#### {t['strongs_number']} · *{t['transliteration'] or ''}* "
            f"({t['language']}) — {t['gloss'] or ''}\n\n"
        )
        f.write(
            f"- mti_id: `{t['mti_id']}`  ·  "
            f"md_version: `{t['md_version']}`  ·  "
            f"testament: `{t['testament'] or '—'}`  ·  "
            f"occurrences: `{occ_str}`\n\n"
        )

        # Mounce
        if t["short_def_mounce"]:
            f.write("**Concise definition (Mounce):** "
                    f"{trim(t['short_def_mounce'], 400)}\n\n")

        # Senses
        senses = load_senses_for(conn, t["parsed_meaning_id"])
        if senses:
            f.write("**Senses:**\n\n")
            for s in senses:
                indent = "  " * max(0, (s["level_depth"] or 1) - 1)
                code = s["level_code"] or ""
                f.write(
                    f"{indent}- `{code}` "
                    f"{trim(s['sense_text'] or '', 320)}\n"
                )
            f.write("\n")

        # Free-form meaning text (OT / Hebrew often populated here)
        if t["meaning"]:
            f.write("**Lexical entry (raw):**\n\n")
            f.write("> " + trim(t["meaning"], 800) + "\n\n")

        # LSJ excerpt
        if t["lsj_entry"]:
            f.write("**LSJ entry (excerpt):**\n\n")
            f.write("> " + trim(t["lsj_entry"], 600) + "\n\n")

        # Anchor note (term-level)
        if t["anchor_note"]:
            f.write("**Anchor note:** "
                    f"{trim(t['anchor_note'], 400)}\n\n")

        f.write("\n")
    f.write("\n---\n\n")


# --------------------- main ---------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True,
                    help="Cluster code, e.g. M06")
    args = ap.parse_args()
    code = args.m_cluster.upper()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cl = load_cluster(conn, code)
    if cl is None:
        print(f"[err] cluster {code} not found")
        return 1

    sgs = load_subgroups(conn, code)
    terms = load_terms(conn, code)
    findings = load_findings(conn, code)
    anchors = load_anchors(conn, code)

    # Tier counts mirror the filters used in load_findings() so the
    # at-a-glance figures match the rendered table.
    tier_rows = list(conn.execute(
        """
        SELECT q.tier AS tier, COUNT(*) AS n
          FROM cluster_finding cf
          LEFT JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id
          LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
         WHERE cf.cluster_code=?
           AND COALESCE(cf.delete_flagged,0)=0
           AND COALESCE(q.deleted,0)=0
           AND COALESCE(cs.delete_flagged,0)=0
           AND COALESCE(cf.finding_text,'')!=''
           AND cf.finding_text NOT LIKE '[Sub-group not separately%'
         GROUP BY q.tier ORDER BY q.tier
        """, (code,)
    ))
    tier_counts = [(r["tier"], r["n"]) for r in tier_rows]

    out_dir = OUT_DIR_TMPL.format(code=code)
    os.makedirs(out_dir, exist_ok=True)
    base = f"wa-cluster-{code}-prose-extract"
    v = next_version(out_dir, base)
    today_str = date.today().strftime("%Y%m%d")
    fname = f"{base}-v{v}-{today_str}.md"
    out_path = os.path.join(out_dir, fname)

    print(f"Cluster {code}: {cl['description'] or cl['gloss'] or ''}")
    print(f"  terms={len(terms)}  anchors={len(anchors)}  "
          f"findings={len(findings)}")
    print(f"Writing: {out_path}")

    with open(out_path, "w", encoding="utf-8") as f:
        write_header(f, cl, sgs, len(terms), len(anchors),
                     len(findings), tier_counts)
        write_findings_section(f, findings)
        write_anchors_section(f, anchors)
        write_terms_section(f, conn, terms)

    print("Done.")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
