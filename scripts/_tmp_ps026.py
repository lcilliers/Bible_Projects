#!/usr/bin/env python
"""Ps 26 (integrity vindication) - a portrait of the upright interior. IB ops:
the appeal from a life walked in integrity; unwavering trust; inviting God to
test heart and mind; walking in God's faithfulness with his love before the eyes;
hating the company of evildoers; washing hands in innocence to approach the
altar; proclaiming thanks; loving God's house; the plea not to be swept away with
sinners; the forward resolve to keep walking in integrity; blessing God in the
assembly."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=26
r = Reading("Psa", 19, CH, note="Integrity portrait: walked-integrity, unwavering trust, invite-testing, walk-faithfulness, hate evildoers' company, wash-innocence, proclaim thanks, love the house, not-swept-with-sinners, resolve, bless")

r.ch(276111,"walked in my integrity","volition","the psalmist","the self appeals for vindication on the ground that it has walked in integrity - a whole life offered as evidence","integrity-of-life","walked-integrity",IB,
     "v1: 'Vindicate me, O LORD, for I have WALKED in my INTEGRITY' - the interior stakes its plea on a consistent, undivided manner of life.")
r.ch(276113,"trusted without wavering","affect","the psalmist","the self has trusted in the LORD without wavering/slipping - steady reliance as part of the integrity","unwavering-trust","trust-not-waver",IB,
     "v1: 'and I have TRUSTED in the LORD without WAVERING' - distinct from the walk: the interior's reliance has not slipped or sagged; a constancy of trust.")
r.ch(276139,"invite God to test the heart","volition","the psalmist","the self invites God to prove, try and test its heart and mind - a confidence willing to be assayed","confident-self-submission","test-my-heart",IB,
     "v2: 'PROVE me, O LORD, and try me; TEST my HEART and my mind' - the operation offers the inmost self for examination; only an integrity sure of itself asks to be tested.")
r.ch(276147,"walk in your faithfulness","volition","the psalmist","with God's steadfast love before its eyes, the self walks in his faithfulness - conduct shaped by keeping God in view","God-oriented-walk","walk-faithfulness",IB,
     "v3: 'For your steadfast love is before my eyes, and I WALK in your FAITHFULNESS' - the operation keeps God's love in constant sight and lets it govern the walk.")
r.ch(276157,"hate the assembly of evildoers","affect","the psalmist","the self will not sit with the false or hypocrites; it hates the assembly of evildoers and will not sit with the wicked - aversion to their company","separation","hate-their-company",IB,
     "v4-5: 'I do not sit with men of falsehood... I HATE the assembly of EVILDOERS and will not sit with the wicked' - the operation is a chosen distancing; the interior refuses the fellowship of the corrupt.")
r.ch(276164,"wash my hands in innocence","volition","the psalmist","the self washes its hands in innocence and goes around the altar - approaching worship with a cleansed conscience","ritual-purity","wash-in-innocence",IB,
     "v6: 'I WASH my hands in INNOCENCE and go around your altar, O LORD' - the operation is a deliberate purification before drawing near; clean conscience as the ticket to the altar.")
r.ch(276170,"proclaim thanksgiving aloud","volition","the psalmist","the self proclaims thanksgiving aloud and tells all God's wondrous deeds - gratitude published at the altar","proclamation","proclaim-thanks",IB,
     "v7: 'PROCLAIMING THANKSGIVING aloud, and telling all your wondrous deeds' - the operation turns worship vocal: the interior recounts God's works for others to hear.")
r.ch(276177,"love the house of the LORD","affect","the psalmist","the self loves the habitation of God's house, the place where his glory dwells - affection for God's dwelling","love-of-the-house","love-your-house",IB,
     "v8: 'O LORD, I LOVE the habitation of your house and the place where your GLORY dwells' - the operation is a warm attachment to the very place of God's presence.")
r.ch(276186,"do not sweep my soul with sinners","affect","the psalmist","the self pleads that God not sweep away its soul with sinners or its life with the bloodthirsty - a longing to be distinguished from the wicked at the reckoning","plea-for-distinction","not-swept-away",IB,
     "v9: 'Do not sweep my SOUL away with sinners, nor my life with bloodthirsty men' - the operation asks that the integrity of the interior be honoured when judgment falls on the wicked.")
r.ch(276124,"I shall walk in my integrity","volition","the psalmist","turning from plea to resolve, the self declares it will walk in its integrity, asking to be redeemed and shown grace - a forward commitment","forward-resolve","resolve-integrity",IB,
     "v11: 'But as for me, I shall WALK in my INTEGRITY; redeem me, and be gracious to me' - distinct from the past claim of v1: this is the future pledge, the interior committing to keep its course.")
r.ch(276134,"bless the LORD in the assembly","affect","the psalmist","standing on level ground, the self will bless the LORD in the great assembly - the integrity ending in public praise","doxology","bless-in-assembly",IB,
     "v12: 'My foot stands on level ground; in the great assembly I will BLESS the LORD' - the operation closes the psalm: the vindicated interior turns to blessing God among the congregation.")

for sid,sense,src,d in [
 (276107,"Vindicate me",276111,"v1: 'VINDICATE me, O LORD' - the judicial verdict the walked-integrity appeals for."),
 (276126,"redeem me",276124,"v11: 'REDEEM me, and be gracious to me' - the rescue the resolve-to-walk asks for."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (bribe/altar/glory imagery or wicked-label); standalone.")
r.write()
