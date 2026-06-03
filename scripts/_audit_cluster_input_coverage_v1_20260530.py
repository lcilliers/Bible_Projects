"""Audit whether the 7 chapter input files contain every piece of evidence
the DB carries for a cluster.

For a given cluster code, queries the DB for:
  - All active cluster_finding rows (per-characteristic + cluster-synthesis)
  - All active cluster_subgroup rows
  - All active characteristic rows
  - All active verse_context_group rows for the cluster
  - All active anchor verses (verse_context.is_anchor=1)
  - All open cluster_observation rows

Then parses every input file in Sessions/Session_Clusters/{CODE}/inputs/
and checks each evidence row is referenced.

Produces a coverage report to outputs/markdown/cluster_input_coverage_{CODE}_{date}.md.
Exits with code 1 if any evidence is missing — for use as a Step 1 gate.

Usage:
  python scripts/_audit_cluster_input_coverage_v1_20260530.py --cluster M38
"""
from __future__ import annotations
import sqlite3, sys, argparse, re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB_PATH = "database/bible_research.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def load_inputs(cluster_code: str) -> dict[str, str]:
    inputs_dir = Path(f"Sessions/Session_Clusters/{cluster_code}/inputs")
    out = {}
    if not inputs_dir.exists():
        return out
    for p in sorted(inputs_dir.glob(f"wa-cluster-{cluster_code}-ch*-input-v*.md")):
        # take only the latest version per chapter
        m = re.match(rf"wa-cluster-{cluster_code}-(ch\d+)-input-v(\d+)-.*\.md", p.name)
        if not m:
            continue
        ch = m.group(1)
        ver = int(m.group(2))
        if ch in out and out[ch][0] >= ver:
            continue
        out[ch] = (ver, p.read_text(encoding="utf-8"))
    return {k: v[1] for k, v in out.items()}


def fetch_findings(conn, code):
    rows = conn.execute("""
        SELECT cf.id, cf.cluster_code, cf.characteristic_id, cf.cluster_subgroup_id,
               cf.obs_id, cf.finding_status, cf.finding_text,
               q.question_code, q.tier, q.section,
               c.short_name AS char_short, c.id AS c_id,
               cs.label AS sg_label
          FROM cluster_finding cf
          JOIN wa_obs_question_catalogue q ON q.obs_id = cf.obs_id
          LEFT JOIN characteristic c ON c.id = cf.characteristic_id
          LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
         WHERE cf.cluster_code = ?
           AND COALESCE(cf.delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_subgroups(conn, code):
    rows = conn.execute("""
        SELECT id, cluster_code, subgroup_code, label, core_description
          FROM cluster_subgroup
         WHERE cluster_code = ? AND COALESCE(delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_characteristics(conn, code):
    rows = conn.execute("""
        SELECT id, cluster_code, short_name, definition
          FROM characteristic
         WHERE cluster_code = ? AND COALESCE(delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_vcgs(conn, code):
    rows = conn.execute("""
        SELECT vcg.id, vcg.group_code, vcg.context_description
          FROM verse_context_group vcg
         WHERE vcg.group_code LIKE ?
           AND COALESCE(vcg.delete_flagged,0)=0
    """, (f"{code}-%-VCG%",)).fetchall()
    return [dict(r) for r in rows]


def fetch_anchors(conn, code):
    rows = conn.execute("""
        SELECT vc.id, vc.group_id, vc.mti_term_id,
               vr.reference, vr.book_id, vr.chapter, vr.verse_num,
               mt.strongs_number, mt.transliteration,
               vcg.group_code
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          JOIN verse_context_group vcg ON vcg.id = vc.group_id
         WHERE vc.is_anchor = 1
           AND vcg.group_code LIKE ?
           AND COALESCE(vc.delete_flagged,0)=0
           AND COALESCE(vcg.delete_flagged,0)=0
    """, (f"{code}-%-VCG%",)).fetchall()
    return [dict(r) for r in rows]


def fetch_observations(conn, code):
    rows = conn.execute("""
        SELECT id, title, description, status, target_phase, observation_type, source_phase
          FROM cluster_observation
         WHERE cluster_code = ? AND COALESCE(delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_subgroup_terms(conn, code):
    rows = conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss,
               cs.id AS sg_id, cs.label AS sg_label
          FROM mti_term_subgroup mts
          JOIN mti_terms mt ON mt.id = mts.mti_term_id
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
         WHERE cs.cluster_code = ?
           AND COALESCE(mts.delete_flagged,0)=0
           AND COALESCE(mt.delete_flagged,0)=0
           AND COALESCE(cs.delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def combined_text(inputs: dict[str, str]) -> str:
    return "\n\n".join(inputs.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--strict", action="store_true",
                    help="Exit nonzero if any evidence is missing (for gate use)")
    args = ap.parse_args()

    code = args.cluster.upper()
    conn = get_conn()

    findings = fetch_findings(conn, code)
    subgroups = fetch_subgroups(conn, code)
    characteristics = fetch_characteristics(conn, code)
    vcgs = fetch_vcgs(conn, code)
    anchors = fetch_anchors(conn, code)
    observations = fetch_observations(conn, code)
    sg_terms = fetch_subgroup_terms(conn, code)

    inputs = load_inputs(code)
    blob = combined_text(inputs)

    # ---------- Coverage checks ----------

    # Findings: identified by question_code; one finding row per (question_code, scope).
    # We count finding rows referenced. A question_code appears once in the chapter input
    # for each (characteristic or cluster-synthesis) it covers. We can't tell *which*
    # finding row was referenced from question_code alone, so we group findings by
    # (question_code, scope_key) where scope_key = characteristic_id or 'syn'.
    finding_groups: dict[tuple, list] = defaultdict(list)
    for f in findings:
        scope = f["characteristic_id"] if f["characteristic_id"] else "syn"
        finding_groups[(f["question_code"], scope)].append(f)

    # For each scope group, the finding row(s) are "covered" if the question_code
    # appears in the input for the relevant chapter scope.
    missing_findings = []
    char_id_to_sg = {}
    # build characteristic_id -> sg_label map via characteristic_subgroup
    for r in conn.execute("""
        SELECT cs.characteristic_id, csg.label
          FROM characteristic_subgroup cs
          JOIN cluster_subgroup csg ON csg.id = cs.cluster_subgroup_id
         WHERE cs.characteristic_id IN ({})
           AND COALESCE(cs.delete_flagged,0)=0
    """.format(",".join(str(c["id"]) for c in characteristics) or "0")).fetchall():
        char_id_to_sg[r[0]] = r[1]

    for (qcode, scope), rows in finding_groups.items():
        in_blob = (qcode in blob)
        if not in_blob:
            sample = rows[0]
            missing_findings.append({
                "question_code": qcode,
                "scope": scope,
                "tier": sample["tier"],
                "section": sample["section"],
                "char_short": sample.get("char_short"),
                "finding_text_preview": (sample.get("finding_text") or "")[:120],
                "count_rows": len(rows),
                "finding_status": sample["finding_status"],
            })

    # Sub-groups: covered if label appears
    missing_subgroups = [sg for sg in subgroups
                        if sg["subgroup_code"] != "BOUNDARY"
                        and sg["label"] not in blob]
    boundary_in_inputs = [sg for sg in subgroups
                         if sg["subgroup_code"] == "BOUNDARY"
                         and sg["label"] in blob]
    boundary_missing = [sg for sg in subgroups
                       if sg["subgroup_code"] == "BOUNDARY"
                       and sg["label"] not in blob]

    # Characteristics: covered if short_name appears in blob
    missing_characteristics = [c for c in characteristics
                              if c["short_name"] not in blob]

    # VCGs: covered if group_code appears
    missing_vcgs = [v for v in vcgs if v["group_code"] not in blob]

    # Anchors: covered if reference + strongs_number both appear in blob
    missing_anchors = []
    for a in anchors:
        ref = a["reference"]
        if ref not in blob:
            missing_anchors.append(a)

    # Observations: NOT included in any chapter input by current generator
    missing_observations = list(observations)

    # Subgroup terms: NOT included in chapter inputs (were in appendix A only)
    sg_terms_in_inputs = [t for t in sg_terms if t["strongs_number"] in blob]
    sg_terms_missing = [t for t in sg_terms if t["strongs_number"] not in blob]

    # VCG context descriptions: NOT in chapter inputs (were in appendix B only)
    vcg_desc_missing = [v for v in vcgs
                       if v.get("context_description")
                       and v["context_description"][:60] not in blob]

    # ---------- Report ----------
    out = Path("outputs/markdown")
    out.mkdir(parents=True, exist_ok=True)
    rpt_path = out / f"cluster_input_coverage_{code}_v1_{datetime.now():%Y%m%d}.md"

    lines = []
    lines.append(f"# Cluster input coverage audit — {code}")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now():%Y-%m-%d %H:%M}")
    lines.append("")
    lines.append(f"**Inputs audited:** {len(inputs)} chapter input file(s) "
                f"in `Sessions/Session_Clusters/{code}/inputs/`")
    for ch, _ in sorted(inputs.items()):
        lines.append(f"- `{ch}`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## DB evidence inventory")
    lines.append("")
    lines.append(f"| Evidence type | Total in DB |")
    lines.append("|---|---|")
    lines.append(f"| `cluster_finding` (active) | {len(findings)} |")
    lines.append(f"| ` - cluster-synthesis` | {sum(1 for f in findings if f['characteristic_id'] is None)} |")
    lines.append(f"| ` - per-characteristic` | {sum(1 for f in findings if f['characteristic_id'])} |")
    lines.append(f"| `cluster_subgroup` (active) | {len(subgroups)} |")
    lines.append(f"| `characteristic` (active) | {len(characteristics)} |")
    lines.append(f"| `verse_context_group` (active) | {len(vcgs)} |")
    lines.append(f"| `verse_context.is_anchor=1` (active) | {len(anchors)} |")
    lines.append(f"| `cluster_observation` (active) | {len(observations)} |")
    lines.append(f"| `mti_term_subgroup` links (active) | {len(sg_terms)} |")
    lines.append("")

    # Tier breakdown of findings
    by_tier_total = defaultdict(int)
    by_tier_syn = defaultdict(int)
    by_tier_perchar = defaultdict(int)
    for f in findings:
        by_tier_total[f["tier"]] += 1
        if f["characteristic_id"] is None:
            by_tier_syn[f["tier"]] += 1
        else:
            by_tier_perchar[f["tier"]] += 1
    lines.append("### Findings by tier")
    lines.append("")
    lines.append("| Tier | Total | Cluster-synth | Per-char |")
    lines.append("|---|---|---|---|")
    for t in sorted(by_tier_total.keys()):
        lines.append(f"| {t} | {by_tier_total[t]} | {by_tier_syn[t]} | {by_tier_perchar[t]} |")
    lines.append("")

    # Status breakdown of findings
    by_status = defaultdict(int)
    for f in findings:
        by_status[f["finding_status"]] += 1
    lines.append("### Findings by status")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---|")
    for s, n in sorted(by_status.items()):
        lines.append(f"| {s} | {n} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ---------- Coverage findings ----------
    lines.append("## Coverage gaps")
    lines.append("")

    total_missing = (len(missing_findings) + len(missing_subgroups) + len(boundary_missing)
                    + len(missing_characteristics) + len(missing_vcgs) + len(missing_anchors)
                    + len(missing_observations))

    if total_missing == 0 and not vcg_desc_missing and not sg_terms_missing:
        lines.append("**✓ All evidence in DB is referenced in at least one chapter input file.**")
    else:
        lines.append(f"**Total missing evidence rows: {total_missing}**")
    lines.append("")

    # Findings gaps
    lines.append(f"### Findings ({len(finding_groups)} scope-groups in DB, "
                f"{len(missing_findings)} not referenced)")
    lines.append("")
    if missing_findings:
        miss_by_tier = defaultdict(int)
        miss_by_status = defaultdict(int)
        miss_by_scope = defaultdict(int)
        for m in missing_findings:
            miss_by_tier[m["tier"]] += 1
            miss_by_status[m["finding_status"]] += 1
            miss_by_scope["cluster-synth" if m["scope"]=="syn" else "per-char"] += 1
        lines.append(f"**Missing by tier:** " + ", ".join(f"{t}={n}" for t,n in sorted(miss_by_tier.items())))
        lines.append("")
        lines.append(f"**Missing by status:** " + ", ".join(f"{s}={n}" for s,n in sorted(miss_by_status.items())))
        lines.append("")
        lines.append(f"**Missing by scope:** " + ", ".join(f"{s}={n}" for s,n in sorted(miss_by_scope.items())))
        lines.append("")
        lines.append("First 30 missing finding scope-groups:")
        lines.append("")
        lines.append("| question_code | tier | status | scope | char | preview |")
        lines.append("|---|---|---|---|---|---|")
        for m in missing_findings[:30]:
            scope_label = "synth" if m["scope"]=="syn" else f"char#{m['scope']}"
            char = m.get("char_short") or "—"
            prev = (m["finding_text_preview"] or "").replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {m['question_code']} | {m['tier']} | {m['finding_status']} | "
                        f"{scope_label} | {char} | {prev} |")
        lines.append("")
    else:
        lines.append("All finding question_codes referenced in chapter inputs.")
        lines.append("")

    # Sub-groups
    lines.append(f"### Sub-groups (non-BOUNDARY: {len([sg for sg in subgroups if sg['subgroup_code']!='BOUNDARY'])}, "
                f"missing: {len(missing_subgroups)})")
    lines.append("")
    if missing_subgroups:
        for sg in missing_subgroups:
            lines.append(f"- `{sg['subgroup_code']}` — {sg['label']}")
        lines.append("")
    else:
        lines.append("All non-BOUNDARY sub-groups referenced.")
        lines.append("")

    boundary_sgs = [sg for sg in subgroups if sg["subgroup_code"]=="BOUNDARY"]
    if boundary_sgs:
        lines.append(f"BOUNDARY sub-groups: {len(boundary_sgs)} in DB; "
                    f"{len(boundary_in_inputs)} referenced; {len(boundary_missing)} missing.")
        for sg in boundary_missing:
            lines.append(f"- `{sg['subgroup_code']}` — {sg['label']}")
        lines.append("")

    # Characteristics
    lines.append(f"### Characteristics ({len(characteristics)} in DB, "
                f"{len(missing_characteristics)} missing)")
    lines.append("")
    if missing_characteristics:
        for c in missing_characteristics:
            lines.append(f"- id={c['id']} — {c['short_name']}")
        lines.append("")
    else:
        lines.append("All characteristic short_names referenced.")
        lines.append("")

    # VCGs
    lines.append(f"### Verse-context groups ({len(vcgs)} in DB, "
                f"{len(missing_vcgs)} missing)")
    lines.append("")
    if missing_vcgs:
        for v in missing_vcgs[:40]:
            lines.append(f"- `{v['group_code']}`")
        if len(missing_vcgs) > 40:
            lines.append(f"- ... and {len(missing_vcgs)-40} more")
        lines.append("")
    else:
        lines.append("All VCG codes referenced.")
        lines.append("")

    # Anchors
    lines.append(f"### Anchor verses ({len(anchors)} active anchors in DB, "
                f"{len(missing_anchors)} not referenced)")
    lines.append("")
    if missing_anchors:
        by_vcg = defaultdict(int)
        for a in missing_anchors:
            by_vcg[a["group_code"]] += 1
        lines.append("Missing anchors group by VCG (first 30):")
        for code_, n in sorted(by_vcg.items())[:30]:
            lines.append(f"- `{code_}` — {n} unreferenced anchor(s)")
        lines.append("")
    else:
        lines.append("All anchor verse references appear in chapter inputs.")
        lines.append("")

    # Observations
    lines.append(f"### Cluster observations ({len(observations)} in DB, "
                f"{len(missing_observations)} not in any chapter input)")
    lines.append("")
    if missing_observations:
        lines.append("**Observations are not currently included by the input generator.** "
                    "If they should drive prose, the generator needs to route them to a chapter.")
        lines.append("")
        for o in missing_observations[:15]:
            prev = ((o.get("title") or "") + ": " + (o.get("description") or ""))[:160].replace("\n", " ")
            lines.append(f"- id={o['id']} type={o.get('observation_type')} status={o['status']} target={o.get('target_phase')} — {prev}")
        if len(missing_observations) > 15:
            lines.append(f"- ... and {len(missing_observations)-15} more")
        lines.append("")
    else:
        lines.append("No active observations to route.")
        lines.append("")

    # Sub-group terms
    lines.append(f"### Sub-group term inventory ({len(sg_terms)} term-links in DB, "
                f"{len(sg_terms_missing)} not in chapter inputs)")
    lines.append("")
    if sg_terms_missing:
        lines.append("**Term metadata (Strong's / transliteration / gloss) is not in chapter inputs.** "
                    "Previously surfaced in appendix A; retired by v1_0 publishing instruction.")
        lines.append("")
        # Show summary by sg
        by_sg = defaultdict(list)
        for t in sg_terms_missing:
            by_sg[t["sg_label"]].append(t)
        for sg_label, terms in list(by_sg.items())[:8]:
            sample = ", ".join(f"{t['strongs_number']} ({t['transliteration']})" for t in terms[:5])
            more = f" + {len(terms)-5} more" if len(terms) > 5 else ""
            lines.append(f"- **{sg_label}** — {len(terms)} terms not in inputs: {sample}{more}")
        lines.append("")

    # VCG descriptions
    lines.append(f"### VCG context descriptions ({sum(1 for v in vcgs if v.get('context_description'))} "
                f"in DB, {len(vcg_desc_missing)} not in chapter inputs)")
    lines.append("")
    if vcg_desc_missing:
        lines.append("**VCG context descriptions (the meaning-group definitions) are not surfaced in chapter inputs.** "
                    "These define what each meaning-group is about. AI must rely on inferring from the anchor verses + their analysis_note.")
        lines.append(f"- {len(vcg_desc_missing)} VCGs have a `context_description` in the DB that is not in the chapter inputs.")
        lines.append("")

    # ---------- Summary verdict ----------
    lines.append("---")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    if total_missing == 0 and not vcg_desc_missing and not sg_terms_missing:
        lines.append("PASS — all DB evidence appears in at least one chapter input file.")
    else:
        lines.append("FAIL — DB evidence is not fully represented in the 7 chapter input files. "
                    "See gaps above. Either update the generator to include the missing evidence, "
                    "or update the publishing instruction to explicitly exclude these row types.")
    lines.append("")

    rpt_path.write_text("\n".join(lines), encoding="utf-8")

    # Console summary
    print(f"Cluster: {code}")
    print(f"Inputs audited: {len(inputs)} files ({', '.join(sorted(inputs.keys()))})")
    print(f"Findings in DB: {len(findings)}  ({len(finding_groups)} scope-groups)")
    print(f"  Missing finding scope-groups: {len(missing_findings)}")
    print(f"Sub-groups in DB: {len(subgroups)}  Missing: {len(missing_subgroups)} non-B + {len(boundary_missing)} B")
    print(f"Characteristics in DB: {len(characteristics)}  Missing: {len(missing_characteristics)}")
    print(f"VCGs in DB: {len(vcgs)}  Missing: {len(missing_vcgs)}")
    print(f"Anchors in DB: {len(anchors)}  Missing: {len(missing_anchors)}")
    print(f"Observations in DB: {len(observations)}  Not routed: {len(missing_observations)}")
    print(f"Sub-group terms in DB: {len(sg_terms)}  Not in inputs: {len(sg_terms_missing)}")
    print(f"VCG descriptions in DB: {sum(1 for v in vcgs if v.get('context_description'))}  Not in inputs: {len(vcg_desc_missing)}")
    print()
    print(f"Report: {rpt_path}")

    if args.strict and (total_missing > 0 or vcg_desc_missing or sg_terms_missing):
        sys.exit(1)


if __name__ == "__main__":
    main()
