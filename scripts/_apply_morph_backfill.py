"""_apply_morph_backfill.py — L0 of the L1 sweep. Populates wa_verse_records.morph_code / stem from STEP
preview-HTML morphology, per term-occurrence. The ONE structural write of the sweep (additive columns;
reversible by NULLing or restoring the pre-sweep backup).

Matching: STEP gives (ref, morph) per verse for a term's own span; the DB row is
wa_verse_records WHERE mti_term_id = term.id AND reference = ref. Both references originate from STEP, so
they align on the "Gen 43:32" key.

Dry-run reports the REFERENCE MATCH-RATE (the systemic-failure guard) before any write.

Usage:
  python scripts/_apply_morph_backfill.py --cluster M01 --dry-run --out <file>.md
  python scripts/_apply_morph_backfill.py --cluster M01 --live    --out <file>.md
  python scripts/_apply_morph_backfill.py --clusters M02,M03,... --live --out <file>.md
"""
import argparse, os, re, sqlite3, sys
sys.path.insert(0, os.path.join("scripts", "analytics"))
sys.stdout.reconfigure(encoding="utf-8")
from step_client import StepClient
DB = os.path.join("database", "bible_research.db")

SPAN = re.compile(r"<span\s+morph='([^']*)'\s+strong='([^']*)'>([^<]*)</span>", re.I)
HEB_STEM = {"q": "Qal", "N": "Niphal", "p": "Piel", "P": "Pual", "h": "Hiphil", "H": "Hophal",
            "t": "Hithpael", "o": "Polel", "O": "Polal", "r": "Hithpolel", "v": "Hithpael"}


def base(code):
    m = re.match(r"^([HG]\d+)", code or ""); return m.group(1) if m else (code or "")


def morph_for(html, strong):
    want = strong; wbase = base(strong)
    for ma, sa, _t in SPAN.findall(html):
        sc = sa.split(); mc = ma.split()
        for i, s in enumerate(sc):
            if s == want or base(s) == wbase:
                return mc[i] if i < len(mc) else (mc[0] if mc else "")
    return ""


def stem_of(morph):
    if not morph or morph[0] != "H":
        return ""
    body = morph[1:].lstrip("-")
    if body[:1] == "V" and len(body) > 1:
        return HEB_STEM.get(body[1], f"?{body[1]}")
    return ""


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--cluster"); g.add_argument("--clusters")
    m = ap.add_mutually_exclusive_group(required=True)
    m.add_argument("--dry-run", action="store_true"); m.add_argument("--live", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    clusters = [a.cluster] if a.cluster else [x.strip() for x in a.clusters.split(",") if x.strip()]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()
    sc = StepClient()

    L = [f"# L0 morph backfill — {'DRY-RUN' if a.dry_run else 'LIVE'} — {', '.join(clusters)}", ""]
    L.append("> `scripts/_apply_morph_backfill.py`. Populates `wa_verse_records.morph_code`/`stem` from STEP "
             "per term-occurrence, matched on `(mti_term_id, reference)`. Watch the **match-rate**.")
    L.append("")
    L.append("| Cluster | terms | DB rows | STEP verses | matched | DB-only (no morph) | STEP-only (no row) | match% | stems |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    g_written = 0
    for CL in clusters:
        terms = c.execute("SELECT id, strongs_number, transliteration FROM mti_terms "
                          "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY strongs_number",
                          (CL,)).fetchall()
        db_rows = step_verses = matched = step_only = written = 0
        stemc = {}
        db_refs_all = set()
        for t in terms:
            db_refs = {r["reference"] for r in c.execute(
                "SELECT DISTINCT reference FROM wa_verse_records WHERE mti_term_id=? "
                "AND COALESCE(delete_flagged,0)=0 AND reference IS NOT NULL", (t["id"],))}
            db_rows += len(db_refs); db_refs_all |= {(t["id"], r) for r in db_refs}
            try:
                recs, html = sc.get_verse_records_with_html(t["strongs_number"])
            except Exception:
                continue
            for r in recs:
                step_verses += 1
                ref = r["ref"]
                mph = morph_for(html.get(r["osisId"], ""), t["strongs_number"])
                st = stem_of(mph)
                if ref in db_refs:
                    matched += 1
                    if st: stemc[st] = stemc.get(st, 0) + 1
                    if a.live and mph:
                        cur = c.execute("UPDATE wa_verse_records SET morph_code=?, stem=? "
                                        "WHERE mti_term_id=? AND reference=? AND COALESCE(delete_flagged,0)=0",
                                        (mph, st or None, t["id"], ref))
                        written += cur.rowcount
                else:
                    step_only += 1
        if a.live:
            conn.commit()
        g_written += written
        rate = f"{100*matched/step_verses:.0f}%" if step_verses else "—"
        db_only = db_rows - matched
        stems = ", ".join(f"{k}:{v}" for k, v in sorted(stemc.items(), key=lambda x: -x[1])[:6]) or "—"
        L.append(f"| {CL} | {len(terms)} | {db_rows} | {step_verses} | {matched} | {db_only} | {step_only} "
                 f"| {rate} | {stems} |")
        print(f"{CL}: terms {len(terms)} db_rows {db_rows} step {step_verses} matched {matched} "
              f"({rate}) written {written}")
    L.append("")
    L.append(f"**{'WROTE morph to '+str(g_written)+' rows.' if a.live else 'DRY-RUN — no writes.'}** "
             "DB-only = rows STEP did not return a morph for (left NULL); STEP-only = STEP verses with no "
             "matching DB row (expected where our corpus is a subset).")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
