#!/usr/bin/env python
"""Ps 22 (the psalm of dereliction, 96 spans). IB ops: the cry of forsakenness;
the unanswered cry; the fathers' remembered trust (trusted->delivered; cried->
not-shamed); the worm-like self-abasement; trust instilled from birth; the
helplessness of having none to help; the melted heart; strength dried to death;
then the turn - the vow to proclaim God's name; summoning the God-fearers to
praise; performing vows; the afflicted satisfied and seekers praising; the
nations remembering and worshipping; posterity serving. The bulls/lions/dogs +
pierced/garments = standalone; deliver/save = qualifier."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=22
r = Reading("Psa", 19, CH, note="Dereliction->vindication->universal praise: forsakenness, unanswered cry, ancestral trust, worm-abasement, birth-trust, melted heart, dried strength; then vow/praise/seek/remember/serve")

r.ch(275573,"why have you forsaken me","affect","the psalmist","the self cries out that God has forsaken it and is far from saving, far from the words of its groaning - the extremity of felt abandonment","forsakenness","why-forsaken",IB,
     "v1: 'My God, my God, why have you FORSAKEN me? Why are you so far from saving me, from the words of my GROANING?' - the operation is the interior's rawest desolation: not doubt that God exists but the agony of his felt absence.")
r.ch(275654,"cry by day, no answer","affect","the psalmist","the self cries by day and by night and finds no answer, no rest - persistence into silence","unanswered-crying","cry-no-answer",IB,
     "v2: 'O my God, I CRY by day, but you do not answer, and by night, but I find no rest' - distinct from v1: this is the wearing continuation, the cry that keeps going into an unbroken silence.")
r.ch(275769,"the fathers trusted and were delivered","affect","the fathers","in God the fathers trusted, and trusting, they were delivered - the remembered pattern the self clings to","remembered-trust","fathers-trusted",IB,
     "v4: 'In you our fathers TRUSTED; they trusted, and you DELIVERED them' - the interior reaches back to ancestral trust as evidence against the present silence.")
r.ch(275774,"the fathers cried and were not shamed","affect","the fathers","to God the fathers cried and were rescued; they trusted and were not put to shame - a second layer of the ancestral ground","remembered-rescue","fathers-not-shamed",IB,
     "v5: 'To you they CRIED and were rescued; in you they trusted and were NOT PUT TO SHAME' - distinct from v4: here the accent is on the cry answered and shame averted, the very things the psalmist now lacks.")
r.ch(275781,"I am a worm, not a man","state","the psalmist","the self reckons itself a worm and not a man, scorned and despised by all - self-estimate crushed below humanity","self-abasement","worm-not-man",IB,
     "v6: 'But I am a WORM and not a man, SCORNED by mankind and DESPISED by the people' - the operation is a collapse of self-worth: mockery has driven the interior below the human.")
r.ch(275799,"you made me trust from the breast","affect","the psalmist","God took the self from the womb and made it trust him at its mother's breasts - trust as lifelong, pre-conscious","lifelong-trust","trust-from-birth",IB,
     "v9: 'you made me TRUST you at my mother's breasts' - the operation grounds the plea in a trust older than memory; the interior has leaned on God since infancy.")
r.ch(275597,"none to help","state","the psalmist","the self pleads that God not be far, for trouble is near and there is none to help - utter isolation","helplessness","none-to-help",IB,
     "v11: 'Be not far from me, for trouble is near and there is NONE to HELP' - the operation names the aloneness: every human support has failed, leaving only God to appeal to.")
r.ch(275610,"my heart melted like wax","state","the psalmist","the heart is like wax, melted within the breast - courage and resolve dissolving under terror","dissolution","heart-melted",IB,
     "v14: 'my HEART is like wax; it is MELTED within my breast' - the operation is the loss of all inner firmness; the seat of courage has run to liquid.")
r.ch(275617,"strength dried to death","state","the psalmist","strength is dried up like a potsherd, the tongue stuck to the jaws, laid in the dust of death - the self desiccated to its end","desiccation","dried-to-death",IB,
     "v15: 'my STRENGTH is DRIED UP like a potsherd... you lay me in the dust of DEATH' - the operation is total depletion; the interior and body alike are parched to the edge of the grave.")
r.ch(275671,"I will tell your name to my brothers","volition","the psalmist","the turn: the self vows to tell God's name to its brothers and praise him in the congregation - dereliction giving way to proclamation","turn-to-proclaim","tell-your-name",IB,
     "v22: 'I will TELL of your name to my brothers; in the midst of the congregation I will PRAISE you' - the hinge of the psalm: the forsaken cry becomes a vow to publish God's name.")
r.ch(275679,"summon the God-fearers to praise","volition","those who fear the LORD","the self calls all who fear the LORD to praise, glorify and stand in awe of him - drawing others into the vindication-praise","summoning-praise","fearers-praise",IB,
     "v23: 'You who FEAR the LORD, PRAISE him! All you offspring of Jacob, GLORIFY him!' - the operation widens the praise: the interior, rescued, recruits the whole God-fearing community.")
r.ch(275708,"perform my vows before the fearers","volition","the psalmist","the self's praise comes from God and it will perform its vows before those who fear him - gratitude discharged publicly","vow-keeping","perform-vows",IB,
     "v25: 'From you comes my PRAISE... my VOWS I will PERFORM before those who fear him' - the operation pays what was pledged in distress, the interior discharging its debt of thanks in the assembly.")
r.ch(275715,"the seekers shall praise and live","affect","those who seek him","the afflicted shall eat and be satisfied; those who seek God shall praise him and their hearts live forever - seeking rewarded with life","seeking","seek-and-live",IB,
     "v26: 'those who SEEK him shall PRAISE the LORD! May your HEARTS LIVE forever!' - the operation promises the seeking interior satisfaction and unending life; the afflicted's hunger is met.")
r.ch(275724,"the nations remember and worship","affect","the nations","all the ends of the earth shall remember and turn to the LORD, all families of the nations worship - the vindication spreading to the peoples","universal-turning","nations-remember",IB,
     "v27: 'All the ends of the earth shall REMEMBER and turn to the LORD; all the families of the nations shall WORSHIP' - the operation universalises the psalm: the one man's rescue draws the nations' interior back to God.")
r.ch(275757,"posterity shall serve and proclaim","volition","posterity","posterity shall serve God; it shall be told of the Lord to a coming generation, who proclaim his righteousness - the praise carried forward in time","generational-service","posterity-serves",IB,
     "v30-31: 'Posterity shall SERVE him... they shall PROCLAIM his righteousness to a people yet unborn' - the operation extends the vindication into the future: unborn generations will serve and tell.")

for sid,sense,src,d in [
 (275662,"Deliver my soul",275597,"v20: 'DELIVER my soul from the sword' - the rescue the helpless plea asks for."),
 (306168,"Save me from the lion's mouth",275597,"v21: 'SAVE me from the mouth of the lion' - the deliverance sought amid the predators."),
 (275702,"he has heard the afflicted",275708,"v24: 'he has not despised... but has HEARD, when he cried to him' - God's regard that vindicates and grounds the vows."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (bulls/lions/dogs encircling, poured-out/bones/pierced/garments affliction imagery, mockers' taunt, or label); standalone.")
r.write()
