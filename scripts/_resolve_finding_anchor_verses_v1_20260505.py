"""_resolve_finding_anchor_verses_v1_20260505.py — read-only.

Resolves anchor_verses text references in wa_session_b_findings to specific
M-cluster terms via wa_verse_records. Produces a per-term count of findings
whose anchor verses contain that term's OWNER verses, and a (term, finding,
verse) detail map.

Usage:
  python scripts/_resolve_finding_anchor_verses_v1_20260505.py --m-cluster M06

Output:
  outputs/markdown/wa-cluster-{m}-anchor-verse-links-v1-{date}.json
  outputs/markdown/wa-cluster-{m}-anchor-verse-links-v1-{date}.md
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
V6_PATH = "archive/Clusters/wa-term-anchor-v6-20260504.json"

# Reference parser: matches "Book Chap:Verse" or "Book Chap:Verse-Verse"
# Allows book abbreviations of 2-5 chars (incl. digit prefix like 1Co, 2Th)
REF_RE = re.compile(
    r"\b(\d?[A-Za-z]{2,5})\s+(\d{1,3}):(\d{1,3})(?:-(\d{1,3}))?",
)
# Strip parenthetical notes from anchor_verses
PAREN_RE = re.compile(r"\([^)]*\)")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def build_book_lookup(conn):
    """Return dict mapping abbreviation/short_code/name to book_id."""
    out = {}
    for r in conn.execute(
        "SELECT id, name, abbreviation, short_code FROM books"
    ).fetchall():
        bid = r["id"]
        for k in (r["abbreviation"], r["short_code"], r["name"]):
            if k:
                out[k.lower()] = bid
    # Common alternatives observed in data
    aliases = {
        "1cor": "1Co", "2cor": "2Co",
        "1th": "1Th", "2th": "2Th",
        "1jo": "1Jn", "2jo": "2Jn", "3jo": "3Jn",
        "song": "Sng", "songs": "Sng",
        "ps": "Psa", "pss": "Psa",
        "jhn": "Joh", "jn": "Joh",
        "mt": "Mat", "mk": "Mar", "lk": "Luk",
        "co1": "1Co", "co2": "2Co",
        "jas": "Jam", "phi": "Php", "phil": "Php",
        "1tim": "1Ti", "2tim": "2Ti",
        "1pet": "1Pe", "2pet": "2Pe",
        "rom": "Rom", "gal": "Gal", "eph": "Eph",
        "col": "Col", "tit": "Tit", "phm": "Phm",
        "heb": "Heb", "rev": "Rev",
        "ezek": "Eze", "zech": "Zec", "zeph": "Zep",
        "matt": "Mat", "mark": "Mar",
        "1sam": "1Sa", "2sam": "2Sa",
        "1kgs": "1Ki", "2kgs": "2Ki",
        "1king": "1Ki", "2king": "2Ki",
        "1chr": "1Ch", "2chr": "2Ch",
        "neh": "Neh", "esth": "Est",
        "deut": "Deu", "lev": "Lev",
        "numb": "Num", "gen": "Gen", "exo": "Exo",
        "psa": "Psa", "prov": "Pro",
        "eccl": "Ecc", "lam": "Lam",
        "dan": "Dan", "hos": "Hos", "joel": "Joe",
        "amos": "Amo", "obad": "Oba", "jonah": "Jon",
        "mic": "Mic", "nah": "Nah", "hab": "Hab",
        "hag": "Hag", "mal": "Mal",
        "isa": "Isa", "jer": "Jer", "ezk": "Eze",
        "josh": "Jos", "judg": "Jdg", "ruth": "Rut",
        "ssol": "Sng", "sos": "Sng",
    }
    for alt, canonical in aliases.items():
        if canonical.lower() in out:
            out[alt.lower()] = out[canonical.lower()]
    return out


def parse_anchor_verses(text, book_lookup):
    """Yield (book_id, chapter, verse_num, raw_ref) tuples."""
    if not text:
        return
    cleaned = PAREN_RE.sub("", text)
    for m in REF_RE.finditer(cleaned):
        bk_token, chap, v1, v2 = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        bid = book_lookup.get(bk_token.lower())
        if not bid:
            continue
        if v2 is None:
            yield (bid, chap, v1, f"{bk_token} {chap}:{v1}")
        else:
            for v in range(v1, int(v2) + 1):
                yield (bid, chap, v, f"{bk_token} {chap}:{v}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    _dest_dir = os.path.join("Sessions", "Session_Clusters", args.m_cluster)
    os.makedirs(_dest_dir, exist_ok=True)
    out_md = args.out or os.path.join(
        _dest_dir,
        f"wa-cluster-{args.m_cluster.lower()}-"
        f"anchor-verse-links-v1-{datetime.now().strftime('%Y%m%d')}.md"
    )
    out_json = out_md.replace(".md", ".json")

    with open(V6_PATH, encoding="utf-8") as f:
        v6 = json.load(f)
    cluster_labels = v6.get("meaning_cluster_labels", {})
    m_label = cluster_labels.get(args.m_cluster, "?")
    m_strongs = [s for s, t in v6["term_anchors"].items()
                 if t.get("cluster_id") == args.m_cluster]
    print(f"M-cluster {args.m_cluster}: {m_label}", flush=True)
    print(f"  M terms: {len(m_strongs)}", flush=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    book_lookup = build_book_lookup(conn)
    print(f"  book name aliases: {len(book_lookup)}", flush=True)

    # Map mti_term_id -> Strong's for our cluster
    ph = ",".join("?" * len(m_strongs))
    rows = conn.execute(f"""
        SELECT id, strongs_number, gloss, transliteration, language
          FROM mti_terms
         WHERE strongs_number IN ({ph})
    """, m_strongs).fetchall()
    mti_to_strong = {r["id"]: r["strongs_number"] for r in rows}
    strong_to_meta = {r["strongs_number"]: dict(r) for r in rows}
    mti_ids = list(mti_to_strong.keys())

    # Index: (book_id, chapter, verse_num) -> set of (mti_term_id) that have
    # an active wa_verse_record at that location.
    print("Indexing verse-record locations for M terms...", flush=True)
    placeholders_t = ",".join("?" * len(mti_ids))
    verse_index = defaultdict(set)
    for r in conn.execute(f"""
        SELECT vr.book_id, vr.chapter, vr.verse_num, vr.mti_term_id
          FROM wa_verse_records vr
         WHERE COALESCE(vr.delete_flagged,0) = 0
           AND vr.mti_term_id IN ({placeholders_t})
    """, mti_ids).fetchall():
        verse_index[(r["book_id"], r["chapter"], r["verse_num"])].add(
            r["mti_term_id"]
        )
    print(f"  unique (book,chap,verse) locations with M terms: "
          f"{len(verse_index):,}", flush=True)

    # Walk findings; resolve anchor_verses
    print("Resolving anchor verses on findings...", flush=True)
    findings = conn.execute("""
        SELECT id, finding_id, registry_id, finding_type,
               anchor_verses, finding
          FROM wa_session_b_findings
         WHERE COALESCE(delete_flag,0) = 0
           AND anchor_verses IS NOT NULL
           AND TRIM(anchor_verses) != ''
    """).fetchall()
    print(f"  findings with anchor_verses: {len(findings):,}", flush=True)

    # Per-term: list of (finding_id, finding_pk, ref) tuples
    per_term_links = defaultdict(list)
    # Per-finding: list of M terms it links to (deduplicated)
    per_finding_terms = defaultdict(set)
    n_with_link = 0
    n_refs_parsed = 0
    n_refs_unresolved = 0
    sample_unresolved = []

    for f in findings:
        text = f["anchor_verses"]
        any_link = False
        seen_refs = set()
        for bid, chap, vnum, raw_ref in parse_anchor_verses(text, book_lookup):
            n_refs_parsed += 1
            seen_refs.add((bid, chap, vnum))
            mti_set = verse_index.get((bid, chap, vnum), set())
            for mid in mti_set:
                strong = mti_to_strong[mid]
                per_term_links[strong].append({
                    "finding_pk": f["id"],
                    "finding_id": f["finding_id"],
                    "finding_type": f["finding_type"],
                    "registry_id": f["registry_id"],
                    "anchor_ref": raw_ref,
                })
                per_finding_terms[f["id"]].add(strong)
                any_link = True
        if any_link:
            n_with_link += 1

    # Re-pass over findings to count unresolved refs separately
    for f in findings:
        text = f["anchor_verses"]
        cleaned = PAREN_RE.sub("", text)
        for m in REF_RE.finditer(cleaned):
            bk = m.group(1).lower()
            if bk not in book_lookup:
                n_refs_unresolved += 1
                if len(sample_unresolved) < 10:
                    sample_unresolved.append(m.group(0))

    # Aggregate per-term counts
    per_term_counts = {
        s: {
            "n_findings_via_anchor": len(set(
                lk["finding_pk"] for lk in per_term_links[s]
            )),
            "n_anchor_links": len(per_term_links[s]),
            "links": per_term_links[s],
        } for s in per_term_links
    }

    # Output JSON
    out_data = {
        "meta": {
            "generated": now_iso(),
            "m_cluster": args.m_cluster,
            "m_label": m_label,
            "n_m_terms": len(m_strongs),
            "n_findings_with_anchor_verses": len(findings),
            "n_findings_with_link_to_m_term": n_with_link,
            "n_anchor_refs_parsed": n_refs_parsed,
            "n_anchor_refs_unresolved": n_refs_unresolved,
            "sample_unresolved": sample_unresolved,
        },
        "per_term": per_term_counts,
    }
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(out_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote: {out_json}", flush=True)

    # Markdown report
    lines = []
    lines.append(f"# {args.m_cluster} {m_label} — finding ↔ term linkage "
                 "via anchor verses\n")
    lines.append(f"**Generated:** {now_iso()}  ")
    lines.append(f"**Method:** parse `anchor_verses` text on each active "
                 "finding; resolve each verse reference to "
                 "`wa_verse_records` rows; record the finding ↔ term link "
                 f"for each M-cluster term that has a verse-record at that "
                 "location.\n")
    lines.append("## Headline\n")
    lines.append(f"- Findings with `anchor_verses`: "
                 f"{len(findings):,}")
    lines.append(f"- Findings linked to ≥1 {args.m_cluster} term via "
                 f"anchor verse: **{n_with_link:,}**")
    lines.append(f"- Anchor refs parsed: {n_refs_parsed:,} "
                 f"(unresolvable book name: {n_refs_unresolved})")
    if sample_unresolved:
        lines.append(f"  - Examples of unresolved: "
                     f"{', '.join(sample_unresolved[:5])}")
    lines.append(f"- {args.m_cluster} terms with ≥1 anchor-verse-linked "
                 f"finding: **{len(per_term_counts)}** of "
                 f"{len(m_strongs)}\n")

    lines.append("## Per-term anchor-verse-linked findings count\n")
    lines.append("Sorted descending by linked-findings count.\n")
    lines.append("| Strong's | Lang | Translit | Gloss | "
                 "Findings via anchor | Total link rows |")
    lines.append("|---|---|---|---|---:|---:|")
    sorted_terms = sorted(
        per_term_counts.items(),
        key=lambda kv: -kv[1]["n_findings_via_anchor"]
    )
    for s, info in sorted_terms:
        meta = strong_to_meta.get(s, {})
        lang = (meta.get("language") or "")[:1]
        translit = meta.get("transliteration") or ""
        gloss = meta.get("gloss") or ""
        lines.append(
            f"| {s} | {lang} | {translit} | {gloss} | "
            f"{info['n_findings_via_anchor']} | {info['n_anchor_links']} |"
        )
    lines.append("")

    # Top-5 terms with detail
    lines.append("## Top 10 terms — sample of linked finding IDs\n")
    for s, info in sorted_terms[:10]:
        meta = strong_to_meta.get(s, {})
        gloss = meta.get("gloss") or ""
        translit = meta.get("transliteration") or ""
        lines.append(f"### {s} {translit} ({gloss}) — "
                     f"{info['n_findings_via_anchor']} findings via anchor")
        # Deduplicate by finding_pk and show at most 12
        seen_pk = set()
        rows = []
        for lk in info["links"]:
            if lk["finding_pk"] in seen_pk:
                continue
            seen_pk.add(lk["finding_pk"])
            rows.append(lk)
            if len(rows) >= 12:
                break
        lines.append("| Finding ID | Type | Anchor verse |")
        lines.append("|---|---|---|")
        for r in rows:
            lines.append(
                f"| {r['finding_id']} | {r['finding_type']} | "
                f"{r['anchor_ref']} |"
            )
        if info["n_findings_via_anchor"] > 12:
            lines.append(f"\n*(showing 12 of "
                         f"{info['n_findings_via_anchor']} unique findings)*")
        lines.append("")

    conn.close()
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {out_md}", flush=True)
    print(f"\n{n_with_link} findings linked to "
          f"{len(per_term_counts)} of {len(m_strongs)} terms via anchor "
          f"verses.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
