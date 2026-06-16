"""build_ve_lexical_extract.py (2026-06-16) — emit a cluster's v2 verse-lexical as JSON for AI Chat.

Read-only. One verse object per reference, an array of term-occurrences, each with the structured lexical
record (sense + lemma_meaning split clean) + verse_report + audit. Narration omitted by default (it is a
deterministic restatement of the lexical — redundant + larger for the AI; include with --with-narration).

  python scripts/build_ve_lexical_extract.py --cluster M01
  python scripts/build_ve_lexical_extract.py --cluster M01 --with-narration --out path.json
"""
import argparse, json, os, re, sqlite3
DB = os.path.join("database", "bible_research.db")

FIELDS_GUIDE = {
    "sense": "per-occurrence contextual sense (the ESV word used in THIS verse)",
    "lemma_meaning": "the lemma's dictionary meaning (concise)",
    "type": "action | status | quality — the grammatical kind (from morphology)",
    "mode": "the term's grammatical realisation: language · part-of-speech · (verb stem)",
    "faculty": "the inner-being faculty the TERM ITSELF engages (affect/cognition/perception/memory/volition/moral_evaluation/conscience); term-intrinsic; ABSENT if the term is not itself a faculty",
    "location": "constitutional seat the state is seated in (spirit/soul/heart/mind/flesh/conscience); READ-disambiguated; absent if none",
    "origin": "where it comes from (within-person/received-from-outside/carried-generationally)",
    "how": "the governing predicate — how a noun/state term operates; ABSENT for verb-terms (the term IS the action; see mode)",
    "object": "what the state is directed at / acts on",
    "object_type": "the object's kind (threat/person/God/spiritual-being/situation/abstract/thing); READ-classified",
    "cause": "what AROUSES the state; READ-resolved; absent = the verse states no cause",
    "cause_clause": "mechanical hint only — the raw clause after a 'because/for' marker (superseded by `cause` once read)",
    "experiencer": "who bears the state: self | other | other (addressed)",
    "divine_involvement": "GOD's role toward the term (agent/possessor/giver/object/addressee); READ-resolved",
    "intensity": "quantifier / intensity (e.g. 'many', 'greatly')",
    "valence": "moral framing in context (righteous/sinful/commanded/forbidden/neutral); READ-resolved",
    "immediate_response": "the immediate reaction the state produces (e.g. 'bowed faces')",
    "compound": "co-occurring terms in THIS verse, each as `translit \"gloss\" — role` (partner/qualifier/co-seated). FAN-OUT: every co-term is present as its OWN full record in this verse's term_occurrences — resolve by matching translit/gloss",
    "relational": "directional / relational force (to, toward, against …)",
}


def base(s):
    m = re.match(r"^([HG]\d+)", s or "")
    return m.group(1) if m else (s or "")


def concise(md):
    md = (md or "").strip()
    if not md:
        return None
    md = re.split(r"[\n;]", md)[0].strip()
    md = re.sub(r"^[:\d]+[a-z]?\)?\s*", "", md).strip()
    return md[:70] or None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--with-narration", action="store_true")
    ap.add_argument("--with-audit", action="store_true")
    ap.add_argument("--batch", type=int, default=0, help="max verses per output file (split a big cluster)")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cc = a.cluster
    desc = (cur.execute("SELECT description FROM cluster WHERE cluster_code=?", (cc,)).fetchone() or [None])[0]

    # fan-out: every term in the cluster's verses (not just the cluster's terms), so each compound node
    # resolves into the co-term's FULL lexical record inside the same verse payload.
    units = cur.execute("""
        SELECT vc.id vcid, vr.reference ref, m.strongs_number sn, m.transliteration tr, m.gloss gloss,
               m.language lang, m.cluster_code occ_cc, vr.target_word tw, vr.morph_code morph, vr.stem stem
        FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        JOIN mti_terms m ON m.id=vc.mti_term_id
        WHERE COALESCE(vc.delete_flagged,0)=0 AND vr.reference IN (
            SELECT DISTINCT vr2.reference FROM verse_context vc2
            JOIN wa_verse_records vr2 ON vr2.id=vc2.verse_record_id AND COALESCE(vr2.delete_flagged,0)=0
            JOIN mti_terms m2 ON m2.id=vc2.mti_term_id
            WHERE m2.cluster_code=? AND COALESCE(vc2.delete_flagged,0)=0)
        ORDER BY vr.book_id, vr.chapter, vr.verse_num, vc.id""", (cc,)).fetchall()

    # field order for the lexical block
    ORDER = ["type", "mode", "location", "origin", "faculty", "how", "object", "object_type", "cause",
             "cause_clause", "experiencer", "divine-involvement", "intensity", "valence", "immediate-response",
             "compound", "relational"]
    verses, vmap = [], {}
    for u in units:
        # lexical items grouped
        lex = {}
        for r in cur.execute("""SELECT ve_label, value FROM ve_lexical WHERE verse_context_id=?
            AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr, id""", (u["vcid"],)):   # all active rows: mechanical + *_read_api
            if r["ve_label"] in ("sense", "lexical_note"):
                continue
            lex.setdefault(r["ve_label"].replace("-", "_"), []).append(r["value"])
        lex = {k: (v[0] if len(v) == 1 else v) for k, v in lex.items()}
        ordered = {k.replace("-", "_"): lex[k.replace("-", "_")] for k in ORDER if k.replace("-", "_") in lex}
        lemma = concise((cur.execute("SELECT medium_def FROM lexicon WHERE strong=?", (base(u["sn"]),)).fetchone() or [None])[0])
        au = cur.execute("""SELECT value FROM ve_lexical WHERE verse_context_id=? AND ve_label='lexical_note'
            AND COALESCE(delete_flagged,0)=0""", (u["vcid"],)).fetchone()
        occ = {"term": {"strong": u["sn"], "translit": u["tr"], "gloss": u["gloss"], "language": u["lang"],
                        "cluster": u["occ_cc"], "focus_cluster": (u["occ_cc"] == cc)},
               "verse_report": {"target_word": u["tw"], "morph": u["morph"], "stem": u["stem"]},
               "lexical": {"sense": u["tw"], "lemma_meaning": lemma, **ordered}}
        if a.with_audit:
            occ["audit"] = au["value"].replace("[audit] ", "") if au else None
        if a.with_narration:
            nr = cur.execute("""SELECT finding_value FROM finding WHERE verse_context_id=? AND provenance='l2_meaning'
                AND COALESCE(delete_flagged,0)=0""", (u["vcid"],)).fetchone()
            occ["narration"] = nr["finding_value"] if nr else None
        if u["ref"] not in vmap:
            vt = cur.execute("SELECT osis_id, testament, verse_text FROM verse WHERE reference=?", (u["ref"],)).fetchone()
            vmap[u["ref"]] = {"verse": {"reference": u["ref"], "osis_id": vt["osis_id"] if vt else None,
                                        "testament": vt["testament"] if vt else None,
                                        "verse_text": vt["verse_text"] if vt else None}, "term_occurrences": []}
            verses.append(vmap[u["ref"]])
        vmap[u["ref"]]["term_occurrences"].append(occ)

    chunks = [verses] if not a.batch else [verses[i:i + a.batch] for i in range(0, len(verses), a.batch)]
    odir = "research/VE-lexical/extracts"
    os.makedirs(odir, exist_ok=True)
    for bi, chunk in enumerate(chunks, 1):
        nocc = sum(len(v["term_occurrences"]) for v in chunk)
        payload = {"meta": {
            "focus_cluster": cc, "description": desc, "batch": f"{bi}/{len(chunks)}" if a.batch else "full",
            "verses": len(chunk), "occurrences": nocc,
            "what_this_is": (f"A per-term-in-verse LEXICAL DECOMPOSITION of the inner-being terms in the verses where "
                             f"cluster {cc} ('{desc}') occurs. Each record shows what a verse says about the inner being, "
                             f"recorded once per term-occurrence. Mechanically derived (01b v2) over the original-language "
                             f"morphology; the interpretive fields (cause, location, divine_involvement, object_type, valence) "
                             f"are resolved by a focused verse-read API pass."),
            "structure": ("data = array of VERSES. Each verse = {verse:{reference,osis_id,testament,verse_text}, "
                          "term_occurrences:[ {term:{strong,translit,gloss,language,cluster,focus_cluster}, "
                          "verse_report:{target_word,morph,stem}, lexical:{...}} ]}."),
            "layout_fan_out": ("VERSE-based fan-out — each verse lists EVERY term in it, not just the focus cluster's "
                               "(focus_cluster=true marks the terms of interest). A term's `compound` lists its co-terms, "
                               "which are present as their OWN full records in the same verse — fan out by matching translit/gloss "
                               "to analyse synergy without leaving the verse."),
            "conventions": {
                "absent_field": "a lexical field that is absent = NONE (genuinely silent in the verse; never imputed)",
                "UNRESOLVED": "the mechanical pass expected a value but could not decide (rare)",
                "provenance": "most fields = mechanical (01b v2); cause/location/divine_involvement/object_type/valence = read-resolved (verse-read API, high quality)",
                "multi_value": "a field may hold a list when several values apply (e.g. faculty, compound)",
            },
            "fields": FIELDS_GUIDE,
            "source": "ve_lexical (v2_engine_iter1 + *_read_api) + verse_morphology measure layer (schema 3.34.0)",
        }, "data": chunk}
        suffix = (f"-b{bi}of{len(chunks)}" if a.batch else "") + ('-narr' if a.with_narration else '')
        out = a.out if (a.out and not a.batch) else f"{odir}/wa-ve-lexical-extract-{cc}-20260616{suffix}.json"
        js = json.dumps(payload, ensure_ascii=False, indent=2)
        open(out, "w", encoding="utf-8").write(js)
        print(f"WROTE {out}  ·  {len(chunk):,} verses · {nocc:,} occ · {len(js):,} chars ≈ {len(js)//4:,} tokens")


if __name__ == "__main__":
    main()
