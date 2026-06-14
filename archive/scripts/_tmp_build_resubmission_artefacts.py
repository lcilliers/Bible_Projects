"""_tmp_build_resubmission_artefacts.py

Build v1.8 input artefacts for any registry's analysis-output (re)submission:

  1. Analytic Status .md — for revision sessions per v1.8 §1
     (lifecycle summary, prior chapters, anchor analyses, open items)
  2. Validation Report .md — gate-passing audit + WARN list

Generalised from the R067-specific original. Output folder is auto-detected
from the existing bundle structure (e.g. "R067 goodness", "R103 love",
"r023-compassion") — falls back to a default pattern if not present.

Usage:
  python scripts/_tmp_build_resubmission_artefacts.py --registry 103
  python scripts/_tmp_build_resubmission_artefacts.py --registry 67
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BUNDLE_DIR = os.path.join(
    "research", "investigations", "ai_question_test_bundle_20260429"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def find_or_make_folder(registry_no: int, word: str) -> str:
    """Find existing bundle subfolder for this registry, or pick a default."""
    candidates = []
    for entry in sorted(os.listdir(BUNDLE_DIR)):
        path = os.path.join(BUNDLE_DIR, entry)
        if not os.path.isdir(path):
            continue
        # Match patterns like "R067 goodness", "r023-compassion", "R103 love"
        lower = entry.lower()
        if (f"r{registry_no:03d}" in lower or f"r{registry_no} " in lower or
                f"r{registry_no}-" in lower) and word.lower() in lower:
            candidates.append(path)
    if candidates:
        return candidates[0]
    # Default: "R{NNN} {word}" (matches R067 goodness pattern)
    default = os.path.join(BUNDLE_DIR, f"R{registry_no:03d} {word}")
    os.makedirs(default, exist_ok=True)
    return default


def build_analytic_status(conn: sqlite3.Connection, registry_no: int) -> str:
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    word = reg["word"]
    word_title = word.title()

    P: list[str] = []
    P.append(f"# R{registry_no:03d} {word_title} — Analytic Status (v1.8 revision-session input)\n")
    P.append(f"**Generated:** {now_iso()}")
    P.append("**Source:** SQLite `database/bible_research.db` (schema v3.17.0)")
    P.append("**Governing instruction:** [wa-sessionb-analysis-output-v1_8-20260430.md](../../../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md) §1 (revision-session input)\n")
    P.append(f"**Purpose.** Capture the prior analytical state for R{registry_no:03d} {word} so a Stage 2 session can resume cleanly under v1.8. Lifecycle summary, resolved Q&As, resolved SD pointers, prior chapters, anchor analyses, and open items.\n")
    P.append("---\n")

    # --- Registry header ---
    P.append("## 1. Registry header\n")
    P.append("| Field | Value |\n| --- | --- |")
    for k in ("no", "id", "word", "category_hint", "dimensions", "cluster_assignment",
              "phase1_status", "verse_context_status", "session_b_status",
              "dim_review_status", "dim_review_version"):
        P.append(f"| `{k}` | {reg[k]} |")
    P.append("")

    # --- Lifecycle summary ---
    P.append("## 2. Lifecycle summary\n")
    n_findings = conn.execute(
        "SELECT COUNT(*) FROM wa_session_b_findings WHERE registry_id=? AND delete_flag=0",
        (registry_no,),
    ).fetchone()[0]
    P.append(f"**Active findings (`wa_session_b_findings`):** {n_findings}\n")

    if n_findings:
        P.append("**By finding_type:**\n")
        P.append("| finding_type | count |\n| --- | ---: |")
        rows = conn.execute(
            """SELECT finding_type, COUNT(*) AS n
               FROM wa_session_b_findings
               WHERE registry_id=? AND delete_flag=0
               GROUP BY finding_type ORDER BY n DESC""",
            (registry_no,),
        ).fetchall()
        for r in rows:
            P.append(f"| {r['finding_type']} | {r['n']} |")
        P.append("")

        P.append("**By status:**\n")
        P.append("| status | count |\n| --- | ---: |")
        rows = conn.execute(
            """SELECT status, COUNT(*) AS n FROM wa_session_b_findings
               WHERE registry_id=? AND delete_flag=0
               GROUP BY status ORDER BY n DESC""",
            (registry_no,),
        ).fetchall()
        for r in rows:
            P.append(f"| {r['status']} | {r['n']} |")
        P.append("")
    else:
        P.append("_No prior `wa_session_b_findings` rows. This is effectively a first Session B Stage 2 pass under v1.8._\n")

    # --- Open research flags ---
    P.append("## 3. Open research flags (`wa_session_research_flags`)\n")
    rows = conn.execute(
        """SELECT flag_code, COUNT(*) AS n FROM wa_session_research_flags
           WHERE registry_id=(SELECT id FROM word_registry WHERE no=?)
           AND (resolved=0 OR resolved IS NULL)
           GROUP BY flag_code ORDER BY n DESC""",
        (registry_no,),
    ).fetchall()
    if rows:
        P.append("| flag_code | open count |\n| --- | ---: |")
        for r in rows:
            P.append(f"| {r['flag_code']} | {r['n']} |")
        P.append("")
    else:
        P.append("_No open flags._\n")

    # SD pointers HIGH list
    P.append("### 3.1 SD pointers — HIGH priority (full list in data package §9)\n")
    rows = conn.execute(
        """SELECT flag_label, priority, SUBSTR(description,1,140) AS d
           FROM wa_session_research_flags
           WHERE registry_id=(SELECT id FROM word_registry WHERE no=?)
           AND flag_code='SD_POINTER' AND priority='HIGH'
           AND (resolved=0 OR resolved IS NULL)
           ORDER BY flag_label""",
        (registry_no,),
    ).fetchall()
    if rows:
        for r in rows:
            P.append(f"- **{r['flag_label']}** ({r['priority']}) — {r['d']}…")
    else:
        P.append("_(no HIGH-priority SD pointers)_")
    P.append("")

    # SB findings
    P.append("### 3.2 Open SB findings (Session B follow-on items)\n")
    rows = conn.execute(
        """SELECT flag_label, priority, SUBSTR(description,1,140) AS d
           FROM wa_session_research_flags
           WHERE registry_id=(SELECT id FROM word_registry WHERE no=?)
           AND flag_code='SB_FINDING'
           AND (resolved=0 OR resolved IS NULL)
           ORDER BY priority, flag_label""",
        (registry_no,),
    ).fetchall()
    if rows:
        for r in rows[:20]:
            P.append(f"- **{r['flag_label']}** ({r['priority']}) — {r['d']}…")
        if len(rows) > 20:
            P.append(f"- _(+{len(rows)-20} more — see data package §9)_")
    else:
        P.append("_(no open SB findings)_")
    P.append("")

    # --- v1 historical Q&A links ---
    P.append("## 4. Prior Q&A coverage — v1 catalogue (retired 2026-04-30)\n")
    n_v1_links = conn.execute(
        """SELECT COUNT(*) FROM wa_finding_catalogue_links l
           JOIN wa_session_b_findings f ON f.id=l.finding_id
           JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
           WHERE f.registry_id=? AND q.status='redundant_v1'
           AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    P.append(f"**Q&A links to retired v1 catalogue:** {n_v1_links}\n")
    if n_v1_links > 0:
        P.append("These links are preserved as analytic provenance. Under v1.8, Stage 2b is run against the v2 catalogue (T0–T7) — the v1 answers serve as Stage 2a source material per §10 of v1.8.\n")
        P.append("**v1 coverage breakdown:**\n")
        P.append("| coverage | count |\n| --- | ---: |")
        rows = conn.execute(
            """SELECT l.coverage, COUNT(*) AS n
               FROM wa_finding_catalogue_links l
               JOIN wa_session_b_findings f ON f.id=l.finding_id
               JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
               WHERE f.registry_id=? AND q.status='redundant_v1'
               AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)
               GROUP BY l.coverage ORDER BY n DESC""",
            (registry_no,),
        ).fetchall()
        for r in rows:
            P.append(f"| {r['coverage']} | {r['n']} |")
        P.append("")
    else:
        P.append("_No prior v1 Q&A work for this registry. This is a first Session B Stage 2 pass under the v2 catalogue._\n")

    # --- v2 catalogue coverage status ---
    P.append("## 5. v2 catalogue coverage status (Stage 2b under v1.8)\n")
    n_v2_total = conn.execute(
        """SELECT COUNT(*) FROM wa_obs_question_catalogue
           WHERE catalogue_version='v2-2026-04-29' AND (deleted=0 OR deleted IS NULL)"""
    ).fetchone()[0]
    n_v2_covered = conn.execute(
        """SELECT COUNT(DISTINCT l.question_id)
           FROM wa_finding_catalogue_links l
           JOIN wa_session_b_findings f ON f.id=l.finding_id
           JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
           WHERE f.registry_id=? AND q.catalogue_version='v2-2026-04-29'
           AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    P.append(f"**v2 prompts in catalogue:** {n_v2_total}")
    P.append(f"**v2 prompts with R{registry_no:03d} link:** {n_v2_covered}")
    P.append(f"**v2 prompts NOT YET covered for R{registry_no:03d}:** {n_v2_total - n_v2_covered}\n")
    if n_v2_covered == 0:
        P.append(f"**Status:** R{registry_no:03d} has not yet been processed against the v2 catalogue. Stage 2b under v1.8 is **outstanding** — all 189 prompts need disposition (A / P / S / N).\n")

    # --- Stage 2c synthesis state ---
    P.append("## 6. Stage 2c synthesis state (under v1.8)\n")
    n_synth = conn.execute(
        """SELECT COUNT(*) FROM wa_session_b_findings
           WHERE registry_id=? AND finding_type LIKE 'SYNTHESIS_%' AND delete_flag=0""",
        (registry_no,),
    ).fetchone()[0]
    P.append(f"**Synthesis findings in DB:** {n_synth} (target: 28 — 7 intra-tier T1–T7 + 21 inter-tier T1–T7 pairs)\n")
    if n_synth == 0:
        P.append("**Status:** Stage 2c synthesis pass under v1.8 has not been run. All 28 synthesis entries are **outstanding**.\n")
    P.append("Per v1.8 SB-29: every entry carries one of three outcomes (D / F / N). T0 is excluded from Stage 2c (held for Session D).\n")

    # --- Prior prose chapters ---
    P.append("## 7. Prior prose chapters\n")
    rows = conn.execute(
        """SELECT pst.code, pst.label, pst.source_stage, ps.id AS section_id, ps.version,
                  LENGTH(ps.body) AS body_chars, ps.status, ps.author, ps.created_at
           FROM prose_section ps
           JOIN prose_section_type pst ON pst.id = ps.section_type_id
           WHERE ps.registry_id=? AND ps.delete_flagged=0 AND ps.superseded_by_id IS NULL
           ORDER BY pst.sort_order""",
        (registry_no,),
    ).fetchall()
    if rows:
        # Distinguish session_a vs sb_s2c chapters
        sa_chapters = [r for r in rows if (r["code"] or "").startswith("sa_")]
        sb_chapters = [r for r in rows if (r["code"] or "").startswith("sb_s2c")]
        other = [r for r in rows if not (r["code"] or "").startswith(("sa_", "sb_s2c"))]

        if sa_chapters:
            P.append(f"**Session A chapters (Phase 1 outputs):** {len(sa_chapters)}\n")
            P.append("| code | label | version | body chars | status | created |")
            P.append("| --- | --- | ---: | ---: | --- | --- |")
            for r in sa_chapters:
                P.append(f"| `{r['code']}` | {r['label']} | v{r['version']} | {r['body_chars']:,} | {r['status']} | {r['created_at'][:10]} |")
            P.append("")

        if sb_chapters:
            P.append(f"**Session B Stage 2c prose chapters (legacy v1.5/v1.7 model):** {len(sb_chapters)}\n")
            P.append("Under v1.8 these remain as historical record — Session C reads from synthesis findings going forward. They become candidates for SUPERSEDE only if a revision session under v1.8 materially changes their analytical scope (per v1.8 §7).\n")
            P.append("| code | label | version | body chars | status | created |")
            P.append("| --- | --- | ---: | ---: | --- | --- |")
            for r in sb_chapters:
                P.append(f"| `{r['code']}` | {r['label']} | v{r['version']} | {r['body_chars']:,} | {r['status']} | {r['created_at'][:10]} |")
            P.append("")

        if other:
            P.append(f"**Other prose sections:** {len(other)}\n")
            for r in other:
                P.append(f"- `{r['code']}` ({r['source_stage']}) — {r['body_chars']:,} chars, {r['status']}")
            P.append("")
    else:
        P.append("_No active `prose_section` rows for this registry._\n")

    # --- Anchor-verse analyses ---
    P.append("## 8. Anchor-verse analyses (`verse_context.analysis_note`)\n")
    rows = conn.execute(
        """SELECT vr.reference, vr.term_id, mt.strongs_number,
                  g.group_code, SUBSTR(vc.analysis_note,1,160) AS note
           FROM verse_context vc
           JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
           JOIN mti_terms mt ON mt.id = vc.mti_term_id
           JOIN verse_context_group g ON g.id = vc.group_id
           WHERE mt.owning_registry_fk = (SELECT id FROM word_registry WHERE no=?)
           AND vc.is_anchor=1 AND vc.analysis_note IS NOT NULL
           AND (vc.delete_flagged=0 OR vc.delete_flagged IS NULL)
           ORDER BY vr.book_id, vr.chapter, vr.verse_num""",
        (registry_no,),
    ).fetchall()
    P.append(f"**Anchor verses with analysis_note populated:** {len(rows)}\n")
    if rows:
        P.append("| Reference | Term | Group | Note (first 160 chars) |")
        P.append("| --- | --- | --- | --- |")
        for r in rows[:40]:
            note = (r["note"] or "").replace("\n", " ").replace("|", "/")
            P.append(f"| {r['reference']} | {r['term_id']} | {r['group_code']} | {note}… |")
        if len(rows) > 40:
            P.append(f"| … | | | _(+{len(rows)-40} more)_ |")
    else:
        P.append("_No anchor-verse analyses captured. Stage 2a Unit 7 in this session will populate `analysis_note` per anchor verse._\n")
    P.append("")

    # --- §N open items ---
    P.append("## 9. Open Session B items — §N for the v1.8 session\n")
    P.append("Per v1.8 §3, every open item must reach one of four outcomes by session close: resolve via Q&A, raise as new GAP question, convert to SD pointer, or mark not_relevant.\n")
    rows = conn.execute(
        """SELECT finding_id, finding_type, status, SUBSTR(finding,1,160) AS f
           FROM wa_session_b_findings
           WHERE registry_id=? AND delete_flag=0
           AND status IN ('open','pending')
           ORDER BY finding_type, finding_id""",
        (registry_no,),
    ).fetchall()
    P.append(f"**Open findings (status=open/pending):** {len(rows)}\n")
    if rows:
        for r in rows[:30]:
            f_text = (r["f"] or "").replace("\n", " ")
            P.append(f"- **{r['finding_id']}** ({r['finding_type']}, status={r['status']}) — {f_text}…")
        if len(rows) > 30:
            P.append(f"- _(+{len(rows)-30} more)_")
    P.append("")

    # --- What v1.8 expects ---
    P.append("## 10. What v1.8 expects on (re)submission\n")
    if n_findings == 0:
        P.append("**Stage 2a:** no prior OBS layer in DB. Stage 2a Unit 1–9 readings are required to build the observation base before Stage 2b can begin.\n")
    else:
        P.append(f"**Stage 2a:** observations layer is in place ({n_findings} findings). No new Stage 2a reading required unless gaps surface during Stage 2b.\n")
    P.append("**Stage 2b:** all 189 v2 catalogue prompts (T0–T7) require disposition (A / P / S / N) per §10. Prior v1 Q&A answers are Stage 2a source material — every v2 prompt receives a fresh answer grounded in the data package.\n")
    P.append("**Stage 2c:** new under v1.8 — produce 28 synthesis entries (7 intra T1–T7 + 21 inter T1–T7 pairs). T0 excluded (Session D). Each entry: outcome D/F/N; D needs ≥2 Q&A citations; F always raises an SD pointer; N requires a one-sentence rationale. See §SB-29.\n")
    P.append(f"**Output:** comprehensive obslog `wa-{registry_no:03d}-{word}-obslog-v{{n}}-{{date}}.md` + session log. CC parses obslog into DB.\n")

    P.append("---\n")
    P.append(f"*Generated by `scripts/_tmp_build_resubmission_artefacts.py` at {now_iso()}.*")
    return "\n".join(P)


def build_validation_report(conn: sqlite3.Connection, registry_no: int) -> str:
    reg = conn.execute("SELECT * FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    word = reg["word"]
    word_title = word.title()

    P: list[str] = []
    P.append(f"# R{registry_no:03d} {word_title} — Validation Report (gate-passing audit)\n")
    P.append(f"**Generated:** {now_iso()}")
    P.append("**Governing instruction:** [wa-sessionb-analysis-output-v1_8-20260430.md](../../../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md)\n")
    P.append("**Verdict:** _(see below)_\n")
    P.append("**Purpose.** Stage 2 prerequisite gate. Per v1.8 prerequisites, Stage 2 cannot start unless this report is at READY. WARN items are informational — AI tracks them where they materially affect findings.\n")
    P.append("---\n")

    checks: list[tuple[str, str, str]] = []

    # 1. session_b_status
    valid_states = (
        "Pre-Analysis Complete", "Analysis Complete", "Ready for Analysis",
        "Session B Complete", "Verse Context Reset",
    )
    if reg["session_b_status"] in valid_states:
        if reg["session_b_status"] == "Verse Context Reset":
            checks.append(("session_b_status sound for Stage 2", "WARN",
                           f"`{reg['session_b_status']}` — Stage 2 has not yet been run on this registry under any catalogue. This will be a first Session B Stage 2 pass."))
        else:
            checks.append(("session_b_status sound for Stage 2", "PASS", f"`{reg['session_b_status']}`"))
    else:
        checks.append(("session_b_status sound for Stage 2", "FAIL", f"`{reg['session_b_status']}` — Stage 2 cannot begin"))

    # 2. verse_context_status
    if reg["verse_context_status"] == "Complete":
        checks.append(("verse_context_status = Complete", "PASS", "Complete"))
    else:
        checks.append(("verse_context_status = Complete", "FAIL", f"`{reg['verse_context_status']}`"))

    # 3. dim_review_status
    if reg["dim_review_status"] == "Complete":
        checks.append(("dim_review_status = Complete", "PASS", "Complete"))
    elif reg["dim_review_status"] is None:
        checks.append(("dim_review_status = Complete", "WARN",
                       "NULL — no dim review record. May affect Stage 2b T2 (Constitutional Location) and T3 (Inner Faculties) prompt-quality."))
    else:
        checks.append(("dim_review_status = Complete", "WARN", f"`{reg['dim_review_status']}`"))

    # 4. catalogue v2 loaded
    n_v2 = conn.execute(
        """SELECT COUNT(*) FROM wa_obs_question_catalogue
           WHERE catalogue_version='v2-2026-04-29' AND (deleted=0 OR deleted IS NULL)"""
    ).fetchone()[0]
    if n_v2 >= 189:
        checks.append(("v2 catalogue loaded (≥189 rows)", "PASS", f"{n_v2} active v2 prompts"))
    else:
        checks.append(("v2 catalogue loaded (≥189 rows)", "FAIL", f"{n_v2} v2 prompts — catalogue migration incomplete"))

    # 5. v1.8 synthesis schema
    cols = [c[1] for c in conn.execute("PRAGMA table_info(wa_session_b_findings)").fetchall()]
    needed = ['synthesis_outcome', 'tiers_engaged', 'structural_relationship', 'session_c_chapter', 'sd_pointer_ref']
    missing = [c for c in needed if c not in cols]
    if not missing:
        checks.append(("v1.8 synthesis schema present", "PASS", "5/5 columns present on `wa_session_b_findings`"))
    else:
        checks.append(("v1.8 synthesis schema present", "FAIL", f"missing: {missing}"))

    # 6. OWNER terms
    n_owner = conn.execute(
        """SELECT COUNT(*) FROM wa_term_inventory ti
           JOIN wa_file_index fi ON fi.id=ti.file_id
           WHERE fi.registry_id=? AND ti.term_owner_type='OWNER'
           AND (ti.delete_flagged=0 OR ti.delete_flagged IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    if n_owner > 0:
        checks.append(("OWNER terms present", "PASS", f"{n_owner} OWNER terms"))
    else:
        checks.append(("OWNER terms present", "FAIL", "0 OWNER terms — extract incomplete"))

    # 7. VC groups
    n_groups = conn.execute(
        """SELECT COUNT(*) FROM verse_context_group g
           JOIN mti_terms mt ON mt.id=g.mti_term_id
           WHERE mt.owning_registry_fk=(SELECT id FROM word_registry WHERE no=?)
           AND (g.delete_flagged=0 OR g.delete_flagged IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    if n_groups > 0:
        checks.append(("VC groups present", "PASS", f"{n_groups} groups"))
    else:
        checks.append(("VC groups present", "FAIL", "0 groups"))

    # 8. anchor verses
    n_anchors = conn.execute(
        """SELECT COUNT(*) FROM verse_context vc
           JOIN mti_terms mt ON mt.id=vc.mti_term_id
           WHERE mt.owning_registry_fk=(SELECT id FROM word_registry WHERE no=?)
           AND vc.is_anchor=1 AND (vc.delete_flagged=0 OR vc.delete_flagged IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    if n_anchors > 0:
        checks.append(("Anchor verses present", "PASS", f"{n_anchors} anchor verses"))
    else:
        checks.append(("Anchor verses present", "FAIL", "0 anchors"))

    # 9. Stage 2a observations
    n_obs = conn.execute(
        """SELECT COUNT(*) FROM wa_session_b_findings
           WHERE registry_id=? AND delete_flag=0
           AND finding_type IN ('OBSERVATION','OBSERVATION_REGISTER')""",
        (registry_no,),
    ).fetchone()[0]
    if n_obs > 0:
        checks.append(("Stage 2a observations present", "PASS", f"{n_obs} observation findings"))
    else:
        checks.append(("Stage 2a observations present", "WARN",
                       "0 — fresh Stage 2a Unit 1–9 readings required during this session before Stage 2b can begin"))

    # 10. v2 Q&A coverage
    n_v2_links = conn.execute(
        """SELECT COUNT(DISTINCT l.question_id) FROM wa_finding_catalogue_links l
           JOIN wa_session_b_findings f ON f.id=l.finding_id
           JOIN wa_obs_question_catalogue q ON q.obs_id=l.question_id
           WHERE f.registry_id=? AND q.catalogue_version='v2-2026-04-29'
           AND (l.delete_flagged=0 OR l.delete_flagged IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    if n_v2_links == 0:
        checks.append(("v2 Q&A coverage (Stage 2b under v1.8)", "WARN",
                       "0/189 — Stage 2b is the work to be done in this session. Not a blocker."))
    elif n_v2_links < 189:
        checks.append(("v2 Q&A coverage", "WARN", f"{n_v2_links}/189 partial — Stage 2b session continues"))
    else:
        checks.append(("v2 Q&A coverage", "PASS", "Complete"))

    # 11. Stage 2c synthesis
    n_synth = conn.execute(
        """SELECT COUNT(*) FROM wa_session_b_findings
           WHERE registry_id=? AND finding_type LIKE 'SYNTHESIS_%' AND delete_flag=0""",
        (registry_no,),
    ).fetchone()[0]
    if n_synth == 0:
        checks.append(("Stage 2c synthesis (under v1.8)", "WARN",
                       "0/28 — Stage 2c is the work to be done. Not a blocker."))
    elif n_synth < 28:
        checks.append(("Stage 2c synthesis", "WARN", f"{n_synth}/28 partial"))
    else:
        checks.append(("Stage 2c synthesis", "PASS", "Complete"))

    # 12. Quality flags
    n_eviflag = conn.execute(
        """SELECT COUNT(*) FROM wa_data_quality_flags qf
           JOIN wa_file_index fi ON fi.id=qf.file_id
           WHERE fi.registry_id=?""",
        (registry_no,),
    ).fetchone()[0]
    checks.append(("Data quality flags reviewed", "INFO",
                   f"{n_eviflag} flag rows in `wa_data_quality_flags` — see data package §7"))

    # 13. SD pointers
    n_sp = conn.execute(
        """SELECT COUNT(*) FROM wa_session_research_flags
           WHERE registry_id=(SELECT id FROM word_registry WHERE no=?)
           AND flag_code='SD_POINTER' AND (resolved=0 OR resolved IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    checks.append(("SD pointers carried forward", "INFO",
                   f"{n_sp} open SD pointers — input to Stage 2c F-outcome decisions"))

    # 14. Open SB findings
    n_sb = conn.execute(
        """SELECT COUNT(*) FROM wa_session_research_flags
           WHERE registry_id=(SELECT id FROM word_registry WHERE no=?)
           AND flag_code='SB_FINDING' AND (resolved=0 OR resolved IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    if n_sb > 0:
        checks.append(("Open SB_FINDING flags", "WARN",
                       f"{n_sb} open — these are §N candidates per v1.8 §3 and must reach a closure outcome before session close"))
    else:
        checks.append(("Open SB_FINDING flags", "PASS", "0 open"))

    # 15. RESEARCHER_DECISION
    n_rd = conn.execute(
        """SELECT COUNT(*) FROM wa_session_research_flags
           WHERE registry_id=(SELECT id FROM word_registry WHERE no=?)
           AND flag_code='RESEARCHER_DECISION' AND (resolved=0 OR resolved IS NULL)""",
        (registry_no,),
    ).fetchone()[0]
    if n_rd > 0:
        checks.append(("Open RESEARCHER_DECISION items", "WARN",
                       f"{n_rd} open — surface to researcher; do not block"))
    else:
        checks.append(("Open RESEARCHER_DECISION items", "PASS", "0 open"))

    # Render
    pass_n = sum(1 for c in checks if c[1] == "PASS")
    warn_n = sum(1 for c in checks if c[1] == "WARN")
    fail_n = sum(1 for c in checks if c[1] == "FAIL")
    info_n = sum(1 for c in checks if c[1] == "INFO")
    verdict = "READY" if fail_n == 0 else "BLOCKED"
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
    P.append(f"*Generated by `scripts/_tmp_build_resubmission_artefacts.py` at {now_iso()}.*")
    return "\n".join(P)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--db", default=DB_PATH)
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row

    reg = conn.execute("SELECT word FROM word_registry WHERE no = ?", (args.registry,)).fetchone()
    if not reg:
        print(f"ERROR: registry {args.registry} not found")
        return 1
    word = reg["word"]
    out_dir = find_or_make_folder(args.registry, word)
    print(f"Output folder: {out_dir}")

    # 1. Analytic Status
    out = build_analytic_status(conn, args.registry)
    out_path = os.path.join(
        out_dir, f"wa-{args.registry:03d}-{word}-analytic-status-v1-20260430.md"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {out_path} ({len(out):,} chars)")

    # 2. Validation Report
    out = build_validation_report(conn, args.registry)
    out_path = os.path.join(
        out_dir, f"wa-{args.registry:03d}-{word}-readiness-validation-v1-20260430.md"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Wrote {out_path} ({len(out):,} chars)")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
