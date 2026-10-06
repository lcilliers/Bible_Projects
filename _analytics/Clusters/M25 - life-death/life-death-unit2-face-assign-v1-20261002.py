"""Life-death unit 2 (dying and death): face assignments, recorded from reading every hit.

Each hit was read by surface in the pull (life-death-unit2-dying-death-pull-v1-20261002.csv).
The assignments are written here as data so the reading is auditable and re-runnable:
  OVR  = verse-level ("ref") or hit-level ("ref#pos") faces, from reading
  rule = the fallback used only for H4191 narrative / legal hits that were read and found to be
         plain notices, sentences or killings (D01 / D02 / D03); every fallback hit was read.
Writes life-death-unit2-faces-v1-20261002.csv and merges it into the pull with
strand-unit-pull-v1-20261002.py --faces.
"""
import csv, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PULL = os.path.join(HERE, 'life-death-unit2-dying-death-pull-v1-20261002.csv')
OUT = os.path.join(HERE, 'life-death-unit2-faces-v1-20261002.csv')

FACES = {
    'D01': 'death notices, lifespans, burial, inheritance (data)',
    'D02': 'put to death under law or sentence (data)',
    'D03': 'killed or spared by people: murder, war, plots, execution, suicide (data; cf. unit 1 face C)',
    'D04': 'struck down by God; death as his judgement (sword, famine, pestilence)',
    'D05': 'near the holy: "lest you die"; seeing or hearing God (cf. unit 1 face Q)',
    'D06': 'dying of hunger, thirst, sickness or danger',
    'D07': 'before I die: last words, blessing, wishes',
    'D08': 'what death is: the common lot, the day of death, gathered to one\'s people',
    'D09': 'the dead: praise, inquiry, sleep, going to them',
    'D10': 'mourning and grief at a death',
    'D11': 'fear and anguish facing death',
    'D12': 'wanting to die; wishing one had died',
    'D13': 'ready to die for or with another',
    'D14': 'death and sin',
    'D15': 'the way to death: set before a person; paths, snares, the tongue (wisdom)',
    'D16': 'turn and do not die: God\'s will for life; the watchman (Ezekiel)',
    'D17': 'death as a power, realm or enemy',
    'D18': 'delivered from death',
    'D19': 'life beyond death: never die; death ended',
    'D20': 'the second death; judgement beyond death',
    'D21': 'Christ\'s death',
    'D22': 'died with Christ; dying to sin and the law; put to death what is earthly',
    'D23': 'death at work in the living',
    'D24': 'like the dead: the living likened to the dead; the heart that died; "dead dog"',
    'D25': 'living and dying to the Lord; the death of the upright',
    'D26': 'uncleanness from the dead (law, data)',
    'D27': 'not the inner being: animals, plants, objects, idiom',
    'D28': 'corruption: the body seeing decay (Q4 link)',
}

def v(face, *refs):
    return {r: face for r in refs}

OVR = {}
# ---- Greek -------------------------------------------------------------------------------
OVR.update(v('D20', 'Rev 21:8', 'Rev 2:11', 'Rev 20:6', 'Rev 20:14#11'))
OVR.update(v('D21', 'Act 2:24', 'Rom 5:6', 'Rom 5:8', 'Rom 6:9', 'Rom 8:34', 'Rom 14:15', '1Cor 8:11',
             '1Cor 15:3', '2Cor 5:14#9', 'Gal 2:21', 'Heb 5:7', 'Joh 12:33', 'Joh 11:51', 'Luk 23:15',
             '2Cor 5:15', 'Mat 26:66', 'Luk 23:22', 'Joh 18:32', 'Heb 9:15', 'Mar 15:44', 'Mat 20:18',
             'Mar 10:33', 'Mar 14:64', 'Luk 24:20', 'Col 1:22', 'Joh 18:14', 'Act 13:28', 'Heb 2:9',
             '1Th 4:14', 'Joh 19:7', 'Rom 5:10', 'Rom 6:10', 'Rev 1:18', '1Cor 11:26', 'Phili 2:8',
             'Joh 11:50', '1Th 5:10', 'Heb 2:14#14'))
OVR.update(v('D13', 'Rev 2:10', 'Phili 2:30', '1Cor 9:15', 'Mat 26:35', 'Rom 5:7', 'Act 21:13', 'Act 25:11',
             'Luk 22:33', 'Joh 11:16', 'Rev 12:11'))
OVR.update(v('D19', 'Rev 21:4', 'Joh 8:51', 'Joh 8:52#22', 'Joh 11:25', 'Joh 11:26', '2Ti 1:10',
             '1Cor 15:54', 'Luk 20:36', 'Heb 11:5', 'Joh 6:50', '1Cor 15:36'))
OVR.update(v('D08', 'Luk 2:26', 'Mat 16:28', 'Mar 9:1', 'Luk 9:27', '1Cor 15:22', 'Joh 8:52#9', 'Joh 21:23',
             'Heb 9:27', 'Heb 7:23', 'Joh 6:58', 'Joh 8:53', '1Cor 15:21', '1Cor 15:32', 'Heb 7:8', 'Joh 6:49'))
OVR.update(v('D28', 'Act 2:31', 'Act 13:35', 'Act 13:34', 'Act 2:27', 'Act 13:36', 'Act 13:37'))
OVR.update(v('D14', 'Rom 5:15', 'Rom 5:17', 'Rom 5:21', 'Rom 6:23', 'Rom 8:2', '1Jo 5:16', 'Rom 1:32',
             'Joh 8:21', 'Joh 8:24', 'Jam 1:15', '1Jo 5:17', 'Rom 5:12', 'Rom 6:16', '1Cor 15:56',
             'Rom 8:13', 'Rom 6:21'))
OVR.update(v('D22', 'Rom 6:3', 'Rom 6:4', 'Rom 6:8', '2Cor 5:14#14', 'Col 2:20', 'Col 3:3', 'Rom 7:6',
             'Rom 6:5', 'Col 3:5', 'Gal 2:19', 'Rom 6:2', 'Rom 6:7'))
OVR.update(v('D25', 'Rom 14:9', '1Cor 15:31', 'Phili 1:20', 'Phili 1:21', 'Joh 12:24', 'Joh 21:19',
             'Rev 14:13', 'Heb 11:13', 'Heb 11:4', 'Heb 11:21', 'Phili 3:10', '2Cor 4:11', 'Rom 14:7',
             'Rom 14:8', '2Cor 6:9', '1Cor 3:22', '2Cor 4:12'))
OVR.update(v('D06', '2Cor 11:23', 'Joh 4:49', 'Joh 11:4', 'Phili 2:27', 'Joh 11:37', 'Joh 4:47', 'Luk 8:42'))
OVR.update(v('D11', 'Heb 2:15', 'Mat 26:38', 'Mar 14:34', '2Cor 1:9'))
OVR.update(v('D04', 'Rev 8:11', 'Rev 6:8#30', 'Rev 18:8', 'Heb 11:31', 'Rev 2:23'))
OVR.update(v('D09', 'Mat 9:24', 'Mar 5:39', 'Joh 11:13', 'Luk 16:22', 'Luk 8:52', 'Luk 8:53'))
OVR.update(v('D02', 'Mat 15:4', 'Act 25:25', 'Mar 7:10', 'Heb 10:28', 'Act 23:29', 'Act 28:18', 'Act 26:31'))
OVR.update(v('D01', 'Mat 22:24', 'Mar 5:35', 'Mar 9:26', 'Luk 20:28', 'Joh 11:14', 'Rom 7:3', 'Heb 9:16',
             'Mar 12:19', 'Mar 12:20', 'Mar 12:22', 'Luk 20:29', 'Act 9:37', 'Rom 7:2', 'Mat 22:27',
             'Mar 12:21', 'Luk 20:31', 'Luk 20:32', 'Act 7:4'))
OVR.update(v('D10', 'Joh 11:32'))
OVR.update(v('D18', 'Joh 5:24', 'Jam 5:20', '1Jo 3:14#5', '2Cor 1:10'))
OVR.update(v('D23', 'Jude 12', 'Rom 7:13', '2Cor 7:10', 'Rev 3:2', 'Rom 7:5', 'Rom 7:9', 'Rom 8:6',
             '1Jo 3:14#15', '2Cor 3:7', 'Mat 4:16', 'Luk 1:79', 'Rom 7:10', 'Rom 7:24', '2Cor 2:16'))
OVR.update(v('D17', 'Rev 6:8#10', 'Rom 5:14', 'Rev 20:13', 'Heb 2:14#18', 'Rom 8:38', '1Cor 15:26',
             '1Cor 15:55', 'Rev 20:14#1'))
OVR.update(v('D12', 'Rev 9:6'))
OVR.update(v('D03', 'Luk 10:30', 'Heb 11:37', 'Act 22:4', 'Mat 10:21', 'Mar 13:12'))
OVR.update(v('D24', 'Rom 4:19', 'Heb 11:12'))
OVR.update(v('D27', 'Mat 8:32', 'Rev 8:9', 'Rev 16:3', 'Rev 13:3', 'Rev 13:12'))

# ---- H4194 (death) and H4191 (to die) -------------------------------------------------------
OVR.update(v('D01', 'Gen 25:11', 'Gen 26:18', 'Num 35:25', 'Num 35:28', 'Num 35:32', 'Jos 1:1', 'Jos 20:6',
             'Judg 1:1', 'Judg 13:7', 'Rut 2:11', '1Sa 15:35', '2Sa 1:1', '2Sa 6:23', '1Ki 11:40#15',
             '2Ki 1:1', '2Ki 3:5', '2Ki 14:17', '2Ki 15:5', '1Ch 2:24', '2Ch 22:4', '2Ch 24:15',
             '2Ch 24:17', '2Ch 25:25', '2Ch 26:21', '2Ch 32:33', 'Est 2:7', 'Isa 6:1', 'Isa 14:28',
             'Jer 52:11', 'Jer 52:34', 'Gen 50:15', 'Num 20:28', 'Deu 24:3', 'Deu 25:5', 'Deu 25:6',
             '2Sa 4:1', '2Ki 4:1', '2Ki 4:20', '2Ki 4:32', 'Job 1:19', '1Ki 3:19', '1Ki 3:20', '1Ki 3:21',
             '1Ki 3:22', '1Ki 3:23', 'Num 27:8'))
OVR.update(v('D07', 'Gen 27:7', 'Gen 27:10', 'Gen 50:16', 'Deu 31:27', 'Deu 31:29', 'Deu 33:1', '1Ki 13:31',
             '1Ch 22:5', 'Gen 27:4', 'Gen 45:28', 'Gen 46:30', 'Gen 47:29', 'Gen 48:21', 'Gen 50:5',
             'Gen 50:24', 'Deu 4:22', 'Deu 31:14', 'Deu 33:6', '2Sa 19:37', '1Ki 2:1', 'Pro 30:7'))
OVR.update(v('D08', 'Gen 27:2', 'Num 16:29', 'Job 30:23', 'Psa 49:17', 'Psa 73:4', 'Psa 89:48', 'Pro 11:7',
             'Ecc 3:19', 'Ecc 7:1', 'Ecc 8:8', 'Eze 31:14', 'Gen 7:22', 'Gen 25:8', 'Gen 25:17', 'Gen 35:18',
             'Gen 35:29', 'Num 20:26', 'Deu 32:50', '1Sa 26:10', '2Sa 14:14', 'Job 4:21', 'Job 9:23',
             'Job 14:10', 'Job 14:14', 'Job 21:23', 'Job 21:25', 'Job 34:20', 'Psa 49:10', 'Psa 82:7',
             'Ecc 2:16', 'Ecc 3:2', 'Ecc 7:17', 'Ecc 9:3', 'Ecc 9:4', 'Ecc 9:5', 'Isa 22:13', 'Isa 51:6',
             'Isa 65:20'))
OVR.update(v('D04', 'Exo 10:17', 'Job 27:15', 'Psa 55:15', 'Psa 78:50', 'Jer 15:2', 'Jer 18:21', 'Jer 43:11',
             'Eze 28:10', 'Gen 18:25', 'Gen 20:3', 'Gen 20:7', 'Gen 38:7', 'Gen 38:10', 'Exo 4:24',
             'Exo 9:19', 'Exo 11:5', 'Exo 12:30', 'Exo 14:30', 'Lev 10:2', 'Lev 20:20', 'Num 3:4',
             'Num 14:15', 'Num 14:35', 'Num 14:37', 'Num 16:41', 'Num 16:48', 'Num 16:49', 'Num 17:10',
             'Num 21:6', 'Num 25:9', 'Num 26:10', 'Num 26:11', 'Num 26:61', 'Num 26:65', 'Deu 2:16',
             'Deu 9:28', 'Deu 32:39', 'Jos 5:4', 'Jos 10:11', 'Judg 1:7', '1Sa 2:6', '1Sa 2:25', '1Sa 2:33',
             '1Sa 2:34', '1Sa 4:11', '1Sa 5:12', '1Sa 25:38', '1Sa 25:39', '2Sa 6:7', '2Sa 12:14',
             '2Sa 24:15', '1Ki 13:24', '1Ki 13:26', '1Ki 14:11', '1Ki 14:12', '1Ki 14:17', '1Ki 16:4',
             '1Ki 17:20', '1Ki 19:17', '1Ki 21:24', '2Ki 1:4', '2Ki 1:6', '2Ki 1:16', '2Ki 1:17', '2Ki 5:7',
             '2Ki 7:17', '2Ki 7:20', '2Ki 8:10', '2Ki 17:26', '2Ki 19:35', '1Ch 2:3', '1Ch 10:14',
             '1Ch 13:10', '1Ch 24:2', '2Ch 13:20', '2Ch 21:19', 'Job 36:14', 'Isa 11:4', 'Isa 14:30',
             'Isa 22:2', 'Isa 22:18', 'Isa 37:36', 'Isa 65:15', 'Jer 11:22', 'Jer 16:4', 'Jer 16:6',
             'Jer 20:6', 'Jer 21:6', 'Jer 21:9', 'Jer 22:12', 'Jer 22:26', 'Jer 27:13', 'Jer 28:16',
             'Jer 28:17', 'Jer 38:2', 'Jer 42:16', 'Jer 42:17', 'Jer 42:22', 'Jer 44:12', 'Eze 5:12',
             'Eze 6:12', 'Eze 7:15', 'Eze 11:13', 'Eze 12:13', 'Eze 17:16', 'Eze 28:8', 'Eze 33:27',
             'Hos 2:3', 'Hos 9:16', 'Amo 2:2', 'Amo 6:9', 'Amo 7:11', 'Amo 7:17', 'Amo 9:10', 'Zec 11:9'))
OVR.update(v('D05', 'Lev 16:1', 'Exo 19:12', 'Exo 20:19', 'Exo 28:35', 'Exo 28:43', 'Exo 30:20', 'Exo 30:21',
             'Lev 8:35', 'Lev 10:6', 'Lev 10:7', 'Lev 10:9', 'Lev 15:31', 'Lev 16:2', 'Lev 16:13', 'Lev 22:9',
             'Num 1:51', 'Num 3:10', 'Num 3:38', 'Num 4:15', 'Num 4:19', 'Num 4:20', 'Num 17:13', 'Num 18:3',
             'Num 18:7', 'Num 18:22', 'Num 18:32', 'Deu 5:25', 'Deu 18:16', 'Judg 6:23', 'Judg 13:22',
             'Judg 13:23'))
OVR.update(v('D25', 'Num 23:10', 'Psa 116:15', 'Pro 14:32', 'Jer 34:4', 'Jer 34:5'))
OVR.update(v('D26', 'Num 6:7', 'Lev 11:39', 'Lev 21:11', 'Num 6:6', 'Num 6:9', 'Num 19:11', 'Num 19:13',
             'Num 19:14', 'Num 19:16', 'Num 19:18', 'Eze 44:25'))
OVR.update(v('D27', 'Lev 11:31', 'Lev 11:32', 'Ecc 10:1', 'Gen 33:13', 'Exo 7:18', 'Exo 7:21', 'Exo 8:13',
             'Exo 9:4', 'Exo 9:6', 'Exo 9:7', 'Exo 21:34', 'Exo 21:35', 'Exo 21:36', 'Exo 22:10', 'Exo 22:14',
             'Job 12:2', 'Job 14:8', 'Psa 48:14', 'Psa 105:29', 'Isa 50:2', 'Isa 59:5'))
OVR.update(v('D02', 'Deu 19:6', 'Deu 21:22', 'Deu 22:26', '1Sa 26:16', '2Sa 12:5', '1Ki 2:26#10', 'Jer 26:11',
             'Jer 26:16', 'Gen 26:11', 'Judg 20:13', 'Judg 21:5', '2Ch 15:13', 'Est 4:11', 'Deu 18:20',
             'Jos 1:18', 'Jos 20:9'))
OVR.update(v('D15', 'Deu 30:15', 'Deu 30:19', 'Pro 2:18', 'Pro 5:5', 'Pro 7:27', 'Pro 8:36', 'Pro 10:2',
             'Pro 11:4', 'Pro 11:19', 'Pro 12:28', 'Pro 13:14', 'Pro 14:12', 'Pro 14:27', 'Pro 16:14',
             'Pro 16:25', 'Pro 18:21', 'Pro 21:6', 'Pro 26:18', 'Ecc 7:26', 'Jer 21:8', 'Job 5:2', 'Psa 34:21',
             'Pro 5:23', 'Pro 10:21', 'Pro 15:10', 'Pro 19:16', 'Pro 19:18', 'Pro 21:25', 'Pro 23:13',
             'Eze 13:19'))
OVR.update(v('D03', 'Jos 2:13', '1Sa 20:31', '2Sa 19:28', 'Psa 7:13', 'Jer 18:23', 'Gen 42:20', 'Gen 42:37',
             'Gen 44:9', 'Exo 10:28', 'Jos 10:26', 'Jos 11:17', 'Judg 3:25', 'Judg 4:21', 'Judg 4:22',
             'Judg 6:30', 'Judg 6:31', 'Judg 9:49', 'Judg 9:54#14', 'Judg 9:55', 'Judg 15:13', 'Judg 16:30#15',
             'Judg 16:30#16', 'Judg 16:30#17', 'Judg 16:30#19', 'Judg 20:5', '1Sa 14:39', '1Sa 14:44', '1Sa 14:45', '1Sa 20:2',
             '1Sa 20:14', '1Sa 28:9', '1Sa 31:5', '1Sa 31:6', '1Sa 31:7', '2Sa 1:10', '2Sa 2:23', '2Sa 3:27',
             '2Sa 10:18', '2Sa 11:17', '2Sa 11:21', '2Sa 11:24', '2Sa 17:23', '2Sa 19:23', '2Sa 20:10',
             '2Sa 20:19', '1Ki 1:52', '1Ki 2:25', '1Ki 2:30', '1Ki 2:37', '1Ki 2:42', '1Ki 2:46', '1Ki 3:26',
             '1Ki 3:27', '1Ki 16:18', '1Ki 21:14', '1Ki 21:15', '1Ki 21:16', '2Ki 8:15', '2Ki 9:27',
             '2Ki 12:21', '2Ki 23:30', '1Ch 10:5', '1Ch 10:6', '1Ch 10:7', '2Ch 22:10', '2Ch 24:22',
             '2Ch 24:25', 'Psa 37:32', 'Psa 59:1', 'Psa 109:16', 'Jer 11:21', 'Jer 26:8', 'Jer 26:15',
             'Jer 26:19', 'Jer 26:21', 'Jer 26:24', 'Jer 38:4', 'Jer 38:15', 'Jer 38:16', 'Jer 38:24',
             'Jer 38:25', 'Jer 38:26', 'Jer 41:2', 'Jer 41:4', 'Jer 41:8', 'Jer 43:3', 'Jer 52:27'))
OVR.update(v('D06', '2Ki 2:21', '2Ki 4:40', 'Psa 107:18', 'Gen 25:32', 'Gen 42:2', 'Gen 43:8', 'Gen 47:15',
             'Gen 47:19', 'Deu 20:5', 'Deu 20:6', 'Deu 20:7', 'Judg 15:18', '2Sa 18:3', '1Ki 17:12',
             '2Ki 7:3', '2Ki 7:4', '2Ki 13:14', '2Ki 18:32', '2Ki 20:1', '2Ch 32:11', '2Ch 32:24', 'Job 33:22',
             'Isa 38:1', 'Jer 37:20', 'Jer 38:9', 'Jer 38:10'))
OVR.update(v('D09', 'Psa 6:5', 'Isa 38:18', 'Deu 18:11', 'Deu 26:14', 'Rut 1:8', 'Rut 2:20', '2Sa 12:23',
             '2Ki 8:5', 'Psa 88:10', 'Psa 106:28', 'Psa 115:17', 'Isa 8:19', 'Isa 26:14'))
OVR.update(v('D10', 'Gen 21:16', '2Sa 3:33', 'Gen 42:38', 'Gen 44:22', 'Gen 44:31', 'Gen 48:7', 'Deu 14:1',
             '1Sa 4:20', '2Sa 11:26', '2Sa 12:18', '2Sa 12:19', '2Sa 12:21', '2Sa 13:33', '2Sa 13:39',
             '2Sa 14:2', '2Sa 18:33', '2Sa 19:6', 'Jer 16:7', 'Jer 22:10', 'Eze 24:17', 'Eze 24:18'))
OVR.update(v('D11', '1Sa 5:11', '1Sa 15:32', '1Sa 20:3', 'Psa 13:3', 'Psa 22:15', 'Psa 55:4', 'Lam 1:20',
             'Gen 19:19', 'Gen 26:9', 'Gen 38:11', 'Exo 12:33', 'Judg 16:16', '1Sa 5:10', '1Sa 12:19',
             'Psa 41:5', 'Isa 51:12'))
OVR.update(v('D12', 'Judg 16:30#3', 'Job 3:21', 'Job 7:15', 'Jer 8:3', 'Jon 4:3', 'Jon 4:8',
             'Jon 4:9', 'Gen 30:1', 'Exo 14:11', 'Exo 14:12', 'Exo 16:3', 'Exo 17:3', 'Num 14:2', 'Num 16:13',
             'Num 20:4', 'Num 21:5', 'Judg 9:54#8', '2Sa 1:9', '1Ki 19:4', 'Job 2:9', 'Job 3:11', 'Ecc 4:2',
             'Jer 20:17'))
OVR.update(v('D13', 'Rut 1:17', '2Sa 1:23', '2Sa 15:21', 'Jos 2:14', 'Judg 5:18', '1Sa 14:43'))
OVR.update(v('D14', 'Gen 2:17', 'Gen 3:3', 'Gen 3:4', 'Num 27:3', 'Deu 24:16', '2Sa 12:13', '1Ki 17:18',
             '2Ki 14:6', '1Ch 10:13', '2Ch 25:4', 'Isa 22:14', 'Jer 31:30', 'Eze 18:4', 'Eze 18:13',
             'Eze 18:17', 'Eze 18:18', 'Eze 18:20', 'Hos 13:1'))
OVR.update(v('D16', 'Eze 18:23', 'Eze 18:32', 'Eze 33:11', 'Eze 3:18', 'Eze 3:19', 'Eze 3:20', 'Eze 18:21',
             'Eze 18:24', 'Eze 18:26', 'Eze 18:28', 'Eze 18:31', 'Eze 33:8', 'Eze 33:9', 'Eze 33:13',
             'Eze 33:14', 'Eze 33:15', 'Eze 33:18'))
OVR.update(v('D17', '2Sa 22:5', '2Sa 22:6', 'Job 18:13', 'Job 28:22', 'Job 38:17', 'Psa 18:4', 'Psa 18:5',
             'Psa 49:14', 'Psa 116:3', 'Song 8:6', 'Isa 28:15', 'Isa 28:18', 'Jer 9:21', 'Hos 13:14#5',
             'Hab 2:5'))
OVR.update(v('D18', 'Job 5:20', 'Psa 9:13', 'Psa 33:19', 'Psa 56:13', 'Psa 68:20', 'Psa 116:8', 'Psa 118:18',
             'Pro 24:11', 'Hos 13:14#4', 'Psa 118:17', 'Isa 51:14', 'Hab 1:12'))
OVR.update(v('D19', 'Isa 25:8', 'Isa 26:19'))
OVR.update(v('D20', 'Isa 66:24'))
OVR.update(v('D21', 'Isa 53:9', 'Isa 53:12'))
OVR.update(v('D24', 'Num 12:12', '1Sa 24:14', '1Sa 25:37', '2Sa 9:8', '2Sa 16:9', 'Psa 31:12', 'Psa 88:5',
             'Psa 143:3', 'Isa 59:10', 'Lam 3:6'))

# Narrative killings whose surface is "death" / "dead" / "die" (the fallback would call them notices),
# and plain notices inside Exodus-Deuteronomy (the fallback would call them legal).
OVR.update(v('D03', '1Ki 1:51', '2Ki 21:23', '1Sa 11:12', '1Sa 22:16', '2Sa 1:15', '2Sa 4:10', '2Sa 11:15',
             '2Sa 21:1', '2Sa 21:4', '1Ki 21:10', '1Ki 21:13', '1Ki 12:18', '2Ch 10:18', '1Sa 17:51',
             '1Sa 20:33', '2Sa 3:30', '2Sa 13:32', 'Exo 1:16'))
OVR.update(v('D01', 'Exo 1:6', 'Exo 2:23', 'Exo 4:19', 'Deu 34:5', 'Deu 34:7', 'Deu 10:6', 'Num 20:1',
             'Num 26:19', 'Num 33:38', 'Num 33:39'))

DIED = {'died', 'dead', 'dies', 'dying', 'died naturally', 'died out', 'dead man', 'man', 'death', 'die'}
LAW = ('Exo ', 'Lev ', 'Num ', 'Deu ')

rows = list(csv.DictReader(open(PULL, encoding='utf-8')))
used = set()
out = []
for r in rows:
    ref, pos = r['reference'], r['position']
    k = f'{ref}#{pos}'
    if k in OVR:
        f = OVR[k]; used.add(k)
    elif ref in OVR:
        f = OVR[ref]; used.add(ref)
    elif r['strong'] == 'H4191':
        s = r['surface'].lower()
        if ref.startswith(LAW):
            f = 'D02'
        elif s in DIED:
            f = 'D01'
        else:
            f = 'D03'
    else:
        sys.exit(f'unassigned non-H4191 hit: {k} {r["strong"]}')
    out.append({'reference': ref, 'position': pos, 'face': f, 'face_name': FACES[f]})
unused = sorted(set(OVR) - used)
if unused:
    sys.exit(f'override keys that match no hit: {unused}')
with open(OUT, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['reference', 'position', 'face', 'face_name'])
    w.writeheader(); w.writerows(out)
print(f'{len(out)} faces written')
subprocess.run([sys.executable, os.path.join(HERE, 'strand-unit-pull-v1-20261002.py'), PULL, '--faces', OUT], check=True)
