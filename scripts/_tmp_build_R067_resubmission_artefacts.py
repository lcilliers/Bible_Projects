"""_tmp_build_R067_resubmission_artefacts.py

One-shot script to build the v1.8 input artefacts for R067 goodness
resubmission:

  1. Analytic Status .md — revision-session input per v1.8 §1
     (lifecycle summary, prior chapters, anchor analyses, open items)
  2. Validation Report .md — gate-passing audit + WARN list

The data package is generated separately by _tmp_build_word_data_package.py.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join(
    "research", "investigations", "ai_question_test_bundle_20260429", "R067 goodness"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def build_analytic_status(conn: sqlite3.Connection) -> str:
    P: list[str] = []

    P.append("# R067 Goodness — Analytic Status (v1.8 revision-session input)\n")
    P.append(f"**Generated:** {now_iso()}")
    P.append(f"**Source:** SQLite `database/bible_research.db` (schema v3.17.0)")
    P.append(f"**Governing instruction:** [wa-sessionb-analysis-output-v1_8-20260430.md](../../../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md) §1 (revision-session input)\n")
    P.append("**Purpose.** Capture the prior analytical state for R067 goodness so a Stage 2 revision session can resume cleanly under v1.8. Lifecycle summary, resolved Q&As, resolved SD pointers, prior chapters, anchor analyses, and open items.\n")
    P.append("---\n")

    # --- Registry header ---
    reg = conn.execute("SELECT * FROM word_registry WHERE no = 67").fetchone()
    P.append("## 1. Registry header\n")
    P.append("| Field | Value |\n| --- | --- |")
    for k in ("no", "id", "word", "category_hint", "dimensions", "cluster_assignment",
              "phase1_status", "verse_context_status", "session_b_status",
              "dim_review_status", "dim_review_version"):
        P.append(f"| `{k}` | {reg[k]} |")
    P.append("")

    # --- Lifecycle summary ---
    P.append("## 2. Lifecycle summary\n")
    n_findings = conn.execute("SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id=67 AND delete_flag=0").fetchone()[0]
    P.append(f"**Active findings (`wa_session_b_findings`):** {n_findings}\n")

    P.append("**By finding_type:**\n")
    P.append("| finding_type | count |\n| --- | ---: |")
    rows = conn.execute("""
        SELECT finding_type, COUNT(*) AS n
        FROM wa_session_b_findings
        WHERE registry_id=67 AND delete_flag=0
        GROUP BY finding_type ORDER BY n DESC
    """).fetchall()
    for r in rows:
        P.append(f"| {r['finding_type']} | {r['n']} |")
    P.append("")

    P.append("**By status:**\n")
    P.append("| status | count |\n| --- | ---: |")
    rows = conn.execute("""
        SELECT status, COUNT(*) AS n FROM wa_session_b_findings
        WHERE registry_id=67 AND delete_flag=0
        GROUP BY status ORDER BY n DESC
    """).fetchall()
    for r in rows:
        P.append(f"| {r['status']} | {r['n']} |")
    P.append("")

    # --- Open research flags ---
    P.append("## 3. Open research flags (`wa_session_research_flags`)\n")
    rows = conn.execute("""
        SELECT flag_code, COUNT(*) AS n FROM wa_session_research_flags
        WHERE registry_id=(SELECT id FROM word_registry WHERE no=67)
        AND (resolved=0 OR resolved IS NULL)
        GROUP BY flag_code ORDER BY n DESC
    """).fetchall()
    P.append("| flag_code | open count |\n| --- | ---: |")
    for r in rows:
        P.append(f"| {r['flag_code']} | {r['n']} |")
    P.append("")

    # SD pointers list
    P.append("### 3.1 SD pointers (high priority shown; full list in data package §9)\n")
    rows = conn.execute("""
        SELECT flag_label, priority, SUBSTR(description,1,140) AS d
        FROM wa_session_research_flags
        WHERE registry_id=(SELECT id FROM word_registry WHERE no=67)
        AND flag_code='SD_POINTER' AND priority='HIGH'
        AND (resolved=0 OR resolved IS NULL)
        ORDER BY flag_label
    """).fetchall()
    if rows:
        for r in rows:
            P.append(f"- **{r['flag_label']}** ({r['priority']}) — {r['d']}…")
    else:
        P.append("_(no HIGH-priority SD pointers)_")
    P.append("")

    # SB findings
    P.append("### 3.2 Open SB findings (Session B follow-on items)\n")
    rows = conn.execute("""
        SELECT flag_label, priority, SUBSTR(description,1,140) AS d
        FROM wa_session_research_flags
        WHERE registry_id=(SELECT id FROM word_registry WHERE no=67)
        AND flag_code='SB_FINDING'
        AND (resolved=0 OR resolved IS NULL)
        ORDER BY priority, flag_label
    """).fetchall()
    if rows:
        for r in rows[:20]:
            P.append(f"- **{r['flag_label']}** ({r['priority']}) — {r['d']}…")
        if len(rows) > 20:
            P.append(f"- _(+{len(rows)-20} more — see data package §9)_")
    else:
        P.append("_(no open SB findings)_")
    P.append("")

    # --- Resolved Q&As (against the retired v1 catalogue) ---
    P.append("## 4. Prior Q&A coverage — v1 catalogue (retired 2026-04-30)\n")
    n_v1_links = conn.execute("""
        SELECT COUNT(*) FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id=l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
        WHERE f.registry_id=67 AND q.status='redundant_v1'
        AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)
    """).fetchone()[0]
    P.append(f"**Q&A links to retired v1 catalogue:** {n_v1_links}\n")
    P.append("These links are preserved as analytic provenance. Under v1.8, Stage 2b is run against the v2 catalogue (T0–T7) — the v1 answers serve as Stage 2a source material per §10 of v1.8.\n")

    P.append("**v1 coverage breakdown:**\n")
    P.append("| coverage | count |\n| --- | ---: |")
    rows = conn.execute("""
        SELECT l.coverage, COUNT(*) AS n
        FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id=l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
        WHERE f.registry_id=67 AND q.status='redundant_v1'
        AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)
        GROUP BY l.coverage ORDER BY n DESC
    """).fetchall()
    for r in rows:
        P.append(f"| {r['coverage']} | {r['n']} |")
    P.append("")

    # --- v2 catalogue coverage status ---
    P.append("## 5. v2 catalogue coverage status (Stage 2b under v1.8)\n")
    n_v2_total = conn.execute("""
        SELECT COUNT(*) FROM wa_obs_question_catalogue
        WHERE catalogue_version='v2-2026-04-29' AND (deleted=0 OR deleted IS NULL)
    """).fetchone()[0]
    n_v2_covered = conn.execute("""
        SELECT COUNT(DISTINCT l.question_id)
        FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id=l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
        WHERE f.registry_id=67 AND q.catalogue_version='v2-2026-04-29'
        AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)
    """).fetchone()[0]
    P.append(f"**v2 prompts in catalogue:** {n_v2_total}")
    P.append(f"**v2 prompts with R067 link:** {n_v2_covered}")
    P.append(f"**v2 prompts NOT YET covered for R067:** {n_v2_total - n_v2_covered}\n")
    if n_v2_covered == 0:
        P.append("**Status:** R067 has not yet been processed against the v2 catalogue. Stage 2b under v1.8 is **outstanding** — all 189 prompts need disposition (A / P / S / N).\n")

    # --- Stage 2c synthesis state ---
    P.append("## 6. Stage 2c synthesis state (under v1.8)\n")
    n_synth = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings
        WHERE registry_id=67 AND finding_type LIKE 'SYNTHESIS_%' AND delete_flag=0
    """).fetchone()[0]
    P.append(f"**Synthesis findings in DB:** {n_synth} (target: 28 — 7 intra-tier T1–T7 + 21 inter-tier T1–T7 pairs)\n")
    if n_synth == 0:
        P.append("**Status:** Stage 2c synthesis pass under v1.8 has not been run. All 28 synthesis entries are **outstanding**.\n")
    P.append("Per v1.8 SB-29: every entry carries one of three outcomes (D / F / N). T0 is excluded from Stage 2c (held for Session D).\n")

    # --- Prior Stage 2c prose chapters (legacy v1.7 model) ---
    P.append("## 7. Prior Stage 2c prose chapters (legacy v1.5/v1.7 model)\n")
    rows = conn.execute("""
        SELECT pst.code, pst.label, ps.id AS section_id, ps.version,
               LENGTH(ps.body) AS body_chars, ps.status, ps.created_at
        FROM prose_section ps
        JOIN prose_section_type pst ON pst.id = ps.section_type_id
        WHERE ps.registry_id=67 AND ps.delete_flagged=0 AND ps.superseded_by_id IS NULL
        ORDER BY pst.sort_order
    """).fetchall()
    P.append("Five chapters exist as `prose_section` rows under the legacy v1.7 model. Under v1.8 these remain as historical record — Session C reads from synthesis findings going forward. They become candidates for SUPERSEDE only if a revision session under v1.8 materially changes their analytical scope (per v1.8 §7).\n")
    P.append("| code | label | version | body chars | status | created |")
    P.append("| --- | --- | ---: | ---: | --- | --- |")
    for r in rows:
        P.append(f"| `{r['code']}` | {r['label']} | v{r['version']} | {r['body_chars']:,} | {r['status']} | {r['created_at'][:10]} |")
    P.append("")

    # --- Anchor-verse analyses ---
    P.append("## 8. Anchor-verse analyses (`verse_context.analysis_note`)\n")
    rows = conn.execute("""
        SELECT vr.reference, vr.term_id, mt.strongs_number,
               g.group_code, SUBSTR(vc.analysis_note,1,160) AS note
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        JOIN verse_context_group g ON g.id = vc.group_id
        WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no=67)
        AND vc.is_anchor=1 AND vc.analysis_note IS NOT NULL
        AND (vc.delete_flagged=0 OR vc.delete_flagged IS NULL)
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """).fetchall()
    P.append(f"**Anchor verses with analysis_note populated:** {len(rows)}\n")
    if rows:
        P.append("| Reference | Term | Group | Note (first 160 chars) |")
        P.append("| --- | --- | --- | --- |")
        for r in rows:
            note = (r["note"] or "").replace("\n", " ").replace("|", "/")
            P.append(f"| {r['reference']} | {r['term_id']} | {r['group_code']} | {note}… |")
    P.append("")

    # --- §N open items (carried forward into the next session) ---
    P.append("## 9. Open Session B items — §N for the v1.8 session\n")
    P.append("Per v1.8 §3, every open item must reach one of four outcomes by session close: resolve via Q&A, raise as new GAP question, convert to SD pointer, or mark not_relevant.\n")

    # Open findings
    rows = conn.execute("""
        SELECT finding_id, finding_type, status, SUBSTR(finding,1,160) AS f
        FROM wa_session_b_findings
        WHERE registry_id=67 AND delete_flag=0
        AND status IN ('open','pending')
        ORDER BY finding_type, finding_id
    """).fetchall()
    P.append(f"**Open findings (status=open/pending):** {len(rows)}\n")
    if rows:
        for r in rows[:30]:
            f_text = (r["f"] or "").replace("\n", " ")
            P.append(f"- **{r['finding_id']}** ({r['finding_type']}, status={r['status']}) — {f_text}…")
        if len(rows) > 30:
            P.append(f"- _(+{len(rows)-30} more)_")
    P.append("")

    # --- What v1.8 expects on resubmission ---
    P.append("## 10. What v1.8 expects on resubmission\n")
    P.append("**Stage 2a:** observations layer is in place (49 OBS findings). No new Stage 2a reading required unless gaps surface during Stage 2b.\n")
    P.append("**Stage 2b:** all 189 v2 catalogue prompts (T0–T7) require disposition (A / P / S / N) per §10. Prior v1 Q&A answers (76 total) are Stage 2a source material — every v2 prompt receives a fresh answer grounded in the data package.\n")
    P.append("**Stage 2c:** new under v1.8 — produce 28 synthesis entries (7 intra T1–T7 + 21 inter T1–T7 pairs). T0 excluded (Session D). Each entry: outcome D/F/N; D needs ≥2 Q&A citations; F always raises an SD pointer; N requires a one-sentence rationale. See §SB-29.\n")
    P.append("**Output:** comprehensive obslog `wa-067-goodness-obslog-v{n}-{date}.md` + session log. CC parses obslog into DB.\n")

    P.append("---\n")
    P.append(f"*Generated by `scripts/_tmp_build_R067_resubmission_artefacts.py` at {now_iso()}.*")

    return "\n".join(P)


def build_validation_report(conn: sqlite3.Connection) -> str:
    P: list[str] = []
    P.append("# R067 Goodness — Validation Report (gate-passing audit)\n")
    P.append(f"**Generated:** {now_iso()}")
    P.append(f"**Governing instruction:** [wa-sessionb-analysis-output-v1_8-20260430.md](../../../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md)\n")
    P.append("**Verdict:** _(see below)_\n")
    P.append("**Purpose.** Stage 2 prerequisite gate. Per v1.8 prerequisites, Stage 2 cannot start unless this report is at READY. WARN items are informational — AI tracks them where they materially affect findings.\n")
    P.append("---\n")

    checks: list[tuple[str, str, str]] = []  # (check, verdict, evidence)

    # 1. Pre-analysis status
    r = conn.execute("SELECT session_b_status, verse_context_status, dim_review_status FROM word_registry WHERE no=67").fetchone()
    if r["session_b_status"] in ("Pre-Analysis Complete", "Analysis Complete", "Ready for Analysis", "Session B Complete"):
        checks.append(("session_b_status sound for Stage 2", "PASS", f"`{r['session_b_status']}`"))
    else:
        checks.append(("session_b_status sound for Stage 2", "FAIL", f"`{r['session_b_status']}` — Stage 2 cannot begin"))

    # 2. Verse Context status
    if r["verse_context_status"] == "Complete":
        checks.append(("verse_context_status = Complete", "PASS", "Complete"))
    else:
        checks.append(("verse_context_status = Complete", "FAIL", f"`{r['verse_context_status']}`"))

    # 3. Dimension review status
    if r["dim_review_status"] == "Complete":
        checks.append(("dim_review_status = Complete", "PASS", "Complete"))
    elif r["dim_review_status"] is None:
        checks.append(("dim_review_status = Complete", "WARN",
                       "NULL — R067 has no dim review record. Other v2-captured words are at Complete. May affect Stage 2b T2 (Constitutional Location) and T3 (Inner Faculties) prompt-quality."))
    else:
        checks.append(("dim_review_status = Complete", "WARN", f"`{r['dim_review_status']}`"))

    # 4. Catalogue v2 loaded
    n_v2 = conn.execute("""SELECT COUNT(*) FROM wa_obs_question_catalogue
        WHERE catalogue_version='v2-2026-04-29' AND (deleted=0 OR deleted IS NULL)""").fetchone()[0]
    if n_v2 >= 189:
        checks.append(("v2 catalogue loaded (≥189 rows)", "PASS", f"{n_v2} active v2 prompts"))
    else:
        checks.append(("v2 catalogue loaded (≥189 rows)", "FAIL", f"{n_v2} v2 prompts — catalogue migration incomplete"))

    # 5. Stage 2c synthesis schema
    cols = [c[1] for c in conn.execute("PRAGMA table_info(wa_session_b_findings)").fetchall()]
    needed = ['synthesis_outcome', 'tiers_engaged', 'structural_relationship', 'session_c_chapter', 'sd_pointer_ref']
    missing = [c for c in needed if c not in cols]
    if not missing:
        checks.append(("v1.8 synthesis schema present", "PASS", "5/5 columns present on `wa_session_b_findings`"))
    else:
        checks.append(("v1.8 synthesis schema present", "FAIL", f"missing: {missing}"))

    # 6. Term inventory
    n_owner = conn.execute("""
        SELECT COUNT(*) FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id=ti.file_id
        WHERE fi.registry_id=67 AND ti.term_owner_type='OWNER'
        AND (ti.delete_flagged=0 OR ti.delete_flagged IS NULL)
    """).fetchone()[0]
    if n_owner > 0:
        checks.append(("OWNER terms present", "PASS", f"{n_owner} OWNER terms"))
    else:
        checks.append(("OWNER terms present", "FAIL", "0 OWNER terms — extract incomplete"))

    # 7. Verse Context groups
    n_groups = conn.execute("""
        SELECT COUNT(*) FROM verse_context_group g
        JOIN mti_terms mt ON mt.id=g.mti_term_id
        WHERE mt.owning_registry_fk=(SELECT id FROM word_registry WHERE no=67)
        AND (g.delete_flagged=0 OR g.delete_flagged IS NULL)
    """).fetchone()[0]
    if n_groups > 0:
        checks.append(("VC groups present", "PASS", f"{n_groups} groups"))
    else:
        checks.append(("VC groups present", "FAIL", "0 groups"))

    # 8. Anchor verses populated
    n_anchors = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id=vc.mti_term_id
        WHERE mt.owning_registry_fk=(SELECT id FROM word_registry WHERE no=67)
        AND vc.is_anchor=1 AND (vc.delete_flagged=0 OR vc.delete_flagged IS NULL)
    """).fetchone()[0]
    if n_anchors > 0:
        checks.append(("Anchor verses present", "PASS", f"{n_anchors} anchor verses"))
    else:
        checks.append(("Anchor verses present", "FAIL", "0 anchors"))

    # 9. Stage 2a observations present
    n_obs = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings
        WHERE registry_id=67 AND delete_flag=0
        AND finding_type IN ('OBSERVATION','OBSERVATION_REGISTER')
    """).fetchone()[0]
    if n_obs > 0:
        checks.append(("Stage 2a observations present (revision)", "PASS", f"{n_obs} observation findings"))
    else:
        checks.append(("Stage 2a observations present (revision)", "WARN", "0 — fresh Stage 2a needed"))

    # 10. v2 Q&A coverage
    n_v2_links = conn.execute("""
        SELECT COUNT(DISTINCT l.question_id) FROM wa_finding_catalogue_links l
        JOIN wa_session_b_findings f ON f.id=l.finding_id
        JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
        WHERE f.registry_id=67 AND q.catalogue_version='v2-2026-04-29'
        AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)
    """).fetchone()[0]
    if n_v2_links == 0:
        checks.append(("v2 Q&A coverage (Stage 2b under v1.8)", "WARN",
                       "0/189 — Stage 2b is the work to be done in this session. Not a blocker."))
    elif n_v2_links < 189:
        checks.append(("v2 Q&A coverage", "WARN",
                       f"{n_v2_links}/189 partial — Stage 2b session continues"))
    else:
        checks.append(("v2 Q&A coverage", "PASS", "Complete"))

    # 11. Stage 2c synthesis present
    n_synth = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings
        WHERE registry_id=67 AND finding_type LIKE 'SYNTHESIS_%' AND delete_flag=0
    """).fetchone()[0]
    if n_synth == 0:
        checks.append(("Stage 2c synthesis (under v1.8)", "WARN",
                       "0/28 — Stage 2c is the work to be done. Not a blocker; this is the resubmission scope."))
    elif n_synth < 28:
        checks.append(("Stage 2c synthesis", "WARN", f"{n_synth}/28 partial"))
    else:
        checks.append(("Stage 2c synthesis", "PASS", "Complete"))

    # 12. Quality flags review
    n_eviflag = conn.execute("""
        SELECT COUNT(*) FROM wa_data_quality_flags qf
        JOIN wa_file_index fi ON fi.id=qf.file_id
        WHERE fi.registry_id=67
    """).fetchone()[0]
    checks.append(("Data quality flags reviewed", "INFO", f"{n_eviflag} flag rows in `wa_data_quality_flags` — see data package §7"))

    # 13. SD pointers in DB
    n_sp = conn.execute("""
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id=(SELECT id FROM word_registry WHERE no=67)
        AND flag_code='SD_POINTER' AND (resolved=0 OR resolved IS NULL)
    """).fetchone()[0]
    checks.append(("SD pointers carried forward", "INFO", f"{n_sp} open SD pointers — input to Stage 2c F-outcome decisions"))

    # 14. Open SB findings
    n_sb = conn.execute("""
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id=(SELECT id FROM word_registry WHERE no=67)
        AND flag_code='SB_FINDING' AND (resolved=0 OR resolved IS NULL)
    """).fetchone()[0]
    if n_sb > 0:
        checks.append(("Open SB_FINDING flags", "WARN",
                       f"{n_sb} open — these are §N candidates per v1.8 §3 and must reach a closure outcome before session close"))
    else:
        checks.append(("Open SB_FINDING flags", "PASS", "0 open"))

    # 15. Researcher decisions
    n_rd = conn.execute("""
        SELECT COUNT(*) FROM wa_session_research_flags
        WHERE registry_id=(SELECT id FROM word_registry WHERE no=67)
        AND flag_code='RESEARCHER_DECISION' AND (resolved=0 OR resolved IS NULL)
    """).fetchone()[0]
    if n_rd > 0:
        checks.append(("Open RESEARCHER_DECISION items", "WARN",
                       f"{n_rd} open — surface to researcher; do not block"))
    else:
        checks.append(("Open RESEARCHER_DECISION items", "PASS", "0 open"))

    # Render the report
    pass_n = sum(1 for c in checks if c[1] == "PASS")
    warn_n = sum(1 for c in checks if c[1] == "WARN")
    fail_n = sum(1 for c in checks if c[1] == "FAIL")
    info_n = sum(1 for c in checks if c[1] == "INFO")

    if fail_n == 0:
        verdict = "READY"
    else:
        verdict = "BLOCKED"

    P[3] = f"**Verdict:** **{verdict}** — {pass_n} PASS, {warn_n} WARN, {fail_n} FAIL, {info_n} INFO across {len(checks)} checks.\n"

    P.append("## Check results\n")
    P.append("| # | Check | Verdict | Evidence |")
    P.append("| ---: | --- | :---: | --- |")
    for i, (label, v, ev) in enumerate(checks, 1):
        P.append(f"| {i} | {label} | **{v}** | {ev} |")
    P.append("")

    P.append("\n## WARN list — informational items for AI to track during Stage 2\n")
    warns = [(i, c) for i, c in enumerate(checks, 1) if c[1] == "WARN"]
    if warns:
        for i, (label, _, ev) in warns:
            P.append(f"- **#{i} {label}:** {ev}")
    else:
        P.append("_(no WARN items)_")
    P.append("")

    if fail_n:
        P.append("## FAIL list — must be resolved before Stage 2\n")
        for i, (label, v, ev) in enumerate(checks, 1):
            if v == "FAIL":
                P.append(f"- **#{i} {label}:** {ev}")
        P.append("")

    P.append("---\n")
    P.append(f"*Generated by `scripts/_tmp_build_R067_resubmission_artefacts.py` at {now_iso()}.*")

    return "\n".join(P)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    os.makedirs(OUT_DIR, exist_ok=True)

    # 1. Analytic Status
    out = build_analytic_status(conn)
    out_path = os.path.join(OUT_DIR, "wa-067-goodness-analytic-status-v1-20260430.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {out_path} ({len(out):,} chars)")

    # 2. Validation Report
    out = build_validation_report(conn)
    out_path = os.path.join(OUT_DIR, "wa-067-goodness-readiness-validation-v1-20260430.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {out_path} ({len(out):,} chars)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
