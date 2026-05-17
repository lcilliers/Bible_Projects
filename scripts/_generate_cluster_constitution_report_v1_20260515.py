"""Generate cluster constitution report (Phase 3 input).

Per wa-sessionb-cluster-instruction-v2_0-20260515 §6.2 — produces a report whose
heart is the per-term meaning corpora (from Phase 2's `verse_context.analysis_note`),
together with the cluster characteristic statement, cross-term signals, and the
programme cluster catalogue.

Inherited VCGs, sub-groups, anchors are deliberately suppressed (§2.3 — structural
enforcement of the inherited-structure contamination guard).

Also fires the inline `Not started` → `Data - In Progress` status transition for the
cluster if applicable (per §6.1 — one documented exception for `_generate_*` scripts).

Usage:
  python scripts/_generate_cluster_constitution_report_v1_20260515.py --m-cluster M01 [--no-status-transition]

Output:
  Sessions/Session_Clusters/{code}/wa-cluster-{code}-constitution-v{N}-{date}.md
"""
from __future__ import annotations
import argparse, json, os, re, sqlite3, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parent.parent
DB = REPO / "database" / "bible_research.db"
BACKUPS = REPO / "backups" / "row_backups"

# Cross-term overlap threshold: terms with Jaccard ≥ this share enough meaning vocabulary
# to be candidate VCG-sharing pairs. Tunable per cluster.
OVERLAP_JACCARD_THRESHOLD = 0.30
# Stopword set for meaning-vocabulary comparison (small, English-skewed; tuned for theological prose)
STOPWORDS = {
    "the","a","an","and","or","but","of","to","in","is","that","this","these","those",
    "it","its","as","for","with","by","on","at","be","are","was","were","been","being",
    "verse","term","names","describes","name","describes","what","which","when","where",
    "from","into","out","up","down","over","under","not","no","than","then","so","also",
    "one","two","three","first","second","third","new","old","more","most","less","least",
    "him","her","his","hers","they","them","their","he","she","i","you","we","us","our","my",
    "do","does","did","done","have","has","had","will","would","can","could","should","may","might",
    "shall","must","being","becomes","become","came","come","comes","goes","go","went",
    "says","said","speak","spoke","spoken","speech","tells","tell","told","read","reads",
    "characteristic","inner","being","verse","verses","scripture","biblical","passage",
}


def open_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def next_version_for(out_dir: Path, prefix: str, date_str: str) -> str:
    """Return the next version string vN+1 by scanning existing files."""
    pat = re.compile(rf"^{re.escape(prefix)}-v(\d+)-{date_str}\.md$")
    max_v = 0
    if out_dir.exists():
        for p in out_dir.iterdir():
            m = pat.match(p.name)
            if m:
                max_v = max(max_v, int(m.group(1)))
    return f"v{max_v + 1}"


def maybe_transition_status(conn, cluster_code: str, dry_run: bool) -> tuple[str, str | None]:
    """If status is 'Not started', backup + transition to 'Data - In Progress'.
    Returns (current_status_after, backup_path_or_None)."""
    r = conn.execute("SELECT status FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone()
    if not r:
        raise RuntimeError(f"cluster {cluster_code} not found")
    cur = r["status"]
    if cur != "Not started":
        return cur, None
    # Backup row
    BACKUPS.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%dT%H%M%S")
    backup_path = BACKUPS / f"cluster_{cluster_code}_pre_constitution_status_init_{ts}.json"
    full = dict(conn.execute("SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)).fetchone())
    backup_path.write_text(json.dumps(full, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    if not dry_run:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        conn.execute(
            "UPDATE cluster SET status='Data - In Progress', last_updated_date=? "
            "WHERE cluster_code=? AND status='Not started'",
            (now, cluster_code)
        )
        conn.commit()
    return "Data - In Progress", str(backup_path.relative_to(REPO))


def tokenize(text: str) -> set[str]:
    """Simple lowercase word tokens, stripped to >=4 chars, stopwords removed."""
    if not text: return set()
    tokens = re.findall(r"[A-Za-z]+", text.lower())
    return {t for t in tokens if len(t) >= 4 and t not in STOPWORDS}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b: return 0.0
    inter = a & b
    union = a | b
    return len(inter) / len(union) if union else 0.0


def build_report(conn, cluster_code: str, status_after: str, backup_path: str | None) -> str:
    cluster = conn.execute(
        "SELECT * FROM cluster WHERE cluster_code=?", (cluster_code,)
    ).fetchone()
    if not cluster:
        raise RuntimeError(f"cluster {cluster_code} not found")

    # Per-term identity + meaning corpus
    terms = list(conn.execute("""
        SELECT id AS mti_id, strongs_number, transliteration, gloss, language,
               owning_word, status AS mti_status, md_version
        FROM mti_terms
        WHERE cluster_code=? AND status IN ('extracted','extracted_thin')
          AND COALESCE(delete_flagged,0)=0
        ORDER BY strongs_number
    """, (cluster_code,)))

    # Meaning corpus per term (only active is_relevant rows with analysis_note populated)
    meanings_by_term: dict[int, list[dict]] = defaultdict(list)
    vc_state_by_term: dict[int, dict] = defaultdict(lambda: {"g": 0, "p": 0, "sa": 0, "ut": 0})
    for r in conn.execute("""
        SELECT vc.mti_term_id, vc.is_relevant, vc.set_aside_reason, vc.analysis_note,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
        JOIN mti_terms mt ON mt.id = vc.mti_term_id
        WHERE mt.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
          AND mt.status IN ('extracted','extracted_thin') AND COALESCE(mt.delete_flagged,0)=0
        ORDER BY vc.mti_term_id, vr.book_id, vr.chapter, vr.verse_num
    """, (cluster_code,)):
        mti = r["mti_term_id"]
        if r["is_relevant"] == 1 and r["analysis_note"]:
            meanings_by_term[mti].append({"reference": r["reference"], "meaning": r["analysis_note"]})
            vc_state_by_term[mti]["g"] += 1
        elif r["is_relevant"] == 1 and not r["analysis_note"]:
            vc_state_by_term[mti]["p"] += 1
        elif r["set_aside_reason"]:
            vc_state_by_term[mti]["sa"] += 1

    # UT count (no vc row at all) — joined separately
    for r in conn.execute("""
        SELECT mt.id AS mti_id, COUNT(*) AS ut_count
        FROM mti_terms mt
        JOIN wa_verse_records vr ON vr.mti_term_id = mt.id
        LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id AND vc.mti_term_id = mt.id
        WHERE mt.cluster_code=? AND mt.status IN ('extracted','extracted_thin')
          AND COALESCE(mt.delete_flagged,0)=0 AND COALESCE(vr.delete_flagged,0)=0
          AND vc.id IS NULL
        GROUP BY mt.id
    """, (cluster_code,)):
        vc_state_by_term[r["mti_id"]]["ut"] = r["ut_count"]

    # Cross-term overlap (Jaccard on meaning vocabulary)
    vocab_by_term: dict[int, set[str]] = {}
    for mti, mlist in meanings_by_term.items():
        tokens: set[str] = set()
        for m in mlist:
            tokens |= tokenize(m["meaning"])
        vocab_by_term[mti] = tokens

    # Compute pairs above threshold
    term_id_list = list(vocab_by_term.keys())
    overlaps: list[tuple] = []
    for i in range(len(term_id_list)):
        for j in range(i + 1, len(term_id_list)):
            a, b = term_id_list[i], term_id_list[j]
            score = jaccard(vocab_by_term[a], vocab_by_term[b])
            if score >= OVERLAP_JACCARD_THRESHOLD:
                overlaps.append((a, b, score))
    overlaps.sort(key=lambda x: -x[2])

    # Programme cluster catalogue (NAMED clusters)
    other_clusters = list(conn.execute("""
        SELECT cluster_code, short_name, description, status
        FROM cluster
        WHERE bucket='NAMED' AND cluster_code != ?
        ORDER BY cluster_code
    """, (cluster_code,)))

    # ===== Render =====
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines: list[str] = []
    lines.append(f"# {cluster_code} {cluster['description']} — Cluster constitution report")
    lines.append("")
    lines.append(f"**Generated:** {now_iso}  ")
    lines.append(f"**Cluster:** `{cluster_code}` ({cluster['short_name']}) · bucket={cluster['bucket']} · status={status_after} · version={cluster['version']}  ")
    lines.append(f"**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §6 (Phase 3 — Cluster constitution debate)  ")
    if backup_path:
        lines.append(f"**Status transition:** `Not started` → `Data - In Progress` (backup: `{backup_path}`)  ")
    lines.append(f"**Source:** `database/bible_research.db`  ")
    lines.append("")
    lines.append("**Scope of this report:** the per-term meaning corpus from Phase 2 Pass A is the analytical material for the constitution debate. AI evaluates each term against the cluster characteristic statement (§1) using its actual meaning corpus (§2). Cross-term signals (§3) highlight VCG-sharing candidates and possible cluster-transfer cases. The programme cluster catalogue (§4) names candidate destinations for transfer decisions.")
    lines.append("")
    lines.append("**Suppressed by design** (per §2.3 inherited-structure contamination guard): inherited VCGs, sub-group structure, anchor designations, prior session findings. None of these appear in this report.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## §1. Cluster characteristic statement")
    lines.append("")
    lines.append(f"**Cluster {cluster_code} — {cluster['description']}**")
    lines.append("")
    lines.append(f"Gloss list (every term currently in the cluster, by transliteration):")
    lines.append("")
    gloss = cluster["gloss"] or ""
    lines.append(gloss)
    lines.append("")
    lines.append("**Constitution debate task** — for each term in §2:")
    lines.append("")
    lines.append("1. Read the term's meaning corpus.")
    lines.append("2. Verdict: **STAYS** (corpus aligns with the cluster's characteristic) / **TRANSFERS-TO-{cluster}** (corpus aligns with another cluster's characteristic — see §4) / **BOUNDARY** (corpus is supportive, qualifying, or undecided).")
    lines.append("3. Record the rationale in the obslog, rooted in specific meanings.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## §2. Per-term identity + meaning corpus ({len(terms)} terms)")
    lines.append("")
    for t in terms:
        mti = t["mti_id"]
        mlist = meanings_by_term.get(mti, [])
        state = vc_state_by_term[mti]
        translit = (t["transliteration"] or "").strip()
        gloss_t = (t["gloss"] or "").strip()
        owner = (t["owning_word"] or "").strip()
        lines.append(f"### {t['strongs_number']} {translit} — {gloss_t} ({t['language']}; mti_id={mti})")
        lines.append("")
        lines.append(f"- Owning word (Session A registry): {owner!r}")
        lines.append(f"- mti_terms.status: {t['mti_status']}  ·  md_version: {t['md_version']}")
        lines.append(f"- Verse counts: G={state['g']}  P={state['p']}  SA={state['sa']}  UT={state['ut']}")
        lines.append("")
        if not mlist:
            lines.append("_(No Phase 2 meanings yet for this term — meaning corpus empty.)_")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue
        lines.append(f"**Meaning corpus** ({len(mlist)} verses, canonical Bible order):")
        lines.append("")
        lines.append("| Reference | Meaning |")
        lines.append("|---|---|")
        for m in mlist:
            meaning_cell = (m["meaning"] or "").replace("|", "\\|").replace("\n", " ").strip()
            lines.append(f"| {m['reference']} | {meaning_cell} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## §3. Cross-term signals")
    lines.append("")
    if not overlaps:
        lines.append(f"_(No term pairs above the meaning-vocabulary Jaccard threshold {OVERLAP_JACCARD_THRESHOLD}. "
                     f"Either the cluster is genuinely diverse, or the meanings are highly term-specific.)_")
        lines.append("")
    else:
        lines.append(f"Term pairs with meaning-vocabulary Jaccard ≥ {OVERLAP_JACCARD_THRESHOLD} — candidate VCG-sharing relationships:")
        lines.append("")
        lines.append("| Term A | Term B | Jaccard | Shared vocabulary (sample) |")
        lines.append("|---|---|---:|---|")
        term_by_id = {t["mti_id"]: t for t in terms}
        for a, b, score in overlaps[:50]:
            shared = sorted(vocab_by_term[a] & vocab_by_term[b])
            shared_cell = ", ".join(shared[:12]) + (f", ... +{len(shared)-12}" if len(shared) > 12 else "")
            ta = term_by_id.get(a, {})
            tb = term_by_id.get(b, {})
            lines.append(f"| {ta.get('strongs_number','?')} {ta.get('transliteration','')} | "
                         f"{tb.get('strongs_number','?')} {tb.get('transliteration','')} | "
                         f"{score:.2f} | {shared_cell} |")
        if len(overlaps) > 50:
            lines.append(f"_(showing top 50 of {len(overlaps)} pairs above threshold)_")
        lines.append("")

    lines.append("**Drift signal — terms whose meaning corpus references vocabulary heavily concentrated in another cluster:**")
    lines.append("")
    lines.append("_(Heuristic deferred to v2 of this tool — for v1 of the constitution report, AI reads the meaning corpus and judges drift manually.)_")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## §4. Programme cluster catalogue")
    lines.append("")
    lines.append(f"Named clusters in the programme (excluding the current cluster {cluster_code}). Use this list to name a destination for TRANSFERS verdicts.")
    lines.append("")
    lines.append("| Cluster code | Short name | Description | Status |")
    lines.append("|---|---|---|---|")
    for c in other_clusters:
        desc = (c["description"] or "")[:120]
        lines.append(f"| `{c['cluster_code']}` | {c['short_name']} | {desc} | {c['status']} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*End of constitution report.*")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m-cluster", required=True)
    ap.add_argument("--no-status-transition", action="store_true",
                    help="Skip the inline 'Not started' → 'Data - In Progress' transition.")
    args = ap.parse_args()

    code = args.m_cluster.strip()
    conn = open_db()
    try:
        status_after, backup_path = (conn.execute(
            "SELECT status FROM cluster WHERE cluster_code=?", (code,)
        ).fetchone()["status"], None) if args.no_status_transition else maybe_transition_status(conn, code, dry_run=False)

        report = build_report(conn, code, status_after, backup_path)

        out_dir = REPO / "Sessions" / "Session_Clusters" / code
        out_dir.mkdir(parents=True, exist_ok=True)
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")
        version = next_version_for(out_dir, f"wa-cluster-{code}-constitution", date_str)
        out_path = out_dir / f"wa-cluster-{code}-constitution-{version}-{date_str}.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Cluster {code}: {status_after}")
        if backup_path:
            print(f"  status transitioned (backup: {backup_path})")
        print(f"Wrote: {out_path.relative_to(REPO)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
