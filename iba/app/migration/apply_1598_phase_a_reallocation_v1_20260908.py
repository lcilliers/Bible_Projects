"""apply_1598_phase_a_reallocation_v1_20260908.py — ONE-OFF. Escalation #1598 (M/T-code cluster
reallocation), Phase A: create the `Places`/`Corporate-Collective`/`Objects-Artifacts` T-code groups
(T10/T11/T12), expand `T4` (Adversarial), and apply the researcher's own direct dispositions on the
two Phase 1 objects (`H3477H`/`H8549J` parked in `T3`) — all sourced from a reviewable JSON payload
rather than hardcoded, per the researcher's own instruction this session ("write each relocation to
a json file, and then a bash command that can perform the relocation that I can run after reviewing
the jsons").

Every insert/relocation below was scanned live against `strong`/`verse_lexical` and reasoned about
individually (gloss + a sample of real verse occurrences) before being added to the payload — not a
blind keyword-crossmatch sweep (`feedback_iba_backfill_cluster_assignment_via_analysis_not_bulk_
automation`). Two flagged Phase-1 candidates (`H6001A`, `G2960`) are deliberately NOT in this
payload — their disposition needs one more round of the researcher's own confirmation (dual-tag
shape for `H6001A`; whether adding `G2960` should formally widen `T7`'s own "is a name" definition)
before they're written anywhere.

What this does, in `iba.db`, all in one transaction, direct writes (`cluster`/`cluster_strong` are
`category='data'` tables with `writer='migration'` grants — not `configmaint.propose` territory,
same governance basis `add_adversarial_cluster_v1_20260905.py`/`add_party_human_angelic_clusters_
v1_20260905.py` already established for this exact table pair):

  1. INSERT each new `cluster` row named in the payload's `new_clusters` list (skipped if it already
     exists — idempotent).
  2. INSERT each new `cluster_strong` row named in `inserts` (skipped if a live row for that exact
     `(strong, cluster_code)` pair already exists).
  3. For each entry in `relocations`, UPDATE the existing live `cluster_strong` row's `cluster_code`
     in place (same "relocated" pattern as `add_adversarial_cluster_v1_20260905.py`), appending to
     `rationale` rather than overwriting it. Skipped (reported, not silently ignored) if no live row
     matches the stated `from_cluster_code`, or if the row is already at `to_cluster_code`.

Idempotent: safe to re-run — every step checks live state before acting.

    python -m iba.app.migration.apply_1598_phase_a_reallocation_v1_20260908
"""

from __future__ import annotations

import json
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
_PAYLOAD_PATH = _REPO_ROOT / "iba" / "docs" / "1598-phase-a-cluster-reallocation-v1-20260908.json"


def main() -> int:
    payload = json.loads(_PAYLOAD_PATH.read_text(encoding="utf-8"))
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        # 1. New clusters
        for c in payload["new_clusters"]:
            exists = conn.execute(
                "SELECT 1 FROM cluster WHERE cluster_code=?", (c["cluster_code"],)).fetchone()
            if exists:
                report.append(f"cluster {c['cluster_code']} already exists -- no-op")
                continue
            conn.execute(
                "INSERT INTO cluster (cluster_code, short_name, description, gloss, deleted) "
                "VALUES (?, ?, ?, '', 0)",
                (c["cluster_code"], c["short_name"], c["description"]))
            report.append(f"cluster {c['cluster_code']} '{c['short_name']}' created")

        # 2. New cluster_strong inserts
        for item in payload["inserts"]:
            exists = conn.execute(
                "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                (item["strong"], item["cluster_code"])).fetchone()
            if exists:
                report.append(f"{item['strong']} -> {item['cluster_code']}: already live -- no-op")
                continue
            review_flag = 1 if item["confidence"] == "low" else 0
            conn.execute(
                "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
                "confidence, operation, review_flag, rationale) "
                "VALUES (?, ?, 'claude-scan-20260908', datetime('now'), 0, ?, 0, ?, ?)",
                (item["strong"], item["cluster_code"], item["confidence"], review_flag,
                 item["rationale"]))
            report.append(f"{item['strong']}: inserted into {item['cluster_code']} "
                          f"(confidence={item['confidence']})")

        # 3. Relocations
        for r in payload["relocations"]:
            row = conn.execute(
                "SELECT id, cluster_code, rationale FROM cluster_strong "
                "WHERE strong=? AND cluster_code=? AND deleted=0",
                (r["strong"], r["from_cluster_code"])).fetchone()
            if row is None:
                already = conn.execute(
                    "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                    (r["strong"], r["to_cluster_code"])).fetchone()
                if already:
                    report.append(f"{r['strong']}: already at {r['to_cluster_code']} -- no-op")
                else:
                    report.append(f"{r['strong']}: NO live row at {r['from_cluster_code']} found -- "
                                  f"skipped, needs its own insert, not a relocation (flagging, not "
                                  f"guessing)")
                continue
            new_rationale = (row["rationale"] or "") + (
                f" | relocated {r['from_cluster_code']}->{r['to_cluster_code']} 2026-09-08 "
                f"(escalation #1598, researcher-approved). {r['note']}")
            conn.execute(
                "UPDATE cluster_strong SET cluster_code=?, rationale=? WHERE id=?",
                (r["to_cluster_code"], new_rationale, row["id"]))
            report.append(f"{r['strong']}: reallocated {r['from_cluster_code']} -> "
                          f"{r['to_cluster_code']} (id={row['id']})")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("apply_1598_phase_a_reallocation_v1_20260908:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
