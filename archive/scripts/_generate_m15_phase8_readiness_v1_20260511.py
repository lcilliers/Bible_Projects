"""_generate_m15_phase8_readiness_v1_20260511.py — read-only.

Produce a single combined report that captures M15's post-Phase-7 state
and serves as the readiness package for Phase 8 (catalogue pass per
wa-sessionb-cluster-instruction §11).

Contents:
  1. Cluster summary (post-cleanup)
  2. Sub-group inventory — each sub-group's label, description, term
     count, verse counts, and its VCGs with anchors and descriptions
  3. Set-aside summary
  4. Outstanding items (the 5 stray cha.shav verses)
  5. Phase 7 directive history (DIR-010..022)
  6. Phase 8 inputs catalogue (file references)
  7. Phase 8 operating principle reminder (§2 verbatim)

Output: Sessions/Session_Clusters/M15/wa-cluster-M15-phase8-readiness-v1-20260511.md
"""
from __future__ import annotations

import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
OUT_PATH = os.path.join(M15_DIR, "wa-cluster-M15-phase8-readiness-v1-20260511.md")
DB_PATH = os.path.join(ROOT, "database", "bible_research.db")

SG_ORDER = ["M15-A", "M15-B", "M15-C", "M15-D", "M15-E", "M15-F", "M15-G",
            "M15-H", "BOUNDARY"]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cluster = conn.execute(
        "SELECT cluster_code, gloss, bucket, status, version, last_updated_date "
        "FROM cluster WHERE cluster_code='M15'"
    ).fetchone()

    # Sub-groups
    sg_rows = list(conn.execute("""
        SELECT id, subgroup_code, label, core_description
          FROM cluster_subgroup
         WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0
         ORDER BY subgroup_code
    """))

    # Per sub-group: terms + verse breakdown + VCGs
    sg_data = {}
    for sg in sg_rows:
        sg_id = sg["id"]
        # Term count via mti_term_subgroup
        terms = list(conn.execute("""
            SELECT DISTINCT mt.id, mt.strongs_number, mt.transliteration, mt.gloss
              FROM mti_term_subgroup mts
              JOIN mti_terms mt ON mt.id = mts.mti_term_id
             WHERE mts.cluster_subgroup_id=?
               AND COALESCE(mts.delete_flagged,0)=0
               AND mt.cluster_code='M15'
             ORDER BY mt.strongs_number
        """, (sg_id,)))
        # Verse counts (status buckets) — only vc rows physically routed here
        statuses = conn.execute("""
            SELECT
              SUM(CASE WHEN vc.is_relevant=1 AND vc.group_id IS NOT NULL
                        AND vc.set_aside_reason IS NULL THEN 1 ELSE 0 END) AS G,
              SUM(CASE WHEN vc.set_aside_reason IS NOT NULL THEN 1 ELSE 0 END) AS SA,
              SUM(CASE WHEN vc.is_relevant=0 AND vc.set_aside_reason IS NULL
                       THEN 1 ELSE 0 END) AS NR,
              SUM(CASE WHEN vc.is_relevant=1 AND vc.group_id IS NULL
                        AND vc.set_aside_reason IS NULL THEN 1 ELSE 0 END) AS P,
              COUNT(*) AS total
              FROM verse_context vc
             WHERE vc.cluster_subgroup_id=?
               AND COALESCE(vc.delete_flagged,0)=0
        """, (sg_id,)).fetchone()
        # VCGs in this sub-group (via verse_context routing)
        vcgs = list(conn.execute("""
            SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description,
                   (SELECT COUNT(*) FROM verse_context vc2
                     WHERE vc2.group_id = vcg.id
                       AND COALESCE(vc2.delete_flagged,0)=0
                       AND vc2.cluster_subgroup_id=?) AS verse_count,
                   (SELECT COUNT(*) FROM verse_context vc3
                     WHERE vc3.group_id = vcg.id
                       AND vc3.is_anchor=1
                       AND COALESCE(vc3.delete_flagged,0)=0
                       AND vc3.cluster_subgroup_id=?) AS anchor_count
              FROM verse_context_group vcg
             WHERE vcg.id IN (SELECT DISTINCT group_id FROM verse_context
                              WHERE cluster_subgroup_id=?
                                AND group_id IS NOT NULL
                                AND COALESCE(delete_flagged,0)=0)
               AND COALESCE(vcg.delete_flagged,0)=0
             ORDER BY vcg.group_code
        """, (sg_id, sg_id, sg_id)))
        # Anchor verses per VCG
        for v in vcgs:
            anchor_rows = list(conn.execute("""
                SELECT vr.id AS vr_id, vr.reference, mt.strongs_number,
                       mt.transliteration
                  FROM verse_context vc
                  JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                  JOIN mti_terms mt ON mt.id = vc.mti_term_id
                 WHERE vc.group_id=?
                   AND vc.is_anchor=1
                   AND COALESCE(vc.delete_flagged,0)=0
                 LIMIT 5
            """, (v["id"],)))
            v_anchors = [
                f"`[{a['vr_id']}]` {a['reference']} ({a['strongs_number']} {a['transliteration']})"
                for a in anchor_rows
            ]
            v_dict = dict(v)
            v_dict["anchor_refs"] = v_anchors
            v_dict["d_short"] = (
                (v["context_description"] or "")[:200] +
                ("…" if len(v["context_description"] or "") > 200 else "")
            )
            # Replace the SQLite row in vcgs list with the dict
            vcgs[vcgs.index(v)] = v_dict
        sg_data[sg["subgroup_code"]] = {
            "id": sg_id,
            "label": sg["label"],
            "description": sg["core_description"],
            "terms": terms,
            "statuses": statuses,
            "vcgs": vcgs,
        }

    # Cluster-wide totals
    total_vc = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15'
           AND COALESCE(vc.delete_flagged,0)=0
    """).fetchone()[0]
    total_setasides = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15'
           AND COALESCE(vc.delete_flagged,0)=0
           AND vc.set_aside_reason IS NOT NULL
    """).fetchone()[0]
    total_vcgs_active = conn.execute("""
        SELECT COUNT(DISTINCT vcg.id) FROM verse_context_group vcg
          JOIN vcg_term vt ON vt.vcg_id=vcg.id
                           AND COALESCE(vt.delete_flagged,0)=0
          JOIN mti_terms mt ON mt.id=vt.mti_term_id
         WHERE mt.cluster_code='M15'
           AND COALESCE(vcg.delete_flagged,0)=0
    """).fetchone()[0]
    total_new_vcgs = conn.execute("""
        SELECT COUNT(*) FROM verse_context_group
         WHERE group_code LIKE 'M15-%-VCG%'
           AND COALESCE(delete_flagged,0)=0
    """).fetchone()[0]
    n_strays = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
         WHERE mt.cluster_code='M15'
           AND COALESCE(vc.delete_flagged,0)=0
           AND vc.group_id IS NULL
           AND vc.set_aside_reason IS NULL
           AND vc.is_relevant = 1
    """).fetchone()[0]
    distinct_terms = conn.execute("""
        SELECT COUNT(DISTINCT strongs_number) FROM mti_terms
         WHERE cluster_code='M15'
    """).fetchone()[0]
    conn.close()

    # Compose
    out: list[str] = []
    w = out.append
    w("# M15 Wisdom, Understanding and Knowledge — Phase 8 readiness")
    w("")
    w(f"_Generated:_ {now_iso()}  ")
    w(f"_Source:_ post-Phase-7 DB state (M15 cluster, all DIR-010..022 applied)")
    w("")
    w("> _Operating principle (cluster instruction §2):_")
    w(">")
    w("> **Read every verse. Do not sample. Read what they say. Let the structure and analysis emerge from what is found. No assumptions from memory. No jumping to conclusions. Write on discovery.**")
    w(">")
    w("> Output that is structured and fluent but not grounded fails this rule.")
    w("")
    w("---")
    w("")
    w("## 1. Headline")
    w("")
    w(f"| | |")
    w(f"|---|---|")
    w(f"| Cluster | M15 — Wisdom, Understanding and Knowledge |")
    w(f"| Status | `{cluster['status']}` (version `{cluster['version']}`) |")
    w(f"| Active sub-groups | {len(sg_rows)} (M15-A through M15-H + BOUNDARY) |")
    w(f"| Distinct Strong's in cluster | {distinct_terms} |")
    w(f"| Active VCGs (new M15-X-VCG…) | {total_new_vcgs} |")
    w(f"| Active VCGs total (incl. carry-overs for multi-sg terms) | {total_vcgs_active} |")
    w(f"| Active verse_context rows | {total_vc} |")
    w(f"| Set-asides (`no_inner_being_phenomenon`) | {total_setasides} |")
    w(f"| Stray rows (no group, no set-aside, relevant) | {n_strays} |")
    w("")
    w("## 2. Sub-group inventory")
    w("")
    w("Each sub-group is listed with its label, full description, term inventory, verse-status breakdown, and the VCGs that anchor the analytical work for Phase 8.")
    w("")
    for sg_code in SG_ORDER:
        d = sg_data.get(sg_code)
        if not d:
            continue
        w(f"### {sg_code} — {d['label']}")
        w("")
        w(f"_{d['description']}_")
        w("")
        s = d["statuses"]
        w(f"**Verse breakdown:** G={s['G'] or 0} · SA={s['SA'] or 0} · "
          f"NR={s['NR'] or 0} · P={s['P'] or 0} · total={s['total'] or 0}")
        w("")
        # Terms
        terms = d["terms"]
        w(f"**Terms in sub-group ({len(terms)}):** "
          + ", ".join(f"{t['strongs_number']} {t['transliteration']} "
                      f"({t['gloss'] or ''})"
                      for t in terms))
        w("")
        # VCGs
        if d["vcgs"]:
            w(f"**VCGs ({len(d['vcgs'])}):**")
            w("")
            for v in d["vcgs"]:
                anchors_text = ", ".join(v["anchor_refs"]) if v["anchor_refs"] else "_(no anchor!)_"
                w(f"- **`{v['group_code']}`** — {v['d_short']}")
                w(f"  - _Verses_: {v['verse_count']} · "
                  f"_Anchors_: {v['anchor_count']} ({anchors_text})")
        else:
            w("_(no active VCGs)_")
        w("")
        w("---")
        w("")

    # Outstanding items
    w("## 3. Outstanding items (Phase 8 must address)")
    w("")
    if n_strays:
        w(f"**{n_strays} stray verse_context rows** (in a sub-group, no group_id, no set-aside, relevant=1):")
        w("")
        # Enumerate the stray verses
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        stray_rows = list(conn.execute("""
            SELECT vc.id, vr.reference, mt.strongs_number, mt.transliteration,
                   cs.subgroup_code, vr.id AS vr_id
              FROM verse_context vc
              JOIN mti_terms mt ON mt.id = vc.mti_term_id
              JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
              JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
             WHERE mt.cluster_code = 'M15'
               AND COALESCE(vc.delete_flagged,0) = 0
               AND vc.group_id IS NULL
               AND vc.set_aside_reason IS NULL
               AND vc.is_relevant = 1
        """))
        conn.close()
        w("| vr_id | reference | term | sub-group | note |")
        w("|---|---|---|---|---|")
        for r in stray_rows:
            w(f"| `{r['vr_id']}` | {r['reference']} | "
              f"`{r['strongs_number']} {r['transliteration']}` | "
              f"`{r['subgroup_code']}` | M15-A reroute from DIR-010 — no VCG yet |")
        w("")
        w("These verses are H2803G cha.shav devising/scheming in non-craft contexts. They were rerouted from M15-A to M15-E in DIR-010, but the M15-E VCG source file (DIR-015) pre-dated the reroute and did not include them. Phase 8 should propose a VCG assignment (likely VCG01 — purposive willing — or a new VCG for adversarial devising).")
        w("")
    else:
        w("_None — all verses are either in a VCG or set-aside._")
        w("")

    # Phase 7 directive history
    w("## 4. Phase 7 directive history (chronological, all applied)")
    w("")
    w("| Directive | Sub-group / action | Highlights |")
    w("|---|---|---|")
    w("| DIR-010 | M15-A VCG cleanup | 10 VCGs, 263 verses assigned, 39 set-asides, 5 verses rerouted to M15-E |")
    w("| DIR-011 | M15-B VCG cleanup | 7 VCGs, 307 verses, 7 set-asides |")
    w("| DIR-012 | Orphan VCG soft-delete (first wave) | 43 empty VCGs soft-deleted |")
    w("| DIR-013 | M15-C VCG cleanup | 12 VCGs, 572 verses, 4 set-asides |")
    w("| DIR-014 | M15-D VCG cleanup | 7 VCGs, 167 verses, 12 set-asides |")
    w("| DIR-015 | M15-E VCG cleanup | 8 VCGs, 193 verses, 2 set-asides, 5 duplicate vc rows resolved |")
    w("| DIR-016 | M15-F VCG cleanup | 4 VCGs, 67 verses, 1 set-aside |")
    w("| DIR-017 | M15-G VCG cleanup | 3 VCGs, 27 verses |")
    w("| DIR-018 | M15-H sub-group created + VCG cleanup | new sub-group, 3 VCGs, 42 verses, 1 set-aside |")
    w("| DIR-019 | BOUNDARY cleanup | 1 VCG, 1 verse, 5 set-asides |")
    w("| DIR-020 | Orphan VCG soft-delete (second wave) | 91 empty VCGs soft-deleted |")
    w("| DIR-021 | mti_term_subgroup backfill | 38 links added to reflect cross-sg verse routings |")
    w("| DIR-022 | Final cleanup sweep | 8 set-aside reasons normalised; 0 orphans, 0 duplicates remaining |")
    w("")

    # Phase 8 inputs catalogue
    w("## 5. Phase 8 input files (the working set)")
    w("")
    w("Per cluster instruction §11 Phase 8, the inputs to the catalogue pass are:")
    w("")
    w("| File | Purpose |")
    w("|---|---|")
    w("| [`Sessions/Session_Clusters/M15/wa-cluster-M15-grouped-v1-20260511.md`](wa-cluster-M15-grouped-v1-20260511.md) | Cluster → sub-group → VCG → anchor + verses (post-Phase-7 state). The primary input AI reads for the catalogue pass. |")
    w("| [`Sessions/Session_Clusters/M15/wa-cluster-M15-comprehensive-v9-20260511.md`](wa-cluster-M15-comprehensive-v9-20260511.md) | Full per-term + verses + groups + findings + pointers, by-sub-group (post-apply). Reference detail for per-prompt analytical work. |")
    w("| [`Workflow/Catalogue/wa-obs-catalogue-tiered-v2-20260511.md`](../../../Workflow/Catalogue/wa-obs-catalogue-tiered-v2-20260511.md) | The 189-prompt T0–T7 catalogue. Phase 8 applies each prompt to each sub-group. |")
    w("| [`Sessions/Session_Clusters/M15/m15-baseline-verses-v17-20260511.json`](m15-baseline-verses-v17-20260511.json) | Per-verse JSON state, including verse text + meaning + new_vcg + new_subgroup + set-aside reasons (for AI re-derivation if needed). |")
    w("| _obslog_ | Phase 7 obslog (carried forward; new obslog opens for Phase 8 per the Session Startup Rule). |")
    w("")
    w("## 6. Phase 8 method — short reminder")
    w("")
    w("Per cluster instruction §11:")
    w("")
    w("1. Apply each of the 189 T0–T7 prompts to each of the 8 inner-being sub-groups (A–H). BOUNDARY receives the structural-characterisation note pattern only (per §11).")
    w("2. Use outcome codes E (Evidenced — must name a specific verse), S (Silent — finding in itself), G (Gap — answer requires CC query / external resource).")
    w("3. Apply the fluency guard at every E response: not 'does this sound right?' but 'which verse evidences this?' If no verse can be named, code as S or G.")
    w("4. Apply the cross-cluster contamination guard: each cluster's verses are the sole authority for its findings.")
    w("5. Sub-group completion gate: confirm all 189 prompts have E/S/G for one sub-group before starting the next.")
    w("6. BOUNDARY characterisation note → T1.2.1 (kind of inner-being phenomenon).")
    w("7. Cross-sub-group review pass at the end — surfaces findings only visible across all sub-groups.")
    w("")
    w("**Output:** four-part consolidated findings document:")
    w("- `WA-M15-consolidated-findings-v1-{date}-part1.md` (T0–T1)")
    w("- `WA-M15-consolidated-findings-v1-{date}-part2-T2.md`")
    w("- `WA-M15-consolidated-findings-v1-{date}-part3-T3-T4.md`")
    w("- `WA-M15-consolidated-findings-v1-{date}-part4-T5-T7.md`")
    w("")
    w("**Phase 8 produces no DB writes.** Phase 9 records findings into `cluster_finding` via a separate directive.")
    w("")
    w("---")
    w("")
    w("_Phase 7 closed. M15 is data-clean and analytically ready. Phase 8 may begin when the obslog is opened and the source files are loaded._")
    w("")

    text = "\n".join(out) + "\n"
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Written: {OUT_PATH}")
    print(f"  size: {os.path.getsize(OUT_PATH):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
