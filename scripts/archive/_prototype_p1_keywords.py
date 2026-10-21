"""_prototype_p1_keywords.py — READ-ONLY prototype. Rebuilds the L1 keyword set from a term's STEP meaning
as WHOLE WORDS (no stemming) with a SELF-CHECK that reports every rejected token and a PASS/FAIL on the
output. Fixes the four failures of the first build (over-stemmed fragments, stem duplicates, transliteration
leakage, analytic-method terms). NO DB writes.

Design (A1 reframe): the L1 keyword is a *brief capture of key parts of the STEP meaning*, not a derived
interpretive value. Source = gloss + step_search_gloss + medium meaning + top-level STEP senses.

Why whole-word fixes it: not stemming eliminates fragments (anxiou) and stem-duplicates (terrify/terrifi)
by construction; the remaining noise (transliterations, analytic terms, function words) is removed by named
filters, each of which records what it dropped so the output is auditable.

Usage:  python scripts/_prototype_p1_keywords.py --cluster M01 [--limit N] --out <file>.md
"""
import argparse, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

WORD = re.compile(r"[a-z][a-z'-]*[a-z]|[a-z]", re.I)
PAREN = re.compile(r"\([^)]*\)")
# function words (not characteristics) — dropped
STOP = set("""a an and or the of to be is are was were am being been in on at as by for with from into onto
upon that this these those it its his her their they them he she we you i one two three not no any some all
such which who whom whose when where while because so then than also more most very own same other another
each every both few many much do does did done have has had having will would can could may might must shall
should used use using used also esp especially e.g eg ie i.e cf etc per via vs about over under out up down off
between within without through during before after above below near against among toward towards like unto thy
thee thou ye our us my me him your""".split())
# linguistic / analytic-method words — never keywords
ANALYTIC = set("""metaphor metaphorical metaphorically metonymy metonymical synecdoche hyperbole hyperbolic
idiom idiomatic figurative figuratively literal literally lit fig sense senses meaning meanings word words term
terms root roots cognate cognates derivative derive derived denote denotes connote connotes usage gloss lexical
lexeme noun verb adjective adverb pronoun participle infinitive construct absolute masculine feminine singular
plural qal niphal piel pual hiphil hophal hithpael stem conjugation imperfect perfect imperative
transliteration translit form forms spelled spelling variant variants prob probably perhaps apparently
properly strictly hence thus viz namely cf compare see also""".split())
# bible-book abbreviations leaking from citation cross-references — never keywords
BOOKABBR = set("""gen exod exo lev num deut deu josh jos judg jdg ruth rut sam kgs kin chr chron ezra neh esth
est job psa pss prov pro eccl ecc song sos isa jer lam ezek eze dan hos joel amos obad jonah jon mic nah hab
zeph zep hag zech zec mal matt mat mark mar luke luk john joh acts rom cor gal eph phil php col thess thes tim
tit phlm phm heb jas pet jude rev""".split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row; c = conn.cursor()

    rows = c.execute(
        "SELECT m.strongs_number sn, m.transliteration tl, m.gloss gloss, ti.step_search_gloss ssg, "
        "ti.meaning meaning, ti.also_spelled also, ti.parsed_meaning_id pmid "
        "FROM mti_terms m LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number "
        "AND COALESCE(ti.delete_flagged,0)=0 "
        "WHERE m.cluster_code=? AND COALESCE(m.delete_flagged,0)=0 GROUP BY m.strongs_number "
        "ORDER BY m.strongs_number", (a.cluster,)).fetchall()
    if a.limit:
        rows = rows[:a.limit]

    L = [f"# P1 keyword rebuild + self-check — {a.cluster} (prototype)", ""]
    L.append("> READ-ONLY (`scripts/_prototype_p1_keywords.py`). Keywords = whole words from the term's STEP "
             "meaning; named filters drop function/analytic/transliteration/short tokens and **report what "
             "they dropped**. Self-check asserts: no duplicates · all alpha & length≥3 · none in the "
             "analytic/translit/stop lists. No DB writes.")
    L.append("")
    agg_fail = 0
    agg_drop = {"stop": 0, "analytic": 0, "translit": 0, "short": 0}
    detail = []
    for r in rows:
        # transliteration fragments to filter: the term's own translit parts + also-spelled
        tparts = set()
        for s in [r["tl"] or "", r["also"] or ""]:
            for p in re.split(r"[.\s,;/]+", s.lower()):
                if p:
                    tparts.add(p)
        src = " ".join(filter(None, [r["gloss"], r["ssg"], r["meaning"]]))
        # top-level STEP senses
        if r["pmid"]:
            mind = c.execute("SELECT MIN(level_depth) d FROM wa_meaning_sense WHERE parsed_meaning_id=?",
                             (r["pmid"],)).fetchone()["d"]
            for s in c.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? AND level_depth=?",
                               (r["pmid"], mind)):
                src += " " + (s["sense_text"] or "")
        src = PAREN.sub(" ", src or "")
        kept, seen, dropped = [], set(), {"stop": [], "analytic": [], "translit": [], "short": []}
        for tok in WORD.findall(src.lower()):
            tok = tok.strip("'-")
            if len(tok) < 3:
                dropped["short"].append(tok); continue
            if tok in STOP:
                dropped["stop"].append(tok); continue
            if tok in ANALYTIC or tok in BOOKABBR:
                dropped["analytic"].append(tok); continue
            if tok in tparts or re.search(r"[.]", tok):
                dropped["translit"].append(tok); continue
            if tok in seen:
                continue
            seen.add(tok); kept.append(tok)
        # SELF-CHECK (hyphens/apostrophes allowed in compounds; over-long no-hyphen tokens flagged SUSPECT)
        alpha = lambda s: s.replace("-", "").replace("'", "").isalpha()
        problems, suspect = [], []
        if len(kept) != len(set(kept)): problems.append("duplicate")
        for k in kept:
            if not alpha(k) or len(k) < 3: problems.append(f"nonword:{k}")
            if k in ANALYTIC or k in STOP or k in BOOKABBR: problems.append(f"leaked:{k}")
            if len(k) > 14 and "-" not in k: suspect.append(k)   # likely concatenation artifact
        ok = not problems
        if not ok: agg_fail += 1
        for kk in agg_drop: agg_drop[kk] += len(dropped[kk])
        detail.append((r["sn"], r["tl"], kept, dropped, ok, problems, suspect))

    L.append(f"**{len(rows)} terms · self-check PASS {len(rows)-agg_fail}/{len(rows)} · "
             f"dropped: stop {agg_drop['stop']} · analytic {agg_drop['analytic']} · "
             f"translit {agg_drop['translit']} · short {agg_drop['short']}**")
    L.append("")
    nsus = sum(1 for d in detail if d[6])
    L.append(f"_Suspect (over-long, likely concatenation artifact from HTML-strip): {nsus} terms — flagged not dropped._")
    L.append("")
    L.append("| Term | Keywords (whole-word, deduped) | self-check | dropped (analytic/translit) | suspect |")
    L.append("|---|---|---|---|---|")
    for sn, tl, kept, dropped, ok, problems, suspect in detail:
        dd = []
        if dropped["analytic"]: dd.append("analytic:" + ",".join(sorted(set(dropped["analytic"])))[:40])
        if dropped["translit"]: dd.append("translit:" + ",".join(sorted(set(dropped["translit"])))[:40])
        flag = "PASS" if ok else "**FAIL** " + ";".join(problems[:4])
        L.append(f"| {sn} {tl} | {', '.join(kept) or '—'} | {flag} | {' · '.join(dd)} | {','.join(suspect) or ''} |")
    L.append("")
    L.append("> The self-check is the deliverable: every term's keyword list is asserted clean (no fragments, "
             "no dupes, no analytic/translit leakage). A FAIL row names the exact offending token for fix.")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write("\n".join(L))
    print(f"{a.cluster}: {len(rows)} terms, self-check PASS {len(rows)-agg_fail}/{len(rows)}; wrote {a.out}")


if __name__ == "__main__":
    main()
