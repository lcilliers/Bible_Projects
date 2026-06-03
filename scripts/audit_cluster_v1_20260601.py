"""Consolidated, reusable cluster auditor (read-only).

Implements the aspect spec in Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md,
synthesised from the proven two-condition gate (_validate_analysis_complete_v1),
the gate design (§3), v3_0 §10 Phase F, the coverage/all-clusters audits, and this
session's incremental-update registers.

Sections per cluster:
  A. Analysis-Complete gate (two-condition contract)  [GATE / INFO]
  B. Structural / phase completeness (v3_0 §10)        [GATE(C present) / STRUCT / INFO]
  C. Data-substrate prerequisites                      [STRUCT / INFO]
  D. Incremental-update inputs (re-submit/clear)       [INCR]

Verdict = FAIL if any GATE aspect fails. Produces per-cluster detail, a
cross-cluster summary, and a consolidated incremental worklist. NEVER writes.

Usage:
  python scripts/audit_cluster_v1_20260601.py                 # all in-progress clusters
  python scripts/audit_cluster_v1_20260601.py --cluster M04   # one cluster
  python scripts/audit_cluster_v1_20260601.py --status "Analysis - In Progress"
"""
import argparse
import glob
import json
import os
import re
import sqlite3

DB = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("outputs", "markdown")
GATING_FLAGS = ("SD_POINTER", "SB_FINDING", "PH2_CROSS_REGISTRY_REQUIRED", "PH2_DATA_SPLIT_REQUIRED",
                "PH2_EXEGETICAL_STUDY_REQUIRED", "PH2_THEOLOGICAL_DEPTH_REQUIRED",
                "PH2_ESCHATOLOGICAL_STUDY_REQUIRED", "PH2_DATA_ERROR")
ACTIONABLE_OBS = ("CROSS_CLUSTER_HANDOFF", "SELF_CHECK_OBSERVATION")
OLD_VCG_RE = re.compile(r"^\d+-\d+")
TSUB = "(SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0)"
# Exclude verse_context rows whose verse-record is soft-deleted — these are unreachable by
# Pass A and must not be counted as backfill gaps (dedup-ghost guard, 2026-06-02).
VRACT = " AND verse_record_id IN (SELECT id FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0)"


def conn():
    c = sqlite3.connect(DB, timeout=30); c.row_factory = sqlite3.Row
    return c


def cap(lines, n=12):
    return lines[:n] + ([f"... (+{len(lines)-n} more)"] if len(lines) > n else [])


def render_dispositions(code):
    """Render the corrective-action WORKINGS from the cluster's disposition record(s)
    (wa-cluster-{CODE}-*disposition*.json), so the evaluation reasoning for each
    pointer / boundary / finding decision appears IN the audit report."""
    cdir = os.path.join("Sessions", "Session_Clusters", code)
    files = sorted(glob.glob(os.path.join(cdir, f"wa-cluster-{code}-*disposition*.json")))
    if not files:
        return ["### Corrective actions — dispositions & workings", "",
                "_None recorded yet (no `wa-cluster-{code}-*disposition*.json` in the cluster folder)._".replace("{code}", code), ""]
    out = ["### Corrective actions — dispositions & workings", ""]
    for fp in files:
        try:
            d = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            out.append(f"- (could not read {os.path.basename(fp)}: {e})")
            continue
        out += [f"_source: `{os.path.basename(fp)}` — {d.get('method', '')}_", "",
                "| Item | Action | Evaluation (workings) | Reason |", "|---|---|---|---|"]
        for it in d.get("dispositions", []):
            ev = str(it.get("evaluation", "")).replace("|", "\\|").replace("\n", " ")
            rs = str(it.get("reason", "")).replace("|", "\\|").replace("\n", " ")
            out.append(f"| {it.get('table','')} id={it.get('id','')} ({it.get('type','')}) | **{it.get('action','')}** | {ev} | {rs} |")
        out.append("")
    return out


def audit_cluster(c, code):
    cur = c.cursor()
    R = []  # (id, name, section, severity, status, count, detail)

    def add(aid, name, section, sev, ok, count, detail):
        if ok:
            st = "PASS"
        elif sev == "INCR":
            st = "—"
        elif sev == "INFO":
            st = "REVIEW"   # surfaced (non-gating) — never a silent FAIL
        else:
            st = "FAIL"
        R.append({"id": aid, "name": name, "section": section, "sev": sev,
                  "status": st, "count": count, "detail": detail})

    def q1(sql, p=()):
        try:
            return cur.execute(sql, p).fetchone()[0]
        except Exception as e:
            return f"ERR:{e}"

    # cluster term ids + registries + subgroups
    term_ids = [r["id"] for r in cur.execute("SELECT id FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (code,))]
    regs = [r["owning_registry_fk"] for r in cur.execute("SELECT DISTINCT owning_registry_fk FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND owning_registry_fk IS NOT NULL", (code,))]
    subg = [r["id"] for r in cur.execute("SELECT id FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (code,))]
    chars = cur.execute("SELECT id, COALESCE(short_name,'') sn FROM characteristic WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (code,)).fetchall()
    tph = ",".join("?" * len(term_ids)) or "NULL"
    sph = ",".join("?" * len(subg)) or "NULL"

    # ---------- A. Analysis-Complete gate ----------
    nf = q1("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (code,))
    add("A1", "findings present", "A", "GATE", isinstance(nf, int) and nf > 0, nf, [f"{nf} active cluster_finding rows"])

    gaps = cur.execute("SELECT id FROM cluster_finding WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND finding_status='cluster_synthesis' AND (finding_text LIKE '%gap%' OR finding_text LIKE '%could not%' OR finding_text LIKE '%unable to%')", (code,)).fetchall()
    add("A2", "nonsense/gap synthesis rows", "A", "INFO", not gaps, len(gaps), cap([f"id={r['id']}" for r in gaps]))

    chars_no_find = cur.execute("SELECT ch.id id, COALESCE(ch.short_name,'') sn FROM characteristic ch WHERE ch.cluster_code=? AND COALESCE(ch.delete_flagged,0)=0 AND NOT EXISTS (SELECT 1 FROM cluster_finding cf WHERE cf.characteristic_id=ch.id AND COALESCE(cf.delete_flagged,0)=0)", (code,)).fetchall()
    add("A3", "every characteristic has findings", "A", "GATE", not chars_no_find, len(chars_no_find),
        cap([f"char {r['id']} '{r['sn']}' has 0 findings" for r in chars_no_find]) or [f"{len(chars)} characteristics all have findings"])

    bsg = cur.execute("SELECT id, label FROM cluster_subgroup WHERE cluster_code=? AND subgroup_code='BOUNDARY' AND COALESCE(delete_flagged,0)=0", (code,)).fetchone()
    if bsg:
        bv = q1("SELECT COUNT(*) FROM verse_context WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0", (bsg["id"],))
        bt = q1("SELECT COUNT(*) FROM mti_term_subgroup WHERE cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0", (bsg["id"],))
        add("A4", "BOUNDARY sub-group empty", "A", "GATE", (bv == 0 and bt == 0), (bv or 0) + (bt or 0), [f"BOUNDARY '{bsg['label']}': {bv} verses, {bt} terms"])
    else:
        add("A4", "BOUNDARY sub-group empty", "A", "GATE", True, 0, ["no BOUNDARY sub-group"])

    bpf = cur.execute("SELECT id, flag_label FROM wa_session_research_flags WHERE flag_code='BOUNDARY_DECISION_PENDING' AND COALESCE(resolved,0)=0 AND (flag_label LIKE ? OR description LIKE ?)", (code + "%", code + "%")).fetchall()
    add("A5", "BOUNDARY_DECISION_PENDING resolved", "A", "GATE", not bpf, len(bpf), cap([f"id={r['id']} {r['flag_label']}" for r in bpf]))

    if regs:
        rph = ",".join("?" * len(regs)); fph = ",".join("?" * len(GATING_FLAGS))
        gf = cur.execute(f"SELECT flag_code, COUNT(*) n FROM wa_session_research_flags WHERE COALESCE(resolved,0)=0 AND flag_code IN ({fph}) AND registry_id IN ({rph}) GROUP BY flag_code ORDER BY n DESC", (*GATING_FLAGS, *regs)).fetchall()
        tot = sum(r["n"] for r in gf)
        add("A6", "gating flags resolved (registry→cluster, non-excl)", "A", "GATE", tot == 0, tot, [f"{r['flag_code']}: {r['n']}" for r in gf] or ["none"])
    else:
        add("A6", "gating flags resolved", "A", "GATE", True, 0, ["no registries mapped"])

    stray = q1(f"SELECT COUNT(DISTINCT sbf.id) FROM wa_session_b_findings sbf JOIN mti_terms mt ON mt.owning_registry_fk=sbf.registry_id AND COALESCE(mt.delete_flagged,0)=0 JOIN mti_term_subgroup mts ON mts.mti_term_id=mt.id AND COALESCE(mts.delete_flagged,0)=0 JOIN cluster_subgroup cs ON cs.id=mts.cluster_subgroup_id WHERE cs.cluster_code=? AND sbf.status IN ('pending','open')", (code,))
    add("A7", "no stray Session-B findings", "A", "GATE", stray == 0, stray, [f"{stray} pending/open SB findings (term→sub-group)"])

    fph2 = ",".join("?" * len(ACTIONABLE_OBS))
    aobs = cur.execute(f"SELECT id, observation_type ot, status FROM cluster_observation WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND observation_type IN ({fph2}) AND COALESCE(status,'')!='confirmed'", (code, *ACTIONABLE_OBS)).fetchall()
    add("A8", "actionable observations confirmed", "A", "GATE", not aobs, len(aobs), cap([f"id={r['id']} {r['ot']} [{r['status']}]" for r in aobs]))

    orph = q1("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND finding_status!='cluster_synthesis' AND characteristic_id IS NULL AND cluster_subgroup_id IS NULL", (code,))
    add("A9", "no orphan findings", "A", "INFO", orph == 0, orph, [f"{orph} dangling findings"])

    # A10: no open Session-D-directed observations may stand at completion (Session D is moot;
    # every pointer/observation closes as finding|resolved|confirmed|set-aside — researcher 2026-06-02).
    opend = cur.execute("SELECT id, title FROM cluster_observation WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND target_phase IN ('D','Session_D','Session D') AND COALESCE(status,'')!='confirmed'", (code,)).fetchall()
    add("A10", "no open Session-D observations (Session D moot)", "A", "GATE", not opend, len(opend),
        cap([f"id={r['id']} {r['title']}" for r in opend]))

    # ---------- B. Structural / phase completeness ----------
    rel = q1("SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN " + TSUB + " AND is_relevant=1 AND COALESCE(delete_flagged,0)=0" + VRACT, (code,))
    relv = rel if isinstance(rel, int) else 0
    note = q1("SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN " + TSUB + " AND is_relevant=1 AND COALESCE(delete_flagged,0)=0" + VRACT + " AND analysis_note IS NOT NULL AND TRIM(analysis_note)<>''", (code,))
    kw = q1("SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN " + TSUB + " AND is_relevant=1 AND COALESCE(delete_flagged,0)=0" + VRACT + " AND keywords IS NOT NULL AND TRIM(keywords)<>''", (code,))
    add("B1a", "Phase A: verse MEANINGS on every is_relevant (mandatory)", "B", "GATE", relv > 0 and note == relv, (relv - note) if isinstance(note, int) else relv, [f"{note}/{relv} is_relevant verses have analysis_note"])
    add("B1b", "Phase A: KEYWORDS on every is_relevant (mandatory cross-cluster)", "B", "GATE", relv > 0 and kw == relv, (relv - kw) if isinstance(kw, int) else relv, [f"{kw}/{relv} is_relevant verses have keywords"])
    rel_grp = q1("SELECT COUNT(*) FROM verse_context WHERE mti_term_id IN " + TSUB + " AND is_relevant=1 AND COALESCE(delete_flagged,0)=0" + VRACT + " AND cluster_subgroup_id IS NOT NULL AND group_id IS NOT NULL", (code,))
    add("B2", "Phase B: is_relevant verses grouped (subgroup+group)", "B", "STRUCT", relv > 0 and rel_grp == relv, (relv - rel_grp) if isinstance(rel_grp, int) else relv, [f"{rel_grp}/{relv} grouped"])

    # B3 characteristics-table completeness: chars present + char-subgroup links + every non-BOUNDARY sub-group linked
    cs_links = q1("SELECT COUNT(*) FROM characteristic_subgroup cs JOIN characteristic ch ON ch.id=cs.characteristic_id WHERE ch.cluster_code=? AND COALESCE(cs.delete_flagged,0)=0", (code,))
    sg_total = q1("SELECT COUNT(*) FROM cluster_subgroup WHERE cluster_code=? AND subgroup_code!='BOUNDARY' AND COALESCE(delete_flagged,0)=0", (code,))
    sg_linked = q1("SELECT COUNT(DISTINCT cs.id) FROM cluster_subgroup cs JOIN characteristic_subgroup chs ON chs.cluster_subgroup_id=cs.id AND COALESCE(chs.delete_flagged,0)=0 WHERE cs.cluster_code=? AND cs.subgroup_code!='BOUNDARY' AND COALESCE(cs.delete_flagged,0)=0", (code,))
    sg_unlinked = (sg_total - sg_linked) if (isinstance(sg_total, int) and isinstance(sg_linked, int)) else 0
    add("B3", "characteristics table complete (chars + every sub-group linked)", "B", "GATE", len(chars) > 0 and isinstance(cs_links, int) and cs_links > 0 and sg_unlinked == 0, sg_unlinked, [f"{len(chars)} characteristics, {cs_links} char-subgroup links; {sg_linked}/{sg_total} non-BOUNDARY sub-groups linked"])

    fc = cur.execute("SELECT ch.id, COALESCE(ch.short_name,'') sn, COUNT(cf.id) n FROM characteristic ch LEFT JOIN cluster_finding cf ON cf.characteristic_id=ch.id AND COALESCE(cf.delete_flagged,0)=0 WHERE ch.cluster_code=? GROUP BY ch.id", (code,)).fetchall()
    add("B4", "Phase D: findings per characteristic", "B", "INFO", True, len(fc), cap([f"char {r['id']} '{r['sn']}': {r['n']}" for r in fc]))

    vcg_no_anchor = q1("SELECT COUNT(*) FROM (SELECT DISTINCT vc.group_id g FROM verse_context vc JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id WHERE cs.cluster_code=? AND vc.group_id IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0) x WHERE NOT EXISTS (SELECT 1 FROM verse_context a WHERE a.group_id=x.g AND a.is_anchor=1 AND COALESCE(a.delete_flagged,0)=0)", (code,))
    add("B5", "every active VCG has an anchor verse", "B", "GATE", vcg_no_anchor == 0, vcg_no_anchor, [f"{vcg_no_anchor} active VCGs without an anchor"])

    cit = q1("SELECT COUNT(*) FROM finding_citation fc JOIN cluster_finding cf ON cf.id=fc.source_id AND fc.source_table='cluster_finding' WHERE cf.cluster_code=? AND COALESCE(cf.delete_flagged,0)=0", (code,))
    add("B6", "Phase D: citation traceability", "B", "STRUCT", isinstance(cit, int) and cit > 0, cit, [f"{cit} finding_citation rows"])

    anchor_uncov = q1("SELECT COUNT(*) FROM (SELECT DISTINCT (b.abbreviation || ' ' || wvr.chapter || ':' || wvr.verse_num) ref FROM verse_context vc JOIN wa_verse_records wvr ON wvr.id=vc.verse_record_id JOIN books b ON b.id=wvr.book_id JOIN cluster_subgroup cs ON cs.id=vc.cluster_subgroup_id WHERE cs.cluster_code=? AND vc.is_anchor=1 AND COALESCE(vc.delete_flagged,0)=0 AND wvr.book_id IS NOT NULL AND wvr.chapter IS NOT NULL AND wvr.verse_num IS NOT NULL) a WHERE a.ref NOT IN (SELECT fc.citation_value FROM finding_citation fc JOIN cluster_finding cf ON cf.id=fc.source_id AND fc.source_table='cluster_finding' WHERE cf.cluster_code=? AND fc.citation_type='verse' AND COALESCE(cf.delete_flagged,0)=0)", (code, code))
    add("B7", "every anchor verse covered in findings", "B", "GATE", anchor_uncov == 0, anchor_uncov, [f"{anchor_uncov} anchor verses not cited in any finding"])

    # ---------- C. Data-substrate prerequisites ----------
    if term_ids:
        oldvcg = q1("SELECT COUNT(DISTINCT vcg.id) FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id=vcg.id WHERE vc.mti_term_id IN " + TSUB + " AND COALESCE(vc.delete_flagged,0)=0 AND COALESCE(vcg.delete_flagged,0)=0 AND vcg.group_code GLOB '[0-9]*-[0-9]*'", (code,))
        add("C1", "old-format VCGs dissolved", "C", "STRUCT", oldvcg == 0, oldvcg, [f"{oldvcg} active old-format VCGs tied to cluster terms (dissolve at Phase C)"])
        linked = q1("SELECT COUNT(DISTINCT mti_term_id) FROM mti_term_subgroup WHERE mti_term_id IN " + TSUB + " AND COALESCE(delete_flagged,0)=0", (code,))
        add("C2", "term→sub-group linkage present", "C", "STRUCT", isinstance(linked, int) and linked > 0, len(term_ids) - (linked if isinstance(linked, int) else 0), [f"{linked}/{len(term_ids)} live terms linked to a sub-group"])
    else:
        add("C1", "old-format VCGs dissolved", "C", "STRUCT", True, 0, ["no terms"])
        add("C2", "term→sub-group linkage present", "C", "STRUCT", False, 0, ["no terms"])

    # ---------- D. Incremental-update inputs (re-submit/clear) ----------
    if term_ids:
        newterms = q1(f"SELECT COUNT(*) FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 AND id NOT IN (SELECT mti_term_id FROM mti_term_subgroup WHERE COALESCE(delete_flagged,0)=0)", (code,))
        add("D1", "new terms to place (cluster_code set, no sub-group)", "D", "INCR", True, newterms, [f"{newterms} terms to place into a sub-group + analyse"])
    else:
        add("D1", "new terms to place", "D", "INCR", True, 0, [])
    # unallocated pointers routed here
    pf = q1("SELECT COUNT(*) FROM wa_session_b_findings WHERE COALESCE(delete_flag,0)=0 AND cluster_link IS NOT NULL AND (','||cluster_link||',') LIKE ? AND status NOT IN ('routed_cluster','set_aside_non_evidenced','superseded','folded') AND session_c_chapter IS NULL AND id NOT IN (SELECT finding_id FROM wa_finding_catalogue_links WHERE COALESCE(delete_flagged,0)=0)", ('%,' + code + ',%',))
    pfl = q1("SELECT COUNT(*) FROM wa_session_research_flags WHERE flag_code IN ('SD_POINTER','SB_FINDING','SB_INNER_BEING','SD_CLUSTER') AND COALESCE(resolved,0)=0 AND cluster_link IS NOT NULL AND (','||cluster_link||',') LIKE ?", ('%,' + code + ',%',))
    add("D2", "unallocated pointers routed here", "D", "INCR", True, (pf or 0) + (pfl or 0), [f"{pf} findings + {pfl} flags to adopt into findings"])

    hard_fail = [r for r in R if r["sev"] == "GATE" and r["status"] == "FAIL"]
    verdict = "FAIL" if hard_fail else "PASS"
    return verdict, R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default=None)
    ap.add_argument("--status", default="Analysis - In Progress")
    a = ap.parse_args()
    c = conn(); cur = c.cursor()
    if a.cluster:
        clusters = cur.execute("SELECT cluster_code, status FROM cluster WHERE cluster_code=?", (a.cluster,)).fetchall()
    else:
        clusters = cur.execute("SELECT cluster_code, status FROM cluster WHERE status=? ORDER BY cluster_code", (a.status,)).fetchall()

    if a.cluster:
        cdir = os.path.join("Sessions", "Session_Clusters", a.cluster)
        out = os.path.join(cdir if os.path.isdir(cdir) else OUT_DIR, f"wa-cluster-{a.cluster}-audit-v1-20260601.md")
    else:
        out = os.path.join(OUT_DIR, "cluster_audit_v1_20260601.md")
    L = ["# Cluster audit — in-progress clusters", "",
         f"**Generated:** 2026-06-01 (read-only). Spec: `Workflow/methodology/wa-cluster-audit-aspect-spec-v1-20260601.md`. Target status: `{a.status if not a.cluster else a.cluster}` ({len(clusters)} clusters).",
         "GATE failure ⇒ not validly Analysis Complete. STRUCT = structural completeness. INFO = advisory. INCR = re-submit/clear work for the incremental update.", ""]

    summ = []  # (code, verdict, gate_fails, incr_terms, incr_ptrs)
    worklist = []
    for cl in clusters:
        code = cl["cluster_code"]
        verdict, R = audit_cluster(c, code)
        gate_fails = [r for r in R if r["sev"] == "GATE" and r["status"] == "FAIL"]
        struct_fails = [r for r in R if r["sev"] == "STRUCT" and r["status"] == "FAIL"]
        review_items = [r for r in R if r["sev"] == "INFO" and r["status"] == "REVIEW"]
        d1 = next((r for r in R if r["id"] == "D1"), None)
        d2 = next((r for r in R if r["id"] == "D2"), None)
        summ.append((code, verdict, len(gate_fails), d1["count"] if d1 else 0, d2["count"] if d2 else 0))
        # every detected issue surfaces — gate-blocking, structural, or advisory-review; nothing fails silently
        parts = []
        if gate_fails:
            parts.append(f"**{len(gate_fails)} GATE-blocking** ({', '.join(r['id'] for r in gate_fails)})")
        if struct_fails:
            parts.append(f"{len(struct_fails)} structural ({', '.join(r['id'] for r in struct_fails)})")
        if review_items:
            parts.append(f"{len(review_items)} advisory-review ({', '.join(r['id'] for r in review_items)})")
        outstanding = "**nothing outstanding**" if not parts else "; ".join(parts)
        L += [f"## {code} — audit verdict **{verdict}**", "",
              f"- **Cluster status (DB):** `{cl['status']}`",
              f"- **Outstanding:** {outstanding}", "",
              "| ID | Aspect | Sec | Sev | Status | Count | Detail |", "|---|---|---|---|---|--:|---|"]
        for r in R:
            det = "<br>".join(str(x).replace("|", "\\|") for x in r["detail"])
            L.append(f"| {r['id']} | {r['name']} | {r['section']} | {r['sev']} | {r['status']} | {r['count']} | {det} |")
        L.append("")
        L += render_dispositions(code)
        # worklist lines
        for r in gate_fails:
            verb = "CLEAR" if r["id"] in ("A4", "A5", "A6", "A7", "A8") else "RE-SUBMIT"
            worklist.append((code, verb, f"{r['id']} {r['name']} ({r['count']})"))
        for r in R:
            if r["sev"] in ("STRUCT",) and r["status"] == "FAIL":
                worklist.append((code, "RE-SUBMIT", f"{r['id']} {r['name']} ({r['count']})"))
            if r["sev"] == "INFO" and r["status"] == "REVIEW":
                worklist.append((code, "REVIEW", f"{r['id']} {r['name']} ({r['count']})"))
            if r["sev"] == "INCR" and isinstance(r["count"], int) and r["count"] > 0:
                worklist.append((code, "RE-SUBMIT" if r["id"] == "D1" else "ADOPT", f"{r['id']} {r['name']} ({r['count']})"))

    # summary table
    L += ["---", "", "## Cross-cluster summary", "",
          "| Cluster | Verdict | GATE fails | New terms (D1) | Unalloc pointers (D2) |", "|---|---|--:|--:|--:|"]
    for code, v, gf, t, p in summ:
        L.append(f"| {code} | {v} | {gf} | {t} | {p} |")
    npass = sum(1 for s in summ if s[1] == "PASS"); nfail = len(summ) - npass
    L += ["", f"**PASS {npass} · FAIL {nfail}** of {len(summ)}.", "",
          "## Consolidated incremental worklist (re-submit / clear / adopt)", "",
          "| Cluster | Action | Item |", "|---|---|---|"]
    for code, verb, item in worklist:
        L.append(f"| {code} | {verb} | {item} |")
    if not worklist:
        L.append("| — | — | (nothing outstanding) |")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"audited {len(summ)} clusters | PASS {npass} FAIL {nfail} | worklist items {len(worklist)}")
    for code, v, gf, t, p in summ:
        print(f"  {code}: {v} (gate_fails={gf}, new_terms={t}, pointers={p})")
    print("report:", out)
    c.close()


if __name__ == "__main__":
    main()
