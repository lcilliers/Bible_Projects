#!/usr/bin/env python
"""Ps 15 (who may dwell on the holy hill) - a near-total portrait of the
righteous INTERIOR/conduct. IB ops: the blameless walk; truth spoken in the
heart; the tongue that refuses to slander; valuation by God's standard (despise
vileness, honour the God-fearers); oath-keeping even to one's own hurt; financial
integrity (no usury, no bribe); the resulting unshakeable stability. Only the
holy hill = standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=15
r = Reading("Psa", 19, CH, note="Portrait of the righteous: blameless walk, inner truth, no slander, right valuation, costly oath-keeping, financial integrity, unshakeableness")

r.ch(274617,"walks blamelessly, does right","volition","the righteous","the one who may dwell walks with integrity and does what is right - a whole manner of life without crookedness","integrity-of-walk","walk-blameless",IB,
     "v2: 'He who WALKS blamelessly and DOES what is right' - the operation is a consistent uprightness of conduct; the life itself is the first qualification.")
r.ch(274621,"speaks truth in the heart","cognition","the righteous","he speaks truth in his heart - honesty that reaches the inmost self, not merely the words","inner-truthfulness","truth-in-heart",IB,
     "v2: 'and SPEAKS TRUTH in his HEART' - distinct from outward conduct: the interior itself is truthful; he does not lie even to himself.")
r.ch(274626,"refuses to slander","volition","the righteous","he does not slander with his tongue, does no evil to a neighbour, takes up no reproach against a friend - restrained speech that protects others","tongue-restraint","no-slander",IB,
     "v3: 'who does not SLANDER with his tongue and does no EVIL to his neighbour' - the operation is the governed tongue: the interior refuses to trade in others' reputations.")
r.ch(274642,"honours the God-fearers","affect","the righteous","in his eyes a vile person is despised but he honours those who fear the LORD - valuing people by God's standard","right-valuation","honour-God-fearers",IB,
     "v4: 'in whose eyes a VILE person is DESPISED, but who HONOURS those who fear the LORD' - the operation is a reordered esteem: the interior's approvals track God's, not status or power.")
r.ch(274645,"keeps a costly oath","volition","the righteous","he swears to his own hurt and does not change - integrity that holds even when keeping the word costs him","costly-fidelity","swear-to-own-hurt",IB,
     "v4: 'who SWEARS to his own HURT and does not change' - the operation is fidelity under cost: the interior will not renege on a promise merely because it turned out expensive.")
r.ch(274652,"no usury, no bribe","volition","the righteous","he does not lend money at interest or take a bribe against the innocent - integrity in money and justice","financial-integrity","no-usury-no-bribe",IB,
     "v5: 'who does not put out his money at INTEREST and does not take a BRIBE against the innocent' - the operation refuses to profit from the vulnerable or to sell a just verdict.")
r.ch(274661,"shall never be moved","state","the righteous","the one who does these things shall never be moved - the settled, unshakeable stability that integrity produces","unshakeableness","never-moved",IB,
     "v5: 'He who does these things shall never be MOVED' - the closing note: this whole interior/conduct yields a stability nothing can topple; character as bedrock.")

for sid,sense,src,d in [
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (the holy hill/tent venue or label); standalone.")
r.write()
