#!/usr/bin/env python
"""Derive the 5 retrofit dims (intensity/specifier/effect/device/direction) for read-2026 chars,
from each char's SAVED PROSE (reading 114 + sense 101 + operation 106 + coupling 112) and the verse,
producing SELF-INTERPRETABLE values (readable without the verse). v1, 2026-07-14.

PAIRS AS SECONDARY CONTROL (researcher): the presence of a source/coupling/manner/target span-pair to a
CONCRETE noun span is a signal of possible imagery — used to CROSS-CHECK the prose-driven device call
(flag possible-missed-imagery), not as the sole trigger.

Returns { span_id: {109:.., 110:.., 111:.., 117:(val[,vehicle_span]), 118:..} } for a book+chapters.
Feed into _apply_retrofit_dims_v1.apply(). Read-only (derivation only)."""
import sqlite3, os, re
DB = os.path.join('database', 'bible_research.db')
PROV = {19:'reread-psalms-2026', 20:'reread-proverbs-2026'}

# device signals searched in reading+operation (prose the reads authored)
DEV = [('personification', r'personif'), ('paradox', r'\bparadox'), ('irony', r'\biron(y|ic)'),
       ('hyperbole', r'hyperbol|emphatic|doubled|exaggerat'), ('litotes', r'litotes|understat'),
       ('metonymy', r'metonym'), ('typology', r'typolog|foreshadow|a type of'),
       ('symbolism', r'symbol'), ('metaphor', r'\bmetaphor')]
SIMILE = re.compile(r'\b(like|as)\b', re.I)
# concrete-noun vehicle words (nature/objects) — imagery vehicles common in poetry/wisdom
CONCRETE = re.compile(r'\b(tree|chaff|water|streams?|deer|grass|flower|dew|rain|snow|fire|smoke|wax|dross|'
   r'lion|dog|bird|sparrow|swallow|serpent|moth|shepherd|sheep|rock|fortress|shield|sun|shadow|clay|'
   r'vessel|gold|silver|ring|thorn|door|hinge|bed|honey|vinegar|sword|arrow|bow|net|snare|pit|cistern|'
   r'fountain|spring|wind|storm|cloud|mountain|valley|potter|furnace|crucible|garment|dust|worm|grasshopper|'
   r'ox|horse|donkey|bear|wolf|eagle|hen|vine|vineyard|field|harvest|seed|root|branch|leaf|fruit)\b', re.I)
DEGREE = re.compile(r'\b(greatly|very|exceedingly|utterly|wholly|sorely|deeply|abundantly|fully|so |too |'
   r'continually|forever|always|never|all day|seven|doubled|emphatic|overwhelm|flood|consume)\b', re.I)
RESULT = re.compile(r'\b(produc|leads? to|so that|results? in|brings?|yields?|recoils?|kindles?|feeds?|'
   r'works? ruin|ends? in|issues? in|drives? |turns? to|makes? |exposes?|delivers?|saves?|revives?)\b', re.I)
SELFWORD = re.compile(r'\b(soul|heart|himself|herself|myself|his own|my own|inmost|within|the self|spirit)\b', re.I)
# OTHER-directed object: only genuine targets of outward movement (NOT the subject 'man'/'men' — too ambiguous)
OTHERWORD = re.compile(r'\b(enem(y|ies)|neighbou?r|nations?|peoples?|the wicked|foe|adversar|the poor|the needy|oppressor)\b', re.I)
GODWARD = re.compile(r'\b(the lord|to god|toward god|trust|refuge|seek|cry|praise|thank|bless the|hope in|'
   r'wait for|take refuge|before you|before the lord|unto you|to you, o)\b', re.I)
RECIP = re.compile(r'\b(recoil|return|repay|requit|back on|rebound|comes? back|reciproc)\b', re.I)

def meaning_tail(reading):
    """the interpretive tail of a reading note (self-interpretable), after the verse-quote."""
    if not reading: return ''
    # after the last ' - ' or ';' following a quote
    parts = re.split(r"'\s*[-–—]\s*|;\s*", reading)
    tail = parts[-1].strip() if len(parts) > 1 else reading.strip()
    return tail[:120]

def vehicle_from_verse(verse, pairs_concrete):
    """the simile vehicle: the concrete noun after like/as; prefer a pair-linked concrete span (the control)."""
    if pairs_concrete:  # a pair already points at a concrete span (secondary control corroborates)
        return pairs_concrete[0]
    m = re.search(r'\b(?:like|as)\s+(?:a |an |the )?([a-z]+)', verse or '', re.I)
    return (None, m.group(1)) if m else (None, None)

def derive_char(reading, sense, operation, coupling, target, bearer, manner, locus, sense_type, verse, pairs_concrete):
    blob = f"{reading or ''} || {operation or ''} || {sense or ''}"
    tail = meaning_tail(reading) or (sense or '')[:100]
    # --- device ---
    dev_type = None; vehicle_span = None
    for name, pat in DEV:
        if re.search(pat, blob, re.I): dev_type = name; break
    if not dev_type and (SIMILE.search(verse or '') and CONCRETE.search(verse or '')):
        dev_type = 'simile'
    if not dev_type and pairs_concrete:            # SECONDARY CONTROL: a pair to a concrete span → likely imagery
        dev_type = 'metaphor'
    if dev_type in ('simile', 'metaphor'):
        vs, vword = vehicle_from_verse(verse, pairs_concrete)
        vehicle_span = vs
        veh_txt = (f"vehicle: {vword}; " if vword else '')
        device = (f"{dev_type} — {veh_txt}{tail}", vehicle_span) if vehicle_span else f"{dev_type} — {veh_txt}{tail}"
    elif dev_type:
        device = f"{dev_type} — {tail}"
    else:
        device = f"literal — {tail}"
    # --- intensity ---
    dm = DEGREE.search(blob)
    intensity = f"emphatic — '{dm.group(1).strip()}' ({tail[:50]})" if dm else 'none'
    # --- effect ---
    rm = RESULT.search(operation or reading or '')
    effect = f"{rm.group(0).strip()} — {tail[:70]}" if rm else 'none'
    # --- specifier (narrowing 'of X' / 'this') ---
    sm = re.search(r"\bof (the LORD|God|[A-Z][a-z]+)\b", (reading or '') + ' ' + (target or ''))
    specifier = f"'{sm.group(0)}' — narrows to {sm.group(1)}" if sm else 'none'
    # --- direction ---
    b = f"{reading or ''} {operation or ''} {sense or ''} {target or ''}"
    if RECIP.search(b): direction = f"reciprocal — {tail[:50]}"
    elif locus == 'external:god' or GODWARD.search(b): direction = f"toward-god — {tail[:50]}"
    elif SELFWORD.search(f"{target or ''} {sense or ''}"): direction = f"inward — {tail[:50]}"
    elif OTHERWORD.search(f"{target or ''} {sense or ''}"): direction = f"outward — {tail[:50]}"
    elif (sense_type or '').lower() in ('state', 'status', 'disposition'): direction = f"static — {tail[:50]}"
    else: direction = f"static — {tail[:50]}"
    return {109: intensity, 110: specifier, 111: effect, 117: device, 118: direction}

def derive(bid, chapters):
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    prov = PROV[bid]
    qc = ','.join('?' * len(chapters))
    out = {}; flags = []
    rows = c.execute(f"""SELECT si.id sid, v.verse_text, v.chapter FROM verse_span_index si JOIN verse v ON v.id=si.verse_id
        WHERE v.book_id=? AND v.chapter IN ({qc}) AND si.role='characteristic' AND si.role_provenance='read-2026'
        ORDER BY v.chapter, v.verse_num, si.id""", (bid, *chapters)).fetchall()
    def d(sid, ve):
        r = c.execute("SELECT value FROM ve_lexical WHERE verse_span_id=? AND ve_nr=? AND source_provenance=? AND delete_flagged=0 LIMIT 1", (sid, ve, prov)).fetchone()
        return r['value'] if r else None
    for r in rows:
        sid = r['sid']
        # pairs control: concrete-noun span endpoints on this char's source/coupling/manner/target pairs
        pc = []
        for pr in c.execute("""SELECT x.to_span, s2.surface FROM ve_lexical x JOIN verse_span_index s2 ON s2.id=x.to_span
              WHERE x.verse_span_id=? AND x.source_provenance=? AND x.delete_flagged=0 AND x.resolution='span'
              AND x.ve_nr IN (103,112,108,107) AND x.to_span IS NOT NULL""", (sid, prov)):
            if pr['surface'] and CONCRETE.search(pr['surface']): pc.append((pr['to_span'], pr['surface']))
        dims = derive_char(d(sid,114), d(sid,101), d(sid,106), d(sid,112), d(sid,107), d(sid,105),
                           d(sid,108), d(sid,116), d(sid,102), r['verse_text'], pc)
        out[sid] = dims
        # SECONDARY-CONTROL FLAG: pair to concrete span but device came out literal → possible missed imagery
        dv = dims[117][0] if isinstance(dims[117], (tuple, list)) else dims[117]
        if pc and dv.startswith('literal'):
            flags.append((sid, r['chapter'], [w for _, w in pc]))
    c.close()
    return out, flags

if __name__ == '__main__':
    import sys
    bid = int(sys.argv[sys.argv.index('--book')+1]) if '--book' in sys.argv else 19
    chs = [int(x) for x in sys.argv[sys.argv.index('--chapters')+1].split(',')] if '--chapters' in sys.argv else [1,2]
    out, flags = derive(bid, chs)
    print(f"derived {len(out)} chars; {len(flags)} pair-control flags (concrete-pair but literal device)")
    for sid, dims in list(out.items())[:6]:
        dv = dims[117][0] if isinstance(dims[117], (tuple, list)) else dims[117]
        print(f"\n[{sid}] device: {dv[:90]}")
        for ve, nm in [(109,'intensity'),(111,'effect'),(118,'direction')]:
            if dims[ve] != 'none': print(f"    {nm}: {dims[ve][:70]}")
