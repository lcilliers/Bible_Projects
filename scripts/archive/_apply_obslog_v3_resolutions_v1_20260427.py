"""_apply_obslog_v3_resolutions_v1_20260427.py

Process the v3 revision obslog for goodness — resolve the 28 open items,
write 8 new SD pointers, 3 new GAP questions, and 8 catalogue coverage
fills. One-off script: this is the first revision-style obslog, validating
the architecture v2 §N resolution flow.

Inputs:
  - data/imports/WA/Patches/wa-067-goodness-obslog-v3-20260427.md

Operations (in transaction):
  - For each §N Resolution: update wa_session_b_findings.status to
    resolved_qa / resolved_sd / not_relevant; set obsolete_reason or
    related_finding_id where applicable; insert
    wa_finding_catalogue_links rows for Q&A resolutions
  - Insert 8 new SD pointers in wa_session_research_flags
  - Insert 3 new GAP questions in wa_obs_question_catalogue
  - Update or insert no_finding catalogue links to proper coverage
  - Pre-write backup; transactional commit

Run --dry-run first; commits only with --live.
"""
from __future__ import annotations
import argparse
import os
import re
import shutil
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("data", "bible_research.db")
OBSLOG_PATH = os.path.join("data", "imports", "WA", "Patches",
                          "wa-067-goodness-obslog-v3-20260427.md")
BACKUP_DIR = "backups"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


# ── Resolution-block parser ────────────────────────────────────────────────


def parse_resolutions(text: str) -> list:
    """Each block: ### §N Resolution NNN — OBS-067-OBS-NNN ... ---"""
    out = []
    block_re = re.compile(
        r"^###\s+§N\s+Resolution\s+\d+\s+—\s+(OBS-\d+-OBS-\d+)\s*\n((?:.|\n)*?)(?=\n###\s+§N\s+Resolution|\n##\s)",
        re.MULTILINE,
    )
    for m in block_re.finditer(text):
        finding_label = m.group(1).strip()
        body = m.group(2)
        # Match flexible Outcome line — full text inside ** ** then take leading keyword
        outcome_m = re.search(r"\*\*Outcome:\s*([^\n]+?)\*\*", body)
        outcome_full = outcome_m.group(1).strip() if outcome_m else ""
        outcome = outcome_full.upper()
        # Categorise into canonical buckets
        if "Q&A" in outcome and "GAP" not in outcome:
            outcome = "RESOLVE VIA Q&A"
        elif "SD" in outcome and "POINTER" in outcome:
            outcome = "SD POINTER"
        elif "NOT_RELEVANT" in outcome or "NOT RELEVANT" in outcome:
            outcome = "NOT_RELEVANT"
        elif "GAP" in outcome:
            outcome = "GAP QUESTION"
        # SD pointer detail block — accept optional parenthetical/notes after the closing **
        sp_m = re.search(
            r"\*\*SD_POINTER\s+—\s+(SP-\d+-\d+)\*\*[^\n]*\n((?:- .+\n)+)",
            body,
        )
        sp_data = None
        if sp_m:
            sp_id = sp_m.group(1)
            sp_fields = {}
            for ln in sp_m.group(2).split("\n"):
                ln = ln.strip()
                if ln.startswith("- ") and ":" in ln:
                    k, v = ln[2:].split(":", 1)
                    sp_fields[k.strip()] = v.strip()
            sp_data = {"sp_id": sp_id, **sp_fields}

        # Citation line: 'Citation: OBS-... → Q### (catalogue Section X) · coverage: ...'
        cite_m = re.search(
            r"\*\*Citation:\*\*\s*(.+?)$",
            body, re.MULTILINE,
        )
        # Q-codes referenced (e.g. Q002, Q036) — multiple possible
        q_codes = []
        cov = None
        if cite_m:
            cite_text = cite_m.group(1)
            q_codes = re.findall(r"\bQ(\d{3})\b", cite_text)
            cov_m = re.search(r"coverage:\s*(\w+)", cite_text)
            if cov_m:
                cov = cov_m.group(1).strip().lower()

        # obsolete_reason for NOT_RELEVANT
        obs_reason = None
        or_m = re.search(r"\*\*obsolete_reason:\*\*\s*(.+?)$", body, re.MULTILINE)
        if or_m:
            obs_reason = or_m.group(1).strip()
        else:
            reason_m = re.search(r"\*\*Reason:\*\*\s*(.+?)$", body, re.MULTILINE)
            if reason_m:
                obs_reason = reason_m.group(1).strip()

        # Free-form "Outcome:" body text — we use it as the Q&A answer
        outcome_body_m = re.search(
            r"\*\*Outcome:.+?\*\*\s*\n+((?:.|\n)+?)(?=\n\*\*Citation:|\n\*\*obsolete_reason:|\n\*\*SD_POINTER|\n---|$)",
            body, re.DOTALL,
        )
        answer_text = outcome_body_m.group(1).strip() if outcome_body_m else None

        # GAP question reference (e.g. "GAP-N-001")
        gap_refs = re.findall(r"GAP-N-\d+", body)

        out.append({
            "finding_label": finding_label,
            "outcome": outcome,
            "q_codes": q_codes,
            "coverage": cov,
            "answer_text": answer_text,
            "sd_pointer": sp_data,
            "obsolete_reason": obs_reason,
            "gap_refs": gap_refs,
            "raw_body": body,
        })
    return out


def parse_new_gap_questions(text: str) -> list:
    """## New GAP Questions — This Session ... blocks"""
    section_m = re.search(r"##\s+New GAP Questions\s+—\s+This Session\s*\n((?:.|\n)+?)(?=\n##\s|\Z)", text)
    if not section_m:
        return []
    body = section_m.group(1)
    out = []
    for m in re.finditer(
        r"\*\*GAP-N-(\d+)\*\*\s*\(from\s+(OBS-\d+-OBS-\d+)\):\s*\n+>\s*(.+?)(?=\n\*\*GAP-N-|\n---|\Z)",
        body, re.DOTALL,
    ):
        out.append({
            "code": f"GAP-N-{m.group(1)}",
            "source_finding": m.group(2),
            "question_text": m.group(3).strip().replace("\n>", "").replace("\n", " "),
        })
    return out


def parse_no_finding_fills(text: str) -> list:
    """## Catalogue Coverage — no_finding Items section"""
    section_m = re.search(
        r"##\s+Catalogue Coverage\s+—\s+no_finding\s+Items.*?\n((?:.|\n)+?)(?=\n##\s|\Z)",
        text, re.DOTALL,
    )
    if not section_m:
        return []
    body = section_m.group(1)
    out = []
    for m in re.finditer(
        r"\*\*Q(\d+)\*\*\s+—\s+(.+?)\n"
        r"Coverage assessment:\s+(\w+)\s*\n"
        r"Source:\s+(.+?)\n"
        r"((?:.|\n)+?)(?=\n\*\*Q\d+\*\*|\n---|\Z)",
        body, re.DOTALL,
    ):
        out.append({
            "q_code": "Q" + m.group(1).zfill(3),
            "question_summary": m.group(2).strip(),
            "coverage": m.group(3).strip().lower(),
            "source": m.group(4).strip(),
            "answer_text": m.group(5).strip(),
        })
    return out


# ── DB resolvers ──────────────────────────────────────────────────────────


def find_finding_by_label(conn, label: str) -> int | None:
    r = conn.execute(
        "SELECT id FROM wa_session_b_findings WHERE finding_id = ? "
        "AND (delete_flag = 0 OR delete_flag IS NULL)",
        (label,),
    ).fetchone()
    return r[0] if r else None


def find_question_id(conn, q_code: str) -> int | None:
    r = conn.execute(
        "SELECT obs_id FROM wa_obs_question_catalogue WHERE question_code = ? "
        "AND (deleted = 0 OR deleted IS NULL)",
        (q_code,),
    ).fetchone()
    return r[0] if r else None


# ── Apply ──────────────────────────────────────────────────────────────────


def apply_resolutions(conn, resolutions: list, registry_id: int, ctx: dict, dry: bool) -> dict:
    out = {
        "qa_resolved": 0, "sd_resolved": 0, "not_relevant": 0,
        "qa_links_inserted": 0, "sd_inserted": 0, "errors": [],
    }
    for r in resolutions:
        fid = find_finding_by_label(conn, r["finding_label"])
        if not fid:
            out["errors"].append(f"Finding {r['finding_label']} not found")
            continue

        if "Q&A" in r["outcome"] or "QA" in r["outcome"] or "RESOLVE VIA" in r["outcome"]:
            # Q&A resolution: insert links + lifecycle update
            for q_num in r["q_codes"]:
                q_code = "Q" + q_num.zfill(3)
                question_id = find_question_id(conn, q_code)
                if not question_id:
                    out["errors"].append(f"{r['finding_label']}: question {q_code} not in catalogue")
                    continue
                # Idempotency: UNIQUE(finding_id, question_id)
                existing = conn.execute(
                    "SELECT id FROM wa_finding_catalogue_links "
                    "WHERE finding_id = ? AND question_id = ? "
                    "AND (delete_flagged = 0 OR delete_flagged IS NULL)",
                    (fid, question_id),
                ).fetchone()
                if existing:
                    continue
                if not dry:
                    conn.execute("""
                        INSERT INTO wa_finding_catalogue_links
                            (finding_id, question_id, coverage, status,
                             mapped_date, validated_date, session_b_note)
                        VALUES (?, ?, ?, 'validated', ?, ?, ?)
                    """, (fid, question_id, r["coverage"] or "full",
                          ctx["ts"][:10], ctx["ts"][:10], r["answer_text"]))
                out["qa_links_inserted"] += 1
            if not dry:
                conn.execute(
                    "UPDATE wa_session_b_findings SET status = 'resolved_qa' "
                    "WHERE id = ? AND status = 'open'",
                    (fid,),
                )
            out["qa_resolved"] += 1

        elif "SD POINTER" in r["outcome"] or "SD_POINTER" in r["outcome"]:
            # Insert SD pointer + lifecycle update with related_finding_id
            sp = r["sd_pointer"]
            if not sp:
                out["errors"].append(f"{r['finding_label']}: SD outcome but no SP block parsed")
                continue
            flag_label = sp["sp_id"]
            existing = conn.execute(
                "SELECT id FROM wa_session_research_flags "
                "WHERE registry_id = ? AND flag_code = 'SD_POINTER' AND flag_label = ?",
                (registry_id, flag_label),
            ).fetchone()
            if not existing:
                cross_reg = sp.get("cross_registry_id")
                cross_id = None
                if cross_reg:
                    # Strip parenthetical descriptions; require numeric leading
                    m_n = re.match(r"\s*(\d+)\b", cross_reg)
                    if m_n:
                        cr = conn.execute("SELECT id FROM word_registry WHERE no = ?", (int(m_n.group(1)),)).fetchone()
                        cross_id = cr[0] if cr else None
                if not dry:
                    cur = conn.execute("""
                        INSERT INTO wa_session_research_flags
                            (registry_id, flag_code, flag_label, priority,
                             description, session_target, session_raised,
                             raised_date, resolved, cross_registry_id)
                        VALUES (?, 'SD_POINTER', ?, ?, ?, 'Session D', ?, ?, 0, ?)
                    """, (registry_id, flag_label,
                          sp.get("priority", "MEDIUM"),
                          sp.get("description", ""),
                          "Session B Stage 2 (revision via obslog v3)",
                          ctx["ts"], cross_id))
                    sd_id = cur.lastrowid
                else:
                    sd_id = None
                out["sd_inserted"] += 1
            else:
                sd_id = existing[0]
            # Lifecycle update on source finding (only if open)
            if not dry:
                conn.execute(
                    "UPDATE wa_session_b_findings SET status = 'resolved_sd', "
                    "related_finding_id = ? WHERE id = ? AND status = 'open'",
                    (sd_id, fid),
                )
            out["sd_resolved"] += 1

        elif "NOT_RELEVANT" in r["outcome"] or "NOT RELEVANT" in r["outcome"]:
            if not dry:
                conn.execute(
                    "UPDATE wa_session_b_findings SET status = 'not_relevant', "
                    "obsolete_reason = ?, obsolete_date = ? WHERE id = ? AND status = 'open'",
                    (r["obsolete_reason"] or "Closed not relevant", ctx["ts"], fid),
                )
            out["not_relevant"] += 1

        elif "GAP" in r["outcome"]:
            # Treated as Q&A for the linked Q-codes; the GAP itself is inserted
            # in the new GAP questions pass below
            for q_num in r["q_codes"]:
                q_code = "Q" + q_num.zfill(3)
                question_id = find_question_id(conn, q_code)
                if not question_id:
                    continue
                existing = conn.execute(
                    "SELECT id FROM wa_finding_catalogue_links "
                    "WHERE finding_id = ? AND question_id = ? "
                    "AND (delete_flagged = 0 OR delete_flagged IS NULL)",
                    (fid, question_id),
                ).fetchone()
                if existing:
                    continue
                if not dry:
                    conn.execute("""
                        INSERT INTO wa_finding_catalogue_links
                            (finding_id, question_id, coverage, status,
                             mapped_date, validated_date, session_b_note)
                        VALUES (?, ?, ?, 'validated', ?, ?, ?)
                    """, (fid, question_id, r["coverage"] or "partial",
                          ctx["ts"][:10], ctx["ts"][:10], r["answer_text"]))
                out["qa_links_inserted"] += 1
            if not dry:
                conn.execute(
                    "UPDATE wa_session_b_findings SET status = 'resolved_qa' "
                    "WHERE id = ? AND status = 'open'",
                    (fid,),
                )
            out["qa_resolved"] += 1
        else:
            out["errors"].append(f"{r['finding_label']}: unrecognised outcome '{r['outcome']}'")
    return out


def apply_gap_questions(conn, gap_qs: list, ctx: dict, dry: bool) -> dict:
    out = {"inserted": 0, "skipped": 0, "errors": []}
    cur = conn.execute("SELECT MAX(obs_id) FROM wa_obs_question_catalogue")
    next_obs_id = (cur.fetchone()[0] or 0) + 1
    for g in gap_qs:
        existing = conn.execute(
            "SELECT obs_id FROM wa_obs_question_catalogue WHERE question_code = ? "
            "AND (deleted = 0 OR deleted IS NULL)",
            (g["code"],),
        ).fetchone()
        if existing:
            out["skipped"] += 1
            continue
        if not dry:
            conn.execute("""
                INSERT INTO wa_obs_question_catalogue
                    (obs_id, question_code, section, source_word, source_registry_no,
                     question_text, scope, status, deleted, date_added, catalogue_version)
                VALUES (?, ?, ?, ?, ?, ?, 'universal', 'active', 0, ?, ?)
            """, (next_obs_id, g["code"],
                  "Generic — Gap (R067 obslog v3)",
                  ctx["word"], ctx["registry_id"],
                  g["question_text"], ctx["ts"][:10],
                  f"v2.1-R{ctx['registry_no']:03d}"))
        next_obs_id += 1
        out["inserted"] += 1
    return out


def apply_no_finding_fills(conn, fills: list, registry_id: int, ctx: dict, dry: bool) -> dict:
    """For each no_finding now properly addressed, update or insert the catalogue link."""
    out = {"updated": 0, "inserted": 0, "skipped": 0, "errors": []}
    for f in fills:
        question_id = find_question_id(conn, f["q_code"])
        if not question_id:
            out["errors"].append(f"{f['q_code']}: not in catalogue")
            continue
        # Existing no_finding link for this registry-scoped finding (NULL finding_id case)
        existing = conn.execute(
            "SELECT id, coverage FROM wa_finding_catalogue_links "
            "WHERE question_id = ? AND finding_id IS NULL "
            "AND (delete_flagged = 0 OR delete_flagged IS NULL)",
            (question_id,),
        ).fetchone()
        if existing:
            link_id, current_cov = existing
            if current_cov != f["coverage"]:
                if not dry:
                    conn.execute(
                        "UPDATE wa_finding_catalogue_links SET coverage = ?, "
                        "session_b_note = ?, validated_date = ? WHERE id = ?",
                        (f["coverage"], f["answer_text"], ctx["ts"][:10], link_id),
                    )
                out["updated"] += 1
            else:
                out["skipped"] += 1
        else:
            if not dry:
                conn.execute("""
                    INSERT INTO wa_finding_catalogue_links
                        (finding_id, question_id, coverage, status,
                         mapped_date, validated_date, session_b_note)
                    VALUES (NULL, ?, ?, 'validated', ?, ?, ?)
                """, (question_id, f["coverage"], ctx["ts"][:10],
                      ctx["ts"][:10], f["answer_text"]))
            out["inserted"] += 1
    return out


# ── Main ──────────────────────────────────────────────────────────────────


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obslog", default=OBSLOG_PATH)
    ap.add_argument("--registry", type=int, default=67)
    ap.add_argument("--db", default=DB_PATH)
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    with open(args.obslog, encoding="utf-8") as f:
        text = f.read()

    resolutions = parse_resolutions(text)
    gap_qs = parse_new_gap_questions(text)
    fills = parse_no_finding_fills(text)

    print(f"Parsed: {len(resolutions)} resolutions · {len(gap_qs)} new GAP qs · {len(fills)} no_finding fills")
    by_outcome = {}
    for r in resolutions:
        by_outcome[r["outcome"]] = by_outcome.get(r["outcome"], 0) + 1
    for k, v in by_outcome.items():
        print(f"  {k!r}: {v}")

    if args.live:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup = os.path.join(BACKUP_DIR,
                              f"bible_research_pre_obslog_v3_{today_compact()}.db")
        shutil.copy2(args.db, backup)
        print(f"\nBackup: {backup}")

    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA foreign_keys = ON")
    reg_row = conn.execute("SELECT id, word FROM word_registry WHERE no = ?", (args.registry,)).fetchone()
    ctx = {
        "registry_id": reg_row[0],
        "registry_no": args.registry,
        "word": reg_row[1],
        "ts": now_iso(),
    }

    try:
        if args.live:
            conn.execute("BEGIN")

        # 1. New GAP questions first (so resolution Q-code lookups can find them)
        gap_result = apply_gap_questions(conn, gap_qs, ctx, dry=not args.live)
        # 2. Resolutions
        res_result = apply_resolutions(conn, resolutions, ctx["registry_id"], ctx, dry=not args.live)
        # 3. No_finding fills
        fill_result = apply_no_finding_fills(conn, fills, ctx["registry_id"], ctx, dry=not args.live)

        if args.live:
            errors = res_result["errors"] + gap_result["errors"] + fill_result["errors"]
            if errors:
                conn.rollback()
                print("\nERRORS — rolled back:")
                for e in errors:
                    print(f"  - {e}")
                return 1
            conn.commit()
            print("\n[LIVE] committed.")
        else:
            print("\n[DRY-RUN] no writes attempted.")
    finally:
        conn.close()

    print("\n--- Summary ---")
    print(f"Resolutions: qa_resolved={res_result['qa_resolved']} · "
          f"sd_resolved={res_result['sd_resolved']} · "
          f"not_relevant={res_result['not_relevant']} · "
          f"qa_links_inserted={res_result['qa_links_inserted']} · "
          f"sd_inserted={res_result['sd_inserted']}")
    print(f"GAP questions: inserted={gap_result['inserted']} · skipped={gap_result['skipped']}")
    print(f"no_finding fills: updated={fill_result['updated']} · inserted={fill_result['inserted']} · skipped={fill_result['skipped']}")
    all_errors = res_result["errors"] + gap_result["errors"] + fill_result["errors"]
    if all_errors:
        print(f"\n{len(all_errors)} error(s):")
        for e in all_errors:
            print(f"  - {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
