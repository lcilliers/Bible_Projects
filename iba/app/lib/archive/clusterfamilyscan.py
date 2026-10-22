"""clusterfamilyscan.py — escalation #1598: a mechanically-grounded alternative to gloss-keyword
matching for finding cluster-reallocation candidates.

Researcher, verbatim, prompting this: "its obvious we need to scan this list with our new tools
that we have." Gloss-keyword matching (used throughout #1598's earlier phases) has a demonstrated
~20% false-positive rate from English homonym collisions ("testify"/"test", "hold fast"/fasting,
"lie down"/"to lie"). This module uses `strong_related` (STEP's own lexical-family data, already in
the schema — L2b in the schema notes) instead: for every strong already tagged to a cluster, pull
its related-word family and check which related codes are STILL sitting in the untagged pool. A
code showing up related to an existing `M18` member is a much better-grounded candidate for `M18`
than one merely sharing an English gloss word.

**Not a bulk-apply mechanism — a candidate-generation aid, still requiring individual review.**
Tested live against M18/T7/T13: the raw method has its own real false-positive source — compound-
morphology and theophoric-name relations pull in proper nouns riding along on a shared root (Greek
"Timothy"/"Simon"/"Christian" surfacing as "related to God/Jesus/Zealot"; Hebrew "Adonijah"/
"Adoniram"/"Adam"/"Admah" surfacing via "lord"/"soil"). Filtering those out (via the same proper-
noun morph-code check used throughout #1598) cuts the raw candidate count roughly in half (2,700 ->
1,273 in the live test) but does not eliminate every false positive — genuine coincidental-root
relations still occur (e.g. "according to" surfacing as related to "desire" via an unrelated STEP
link). Every candidate this produces still needs the same gloss-read + verse-check discipline
already applied throughout this escalation before being added to a cluster.

    python -m iba.app.lib.clusterfamilyscan                  # full scan, all clusters
    python -m iba.app.lib.clusterfamilyscan --cluster M18     # one cluster only
"""

from __future__ import annotations

import argparse
import collections
import sqlite3

from .cfg import DB_PATH


def get_untagged_pool(conn: sqlite3.Connection) -> set[str]:
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        WITH tagged AS (SELECT DISTINCT strong FROM cluster_strong WHERE deleted=0),
        live_content AS (SELECT DISTINCT strong FROM verse_lexical WHERE deleted=0 AND role='content')
        SELECT lc.strong FROM live_content lc LEFT JOIN tagged t ON t.strong=lc.strong
        WHERE t.strong IS NULL
    """).fetchall()
    return {r["strong"] for r in rows}


def is_proper_noun(conn: sqlite3.Connection, strong: str) -> bool:
    row = conn.execute(
        "SELECT morph_code FROM verse_lexical WHERE strong=? AND deleted=0 "
        "GROUP BY morph_code ORDER BY COUNT(*) DESC LIMIT 1", (strong,)).fetchone()
    m = row["morph_code"] if row and row["morph_code"] else ""
    if strong.startswith("H") or strong.startswith("A"):
        return m[:2] in ("HN", "AN") and m[2:3] == "p"
    if strong.startswith("G"):
        return "PRI" in m
    return False


def scan(conn: sqlite3.Connection, cluster_codes: list[str] | None = None,
        exclude_proper_nouns: bool = True) -> dict[str, list[dict]]:
    """Returns {cluster_code: [{"candidate": strong, "via": strong, "via_gloss": str,
    "related_gloss": str, "occurrences": int}, ...]} for every candidate still untagged."""
    untagged = get_untagged_pool(conn)
    if cluster_codes is None:
        cluster_codes = [r["cluster_code"] for r in conn.execute(
            "SELECT cluster_code FROM cluster WHERE deleted=0 "
            "AND cluster_code NOT IN ('T2','T3','FLAG')")]

    results: dict[str, list[dict]] = {}
    for code in cluster_codes:
        members = [r["strong"] for r in conn.execute(
            "SELECT DISTINCT strong FROM cluster_strong WHERE cluster_code=? AND deleted=0",
            (code,))]
        if not members:
            continue
        ph = ",".join("?" * len(members))
        rels = conn.execute(
            f"SELECT strong, related_strong, related_gloss FROM strong_related "
            f"WHERE strong IN ({ph}) AND deleted=0", members).fetchall()
        seen: set[str] = set()
        items = []
        for r in rels:
            cand = r["related_strong"]
            if cand not in untagged or cand in seen:
                continue
            if exclude_proper_nouns and is_proper_noun(conn, cand):
                continue
            seen.add(cand)
            via_gloss = conn.execute(
                "SELECT stepGloss FROM strong WHERE strongNumber=?", (r["strong"],)).fetchone()
            own_gloss = conn.execute(
                "SELECT stepGloss FROM strong WHERE strongNumber=?", (cand,)).fetchone()
            occ = conn.execute(
                "SELECT COUNT(*) c FROM verse_lexical WHERE strong=? AND deleted=0",
                (cand,)).fetchone()["c"]
            items.append({
                "candidate": cand,
                "candidate_gloss": own_gloss["stepGloss"] if own_gloss else None,
                "via": r["strong"],
                "via_gloss": via_gloss["stepGloss"] if via_gloss else None,
                "related_gloss": r["related_gloss"],
                "occurrences": occ,
            })
        if items:
            items.sort(key=lambda x: -x["occurrences"])
            results[code] = items
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cluster", help="Scan one cluster_code only")
    parser.add_argument("--include-proper-nouns", action="store_true")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    codes = [args.cluster] if args.cluster else None
    results = scan(conn, codes, exclude_proper_nouns=not args.include_proper_nouns)
    conn.close()

    total = sum(len(v) for v in results.values())
    print(f"clusterfamilyscan: {total} candidates across {len(results)} clusters")
    for code, items in sorted(results.items(), key=lambda x: -len(x[1])):
        print(f"\n{code}: {len(items)} candidates")
        for it in items[:10]:
            print(f"  {it['candidate']} '{it['candidate_gloss']}' (occ={it['occurrences']}) "
                  f"<- via {it['via']} '{it['via_gloss']}'")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
