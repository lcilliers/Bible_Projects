"""_exploratory_empty_registry_inspection_v1_20260503.py — read-only.

Surfaces the 8 zero-OWNER registries NOT auto-merged in the obvious-merges
patch, with full cluster context, conceptual proximity hints, and the
researcher's call.
"""
from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_MD = os.path.join("outputs", "markdown", "empty-registry-inspection-20260503.md")

# These 8 are surfaced for inspection (not auto-merged)
INSPECT = [
    27,   # consciousness
    48,   # diligence
    104,  # loyalty
    109,  # meekness
    129,  # recognition
    138,  # reverence
    144,  # sensuality
    205,  # resentment
]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    L = []
    L.append("# Empty Registry Inspection — Non-Obvious Merge Candidates")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  source: "
             "`scripts/_exploratory_empty_registry_inspection_v1_20260503.py`")
    L.append("")
    L.append("8 zero-OWNER registries that were NOT auto-merged in the "
             "`_repair_empty_registry_merges_v1_20260503.py` patch — these need researcher "
             "judgement on whether to merge, build out, or keep as semantic-shell.")
    L.append("")
    L.append("Three were auto-merged on 2026-05-03: R137 resolve→R173 will, "
             "R200 energy→R187 strength, R214 suffering→R051 distress.")
    L.append("")

    for reg_no in INSPECT:
        r = conn.execute(
            "SELECT no, word, cluster_assignment, description FROM word_registry WHERE no = ?",
            (reg_no,)
        ).fetchone()
        cluster = r["cluster_assignment"]
        desc = r["description"] or ""

        L.append(f"## R{reg_no:03d} — {r['word']}")
        L.append("")
        L.append(f"**Cluster:** {cluster or '(none)'}")
        L.append("")
        if desc:
            L.append(f"**Description:**")
            L.append("")
            for line in desc.split("\n"):
                L.append(f"> {line}" if line else ">")
            L.append("")

        siblings = []
        if cluster:
            siblings = conn.execute("""
                SELECT no, word, phase1_status,
                       (SELECT COUNT(*) FROM mti_terms mt
                          JOIN wa_term_inventory ti ON ti.strongs_number=mt.strongs_number
                                                    AND ti.term_owner_type='OWNER'
                                                    AND ti.delete_flagged=0
                          JOIN wa_file_index fi ON fi.id=ti.file_id
                         WHERE fi.word_registry_fk = wr.id
                           AND mt.delete_flagged=0
                           AND mt.status IN ('extracted','extracted_thin',
                                             'extracted_theological_anchor')) AS terms,
                       (SELECT COUNT(*) FROM verse_context vc
                          JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
                          JOIN wa_term_inventory ti ON ti.id=vr.term_inv_id
                          JOIN wa_file_index fi ON fi.id=ti.file_id
                         WHERE fi.word_registry_fk = wr.id
                           AND ti.term_owner_type='OWNER' AND ti.delete_flagged=0
                           AND vr.delete_flagged=0
                           AND vc.delete_flagged=0 AND vc.is_anchor=1) AS anchors,
                       SUBSTR(description, 1, 100) AS desc
                  FROM word_registry wr
                 WHERE cluster_assignment = ? AND no != ?
                    AND phase1_status != 'Excluded'
                 ORDER BY anchors DESC
            """, (cluster, reg_no)).fetchall()

        if siblings:
            L.append(f"### Cluster {cluster} siblings")
            L.append("")
            L.append("| Reg | Word | Terms | Anchors | Description (excerpt) |")
            L.append("|---:|---|---:|---:|---|")
            for s in siblings:
                L.append(f"| {s['no']} | {s['word']} | {s['terms']} | {s['anchors']} | "
                         f"{(s['desc'] or '')[:80]} |")
            L.append("")

        # Decision-options framework
        L.append(f"### Options for R{reg_no:03d}")
        L.append("")
        L.append("- **Build out:** treat as a genuine standalone concept; commission term extraction.")
        L.append("- **Merge into a sibling:** if a cluster sibling carries the same analytical territory.")
        L.append("- **Keep as shell:** if the concept is structurally important but currently subsumed by neighbours.")
        L.append("")
        L.append("---")
        L.append("")

    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Wrote: {OUT_MD}")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
