"""Fold the 2 Phase 10 FOLD-INTO-PROMPT items into M02 cluster_finding rows
using fallback lookup (Phase 11 main loader's exact-match query missed them).

Issue: AI's Phase 10 reconciliation pointed at VCG-level targets ([E-VCG-01/02/03/04],
[E-VCG-04]) but AI's Phase 9 authored those prompts at sub-group level ([A,B,C,D,E])
or CLUSTER level. Exact match fails. This script uses fallback:
  1. Try exact VCG-level match
  2. Try sub-group-level match (same letter, vcg_scope=NULL)
  3. Try CLUSTER-level match (sg_id=NULL, vcg_scope=NULL)

Targets:
  - sbf.74 (R56 envy, DIM-56-001) → T0.3.2 [E-VCG-01/02/03/04]
  - srf.622 (R103 love) → T6.6.2 [E-VCG-04]
"""
from __future__ import annotations
import argparse, shutil, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
DIRECTIVE = "DIR-20260516-013-folds"
CLUSTER = "M02"
VERSION = "v1-20260516"

# (source, source_id, target_tcode, target_sg_letter, target_vcg_codes_list)
FOLDS = [
    ("sbf", 74, "T0.3.2", "E", ["M02-E-VCG-01", "M02-E-VCG-02", "M02-E-VCG-03", "M02-E-VCG-04"]),
    ("srf", 622, "T6.6.2", "E", ["M02-E-VCG-04"]),
]


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def backup_db() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = f"bible_research_backup_{ts}_{DIRECTIVE}.db"
    out = REPO / "backups" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def fetch_fold_source(conn, src: str, sid: int) -> dict:
    if src == "sbf":
        r = conn.execute("""
            SELECT sbf.id, sbf.finding_id, sbf.finding AS text,
                   wr.no AS registry_no, wr.word AS registry_word
            FROM wa_session_b_findings sbf
            LEFT JOIN word_registry wr ON wr.id = sbf.registry_id
            WHERE sbf.id=?
        """, (sid,)).fetchone()
    else:
        r = conn.execute("""
            SELECT srf.id, srf.flag_label AS finding_id, srf.description AS text,
                   wr.no AS registry_no, wr.word AS registry_word
            FROM wa_session_research_flags srf
            LEFT JOIN word_registry wr ON wr.id = srf.registry_id
            WHERE srf.id=?
        """, (sid,)).fetchone()
    return dict(r) if r else None


def find_target_row(conn, obs_id: int, sg_id: int | None, vcg_scope: str | None) -> int | None:
    """Try exact match, then fallback to sub-group level, then CLUSTER."""
    # Exact match (VCG-level)
    if vcg_scope:
        r = conn.execute("""
            SELECT id FROM cluster_finding
            WHERE obs_id=? AND cluster_code=? AND cluster_subgroup_id IS ?
              AND vcg_scope=? AND version=? AND COALESCE(delete_flagged,0)=0
        """, (obs_id, CLUSTER, sg_id, vcg_scope, VERSION)).fetchone()
        if r:
            return r["id"]
    # Sub-group level (sg_id set, vcg_scope NULL)
    if sg_id is not None:
        r = conn.execute("""
            SELECT id FROM cluster_finding
            WHERE obs_id=? AND cluster_code=? AND cluster_subgroup_id=?
              AND vcg_scope IS NULL AND version=? AND COALESCE(delete_flagged,0)=0
        """, (obs_id, CLUSTER, sg_id, VERSION)).fetchone()
        if r:
            return r["id"]
    # CLUSTER level
    r = conn.execute("""
        SELECT id FROM cluster_finding
        WHERE obs_id=? AND cluster_code=? AND cluster_subgroup_id IS NULL
          AND vcg_scope IS NULL AND version=? AND COALESCE(delete_flagged,0)=0
    """, (obs_id, CLUSTER, VERSION)).fetchone()
    return r["id"] if r else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"M02 Phase 11 fold patch — directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_db()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Fetch sub-group ids
    sg_map = {}
    for r in conn.execute("SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (CLUSTER,)):
        code = r["subgroup_code"].split("-")[-1]  # 'A' from 'M02-A'
        if code == "BOUNDARY":
            sg_map["BOUNDARY"] = r["id"]
        else:
            sg_map[code] = r["id"]

    # Fetch obs_map
    obs_map = {r["question_code"]: r["obs_id"] for r in conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue WHERE tier IS NOT NULL AND deleted=0"
    )}

    try:
        conn.execute("BEGIN")
        applied = 0
        for src, sid, tcode, sg_letter, vcg_codes in FOLDS:
            log(f"\nProcessing {src}.id={sid} → {tcode} [{sg_letter}, vcg={';'.join(vcg_codes)}]")
            fc = fetch_fold_source(conn, src, sid)
            if not fc:
                log(f"  WARN: source {src}.id={sid} not found")
                continue
            obs_id = obs_map.get(tcode)
            if not obs_id:
                log(f"  WARN: obs_id not found for {tcode}")
                continue
            sg_id = sg_map.get(sg_letter)
            vcg_scope = ";".join(vcg_codes)
            cf_id = find_target_row(conn, obs_id, sg_id, vcg_scope)
            if not cf_id:
                log(f"  WARN: no cluster_finding row found even after fallback")
                continue
            log(f"  Folding into cluster_finding.id={cf_id}")

            src_table = "wa_session_b_findings" if src == "sbf" else "wa_session_research_flags"
            fold_prefix = (f"\n\n**[Folded from {src_table}.id={sid}; "
                          f"finding_id={fc['finding_id']}; registry={fc['registry_word']}]**\n"
                          f"_(Phase 10 target was {tcode} [{sg_letter}-VCG-...]; folded into available {tcode} row via fallback)_\n")
            fold_body = fc["text"] or ""

            if not dry_run:
                conn.execute(
                    "UPDATE cluster_finding SET finding_text = COALESCE(finding_text,'') || ? WHERE id=?",
                    (fold_prefix + fold_body, cf_id)
                )
                note_append = f" | {DIRECTIVE}: folded into cluster_finding.id={cf_id}"
                if src == "sbf":
                    conn.execute(
                        "UPDATE wa_session_b_findings SET resolution_note = COALESCE(resolution_note,'') || ? WHERE id=?",
                        (note_append, sid)
                    )
                else:
                    conn.execute(
                        "UPDATE wa_session_research_flags SET resolved_note = COALESCE(resolved_note,'') || ? WHERE id=?",
                        (note_append, sid)
                    )
            applied += 1

        if dry_run:
            conn.execute("ROLLBACK")
            log("\nDRY-RUN — rolled back")
        else:
            conn.execute("COMMIT")
            log("\nCommitted")
        log(f"DONE — {applied} fold operations {'simulated' if dry_run else 'applied'}")
    except Exception as e:
        conn.execute("ROLLBACK")
        log(f"ERROR: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
