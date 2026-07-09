"""_assess_cluster_coverage_v1_20260505.py — read-only.

Per-cluster (legacy registry-cluster) coverage report. For each registry in the
target cluster, list its OWNER terms and count verses by status:

  - analysed:     verse assigned to a verse_context_group (group_id > 0, is_relevant=1)
  - set_aside:    verse explicitly excluded with set_aside_reason
  - not_relevant: verse marked is_relevant=0 (rejected as not contributing)
  - pending_in_vc: in verse_context but no decision yet (is_relevant=1, no group, no set_aside)
  - untouched:    in wa_verse_records but no verse_context row at all

Coverage % = (analysed + set_aside + not_relevant) / active.
"Fully covered" = pending = pending_in_vc + untouched = 0.

Usage:
  python scripts/_assess_cluster_coverage_v1_20260505.py --cluster C17
"""
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    # Legacy C-cluster coverage reports go to a dedicated subfolder
    _dest_dir = os.path.join(
        "Sessions", "Session_Clusters", "legacy_c_clusters"
    )
    os.makedirs(_dest_dir, exist_ok=True)
    out_path = args.out or os.path.join(
        _dest_dir,
        f"wa-cluster-{args.cluster.lower()}-coverage-"
        f"v1-{datetime.now().strftime('%Y%m%d')}.md"
    )

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Registries
    registries = conn.execute("""
        SELECT id, no, word, session_b_status, verse_context_status,
               phase1_verse_count, unique_term_count
          FROM word_registry
         WHERE cluster_assignment = ?
         ORDER BY no
    """, (args.cluster,)).fetchall()
    print(f"Cluster {args.cluster}: {len(registries)} registries", flush=True)
    if not registries:
        print("No registries found.", flush=True)
        return 0
    reg_ids = [r["id"] for r in registries]
    placeholders = ",".join("?" * len(reg_ids))

    # Bulk fetch all OWNER terms for these registries
    print("Fetching OWNER terms...", flush=True)
    terms = conn.execute(f"""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.gloss,
               mt.transliteration, mt.language, mt.status,
               mt.owning_registry_fk
          FROM mti_terms mt
         WHERE mt.owning_registry_fk IN ({placeholders})
           AND mt.status NOT IN ('candidate_delete','delete','excluded')
         ORDER BY mt.strongs_number
    """, reg_ids).fetchall()
    print(f"OWNER terms: {len(terms)}", flush=True)
    term_by_id = {t["mti_id"]: dict(t) for t in terms}
    mti_ids = list(term_by_id.keys())

    # Per-verse-record status: each unique active wa_verse_records row gets
    # a single status, derived by precedence over its verse_context rows
    # (analysed > set_aside > not_relevant > pending). Untouched = no VC rows.
    print("Computing per-verse-record status (precedence-based)...",
          flush=True)
    placeholders_t = ",".join("?" * len(mti_ids))
    vc_status = {}
    for mid in mti_ids:
        vc_status[mid] = {
            "active": 0, "analysed": 0, "set_aside": 0,
            "not_relevant": 0, "pending_in_vc": 0, "untouched": 0,
        }
    rows = conn.execute(f"""
        WITH verse_status AS (
          SELECT vr.id AS verse_id, vr.mti_term_id,
                 MAX(CASE WHEN COALESCE(vc.delete_flagged,0)=0
                            AND vc.group_id IS NOT NULL
                            AND vc.group_id > 0
                            AND vc.is_relevant = 1
                          THEN 1 ELSE 0 END) AS has_analysed,
                 MAX(CASE WHEN COALESCE(vc.delete_flagged,0)=0
                            AND vc.set_aside_reason IS NOT NULL
                          THEN 1 ELSE 0 END) AS has_set_aside,
                 MAX(CASE WHEN COALESCE(vc.delete_flagged,0)=0
                            AND (vc.group_id IS NULL OR vc.group_id = 0)
                            AND vc.is_relevant = 0
                            AND vc.set_aside_reason IS NULL
                          THEN 1 ELSE 0 END) AS has_not_relevant,
                 MAX(CASE WHEN COALESCE(vc.delete_flagged,0)=0
                            AND (vc.group_id IS NULL OR vc.group_id = 0)
                            AND vc.is_relevant = 1
                            AND vc.set_aside_reason IS NULL
                          THEN 1 ELSE 0 END) AS has_pending,
                 SUM(CASE WHEN vc.id IS NOT NULL
                            AND COALESCE(vc.delete_flagged,0)=0
                          THEN 1 ELSE 0 END) AS active_vc_rows
            FROM wa_verse_records vr
            LEFT JOIN verse_context vc
                   ON vc.verse_record_id = vr.id
                  AND vc.mti_term_id = vr.mti_term_id
           WHERE COALESCE(vr.delete_flagged,0) = 0
             AND vr.mti_term_id IN ({placeholders_t})
           GROUP BY vr.id, vr.mti_term_id
        )
        SELECT mti_term_id,
               COUNT(*) AS active,
               SUM(CASE WHEN has_analysed = 1 THEN 1 ELSE 0 END) AS analysed,
               SUM(CASE WHEN has_analysed = 0 AND has_set_aside = 1
                          THEN 1 ELSE 0 END) AS set_aside,
               SUM(CASE WHEN has_analysed = 0 AND has_set_aside = 0
                          AND has_not_relevant = 1
                          THEN 1 ELSE 0 END) AS not_relevant,
               SUM(CASE WHEN active_vc_rows > 0
                          AND has_analysed = 0 AND has_set_aside = 0
                          AND has_not_relevant = 0 AND has_pending = 1
                          THEN 1 ELSE 0 END) AS pending_in_vc,
               SUM(CASE WHEN active_vc_rows = 0
                          THEN 1 ELSE 0 END) AS untouched
          FROM verse_status
         GROUP BY mti_term_id
    """, mti_ids).fetchall()
    for r in rows:
        mid = r["mti_term_id"]
        if mid not in vc_status:
            continue
        vc_status[mid]["active"] = r["active"] or 0
        vc_status[mid]["analysed"] = r["analysed"] or 0
        vc_status[mid]["set_aside"] = r["set_aside"] or 0
        vc_status[mid]["not_relevant"] = r["not_relevant"] or 0
        vc_status[mid]["pending_in_vc"] = r["pending_in_vc"] or 0
        vc_status[mid]["untouched"] = r["untouched"] or 0

    # Build per-term coverage
    print("Building report...", flush=True)
    by_reg = {r["id"]: {
        "no": r["no"], "word": r["word"], "id": r["id"],
        "sb_status": r["session_b_status"],
        "vc_status": r["verse_context_status"],
        "p1_verses": r["phase1_verse_count"],
        "uniq_terms": r["unique_term_count"],
        "terms": [],
    } for r in registries}
    for mid, t in term_by_id.items():
        s = vc_status[mid]
        active = s["active"]
        analysed = s["analysed"]
        set_aside = s["set_aside"]
        not_relevant = s["not_relevant"]
        pending_in_vc = s["pending_in_vc"]
        untouched = s["untouched"]
        covered = analysed + set_aside + not_relevant
        pending = pending_in_vc + untouched
        cov_pct = (covered / active * 100.0) if active else 100.0
        term_record = {
            "mti_id": mid,
            "strongs": t["strongs_number"],
            "gloss": t["gloss"],
            "translit": t["transliteration"],
            "lang": t["language"],
            "active": active,
            "analysed": analysed,
            "set_aside": set_aside,
            "not_relevant": not_relevant,
            "pending_in_vc": pending_in_vc,
            "untouched": untouched,
            "pending": pending,
            "covered": covered,
            "coverage_pct": cov_pct,
            "fully_covered": pending == 0 and active > 0,
        }
        by_reg[t["owning_registry_fk"]]["terms"].append(term_record)

    # Per-registry roll-up
    report = []
    for r in registries:
        rd = by_reg[r["id"]]
        rd["term_count"] = len(rd["terms"])
        rd["fully_covered_terms"] = sum(
            1 for t in rd["terms"] if t["fully_covered"]
        )
        rd["zero_verse_terms"] = sum(
            1 for t in rd["terms"] if t["active"] == 0
        )
        rd["total_active_verses"] = sum(t["active"] for t in rd["terms"])
        rd["total_covered_verses"] = sum(t["covered"] for t in rd["terms"])
        rd["total_pending_verses"] = sum(t["pending"] for t in rd["terms"])
        rd["total_untouched"] = sum(t["untouched"] for t in rd["terms"])
        rd["coverage_pct"] = (
            rd["total_covered_verses"] / rd["total_active_verses"] * 100.0
            if rd["total_active_verses"] else 100.0
        )
        report.append(rd)

    conn.close()

    # Render
    lines = []
    lines.append(f"# Cluster {args.cluster} — coverage status by registry "
                 f"and term\n")
    lines.append(f"**Generated:** {now_iso()}  ")
    lines.append(f"**Cluster:** `{args.cluster}` "
                 f"({len(registries)} registries)\n")
    lines.append("**Coverage definition:** a term is *fully covered* when "
                 "every active OWNER verse (in `wa_verse_records`) is either "
                 "**analysed** (assigned to a `verse_context_group`), "
                 "explicitly **set-aside** with a reason, or marked "
                 "**not-relevant** — i.e. **pending = 0**.\n")
    lines.append("Pending splits into two:")
    lines.append("- **pending in VC** — the verse has a `verse_context` row "
                 "but no decision yet (`is_relevant=1`, no group, no "
                 "set_aside).")
    lines.append("- **untouched** — the verse exists in `wa_verse_records` "
                 "but has no `verse_context` row at all (was never reviewed).")
    lines.append("\nCoverage % = (analysed + set_aside + not_relevant) / "
                 "total active verses.\n")
    lines.append("---\n")
    lines.append("## Registry roll-up\n")
    lines.append("| # | Word | SB status | VC status | Terms (✅/zero/total) | "
                 "Active verses | Covered | Pending in VC | Untouched | "
                 "Coverage % |")
    lines.append("|---|---|---|---|---|---:|---:|---:|---:|---:|")
    for r in report:
        pending_in_vc_total = sum(t["pending_in_vc"] for t in r["terms"])
        lines.append(
            f"| R{r['no']:03d} | {r['word']} | "
            f"{r['sb_status'] or '—'} | {r['vc_status'] or '—'} | "
            f"{r['fully_covered_terms']} / {r['zero_verse_terms']} / "
            f"{r['term_count']} | "
            f"{r['total_active_verses']:,} | "
            f"{r['total_covered_verses']:,} | "
            f"{pending_in_vc_total} | "
            f"{r['total_untouched']} | "
            f"{r['coverage_pct']:.1f}% |"
        )
    lines.append("")

    for r in report:
        lines.append(f"\n## R{r['no']:03d} {r['word']}\n")
        lines.append(f"**SB status:** {r['sb_status'] or '—'} · "
                     f"**VC status:** {r['vc_status'] or '—'}  ")
        lines.append(f"**Terms:** {r['term_count']} OWNER — "
                     f"{r['fully_covered_terms']} ✅ fully covered, "
                     f"{r['zero_verse_terms']} — with no active verses, "
                     f"{r['term_count'] - r['fully_covered_terms'] - r['zero_verse_terms']} "
                     f"⚠ with pending verses  ")
        lines.append(f"**Verses:** {r['total_active_verses']:,} active — "
                     f"**{r['total_covered_verses']:,}** covered "
                     f"({r['coverage_pct']:.1f}%), "
                     f"{r['total_pending_verses']:,} pending "
                     f"({r['total_untouched']} untouched)\n")
        if not r["terms"]:
            lines.append("*(no OWNER terms)*\n")
            continue
        lines.append("| ✓ | Strong's | Lang | Translit | Gloss | "
                     "Active | Analysed | Set aside | Not relevant | "
                     "Pending in VC | Untouched | Coverage |")
        lines.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|")
        for t in sorted(r["terms"], key=lambda x: -x["active"]):
            mark = "✅" if t["fully_covered"] else (
                "—" if t["active"] == 0 else "⚠"
            )
            lines.append(
                f"| {mark} | {t['strongs']} | {t['lang'][:1]} | "
                f"{t['translit']} | {t['gloss']} | "
                f"{t['active']} | {t['analysed']} | "
                f"{t['set_aside']} | {t['not_relevant']} | "
                f"{t['pending_in_vc']} | {t['untouched']} | "
                f"{t['coverage_pct']:.1f}% |"
            )

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
