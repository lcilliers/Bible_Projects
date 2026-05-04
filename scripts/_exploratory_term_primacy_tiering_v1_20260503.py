"""_exploratory_term_primacy_tiering_v1_20260503.py — read-only.

Classifies every active OWNER term into a four-tier primacy band so per-registry
term relevance can be read at a glance. Tiering is rule-based on existing
signals; rules below are explicit so they can be tuned and re-run.

Tier rule (applied per OWNER term, in priority order):

  U — Unanalysed
      The term has zero verse_context rows at all (no active vc rows for
      this mti_term, regardless of is_relevant or set_aside_reason).
      NOTE: mti_terms.vc_status is stale on most rows ('not_done' even when
      the term has been classified). Row presence is authoritative.

  C — Marginal (thin / vestigial / data-only)
      status IN ('extracted_thin','candidate_delete','phase2_enrichment'),
      OR (groups_active = 0 AND anchors = 0),
      OR (anchors = 0 AND vc_relevant < 3).

  A — Primary (carries the registry's analytical core)
      status = 'extracted_theological_anchor',
      OR (anchors >= 2 AND groups_active >= 1 AND vc_relevant >= 10),
      OR (anchors >= 1 AND groups_active >= 2 AND vc_relevant >= 20).

  B — Secondary (substantive contributor; everything that isn't U/C/A)

Output: markdown report + JSON sidecar with per-term assignments.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_MD = os.path.join("outputs", "markdown", "term-primacy-tiering-20260503.md")
OUT_JSON = os.path.join("outputs", "markdown", "term-primacy-tiering-20260503.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def classify(t) -> str:
    """Apply the tier rule to a per-term dict. Returns 'A' | 'B' | 'C' | 'U'."""
    has_any_vc = (t["vc_rel"] + t["vc_set_aside"] + t["vc_other"] + t["anchors"]) > 0

    # U — Unanalysed (vc_status flag is unreliable; trust row presence)
    if not has_any_vc:
        return "U"

    status = (t["status"] or "").lower()
    anchors = t["anchors"]
    groups = t["groups_active"]
    vc_rel = t["vc_rel"]

    # C — Marginal (catch the explicit thin markers + the structurally empty)
    if status in ("extracted_thin", "candidate_delete", "phase2_enrichment"):
        return "C"
    if groups == 0 and anchors == 0:
        return "C"
    if anchors == 0 and vc_rel < 3:
        return "C"

    # A — Primary
    if status == "extracted_theological_anchor":
        return "A"
    if anchors >= 2 and groups >= 1 and vc_rel >= 10:
        return "A"
    if anchors >= 1 and groups >= 2 and vc_rel >= 20:
        return "A"

    # B — Secondary (default for the substantive middle)
    return "B"


TIER_LABEL = {
    "A": "Primary",
    "B": "Secondary",
    "C": "Marginal",
    "U": "Unanalysed",
}


def fetch_all_terms(conn) -> list[dict]:
    rows = conn.execute("""
        SELECT
          mt.id           AS mti_id,
          mt.strongs_number,
          mt.transliteration,
          mt.gloss,
          mt.language,
          mt.status,
          mt.vc_status,
          mt.anchor_note,
          ti.id           AS ti_id,
          ti.evidential_status,
          ti.retention_note,
          wr.id           AS reg_id,
          wr.no           AS reg_no,
          wr.word         AS reg_word,
          wr.cluster_assignment,
          (SELECT COUNT(*) FROM wa_verse_records vr
            WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0) AS verses,
          (SELECT COUNT(*) FROM verse_context_group g
            WHERE g.mti_term_id = mt.id AND g.delete_flagged = 0) AS groups_active,
          (SELECT COUNT(*) FROM verse_context vc
            WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
              AND vc.is_relevant = 1) AS vc_rel,
          (SELECT COUNT(*) FROM verse_context vc
            WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
              AND vc.is_anchor = 1) AS anchors,
          (SELECT COUNT(*) FROM verse_context vc
            WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
              AND vc.is_relevant = 0
              AND vc.set_aside_reason IS NOT NULL
              AND vc.set_aside_reason != '') AS vc_set_aside,
          (SELECT COUNT(*) FROM verse_context vc
            WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
              AND vc.is_relevant = 0
              AND (vc.set_aside_reason IS NULL OR vc.set_aside_reason = '')) AS vc_other,
          (SELECT mp.top_sense_count FROM wa_meaning_parsed mp
            WHERE mp.term_inv_id = ti.id LIMIT 1) AS top_senses,
          (SELECT mp.stem_count FROM wa_meaning_parsed mp
            WHERE mp.term_inv_id = ti.id LIMIT 1) AS stems,
          (SELECT COUNT(DISTINCT fi2.word_registry_fk) FROM wa_term_inventory ti2
             JOIN wa_file_index fi2 ON fi2.id = ti2.file_id
            WHERE ti2.strongs_number = mt.strongs_number
              AND ti2.term_owner_type = 'XREF'
              AND ti2.delete_flagged = 0) AS xref_into_n_other_regs
        FROM mti_terms mt
        JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                 AND ti.term_owner_type = 'OWNER'
                                 AND ti.delete_flagged = 0
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
       WHERE mt.delete_flagged = 0
         AND mt.status NOT IN ('delete','excluded')
       ORDER BY wr.no, mt.language DESC, mt.strongs_number
    """).fetchall()
    return [dict(r) for r in rows]


def render(terms: list[dict]) -> str:
    L: list[str] = []
    L.append("# OWNER Term Primacy Tiering")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  source: "
             "`scripts/_exploratory_term_primacy_tiering_v1_20260503.py`")
    L.append("")
    L.append("Every active OWNER term is classified into one of four tiers based on the rule "
             "in the script header. Re-run the script to refresh after DB changes; tweak the "
             "rule in `classify()` to refine.")
    L.append("")

    # Tier rule restatement
    L.append("## Tier rule (applied in this order; first match wins)")
    L.append("")
    L.append("| Tier | Label | Rule |")
    L.append("|---|---|---|")
    L.append("| **U** | Unanalysed | zero active `verse_context` rows for this term (row presence is authoritative; `mti_terms.vc_status` is stale on most rows and is NOT used) |")
    L.append("| **C** | Marginal | `mti_terms.status` in (`extracted_thin`, `candidate_delete`, `phase2_enrichment`) **or** zero groups & zero anchors **or** anchors=0 & vc_relevant<3 |")
    L.append("| **A** | Primary | `status='extracted_theological_anchor'` **or** anchors≥2 & groups≥1 & vc_relevant≥10 **or** anchors≥1 & groups≥2 & vc_relevant≥20 |")
    L.append("| **B** | Secondary | everything else (the substantive middle) |")
    L.append("")

    # Programme totals per tier
    by_tier = defaultdict(list)
    for t in terms:
        by_tier[t["tier"]].append(t)
    n_total = len(terms)

    L.append("## Programme totals")
    L.append("")
    L.append(f"Active OWNER terms classified: **{n_total:,}**")
    L.append("")
    L.append("| Tier | Label | Count | % |")
    L.append("|---|---|---:|---:|")
    for tier in ("A", "B", "C", "U"):
        n = len(by_tier[tier])
        pct = (n / n_total * 100) if n_total else 0
        L.append(f"| **{tier}** | {TIER_LABEL[tier]} | {n:,} | {pct:.1f}% |")
    L.append("")

    # Language breakdown
    L.append("## By language")
    L.append("")
    L.append("| Tier | Hebrew | Greek |")
    L.append("|---|---:|---:|")
    for tier in ("A", "B", "C", "U"):
        h = sum(1 for t in by_tier[tier] if t["language"] == "Hebrew")
        g = sum(1 for t in by_tier[tier] if t["language"] == "Greek")
        L.append(f"| {tier} {TIER_LABEL[tier]} | {h:,} | {g:,} |")
    L.append("")

    # By cluster
    L.append("## By cluster")
    L.append("")
    L.append("Counts per cluster across the four tiers (registries grouped by their "
             "`cluster_assignment` from `word_registry`).")
    L.append("")
    by_cluster_tier: dict = defaultdict(lambda: defaultdict(int))
    for t in terms:
        cl = t.get("cluster_assignment") or "(none)"
        by_cluster_tier[cl][t["tier"]] += 1
    L.append("| Cluster | A | B | C | U | total |")
    L.append("|---|---:|---:|---:|---:|---:|")
    cluster_keys = sorted(by_cluster_tier.keys(),
                          key=lambda k: (k == "(none)", k))
    for cl in cluster_keys:
        row = by_cluster_tier[cl]
        tot = sum(row.values())
        L.append(f"| `{cl}` | {row['A']:,} | {row['B']:,} | {row['C']:,} | {row['U']:,} | {tot:,} |")
    L.append("")

    # Per-registry composition
    L.append("## Per-registry tier composition")
    L.append("")
    L.append("Each registry's OWNER term portfolio at a glance. Registries are listed in "
             "`no` order. The `archetype` column flags structural patterns:")
    L.append("")
    L.append("- **single-pillar** — exactly one Primary, the rest Secondary/Marginal")
    L.append("- **multi-pillar** — two or more Primary terms")
    L.append("- **distributed** — no Primary; analytical weight spread across Secondary terms")
    L.append("- **thin** — only Marginal terms")
    L.append("- **unanalysed** — only Unanalysed terms")
    L.append("- **mixed-no-primary** — a mix without any Primary")
    L.append("")
    L.append("| Reg | Word | A | B | C | U | total | archetype |")
    L.append("|---:|---|---:|---:|---:|---:|---:|---|")

    by_reg: dict = defaultdict(list)
    for t in terms:
        by_reg[(t["reg_no"], t["reg_word"])].append(t)

    archetype_counts: dict = defaultdict(int)
    for (reg_no, word) in sorted(by_reg.keys()):
        bucket = by_reg[(reg_no, word)]
        a = sum(1 for t in bucket if t["tier"] == "A")
        b = sum(1 for t in bucket if t["tier"] == "B")
        c = sum(1 for t in bucket if t["tier"] == "C")
        u = sum(1 for t in bucket if t["tier"] == "U")
        tot = a + b + c + u
        if a == 1 and (b + c) > 0:
            arch = "single-pillar"
        elif a >= 2:
            arch = "multi-pillar"
        elif a == 0 and u == tot:
            arch = "unanalysed"
        elif a == 0 and (b + c == 0):
            arch = "thin"
        elif a == 0 and b > 0:
            arch = "distributed"
        elif a == 0 and c == tot:
            arch = "thin"
        else:
            arch = "mixed-no-primary"
        archetype_counts[arch] += 1
        L.append(f"| {reg_no} | {word} | {a} | {b} | {c} | {u} | {tot} | {arch} |")
    L.append("")

    # Archetype summary
    L.append("### Archetype summary across 214 registries")
    L.append("")
    L.append("| Archetype | n |")
    L.append("|---|---:|")
    for arch, n in sorted(archetype_counts.items(), key=lambda x: -x[1]):
        L.append(f"| {arch} | {n} |")
    L.append("")

    # Top Primary list
    L.append("## All Primary (Tier A) terms — full list")
    L.append("")
    L.append("Ordered by anchor count, then vc_relevant.")
    L.append("")
    primaries = sorted(by_tier["A"],
                       key=lambda t: (-t["anchors"], -t["vc_rel"]))
    L.append("| reg | word | strongs | translit | gloss | lang | status | anchors | groups | vc_rel | xref→ |")
    L.append("|---:|---|---|---|---|---|---|---:|---:|---:|---:|")
    for t in primaries:
        L.append(f"| {t['reg_no']} | {t['reg_word']} | `{t['strongs_number']}` | "
                 f"{t['transliteration'] or ''} | {(t['gloss'] or '')[:30]} | "
                 f"{t['language'][:1]} | `{t['status']}` | {t['anchors']} | "
                 f"{t['groups_active']} | {t['vc_rel']} | {t['xref_into_n_other_regs']} |")
    L.append("")

    # Anomalies — registries with no Primary, all-marginal, all-unanalysed
    no_primary = []
    all_marginal = []
    all_unanalysed = []
    for (reg_no, word), bucket in by_reg.items():
        a = sum(1 for t in bucket if t["tier"] == "A")
        b = sum(1 for t in bucket if t["tier"] == "B")
        c = sum(1 for t in bucket if t["tier"] == "C")
        u = sum(1 for t in bucket if t["tier"] == "U")
        if a == 0:
            no_primary.append((reg_no, word, b, c, u))
        if c > 0 and a == 0 and b == 0 and u == 0:
            all_marginal.append((reg_no, word, c))
        if u > 0 and a == 0 and b == 0 and c == 0:
            all_unanalysed.append((reg_no, word, u))

    L.append("## Anomalies")
    L.append("")
    L.append(f"### Registries with no Primary term ({len(no_primary)})")
    L.append("")
    if no_primary:
        L.append("| Reg | Word | B | C | U |")
        L.append("|---:|---|---:|---:|---:|")
        for reg_no, word, b, c, u in sorted(no_primary):
            L.append(f"| {reg_no} | {word} | {b} | {c} | {u} |")
    else:
        L.append("_None — every registry has at least one Primary term._")
    L.append("")

    L.append(f"### Registries with only Marginal terms ({len(all_marginal)})")
    L.append("")
    if all_marginal:
        L.append("| Reg | Word | C |")
        L.append("|---:|---|---:|")
        for reg_no, word, c in sorted(all_marginal):
            L.append(f"| {reg_no} | {word} | {c} |")
    else:
        L.append("_None._")
    L.append("")

    L.append(f"### Registries with only Unanalysed terms ({len(all_unanalysed)})")
    L.append("")
    if all_unanalysed:
        L.append("| Reg | Word | U |")
        L.append("|---:|---|---:|")
        for reg_no, word, u in sorted(all_unanalysed):
            L.append(f"| {reg_no} | {word} | {u} |")
    else:
        L.append("_None._")
    L.append("")

    return "\n".join(L)


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    terms = fetch_all_terms(conn)
    for t in terms:
        t["tier"] = classify(t)
    conn.close()

    md = render(terms)
    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(md)

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "generator": "_exploratory_term_primacy_tiering_v1_20260503.py",
            "rule_version": "v1",
            "n_terms": len(terms),
        },
        "tiers": {tier: TIER_LABEL[tier] for tier in ("A", "B", "C", "U")},
        "terms": terms,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)

    by_tier: dict = defaultdict(int)
    for t in terms:
        by_tier[t["tier"]] += 1
    print(f"Wrote: {OUT_MD}")
    print(f"Wrote: {OUT_JSON}")
    print(f"Classified {len(terms):,} OWNER terms:")
    for tier in ("A", "B", "C", "U"):
        n = by_tier[tier]
        pct = n / len(terms) * 100 if terms else 0
        print(f"  {tier} {TIER_LABEL[tier]:12s}  {n:5,}  ({pct:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
