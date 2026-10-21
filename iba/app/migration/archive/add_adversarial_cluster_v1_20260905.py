"""add_adversarial_cluster_v1_20260905.py — ONE-OFF. Architecture correction, escalation TBD
(2026-09-05, researcher's own verdict): Strong's-code classification by referent/function
("negator", "connective", "party of a given kind") is a CLUSTERING decision, not cfg territory --
`cluster`/`cluster_strong` already has the mechanism (evidence-backed strong->code assignment,
`confidence`/`rationale`/`review_flag`, multi-row-per-code precedent from the 2026-08-13 M10->M10b
refinement) and does not go through `configmaint.propose` (writer='migration'/'cluster.assign',
never 'configmaint.propose'). The parallel `cfg_lexical_code_class` table (escalation #1383,
2026-09-04) duplicated this job under the wrong governance regime -- being unwound across several
tracked escalations (see BUILD.md for the full list). This script does the FIRST piece the
researcher explicitly named as ready to proceed now: a new cluster for the adversarial party
(Satan/the Devil), reallocated OUT of the rough T2 "Supplementary" catch-all it currently sits in
-- "the big T2 and T3 buckets are still quite rough... this adversarial grouping is the first [new
bucket] to emerge" (researcher, verbatim).

What this does, in iba.db, all in one transaction, direct writes (cluster/cluster_strong are
`category='data'` tables with `writer='migration'` grants -- not `configmaint.propose` territory,
per the researcher's own verdict this script implements):

  1. INSERT a new `cluster` row: cluster_code='T4', short_name='Adversarial', matching the T2/T3
     shape (no worked-example `gloss` list -- like T3, this is evidence-curated, not a target of
     `clusterassign.py`'s mechanical P1/P2 gloss-precedent sweep).
  2. REASSIGN (UPDATE in place, not a new row) the 3 evidence-checked adversarial codes from their
     current T2 membership to T4 -- same "relocated" pattern as the 2026-08-13 M10->M10b
     refinement, `rationale` appended not overwritten:
       H7854  satan    (Satan)   -- currently T2
       G4567  satanas  (Satan)   -- currently T2
       G1228G diabolos (Devil)   -- currently T2 (G1228H "slanderous", the adjective sense, stays
                                     at its existing M14/Deceit assignment -- untouched, different
                                     sense, different reason)

Idempotent: checks for an existing T4 row / already-reallocated codes before acting.

    python -m iba.app.migration.add_adversarial_cluster_v1_20260905
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_REASSIGN = [
    ("H7854", "satan, gloss 'Satan' -- evidence-checked live against strong.stepGloss"),
    ("G4567", "satanas, gloss 'Satan' -- evidence-checked live against strong.stepGloss"),
    ("G1228G", "diabolos, gloss 'Devil' -- evidence-checked live against strong.stepGloss "
               "(G1228H 'slanderous', the adjective sense, is untouched -- stays at its existing "
               "M14/Deceit assignment, a different sense for a different reason)"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        exists = conn.execute(
            "SELECT 1 FROM cluster WHERE cluster_code='T4'").fetchone()
        if not exists:
            conn.execute(
                "INSERT INTO cluster (cluster_code, short_name, description, gloss, deleted) "
                "VALUES ('T4', 'Adversarial', "
                "'T4 - Adversarial: a strong referring to the adversarial spiritual party "
                "(Satan/the Devil) -- referent-identity classification, orthogonal to the "
                "thematic M-code axis; a code can carry both an M-cluster assignment and this "
                "one. First of the emerging finer-grained buckets refining T2/T3, per researcher "
                "instruction 2026-09-05.', '', 0)")
            report.append("cluster T4 'Adversarial' created")
        else:
            report.append("cluster T4 already exists -- no-op")

        for strong, note in _REASSIGN:
            row = conn.execute(
                "SELECT id, cluster_code, rationale FROM cluster_strong "
                "WHERE strong=? AND deleted=0", (strong,)).fetchone()
            if row is None:
                report.append(f"{strong}: NO live cluster_strong row found -- skipped, needs its "
                               f"own insert, not a reassignment (flagging, not guessing)")
                continue
            if row["cluster_code"] == "T4":
                report.append(f"{strong}: already T4 -- no-op")
                continue
            old_code = row["cluster_code"]
            new_rationale = (row["rationale"] or "") + (
                f" | relocated {old_code}->T4 2026-09-05 (adversarial-party cluster refinement, "
                f"researcher-approved verbatim this session: 'this is not cfg territory... "
                f"continue with setting a new cluster code'). {note}")
            conn.execute(
                "UPDATE cluster_strong SET cluster_code='T4', rationale=? WHERE id=?",
                (new_rationale, row["id"]))
            report.append(f"{strong}: reallocated {old_code} -> T4 (id={row['id']})")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("add_adversarial_cluster_v1_20260905:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
