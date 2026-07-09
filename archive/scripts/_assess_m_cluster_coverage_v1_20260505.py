"""_assess_m_cluster_coverage_v1_20260505.py — read-only.

Per-term verse-coverage report for a named-characteristic M-cluster, with
per-term counts of related Session-B findings and Session-D pointers.

For each term in the chosen M-cluster (drawn from the v6 term-anchor):

  Verse coverage (precedence over verse_context rows):
    - analysed:     verse has a verse_context_group assignment
    - set_aside:    verse has a set_aside_reason
    - not_relevant: verse marked is_relevant=0
    - pending_in_vc: in VC but undecided
    - untouched:    in wa_verse_records but no VC row at all

  Findings/pointers attached to the term:
    - findings_direct: findings whose finding-text mentions this term's
      Strong's number directly
    - findings_registry: findings whose owning registry matches this term's
      owning_registry (broader topical context)
    - pointers_direct: SD pointers whose strongs_reference matches this term
      OR whose description mentions this Strong's

Coverage % = (analysed + set_aside + not_relevant) / active.
Fully covered = pending = 0.

Optional: surface T1-bucketed terms from a related legacy C-cluster that
landed in a *different* M-cluster (--c-cluster) — these are candidates the
researcher may want to reassess as belonging to this M-cluster.

Usage:
  python scripts/_assess_m_cluster_coverage_v1_20260505.py --m-cluster M05
  python scripts/_assess_m_cluster_coverage_v1_20260505.py --m-cluster M05 --c-cluster C17
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

STRONGS_RE = re.compile(r"\b([HG]\d{4}[A-Z]?)\b")
ANCHOR_REF_RE = re.compile(
    r"\b(\d?[A-Za-z]{2,5})\s+(\d{1,3}):(\d{1,3})(?:-(\d{1,3}))?",
)
ANCHOR_PAREN_RE = re.compile(r"\([^)]*\)")


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

DB_PATH = os.path.join("database", "bible_research.db")
V6_PATH = "archive/Clusters/wa-term-anchor-v6-20260504.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_v6():
    with open(V6_PATH, encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True,
                    help="M-cluster ID (e.g. M05)")
    ap.add_argument("--c-cluster", default=None,
                    help="optional legacy C-cluster to flag candidate "
                         "T1-terms-not-in-this-M-cluster (e.g. C17)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    _dest_dir = os.path.join("Sessions", "Session_Clusters", args.m_cluster)
    os.makedirs(_dest_dir, exist_ok=True)
    out_path = args.out or os.path.join(
        _dest_dir,
        f"wa-cluster-{args.m_cluster.lower()}-coverage-"
        f"v1-{datetime.now().strftime('%Y%m%d')}.md"
    )

    v6 = load_v6()
    cluster_labels = v6.get("meaning_cluster_labels", {})
    m_label = cluster_labels.get(args.m_cluster, "?")
    print(f"M-cluster {args.m_cluster}: {m_label}", flush=True)

    # All Strong's currently in this M-cluster
    m_terms = [
        (s, t) for s, t in v6["term_anchors"].items()
        if t.get("cluster_id") == args.m_cluster
    ]
    print(f"Terms in {args.m_cluster}: {len(m_terms)}", flush=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Map Strong's -> mti_terms metadata (id, owning_registry_fk, gloss, etc.)
    strongs_list = [s for s, _ in m_terms]
    placeholders = ",".join("?" * len(strongs_list))
    db_terms = conn.execute(f"""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.gloss,
               mt.transliteration, mt.language, mt.status,
               mt.owning_registry_fk, wr.no AS reg_no, wr.word AS reg_word,
               wr.cluster_assignment
          FROM mti_terms mt
          LEFT JOIN word_registry wr ON wr.id = mt.owning_registry_fk
         WHERE mt.strongs_number IN ({placeholders})
    """, strongs_list).fetchall()
    db_by_strong = {t["strongs_number"]: dict(t) for t in db_terms}
    mti_ids = [t["mti_id"] for t in db_terms if t["mti_id"]]
    placeholders_t = ",".join("?" * len(mti_ids))

    # Per-verse-record status (same precedence query as C-cluster script)
    print("Computing per-verse-record status...", flush=True)
    vc_status = {mid: {"active": 0, "analysed": 0, "set_aside": 0,
                       "not_relevant": 0, "pending_in_vc": 0, "untouched": 0}
                 for mid in mti_ids}
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
               SUM(CASE WHEN active_vc_rows = 0 THEN 1 ELSE 0 END) AS untouched
          FROM verse_status
         GROUP BY mti_term_id
    """, mti_ids).fetchall()
    for r in rows:
        mid = r["mti_term_id"]
        if mid not in vc_status:
            continue
        for k in ("active", "analysed", "set_aside", "not_relevant",
                  "pending_in_vc", "untouched"):
            vc_status[mid][k] = r[k] or 0

    # Pull all active findings + pointers, parse Strong's references from
    # text, and build per-term counts.
    print("Indexing findings + SD pointers...", flush=True)
    findings = conn.execute("""
        SELECT id, finding_id, registry_id, finding, anchor_verses
          FROM wa_session_b_findings
         WHERE COALESCE(delete_flag,0) = 0
    """).fetchall()
    pointers = conn.execute("""
        SELECT id, registry_id, flag_label, strongs_reference,
               description, cross_registry_id
          FROM wa_session_research_flags
         WHERE COALESCE(resolved,0) = 0
           AND flag_code = 'SD_POINTER'
    """).fetchall()

    # Per-strong's: direct mentions (text contains the Strong's)
    findings_direct = defaultdict(set)
    pointers_direct = defaultdict(set)
    # Per-registry: count of findings owned by that registry
    findings_by_registry = defaultdict(set)
    pointers_by_registry = defaultdict(set)
    # Per-strong's: pointers whose strongs_reference is exactly that strong
    pointers_strongs_ref = defaultdict(set)

    # Also build verse-record location index for M-terms so we can resolve
    # finding anchor_verses → M-cluster term
    print("Indexing verse-record locations for M-cluster terms...", flush=True)
    book_lookup = build_book_lookup(conn)
    verse_index = defaultdict(set)  # (book_id, chapter, verse_num) -> {strong}
    if mti_ids:
        ph_t = ",".join("?" * len(mti_ids))
        # Build mti_id -> strong from the actual db rows (not zip)
        mti_to_strong = {
            t["mti_id"]: t["strongs_number"]
            for t in db_terms if t["mti_id"]
        }
        for r in conn.execute(f"""
            SELECT vr.book_id, vr.chapter, vr.verse_num, vr.mti_term_id
              FROM wa_verse_records vr
             WHERE COALESCE(vr.delete_flagged,0) = 0
               AND vr.mti_term_id IN ({ph_t})
        """, mti_ids).fetchall():
            mid = r["mti_term_id"]
            if mid in mti_to_strong:
                verse_index[(r["book_id"], r["chapter"], r["verse_num"])].add(
                    mti_to_strong[mid]
                )

    # Per-strong's: findings linked via anchor verses
    findings_anchor = defaultdict(set)

    target_set = set(strongs_list)
    for f in findings:
        text = " | ".join([f["finding"] or "", f["anchor_verses"] or ""])
        refs = set(STRONGS_RE.findall(text)) & target_set
        for s in refs:
            findings_direct[s].add(f["id"])
        if f["registry_id"]:
            findings_by_registry[f["registry_id"]].add(f["id"])
        # Anchor-verse resolution
        anchor_text = f["anchor_verses"]
        if anchor_text:
            for bid, chap, vnum in parse_anchor_verses(anchor_text,
                                                       book_lookup):
                for s in verse_index.get((bid, chap, vnum), set()):
                    findings_anchor[s].add(f["id"])
    for p in pointers:
        sref = (p["strongs_reference"] or "")
        text = " | ".join([p["description"] or "", sref])
        # parse strong's from full text
        refs = set(STRONGS_RE.findall(text)) & target_set
        for s in refs:
            pointers_direct[s].add(p["id"])
        # exact strongs_reference field
        sref_strongs = set(STRONGS_RE.findall(sref)) & target_set
        for s in sref_strongs:
            pointers_strongs_ref[s].add(p["id"])
        if p["registry_id"]:
            pointers_by_registry[p["registry_id"]].add(p["id"])
        if p["cross_registry_id"]:
            pointers_by_registry[p["cross_registry_id"]].add(p["id"])

    # Build per-term records, joining v6 metadata + DB metadata + status
    # + finding/pointer counts
    term_records = []
    for s, anchor in m_terms:
        db = db_by_strong.get(s, {})
        mid = db.get("mti_id")
        s_info = vc_status.get(mid, {"active": 0, "analysed": 0,
                                     "set_aside": 0, "not_relevant": 0,
                                     "pending_in_vc": 0, "untouched": 0})
        active = s_info["active"]
        covered = (s_info["analysed"] + s_info["set_aside"]
                   + s_info["not_relevant"])
        pending = s_info["pending_in_vc"] + s_info["untouched"]
        cov_pct = (covered / active * 100.0) if active else 100.0
        reg_id = db.get("owning_registry_fk")
        n_find_direct = len(findings_direct.get(s, set()))
        n_find_anchor = len(findings_anchor.get(s, set()))
        n_find_registry = (
            len(findings_by_registry.get(reg_id, set()))
            if reg_id else 0
        )
        n_ptr_direct = len(pointers_direct.get(s, set()))
        n_ptr_strongs_ref = len(pointers_strongs_ref.get(s, set()))
        n_ptr_registry = (
            len(pointers_by_registry.get(reg_id, set()))
            if reg_id else 0
        )
        term_records.append({
            "strong": s,
            "gloss": anchor.get("gloss") or db.get("gloss"),
            "translit": anchor.get("transliteration")
                        or db.get("transliteration"),
            "lang": anchor.get("lang") or (db.get("language", "")[:1]),
            "bucket": anchor.get("bucket"),
            "cluster_source": anchor.get("cluster_source"),
            "legacy_cluster_id": anchor.get("legacy_cluster_id"),
            "registry": (
                f"R{db['reg_no']:03d} {db['reg_word']}"
                if db.get("reg_no") else None
            ),
            "registry_c_cluster": db.get("cluster_assignment"),
            "active": active,
            "analysed": s_info["analysed"],
            "set_aside": s_info["set_aside"],
            "not_relevant": s_info["not_relevant"],
            "pending_in_vc": s_info["pending_in_vc"],
            "untouched": s_info["untouched"],
            "covered": covered,
            "pending": pending,
            "coverage_pct": cov_pct,
            "fully_covered": pending == 0 and active > 0,
            "no_verses": active == 0,
            "n_find_direct": n_find_direct,
            "n_find_anchor": n_find_anchor,
            "n_find_registry": n_find_registry,
            "n_ptr_direct": n_ptr_direct,
            "n_ptr_strongs_ref": n_ptr_strongs_ref,
            "n_ptr_registry": n_ptr_registry,
        })
    term_records.sort(key=lambda x: -x["active"])

    # Roll-up
    total_terms = len(term_records)
    fully = sum(1 for t in term_records if t["fully_covered"])
    zero = sum(1 for t in term_records if t["no_verses"])
    pending_term_count = total_terms - fully - zero
    total_active = sum(t["active"] for t in term_records)
    total_covered = sum(t["covered"] for t in term_records)
    total_untouched = sum(t["untouched"] for t in term_records)
    total_pending_in_vc = sum(t["pending_in_vc"] for t in term_records)
    total_pending = total_untouched + total_pending_in_vc
    cov_pct = (total_covered / total_active * 100.0) if total_active else 100.0

    # Optional: T1-from-C-cluster candidates that aren't in this M-cluster
    candidates = []
    if args.c_cluster:
        c_strongs = conn.execute("""
            SELECT mt.strongs_number, mt.gloss, mt.transliteration,
                   mt.language, wr.no AS reg_no, wr.word AS reg_word
              FROM mti_terms mt
              JOIN word_registry wr ON wr.id = mt.owning_registry_fk
             WHERE wr.cluster_assignment = ?
               AND mt.status NOT IN ('candidate_delete','delete','excluded')
        """, (args.c_cluster,)).fetchall()
        for r in c_strongs:
            s = r["strongs_number"]
            anchor = v6["term_anchors"].get(s)
            if not anchor:
                continue
            if anchor.get("cluster_id") == args.m_cluster:
                continue  # already in M-cluster
            if anchor.get("bucket") != "T1":
                continue  # not T1
            candidates.append({
                "strong": s,
                "gloss": anchor.get("gloss") or r["gloss"],
                "translit": anchor.get("transliteration")
                            or r["transliteration"],
                "lang": anchor.get("lang") or (r["language"] or "")[:1],
                "current_cluster_id": anchor.get("cluster_id"),
                "current_cluster_label": anchor.get("cluster_label"),
                "registry": f"R{r['reg_no']:03d} {r['reg_word']}",
            })
    conn.close()

    # Render
    lines = []
    lines.append(f"# {args.m_cluster} {m_label} — term-level coverage report\n")
    lines.append(f"**Generated:** {now_iso()}  ")
    lines.append(f"**M-cluster:** `{args.m_cluster}` — *{m_label}*  ")
    lines.append(f"**Source anchor:** "
                 f"[wa-term-anchor-v6-20260504.json]"
                 f"(wa-term-anchor-v6-20260504.json)\n")
    lines.append("**Coverage definition:** a term is *fully covered* when "
                 "every active OWNER verse (in `wa_verse_records`) is "
                 "**analysed** (in a `verse_context_group`), explicitly "
                 "**set-aside** with a reason, or marked **not-relevant** "
                 "— i.e. **pending = 0**.  ")
    lines.append("Pending splits into **pending in VC** (verse_context row "
                 "exists but undecided) and **untouched** (no VC row at "
                 "all).  ")
    lines.append("Coverage % = (analysed + set_aside + not_relevant) / "
                 "active.\n")
    lines.append("---\n")

    lines.append("## Cluster headline\n")
    lines.append(f"- **Terms in {args.m_cluster}:** {total_terms}")
    lines.append(f"- **Fully covered:** {fully} ({fully/total_terms*100:.0f}%)"
                 if total_terms else "- **Fully covered:** 0")
    lines.append(f"- **Zero active verses:** {zero}")
    lines.append(f"- **With pending verses:** {pending_term_count}")
    lines.append(f"- **Active verses (sum):** {total_active:,}")
    lines.append(f"- **Covered:** {total_covered:,} "
                 f"({cov_pct:.1f}%)")
    lines.append(f"- **Pending:** {total_pending:,} "
                 f"({total_pending_in_vc} in VC + "
                 f"{total_untouched} untouched)\n")
    # Findings/pointers headline
    n_find_direct_terms = sum(
        1 for t in term_records if t["n_find_direct"] > 0
    )
    n_find_anchor_terms = sum(
        1 for t in term_records if t["n_find_anchor"] > 0
    )
    n_find_any_terms = sum(
        1 for t in term_records
        if t["n_find_direct"] > 0 or t["n_find_anchor"] > 0
    )
    n_ptr_direct_terms = sum(
        1 for t in term_records if t["n_ptr_direct"] > 0
    )
    lines.append(f"- **Terms with direct findings (Strong's-mention):** "
                 f"{n_find_direct_terms} of {total_terms}")
    lines.append(f"- **Terms with anchor-verse-resolved findings:** "
                 f"{n_find_anchor_terms} of {total_terms}")
    lines.append(f"- **Terms with any term-level finding link "
                 f"(D or V):** {n_find_any_terms} of {total_terms}")
    lines.append(f"- **Terms with direct SD pointers:** {n_ptr_direct_terms} "
                 f"of {total_terms}\n")

    # Per-term table
    lines.append("## Per-term coverage + findings/pointers\n")
    lines.append("Sorted by active verses descending. ✅ = fully covered, "
                 "⚠ = has pending verses, — = no active verses.  ")
    lines.append("**Findings (D)** = findings whose text directly mentions "
                 "this Strong's. **Findings (V)** = findings whose "
                 "`anchor_verses` resolve to a verse where this term "
                 "appears (verse-level term linkage). **Findings (R)** = "
                 "findings whose owning registry matches this term's owning "
                 "registry (broader topical context). **Pointers (D)** = SD "
                 "pointers whose `strongs_reference` or description directly "
                 "references this Strong's.\n")
    lines.append("| ✓ | Strong's | Lang | Translit | Gloss | Registry | "
                 "Bucket | Active | Analysed | Set aside | Not relevant | "
                 "Pending in VC | Untouched | Coverage | "
                 "Find (D) | Find (V) | Find (R) | Ptr (D) | Ptr (R) |")
    lines.append("|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|"
                 "---:|---:|---:|---:|---:|---:|---:|")
    for t in term_records:
        mark = "✅" if t["fully_covered"] else (
            "—" if t["no_verses"] else "⚠"
        )
        lang = t["lang"][:1] if t["lang"] else ""
        translit = t["translit"] or ""
        gloss = t["gloss"] or ""
        registry = t["registry"] or "—"
        bucket = t["bucket"] or "—"
        lines.append(
            f"| {mark} | {t['strong']} | {lang} | "
            f"{translit} | {gloss} | {registry} | "
            f"{bucket} | "
            f"{t['active']} | {t['analysed']} | "
            f"{t['set_aside']} | {t['not_relevant']} | "
            f"{t['pending_in_vc']} | {t['untouched']} | "
            f"{t['coverage_pct']:.1f}% | "
            f"{t['n_find_direct']} | {t['n_find_anchor']} | "
            f"{t['n_find_registry']} | "
            f"{t['n_ptr_direct']} | {t['n_ptr_registry']} |"
        )
    lines.append("")

    # Candidates section
    if args.c_cluster:
        lines.append(f"\n## T1 terms from {args.c_cluster} that landed "
                     f"outside {args.m_cluster}\n")
        lines.append(f"These are bucket=**T1** terms whose owning registry is "
                     f"in legacy cluster **{args.c_cluster}** but the term is "
                     f"currently assigned to a different M-cluster (or none). "
                     f"Review whether any of these *fundamentally* belong in "
                     f"**{args.m_cluster}** — the algorithm/curator may have "
                     f"placed them elsewhere.\n")
        if not candidates:
            lines.append("*(no candidates — every T1 term from "
                         f"{args.c_cluster} is already in {args.m_cluster}.)*"
                         )
        else:
            lines.append("| Strong's | Lang | Translit | Gloss | "
                         "Currently in | Registry |")
            lines.append("|---|---|---|---|---|---|")
            for c in sorted(candidates,
                            key=lambda x: (x["current_cluster_id"] or "",
                                           x["strong"])):
                cur = (
                    f"{c['current_cluster_id']} "
                    f"{c['current_cluster_label'] or ''}"
                ).strip() or "—"
                lines.append(
                    f"| {c['strong']} | {c['lang']} | "
                    f"{c['translit'] or ''} | {c['gloss'] or ''} | "
                    f"{cur} | {c['registry']} |"
                )
        lines.append("")

    # Origin breakdown — which legacy clusters fed M05
    lines.append("\n## Legacy crosswalk — where M-cluster terms came from\n")
    from collections import Counter
    legacy_counts = Counter(
        (t["registry"] or "(no registry)") for t in term_records
    )
    legacy_c_counts = Counter(
        (t["registry_c_cluster"] or "(no c-cluster)") for t in term_records
    )
    lines.append("### By owning legacy registry\n")
    lines.append("| Registry | Terms |")
    lines.append("|---|---:|")
    for r, n in legacy_counts.most_common():
        lines.append(f"| {r} | {n} |")
    lines.append("\n### By owning legacy C-cluster\n")
    lines.append("| Legacy C-cluster | Terms |")
    lines.append("|---|---:|")
    for c, n in legacy_c_counts.most_common():
        lines.append(f"| {c} | {n} |")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote: {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
