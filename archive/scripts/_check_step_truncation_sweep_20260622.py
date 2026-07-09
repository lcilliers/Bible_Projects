"""_check_step_truncation_sweep_20260622.py — programme-wide sweep for the STEP 60-cap truncation.

For every active, cluster-assigned OWNER term, compare STEP's reported TRUE total (first-call, no range
— the completeness oracle) against the DB occurrence count. A term with STEP_total > DB AND STEP_total > 60
is a cap-truncation suspect (only terms exceeding 60 in a section could be silently truncated by the old
split). Read-only. Resumable (skips terms already in the checkpoint). Writes a ranked report.

  python scripts/_check_step_truncation_sweep_20260622.py [--limit N]
"""
import argparse, json, os, sqlite3, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
from step_client import StepClient
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
CKPT = "outputs/_tmp_truncation_sweep_ckpt.jsonl"
REPORT = "outputs/markdown/wa-step-truncation-sweep-20260622.md"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sc = StepClient()

    terms = cur.execute("""
        SELECT m.id, m.strongs_number sn, m.transliteration tr, m.gloss, m.cluster_code cc,
               COUNT(DISTINCT CASE WHEN COALESCE(vr.delete_flagged,0)=0 THEN vr.reference END) db_active
        FROM mti_terms m
        JOIN wa_verse_records vr ON vr.mti_term_id=m.id
        WHERE m.cluster_code IS NOT NULL AND COALESCE(m.delete_flagged,0)=0
        GROUP BY m.id ORDER BY db_active DESC""").fetchall()
    if a.limit:
        terms = terms[:a.limit]

    done = {}
    if os.path.exists(CKPT):
        for line in open(CKPT, encoding="utf-8"):
            r = json.loads(line); done[r["id"]] = r
    fh = open(CKPT, "a", encoding="utf-8")
    t0 = time.time()
    for i, t in enumerate(terms, 1):
        if t["id"] in done:
            continue
        sn = t["sn"]
        try:
            total = sc._search_range(sn).get("total", 0)
            if total == 0 and sn and sn[-1].isalpha():           # letter-suffix fallback
                total = sc._search_range(sc._resolved_strong(sn)).get("total", 0)
        except Exception as e:
            total = -1
        rec = {"id": t["id"], "sn": sn, "tr": t["tr"], "gloss": t["gloss"], "cc": t["cc"],
               "db": t["db_active"], "step": total, "gap": (total - t["db_active"]) if total >= 0 else None}
        fh.write(json.dumps(rec) + "\n"); fh.flush(); done[t["id"]] = rec
        if i % 100 == 0:
            print(f"  {i}/{len(terms)}  ({time.time()-t0:.0f}s)")
    fh.close()

    # ---- report ----
    rows = list(done.values())
    # T2 = grammatical co-terms: only ingested inside focus-term verses by design, so a gap is EXPECTED,
    # not truncation. Real truncation suspects are non-T2 FOCUS terms with STEP>60 and a material gap.
    susp = [r for r in rows if r["cc"] != "T2" and r["step"] is not None and r["step"] > 60 and r["gap"] and r["gap"] >= 5]
    susp.sort(key=lambda r: -r["gap"])
    t2 = [r for r in rows if r["cc"] == "T2" and (r["gap"] or 0) > 0]
    span = [r for r in rows if r["cc"] != "T2" and r["step"] is not None and 0 < (r["gap"] or 0) and r["step"] <= 60]
    errs = [r for r in rows if r["step"] == -1]
    L = [f"# STEP 60-cap truncation sweep — {len(rows)} cluster-assigned OWNER terms", "",
         "_Read-only. STEP true total (oracle) vs DB occurrence count. Run 2026-06-22 on the **fixed** client._", "",
         f"- **Truncation suspects** (non-T2 focus terms, STEP>60 and STEP−DB ≥ 5): **{len(susp)}** — need contiguity confirmation (truncation vs legitimate span-filter/scope)",
         f"- T2 grammatical co-terms with a gap (EXPECTED by design — sampled only in focus verses, not truncation): {len(t2)}",
         f"- Non-T2 sub-cap gaps (STEP ≤ 60, span-filter / set-aside — not cap-truncation): {len(span)}",
         f"- Query errors: {len(errs)}", "",
         "> A non-T2 gap is a *suspect*, not a confirmed truncation: it can also be legitimate span-filter "
         "(literal-sense occurrences) or scope set-aside. Confirm by re-pulling via the fixed client and "
         "checking whether the missing verses form **contiguous ranges** (truncation, like rāšāʿ) vs **scattered** (span-filter).", "",
         "## Truncation suspects (non-T2 focus terms, worst first)", "",
         "| Strong's | term | cluster | STEP | DB | gap |", "|---|---|---|---|---|---|"]
    for r in susp:
        L.append(f"| {r['sn']} | {r['tr']} ({r['gloss']}) | {r['cc']} | {r['step']} | {r['db']} | **{r['gap']}** |")
    L += ["", "## Sub-cap gaps (informational — not cap-truncation)", ""]
    span.sort(key=lambda r: -(r["gap"] or 0))
    for r in span[:40]:
        L.append(f"- {r['sn']} {r['tr']} ({r['cc']}): STEP {r['step']} vs DB {r['db']} (gap {r['gap']})")
    if errs:
        L += ["", "## Query errors", ""] + [f"- {r['sn']} {r['tr']}" for r in errs]
    open(REPORT, "w", encoding="utf-8").write("\n".join(L))
    print(f"\nWROTE {REPORT}")
    print(f"truncation suspects: {len(susp)} | sub-cap gaps: {len(span)} | errors: {len(errs)}")
    for r in susp[:15]:
        print(f"  SUSPECT {r['sn']:8} {r['tr']:14} {r['cc']:5} STEP={r['step']} DB={r['db']} gap={r['gap']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
