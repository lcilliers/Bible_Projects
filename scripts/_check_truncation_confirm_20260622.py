"""_check_truncation_confirm_20260622.py — classify the sweep's 62 suspects: real truncation vs scope/span-filter.

For each suspect, re-pull via the FIXED client and apply the definitive **chapter-cutoff** test in the
term's own densest book: cap-truncation leaves a clean canonical cutoff (DB covers a dense book only up
to chapter X while STEP continues far beyond — like rāšāʿ Psalms 41/147, lev too). Span-filter/scope gaps
are scattered (DB has some coverage throughout). Read-only.

  python scripts/_check_truncation_confirm_20260622.py
"""
import json, os, re, sqlite3, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
from step_client import StepClient
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
CKPT = "outputs/_tmp_truncation_sweep_ckpt.jsonl"
REPORT = "outputs/markdown/wa-step-truncation-sweep-20260622.md"


def main():
    sc = StepClient()
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = [json.loads(l) for l in open(CKPT, encoding="utf-8")]
    susp = [r for r in rows if r["cc"] != "T2" and r["step"] and r["step"] > 60 and (r["gap"] or 0) >= 5]
    susp.sort(key=lambda r: -r["gap"])

    def chs(refs, bk):
        return sorted({int(re.match(r"\S+ (\d+):", x).group(1)) for x in refs if x.startswith(bk + " ")})

    out = []
    for r in susp:
        sn = r["sn"]
        step = [x["ref"] for x in sc.get_verse_records(sn)]
        dbrefs = {x["reference"] for x in c.execute(
            "SELECT DISTINCT reference FROM wa_verse_records WHERE mti_term_id=?", (r["id"],))}
        absent = set(step) - dbrefs
        # term's own densest book IN THE DB (the book it is clearly studied in)
        db_books = Counter(x.split()[0] for x in dbrefs)
        verdict, detail = "scope/span", ""
        if db_books:
            dbk = db_books.most_common(1)[0][0]
            db_ch, st_ch = chs(dbrefs, dbk), chs(step, dbk)
            if db_ch and st_ch:
                dmax, smax = max(db_ch), max(st_ch)
                beyond = sum(1 for ch in st_ch if ch > dmax)
                # clean cutoff: DB stops well before STEP's reach in its OWN densest book, with real tail
                if smax >= dmax * 1.4 and beyond >= 3:
                    verdict = "TRUNCATION"
                    detail = f"{dbk}: DB to ch{dmax}, STEP to ch{smax} ({beyond} later chapters present in STEP)"
                else:
                    detail = f"{dbk}: DB ch{dmax} vs STEP ch{smax} (no clean cutoff)"
        out.append({**r, "absent": len(absent), "verdict": verdict, "detail": detail})

    trunc = [o for o in out if o["verdict"] == "TRUNCATION"]
    scope = [o for o in out if o["verdict"] != "TRUNCATION"]
    L = [f"# STEP 60-cap truncation sweep + confirmation — {len(rows)} terms, {len(susp)} non-T2 suspects", "",
         "_Read-only. STEP true total (oracle) vs DB; suspects confirmed by the chapter-cutoff test in each "
         "term's own densest book. Run 2026-06-22 on the fixed client._", "",
         f"- **Confirmed TRUNCATION** (clean canonical cutoff, recoverable like rāšāʿ): **{len(trunc)}**",
         f"- Scope / span-filter gaps (scattered — legitimate, NOT cap-truncation): {len(scope)}",
         "",
         "> A high STEP−DB gap on a *polysemous* term is mostly legitimate span-filter (the cluster keeps only "
         "the inner-being sense). Only a **clean chapter cutoff** in the term's own densest book proves the cap "
         "silently dropped recoverable verses. Even there, the recoverable inner-being count is a subset of the "
         "raw gap — re-ingest via the fixed client (engine audit_word per registry) lets the span-filter re-select.",
         "",
         "## Confirmed truncation (fix candidates, worst first)", "",
         "| Strong's | term | cluster | STEP | DB | gap | cutoff evidence |", "|---|---|---|---|---|---|---|"]
    for o in sorted(trunc, key=lambda x: -x["gap"]):
        L.append(f"| {o['sn']} | {o['tr']} ({o['gloss']}) | {o['cc']} | {o['step']} | {o['db']} | {o['gap']} | {o['detail']} |")
    L += ["", "## Scope / span-filter (high gap but scattered — not cap-truncation)", "",
          "| Strong's | term | cluster | STEP | DB | gap | densest-book pattern |", "|---|---|---|---|---|---|---|"]
    for o in sorted(scope, key=lambda x: -x["gap"])[:40]:
        L.append(f"| {o['sn']} | {o['tr']} ({o['gloss']}) | {o['cc']} | {o['step']} | {o['db']} | {o['gap']} | {o['detail']} |")
    open(REPORT, "w", encoding="utf-8").write("\n".join(L))
    print(f"WROTE {REPORT}")
    print(f"CONFIRMED TRUNCATION: {len(trunc)} | scope/span: {len(scope)}")
    for o in sorted(trunc, key=lambda x: -x["gap"]):
        print(f"  TRUNC {o['sn']:8} {o['tr']:10} {o['cc']:5} STEP={o['step']} DB={o['db']} | {o['detail']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
