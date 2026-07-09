"""Apply DIR-20260513-009 — M20 Phase 9 findings record.

Parses 4 consolidated findings parts and INSERTs into cluster_finding.
M20 format uses inline scope markers (multiple **[X]** markers within one
paragraph), unlike M15 which used line-anchored markers. Custom parser
handles inline scopes.

Per directive item 8/9: do NOT auto-stub unaddressed sub-groups.
Only insert rows the source authored.
"""
from __future__ import annotations
import argparse, os, re, shutil, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DIRECTIVE_ID = "DIR-20260513-009"
CLUSTER_CODE = "M20"
CATALOGUE_VERSION = "v2.1-2026-05-13"
OBSLOG_REF = "wa-obslog-M20-m20-doubt-v1-20260513.md"
PHASE8_DIR = os.path.join("Sessions", "Session_Clusters", "M20", "files phase 8")
PART_FILES = [
    "WA-M20-consolidated-findings-v1-20260513-part1.md",
    "WA-M20-consolidated-findings-v1-20260513-part2-T2.md",
    "WA-M20-consolidated-findings-v1-20260513-part3-T3-T4.md",
    "WA-M20-consolidated-findings-v1-20260513-part4-T5-T7.md",
]

SG_LETTER_TO_ID: dict[str, int | None] = {"A": None, "B": None, "C": None, "D": None}

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
    """Return list of scope keys. Letters A/B/C/D or 'CLUSTER'.
    Multi-scope [A, B, C] returns multiple. [A — Label] returns ['A']."""
    s = raw.strip()
    # CLUSTER variants
    if s.upper() == "CLUSTER" or s.upper().startswith("CLUSTER —") or s.upper().startswith("CLUSTER -"):
        return ["CLUSTER"]
    # Multi-scope (before any " — Label")
    head = s.split(" — ")[0].split(" - ")[0]
    if "," in head:
        letters = [p.strip().upper() for p in head.split(",")]
        out = []
        for L in letters:
            if L in ("A", "B", "C", "D"):
                out.append(L)
            elif L == "CLUSTER":
                out.append("CLUSTER")
        if out:
            return out
    # Single letter or [letter — label]
    m = re.match(r"^([A-D])\b", s)
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
    """Parse a consolidated-findings part file.

    M20 format: prompt headers are `**T#.#.#** — text`. Scope markers
    `**[X]**` appear inline within the text — may be multiple per
    paragraph. We split each prompt block by inline scope markers.
    """
    src = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    rows: list[dict] = []
    lines = text.splitlines()

    # First pass: identify line positions of prompt headers
    prompt_positions: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = PROMPT_HEADER_RE.match(line.strip())
        if m:
            prompt_positions.append((i, m.group(1)))

    # For each prompt, collect block text until the next prompt or EOF
    for idx, (start_line, qcode) in enumerate(prompt_positions):
        end_line = prompt_positions[idx + 1][0] if idx + 1 < len(prompt_positions) else len(lines)
        # Skip the header line itself; collect content until next prompt
        block_lines = lines[start_line + 1:end_line]
        # Strip trailing horizontal rules / blank lines
        while block_lines and (block_lines[-1].strip() in ("---", "")):
            block_lines.pop()
        block = "\n".join(block_lines).strip()
        if not block:
            continue

        # Find all inline scope markers
        scope_matches = list(SCOPE_INLINE_RE.finditer(block))
        if not scope_matches:
            # Shorthand pattern: prompt has no explicit scope marker.
            # Author intent: a cluster-wide finding covering all sub-groups.
            # Detect S/G prefix; default to cluster_synthesis.
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

        # For each scope marker, capture text from end of marker to start of
        # next marker (or end of block)
        for sm_idx, m in enumerate(scope_matches):
            scope_raw = m.group(1)
            text_start = m.end()
            text_end = scope_matches[sm_idx + 1].start() if sm_idx + 1 < len(scope_matches) else len(block)
            seg = block[text_start:text_end].strip()
            scope_keys = normalize_scope(scope_raw)
            if not scope_keys:
                continue
            status, cleaned = parse_outcome(seg)
            # For CLUSTER markers, force cluster_synthesis status unless the
            # marker explicitly carries an S/G outcome (rare but possible).
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
    print(f"{DIRECTIVE_ID} apply — M20 Phase 9 findings record")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'LIVE'}")
    print("=" * 72)
    print()

    # Parse all four parts
    print("PARSE")
    print("-" * 72)
    all_rows: list[dict] = []
    for fn in PART_FILES:
        p = os.path.join(PHASE8_DIR, fn)
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

    # Pre-flight
    print()
    print("PRE-FLIGHT")
    print("-" * 72)
    ok = True

    for r in conn.execute("SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code='M20' AND COALESCE(delete_flagged,0)=0"):
        letter = r["subgroup_code"].split("-")[-1]
        if letter in SG_LETTER_TO_ID:
            SG_LETTER_TO_ID[letter] = r["id"]
    print(f"  sub-group letter map: {SG_LETTER_TO_ID}")
    for L in ("A", "B", "C", "D"):
        if SG_LETTER_TO_ID[L] is None:
            print(f"  [ERR] M20-{L} not found"); ok = False

    n_existing = conn.execute("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M20'").fetchone()[0]
    print(f"  existing M20 cluster_finding rows: {n_existing}")
    if n_existing > 0:
        print(f"  [ERR] M20 cluster_finding already has rows — refusing to load")
        ok = False

    obs_by_q = {r["question_code"]: r["obs_id"] for r in conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
        "WHERE question_code GLOB 'T[0-9]*' AND COALESCE(deleted,0)=0"
    )}
    print(f"  catalogue T-prompts: {len(obs_by_q)} (expected 189)")
    parsed_qcodes = set(r["qcode"] for r in all_rows)
    missing_q = parsed_qcodes - set(obs_by_q.keys())
    if missing_q:
        print(f"  [ERR] parsed qcodes not in catalogue: {sorted(missing_q)[:10]}")
        ok = False
    unaddressed_q = sorted(set(obs_by_q.keys()) - parsed_qcodes)
    if unaddressed_q:
        print(f"  [info] {len(unaddressed_q)} catalogue prompts not addressed in source")
        print(f"         (no rows will be inserted for these — per directive item 8)")
        if len(unaddressed_q) <= 10:
            print(f"         {unaddressed_q}")

    # sb baseline
    sb_baseline = conn.execute("""
        SELECT COUNT(*) FROM wa_session_b_findings sbf
          JOIN mti_terms mt ON mt.id=sbf.term_id
         WHERE mt.cluster_code='M20'
    """).fetchone()[0]
    print(f"  wa_session_b_findings baseline (M20 terms): {sb_baseline}")

    if not ok:
        print("\nPre-flight FAILED.")
        return 1

    if args.dry_run:
        # Show what would happen
        print()
        print("DRY-RUN — would insert:")
        # Tally per scope
        by_scope = Counter()
        for r in all_rows:
            by_scope[(r["scope"], r["status"])] += 1
        for (scope, status), n in sorted(by_scope.items()):
            print(f"  scope={scope:8s} status={status:20s} count={n}")
        print(f"  TOTAL rows: {len(all_rows)}")
        return 0

    # LIVE
    backup = take_backup("m20_dir009_phase9")
    print(f"\nBackup: {backup}\n")

    try:
        conn.execute("BEGIN")
        ts = now_iso()
        cur = conn.cursor()
        notes_template = (
            f"{DIRECTIVE_ID} (Phase 9 findings load 2026-05-13); "
            f"source: {{src}}; catalogue: {CATALOGUE_VERSION}; "
            f"obslog: {OBSLOG_REF}"
        )

        # Collapse same-(qcode, scope) entries — append text segments.
        # Unique constraint is (obs_id, cluster_code, cluster_subgroup_id,
        # version) so at most one row per (qcode × scope × catalogue version).
        collapsed: dict[tuple[str, str], dict] = {}
        for r in all_rows:
            key = (r["qcode"], r["scope"])
            if key in collapsed:
                collapsed[key]["text"] = (
                    collapsed[key]["text"].rstrip() + "\n\n---\n\n" + r["text"]
                )
                # Status precedence: finding > cluster_synthesis > silent > gap
                # (if any segment is substantive, the row is substantive)
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
            sg_id = None if r["scope"] == "CLUSTER" else SG_LETTER_TO_ID[r["scope"]]
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

        # Verification
        print("VERIFICATION")
        print("-" * 72)
        print("  by status:")
        for r in conn.execute("SELECT finding_status, COUNT(*) AS n FROM cluster_finding WHERE cluster_code='M20' GROUP BY finding_status ORDER BY finding_status"):
            print(f"    {r['finding_status']:25s} {r['n']}")
        print("  by scope:")
        for r in conn.execute("""
            SELECT COALESCE(cs.subgroup_code,'(CLUSTER)') AS scope, COUNT(*) AS n
              FROM cluster_finding cf
              LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id
             WHERE cf.cluster_code='M20'
             GROUP BY scope ORDER BY scope
        """):
            print(f"    {r['scope']:18s} {r['n']}")

        # Prompt coverage
        uncovered = list(conn.execute("""
            SELECT q.question_code FROM wa_obs_question_catalogue q
             WHERE COALESCE(q.deleted,0)=0 AND q.question_code GLOB 'T[0-9]*'
               AND NOT EXISTS (
                 SELECT 1 FROM cluster_finding cf
                  WHERE cf.cluster_code='M20' AND cf.obs_id=q.obs_id
               )
             ORDER BY q.question_code
        """))
        print(f"  prompts with no M20 row: {len(uncovered)}")
        if uncovered and len(uncovered) <= 30:
            for r in uncovered:
                print(f"    {r['question_code']}")

        # Gap list
        n_gaps = conn.execute("SELECT COUNT(*) FROM cluster_finding WHERE cluster_code='M20' AND finding_status='gap'").fetchone()[0]
        print(f"  gap rows: {n_gaps}")

        # sb unchanged
        sb_now = conn.execute("""
            SELECT COUNT(*) FROM wa_session_b_findings sbf
              JOIN mti_terms mt ON mt.id=sbf.term_id
             WHERE mt.cluster_code='M20'
        """).fetchone()[0]
        mark = "✓" if sb_now == sb_baseline else "✗"
        print(f"  wa_session_b_findings (M20 terms): {sb_now}  (baseline {sb_baseline})  {mark}")

    except Exception as e:
        conn.rollback()
        print(f"\nROLLED BACK: {e}")
        return 1

    conn.close()
    print(f"\n[LIVE] {DIRECTIVE_ID} applied successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
