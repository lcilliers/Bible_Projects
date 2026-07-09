"""_apply_m15_dir024_phase9_findings_v1_20260512.py — DB-modifying.

Apply DIR-20260512-001 (M15 Phase 9 findings record) + FLAG-M15-006
(stray cha.shav verses → M15-E-VCG05) prerequisite.

Operations (single transaction, foreign_keys=ON):

  Phase 0 — Backup
  Phase 1 — FLAG-M15-006: assign 5 stray H2803G cha.shav verses
            (vr_ids 54610/11/12/13/26) to M15-E-VCG05 (vcg_id 3674)
  Phase 2 — Parse 4 consolidated-findings part files
  Phase 3 — INSERT cluster_finding rows (M06 authored-only pattern)
  Phase 4 — Verification queries (status counts, gap list, sb_findings
             unchanged, FLAG-006 confirmed)

Catalogue version recorded: v2-20260511 (per directive §6).
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIRECTIVE_ID = "DIR-20260512-001"
CLUSTER_CODE = "M15"
CATALOGUE_VERSION = "v2-20260511"
OBSLOG_REF = "wa-obslog-M15-phase8-v2-20260511.md"
PHASE9_DIR = os.path.join("Sessions", "Session_Clusters", "M15", "files phase 9")
PART_FILES = [
    "WA-M15-consolidated-findings-v1-20260511-part1.md",
    "WA-M15-consolidated-findings-v1-20260511-part2-T2.md",
    "WA-M15-consolidated-findings-v1-20260511-part3-T3-T4.md",
    "WA-M15-consolidated-findings-v1-20260511-part4-T5-T7.md",
]

# FLAG-M15-006
FLAG006_VR_IDS = [54610, 54611, 54612, 54613, 54626]
FLAG006_TARGET_VCG_CODE = "M15-E-VCG05"

# Sub-group letter → cluster_subgroup id (filled in main())
SG_LETTER_TO_ID: dict[str, int | None] = {
    "A": None, "B": None, "C": None, "D": None,
    "E": None, "F": None, "G": None, "H": None,
}

# Parse markers
_PROMPT_RE = re.compile(r"^####\s+(T\d+\.\d+\.\d+)\b")
_SCOPE_RE = re.compile(r"^\*\*\[(.+?)\]\*\*\s*(.*)$")
_OUTCOME_RE = re.compile(r"^([ESG])\s*[—–-]\s*(.+)$")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR,
                     f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, p)
    return p


def parse_scope(scope_raw: str) -> list[tuple[str, str | None]]:
    """Return list of (scope_key, status_override).

    Scope keys: 'A'..'H' (sub-groups) or 'CLUSTER' or 'BOUNDARY'.
    Status override is 'cluster_synthesis' for CLUSTER variants, else None.
    Multi-scope markers like [A, B, C] return multiple tuples.
    """
    s = scope_raw.strip()
    # CLUSTER variants
    if s == "CLUSTER" or s.startswith("CLUSTER —") or s.startswith("CLUSTER -") \
            or s.lower().startswith("cluster-level finding"):
        return [("CLUSTER", "cluster_synthesis")]
    if s == "BOUNDARY" or s.startswith("BOUNDARY —"):
        return [("BOUNDARY", None)]
    # Multi-scope like [A, B, C, D, E, G, H]
    if "," in s.split(" — ")[0]:
        # Take the part before any " — Label" and split on comma
        head = s.split(" — ")[0]
        letters = [p.strip() for p in head.split(",")]
        out: list[tuple[str, str | None]] = []
        for L in letters:
            L = L.strip()
            if L in ("A", "B", "C", "D", "E", "F", "G", "H"):
                out.append((L, None))
        if out:
            return out
    # Single sub-group [X — Label] or [X]
    m = re.match(r"^([A-H])\b", s)
    if m:
        return [(m.group(1), None)]
    return []


def parse_outcome(rest: str) -> tuple[str | None, str]:
    """rest is text after the **[scope]** marker.
    Detect leading 'E —', 'S —', or 'G —'.
    Returns (finding_status, cleaned_text).
    """
    r = rest.lstrip()
    m = _OUTCOME_RE.match(r)
    if m:
        letter = m.group(1)
        text = m.group(2).strip()
        status = {"E": "finding", "S": "silent", "G": "gap"}[letter]
        return status, text
    return None, r


def parse_part_file(path: str) -> list[dict]:
    """Return list of {qcode, scope_key, status, text, source_file}."""
    src = os.path.basename(path)
    rows: list[dict] = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_q: str | None = None
    current_scopes: list[tuple[str, str | None]] | None = None
    current_status: str | None = None
    buf: list[str] = []

    def flush():
        nonlocal current_scopes, current_status, buf
        if current_q and current_scopes is not None:
            text = "\n".join(buf).strip()
            for scope_key, override in current_scopes:
                status = override or current_status or "finding"
                rows.append({
                    "qcode": current_q,
                    "scope_key": scope_key,
                    "status": status,
                    "text": text,
                    "source_file": src,
                })
        current_scopes = None
        current_status = None
        buf = []

    for raw in lines:
        line = raw.rstrip("\n")
        # Skip separator
        if line.strip() == "---":
            flush()
            continue
        # Prompt header
        m = _PROMPT_RE.match(line)
        if m:
            flush()
            current_q = m.group(1)
            continue
        # Scope marker
        m = _SCOPE_RE.match(line)
        if m and current_q:
            flush()
            scope_raw = m.group(1)
            rest = m.group(2)
            scopes = parse_scope(scope_raw)
            if not scopes:
                continue
            override = scopes[0][1] if scopes else None
            # Parse leading outcome on the same line if present
            if rest:
                status, cleaned = parse_outcome(rest)
                current_scopes = scopes
                current_status = status
                if override == "cluster_synthesis" and not status:
                    current_status = "cluster_synthesis"
                buf = [cleaned] if cleaned else []
            else:
                current_scopes = scopes
                current_status = override
                buf = []
            continue
        # Continuation — check if next line begins with outcome code
        if current_scopes is not None and current_status is None:
            m2 = _OUTCOME_RE.match(line.lstrip())
            if m2:
                letter = m2.group(1)
                current_status = {"E": "finding", "S": "silent",
                                  "G": "gap"}[letter]
                buf.append(m2.group(2).strip())
                continue
        # Plain continuation
        if current_scopes is not None:
            if line.strip() != "":
                buf.append(line)
            elif buf:
                # Blank line ends the paragraph; keep accumulating in case
                # of multi-paragraph body
                buf.append("")
    flush()
    return rows


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply (M15 Phase 9 findings + FLAG-M15-006)")
    print(f"  Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    # Parse
    print("PARSE")
    print("-" * 72)
    all_rows: list[dict] = []
    per_file: dict[str, int] = {}
    for fn in PART_FILES:
        path = os.path.join(PHASE9_DIR, fn)
        rows = parse_part_file(path)
        per_file[fn] = len(rows)
        print(f"  {fn:55s} {len(rows):>4d}")
        all_rows.extend(rows)
    print(f"  TOTAL parsed: {len(all_rows)}")

    by_scope = Counter(r["scope_key"] for r in all_rows)
    by_status = Counter(r["status"] for r in all_rows)
    print(f"  by scope:  {dict(by_scope)}")
    print(f"  by status: {dict(by_status)}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    # Pre-flight
    print()
    print("PRE-FLIGHT")
    print("-" * 72)
    ok = True

    # Resolve sub-group ids
    for r in conn.execute("""
        SELECT id, subgroup_code FROM cluster_subgroup
         WHERE cluster_code='M15' AND COALESCE(delete_flagged,0)=0
    """):
        code = r["subgroup_code"]
        if code.startswith("M15-"):
            SG_LETTER_TO_ID[code.split("-")[-1]] = r["id"]
    BOUNDARY_ID = next((r["id"] for r in conn.execute("""
        SELECT id FROM cluster_subgroup
         WHERE cluster_code='M15' AND subgroup_code='BOUNDARY'
           AND COALESCE(delete_flagged,0)=0
    """)), None)
    print(f"  sub-group letter map: {SG_LETTER_TO_ID}")
    print(f"  BOUNDARY id: {BOUNDARY_ID}")
    for L in ("A", "B", "C", "D", "E", "F", "G", "H"):
        if SG_LETTER_TO_ID[L] is None:
            print(f"  [ERR] missing M15-{L}")
            ok = False

    # Existing M15 cluster_finding rows
    n_existing = conn.execute(
        "SELECT COUNT(*) FROM cluster_finding WHERE cluster_code=?",
        (CLUSTER_CODE,),
    ).fetchone()[0]
    print(f"  existing M15 cluster_finding rows: {n_existing}")
    if n_existing > 0:
        print(f"  [ERR] cluster_finding already has M15 rows — refusing to load")
        ok = False

    # FLAG-M15-006 — VCG exists, verses pending
    flag006_vcg = conn.execute(
        "SELECT id FROM verse_context_group "
        " WHERE group_code = ? AND COALESCE(delete_flagged,0)=0",
        (FLAG006_TARGET_VCG_CODE,),
    ).fetchone()
    if not flag006_vcg:
        print(f"  [ERR] {FLAG006_TARGET_VCG_CODE} not found")
        ok = False
    else:
        print(f"  [ok] {FLAG006_TARGET_VCG_CODE} id={flag006_vcg['id']}")

    # Resolve all 189 T-prompts (the full catalogue), not just authored
    obs_by_q = {r["question_code"]: r["obs_id"] for r in conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
        " WHERE question_code GLOB 'T[0-9]*' "
        " ORDER BY question_code"
    )}
    print(f"  [ok] {len(obs_by_q)} T-prompt qcodes resolved (full catalogue)")
    # Verify all parsed qcodes are in catalogue
    parsed_qcodes = {r["qcode"] for r in all_rows}
    missing_q = [q for q in parsed_qcodes if q not in obs_by_q]
    if missing_q:
        print(f"  [ERR] parsed qcodes not in catalogue: {missing_q[:10]}")
        ok = False
    not_parsed = sorted(set(obs_by_q) - parsed_qcodes)
    if not_parsed:
        print(f"  [info] {len(not_parsed)} catalogue prompts not in source "
              f"(will be stubbed): {not_parsed[:5]}…"
              if len(not_parsed) > 5 else
              f"  [info] {len(not_parsed)} catalogue prompts not in source "
              f"(will be stubbed): {not_parsed}")

    # Baseline sb_findings count for M15 terms
    sb_baseline = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings sbf
          JOIN mti_terms mt ON mt.id = sbf.term_id
         WHERE mt.cluster_code = 'M15'
    """).fetchone()[0]
    print(f"  wa_session_b_findings baseline (M15 terms): {sb_baseline}")

    print()
    if not ok:
        print("Pre-flight failed.")
        return 1

    if args.live:
        b = take_backup("m15_dir024_phase9_findings")
        print(f"Backup: {b}")
        print()

    counts: dict[str, int] = {}
    try:
        conn.execute("BEGIN")
        cur = conn.cursor()
        ts = now_iso()

        # Phase 1 — FLAG-M15-006
        print("Phase 1 — FLAG-M15-006: assign 5 stray cha.shav to M15-E-VCG05")
        print("-" * 72)
        flag006_vcg_id = flag006_vcg["id"]
        M15E_ID = SG_LETTER_TO_ID["E"]
        flag006_updated = 0
        for vr_id in FLAG006_VR_IDS:
            rc = cur.execute(
                "UPDATE verse_context "
                "   SET group_id = ?, "
                "       cluster_subgroup_id = ?, "
                "       is_relevant = 1, "
                "       set_aside_reason = NULL "
                " WHERE verse_record_id = ? "
                "   AND mti_term_id IN ("
                "       SELECT id FROM mti_terms WHERE strongs_number='H2803G'"
                "   ) "
                "   AND COALESCE(delete_flagged,0) = 0",
                (flag006_vcg_id, M15E_ID, vr_id),
            ).rowcount
            flag006_updated += rc
        counts["phase1_flag006_assignments"] = flag006_updated
        print(f"  {flag006_updated} verse_context rows updated")

        # Phase 2 — build cluster_finding rows (structural + full-text)
        print()
        print("Phase 2 — Build cluster_finding rows (structural + full-text)")
        print("-" * 72)
        notes_template = (
            f"{DIRECTIVE_ID} (Phase 9 findings load {today_compact()[:4]}-"
            f"{today_compact()[4:6]}-{today_compact()[6:]}); "
            f"source: {{src}}; obslog: {OBSLOG_REF}"
        )

        # Index authored rows by (qcode, scope_key); collapse same-scope
        # multiple entries by appending text.
        authored: dict[tuple[str, str], dict] = {}
        for r in all_rows:
            key = (r["qcode"], r["scope_key"])
            if key in authored:
                authored[key]["text"] = (
                    authored[key]["text"].rstrip() + "\n\n---\n\n" + r["text"])
                # Status: keep the strongest signal (finding > silent > gap)
            else:
                authored[key] = dict(r)
        print(f"  Authored cells (collapsed): {len(authored)}")

        # All qcodes that will be loaded — use full catalogue 189
        all_qcodes = sorted(obs_by_q.keys())

        insert_rows: list[tuple] = []
        stubs_for_subgroups = 0
        stubs_for_boundary = 0
        for qcode in all_qcodes:
            obs_id = obs_by_q[qcode]
            # 1. Sub-group rows A-H — always 8 per prompt
            for letter in ("A", "B", "C", "D", "E", "F", "G", "H"):
                sg_id = SG_LETTER_TO_ID[letter]
                a = authored.get((qcode, letter))
                if a:
                    text = a["text"]
                    status = a["status"]
                    src = a["source_file"]
                else:
                    text = "[Sub-group not separately addressed in source — see cluster-level finding for this prompt]"
                    status = "finding"
                    src = None
                    stubs_for_subgroups += 1
                insert_rows.append((
                    obs_id, CLUSTER_CODE, sg_id, status, text,
                    src, CATALOGUE_VERSION,
                    notes_template.format(src=src or "(stub)"),
                    0, ts, ts,
                ))
            # 2. BOUNDARY — always 1 per prompt
            a = authored.get((qcode, "BOUNDARY"))
            if a:
                text = a["text"]
                status = a["status"]
                src = a["source_file"]
            else:
                text = "[BOUNDARY — structural characterisation note only; full catalogue pass not applicable per §11 BOUNDARY treatment rule]"
                status = "finding"
                src = None
                stubs_for_boundary += 1
            insert_rows.append((
                obs_id, CLUSTER_CODE, BOUNDARY_ID, status, text,
                src, CATALOGUE_VERSION,
                notes_template.format(src=src or "(stub)"),
                0, ts, ts,
            ))
            # 3. CLUSTER — only where authored
            a = authored.get((qcode, "CLUSTER"))
            if a:
                insert_rows.append((
                    obs_id, CLUSTER_CODE, None, a["status"], a["text"],
                    a["source_file"], CATALOGUE_VERSION,
                    notes_template.format(src=a["source_file"]),
                    0, ts, ts,
                ))
        print(f"  Sub-group rows: {189*8} (stubs: {stubs_for_subgroups}, "
              f"authored: {189*8 - stubs_for_subgroups})")
        print(f"  BOUNDARY rows:  {189} (stubs: {stubs_for_boundary}, "
              f"authored: {189 - stubs_for_boundary})")
        n_cluster_authored = sum(
            1 for k in authored if k[1] == "CLUSTER")
        print(f"  CLUSTER rows:   {n_cluster_authored} (authored only)")
        print(f"  Total rows:     {len(insert_rows)}")

        # Phase 3 — INSERT
        print()
        print("Phase 3 — INSERT cluster_finding rows")
        print("-" * 72)
        cur.executemany(
            "INSERT INTO cluster_finding "
            "  (obs_id, cluster_code, cluster_subgroup_id, finding_status, "
            "   finding_text, source_file, version, notes, delete_flagged, "
            "   created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            insert_rows,
        )
        counts["phase3_cluster_finding_inserts"] = len(insert_rows)
        print(f"  Inserted {len(insert_rows)} rows")

        # FK check
        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {len(fkv)}; sample: {fkv[:3]}")
        print("FK check: ok")

        # Phase 4 — Verification
        print()
        print("VERIFICATION")
        print("-" * 72)
        # status counts
        print("  cluster_finding by status (M15):")
        for r in conn.execute("""
            SELECT finding_status, COUNT(*) n FROM cluster_finding
             WHERE cluster_code = ? GROUP BY finding_status
        """, (CLUSTER_CODE,)):
            print(f"    {r['finding_status']:25s} {r['n']}")
        # by scope
        print("  by scope:")
        for r in conn.execute("""
            SELECT COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope, COUNT(*) n
              FROM cluster_finding cf
              LEFT JOIN cluster_subgroup cs ON cs.id = cf.cluster_subgroup_id
             WHERE cf.cluster_code = ? GROUP BY scope ORDER BY scope
        """, (CLUSTER_CODE,)):
            print(f"    {r['scope']:15s} {r['n']}")
        # gap rows summary
        n_gaps = conn.execute("""
            SELECT COUNT(*) FROM cluster_finding
             WHERE cluster_code = ? AND finding_status = 'gap'
        """, (CLUSTER_CODE,)).fetchone()[0]
        print(f"  gap rows: {n_gaps}")
        # sb_findings unchanged
        sb_post = conn.execute("""
            SELECT COUNT(*) FROM wa_session_b_findings sbf
              JOIN mti_terms mt ON mt.id = sbf.term_id
             WHERE mt.cluster_code = 'M15'
        """).fetchone()[0]
        print(f"  wa_session_b_findings (M15 terms): pre={sb_baseline} post={sb_post}")
        # FLAG-006 check
        f006 = list(conn.execute("""
            SELECT vc.verse_record_id, vcg.group_code
              FROM verse_context vc
              JOIN verse_context_group vcg ON vcg.id = vc.group_id
             WHERE vc.verse_record_id IN ({})
               AND COALESCE(vc.delete_flagged,0) = 0
               AND vc.mti_term_id IN (SELECT id FROM mti_terms
                                       WHERE strongs_number='H2803G')
        """.format(",".join("?" * len(FLAG006_VR_IDS))), FLAG006_VR_IDS))
        print(f"  FLAG-M15-006 verses now in VCG:")
        for r in f006:
            print(f"    [{r['verse_record_id']}] → {r['group_code']}")

        if args.dry_run:
            conn.execute("ROLLBACK")
            print()
            print("DRY-RUN: rolled back.")
        else:
            conn.execute("COMMIT")
            print()
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {e}")
        raise

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:40s} {v}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
