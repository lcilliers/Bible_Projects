"""Apply Phase 11 — load M01 Phase 9 consolidated findings into cluster_finding.

Directive: wa-cluster-M01-dir-006-findings-record-v1-20260516
Governing: wa-sessionb-cluster-instruction-v2_2-20260516 §14

Inputs (4 parts):
  Sessions/Session_Clusters/M01/WA-M01-consolidated-findings-v1-20260516-part1.md
  ...-part2-T2.md  ...-part3-T3-T4.md  ...-part4-T5-T7.md

Operations (single transaction):
  Op A — INSERT cluster_finding rows (one per prompt × resolved-scope cell)
  Op B — Fold inherited RESOLVED-BY-CATALOGUE findings into named cluster_finding rows
  Op C — UPDATE wa_session_b_findings.resolution_note to record fold targets

Scope-marker resolution per v2_2 §14.4:
  [A] / [A,B,C]                 → row(s) per letter, vcg_scope=NULL
  [CLUSTER]                     → 1 row, sg=NULL, vcg_scope=NULL
  [BOUNDARY — H1234 translit]   → 1 row, sg=BOUNDARY.id, vcg_scope='term:H1234'
  [BOUNDARY]                    → 1 row, sg=BOUNDARY.id, vcg_scope=NULL
  [E-VCG-02]                    → 1 row, sg=E.id, vcg_scope='M01-E-VCG-02'
  [E-VCG-02/03/04/05]           → 1 row, sg=E.id, vcg_scope='M01-E-VCG-02;...VCG-05' (semicolon list)
  [A/Love], [A/Wisdom]          → merged into the prompt's CLUSTER row body (§14.4.1)

Outcome → finding_status:
  E (sub-group)  → 'finding'
  E (CLUSTER)    → 'cluster_synthesis'
  S              → 'silent'
  G              → 'gap'
  (no code)      → treated as E
"""
from __future__ import annotations
import argparse, json, re, shutil, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
M01 = REPO / "Sessions" / "Session_Clusters" / "M01"
DIRECTIVE = "DIR-20260516-006"
CLUSTER = "M01"
VERSION = "v1-20260516"

PARTS = [
    ("part1", M01 / "WA-M01-consolidated-findings-v1-20260516-part1.md"),
    ("part2", M01 / "WA-M01-consolidated-findings-v1-20260516-part2-T2.md"),
    ("part3", M01 / "WA-M01-consolidated-findings-v1-20260516-part3-T3-T4.md"),
    ("part4", M01 / "WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md"),
]

PROMPT_HEADER_RE = re.compile(r"^### (T\d+\.\d+\.\d+)[ —].*$", re.MULTILINE)
SCOPE_LINE_RE = re.compile(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$", re.MULTILINE)
SEPARATOR_RE = re.compile(r"^---\s*$", re.MULTILINE)
OUTCOME_RE = re.compile(r"^\s*([ESG])\s*[—-]\s+")


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%SZ')}] {msg}")


def backup_db() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    name = f"bible_research_backup_{ts}_{DIRECTIVE}.db"
    out = REPO / "backups" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(DB, out)
    return out


def fetch_obs_map(conn) -> dict[str, int]:
    rows = conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue WHERE tier IS NOT NULL AND deleted=0"
    ).fetchall()
    return {r["question_code"]: r["obs_id"] for r in rows}


def fetch_subgroup_map(conn) -> dict[str, int]:
    rows = conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchall()
    out: dict[str, int] = {}
    for r in rows:
        code = r["subgroup_code"]  # e.g. 'M01-A' or 'M01-BOUNDARY'
        # Map letter (A-G) and BOUNDARY
        if code.endswith("-BOUNDARY"):
            out["BOUNDARY"] = r["id"]
        else:
            letter = code.split("-")[-1]  # 'A' from 'M01-A'
            out[letter] = r["id"]
    return out


def parse_scope_marker(raw: str) -> list[dict]:
    """Parse a `[...]` body into a list of resolved scope rows.

    Returns list of dicts with keys: subgroup_letter (str|None for CLUSTER),
    vcg_scope (str|None), cross_cluster_axis (str|None — triggers merge-into-CLUSTER),
    boundary_term (str|None).
    """
    s = raw.strip()
    # Strip "— Label" suffix if present
    s_main = re.split(r"\s+[—-]\s+", s, maxsplit=1)[0]

    # BOUNDARY with optional term descriptor
    if s_main.startswith("BOUNDARY"):
        # Could be plain BOUNDARY, or "BOUNDARY - H1234 translit" (em-dash form)
        m = re.match(r"BOUNDARY\s*[—-]\s*(H\d+\w*)\s+(.+)$", s.strip())
        if m:
            return [{"subgroup_letter": "BOUNDARY", "vcg_scope": f"term:{m.group(1)}",
                     "cross_cluster_axis": None, "boundary_term": m.group(2).strip()}]
        return [{"subgroup_letter": "BOUNDARY", "vcg_scope": None,
                 "cross_cluster_axis": None, "boundary_term": None}]

    # CLUSTER (with optional descriptor)
    if s_main.startswith("CLUSTER"):
        return [{"subgroup_letter": None, "vcg_scope": None,
                 "cross_cluster_axis": None, "boundary_term": None}]

    # Comma-split into elements
    elements = [e.strip() for e in s_main.split(",")]
    out: list[dict] = []
    for e in elements:
        # Cross-cluster axis: [A/Wisdom] or [A/Love]
        m = re.fullmatch(r"([A-G])/(\w+)", e)
        if m:
            out.append({"subgroup_letter": None, "vcg_scope": None,
                        "cross_cluster_axis": m.group(2), "boundary_term": None})
            continue
        # VCG-specific: [E-VCG-02] or [E-VCG-02/03/04/05]
        m = re.fullmatch(r"([A-G])-VCG-(\d+(?:/\d+)*)", e)
        if m:
            letter = m.group(1)
            nums = m.group(2).split("/")
            vcg_codes = [f"M01-{letter}-VCG-{n.zfill(2)}" for n in nums]
            out.append({"subgroup_letter": letter,
                        "vcg_scope": ";".join(vcg_codes),
                        "cross_cluster_axis": None, "boundary_term": None})
            continue
        # Plain single letter
        if re.fullmatch(r"[A-G]", e):
            out.append({"subgroup_letter": e, "vcg_scope": None,
                        "cross_cluster_axis": None, "boundary_term": None})
            continue
        # Unrecognised — log and skip (or could raise)
        log(f"  WARN: unrecognised scope element {e!r} in marker {raw!r}")
    return out


def parse_part(path: Path, label: str) -> list[dict]:
    """Return list of {prompt_code, scope_raw, scope_resolved, outcome, body_text, source_label}."""
    text = path.read_text(encoding="utf-8")
    out: list[dict] = []
    # Locate prompts
    prompt_matches = list(PROMPT_HEADER_RE.finditer(text))
    for i, m in enumerate(prompt_matches):
        prompt_code = m.group(1)
        start = m.end()
        end = prompt_matches[i+1].start() if i+1 < len(prompt_matches) else len(text)
        body = text[start:end]
        # Find end-of-prompt separator
        sep_m = SEPARATOR_RE.search(body)
        prompt_body = body[:sep_m.start()] if sep_m else body
        # Find scope marker blocks
        scope_matches = list(SCOPE_LINE_RE.finditer(prompt_body))
        for j, sm in enumerate(scope_matches):
            scope_raw = sm.group(1).strip()
            head_body = sm.group(2).strip()
            block_start = sm.end()
            block_end = scope_matches[j+1].start() if j+1 < len(scope_matches) else len(prompt_body)
            block_text = (head_body + "\n" + prompt_body[block_start:block_end]).strip()
            # Outcome code
            m_out = OUTCOME_RE.match(head_body)
            outcome = m_out.group(1) if m_out else "E"
            # Strip leading "E — " from body for clean storage
            body_text = block_text
            if m_out:
                body_text = OUTCOME_RE.sub("", head_body, count=1).strip()
                rest = prompt_body[block_start:block_end].strip()
                if rest:
                    body_text = body_text + "\n\n" + rest
            scope_resolved = parse_scope_marker(scope_raw)
            out.append({
                "prompt_code": prompt_code,
                "scope_raw": scope_raw,
                "scope_resolved": scope_resolved,
                "outcome": outcome,
                "body_text": body_text.strip(),
                "source_label": label,
            })
    return out


def build_rows(parsed_blocks: list[dict], obs_map: dict[str, int], sg_map: dict[str, int],
               source_files: dict[str, str]) -> tuple[list[dict], dict]:
    """Group parsed blocks into cluster_finding rows.

    Returns (rows_to_insert, stats) where rows_to_insert is the list of row-dicts.
    Cross-cluster-axis blocks (e.g. [A/Wisdom]) merge into the prompt's CLUSTER row body.
    """
    # First pass: collect all blocks per (prompt_code, scope_key)
    # scope_key = (sg_letter, vcg_scope) — distinguishes rows
    # Cross-cluster axis blocks are gathered separately for CLUSTER merge.
    grouped: dict[tuple, dict] = {}
    cross_axis_merges: dict[str, list[dict]] = defaultdict(list)  # prompt_code -> [axis_block...]
    unmapped_prompts: set[str] = set()

    for b in parsed_blocks:
        if b["prompt_code"] not in obs_map:
            unmapped_prompts.add(b["prompt_code"])
            continue
        for scope in b["scope_resolved"]:
            # Cross-cluster axis: merge into CLUSTER
            if scope["cross_cluster_axis"]:
                cross_axis_merges[b["prompt_code"]].append({
                    "axis": scope["cross_cluster_axis"],
                    "outcome": b["outcome"],
                    "body_text": b["body_text"],
                    "source_label": b["source_label"],
                })
                continue
            sg_letter = scope["subgroup_letter"]  # None for CLUSTER
            sg_id = sg_map[sg_letter] if sg_letter else None
            vcg_scope = scope["vcg_scope"]
            key = (b["prompt_code"], sg_id, vcg_scope)
            if key in grouped:
                # Merge bodies — gap > silent > finding precedence
                existing = grouped[key]
                # Combine bodies with separator
                existing["body_parts"].append((b["outcome"], b["body_text"], b["source_label"]))
            else:
                grouped[key] = {
                    "prompt_code": b["prompt_code"],
                    "obs_id": obs_map[b["prompt_code"]],
                    "subgroup_id": sg_id,
                    "vcg_scope": vcg_scope,
                    "body_parts": [(b["outcome"], b["body_text"], b["source_label"])],
                }

    # Apply cross-cluster-axis merges into the CLUSTER row
    for prompt_code, axis_blocks in cross_axis_merges.items():
        if prompt_code not in obs_map:
            continue
        cluster_key = (prompt_code, None, None)
        if cluster_key not in grouped:
            # Create a CLUSTER row
            grouped[cluster_key] = {
                "prompt_code": prompt_code,
                "obs_id": obs_map[prompt_code],
                "subgroup_id": None,
                "vcg_scope": None,
                "body_parts": [],
            }
        for ax in axis_blocks:
            prefix = f"**M01 ↔ {ax['axis']} pair:** "
            grouped[cluster_key]["body_parts"].append(
                (ax["outcome"], prefix + ax["body_text"], ax["source_label"])
            )

    # Now resolve final status + body for each group
    rows: list[dict] = []
    for key, g in grouped.items():
        outcomes = [bp[0] for bp in g["body_parts"]]
        # Precedence: gap > silent > finding/cluster_synthesis
        if "G" in outcomes:
            status = "gap"
        elif all(o == "S" for o in outcomes):
            status = "silent"
        else:
            # Any E present
            if g["subgroup_id"] is None and g["vcg_scope"] is None:
                # CLUSTER scope with E → cluster_synthesis
                status = "cluster_synthesis"
            else:
                status = "finding"
        # Body assembly
        if len(g["body_parts"]) == 1:
            body_text = g["body_parts"][0][1]
        else:
            # Multi-block merge — separator between bodies
            parts = []
            for o, txt, lbl in g["body_parts"]:
                parts.append(f"[{o}] {txt}")
            body_text = "\n\n---\n\n".join(parts)
        source_file = source_files.get(g["body_parts"][0][2], "unknown")
        rows.append({
            "prompt_code": g["prompt_code"],
            "obs_id": g["obs_id"],
            "subgroup_id": g["subgroup_id"],
            "vcg_scope": g["vcg_scope"],
            "finding_status": status,
            "finding_text": body_text,
            "source_file": source_file,
        })

    stats = {
        "total_rows": len(rows),
        "unmapped_prompts": sorted(unmapped_prompts),
        "cross_axis_merges": sum(len(v) for v in cross_axis_merges.values()),
    }
    return rows, stats


def precheck(conn) -> None:
    log("Running pre-conditions...")
    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(f"cluster.status expected 'Analysis - In Progress', got {cluster and cluster['status']!r}")
    log(f"  cluster.status = {cluster['status']} ✓")
    # Check existing cluster_finding rows for M01
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=?",
        (CLUSTER, VERSION)
    ).fetchone()
    if r["n"] > 0:
        raise RuntimeError(f"cluster_finding already has {r['n']} rows for M01 version={VERSION}. Aborting.")
    log(f"  no pre-existing cluster_finding rows for M01 version={VERSION} ✓")


def fetch_fold_candidates(conn) -> list[dict]:
    """Find wa_session_b_findings rows with status='resolved_qa' where resolution_note
    names Phase 9 Tier targets."""
    rows = conn.execute("""
        SELECT sbf.id, sbf.finding_id, sbf.registry_id, sbf.finding, sbf.resolution_note,
               wr.no AS registry_no, wr.word AS registry_word
        FROM wa_session_b_findings sbf
        LEFT JOIN word_registry wr ON wr.id = sbf.registry_id
        WHERE sbf.status='resolved_qa'
          AND sbf.resolution_note LIKE '%DIR-20260516-005%'
          AND sbf.resolution_note LIKE '%RESOLVED-BY-CATALOGUE%'
    """).fetchall()
    return [dict(r) for r in rows]


def parse_fold_targets(resolution_note: str) -> list[tuple[str, str | None]]:
    """Parse 'T3.8.1 [A], T1.8.3 [A], T3.4.1 [A]' → [('T3.8.1','A'), ('T1.8.3','A'), ('T3.4.1','A')].

    Dedupes — the resolution_note may mention the same T-code in both the target list and
    the rationale text.
    """
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, str | None]] = []
    pat = re.compile(r"(T\d+\.\d+\.\d+)\s*\[([^\]]+)\]")
    for m in pat.finditer(resolution_note):
        tcode = m.group(1)
        scope_raw = m.group(2).strip()
        for elem in [e.strip() for e in scope_raw.split(",")]:
            elem_main = re.split(r"\s+[—-]\s+", elem, maxsplit=1)[0]
            key = (tcode, elem_main)
            if key in seen:
                continue
            seen.add(key)
            out.append(key)
    return out


def apply(conn, dry_run: bool) -> dict:
    obs_map = fetch_obs_map(conn)
    sg_map = fetch_subgroup_map(conn)
    log(f"  obs_map: {len(obs_map)} prompts; sg_map: {sorted(sg_map.keys())}")

    # Parse all 4 parts
    all_blocks: list[dict] = []
    source_files = {}
    for label, path in PARTS:
        blocks = parse_part(path, label)
        all_blocks.extend(blocks)
        source_files[label] = path.name
        log(f"  Parsed {label}: {len(blocks)} blocks")
    log(f"  Total parsed blocks: {len(all_blocks)}")

    # Build rows
    rows, stats = build_rows(all_blocks, obs_map, sg_map, source_files)
    log(f"\n{'='*60}")
    log(f"Op A — INSERT cluster_finding rows")
    log(f"{'='*60}")
    log(f"  Rows to insert: {stats['total_rows']}")
    if stats["unmapped_prompts"]:
        log(f"  WARN: unmapped prompts: {stats['unmapped_prompts']}")
    log(f"  Cross-axis merges absorbed into CLUSTER rows: {stats['cross_axis_merges']}")

    # Row distribution stats
    by_status: dict[str, int] = defaultdict(int)
    by_scope: dict[str, int] = defaultdict(int)
    by_vcg_scope_used: int = 0
    for r in rows:
        by_status[r["finding_status"]] += 1
        if r["subgroup_id"] is None:
            by_scope["CLUSTER"] += 1
        else:
            by_scope[f"sg={r['subgroup_id']}"] += 1
        if r["vcg_scope"]:
            by_vcg_scope_used += 1
    log(f"  By status: {dict(by_status)}")
    log(f"  Rows with vcg_scope: {by_vcg_scope_used}")

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not dry_run:
        for r in rows:
            conn.execute("""
                INSERT INTO cluster_finding
                    (obs_id, cluster_code, cluster_subgroup_id, vcg_scope, finding_status,
                     finding_text, source_file, version, notes, created_at, last_updated_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (r["obs_id"], CLUSTER, r["subgroup_id"], r["vcg_scope"], r["finding_status"],
                  r["finding_text"], r["source_file"], VERSION, DIRECTIVE, now_iso, now_iso))

    # Op B — Fold inherited RESOLVED-BY-CATALOGUE
    log(f"\n{'='*60}")
    log(f"Op B + C — Fold inherited findings into cluster_finding")
    log(f"{'='*60}")
    fold_candidates = fetch_fold_candidates(conn)
    log(f"  Fold candidates from wa_session_b_findings: {len(fold_candidates)}")
    fold_actions = []  # list of (sbf_id, target_obs_id, target_sg_id, cluster_finding_id)
    for fc in fold_candidates:
        targets = parse_fold_targets(fc["resolution_note"] or "")
        log(f"    sbf.id={fc['id']} reg={fc['registry_word']} → targets: {targets}")
        # For each (T-code, scope_letter) target, find the cluster_finding row
        cluster_finding_ids: list[int] = []
        for tcode, scope_elem in targets:
            obs_id = obs_map.get(tcode)
            if not obs_id:
                log(f"      WARN: T-code {tcode!r} not in obs_map; skipping")
                continue
            if scope_elem == "CLUSTER":
                sg_id = None
            elif scope_elem in sg_map:
                sg_id = sg_map[scope_elem]
            else:
                log(f"      WARN: scope {scope_elem!r} not in sg_map; skipping target {tcode} [{scope_elem}]")
                continue
            # Locate the row
            r = conn.execute("""
                SELECT id, finding_text FROM cluster_finding
                WHERE obs_id=? AND cluster_code=? AND cluster_subgroup_id IS ?
                  AND vcg_scope IS NULL AND version=?
            """, (obs_id, CLUSTER, sg_id, VERSION)).fetchone()
            if not r:
                log(f"      WARN: no cluster_finding row found for obs={tcode} sg={scope_elem}")
                continue
            cluster_finding_ids.append(r["id"])
            # Build fold text
            fold_prefix = (f"\n\n**[Folded from wa_session_b_findings.id={fc['id']}; "
                          f"finding_id={fc['finding_id']}; registry={fc['registry_word']}]**\n")
            fold_body = fc["finding"] or ""
            if not dry_run:
                conn.execute(
                    "UPDATE cluster_finding SET finding_text = COALESCE(finding_text,'') || ? WHERE id=?",
                    (fold_prefix + fold_body, r["id"])
                )
        if cluster_finding_ids:
            fold_actions.append((fc["id"], cluster_finding_ids))
            if not dry_run:
                # Op C — append to resolution_note
                note_append = f" | DIR-20260516-006: folded into cluster_finding.id IN ({','.join(str(i) for i in cluster_finding_ids)})"
                conn.execute(
                    "UPDATE wa_session_b_findings SET resolution_note = COALESCE(resolution_note,'') || ? WHERE id=?",
                    (note_append, fc["id"])
                )

    log(f"  Folded {len(fold_actions)} inherited findings into cluster_finding rows.")
    return {
        "inserted": stats["total_rows"],
        "folded": len(fold_actions),
        "fold_actions": fold_actions,
    }


def healthcheck(conn) -> None:
    log(f"\n{'='*60}")
    log(f"Health checks")
    log(f"{'='*60}")
    # P1 row count for M01 version
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=?",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P1 cluster_finding rows for M01 v={VERSION}: {r['n']}")
    # P2 distinct prompt count
    r = conn.execute(
        "SELECT COUNT(DISTINCT obs_id) AS n FROM cluster_finding WHERE cluster_code=? AND version=?",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P2 distinct prompts: {r['n']} (expected 189)")
    assert r["n"] == 189, f"P2 failed: expected 189 distinct prompts, got {r['n']}"
    # P3 status distribution
    log(f"  P3 status distribution:")
    for row in conn.execute(
        "SELECT finding_status, COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=? GROUP BY finding_status ORDER BY n DESC",
        (CLUSTER, VERSION)
    ):
        log(f"      {row['finding_status']}: {row['n']}")
    # P4 vcg_scope usage
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=? AND vcg_scope IS NOT NULL",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P4 rows with vcg_scope set: {r['n']}")
    # P5 fold markers present
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=? AND finding_text LIKE '%[Folded from wa_session_b_findings.id=%'",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P5 rows carrying fold-in markers: {r['n']}")
    assert r["n"] > 0, "P5 failed: no fold markers found"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()
    dry_run = not args.live

    log(f"Phase 11 findings load — cluster={CLUSTER} directive={DIRECTIVE}")
    log(f"Mode: {'DRY-RUN' if dry_run else 'LIVE'}")

    if not dry_run:
        backup_path = backup_db()
        log(f"Backup: {backup_path.relative_to(REPO)}")

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("BEGIN")
        precheck(conn)
        result = apply(conn, dry_run=dry_run)
        if dry_run:
            log("\nDRY-RUN — rolling back")
            conn.execute("ROLLBACK")
        else:
            log("\nCommitting...")
            conn.execute("COMMIT")
            healthcheck(conn)
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: inserted={result['inserted']} folded={result['folded']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
