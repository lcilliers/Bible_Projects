"""_generate_cluster_term_report_v1_20260505.py — read-only.

Builds a comprehensive term-by-cluster report from the database:

  Workflow/Clusters/wa-cluster-overview-v{ver}-{date}.md     — index over all clusters
  Workflow/Clusters/wa-cluster-overview-v{ver}-{date}.json   — same in JSON
  Workflow/Clusters/per-cluster/wa-cluster-{code}-detail-v{ver}-{date}.md
                                                              — one per cluster

Per-term info pulled from the database:
  - Identity:    strongs_number, transliteration, gloss, language
  - Provenance:  owning registry, bucket, term_owner_type
  - Meaning:     wa_term_inventory.meaning, short_def_mounce, evidential_status
  - Coverage:    active verses + verse-level status (analysed / set_aside /
                 not_relevant / pending_in_vc / untouched) using the same
                 precedence-based per-verse-record logic as the M-cluster
                 coverage script
  - Context:     root family count, related-word count, cross-ref count
  - Findings:    direct (Strong's mention) + via anchor verse + via registry
  - Pointers:    direct + via registry

Read-only — does not modify the DB.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
WF_DIR = os.path.join("Workflow", "Clusters")
SESSIONS_DIR = os.path.join("Sessions", "Session_Clusters")

STRONGS_RE = re.compile(r"\b([HG]\d{4}[A-Z]?)\b")
ANCHOR_REF_RE = re.compile(
    r"\b(\d?[A-Za-z]{2,5})\s+(\d{1,3}):(\d{1,3})(?:-(\d{1,3}))?",
)
ANCHOR_PAREN_RE = re.compile(r"\([^)]*\)")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_version_in_dirs(dirs_and_bases, exts=("md", "json")) -> str:
    """Scan multiple (dir, base_name) pairs for files of pattern
    `{base}-v{N}-{YYYYMMDD}.{ext}`. Return next vN as 'vN' string."""
    import re as _re
    max_v = 0
    for d, base in dirs_and_bases:
        if not os.path.isdir(d):
            continue
        pat = _re.compile(
            r"^" + _re.escape(base)
            + r"-v(\d+)-\d{8}\.(?:" + "|".join(exts) + r")$"
        )
        for f in os.listdir(d):
            m = pat.match(f)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def build_book_lookup(conn):
    out = {}
    for r in conn.execute(
        "SELECT id, name, abbreviation, short_code FROM books"
    ).fetchall():
        bid = r["id"]
        for k in (r["abbreviation"], r["short_code"], r["name"]):
            if k:
                out[k.lower()] = bid
    aliases = {
        "1cor": "1Co", "2cor": "2Co", "1th": "1Th", "2th": "2Th",
        "1jo": "1Jn", "2jo": "2Jn", "3jo": "3Jn",
        "song": "Sng", "ps": "Psa", "jn": "Joh",
        "mt": "Mat", "mk": "Mar", "lk": "Luk",
        "co1": "1Co", "co2": "2Co",
        "jas": "Jam", "phi": "Php", "phil": "Php", "phili": "Php",
        "1tim": "1Ti", "2tim": "2Ti", "1pet": "1Pe", "2pet": "2Pe",
        "ezek": "Eze", "zech": "Zec", "matt": "Mat",
        "1sam": "1Sa", "2sam": "2Sa", "1kgs": "1Ki", "2kgs": "2Ki",
        "1chr": "1Ch", "2chr": "2Ch",
        "deut": "Deu", "prov": "Pro", "eccl": "Ecc",
        "isa": "Isa", "jer": "Jer", "josh": "Jos", "judg": "Jdg",
    }
    for alt, canonical in aliases.items():
        if canonical.lower() in out:
            out[alt.lower()] = out[canonical.lower()]
    return out


def parse_anchor_verses(text, book_lookup):
    if not text:
        return
    cleaned = ANCHOR_PAREN_RE.sub("", text)
    for m in ANCHOR_REF_RE.finditer(cleaned):
        bk_token = m.group(1)
        chap = int(m.group(2))
        v1 = int(m.group(3))
        v2 = m.group(4)
        bid = book_lookup.get(bk_token.lower())
        if not bid:
            continue
        if v2 is None:
            yield (bid, chap, v1)
        else:
            for v in range(v1, int(v2) + 1):
                yield (bid, chap, v)


def fetch_clusters(conn):
    return conn.execute("""
        SELECT cluster_code, description, gloss, source, bucket, status,
               version, last_updated_date
          FROM cluster
         ORDER BY
           CASE bucket WHEN 'NAMED' THEN 0 ELSE 1 END,
           cluster_code
    """).fetchall()


def fetch_term_metadata(conn):
    """Return dict: strongs -> dict of all term metadata, keyed once per
    Strong's (deduplicated since mti_terms has duplicates)."""
    rows = conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.gloss, mt.transliteration,
               mt.language, mt.status AS mti_status, mt.cluster_code,
               mt.owning_registry_fk,
               wr.no AS reg_no, wr.word AS reg_word,
               wr.cluster_assignment AS legacy_c_cluster,
               ti.meaning AS inv_meaning,
               ti.short_def_mounce AS mounce,
               ti.evidential_status,
               ti.term_owner_type,
               ti.occurrence_count
          FROM mti_terms mt
          LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
          LEFT JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
         WHERE mt.cluster_code IS NOT NULL
    """).fetchall()
    by_strong = {}
    mti_to_strong = {}
    for r in rows:
        s = r["strongs_number"]
        if s not in by_strong:
            by_strong[s] = dict(r)
        # Track all mti_ids for this Strong's (for verse lookup)
        by_strong[s].setdefault("_mti_ids", set()).add(r["mti_id"])
        mti_to_strong[r["mti_id"]] = s
    return by_strong, mti_to_strong


def fetch_verse_coverage(conn, mti_ids):
    """Return dict: mti_term_id -> coverage stats per the precedence rule."""
    out = defaultdict(lambda: {
        "active": 0, "analysed": 0, "set_aside": 0,
        "not_relevant": 0, "pending_in_vc": 0, "untouched": 0,
    })
    if not mti_ids:
        return out
    ph = ",".join("?" * len(mti_ids))
    rows = conn.execute(f"""
        WITH verse_status AS (
          SELECT vr.id AS verse_id, vr.mti_term_id,
                 MAX(CASE WHEN COALESCE(vc.delete_flagged,0)=0
                            AND vc.group_id IS NOT NULL AND vc.group_id > 0
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
             AND vr.mti_term_id IN ({ph})
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
    """, list(mti_ids)).fetchall()
    for r in rows:
        for k in ("active", "analysed", "set_aside", "not_relevant",
                  "pending_in_vc", "untouched"):
            out[r["mti_term_id"]][k] = r[k] or 0
    return out


def fetch_finding_pointer_counts(conn, strongs_set, mti_to_strong,
                                  registry_to_strongs):
    """Build per-Strong's counts: findings_direct, findings_via_anchor,
    findings_via_registry, pointers_direct, pointers_via_registry."""
    findings = conn.execute("""
        SELECT id, registry_id, finding, anchor_verses
          FROM wa_session_b_findings
         WHERE COALESCE(delete_flag,0) = 0
    """).fetchall()
    pointers = conn.execute("""
        SELECT id, registry_id, cross_registry_id, strongs_reference, description
          FROM wa_session_research_flags
         WHERE COALESCE(resolved,0) = 0
           AND flag_code = 'SD_POINTER'
    """).fetchall()

    # Verse-record location index for cluster terms
    book_lookup = build_book_lookup(conn)
    verse_index = defaultdict(set)
    if mti_to_strong:
        ph = ",".join("?" * len(mti_to_strong))
        for r in conn.execute(f"""
            SELECT book_id, chapter, verse_num, mti_term_id
              FROM wa_verse_records
             WHERE COALESCE(delete_flagged,0) = 0
               AND mti_term_id IN ({ph})
        """, list(mti_to_strong.keys())).fetchall():
            mid = r["mti_term_id"]
            if mid in mti_to_strong:
                verse_index[(r["book_id"], r["chapter"], r["verse_num"])].add(
                    mti_to_strong[mid]
                )

    findings_direct = defaultdict(set)
    findings_anchor = defaultdict(set)
    findings_registry = defaultdict(set)  # by reg_id
    pointers_direct = defaultdict(set)
    pointers_registry = defaultdict(set)

    for f in findings:
        text = " | ".join([f["finding"] or "", f["anchor_verses"] or ""])
        for s in set(STRONGS_RE.findall(text)) & strongs_set:
            findings_direct[s].add(f["id"])
        # registry
        if f["registry_id"]:
            findings_registry[f["registry_id"]].add(f["id"])
        # anchor-verse resolution
        if f["anchor_verses"]:
            for bid, chap, vnum in parse_anchor_verses(f["anchor_verses"],
                                                       book_lookup):
                for s in verse_index.get((bid, chap, vnum), set()):
                    findings_anchor[s].add(f["id"])

    for p in pointers:
        sref = p["strongs_reference"] or ""
        text = " | ".join([p["description"] or "", sref])
        for s in set(STRONGS_RE.findall(text)) & strongs_set:
            pointers_direct[s].add(p["id"])
        if p["registry_id"]:
            pointers_registry[p["registry_id"]].add(p["id"])
        if p["cross_registry_id"]:
            pointers_registry[p["cross_registry_id"]].add(p["id"])

    return {
        "findings_direct": findings_direct,
        "findings_anchor": findings_anchor,
        "findings_registry": findings_registry,
        "pointers_direct": pointers_direct,
        "pointers_registry": pointers_registry,
    }


def fetch_aux_counts(conn, strongs_list):
    """root_family_count, related_word_count, cross_ref_count per strongs.

    Joins via term_inv_id (root_family, related_words) or mti_term_id
    (cross_refs) since those are the actual FK columns."""
    if not strongs_list:
        return defaultdict(lambda: {"rf": 0, "rel": 0, "xref": 0})
    out = defaultdict(lambda: {"rf": 0, "rel": 0, "xref": 0})
    ph = ",".join("?" * len(strongs_list))

    # Root family — wa_term_root_family.term_inv_id → wa_term_inventory
    for r in conn.execute(f"""
        SELECT ti.strongs_number, COUNT(DISTINCT wrf.id) c
          FROM wa_term_inventory ti
          JOIN wa_term_root_family wrf ON wrf.term_inv_id = ti.id
         WHERE ti.strongs_number IN ({ph})
           AND COALESCE(wrf.delete_flagged,0) = 0
         GROUP BY ti.strongs_number
    """, strongs_list).fetchall():
        out[r["strongs_number"]]["rf"] = r["c"]

    # Related words — wa_term_related_words.term_inv_id → wa_term_inventory
    for r in conn.execute(f"""
        SELECT ti.strongs_number, COUNT(DISTINCT wtrw.id) c
          FROM wa_term_inventory ti
          JOIN wa_term_related_words wtrw ON wtrw.term_inv_id = ti.id
         WHERE ti.strongs_number IN ({ph})
           AND COALESCE(wtrw.delete_flagged,0) = 0
         GROUP BY ti.strongs_number
    """, strongs_list).fetchall():
        out[r["strongs_number"]]["rel"] = r["c"]

    # Cross-refs — mti_term_cross_refs.mti_term_id → mti_terms
    for r in conn.execute(f"""
        SELECT mt.strongs_number, COUNT(DISTINCT mtcr.id) c
          FROM mti_terms mt
          JOIN mti_term_cross_refs mtcr ON mtcr.mti_term_id = mt.id
         WHERE mt.strongs_number IN ({ph})
         GROUP BY mt.strongs_number
    """, strongs_list).fetchall():
        out[r["strongs_number"]]["xref"] = r["c"]

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--version", default="auto",
        help="vN override; default 'auto' = scan dirs for highest vN, bump",
    )
    args = ap.parse_args()
    date = datetime.now().strftime("%Y%m%d")
    os.makedirs(WF_DIR, exist_ok=True)
    os.makedirs(SESSIONS_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Loading clusters...", flush=True)
    clusters = fetch_clusters(conn)
    print(f"  {len(clusters)} clusters")

    if args.version == "auto":
        scan_pairs = [(WF_DIR, "wa-cluster-overview")]
        for c in clusters:
            cid = c["cluster_code"]
            scan_pairs.append((
                os.path.join(SESSIONS_DIR, cid),
                f"wa-cluster-{cid}-detail",
            ))
        version = next_version_in_dirs(scan_pairs)
        print(f"  auto-version: {version} "
              f"(scanned overview + {len(clusters)} per-cluster dirs)")
    else:
        version = args.version
    args.version = version  # downstream code uses args.version

    print("Loading term metadata...", flush=True)
    term_meta, mti_to_strong = fetch_term_metadata(conn)
    print(f"  {len(term_meta)} distinct Strong's with cluster_code")

    # Collect all mti_ids for verse-coverage lookup
    all_mti_ids = set(mti_to_strong.keys())

    print("Computing verse coverage...", flush=True)
    coverage = fetch_verse_coverage(conn, all_mti_ids)
    print(f"  computed for {len(coverage)} mti_term_ids")

    print("Counting findings + pointers per term...", flush=True)
    strongs_set = set(term_meta.keys())
    fp_counts = fetch_finding_pointer_counts(
        conn, strongs_set, mti_to_strong, None
    )
    print(f"  findings_direct: "
          f"{sum(len(v) for v in fp_counts['findings_direct'].values())}")
    print(f"  findings_anchor: "
          f"{sum(len(v) for v in fp_counts['findings_anchor'].values())}")

    print("Counting root-family / related-words / cross-refs...", flush=True)
    aux = fetch_aux_counts(conn, list(strongs_set))

    # Aggregate per Strong's: combine coverage from all mti_ids for that
    # Strong's (since duplicates in mti_terms — same Strong's, multiple ids)
    print("Aggregating per-term records...", flush=True)
    per_strong = {}
    for s, m in term_meta.items():
        agg = {"active": 0, "analysed": 0, "set_aside": 0,
               "not_relevant": 0, "pending_in_vc": 0, "untouched": 0}
        for mid in m["_mti_ids"]:
            cov = coverage.get(mid, {})
            for k in agg:
                agg[k] += cov.get(k, 0)
        # If multiple mti_ids inflate counts, dedupe by using max where
        # appropriate. But simplest: take max across mti_ids per category.
        # Actually since the duplicates likely contain the same data, use
        # the MAX across mti_ids (not sum) — duplicate rows overlap.
        max_per_cat = {"active": 0, "analysed": 0, "set_aside": 0,
                       "not_relevant": 0, "pending_in_vc": 0,
                       "untouched": 0}
        for mid in m["_mti_ids"]:
            cov = coverage.get(mid, {})
            for k in max_per_cat:
                if cov.get(k, 0) > max_per_cat[k]:
                    max_per_cat[k] = cov.get(k, 0)
        cov = max_per_cat
        active = cov["active"]
        covered = cov["analysed"] + cov["set_aside"] + cov["not_relevant"]
        pending = cov["pending_in_vc"] + cov["untouched"]
        cov_pct = (covered / active * 100.0) if active else 100.0
        reg = m.get("reg_no")
        registry_label = f"R{reg:03d} {m['reg_word']}" if reg else "—"
        # finding/pointer counts
        n_fd = len(fp_counts["findings_direct"].get(s, set()))
        n_fa = len(fp_counts["findings_anchor"].get(s, set()))
        n_fr = (
            len(fp_counts["findings_registry"].get(m["owning_registry_fk"],
                                                   set()))
            if m.get("owning_registry_fk") else 0
        )
        n_pd = len(fp_counts["pointers_direct"].get(s, set()))
        n_pr = (
            len(fp_counts["pointers_registry"].get(m["owning_registry_fk"],
                                                   set()))
            if m.get("owning_registry_fk") else 0
        )
        per_strong[s] = {
            "strong": s,
            "transliteration": m.get("transliteration") or "",
            "gloss": m.get("gloss") or "",
            "language": m.get("language") or "",
            "owner_type": m.get("term_owner_type") or "",
            "evidential_status": m.get("evidential_status") or "",
            "occurrence_count": m.get("occurrence_count") or 0,
            "registry": registry_label,
            "legacy_c_cluster": m.get("legacy_c_cluster") or "",
            "cluster_code": m.get("cluster_code"),
            "mounce_short_def": m.get("mounce") or "",
            "meaning_text": m.get("inv_meaning") or "",
            "active": active,
            "analysed": cov["analysed"],
            "set_aside": cov["set_aside"],
            "not_relevant": cov["not_relevant"],
            "pending_in_vc": cov["pending_in_vc"],
            "untouched": cov["untouched"],
            "covered": covered,
            "pending": pending,
            "coverage_pct": cov_pct,
            "fully_covered": pending == 0 and active > 0,
            "no_verses": active == 0,
            "n_find_direct": n_fd,
            "n_find_anchor": n_fa,
            "n_find_registry": n_fr,
            "n_ptr_direct": n_pd,
            "n_ptr_registry": n_pr,
            "n_root_family": aux[s]["rf"],
            "n_related_words": aux[s]["rel"],
            "n_cross_refs": aux[s]["xref"],
        }

    # Group terms by cluster
    by_cluster = defaultdict(list)
    for s, t in per_strong.items():
        by_cluster[t["cluster_code"]].append(t)
    for cid in by_cluster:
        by_cluster[cid].sort(key=lambda x: -x["active"])

    # ---- Overview ----
    print("Building overview...", flush=True)
    overview_clusters = []
    for c in clusters:
        cid = c["cluster_code"]
        terms_here = by_cluster.get(cid, [])
        n_total = len(terms_here)
        n_full = sum(1 for t in terms_here if t["fully_covered"])
        n_zero = sum(1 for t in terms_here if t["no_verses"])
        n_pending = n_total - n_full - n_zero
        sum_active = sum(t["active"] for t in terms_here)
        sum_covered = sum(t["covered"] for t in terms_here)
        sum_untouched = sum(t["untouched"] for t in terms_here)
        cov_pct = (sum_covered / sum_active * 100.0) if sum_active else 0
        n_h = sum(1 for t in terms_here if t["language"] == "Hebrew")
        n_g = sum(1 for t in terms_here if t["language"] == "Greek")
        overview_clusters.append({
            "cluster_code": cid,
            "description": c["description"],
            "bucket": c["bucket"],
            "status": c["status"],
            "version": c["version"],
            "n_terms": n_total,
            "n_hebrew": n_h,
            "n_greek": n_g,
            "n_fully_covered": n_full,
            "n_zero_verses": n_zero,
            "n_with_pending": n_pending,
            "active_verses": sum_active,
            "covered_verses": sum_covered,
            "untouched_verses": sum_untouched,
            "coverage_pct": round(cov_pct, 1),
            "top_terms": [
                {"strong": t["strong"], "gloss": t["gloss"],
                 "active": t["active"]}
                for t in terms_here[:5]
            ],
        })

    overview_json = {
        "meta": {
            "generated": now_iso(),
            "version": args.version,
            "source": "database/bible_research.db",
            "total_clusters": len(clusters),
            "total_terms_with_cluster": len(per_strong),
        },
        "clusters": overview_clusters,
    }
    out_overview_json = os.path.join(
        WF_DIR, f"wa-cluster-overview-{args.version}-{date}.json"
    )
    with open(out_overview_json, "w", encoding="utf-8") as f:
        json.dump(overview_json, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {out_overview_json}")

    # ---- Overview MD ----
    lines = []
    lines.append(f"# Cluster overview — {args.version}\n")
    lines.append(f"**Generated:** {now_iso()}  ")
    lines.append(f"**Source:** `database/bible_research.db`  ")
    lines.append(f"**Companion:** see "
                 f"[Sessions/Session_Clusters/](../../Sessions/Session_Clusters/) "
                 "for per-cluster working folders.\n")
    lines.append(f"## Headline\n")
    total_terms = len(per_strong)
    total_active = sum(c["active_verses"] for c in overview_clusters)
    total_covered = sum(c["covered_verses"] for c in overview_clusters)
    total_untouched = sum(c["untouched_verses"] for c in overview_clusters)
    overall_pct = (total_covered/total_active*100) if total_active else 0
    lines.append(f"- **Clusters:** {len(clusters)} "
                 f"(45 NAMED + 1 SUPPLEMENTARY + 1 REVIEW)")
    lines.append(f"- **Distinct terms with cluster:** {total_terms:,}")
    lines.append(f"- **Active OWNER verses:** {total_active:,}")
    lines.append(f"- **Covered verses:** {total_covered:,} "
                 f"({overall_pct:.1f}%)")
    lines.append(f"- **Untouched verses:** {total_untouched:,}\n")

    lines.append("## All clusters — at-a-glance\n")
    lines.append("Sorted: NAMED clusters first by code, then SUPPLEMENTARY "
                 "(T2), then REVIEW (FLAG).\n")
    lines.append("| Code | Description | Status | Bucket | Terms (H/G) | "
                 "Active verses | Cov % | ✅ Full | ⚠ Pending | "
                 "Untouched | Detail |")
    lines.append("|---|---|---|---|---|---:|---:|---:|---:|---:|---|")
    for c in overview_clusters:
        detail_link = (f"[detail](../../Sessions/Session_Clusters/"
                       f"{c['cluster_code']}/wa-cluster-"
                       f"{c['cluster_code']}-detail-{args.version}-{date}.md)")
        terms_split = f"{c['n_terms']} ({c['n_hebrew']}/{c['n_greek']})"
        lines.append(
            f"| **{c['cluster_code']}** | {c['description']} | "
            f"{c['status']} | {c['bucket']} | {terms_split} | "
            f"{c['active_verses']:,} | {c['coverage_pct']:.0f}% | "
            f"{c['n_fully_covered']} | {c['n_with_pending']} | "
            f"{c['untouched_verses']} | {detail_link} |"
        )
    lines.append("")

    out_overview_md = os.path.join(
        WF_DIR, f"wa-cluster-overview-{args.version}-{date}.md"
    )
    with open(out_overview_md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {out_overview_md}")

    # ---- Per-cluster MDs ----
    print("Building per-cluster detail files...", flush=True)
    for c in clusters:
        cid = c["cluster_code"]
        terms_here = by_cluster.get(cid, [])
        n_terms = len(terms_here)
        n_full = sum(1 for t in terms_here if t["fully_covered"])
        n_zero = sum(1 for t in terms_here if t["no_verses"])
        n_pending = n_terms - n_full - n_zero
        sum_active = sum(t["active"] for t in terms_here)
        sum_covered = sum(t["covered"] for t in terms_here)
        sum_pending = sum(t["pending"] for t in terms_here)
        cov_pct = (sum_covered / sum_active * 100.0) if sum_active else 0

        lines = []
        lines.append(f"# {cid} — {c['description']}\n")
        lines.append(f"**Generated:** {now_iso()}  ")
        lines.append(f"**Cluster:** `{cid}`  ")
        lines.append(f"**Bucket:** {c['bucket']}  ")
        lines.append(f"**Status:** {c['status']}  ")
        lines.append(f"**Version:** {c['version']}  ")
        lines.append(f"**Last updated:** {c['last_updated_date']}\n")

        lines.append("## Cluster summary\n")
        lines.append(f"- Terms: **{n_terms}** "
                     f"({sum(1 for t in terms_here if t['language']=='Hebrew')} H / "
                     f"{sum(1 for t in terms_here if t['language']=='Greek')} G)")
        lines.append(f"- Active OWNER verses: **{sum_active:,}**")
        lines.append(f"- Coverage: **{sum_covered:,}** ({cov_pct:.1f}%)")
        lines.append(f"- Pending: {sum_pending:,}")
        lines.append(f"- Fully covered terms: {n_full} / {n_terms}")
        lines.append(f"- Zero-verse terms: {n_zero}")
        lines.append(f"- Terms with pending verses: {n_pending}\n")

        if not terms_here:
            lines.append("\n*(no terms in this cluster)*\n")
        else:
            # Compact table (full info per term inline)
            lines.append("## Term coverage table\n")
            lines.append("Sorted by active verse count descending. ✅ = fully "
                         "covered, ⚠ = has pending verses, — = no active "
                         "verses.\n")
            lines.append("**Columns:** Active = active OWNER verses; A/SA/NR/PV/UT = "
                         "analysed/set-aside/not-relevant/pending-in-VC/untouched; "
                         "Cov% = coverage percent; Find D/V/R = findings via "
                         "direct mention / via anchor verse / via registry; "
                         "Ptr D/R = pointers direct / via registry.\n")
            lines.append("| ✓ | Strong's | Lang | Translit | Gloss | Owner | "
                         "Registry | Legacy C | Active | A | SA | NR | PV | "
                         "UT | Cov% | Find D | Find V | Find R | Ptr D | "
                         "Ptr R | RF | Rel | XRef |")
            lines.append("|---|---|---|---|---|---|---|---|---:|---:|---:|"
                         "---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
                         "---:|---:|")
            for t in terms_here:
                mark = ("✅" if t["fully_covered"]
                        else ("—" if t["no_verses"] else "⚠"))
                lang = t["language"][:1] if t["language"] else ""
                lines.append(
                    f"| {mark} | {t['strong']} | {lang} | "
                    f"{t['transliteration']} | {t['gloss']} | "
                    f"{t['owner_type'] or '—'} | "
                    f"{t['registry']} | {t['legacy_c_cluster'] or '—'} | "
                    f"{t['active']} | {t['analysed']} | "
                    f"{t['set_aside']} | {t['not_relevant']} | "
                    f"{t['pending_in_vc']} | {t['untouched']} | "
                    f"{t['coverage_pct']:.0f}% | "
                    f"{t['n_find_direct']} | {t['n_find_anchor']} | "
                    f"{t['n_find_registry']} | "
                    f"{t['n_ptr_direct']} | {t['n_ptr_registry']} | "
                    f"{t['n_root_family']} | {t['n_related_words']} | "
                    f"{t['n_cross_refs']} |"
                )
            lines.append("")

            # Per-term meaning panel
            lines.append("\n## Per-term meaning detail\n")
            lines.append("Mounce short-def + parsed meaning text per term "
                         "(truncated where lengthy).\n")
            for t in terms_here:
                lines.append(f"### {t['strong']} {t['transliteration']} — "
                             f"{t['gloss']}")
                lines.append(f"_lang: {t['language']} · "
                             f"registry: {t['registry']} · "
                             f"owner: {t['owner_type'] or '—'} · "
                             f"evidential: {t['evidential_status'] or '—'} · "
                             f"occurrence_count: {t['occurrence_count']}_  ")
                if t["mounce_short_def"]:
                    lines.append(f"**Mounce short-def:** "
                                 f"{t['mounce_short_def']}  ")
                if t["meaning_text"]:
                    meaning = t["meaning_text"]
                    if len(meaning) > 600:
                        meaning = meaning[:600] + "…"
                    lines.append(f"**Meaning:** {meaning}")
                lines.append("")

        cluster_dir = os.path.join(SESSIONS_DIR, cid)
        os.makedirs(cluster_dir, exist_ok=True)
        out_path = os.path.join(
            cluster_dir,
            f"wa-cluster-{cid}-detail-{args.version}-{date}.md"
        )
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    print(f"Wrote: {len(clusters)} per-cluster files into "
          f"{SESSIONS_DIR}/<cluster>/")

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
