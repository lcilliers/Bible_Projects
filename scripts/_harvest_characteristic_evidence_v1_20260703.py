"""Read-only harvest: scan the 150 Psalm Phase-2 readings for the recurring
inner-being CHARACTERISTICS/movements, returning a characteristic x psalm grid.

Grounds the cross-chapter synthesis in the written record (not memory):
feedback_source_of_truth_is_written_record, feedback_verse_raw_data_must_pull_all_study_evidence.

Source of truth = the ACTIVE prose_section chapter-readings in the DB (version-aware),
falling back to the .md files. Matching is over the reading body text with per-characteristic
regexes; a psalm counts if ANY of its characteristic's patterns fire in its reading.

Reusable (feedback_reusable_engine_scripts_and_continuous_learning): edit CHARACTERISTICS
and re-run. Read-only (no DB writes).

Usage: python scripts/_harvest_characteristic_evidence_v1_20260703.py [--out PATH]
"""
import sqlite3, os, re, sys, io

DB = os.path.join('database', 'bible_research.db')

# name -> list of case-insensitive regex fragments (any match = attested in that psalm)
CHARACTERISTICS = {
    "Self-address / the dialogical, self-governing self": [
        r"self-address", r"self-govern", r"dialogical", r"command(s|ed|ing)? (its|itself|the) (own )?soul",
        r"rous(e|es|ing) (its|the|itself)", r"still(ing|s)? (its|the) (own )?soul",
        r"O my soul", r"return, o my soul", r"weaned child", r"exhort(s|ed|ing)? its own",
    ],
    "Being known / searched / tested before God": [
        r"fully known", r"exhaustively known", r"searched me", r"search me",
        r"test(s|ed|ing)? (the |my |its )?(heart|inmost)", r"assay", r"offered? (itself|its integrity) (to be|for)",
        r"transparent to God", r"seen and known", r"known the distress",
    ],
    "Trust / refuge / taking shelter": [
        r"take refuge", r"took refuge", r"refuge", r"trust(s|ed|ing)?\b", r"immovable",
        r"cannot be moved", r"become what (you|it) trust", r"nakon", r"stabilis",
    ],
    "The fear of the LORD (as root / awe)": [
        r"fear of the LORD", r"reverent (fear|awe)", r"beginning of wisdom",
        r"trembl(e|ing)", r"glad awe", r"fear.{0,20}(root|foundation|beginning)",
    ],
    "Waiting / hope on the LORD": [
        r"wait(s|ed|ing)? (on|for) (the )?LORD", r"watchmen for the morning", r"hope(s|d)? in (his|your|the)",
        r"expectant wait", r"hope as (the )?inner", r"\bqavah\b", r"\byachal\b",
    ],
    "Desire / longing / appetite met in God": [
        r"thirst(s|ing)?", r"longing", r"long(s|ed|ing)? for", r"pant(s|ing)?", r"crav(e|ing)",
        r"satisf(y|ies|ied)", r"the desire of", r"appetite", r"one thing", r"consuming desire",
    ],
    "The word / law and the inner being": [
        r"\blaw\b", r"\btorah\b", r"the word (revives|is|internalised|hidden)", r"your word",
        r"delight.{0,15}(law|commandments|testimonies)", r"meditat(e|es|ion).{0,15}(law|word|day and night)",
        r"lamp to my feet", r"sweeter than honey",
    ],
    "Grief / lament / sorrow handled": [
        r"grief", r"sorrow", r"weep(ing)?", r"tears", r"mourn(ing)?", r"lament",
        r"sow(n|ing)? in tears", r"won't fake joy", r"integrity of (grief|sorrow)",
        r"pour(s|ed)? out (its|my|the) (complaint|heart|soul)", r"deliberate(ly)? remember",
    ],
    "Being heard / the cry answered": [
        r"cr(y|ies|ied) (out|aloud|to)", r"has heard", r"you (have )?heard", r"the LORD has heard",
        r"cry (from|of) the (depths|bottom)", r"one fact grasped", r"pivot.{0,20}heard",
        r"pleas for mercy",
    ],
    "Forgiveness / mercy / awe of the forgiven": [
        r"forgiv(e|es|en|eness)", r"pardon", r"cleans(e|ed)", r"blot(s|ted)? out",
        r"that you may be feared", r"awe of the forgiven", r"steadfast love.{0,20}(forgive|removes|remove)",
        r"as far as the east", r"hidden faults", r"presumptuous sins",
    ],
    "Rest / stillness / peace / sleep": [
        r"\brest\b", r"stillness", r"\bstill(ed|s)?\b", r"peace(ful)?", r"\bsleep\b", r"lie down",
        r"quiet(ed|s|ness)?", r"be silent", r"menuchah", r"safety",
    ],
    "Restoration / revival of the self": [
        r"restore(s|d)? (my|the|its)? ?soul", r"reviv(e|es|al|ed)", r"give me life", r"renew(ed|s|al)?",
        r"raised (up )?from the (dust|pit)", r"brought back", r"re-?youth", r"turned my mourning",
    ],
    "Memory / remembering (self remembers; God remembers)": [
        r"remember(s|ed|ing)?", r"memory", r"forget( not|s|ting)?", r"recount", r"\bzakar\b",
        r"mindful", r"held in (God'?s )?mind", r"willed remember",
    ],
    "Humility / self-sizing / lowliness / the un-lifted heart": [
        r"humilit(y|ies)", r"humble", r"lowl(y|iness)", r"what is man", r"but (a )?breath",
        r"un-?lifted", r"not lifted up", r"over-?reach", r"chosen (smallness|proportion)",
        r"right(ly)? (self-?siz|siz)", r"weaned child", r"dust",
    ],
    "Joy / gladness (its varieties)": [
        r"\bjoy(ous|ful)?\b", r"glad(ness)?", r"rejoic(e|es|ed|ing)", r"exult(s|ed|ing)?",
        r"joy above (plenty|abundance)", r"private (joy|hours)", r"dreamlike joy", r"fullness of joy",
    ],
    "Integrity / the inner condition legible / uprightness": [
        r"integrity", r"upright(ness)?", r"\btom\b", r"blameless", r"legible (in|through) speech",
        r"double(-| )heart", r"corruption.{0,15}speech", r"clean hands", r"truth in the (heart|inward)",
    ],
    "Entrustment / committing the self to God": [
        r"entrust(s|ed|ment)?", r"commit(s|ted)? (my|its|the) (spirit|way|times)", r"into your hand",
        r"my times are in your hand", r"deposit(s|ed)?", r"cast(s|ing)? (itself|its cause) on",
        r"becomes prayer",
    ],
    "Being seen by God / God's attentiveness": [
        r"God sees", r"but you (do )?see", r"his eyes (see|test|behold)", r"attentiv",
        r"God'?s (downward )?gaze", r"watched over", r"inclined his ear", r"beheld",
    ],
    "The seeking of God's face / presence": [
        r"seek (your|his|God'?s) face", r"your face.{0,10}I seek", r"behold (his|your) (face|beauty)",
        r"gaze on (his|your) beauty", r"dwell in (the house|your presence)", r"presence of God",
        r"seek(s|ing)? the LORD", r"lift(s|ed)? up (my|its) (eyes|soul)",
    ],
    "Fearlessness / courage derived from God": [
        r"not (be )?afraid", r"fearless", r"will not fear", r"take courage", r"be strong",
        r"what can man do", r"cancels? the fear", r"displaced? (dread|fear)",
    ],
}

def load_readings(conn):
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT CAST(json_extract(metadata_json,'$.chapter') AS INT) ch, body
        FROM prose_section
        WHERE section_type_id=104 AND json_extract(metadata_json,'$.book')='Psa'
          AND json_extract(metadata_json,'$.phase')='2-chapter-reading'
          AND COALESCE(delete_flagged,0)=0
    """).fetchall()
    return {ch: (body or '') for ch, body in rows if ch}

def main():
    out_path = None
    if '--out' in sys.argv:
        out_path = sys.argv[sys.argv.index('--out')+1]
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    readings = load_readings(conn)
    lines = []
    lines.append(f"# Characteristic x Psalm harvest (read-only) — {len(readings)} active readings")
    lines.append("")
    grid = {}
    for name, pats in CHARACTERISTICS.items():
        rx = [re.compile(p, re.I) for p in pats]
        hits = []
        for ch in sorted(readings):
            text = readings[ch]
            if any(r.search(text) for r in rx):
                hits.append(ch)
        grid[name] = hits
        lines.append(f"## {name}")
        lines.append(f"- **count:** {len(hits)}")
        lines.append(f"- **psalms:** {', '.join(str(c) for c in hits)}")
        lines.append("")
    # coverage: any psalm matched by no characteristic
    covered = set()
    for hits in grid.values():
        covered.update(hits)
    uncovered = [c for c in sorted(readings) if c not in covered]
    lines.append("## Coverage check")
    lines.append(f"- psalms matched by >=1 characteristic: {len(covered)}/{len(readings)}")
    lines.append(f"- psalms matched by NONE (candidate arena-only / missed): {uncovered}")
    text = "\n".join(lines)
    if out_path:
        io.open(out_path, 'w', encoding='utf-8').write(text)
        print(f"wrote {out_path} ({len(CHARACTERISTICS)} characteristics, {len(readings)} readings)")
    else:
        print(text)

if __name__ == '__main__':
    main()
