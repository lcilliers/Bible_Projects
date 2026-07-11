#!/usr/bin/env python
"""Ps 41 (blessed is the one who considers the poor; the betrayal; Book I close).
IB ops: the blessedness of considering the poor (compassion); confessing sin
while pleading for healing; the false visitor's hypocrisy (empty words, heart
gathering malice); the deep wound of betrayal by a trusted friend who ate the
psalmist's bread; the assurance of God's delight; the integrity for which God
upholds him; the closing doxology of Book I."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=41
r = Reading("Psa", 19, CH, note="Consider-the-poor + betrayal (Book I close): compassion, confess-and-heal, false-visitor, friend's-betrayal, God-delights, upheld-for-integrity, doxology")

r.ch(278395,"blessed is the one who considers the poor","affect","the compassionate","blessed is the one who considers the poor; in the day of trouble the LORD delivers him - compassion that is itself blessed","compassion","consider-the-poor",IB,
     "v1: 'BLESSED is the one who CONSIDERS the poor! In the day of trouble the LORD delivers him' - the operation is an attentive care for the weak; the interior that weighs the poor's plight is pronounced happy and kept.")
r.ch(278456,"heal me, for I have sinned against you","cognition","the psalmist","the self asks God to be gracious and heal it, confessing that it has sinned against him - healing sought with confession","penitent-plea","heal-me-i-sinned",IB,
     "v4: 'O LORD, be gracious to me; HEAL me, for I have SINNED against you!' - the operation joins petition to confession: the interior does not plead innocence but asks healing while owning its sin.")
r.ch(278469,"empty words, heart gathering malice","cognition","the false visitor","when one comes to see the self he utters empty words, while his heart gathers iniquity, and going out he tells it abroad - hollow sympathy masking inner malice","false-sympathy","empty-words-heart-malice",IB,
     "v6: 'when one comes to SEE me, he utters EMPTY words, while his HEART GATHERS iniquity; when he goes out, he tells it abroad' - the operation exposes a split interior: the visitor's mouth offers comfort while his heart hoards malice to spread.")
r.ch(278491,"my trusted friend has lifted his heel","affect","the psalmist","even the self's close friend, in whom it trusted, who ate its bread, has lifted his heel against it - the wound of intimate betrayal","betrayal","friend-lifts-heel",IB,
     "v9: 'Even my close FRIEND in whom I TRUSTED, who ATE my bread, has LIFTED his heel against me' - the operation is the sharpest social wound: the interior is stabbed by the very one it had drawn closest and fed.")
r.ch(278410,"by this I know you delight in me","cognition","the psalmist","by this the self knows God delights in it: its enemy does not shout in triumph over it - assurance read from the outcome","assurance-of-favour","know-you-delight",IB,
     "v11: 'By this I KNOW that you DELIGHT in me: my enemy will not shout in triumph over me' - the operation is confidence inferred from deliverance: the interior reads God's favour in the enemy's silencing.")
r.ch(278419,"you uphold me because of my integrity","affect","the psalmist","God has upheld the self because of its integrity and set it in his presence forever - integrity that God sustains","upheld-integrity","upheld-for-integrity",IB,
     "v12: 'But you have UPHELD me because of my INTEGRITY, and set me in your presence forever' - the operation is the self's confidence that its uprightness is honoured: God holds it up and stations it before his face.")
r.ch(278423,"blessed be the LORD, from everlasting to everlasting","affect","the psalmist","the self blesses the LORD, the God of Israel, from everlasting to everlasting - the doxology closing Book I","doxology","bless-everlasting",IB,
     "v13: 'BLESSED be the LORD, the God of Israel, from EVERLASTING to everlasting! Amen and Amen' - the operation seals Book I in blessing; the interior lifts God above the whole span of time.")

for sid,sense,src,d in [
 (278401,"the LORD delivers him",278395,"v1: 'in the day of trouble the LORD DELIVERS him' - the keeping promised to the one who considers the poor."),
 (278454,"heal me",278456,"v4: 'HEAL me' - the restoration the confession pleads for."),
 (278405,"raise me up",278419,"v10: 'be gracious to me, and RAISE me up' - the lifting the integrity-upheld self asks for."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (sickbed/health imagery, enemies'-malice-whispers, or God's-act label); standalone.")
r.write()
