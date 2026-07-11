#!/usr/bin/env python
"""Ps 34 (acrostic, taste and see; 84 spans). IB ops: continual blessing; the
soul boasting in God; summoning others to magnify him; seeking God and being
freed from fears; those who look to him radiant/unashamed; the poor man's cry
heard; tasting that God is good (experiential trust); fearing God (no lack);
seeking God and lacking no good; teaching the fear of the LORD; the desire for
life and good; guarding the tongue from evil; turning from evil to pursue peace;
the brokenhearted/crushed-spirit near to God; taking refuge, not condemned."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=34
r = Reading("Psa", 19, CH, note="Taste-and-see: bless, soul-boast, magnify, sought/freed-of-fears, radiant, poor's cry, taste, fear/no-lack, seek, teach-the-fear, desire-life, guard-tongue, seek-peace, brokenhearted, refuge")

r.ch(277128,"bless the LORD at all times","affect","the psalmist","the self resolves to bless the LORD at all times, his praise continually in the mouth - unbroken praise","continual-praise","bless-at-all-times",IB,
     "v1: 'I will BLESS the LORD at all times; his PRAISE shall continually be in my mouth' - the operation is praise made ceaseless, a standing posture of the interior.")
r.ch(277213,"my soul boasts in the LORD","affect","the psalmist","the self's soul makes its boast in the LORD, that the humble may hear and be glad - glorying redirected to God","God-ward-boast","soul-boasts",IB,
     "v2: 'My SOUL makes its BOAST in the LORD; let the HUMBLE hear and be GLAD' - the operation is boasting turned from self to God; the interior's pride is relocated onto him.")
r.ch(277239,"magnify the LORD with me","volition","the psalmist","the self calls others to magnify the LORD and exalt his name together - praise made communal","summoning-praise","magnify-together",IB,
     "v3: 'Oh, MAGNIFY the LORD with me, and let us EXALT his name together' - the operation reaches out: the interior wants company in enlarging God.")
r.ch(277244,"I sought the LORD, freed from fears","affect","the psalmist","the self sought the LORD, who answered and delivered it from all its fears - seeking that dissolves dread","fear-dissolving-seeking","sought-and-freed",IB,
     "v4: 'I SOUGHT the LORD, and he answered me and delivered me from all my FEARS' - the operation is the turning-to-God that empties the interior of its fears.")
r.ch(277254,"those who look to him are radiant","affect","those who look to him","those who look to God are radiant, their faces never ashamed - the interior lit up by looking to him","radiance","look-and-be-radiant",IB,
     "v5: 'Those who LOOK to him are RADIANT, and their faces shall never be ashamed' - the operation is transformation by gaze: the interior that turns to God is lit and kept from shame.")
r.ch(277260,"this poor man cried and was heard","affect","the poor man","this poor man cried, and the LORD heard and saved him from all his troubles - the cry of the lowly answered","crying-answered","poor-man-cried",IB,
     "v6: 'This poor man CRIED, and the LORD HEARD him and SAVED him out of all his troubles' - the operation is the lowly cry that reaches God; poverty of estate is no barrier to being heard.")
r.ch(277275,"taste and see that the LORD is good","affect","the worshipper","the self invites others to taste and see that the LORD is good - trust made experiential, savoured","experiential-trust","taste-and-see",IB,
     "v8: 'Oh, TASTE and see that the LORD is GOOD! Blessed is the man who takes refuge in him!' - the operation is a summons to first-hand experience; the interior is to sample God's goodness, not just hear of it.")
r.ch(277284,"fear the LORD, you his saints","affect","the saints","the self calls the saints to fear the LORD, for those who fear him have no lack - reverent fear that wants nothing","reverent-fear","fear-no-lack",IB,
     "v9: 'Oh, FEAR the LORD, you his saints, for those who fear him have no LACK!' - the operation commends reverence as the interior posture that is fully supplied.")
r.ch(277140,"those who seek the LORD lack no good","affect","those who seek","the young lions hunger, but those who seek the LORD lack no good thing - seeking that is satisfied","satisfied-seeking","seek-no-good-lacking",IB,
     "v10: 'those who SEEK the LORD lack no GOOD thing' - distinct from v4's seeking-freed-from-fear: this seeking is answered with provision; the interior that seeks God wants for nothing good.")
r.ch(277148,"I will teach you the fear of the LORD","volition","the teacher","the self calls children to listen and be taught the fear of the LORD - passing on reverence","teaching-reverence","teach-the-fear",IB,
     "v11: 'Come, O children, listen to me; I will TEACH you the FEAR of the LORD' - the operation turns instructor: the interior wants to hand its reverence to others.")
r.ch(277154,"who desires life and to see good","volition","the seeker of life","the self names the one who desires life and loves many days to see good - the longing the psalm will answer","desire-for-life","desire-life-good",IB,
     "v12: 'What man is there who DESIRES life and LOVES many days, that he may see GOOD?' - the operation surfaces a universal want - a good, long life - and prepares to redirect it toward the fear of God.")
r.ch(277160,"keep your tongue from evil","volition","the hearer","the self teaches: keep the tongue from evil and the lips from deceit - the guarded mouth as the path to life","tongue-guarding","keep-tongue",IB,
     "v13: 'KEEP your tongue from EVIL and your lips from speaking DECEIT' - the operation is the governed tongue; the interior that wants good life must first police its speech.")
r.ch(277173,"seek peace and pursue it","volition","the hearer","the self teaches: turn from evil, do good, seek peace and pursue it - an active chase after peace","peace-pursuit","seek-and-pursue-peace",IB,
     "v14: 'Turn away from evil and do good; SEEK PEACE and PURSUE it' - the operation makes peace a quarry: the interior does not merely wish peace but hunts it.")
r.ch(277202,"the LORD near the brokenhearted","state","the brokenhearted","the LORD is near to the brokenhearted and saves the crushed in spirit - the shattered interior is where God draws closest","brokenness","brokenhearted-near",IB,
     "v18: 'The LORD is NEAR to the BROKENHEARTED and saves the CRUSHED in SPIRIT' - the operation names the crushed interior not as abandoned but as the very place of God's nearness.")
r.ch(277236,"none who take refuge are condemned","affect","those who take refuge","the LORD redeems the life of his servants; none who take refuge in him will be condemned - shelter that guarantees acquittal","refuge-taking","refuge-not-condemned",IB,
     "v22: 'The LORD REDEEMS the life of his servants; none of those who TAKE REFUGE in him will be condemned' - the operation closes the acrostic on refuge: the interior that shelters in God is safe from condemnation.")

for sid,sense,src,d in [
 (277246,"he answered me",277244,"v4: 'and he ANSWERED me' - the response the seeking received."),
 (277262,"the LORD heard him",277260,"v6: 'and the LORD HEARD him' - the divine hearing that answered the poor man's cry."),
 (277203,"saves the crushed in spirit",277202,"v18: 'and SAVES the crushed in spirit' - the rescue God brings to the broken interior."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (angel-encamps/lions/bones imagery, wicked's-fate, or God's-deliverance label); standalone.")
r.write()
