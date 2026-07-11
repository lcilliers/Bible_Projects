#!/usr/bin/env python
"""Ps 31 ('into your hand I commit my spirit', 90 spans). IB ops: refuge-taking;
the total entrustment of the spirit; trust in God vs regard for idols; rejoicing
in the love that sees the soul's distress; life spent with sorrow; the shame of
being shunned (a reproach, dreaded, fled from); feeling forgotten like the dead;
the terror of encircling whispered plots; the turn 'my times are in your hand';
the fear/refuge for whom goodness is stored; blessing God for wondrous love; the
alarm of feeling cut off, then heard; summoning the saints to love God; the
exhortation to courage while waiting."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=31
r = Reading("Psa", 19, CH, note="Commit-my-spirit: refuge, entrust-spirit, trust-vs-idols, rejoice-in-love, life-spent-sorrow, shunned-reproach, forgotten, terror-of-plots, times-in-hand, fear/stored-goodness, bless, alarm-cut-off, love-God saints, courage-in-waiting")

r.ch(276660,"in you I take refuge","affect","the psalmist","the self takes refuge in God, asking never to be put to shame and to be delivered in his righteousness","refuge-taking","take-refuge",IB,
     "v1: 'In you, O LORD, do I TAKE REFUGE; let me never be put to shame' - the interior shelters in God as the psalm's opening posture; refuge is where the whole plea is spoken from.")
r.ch(276830,"into your hand I commit my spirit","affect","the psalmist","the self commits its spirit into God's hand, resting on him as its redeemer - total entrustment","entrustment","commit-my-spirit",IB,
     "v5: 'Into your hand I COMMIT my SPIRIT; you have redeemed me, O LORD, faithful God' - the operation is the handing-over of the innermost self; the interior places its very spirit in God's keeping.")
r.ch(276840,"I trust in the LORD, not idols","affect","the psalmist","the self hates those who pay regard to worthless idols, and trusts instead in the LORD - reliance fixed on God against emptiness","idol-refusing-trust","trust-not-idols",IB,
     "v6: 'I HATE those who pay regard to worthless idols, but I TRUST in the LORD' - the operation contrasts two directions of reliance: the interior refuses the empty gods and rests on God.")
r.ch(276842,"rejoice in the love that sees my soul","affect","the psalmist","the self will rejoice and be glad in God's steadfast love, because he has seen its affliction and known the distress of its soul - joy that God knows the interior","being-known","rejoice-love-sees",IB,
     "v7: 'I will REJOICE and be glad in your steadfast love, because you have seen my affliction; you have KNOWN the distress of my SOUL' - the operation is joy grounded in being seen; the interior rejoices that its hidden distress is known to God.")
r.ch(276668,"my life is spent with sorrow","state","the psalmist","the self's life is spent with sorrow, its years with sighing, strength failing through iniquity, bones wasting - a whole life eroded by grief","erosion","life-spent-sorrow",IB,
     "v10: 'For my life is SPENT with SORROW, and my years with SIGHING; my strength fails... and my bones waste away' - the operation is depletion over time: the interior and body worn down by prolonged grief.")
r.ch(276683,"a reproach, dreaded, fled from","state","the psalmist","because of adversaries the self has become a reproach, an object of dread to acquaintances, fled from in the street - the pain of social rejection","social-shame","reproach-shunned",IB,
     "v11: 'I have become a REPROACH... an object of DREAD to my acquaintances; those who see me in the street FLEE from me' - the operation is the wound of being shunned; the interior suffers the withdrawal of everyone.")
r.ch(276692,"forgotten like one who is dead","state","the psalmist","the self has been forgotten like a dead man, become like a broken vessel - the sense of being erased and discarded","erasure","forgotten-like-dead",IB,
     "v12: 'I have been FORGOTTEN like one who is dead; I have become like a broken vessel' - distinct from being shunned: this is the sense of having dropped out of memory entirely, useless and cast aside.")
r.ch(276699,"terror on every side, they plot my life","affect","the psalmist","the self hears the whispering of many, terror on every side, as they scheme and plot to take its life - dread of an encircling conspiracy","encircled-dread","terror-on-every-side",IB,
     "v13: 'For I hear the WHISPERING of many - TERROR on every side! - as they SCHEME together against me, as they PLOT to take my life' - the operation is the dread of surrounding malice; the interior feels the net of conspiracy closing.")
r.ch(276708,"my times are in your hand","affect","the psalmist","against the terror the self trusts, saying 'you are my God; my times are in your hand' - the whole course of life entrusted","entrusting-my-times","times-in-your-hand",IB,
     "v14-15: 'But I TRUST in you, O LORD... My TIMES are in your HAND' - the operation is the turn from dread to trust: the interior hands over not just its spirit but the timing of its whole life.")
r.ch(276748,"goodness stored for those who fear you","affect","those who fear him","the self marvels at the abundant goodness God has stored up for those who fear him and take refuge in him - reverent trust and its treasured reward","reverent-refuge","goodness-stored",IB,
     "v19: 'how abundant is your GOODNESS, which you have stored up for those who FEAR you and worked for those who TAKE REFUGE in you' - the operation names the interior posture (fear + refuge) that God secretly rewards with hoarded good.")
r.ch(276777,"blessed be the LORD for his wondrous love","affect","the psalmist","the self blesses the LORD for wondrously showing his steadfast love in a besieged city - praise for a marvel of love","grateful-blessing","bless-wondrous-love",IB,
     "v21: 'BLESSED be the LORD, for he has WONDROUSLY shown his steadfast love to me' - the operation is blessing that names the deliverance a wonder; the interior marvels and praises.")
r.ch(276785,"in alarm I said 'I am cut off'","state","the psalmist","the self recalls that in its alarm it thought it was cut off from God's sight - yet God heard when it cried - panic corrected by being heard","panic-corrected","cut-off-yet-heard",IB,
     "v22: 'I had said in my ALARM, I am CUT OFF from your sight. But you HEARD the voice of my pleas' - the operation is the confession of a panic: the interior had despaired of God's attention, and was proved wrong.")
r.ch(276798,"love the LORD, all his saints","volition","the saints","the self calls all God's saints to love the LORD, who preserves the faithful but repays the proud - drawing the community into love and confidence","summoning-love","love-the-LORD",IB,
     "v23: 'LOVE the LORD, all you his SAINTS! The LORD preserves the faithful' - the operation turns the personal deliverance into a summons: the interior invites the whole community to love God.")
r.ch(276809,"be strong, take courage, you who wait","volition","those who wait","the self exhorts all who wait for the LORD to be strong and let their heart take courage - self-and-communal command to steadfast hope","exhortation","strong-in-waiting",IB,
     "v24: 'Be STRONG, and let your HEART take COURAGE, all you who WAIT for the LORD!' - the operation closes the psalm by commanding the waiting interior to summon strength; hope braced with courage.")

for sid,sense,src,d in [
 (276665,"in your righteousness deliver me",276660,"v1: 'in your righteousness DELIVER me' - the rescue the refuge-taking asks for."),
 (276832,"you have redeemed me",276830,"v5: 'you have REDEEMED me, O LORD, faithful God' - the ransom that grounds the committing of the spirit."),
 (276716,"rescue me from persecutors",276708,"v15: 'RESCUE me from the hand of my enemies and from my persecutors' - the deliverance the times-in-hand trust asks for."),
 (276803,"the LORD preserves the faithful",276798,"v23: 'The LORD PRESERVES the faithful' - the keeping that grounds the call to love him."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (net/rock/fortress imagery, God's-hiding/storing acts, lying-lips-of-foes, or label); standalone.")
r.write()
