"""Apply DIR-20260514-004 — M39 Phase 9 findings record.

Parses 4 consolidated findings parts and INSERTs into cluster_finding.
Per v1_11 §11.8 canonical syntax: line-anchored scope markers (`**[X]**`
each on its own line). Adapted from M20's apply script.

Sub-groups: A, B, BOUNDARY (M39 differs from M20's A/B/C/D).

Does NOT change cluster.status — Phase 10 closure is a separate directive.
"""
from __future__ import annotations
import argparse, os, re, shutil, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIRECTIVE_ID = "DIR-20260514-004"
CLUSTER_CODE = "M39"
CATALOGUE_VERSION = "v2.1-2026-05-13"
OBSLOG_REF = "wa-obslog-M39-sessionb-v1-20260514.md"
PHASE9_DIR = os.path.join("Sessions", "Session_Clusters", "M39", "files phase 9")
PART_FILES = [
    "WA-M39-consolidated-findings-v1-20260514-part1.md",
    "WA-M39-consolidated-findings-v1-20260514-part2-T2.md",
    "WA-M39-consolidated-findings-v1-20260514-part3-T3-T4.md",
    "WA-M39-consolidated-findings-v1-20260514-part4-T5-T7.md",
]

SG_LETTER_TO_ID: dict[str, int | None] = {"A": None, "B": None, "BOUNDARY": None}

PROMPT_HEADER_RE = re.compile(r"^\*\*(T\d+\.\d+\.\d+)\*\*\s*(?:[—–-]\s*(.*))?$")
SCOPE_INLINE_RE  = re.compile(r"\*\*\[([^\]]+)\]\*\*")
OUTCOME_RE       = re.compile(r"^\s*([ESG])\s*[—–-]\s*(.*)$", re.DOTALL)


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def take_backup(label):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    p = os.path.join(BACKUP_DIR, f"bible_research_pre_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db")
    shutil.copy2(DB_PATH, p)
    return p


def normalize_scope(raw: str) -> list[str]:
    """Return list of scope keys. Letters A/B or 'BOUNDARY' or 'CLUSTER'.
    Multi-scope [A, B] returns multiple. [A — Label] returns ['A']."""
    s = raw.strip()
    up = s.upper()
    if up == "CLUSTER" or up.startswith("CLUSTER —") or up.startswith("CLUSTER -"):
        return ["CLUSTER"]
    if up == "BOUNDARY" or up.startswith("BOUNDARY —") or up.startswith("BOUNDARY -"):
        return ["BOUNDARY"]
    head = s.split(" — ")[0].split(" - ")[0]
    if "," in head:
        parts = [p.strip().upper() for p in head.split(",")]
        out = []
        for L in parts:
            if L in ("A", "B"):
                out.append(L)
            elif L == "BOUNDARY":
                out.append("BOUNDARY")
            elif L == "CLUSTER":
                out.append("CLUSTER")
        if out:
            return out
    m = re.match(r"^([AB])\b", s)
    if m:
        return [m.group(1)]
    return []


def parse_outcome(text: str) -> tuple[str, str]:
    """Detect leading E/S/G outcome marker. Returns (status, cleaned_text)."""
    m = OUTCOME_RE.match(text.lstrip())
    if m:
        letter = m.group(1)
        status = {"E": "finding", "S": "silent", "G": "gap"}[letter]
        return status, m.group(2).strip()
    return "finding", text.strip()


def parse_part_file(path: str) -> list[dict]:
    """Parse a consolidated-findings part file."""
    src = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    rows: list[dict] = []
    lines = text.splitlines()

    prompt_positions: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = PROMPT_HEADER_RE.match(line.strip())
        if m:
            prompt_positions.append((i, m.group(1)))

    for idx, (start_line, qcode) in enumerate(prompt_positions):
        end_line = prompt_positions[idx + 1][0] if idx + 1 < len(prompt_positions) else len(lines)
        block_lines = lines[start_line + 1:end_line]
        while block_lines and (block_lines[-1].strip() in ("---", "")):
            block_lines.pop()
        block = "\n".join(block_lines).strip()
        if not block:
            continue

        scope_matches = list(SCOPE_INLINE_RE.finditer(block))
        if not scope_matches:
            status, cleaned = parse_outcome(block)
            if status == "finding":
                status = "cluster_synthesis"
            rows.append({
                "qcode": qcode,
                "scope": "CLUSTER",
                "status": status,
                "text": cleaned,
                "source_file": src,
            })
            continue

        for sm_idx, m in enumerate(scope_matches):
            scope_raw = m.group(1)
            text_start = m.end()
            text_end = scope_matches[sm_idx + 1].start() if sm_idx + 1 < len(scope_matches) else len(block)
            seg = block[text_start:text_end].strip()
            scope_keys = normalize_scope(scope_raw)
            if not scope_keys:
                continue
            status, cleaned = parse_outcome(seg)
            for sk in scope_keys:
                final_status = status
                if sk == "CLUSTER" and status == "finding":
                    final_status = "cluster_synthesis"
                rows.append({
                    "qcode": qcode,
                    "scope": sk,
                    "status": final_status,
                    "text": cleaned,
                    "source_file": src,
                })
    return rows


def main() -> int:
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.live:
        print("ERROR: pass --dry-run or --live", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"{DIRECTIVE_ID} apply — M39 Phase 9 findings record")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    print("PARSE")
    print("-" * 72)
    all_rows: list[dict] = []
    for fn in PART_FILES:
        p = os.path.join(PHASE9_DIR, fn)
        rows = parse_part_file(p)
        print(f"  {fn:55s} parsed_rows={len(rows)}")
        all_rows.extend(rows)
    print(f"  TOTAL parsed cells: {len(all_rows)}")
    print(f"  by scope:  {dict(Counter(r['scope'] for r in all_rows))}")
    print(f"  by status: {dict(Counter(r['status'] for r in all_rows))}")
    distinct_q = set(r["qcode"] for r in all_rows)
    print(f"  distinct prompts addressed: {len(distinct_q)}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    print()
    print("PRE-FLIGHT")
    print("-" * 72)
    ok = True

    for r in conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        "WHERE cluster_code='M39' AND COALESCE(delete_flagged,0)=0"
    ):
        sg_code = r["subgroup_code"]
        if sg_code == "M39-BOUNDARY":
            SG_LETTER_TO_ID["BOUNDARY"] = r["id"]
        else:
            letter = sg_code.split("-")[-1]
            if letter in SG_LETTER_TO_ID:
                SG_LETTER_TO_ID[letter] = r["id"]
    print(f"  sub-group map: {SG_LETTER_TO_ID}")
    for k, v in SG_LETTER_TO_ID.items():
        if v is None:
            print(f"  [ERR] M39 sub-group {k} not found"); ok = False

    n_existing = conn.execute("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M39'").fetchone()[0]
    print(f"  existing M39 cluster_finding rows: {n_existing}")
    if n_existing > 0:
        print(f"  [ERR] M39 cluster_finding already has rows — refusing to load")
        ok = False

    obs_by_q = {r["question_code"]: r["obs_id"] for r in conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
        "WHERE question_code GLOB 'T[0-9]*' AND COALESCE(deleted,0)=0"
    )}
    print(f"  catalogue T-prompts: {len(obs_by_q)}")
    parsed_qcodes = set(r["qcode"] for r in all_rows)
    missing_q = parsed_qcodes - set(obs_by_q.keys())
    if missing_q:
        print(f"  [ERR] parsed qcodes not in catalogue: {sorted(missing_q)[:10]}")
        ok = False
    unaddressed_q = sorted(set(obs_by_q.keys()) - parsed_qcodes)
    if unaddressed_q:
        print(f"  [info] {len(unaddressed_q)} catalogue prompts not addressed in source")
        if len(unaddressed_q) <= 20:
            print(f"         {unaddressed_q}")

    # wa_session_research_flags baseline (not modified by Phase 9)
    flag_baseline = conn.execute("""
        SELECT COUNT(*) FROM wa_session_research_flags wsrf
          JOIN mti_terms mt ON mt.owning_registry_fk = wsrf.registry_id
         WHERE mt.cluster_code='M39' AND COALESCE(mt.delete_flagged,0)=0
    """).fetchone()[0]
    print(f"  wa_session_research_flags baseline (M39-term registries): {flag_baseline}")

    if not ok:
        print("\nPre-flight FAILED.")
        return 1

    if args.dry_run:
        print()
        print("DRY-RUN — would insert (collapsed):")
        # Collapse same-(qcode, scope) entries for reporting
        collapsed_dry: dict[tuple[str, str], dict] = {}
        for r in all_rows:
            key = (r["qcode"], r["scope"])
            if key in collapsed_dry:
                continue
            collapsed_dry[key] = r
        by = Counter((r["scope"], r["status"]) for r in collapsed_dry.values())
        for (scope, status), n in sorted(by.items()):
            print(f"  scope={scope:10s} status={status:20s} count={n}")
        print(f"  TOTAL collapsed rows: {len(collapsed_dry)}")
        return 0

    # LIVE
    backup = take_backup("m39_dir004_phase9")
    print(f"\nBackup: {backup}\n")

    try:
        conn.execute("BEGIN")
        ts = now_iso()
        cur = conn.cursor()
        notes_template = (
            f"{DIRECTIVE_ID} (Phase 9 findings load 2026-05-14); "
            f"source: {{src}}; catalogue: {CATALOGUE_VERSION}; "
            f"obslog: {OBSLOG_REF}"
        )

        collapsed: dict[tuple[str, str], dict] = {}
        for r in all_rows:
            key = (r["qcode"], r["scope"])
            if key in collapsed:
                collapsed[key]["text"] = (
                    collapsed[key]["text"].rstrip() + "\n\n---\n\n" + r["text"]
                )
                prec = {"finding": 0, "cluster_synthesis": 1, "silent": 2, "gap": 3}
                if prec.get(r["status"], 4) < prec.get(collapsed[key]["status"], 4):
                    collapsed[key]["status"] = r["status"]
            else:
                collapsed[key] = dict(r)
        n_collapsed = len(all_rows) - len(collapsed)
        if n_collapsed:
            print(f"  Collapsed {n_collapsed} duplicate (qcode, scope) entries.")

        insert_rows = []
        for r in collapsed.values():
            obs_id = obs_by_q[r["qcode"]]
            if r["scope"] == "CLUSTER":
                sg_id = None
            else:
                sg_id = SG_LETTER_TO_ID[r["scope"]]
            insert_rows.append((
                obs_id, CLUSTER_CODE, sg_id, r["status"], r["text"],
                r["source_file"], CATALOGUE_VERSION,
                notes_template.format(src=r["source_file"]),
                0, ts, ts,
            ))
        cur.executemany(
            "INSERT INTO cluster_finding "
            " (obs_id, cluster_code, cluster_subgroup_id, finding_status, "
            "  finding_text, source_file, version, notes, delete_flagged, "
            "  created_at, last_updated_date) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            insert_rows,
        )
        print(f"Inserted {len(insert_rows)} cluster_finding rows.")

        fkv = list(conn.execute("PRAGMA foreign_key_check"))
        if fkv:
            raise RuntimeError(f"FK violations: {fkv[:3]}")
        conn.commit()
        print("Commit OK.\n")

        print("VERIFICATION")
        print("-" * 72)
        print("  by status:")
        for r in conn.execute(
            "SELECT finding_status, COUNT(*) AS n FROM cluster_finding "
            "WHERE cluster_code='M39' GROUP BY finding_status ORDER BY finding_status"
        ):
            print(f"    {r['finding_status']:25s} {r['n']}")
        print("  by scope:")
        for r in conn.execute("""
            SELECT COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope, COUNT(*) AS n
              FROM cluster_finding cf
              LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
             WHERE cf.cluster_code='M39'
             GROUP BY scope ORDER BY scope
        """):
            print(f"    {r['scope']:18s} {r['n']}")

        uncovered = list(conn.execute("""
            SELECT q.question_code FROM wa_obs_question_catalogue q
             WHERE COALESCE(q.deleted,0)=0 AND q.question_code GLOB 'T[0-9]*'
               AND NOT EXISTS (
                 SELECT 1 FROM cluster_finding cf
                  WHERE cf.cluster_code='M39' AND cf.obs_id=q.obs_id
               )
             ORDER BY q.question_code
        """))
        print(f"  prompts with no M39 row: {len(uncovered)}")
        if uncovered and len(uncovered) <= 20:
            print(f"    {[r['question_code'] for r in uncovered]}")

        n_gaps = conn.execute(
            "SELECT COUNT(*) FROM cluster_finding "
            "WHERE cluster_code='M39' AND finding_status='gap'"
        ).fetchone()[0]
        print(f"  gap rows: {n_gaps}")

        n_synth = conn.execute(
            "SELECT COUNT(*) FROM cluster_finding "
            "WHERE cluster_code='M39' AND finding_status='cluster_synthesis'"
        ).fetchone()[0]
        print(f"  cluster_synthesis rows: {n_synth}")

        flag_now = conn.execute("""
            SELECT COUNT(*) FROM wa_session_research_flags wsrf
              JOIN mti_terms mt ON mt.owning_registry_fk = wsrf.registry_id
             WHERE mt.cluster_code='M39' AND COALESCE(mt.delete_flagged,0)=0
        """).fetchone()[0]
        mark = "✓" if flag_now == flag_baseline else "✗"
        print(f"  wa_session_research_flags (M39-term registries): {flag_now}  (baseline {flag_baseline})  {mark}")

        cluster_status = conn.execute(
            "SELECT status FROM cluster WHERE cluster_code='M39'"
        ).fetchone()["status"]
        print(f"  cluster.status: {cluster_status!r} (unchanged — Phase 10 closure separate)")

    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    conn.close()
    print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
    print(f"\nNOTE: Phase 10 (verification + BOUNDARY exit + Analysis Completed status flip)")
    print(f"      is a separate directive per v1_11 §13.7/§13.9 — not authored yet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
