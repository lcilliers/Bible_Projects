#!/usr/bin/env python
"""Ps 145 (David, acrostic praise). IB ops (human praise-operations, movement-
anchored to avoid flattened reuse): resolve to extol/bless forever; daily
blessing; generation-to-generation transmission; meditation on wondrous works;
declaring awesome deeds; exuberant pouring-forth of fame + singing; the saints'
thanks; telling the kingdom's glory; calling on God in truth; the fear-of-God
whose desire is fulfilled and cry heard; loving God; final resolve that all
flesh bless his holy name. God's attributes = qual; kingdom/glory/works imagery
= standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=145
r = Reading("Psa", 19, CH, note="Acrostic praise: the human praise-operations across the alphabet, movement-anchored")

r.ch(274030,"resolve to extol forever","affect","the psalmist","the self resolves to extol and bless God's name for ever and ever - praise as vow","praise-vow","extol-forever",IB,
     "v1: 'I will EXTOL you, my God and King, and BLESS your name forever' - the interior binds itself to unending praise, the acrostic's opening pledge.")
r.ch(274121,"daily blessing","affect","the psalmist","every single day the self will bless and praise - praise made a daily discipline","daily-praise","bless-every-day",IB,
     "v2: 'EVERY DAY I will BLESS you' - distinct from the forever-vow: praise distributed into the grain of ordinary time, a habit not just an oath.")
r.ch(274151,"generational transmission","volition","the psalmist","one generation commends God's works to the next - praise handed forward as inheritance","hand-forward","commend-to-next",IB,
     "v4: 'One generation shall COMMEND your works to another' - the operation reaches beyond the self: praise as a relay across time.")
r.ch(274161,"meditation on works","cognition","the psalmist","the self meditates on the glorious splendour and wondrous works of God","contemplation","meditate-on-splendour",IB,
     "v5: 'I will MEDITATE on your wondrous works' - the interior dwells, ponders, feeds attention on God's majesty.")
r.ch(274165,"declare awesome deeds","volition","the psalmist","the self declares God's mighty, awesome deeds - proclamation of his greatness","proclamation","declare-awesome",IB,
     "v6: 'they shall speak of the might of your AWESOME DEEDS, and I will DECLARE your greatness' - the interior overflows into public telling.")
r.ch(274167,"pour forth fame + sing","affect","the psalmist","the self pours forth the fame of God's abundant goodness and sings of his righteousness","exuberance","pour-and-sing",IB,
     "v7: 'they shall POUR FORTH the fame of your abundant goodness and SING of your righteousness' - the operation is exuberant overflow, memory of goodness spilling into song.")
r.ch(274041,"the saints give thanks","affect","the saints","all God's works give thanks and his saints bless him - the community's gratitude","corporate-thanks","saints-give-thanks",IB,
     "v10: 'all your works shall GIVE THANKS to you, and your SAINTS shall BLESS you' - the interior of the whole godly community turns grateful.")
r.ch(274049,"tell the kingdom's glory","volition","the saints","the saints speak of the glory of God's kingdom and tell of his power","kingdom-telling","tell-the-glory",IB,
     "v11: 'they shall speak of the GLORY of your kingdom and TELL of your power' - the interior makes known God's reign to the children of man.")
r.ch(274103,"call on God in truth","affect","those who call","the operation of calling on God sincerely, in truth - not mere formula but real appeal","sincere-appeal","call-in-truth",IB,
     "v18: 'the LORD is near to all who CALL on him, to all who call on him in TRUTH' - the interior condition that draws God near is truthful calling.")
r.ch(274113,"the fear that is heard","affect","those who fear","the reverent fear of God whose desire he fulfils and whose cry he hears and saves","reverent-dependence","fear-and-be-heard",IB,
     "v19: 'he fulfils the DESIRE of those who FEAR him; he also hears their cry and saves them' - the interior posture of fear is met with fulfilment and rescue.")
r.ch(274129,"love God","affect","those who love","the love of God that he preserves - the interior attachment God guards","love-attachment","love-and-be-kept",IB,
     "v20: 'the LORD preserves all who LOVE him' - the operation is the self's fastening onto God in love, answered by preservation.")
r.ch(274133,"all flesh bless his name","affect","the psalmist","the closing resolve: the self's mouth speaks praise, and all flesh will bless God's holy name forever","universal-praise","all-flesh-bless",IB,
     "v21: 'My MOUTH will speak the PRAISE of the LORD, and let all FLESH BLESS his holy name forever' - the acrostic closes by widening the self's praise to all creation.")

for sid,sense,src,d in [
 (274174,"gracious (chanun)",274167,"v8: 'The LORD is GRACIOUS and merciful' - the goodness the psalmist pours forth."),
 (274175,"merciful (rachum)",274167,"v8: 'MERCIFUL, slow to anger' - God's compassion praised."),
 (274179,"steadfast love (chesed)",274167,"v8: 'abounding in STEADFAST LOVE' - the covenant loyalty sung."),
 (274181,"good to all (tob)",274041,"v9: 'The LORD is GOOD to all' - the goodness the saints thank him for."),
 (274183,"mercy over all works",274041,"v9: 'his MERCY is over all that he has made' - the compassion evoking thanks."),
 (274067,"faithful in words",274049,"v13: 'The LORD is FAITHFUL in all his words' - the reliability told of the kingdom."),
 (274073,"kind in works",274049,"v13: 'KIND in all his works' - God's graciousness in the kingdom-telling."),
 (308157,"upholds the falling",274113,"v14: 'The LORD UPHOLDS all who are falling' - the support the God-fearer relies on."),
 (308160,"raises the bowed down",274113,"v14: 'RAISES up all who are bowed down' - God's lifting act."),
 (274088,"satisfies desire",274113,"v16: 'you SATISFY the DESIRE of every living thing' - the provision the fear waits on."),
 (274101,"near to all who call",274103,"v18: 'The LORD is NEAR to all who call on him' - the nearness truthful calling meets."),
 (274127,"preserves who love",274129,"v20: 'the LORD PRESERVES all who love him' - the keeping love is answered with."),
 (274115,"hears their cry",274113,"v19: 'he HEARS their cry and saves them' - God's response to the fearers."),
 (274111,"fulfils desire",274113,"v19: 'he FULFILS the desire of those who fear him' - the answered longing."),
 (274154,"declare mighty acts",274151,"v4: 'they shall DECLARE your mighty acts' - part of the generational commending."),
 (274052,"make known deeds",274049,"v12: 'to make KNOWN to the children of man his mighty deeds' - the aim of the telling."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (kingdom/glory/majesty/works imagery or attribute-label); standalone.")
r.write()
