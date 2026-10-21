"""_assess_verse_corroboration.py  — READ-ONLY (A1 verse-meaning corroboration scan).

For a cluster, corroborate each verse's derived meaning (verse_context.analysis_note) against the
term's STEP lexical sense-set. v1 = mechanical lexical-overlap triage (Tier 1): it auto-confirms the
verses whose meaning echoes a STEP sense word, and isolates the no-overlap RESIDUE that needs real
(AI / researcher) judgement (Tier 2). Writes a results .md.

This is the gravest-risk audit (A1 in wa-cluster-rollup-design.md). Mechanical, no DB writes.

Usage:
    python scripts/_assess_verse_corroboration.py --cluster M01 --out research/investigations/<file>.md
"""
import argparse, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")

DB = os.path.join("database", "bible_research.db")

# Tokens that carry no sense signal — stripped from both sides before overlap.
STOP = set("""a an and or the of to be is are was were in on at as by for with from into onto upon
that this these those it its he she his her him they them their being been have has had not no any
one two three some all such which who whom whose when where while because so then than also more most
very own same other another each every both few many much own s t state inner outer person someone
something condition manner way thing things qqal niphal piel hiphil hithpael pual hophal twot bdb
means also spelled cause caused causing make made making get got getting""".split())

# Crude stemmer: lowercase, strip punctuation, collapse common suffixes so fear/afraid/feared/fearful
# all collapse toward a comparable stem. Not linguistically perfect — its job is triage recall.
SUFFIXES = ("ingly", "ing", "edly", "ed", "ied", "ies", "ness", "ment", "ful", "less", "ity", "ly",
            "es", "s")

def stem(w):
    w = w.lower()
    for suf in SUFFIXES:
        if len(w) > len(suf) + 2 and w.endswith(suf):
            w = w[: -len(suf)]
            break
    return w

WORD = re.compile(r"[a-zA-Z]+")

def toks(text):
    if not text:
        return set()
    out = set()
    for m in WORD.findall(text):
        if len(m) < 3:
            continue
        sm = stem(m)
        if sm in STOP or len(sm) < 3:
            continue
        out.add(sm)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    terms = c.execute(
        "SELECT id, strongs_number, transliteration, gloss, language, status "
        "FROM mti_terms WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 "
        "ORDER BY id", (args.cluster,)).fetchall()

    lines = []
    grand = dict(terms=0, verses=0, relevant=0, meaning=0, aligned=0, residue=0, nomean=0)
    residue_rows = []  # (term, ref, target, sense_summary, meaning)
    term_summ = []     # (strongs, translit, gloss, n_rel_meaning, aligned, residue)

    for t in terms:
        grand["terms"] += 1
        inv = c.execute(
            "SELECT step_search_gloss, word_analysis_gloss, short_def_mounce, meaning, "
            "parsed_meaning_id FROM wa_term_inventory "
            "WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0",
            (t["strongs_number"],)).fetchone()
        sense_text = ""
        if inv and inv["parsed_meaning_id"]:
            for s in c.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=?",
                               (inv["parsed_meaning_id"],)):
                sense_text += " " + (s["sense_text"] or "")
        # Build the term's STEP sense-token set (the corroboration envelope).
        baseline_text = " ".join(filter(None, [
            t["gloss"],
            inv["step_search_gloss"] if inv else "",
            inv["word_analysis_gloss"] if inv else "",
            inv["short_def_mounce"] if inv else "",
            inv["meaning"] if inv else "",
            sense_text,
        ]))
        sense_tokens = toks(baseline_text)
        sense_summary = ", ".join(sorted(sense_tokens)[:12])

        verses = c.execute(
            "SELECT vc.is_relevant, vc.set_aside_reason, vc.analysis_note, vc.is_anchor, "
            "vr.reference, vr.target_word "
            "FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id "
            "WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0 "
            "ORDER BY vr.book_id, vr.chapter, vr.verse_num", (t["id"],)).fetchall()

        n_aligned = n_res = n_nomean = n_rel = 0
        for v in verses:
            grand["verses"] += 1
            if v["is_relevant"]:
                grand["relevant"] += 1
                n_rel += 1
            note = v["analysis_note"]
            if not note or not note.strip():
                n_nomean += 1
                grand["nomean"] += 1
                continue
            grand["meaning"] += 1
            mt = toks(note)
            overlap = sense_tokens & mt
            if overlap:
                n_aligned += 1
                grand["aligned"] += 1
            else:
                n_res += 1
                grand["residue"] += 1
                residue_rows.append((f"{t['strongs_number']} {t['transliteration']}",
                                     v["reference"], v["target_word"], sense_summary,
                                     (note or "").strip()))
        term_summ.append((t["strongs_number"], t["transliteration"], t["gloss"],
                          len(verses), n_aligned, n_res, n_nomean, sense_summary))

    # ---- write md ----
    L = lines.append
    L(f"# A1 verse-meaning corroboration — mechanical scan · cluster {args.cluster}")
    L("")
    L("> READ-ONLY Tier-1 lexical-overlap triage (`scripts/_assess_verse_corroboration.py`). "
      "Auto-confirms verses whose derived meaning echoes a STEP sense word; isolates the no-overlap "
      "**residue** for Tier-2 judgement. Overlap is necessary-not-sufficient evidence of alignment; "
      "**no overlap ≠ wrong** — it means *not mechanically corroborated*, read it.")
    L("")
    g = grand
    cov = (100 * g["aligned"] / g["meaning"]) if g["meaning"] else 0
    L("## Totals")
    L("")
    L(f"- Terms: **{g['terms']}**")
    L(f"- Verse rows: **{g['verses']}**  ·  relevant: **{g['relevant']}**  ·  with derived meaning: **{g['meaning']}**")
    L(f"- **Mechanically corroborated (overlap):** {g['aligned']} / {g['meaning']}  (**{cov:.1f}%**)")
    L(f"- **Residue (no overlap — needs judgement):** {g['residue']}")
    L(f"- Relevant verses missing a meaning: {g['nomean']}")
    L("")
    L("## Per-term summary")
    L("")
    L("| Strongs | Translit | Gloss | Verses | Corrob. | Residue | NoMean | STEP sense-tokens (sample) |")
    L("|---|---|---|---|---|---|---|---|")
    for s in term_summ:
        L(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]} | {s[5]} | {s[6]} | {s[7]} |")
    L("")
    L(f"## Residue — verses NOT mechanically corroborated ({len(residue_rows)})")
    L("")
    L("These need Tier-2 reading: the meaning may realise a STEP sense in different words (synonym — a "
      "true alignment the heuristic missed), or be a genuine drift/divergence, or be the physical/external "
      "pole of a sense. One row per verse.")
    L("")
    L("| Term | Ref | Target | STEP sense-tokens | Derived meaning |")
    L("|---|---|---|---|---|")
    for r in residue_rows:
        meaning = r[4].replace("|", "\\|").replace("\n", " ")
        L(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {meaning} |")
    L("")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Terms {g['terms']}  verses {g['verses']}  meaning {g['meaning']}")
    print(f"Corroborated {g['aligned']} ({cov:.1f}%)  Residue {g['residue']}  NoMean {g['nomean']}")
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
