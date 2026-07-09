"""_apply_m32_dir005_step2b_synthesis_v1_20260508.py — DB-modifying.

Corrective sub-pass for DIR-20260508-004 step 2: split the 5
**[CLUSTER — Finding N: ...]** synthesis findings (all under T7.3.4 in
part4) into 5 distinct cluster_finding rows. The strict UPSERT key
(obs_id, cluster_code, cluster_subgroup_id, version) was collapsing
them into one — this script differentiates them with version values
'v1-finding-1' .. 'v1-finding-5'.

Operations:
  1. Restore the v1 T7.3.4 cluster-level row to a stub state (placeholder
     text, status='finding') so the canonical v1 row reflects 'no
     authored T7.3.4 cluster-level synthesis on the prompt itself' —
     because the source author placed standalone findings here, not a
     single synthesis answer to T7.3.4.
  2. INSERT 5 new rows at obs_id=T7.3.4, cluster_subgroup_id=NULL,
     finding_status='cluster_synthesis', version='v1-finding-1' .. 5,
     each with the verbatim finding text from the parser.
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
SOURCE_FILE = "WA-M32-consolidated-findings-v1-20260508-part4-T5-T7.md"
QCODE = "T7.3.4"

PLACEHOLDER_TEXT = (
    "[Sub-group not separately addressed in source — see cluster-level "
    "finding for this prompt]"
)

PART4 = ("Sessions/Session_Clusters/M32/"
         "WA-M32-consolidated-findings-v1-20260508-part4-T5-T7.md")

QCODE_RE = re.compile(r"^\*\*(T\d+\.\d+\.\d+)\*\*\s*[—-]")
MARKER_RE = re.compile(r"^\*\*\[([^\]]+)\][^*]*\*\*\s*(.*)$")
H3_RE = re.compile(r"^###\s+")
BOUNDARY_RE = re.compile(r"^\*\*BOUNDARY\b")
FINDING_RE = re.compile(r"^CLUSTER\s+—\s+Finding\s+(\d+):")


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def collect_findings():
    """Return [(finding_n, label, body_text)] for the 5 named findings."""
    text = Path(PART4).read_text(encoding="utf-8")
    lines = text.splitlines()
    cur_q = None
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = QCODE_RE.match(line)
        if m:
            cur_q = m.group(1)
            i += 1
            continue
        m = MARKER_RE.match(line)
        if m and cur_q == QCODE:
            scope_str = m.group(1)
            body_first = m.group(2)
            fm = FINDING_RE.match(scope_str)
            if not fm:
                i += 1
                continue
            n = int(fm.group(1))
            label = scope_str
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
            # Prefix the body with the finding label so the row is
            # self-describing (the scope_str is dropped from finding_text
            # otherwise).
            full_body = f"**{label}** {body}"
            out.append((n, label, full_body))
            i = j
            continue
        i += 1
    return out


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    ts = now_iso()

    # Resolve T7.3.4 obs_id
    obs_row = cur.execute(
        "SELECT obs_id FROM wa_obs_question_catalogue "
        " WHERE question_code=? AND catalogue_version='v2-2026-04-29'",
        (QCODE,),
    ).fetchone()
    if obs_row is None:
        print(f"[err] obs_id not found for {QCODE}")
        return 1
    obs_id = obs_row["obs_id"]
    print(f"T7.3.4 obs_id = {obs_id}")

    findings = collect_findings()
    print(f"Findings parsed from source: {len(findings)} (expected 5)")
    if len(findings) != 5:
        for f in findings:
            print(f"  Finding {f[0]}: {f[1][:80]}")
        print("[err] expected exactly 5 [CLUSTER — Finding N:] markers")
        return 1

    try:
        cur.execute("BEGIN")

        # 1. Restore T7.3.4 v1 cluster-level row to stub state
        rc = cur.execute(
            "UPDATE cluster_finding "
            "   SET finding_text=?, finding_status='finding', "
            "       source_file='[stub-loader-step1]', "
            "       last_updated_date=? "
            " WHERE obs_id=? AND cluster_code=? "
            "   AND cluster_subgroup_id IS NULL "
            "   AND version='v1' "
            "   AND COALESCE(delete_flagged,0)=0",
            (PLACEHOLDER_TEXT, ts, obs_id, CLUSTER_CODE),
        ).rowcount
        print(f"v1 T7.3.4 cluster-level row restored to stub: rc={rc}")

        # 2. Insert 5 new rows (one per finding) under distinct versions
        for n, label, body in sorted(findings, key=lambda x: x[0]):
            version = f"v1-finding-{n}"
            cur.execute(
                "INSERT OR REPLACE INTO cluster_finding "
                "  (obs_id, cluster_code, cluster_subgroup_id, "
                "   finding_status, finding_text, source_file, "
                "   version, created_at, last_updated_date, "
                "   delete_flagged) "
                "VALUES (?, ?, NULL, 'cluster_synthesis', ?, ?, ?, ?, ?, 0)",
                (obs_id, CLUSTER_CODE, body, SOURCE_FILE,
                 version, ts, ts),
            )
            print(f"  + INSERT version={version!r} (Finding {n})")

        cur.execute("COMMIT")
    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"[err] rolled back: {e}")
        raise

    # Verification
    print()
    print("=== Verification: M32 cluster_synthesis rows ===")
    for r in cur.execute(
        "SELECT cf.id, cf.version, q.question_code, "
        "       SUBSTR(cf.finding_text, 1, 100) AS preview "
        "  FROM cluster_finding cf "
        "  JOIN wa_obs_question_catalogue q ON q.obs_id=cf.obs_id "
        " WHERE cf.cluster_code=? AND cf.finding_status='cluster_synthesis' "
        "   AND COALESCE(cf.delete_flagged,0)=0 "
        " ORDER BY q.question_code, cf.version",
        (CLUSTER_CODE,),
    ):
        print(f"  cf.id={r['id']:5d} q={r['question_code']:8s} "
              f"version={r['version']!r}")
        print(f"    {r['preview']}")

    print()
    print("=== M32 by status (post-fix) ===")
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
