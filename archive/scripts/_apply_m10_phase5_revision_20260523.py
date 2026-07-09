"""Apply the M10 Phase 5 REVISION — partial Phase 6 redo for M10-A and M10-B only.

Per directive wa-cluster-M10-phase5-revision-brief-v1-20260523.md and the AI's
output `wa-cluster-M10-subgroup-mapping-revision-v1-20260523.json` (under
'files phase 5 b/').

What this script does:
  Stage 1 — RESOLVE: parse the AI's term routing rules + per-verse split rules
    into a flat vc_id → new-subgroup-code mapping for all 613 verses currently
    routed to M10-A or M10-B. Verses match split rules by reference; the term's
    `primary_route` is the default.
  Stage 2 — VERIFY: every vc_id is routed exactly once; every new sub-group
    code is in the AI's `new_subgroup_definitions` list; §8.6 distribution
    check holds.
  Stage 3 — APPLY (single transaction):
    (a) INSERT 16 new cluster_subgroup rows (M10-J..M10-Y).
    (b) DELETE old mti_term_subgroup rows for the M10-A and M10-B sub-groups
        (the term → sub-group links are about to be re-established).
    (c) UPDATE verse_context.cluster_subgroup_id for the 613 verses to point
        at the new sub-groups.
    (d) INSERT new mti_term_subgroup rows reflecting the per-term primary +
        split routes (one row per (term, destination) pair, with placement_note
        capturing verse counts).
    (e) SOFT-DELETE the old M10-A and M10-B cluster_subgroup rows
        (set delete_flagged=1).
  Stage 4 — REPORT: per-new-sub-group verse counts; confirm zero unrouted.

The resolved flat mapping is written to:
  Sessions/Session_Clusters/M10/files phase 5 b/wa-cluster-M10-subgroup-mapping-revision-resolved-v1-20260523.json
"""
from __future__ import annotations
import argparse, io, json, re, sqlite3, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DIRECTIVE_ID = "wa-cluster-M10-phase5-revision-v1-20260523"

REV_DIR = REPO / "Sessions" / "Session_Clusters" / "M10" / "files phase 5 b"
MAPPING_PATH = REV_DIR / "wa-cluster-M10-subgroup-mapping-revision-v1-20260523.json"
RESOLVED_PATH = REV_DIR / "wa-cluster-M10-subgroup-mapping-revision-resolved-v1-20260523.json"

# Cross-register flags per new sub-group (from the AI's design + brief)
CROSS_FLAGS: dict[str, list[str]] = {
    "M10-R": ["M06"],
    "M10-S": ["M14", "M08", "M31"],
    "M10-W": ["M11"],
}


def _norm_ref(ref: str) -> str:
    return " ".join(ref.split())


# Parse "Book ch:v" or "Book ch:v-v" tokens out of free-form prose.
REF_RE = re.compile(r"\b([1-3]?[A-Z][a-z]{1,4})\s*(\d+):(\d+(?:[/–-]\d+)?)\b")


def extract_refs_from_rule_text(rule_text: str, mti_refs: set[str]) -> list[str]:
    """Pull canonical references out of a rule text. Handles 'Lev 4:2/3/14' shorthand.

    Returns a list of matched canonical references (matching mti_refs membership).
    """
    found: set[str] = set()
    for m in REF_RE.finditer(rule_text):
        book = m.group(1)
        chapter = m.group(2)
        verses_part = m.group(3)
        # Split on / and -
        parts = re.split(r"[/–-]", verses_part)
        for p in parts:
            if p.strip().isdigit():
                ref = _norm_ref(f"{book} {chapter}:{p.strip()}")
                if ref in mti_refs:
                    found.add(ref)
    return sorted(found)


def fetch_vc_index(conn) -> dict:
    """Build maps from DB state needed to resolve.

    Returns:
      old_sg_id: {old_subgroup_code: cluster_subgroup_id}
      mti_term_id_by_strongs: {strongs: mti_term_id}
      vc_by_mti_ref: {(mti_term_id, reference): vc_id}
      mti_refs_by_id: {mti_term_id: set(reference)}
      old_vc_by_sg: {old_subgroup_code: [vc_id, ...]}
    """
    # Old M10-A and M10-B sub-group ids
    sg_rows = conn.execute(
        "SELECT id, subgroup_code FROM cluster_subgroup "
        "WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
    ).fetchall()
    old_sg_id = {r["subgroup_code"]: r["id"] for r in sg_rows}

    # mti_term_id by strongs (canonical Strong's)
    mt_rows = conn.execute(
        "SELECT id, strongs_number FROM mti_terms "
        "WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
    ).fetchall()
    mti_term_id_by_strongs = {r["strongs_number"]: r["id"] for r in mt_rows}

    # vc rows currently in M10-A or M10-B (the 613 in scope)
    vc_rows = conn.execute("""
        SELECT vc.id AS vc_id, vc.mti_term_id, vr.reference, cs.subgroup_code
        FROM verse_context vc
        JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        WHERE cs.cluster_code='M10' AND cs.subgroup_code IN ('M10-A','M10-B')
          AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0
          AND COALESCE(cs.delete_flagged,0)=0
          AND COALESCE(vr.delete_flagged,0)=0
    """).fetchall()
    vc_by_mti_ref: dict[tuple[int, str], int] = {}
    mti_refs_by_id: dict[int, set[str]] = defaultdict(set)
    old_vc_by_sg: dict[str, list[int]] = defaultdict(list)
    for r in vc_rows:
        ref = _norm_ref(r["reference"])
        vc_by_mti_ref[(r["mti_term_id"], ref)] = r["vc_id"]
        mti_refs_by_id[r["mti_term_id"]].add(ref)
        old_vc_by_sg[r["subgroup_code"]].append(r["vc_id"])

    return {
        "old_sg_id": old_sg_id,
        "mti_term_id_by_strongs": mti_term_id_by_strongs,
        "vc_by_mti_ref": vc_by_mti_ref,
        "mti_refs_by_id": mti_refs_by_id,
        "old_vc_by_sg": old_vc_by_sg,
    }


def resolve_routes(spec: dict, idx: dict) -> tuple[dict[int, str], list[str]]:
    """Return (vc_id -> new_subgroup_code, warnings)."""
    warnings: list[str] = []
    vc_to_new_sg: dict[int, str] = {}

    # Multi-faceted handling: pa.sha_political and paraptōma_remaining are virtual term
    # names. We need to handle them carefully — the actual mti_term_id is the same
    # as pa.sha (H6586) and paraptōma (G3900) respectively. The split rule for these
    # specifies a verse-reference list; we apply it.

    PA_SHA_POLITICAL_REFS = {
        "1Ki 12:19", "2Ki 1:1", "2Ki 3:5", "2Ki 3:7", "2Ki 8:20", "2Ki 8:22",
        "2Ch 10:19", "2Ch 21:8", "2Ch 21:10",
    }
    PARAPTOMA_ADAM_REFS = {  # already in M10-F (Phase 6 multi-faceted); not in scope
        "Rom 5:15", "Rom 5:16", "Rom 5:17", "Rom 5:18", "Rom 5:20",
    }

    for term in spec["term_routing_rules"]:
        strongs = term["strongs"]
        translit = term["translit"]
        primary = term["primary_route"]
        rules = term.get("split_rules") or []

        # Resolve mti_term_id
        if translit == "pa.sha_political":
            mti = idx["mti_term_id_by_strongs"].get("H6586")
            if not mti:
                warnings.append(f"pa.sha_political: no mti_term_id found for H6586")
                continue
            # Only the 9 political-revolt refs are in scope (the rest of pa.sha
            # is in M10-F, not in this revision)
            allowed_refs = PA_SHA_POLITICAL_REFS & idx["mti_refs_by_id"].get(mti, set())
        elif translit == "paraptōma_remaining":
            mti = idx["mti_term_id_by_strongs"].get("G3900")
            if not mti:
                warnings.append(f"paraptōma_remaining: no mti_term_id found for G3900")
                continue
            # All paraptōma vc rows currently in M10-B (the Adam ones went to M10-F)
            allowed_refs = idx["mti_refs_by_id"].get(mti, set())
        else:
            mti = idx["mti_term_id_by_strongs"].get(strongs)
            if not mti:
                warnings.append(f"{strongs}: no mti_term_id found")
                continue
            allowed_refs = idx["mti_refs_by_id"].get(mti, set())

        # Apply split rules first (verse-list rules); leftover verses get primary_route.
        routed_refs: set[str] = set()
        for rule in rules:
            dest = rule["destination"]
            refs = extract_refs_from_rule_text(rule["rule"], allowed_refs)
            for ref in refs:
                vc_id = idx["vc_by_mti_ref"].get((mti, ref))
                if vc_id is None:
                    warnings.append(f"{strongs}: ref '{ref}' not found in this term's pool")
                    continue
                if vc_id in vc_to_new_sg:
                    # Already routed (would be a conflict)
                    warnings.append(
                        f"{strongs}: vc_id {vc_id} ({ref}) routed twice "
                        f"(prev={vc_to_new_sg[vc_id]}, now={dest})"
                    )
                    continue
                vc_to_new_sg[vc_id] = dest
                routed_refs.add(ref)

        # Apply primary_route to all remaining refs for this term
        for ref in allowed_refs - routed_refs:
            vc_id = idx["vc_by_mti_ref"].get((mti, ref))
            if vc_id is None:
                continue
            if vc_id in vc_to_new_sg:
                continue
            vc_to_new_sg[vc_id] = primary

    return vc_to_new_sg, warnings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    spec = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))
    new_sg_defs = spec["new_subgroup_definitions"]
    new_codes_set = {d["code"] for d in new_sg_defs}

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print("=== STAGE 1: RESOLVE ===")
    idx = fetch_vc_index(conn)
    n_in_scope = sum(len(v) for v in idx["old_vc_by_sg"].values())
    print(f"  Verses currently in M10-A + M10-B: {n_in_scope}")
    assert n_in_scope == 613, f"Expected 613 verses in scope; found {n_in_scope}"

    vc_to_new_sg, warnings = resolve_routes(spec, idx)
    print(f"  Resolved: {len(vc_to_new_sg)} vc_id assignments")
    print(f"  Warnings: {len(warnings)}")
    for w in warnings[:20]:
        print(f"    {w}")
    if len(warnings) > 20:
        print(f"    ... +{len(warnings) - 20} more")

    print()
    print("=== STAGE 2: VERIFY ===")
    if len(vc_to_new_sg) != n_in_scope:
        unmapped = [v for sg in ("M10-A", "M10-B") for v in idx["old_vc_by_sg"][sg]
                    if v not in vc_to_new_sg]
        print(f"  MISSING {len(unmapped)} vc_ids from resolved mapping (first 20):")
        for vc_id in unmapped[:20]:
            r = cur.execute(
                "SELECT vr.reference, mt.strongs_number, mt.transliteration "
                "FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
                "JOIN mti_terms mt ON mt.id=vc.mti_term_id WHERE vc.id=?",
                (vc_id,)
            ).fetchone()
            print(f"    vc_id={vc_id} {r['reference']} {r['strongs_number']} {r['transliteration']}")
        raise SystemExit("Resolution incomplete — fix and re-run.")
    print(f"  All {len(vc_to_new_sg)} vc_ids routed.")

    # Unknown destinations?
    bad = [(vc, sg) for vc, sg in vc_to_new_sg.items() if sg not in new_codes_set]
    if bad:
        print(f"  Unknown destinations: {len(bad)}")
        for vc, sg in bad[:10]:
            print(f"    vc_id={vc} -> {sg!r}")
        raise SystemExit("Unknown sub-group codes in resolution.")
    print("  All destinations are valid new sub-group codes.")

    # Distribution check
    from collections import Counter
    tallies = Counter(vc_to_new_sg.values())
    GATE = 530
    print("  Per-new-sub-group routed counts:")
    for d in new_sg_defs:
        c = tallies.get(d["code"], 0)
        gate_ok = "✓" if c <= GATE else "FAIL"
        print(f"    {d['code']:<8s} {c:>4d}  {gate_ok}")

    # Write resolved JSON
    resolved = {
        "_resolved_meta": {
            "cluster_code": "M10",
            "phase": "5-REVISION",
            "date": NOW,
            "source_mapping": MAPPING_PATH.name,
            "vc_count": len(vc_to_new_sg),
            "warnings": warnings,
        },
        "vc_id_to_new_subgroup": {str(k): v for k, v in sorted(vc_to_new_sg.items())},
    }
    RESOLVED_PATH.write_text(json.dumps(resolved, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote resolved mapping: {RESOLVED_PATH.relative_to(REPO)}")

    if args.dry_run:
        print("\n[DRY-RUN — no writes]")
        conn.close()
        return 0

    print()
    print("=== STAGE 3: APPLY ===")
    cur.execute("BEGIN")
    try:
        # (a) INSERT 16 new cluster_subgroup rows
        existing_codes = {
            r["subgroup_code"] for r in conn.execute(
                "SELECT subgroup_code FROM cluster_subgroup "
                "WHERE cluster_code='M10' AND COALESCE(delete_flagged,0)=0"
            ).fetchall()
        }
        # Compute which sub-groups actually get verses; skip empty ones (Option A:
        # the AI's design listed 16 sub-groups but the routing rules left some empty —
        # we don't create empty sub-groups; they would violate §8.4.1).
        routed_codes = set(vc_to_new_sg.values())
        empty_codes = [d["code"] for d in new_sg_defs if d["code"] not in routed_codes]
        if empty_codes:
            print(f"  Note: skipping {len(empty_codes)} sub-group(s) with 0 routed verses: "
                  f"{', '.join(empty_codes)}")

        new_sg_id: dict[str, int] = {}
        next_sort = max(
            (r["sort_order"] for r in conn.execute(
                "SELECT sort_order FROM cluster_subgroup WHERE cluster_code='M10'"
            ).fetchall()), default=0
        ) + 1
        for d in new_sg_defs:
            if d["code"] in empty_codes:
                continue
            if d["code"] in existing_codes:
                raise SystemExit(f"Sub-group {d['code']} already exists — aborting")
            descr = d["characteristic"]
            cur.execute(
                "INSERT INTO cluster_subgroup "
                "(cluster_code, subgroup_code, label, core_description, "
                "sort_order, status, version, source, delete_flagged, created_at, last_updated_date) "
                "VALUES ('M10', ?, ?, ?, ?, 'active', 'v1', ?, 0, ?, ?)",
                (d["code"], d["label"], descr, next_sort, DIRECTIVE_ID, NOW, NOW),
            )
            new_sg_id[d["code"]] = cur.lastrowid
            next_sort += 1
        print(f"  (a) Inserted {len(new_sg_id)} cluster_subgroup rows "
              f"(of {len(new_sg_defs)} designed; {len(empty_codes)} skipped as empty)")

        # (b) DELETE old mti_term_subgroup rows for M10-A and M10-B
        n_old_links = cur.execute(
            "SELECT COUNT(*) FROM mti_term_subgroup "
            "WHERE cluster_subgroup_id IN (?, ?)",
            (idx["old_sg_id"]["M10-A"], idx["old_sg_id"]["M10-B"])
        ).fetchone()[0]
        cur.execute(
            "DELETE FROM mti_term_subgroup "
            "WHERE cluster_subgroup_id IN (?, ?)",
            (idx["old_sg_id"]["M10-A"], idx["old_sg_id"]["M10-B"])
        )
        print(f"  (b) Deleted {n_old_links} old mti_term_subgroup rows (M10-A + M10-B)")

        # (c) UPDATE verse_context.cluster_subgroup_id for the 613 verses
        n_updated = 0
        for vc_id, new_sg_code in vc_to_new_sg.items():
            cur.execute(
                "UPDATE verse_context SET cluster_subgroup_id=? "
                "WHERE id=? AND COALESCE(delete_flagged,0)=0",
                (new_sg_id[new_sg_code], vc_id)
            )
            n_updated += cur.rowcount
        print(f"  (c) Updated {n_updated} verse_context rows")
        assert n_updated == len(vc_to_new_sg)

        # (d) INSERT new mti_term_subgroup rows reflecting term → new sub-group links
        term_sg_counts: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        # vc_id → mti_term_id needed
        vc_to_mti = {
            r["id"]: r["mti_term_id"]
            for r in conn.execute(
                "SELECT id, mti_term_id FROM verse_context "
                "WHERE id IN ({})".format(",".join("?" * len(vc_to_new_sg))),
                list(vc_to_new_sg.keys())
            ).fetchall()
        }
        for vc_id, new_sg_code in vc_to_new_sg.items():
            mti = vc_to_mti[vc_id]
            term_sg_counts[mti][new_sg_code] += 1

        n_new_links = 0
        for mti, sg_counts in term_sg_counts.items():
            sorted_sg = sorted(sg_counts.items(), key=lambda x: -x[1])
            primary_sg = sorted_sg[0][0]
            for sg_code, count in sorted_sg:
                note = (f"[primary] {count} verses" if sg_code == primary_sg
                        else f"[secondary] {count} verses")
                cur.execute(
                    "INSERT INTO mti_term_subgroup "
                    "(mti_term_id, cluster_subgroup_id, placement_note, "
                    "delete_flagged, created_at, last_updated_date) "
                    "VALUES (?, ?, ?, 0, ?, ?)",
                    (mti, new_sg_id[sg_code], note, NOW, NOW),
                )
                n_new_links += 1
        print(f"  (d) Inserted {n_new_links} new mti_term_subgroup rows")

        # (e) SOFT-DELETE the old M10-A and M10-B cluster_subgroup rows
        for old_code in ("M10-A", "M10-B"):
            cur.execute(
                "UPDATE cluster_subgroup SET delete_flagged=1, last_updated_date=? "
                "WHERE id=?",
                (NOW, idx["old_sg_id"][old_code])
            )
        print("  (e) Soft-deleted old M10-A and M10-B cluster_subgroup rows")

        conn.commit()
        print(f"\n  Committed at {NOW}")
    except Exception:
        conn.rollback()
        print("ROLLED BACK")
        raise

    # Stage 4: post-checks
    print()
    print("=== STAGE 4: POST-CHECKS ===")
    n_unrouted = cur.execute("""
        SELECT COUNT(*) FROM verse_context vc
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code='M10' AND vc.is_relevant=1
          AND COALESCE(vc.delete_flagged,0)=0 AND vc.cluster_subgroup_id IS NULL
    """).fetchone()[0]
    print(f"  Unrouted is_relevant verses: {n_unrouted}")
    assert n_unrouted == 0

    print()
    print("Final per-sub-group routed counts:")
    rows = cur.execute("""
        SELECT cs.subgroup_code, cs.label, COUNT(vc.id) AS n
        FROM cluster_subgroup cs
        LEFT JOIN verse_context vc ON vc.cluster_subgroup_id=cs.id
            AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
        WHERE cs.cluster_code='M10' AND COALESCE(cs.delete_flagged,0)=0
        GROUP BY cs.subgroup_code ORDER BY cs.sort_order
    """).fetchall()
    total = 0
    for r in rows:
        print(f"  {r['subgroup_code']:<8s} {r['n']:>5d}  {r['label']}")
        total += r["n"]
    print(f"  TOTAL: {total}")

    conn.close()
    print()
    print("=== M10 PHASE 5 REVISION APPLIED ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
