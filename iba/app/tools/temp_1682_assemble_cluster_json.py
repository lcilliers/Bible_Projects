"""
temp_1682_assemble_cluster_json.py

Process (a) of the escalation #1682 cluster-reading spec
(iba/docs/1682-cluster-reading-process-spec-v1-20260911.md): deterministic assembly of the base
JSON for a cluster -- occurrence-level span/verse data plus 3-source-consolidated meaning, per
strong. No LLM involved; this is a one-off test script (governance.scripts_and_routines temp_
convention) pending approval of the spec, at which point it would be registered in cfg_utility
(and cfg_step/cfg_write_grant if it starts writing).

Usage:
    python iba/app/tools/temp_1682_assemble_cluster_json.py --cluster M10 --out <path>
"""
import argparse
import json
import sqlite3
import sys


def build(conn: sqlite3.Connection, cluster_code: str) -> dict:
    conn.row_factory = sqlite3.Row

    strongs = [r["strong"] for r in conn.execute(
        "SELECT strong FROM cluster_strong WHERE cluster_code = ? GROUP BY strong ORDER BY strong",
        (cluster_code,),
    )]
    if not strongs:
        raise SystemExit(f"No cluster_strong rows found for cluster_code={cluster_code!r}")

    placeholders = ",".join("?" * len(strongs))

    gloss_rows = conn.execute(
        f"SELECT strongNumber, stepGloss, language FROM strong WHERE strongNumber IN ({placeholders})",
        strongs,
    )
    gloss = {r["strongNumber"]: {"stepGloss": r["stepGloss"], "language": r["language"]} for r in gloss_rows}

    occ_rows = conn.execute(
        f"""
        SELECT sp.strong_variant AS strong, v.osisId, v.reference, v.text AS verse_text,
               sp.surface AS span_surface, sp.morph_code AS span_morph, sp.position
        FROM span sp
        JOIN verse v ON v.id = sp.verse_id
        WHERE sp.strong_variant IN ({placeholders}) AND sp.deleted = 0 AND v.deleted = 0
        ORDER BY sp.strong_variant, v.id, sp.position
        """,
        strongs,
    )
    occurrences_by_strong: dict[str, list] = {s: [] for s in strongs}
    for r in occ_rows:
        occurrences_by_strong[r["strong"]].append({
            "osisId": r["osisId"],
            "reference": r["reference"],
            "verse_text": r["verse_text"],
            "span_surface": r["span_surface"],
            "span_morph": r["span_morph"],
        })

    meaning_rows = conn.execute(
        f"""
        SELECT strong, source, sense_code, raw_text, ord
        FROM vw_strong_meaning_raw
        WHERE strong IN ({placeholders})
        ORDER BY strong, source, ord
        """,
        strongs,
    )
    # consolidate strong_meaning_tree's multiple sense-coded rows into one text block per strong;
    # lsj/mounce are already single-row per strong in the view.
    meaning_by_strong: dict[str, dict[str, list[str]]] = {s: {} for s in strongs}
    for r in meaning_rows:
        bucket = meaning_by_strong[r["strong"]].setdefault(r["source"], [])
        prefix = f"{r['sense_code']}) " if r["sense_code"] else ""
        bucket.append(f"{prefix}{r['raw_text']}")

    out = {"cluster_code": cluster_code, "process": "1682-cluster-reading-process-a", "strongs": []}
    for s in strongs:
        meaning = []
        for source in ("strong_meaning_tree", "strong_lexicon.lsj", "strong_lexicon.mounce"):
            parts = meaning_by_strong[s].get(source)
            if parts:
                meaning.append({"source": source, "text": "; ".join(parts)})
        out["strongs"].append({
            "strong": s,
            "stepGloss": gloss.get(s, {}).get("stepGloss"),
            "language": gloss.get(s, {}).get("language"),
            "occurrence_count": len(occurrences_by_strong[s]),
            "occurrences": occurrences_by_strong[s],
            "meaning": meaning,
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--db", default="iba/app/db/iba.db")
    args = ap.parse_args()

    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    data = build(conn, args.cluster)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total_occ = sum(s["occurrence_count"] for s in data["strongs"])
    print(f"cluster={args.cluster} strongs={len(data['strongs'])} total_occurrences={total_occ} -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
