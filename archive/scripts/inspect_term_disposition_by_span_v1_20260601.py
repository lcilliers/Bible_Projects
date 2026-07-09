"""Term disposition judged on SPAN (actual usage), not on delete_flagged/mti_term_id.

Researcher's rule (2026-06-01):
  - each Strong's term once; each verse for a term once.
  - term linked to a real cluster?            -> CLUSTERED (out of scope here)
  - not linked to a cluster:
      * has span verses (term actually used in the verse)?
          NO  -> DELETE (not attested)
          YES -> REVIEW relevance (relevant=cluster / not=set aside)

Truth signal = wa_verse_records.span_strong_match = 1 (term genuinely used;
target_word present in 99.998% of such rows). Verses deduped by distinct
reference. Terms deduped to strongs_number. delete_flagged is reported only to
show how far the flags have drifted from the truth — it does NOT drive disposition.

Real cluster = cluster_code matching M<digits> (e.g. M03, M10b). FLAG / T2 = holding
pens, treated as NOT in a real cluster.

Read-only.
Output: research/investigations/term-disposition-by-span-20260601.md
  python scripts/inspect_term_disposition_by_span_v1_20260601.py
"""
import os
import re
import sqlite3
from collections import defaultdict

DB = os.path.join("database", "bible_research.db")
OUT = os.path.join("research", "investigations", "term-disposition-by-span-20260601.md")
M_RE = re.compile(r"^M\d")


def main():
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # span verses (actual usage), deduped by reference, grouped by term_id
    span = defaultdict(set)
    for r in cur.execute("SELECT term_id, reference FROM wa_verse_records WHERE span_strong_match=1 AND term_id IS NOT NULL AND reference IS NOT NULL"):
        span[r["term_id"]].add(r["reference"])
    span_n = {k: len(v) for k, v in span.items()}

    # mti_terms grouped by strongs_number
    terms = defaultdict(lambda: {"rows": 0, "clustered": False, "flag": False, "any_live": False,
                                  "gloss": None, "translit": None, "lang": None})
    for r in cur.execute("SELECT strongs_number sn, transliteration tr, gloss, language, cluster_code cc, COALESCE(delete_flagged,0) df FROM mti_terms"):
        t = terms[r["sn"]]
        t["rows"] += 1
        if t["gloss"] is None:
            t["gloss"], t["translit"], t["lang"] = r["gloss"], r["tr"], r["language"]
        if r["cc"] and M_RE.match(r["cc"]):
            t["clustered"] = True
        if r["cc"] in ("FLAG", "T2"):
            t["flag"] = True
        if r["df"] == 0:
            t["any_live"] = True

    # disposition
    rows = []
    for sn, t in terms.items():
        sv = span_n.get(sn, 0)
        if t["clustered"]:
            disp = "CLUSTERED"
        elif sv == 0:
            disp = "DELETE (no usage)"
        else:
            disp = "REVIEW (used, not clustered)"
        rows.append((sn, t, sv, disp))

    # term_ids with span usage but NO mti_terms row (term-list gap)
    no_term = sorted([(tid, n) for tid, n in span_n.items() if tid not in terms and n > 0], key=lambda x: -x[1])

    from collections import Counter
    disp_counts = Counter(r[3] for r in rows)

    # divergence: truth vs the delete flag
    wrongly_deleted = [(sn, t, sv) for sn, t, sv, d in rows if not t["any_live"] and sv > 0]      # all rows deleted, yet used
    should_delete_live = [(sn, t, sv) for sn, t, sv, d in rows if t["any_live"] and not t["clustered"] and sv == 0]  # live, unclustered, unused

    L = ["# Term disposition by span (actual usage) — truth from the data", "",
         "**Generated:** 2026-06-01 (read-only). Disposition driven by `span_strong_match=1` (the term genuinely used in the verse), NOT by `delete_flagged`. Terms deduped to Strong's; verses deduped to distinct reference.", "",
         f"**Distinct Strong's terms: {len(terms)}** (raw mti_terms rows carry {sum(t['rows'] for t in terms.values())}; duplication = OT-DBR-009).", "",
         "## Disposition (researcher rule)", ""]
    for k in ("CLUSTERED", "REVIEW (used, not clustered)", "DELETE (no usage)"):
        L.append(f"- {k}: **{disp_counts.get(k,0)}**")
    L += ["",
          "## Divergence: the flags vs the truth", "",
          f"- **Currently fully-deleted yet HAVE span usage (wrongly deleted): {len(wrongly_deleted)} terms** — these should NOT be deleted; they need review/cluster.",
          f"- Currently live + unclustered + NO span usage (truly deletable): {len(should_delete_live)} terms.",
          f"- Span usages under a `term_id` with NO term row at all (term-list gap): {len(no_term)} term_ids.", "",
          "## Wrongly-deleted (fully deleted, yet used) — top 40 by usage", "",
          "| strongs | translit | gloss | lang | span verses | rows |", "|---|---|---|---|---:|---:|"]
    for sn, t, sv in sorted(wrongly_deleted, key=lambda x: -x[2])[:40]:
        L.append(f"| {sn} | {t['translit'] or ''} | {(t['gloss'] or '').replace('|','/')} | {t['lang'] or ''} | {sv} | {t['rows']} |")

    if no_term:
        L += ["", "## term_ids with usage but no term row (add to term list?)", "", "| term_id | span verses |", "|---|---:|"]
        for tid, n in no_term:
            L.append(f"| {tid} | {n} |")

    L += ["", "## Full disposition list (REVIEW + DELETE, not clustered) — sorted by span verses desc", "",
          "| strongs | translit | gloss | lang | span verses | currently-live? | disposition |", "|---|---|---|---|---:|---|---|"]
    for sn, t, sv, d in sorted([r for r in rows if r[3] != "CLUSTERED"], key=lambda x: -x[2]):
        L.append(f"| {sn} | {t['translit'] or ''} | {(t['gloss'] or '').replace('|','/')} | {t['lang'] or ''} | {sv} | {'yes' if t['any_live'] else 'no'} | {d} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"distinct strongs={len(terms)} | " + " ".join(f"{k}={v}" for k, v in disp_counts.items()))
    print(f"wrongly-deleted (deleted yet used)={len(wrongly_deleted)} | live+unclustered+unused={len(should_delete_live)} | term-list gaps={len(no_term)}")
    print(f"wrote: {OUT}")
    conn.close()


if __name__ == "__main__":
    main()
