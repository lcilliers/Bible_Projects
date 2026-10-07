"""#1978, 2026-10-07: the M-coded words in the 222 uncited "choose" verses, split into
(1) a real inner-being characteristic in operation (human, or God's own), and
(2) a qualifier: a word that places the choosing (who, what, where, office, status, event, outward act),
    which behaves like a T-code rather than a characteristic that operates with choosing.
Researcher: "isolate the M-code word that have a direct HIB impact, and the words that is that a qualifyer,
that is more like one of the T-codes that a real characteristic that operates with choosing."

Each word is judged in its own verse (#1919: a word's meaning is never taken from its cluster tag), from the
ESV text and the aligned surface. No DB query (rule 71): reads m64-choose-reading-v3-20261007.csv only.
A default is set per Strong's; a verse override is used where the same word has a different face.

Classes:  HIB = a human inner-being characteristic in operation
          DIV = the same kind of word, but God's or Jesus' own inner activity (route A, Ch 13.1 ground)
          QUAL = qualifier, with the kind and the nearest existing T-code (or none)
Relation (HIB/DIV only), as the verse states it:
  ground    - why or how the choice is made (the chooser's knowing, liking, love, pleasure)
  paired    - named alongside the choosing as a parallel act ("refuse the evil and choose the good")
  object    - the inner thing that is itself chosen (wisdom, knowledge, faithfulness)
  purpose   - what the chosen are chosen for ("that you may know and believe")
  trait     - a trait the verse gives the chosen ("full of faith", "called and chosen and faithful")
  response  - follows the choosing (shame at what was chosen, anger at it, joy of the chosen)
  contrast  - set against the choosing (God rejects / men reject the one God chose)
  toward    - an inner movement toward what was chosen (repent and pray toward the chosen city)
  setting   - happens at or through what was chosen (rejoice at the chosen place)
  awareness - knowing that a choice has been made ("you know that God made a choice")
  none      - same verse, not bound to the choosing
Usage: python m64-choose-mcode-hib-qualifier-v1-20261007.py
"""
import csv, os, re
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'm64-choose-reading-v3-20261007.csv')
OUT = os.path.join(HERE, 'm64-choose-mcode-hib-qualifier-v1-20261007.csv')
OUT_SUM = os.path.join(HERE, 'm64-choose-mcode-hib-qualifier-summary-v1-20261007.csv')
WORD = re.compile(r'^(M\d+) (\S+) (.*?) "(.*)" @(\d+)$')

TCODE = {'party-divine': 'T7', 'divine attribute': 'T7', 'party-human': 'T8', 'office/rank': 'T8',
         'corporate': 'T11', 'adversarial': 'T4', 'place/realm': 'T10', 'object': 'T12', 'natural': 'T13',
         'body': 'T14', 'operation': 'T3'}  # every other qualifier kind: no existing T-code

H = lambda rel, who: ('HIB', rel, who)
D = lambda rel, who='God': ('DIV', rel, who)
Q = lambda kind: ('QUAL', kind, '')

DEFAULT = {
    # M72 authority
    **{s: Q('office/rank') for s in ['H4428G', 'H8269', 'H4427A', 'H7218H', 'H5387A', 'H4910', 'G2233']},
    'H6635B': Q('party-divine'), 'H3027H': Q('body'), 'H4467': Q('place/realm'), 'H4438': Q('place/realm'),
    'G0932': Q('place/realm'), 'H1002': Q('place/realm'), 'H3678G': Q('object'), 'G0746': Q('status'),
    'G0934': Q('status'),
    # M42 call / prayer
    **{s: Q('operation') for s in ['H7121G', 'G2564G', 'H6419', 'H2199', 'H8605', 'H7440', 'H7121I', 'H7121J',
                                   'G4377', 'G0994', 'G4336', 'G1941']},
    'G2822': Q('status'), 'G2821': Q('status'),
    # M18 desire
    'H2896A': Q('value comparison'), 'H2836A': D('ground'), 'H0185': H('setting', 'other'), 'H0183': D('ground'),
    'H7065': H('paired', 'chooser'), 'H2530A': H('paired', 'chooser'), 'H7522': D('object'),
    'H2654A': D('object'), 'G2106': D('ground'),
    # M15 knowing
    'H3045': H('paired', 'chooser'), 'G6063': H('awareness', 'other'), 'G1380': H('ground', 'chooser'),
    'H1847': H('object', 'chooser'), 'H0998': H('object', 'chooser'), 'H0995': H('purpose', 'chosen'),
    'G1987': H('awareness', 'other'), 'G1922': H('purpose', 'chosen'), 'G1097': H('none', 'other'),
    # M23 strength
    'H2428G': Q('attribute'), 'H2428A': Q('party-human'), 'H2388G': H('response', 'chosen'), 'H0386': Q('natural'),
    'G1415': Q('attribute'), 'G1411': Q('circumstance'), 'H3581B': Q('divine attribute'), 'H6696A': Q('operation'),
    'H2388J': Q('operation'), 'H2388H': H('paired', 'chooser'), 'G2478': Q('status'), 'G0949': Q('operation'),
    'G3528': Q('operation'),
    # M47 inner seat
    'H5315I': H('setting', 'other'), 'H5315L': H('toward', 'other'), 'H3824': H('toward', 'other'),
    'H3820A': H('toward', 'other'), 'H5315G': H('toward', 'other'), 'H5315J': Q('party-human'),
    'G5590G': D('ground'), 'G4151G': Q('party-divine'), 'G4561': Q('party-human'), 'G2589': D('ground'),
    # M61 holy
    'H6918G': Q('status'), 'H6944G': Q('object'), 'H6942G': Q('operation'), 'G0040G': Q('status'),
    'G0038': Q('operation'),
    # M10 violence
    'H4421': Q('event/setting'), 'H7379': Q('event/setting'), 'H2555': Q('moral value chosen'),
    'H7533': Q('party-human'),
    # M51 love
    'H0157G': D('ground'), 'H0157H': Q('status'), 'G5368': H('response', 'other'), 'G0026': H('purpose', 'chosen'),
    'G0025': D('ground'),
    # M65 speech
    **{s: Q('operation') for s in ['H1696G', 'H6310I', 'H5046', 'H1696I', 'G3056']},
    'H1697G': Q('object'),
    # M30 rejection
    'H3988A': H('paired', 'chooser'), 'H4780': Q('verdict on a party'), 'H5800A': Q('outcome'),
    'H0959': H('contrast', 'other'), 'H5006': H('contrast', 'other'), 'G1848': Q('status'),
    'G0593': H('contrast', 'other'),
    # M45 renewal / help
    'H2319H': Q('attribute'), 'H3467': Q('operation'), 'H5162G': Q('operation'), 'H5826': Q('operation'),
    'H7646': H('response', 'chosen'), 'H5337': Q('operation'), 'G4982': Q('outcome'),
    # M58 wickedness
    'H7451H': Q('moral value chosen'), 'H0205G': Q('moral value chosen'), 'H7562': Q('moral value chosen'),
    'H7451B': Q('moral value chosen'), 'H7563': Q('party-human'), 'H8441': Q('verdict on a party'),
    'H8251': Q('object'), 'G2556G': Q('moral value chosen'),
    # M13 faith
    'H6918H': Q('status'), 'G4102G': H('trait', 'chosen'), 'G0225': Q('object'), 'H0539': H('purpose', 'chosen'),
    'H0530': H('object', 'chooser'), 'G4103': H('trait', 'chosen'),
    # M36 service
    'H8334': Q('operation'), 'H5647H': Q('operation'), 'H5930A': Q('object'), 'H4503G': Q('object'),
    # M12 righteousness
    'H4941G': Q('law/covenant/word'), 'H4941H': Q('moral value chosen'), 'H6337': Q('object'),
    'H6662': Q('party-human'), 'H6666': Q('moral value chosen'), 'G0299': H('purpose', 'chosen'),
    # M24 affliction
    'H6040': Q('circumstance'), 'H3490': Q('party-human'), 'H3238': Q('operation'), 'H6869B': Q('circumstance'),
    'H7451C': Q('outcome'), 'H6031B': H('object', 'other'), 'G4778': Q('circumstance'),
    # M04 joy
    'H8055': H('setting', 'other'), 'H8056': H('setting', 'other'), 'H7832': H('response', 'chosen'),
    'H8342': H('response', 'chosen'), 'H8057': H('response', 'chosen'), 'G0700': H('ground', 'chooser'),
    # M05 kindness
    'H2896B': Q('moral value chosen'), 'H7390': Q('attribute'), 'H2623': Q('party-human'),
    'G0018': Q('moral value chosen'), 'G4236': H('trait', 'chosen'),
    # M06 enmity
    'H0341': Q('party-human'), 'H6973': H('none', 'other'), 'H8581': H('contrast', 'other'),
    'G3404': H('response', 'other'), 'G2190': Q('status'),
    # M16 wisdom
    'H3384B': Q('operation'), 'H6175': Q('moral value chosen'), 'H2451': H('object', 'chooser'),
    'H2450': Q('attribute'), 'G3474': Q('status'), 'G4680': Q('status'), 'G2602': Q('time'),
    # M46 wealth
    'H5159': Q('object'), 'H7230': Q('attribute'), 'H6239': Q('value comparison'), 'G4145': Q('status'),
    # M74 keeping
    'H8104G': Q('operation'), 'H8104J': H('setting', 'other'), 'G5442G': Q('operation'),
    # M80 blessing
    'H1288': Q('operation'), 'H0835': Q('status'),
    # M08 pride
    'H1347': Q('natural'), 'H1984H': H('toward', 'other'), 'G5308': Q('body'),
    # M25 life / death
    'H2421': Q('operation'), 'H2416E': Q('time'), 'H2416C': Q('natural'), 'H4191': Q('outcome'),
    'G2198': Q('attribute'),
    # M26 judgment
    'H1779': Q('event/setting'), 'G2920': Q('object'), 'G1557': Q('operation'), 'G1344': Q('operation'),
    'G0703': Q('divine attribute'),
    # M43 prophecy
    'H5002': Q('operation'), 'H5030': Q('party-human'), 'G4592': Q('object'),
    # M76 way
    'H1870G': Q('course of conduct'),
    # M83 seeking
    'H1245': Q('operation'), 'H1875': Q('operation'), 'G1934': H('contrast', 'other'),
    # M07 shame
    'H1322': Q('outcome'), 'H0954': H('response', 'chooser'), 'H2659': H('response', 'chooser'),
    'G2617': Q('operation'),
    # M11 turning
    'H7725O': H('toward', 'other'), 'H5493G': Q('operation'),
    # M14 deceit
    'G5580': Q('party-human'), 'G5578': Q('party-human'), 'H3655': Q('operation'), 'G1228H': Q('adversarial'),
    # M34 patience
    'H5327A': Q('operation'), 'G3114': D('toward'), 'G3115': H('trait', 'chosen'), 'G5278': H('toward', 'other'),
    # M41 hearing
    'H8085G': Q('operation'), 'G0611': Q('operation'),
    # M01 fear
    'H3372H': H('purpose', 'other'), 'H3373': H('ground', 'chooser'), 'H3372G': H('response', 'chosen'),
    # M09 humility
    'G0036': Q('status'), 'G5012': H('trait', 'chosen'), 'G4434': Q('status'),
    # M21 asking / piety
    'H7592': Q('operation'), 'G0154': Q('operation'), 'G2150': H('trait', 'chosen'),
    # M37
    'H7122H': Q('function word'), 'H1060': Q('object'),
    # M50 grace / compassion
    'H7355': D('ground'), 'G5485': D('ground'), 'G3628': H('trait', 'chosen'), 'G4698': H('trait', 'chosen'),
    'G5544': H('trait', 'chosen'),
    # M54, M55, M56
    'H4687': Q('law/covenant/word'), 'H8451': Q('law/covenant/word'), 'H6459': Q('object'), 'H5566': Q('object'),
    'H2398': Q('operation'), 'H5771G': H('ground', 'chooser'), 'G0266': Q('object'),
    # M19, M22, M32, M33, M39, M44
    'G4100': H('toward', 'other'), 'H7311A': Q('operation'), 'G1391': Q('outcome'),
    'H1285': Q('law/covenant/word'), 'H3772H': Q('operation'), 'H5117': Q('operation'),
    'H7521': D('ground'), 'H2580': Q('value comparison'), 'H6951': Q('corporate'), 'G1577': Q('corporate'),
    # M69, M75, M79, M84
    'G4705': H('ground', 'chooser'), 'G4704': H('response', 'chosen'), 'H3513H': Q('attribute'),
    'G4456': H('contrast', 'other'), 'G4991': Q('outcome'), 'H7321': Q('operation'), 'G5456H': Q('operation'),
    # single-verse M-codes
    'H0639G': H('response', 'other'), 'H2734': H('response', 'other'), 'H0057': Q('party-human'),
    'H3885B': H('ground', 'other'), 'H6381': Q('attribute'), 'G2168': Q('operation'), 'G3874': Q('operation'),
    'H5753B': Q('verdict on a party'), 'G4286': D('ground'), 'H5375P': Q('operation'), 'H2287': Q('event/setting'),
    'G0772G': Q('status'), 'G4417': Q('outcome'), 'G1401': Q('status'), 'H2142': Q('object'),
    'G3140': Q('operation'),
}

# the same word with a different face in a given verse (#1919)
OVERRIDE = {
    ('Luk 14:7', 'G2564G'): Q('party-human'),
    ('Gen 6:2', 'H2896A'): Q('value / quality that draws the choice'),
    ('Deu 23:16', 'H2896A'): H('ground', 'chooser'),
    ('2Sa 19:38', 'H2896A'): H('ground', 'chooser'),
    ('Job 34:4', 'H2896A'): Q('moral value chosen'),
    ('Deu 18:6', 'H0185'): H('toward', 'other'),
    ('Isa 66:3', 'H2654A'): H('paired', 'chooser'),
    ('Num 16:5', 'H3045'): Q('operation'),
    ('Eze 20:5', 'H3045'): Q('operation'),
    ('Judg 20:34', 'H3045'): H('none', 'other'),
    ('1Sa 20:30', 'H3045'): H('response', 'other'),
    ('Isa 7:15', 'H3045'): H('ground', 'chooser'),
    ('Isa 7:16', 'H3045'): H('ground', 'chooser'),
    ('Isa 43:10', 'H3045'): H('purpose', 'chosen'),
    ('Isa 45:4', 'H3045'): H('contrast', 'other'),
    ('Joh 13:18', 'G6063'): D('ground', 'Jesus'),
    ('2Ch 12:13', 'H2388G'): Q('outcome'),
    ('Isa 58:5', 'H5315I'): H('object', 'other'),
    ('2Ch 7:16', 'H3820A'): D('response'),
    ('Pro 10:20', 'H3820A'): H('contrast', 'other'),
    ('Mat 12:18', 'G5590G'): D('ground'),
    ('Deu 12:26', 'H6944G'): Q('object'),
    ('Psa 65:4', 'H6918G'): Q('place/realm'),
    ('Isa 49:7', 'H6918G'): Q('party-divine'),
    ('Zec 2:12', 'H6944G'): Q('place/realm'),
    ('Act 1:2', 'G0040G'): Q('party-divine'),
    ('Act 6:5', 'G0040G'): Q('party-divine'),
    ('Eph 1:4', 'G0040G'): H('purpose', 'chosen'),
    ('Jam 2:5', 'G0025'): H('trait', 'chosen'),
    ('2Jo 1', 'G0025'): H('none', 'other'),
    ('Job 9:14', 'H1697G'): Q('object'),
    ('Act 15:7', 'G3056'): Q('object'),
    ('2Ki 23:27', 'H3988A'): D('contrast'),
    ('Psa 78:67', 'H3988A'): D('contrast'),
    ('Isa 41:9', 'H3988A'): D('contrast'),
    ('Jer 33:24', 'H3988A'): D('contrast'),
    ('Jos 24:15', 'H7451H'): H('ground', 'chooser'),
    ('Isa 66:3', 'H0205G'): Q('object'),
    ('Isa 58:6', 'H7562'): Q('circumstance'),
    ('2Th 2:13', 'G4102G'): H('purpose', 'chosen'),
    ('Jam 2:5', 'G4102G'): H('purpose', 'chosen'),
    ('Isa 49:7', 'H0539'): D('ground'),
    ('Deu 17:8', 'H4941G'): Q('event/setting'),
    ('Job 34:4', 'H4941H'): Q('moral value chosen'),
    ('Psa 106:5', 'H8055'): H('toward', 'other'),
    ('Zec 1:17', 'H2896B'): Q('outcome'),
    ('Job 36:21', 'H8104J'): H('paired', 'chooser'),
    ('Psa 47:4', 'H1347'): Q('object'),
    ('1Cor 1:27', 'G2617'): Q('operation'),
    ('1Pe 2:6', 'G2617'): Q('outcome'),
    ('Isa 65:12', 'H8085G'): H('ground', 'chooser'),
    ('Act 15:7', 'G4100'): H('purpose', 'other'),
    ('Isa 41:8', 'H0157H'): Q('status'),
}

CLASS_NAME = {'HIB': 'human inner-being characteristic', 'DIV': "God's own inner activity",
              'QUAL': 'qualifier'}


def main():
    rows = [r for r in csv.DictReader(open(SRC, encoding='utf-8-sig')) if not r['narrative_refs']]
    out, missing = [], []
    for r in rows:
        if not r['other_m_words']:
            continue
        for w in r['other_m_words'].split(' | '):
            code, strong, gloss, surface, _ = WORD.match(w.strip()).groups()
            c = OVERRIDE.get((r['reference'], strong)) or DEFAULT.get(strong)
            if not c:
                missing.append((r['reference'], strong))
                continue
            cls, rel_kind, who = c
            out.append({'reference': r['reference'], 'route': r['route'], 'group': r['group'], 'cluster_code': code,
                        'strong': strong, 'gloss': gloss, 'surface': surface, 'class': cls,
                        'relation': rel_kind if cls != 'QUAL' else '', 'whose': who,
                        'qualifier_kind': rel_kind if cls == 'QUAL' else '',
                        'nearest_tcode': TCODE.get(rel_kind, 'none') if cls == 'QUAL' else '',
                        'esv_text': r['esv_text']})
    assert not missing, f'unclassified: {missing}'
    used = {(o['reference'], o['strong']) for o in out}
    assert all(k in used for k in OVERRIDE), [k for k in OVERRIDE if k not in used]
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)

    # summary: one row per Strong's (a word with more than one face shows each)
    by = defaultdict(lambda: {'code': '', 'gloss': '', 'faces': Counter(), 'verses': defaultdict(list)})
    for o in out:
        d = by[o['strong']]
        d['code'], d['gloss'] = o['cluster_code'], o['gloss']
        face = f"{o['class']}:{o['relation'] or o['qualifier_kind']}" + (f"/{o['whose']}" if o['whose'] else '')
        d['faces'][face] += 1
        if o['reference'] not in d['verses'][face]:
            d['verses'][face].append(o['reference'])
    with open(OUT_SUM, 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['cluster_code', 'strong', 'gloss', 'rows', 'faces', 'face_count', 'verses_by_face'])
        for s, d in sorted(by.items(), key=lambda i: (i[1]['code'], i[0])):
            w.writerow([d['code'], s, d['gloss'], sum(d['faces'].values()),
                        ' | '.join(f'{f} ({n})' for f, n in d['faces'].most_common()), len(d['faces']),
                        ' | '.join(f'{f}: {", ".join(v)}' for f, v in d['verses'].items())])
    cls = Counter(o['class'] for o in out)
    print(f'{len(out)} word rows in {len({o["reference"] for o in out})} verses: {dict(cls)}; '
          f'{len(by)} Strong\'s, {sum(1 for d in by.values() if len(d["faces"]) > 1)} with more than one face')
    print(f'-> {OUT}\n-> {OUT_SUM}')


if __name__ == '__main__':
    main()
