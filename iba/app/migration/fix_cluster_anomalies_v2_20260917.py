"""Resolve the 4 items escalated in #1714 (cluster anomaly audit) on the researcher's instruction:
"you surfaced obvious errors, and only if you really need my judgement, then ask, else fix." On
investigation, none of the 4 actually needed a judgement call -- each had a real, checkable answer.

1. `M59` (Release & Reconciliation) had zero reconciliation vocabulary. Checked: real reconciliation
   vocabulary EXISTS in the corpus (katallasso family, 6 strongs) but was tagged to `M05` (its old
   scope was "Love, Compassion, Kindness" before today's reconciliation work re-scoped it to
   "Kindness & Friendship") -- moved to `M59` where it actually belongs. `G0786` "irreconcilable"
   stays at `M06` (Malice & Enmity) -- its sense is persistent hostility, not reconciliation-
   achieved, a better fit there.

2. `M60` (Confession & Forgiveness) had zero confession vocabulary. Checked: the 2 confession
   strongs that exist (G3670/G3671) were tagged only to role-clusters (`T2`/`T3`), never to any
   M-cluster -- added as `M60` tags (keeping their existing role tags, a different axis, per the
   already-established M-code+T-code coexistence pattern).

3. `M67` (Sloth & Diligence) had only 2 live strongs. Checked: 7 more genuine idleness/diligence
   strongs exist, all currently sitting untagged at the M-cluster level, only in the giant `T2`
   "Supplementary" catch-all -- added as `M67` tags.

4. `M47`'s `cluster.gloss` field listed `nous`/`G3563` as a member, not present in live
   `cluster_strong`. Checked: NOT a staleness bug -- `nous` was deliberately, evidence-basedly
   moved to `M15` (Knowing & Understanding) on 2026-09-06 (escalation #1525), per the researcher's
   own explicit rule that a strong may only live in one M-cluster. The bug is that `cluster.gloss`
   (a cached summary text field) was never regenerated after that move. Fixed by regenerating
   `cluster.gloss` from live `cluster_strong` membership for every cluster where the two disagree
   (not just `M47` -- swept all 45 populated-gloss clusters for the same drift).

`M12`/`M13`'s "duplication" checked separately and found NOT to be a data bug: 0 strongs are
tagged to both (confirmed in the first #1714 sweep) -- the overlap is between two legitimately
adjacent clusters' own vocabulary (integrity vs. faithfulness), not a mistake. Nothing to fix.

Safe to re-run: idempotent (checks current `deleted`/membership state first).

Usage:
    python iba/app/migration/fix_cluster_anomalies_v2_20260917.py [--db PATH] [--dry-run]
"""
import argparse
import sqlite3
import sys

DEFAULT_DB = r"C:\Bible_study_projects\iba\app\db\iba.db"

# (strong, from_cluster, to_cluster, reason)
MOVES = [
    ("G1259", "M05", "M59", "be reconciled -- belongs at Release & Reconciliation, not Kindness & Friendship"),
    ("G2643", "M05", "M59", "reconciliation -- belongs at Release & Reconciliation, not Kindness & Friendship"),
    ("G2132", "M05", "M59", "to reconcile -- belongs at Release & Reconciliation, not Kindness & Friendship"),
    ("G2644", "M05", "M59", "to reconcile -- belongs at Release & Reconciliation, not Kindness & Friendship"),
    ("G0604", "M05", "M59", "to reconcile -- belongs at Release & Reconciliation, not Kindness & Friendship"),
]

# (strong, cluster, note) -- new M-cluster tag, existing role-cluster tags (if any) untouched
ADDITIONS = [
    ("G3670", "M60", "to confess/profess -- was only role-tagged (T3), never M-cluster-tagged"),
    ("G3671", "M60", "confession -- was only role-tagged (T2), never M-cluster-tagged"),
    ("H0149", "M67", "diligently -- was only role-tagged (T2), never M-cluster-tagged"),
    ("G0691", "M67", "be idle -- was only role-tagged (T2), never M-cluster-tagged"),
    ("G0812", "M67", "be idle -- was only role-tagged (T2), never M-cluster-tagged"),
    ("G0692", "M67", "idle -- was only role-tagged (T2), never M-cluster-tagged"),
    ("H8220", "M67", "idleness -- was only role-tagged (T2), never M-cluster-tagged"),
    ("G4709", "M67", "diligently -- was only role-tagged (T2), never M-cluster-tagged"),
    ("H0629", "M67", "diligently -- was only role-tagged (T2), never M-cluster-tagged"),
]


def regenerate_gloss(cur, cluster_code) -> str:
    # Match the corpus's own established format ("english-gloss (transliteration)", confirmed
    # against M01's untouched, non-stale field) -- not "transliteration (code)", which would
    # silently discard the English gloss every other cluster's field already carries.
    rows = cur.execute(
        """SELECT s.stepGloss, s.stepTransliteration FROM cluster_strong cs
           JOIN strong s ON s.strongNumber=cs.strong
           WHERE cs.cluster_code=? AND cs.deleted=0 ORDER BY s.stepGloss""",
        (cluster_code,)).fetchall()
    return ", ".join(f"{r[0]} ({r[1]})" for r in rows)


def live_code_set(cur, cluster_code) -> set[str]:
    return {r[0] for r in cur.execute(
        "SELECT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0", (cluster_code,))}


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

        for strong, from_c, to_c, reason in MOVES:
            row = cur.execute(
                "SELECT id, rationale FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                (strong, from_c)).fetchone()
            if row is None:
                report.append(f"MOVE {strong} {from_c}->{to_c}: source row not found/already moved -- skipped")
                continue
            existing_at_target = cur.execute(
                "SELECT id FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                (strong, to_c)).fetchone()
            if existing_at_target:
                report.append(f"MOVE {strong} {from_c}->{to_c}: already present at target -- skipped")
                continue
            new_rationale = ((row["rationale"] or "") +
                            f" -- MOVED 2026-09-17, escalation #1714: {reason}").strip()
            cur.execute(
                "UPDATE cluster_strong SET cluster_code=?, rationale=? WHERE id=?",
                (to_c, new_rationale, row["id"]))
            report.append(f"MOVE {strong}: {from_c} -> {to_c} ({reason})")

        for strong, cluster, note in ADDITIONS:
            existing = cur.execute(
                "SELECT id FROM cluster_strong WHERE strong=? AND cluster_code=? AND deleted=0",
                (strong, cluster)).fetchone()
            if existing:
                report.append(f"ADD {strong} {cluster}: already present -- skipped")
                continue
            cur.execute(
                "INSERT INTO cluster_strong (strong, cluster_code, source, created_at, deleted, "
                "confidence, rationale) VALUES (?,?,?,datetime('now'),0,?,?)",
                (strong, cluster, "escalation-1714-anomaly-fix-20260917", "high",
                 f"ADDED 2026-09-17, escalation #1714: {note}"))
            report.append(f"ADD {strong} -> {cluster} ({note})")

        # Regenerate cluster.gloss ONLY where the SET of strong codes it mentions genuinely
        # differs from live cluster_strong membership (a real gap) -- not wherever the cosmetic
        # format differs, which would silently discard good existing content (M01's field uses
        # "gloss (translit)" already and is NOT stale; comparing by code set, not exact string,
        # avoids flagging it).
        import re
        fixed_gloss = 0
        # .fetchall() first -- reusing `cur` for the nested per-cluster queries below while still
        # iterating its own outer result set silently truncates the iteration in sqlite3.
        gloss_rows = cur.execute(
            "SELECT cluster_code, gloss FROM cluster WHERE cluster_code LIKE 'M%' AND deleted=0 "
            "AND gloss IS NOT NULL AND gloss != ''").fetchall()
        for row in gloss_rows:
            code, current_gloss = row["cluster_code"], row["gloss"]
            mentioned = set(re.findall(r"\b[HG]\d{3,4}[A-Z]?\b", current_gloss))
            live = live_code_set(cur, code)
            if mentioned and mentioned != live:
                regenerated = regenerate_gloss(cur, code)
                cur.execute("UPDATE cluster SET gloss=? WHERE cluster_code=?", (regenerated, code))
                fixed_gloss += 1
                report.append(f"REGENERATE gloss for {code}: mentioned {len(mentioned)} codes, "
                             f"live has {len(live)} -- {len(mentioned - live)} stale, "
                             f"{len(live - mentioned)} missing from old summary")
        report.append(f"cluster.gloss regenerated for {fixed_gloss} cluster(s) found genuinely stale")

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
