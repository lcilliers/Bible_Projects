"""_exploratory_no_primary_registries_v1_20260503.py — read-only.

Drills into the 33 registries flagged 'no Primary' (archetype 'distributed',
'mixed-no-primary', or 'thin') by the term primacy tiering. For each, lists
OWNER terms with their tier and the structural signals, then the XREF terms
with gloss + OWNER home. Lets the researcher see whether these registries are
genuinely diffuse semantic fields or are leaning on other registries' OWNER
terms for analytical content.

Reads the tiering JSON sidecar produced by
`_exploratory_term_primacy_tiering_v1_20260503.py`.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
TIER_JSON = os.path.join("outputs", "markdown", "term-primacy-tiering-20260503.json")
OUT_MD = os.path.join("outputs", "markdown",
                      "no-primary-registries-detail-20260503.md")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    with open(TIER_JSON, encoding="utf-8") as f:
        payload = json.load(f)
    terms = payload["terms"]

    # Group OWNER terms by registry
    by_reg: dict = defaultdict(list)
    for t in terms:
        by_reg[(t["reg_no"], t["reg_word"])].append(t)

    # Find no-Primary registries
    no_primary = []
    for (reg_no, word), bucket in by_reg.items():
        a = sum(1 for t in bucket if t["tier"] == "A")
        if a == 0:
            no_primary.append((reg_no, word, bucket))
    no_primary.sort()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    L: list[str] = []
    L.append("# No-Primary Registries — OWNER + XREF Detail")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  source: "
             "`scripts/_exploratory_no_primary_registries_v1_20260503.py`")
    L.append("")
    L.append(f"**{len(no_primary)} registries** have no Tier-A (Primary) OWNER term per the "
             "tiering rule in [term-primacy-tiering-20260503.md](term-primacy-tiering-20260503.md). "
             "For each, both the OWNER inventory and the XREF inventory are shown so it can be "
             "seen whether analytical weight is genuinely distributed or has migrated to "
             "other registries' OWNER terms via XREF.")
    L.append("")
    L.append("Tier legend: **A** Primary · **B** Secondary · **C** Marginal · **U** Unanalysed.")
    L.append("")

    # Index — quick contents
    L.append("## Index")
    L.append("")
    L.append("| Reg | Word | OWNER B/C/U | XREF count | XREF distinct registries |")
    L.append("|---:|---|---|---:|---:|")
    reg_xref_counts = {}
    for reg_no, word, bucket in no_primary:
        b = sum(1 for t in bucket if t["tier"] == "B")
        c = sum(1 for t in bucket if t["tier"] == "C")
        u = sum(1 for t in bucket if t["tier"] == "U")
        # XREF counts
        xrows = conn.execute("""
            SELECT COUNT(*) AS n,
                   COUNT(DISTINCT (
                     SELECT wr2.no FROM wa_term_inventory ti2
                       JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
                       JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
                      WHERE ti2.strongs_number = ti.strongs_number
                        AND ti2.term_owner_type='OWNER'
                        AND ti2.delete_flagged=0
                      LIMIT 1)) AS distinct_owner_regs
              FROM wa_term_inventory ti
              JOIN wa_file_index fi ON fi.id = ti.file_id
              JOIN word_registry wr ON wr.id = fi.word_registry_fk
             WHERE wr.no = ? AND ti.term_owner_type='XREF'
               AND ti.delete_flagged=0
        """, (reg_no,)).fetchone()
        reg_xref_counts[reg_no] = (xrows[0] or 0, xrows[1] or 0)
        L.append(f"| {reg_no} | {word} | {b}/{c}/{u} | "
                 f"{xrows[0] or 0} | {xrows[1] or 0} |")
    L.append("")

    # Per-registry detail
    L.append("---")
    L.append("")
    for reg_no, word, bucket in no_primary:
        L.append(f"## R{reg_no:03d} — {word}")
        L.append("")

        # OWNER terms (B/C/U sub-grouped)
        owners_sorted = sorted(bucket, key=lambda t: (t["tier"], -t["anchors"],
                                                     -t["vc_rel"]))
        L.append(f"### OWNER terms ({len(bucket)})")
        L.append("")
        L.append("| Tier | strongs | translit | gloss | lang | status | anchors | groups | vc_rel |")
        L.append("|---|---|---|---|---|---|---:|---:|---:|")
        for t in owners_sorted:
            L.append(f"| {t['tier']} | `{t['strongs_number']}` | "
                     f"{t['transliteration'] or ''} | "
                     f"{(t['gloss'] or '')[:35]} | {t['language'][:1]} | "
                     f"`{t['status']}` | {t['anchors']} | {t['groups_active']} | "
                     f"{t['vc_rel']} |")
        L.append("")

        # XREF terms with gloss + OWNER home
        xref_rows = conn.execute("""
            SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
                   mt.status,
                   (SELECT wr2.no || ':' || wr2.word
                      FROM wa_term_inventory ti2
                      JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
                      JOIN word_registry wr2 ON wr2.id = fi2.word_registry_fk
                     WHERE ti2.strongs_number = mt.strongs_number
                       AND ti2.term_owner_type='OWNER'
                       AND ti2.delete_flagged=0
                     LIMIT 1) AS owner_home,
                   (SELECT COUNT(*) FROM wa_verse_records vr
                      JOIN wa_term_inventory ti3 ON ti3.id = vr.term_inv_id
                     WHERE ti3.strongs_number = mt.strongs_number
                       AND ti3.term_owner_type='OWNER'
                       AND ti3.delete_flagged=0
                       AND vr.delete_flagged=0) AS owner_verse_count
              FROM mti_terms mt
              JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                       AND ti.term_owner_type='XREF'
                                       AND ti.delete_flagged=0
              JOIN wa_file_index fi ON fi.id = ti.file_id
              JOIN word_registry wr ON wr.id = fi.word_registry_fk
             WHERE wr.no = ?
               AND mt.delete_flagged=0
               AND mt.status NOT IN ('delete','excluded')
             ORDER BY mt.language DESC, mt.strongs_number
        """, (reg_no,)).fetchall()

        L.append(f"### XREF terms ({len(xref_rows)})")
        L.append("")
        if not xref_rows:
            L.append("_None._")
        else:
            L.append("| strongs | translit | gloss | lang | status | OWNER home | OWNER verses |")
            L.append("|---|---|---|---|---|---|---:|")
            for x in xref_rows:
                L.append(f"| `{x['strongs_number']}` | "
                         f"{x['transliteration'] or ''} | "
                         f"{(x['gloss'] or '')[:35]} | {x['language'][:1]} | "
                         f"`{x['status']}` | {x['owner_home'] or '?'} | "
                         f"{x['owner_verse_count']} |")
        L.append("")
        L.append("---")
        L.append("")

    conn.close()

    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Wrote: {OUT_MD}")
    print(f"No-Primary registries: {len(no_primary)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
