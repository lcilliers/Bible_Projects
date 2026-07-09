"""Apply Phase 11 — load M03 Phase 9 consolidated findings into cluster_finding.

Directive: wa-cluster-M03-dir-006-findings-record-v1-20260517 (DIR-20260517-002)
Governing: wa-sessionb-cluster-instruction-v2_2-20260516 §14

Inputs (4 parts in files phase 9/):
  WA-M03-consolidated-findings-v1-20260517-part1.md           (T0-T1, 36 prompts)
  WA-M03-consolidated-findings-v1-20260517-part2-T2.md        (T2, 31 prompts)
  WA-M03-consolidated-findings-v1-20260517-part3-T3-T4.md     (T3+T4, 57 prompts)
  WA-M03-consolidated-findings-v1-20260517-part4-T5-T7.md     (T5-T7, 65 prompts)

Operations (single transaction):
  Op A — INSERT cluster_finding rows (one per prompt × resolved-scope cell)
  Op B + C — Fold inherited FOLD-INTO-PROMPT findings (M03: 1 row — sbf.73 DIM-13-001)
             into named cluster_finding rows + record fold target in resolution_note.

M03 differences from M02 template:
  - AI used `**T0.1.1**` inline bold prompt headers (not `### T0.1.1`). Regex adapted.
  - VCG codes use "M03-" prefix.
  - Phase 10 directive was DIR-20260517-001 (vs M02's DIR-20260516-012).
  - 1 fold target (sbf.73 → T1.2.1 [CLUSTER], T1.3.2 [CLUSTER]) — M02 had 2.

Scope-marker resolution per v2_2 §14.4 (canonical):
  [A] / [A,B,C]                 → row(s) per letter, vcg_scope=NULL
  [CLUSTER]                     → 1 row, sg=NULL, vcg_scope=NULL
  [BOUNDARY — H1234 translit]   → 1 row, sg=BOUNDARY.id, vcg_scope='term:H1234'
  [A-VCG-02]                    → 1 row, sg=A.id, vcg_scope='M03-A-VCG-02'
  [A-VCG-02/03/04/05]           → semicolon list

Outcome → finding_status:
  E (sub-group)  → 'finding'
  E (CLUSTER)    → 'cluster_synthesis'
  S              → 'silent'
  G              → 'gap'
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
M03 = REPO / "Sessions" / "Session_Clusters" / "M03"
PHASE9 = M03 / "files phase 9"
DIRECTIVE = "DIR-20260517-002"
PHASE10_DIRECTIVE = "DIR-20260517-001"
CLUSTER = "M03"
VERSION = "v1-20260517"

PARTS = [
    ("part1", PHASE9 / "WA-M03-consolidated-findings-v1-20260517-part1.md"),
    ("part2", PHASE9 / "WA-M03-consolidated-findings-v1-20260517-part2-T2.md"),
    ("part3", PHASE9 / "WA-M03-consolidated-findings-v1-20260517-part3-T3-T4.md"),
    ("part4", PHASE9 / "WA-M03-consolidated-findings-v1-20260517-part4-T5-T7.md"),
]

# M03 uses bold-inline prompt headers (**T0.1.1**) not ### T0.1.1
PROMPT_HEADER_RE = re.compile(
    r"^(?:### |\*\*)(T\d+\.\d+\.\d+)(?:\*\*)?[ —\-].*$", re.MULTILINE
)
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
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
        "WHERE tier IS NOT NULL AND deleted=0"
    ).fetchall()
    return {r["question_code"]: r["obs_id"] for r in rows}


def fetch_subgroup_map(conn) -> dict[str, int]:
    rows = conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER,)
    ).fetchall()
    out: dict[str, int] = {}
    for r in rows:
        code = r["subgroup_code"]
        if code.endswith("-BOUNDARY"):
            out["BOUNDARY"] = r["id"]
        else:
            letter = code.split("-")[-1]
            out[letter] = r["id"]
    return out


def parse_scope_marker(raw: str) -> list[dict]:
    s = raw.strip()
    if " vs " not in s and "→" not in s:
        s_main = re.split(r"\s+[—-]\s+", s, maxsplit=1)[0]
    else:
        s_main = s

    if s_main.startswith("BOUNDARY"):
        m = re.match(r"BOUNDARY\s*[—-]\s*(H\d+\w*|G\d+\w*)\s+(.+)$", s.strip())
        if m:
            return [{"subgroup_letter": "BOUNDARY", "vcg_scope": f"term:{m.group(1)}",
                     "cross_cluster_axis": None, "contrast_label": None,
                     "boundary_term": m.group(2).strip()}]
        return [{"subgroup_letter": "BOUNDARY", "vcg_scope": None,
                 "cross_cluster_axis": None, "contrast_label": None, "boundary_term": None}]

    if s_main.startswith("CLUSTER"):
        return [{"subgroup_letter": None, "vcg_scope": None,
                 "cross_cluster_axis": None, "contrast_label": None, "boundary_term": None}]

    if " vs " in s_main:
        return [{"subgroup_letter": None, "vcg_scope": None,
                 "cross_cluster_axis": None, "contrast_label": f"Contrast: {s_main}",
                 "boundary_term": None}]

    if "→" in s_main:
        return [{"subgroup_letter": None, "vcg_scope": None,
                 "cross_cluster_axis": None, "contrast_label": f"Transition: {s_main}",
                 "boundary_term": None}]

    if re.search(r"\bpericope\b", s_main, re.IGNORECASE):
        return [{"subgroup_letter": None, "vcg_scope": None,
                 "cross_cluster_axis": None, "contrast_label": f"Pericope: {s_main}",
                 "boundary_term": None}]

    if re.search(r"\banchor\s*:", s_main, re.IGNORECASE):
        return [{"subgroup_letter": None, "vcg_scope": None,
                 "cross_cluster_axis": None, "contrast_label": f"Anchor focus: {s_main}",
                 "boundary_term": None}]

    elements = [e.strip() for e in s_main.split(",")]
    out: list[dict] = []
    for e in elements:
        # Cross-cluster axis: [A/Wisdom]
        m = re.fullmatch(r"([A-G])/([A-Z]\w+)", e)
        if m and "VCG" not in e:
            out.append({"subgroup_letter": None, "vcg_scope": None,
                        "cross_cluster_axis": m.group(2), "contrast_label": None,
                        "boundary_term": None})
            continue
        # VCG-specific: [E-VCG-02] or [E-VCG-02/03/04/05]
        m = re.fullmatch(r"([A-G])-VCG-(\d+(?:/\d+)*)", e)
        if m:
            letter = m.group(1)
            nums = m.group(2).split("/")
            vcg_codes = [f"{CLUSTER}-{letter}-VCG-{n.zfill(2)}" for n in nums]
            out.append({"subgroup_letter": letter,
                        "vcg_scope": ";".join(vcg_codes),
                        "cross_cluster_axis": None, "contrast_label": None,
                        "boundary_term": None})
            continue
        # VCG with qualifier suffix
        m = re.match(r"^([A-G])-VCG-(\d+(?:/\d+)*)\s+(.+)$", e)
        if m:
            letter = m.group(1)
            nums = m.group(2).split("/")
            vcg_codes = [f"{CLUSTER}-{letter}-VCG-{n.zfill(2)}" for n in nums]
            qualifier = m.group(3)
            out.append({"subgroup_letter": letter,
                        "vcg_scope": ";".join(vcg_codes),
                        "cross_cluster_axis": None,
                        "contrast_label": f"Qualifier: {qualifier}",
                        "boundary_term": None})
            continue
        if re.fullmatch(r"[A-G]", e):
            out.append({"subgroup_letter": e, "vcg_scope": None,
                        "cross_cluster_axis": None, "contrast_label": None,
                        "boundary_term": None})
            continue
        # BOUNDARY as a list element (e.g. "B-VCG-04, BOUNDARY")
        if e == "BOUNDARY":
            out.append({"subgroup_letter": "BOUNDARY", "vcg_scope": None,
                        "cross_cluster_axis": None, "contrast_label": None,
                        "boundary_term": None})
            continue
        log(f"  WARN: unrecognised scope element {e!r} in marker {raw!r}")
    return out


def parse_part(path: Path, label: str) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    out: list[dict] = []
    prompt_matches = list(PROMPT_HEADER_RE.finditer(text))
    for i, m in enumerate(prompt_matches):
        prompt_code = m.group(1)
        start = m.end()
        end = prompt_matches[i+1].start() if i+1 < len(prompt_matches) else len(text)
        body = text[start:end]
        sep_m = SEPARATOR_RE.search(body)
        prompt_body = body[:sep_m.start()] if sep_m else body
        scope_matches = list(SCOPE_LINE_RE.finditer(prompt_body))
        if not scope_matches:
            stripped = prompt_body.strip()
            m_out = OUTCOME_RE.match(stripped)
            outcome = m_out.group(1) if m_out else "S"
            body_text = OUTCOME_RE.sub("", stripped, count=1).strip() if m_out else stripped
            if body_text:
                out.append({
                    "prompt_code": prompt_code,
                    "scope_raw": "(no-marker default → CLUSTER)",
                    "scope_resolved": [{"subgroup_letter": None, "vcg_scope": None,
                                        "cross_cluster_axis": None, "contrast_label": None,
                                        "boundary_term": None}],
                    "outcome": outcome,
                    "body_text": body_text,
                    "source_label": label,
                })
        for j, sm in enumerate(scope_matches):
            scope_raw = sm.group(1).strip()
            head_body = sm.group(2).strip()
            block_start = sm.end()
            block_end = scope_matches[j+1].start() if j+1 < len(scope_matches) else len(prompt_body)
            block_text = (head_body + "\n" + prompt_body[block_start:block_end]).strip()
            m_out = OUTCOME_RE.match(head_body)
            outcome = m_out.group(1) if m_out else "E"
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


def build_rows(parsed_blocks, obs_map, sg_map, source_files):
    grouped: dict[tuple, dict] = {}
    cross_axis_merges: dict[str, list[dict]] = defaultdict(list)
    contrast_merges: dict[str, list[dict]] = defaultdict(list)
    unmapped_prompts: set[str] = set()

    for b in parsed_blocks:
        if b["prompt_code"] not in obs_map:
            unmapped_prompts.add(b["prompt_code"])
            continue
        for scope in b["scope_resolved"]:
            if scope.get("cross_cluster_axis"):
                cross_axis_merges[b["prompt_code"]].append({
                    "axis": scope["cross_cluster_axis"],
                    "outcome": b["outcome"],
                    "body_text": b["body_text"],
                    "source_label": b["source_label"],
                })
                continue
            if scope.get("contrast_label") and not scope.get("vcg_scope") and not scope.get("subgroup_letter"):
                contrast_merges[b["prompt_code"]].append({
                    "label": scope["contrast_label"],
                    "outcome": b["outcome"],
                    "body_text": b["body_text"],
                    "source_label": b["source_label"],
                })
                continue
            sg_letter = scope.get("subgroup_letter")
            sg_id = sg_map[sg_letter] if sg_letter else None
            vcg_scope = scope.get("vcg_scope")
            key = (b["prompt_code"], sg_id, vcg_scope)
            body_with_prefix = b["body_text"]
            if scope.get("contrast_label"):
                body_with_prefix = f"**{scope['contrast_label']}:** {body_with_prefix}"
            if key in grouped:
                existing = grouped[key]
                existing["body_parts"].append((b["outcome"], body_with_prefix, b["source_label"]))
            else:
                grouped[key] = {
                    "prompt_code": b["prompt_code"],
                    "obs_id": obs_map[b["prompt_code"]],
                    "subgroup_id": sg_id,
                    "vcg_scope": vcg_scope,
                    "body_parts": [(b["outcome"], body_with_prefix, b["source_label"])],
                }

    for prompt_code, axis_blocks in cross_axis_merges.items():
        if prompt_code not in obs_map:
            continue
        cluster_key = (prompt_code, None, None)
        if cluster_key not in grouped:
            grouped[cluster_key] = {
                "prompt_code": prompt_code,
                "obs_id": obs_map[prompt_code],
                "subgroup_id": None,
                "vcg_scope": None,
                "body_parts": [],
            }
        for ax in axis_blocks:
            prefix = f"**{CLUSTER} ↔ {ax['axis']} pair:** "
            grouped[cluster_key]["body_parts"].append(
                (ax["outcome"], prefix + ax["body_text"], ax["source_label"])
            )

    for prompt_code, ctr_blocks in contrast_merges.items():
        if prompt_code not in obs_map:
            continue
        cluster_key = (prompt_code, None, None)
        if cluster_key not in grouped:
            grouped[cluster_key] = {
                "prompt_code": prompt_code,
                "obs_id": obs_map[prompt_code],
                "subgroup_id": None,
                "vcg_scope": None,
                "body_parts": [],
            }
        for ct in ctr_blocks:
            prefix = f"**{ct['label']}:** "
            grouped[cluster_key]["body_parts"].append(
                (ct["outcome"], prefix + ct["body_text"], ct["source_label"])
            )

    rows = []
    for key, g in grouped.items():
        outcomes = [bp[0] for bp in g["body_parts"]]
        if "G" in outcomes:
            status = "gap"
        elif all(o == "S" for o in outcomes):
            status = "silent"
        else:
            if g["subgroup_id"] is None and g["vcg_scope"] is None:
                status = "cluster_synthesis"
            else:
                status = "finding"
        if len(g["body_parts"]) == 1:
            body_text = g["body_parts"][0][1]
        else:
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
        "contrast_merges": sum(len(v) for v in contrast_merges.values()),
    }
    return rows, stats


def precheck(conn) -> None:
    log("Running pre-conditions...")
    cluster = conn.execute(
        "SELECT status FROM cluster WHERE cluster_code=?", (CLUSTER,)
    ).fetchone()
    if not cluster or cluster["status"] != "Analysis - In Progress":
        raise RuntimeError(
            f"cluster.status expected 'Analysis - In Progress', "
            f"got {cluster and cluster['status']!r}"
        )
    log(f"  cluster.status = {cluster['status']} ✓")
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=?",
        (CLUSTER, VERSION)
    ).fetchone()
    if r["n"] > 0:
        raise RuntimeError(
            f"cluster_finding already has {r['n']} rows for {CLUSTER} version={VERSION}. Aborting."
        )
    log(f"  no pre-existing cluster_finding rows for {CLUSTER} version={VERSION} ✓")


def fetch_fold_candidates(conn) -> list[dict]:
    """Find rows flagged FOLD-INTO-PROMPT for M03 by Phase 10 (DIR-20260517-001)."""
    rows = []
    for r in conn.execute(f"""
        SELECT 'sbf' AS source, sbf.id, sbf.finding_id, sbf.registry_id, sbf.finding AS text,
               sbf.resolution_note,
               wr.no AS registry_no, wr.word AS registry_word
        FROM wa_session_b_findings sbf
        LEFT JOIN word_registry wr ON wr.id = sbf.registry_id
        WHERE sbf.status='folded'
          AND sbf.resolution_note LIKE '%{PHASE10_DIRECTIVE}%'
          AND sbf.resolution_note LIKE '%FOLD-INTO-PROMPT%'
    """):
        rows.append(dict(r))
    for r in conn.execute(f"""
        SELECT 'srf' AS source, srf.id, srf.flag_label AS finding_id, srf.registry_id,
               srf.description AS text, srf.resolved_note AS resolution_note,
               wr.no AS registry_no, wr.word AS registry_word
        FROM wa_session_research_flags srf
        LEFT JOIN word_registry wr ON wr.id = srf.registry_id
        WHERE srf.resolved=1
          AND srf.resolved_note LIKE '%{PHASE10_DIRECTIVE}%'
          AND srf.resolved_note LIKE '%FOLD-INTO-PROMPT%'
    """):
        rows.append(dict(r))
    return rows


def parse_fold_targets(resolution_note: str) -> list[tuple[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, str]] = []
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

    all_blocks = []
    source_files = {}
    for label, path in PARTS:
        blocks = parse_part(path, label)
        all_blocks.extend(blocks)
        source_files[label] = path.name
        log(f"  Parsed {label}: {len(blocks)} blocks")
    log(f"  Total parsed blocks: {len(all_blocks)}")

    rows, stats = build_rows(all_blocks, obs_map, sg_map, source_files)
    log(f"\n{'='*60}\nOp A — INSERT cluster_finding rows\n{'='*60}")
    log(f"  Rows to insert: {stats['total_rows']}")
    if stats["unmapped_prompts"]:
        log(f"  WARN: unmapped prompts: {stats['unmapped_prompts']}")
    log(f"  Cross-axis merges absorbed: {stats['cross_axis_merges']}")
    log(f"  Contrast/transition/pericope/anchor merges: {stats['contrast_merges']}")

    by_status = defaultdict(int)
    by_vcg = 0
    for r in rows:
        by_status[r["finding_status"]] += 1
        if r["vcg_scope"]:
            by_vcg += 1
    log(f"  By status: {dict(by_status)}")
    log(f"  Rows with vcg_scope: {by_vcg}")

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

    log(f"\n{'='*60}\nOp B + C — Fold inherited findings\n{'='*60}")
    fold_candidates = fetch_fold_candidates(conn)
    log(f"  Fold candidates flagged by Phase 10: {len(fold_candidates)}")
    fold_actions = []
    for fc in fold_candidates:
        src = fc["source"]
        sid = fc["id"]
        targets = parse_fold_targets(fc["resolution_note"] or "")
        log(f"    {src}.id={sid} reg={fc['registry_word']} → targets: {targets}")
        cluster_finding_ids = []
        for tcode, scope_elem in targets:
            obs_id = obs_map.get(tcode)
            if not obs_id:
                log(f"      WARN: T-code {tcode!r} not in obs_map; skipping")
                continue
            sg_id = None
            vcg_scope = None
            if scope_elem == "CLUSTER":
                sg_id = None
            elif scope_elem in sg_map:
                sg_id = sg_map[scope_elem]
            else:
                m_vcg = re.fullmatch(r"([A-G])-VCG-(\d+(?:/\d+)*)", scope_elem)
                if m_vcg:
                    letter = m_vcg.group(1)
                    sg_id = sg_map.get(letter)
                    nums = m_vcg.group(2).split("/")
                    vcg_codes = [f"{CLUSTER}-{letter}-VCG-{n.zfill(2)}" for n in nums]
                    vcg_scope = ";".join(vcg_codes)
                else:
                    log(f"      WARN: scope {scope_elem!r} not parseable; "
                        f"skipping target {tcode} [{scope_elem}]")
                    continue
            if vcg_scope:
                r = conn.execute("""
                    SELECT id FROM cluster_finding
                    WHERE obs_id=? AND cluster_code=? AND cluster_subgroup_id IS ?
                      AND vcg_scope=? AND version=?
                """, (obs_id, CLUSTER, sg_id, vcg_scope, VERSION)).fetchone()
            else:
                r = conn.execute("""
                    SELECT id FROM cluster_finding
                    WHERE obs_id=? AND cluster_code=? AND cluster_subgroup_id IS ?
                      AND vcg_scope IS NULL AND version=?
                """, (obs_id, CLUSTER, sg_id, VERSION)).fetchone()
            if not r:
                log(f"      WARN: no cluster_finding row for obs={tcode} sg={scope_elem} vcg={vcg_scope}")
                continue
            cluster_finding_ids.append(r["id"])
            src_table = "wa_session_b_findings" if src == "sbf" else "wa_session_research_flags"
            fold_prefix = (f"\n\n**[Folded from {src_table}.id={sid}; "
                          f"finding_id={fc['finding_id']}; registry={fc['registry_word']}]**\n")
            fold_body = fc["text"] or ""
            if not dry_run:
                conn.execute(
                    "UPDATE cluster_finding SET finding_text = COALESCE(finding_text,'') || ? "
                    "WHERE id=?",
                    (fold_prefix + fold_body, r["id"])
                )
        if cluster_finding_ids:
            fold_actions.append((src, sid, cluster_finding_ids))
            if not dry_run:
                note_append = (
                    f" | {DIRECTIVE}: folded into cluster_finding.id IN "
                    f"({','.join(str(i) for i in cluster_finding_ids)})"
                )
                if src == "sbf":
                    conn.execute(
                        "UPDATE wa_session_b_findings SET resolution_note = "
                        "COALESCE(resolution_note,'') || ? WHERE id=?",
                        (note_append, sid)
                    )
                else:
                    conn.execute(
                        "UPDATE wa_session_research_flags SET resolved_note = "
                        "COALESCE(resolved_note,'') || ? WHERE id=?",
                        (note_append, sid)
                    )
    log(f"  Folded {len(fold_actions)} inherited findings.")
    return {"inserted": stats["total_rows"], "folded": len(fold_actions), "fold_actions": fold_actions}


def healthcheck(conn) -> None:
    log(f"\n{'='*60}\nHealth checks\n{'='*60}")
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=?",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P1 cluster_finding rows for {CLUSTER} v={VERSION}: {r['n']}")
    r = conn.execute(
        "SELECT COUNT(DISTINCT obs_id) AS n FROM cluster_finding "
        "WHERE cluster_code=? AND version=?",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P2 distinct prompts: {r['n']} (expected 189) "
        f"{'✓' if r['n']==189 else '✗'}")
    assert r["n"] == 189
    log(f"  P3 status distribution:")
    for row in conn.execute(
        "SELECT finding_status, COUNT(*) AS n FROM cluster_finding "
        "WHERE cluster_code=? AND version=? GROUP BY finding_status ORDER BY n DESC",
        (CLUSTER, VERSION)
    ):
        log(f"      {row['finding_status']}: {row['n']}")
    r = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding "
        "WHERE cluster_code=? AND version=? AND vcg_scope IS NOT NULL",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P4 rows with vcg_scope set: {r['n']}")
    r = conn.execute(
        """SELECT COUNT(*) AS n FROM cluster_finding WHERE cluster_code=? AND version=?
           AND (finding_text LIKE '%[Folded from wa_session_b_findings.id=%'
                OR finding_text LIKE '%[Folded from wa_session_research_flags.id=%')""",
        (CLUSTER, VERSION)
    ).fetchone()
    log(f"  P5 rows carrying fold-in markers: {r['n']} (expected ≥1 for sbf.73)")
    assert r["n"] >= 1


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

    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
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
        log(f"\nDONE — {'simulated' if dry_run else 'applied'}: "
            f"inserted={result['inserted']} folded={result['folded']}")
    except Exception as e:
        log(f"ERROR: {e}")
        try: conn.execute("ROLLBACK")
        except: pass
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
