#!/usr/bin/env python
"""Ps 35 (contend against my adversaries; 129 spans - much imprecation/enemy
imagery = standalone). IB ops: the soul longing to hear 'I am your salvation';
the soul that will rejoice in his salvation; the bereft soul repaid evil for good;
the costly compassion once shown to enemies (sackcloth, fasting, prayer when they
were sick); mourning for them as for kin; thanksgiving in the great congregation;
those who delight in the psalmist's vindication; telling God's righteousness all
day. Contend/net/pit/lions/mockers/vindicate = qualifier/standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=35
r = Reading("Psa", 19, CH, note="Contend: soul longs to hear salvation, soul rejoices, bereft(evil-for-good), costly compassion-for-enemies, mourning-for-them, thanks-in-assembly, delight-in-vindication, tell-righteousness")

r.ch(277461,"say to my soul 'I am your salvation'","affect","the psalmist","the self asks God to say to its soul, 'I am your salvation' - a longing to hear the inner assurance spoken","longing-for-assurance","say-to-my-soul",IB,
     "v3: 'Say to my SOUL, I am your SALVATION!' - the operation is a craving not just for rescue but for the word of it: the interior wants God to address its soul directly.")
r.ch(277482,"my soul shall rejoice in his salvation","affect","the psalmist","the self's soul will rejoice in the LORD, exulting in his salvation - anticipated inner joy","anticipated-joy","soul-shall-rejoice",IB,
     "v9: 'Then my SOUL will REJOICE in the LORD, EXULTING in his salvation' - the operation leans forward into joy: the interior already tastes the gladness the rescue will bring.")
r.ch(277325,"my soul bereft, repaid evil for good","state","the psalmist","the enemies repay evil for good, leaving the self's soul bereaved - the desolation of betrayed kindness","bereavement","evil-for-good",IB,
     "v12: 'They REPAY me EVIL for GOOD; my SOUL is BEREFT' - the operation is the specific wound of ingratitude: the interior is emptied because its good was answered with harm.")
r.ch(277330,"I afflicted myself when they were sick","affect","the psalmist","when the enemies were sick, the self wore sackcloth, afflicted itself with fasting, and prayed with head bowed - costly compassion once shown to those who now repay evil","compassion-for-enemies","afflict-self-for-them",IB,
     "v13: 'But I, when they were sick - I wore sackcloth; I AFFLICTED myself with FASTING; I PRAYED with head bowed' - the operation is love spent on the very ones who now betray: the interior once grieved and interceded for its persecutors.")
r.ch(277341,"I mourned for them as for kin","affect","the psalmist","the self went about as though grieving for a friend or brother, bowed in mourning as for its mother - identifying with the enemies' suffering","kinship-grief","mourn-as-for-kin",IB,
     "v14: 'I went about as though I grieved for my friend or my brother; as one who LAMENTS his mother, I bowed down in MOURNING' - distinct from the fasting: this is the depth of felt grief, the interior mourning enemies as its closest family.")
r.ch(277364,"I will thank you in the great congregation","volition","the psalmist","the self vows to thank God in the great congregation, to praise him among the mighty throng - gratitude discharged publicly","public-thanks","thank-in-congregation",IB,
     "v18: 'I will THANK you in the great congregation; in the mighty throng I will PRAISE you' - the operation turns the anticipated rescue into a pledge of public thanksgiving.")
r.ch(277438,"those who delight in my vindication","affect","those who favour the right","the self asks that those who delight in its righteousness shout for joy and be glad, saying 'Great is the LORD' - the joy of those who love justice","shared-vindication-joy","delight-in-righteousness",IB,
     "v27: 'Let those who DELIGHT in my righteousness shout for JOY and be GLAD... Great is the LORD, who delights in the WELFARE of his servant' - the operation invokes a company whose interior is gladdened by the vindication of the right.")
r.ch(277451,"my tongue shall tell your righteousness all day","volition","the psalmist","the self's tongue will tell of God's righteousness and praise all the day long - unceasing testimony","unceasing-testimony","tell-all-day",IB,
     "v28: 'Then my TONGUE shall TELL of your righteousness and of your praise all the day long' - the operation closes the psalm in perpetual proclamation; the vindicated interior will not stop speaking God's justice.")

for sid,sense,src,d in [
 (277464,"you are my salvation",277461,"v3: 'Say to my soul, I am your SALVATION' - the assurance the soul longs to hear (God's own word)."),
 (277358,"rescue me from the lions",277482,"v17: 'RESCUE me from their destruction, my precious life from the lions' - the deliverance the soul's rejoicing anticipates."),
 (277411,"vindicate me",277438,"v24: 'VINDICATE me, O LORD my God, according to your righteousness' - the verdict that gladdens those who love the right."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (contend/shield/spear, net/pit/chaff/lions imagery, mockers, or vindicate-petition label); standalone.")
r.write()
