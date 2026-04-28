"""
build_correlation_extract.py
────────────────────────────
Automated inter-word correlation analysis.

Mines five structural signals from the database to identify word pairs
and clusters that warrant Session D investigation:

  1. XREF term sharing — words connected by shared Strong's numbers
  2. Verse co-occurrence — OWNER terms appearing in the same verse
  3. Dimension profile similarity — words with overlapping dimension distributions
  4. Root family connections — words sharing etymological roots
  5. Shared anchor verses — different words both anchoring on the same verse

Output: Sessions/Session_D/session_d/wa-correlations-{date}.json

Usage:
  python scripts/build_correlation_extract.py
  python scripts/build_correlation_extract.py --min-xref=3 --min-cooccur=5
"""

import argparse
import json
import os
import sqlite3
from collections import defaultdict
from datetime import date, datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "bible_research.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "exports", "session_d")


def build_correlations(conn, min_xref=3, min_cooccur=5, min_dim_overlap=2) -> dict:
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Registry lookup
    reg_map = {}
    for r in conn.execute(
        "SELECT no, word, cluster_assignment FROM word_registry"
    ):
        reg_map[r[0]] = {"word": r[1], "cluster": r[2]}

    # ── Signal 1: XREF Term Sharing ──────────────────────────────────────────

    xref_pairs = []
    for r in conn.execute("""
        SELECT w1.no as reg1, w1.word as word1, w1.cluster_assignment as c1,
               w2.no as reg2, w2.word as word2, w2.cluster_assignment as c2,
               COUNT(DISTINCT a.strongs_number) as shared_terms,
               GROUP_CONCAT(DISTINCT a.strongs_number) as shared_strongs
        FROM wa_term_inventory a
        JOIN wa_term_inventory b ON a.strongs_number = b.strongs_number
            AND a.file_id < b.file_id
            AND a.delete_flagged = 0 AND b.delete_flagged = 0
        JOIN wa_file_index fi1 ON fi1.id = a.file_id
        JOIN wa_file_index fi2 ON fi2.id = b.file_id
        JOIN word_registry w1 ON w1.id = fi1.word_registry_fk
        JOIN word_registry w2 ON w2.id = fi2.word_registry_fk
        GROUP BY w1.no, w2.no
        HAVING shared_terms >= ?
        ORDER BY shared_terms DESC
    """, (min_xref,)):
        xref_pairs.append({
            "reg1": r[0], "word1": r[1], "cluster1": r[2],
            "reg2": r[3], "word2": r[4], "cluster2": r[5],
            "shared_term_count": r[6],
            "shared_strongs": r[7].split(",") if r[7] else [],
            "cross_cluster": r[2] != r[5],
        })

    # ── Signal 2: Verse Co-occurrence (OWNER terms only) ─────────────────────

    cooccur_pairs = []
    for r in conn.execute("""
        SELECT w1.no as reg1, w1.word as word1, w1.cluster_assignment as c1,
               w2.no as reg2, w2.word as word2, w2.cluster_assignment as c2,
               COUNT(DISTINCT vr1.reference) as shared_verses
        FROM wa_verse_records vr1
        JOIN wa_term_inventory ti1 ON ti1.id = vr1.term_inv_id
            AND ti1.delete_flagged = 0 AND ti1.term_owner_type = 'OWNER'
        JOIN wa_file_index fi1 ON fi1.id = ti1.file_id
        JOIN word_registry w1 ON w1.id = fi1.word_registry_fk
        JOIN wa_verse_records vr2 ON vr1.reference = vr2.reference
            AND vr1.id != vr2.id AND vr2.delete_flagged = 0
        JOIN wa_term_inventory ti2 ON ti2.id = vr2.term_inv_id
            AND ti2.delete_flagged = 0 AND ti2.term_owner_type = 'OWNER'
        JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
        JOIN word_registry w2 ON w2.id = fi2.word_registry_fk AND w1.no < w2.no
        GROUP BY w1.no, w2.no
        HAVING shared_verses >= ?
        ORDER BY shared_verses DESC
    """, (min_cooccur,)):
        cooccur_pairs.append({
            "reg1": r[0], "word1": r[1], "cluster1": r[2],
            "reg2": r[3], "word2": r[4], "cluster2": r[5],
            "shared_verse_count": r[6],
            "cross_cluster": r[2] != r[5],
        })

    # ── Signal 3: Dimension Profile Similarity ───────────────────────────────

    # Build per-registry dimension vectors (CLAUDE_AI reviewed only)
    dim_profiles: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for r in conn.execute("""
        SELECT owning_registry_no, dimension, COUNT(*) as cnt
        FROM wa_dimension_index
        WHERE dimension_confidence = 'CLAUDE_AI' AND delete_flagged = 0
            AND dimension IS NOT NULL
        GROUP BY owning_registry_no, dimension
    """):
        dim_profiles[r[0]][r[1]] = r[2]

    dim_pairs = []
    regs_with_dims = sorted(dim_profiles.keys())
    for i, r1 in enumerate(regs_with_dims):
        for r2 in regs_with_dims[i + 1:]:
            shared_dims = set(dim_profiles[r1].keys()) & set(dim_profiles[r2].keys())
            if len(shared_dims) >= min_dim_overlap:
                overlap = []
                for d in sorted(shared_dims):
                    overlap.append({
                        "dimension": d,
                        "count_reg1": dim_profiles[r1][d],
                        "count_reg2": dim_profiles[r2][d],
                    })
                dim_pairs.append({
                    "reg1": r1, "word1": reg_map.get(r1, {}).get("word", "?"),
                    "cluster1": reg_map.get(r1, {}).get("cluster", "?"),
                    "reg2": r2, "word2": reg_map.get(r2, {}).get("word", "?"),
                    "cluster2": reg_map.get(r2, {}).get("cluster", "?"),
                    "shared_dimension_count": len(shared_dims),
                    "overlap": overlap,
                })
    dim_pairs.sort(key=lambda x: x["shared_dimension_count"], reverse=True)

    # ── Signal 4: Root Family Connections ────────────────────────────────────

    root_families = []
    for r in conn.execute("""
        SELECT rf.root_code, rf.root_gloss,
               COUNT(DISTINCT wr.no) as reg_count,
               GROUP_CONCAT(DISTINCT wr.no) as reg_nos,
               GROUP_CONCAT(DISTINCT wr.word) as words,
               GROUP_CONCAT(DISTINCT wr.cluster_assignment) as clusters
        FROM wa_term_root_family rf
        JOIN wa_term_inventory ti ON ti.id = rf.term_inv_id AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        GROUP BY rf.root_code
        HAVING reg_count >= 2
        ORDER BY reg_count DESC
    """):
        clusters = r[5].split(",") if r[5] else []
        root_families.append({
            "root_code": r[0],
            "root_gloss": r[1],
            "registry_count": r[2],
            "registry_nos": [int(x) for x in r[3].split(",")] if r[3] else [],
            "words": r[4].split(",") if r[4] else [],
            "clusters": clusters,
            "cross_cluster": len(set(clusters)) > 1,
        })

    # ── Signal 5: Shared Anchor Verses ───────────────────────────────────────

    anchor_overlaps = []
    for r in conn.execute("""
        SELECT vr1.reference,
               w1.no as reg1, w1.word as word1, w1.cluster_assignment as c1,
               vcg1.group_code as group1,
               w2.no as reg2, w2.word as word2, w2.cluster_assignment as c2,
               vcg2.group_code as group2
        FROM verse_context vc1
        JOIN wa_verse_records vr1 ON vr1.id = vc1.verse_record_id
        JOIN wa_term_inventory ti1 ON ti1.id = vr1.term_inv_id AND ti1.term_owner_type = 'OWNER'
        JOIN wa_file_index fi1 ON fi1.id = ti1.file_id
        JOIN word_registry w1 ON w1.id = fi1.word_registry_fk
        JOIN verse_context_group vcg1 ON vcg1.id = vc1.group_id
        JOIN verse_context vc2 ON vc1.verse_record_id != vc2.verse_record_id
        JOIN wa_verse_records vr2 ON vr2.id = vc2.verse_record_id
            AND vr2.reference = vr1.reference AND vr2.id != vr1.id
        JOIN wa_term_inventory ti2 ON ti2.id = vr2.term_inv_id AND ti2.term_owner_type = 'OWNER'
        JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
        JOIN word_registry w2 ON w2.id = fi2.word_registry_fk AND w1.no < w2.no
        JOIN verse_context_group vcg2 ON vcg2.id = vc2.group_id
        WHERE vc1.is_anchor = 1 AND vc2.is_anchor = 1
            AND vc1.delete_flagged = 0 AND vc2.delete_flagged = 0
        GROUP BY vr1.reference, w1.no, w2.no
        ORDER BY vr1.reference
    """):
        anchor_overlaps.append({
            "reference": r[0],
            "reg1": r[1], "word1": r[2], "cluster1": r[3], "group1": r[4],
            "reg2": r[5], "word2": r[6], "cluster2": r[7], "group2": r[8],
            "cross_cluster": r[3] != r[7],
        })

    # ── Composite Scoring ────────────────────────────────────────────────────

    # Build a pair-level score combining all signals
    pair_scores: dict[tuple, dict] = {}
    for p in xref_pairs:
        key = (min(p["reg1"], p["reg2"]), max(p["reg1"], p["reg2"]))
        if key not in pair_scores:
            pair_scores[key] = {
                "reg1": key[0], "word1": reg_map.get(key[0], {}).get("word", "?"),
                "reg2": key[1], "word2": reg_map.get(key[1], {}).get("word", "?"),
                "xref_shared": 0, "verse_cooccur": 0, "dim_overlap": 0,
                "root_shared": 0, "anchor_shared": 0, "signals": [],
            }
        pair_scores[key]["xref_shared"] = p["shared_term_count"]
        pair_scores[key]["signals"].append("xref")

    for p in cooccur_pairs:
        key = (min(p["reg1"], p["reg2"]), max(p["reg1"], p["reg2"]))
        if key not in pair_scores:
            pair_scores[key] = {
                "reg1": key[0], "word1": reg_map.get(key[0], {}).get("word", "?"),
                "reg2": key[1], "word2": reg_map.get(key[1], {}).get("word", "?"),
                "xref_shared": 0, "verse_cooccur": 0, "dim_overlap": 0,
                "root_shared": 0, "anchor_shared": 0, "signals": [],
            }
        pair_scores[key]["verse_cooccur"] = p["shared_verse_count"]
        if "cooccur" not in pair_scores[key]["signals"]:
            pair_scores[key]["signals"].append("cooccur")

    for p in dim_pairs:
        key = (min(p["reg1"], p["reg2"]), max(p["reg1"], p["reg2"]))
        if key not in pair_scores:
            pair_scores[key] = {
                "reg1": key[0], "word1": reg_map.get(key[0], {}).get("word", "?"),
                "reg2": key[1], "word2": reg_map.get(key[1], {}).get("word", "?"),
                "xref_shared": 0, "verse_cooccur": 0, "dim_overlap": 0,
                "root_shared": 0, "anchor_shared": 0, "signals": [],
            }
        pair_scores[key]["dim_overlap"] = p["shared_dimension_count"]
        if "dimension" not in pair_scores[key]["signals"]:
            pair_scores[key]["signals"].append("dimension")

    for a in anchor_overlaps:
        key = (min(a["reg1"], a["reg2"]), max(a["reg1"], a["reg2"]))
        if key not in pair_scores:
            pair_scores[key] = {
                "reg1": key[0], "word1": reg_map.get(key[0], {}).get("word", "?"),
                "reg2": key[1], "word2": reg_map.get(key[1], {}).get("word", "?"),
                "xref_shared": 0, "verse_cooccur": 0, "dim_overlap": 0,
                "root_shared": 0, "anchor_shared": 0, "signals": [],
            }
        pair_scores[key]["anchor_shared"] += 1
        if "anchor" not in pair_scores[key]["signals"]:
            pair_scores[key]["signals"].append("anchor")

    # Root family — count shared roots per pair
    for rf in root_families:
        regs = rf["registry_nos"]
        for i, r1 in enumerate(regs):
            for r2 in regs[i + 1:]:
                key = (min(r1, r2), max(r1, r2))
                if key not in pair_scores:
                    pair_scores[key] = {
                        "reg1": key[0], "word1": reg_map.get(key[0], {}).get("word", "?"),
                        "reg2": key[1], "word2": reg_map.get(key[1], {}).get("word", "?"),
                        "xref_shared": 0, "verse_cooccur": 0, "dim_overlap": 0,
                        "root_shared": 0, "anchor_shared": 0, "signals": [],
                    }
                pair_scores[key]["root_shared"] += 1
                if "root" not in pair_scores[key]["signals"]:
                    pair_scores[key]["signals"].append("root")

    # Score = weighted signal count
    for ps in pair_scores.values():
        ps["signal_count"] = len(ps["signals"])
        ps["composite_score"] = (
            min(ps["xref_shared"], 50) * 2
            + min(ps["verse_cooccur"], 200) * 0.5
            + ps["dim_overlap"] * 10
            + ps["root_shared"] * 15
            + ps["anchor_shared"] * 20
        )

    ranked_pairs = sorted(pair_scores.values(), key=lambda x: x["composite_score"], reverse=True)

    # ── Statistics ───────────────────────────────────────────────────────────

    stats = {
        "xref_pairs_above_threshold": len(xref_pairs),
        "cooccurrence_pairs_above_threshold": len(cooccur_pairs),
        "dimension_overlap_pairs": len(dim_pairs),
        "root_family_connections": len(root_families),
        "shared_anchor_verses": len(anchor_overlaps),
        "total_composite_pairs": len(ranked_pairs),
        "multi_signal_pairs": sum(1 for p in ranked_pairs if p["signal_count"] >= 3),
        "thresholds": {
            "min_xref": min_xref,
            "min_cooccur": min_cooccur,
            "min_dim_overlap": min_dim_overlap,
        },
    }

    return {
        "_extract_meta": {
            "extract_type": "inter_word_correlations",
            "produced_date": date.today().isoformat(),
            "produced_at": now_utc,
            "produced_by": "Claude Code — build_correlation_extract.py",
            "description": "Automated inter-word correlation analysis from five structural signals",
        },
        "statistics": stats,
        "ranked_pairs": ranked_pairs[:200],
        "signals": {
            "xref_sharing": xref_pairs,
            "verse_cooccurrence": cooccur_pairs[:100],
            "dimension_overlap": dim_pairs,
            "root_families": root_families,
            "shared_anchor_verses": anchor_overlaps,
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Build automated inter-word correlation extract")
    parser.add_argument("--min-xref", type=int, default=3,
                        help="Minimum shared XREF terms (default: 3)")
    parser.add_argument("--min-cooccur", type=int, default=5,
                        help="Minimum shared verses for co-occurrence (default: 5)")
    parser.add_argument("--min-dim-overlap", type=int, default=2,
                        help="Minimum shared dimensions (default: 2)")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    print("Building inter-word correlations...")
    data = build_correlations(conn, args.min_xref, args.min_cooccur, args.min_dim_overlap)
    conn.close()

    os.makedirs(OUT_DIR, exist_ok=True)
    today = date.today().isoformat()
    out_path = os.path.join(OUT_DIR, f"wa-correlations-{today}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    fsize = os.path.getsize(out_path)
    stats = data["statistics"]
    print(f"Written: {out_path}")
    print(f"Size: {fsize / 1024:.0f} KB")
    print(f"XREF pairs (>={args.min_xref} shared): {stats['xref_pairs_above_threshold']}")
    print(f"Verse co-occurrence pairs (>={args.min_cooccur}): {stats['cooccurrence_pairs_above_threshold']}")
    print(f"Dimension overlap pairs: {stats['dimension_overlap_pairs']}")
    print(f"Root family connections (2+ registries): {stats['root_family_connections']}")
    print(f"Shared anchor verses: {stats['shared_anchor_verses']}")
    print(f"Total composite pairs: {stats['total_composite_pairs']}")
    print(f"Multi-signal pairs (3+ signals): {stats['multi_signal_pairs']}")


if __name__ == "__main__":
    main()
