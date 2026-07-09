"""Apply wa-cluster-M46-dir-001-findings-record-v1-20260515.md — Phase 9 cluster_finding load.

Parses the 4 consolidated findings markdown files for M46 and inserts cluster_finding
rows per the directive's parsing rules.

Format expected per scope marker:
  **T{tier}.{component}.{seq}** — <question text>            (prompt header)

  **[A]** <body>                                              (scope marker + body)
  **[A — Inner closure]** <body>
  **[A, B]** <body>                                           (combined → split)
  **[CLUSTER]** <body>                                         (cluster scope, subgroup_id=NULL)

Status mapping from body prefix:
  S — ...   → silent
  G — ...   → gap
  (other)   → finding (or cluster_synthesis for CLUSTER scope)

Also handles "CLUSTER-LEVEL ADDITIONS — Phase 9 cross-sub-group review" sections in
parts 1–3: each `**T#.#.#** — supplementary cluster finding` followed by a scope marker
creates an additional row (per directive §SCOPE bullet 3).

Usage: python scripts/_apply_m46_dir001_findings_record_20260515.py [--dry-run]
"""
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
INPUT_DIR = REPO / "Sessions" / "Session_Clusters" / "M46" / "files phase 9"
PARTS = [
    "wa-cluster-M46-consolidated-findings-v1-20260515-part1.md",
    "wa-cluster-M46-consolidated-findings-v1-20260515-part2.md",
    "wa-cluster-M46-consolidated-findings-v1-20260515-part3.md",
    "wa-cluster-M46-consolidated-findings-v1-20260515-part4.md",
]

CLUSTER_CODE = "M46"
DIRECTIVE = "wa-cluster-M46-dir-001-findings-record-v1-20260515"
INSTRUCTION_VERSION = "wa-sessionb-cluster-instruction-v1_13-20260514"
CATALOGUE_VERSION = "v2.1-2026-05-15"  # stamped on emitted rows

# Subgroup letter → cluster_subgroup.id (M46 subgroups)
SUBGROUP_ID = {"A": 45, "B": 46, "C": 47, "D": 48}

PROMPT_HEADER_RE = re.compile(r"^\*\*(T\d+\.\d+\.\d+(?:\s*,\s*T\d+\.\d+\.\d+)*)\*\*\s*(.*)$")
SCOPE_LINE_RE = re.compile(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$")
HORIZ_RULE_RE = re.compile(r"^---+\s*$")
INLINE_DIRECT_RE = re.compile(r"^\s*([SGE])\s*[—\-]\s*(.*)$", re.DOTALL)


def parse_scope_letters(scope_str: str) -> list[str]:
    """Parse '[A]', '[A — Inner closure]', '[A, B]', '[CLUSTER — ...]' etc → list of letters or ['CLUSTER']."""
    s = scope_str.strip()
    # Drop trailing "— label" if present
    if "—" in s:
        s = s.split("—", 1)[0].strip()
    if s.upper() == "CLUSTER":
        return ["CLUSTER"]
    letters = []
    for tok in re.split(r"[,\s]+", s):
        tok = tok.strip()
        if not tok: continue
        if tok in ("A", "B", "C", "D"):
            letters.append(tok)
        elif tok.upper() == "CLUSTER":
            letters.append("CLUSTER")
    return letters


def classify_status(body: str, is_cluster_scope: bool) -> tuple[str, str]:
    """Return (finding_status, cleaned_body) — strip leading S—/G—/E— prefix."""
    body_stripped = body.lstrip()
    m = re.match(r"^([SGE])\s*[—\-]\s*(.*)", body_stripped, re.DOTALL)
    if m:
        prefix, rest = m.group(1), m.group(2)
        if prefix == "S":
            return "silent", rest.strip()
        elif prefix == "G":
            return "gap", rest.strip()
        elif prefix == "E":
            return ("cluster_synthesis" if is_cluster_scope else "finding"), rest.strip()
    return ("cluster_synthesis" if is_cluster_scope else "finding"), body.strip()


def parse_file(path: Path) -> list[dict]:
    """Yield (prompt_code, scope_letter, status, body, source_file, is_addition) records."""
    rows = []
    lines = path.read_text(encoding="utf-8").splitlines()

    cur_prompts: list[str] = []  # may be multi-code, e.g. ["T3.5.2","T3.5.3"]
    cur_scope_letters = None
    cur_body: list[str] = []
    in_additions = False

    def flush():
        if cur_prompts and cur_scope_letters is not None:
            body_text = "\n".join(cur_body).strip()
            for prompt_code in cur_prompts:
                for L in cur_scope_letters:
                    is_cluster = (L == "CLUSTER")
                    status, cleaned = classify_status(body_text, is_cluster)
                    rows.append({
                        "prompt_code": prompt_code,
                        "scope": L,
                        "status": status,
                        "body": cleaned,
                        "source_file": path.name,
                        "is_addition": in_additions,
                    })

    for i, raw in enumerate(lines):
        line = raw.rstrip("\n")

        if "CLUSTER-LEVEL ADDITIONS" in line and line.startswith("## "):
            flush()
            cur_prompts = []
            cur_scope_letters = None
            cur_body = []
            in_additions = True
            continue

        # Prompt header — may be single or multi-code
        m = PROMPT_HEADER_RE.match(line.strip())
        if m:
            flush()
            cur_prompts = [c.strip() for c in m.group(1).split(",")]
            cur_scope_letters = None
            cur_body = []
            # Check whether the trailing text after `** —` is a direct-body
            # (`S —` / `G —` / `E —` immediately) rather than a question.
            trailing = m.group(2).lstrip("— -").strip()
            direct = INLINE_DIRECT_RE.match(trailing)
            if direct:
                # This is a multi-code direct-body line. Implicit scope = CLUSTER.
                cur_scope_letters = ["CLUSTER"]
                cur_body = [trailing]  # keep full prefix so classify_status can strip it
            continue

        # Scope marker line — may also carry leading inline body
        m = SCOPE_LINE_RE.match(line.strip())
        if m:
            flush()
            scope_str, inline_body = m.group(1), m.group(2)
            cur_scope_letters = parse_scope_letters(scope_str)
            cur_body = [inline_body] if inline_body.strip() else []
            continue

        # Horizontal rule ends a scope block
        if HORIZ_RULE_RE.match(line.strip()):
            flush()
            cur_scope_letters = None
            cur_body = []
            continue

        # Section header (### or ## that's not a finding row)
        if line.startswith("### ") or line.startswith("## "):
            flush()
            cur_scope_letters = None
            cur_body = []
            continue

        # Accumulate body lines
        if cur_scope_letters is not None:
            cur_body.append(line)

    flush()
    return rows


def main():
    dry_run = "--dry-run" in sys.argv
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    # Build T-code → obs_id map
    code_to_obs = {}
    for r in conn.execute(
        "SELECT question_code, obs_id FROM wa_obs_question_catalogue WHERE question_code LIKE 'T%' AND deleted=0"
    ):
        code_to_obs[r["question_code"]] = r["obs_id"]
    print(f"Loaded {len(code_to_obs)} T-coded catalogue prompts")

    all_rows = []
    for part in PARTS:
        path = INPUT_DIR / part
        parsed = parse_file(path)
        all_rows.extend(parsed)
        print(f"  {part}: parsed {len(parsed)} (prompt, scope) rows")

    print(f"\nTotal parsed rows: {len(all_rows)}")

    # Resolve obs_id, count missing
    missing_codes = set()
    for r in all_rows:
        if r["prompt_code"] not in code_to_obs:
            missing_codes.add(r["prompt_code"])
    if missing_codes:
        print(f"\nWARNING: {len(missing_codes)} prompt codes not in catalogue:")
        for c in sorted(missing_codes): print(f"  {c}")
        return

    # Status summary
    from collections import Counter
    status_count = Counter(r["status"] for r in all_rows)
    print(f"\nStatus distribution: {dict(status_count)}")

    # Scope letter summary
    scope_count = Counter(r["scope"] for r in all_rows)
    print(f"Scope distribution: {dict(scope_count)}")

    # Addition rows
    n_additions = sum(1 for r in all_rows if r["is_addition"])
    print(f"CLUSTER-LEVEL ADDITION rows: {n_additions}")

    # Group by (prompt_code, scope) — additions merge into inline rows per directive
    # ("they are additions to the prompt records at T1.1.3 etc.").
    # UNIQUE constraint on cluster_finding(obs_id, cluster_code, cluster_subgroup_id, version)
    # enforces one row per (prompt, scope, version).
    grouped: dict[tuple[str, str], dict] = {}
    for r in all_rows:
        key = (r["prompt_code"], r["scope"])
        if key not in grouped:
            grouped[key] = {
                "prompt_code": r["prompt_code"],
                "scope": r["scope"],
                "bodies": [],
                "statuses": [],
                "sources": [],
                "any_addition": False,
            }
        # Annotate addition bodies with a separator
        body = r["body"]
        if r["is_addition"]:
            body = "[Cluster-level addition — Phase 9 cross-sub-group review] " + body
            grouped[key]["any_addition"] = True
        grouped[key]["bodies"].append(body)
        grouped[key]["statuses"].append(r["status"])
        grouped[key]["sources"].append(r["source_file"])

    # Resolve final status per group: gap > silent > finding/cluster_synthesis
    def final_status(statuses: list[str], is_cluster_scope: bool) -> str:
        if "gap" in statuses: return "gap"
        if all(s == "silent" for s in statuses): return "silent"
        if "silent" in statuses and any(s != "silent" for s in statuses):
            # Mixed silent + finding — the finding wins
            return "cluster_synthesis" if is_cluster_scope else "finding"
        return "cluster_synthesis" if is_cluster_scope else "finding"

    print(f"\nUnique (prompt, scope) groups: {len(grouped)}")
    n_merged = sum(1 for v in grouped.values() if len(v["bodies"]) > 1)
    print(f"Groups with >1 body (inline + addition merged): {n_merged}")

    # Insert
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    inserts = 0
    try:
        for key, g in grouped.items():
            obs_id = code_to_obs[g["prompt_code"]]
            sg_id = SUBGROUP_ID.get(g["scope"])  # None for CLUSTER
            is_cluster_scope = (g["scope"] == "CLUSTER")
            status = final_status(g["statuses"], is_cluster_scope)
            body = "\n\n".join(g["bodies"])
            sources = "; ".join(sorted(set(g["sources"])))
            kind = "Phase 9 inline + addition merge" if g["any_addition"] else "Phase 9 inline finding"
            notes = (
                f"{DIRECTIVE} ({kind}); "
                f"source: {sources}; "
                f"catalogue: {g['prompt_code']}; "
                f"scope: {g['scope']}; "
                f"governing_instruction: {INSTRUCTION_VERSION}"
            )
            conn.execute(
                """INSERT INTO cluster_finding
                   (obs_id, cluster_code, cluster_subgroup_id, finding_status, finding_text,
                    source_file, version, notes, delete_flagged, created_at, last_updated_date)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)""",
                (obs_id, CLUSTER_CODE, sg_id, status, body,
                 sources, CATALOGUE_VERSION, notes, now, now)
            )
            inserts += 1

        if dry_run:
            conn.rollback()
            print(f"\n[DRY RUN] Would insert {inserts} rows. Rolled back.")
        else:
            conn.commit()
            print(f"\nInserted {inserts} cluster_finding rows. Committed.")
    except Exception as exc:
        conn.rollback()
        print(f"\nERROR: {exc}\nRolled back.")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
