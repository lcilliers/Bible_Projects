"""_pilot_validate_readiness_v1_20260427.py — Readiness validation checklist.

Runs a fixed set of validation checks against the DB state for a registry
that has been through Phase A prose + readiness sweep. Outputs a per-registry
validation report (.md + .json) recording PASS / WARN / FAIL on each check.

When all FAIL = 0, the registry is cleared for handoff to Session B Stage 2
(analysis-output instruction).

Checks implemented:

  C01  Schema version at 3.17.0 (M40-M43 applied)
  C02  Engine audit clean — last_automation_run = 'AUDITED'
  C03  Phase 1 status Complete
  C04  Verse Context registry status Complete
  C05  Dimension Review registry status Complete
  C06  Phase A prose captured — 6 prose_section rows under source_stage='session_a'
  C07  Readiness sweep produced — paired .md + .json in 07_Analysis_Readiness_Status/
  C08  Term inventory non-empty and at least 1 verse per OWNER term
  C09  All VC groups have a dimension assignment
  C10  Every group has at least 1 anchor verse
  C11  No group with extreme set-aside ratio (>90%) — possible VC drift signal
  C12  Per-term legacy-VC caveat surfaced (informational; vc_status='not_done' allowed)
  C13  Dimension confidence — note any 'queried' (researcher-flagged) assignments
  C14  No DATA_ANOMALY_* findings open for this registry
  C15  Researcher fields (inference_note / word_synopsis) — informational only

Verdict mapping:
  PASS — check satisfied
  WARN — informational; surfaces in §N of readiness output for AI to address
  FAIL — blocking; readiness cannot hand off to analysis-output

Usage:
  python scripts/_pilot_validate_readiness_v1_20260427.py --registry N
  python scripts/_pilot_validate_readiness_v1_20260427.py --registry N --json-only
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
OUT_DIR = os.path.join("Sessions", "Session_B", "07_Analysis_Readiness_Status")
EXPECTED_SCHEMA = "3.17.0"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def get_word_for_registry(conn, registry_no: int) -> str:
    r = conn.execute("SELECT word FROM word_registry WHERE no = ?", (registry_no,)).fetchone()
    return r[0] if r else f"reg{registry_no:03d}"


# ── Individual checks ────────────────────────────────────────────────────────


def check_schema_version(conn) -> dict:
    r = conn.execute("SELECT version_code FROM schema_version ORDER BY id DESC LIMIT 1").fetchone()
    actual = r[0] if r else None
    if actual == EXPECTED_SCHEMA:
        return {"verdict": "PASS", "detail": f"schema_version = {actual}"}
    if actual and actual >= EXPECTED_SCHEMA:
        return {"verdict": "PASS", "detail": f"schema_version = {actual} (>= {EXPECTED_SCHEMA})"}
    return {"verdict": "FAIL", "detail": f"schema_version = {actual!r}; expected {EXPECTED_SCHEMA}"}


def check_engine_audit(conn, reg_no: int) -> dict:
    r = conn.execute(
        "SELECT last_automation_run FROM word_registry WHERE no = ?", (reg_no,)
    ).fetchone()
    val = r[0] if r else None
    if val == "AUDITED":
        return {"verdict": "PASS", "detail": "last_automation_run = 'AUDITED'"}
    return {"verdict": "WARN", "detail": f"last_automation_run = {val!r}; expected 'AUDITED'"}


def check_phase1_complete(conn, reg_no: int) -> dict:
    r = conn.execute(
        "SELECT phase1_status FROM word_registry WHERE no = ?", (reg_no,)
    ).fetchone()
    val = r[0] if r else None
    if val == "Complete":
        return {"verdict": "PASS", "detail": "phase1_status = 'Complete'"}
    return {"verdict": "FAIL", "detail": f"phase1_status = {val!r}; expected 'Complete'"}


def check_vc_complete(conn, reg_no: int) -> dict:
    r = conn.execute(
        "SELECT verse_context_status FROM word_registry WHERE no = ?", (reg_no,)
    ).fetchone()
    val = r[0] if r else None
    if val == "Complete":
        return {"verdict": "PASS", "detail": "verse_context_status = 'Complete'"}
    return {"verdict": "FAIL", "detail": f"verse_context_status = {val!r}; expected 'Complete'"}


def check_dim_review_complete(conn, reg_no: int) -> dict:
    r = conn.execute(
        "SELECT dim_review_status, dim_review_version FROM word_registry WHERE no = ?", (reg_no,)
    ).fetchone()
    if not r:
        return {"verdict": "FAIL", "detail": "registry not found"}
    status, version = r[0], r[1]
    if status == "Complete":
        return {"verdict": "PASS",
                "detail": f"dim_review_status = 'Complete' (version: {version or '(none)'})"}
    return {"verdict": "FAIL", "detail": f"dim_review_status = {status!r}; expected 'Complete'"}


def check_phase_a_prose(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT pst.code FROM prose_section ps
          JOIN prose_section_type pst ON pst.id = ps.section_type_id
         WHERE ps.registry_id = (SELECT id FROM word_registry WHERE no = ?)
           AND pst.source_stage = 'session_a'
           AND ps.superseded_by_id IS NULL
           AND (ps.delete_flagged = 0 OR ps.delete_flagged IS NULL)
         ORDER BY pst.sort_order
    """, (reg_no,)).fetchall()
    codes = [r[0] for r in rows]
    expected = ["sa_s1_d1", "sa_s1_d2", "sa_s1_d3", "sa_s1_d4", "sa_s1_d5", "sa_s1_d6"]
    if codes == expected:
        return {"verdict": "PASS", "detail": f"6/6 sa_s1_d* rows present"}
    missing = [c for c in expected if c not in codes]
    return {"verdict": "FAIL",
            "detail": f"{len(codes)}/6 sa_s1_d* rows; missing: {missing}. "
                      f"Run `python scripts/generate_session_a_extract.py --registry={reg_no}` "
                      f"per wa-sessiona-prose-instruction [current]."}


def check_readiness_output_present(reg_no: int, word: str) -> dict:
    out_dir = Path(OUT_DIR)
    if not out_dir.exists():
        return {"verdict": "FAIL", "detail": f"directory missing: {OUT_DIR}"}
    md_pattern = f"wa-{reg_no:03d}-{word}-readiness-output-v*.md"
    json_pattern = f"wa-{reg_no:03d}-{word}-readiness-output-v*.json"
    md_files = sorted(out_dir.glob(md_pattern))
    json_files = sorted(out_dir.glob(json_pattern))
    if md_files and json_files:
        return {"verdict": "PASS",
                "detail": f"latest .md: {md_files[-1].name}; latest .json: {json_files[-1].name}"}
    return {"verdict": "FAIL",
            "detail": f"missing readiness output for R{reg_no:03d}. "
                      f"Run `python scripts/_pilot_build_readiness_output_v2_20260426.py --registry {reg_no}`."}


def check_term_inventory(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT mt.strongs_number, mt.gloss, mt.status,
               (SELECT COUNT(*) FROM wa_verse_records vr
                  JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
                 WHERE ti.strongs_number = mt.strongs_number
                   AND ti.term_owner_type = 'OWNER'
                   AND ti.delete_flagged = 0
                   AND vr.delete_flagged = 0
                   AND vr.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk =
                       (SELECT id FROM word_registry WHERE no = ?))) AS verse_count
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
           AND mt.delete_flagged = 0
           AND mt.status IN ('extracted', 'extracted_thin')
         ORDER BY mt.strongs_number
    """, (reg_no, reg_no)).fetchall()
    if not rows:
        return {"verdict": "FAIL", "detail": "no active OWNER terms"}
    zero_verse = [r[0] for r in rows if r[3] == 0]
    if zero_verse:
        return {"verdict": "WARN",
                "detail": f"{len(rows)} OWNER terms; {len(zero_verse)} with 0 verses: {zero_verse}"}
    return {"verdict": "PASS", "detail": f"{len(rows)} OWNER terms, all with ≥1 verse"}


def check_groups_have_dimensions(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT vcg.group_code, di.dimension
          FROM verse_context_group vcg
          JOIN mti_terms mt ON mt.id = vcg.mti_term_id
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id
                                          AND di.delete_flagged = 0
         WHERE fi.word_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
           AND vcg.delete_flagged = 0
    """, (reg_no,)).fetchall()
    if not rows:
        return {"verdict": "FAIL", "detail": "no VC groups for registry"}
    no_dim = [r[0] for r in rows if not r[1]]
    if no_dim:
        return {"verdict": "FAIL",
                "detail": f"{len(rows)} groups; {len(no_dim)} without dimension: {no_dim[:5]}"}
    return {"verdict": "PASS", "detail": f"{len(rows)}/{len(rows)} groups have dimension assignments"}


def check_groups_have_anchors(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT vcg.group_code, di.anchor_count
          FROM verse_context_group vcg
          JOIN mti_terms mt ON mt.id = vcg.mti_term_id
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id
                                          AND di.delete_flagged = 0
         WHERE fi.word_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
           AND vcg.delete_flagged = 0
    """, (reg_no,)).fetchall()
    if not rows:
        return {"verdict": "FAIL", "detail": "no VC groups for registry"}
    no_anchor = [r[0] for r in rows if (r[1] or 0) == 0]
    if no_anchor:
        return {"verdict": "WARN",
                "detail": f"{len(no_anchor)}/{len(rows)} groups without an anchor: {no_anchor[:5]}"}
    return {"verdict": "PASS", "detail": f"{len(rows)}/{len(rows)} groups have ≥1 anchor"}


def check_set_aside_ratio(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT vcg.group_code, di.anchor_count, di.related_count, di.set_aside_count, di.total_verse_count
          FROM verse_context_group vcg
          JOIN mti_terms mt ON mt.id = vcg.mti_term_id
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id
                                          AND di.delete_flagged = 0
         WHERE fi.word_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
           AND vcg.delete_flagged = 0
    """, (reg_no,)).fetchall()
    extreme = []
    for r in rows:
        total = r[4] or 0
        sa = r[3] or 0
        if total > 0 and (sa / total) > 0.90:
            extreme.append(f"{r[0]} ({sa}/{total} = {sa/total*100:.0f}%)")
    if extreme:
        return {"verdict": "WARN",
                "detail": f"{len(extreme)} group(s) with set-aside > 90%: {extreme}. Possible VC drift; review Stage 2a."}
    return {"verdict": "PASS", "detail": "no group at extreme set-aside ratio (all ≤ 90%)"}


def check_legacy_vc_caveat(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT mt.strongs_number, mt.vc_status
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
         WHERE fi.word_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
           AND mt.delete_flagged = 0
           AND mt.status IN ('extracted', 'extracted_thin')
    """, (reg_no,)).fetchall()
    legacy = [r[0] for r in rows if (r[1] or "not_done") == "not_done"]
    if legacy and len(legacy) == len(rows):
        return {"verdict": "WARN",
                "detail": f"all {len(rows)} OWNER terms are legacy-VC (vc_status='not_done'). "
                          f"§K of readiness output instructs AI to flag any material dependence. "
                          f"Not blocking, but registry has not been re-classified under v3 contracts."}
    if legacy:
        return {"verdict": "WARN",
                "detail": f"{len(legacy)}/{len(rows)} OWNER terms legacy-VC: {legacy[:5]}. Mixed-state."}
    return {"verdict": "PASS", "detail": f"all {len(rows)} OWNER terms have vc_status set under v3 contracts"}


def check_dimension_confidence(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT vcg.group_code, di.dimension_confidence, di.dimension
          FROM verse_context_group vcg
          JOIN mti_terms mt ON mt.id = vcg.mti_term_id
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type = 'OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          LEFT JOIN wa_dimension_index di ON di.verse_context_group_id = vcg.id
                                          AND di.delete_flagged = 0
         WHERE fi.word_registry_fk = (SELECT id FROM word_registry WHERE no = ?)
           AND vcg.delete_flagged = 0
    """, (reg_no,)).fetchall()
    by_conf = {}
    queried = []
    for r in rows:
        c = (r[1] or "(null)").strip()
        by_conf[c] = by_conf.get(c, 0) + 1
        if c.lower() == "queried":
            queried.append(r[0])
    summary = ", ".join(f"{k}: {v}" for k, v in sorted(by_conf.items()))
    if queried:
        return {"verdict": "WARN",
                "detail": f"dimension_confidence: {summary}. Queried groups (researcher-flagged) — review at Stage 2: {queried}"}
    if "confirmed" not in {k.lower() for k in by_conf}:
        return {"verdict": "WARN",
                "detail": f"dimension_confidence: {summary}. No 'confirmed' assignments — Session B can promote during Stage 2."}
    return {"verdict": "PASS", "detail": f"dimension_confidence: {summary}"}


def check_open_anomalies(conn, reg_no: int) -> dict:
    rows = conn.execute("""
        SELECT finding_id, finding_type, SUBSTR(finding, 1, 80) AS f
          FROM wa_session_b_findings
         WHERE registry_id = (SELECT id FROM word_registry WHERE no = ?)
           AND finding_type LIKE 'DATA_ANOMALY_%'
           AND status = 'open'
           AND (delete_flag = 0 OR delete_flag IS NULL)
    """, (reg_no,)).fetchall()
    if not rows:
        return {"verdict": "PASS", "detail": "no open DATA_ANOMALY_* findings for this registry"}
    samples = [f"{r[0]} ({r[1]})" for r in rows[:5]]
    return {"verdict": "FAIL",
            "detail": f"{len(rows)} open DATA_ANOMALY_* findings: {samples}. Resolve before handoff."}


def check_researcher_fields(conn, reg_no: int) -> dict:
    r = conn.execute(
        "SELECT inference_note, word_synopsis FROM word_registry WHERE no = ?", (reg_no,)
    ).fetchone()
    if not r:
        return {"verdict": "FAIL", "detail": "registry not found"}
    parts = []
    parts.append(f"inference_note: {'present' if r[0] else 'absent'}")
    parts.append(f"word_synopsis: {'present' if r[1] else 'absent'}")
    if r[0] and r[1]:
        return {"verdict": "PASS", "detail": "; ".join(parts)}
    return {"verdict": "WARN",
            "detail": "; ".join(parts) + ". Researcher-authored fields are informational; absence is not blocking."}


# ── Driver ───────────────────────────────────────────────────────────────────


CHECKS = [
    ("C01", "Schema version", "schema"),
    ("C02", "Engine audit clean", "registry"),
    ("C03", "Phase 1 status", "registry"),
    ("C04", "Verse Context status", "registry"),
    ("C05", "Dimension Review status", "registry"),
    ("C06", "Phase A prose captured", "prose"),
    ("C07", "Readiness output present", "filesystem"),
    ("C08", "Term inventory health", "terms"),
    ("C09", "All groups have dimensions", "dimensions"),
    ("C10", "All groups have anchors", "dimensions"),
    ("C11", "Set-aside ratio", "vc"),
    ("C12", "Legacy-VC caveat", "vc"),
    ("C13", "Dimension confidence", "dimensions"),
    ("C14", "No open DATA_ANOMALY_* findings", "findings"),
    ("C15", "Researcher fields", "registry"),
]


def run_all(conn, reg_no: int, word: str) -> dict:
    return {
        "C01": check_schema_version(conn),
        "C02": check_engine_audit(conn, reg_no),
        "C03": check_phase1_complete(conn, reg_no),
        "C04": check_vc_complete(conn, reg_no),
        "C05": check_dim_review_complete(conn, reg_no),
        "C06": check_phase_a_prose(conn, reg_no),
        "C07": check_readiness_output_present(reg_no, word),
        "C08": check_term_inventory(conn, reg_no),
        "C09": check_groups_have_dimensions(conn, reg_no),
        "C10": check_groups_have_anchors(conn, reg_no),
        "C11": check_set_aside_ratio(conn, reg_no),
        "C12": check_legacy_vc_caveat(conn, reg_no),
        "C13": check_dimension_confidence(conn, reg_no),
        "C14": check_open_anomalies(conn, reg_no),
        "C15": check_researcher_fields(conn, reg_no),
    }


VERDICT_GLYPH = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗"}


def render_md(reg_no: int, word: str, results: dict) -> str:
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for r in results.values():
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    overall = "READY" if counts["FAIL"] == 0 else "BLOCKED"

    L = []
    L.append(f"# Readiness Validation — R{reg_no:03d} {word}")
    L.append("")
    L.append(f"_Generated {now_iso()}_")
    L.append("")
    L.append("## Verdict")
    L.append("")
    L.append(f"**Overall: {overall}** — PASS={counts['PASS']}  WARN={counts['WARN']}  FAIL={counts['FAIL']}")
    L.append("")
    if overall == "READY":
        L.append("Registry has cleared all blocking checks. Cleared for handoff to Session B Stage 2 "
                 "(per wa-sessionb-analysis-output [current]). WARN items are informational and "
                 "should be addressed during Stage 2a where they affect findings.")
    else:
        L.append("Registry has at least one FAIL. Resolve the failing checks before handing off to "
                 "Session B Stage 2.")
    L.append("")
    L.append("## Checks")
    L.append("")
    L.append("| ID | Check | Verdict | Detail |")
    L.append("|---|---|---|---|")
    for code, label, _category in CHECKS:
        r = results[code]
        verdict = f"{VERDICT_GLYPH[r['verdict']]} {r['verdict']}"
        detail = r["detail"].replace("\n", " ")
        L.append(f"| {code} | {label} | {verdict} | {detail} |")
    L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=int, required=True)
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--out-dir", default=OUT_DIR)
    ap.add_argument("--json-only", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    word = get_word_for_registry(conn, args.registry).replace(" ", "_").lower()
    results = run_all(conn, args.registry, word)
    conn.close()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = f"wa-{args.registry:03d}-{word}-readiness-validation-v1-{today_compact()}"

    payload = {
        "meta": {
            "registry_no": args.registry,
            "word": word,
            "generated_at": now_iso(),
            "schema_expected": EXPECTED_SCHEMA,
            "checks_run": len(CHECKS),
        },
        "verdict_summary": {
            "PASS": sum(1 for r in results.values() if r["verdict"] == "PASS"),
            "WARN": sum(1 for r in results.values() if r["verdict"] == "WARN"),
            "FAIL": sum(1 for r in results.values() if r["verdict"] == "FAIL"),
        },
        "overall": "READY" if all(r["verdict"] != "FAIL" for r in results.values()) else "BLOCKED",
        "checks": [
            {"id": code, "label": label, "category": cat, **results[code]}
            for code, label, cat in CHECKS
        ],
    }

    json_path = out_dir / f"{base}.json"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    if not args.json_only:
        md_path = out_dir / f"{base}.md"
        md_path.write_text(render_md(args.registry, word, results), encoding="utf-8")

    # Console summary
    print(f"Validation: {payload['overall']}  "
          f"PASS={payload['verdict_summary']['PASS']}  "
          f"WARN={payload['verdict_summary']['WARN']}  "
          f"FAIL={payload['verdict_summary']['FAIL']}")
    for code, label, _ in CHECKS:
        r = results[code]
        print(f"  {VERDICT_GLYPH[r['verdict']]} {code} {label}: {r['detail'][:90]}")
    print()
    print(f"Wrote: {json_path}")
    if not args.json_only:
        print(f"Wrote: {out_dir / (base + '.md')}")

    return 0 if payload["overall"] == "READY" else 1


if __name__ == "__main__":
    sys.exit(main())
