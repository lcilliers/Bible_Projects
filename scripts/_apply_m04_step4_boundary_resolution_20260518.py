"""M04 retrofit Step 4: parse AI's BOUNDARY disposition output + apply bundled directive.

Parses the 6 batch files in `Sessions/Session_Clusters/M04/files boundary correction/`
extracting per-vc_id dispositions. Validates §18.2 eligibility. Builds and applies
the bundled Phase 8.5 directive per researcher Q1 decision (one bundled).

AI's session-log finding: 0% SET-ASIDE, 0% ROUTE-TO-CLUSTER (correctly excluded —
no co-occurring target terms across 257 verses); 100% PROMOTE-TO-SUBGROUP across
M04's 16 sub-groups.

Mode:
  --dry-run    Parse + validate; report; no DB writes.
  --apply      Parse + validate + apply (transactional).

Output files:
  Sessions/Session_Clusters/M04/WA-M04-step4-boundary-resolution-applied-v1-{date}.md
"""
from __future__ import annotations
import argparse
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB = Path("database/bible_research.db")
TODAY = datetime.now().strftime("%Y%m%d")
NOW_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
INPUT_DIR = Path("Sessions/Session_Clusters/M04/files boundary correction")
OUT_REPORT = Path(f"Sessions/Session_Clusters/M04/WA-M04-step4-boundary-resolution-applied-v1-{TODAY}.md")

# Regex for disposition line. Em-dash em (—), hyphen, en-dash variants all accepted.
DISPOSITION_RE = re.compile(
    r"^vc=(\d+)\s+"                                         # vc=<id>
    r"(PROMOTE-TO-SUBGROUP|SET-ASIDE|ROUTE-TO-CLUSTER|RESEARCHER-DECISION)"  # disposition
    r"(?:\s+(M\d+-[A-Z]+))?"                                # optional target (M04-K etc.)
    r"\s*[—–\-]+\s*"                              # em/en dash or hyphen
    r"(.+?)$",                                              # rationale
    re.IGNORECASE,
)


def parse_batch_files() -> list[dict]:
    """Walk all .md files in the input dir; extract vc_id disposition lines."""
    disp = []
    seen_vc_ids = set()
    for fp in sorted(INPUT_DIR.glob("WA-M04-step4-boundary-output-batch*.md")):
        for line in fp.read_text(encoding="utf-8").splitlines():
            m = DISPOSITION_RE.match(line.strip())
            if not m:
                continue
            vc_id = int(m.group(1))
            if vc_id in seen_vc_ids:
                # Duplicate vc_id — flag and skip
                print(f"WARNING: duplicate vc_id {vc_id} in {fp.name}")
                continue
            seen_vc_ids.add(vc_id)
            disp.append({
                "vc_id": vc_id,
                "disposition": m.group(2).upper(),
                "target": m.group(3),  # may be None for SET-ASIDE
                "rationale": m.group(4).strip(),
                "source_file": fp.name,
            })
    return disp


def validate(disp_list, conn):
    """Validate per §18.2: vc_ids match BOUNDARY corpus; targets exist; disposition formed correctly."""
    errors = []
    warnings = []

    # 1. Build the expected BOUNDARY set
    expected = {
        r[0] for r in conn.execute(
            """
            SELECT vc.id FROM verse_context vc
            JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
            WHERE cs.cluster_code='M04' AND cs.subgroup_code='M04-BOUNDARY'
              AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
            """
        ).fetchall()
    }
    actual = {d["vc_id"] for d in disp_list}
    missing = expected - actual
    extra = actual - expected
    if missing:
        errors.append(f"Missing {len(missing)} expected vc_ids (in BOUNDARY but no disposition): {sorted(missing)[:20]}{'...' if len(missing)>20 else ''}")
    if extra:
        errors.append(f"Extra {len(extra)} unexpected vc_ids (have disposition but not in BOUNDARY): {sorted(extra)[:20]}{'...' if len(extra)>20 else ''}")

    # 2. Build valid sub-group code → id map
    sg_map = {
        r[0]: r[1] for r in conn.execute(
            "SELECT subgroup_code, id FROM cluster_subgroup WHERE cluster_code='M04' AND COALESCE(delete_flagged,0)=0"
        ).fetchall()
    }

    # 3. Per-disposition validation
    for d in disp_list:
        if d["disposition"] == "PROMOTE-TO-SUBGROUP":
            if not d["target"]:
                errors.append(f"vc={d['vc_id']}: PROMOTE without target sub-group")
                continue
            if d["target"] not in sg_map:
                errors.append(f"vc={d['vc_id']}: PROMOTE target {d['target']!r} is not a valid M04 sub-group code")
                continue
            if d["target"] == "M04-BOUNDARY":
                errors.append(f"vc={d['vc_id']}: PROMOTE to M04-BOUNDARY is forbidden — that's the source we're emptying")
                continue
        elif d["disposition"] == "ROUTE-TO-CLUSTER":
            warnings.append(f"vc={d['vc_id']}: ROUTE-TO-CLUSTER {d['target']!r} — verify eligibility (target term at same vr_id)")
        elif d["disposition"] == "SET-ASIDE":
            # Check rationale isn't a forbidden ground (lightweight)
            r = (d["rationale"] or "").lower()
            forbidden_patterns = ["not god-directed", "no clear vertical", "lacks theolog", "no spiritual",
                                   "physical_only", "no_inner_being", "too mundane"]
            for p in forbidden_patterns:
                if p in r:
                    warnings.append(f"vc={d['vc_id']}: SET-ASIDE rationale contains §4.5.1 forbidden ground '{p}'")
        elif d["disposition"] == "RESEARCHER-DECISION":
            warnings.append(f"vc={d['vc_id']}: flagged for researcher decision")

    return errors, warnings, sg_map


def build_directive_operations(disp_list, sg_map, conn) -> list[dict]:
    """Build the SQL operations for the bundled Phase 8.5 directive."""
    operations = []

    # Determine which mti_term_subgroup links need creating
    # For each (term, target_sg) in the disposition list, check if active link exists
    needed_links = set()
    for d in disp_list:
        if d["disposition"] != "PROMOTE-TO-SUBGROUP":
            continue
        target_sg_id = sg_map[d["target"]]
        # Get the term for this vc
        term_row = conn.execute("SELECT mti_term_id FROM verse_context WHERE id=?", (d["vc_id"],)).fetchone()
        if term_row:
            needed_links.add((term_row[0], target_sg_id, d["target"]))

    # Filter out links that already exist (active)
    new_links = []
    for term_id, sg_id, sg_code in sorted(needed_links):
        existing = conn.execute(
            "SELECT id FROM mti_term_subgroup WHERE mti_term_id=? AND cluster_subgroup_id=? AND COALESCE(delete_flagged,0)=0",
            (term_id, sg_id),
        ).fetchone()
        if not existing:
            term_info = conn.execute("SELECT strongs_number, transliteration FROM mti_terms WHERE id=?", (term_id,)).fetchone()
            new_links.append({
                "mti_term_id": term_id,
                "cluster_subgroup_id": sg_id,
                "subgroup_code": sg_code,
                "strongs": term_info[0],
                "translit": term_info[1],
            })

    op_id = 1

    # Operation A: INSERT mti_term_subgroup links (where needed)
    for link in new_links:
        operations.append({
            "op_id": f"OP-{op_id:05d}",
            "operation": "insert_mti_term_subgroup",  # custom — script handles directly
            "table": "mti_term_subgroup",
            "values": {
                "mti_term_id": link["mti_term_id"],
                "cluster_subgroup_id": link["cluster_subgroup_id"],
                "placement_note": f"[primary, M04 Step 4 BOUNDARY resolution 2026-05-18] Term routed to {link['subgroup_code']} per AI disposition pass (Phase 8.5 §11A).",
            },
            "description": f"INSERT mti_term_subgroup: {link['strongs']} {link['translit']} → {link['subgroup_code']}",
        })
        op_id += 1

    # Operation B: PROMOTE updates per vc_id
    for d in disp_list:
        if d["disposition"] == "PROMOTE-TO-SUBGROUP":
            target_sg_id = sg_map[d["target"]]
            operations.append({
                "op_id": f"OP-{op_id:05d}",
                "operation": "update_verse_context",
                "table": "verse_context",
                "match": {"id": d["vc_id"]},
                "set": {
                    "cluster_subgroup_id": target_sg_id,
                    "group_id": None,
                    "is_anchor": 0,
                    "notes": f"[audit-fix v2_5 Step 4 Phase 8.5 2026-05-18] PROMOTE-TO-SUBGROUP {d['target']} per AI disposition pass. VCG to be assigned in Step 5.",
                },
                "description": f"PROMOTE vc={d['vc_id']} → {d['target']}",
                "rationale": d["rationale"][:240],
            })
            op_id += 1
        elif d["disposition"] == "SET-ASIDE":
            operations.append({
                "op_id": f"OP-{op_id:05d}",
                "operation": "update_verse_context",
                "table": "verse_context",
                "match": {"id": d["vc_id"]},
                "set": {
                    "is_relevant": 0,
                    "is_anchor": 0,
                    "cluster_subgroup_id": None,
                    "group_id": None,
                    "set_aside_reason": d["rationale"][:480],
                    "notes": f"[audit-fix v2_5 Step 4 Phase 8.5 2026-05-18] SET-ASIDE per AI disposition pass.",
                },
                "description": f"SET-ASIDE vc={d['vc_id']}",
                "rationale": d["rationale"][:240],
            })
            op_id += 1
        # ROUTE-TO-CLUSTER and RESEARCHER-DECISION — none expected per AI summary
        else:
            operations.append({
                "op_id": f"OP-{op_id:05d}",
                "operation": "SKIP_FOR_REVIEW",
                "vc_id": d["vc_id"],
                "disposition": d["disposition"],
                "target": d["target"],
                "rationale": d["rationale"],
                "description": f"SKIP vc={d['vc_id']} disposition={d['disposition']} — requires researcher review",
            })
            op_id += 1

    return operations


def apply_directive(operations, conn):
    """Apply the operations in a single transaction."""
    cur = conn.cursor()
    cur.execute("BEGIN")
    counts = Counter()
    try:
        for op in operations:
            if op["operation"] == "insert_mti_term_subgroup":
                v = op["values"]
                cur.execute(
                    """
                    INSERT INTO mti_term_subgroup
                      (mti_term_id, cluster_subgroup_id, placement_note, delete_flagged, created_at, last_updated_date)
                    VALUES (?, ?, ?, 0, ?, ?)
                    """,
                    (v["mti_term_id"], v["cluster_subgroup_id"], v["placement_note"], NOW_UTC, NOW_UTC),
                )
                counts["mti_term_subgroup_inserted"] += 1
            elif op["operation"] == "update_verse_context":
                set_clauses = []
                set_vals = []
                for k, v in op["set"].items():
                    set_clauses.append(f"{k}=?")
                    set_vals.append(v)
                set_vals.append(op["match"]["id"])
                cur.execute(
                    f"UPDATE verse_context SET {', '.join(set_clauses)} WHERE id=? AND COALESCE(delete_flagged,0)=0",
                    set_vals,
                )
                if "set_aside_reason" in op["set"]:
                    counts["set_aside"] += 1
                else:
                    counts["promote"] += 1
            elif op["operation"] == "SKIP_FOR_REVIEW":
                counts["skipped"] += 1
        conn.commit()
        return counts
    except Exception:
        conn.rollback()
        raise


def write_report(disp_list, operations, errors, warnings, counts, dry_run):
    sg_counts = Counter()
    for d in disp_list:
        if d["disposition"] == "PROMOTE-TO-SUBGROUP":
            sg_counts[d["target"]] += 1
        elif d["disposition"] == "SET-ASIDE":
            sg_counts["SET-ASIDE"] += 1
        else:
            sg_counts[d["disposition"]] += 1

    L = []
    L.append("# M04 Step 4 — BOUNDARY resolution applied report")
    L.append("")
    L.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    L.append(f"**Mode:** {'DRY RUN' if dry_run else 'LIVE'}")
    L.append(f"**Source:** 6 batch files in `{INPUT_DIR}`")
    L.append(f"**Total dispositions parsed:** {len(disp_list)}")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Disposition distribution")
    L.append("")
    L.append("| Target | Count |")
    L.append("|---|---:|")
    for target in sorted(sg_counts.keys()):
        L.append(f"| {target} | {sg_counts[target]} |")
    L.append(f"| **TOTAL** | **{sum(sg_counts.values())}** |")
    L.append("")

    if errors:
        L.append("## Validation errors")
        L.append("")
        for e in errors:
            L.append(f"- {e}")
        L.append("")

    if warnings:
        L.append(f"## Warnings ({len(warnings)})")
        L.append("")
        for w in warnings[:30]:
            L.append(f"- {w}")
        if len(warnings) > 30:
            L.append(f"- … and {len(warnings)-30} more")
        L.append("")

    L.append("## Operations summary")
    L.append("")
    op_counts = Counter(op["operation"] for op in operations)
    for op_type, n in op_counts.most_common():
        L.append(f"- {op_type}: {n}")
    L.append("")

    if not dry_run:
        L.append("## Apply outcome")
        L.append("")
        for k, v in counts.items():
            L.append(f"- {k}: {v}")
        L.append("")

    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUT_REPORT.write_text("\n".join(L), encoding="utf-8")
    print(f"Report written: {OUT_REPORT}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Parse + validate; no DB writes")
    parser.add_argument("--apply", action="store_true", help="Apply (transactional)")
    args = parser.parse_args()
    if not (args.dry_run or args.apply):
        parser.error("Must pass --dry-run or --apply")
    dry_run = args.dry_run

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    disp_list = parse_batch_files()
    print(f"Parsed {len(disp_list)} dispositions from batch files")

    errors, warnings, sg_map = validate(disp_list, conn)
    if errors:
        print(f"\n{'!'*60}")
        print(f"VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print('!'*60)
        if not dry_run:
            print("\nApply blocked by errors. Re-run with --dry-run to inspect.")
            write_report(disp_list, [], errors, warnings, {}, dry_run=False)
            conn.close()
            return

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings[:10]:
            print(f"  - {w}")
        if len(warnings) > 10:
            print(f"  ... and {len(warnings)-10} more")

    operations = build_directive_operations(disp_list, sg_map, conn)
    print(f"\nBuilt {len(operations)} operations.")

    counts = {}
    if dry_run:
        print("\nDRY RUN — no DB writes.")
    else:
        print("\nApplying ...")
        counts = apply_directive(operations, conn)
        print(f"Applied: {dict(counts)}")
        # Post-apply: M04-BOUNDARY remaining count
        post = conn.execute(
            """
            SELECT COUNT(*) FROM verse_context vc
            JOIN cluster_subgroup cs ON cs.id = vc.cluster_subgroup_id
            WHERE cs.cluster_code='M04' AND cs.subgroup_code='M04-BOUNDARY'
              AND vc.is_relevant=1 AND COALESCE(vc.delete_flagged,0)=0
            """
        ).fetchone()[0]
        print(f"\nPost-apply M04-BOUNDARY active relevant verses: {post}")

    write_report(disp_list, operations, errors, warnings, counts, dry_run)
    conn.close()


if __name__ == "__main__":
    main()
