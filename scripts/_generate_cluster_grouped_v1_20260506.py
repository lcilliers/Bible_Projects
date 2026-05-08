"""_generate_cluster_grouped_v1_20260506.py — read-only.

Comprehensive M-cluster report, 4th-iteration organisation:

  Cluster
    -> Sub-group (e.g. M06-A Hatred)
      -> Verse_context_group (e.g. 1601, M06-A-NEW-01)
        -> Description + anchor verse (highlighted)
        -> Other verses related to the group's context
        -> Observation per verse (analysis_note)

Plus, separately at sub-group level:
  -> Unconnected verses (set-aside or no group_id)

Distinct from the §2-per-term and §2-by-sub-group reports — it shows
the analysed verse_context as the primary structural axis, anchored
by group description and anchor verse.

Usage:
  python scripts/_generate_cluster_grouped_v1_20260506.py --m-cluster M06
"""
from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
SESSIONS_DIR = os.path.join("Sessions", "Session_Clusters")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_version(out_dir: str, base_name: str) -> str:
    pat = re.compile(
        r"^" + re.escape(base_name) + r"-v(\d+)-\d{8}\.md$"
    )
    max_v = 0
    if os.path.isdir(out_dir):
        for f in os.listdir(out_dir):
            m = pat.match(f)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def sanitise(s):
    if not s:
        return ""
    s = str(s)
    s = s.replace("```", "")
    s = s.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
    s = s.replace("\t", " ")
    while "  " in s:
        s = s.replace("  ", " ")
    return s.strip().replace("|", "\\|")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--version", default="auto")
    args = ap.parse_args()

    date = datetime.now().strftime("%Y%m%d")
    dest_dir = os.path.join(SESSIONS_DIR, args.m_cluster)
    os.makedirs(dest_dir, exist_ok=True)
    base = f"wa-cluster-{args.m_cluster}-grouped"
    version = (
        next_version(dest_dir, base)
        if args.version == "auto" else args.version
    )
    out_path = os.path.join(dest_dir, f"{base}-{version}-{date}.md")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # ---- Cluster
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (args.m_cluster,)
    ).fetchone()
    if not cluster:
        print(f"ERROR: cluster {args.m_cluster} not found.")
        return 1
    print(f"Cluster {args.m_cluster}: {cluster['description']}")

    # ---- Sub-groups
    subgroups = [dict(r) for r in conn.execute("""
        SELECT id, subgroup_code, label, core_description, sort_order
          FROM cluster_subgroup
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
         ORDER BY sort_order, subgroup_code
    """, (args.m_cluster,)).fetchall()]
    print(f"  sub-groups: {len(subgroups)}")

    # ---- mti_terms in cluster (active OWNER + XREF distinction not relevant
    # here; we just need term identity per mti_id)
    term_meta = {}
    sg_to_mti_ids = defaultdict(list)
    mti_to_sg_id = {}
    for r in conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.gloss,
               mt.transliteration, mt.cluster_subgroup_id
          FROM mti_terms mt
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
    """, (args.m_cluster,)).fetchall():
        term_meta[r["mti_id"]] = dict(r)
        if r["cluster_subgroup_id"]:
            sg_to_mti_ids[r["cluster_subgroup_id"]].append(r["mti_id"])
            mti_to_sg_id[r["mti_id"]] = r["cluster_subgroup_id"]
    print(f"  terms: {len(term_meta)}")

    # ---- verse_context_group rows for each sub-group's terms
    sg_to_groups = defaultdict(list)
    group_meta = {}
    for sg_id, mti_ids in sg_to_mti_ids.items():
        if not mti_ids:
            continue
        ph = ",".join("?" * len(mti_ids))
        for r in conn.execute(f"""
            SELECT vcg.id, vcg.mti_term_id, vcg.group_code,
                   vcg.context_description, vcg.notes
              FROM verse_context_group vcg
             WHERE vcg.mti_term_id IN ({ph})
               AND COALESCE(vcg.delete_flagged,0)=0
             ORDER BY vcg.id
        """, mti_ids):
            row = dict(r)
            sg_to_groups[sg_id].append(row)
            group_meta[row["id"]] = row

    # ---- Lexical context per term: root family, related words, cross-refs
    rf_by_strong = defaultdict(list)
    for r in conn.execute("""
        SELECT mt.strongs_number, rf.root_code, rf.root_language,
               rf.root_gloss, rf.note
          FROM wa_term_root_family rf
          JOIN wa_term_inventory ti ON ti.id=rf.term_inv_id
          JOIN mti_terms mt ON mt.strongs_number=ti.strongs_number
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(rf.delete_flagged,0)=0
         ORDER BY mt.strongs_number, rf.id
    """, (args.m_cluster,)).fetchall():
        rf_by_strong[r["strongs_number"]].append(dict(r))

    rel_by_strong = defaultdict(list)
    for r in conn.execute("""
        SELECT mt.strongs_number AS owner_strong,
               rw.strongs_number AS related_strong,
               rw.transliteration AS related_translit,
               rw.gloss AS related_gloss,
               rw.relationship_note
          FROM wa_term_related_words rw
          JOIN wa_term_inventory ti ON ti.id=rw.term_inv_id
          JOIN mti_terms mt ON mt.strongs_number=ti.strongs_number
         WHERE mt.cluster_code=? AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(rw.delete_flagged,0)=0
         ORDER BY mt.strongs_number, rw.id
    """, (args.m_cluster,)).fetchall():
        rel_by_strong[r["owner_strong"]].append(dict(r))

    # ---- Cluster findings counts per sub-group + cluster (for stats)
    findings_by_sg = defaultdict(lambda: defaultdict(int))
    for r in conn.execute("""
        SELECT cf.cluster_subgroup_id, cf.finding_status,
               cf.finding_text
          FROM cluster_finding cf
         WHERE cf.cluster_code=? AND COALESCE(cf.delete_flagged,0)=0
    """, (args.m_cluster,)).fetchall():
        sg_id = r["cluster_subgroup_id"]
        text = r["finding_text"] or ""
        is_stub = text.startswith("[Sub-group not")
        if is_stub:
            findings_by_sg[sg_id]["NA"] += 1
        elif r["finding_status"] == "finding":
            findings_by_sg[sg_id]["E"] += 1
        elif r["finding_status"] == "silent":
            findings_by_sg[sg_id]["S"] += 1
        elif r["finding_status"] == "gap":
            findings_by_sg[sg_id]["G"] += 1
        elif r["finding_status"] == "cluster_synthesis":
            findings_by_sg[sg_id]["C"] += 1

    # ---- verse_context rows + verse_record info, per group
    # We pull all verse_context for any mti_id in the cluster, then bucket
    # by group_id. Same row can fall under multiple groups only via duals
    # (separate rows, distinct group_ids).
    cluster_mti_ids = list(term_meta.keys())
    if not cluster_mti_ids:
        print("No active terms in cluster.")
        return 1
    ph = ",".join("?" * len(cluster_mti_ids))

    vc_rows = []
    for r in conn.execute(f"""
        SELECT vc.id AS vc_id, vc.verse_record_id, vc.mti_term_id,
               vc.group_id, vc.is_anchor, vc.is_relevant, vc.is_related,
               vc.set_aside_reason, vc.analysis_note, vc.notes,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               vr.verse_text
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
         WHERE vc.mti_term_id IN ({ph})
           AND COALESCE(vc.delete_flagged,0)=0
         ORDER BY vr.book_id, vr.chapter, vr.verse_num,
                  vc.mti_term_id, vc.group_id
    """, cluster_mti_ids):
        vc_rows.append(dict(r))

    # bucket
    vc_by_group = defaultdict(list)
    vc_unconnected = []  # set-aside or no group_id
    for r in vc_rows:
        if r["group_id"] and r["group_id"] > 0 and not r["set_aside_reason"]:
            vc_by_group[r["group_id"]].append(r)
        else:
            vc_unconnected.append(r)

    # ---- Build markdown
    L = []

    def add(s=""):
        L.append(s)

    n_h = sum(1 for m in term_meta.values() if False)  # placeholder
    n_terms = len(term_meta)
    add(f"# {args.m_cluster} {cluster['description']} — grouped report")
    add()
    add(f"**Generated:** {now_iso()}  ")
    add(f"**Cluster:** `{args.m_cluster}` "
        f"(bucket={cluster['bucket']}, status={cluster['status']}, "
        f"version={cluster['version']})  ")
    add(f"**Source:** `database/bible_research.db`  ")
    add(f"**Organisation:** Cluster → Sub-group → "
        f"Verse-context-group → Anchor + verses; unconnected verses "
        f"shown separately per sub-group.  ")
    add()
    add("---")
    add()

    # § Cluster summary
    add(f"## §1. Cluster summary")
    add()
    add(f"1. Description: {cluster['description']}")
    add(f"2. Active terms: {n_terms}")
    add(f"3. Sub-groups: {len(subgroups)}")
    n_total_groups = len(group_meta)
    n_total_vc_rows = sum(len(v) for v in vc_by_group.values())
    n_total_unconnected = len(vc_unconnected)
    add(f"4. Verse-context groups across the cluster: {n_total_groups}")
    add(f"5. Connected verse-context rows: {n_total_vc_rows}")
    add(f"6. Unconnected (set-aside or no group): {n_total_unconnected}")
    add()

    # Sub-group breakdown
    add("**Sub-group breakdown:**")
    add()
    add("| Sub-group | Label | Terms | Groups | Connected verses | "
        "Unconnected | Findings E | S | G | C-synth | N/A |")
    add("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for sg in subgroups:
        sg_id = sg["id"]
        sg_term_ids = sg_to_mti_ids.get(sg_id, [])
        sg_groups = sg_to_groups.get(sg_id, [])
        sg_group_ids = {g["id"] for g in sg_groups}
        sg_connected = sum(
            len(vc_by_group.get(gid, [])) for gid in sg_group_ids
        )
        sg_unconnected = sum(
            1 for r in vc_unconnected
            if r["mti_term_id"] in sg_term_ids
        )
        f = findings_by_sg.get(sg_id, {})
        add(f"| `{sg['subgroup_code']}` | "
            f"{sanitise(sg['label'])} | "
            f"{len(sg_term_ids)} | {len(sg_groups)} | "
            f"{sg_connected} | {sg_unconnected} | "
            f"{f.get('E', 0)} | {f.get('S', 0)} | "
            f"{f.get('G', 0)} | {f.get('C', 0)} | {f.get('NA', 0)} |")
    # Cluster-level findings row
    fc = findings_by_sg.get(None, {})
    add(f"| **CLUSTER** | _cluster-level synthesis_ | — | — | — | — | "
        f"{fc.get('E', 0)} | {fc.get('S', 0)} | "
        f"{fc.get('G', 0)} | {fc.get('C', 0)} | {fc.get('NA', 0)} |")
    add()
    add("_Findings columns: **E**=evidenced finding, **S**=silent (no "
        "verse evidence), **G**=gap (CC database query needed), "
        "**C-synth**=cluster-level synthesis paragraph, **N/A**=sub-group "
        "not separately addressed (see cluster-level finding for that "
        "prompt). Catalogue prompts: 189 (T0–T7)._")
    add()
    add("---")
    add()

    # ---- Per-sub-group sections
    sg_idx = 0
    for sg in subgroups:
        sg_idx += 1
        sg_id = sg["id"]
        sg_term_ids = sg_to_mti_ids.get(sg_id, [])
        sg_groups = sg_to_groups.get(sg_id, [])
        sg_group_ids = {g["id"] for g in sg_groups}

        add(f"## §2.{sg_idx} `{sg['subgroup_code']}` — "
            f"{sanitise(sg['label'])}")
        add()
        add(f"_{sanitise(sg['core_description'])}_")
        add()
        # Terms
        sg_term_strings = sorted(
            f"{term_meta[mid]['strongs_number']} "
            f"{term_meta[mid].get('transliteration') or ''}".strip()
            for mid in sg_term_ids
        )
        add(f"1. Terms in sub-group ({len(sg_term_ids)}): "
            + ", ".join(sg_term_strings))
        add(f"2. Verse-context groups in sub-group "
            f"({len(sg_groups)}):")
        add()

        # Per-group details
        if not sg_groups:
            add("(no verse_context_group rows for terms in this "
                "sub-group yet)")
            add()
        else:
            grp_idx = 0
            for grp in sg_groups:
                grp_idx += 1
                gid = grp["id"]
                vc_rows_for_grp = vc_by_group.get(gid, [])
                # Anchor row (max one is_anchor=1 per group, but multiple
                # could exist if data was inconsistent — pick all to show)
                anchors = [
                    r for r in vc_rows_for_grp if r["is_anchor"] == 1
                ]
                others = [
                    r for r in vc_rows_for_grp if r["is_anchor"] != 1
                ]
                term_for_grp = term_meta.get(grp["mti_term_id"])
                term_label = (
                    f"{term_for_grp['strongs_number']} "
                    f"{term_for_grp.get('transliteration') or ''}"
                    if term_for_grp else "—"
                )
                add(f"### §2.{sg_idx}.{grp_idx} Group "
                    f"`{grp['group_code']}` (id={gid}) — {term_label}")
                add()
                add(f"_{sanitise(grp['context_description'])}_")
                add()
                if grp.get("notes"):
                    add(f"**Notes:** {sanitise(grp['notes'])}  ")
                    add()
                add(f"**Verses:** {len(vc_rows_for_grp)} connected "
                    f"({len(anchors)} anchor, {len(others)} other)  ")
                add()

                # Anchor verse(s) — highlighted
                if anchors:
                    add("**Anchor verse:**")
                    add()
                    add("| Reference | Term | Verse text | Observation |")
                    add("|---|---|---|---|")
                    for a in anchors:
                        tm = term_meta.get(a["mti_term_id"])
                        tl = (
                            f"{tm['strongs_number']} "
                            f"{tm.get('transliteration') or ''}"
                            if tm else "—"
                        )
                        add(
                            f"| **{sanitise(a['reference'])}** | "
                            f"{tl} | "
                            f"{sanitise(a['verse_text'])} | "
                            f"{sanitise(a['analysis_note'])} |"
                        )
                    add()

                # Other verses
                if others:
                    add("**Other verses related to the context:**")
                    add()
                    add("| Reference | Term | Verse text | Observation |")
                    add("|---|---|---|---|")
                    for o in others:
                        tm = term_meta.get(o["mti_term_id"])
                        tl = (
                            f"{tm['strongs_number']} "
                            f"{tm.get('transliteration') or ''}"
                            if tm else "—"
                        )
                        add(
                            f"| {sanitise(o['reference'])} | "
                            f"{tl} | "
                            f"{sanitise(o['verse_text'])} | "
                            f"{sanitise(o['analysis_note'])} |"
                        )
                    add()
                elif not anchors:
                    add("(no verse_context rows yet)")
                    add()

        # Unconnected verses for this sub-group
        sg_unconnected_rows = [
            r for r in vc_unconnected
            if r["mti_term_id"] in sg_term_ids
        ]
        # Plus: untouched verses (no verse_context row at all). Pull
        # for the whole sub-group in one query (avoid N+1).
        if sg_term_ids:
            ph_t = ",".join("?" * len(sg_term_ids))
            for r in conn.execute(f"""
                SELECT vr.id AS vr_id, vr.book_id, vr.chapter,
                       vr.verse_num, vr.reference, vr.verse_text,
                       vr.mti_term_id
                  FROM wa_verse_records vr
                  LEFT JOIN verse_context vc
                    ON vc.verse_record_id=vr.id
                   AND vc.mti_term_id=vr.mti_term_id
                   AND COALESCE(vc.delete_flagged,0)=0
                 WHERE vr.mti_term_id IN ({ph_t})
                   AND COALESCE(vr.delete_flagged,0)=0
                   AND vc.id IS NULL
                 ORDER BY vr.book_id, vr.chapter, vr.verse_num
            """, sg_term_ids):
                sg_unconnected_rows.append({
                    **dict(r), "vc_id": None, "group_id": None,
                    "is_anchor": 0, "is_relevant": None,
                    "is_related": None, "set_aside_reason": None,
                    "analysis_note": "(untouched — no verse_context row)",
                    "notes": None,
                })

        if sg_unconnected_rows:
            add(f"### §2.{sg_idx}.X Unconnected verses for "
                f"sub-group `{sg['subgroup_code']}`")
            add()
            add(f"_Verses for terms in this sub-group that are "
                f"set-aside, untouched (no verse_context row), or have "
                f"no group assignment yet. **Not in active analysis.**_  ")
            add()
            add(f"Count: {len(sg_unconnected_rows)}")
            add()
            add("| Reference | Term | Status | Reason / note | "
                "Verse text |")
            add("|---|---|---|---|---|")
            sg_unconnected_rows.sort(
                key=lambda r: (
                    r["book_id"], r["chapter"], r["verse_num"],
                    r["mti_term_id"],
                )
            )
            for r in sg_unconnected_rows:
                tm = term_meta.get(r["mti_term_id"])
                tl = (
                    f"{tm['strongs_number']} "
                    f"{tm.get('transliteration') or ''}"
                    if tm else "—"
                )
                if r.get("set_aside_reason"):
                    status = "SA"
                    reason = r["set_aside_reason"]
                elif r.get("vc_id") is None:
                    status = "UT"
                    reason = "no verse_context row"
                elif r.get("group_id") in (None, 0):
                    if r.get("is_relevant") == 0:
                        status = "NR"
                    else:
                        status = "P"
                    reason = (r.get("analysis_note") or
                              r.get("notes") or "")
                else:
                    status = "?"
                    reason = ""
                add(
                    f"| {sanitise(r['reference'])} | {tl} | {status} | "
                    f"{sanitise(reason)} | "
                    f"{sanitise(r['verse_text'])} |"
                )
            add()

        add("---")
        add()

    # ---- §3. Per-term lexical context (root family, related words)
    sg_by_id = {sg["id"]: sg for sg in subgroups}
    add("## §3. Per-term lexical context")
    add()
    add("Lexical anchors per term: root family (Hebrew or Greek), related "
        "words, and key meaning notes. Terms ordered by sub-group then "
        "Strong's number.")
    add()
    # Group terms by sub-group (then unassigned)
    terms_by_sg = defaultdict(list)
    for mid, m in term_meta.items():
        terms_by_sg[m.get("cluster_subgroup_id")].append(m)

    sg_order = [sg["id"] for sg in subgroups] + [None]
    sg_idx = 0
    for sg_id in sg_order:
        terms = terms_by_sg.get(sg_id, [])
        if not terms:
            continue
        sg_idx += 1
        if sg_id is None:
            label = "Unassigned (no cluster_subgroup_id)"
            sg_code = "—"
        else:
            sg = sg_by_id[sg_id]
            label = sg["label"]
            sg_code = sg["subgroup_code"]
        add(f"### §3.{sg_idx} `{sg_code}` — {sanitise(label)} "
            f"({len(terms)} terms)")
        add()
        terms_sorted = sorted(
            terms, key=lambda t: t["strongs_number"]
        )
        for m in terms_sorted:
            sn = m["strongs_number"]
            add(f"#### {sn} {m.get('transliteration') or ''} — "
                f"{m.get('gloss') or ''}")
            add()
            rfs = rf_by_strong.get(sn, [])
            rels = rel_by_strong.get(sn, [])
            if rfs:
                add(f"**Root family ({len(rfs)}):**")
                add()
                for rf in rfs:
                    bits = [f"`{rf['root_code']}`"]
                    if rf.get("root_language"):
                        bits.append(rf["root_language"])
                    if rf.get("root_gloss"):
                        bits.append(f"_{rf['root_gloss']}_")
                    add(f"- {' · '.join(bits)}"
                        + (f" — {sanitise(rf['note'])}"
                           if rf.get("note") else ""))
                add()
            else:
                add("_Root family: (none recorded)_")
                add()
            if rels:
                add(f"**Related words ({len(rels)}):**")
                add()
                for rel in rels:
                    label_bits = [
                        rel.get("related_strong") or "?",
                        rel.get("related_translit") or "",
                    ]
                    label_str = " ".join(b for b in label_bits if b).strip()
                    extra = []
                    if rel.get("related_gloss"):
                        extra.append(f"_{rel['related_gloss']}_")
                    if rel.get("relationship_note"):
                        extra.append(sanitise(rel['relationship_note']))
                    add(f"- {label_str}"
                        + (" — " + " · ".join(extra) if extra else ""))
                add()
        add("---")
        add()

    # If there are mti_ids in the cluster with no cluster_subgroup_id,
    # show their unconnected verses in an "Unassigned" tail section.
    unassigned_mti = [
        mid for mid, m in term_meta.items() if not m["cluster_subgroup_id"]
    ]
    if unassigned_mti:
        add(f"## §4. Terms in cluster without a sub-group "
            f"({len(unassigned_mti)})")
        add()
        for mid in unassigned_mti:
            m = term_meta[mid]
            add(f"- {m['strongs_number']} "
                f"{m.get('transliteration') or ''} "
                f"— {m.get('gloss') or ''}")
        add()

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"Wrote: {out_path}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
