"""assign_1807_unmapped_strongs_v1_20260921.py — ONE-OFF migration, escalation #1807/#1817.

Researcher instruction, verbatim, escalation #1817: "allocate the three clear items to T12,T3 and
the remaining to T2." The 9 strongs are the whole live Leg 3 gap (`lexical.readiness`): occurring
strongs with zero `cluster_strong` allocation at all, none of them fitting any inner-being cluster
(escalation #1807's own investigation) but 3 of them fitting an existing T-code once actually
checked against every T-code definition and live precedent (escalation #1807 -> #1817, not
re-derived here):

- G2375 "long shield" (Eph 6.16) -> T12 (Objects-Artifacts) -- T12 already has G3696 "weapon" as a
  live member; a shield is the same referent class.
- H6446 "long-sleeved" (Joseph's robe, Gen 37.3/23/32) -> T12 (Objects-Artifacts) -- T12 already has
  8+ garment/coat members (H0899B/H8008/H4055/H4403/H2436H/H3831/H4063/H7897/G1903).
- G4537 "to sound a trumpet" (Matt 6.2, Rev 8/9/11) -> T3 (Operations) -- an unambiguous action verb,
  matching T3's own live mix of action-verb members.

The other 6 (G2279, G2863, G3118, G5353, H1998, H8088A) genuinely fit no existing T-code after
individual evaluation against every T-code definition (T3-T15) -- researcher-confirmed T2
(Supplementary, no impact on the study), same shape as `assign_leg3_orphan_strongs_v1_20260915.py`'s
own T2 fallback for the same reason (grammatical/incidental, no inner-being relevance).

Idempotent (checks for an existing live row before inserting, same convention as
`assign_leg3_orphan_strongs_v1_20260915.py`/`apply_1598_cluster_batch.py`) -- re-running this script
is a no-op on every row it already applied.

    python -m iba.app.migration.assign_1807_unmapped_strongs_v1_20260921
"""

from __future__ import annotations

import sqlite3

from ..lib.cfg import DB_PATH

_SOURCE = "claude-scan-20260921"

_ASSIGNMENTS = {
    "G2375": ("T12", "'long shield' (Eph 6.16, the shield of faith) -- T12 already has G3696 "
                     "'weapon' as a live member; a shield is the same referent class (Objects/"
                     "Artifacts). Escalation #1807/#1817."),
    "H6446": ("T12", "'long-sleeved' (Joseph's robe, Gen 37.3/23/32) -- T12 already has 8+ garment/"
                     "coat members (H0899B/H8008/H4055/H4403/H2436H/H3831/H4063/H7897 'garment', "
                     "G1903 'coat'); a robe is the same referent class. Escalation #1807/#1817."),
    "G4537": ("T3", "'to sound a trumpet' (Matt 6.2, Rev 8.13/9/11) -- an unambiguous action verb, "
                    "matching T3's own live mix of action-verb members (to hear/to search/to take "
                    "an oath). Escalation #1807/#1817."),
    "G2279": ("T2", "'sound/echo' (Acts 2.2 wind-sound, Heb 12.19 trumpet-sound, Luke 4.37 'report/"
                    "news') -- an acoustic-phenomenon/report noun; checked against every T-code "
                    "definition (T3-T15), no fit. Not a place/object/party/operation/body-part/"
                    "calendar-term. Escalation #1807/#1817, researcher-confirmed T2."),
    "G2863": ("T2", "'be long-haired' (1Cor 11.14-15) -- a verb describing a state of hair length, "
                    "not a body-part NOUN with figurative significance (T14 is specifically nouns "
                    "like hand=power, face=presence; different grammatical category). Checked "
                    "against every T-code, no fit. Escalation #1807/#1817, researcher-confirmed T2."),
    "G3118": ("T2", "'long-lived' (Eph 6.3, 'that you may live long') -- a lifespan/duration "
                    "adjective; checked against every T-code, no fit. Escalation #1807/#1817, "
                    "researcher-confirmed T2."),
    "G5353": ("T2", "'sound/note' (Rom 10.18, 1Cor 14.7) -- same acoustic-phenomenon pattern as "
                    "G2279; checked against every T-code, no fit. Escalation #1807/#1817, "
                    "researcher-confirmed T2."),
    "H1998": ("T2", "'sound' (Isa 14.11, the sound of harps) -- same acoustic-phenomenon pattern; "
                    "checked against every T-code, no fit. Escalation #1807/#1817, "
                    "researcher-confirmed T2."),
    "H8088A": ("T2", "'sound' (Ps 150.5, cymbals sounding) -- same acoustic-phenomenon pattern; "
                     "checked against every T-code, no fit. Escalation #1807/#1817, "
                     "researcher-confirmed T2."),
}


def build_payload(conn: sqlite3.Connection) -> list[dict]:
    """Fail loudly if any listed code has disappeared (soft-deleted) since this script was
    written, rather than silently skipping it -- same discipline as the #1606 precedent script."""
    gone = [code for code in _ASSIGNMENTS
            if not conn.execute("SELECT 1 FROM strong WHERE strongNumber=? AND deleted=0",
                                (code,)).fetchone()]
    if gone:
        raise RuntimeError(
            f"{len(gone)} code(s) in this script's payload no longer exist as a live strong row: "
            f"{sorted(gone)} -- re-check before running, do not silently skip.")
    return [{"strong": code, "cluster_code": cluster_code, "rationale": rationale}
            for code, (cluster_code, rationale) in _ASSIGNMENTS.items()]


def apply_cluster_strong(conn: sqlite3.Connection) -> list[str]:
    report = []
    for item in build_payload(conn):
        exists = conn.execute(
            "SELECT 1 FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
            (item["strong"], item["cluster_code"])).fetchone()
        if exists:
            report.append(f"{item['strong']} -> {item['cluster_code']}: already live -- no-op")
            continue
        conn.execute(
            "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
            "confidence, operation, review_flag, rationale) "
            "VALUES (?, ?, ?, datetime('now'), 0, 'medium', 0, 0, ?)",
            (item["strong"], item["cluster_code"], _SOURCE, item["rationale"]))
        report.append(f"{item['strong']}: inserted into {item['cluster_code']}")
    return report


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        report = apply_cluster_strong(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print("\n".join(report))
    print(f"\n{len(report)} action(s) applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
