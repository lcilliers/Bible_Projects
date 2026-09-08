"""apply_1598_cluster_batch.py — reusable, parameter-driven runner for escalation #1598's ongoing
"small cleared batches" workflow (researcher, verbatim: "lets keep going in small cleared batches,
so if 1 is ready, then go for it."). Every batch this escalation produces (Phase A2 onward) is a
reviewable JSON payload under `iba/docs/`; this script is the one tool that applies any of them,
rather than a new one-off script per batch.

Same governance basis as `apply_1598_phase_a_reallocation_v1_20260908.py` (that script's own first
run, still the historical record for Phase A) and the original `add_adversarial_cluster_v1_
20260905.py`/`add_party_human_angelic_clusters_v1_20260905.py` precedent: `cluster`/`cluster_strong`
are `category='data'` tables with `writer='migration'` grants, not `configmaint.propose` territory.

Payload shape (JSON): {"new_clusters": [...], "inserts": [...], "relocations": [...]} — any of the
three keys may be empty or omitted. See `1598-phase-a-cluster-reallocation-v1-20260908.json` and
`1598-phase-a2-cluster-reallocation-v1-20260908.json` for worked examples.

  - `new_clusters`: {cluster_code, short_name, description} — INSERT if the cluster_code doesn't
    already exist, no-op otherwise.
  - `inserts`: {strong, cluster_code, confidence, rationale} — INSERT a new `cluster_strong` row if
    no live row for that exact (strong, cluster_code) pair exists yet; `confidence='low'` sets
    `review_flag=1` automatically. No-op if it already exists.
  - `relocations`: {strong, from_cluster_code, to_cluster_code, note} — UPDATE the live row's
    `cluster_code` in place (rationale appended, not overwritten) — same "relocated" pattern used
    throughout this escalation. Reports (does not fail) if no live row matches `from_cluster_code`,
    or if it's already at `to_cluster_code`.
  - `removals`: {strong, cluster_code, note} — soft-delete (`deleted=1`) the live row for that exact
    (strong, cluster_code) pair, e.g. to correct an `inserts` batch that should have been a
    `relocations` batch (added a new tag but left a stale one behind, escalation #1598 Phase C1's
    own correction). No-op if no live row matches.

Idempotent: every step checks live state before acting, so re-running the same payload is a no-op.

    python -m iba.app.migration.apply_1598_cluster_batch --payload iba/docs/1598-phase-a2-cluster-reallocation-v1-20260908.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sqlite3
import sys

from ..lib.cfg import DB_PATH

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]


def apply_payload(conn: sqlite3.Connection, payload: dict) -> list[str]:
    report: list[str] = []

    for c in payload.get("new_clusters", []):
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

    for item in payload.get("inserts", []):
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

    for r in payload.get("relocations", []):
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

    for rm in payload.get("removals", []):
        row = conn.execute(
            "SELECT id FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            (rm["strong"], rm["cluster_code"])).fetchone()
        if row is None:
            report.append(f"{rm['strong']} -> {rm['cluster_code']}: no live row found -- no-op")
            continue
        conn.execute("UPDATE cluster_strong SET deleted=1 WHERE id=?", (row["id"],))
        report.append(f"{rm['strong']}: removed from {rm['cluster_code']} (id={row['id']}) -- "
                      f"{rm.get('note', '')}")

    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", required=True,
                        help="Path to a reviewable JSON payload (repo-root-relative or absolute)")
    args = parser.parse_args()

    payload_path = pathlib.Path(args.payload)
    if not payload_path.is_absolute():
        payload_path = _REPO_ROOT / payload_path
    payload = json.loads(payload_path.read_text(encoding="utf-8"))

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_payload(conn, payload)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print(f"apply_1598_cluster_batch ({payload_path.name}):")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
