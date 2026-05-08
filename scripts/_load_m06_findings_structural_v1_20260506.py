"""_load_m06_findings_structural_v1_20260506.py — DB-modifying.

Structural loader for the M06 consolidated findings.

For every (catalogue prompt × M06 sub-group) AND every (catalogue prompt ×
cluster-level), creates a row in cluster_finding. Initial finding_text is
a stub pointer to the source transcript file (one of parts 1–4 by tier).
Status defaults to 'finding'; a small override list flags known silent
and gap cells per the consolidated findings document.

Coverage:
  189 catalogue prompts (T0..T7) × 7 sub-groups (A..G)
  + 189 prompts × cluster-level synthesis row
  = 1512 rows total

Sub-sequent step: full-text population per (prompt × scope) from the
consolidated findings prose.

Idempotent: ON CONFLICT DO UPDATE on the UNIQUE key
(obs_id, cluster_code, cluster_subgroup_id, version).
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"

CLUSTER_CODE = "M06"
VERSION = "v1"
SOURCE_FILE_PREFIX = "WA-M06-consolidated-findings-v1-20260506"

# Map tier → source-file part suffix (what's on disk)
TIER_TO_PART = {
    "T0": "part1",
    "T1": "part1",
    "T2": "part2-T2",
    "T3": "part3-T3-T4",
    "T4": "part3-T3-T4",
    "T5": "part4-T5-T7",
    "T6": "part4-T5-T7",
    "T7": "part4-T5-T7",
}

# Status overrides — (question_code, scope) → status.
# scope is sub-group letter A..G or 'CLUSTER'.
# Derived from the consolidated findings 'S' (silent) and 'G' (gap) markers.
# CLUSTER-level silents and gaps are the most consistent overrides.
STATUS_OVERRIDES = {
    # T2.1 spirit-level silence — entire cluster, all sub-groups
    ("T2.1.1", "CLUSTER"): "silent",
    ("T2.1.2", "CLUSTER"): "silent",
    ("T2.1.3", "CLUSTER"): "silent",
    ("T2.1.4", "CLUSTER"): "silent",
    # T2.1 — also silent for each sub-group A..G
    **{(f"T2.1.{i}", letter): "silent"
       for i in (1, 2, 3, 4) for letter in "ABCDEFG"},
    # T3.5 creativity — silent for all sub-groups except A (and even there
    # the engagement is distorted, not enabling)
    ("T3.5.1", "B"): "silent", ("T3.5.1", "C"): "silent",
    ("T3.5.1", "D"): "silent", ("T3.5.1", "E"): "silent",
    ("T3.5.1", "F"): "silent", ("T3.5.1", "G"): "silent",
    # T4.6 spiritual-beings interface — silent for B, C, D, E, G
    ("T4.6.1", "B"): "silent", ("T4.6.1", "C"): "silent",
    ("T4.6.1", "D"): "silent", ("T4.6.1", "E"): "silent",
    ("T4.6.1", "G"): "silent",
    ("T4.6.3", "CLUSTER"): "silent",
    # T6.4.2 root architecture — gap
    ("T6.4.2", "CLUSTER"): "gap",
    # T6.7 dimensional sharing — gap (needs DB query)
    ("T6.7.1", "CLUSTER"): "gap",
    ("T6.7.2", "CLUSTER"): "gap",
    ("T6.7.3", "CLUSTER"): "gap",
    # T7.1.8 LXX mapping — gap
    ("T7.1.8", "CLUSTER"): "gap",
    # T7.1.9 NT coinage — gap
    ("T7.1.9", "CLUSTER"): "gap",
    # T2.8.3, T5.7.3 — most sub-groups silent on deposit consequence
    ("T2.8.3", "B"): "silent", ("T2.8.3", "C"): "silent",
    ("T2.8.3", "D"): "silent", ("T2.8.3", "F"): "silent",
    ("T2.8.3", "G"): "silent",
    ("T5.7.3", "B"): "silent", ("T5.7.3", "C"): "silent",
    ("T5.7.3", "D"): "silent", ("T5.7.3", "F"): "silent",
    ("T5.7.3", "G"): "silent",
}

# CLUSTER-level synthesis prompts — promote status to cluster_synthesis
# where the consolidated findings have a [CLUSTER] paragraph that ties the
# sub-groups together.
CLUSTER_SYNTHESIS_PROMPTS = {
    "T0.1.1", "T1.4.3", "T1.5.2", "T1.6.3", "T1.7.2", "T2.10.2",
    "T3.1.3", "T3.2.3", "T3.3.3", "T3.4.3", "T3.6.3", "T3.7.3",
    "T3.8.3", "T3.9.3", "T3.10.3", "T3.11.3",
    "T4.5.2", "T4.5.3", "T5.5.2", "T6.1.2", "T6.2.2",
    "T7.3.1", "T7.3.2", "T7.3.3",
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def backup_db():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(
        BACKUP_DIR, f"bible_research_{ts}_pre_m06_findings_load.db"
    )
    shutil.copy2(DB_PATH, dest)
    return dest


def main():
    print(f"DB: {DB_PATH}")
    print("Backing up...", flush=True)
    bak = backup_db()
    print(f"  -> {bak}\n")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Catalogue prompts (T0..T7)
    prompts = [dict(r) for r in conn.execute("""
        SELECT obs_id, question_code, tier, component_code, question_text
          FROM wa_obs_question_catalogue
         WHERE tier IS NOT NULL AND COALESCE(deleted,0) = 0
         ORDER BY tier, component_code, prompt_seq, obs_id
    """).fetchall()]
    print(f"Tier prompts: {len(prompts)}")

    # M06 sub-groups
    subgroups = [dict(r) for r in conn.execute("""
        SELECT id, subgroup_code, label
          FROM cluster_subgroup
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
         ORDER BY sort_order
    """, (CLUSTER_CODE,)).fetchall()]
    sg_letter_to_id = {}
    for sg in subgroups:
        # subgroup_code is like 'M06-A' → letter 'A'; or 'BOUNDARY'
        if sg["subgroup_code"].startswith(f"{CLUSTER_CODE}-"):
            letter = sg["subgroup_code"][len(CLUSTER_CODE) + 1:]
            sg_letter_to_id[letter] = sg["id"]
        else:
            sg_letter_to_id[sg["subgroup_code"]] = sg["id"]
    print(f"Sub-groups: {len(subgroups)}")
    print(f"  Letter mapping: {sg_letter_to_id}")
    print()

    # Sub-group letters used for atomic finding rows (A..G, exclude
    # BOUNDARY — it has no findings in the consolidated doc as it wasn't
    # internally sub-grouped).
    SCOPE_LETTERS = ["A", "B", "C", "D", "E", "F", "G"]

    n_inserted = 0
    n_updated = 0
    counts_by_status = {"finding": 0, "silent": 0, "gap": 0,
                        "cluster_synthesis": 0}

    try:
        conn.execute("BEGIN")

        for p in prompts:
            qcode = p["question_code"]
            tier = p["tier"]
            source_file = (
                f"{SOURCE_FILE_PREFIX}-{TIER_TO_PART.get(tier, 'unknown')}.md"
            )

            # Sub-group rows
            for letter in SCOPE_LETTERS:
                sg_id = sg_letter_to_id.get(letter)
                if not sg_id:
                    continue
                status = STATUS_OVERRIDES.get((qcode, letter), "finding")
                stub = (
                    f"[Pending full-text load — see {source_file} "
                    f"§{tier} for prompt {qcode} sub-group M06-{letter}]"
                    if status == "finding" else
                    f"[Silent — no verse evidence in source for M06-{letter} "
                    f"on prompt {qcode}]"
                    if status == "silent" else
                    f"[Gap — flagged in source for CC database query]"
                )
                row = (
                    p["obs_id"], CLUSTER_CODE, sg_id, status, stub,
                    source_file, VERSION,
                    f"Loaded by structural loader v1 (2026-05-06); "
                    f"full-text population pending",
                    now_iso(), now_iso(),
                )
                _insert_or_replace(conn, row)
                counts_by_status[status] = counts_by_status.get(status, 0) + 1
                n_inserted += 1

            # Cluster-level row (cluster_subgroup_id = NULL)
            cs_status = STATUS_OVERRIDES.get((qcode, "CLUSTER"))
            if not cs_status:
                cs_status = (
                    "cluster_synthesis"
                    if qcode in CLUSTER_SYNTHESIS_PROMPTS
                    else "finding"
                )
            stub = (
                f"[Pending full-text load — see {source_file} "
                f"§{tier} for prompt {qcode} CLUSTER-level]"
                if cs_status == "finding" else
                f"[Cluster synthesis pending full-text load — "
                f"see {source_file} §{tier} for {qcode}]"
                if cs_status == "cluster_synthesis" else
                f"[Silent at cluster level — no verse evidence]"
                if cs_status == "silent" else
                f"[Gap at cluster level — flagged for CC query]"
            )
            row = (
                p["obs_id"], CLUSTER_CODE, None, cs_status, stub,
                source_file, VERSION,
                f"Loaded by structural loader v1 (2026-05-06)",
                now_iso(), now_iso(),
            )
            _insert_or_replace(conn, row)
            counts_by_status[cs_status] = (
                counts_by_status.get(cs_status, 0) + 1
            )
            n_inserted += 1

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"[err] ERROR — rolled back: {e}")
        raise

    print(f"Total rows touched: {n_inserted}")
    print()
    print("By status:")
    for st, n in counts_by_status.items():
        print(f"  {st:20s} {n}")

    # Verification
    print()
    print("Verification — cluster_finding row counts in DB:")
    r = conn.execute("""
        SELECT finding_status, COUNT(*) AS n FROM cluster_finding
         WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0
         GROUP BY finding_status
    """, (CLUSTER_CODE,)).fetchall()
    for x in r:
        print(f"  {x['finding_status']:20s} {x['n']}")
    total = conn.execute(
        "SELECT COUNT(*) AS n FROM cluster_finding "
        " WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0",
        (CLUSTER_CODE,),
    ).fetchone()["n"]
    print(f"  {'TOTAL':20s} {total}")

    conn.close()
    return 0


def _insert_or_replace(conn, row):
    conn.execute("""
        INSERT INTO cluster_finding
          (obs_id, cluster_code, cluster_subgroup_id, finding_status,
           finding_text, source_file, version, notes, delete_flagged,
           created_at, last_updated_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)
        ON CONFLICT (obs_id, cluster_code, cluster_subgroup_id, version)
        DO UPDATE SET
          finding_status=excluded.finding_status,
          finding_text=excluded.finding_text,
          source_file=excluded.source_file,
          notes=excluded.notes,
          last_updated_date=excluded.last_updated_date
    """, row)


if __name__ == "__main__":
    sys.exit(main())
