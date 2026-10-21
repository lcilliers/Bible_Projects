"""build_m01_by_characteristic.py (2026-06-18) — emit M01 verse-records grouped BY characteristic.
Characteristic -> Strong's mapping is taken from WA-m01-characteristics-v1.0-2026-06-16.md (lemma-anchored).
Reads the read-complete ve_lexical (DB), pivots per term-in-verse, assigns to characteristic(s) by Strong's.
Read-only. Output: Sessions-v2/M01-Fear/Analysis/wa-m01-by-characteristic-verse-records-20260618.json
"""
import json, os, re, sqlite3
DB = os.path.join("database", "bible_research.db")
OUT = "Sessions-v2/M01-Fear/Data/wa-m01-by-characteristic-verse-records-20260618.json"


def canon(s):
    m = re.match(r"^([HG])(\d+)([A-Za-z]*)$", s or "")
    return f"{m.group(1)}{int(m.group(2)):04d}{m.group(3)}" if m else (s or "")


# characteristic -> (name, description, [Strong's]) — transcribed from WA-m01-characteristics-v1.0
CHARS = [
    ("c1", "Reverent fear / awe (chiefly toward God)", "God-directed, honouring fear; valence righteous/commanded dominant.",
     ["H3372H", "H3373", "H4172A", "H4172B", "H6345", "G6015", "G5401"]),
    ("c2", "Fear / being afraid (apprehension of danger)", "General affect of being afraid; forbidden/neutral dominant.",
     ["H3372G", "G5399", "H3374", "H3025", "H7297", "H3016", "H1763"]),
    ("c3", "Dread (anticipatory fear of a coming threat)", "Forward-looking apprehension.",
     ["H6343", "H6342", "H2844A", "H4034", "H0366"]),
    ("c4", "Terror (overwhelming / externally-sourced fear)", "Strong, often externally inspired/inflicted.",
     ["H0367", "H4032", "H2851", "H1091", "H1205", "H2847", "H2849", "H2866", "H2283", "H4637", "G1630", "G5398", "G5400", "H8606"]),
    ("c5", "Trembling / quaking (body shaken by fear)", "Fear realised as physical agitation.",
     ["H7264", "H2729", "H7460", "H7461A", "H7461B", "H2730", "H7268", "H7269", "H7578", "H6426", "G5156", "G1790"]),
    ("c6", "Shuddering / horror (recoil and bristling)", "Shrinking, hair-raising recoil.",
     ["H6427", "H2189", "H8178A", "H8175A", "H2113"]),
    ("c7", "Dismay / being shattered (loss of inner strength)", "Fear that breaks composure.",
     ["H0926", "H2865", "H0927", "H0928", "H1670", "H1205"]),
    ("c8", "Alarm / sudden fright (startle and panic)", "Abrupt, reactive onset of fear.",
     ["H0927", "H8429", "G4422", "G4426", "G1719", "H7374"]),
    ("c9", "Anxiety / disquiet (anxious care, inner unrest)", "Settled, gnawing worry/distress.",
     ["H1674", "H8312", "H2731", "H3735", "G0085", "H7661"]),
    ("c10", "Astonishment / being awe-struck (stunned)", "Overwhelmed-and-stilled response.",
     ["H8539", "G1568", "G2285", "G1569", "H8429"]),
    ("c11", "Cowardice / timidity (defective/culpable fear)", "Fear as a fault; valence sinful/forbidden.",
     ["G1169", "G1168", "G1167"]),
    ("B1", "NOT inner-being: Constraint / compulsion", "anankE - constraint/hardship, not fear; candidate exclusion.",
     ["G0318"]),
    ("B2", "NOT inner-being: External result / object of terror", "Names what terror produces (desolation/ruin).",
     ["H8047G", "H4288", "H1091", "H2866"]),
    ("B3", "NOT inner-being: Probable homonym / sense-noise", "Wide-lemma/homonym pulled on the wrong sense.",
     ["H4867", "H6178", "H4035", "H2119B", "H6125"]),
]
CHAR_SET = {cid: {canon(s) for s in strs} for cid, _n, _d, strs in CHARS}

c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
units = c.execute("""
    SELECT vc.id vcid, vr.reference ref, m.strongs_number strong, vr.transliteration translit,
           m.gloss gloss, m.language lang, vr.target_word tw, vr.morph_code morph, vr.stem stem,
           COALESCE(v.verse_text, vr.verse_text) verse_text
    FROM verse_context vc
    JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
    JOIN mti_terms m ON m.id=vc.mti_term_id
    LEFT JOIN verse v ON v.reference=vr.reference
    WHERE COALESCE(vc.delete_flagged,0)=0 AND m.cluster_code='M01'
    ORDER BY vr.book_id, vr.chapter, vr.verse_num""").fetchall()

LEX_ORDER = ["sense", "lemma_meaning", "type", "mode", "faculty", "location", "origin", "how", "object",
             "object-type", "cause", "cause_clause", "experiencer", "divine-involvement", "intensity",
             "valence", "immediate-response", "relational", "compound"]


def lexical_for(vcid, strong):
    lex = {}
    for r in c.execute("""SELECT ve_label, value FROM ve_lexical WHERE verse_context_id=?
        AND ve_label NOT IN ('lexical_note') AND COALESCE(delete_flagged,0)=0 ORDER BY ve_nr, id""", (vcid,)):
        lex.setdefault(r["ve_label"], []).append(r["value"])
    lex = {k: (v[0] if len(v) == 1 else v) for k, v in lex.items()}
    md = c.execute("SELECT medium_def FROM lexicon WHERE strong=?", (canon(re.match(r'^[HG]\d+', strong).group(0)) if re.match(r'^[HG]\d+', strong) else strong,)).fetchone()
    if md and md[0]:
        lex["lemma_meaning"] = re.split(r"[\n;]", md[0])[0].strip()[:80]
    return {k.replace("-", "_"): lex[k] for k in LEX_ORDER if k in lex}


# assign units to characteristics (a term may serve more than one -> appears under each)
records = {cid: [] for cid, *_ in CHARS}
assigned_vcids = set()
for u in units:
    cs = canon(u["strong"])
    rec = None
    for cid, codes in CHAR_SET.items():
        if cs in codes:
            if rec is None:
                rec = {"reference": u["ref"],
                       "verse_text": u["verse_text"],
                       "term": {"strong": u["strong"], "translit": u["translit"], "gloss": u["gloss"], "language": u["lang"]},
                       "verse_report": {"target_word": u["tw"], "morph": u["morph"], "stem": u["stem"]},
                       "lexical": lexical_for(u["vcid"], u["strong"])}
            records[cid].append(rec)
            assigned_vcids.add(u["vcid"])

# unassigned = focus units not matched to any characteristic in the v1.0 doc lists — kept as their own group
unassigned_records = []
unassigned_strongs = set()
for u in units:
    if u["vcid"] not in assigned_vcids:
        unassigned_strongs.add(u["strong"])
        unassigned_records.append({"reference": u["ref"],
                                   "verse_text": u["verse_text"],
                                   "term": {"strong": u["strong"], "translit": u["translit"], "gloss": u["gloss"], "language": u["lang"]},
                                   "verse_report": {"target_word": u["tw"], "morph": u["morph"], "stem": u["stem"]},
                                   "lexical": lexical_for(u["vcid"], u["strong"])})

out = {
    "meta": {
        "what_this_is": "M01 (Fear) focus-cluster term-in-verse records GROUPED BY inner-being characteristic. "
                        "Characteristics + their Strong's are lemma-anchored per WA-m01-characteristics-v1.0-2026-06-16.md; "
                        "lexical detail per record is the read-complete ve_lexical (2026-06-18).",
        "source_doc": "Sessions-v2/M01-Fear/Analysis/WA-m01-characteristics-v1.0-2026-06-16.md",
        "data_source": "ve_lexical (v2_engine_iter1 mechanical + *_read_api read-resolved) — schema 3.34.0",
        "caveats": [
            "LEMMA-ANCHORED (interpretive): a term that spans families appears under EVERY characteristic that lists it "
            "(e.g. H1205 in c4+c7; H0927 in c7+c8; H8429 in c8+c10; H1091/H2866 in c4+B2). Records are duplicated across those.",
            "G5401 ('fear/terror') is doc-assigned to c1 for reverent uses, but many of its occurrences are general fear — "
            "use the per-record `valence`/`object_type` to refine (object_type=God + valence righteous/commanded = reverent).",
            "B1/B2/B3 are NOT inner-being characteristics (kept separate per the doc).",
            "object TEXT is mechanical (~13% imprecise); object_type is read-authoritative — trust object_type on disagreement.",
            "valence: mechanical + M01-pilot read only (corpus valence read PARKED).",
        ],
        "totals": {"focus_units": len(units), "assigned_units": len(assigned_vcids), "unassigned_units": len(unassigned_records)},
    },
    "characteristics": [
        {"id": cid, "name": name, "description": desc, "strongs": strs,
         "occurrence_count": len(records[cid]), "verse_records": records[cid]}
        for cid, name, desc, strs in CHARS
    ] + [
        {"id": "unassigned", "name": "Unassigned (M01 terms not mapped to any v1.0 characteristic)",
         "description": "Focus terms present in M01 but absent from every characteristic's lemma list in "
                        "WA-m01-characteristics-v1.0 — a coverage gap to fold into the right characteristic.",
         "strongs": sorted(unassigned_strongs),
         "occurrence_count": len(unassigned_records), "verse_records": unassigned_records},
    ],
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
js = json.dumps(out, ensure_ascii=False, indent=2)
open(OUT, "w", encoding="utf-8").write(js)
print(f"WROTE {OUT}  ·  {len(js):,} chars ≈ {len(js)//4:,} tokens")
print(f"focus units {len(units)} · assigned {len(assigned_vcids)} · unassigned {len(unassigned_records)}")
for cid, name, _d, _s in CHARS:
    print(f"  {cid:4} n={len(records[cid]):4}  {name}")
print(f"  {'unassigned':4} n={len(unassigned_records):4}  {sorted(unassigned_strongs)}")
