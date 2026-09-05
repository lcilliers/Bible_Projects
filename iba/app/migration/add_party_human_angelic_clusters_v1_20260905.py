"""add_party_human_angelic_clusters_v1_20260905.py — ONE-OFF. Part of the cfg_lexical_code_class ->
cluster de-cfg-ification (escalation #1500, researcher approved 2026-09-05: "yes continue, and
there may be more that may be identified as the analytics progress"). Re-does the withdrawn
party_human/party_angelic seeding (escalations #1479-1489, withdrawn -- content already
researched+evidence-checked, escalation #1448's own resolution) as cluster_strong reallocations
instead, matching T4/T5/T6/T7's own precedent (add_adversarial_cluster_v1_20260905.py,
add_negator_connective_partydivine_clusters_v1_20260905.py).

Two new clusters:
  - T8 (Party-Human, 8 codes): adam/ish/ishah/enosh/anthropos/aner/gyne/anthropinos.
  - T9 (Party-Angelic, 3 codes): mal'ak (2 forms)/angelos.

Mechanics, in iba.db, one transaction, direct writes (writer='migration'): reallocate (UPDATE in
place) codes currently at T2 (H0120G/H0376G/G0435G); insert fresh where no live cluster_strong row
exists (the majority -- these words were mostly missed by the original 2026-08-11 mechanical
sweep).

Idempotent: checks each code's current cluster_code before acting.

    python -m iba.app.migration.add_party_human_angelic_clusters_v1_20260905
"""

from __future__ import annotations

import sqlite3
import sys

from ..lib.cfg import DB_PATH

_CLUSTERS = [
    ("T8", "Party-Human", "T8 - Party-Human: a strong referring to a human party (man/woman/"
     "mankind/human) -- referent-identity classification, orthogonal to the thematic M-code axis; "
     "directly supports observation-catalogue party-kind questions. A code can carry both an "
     "M-cluster assignment and this one."),
    ("T9", "Party-Angelic", "T9 - Party-Angelic: a strong referring to an angelic party (messenger/"
     "angel) -- referent-identity classification, orthogonal to the thematic M-code axis; "
     "distinguished from T4/Adversarial per the observation catalogue's own T4.6.1/T4.6.2 split "
     "(angelic vs adversarial genuinely need telling apart). A code can carry both an M-cluster "
     "assignment and this one."),
]

# (strong, target_cluster_code, note) -- reallocate if currently T2, insert fresh if no row exists.
_ITEMS = [
    ("H0120G", "T8", "adam, gloss 'man'/mankind -- evidence-checked live against strong.stepGloss"),
    ("H0376G", "T8", "ish, gloss 'man' -- evidence-checked live"),
    ("H0802", "T8", "ishah, gloss 'woman' -- evidence-checked live (no prior cluster_strong row)"),
    ("H0582", "T8", "enosh, gloss 'human' -- evidence-checked live (no prior cluster_strong row)"),
    ("G0444", "T8", "anthropos, gloss 'a human' -- evidence-checked live (no prior row)"),
    ("G0435G", "T8", "aner, gloss 'man: husband' -- evidence-checked live"),
    ("G1135", "T8", "gyne, gloss 'woman' -- evidence-checked live (no prior cluster_strong row)"),
    ("G0442", "T8", "anthropinos, gloss 'human' -- evidence-checked live (no prior row)"),
    ("H4397G", "T9", "mal'akh, gloss 'messenger' (base H4397's own G-suffix sub-entry) -- "
     "evidence-checked live (no prior cluster_strong row)"),
    ("H4397H", "T9", "mal'akh, gloss 'messenger: angel' (base H4397's own H-suffix sub-entry) -- "
     "evidence-checked live (no prior cluster_strong row)"),
    ("H4398", "T9", "mal'akh (Aramaic), gloss 'angel' -- evidence-checked live (no prior row)"),
    ("G0032G", "T9", "angelos, gloss 'angel' -- evidence-checked live (no prior cluster_strong row)"),
    ("G0032H", "T9", "angelos, gloss 'angel: messenger' -- evidence-checked live (no prior row)"),
]


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    report: list[str] = []
    try:
        for code, short_name, description in _CLUSTERS:
            exists = conn.execute(
                "SELECT 1 FROM cluster WHERE cluster_code=?", (code,)).fetchone()
            if not exists:
                conn.execute(
                    "INSERT INTO cluster (cluster_code, short_name, description, gloss, deleted) "
                    "VALUES (?, ?, ?, '', 0)", (code, short_name, description))
                report.append(f"cluster {code} '{short_name}' created")
            else:
                report.append(f"cluster {code} already exists -- no-op")

        for strong, target, note in _ITEMS:
            row = conn.execute(
                "SELECT id, cluster_code, rationale FROM cluster_strong "
                "WHERE strong=? AND deleted=0", (strong,)).fetchone()
            if row is None:
                conn.execute(
                    "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, "
                    "deleted, rationale) VALUES (?, ?, 'migration-20260905-decfgification', "
                    "datetime('now'), 0, ?)",
                    (strong, target, f"new assignment 2026-09-05 (no prior cluster_strong row) "
                                      f"-- {note}"))
                report.append(f"{strong}: inserted fresh at {target}")
                continue
            if row["cluster_code"] == target:
                report.append(f"{strong}: already {target} -- no-op")
                continue
            if row["cluster_code"] != "T2":
                report.append(f"{strong}: currently {row['cluster_code']} (not T2) -- left "
                               f"untouched, not part of this reallocation")
                continue
            new_rationale = (row["rationale"] or "") + (
                f" | relocated T2->{target} 2026-09-05 (de-cfg-ification, researcher-approved, "
                f"escalation #1500). {note}")
            conn.execute(
                "UPDATE cluster_strong SET cluster_code=?, rationale=? WHERE id=?",
                (target, new_rationale, row["id"]))
            report.append(f"{strong}: reallocated T2 -> {target} (id={row['id']})")

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print("add_party_human_angelic_clusters_v1_20260905:")
    for line in report:
        print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
