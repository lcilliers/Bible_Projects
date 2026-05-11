"""_apply_m26a_split_v1_20260510.py — DB-modifying.

Apply the M26-A split per researcher decisions DEC-3..DEC-6 of
m39-subgroup-multi-term-design-v1-20260510.

This script does NO analysis. It mechanically routes the 589 active
M26-A verse_context rows according to the subject classifier output,
adds m:n term linkages for the new sub-groups, and renames M26-A.

Operations (single transaction, foreign_keys=OFF for safety around
'both'-verse vc INSERTs):

  1. Bump sort_order of all M26 sub-groups EXCEPT M26-A by +1
     (creates room for M26-A1 at sort_order=1)

  2. UPDATE existing M26-A row:
       - subgroup_code  → 'M26-A2'
       - label          → 'Human Righteousness — State of being right'
       - core_description prepended with split note (DEC-5)
       - sort_order     → 2

  3. INSERT new M26-A1 row (DEC-6):
       - subgroup_code  = 'M26-A1'
       - label          = 'God Righteousness'
       - sort_order     = 1
       - status         = 'Analysis - In Progress' (split context)

  4. Add mti_term_subgroup links (DEC-3, DEC-4):
       For each of the 6 M26-A terms (G1342, G1343, H6662, H6664G,
       H6664H, H6666), INSERT links to:
         - M26-A1   (the new God sub-group)
         - M26-BOUNDARY  (so 'neither' verses can route there)
       (The link to M26-A2 already exists from M46 backfill — it
       was on M26-A and survived the rename.)

  5. Route the 589 active M26-A vc rows by subject (DEC-3, DEC-4):
       - 'God'     (157) → UPDATE vc.cluster_subgroup_id = M26-A1
       - 'man'     (341) → no change (still points at the renamed M26-A2)
       - 'both'    ( 11) → UPDATE existing row to M26-A1, plus INSERT
                            sibling vc row pointing at M26-A2 (DEC-3)
       - 'neither' ( 80) → UPDATE vc.cluster_subgroup_id = M26-BOUNDARY
       - 'unclassified' → leave alone, surface in verification

Pre-flight aborts if M26-A1 already exists, if the JSONL is missing,
or if any classified (vr_id, mti_term_id) pair doesn't resolve to an
active M26-A vc row.

NO API calls. ~2 sec wall time. No cost.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")
BACKUP_DIR = "backups"
DEFAULT_SUBJECTS_JSONL = os.path.join(
    "outputs", "markdown",
    "m26-subject-claude-sonnet-4-6-M26-A-20260509.jsonl",
)
SCHEMA_VERSION_AFTER = None  # No schema change; only data routing

EXPECTED_M26A_TERMS = {
    "G1342", "G1343", "H6662", "H6664G", "H6664H", "H6666",
}

M26_A1_LABEL = "God Righteousness"
M26_A1_DESC = (
    "[Split off from M26-A on 2026-05-10 per researcher decision. "
    "Verses where the term names God's own righteousness — divine "
    "character, judgments, acts, standards. Distinguished from M26-A2 "
    "(Human Righteousness), which holds verses about persons in right "
    "standing or living rightly. Composer should refresh this "
    "description with full inner-being framing on next analytical pass.]"
)
M26_A2_LABEL = "Human Righteousness — State of being right"
M26_A2_DESC_PREFIX = (
    "[Split on 2026-05-10: God-righteousness verses moved to M26-A1. "
    "This sub-group now scoped to human righteousness only. Composer "
    "should narrow this description on next analytical pass.] "
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def take_backup(label: str) -> str:
    os.makedirs(BACKUP_DIR, exist_ok=True)
    path = os.path.join(BACKUP_DIR,
                        f"bible_research_pre_{label}_{today_compact()}.db")
    shutil.copy2(DB_PATH, path)
    return path


def load_subjects(path: str) -> list[dict]:
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def preflight(conn, subjects: list[dict]) -> tuple[bool, list[str], dict]:
    """Returns (ok, msgs, ctx). ctx carries ids the migration will use."""
    msgs = []
    ok = True
    ctx: dict = {}

    # 1. M26-A exists, M26-A1 does not, M26-BOUNDARY exists
    sg_rows = {
        r[1]: dict(zip(("id", "code", "label", "sort_order"), r))
        for r in conn.execute(
            "SELECT id, subgroup_code, label, sort_order "
            "  FROM cluster_subgroup "
            " WHERE cluster_code='M26' AND COALESCE(delete_flagged,0)=0"
        )
    }

    if "M26-A" not in sg_rows:
        msgs.append("[ERR] M26-A sub-group not found.")
        ok = False
    else:
        msgs.append(f"[ok] M26-A exists (id={sg_rows['M26-A']['id']}, "
                    f"sort_order={sg_rows['M26-A']['sort_order']}).")
        ctx["m26_a_id"] = sg_rows["M26-A"]["id"]
        ctx["m26_a_sort_order"] = sg_rows["M26-A"]["sort_order"]

    if "M26-A1" in sg_rows:
        msgs.append("[ERR] M26-A1 already exists — apply already ran. "
                    "Aborting.")
        ok = False
    else:
        msgs.append("[ok] M26-A1 does not yet exist.")

    if "M26-BOUNDARY" not in sg_rows:
        msgs.append("[ERR] M26-BOUNDARY sub-group not found — required "
                    "for 'neither' routing (DEC-4).")
        ok = False
    else:
        msgs.append(
            f"[ok] M26-BOUNDARY exists (id={sg_rows['M26-BOUNDARY']['id']})."
        )
        ctx["m26_boundary_id"] = sg_rows["M26-BOUNDARY"]["id"]

    if not ok:
        return ok, msgs, ctx

    # 2. The 6 M26-A terms are still mapped to M26-A in mti_term_subgroup
    mt_rows = {
        r["strongs_number"]: r["id"]
        for r in conn.execute(
            "SELECT mt.id, mt.strongs_number "
            "  FROM mti_terms mt "
            "  JOIN mti_term_subgroup mts ON mts.mti_term_id=mt.id "
            " WHERE mt.cluster_code='M26' "
            "   AND mts.cluster_subgroup_id=? "
            "   AND COALESCE(mt.delete_flagged,0)=0 "
            "   AND COALESCE(mts.delete_flagged,0)=0",
            (ctx["m26_a_id"],),
        )
    }
    found = set(mt_rows.keys())
    if found != EXPECTED_M26A_TERMS:
        missing = EXPECTED_M26A_TERMS - found
        extra = found - EXPECTED_M26A_TERMS
        if missing:
            msgs.append(f"[ERR] M26-A is missing expected terms: "
                        f"{sorted(missing)}")
        if extra:
            msgs.append(f"[ERR] M26-A has unexpected extra terms: "
                        f"{sorted(extra)}")
        ok = False
    else:
        msgs.append(f"[ok] all 6 expected M26-A terms present: "
                    f"{sorted(found)}")
        ctx["m26_a_term_ids"] = mt_rows  # {strong: mti_id}

    # 3. Subject classifier file: count and key resolution
    msgs.append(f"[info] subjects loaded: {len(subjects)}")
    subj_counter = Counter(s["subject"] for s in subjects)
    for k in ("God", "man", "both", "neither"):
        msgs.append(f"  {k:8s} {subj_counter.get(k, 0)}")
    other = sum(v for k, v in subj_counter.items()
                if k not in ("God", "man", "both", "neither"))
    if other:
        msgs.append(f"  other    {other} (will be reported in verification)")
    ctx["subj_counter"] = dict(subj_counter)

    # 4. Each (vr_id, mti_term_id) in subjects must map to an active
    #    M26-A vc row
    if "m26_a_id" in ctx:
        m26a_id = ctx["m26_a_id"]
        active_keys = {
            (r["verse_record_id"], r["mti_term_id"]): r["id"]
            for r in conn.execute(
                "SELECT id, verse_record_id, mti_term_id "
                "  FROM verse_context "
                " WHERE cluster_subgroup_id=? "
                "   AND COALESCE(delete_flagged,0)=0",
                (m26a_id,),
            )
        }
        msgs.append(f"[info] active M26-A vc rows in DB: {len(active_keys)}")
        ctx["m26_a_vc_keys"] = active_keys

        # All subjects must resolve
        unmatched = []
        for s in subjects:
            key = (s["vr_id"], s["mti_term_id"])
            if key not in active_keys:
                unmatched.append(key)
        if unmatched:
            msgs.append(f"[ERR] {len(unmatched)} subject records do not "
                        f"map to an active M26-A vc row. First 5: "
                        f"{unmatched[:5]}")
            ok = False
        else:
            msgs.append(f"[ok] all {len(subjects)} subject keys map to "
                        f"active M26-A vc rows")

        # Conversely: the subjects file should cover every active M26-A vc
        # row (otherwise some verses won't be routed correctly)
        subject_keys = {(s["vr_id"], s["mti_term_id"]) for s in subjects}
        uncovered = [
            k for k in active_keys.keys() if k not in subject_keys
        ]
        if uncovered:
            msgs.append(f"[WARN] {len(uncovered)} active M26-A vc rows have "
                        f"no subject classification. They will stay routed "
                        f"to M26-A2 (the renamed M26-A) by default.")
        else:
            msgs.append("[ok] every active M26-A vc row has a subject "
                        "classification")

    return ok, msgs, ctx


def run_apply(conn, ctx: dict, subjects: list[dict]) -> dict:
    cur = conn.cursor()
    counts: dict = {}
    ts = now_iso()

    m26a_id = ctx["m26_a_id"]
    m26b_id = ctx["m26_boundary_id"]
    term_ids = ctx["m26_a_term_ids"]   # {strong: mti_id}
    vc_keys = ctx["m26_a_vc_keys"]     # {(vr_id, mti_term_id): vc_id}

    # ── 1. Bump sort_order of all M26 sub-groups EXCEPT M26-A by +1 ──
    cur.execute(
        "UPDATE cluster_subgroup "
        "   SET sort_order = sort_order + 1, "
        "       last_updated_date=? "
        " WHERE cluster_code='M26' "
        "   AND id != ? "
        "   AND COALESCE(delete_flagged,0)=0",
        (ts, m26a_id),
    )
    counts["sort_order_bumped"] = cur.rowcount
    print(f"  [1/5] sort_order bumped on {cur.rowcount} other M26 "
          f"sub-groups")

    # ── 2. Rename M26-A → M26-A2 ─────────────────────────────────────
    # Build the new core_description by prepending the split note
    cs_row = conn.execute(
        "SELECT core_description FROM cluster_subgroup WHERE id=?",
        (m26a_id,),
    ).fetchone()
    new_desc = M26_A2_DESC_PREFIX + (cs_row["core_description"] or "")
    cur.execute(
        "UPDATE cluster_subgroup "
        "   SET subgroup_code=?, label=?, core_description=?, "
        "       sort_order=2, last_updated_date=? "
        " WHERE id=?",
        ("M26-A2", M26_A2_LABEL, new_desc, ts, m26a_id),
    )
    counts["m26_a_renamed"] = cur.rowcount
    print(f"  [2/5] M26-A renamed to M26-A2 (label='{M26_A2_LABEL[:40]}...')")

    # ── 3. INSERT M26-A1 ─────────────────────────────────────────────
    cur.execute(
        "INSERT INTO cluster_subgroup "
        "  (cluster_code, subgroup_code, label, core_description, "
        "   sort_order, status, version, source, "
        "   delete_flagged, created_at, last_updated_date) "
        "VALUES (?, ?, ?, ?, 1, 'Analysis - In Progress', 'v1', "
        "        'M26-A split per DEC-3..DEC-6 (m39 design)', "
        "        0, ?, ?)",
        ("M26", "M26-A1", M26_A1_LABEL, M26_A1_DESC, ts, ts),
    )
    m26a1_id = cur.lastrowid
    counts["m26_a1_inserted"] = 1
    counts["m26_a1_id"] = m26a1_id
    print(f"  [3/5] M26-A1 inserted (id={m26a1_id})")

    # ── 4. Add mti_term_subgroup links (term × {M26-A1, M26-BOUNDARY}) ─
    inserted_links = 0
    for strong, mti_id in term_ids.items():
        # Term × M26-A1
        cur.execute(
            "INSERT INTO mti_term_subgroup "
            "  (mti_term_id, cluster_subgroup_id, placement_note, "
            "   delete_flagged, created_at, last_updated_date) "
            "VALUES (?, ?, ?, 0, ?, ?)",
            (mti_id, m26a1_id,
             "M26-A split (DEC-3): God-righteousness verses route here",
             ts, ts),
        )
        inserted_links += 1
        # Term × M26-BOUNDARY (DEC-4): 'neither' verses route here
        # Idempotent: only INSERT if not already present (some terms
        # may already have a BOUNDARY link from earlier work).
        existing = conn.execute(
            "SELECT 1 FROM mti_term_subgroup "
            " WHERE mti_term_id=? AND cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (mti_id, m26b_id),
        ).fetchone()
        if not existing:
            cur.execute(
                "INSERT INTO mti_term_subgroup "
                "  (mti_term_id, cluster_subgroup_id, placement_note, "
                "   delete_flagged, created_at, last_updated_date) "
                "VALUES (?, ?, ?, 0, ?, ?)",
                (mti_id, m26b_id,
                 "M26-A split (DEC-4): 'neither'-subject verses route here",
                 ts, ts),
            )
            inserted_links += 1
    counts["mti_term_subgroup_links_inserted"] = inserted_links
    print(f"  [4/5] mti_term_subgroup: {inserted_links} new links "
          f"(6 terms × M26-A1 + selective × M26-BOUNDARY)")

    # ── 5. Route 589 vc rows by subject ─────────────────────────────
    bucket = Counter()
    n_god = n_man = n_both = n_neither = n_other = 0
    n_both_inserts = 0

    # Collect existing vc row attributes once for sibling INSERTs (needed for
    # 'both' rows). We must preserve everything else about the vc row.
    vc_id_list = list(vc_keys.values())
    ph = ",".join("?" * len(vc_id_list))
    vc_attr = {
        r["id"]: dict(r) for r in conn.execute(
            f"SELECT id, verse_record_id, mti_term_id, group_id, "
            f"       cluster_subgroup_id, is_anchor, is_relevant, "
            f"       is_related, notes, delete_flagged, "
            f"       vertical_pass_flag, set_aside_reason, analysis_note "
            f"  FROM verse_context "
            f" WHERE id IN ({ph})", vc_id_list,
        )
    }

    for s in subjects:
        key = (s["vr_id"], s["mti_term_id"])
        vc_id = vc_keys[key]
        subj = s["subject"]
        bucket[subj] += 1
        if subj == "God":
            cur.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? WHERE id=?",
                (m26a1_id, vc_id),
            )
            n_god += 1
        elif subj == "man":
            # No change — already routed to renamed M26-A2 (was M26-A)
            n_man += 1
        elif subj == "both":
            # Route the existing row to M26-A1; INSERT a sibling pointing
            # to M26-A2 (the renamed M26-A row, id=m26a_id).
            cur.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? WHERE id=?",
                (m26a1_id, vc_id),
            )
            attr = vc_attr[vc_id]
            cur.execute(
                "INSERT INTO verse_context "
                "  (verse_record_id, mti_term_id, group_id, "
                "   cluster_subgroup_id, is_anchor, is_relevant, "
                "   is_related, notes, delete_flagged, "
                "   vertical_pass_flag, set_aside_reason, analysis_note) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    attr["verse_record_id"], attr["mti_term_id"],
                    attr["group_id"], m26a_id,  # NEW row at M26-A2
                    attr["is_anchor"], attr["is_relevant"],
                    attr["is_related"], attr["notes"],
                    attr["delete_flagged"], attr["vertical_pass_flag"],
                    attr["set_aside_reason"], attr["analysis_note"],
                ),
            )
            n_both += 1
            n_both_inserts += 1
        elif subj == "neither":
            cur.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? WHERE id=?",
                (m26b_id, vc_id),
            )
            n_neither += 1
        else:
            n_other += 1

    counts["vc_to_m26_a1"] = n_god
    counts["vc_kept_at_m26_a2"] = n_man
    counts["vc_both_pairs"] = n_both
    counts["vc_both_sibling_inserts"] = n_both_inserts
    counts["vc_to_m26_boundary"] = n_neither
    counts["vc_other_subjects_skipped"] = n_other

    print(f"  [5/5] vc rows routed:")
    print(f"        God     → M26-A1:       {n_god}")
    print(f"        man     → M26-A2 (kept): {n_man}")
    print(f"        both    → M26-A1 + insert sibling at M26-A2: "
          f"{n_both} ({n_both_inserts} new vc rows)")
    print(f"        neither → M26-BOUNDARY: {n_neither}")
    if n_other:
        print(f"        other   → skipped:       {n_other}")

    return counts


def verify(conn, ctx: dict) -> dict:
    invariants = {}
    m26a_id = ctx["m26_a_id"]   # post-rename = M26-A2
    m26b_id = ctx["m26_boundary_id"]
    m26a1_id = conn.execute(
        "SELECT id FROM cluster_subgroup "
        " WHERE cluster_code='M26' AND subgroup_code='M26-A1'"
    ).fetchone()
    m26a1_id = m26a1_id[0] if m26a1_id else None

    # I-1: vc count per relevant sub-group
    for sg_id, label in [
        (m26a1_id, "M26-A1"),
        (m26a_id, "M26-A2 (renamed M26-A)"),
        (m26b_id, "M26-BOUNDARY"),
    ]:
        if sg_id is None:
            continue
        n = conn.execute(
            "SELECT COUNT(*) FROM verse_context "
            " WHERE cluster_subgroup_id=? "
            "   AND COALESCE(delete_flagged,0)=0",
            (sg_id,),
        ).fetchone()[0]
        invariants[f"active vc rows → {label}"] = n

    # I-2: every active M26 vc row has cluster_subgroup_id (except FLAGGED)
    n_unrouted = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE mt.cluster_code='M26' "
        "   AND vc.cluster_subgroup_id IS NULL "
        "   AND COALESCE(vc.delete_flagged,0)=0"
    ).fetchone()[0]
    invariants["active M26 vc rows still unrouted"] = n_unrouted

    # I-3: distinct mti_term_subgroup count per term
    rows = conn.execute(
        "SELECT mt.strongs_number, COUNT(DISTINCT mts.cluster_subgroup_id) "
        "  FROM mti_terms mt "
        "  JOIN mti_term_subgroup mts ON mts.mti_term_id=mt.id "
        " WHERE mt.cluster_code='M26' "
        "   AND mt.strongs_number IN "
        "       ('G1342','G1343','H6662','H6664G','H6664H','H6666') "
        "   AND COALESCE(mts.delete_flagged,0)=0 "
        " GROUP BY mt.strongs_number ORDER BY mt.strongs_number"
    ).fetchall()
    invariants["mti_term_subgroup mappings per M26-A term"] = {
        r[0]: r[1] for r in rows
    }

    # I-4: total active vc rows in M26 (was 955; expect 955 + n_both_inserts)
    n_m26 = conn.execute(
        "SELECT COUNT(*) FROM verse_context vc "
        "  JOIN mti_terms mt ON mt.id=vc.mti_term_id "
        " WHERE mt.cluster_code='M26' "
        "   AND COALESCE(vc.delete_flagged,0)=0"
    ).fetchone()[0]
    invariants["total active M26 vc rows"] = n_m26

    return invariants


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--subjects", default=DEFAULT_SUBJECTS_JSONL)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    if not args.dry_run and not args.live:
        print("ERROR: must pass --dry-run or --live", file=sys.stderr)
        return 2
    if args.dry_run and args.live:
        print("ERROR: --dry-run and --live are mutually exclusive",
              file=sys.stderr)
        return 2

    if not Path(args.subjects).exists():
        print(f"ERROR: subjects JSONL not found: {args.subjects}",
              file=sys.stderr)
        return 2

    print("=" * 72)
    print("M26-A SPLIT (DEC-3..DEC-6)")
    print(f"  Mode:     {'DRY-RUN (rollback)' if args.dry_run else 'LIVE (commit)'}")
    print(f"  DB:       {DB_PATH}")
    print(f"  Subjects: {args.subjects}")
    print("=" * 72)
    print()

    subjects = load_subjects(args.subjects)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = OFF")

    print("PRE-FLIGHT")
    print("-" * 72)
    ok, msgs, ctx = preflight(conn, subjects)
    for m in msgs:
        print(m)
    print()
    if not ok:
        print("Pre-flight failed — exiting without changes.")
        conn.execute("PRAGMA foreign_keys = ON")
        return 1

    if args.live:
        print("Taking pre-apply backup...")
        b = take_backup("m26a_split")
        print(f"  Backup saved: {b}")
        print()

    print("EXECUTE")
    print("-" * 72)
    try:
        conn.execute("BEGIN")
        counts = run_apply(conn, ctx, subjects)
        print()
        print("FOREIGN-KEY CHECK")
        print("-" * 72)
        fk_violations = list(conn.execute("PRAGMA foreign_key_check"))
        if fk_violations:
            print(f"  [ERR] {len(fk_violations)} FK violation(s):")
            for v in fk_violations[:20]:
                print(f"    {dict(zip(['table','rowid','parent','fkid'], v))}")
            raise RuntimeError(
                f"foreign_key_check failed: {len(fk_violations)}"
            )
        print("  [ok] zero violations")
        print()
        print("VERIFICATION")
        print("-" * 72)
        invariants = verify(conn, ctx)
        for k, v in invariants.items():
            print(f"  {k}: {v}")
        print()
        if args.dry_run:
            conn.execute("ROLLBACK")
            print("DRY-RUN: changes rolled back.")
        else:
            conn.execute("COMMIT")
            print("LIVE: COMMIT successful.")
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"\n[err] rolled back: {type(e).__name__}: {e}")
        conn.execute("PRAGMA foreign_keys = ON")
        raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")

    print()
    print("Operations:")
    for k, v in counts.items():
        print(f"  {k:40s} {v}")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
