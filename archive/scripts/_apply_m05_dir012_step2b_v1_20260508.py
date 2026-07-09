"""_apply_m05_dir012_step2b_v1_20260508.py — DB-modifying.

Corrective second pass for Step 2 of DIR-20260507-M05-012. The strict
marker regex used by step2 missed the `**[A] Love:**`-style variant
(label inside the same bold span as the scope tag). This script uses
a loose regex that accepts any text between `]` and the closing `**`,
and updates ONLY stub rows (source_file='[stub-loader-step1]') so
that already-authored rows are not touched.
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
STUB_SOURCE = "[stub-loader-step1]"

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
# Loose: allows label text between ] and closing **
MARKER_RE = re.compile(r"^\*\*\[([^\]]+)\]([^*]*)\*\*\s*(.*)$")
SINGLE_RE = re.compile(r"^([A-G])$")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sg_id_by_letter = {}
    for letter in "ABCDEFG":
        r = cur.execute(
            "SELECT id FROM cluster_subgroup "
            " WHERE cluster_code=? AND subgroup_code=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (CLUSTER_CODE, f"M05-{letter}"),
        ).fetchone()
        sg_id_by_letter[letter] = r["id"]

    obs_by_q = {}
    for r in cur.execute(
        "SELECT obs_id, question_code FROM wa_obs_question_catalogue "
        " WHERE catalogue_version='v2-2026-04-29' "
        "   AND COALESCE(deleted,0)=0"
    ):
        obs_by_q[r["question_code"]] = r["obs_id"]

    n_updated = 0
    n_seen = 0
    seen_examples = []

    ts = now_iso()

    try:
        cur.execute("BEGIN")

        for src_path, src_basename in PARTS:
            text = Path(src_path).read_text(encoding="utf-8")
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
                    scope_str = m.group(1).strip()
                    label_inside_bold = m.group(2).strip()
                    body_first = m.group(3).strip()
                    n_seen += 1

                    # Capture body
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

                    # Only process simple A..G single-letter scopes — these
                    # are the ones the strict regex missed (loose variant).
                    sm = SINGLE_RE.match(scope_str)
                    if sm:
                        letter = sm.group(1)
                        sg_id = sg_id_by_letter[letter]
                        obs_id = obs_by_q.get(cur_q)
                        if obs_id is None:
                            i = j
                            continue
                        # Determine status from body
                        low = body.lstrip().lower()
                        if low.startswith("silent") or low.startswith("s —") or low.startswith("s -"):
                            status = "silent"
                        elif low.startswith("gap") or low.startswith("g —") or low.startswith("g -"):
                            status = "gap"
                        else:
                            status = "finding"

                        # Update ONLY if the row is still a stub
                        rc = cur.execute(
                            "UPDATE cluster_finding "
                            "   SET finding_text=?, finding_status=?, "
                            "       source_file=?, last_updated_date=? "
                            " WHERE obs_id=? AND cluster_code=? "
                            "   AND cluster_subgroup_id=? AND version=? "
                            "   AND source_file=? "
                            "   AND COALESCE(delete_flagged,0)=0",
                            (body, status, src_basename, ts,
                             obs_id, CLUSTER_CODE, sg_id, PATCH_VERSION,
                             STUB_SOURCE),
                        ).rowcount
                        if rc:
                            n_updated += 1
                            if len(seen_examples) < 10:
                                seen_examples.append(
                                    f"{src_basename}:{i+1} {cur_q}/M05-{letter} "
                                    f"label_inside_bold={label_inside_bold!r}"
                                )
                    i = j
                    continue
                i += 1

        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    print(f"Loose-marker updates applied (stub-only): {n_updated}")
    print(f"Loose-marker scans (informational):       {n_seen}")
    print()
    print("Examples updated:")
    for e in seen_examples:
        print(f"  {e}")

    # Verification — show T0.1.1 row state
    print()
    print("=== T0.1.1 rows after corrective pass ===")
    obs_id = obs_by_q.get("T0.1.1")
    for r in cur.execute(
        "SELECT cs.subgroup_code, cf.finding_status, cf.source_file, "
        "       SUBSTR(cf.finding_text, 1, 80) AS preview "
        "  FROM cluster_finding cf "
        "  LEFT JOIN cluster_subgroup cs ON cs.id=cf.cluster_subgroup_id "
        " WHERE cf.cluster_code=? AND cf.obs_id=? "
        "   AND COALESCE(cf.delete_flagged,0)=0 "
        " ORDER BY COALESCE(cs.subgroup_code, 'ZZZ')",
        (CLUSTER_CODE, obs_id),
    ):
        sg = r["subgroup_code"] or "CLUSTER-LEVEL"
        print(f"  {sg:14s} {r['finding_status']:20s} src={r['source_file']}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
