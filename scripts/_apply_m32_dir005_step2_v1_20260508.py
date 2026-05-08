"""_apply_m32_dir005_step2_v1_20260508.py — DB-modifying.

DIR-20260508-004 (dir-005), Step B — Full-text loader for M32.

Parses the four consolidated-findings parts and updates the stub rows
created in Step A. Non-authored stubs remain at status='finding' with
the placeholder text.

Marker patterns:
  **[A]**, **[A — Conscience]**                    → M32-A
  **[B]**, **[B — Self-Awareness / Inner Attention]** → M32-B
  **[CLUSTER]**, **[CLUSTER — anything-but-Finding]** → cluster-level,
                                                    default 'cluster_synthesis'
                                                    (overridden if body marks
                                                    explicit gap/silent)
  **[CLUSTER — Finding N: ...]**                   → cluster-level,
                                                    'cluster_synthesis'

Body-text status overrides (for sub-group markers):
  body starts 'S —' or 'Silent'  → 'silent'
  body starts 'G —' or 'Gap'     → 'gap'
  body starts 'E —' or 'E ' or anything else → 'finding'

Q-headers in M32 sources use **T#.#.#** — text format (not ### T...).
"""
from __future__ import annotations

import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M32"
PATCH_VERSION = "v1"

PARTS = [
    ("Sessions/Session_Clusters/M32/WA-M32-consolidated-findings-v1-20260508-part1.md",
     "WA-M32-consolidated-findings-v1-20260508-part1.md"),
    ("Sessions/Session_Clusters/M32/WA-M32-consolidated-findings-v1-20260508-part2-T2.md",
     "WA-M32-consolidated-findings-v1-20260508-part2-T2.md"),
    ("Sessions/Session_Clusters/M32/WA-M32-consolidated-findings-v1-20260508-part3-T3-T4.md",
     "WA-M32-consolidated-findings-v1-20260508-part3-T3-T4.md"),
    ("Sessions/Session_Clusters/M32/WA-M32-consolidated-findings-v1-20260508-part4-T5-T7.md",
     "WA-M32-consolidated-findings-v1-20260508-part4-T5-T7.md"),
]

# Q-header style for M32: **T#.#.#** — text
QCODE_RE = re.compile(r"^\*\*(T\d+\.\d+\.\d+)\*\*\s*[—-]")
# Marker: **[scope]** ... ** with possibly extra text inside the bold span
MARKER_RE = re.compile(r"^\*\*\[([^\]]+)\][^*]*\*\*\s*(.*)$")
# Section heading like "### T1.3 — Boundary"
H3_RE = re.compile(r"^###\s+")
# Bold "BOUNDARY — <term> (<strongs>):" — special inline marker at T1.2.1
BOUNDARY_RE = re.compile(r"^\*\*BOUNDARY\b")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def expand_scope(scope_str: str):
    """Return (kind, payload) — kind in {'subgroup','cluster','synthesis'}.

    'synthesis' means cluster-level with explicit cluster_synthesis status
    (the **[CLUSTER — Finding N: ...]** form). Plain '[CLUSTER]' or
    '[CLUSTER — ...]' (other than Finding N) returns ('cluster', None) and
    the caller decides default status (we use 'cluster_synthesis' too,
    matching the M05/M06 precedent).
    """
    s = scope_str.strip()
    upper = s.upper()
    if upper.startswith("CLUSTER"):
        if "FINDING" in upper:
            return ("synthesis", None)
        return ("cluster", None)
    # Sub-group: starts with letter A or B (single letter, possibly followed
    # by " — Label")
    m = re.match(r"^([AB])(?:\s*[—-].*)?$", s)
    if m:
        return ("subgroup", m.group(1))
    return (None, None)


def determine_status(scope_kind: str, body: str) -> str:
    if scope_kind in ("cluster", "synthesis"):
        return "cluster_synthesis"
    low = body.lstrip().lower()
    if low.startswith("silent") or low.startswith("s —") or low.startswith("s -"):
        return "silent"
    if low.startswith("gap") or low.startswith("g —") or low.startswith("g -"):
        return "gap"
    return "finding"


def parse_part(file_path: str):
    """Yield (qcode, scope_kind, payload, body, status) per marker."""
    text = Path(file_path).read_text(encoding="utf-8")
    lines = text.splitlines()
    cur_q = None
    i = 0
    while i < len(lines):
        line = lines[i]

        m = QCODE_RE.match(line)
        if m:
            cur_q = m.group(1)
            i += 1
            continue

        m = MARKER_RE.match(line)
        if m and cur_q is not None:
            scope_str = m.group(1)
            body_first = m.group(2)
            kind, payload = expand_scope(scope_str)
            if kind is None:
                i += 1
                continue

            # Capture body — continue until next marker / qcode / heading /
            # bold-line that isn't body-text
            body_parts = [body_first] if body_first else []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if (
                    MARKER_RE.match(nxt)
                    or QCODE_RE.match(nxt)
                    or H3_RE.match(nxt)
                    or BOUNDARY_RE.match(nxt)
                    or nxt.strip() == "---"
                ):
                    break
                body_parts.append(nxt)
                j += 1
            body = "\n".join(body_parts).strip()

            status = determine_status(kind, body)
            if kind == "synthesis":
                yield (cur_q, "cluster", None, body, "cluster_synthesis")
            elif kind == "cluster":
                yield (cur_q, "cluster", None, body, status)
            else:  # subgroup
                yield (cur_q, "subgroup", payload, body, status)

            i = j
            continue

        i += 1


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sg_id_by_letter = {}
    for letter in "AB":
        r = cur.execute(
            "SELECT id FROM cluster_subgroup "
            " WHERE cluster_code=? AND subgroup_code=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (CLUSTER_CODE, f"M32-{letter}"),
        ).fetchone()
        sg_id_by_letter[letter] = r["id"]
    print("Sub-group ids:", sg_id_by_letter)

    obs_by_q = {
        r["question_code"]: r["obs_id"]
        for r in cur.execute(
            "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
            " WHERE catalogue_version='v2-2026-04-29' "
            "   AND COALESCE(deleted,0)=0"
        )
    }
    print(f"Catalogue lookup populated: {len(obs_by_q)} entries")

    n_subgroup_updated = 0
    n_cluster_updated = 0
    n_promoted_to_silent = 0
    n_promoted_to_gap = 0
    n_promoted_to_synth = 0
    halts = []
    parsed_yields = 0

    ts = now_iso()
    try:
        cur.execute("BEGIN")
        for src_path, src_basename in PARTS:
            print(f"\nParsing {src_basename} ...")
            n_part = 0
            for qcode, scope_kind, payload, body, status in parse_part(src_path):
                parsed_yields += 1
                n_part += 1
                obs_id = obs_by_q.get(qcode)
                if obs_id is None:
                    halts.append(("UNKNOWN_QCODE", qcode, src_basename))
                    continue

                if scope_kind == "subgroup":
                    sg_id = sg_id_by_letter.get(payload)
                    if sg_id is None:
                        halts.append(("UNKNOWN_SUBGROUP", payload, src_basename))
                        continue
                    rc = cur.execute(
                        "UPDATE cluster_finding "
                        "   SET finding_text=?, finding_status=?, "
                        "       source_file=?, last_updated_date=? "
                        " WHERE obs_id=? AND cluster_code=? "
                        "   AND cluster_subgroup_id=? AND version=? "
                        "   AND COALESCE(delete_flagged,0)=0",
                        (body, status, src_basename, ts,
                         obs_id, CLUSTER_CODE, sg_id, PATCH_VERSION),
                    ).rowcount
                    if rc:
                        n_subgroup_updated += 1
                        if status == "silent":
                            n_promoted_to_silent += 1
                        elif status == "gap":
                            n_promoted_to_gap += 1
                    else:
                        halts.append(("NO_STUB", f"{qcode}/M32-{payload}",
                                      src_basename))
                else:  # cluster
                    rc = cur.execute(
                        "UPDATE cluster_finding "
                        "   SET finding_text=?, finding_status=?, "
                        "       source_file=?, last_updated_date=? "
                        " WHERE obs_id=? AND cluster_code=? "
                        "   AND cluster_subgroup_id IS NULL "
                        "   AND version=? "
                        "   AND COALESCE(delete_flagged,0)=0",
                        (body, status, src_basename, ts,
                         obs_id, CLUSTER_CODE, PATCH_VERSION),
                    ).rowcount
                    if rc:
                        n_cluster_updated += 1
                        if status == "cluster_synthesis":
                            n_promoted_to_synth += 1
                        elif status == "gap":
                            n_promoted_to_gap += 1
                    else:
                        halts.append(("NO_CLUSTER_STUB", qcode, src_basename))
            print(f"  yielded {n_part} markers")

        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print()
    print(f"Parsed yields total:        {parsed_yields}")
    print(f"Sub-group rows updated:     {n_subgroup_updated}")
    print(f"Cluster-level rows updated: {n_cluster_updated}")
    print(f"  promoted to silent:       {n_promoted_to_silent}")
    print(f"  promoted to gap:          {n_promoted_to_gap}")
    print(f"  promoted to synthesis:    {n_promoted_to_synth}")
    print(f"Halts (issues):             {len(halts)}")
    if halts:
        from collections import Counter
        bykind = Counter(h[0] for h in halts)
        for k, n in bykind.items():
            print(f"  {k}: {n}")
        for h in halts[:10]:
            print(f"   {h}")

    print()
    print("=== M32 cluster_finding by status ===")
    for r in cur.execute(
        "SELECT finding_status, COUNT(*) AS n FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY finding_status ORDER BY finding_status",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['finding_status']:25s} {r['n']:5d}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
