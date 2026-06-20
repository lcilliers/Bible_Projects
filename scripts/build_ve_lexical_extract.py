"""build_ve_lexical_extract.py (2026-06-16) — emit a cluster's v2 verse-lexical as JSON for AI Chat.

Read-only. One verse object per reference, an array of term-occurrences, each with the structured lexical
record (sense + lemma_meaning split clean) + verse_report + audit. Narration omitted by default (it is a
deterministic restatement of the lexical — redundant + larger for the AI; include with --with-narration).

  python scripts/build_ve_lexical_extract.py --cluster M01
  python scripts/build_ve_lexical_extract.py --cluster M01 --with-narration --out path.json
"""
import argparse, json, os, re, sqlite3, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "analytics"))
sys.path.insert(0, os.path.dirname(__file__))
import morph_util
import _ve_engine_v2 as eng
DB = os.path.join("database", "bible_research.db")
T2_CONTENT_POS = {"verb", "noun", "adjective"}  # 01c §A2: T2-content kept as context; grammatical T2 excluded
# meaningful-qualifier signal union (base strongs): a T2 occurrence is kept ONLY if it serves a recognised
# inner-being qualifier role (seat · intensifier · faculty · perception/cognition · divine · spirit-being ·
# valence). Other T2 content-words (e.g. "seed", "to sow", "hand", "name") have no bearing on the inner-being
# characteristic and are set aside as noise (researcher direction 2026-06-20).
QUAL_KEEP = {eng.base(s) for s in (set(eng.SEAT) | set(eng.DIVINE) | set(eng.INTENSIFIER) | set(eng.FACULTY_LEMMA)
                                   | set(eng.SPIRIT_BEINGS) | set(eng.PERCEPTION) | set(eng.COGNITION)
                                   | set(eng.INHERENT_VALENCE))}


def _t2_noise(occ_cc, strong, morph):
    """A T2 occurrence with no inner-being qualifier bearing (grammatical, or content-word not in QUAL_KEEP)."""
    if occ_cc != "T2":
        return False
    if morph_util.morph_category(morph) not in T2_CONTENT_POS:
        return True   # grammatical T2 function word
    return eng.base(strong) not in QUAL_KEEP   # content T2 that is not a recognised qualifier

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

# summary of the engine-driven data changes behind THIS extract (2026-06-17 session)
ENGINE_CHANGES = {
    "zero_pad_fix": "FOUNDATIONAL: Strong's seed lists were short-form (H430/H408/H853) but the DB measure layer is "
                    "zero-padded 4-digit (H0430/H0408/H0853) — so every <4-digit Hebrew lemma silently failed to match "
                    "(Elohim, 'al, 'et, faculty lemmas). Fixed (_canon). This restored divine/negation/faculty/object-type "
                    "detection; much of the prior 'thin' output was this bug.",
    "valence": "context rule added: prohibition ('al/me + 2nd/3rd-person volitive) -> forbidden (mechanical); "
               "commanded/righteous/neutral are interpretive -> verse-read. UNPARKED 2026-06-18: the corpus valence "
               "read is now COMPLETE (verse-read API, 0 active residue) — valence here is READ-resolved, same status "
               "as cause/divine/object-type.",
    "divine_involvement": "role taxonomy: object (divine adjacent to term, or 'et-marked) is mechanical (~92%); "
                          "agent/possessor/giver/addressee are read-resolved (morphologically overlapping); no divine lemma -> NONE. "
                          "The old meaningless 'present' value is gone.",
    "location_dedup": "one location row per DISTINCT constitutional seat-level even when several same-level seat-words "
                      "co-occur (no 'triple-heart'); spirit/breath (ruach/pneuma) sense-gated, ambiguity read-disambiguated.",
    "t2_treatment": "T2 = reference/qualifier terms, never analysed standalone. T2-GRAMMATICAL (function words: prepositions, "
                    "pronouns, particles, the object-marker 'et) are EXCLUDED from generation/this extract/reads. T2-CONTENT "
                    "(noun/verb/adjective) stay as co-term context only.",
    "base_rerun": "the whole corpus (38,971 term-in-verse units) was re-derived on the corrected engine; 1,768 T2-grammatical "
                  "units disposed; narration regenerated. Integrity verified (quick_check ok, reads preserved).",
    "reads_complete": "the interpretive residue was resolved by a governed verse-read API pass (batched-by-verse, "
                      "circuit-breaker, cost-cap, self-verified): location, cause, object-type, divine-involvement, AND "
                      "valence (unparked + read 2026-06-18) all to 0 M-cluster residue. divine role + object-type split "
                      "+ valence are now fully populated by the read.",
    "signal_list_audit_20260619": "completeness audit of EVERY hand-seeded signal list (divine names, perception, "
                      "cognition, intensifier, …) against canonical lemmas, gated on corpus presence. Closed the gaps "
                      "(DIVINE +Eloah/Yah/Elyon/YHWH-var/Christos; PERCEPTION +shama/nabat/azan; COGNITION +bin; "
                      "INTENSIFIER +gadol) and re-ran the full base. Net new readable residue: divine-involvement only "
                      "(+432, corpus-wide); object-type/cause/location new residue was entirely T2 (excluded). "
                      "0 active readable non-T2 residue remains.",
}

# WHY each lexical element is derived — the measure + rule that FORCES it (traceability), and its provenance.
DERIVATION = {
    "_principle": "Every value is DERIVED from a named original-language measure (lemma · morphology · per-occurrence "
                  "STEP sense · co-occurring tagged terms) — never from the English string. 'Mechanical' = fixed by rule "
                  "over the measure layer; 'read' = the verse was read by API where the rule cannot be decisive (clarify/"
                  "enrich only, never an opt-out). Silence = NONE (never imputed).",
    "sense": "measure: per-occurrence ESV target_word (wa_verse_records) + the lemma's medium_def (lexicon, shown as "
             "lemma_meaning). Mechanical — the sense the term carries HERE, not a uniform gloss.",
    "type": "measure: part-of-speech (morphology). Rule: verb/participle->action, noun->status, adjective->quality. Mechanical (POS-only).",
    "mode": "measure: morph stem/voice/form. The term's own grammatical realisation (language · POS · stem). Mechanical bedrock.",
    "faculty": "measure: the TERM's own lemma meaning, classified to a faculty (R1 term-intrinsic). Why term-intrinsic: the "
               "trigger's faculty (e.g. the perception that caused fear) belongs to cause/compound, not to this term. "
               "Mechanical. (R2 = co-occurring faculty-lemma assignment is a known not-yet-implemented extension.)",
    "location": "measure: a constitutional-seat lemma (Strong's seat-map: heart/soul/spirit/mind/flesh) present in the verse, "
                "SENSE-GATED for spirit/breath (ruach/pneuma may be wind/disposition, not the seat). De-duplicated per level. "
                "Mechanical floor + READ for the spirit/breath ambiguity. Absent = not located.",
    "origin": "measure: a 'from'-source preposition (min/apo/ek) governing the term -> received-from-outside; else absent. "
              "Mechanical (partial — within-person/generational/giver-source rules are not yet implemented).",
    "how": "measure: the governing finite verb of a NOUN/adjective term (the predicate the state operates BY, e.g. 'seized'). "
           "Mechanical. ABSENT for verb-terms — the term IS the action (see mode).",
    "object / object-type": "measure: the term's governed object (noun/pronoun after the term or its governing verb; 'et marks "
                            "the accusative). object-type classifies it: God/spiritual-being/person are mechanical (divine/"
                            "spirit-being lemma, or person morph); thing/abstract/situation/threat are READ-classified (the "
                            "mechanical 'thing/abstract' lump is split by the verse-read). ⚠ CAVEAT: the `object` TEXT is a "
                            "MECHANICAL best-guess and is imprecise in ~13% of cases (it can grab a determiner/pronoun like "
                            "'every'/'his'/'the', or the addressee). `object_type` is READ-derived and AUTHORITATIVE — when the "
                            "two disagree, trust `object_type` and treat `object` text as a hint only.",
    "cause": "measure: a causal marker (ki/hoti/gar) -> the eliciting clause, READ-resolved to the actual cause; OR the object "
             "of a perception verb for an affect term (mechanical). Else NONE (most verses state no cause). Why read: the cause "
             "is the verse's argument, not a single lemma.",
    "cause_clause": "mechanical HINT only — the raw clause after the 'because/for' marker; superseded by `cause` once read.",
    "experiencer": "measure: the term's possessive-suffix person / nominative subject (morphology) -> self | other | "
                   "other(addressed). Mechanical.",
    "divine_involvement": "measure: a divine lemma (YHWH/Elohim/…) and its grammatical relation to the term. object (adjacent / "
                          "'et-marked) is mechanical; agent/possessor/giver/addressee are READ-resolved (these roles overlap "
                          "morphologically — the role is the semantic judgement 'is God feared, acting, or giving'). No divine lemma -> NONE.",
    "intensity": "measure: a quantifier/intensifier lemma modifying the term (kol 'all', me'od 'very', rab 'many'). Mechanical.",
    "valence": "measure: term-inherent moral lemma + context. forbidden = a dedicated prohibition particle ('al/me) on a "
               "2nd/3rd-person volitive (mechanical, ~80% — the 'fear not' reassurance shares the form). commanded/righteous/"
               "neutral are interpretive -> read. Corpus valence read COMPLETE (unparked 2026-06-18) — values here are READ-resolved.",
    "immediate_response": "measure: the coordinated reaction verb-phrase following the term's clause (the inner being's first "
                          "response). Mechanical (light). Expectation test: silent -> NONE.",
    "relational": "measure: a directional preposition adjacent to the term (to/toward/against/above). Mechanical (crude — the "
                  "{direction->object} pairing is a not-yet-implemented extension).",
    "compound": "measure: the verse's OTHER active tagged terms (the reference's term inventory), each with its role to the head "
                "term (partner = co-T1 · qualifier = T2 · co-seated = shares a constitutional seat). This is the synergy web; "
                "fan out to each co-term's own full record by translit/gloss.",
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
    ap.add_argument("--date", default="20260618", help="date stamp in the output filename (bump when regenerating)")
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
    nskip_t2 = 0
    # per-verse set of dropped (noise-T2) transliterations, so kept terms' `compound` lists can drop them too.
    drop_tr = {}
    for u in units:
        if _t2_noise(u["occ_cc"], u["sn"], u["morph"]):
            drop_tr.setdefault(u["ref"], set()).add(u["tr"])
    for u in units:
        # 01c §A3 + 2026-06-20: drop T2 co-terms that carry no inner-being qualifier bearing (grammatical
        # function words, and content-words not in the qualifier signal union) — noise that cannot connect
        # to a character term. Genuine T2 qualifiers (seats/intensifiers/perception/divine/…) are kept.
        if _t2_noise(u["occ_cc"], u["sn"], u["morph"]):
            nskip_t2 += 1
            continue
        # lexical items grouped
        lex = {}
        for r in cur.execute("""SELECT ve_label, value FROM ve_lexical WHERE verse_context_id=?
            AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr, id""", (u["vcid"],)):   # all active rows: mechanical + *_read_api
            if r["ve_label"] in ("sense", "lexical_note"):
                continue
            lex.setdefault(r["ve_label"].replace("-", "_"), []).append(r["value"])
        # drop noise-T2 co-terms from the `compound` list (their standalone records are excluded above)
        if "compound" in lex and drop_tr.get(u["ref"]):
            _dt = drop_tr[u["ref"]]
            lex["compound"] = [e for e in lex["compound"] if e.split(' "')[0].strip() not in _dt]
            if not lex["compound"]:
                del lex["compound"]
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
    # write the per-cluster DATA into the cluster's Sessions-v2 Data/ folder (resolve {CODE}-* exactly once);
    # fall back to the methodology extracts dir for clusters without a Sessions-v2 home.
    import glob as _glob
    _cl = _glob.glob(f"Sessions-v2/{cc}-*/")
    odir = os.path.join(_cl[0], "Data") if len(_cl) == 1 else "research/VE-lexical/extracts"
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
                "UNRESOLVED": "the mechanical pass expected a value but could not decide (rare; reads have since resolved these)",
                "provenance": "most fields = mechanical (01b v2, source v2_engine_iter1); cause/location/divine_involvement/object_type/valence = READ-resolved corpus-wide (verse-read API; valence unparked + read 2026-06-18)",
                "multi_value": "a field may hold a list when several values apply (e.g. faculty, compound)",
            },
            "engine_changes_20260617": ENGINE_CHANGES,
            "why_each_element_is_derived": DERIVATION,
            "fields": FIELDS_GUIDE,
            "source": "ve_lexical (v2_engine_iter1 + *_read_api) + verse_morphology measure layer (schema 3.34.0); regenerated 2026-06-18",
        }, "data": chunk}
        suffix = (f"-b{bi}of{len(chunks)}" if a.batch else "") + ('-narr' if a.with_narration else '')
        out = a.out if (a.out and not a.batch) else f"{odir}/wa-ve-lexical-extract-{cc}-{a.date}{suffix}.json"
        js = json.dumps(payload, ensure_ascii=False, indent=2)
        open(out, "w", encoding="utf-8").write(js)
        print(f"WROTE {out}  ·  {len(chunk):,} verses · {nocc:,} occ · {len(js):,} chars ≈ {len(js)//4:,} tokens")
    print(f"(01c §A3: {nskip_t2:,} T2-grammatical co-terms excluded from the fan-out)")


if __name__ == "__main__":
    main()
