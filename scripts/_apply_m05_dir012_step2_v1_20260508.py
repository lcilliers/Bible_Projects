"""_apply_m05_dir012_step2_v1_20260508.py — DB-modifying.

DIR-20260507-M05-012, Step 2 — Full-text loader.

Parses the four consolidated-findings parts and updates the stub
rows created in Step 1 with authored finding_text and the correct
finding_status. Stubs that aren't authored in the source remain as
status='finding' with the placeholder text.

Marker patterns recognised (per directive §SCOPE — Marker recognition):

  **[A]**, **[A] Love:**, **[A — Love]**       → sub-group A
  **[A-G]**                                     → range A..G
  **[B-D]**                                     → range B..D
  **[A, C, D, E, F, G]**                        → comma list
  **[CLUSTER]**                                 → cluster_subgroup_id=NULL
                                                  status='cluster_synthesis'
  **[G-code Tx.y.z]**                           → status='gap' written at
                                                  obs_id(Tx.y.z),
                                                  cluster_subgroup_id=NULL

Body-text status overrides (within a sub-group marker only):

  Body starts with 'Silent' or 'S —'           → status='silent'
  Body starts with 'Gap' or 'G —'              → status='gap'
  Body starts with 'Partial' or 'P —'          → status='finding'
  Otherwise                                    → status='finding'

Three G-codes named in directive (T6.4.3, T6.6.3, T6.7.3) must be
recorded as gap rows. T6.6.3 and T6.7.3 are already represented by
inline [G-code …] markers; T6.4.3 has no inline marker and is sourced
from the closing-section list in part 4.
"""
from __future__ import annotations

import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
CLUSTER_CODE = "M05"
PATCH_VERSION = "v1"

PARTS = [
    ("Sessions/Session_Clusters/M05/files session 2 consolidation/"
     "WA-M05-consolidated-findings-v1-20260507-part1.md",
     "WA-M05-consolidated-findings-v1-20260507-part1.md"),
    ("Sessions/Session_Clusters/M05/files session 2 consolidation/"
     "WA-M05-consolidated-findings-v1-20260507-part2.md",
     "WA-M05-consolidated-findings-v1-20260507-part2.md"),
    ("Sessions/Session_Clusters/M05/files session 2 consolidation/"
     "WA-M05-consolidated-findings-v1-20260507-part3.md",
     "WA-M05-consolidated-findings-v1-20260507-part3.md"),
    ("Sessions/Session_Clusters/M05/files session 2 consolidation/"
     "WA-M05-consolidated-findings-v1-20260507-part4.md",
     "WA-M05-consolidated-findings-v1-20260507-part4.md"),
]

QCODE_RE = re.compile(r"^###\s+(T\d+\.\d+\.\d+)\b")
MARKER_RE = re.compile(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$")
GCODE_INNER_RE = re.compile(r"^G-code\s+(T\d+\.\d+\.\d+)$", re.IGNORECASE)
RANGE_RE = re.compile(r"^([A-G])\s*-\s*([A-G])$")
SINGLE_RE = re.compile(r"^([A-G])$")
LABELED_RE = re.compile(r"^([A-G])\b")  # e.g. "A Love" or "A — Love"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def expand_scope(scope_str):
    """Return a list of (kind, payload) where kind is 'subgroup', 'cluster',
    or 'gcode', and payload is the sub-group letter, None, or the redirected
    T-code."""
    s = scope_str.strip()

    # CLUSTER (any variant)
    if s.upper().startswith("CLUSTER"):
        return [("cluster", None)]

    # G-code Tx.y.z
    m = GCODE_INNER_RE.match(s)
    if m:
        return [("gcode", m.group(1))]

    # Range A-G or A-D
    m = RANGE_RE.match(s)
    if m:
        a, b = m.group(1), m.group(2)
        if a > b:
            a, b = b, a
        return [("subgroup", chr(c)) for c in range(ord(a), ord(b) + 1)]

    # Comma list "A, C, D, E, F, G"
    if "," in s:
        out = []
        for piece in s.split(","):
            p = piece.strip()
            mm = SINGLE_RE.match(p)
            if mm:
                out.append(("subgroup", mm.group(1)))
            else:
                # also accept first letter ("A — Love")
                mm = LABELED_RE.match(p)
                if mm:
                    out.append(("subgroup", mm.group(1)))
        if out:
            return out

    # Single letter, possibly followed by a label
    m = SINGLE_RE.match(s)
    if m:
        return [("subgroup", m.group(1))]
    m = LABELED_RE.match(s)
    if m:
        return [("subgroup", m.group(1))]

    # Unrecognised
    return []


def determine_status(scope_kind, body):
    if scope_kind == "cluster":
        return "cluster_synthesis"
    if scope_kind == "gcode":
        return "gap"
    low = body.lstrip().lower()
    if low.startswith("silent") or low.startswith("s —") or low.startswith("s -"):
        return "silent"
    if low.startswith("gap") or low.startswith("g —") or low.startswith("g -"):
        return "gap"
    return "finding"


def parse_part(file_path):
    """Yield (qcode, scope_kind, scope_letter_or_T, body_text)."""
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
            scope_targets = expand_scope(scope_str)

            # Capture body: continuation lines until next marker / heading / ---
            body_parts = [body_first] if body_first else []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if (
                    MARKER_RE.match(nxt)
                    or QCODE_RE.match(nxt)
                    or nxt.strip() == "---"
                    or nxt.startswith("## ")
                    or nxt.startswith("### ")
                ):
                    break
                body_parts.append(nxt)
                j += 1
            body = "\n".join(body_parts).strip()

            for kind, payload in scope_targets:
                if kind == "gcode":
                    yield (payload, "cluster", None, body, "gap")
                elif kind == "cluster":
                    yield (cur_q, "cluster", None, body, "cluster_synthesis")
                else:
                    sub_letter = payload  # 'A'..'G'
                    status = determine_status("subgroup", body)
                    yield (cur_q, "subgroup", sub_letter, body, status)

            i = j
            continue

        i += 1


def main():
    print(f"DB: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Resolve M05 sub-group ids
    sg_id_by_letter = {}
    for letter in "ABCDEFG":
        r = conn.execute(
            "SELECT id FROM cluster_subgroup "
            " WHERE cluster_code=? AND subgroup_code=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (CLUSTER_CODE, f"M05-{letter}"),
        ).fetchone()
        sg_id_by_letter[letter] = r["id"]
    print("Sub-group ids:", sg_id_by_letter)

    # Build qcode -> obs_id lookup (only directive's catalogue version)
    obs_by_qcode = {}
    for r in conn.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
        " WHERE catalogue_version='v2-2026-04-29' AND COALESCE(deleted,0)=0"
    ):
        obs_by_qcode[r["question_code"]] = r["obs_id"]
    print(f"Catalogue obs lookup populated: {len(obs_by_qcode)} entries")

    # Stats
    n_updated_subgroup = 0
    n_updated_cluster = 0
    n_promoted_to_silent = 0
    n_promoted_to_gap = 0
    n_promoted_to_synth = 0
    halts = []
    unrecognised_scopes = []
    parsed_yields = 0

    ts = now_iso()
    try:
        conn.execute("BEGIN")

        for src_path, src_basename in PARTS:
            print(f"\nParsing {src_basename} ...")
            n_part = 0
            for qcode, scope_kind, sub_letter, body, status in parse_part(src_path):
                parsed_yields += 1
                n_part += 1
                obs_id = obs_by_qcode.get(qcode)
                if obs_id is None:
                    halts.append(("UNKNOWN_QCODE", qcode, src_basename))
                    continue

                if scope_kind == "subgroup":
                    sg_id = sg_id_by_letter.get(sub_letter)
                    if sg_id is None:
                        halts.append(("UNKNOWN_SUBGROUP", sub_letter,
                                      src_basename))
                        continue
                    rc = conn.execute(
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
                        n_updated_subgroup += 1
                        if status == "silent":
                            n_promoted_to_silent += 1
                        elif status == "gap":
                            n_promoted_to_gap += 1
                    else:
                        halts.append(("NO_STUB_FOUND",
                                     f"{qcode}/M05-{sub_letter}",
                                     src_basename))
                else:  # cluster
                    rc = conn.execute(
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
                        n_updated_cluster += 1
                        if status == "cluster_synthesis":
                            n_promoted_to_synth += 1
                        elif status == "gap":
                            n_promoted_to_gap += 1
                    else:
                        halts.append(("NO_CLUSTER_STUB",
                                      qcode, src_basename))
            print(f"  yielded {n_part} markers")

        # Special case: T6.4.3 has no inline [G-code] marker but is named
        # in the directive's three G-codes. Source line 478 of part4 lists
        # it. Write the gap row from that text.
        T643_TEXT = (
            "T6.4.3 — cross-registry chesed distribution count (first raised "
            "M05-A; reconfirmed through all sub-groups). G-code recorded "
            "from outstanding-actions list in WA-M05-consolidated-findings-"
            "v1-20260507-part4 §Outstanding CC actions and G-codes."
        )
        obs_643 = obs_by_qcode.get("T6.4.3")
        if obs_643 is not None:
            rc = conn.execute(
                "UPDATE cluster_finding "
                "   SET finding_text=?, finding_status='gap', "
                "       source_file=?, last_updated_date=? "
                " WHERE obs_id=? AND cluster_code=? "
                "   AND cluster_subgroup_id IS NULL "
                "   AND version=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (T643_TEXT,
                 "WA-M05-consolidated-findings-v1-20260507-part4.md",
                 ts, obs_643, CLUSTER_CODE, PATCH_VERSION),
            ).rowcount
            if rc:
                print(f"\nT6.4.3 gap row written (rc={rc})")
                n_updated_cluster += 1
                n_promoted_to_gap += 1
        else:
            halts.append(("UNKNOWN_QCODE", "T6.4.3 (directive G-code)",
                          "directive"))

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print()
    print(f"Parsed yields total:       {parsed_yields}")
    print(f"Sub-group rows updated:    {n_updated_subgroup}")
    print(f"Cluster-level rows updated: {n_updated_cluster}")
    print(f"  promoted to silent:      {n_promoted_to_silent}")
    print(f"  promoted to gap:         {n_promoted_to_gap}")
    print(f"  promoted to synthesis:   {n_promoted_to_synth}")
    print(f"Halts (problems):          {len(halts)}")
    if halts:
        from collections import Counter
        bykind = Counter(h[0] for h in halts)
        for kind, n in bykind.items():
            print(f"  {kind}: {n}")
        # Show first 10
        for h in halts[:10]:
            print(f"   {h}")

    # Verification — distribution
    print()
    print("=== Verification: M05 cluster_finding by status ===")
    for r in conn.execute(
        "SELECT finding_status, COUNT(*) AS n FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY finding_status ORDER BY finding_status",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['finding_status']:25s} {r['n']:5d}")

    print()
    print("=== Per sub-group + cluster-level row counts ===")
    for r in conn.execute(
        "SELECT "
        "  CASE WHEN cluster_subgroup_id IS NULL THEN 'CLUSTER-LEVEL' "
        "       ELSE (SELECT subgroup_code FROM cluster_subgroup "
        "             WHERE id=cluster_finding.cluster_subgroup_id) END "
        "    AS scope, "
        "  COUNT(*) AS n "
        "  FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        " GROUP BY scope ORDER BY scope",
        (CLUSTER_CODE,),
    ):
        print(f"  {r['scope']:15s} {r['n']:5d}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
