"""#1986, 2026-10-08: scan of the plan set (m64-plan-verses-v1-20261008.csv) for the 'looking ahead' assessment.
Writes m64-plan-scan-v1-20261008.csv: each verse with the scan group and rule 72 route (A other beings / B HIB / C data only),
as assigned by hand in the verse-level scan. Read-only; no DB access."""
import csv, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
G = {
 'P1': 'Devising against another', 'P2': 'A purpose held, the mind set', 'P3': 'Weighing and deciding ahead',
 'P4': 'Devising a design (skill)', 'P5': 'Reckoning forward (years to jubilee)', 'P6': 'God sees the intention of the heart',
 'P7': 'A human plan and its outcome', 'P8': 'Devised from one\'s own heart', 'G': 'God\'s own purposing',
 'K': 'Counting, regarding, esteeming', 'X': 'No bearing (data only)'}
A = """Gen 6:5 P6 AB|Gen 8:21 P6 AB|Gen 11:6 P6 AB|Gen 15:6 K AB|Gen 31:15 K B|Gen 50:20 P1 AB|Exo 26:1 X C|Exo 26:31 X C|Exo 28:6 X C|Exo 28:15 X C|Exo 31:4 P4 AB|Exo 35:32 P4 AB|Exo 35:35 P4 AB|Exo 36:8 X C|Exo 36:35 X C|Exo 39:3 X C|Exo 39:8 X C|Lev 7:18 K A|Lev 17:4 K A|Lev 25:27 P5 C|Lev 25:31 X C|Lev 25:50 P5 C|Lev 25:52 P5 C|Lev 27:18 P5 C|Lev 27:23 P5 C|Num 18:27 K C|Num 18:30 K C|Num 23:9 K B|Deu 19:19 P1 B|Deu 31:21 P6 AB|Jos 13:3 X C|Judg 19:30 P3 B|1Sa 18:25 P1 B|2Sa 4:2 X C|2Sa 14:13 P1 B|2Sa 14:14 G AB|2Sa 19:19 K B|1Ki 10:21 X C|1Ki 12:33 P8 B|2Ki 12:15 K C|2Ki 22:7 K C|1Ch 28:9 P6 AB|1Ch 29:18 P2 AB|2Ch 2:14 P4 B|2Ch 9:20 X C|2Ch 26:15 P4 B|Neh 6:2 P1 B|Neh 6:6 P1 B|Neh 6:8 P8 B|Neh 13:13 K B|Est 8:3 P1 B|Est 9:24 P1 B|Est 9:25 P1 B|Psa 10:2 P1 B|Psa 17:3 P2 B|Psa 21:11 P1 B|Psa 31:13 P1 B|Psa 32:2 K AB|Psa 35:4 P1 B|Psa 35:20 P1 B|Psa 36:4 P1 B|Psa 37:12 P1 B|Psa 40:17 G AB|Psa 41:7 P1 B|Psa 44:22 K B|Psa 52:2 P1 B|Psa 88:4 K B|Psa 103:14 P6 AB|Psa 106:31 K AB|Psa 140:2 P1 B|Psa 140:4 P1 B|Psa 140:8 P1 B|Pro 16:9 P7 AB|Pro 16:30 P1 B|Pro 24:8 P1 B|Pro 27:14 K B|Pro 30:32 P1 B|Pro 31:16 P3 B|Isa 8:10 P7 AB|Isa 10:7 P1 B|Isa 13:17 K B|Isa 26:3 P2 AB|Isa 29:16 P6 AB|Isa 33:8 K B|Isa 40:15 K A|Isa 40:17 K A|Isa 53:3 K B|Jer 4:28 G A|Jer 11:19 P1 B|Jer 18:8 G AB|Jer 18:11 G AB|Jer 18:18 P1 B|Jer 26:3 G AB|Jer 29:11 G AB|Jer 36:3 G AB|Jer 48:2 P1 B|Jer 49:20 G A|Jer 49:30 P1 B|Jer 50:45 G A|Jer 51:12 G A|Lam 2:8 G A|Lam 2:17 G A|Lam 4:2 K B|Eze 11:2 P1 B|Eze 38:10 P1 B|Dan 6:3 P3 B|Dan 11:24 P1 B|Dan 11:25 P1 B|Hos 7:15 P1 B|Hos 8:12 K B|Amo 6:5 P4 B|Jon 1:4 X C|Mic 2:1 P1 B|Mic 2:3 G A|Nah 1:9 P1 B|Nah 1:11 P1 B|Hab 2:18 P8 B|Zec 1:6 G AB|Zec 7:10 P1 B|Zec 8:14 G A|Zec 8:15 G A|Zec 8:17 P1 B|Mal 3:16 K B|Mat 12:4 X C|Mar 2:26 X C|Luk 6:4 X C|Luk 7:30 G AB|Luk 14:31 P3 B|Luk 23:51 P3 B|Joh 11:53 P1 B|Joh 12:10 P1 B|Act 2:23 G AB|Act 4:28 G A|Act 5:33 P1 B|Act 5:38 P7 AB|Act 11:23 P2 B|Act 13:36 G AB|Act 15:37 P3 B|Act 20:27 G A|Act 27:12 P3 B|Act 27:13 P3 B|Act 27:39 P3 B|Act 27:42 P1 B|Rom 1:13 P7 B|Rom 3:25 G A|Rom 8:6 P2 B|Rom 8:7 P2 B|Rom 8:27 G A|Rom 8:28 G AB|Rom 9:11 G A|1Cor 4:5 P6 AB|2Cor 1:17 P3 B|Eph 1:9 G A|Eph 1:11 G AB|Eph 3:11 G A|2Ti 1:9 G AB|2Ti 3:10 P2 B|Heb 6:17 G AB|Heb 9:2 X C"""
m = {}
for e in A.split('|'):
    p = e.split(); m[' '.join(p[:-2])] = (p[-2], p[-1])
src = list(csv.DictReader(open(os.path.join(HERE, 'm64-plan-verses-v1-20261008.csv'), encoding='utf-8-sig')))
missing = [r['reference'] for r in src if r['reference'] not in m]; extra = set(m) - {r['reference'] for r in src}
assert not missing and not extra, (missing, extra)
with open(os.path.join(HERE, 'm64-plan-scan-v1-20261008.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh); w.writerow(['reference', 'scan_group', 'group_name', 'route', 'hit_words', 'esv_text'])
    for r in src:
        g, rt = m[r['reference']]; w.writerow([r['reference'], g, G[g], rt, r['hit_words'], r['esv_text']])
c = collections.Counter(v[0] for v in m.values()); rc = collections.Counter(v[1] for v in m.values())
for g in G: print(g, G[g], c[g])
print(rc, len(m))
