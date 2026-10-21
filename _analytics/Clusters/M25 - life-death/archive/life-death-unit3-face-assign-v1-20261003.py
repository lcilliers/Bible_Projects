"""Life-death unit 3 (living before God): face assignments, recorded from reading every hit.

Each hit was read by surface in the pull (life-death-unit3-living-before-god-pull-v1-20261003.csv).
The assignments are written here as data so the reading is auditable and re-runnable:
  VERSES = verse-level faces, from reading ("ref")
  HITS   = hit-level faces where two hits in one verse read differently ("ref#pos")
There is no fallback rule in unit 3: every verse is named. The script refuses to run if any hit
is left without a face, or if any assignment matches no hit.
Writes life-death-unit3-faces-v1-20261003.csv and merges it into the pull with
strand-unit-pull-v1-20261002.py --faces.
"""
import csv, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PULL = os.path.join(HERE, 'life-death-unit3-living-before-god-pull-v1-20261003.csv')
OUT = os.path.join(HERE, 'life-death-unit3-faces-v1-20261003.csv')

FACES = {
    'L01': 'oath by the LORD\'s life or by a person\'s life ("as the LORD lives", "as your soul lives")',
    'L02': 'God swears by his own life ("As I live, declares the Lord")',
    'L03': 'the living God; "the LORD lives"; him who lives forever',
    'L05': 'still alive; alive or dead; taken alive (narrative, data)',
    'L06': 'living creatures, all flesh, the breath of life in creation and flood (data)',
    'L07': 'not the inner being: raw, fresh, spring, next year, poles, live bird, idiom (data)',
    'L08': 'lifespan notices; "all the days of his life" as a measure (data)',
    'L09': 'long life, days prolonged: with keeping, fearing, honouring; and its loss',
    'L10': 'the days one lives as the span of fearing, remembering, learning, serving',
    'L11': 'life set before a person; choose life; the heart circumcised "that you may live"',
    'L12': 'life from wisdom, the fear of the LORD, righteousness, the tongue (Proverbs)',
    'L13': 'life by doing: the law, the statutes of life, "do this and you will live"; eternal life asked about',
    'L14': 'life weighed from within: loathed, bitter, brief, in doubt, despaired of; the living weighed',
    'L15': 'life valued: enjoyed, loved, and what it does not consist in',
    'L16': 'life given, kept, redeemed and fed by God (and life asked of him)',
    'L17': 'as long as I live: praise, and dwelling in his house all my days',
    'L18': 'the land, book and bundle of the living; the living and the dead',
    'L19': 'gone down alive (swallowed alive into Sheol)',
    'L20': 'living water: fountain, spring, river',
    'L21': 'eternal life: given, had, inherited, promised',
    'L22': 'Christ the life; life in the Son; Christ alive',
    'L23': 'living to God: Christ lives in me; dead to sin, alive to God; live by faith; all live to him',
    'L24': 'life and the Spirit',
    'L25': 'from death to life; alive yet dead',
    'L26': 'entering life; the tree, crown and book of life; the living and the dead judged; resurrection of life',
    'L27': 'living word, hope, stones, way; the word of life',
    'L28': 'long of anger, patience, delay (H0748 with anger; Psa 30:5)',
    'L29': 'life threatened or taken by people',
    'L30': 'healed or raised: "she will live", "your son lives"',
    'L31': 'bound by law while one lives (data)',
    'L32': 'living as a manner of conduct (data)',
}

VERSES = {
    'L01': '2Sa 12:5; 2Sa 4:9; 1Ki 1:29; 1Sa 26:16; 1Ki 17:12; Judg 8:19; Job 27:2; 2Sa 2:27; 2Sa 14:19; '
           '1Ki 22:14; 2Ch 18:13; Jer 4:2; 2Sa 14:11; Gen 42:16; 2Sa 11:11; 2Sa 15:21; 1Sa 1:26; 1Sa 14:45; '
           '1Sa 17:55; 1Sa 20:3; 1Sa 20:21; 1Sa 26:10; 1Sa 28:10; 1Sa 29:6; 1Ki 17:1; 1Ki 18:10; 1Ki 18:15; '
           '2Ki 2:2; 2Ki 2:4; 2Ki 2:6; 2Ki 3:14; 2Ki 4:30; 2Ki 5:16; 2Ki 5:20; Jer 5:2; Jer 16:14; Jer 23:7; '
           'Jer 38:16; Jer 44:26; Amo 8:14; 1Sa 14:39; Jer 12:16; Hos 4:15; 1Sa 19:6; 1Ki 2:24; Rut 3:13; '
           'Jer 16:15; 1Sa 25:26; 1Sa 25:34; Jer 23:8; Gen 42:15',
    'L02': 'Eze 35:6; Eze 5:11; Eze 35:11; Eze 20:33; Eze 33:11; Num 14:28; Eze 20:3; Jer 22:24; Eze 17:19; '
           'Eze 17:16; Eze 34:8; Deu 32:40; Eze 33:27; Jer 46:18; Isa 49:18; Num 14:21; Eze 20:31; Eze 14:16; '
           'Zep 2:9; Eze 18:3; Eze 14:20; Eze 16:48; Eze 14:18; Rom 14:11',
    'L03': 'Jer 10:10; Deu 5:26; 1Sa 17:36; Dan 12:7; Jos 3:10; 1Sa 17:26; 2Ki 19:4; 2Ki 19:16; Isa 37:4; '
           'Isa 37:17; Hos 1:10; Jer 23:36; Psa 84:2; Job 19:25; Psa 42:2; 2Sa 22:47; Psa 18:46; Rev 15:7; '
           'Mat 16:16; Mat 26:63; Heb 9:14; Rev 4:10; 1Th 1:9; Heb 12:22; 2Cor 6:16; Rom 9:26; Rev 7:2; '
           'Rev 4:9; Heb 3:12; 1Ti 4:10; Act 14:15; 1Ti 3:15; Heb 10:31; Rev 10:6',
    'L05': '2Sa 19:6; 2Sa 12:18; 2Sa 12:22; 1Ki 20:32; Deu 31:27; 1Ki 3:22; Gen 43:28; 2Sa 12:21; 2Ki 7:12; '
           'Gen 43:7; Gen 43:27; Gen 45:3; Gen 45:26; Gen 45:28; Gen 46:30; Exo 4:18; 2Sa 18:14; 1Ki 3:23; '
           '1Ki 3:25; 1Ki 3:26; 1Ki 3:27; 1Ki 12:6; 1Ki 20:18; 1Ki 21:15; 2Ki 10:14; 2Ch 10:6; 1Sa 20:14; '
           'Deu 5:3; 1Sa 15:8; 2Ch 25:12; Jos 8:23; 2Sa 1:23',
    'L06': 'Lev 11:10; Gen 6:19; Gen 1:28; Gen 1:20; Gen 1:24; Gen 8:21; Gen 9:12; Gen 2:19; Gen 3:20; '
           'Gen 9:15; Gen 9:16; Gen 1:21; Gen 9:3; Gen 9:10; Lev 11:46; Gen 1:30; Gen 7:22; Gen 6:17; '
           'Gen 7:15; Rev 16:3',
    'L07': 'Psa 38:19; Psa 58:9; 2Ki 4:17; Gen 26:19; Gen 18:10; 1Sa 2:15; 1Sa 25:6; 2Ki 4:16; Lev 16:10; '
           'Lev 16:21; Exo 21:35; Lev 13:10; Lev 13:16; Gen 18:14; Lev 13:14; Lev 13:15; Num 19:17; '
           'Lev 14:53; Lev 16:20; Lev 14:52; Lev 14:6; Lev 14:51; Exo 22:4; Lev 14:4; Lev 14:5; Lev 14:7; '
           'Lev 14:50; Lev 15:13; Eze 31:5; Isa 54:2; Isa 57:4; Gen 26:8; 1Ki 8:8; 2Ch 5:9; Num 9:19; '
           'Num 9:22; Psa 129:3; Rev 13:14; 1Cor 9:14',
    'L08': 'Gen 25:6; Gen 25:7; Gen 47:28; 1Ki 4:21; 1Ki 11:34; Gen 3:14; Gen 3:17; Gen 47:8; Judg 16:30; '
           '2Sa 18:18; Exo 6:16; Gen 25:17; 1Sa 7:15; 2Ki 25:30; Jer 52:34; 1Ki 15:6; Pro 31:12; Gen 7:11; '
           '2Ki 25:29; Jer 52:33; Exo 6:20; Gen 23:1; Luk 2:36',
    'L09': 'Pro 28:16; Deu 5:33; Ecc 8:12; Exo 20:12; Deu 5:16; Pro 4:10; Pro 9:11; Deu 4:26; Deu 30:18; '
           'Ecc 7:15; Isa 53:10; Ecc 8:13; Deu 4:40; Deu 22:7; Deu 11:9; Psa 34:12; Deu 25:15; Pro 28:2; '
           'Psa 128:5; Job 24:22; Deu 17:20; 1Ki 3:14; Pro 3:2; 1Pe 3:10',
    'L10': '1Ki 8:40; 2Ch 6:31; Deu 4:10; Deu 31:13; Deu 12:1; Deu 17:19; Jos 4:14; 1Sa 1:11; Deu 4:9; '
           '1Ki 15:5; Jos 24:31; Judg 2:7; Deu 16:3',
    'L11': 'Deu 30:19; Jer 21:8; Deu 30:20; Deu 30:6; Deu 30:15',
    'L12': 'Pro 15:4; Pro 3:18; Pro 21:21; Pro 10:11; Pro 10:16; Pro 19:23; Pro 15:31; Pro 8:35; Pro 16:15; '
           'Pro 13:12; Pro 18:21; Pro 22:4; Pro 5:6; Pro 16:22; Pro 11:19; Pro 4:23; Pro 14:27; Pro 3:22; '
           'Pro 14:30; Pro 4:22; Pro 12:28; Pro 11:30; Pro 15:24; Pro 10:17; Pro 2:19; Pro 4:13; Pro 13:14; '
           'Pro 6:23',
    'L13': 'Eze 33:15; Mal 2:5; Deu 32:47; Luk 10:25; Luk 18:18; Gal 3:12; Mat 19:16; Mat 19:17; Luk 10:28; '
           'Mar 10:17; Rom 10:5; Rom 7:10',
    'L14': 'Psa 143:2; Ecc 4:2; Ecc 9:4; Ecc 9:5; Ecc 7:2; Lam 3:39; Ecc 2:17; Psa 31:10; Job 3:20; Job 10:1; '
           'Psa 88:3; Deu 28:66; Exo 1:14; Isa 38:12; Gen 27:46; Gen 47:9; 2Sa 19:34; Jon 4:8; Ecc 9:3; '
           'Eze 7:13; Ecc 6:12; Jon 4:3; Jer 8:3; Job 9:21; Job 7:7; 2Cor 1:8; Heb 2:15; Jam 4:14',
    'L15': 'Ecc 5:18; Ecc 8:15; Ecc 9:9; Ecc 5:20; Ecc 10:19; Psa 17:14; Psa 49:18; Ecc 2:3; Ecc 3:12; '
           'Luk 16:25; 1Cor 15:19; Luk 12:15; Luk 15:13; 1Ti 6:19; 1Ti 4:8; Joh 12:25',
    'L16': 'Gen 2:7; Psa 145:16; Job 33:30; Psa 56:13; Job 12:10; Isa 38:16; Psa 27:1; Psa 64:1; Job 10:12; '
           'Psa 42:8; Psa 63:3; Psa 103:4; Lam 3:58; Psa 16:11; Jon 2:6; Psa 21:4; Psa 36:9; Jos 1:5; '
           'Psa 133:3; Psa 66:9; Mat 4:4; Luk 4:4; Act 17:25; Act 17:28; Act 2:28',
    'L17': 'Isa 38:19; Psa 146:2; Psa 63:4; Psa 23:6; Psa 27:4; Psa 104:33; Isa 38:20',
    'L18': 'Rut 2:20; Psa 142:5; Isa 8:19; Isa 38:11; Eze 32:25; Eze 32:23; Eze 32:24; Eze 32:26; Num 16:48; '
           'Eze 32:32; 1Sa 25:29; Eze 26:20; Eze 32:27; Job 28:13; Job 30:23; Ecc 6:8; Psa 27:13; Ecc 4:15; '
           'Psa 69:28; Job 28:21; Psa 52:5; Isa 4:3',
    'L19': 'Psa 124:3; Num 16:30; Num 16:33; Psa 55:15; Pro 1:12; Rev 19:20',
    'L20': 'Eze 47:9; Jer 2:13; Jer 17:13; Zec 14:8; Song 4:15; Joh 7:38; Joh 4:10; Joh 4:11; Rev 22:17; '
           'Rev 21:6; Rev 7:17; Rev 22:1; Joh 4:14',
    'L21': 'Joh 3:36; Joh 17:3; Rom 5:21; Rom 6:23; 1Ti 1:16; Jude 21; Joh 6:47; Act 13:46; Rom 6:22; '
           'Joh 3:16; Joh 6:27; Joh 12:50; 1Ti 6:12; Mat 19:29; 1Jo 5:13; Joh 4:36; Act 13:48; Rom 2:7; '
           'Joh 6:40; Joh 5:39; Tit 1:2; Tit 3:7; Joh 3:15; 1Jo 5:11; Mar 10:30; Joh 10:28; Joh 17:2; '
           'Joh 6:54; 1Jo 2:25; Joh 6:68; Luk 18:30',
    'L22': 'Joh 20:31; Rom 5:17; Col 3:3; Col 3:4; 2Ti 1:1; 2Ti 1:10; 1Jo 5:20; Mat 27:63; Luk 24:23; '
           'Joh 6:53; Joh 8:12; Joh 14:6; Act 1:3; Rev 2:8; Mar 16:11; 1Pe 2:4; Heb 7:16; Heb 7:25; '
           'Luk 24:5; Joh 6:35; Joh 11:25; Rom 5:18; Act 25:19; Joh 5:40; Heb 7:3; Joh 14:19; Joh 11:26; '
           'Joh 6:33; Act 3:15; Rom 5:10; Rom 6:10; 1Jo 4:9; 1Jo 5:12; Joh 6:58; Rev 1:18; Joh 10:10; '
           'Joh 5:26; Joh 6:57; Heb 7:8; 1Jo 1:2; Joh 6:51; Joh 1:4; Joh 6:48; 2Cor 13:4',
    'L23': 'Rom 6:4; Rom 6:11; Gal 2:20; Phili 1:20; Phili 1:21; 2Ti 3:12; Jam 4:15; Mat 22:32; Mar 12:27; '
           'Luk 20:38; 2Cor 5:15; Rom 12:1; Heb 10:38; Tit 2:12; Rom 1:17; Gal 3:11; Gal 2:19; Rom 6:2; '
           '1Pe 2:24; 2Cor 4:10; 2Cor 4:11; 1Th 5:10; Rom 8:38; Rom 14:7; Rom 14:8; 2Cor 6:9; Phili 1:22; '
           '1Cor 3:22; 2Cor 4:12',
    'L24': 'Rom 8:2; Rom 8:10; 2Cor 3:3; 1Pe 4:6; Gal 6:8; Joh 6:63; Rom 8:6; Rom 8:13; 1Cor 15:45; '
           'Gal 5:25; Heb 12:9; Rom 8:12',
    'L25': 'Col 2:20; Joh 5:24; Joh 5:25; 1Jo 5:16; Rev 3:1; Rom 6:13; Luk 15:32; Col 3:7; 1Jo 3:14; '
           '1Jo 3:15; Eph 4:18; Rom 7:9; Rom 11:15; 2Cor 2:16; 1Ti 5:6',
    'L26': 'Gen 3:22; Gen 3:24; Gen 2:9; Dan 12:2; Rev 21:27; Rev 2:10; Rom 14:9; 2Ti 4:1; Rev 20:4; '
           '1Th 4:15; Rev 2:7; Act 10:42; 2Cor 5:4; Phili 4:3; Rev 3:5; Rev 13:8; Rev 17:8; 1Pe 4:5; '
           'Rev 20:12; Joh 5:29; Rev 22:19; Mat 7:14; Jam 1:12; Mat 18:9; Mat 18:8; Mar 9:43; Mar 9:45; '
           'Mat 25:46; Rev 20:5; Rev 22:14; Rev 22:2; 1Th 4:17; Rev 20:15',
    'L27': 'Phili 2:16; 1Pe 1:3; 1Pe 2:5; Act 11:18; 2Pe 1:3; Heb 4:12; 1Jo 1:1; Heb 10:20; Act 7:38; '
           '1Pe 3:7; Act 5:20',
    'L28': 'Psa 30:5; Pro 19:11; Isa 48:9; Job 6:11; Eze 12:22',
    'L29': 'Jer 11:19; Isa 53:8; Psa 7:5; Psa 26:9; Lam 3:53; Act 22:22; Act 28:4; Act 8:33; Act 25:24',
    'L30': '1Ki 17:23; Rev 11:11; Mat 9:18; Mar 5:23; Joh 4:50; Joh 4:51; Joh 4:53; Act 20:12; Act 9:41',
    'L31': 'Lev 18:18; Rom 7:3; Heb 9:17; 1Cor 7:39; Rom 7:2; Rom 7:1',
    'L32': 'Act 26:5; Gal 2:14',
}

HITS = {
    'Deu 6:2#17': 'L10',   # "all the days of your life" (fear the LORD)
    'Deu 6:2#21': 'L09',   # "that your days may be long"
    'Deu 32:47#9': 'L09',  # "you shall live long in the land"
    '2Cor 13:4#18': 'L23', # "we will live with him by the power of God" (5 = Christ lives: L22)
}

def main():
    verse_face = {}
    for face, refs in VERSES.items():
        for ref in (r.strip() for r in refs.split(';')):
            if ref in verse_face:
                sys.exit(f'{ref} assigned twice ({verse_face[ref]}, {face})')
            verse_face[ref] = face
    with open(PULL, encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    used_v, used_h, out, missing = set(), set(), [], []
    for r in rows:
        key = f"{r['reference']}#{r['position']}"
        if key in HITS:
            face = HITS[key]; used_h.add(key)
        elif r['reference'] in verse_face:
            face = verse_face[r['reference']]; used_v.add(r['reference'])
        else:
            missing.append(key); continue
        out.append({'reference': r['reference'], 'position': r['position'], 'face': face, 'face_name': FACES[face]})
    unused = (set(verse_face) - used_v) | (set(HITS) - used_h)
    # verses whose only hits are covered by HITS count as used
    unused = {u for u in unused if not any(h.startswith(u + '#') for h in used_h)}
    if missing or unused:
        sys.exit(f'missing: {missing}\nunused: {sorted(unused)}')
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['reference', 'position', 'face', 'face_name']); w.writeheader(); w.writerows(out)
    print(f'{len(out)} hits faced -> {os.path.basename(OUT)}')
    subprocess.run([sys.executable, os.path.join(HERE, 'strand-unit-pull-v1-20261002.py'), PULL, '--faces', OUT], check=True)

if __name__ == '__main__':
    main()
