import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,121,
  note="Ps121 the keeper-psalm (8v). Almost all God-as-keeper (keeps x6). Human IB thin: the LIFTING of the eyes to seek help v1; the LIFE God keeps v7. God's help/keeps/not-slumber/shade/keep-going-out-and-coming-in = qualifiers; Ascents heading + evil/going-out/coming-in imagery = standalone.")
CH=[
 (272330,"lift up the eyes (nasa)","action","the psalmist","lift up the eyes","to seek help",GOD,"paired with the help that comes from the LORD",
  "v1: 'I LIFT UP (nasa) my eyes to the hills. From where does my help come?' - the seeking gaze of the pilgrim, looking beyond the hills to God for help."),
 (272374,"life / soul (nephesh)","faculty","the pilgrim","be kept","by the LORD",IB,"paired with God keeping from all evil",
  "v7: 'he will keep your LIFE (nephesh)' - the very self kept by God, the soul preserved from all evil."),
]
for a in CH: r.ch(*a)
LI=272374; LU=272330
QU=[
 (272337,"help (ezer)",LU,"v1: 'From where does my HELP (ezer) come?' - the help sought; God-content. Qualifier."),
 (272338,"come (bo)",LU,"v1: 'From where does my help COME (bo)?' - the coming of help from God. Qualifier."),
 (272339,"help (ezer)",LU,"v2: 'My HELP (ezer) comes from the LORD, who made heaven and earth' - God the source of help. Qualifier."),
 (272348,"be moved (mot)",LI,"v3: 'He will not let your foot be MOVED (mot)' - God's steadying of the pilgrim. Qualifier."),
 (272349,"keeps (shamar)",LI,"v3: 'he who KEEPS (shamar) you will not slumber' - God's keeping. Qualifier."),
 (272352,"slumber (num)",LI,"v3: 'he who keeps you will not SLUMBER (num)' - God's unsleeping watch. Qualifier."),
 (272354,"keeps (shamar)",LI,"v4: 'he who KEEPS (shamar) Israel will neither slumber nor sleep' - God's keeping of Israel. Qualifier."),
 (272357,"slumber (num)",LI,"v4: 'will neither SLUMBER (num)' - God's tireless keeping. Qualifier."),
 (272359,"sleep (yashen)",LI,"v4: 'nor SLEEP (yashen)' - God's ceaseless watch. Qualifier."),
 (272361,"keeper (shamar)",LI,"v5: 'The LORD is your KEEPER (shamar)' - God as the pilgrim's keeper. Qualifier."),
 (272363,"shade (tsel)",LI,"v5: 'the LORD is your SHADE (tsel) on your right hand' - God as protecting shade. Qualifier."),
 (307791,"strike (nakah)",LI,"v6: 'The sun shall not STRIKE (nakah) you by day, nor the moon by night' - God's shielding from harm. Qualifier."),
 (272368,"keep (shamar)",LI,"v7: 'The LORD will KEEP (shamar) you from all evil' - God's keeping from evil. Qualifier."),
 (272372,"keep (shamar)",LI,"v7: 'he will KEEP (shamar) your life' - God's keeping of the self. Qualifier."),
 (272376,"keep (shamar)",LI,"v8: 'The LORD will KEEP (shamar) your going out and your coming in' - God's keeping of all the pilgrim's way. Qualifier."),
]
for sid,sense,src,d in QU: r.qu(sid,sense,src,d)
for sid,sense,d in [
 (272329,"Ascents (maalah)","v0 superscription: 'A Song of ASCENTS (maalah)' - the pilgrim-song heading. Standalone."),
 (272371,"evil (ra)","v7: 'The LORD will keep you from all EVIL (ra)' - the evil God keeps the pilgrim from, object. Standalone."),
 (272377,"going out (yatsa)","v8: 'will keep your GOING OUT (yatsa)' - the pilgrim's departure, image of all his way. Standalone."),
 (272378,"coming in (bo)","v8: 'and your COMING IN (bo) from this time forth and forevermore' - the pilgrim's return, image of the whole journey God keeps. Standalone."),
]: r.st(sid,sense,d)
r.write()
