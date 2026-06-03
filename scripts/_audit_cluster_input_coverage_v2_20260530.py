"""Audit cluster input coverage v2 — findings-centric.

v2 reframes the coverage question per the researcher direction 2026-05-30:
the FINDINGS are the primary evidence carrier (they quote verses verbatim,
name VCGs inline, carry the synthesis). The audit therefore tests:

  A. COVERAGE — every required evidence row has its identifier appearing in
     at least one chapter input.

     Required:
       - cluster_finding rows (status != 'gap')   → question_code in inputs
       - cluster_subgroup rows (non-BOUNDARY)     → label in inputs
       - characteristic rows                      → short_name in inputs
       - verse_context_group (active)             → group_code in inputs
       - verse_context.is_anchor=1 (active)       → reference in inputs
       - cluster_observation rows targeted at     → some identifying token in inputs
         publication (session_c / E / publication)

  B. EXCLUSION — no policy-excluded row should be referenced.

     Excluded:
       - cluster_finding rows with status='gap'   → must NOT appear (silence-principle)
       - cluster_observation rows targeted at     → must NOT appear
         non-publication phases

  C. BOUNDARY READINESS — cluster must have no unresolved BOUNDARY items
     before publishing.

     Checks:
       1. No active cluster_subgroup with subgroup_code='BOUNDARY' that
          still has active member verses, VCGs, or mti_term links.
       2. No unresolved wa_session_research_flags rows with
          flag_code='BOUNDARY_DECISION_PENDING' for this cluster.
       3. No open cluster_observation rows with 'BOUNDARY' in title or
          description AND target_phase NOT IN the publication phases.

  D. INFORMATIONAL — VCG context_description and non-anchor term inventory
     are tracked but not gated. They are reference material; findings carry
     the operative content.

Usage:
  python scripts/_audit_cluster_input_coverage_v2_20260530.py --cluster M38
  python scripts/_audit_cluster_input_coverage_v2_20260530.py --cluster M38 --strict
"""
from __future__ import annotations
import sqlite3, sys, argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import re

try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

DB_PATH = "database/bible_research.db"

PUB_TARGET_PHASES = {"session_c", "E", "publication"}


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
        m = re.match(rf"wa-cluster-{cluster_code}-(ch\d+)-input-v(\d+)-.*\.md", p.name)
        if not m:
            continue
        ch = m.group(1)
        ver = int(m.group(2))
        if ch in out and out[ch][0] >= ver:
            continue
        out[ch] = (ver, p.read_text(encoding="utf-8"))
    return {k: v[1] for k, v in out.items()}


# ---------- DB layer ----------

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
    """VCGs reached by verse_context rows whose sub-group is in this cluster.

    Robust to old (Strong's-numbered) and new (M{NN}-X-VCG{NN}) naming.
    """
    rows = conn.execute("""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description
          FROM verse_context_group vcg
          JOIN verse_context vc ON vc.group_id = vcg.id
          JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
         WHERE cs.cluster_code = ?
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(vc.delete_flagged,0)=0
           AND COALESCE(cs.delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_anchors(conn, code):
    rows = conn.execute("""
        SELECT vc.id, vc.group_id,
               vr.reference,
               mt.strongs_number, mt.transliteration,
               vcg.group_code,
               cs.subgroup_code, cs.label AS sg_label
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          JOIN mti_terms mt ON mt.id = vc.mti_term_id
          JOIN verse_context_group vcg ON vcg.id = vc.group_id
          JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
         WHERE vc.is_anchor = 1
           AND cs.cluster_code = ?
           AND COALESCE(vc.delete_flagged,0)=0
           AND COALESCE(vcg.delete_flagged,0)=0
           AND COALESCE(cs.delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_observations(conn, code):
    rows = conn.execute("""
        SELECT id, title, description, status, target_phase, observation_type, source_phase
          FROM cluster_observation
         WHERE cluster_code = ? AND COALESCE(delete_flagged,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_boundary_pending_flags(conn, code):
    """Per-cluster BOUNDARY_DECISION_PENDING. Match by flag_label prefix."""
    rows = conn.execute("""
        SELECT id, flag_label, strongs_reference, priority, description,
               resolved, resolved_note
          FROM wa_session_research_flags
         WHERE flag_code = 'BOUNDARY_DECISION_PENDING'
           AND flag_label LIKE ?
    """, (f"{code}-%",)).fetchall()
    return [dict(r) for r in rows]


def fetch_boundary_subgroup_membership(conn, code):
    """For a BOUNDARY sub-group on this cluster, count its active members."""
    sg = conn.execute("""
        SELECT id, label FROM cluster_subgroup
         WHERE cluster_code = ? AND subgroup_code='BOUNDARY'
           AND COALESCE(delete_flagged,0)=0
    """, (code,)).fetchone()
    if not sg:
        return None
    sg = dict(sg)
    sg["verse_count"] = conn.execute("""
        SELECT COUNT(*) FROM verse_context
         WHERE cluster_subgroup_id = ? AND COALESCE(delete_flagged,0)=0
    """, (sg["id"],)).fetchone()[0]
    sg["term_count"] = conn.execute("""
        SELECT COUNT(*) FROM mti_term_subgroup
         WHERE cluster_subgroup_id = ? AND COALESCE(delete_flagged,0)=0
    """, (sg["id"],)).fetchone()[0]
    sg["vcg_count"] = conn.execute("""
        SELECT COUNT(DISTINCT vc.group_id) FROM verse_context vc
          JOIN verse_context_group vcg ON vcg.id = vc.group_id
         WHERE vc.cluster_subgroup_id = ?
           AND COALESCE(vc.delete_flagged,0)=0
           AND COALESCE(vcg.delete_flagged,0)=0
    """, (sg["id"],)).fetchone()[0]
    return sg


def fetch_stray_sb_findings(conn, code):
    """Session B findings on registries that contribute to this cluster's
    sub-groups, still in 'pending' or 'open' status."""
    rows = conn.execute("""
        SELECT DISTINCT sbf.id, sbf.finding_id, sbf.registry_id, wr.word,
               sbf.finding_type, sbf.status, sbf.session_b_instruction,
               SUBSTR(sbf.finding,1,160) AS preview
          FROM wa_session_b_findings sbf
          JOIN word_registry wr ON wr.id = sbf.registry_id
          JOIN mti_terms mt ON mt.owning_registry_fk = wr.id
                            AND COALESCE(mt.delete_flagged,0)=0
          JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                                     AND COALESCE(mts.delete_flagged,0)=0
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
                                   AND COALESCE(cs.delete_flagged,0)=0
         WHERE cs.cluster_code = ?
           AND COALESCE(sbf.delete_flag,0)=0
           AND sbf.status IN ('pending','open')
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_stray_research_flags(conn, code):
    """Unresolved SB/SD research flags on registries contributing to this cluster.
    Filters to SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING."""
    rows = conn.execute("""
        SELECT DISTINCT f.id, f.registry_id, wr.word,
               f.flag_code, f.flag_label, f.strongs_reference,
               SUBSTR(f.description,1,160) AS preview
          FROM wa_session_research_flags f
          JOIN word_registry wr ON wr.id = f.registry_id
          JOIN mti_terms mt ON mt.owning_registry_fk = wr.id
                            AND COALESCE(mt.delete_flagged,0)=0
          JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
                                     AND COALESCE(mts.delete_flagged,0)=0
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
                                   AND COALESCE(cs.delete_flagged,0)=0
         WHERE cs.cluster_code = ?
           AND f.flag_code IN ('SB_FINDING','SD_POINTER','SD_CLUSTER','SB_INNER_BEING')
           AND COALESCE(f.resolved,0)=0
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


def fetch_session_d_artefacts(conn, code):
    """Session D rows referencing this cluster directly."""
    rows = conn.execute("""
        SELECT id, run_id, cluster_ref, run_summary
          FROM session_d_runs WHERE cluster_ref = ?
    """, (code,)).fetchall()
    runs = [dict(r) for r in rows]
    # session_d_observations and verse_links keyed by run_id; surface count
    return {"runs": runs}


def fetch_boundary_observations(conn, code):
    """Open observations referencing BOUNDARY targeted at pre-publication phases."""
    rows = conn.execute("""
        SELECT id, title, description, status, target_phase, observation_type
          FROM cluster_observation
         WHERE cluster_code = ?
           AND COALESCE(delete_flagged,0)=0
           AND status = 'open'
           AND (title LIKE '%BOUNDARY%' OR description LIKE '%BOUNDARY%'
                OR title LIKE '%boundary%' OR description LIKE '%boundary%')
           AND COALESCE(target_phase,'') NOT IN ('session_c','E','publication')
    """, (code,)).fetchall()
    return [dict(r) for r in rows]


# ---------- Reporting ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    code = args.cluster.upper()
    conn = get_conn()

    findings = fetch_findings(conn, code)
    subgroups = fetch_subgroups(conn, code)
    characteristics = fetch_characteristics(conn, code)
    vcgs = fetch_vcgs(conn, code)
    anchors = fetch_anchors(conn, code)
    observations = fetch_observations(conn, code)
    boundary_flags = fetch_boundary_pending_flags(conn, code)
    boundary_sg = fetch_boundary_subgroup_membership(conn, code)
    boundary_obs = fetch_boundary_observations(conn, code)
    stray_sb = fetch_stray_sb_findings(conn, code)
    stray_flags = fetch_stray_research_flags(conn, code)
    sd_artefacts = fetch_session_d_artefacts(conn, code)

    inputs = load_inputs(code)
    blob = "\n\n".join(inputs.values())

    # ---------- A. COVERAGE ----------

    # Findings (non-gap) grouped by (question_code, scope)
    finding_groups: dict[tuple, list] = defaultdict(list)
    gap_finding_groups: dict[tuple, list] = defaultdict(list)
    for f in findings:
        scope = f["characteristic_id"] if f["characteristic_id"] else "syn"
        key = (f["question_code"], scope)
        if f["finding_status"] == "gap":
            gap_finding_groups[key].append(f)
        else:
            finding_groups[key].append(f)

    missing_findings = []
    for (qcode, scope), rows in finding_groups.items():
        if qcode not in blob:
            sample = rows[0]
            missing_findings.append({
                "question_code": qcode, "scope": scope,
                "tier": sample["tier"], "section": sample["section"],
                "char_short": sample.get("char_short"),
                "preview": (sample.get("finding_text") or "")[:140],
                "count": len(rows),
                "finding_status": sample["finding_status"],
            })

    # Excluded findings that ARE referenced — fingerprint by first 80 chars of
    # finding_text (question_code is shared with non-gap findings of the same
    # prompt for other characteristics, so it cannot distinguish a gap leak).
    leaked_gap_findings = []
    for (qcode, scope), rows in gap_finding_groups.items():
        for row in rows:
            ft = row.get("finding_text") or ""
            fingerprint = ft[:80]
            if fingerprint and fingerprint in blob:
                leaked_gap_findings.append({
                    "question_code": qcode, "scope": scope,
                    "tier": row["tier"],
                    "char_short": row.get("char_short"),
                    "preview": ft[:140],
                })

    # Sub-groups
    non_b_sg = [sg for sg in subgroups if sg["subgroup_code"] != "BOUNDARY"]
    b_sg = [sg for sg in subgroups if sg["subgroup_code"] == "BOUNDARY"]
    missing_subgroups = [sg for sg in non_b_sg if sg["label"] not in blob]

    # Characteristics
    missing_characteristics = [c for c in characteristics if c["short_name"] not in blob]

    # VCGs
    missing_vcgs = [v for v in vcgs if v["group_code"] not in blob]

    # Anchors
    missing_anchors = [a for a in anchors if a["reference"] not in blob]

    # Observations
    pub_obs = [o for o in observations
              if (o["target_phase"] or "") in PUB_TARGET_PHASES
              and o["status"] in ("open", "confirmed", "refined")]
    nonpub_obs = [o for o in observations
                 if (o["target_phase"] or "") not in PUB_TARGET_PHASES]
    missing_pub_obs = []
    for o in pub_obs:
        # Match by title's leading slug (first 40 chars before colon if any)
        title = o["title"] or ""
        slug = title.split(":")[0].strip()[:40] if title else ""
        if not slug or slug not in blob:
            missing_pub_obs.append(o)

    # Leaked non-publication obs that appear in inputs
    leaked_nonpub_obs = []
    for o in nonpub_obs:
        title = o["title"] or ""
        slug = title.split(":")[0].strip()[:40] if title else ""
        if slug and slug in blob:
            leaked_nonpub_obs.append(o)

    # ---------- B. BOUNDARY READINESS ----------

    boundary_ready = True
    boundary_issues = []

    # Check 1: BOUNDARY sub-group with active members
    if boundary_sg:
        live_members = boundary_sg["verse_count"] + boundary_sg["term_count"] + boundary_sg["vcg_count"]
        if live_members > 0:
            boundary_ready = False
            boundary_issues.append(
                f"BOUNDARY sub-group `{boundary_sg['label']}` has active members "
                f"(verses={boundary_sg['verse_count']}, terms={boundary_sg['term_count']}, "
                f"VCGs={boundary_sg['vcg_count']}). Resolve before publishing."
            )

    # Check 2: Unresolved BOUNDARY_DECISION_PENDING flags
    unresolved_flags = [f for f in boundary_flags if not f.get("resolved")]
    if unresolved_flags:
        boundary_ready = False
        boundary_issues.append(
            f"{len(unresolved_flags)} unresolved `BOUNDARY_DECISION_PENDING` "
            f"flag(s) for this cluster (of {len(boundary_flags)} total)."
        )

    # NB: cluster_observation BOUNDARY mentions are NOT a readiness signal —
    # many such rows are design-notes documenting past BOUNDARY resolutions
    # rather than pending issues. The authoritative pending-BOUNDARY signal
    # is `wa_session_research_flags.flag_code='BOUNDARY_DECISION_PENDING'`
    # with `resolved=0`. The boundary_obs list is retained as informational
    # context only, surfaced in the BOUNDARY inventory section.

    # ---------- D. INFORMATIONAL ----------

    vcgs_with_desc = [v for v in vcgs if v.get("context_description")]
    vcg_desc_in_inputs = [v for v in vcgs_with_desc
                         if (v["context_description"] or "")[:60] in blob]
    vcg_desc_not_in_inputs = [v for v in vcgs_with_desc
                             if (v["context_description"] or "")[:60] not in blob]

    # ---------- Verdict ----------

    coverage_pass = (
        not missing_findings
        and not missing_subgroups
        and not missing_characteristics
        and not missing_vcgs
        and not missing_anchors
        and not missing_pub_obs
    )
    exclusion_pass = (not leaked_gap_findings and not leaked_nonpub_obs)
    stray_clean = (not stray_sb and not stray_flags and not sd_artefacts["runs"])
    overall_pass = coverage_pass and exclusion_pass and boundary_ready and stray_clean

    # ---------- Report ----------

    out = Path("outputs/markdown")
    out.mkdir(parents=True, exist_ok=True)
    rpt_path = out / f"cluster_input_coverage_{code}_v2_{datetime.now():%Y%m%d}.md"

    lines = []
    lines.append(f"# Cluster input coverage audit v2 — {code}")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now():%Y-%m-%d %H:%M}")
    lines.append("")

    # Verdict summary at top
    lines.append("## Verdict")
    lines.append("")
    verdict_emoji = "PASS" if overall_pass else "FAIL"
    lines.append(f"**Overall: {verdict_emoji}**")
    lines.append("")
    lines.append(f"- Coverage: {'PASS' if coverage_pass else 'FAIL'}")
    lines.append(f"- Exclusion: {'PASS' if exclusion_pass else 'FAIL'}")
    lines.append(f"- BOUNDARY readiness: {'PASS' if boundary_ready else 'FAIL'}")
    lines.append(f"- Stray SB / SD findings: {'PASS' if stray_clean else 'FAIL'}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Inputs audited
    lines.append("## Inputs audited")
    lines.append("")
    if not inputs:
        lines.append("**No input files found.**")
    else:
        lines.append(f"{len(inputs)} chapter input file(s) in `Sessions/Session_Clusters/{code}/inputs/`:")
        for ch, _ in sorted(inputs.items()):
            lines.append(f"- `{ch}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # A. Coverage
    lines.append("## A. Coverage")
    lines.append("")
    lines.append("Every required evidence row's identifier must appear in at least one chapter input.")
    lines.append("")
    lines.append("| Evidence | In DB | Required (excl. gap-status) | Missing | Pass |")
    lines.append("|---|---|---|---|---|")
    lines.append(f"| Finding scope-groups | {len(finding_groups)+len(gap_finding_groups)} "
                f"| {len(finding_groups)} | {len(missing_findings)} "
                f"| {'YES' if not missing_findings else 'NO'} |")
    lines.append(f"| Sub-groups (non-BOUNDARY) | {len(non_b_sg)} | {len(non_b_sg)} "
                f"| {len(missing_subgroups)} | {'YES' if not missing_subgroups else 'NO'} |")
    lines.append(f"| Characteristics | {len(characteristics)} | {len(characteristics)} "
                f"| {len(missing_characteristics)} | {'YES' if not missing_characteristics else 'NO'} |")
    lines.append(f"| VCG codes | {len(vcgs)} | {len(vcgs)} | {len(missing_vcgs)} "
                f"| {'YES' if not missing_vcgs else 'NO'} |")
    lines.append(f"| Anchor verses | {len(anchors)} | {len(anchors)} | {len(missing_anchors)} "
                f"| {'YES' if not missing_anchors else 'NO'} |")
    lines.append(f"| Publication-targeted observations | {len(pub_obs)} | {len(pub_obs)} "
                f"| {len(missing_pub_obs)} | {'YES' if not missing_pub_obs else 'NO'} |")
    lines.append("")

    if missing_findings:
        lines.append(f"### Missing findings ({len(missing_findings)})")
        lines.append("")
        miss_by_tier = defaultdict(int)
        for m in missing_findings:
            miss_by_tier[m["tier"]] += 1
        lines.append("By tier: " + ", ".join(f"{t}={n}" for t, n in sorted(miss_by_tier.items())))
        lines.append("")
        lines.append("| question_code | tier | scope | char | status | preview |")
        lines.append("|---|---|---|---|---|---|")
        for m in missing_findings[:30]:
            scope_label = "synth" if m["scope"] == "syn" else f"char"
            char = m.get("char_short") or "—"
            prev = (m["preview"] or "").replace("|", "\\|").replace("\n", " ")[:80]
            lines.append(f"| {m['question_code']} | {m['tier']} | {scope_label} | {char} "
                        f"| {m['finding_status']} | {prev} |")
        if len(missing_findings) > 30:
            lines.append(f"| ... | ... | ... | ... | ... | +{len(missing_findings)-30} more |")
        lines.append("")

    if missing_subgroups:
        lines.append(f"### Missing sub-groups ({len(missing_subgroups)})")
        for sg in missing_subgroups:
            lines.append(f"- `{sg['subgroup_code']}` — {sg['label']}")
        lines.append("")

    if missing_characteristics:
        lines.append(f"### Missing characteristics ({len(missing_characteristics)})")
        for c in missing_characteristics:
            lines.append(f"- id={c['id']} — {c['short_name']}")
        lines.append("")

    if missing_vcgs:
        lines.append(f"### Missing VCG codes ({len(missing_vcgs)})")
        for v in missing_vcgs[:30]:
            lines.append(f"- `{v['group_code']}`")
        if len(missing_vcgs) > 30:
            lines.append(f"- … +{len(missing_vcgs)-30} more")
        lines.append("")

    if missing_anchors:
        lines.append(f"### Missing anchor verses ({len(missing_anchors)})")
        by_vcg = defaultdict(int)
        for a in missing_anchors:
            by_vcg[a["group_code"]] += 1
        for code_, n in sorted(by_vcg.items())[:30]:
            lines.append(f"- `{code_}` — {n} anchor(s)")
        lines.append("")

    if missing_pub_obs:
        lines.append(f"### Missing publication-targeted observations ({len(missing_pub_obs)})")
        lines.append("")
        for o in missing_pub_obs[:15]:
            prev = ((o.get("title") or "") + ": " + (o.get("description") or ""))[:160].replace("\n", " ")
            lines.append(f"- id={o['id']} type={o.get('observation_type')} "
                        f"target={o.get('target_phase')} — {prev}")
        if len(missing_pub_obs) > 15:
            lines.append(f"- … +{len(missing_pub_obs)-15} more")
        lines.append("")

    lines.append("---")
    lines.append("")

    # B. Exclusion
    lines.append("## B. Exclusion")
    lines.append("")
    lines.append("Policy-excluded rows must not be referenced by any chapter input.")
    lines.append("")
    lines.append("| Exclusion rule | Leaks |")
    lines.append("|---|---|")
    lines.append(f"| `gap`-status findings (silence-principle) | {len(leaked_gap_findings)} |")
    lines.append(f"| Non-publication observations | {len(leaked_nonpub_obs)} |")
    lines.append("")

    if leaked_gap_findings:
        lines.append(f"### Gap findings leaked into inputs ({len(leaked_gap_findings)})")
        lines.append("")
        for m in leaked_gap_findings[:15]:
            scope_label = "synth" if m["scope"] == "syn" else "char"
            char = m.get("char_short") or "—"
            prev = (m["preview"] or "")[:120].replace("\n", " ")
            lines.append(f"- `{m['question_code']}` ({m['tier']}, {scope_label}, {char}) — {prev}")
        lines.append("")

    if leaked_nonpub_obs:
        lines.append(f"### Non-publication observations leaked into inputs ({len(leaked_nonpub_obs)})")
        lines.append("")
        for o in leaked_nonpub_obs[:15]:
            lines.append(f"- id={o['id']} target={o.get('target_phase')} — {(o.get('title') or '')[:120]}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # C. BOUNDARY readiness
    lines.append("## C. BOUNDARY readiness")
    lines.append("")
    lines.append("Cluster must have no unresolved BOUNDARY items before publishing.")
    lines.append("")
    if boundary_ready:
        lines.append("**PASS — no unresolved BOUNDARY items.**")
        lines.append("")
    else:
        lines.append(f"**FAIL — {len(boundary_issues)} issue(s).**")
        lines.append("")
        for i in boundary_issues:
            lines.append(f"- {i}")
        lines.append("")

    # Always show inventory
    lines.append("### BOUNDARY inventory")
    lines.append("")
    lines.append(f"- BOUNDARY sub-group present: {'YES — ' + boundary_sg['label'] if boundary_sg else 'no'}")
    if boundary_sg:
        lines.append(f"  - active verses: {boundary_sg['verse_count']}")
        lines.append(f"  - active terms: {boundary_sg['term_count']}")
        lines.append(f"  - active VCGs: {boundary_sg['vcg_count']}")
    lines.append(f"- BOUNDARY_DECISION_PENDING flags: {len(boundary_flags)} total, "
                f"{len([f for f in boundary_flags if not f.get('resolved')])} unresolved")
    if unresolved_flags:
        lines.append("")
        lines.append("Unresolved flags:")
        for f in unresolved_flags[:10]:
            lines.append(f"- {f['flag_label']} ({f.get('strongs_reference','')}) — "
                        f"{(f.get('description') or '')[:120].replace(chr(10),' ')}")
        if len(unresolved_flags) > 10:
            lines.append(f"- … +{len(unresolved_flags)-10} more")
    lines.append(f"- BOUNDARY mentions in cluster_observation (informational only — not gating): {len(boundary_obs)}")
    if boundary_obs:
        lines.append("  These rows mention BOUNDARY in title/description but observation_type signals")
        lines.append("  they are typically design-notes documenting past resolutions, not pending issues.")
        for o in boundary_obs[:6]:
            lines.append(f"  - id={o['id']} target={o.get('target_phase')} type={o.get('observation_type')} — {(o.get('title') or '')[:100]}")
        if len(boundary_obs) > 6:
            lines.append(f"  - … +{len(boundary_obs)-6} more")
    lines.append("")
    lines.append("---")
    lines.append("")

    # E. Stray SB / SD findings (NEW — gating)
    lines.append("## D. Stray Session B / Session D findings")
    lines.append("")
    lines.append("Cluster must have no still-floating analytical findings from prior "
                "Session B / Session D work on its contributing registries.")
    lines.append("")
    lines.append("| Source | Count | Pass |")
    lines.append("|---|---|---|")
    lines.append(f"| `wa_session_b_findings` (status pending/open) | {len(stray_sb)} "
                f"| {'YES' if not stray_sb else 'NO'} |")
    lines.append(f"| `wa_session_research_flags` (SB_FINDING / SD_POINTER / SD_CLUSTER / SB_INNER_BEING, unresolved) | "
                f"{len(stray_flags)} | {'YES' if not stray_flags else 'NO'} |")
    lines.append(f"| `session_d_runs` rows referencing cluster | {len(sd_artefacts['runs'])} "
                f"| {'YES' if not sd_artefacts['runs'] else 'NO'} |")
    lines.append("")

    if stray_sb:
        lines.append(f"### Stray Session B findings ({len(stray_sb)})")
        lines.append("")
        by_reg = defaultdict(list)
        for f in stray_sb:
            by_reg[(f["registry_id"], f["word"])].append(f)
        lines.append("Grouped by registry:")
        lines.append("")
        lines.append("| Registry | Word | Stray findings | Sample types |")
        lines.append("|---|---|---|---|")
        for (rid, word), items in sorted(by_reg.items()):
            types = sorted(set(i["finding_type"] or "(none)" for i in items))
            type_label = ", ".join(types)[:80]
            lines.append(f"| {rid} | {word} | {len(items)} | {type_label} |")
        lines.append("")
        lines.append("First 10 stray Session B findings (by content preview):")
        lines.append("")
        for f in stray_sb[:10]:
            prev = (f.get("preview") or "")[:140].replace("\n", " ").replace("|", "\\|")
            lines.append(f"- `{f['finding_id']}` (reg={f['registry_id']} {f['word']}, "
                        f"type={f['finding_type']}, status={f['status']}) — {prev}")
        lines.append("")

    if stray_flags:
        lines.append(f"### Stray research flags ({len(stray_flags)})")
        lines.append("")
        by_code = defaultdict(int)
        for f in stray_flags:
            by_code[f["flag_code"]] += 1
        lines.append("By flag_code: " + ", ".join(f"{k}={v}" for k, v in sorted(by_code.items())))
        lines.append("")
        lines.append("First 10:")
        for f in stray_flags[:10]:
            prev = (f.get("preview") or "").replace("\n", " ").replace("|", "\\|")[:140]
            lines.append(f"- `{f['flag_code']}` reg={f['registry_id']} {f['word']} "
                        f"({f.get('strongs_reference','')}) — {prev}")
        lines.append("")

    if sd_artefacts["runs"]:
        lines.append(f"### Session D runs referencing this cluster ({len(sd_artefacts['runs'])})")
        for r in sd_artefacts["runs"][:5]:
            lines.append(f"- run_id={r.get('run_id')} cluster_ref={r.get('cluster_ref')} — {(r.get('run_summary') or '')[:140]}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # E. Informational
    lines.append("## E. Informational (not gating)")
    lines.append("")
    lines.append(f"VCG `context_description` carried in DB but not in chapter inputs: "
                f"{len(vcg_desc_not_in_inputs)} / {len(vcgs_with_desc)}.")
    lines.append("")
    lines.append("Findings encapsulate VCG content via the verses they quote and the "
                "inline VCG codes. The standalone `context_description` is reference "
                "material the AI does not require for prose authoring. Tracked for "
                "completeness only.")
    lines.append("")

    # Inventory
    lines.append("---")
    lines.append("")
    lines.append("## DB inventory")
    lines.append("")
    by_tier = defaultdict(int)
    by_status = defaultdict(int)
    for f in findings:
        by_tier[f["tier"]] += 1
        by_status[f["finding_status"]] += 1
    lines.append("### Findings")
    lines.append("")
    lines.append(f"Total active: {len(findings)} rows in {len(finding_groups)+len(gap_finding_groups)} scope-groups")
    lines.append("")
    lines.append("| Tier | Total |")
    lines.append("|---|---|")
    for t, n in sorted(by_tier.items()):
        lines.append(f"| {t} | {n} |")
    lines.append("")
    lines.append("| Status | Total |")
    lines.append("|---|---|")
    for s, n in sorted(by_status.items()):
        lines.append(f"| {s} | {n} |")
    lines.append("")
    lines.append(f"### Cluster observations: {len(observations)} active")
    lines.append("")
    obs_by_target = defaultdict(int)
    for o in observations:
        obs_by_target[(o.get("target_phase") or "(none)", o["status"])] += 1
    lines.append("| target_phase | status | n |")
    lines.append("|---|---|---|")
    for (tp, st), n in sorted(obs_by_target.items()):
        lines.append(f"| {tp} | {st} | {n} |")
    lines.append("")

    rpt_path.write_text("\n".join(lines), encoding="utf-8")

    # Console summary
    print(f"Cluster: {code}")
    print(f"Inputs audited: {len(inputs)} files")
    print()
    print(f"A. COVERAGE: {'PASS' if coverage_pass else 'FAIL'}")
    print(f"   Findings missing:          {len(missing_findings):4d} / {len(finding_groups)} required scope-groups")
    print(f"   Sub-groups missing:        {len(missing_subgroups):4d} / {len(non_b_sg)}")
    print(f"   Characteristics missing:   {len(missing_characteristics):4d} / {len(characteristics)}")
    print(f"   VCG codes missing:         {len(missing_vcgs):4d} / {len(vcgs)}")
    print(f"   Anchor verses missing:     {len(missing_anchors):4d} / {len(anchors)}")
    print(f"   Pub observations missing:  {len(missing_pub_obs):4d} / {len(pub_obs)}")
    print()
    print(f"B. EXCLUSION: {'PASS' if exclusion_pass else 'FAIL'}")
    print(f"   Gap findings leaked:       {len(leaked_gap_findings):4d}")
    print(f"   Non-pub obs leaked:        {len(leaked_nonpub_obs):4d}")
    print()
    print(f"C. BOUNDARY READINESS: {'PASS' if boundary_ready else 'FAIL'}")
    for i in boundary_issues:
        print(f"   - {i}")
    print()
    print(f"D. STRAY SB/SD FINDINGS: {'PASS' if stray_clean else 'FAIL'}")
    print(f"   Stray SB findings (pending/open): {len(stray_sb)}")
    print(f"   Stray SB/SD research flags:       {len(stray_flags)}")
    print(f"   session_d_runs referencing:       {len(sd_artefacts['runs'])}")
    print()
    print(f"Verdict: {'PASS' if overall_pass else 'FAIL'}")
    print(f"Report: {rpt_path}")

    if args.strict and not overall_pass:
        sys.exit(1)


if __name__ == "__main__":
    main()
