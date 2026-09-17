"""Fix confirmed keyword/homonym-collision mistags in `cluster_strong` (escalation #1714,
2026-09-17). Corpus-wide sweep (English-gloss homonym search, cross-checked against
`stepTransliteration` and, where available, lexicon data) found two clusters where strongs were
tagged in because their English `stepGloss` happens to share a word with the cluster's theme, in a
completely different sense:

`M18` (Desire & Longing) -- "long" (desire) vs "long" (length): `G2375` "long shield", `G2863` "be
long-haired", `G3118` "long-lived", `H6446` "long-sleeved" are all the physical-length sense, no
relation to desire/longing.

`M62` (Truth & Sincerity) -- "sound" (sincere/wholesome, correctly `G0573` haplous "single/sincere")
vs "sound" (audible noise): `G2279` (ēchos, "echo/noise"), `G5353` (fthongos, "musical tone"),
`G4537` (salpizō, "to sound a trumpet"), `H1998` (hemyah, "roar/noise"), `H8088A` (shema,
"report/something heard") are all the audible-noise sense, no relation to sincerity of character.
`G0573` (haplous) is genuinely correct and NOT touched.

Soft-deleted (`deleted=1`), not hard-removed, per the project's standing soft-delete discipline --
the mis-tag stays visible/auditable, not silently erased.

Safe to re-run: idempotent (checks current `deleted` state first).

Usage:
    python iba/app/migration/fix_cluster_keyword_collisions_v1_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

REMOVALS = [
    ("M18", "G2375", "long shield -- physical-length sense, not desire/longing"),
    ("M18", "G2863", "be long-haired -- physical-length sense, not desire/longing"),
    ("M18", "G3118", "long-lived -- physical-length sense, not desire/longing"),
    ("M18", "H6446", "long-sleeved -- physical-length sense, not desire/longing"),
    ("M62", "G2279", "sound (echos, echo/noise) -- audible sense, not sincerity"),
    ("M62", "G5353", "sound (fthongos, musical tone) -- audible sense, not sincerity"),
    ("M62", "G4537", "to sound a trumpet (salpizo) -- audible sense, not sincerity"),
    ("M62", "H1998", "sound (hemyah, roar/noise) -- audible sense, not sincerity"),
    ("M62", "H8088A", "sound (shema, report/something heard) -- audible sense, not sincerity"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    report: list[str] = []
    try:
        cur.execute("BEGIN")

        for cluster_code, strong, reason in REMOVALS:
            row = cur.execute(
                "SELECT id, deleted, rationale FROM cluster_strong WHERE cluster_code=? AND strong=?",
                (cluster_code, strong)).fetchone()
            if row is None:
                report.append(f"{cluster_code}/{strong}: NOT FOUND -- skipped")
                continue
            if row["deleted"]:
                report.append(f"{cluster_code}/{strong}: already deleted -- skipped")
                continue
            new_rationale = ((row["rationale"] or "") +
                            f" -- SOFT-DELETED 2026-09-17, escalation #1714: keyword-collision "
                            f"mistag, {reason}").strip()
            cur.execute(
                "UPDATE cluster_strong SET deleted=1, rationale=? WHERE id=?",
                (new_rationale, row["id"]))
            report.append(f"{cluster_code}/{strong}: soft-deleted ({reason})")

        if args.dry_run:
            conn.rollback()
            report.append("DRY-RUN: rolled back")
        else:
            conn.commit()
            report.append("COMMITTED")

        print("\n".join(report))
        return 0
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
