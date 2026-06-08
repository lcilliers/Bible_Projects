"""_assess_p2_verse_scenarios.py — READ-ONLY. Types every verse of a cluster into the L2 decision-scenario
space and measures, per scenario, whether the STEP signal needed to DECIDE it is actually present.

Purpose (researcher 2026-06-08): the qualifier "pull-through" lives in L2. L2 may split into separate
decision processes (qualifier+term · multi-term-same-cluster · multi-cluster) — and possibly more. This
prototype answers: (a) what is the real distribution of decision scenarios across a cluster's verses, and
(b) does the STEP meaning (span match · sub-gloss · morph/stem · sense multiplicity) carry the decision, or
will L2 need a deeper read? No DB writes.

Scenario taxonomy (a verse can trigger SEVERAL — they compose, they are not a partition):
  S0 set-aside     : occurrence not relevant in context (legacy is_relevant=0 / set_aside_reason)
  S1 clean single  : exactly one in-cluster char, single sense, no other-cluster, no qualifier  -> pure L1
  S2 multi-sense   : an in-cluster char with >1 STEP sense  -> L2 sense-resolution
  S3 same-cluster  : >=2 in-cluster chars in the verse      -> pair (sibling span) vs distinct
  S4 qualifier     : a T2 qualifier co-present with an in-cluster char -> route qualifier occurrence in
  S5 cross-cluster : an other-cluster char co-present with an in-cluster char -> reciprocal / multi-belong
  (S6 qualifier-orphan: qualifier with NO char in verse — not reachable from a cluster's own ref-set)

Usage:  python scripts/_assess_p2_verse_scenarios.py --cluster M01 --out <file>.md
"""
import argparse, os, sqlite3, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
MCLUS = lambda cc: cc is not None and cc not in ("T2", "FLAG")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    CL = a.cluster
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    clus, strg = {}, {}
    for r in c.execute("SELECT id, cluster_code, strongs_number FROM mti_terms WHERE COALESCE(delete_flagged,0)=0"):
        clus[r["id"]] = r["cluster_code"]; strg[r["id"]] = r["strongs_number"]
    # true multi-sense = count of DEPTH-1 (top-level) STEP senses per term (not sense-tree nodes)
    sense_n = {}
    for r in c.execute(
        "SELECT ti.strongs_number sn, COUNT(*) n FROM wa_term_inventory ti "
        "JOIN wa_meaning_sense s ON s.parsed_meaning_id = ti.parsed_meaning_id "
        "WHERE ti.parsed_meaning_id IS NOT NULL AND s.level_depth = "
        "  (SELECT MIN(level_depth) FROM wa_meaning_sense WHERE parsed_meaning_id = ti.parsed_meaning_id) "
        "GROUP BY ti.strongs_number"):
        sense_n[r["sn"]] = r["n"]

    # references that contain at least one active CL term
    cl_ids = [i for i, cc in clus.items() if cc == CL]
    qs = ",".join("?" * len(cl_ids))
    cl_refs = set(r[0] for r in c.execute(
        f"SELECT DISTINCT reference FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 "
        f"AND reference IS NOT NULL AND mti_term_id IN ({qs})", cl_ids))

    # all active occurrences at those references
    occ = defaultdict(list)
    qr = ",".join("?" * len(cl_refs))
    for r in c.execute(
        f"SELECT id, reference, mti_term_id, transliteration, span_strong_match, "
        f"morph_code, stem FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 "
        f"AND reference IN ({qr})", list(cl_refs)):
        occ[r["reference"]].append(r)

    # legacy relevance per (verse_record) — what L1 must RE-EVALUATE
    irrel = set()
    for r in c.execute("SELECT verse_record_id FROM verse_context "
                       "WHERE COALESCE(delete_flagged,0)=0 AND COALESCE(is_relevant,1)=0"):
        irrel.add(r["verse_record_id"])

    # signal population (over CL occurrences only)
    sig = {"span": 0, "morph": 0, "stem": 0, "n_cl_occ": 0}
    tally = defaultdict(int)
    compound = 0
    samples = defaultdict(list)

    for ref, rows in occ.items():
        cl_occ = [x for x in rows if clus.get(x["mti_term_id"]) == CL]
        other = [x for x in rows if MCLUS(clus.get(x["mti_term_id"])) and clus.get(x["mti_term_id"]) != CL]
        qual = [x for x in rows if clus.get(x["mti_term_id"]) == "T2"]
        if not cl_occ:
            continue
        n_in = len(cl_occ)
        multi = any(sense_n.get(strg.get(x["mti_term_id"]), 1) > 1 for x in cl_occ)
        setaside = any(x["id"] in irrel for x in cl_occ)
        for x in cl_occ:
            sig["n_cl_occ"] += 1
            if x["span_strong_match"]: sig["span"] += 1
            if x["morph_code"]: sig["morph"] += 1
            if x["stem"]: sig["stem"] += 1

        flags = []
        if setaside: flags.append("S0")
        if n_in == 1 and not other and not qual and not multi: flags.append("S1")
        if multi: flags.append("S2")
        if n_in >= 2: flags.append("S3")
        if qual and n_in >= 1: flags.append("S4")
        if other and n_in >= 1: flags.append("S5")
        for f in flags: tally[f] += 1
        decision_flags = [f for f in flags if f != "S0"]
        if len([f for f in flags if f in ("S2", "S3", "S4", "S5")]) > 1:
            compound += 1
            tally["COMPOUND"] += 1
        # collect a few samples per scenario, with the STEP signal present
        for f in flags:
            if len(samples[f]) < 6:
                others_s = ",".join(sorted(set(clus.get(x["mti_term_id"]) or "—" for x in other)))
                spans = sorted(set(x["span_strong_match"] for x in cl_occ if x["span_strong_match"]))
                samples[f].append((ref,
                                   "+".join(x["transliteration"] or strg.get(x["mti_term_id"]) or "?" for x in cl_occ),
                                   f"other={others_s}" if other else "",
                                   f"qual={len(qual)}" if qual else "",
                                   f"span={'Y' if spans else '-'}",
                                   f"morph={'Y' if any(x['morph_code'] for x in cl_occ) else '-'}"))

    nrefs = len([r for r in cl_refs if any(clus.get(x["mti_term_id"]) == CL for x in occ[r])])
    def pct(n): return f"{100*n/nrefs:.0f}%" if nrefs else "—"
    def spct(n): return f"{100*n/sig['n_cl_occ']:.0f}%" if sig['n_cl_occ'] else "—"

    L = [f"# {CL} — L2 decision-scenario typing + STEP-signal sufficiency (prototype)", ""]
    L.append(f"> READ-ONLY (`scripts/_assess_p2_verse_scenarios.py --cluster {CL}`). Types every {CL} verse "
             "into the L2 decision-scenario space and measures whether the STEP signal to decide it is present. "
             "A verse can trigger several scenarios (they compose).")
    L.append("")
    L.append(f"**{CL}: {nrefs} verses (references), {sig['n_cl_occ']} in-cluster occurrences.**")
    L.append("")
    L.append("## Scenario distribution (verses; non-exclusive)")
    L.append(""); L.append("| Scenario | Verses | % | Decision needed |"); L.append("|---|---|---|---|")
    rowdesc = {
        "S0": "set-aside / relevance re-eval (Song-6 class)",
        "S1": "**none — pure L1 mechanical**",
        "S2": "L2 sense-resolution (which STEP sense)",
        "S3": "L2 pair (sibling span) vs distinct",
        "S4": "L2 route qualifier occurrence in",
        "S5": "L2 reciprocal / multi-belong (cross-cluster)",
        "COMPOUND": "**>1 decision in one verse (compose)**",
    }
    for k in ("S1", "S0", "S2", "S3", "S4", "S5", "COMPOUND"):
        L.append(f"| {k} {rowdesc[k]} | {tally.get(k,0)} | {pct(tally.get(k,0))} | |")
    L.append("")
    L.append("## STEP-signal population (over in-cluster occurrences)")
    L.append("")
    L.append("| Signal | Present | Carries which decision |"); L.append("|---|---|---|")
    L.append(f"| `span_strong_match` | {sig['span']} ({spct(sig['span'])}) | S3 pairing · S4 qualifier-attach |")
    L.append(f"| `morph_code` | {sig['morph']} ({spct(sig['morph'])}) | S2 sense-resolution (stem→branch) |")
    L.append(f"| `stem` | {sig['stem']} ({spct(sig['stem'])}) | S2 sense-resolution |")
    L.append("")
    L.append("> If a signal is sparsely populated, L2 cannot lean on it yet — it needs a STEP backfill or a "
             "deeper read. That is the key finding for 'will L2 STEP meaning suffice'.")
    L.append("")
    for k in ("S2", "S3", "S4", "S5"):
        L.append(f"## Sample — {k} {rowdesc[k]}")
        L.append(""); L.append("| Ref | In-cluster terms | Other | Qual | span | morph |")
        L.append("|---|---|---|---|---|---|")
        for s in samples.get(k, []):
            L.append("| " + " | ".join(s) + " |")
        L.append("")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{CL}: {nrefs} verses | " + " ".join(f"{k}={tally.get(k,0)}" for k in ("S1","S0","S2","S3","S4","S5","COMPOUND")))
    print(f"signals: span {spct(sig['span'])} morph {spct(sig['morph'])} stem {spct(sig['stem'])} (of {sig['n_cl_occ']} occ)")
    print(f"Wrote {a.out}")


if __name__ == "__main__":
    main()
