#!/usr/bin/env python
"""Ps 32 (the great confession psalm). IB ops: the beatitude of forgiveness; the
blessedness of a spirit without deceit (guilelessness); the wasting of
unconfessed sin (silence rotting the bones); the crushing weight of God's hand;
the turn - acknowledging and confessing sin instead of covering it; the godly
praying while God may be found; the warning against being a senseless mule
(willing understanding vs forced curbing); the one who trusts surrounded by love;
the summons to the upright to be glad. God's forgive/preserve/instruct =
qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=32
r = Reading("Psa", 19, CH, note="Confession psalm: beatitude of forgiveness, guileless spirit, silence-wastes-bones, heavy hand, the confessing turn, godly pray while found, not-a-mule understanding, trust surrounded by love, upright glad")

r.ch(276872,"blessed is the forgiven","affect","the forgiven one","the self pronounces blessed the one whose transgression is forgiven, whose sin is covered - happiness located in pardon","beatitude-of-pardon","blessed-forgiven",IB,
     "v1: 'BLESSED is the one whose transgression is FORGIVEN, whose sin is COVERED' - the operation weighs a life as happy not for innocence but for forgiveness; the interior's relief at being pardoned.")
r.ch(276898,"a spirit without deceit","cognition","the forgiven one","blessed is the one in whose spirit there is no deceit - a transparency before God that has stopped hiding","guilelessness","spirit-no-deceit",IB,
     "v2: 'blessed is the man against whom the LORD counts no iniquity, and in whose SPIRIT there is no DECEIT' - the operation is an interior that has quit self-deception; the guile is gone because the sin is confessed.")
r.ch(276902,"kept silent, my bones wasted","state","the psalmist","when the self kept silent about its sin, its bones wasted away through its groaning all day - concealment corroding the body","concealment's-cost","silence-wastes",IB,
     "v3: 'For when I kept SILENT, my bones WASTED AWAY through my GROANING all day long' - the operation is the self-destruction of the unconfessed: the interior, refusing to speak, rots itself.")
r.ch(276913,"your hand was heavy on me","state","the psalmist","day and night God's hand was heavy on the self; its strength dried up as by summer heat - the felt pressure of conviction","conviction's-weight","heavy-hand",IB,
     "v4: 'For day and night your HAND was HEAVY upon me; my strength was DRIED UP as by the heat of summer' - the operation is the crushing weight of unrelieved guilt; the interior is pressed dry until it must confess.")
r.ch(276927,"I confessed and did not cover it","volition","the psalmist","the self acknowledged its sin, did not cover its iniquity, resolved to confess - and God forgave - the decisive turn","confessing-turn","acknowledge-confess",IB,
     "v5: 'I ACKNOWLEDGED my sin to you, and I did not COVER my iniquity... I will CONFESS my transgressions, and you FORGAVE the iniquity of my sin' - the operation is the hinge of the psalm: the interior stops hiding and speaks, and forgiveness follows at once.")
r.ch(276938,"let the godly pray while you may be found","volition","the godly","therefore let everyone who is godly offer prayer at a time when God may be found, safe from the rush of great waters - urgency of seeking while there is time","timely-prayer","pray-while-found",IB,
     "v6: 'let everyone who is GODLY OFFER PRAYER to you at a time when you may be FOUND' - the operation draws the lesson: the interior should seek God now, in the window of grace, before the flood.")
r.ch(276969,"be not like a horse or mule, without understanding","cognition","the hearer","the self is warned not to be like a senseless horse or mule that must be curbed with bit and bridle - the call to willing understanding rather than forced compliance","teachable-understanding","not-a-mule",IB,
     "v9: 'Be not like a HORSE or a mule, without UNDERSTANDING, which must be CURBED with bit and bridle' - the operation contrasts two interiors: the one that understands and comes freely, and the brute that must be dragged.")
r.ch(276882,"steadfast love surrounds the one who trusts","affect","the one who trusts","many are the sorrows of the wicked, but steadfast love surrounds the one who trusts in the LORD - trust encircled by love","encircling-love","trust-surrounded",IB,
     "v10: 'steadfast love SURROUNDS the one who TRUSTS in the LORD' - the operation sets the trusting interior inside a ring of love, over against the wicked's many sorrows.")
r.ch(276884,"be glad and shout for joy, you upright","affect","the righteous / upright","the self calls the righteous to be glad in the LORD, to rejoice and shout for joy, all the upright in heart - the confession ending in communal joy","summons-to-joy","glad-and-shout",IB,
     "v11: 'Be GLAD in the LORD, and REJOICE, O righteous, and shout for JOY, all you upright in heart!' - the operation closes the psalm by turning the relief of forgiveness into a summons for all the upright to rejoice.")

for sid,sense,src,d in [
 (276931,"you forgave my iniquity",276927,"v5: 'and you FORGAVE the iniquity of my sin' - the pardon that answered the confession."),
 (276950,"you preserve me from trouble",276938,"v7: 'you PRESERVE me from trouble; you surround me with shouts of deliverance' - the hiding-place the godly pray to."),
 (276957,"I will instruct you in the way",276969,"v8: 'I will INSTRUCT you and TEACH you in the way you should go' - the divine guidance the mule-warning presses the hearer to receive willingly."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (bit/bridle/waters imagery, God's-deliverance label, or repeated sin/iniquity noun carried by a char); standalone.")
r.write()
