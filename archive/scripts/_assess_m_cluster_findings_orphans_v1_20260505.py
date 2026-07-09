"""_assess_m_cluster_findings_orphans_v1_20260505.py — read-only.

Find Session B findings + Session D pointers whose text content suggests
M-cluster relevance but are NOT paired to that M-cluster through term,
verse, or registry references.

Method:
  1. Identify M-cluster strong's (from v6 anchor) and M-cluster contributor
     registries.
  2. For each finding (wa_session_b_findings) and SD pointer
     (wa_session_research_flags WHERE flag_code='SD_POINTER'):
       - Determine "paired" status:
         * Finding paired = registry_id is in M-contributor registries
           OR anchor_verses contains a Strong's reference matching an M-term
         * Pointer paired = strongs_reference matches any M-term
           OR registry_id / cross_registry_id is an M-contributor registry
       - Scan text content (finding / description) for M-cluster keywords.
  3. Tier the candidates:
       - Tier A — KEYWORD-HIT + UNPAIRED (review priority — content suggests
         M-cluster relevance but no link)
       - Tier B — KEYWORD-HIT + PAIRED (already covered; sanity check)
       - Tier C — UNPAIRED + no keyword (no signal; ignored)

Usage:
  python scripts/_assess_m_cluster_findings_orphans_v1_20260505.py --m-cluster M05
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
V6_PATH = "archive/Clusters/wa-term-anchor-v6-20260504.json"

LEXICON = {
    "M05": [
        "love", "lover", "loving", "beloved", "dear", "dearly",
        "friend", "friendly", "friendship", "companion", "companionship",
        "affection", "affectionate", "tender", "tenderly",
        "compassion", "compassionate", "pity", "pitiful",
        "mercy", "merciful", "merciless",
        "kind", "kindness", "kindly",
        "gentle", "gentleness", "meek", "meekness",
        "comfort", "console", "consolation", "encouragement",
        "sympathy", "sympathize", "sympathetic",
        "benevolence", "benevolent",
        "embrace", "kiss",
        "hospitable", "hospitality",
        "graciousness", "chesed", "agape", "agapē", "phileo", "fileō",
        "racham", "rachamim",
    ],
    "M06": [
        "hate", "hated", "hatred", "hateful", "hating",
        "contempt", "contemptuous", "contemptible",
        "despise", "despised", "despising",
        "hostility", "hostile", "enemy", "enmity", "adversary",
        "abhor", "abhorrent", "abhorrence",
        "detest", "detested", "detestable",
        "abomination", "abominable",
        "scorn", "scornful", "mock", "mocking", "mockery",
        "derision", "deride", "ridicule", "taunt", "taunting",
        "spurn", "reject", "rejection",
        "disgust", "disgusting", "loathe", "loathsome", "loathing",
        "revile", "reviling", "revilement", "curse", "cursing",
        "reproach", "reviled", "vilify",
        "antagonism", "animosity", "rancor", "rancour",
        "miseo", "miseō", "echthros", "echthra",
        "sane", "buz",
    ],
}

STRONGS_RE = re.compile(r"\b([HG]\d{4}[A-Z]?)\b")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def keyword_hits(text, lex):
    if not text:
        return []
    t = text.lower()
    return [kw for kw in lex
            if re.search(rf"\b{re.escape(kw)}\b", t)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if args.m_cluster not in LEXICON:
        print(f"ERROR: no keyword lexicon for {args.m_cluster}.", flush=True)
        return 1
    lex = LEXICON[args.m_cluster]

    _dest_dir = os.path.join("Sessions", "Session_Clusters", args.m_cluster)
    os.makedirs(_dest_dir, exist_ok=True)
    out_path = args.out or os.path.join(
        _dest_dir,
        f"wa-cluster-{args.m_cluster.lower()}-finding-"
        f"orphans-v1-{datetime.now().strftime('%Y%m%d')}.md"
    )

    # Load v6: M-cluster strong's and contributor registries
    with open(V6_PATH, encoding="utf-8") as f:
        v6 = json.load(f)
    cluster_labels = v6.get("meaning_cluster_labels", {})
    m_label = cluster_labels.get(args.m_cluster, "?")
    print(f"M-cluster {args.m_cluster}: {m_label}", flush=True)

    m_strongs = set()
    for s, t in v6["term_anchors"].items():
        if t.get("cluster_id") == args.m_cluster:
            m_strongs.add(s)
    print(f"  M-cluster terms: {len(m_strongs)}", flush=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Map M-cluster strong's to owning registry IDs and registry names
    placeholders = ",".join("?" * len(m_strongs))
    rows = conn.execute(f"""
        SELECT mt.strongs_number, mt.owning_registry_fk,
               wr.no, wr.word
          FROM mti_terms mt
          LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
         WHERE mt.strongs_number IN ({placeholders})
    """, list(m_strongs)).fetchall()
    m_registries = set()
    reg_id_to_name = {}
    for r in rows:
        if r["owning_registry_fk"]:
            m_registries.add(r["owning_registry_fk"])
        if r["no"]:
            reg_id_to_name[r["owning_registry_fk"]] = (
                f"R{r['no']:03d} {r['word']}"
            )
    print(f"  M-cluster contributor registries: {len(m_registries)}",
          flush=True)

    # Pull findings (active)
    findings = conn.execute("""
        SELECT id, finding_id, registry_id, finding_type, finding,
               anchor_verses, status
          FROM wa_session_b_findings
         WHERE COALESCE(delete_flag,0) = 0
    """).fetchall()
    print(f"Active findings: {len(findings)}", flush=True)

    # Pull SD pointers (active)
    pointers = conn.execute("""
        SELECT id, registry_id, flag_label, flag_code, strongs_reference,
               cross_registry_id, priority, description, resolved
          FROM wa_session_research_flags
         WHERE COALESCE(resolved,0) = 0
           AND flag_code = 'SD_POINTER'
    """).fetchall()
    print(f"Active SD pointers: {len(pointers)}", flush=True)

    # Map all known registry IDs for label resolution
    all_regs = conn.execute("SELECT id, no, word FROM word_registry").fetchall()
    reg_lookup = {r["id"]: f"R{r['no']:03d} {r['word']}" for r in all_regs}

    conn.close()

    def _strongs_in_text(text):
        if not text:
            return set()
        return set(STRONGS_RE.findall(text))

    # Score each finding
    finding_records = []
    for f in findings:
        text = f["finding"] or ""
        anchor = f["anchor_verses"] or ""
        scan_text = " | ".join([text, anchor])
        hits = keyword_hits(scan_text, lex)
        # Pair via registry
        paired_via_registry = (
            f["registry_id"] in m_registries
            if f["registry_id"] else False
        )
        # Pair via Strong's references in finding text (rare for findings
        # but we check in case)
        text_strongs = _strongs_in_text(scan_text)
        m_hits_in_text = m_strongs & text_strongs
        paired_via_strongs = bool(m_hits_in_text)
        finding_records.append({
            "id": f["id"],
            "finding_id": f["finding_id"],
            "type": f["finding_type"],
            "registry_id": f["registry_id"],
            "registry_label": reg_lookup.get(
                f["registry_id"], "(unknown)"
            ),
            "anchor_verses": anchor,
            "text": text,
            "status": f["status"],
            "kw_hits": hits,
            "n_kw_hits": len(hits),
            "paired_via_registry": paired_via_registry,
            "paired_via_strongs": paired_via_strongs,
            "m_strongs_referenced": sorted(m_hits_in_text),
            "any_strongs_referenced": sorted(text_strongs),
            "paired": paired_via_registry or paired_via_strongs,
        })

    # Score each pointer
    pointer_records = []
    for p in pointers:
        text = p["description"] or ""
        sref = p["strongs_reference"] or ""
        scan_text = " | ".join([text, sref])
        hits = keyword_hits(scan_text, lex)
        # Pair via strongs_reference (single strong, like 'G3340')
        sref_strongs = _strongs_in_text(sref)
        text_strongs = _strongs_in_text(text)
        all_referenced = sref_strongs | text_strongs
        m_hits_in_text = m_strongs & all_referenced
        paired_via_strongs = bool(m_hits_in_text)
        paired_via_registry = (
            p["registry_id"] in m_registries
            if p["registry_id"] else False
        ) or (
            p["cross_registry_id"] in m_registries
            if p["cross_registry_id"] else False
        )
        pointer_records.append({
            "id": p["id"],
            "label": p["flag_label"],
            "registry_id": p["registry_id"],
            "registry_label": reg_lookup.get(p["registry_id"], "(unknown)"),
            "cross_registry_id": p["cross_registry_id"],
            "cross_registry_label": (
                reg_lookup.get(p["cross_registry_id"])
                if p["cross_registry_id"] else None
            ),
            "priority": p["priority"],
            "strongs_reference": sref,
            "text": text,
            "kw_hits": hits,
            "n_kw_hits": len(hits),
            "paired_via_strongs": paired_via_strongs,
            "paired_via_registry": paired_via_registry,
            "m_strongs_referenced": sorted(m_hits_in_text),
            "any_strongs_referenced": sorted(all_referenced),
            "paired": paired_via_strongs or paired_via_registry,
        })

    # Tier
    finding_tier_a = [
        x for x in finding_records
        if x["n_kw_hits"] > 0 and not x["paired"]
    ]
    finding_tier_b = [
        x for x in finding_records
        if x["n_kw_hits"] > 0 and x["paired"]
    ]
    pointer_tier_a = [
        x for x in pointer_records
        if x["n_kw_hits"] > 0 and not x["paired"]
    ]
    pointer_tier_b = [
        x for x in pointer_records
        if x["n_kw_hits"] > 0 and x["paired"]
    ]
    finding_tier_a.sort(key=lambda x: -x["n_kw_hits"])
    pointer_tier_a.sort(key=lambda x: -x["n_kw_hits"])

    # Render
    lines = []
    lines.append(f"# {args.m_cluster} {m_label} — orphan findings + "
                 "Session-D pointers\n")
    lines.append(f"**Generated:** {now_iso()}  ")
    lines.append(f"**M-cluster contributor registries:** "
                 f"{len(m_registries)}  ")
    lines.append(f"**M-cluster Strong's:** {len(m_strongs)}\n")
    lines.append("**Method:** scan finding-text and pointer-description for "
                 "M-cluster keywords (love, compassion, kindness, mercy, …). "
                 "Mark each as **paired** when its `registry_id` / "
                 "`cross_registry_id` is one of the M-cluster contributor "
                 "registries, or its Strong's references include any "
                 "M-cluster term.\n")
    lines.append("**Tiers:**")
    lines.append("- **A — ORPHAN** — keyword hit, but NOT paired through "
                 "term/registry: should be reviewed for M-cluster relevance.")
    lines.append("- **B — PAIRED+matched** — keyword hit AND already paired: "
                 "the expected baseline, listed for completeness.\n")
    lines.append("---\n")
    lines.append("## Headline\n")
    lines.append(f"- Active findings: {len(findings)}")
    lines.append(f"- Active SD pointers: {len(pointers)}")
    lines.append(f"- **Findings — keyword hits:** "
                 f"{len(finding_tier_a) + len(finding_tier_b)} "
                 f"(orphan {len(finding_tier_a)} / paired "
                 f"{len(finding_tier_b)})")
    lines.append(f"- **SD pointers — keyword hits:** "
                 f"{len(pointer_tier_a) + len(pointer_tier_b)} "
                 f"(orphan {len(pointer_tier_a)} / paired "
                 f"{len(pointer_tier_b)})")
    lines.append("")

    # Section: orphan findings
    lines.append(f"## Tier A — ORPHAN findings ({len(finding_tier_a)})\n")
    if not finding_tier_a:
        lines.append("*(none)*\n")
    else:
        lines.append("Findings whose text mentions M-cluster vocabulary but "
                     "whose owning registry is NOT a contributor to "
                     f"{args.m_cluster}. Review whether they describe a "
                     "characteristic relevant to this cluster.\n")
        lines.append("| Finding ID | Type | Owning registry | Hits | "
                     "Anchor verses | Excerpt |")
        lines.append("|---|---|---|---|---|---|")
        for f in finding_tier_a[:50]:
            excerpt = (f["text"][:200] + "…") if len(f["text"]) > 200 else f["text"]
            excerpt = excerpt.replace("|", "\\|").replace("\n", " ")
            kw = ", ".join(f["kw_hits"])
            anchor = (f["anchor_verses"] or "")[:80]
            lines.append(
                f"| {f['finding_id']} | {f['type']} | "
                f"{f['registry_label']} | {kw} | {anchor} | {excerpt} |"
            )
        if len(finding_tier_a) > 50:
            lines.append(f"\n*(showing 50 of {len(finding_tier_a)} — full "
                         "list in JSON companion)*")
    lines.append("")

    # Section: orphan pointers
    lines.append(f"## Tier A — ORPHAN SD pointers ({len(pointer_tier_a)})\n")
    if not pointer_tier_a:
        lines.append("*(none)*\n")
    else:
        lines.append("Pointers whose description mentions M-cluster "
                     "vocabulary but whose Strong's-reference / registries "
                     f"do not link to {args.m_cluster}. Likely candidates "
                     "for re-tagging or for inclusion in cross-cluster "
                     "analysis.\n")
        lines.append("| Pointer | Priority | Owning reg | "
                     "Cross-reg | Strong's ref | Hits | Excerpt |")
        lines.append("|---|---|---|---|---|---|---|")
        for p in pointer_tier_a[:50]:
            excerpt = (p["text"][:200] + "…") if len(p["text"]) > 200 else p["text"]
            excerpt = excerpt.replace("|", "\\|").replace("\n", " ")
            kw = ", ".join(p["kw_hits"])
            xreg = p["cross_registry_label"] or "—"
            sref = (p["strongs_reference"] or "")[:60]
            lines.append(
                f"| {p['label']} | {p['priority'] or '—'} | "
                f"{p['registry_label']} | {xreg} | {sref} | {kw} | "
                f"{excerpt} |"
            )
        if len(pointer_tier_a) > 50:
            lines.append(f"\n*(showing 50 of {len(pointer_tier_a)})*")
    lines.append("")

    # Sanity: paired counts (just totals — no detail dump)
    lines.append("## Tier B — keyword-matched but already PAIRED "
                 "(sanity check)\n")
    lines.append(f"- Findings: **{len(finding_tier_b)}** "
                 "(content matches M-cluster vocabulary AND owning registry "
                 "contributes to M-cluster)")
    lines.append(f"- SD pointers: **{len(pointer_tier_b)}** "
                 "(content matches AND Strong's/registry already links)")
    lines.append("\n*(detail in JSON companion if needed)*\n")

    # Companion JSON
    out_json = out_path.replace(".md", ".json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "generated": now_iso(),
                "m_cluster": args.m_cluster,
                "m_label": m_label,
                "n_m_strongs": len(m_strongs),
                "n_m_registries": len(m_registries),
                "n_findings_active": len(findings),
                "n_pointers_active": len(pointers),
            },
            "lexicon": lex,
            "findings_orphan": finding_tier_a,
            "findings_paired_keyword": finding_tier_b,
            "pointers_orphan": pointer_tier_a,
            "pointers_paired_keyword": pointer_tier_b,
        }, f, indent=2, ensure_ascii=False)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {out_path}", flush=True)
    print(f"Wrote: {out_json}", flush=True)
    print(f"\nORPHANS: findings={len(finding_tier_a)} "
          f"pointers={len(pointer_tier_a)}", flush=True)
    print(f"PAIRED keyword-matched: findings={len(finding_tier_b)} "
          f"pointers={len(pointer_tier_b)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
