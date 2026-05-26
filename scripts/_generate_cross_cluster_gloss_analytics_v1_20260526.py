"""Cross-cluster gloss analytics.

Surfaces glosses that appear in multiple clusters — the diagnostic for
"characteristic-legs scattered across clusters" diagnosed during M11 review
(2026-05-26). Reports four lenses:

  §1  Exact gloss collisions: identical gloss strings appearing on terms
      in 2+ clusters
  §2  Gloss-base collisions: strip the colon-qualifier ('to hear: welcome'
      → 'to hear') and group; bases that span 2+ clusters
  §3  Token collisions: split glosses into tokens, find tokens (excluding
      stop-words) that appear in 2+ clusters' gloss vocabulary
  §4  Sister-Strong's spread: Strong's with the same numeric root but
      different sense-suffix letters (H2930A, H2930B, etc.) and whether
      they sit in the same or different clusters

T2 cluster excluded throughout (supplementary, not a primary cluster).

Output: Workflow/Clusters/wa-cross-cluster-gloss-analytics-v1-{date}.md
"""
from __future__ import annotations
import io
import re
import sqlite3
import sys
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
OUT_DIR = REPO / "Workflow" / "Clusters"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
TODAY = datetime.now(timezone.utc).strftime("%Y%m%d")

STOPWORDS = {
    "to", "a", "an", "the", "of", "in", "on", "at", "by", "with", "from",
    "as", "be", "is", "it", "or", "and", "for", "into",
}


def normalize_token(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", t.lower())


def gloss_base(gloss: str) -> str:
    """Strip colon-qualifier — 'to hear: welcome' -> 'to hear'."""
    return gloss.split(":", 1)[0].strip().lower()


def gloss_tokens(gloss: str) -> list[str]:
    """Split gloss into normalized non-stop tokens."""
    parts = re.split(r"[\s:,/()-]+", gloss.lower())
    out = []
    for p in parts:
        n = normalize_token(p)
        if n and n not in STOPWORDS and len(n) > 1:
            out.append(n)
    return out


def main() -> int:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        "SELECT id, strongs_number, transliteration, gloss, cluster_code, language "
        "FROM mti_terms "
        "WHERE cluster_code IS NOT NULL AND cluster_code != 'T2' "
        "  AND COALESCE(delete_flagged, 0) = 0 "
        "  AND gloss IS NOT NULL AND TRIM(gloss) != '' "
        "ORDER BY cluster_code, strongs_number"
    ).fetchall()
    total_terms = len(rows)
    cluster_codes = sorted({r["cluster_code"] for r in rows})

    cluster_meta = {r["cluster_code"]: r["description"] for r in conn.execute(
        "SELECT cluster_code, description FROM cluster"
    ).fetchall()}

    # §1 Exact gloss collisions
    exact_map: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        g = r["gloss"].strip()
        exact_map[g].append({
            "strongs": r["strongs_number"],
            "translit": r["transliteration"],
            "cluster": r["cluster_code"],
            "lang": r["language"],
        })
    exact_collisions = {g: terms for g, terms in exact_map.items()
                        if len({t["cluster"] for t in terms}) > 1}

    # §2 Gloss-base collisions
    base_map: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        b = gloss_base(r["gloss"])
        base_map[b].append({
            "strongs": r["strongs_number"],
            "translit": r["transliteration"],
            "cluster": r["cluster_code"],
            "lang": r["language"],
            "full_gloss": r["gloss"].strip(),
        })
    base_collisions = {b: terms for b, terms in base_map.items()
                       if len({t["cluster"] for t in terms}) > 1}

    # §3 Token collisions
    token_cluster_terms: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for r in rows:
        for tok in gloss_tokens(r["gloss"]):
            token_cluster_terms[tok][r["cluster_code"]].append({
                "strongs": r["strongs_number"],
                "translit": r["transliteration"],
                "full_gloss": r["gloss"].strip(),
            })
    # Keep tokens that span 2+ clusters
    token_collisions: list[tuple[str, int, int, dict[str, list[dict]]]] = []
    for tok, by_cluster in token_cluster_terms.items():
        if len(by_cluster) >= 2:
            n_terms = sum(len(v) for v in by_cluster.values())
            token_collisions.append((tok, len(by_cluster), n_terms, by_cluster))
    token_collisions.sort(key=lambda x: (-x[1], -x[2], x[0]))

    # §4 Sister-Strong's sense-suffix spread
    # Group by base Strong's (strip trailing letter), e.g. H2930A -> H2930
    strongs_groups: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        s = r["strongs_number"]
        m = re.match(r"^([HG]\d+)([A-Z]+)$", s)
        if m:
            base = m.group(1)
            strongs_groups[base].append({
                "strongs": s,
                "translit": r["transliteration"],
                "gloss": r["gloss"].strip(),
                "cluster": r["cluster_code"],
            })
    cross_cluster_strongs = {b: senses for b, senses in strongs_groups.items()
                              if len(senses) >= 2 and len({t["cluster"] for t in senses}) >= 2}

    # ============================================================
    # Build report
    # ============================================================
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"wa-cross-cluster-gloss-analytics-v1-{TODAY}.md"

    L: list[str] = []
    L.append("# Cross-cluster gloss analytics")
    L.append("")
    L.append(f"_Generated: {NOW}_  ")
    L.append(f"_Source: `database/bible_research.db` — `mti_terms.gloss`_  ")
    L.append(f"_Scope: {total_terms} non-T2 active terms across {len(cluster_codes)} clusters_")
    L.append("")
    L.append("**Purpose:** surface glosses that span multiple clusters — the diagnostic for the 'characteristic-legs scattered across clusters' pattern observed during M11 Phase 3 review. Four lenses:")
    L.append("")
    L.append("- §1 Exact gloss matches across clusters")
    L.append("- §2 Gloss-base matches across clusters (strip `: qualifier`)")
    L.append("- §3 Token matches across clusters (split glosses to words, exclude stop-words)")
    L.append("- §4 Sister-Strong's sense-suffix spread (same root, different sense letters, different clusters)")
    L.append("")
    L.append("---")
    L.append("")

    # §1
    L.append(f"## §1. Exact gloss collisions ({len(exact_collisions)} glosses span 2+ clusters)")
    L.append("")
    if exact_collisions:
        L.append("Identical gloss strings appearing on terms in different clusters. These are the strongest signal that the same concept is being captured under different anchor terms.")
        L.append("")
        L.append("| Gloss | Clusters | Terms |")
        L.append("|---|---|---|")
        for g in sorted(exact_collisions.keys(), key=lambda x: (-len({t["cluster"] for t in exact_collisions[x]}), x)):
            terms = exact_collisions[g]
            cluster_set = sorted({t["cluster"] for t in terms})
            term_strs = ", ".join(f"{t['strongs']} {t['translit']} [{t['cluster']}]" for t in terms)
            L.append(f"| `{g}` | {', '.join(cluster_set)} | {term_strs} |")
    else:
        L.append("_No exact gloss collisions._")
    L.append("")
    L.append("---")
    L.append("")

    # §2
    L.append(f"## §2. Gloss-base collisions ({len(base_collisions)} bases span 2+ clusters)")
    L.append("")
    L.append("Stripping the `: qualifier` suffix from each gloss yields a 'base' sense. Bases appearing in multiple clusters reveal where the programme captures the same root sense across different anchor terms (often the same Strong's with sense-letter suffixes).")
    L.append("")
    if base_collisions:
        L.append("| Gloss base | Clusters | Term-rows |")
        L.append("|---|---|---|")
        sorted_bases = sorted(base_collisions.keys(),
                              key=lambda x: (-len({t["cluster"] for t in base_collisions[x]}), x))
        for b in sorted_bases:
            terms = base_collisions[b]
            cluster_set = sorted({t["cluster"] for t in terms})
            n_terms = len(terms)
            cluster_str = ", ".join(cluster_set)
            term_strs = "; ".join(f"`{t['strongs']}` {t['translit']} → `{t['full_gloss']}` [{t['cluster']}]" for t in terms)
            L.append(f"| `{b}` | {cluster_str} ({len(cluster_set)} clusters, {n_terms} term-rows) | {term_strs} |")
    else:
        L.append("_No gloss-base collisions._")
    L.append("")
    L.append("---")
    L.append("")

    # §3
    L.append(f"## §3. Token collisions ({len(token_collisions)} tokens appear in 2+ clusters)")
    L.append("")
    L.append("Each gloss is split into tokens (excluding stop-words: `to, a, an, the, of, in, on, at, by, with, from, as, be, is, it, or, and, for, into`). Tokens appearing in 2+ clusters' gloss vocabulary are listed by cluster-spread (most clusters first), then by term count. Truncated to top 50 by spread; full list in §3.1 below.")
    L.append("")
    L.append("| Token | # Clusters | # Term-rows | Clusters (term count per cluster) |")
    L.append("|---|---:|---:|---|")
    top_n = 50
    for tok, n_clusters, n_terms, by_cluster in token_collisions[:top_n]:
        cluster_str = ", ".join(
            f"{cc}={len(by_cluster[cc])}" for cc in sorted(by_cluster.keys())
        )
        L.append(f"| `{tok}` | {n_clusters} | {n_terms} | {cluster_str} |")
    L.append("")

    L.append(f"### §3.1 Token detail (all {len(token_collisions)} tokens with cluster-spread ≥ 2)")
    L.append("")
    L.append("For each token, the full list of terms per cluster.")
    L.append("")
    for tok, n_clusters, n_terms, by_cluster in token_collisions:
        L.append(f"#### `{tok}` — {n_clusters} clusters, {n_terms} term-rows")
        L.append("")
        for cc in sorted(by_cluster.keys()):
            terms_here = by_cluster[cc]
            L.append(f"- **{cc}** ({cluster_meta.get(cc, '?')}) — {len(terms_here)} term(s):")
            for t in terms_here[:10]:
                L.append(f"  - `{t['strongs']}` {t['translit']} — `{t['full_gloss']}`")
            if len(terms_here) > 10:
                L.append(f"  - … and {len(terms_here) - 10} more")
        L.append("")
    L.append("---")
    L.append("")

    # §4
    L.append(f"## §4. Sister-Strong's sense-suffix spread ({len(cross_cluster_strongs)} Strong's roots have sense-rows in 2+ clusters)")
    L.append("")
    L.append("Strong's numbers with letter-suffixes (e.g. `H2930A`, `H2930B`) are sense-splits of one Hebrew/Greek lemma. When the sense-rows sit in different clusters, the same lexical root is split analytically by sense.")
    L.append("")
    if cross_cluster_strongs:
        L.append("| Root | Senses | Cluster spread |")
        L.append("|---|---|---|")
        for base in sorted(cross_cluster_strongs.keys()):
            senses = cross_cluster_strongs[base]
            cluster_set = sorted({t["cluster"] for t in senses})
            sense_str = "; ".join(f"`{t['strongs']}` {t['translit']} — `{t['gloss']}` [{t['cluster']}]" for t in senses)
            L.append(f"| `{base}` | {sense_str} | {', '.join(cluster_set)} ({len(cluster_set)} clusters) |")
    else:
        L.append("_No cross-cluster sister-Strong's._")
    L.append("")
    L.append("---")
    L.append("")

    # Summary
    L.append("## Summary")
    L.append("")
    L.append(f"- **Total non-T2 terms scanned:** {total_terms}")
    L.append(f"- **Clusters in scope:** {len(cluster_codes)}")
    L.append(f"- **Exact gloss collisions:** {len(exact_collisions)}")
    L.append(f"- **Gloss-base collisions:** {len(base_collisions)}")
    L.append(f"- **Token collisions (≥ 2 clusters):** {len(token_collisions)}")
    L.append(f"- **Sister-Strong's spread across clusters:** {len(cross_cluster_strongs)}")
    L.append("")

    out_path.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote: {out_path.relative_to(REPO)}")
    print(f"  Exact gloss collisions:           {len(exact_collisions)}")
    print(f"  Gloss-base collisions:            {len(base_collisions)}")
    print(f"  Token collisions (>=2 clusters):  {len(token_collisions)}")
    print(f"  Sister-Strong's spread:           {len(cross_cluster_strongs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
