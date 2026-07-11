#!/usr/bin/env python
"""Ps 16 (refuge, portion, the path of life) - a dense psalm of contented trust.
IB ops: refuge-taking; the confession that there is no good apart from God;
delight in the saints; the refusal of idolatry; God as the chosen portion;
contentment with a pleasant lot; blessing God for inner counsel; the heart
instructed in the night; setting the LORD ever before oneself; the whole self
glad and secure; the soul confident it will not be abandoned to death; the
anticipated fullness of joy in God's presence."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=16
r = Reading("Psa", 19, CH, note="Contented trust: refuge, no-good-apart, delight in saints, refuse idols, God as portion, pleasant lot, night-counsel, set-the-LORD, glad+secure self, soul not-abandoned, fullness of joy")

r.ch(274668,"take refuge in God","affect","the psalmist","the self takes refuge in God as the ground of its preservation - shelter as the opening posture","refuge-taking","take-refuge",IB,
     "v1: 'Preserve me, O God, for in you I TAKE REFUGE' - the whole psalm's contentment is spoken from inside this refuge; trust is the starting point, not a conclusion.")
r.ch(274694,"no good apart from you","cognition","the psalmist","the self confesses it has no good apart from the Lord - all its welfare located in God alone","total-dependence","no-good-apart",IB,
     "v2: 'I say to the LORD, You are my Lord; I have no GOOD apart from you' - the operation is a radical relocation of the good: nothing outside God counts as the self's benefit.")
r.ch(274707,"delight in the saints","affect","the psalmist","the saints in the land are the excellent ones in whom is all the self's delight - joy taken in godly company","holy-fellowship","delight-in-saints",IB,
     "v3: 'the SAINTS in the land, they are the excellent ones, in whom is all my DELIGHT' - the interior's pleasure is fixed on the godly; its company of joy is chosen by holiness.")
r.ch(274716,"refuse the idolaters' offerings","volition","the psalmist","the self will not pour out their blood drink-offerings or take other gods' names on its lips - a deliberate turning from idolatry","refusal-of-idols","refuse-idolatry",IB,
     "v4: 'their drink offerings of blood I will not POUR OUT or take their NAMES on my lips' - the operation is a clean break: the interior refuses even to name the rival gods.")
r.ch(274724,"the LORD my chosen portion","affect","the psalmist","the LORD is the self's chosen portion and cup, the one who holds its lot - God received as inheritance","God-as-inheritance","chosen-portion",IB,
     "v5: 'The LORD is my CHOSEN PORTION and my cup; you hold my lot' - the operation takes God himself, not any gift, as the inheritance; the giver is the portion.")
r.ch(274730,"a pleasant lot gladly owned","affect","the psalmist","the boundary lines have fallen in pleasant places; the self owns its inheritance as beautiful - contentment with what it has been given","contentment","pleasant-lines",IB,
     "v6: 'The LINES have fallen for me in PLEASANT places; indeed, I have a beautiful inheritance' - distinct from taking God as portion: this is glad acceptance of the actual circumstances of one's life.")
r.ch(274737,"bless God for his counsel","affect","the psalmist","the self blesses the LORD who gives it counsel - gratitude for divine guidance","grateful-blessing","bless-for-counsel",IB,
     "v7: 'I BLESS the LORD who gives me COUNSEL' - the interior returns thanks specifically for being guided; blessing as the response to God's advising.")
r.ch(274743,"the heart instructs in the night","cognition","the psalmist","in the night the self's heart/kidneys instruct it - an inner, nocturnal tutoring","night-instruction","heart-instructs",IB,
     "v7: 'in the night also my HEART INSTRUCTS me' - distinct from God's counsel: the interior itself, in the dark hours, becomes a teacher, working over what it has received.")
r.ch(274745,"set the LORD always before me","volition","the psalmist","the self keeps the LORD continually before it, so that with him at its right hand it will not be shaken - a sustained practice of attention","God-before-me","set-the-LORD",IB,
     "v8: 'I have SET the LORD always before me; because he is at my right hand, I shall not be shaken' - the operation is a chosen, continual orientation; the steadiness follows from the practice.")
r.ch(274755,"heart glad, whole being rejoices","affect","the psalmist","therefore the heart is glad, the whole being rejoices, the flesh dwells secure - the total self at rest","total-gladness","glad-and-secure",IB,
     "v9: 'Therefore my HEART is GLAD, and my whole being REJOICES; my flesh also dwells SECURE' - the operation sweeps the entire person - heart, glory, flesh - into one settled gladness.")
r.ch(274672,"the soul not abandoned to Sheol","affect","the psalmist","the self is confident God will not abandon its soul to Sheol nor let his holy one see corruption - trust reaching past death","death-defying-trust","soul-not-abandoned",IB,
     "v10: 'For you will not ABANDON my SOUL to Sheol, or let your holy one see corruption' - the interior's confidence extends beyond the grave; trust that death is not the end of the relation.")
r.ch(274684,"fullness of joy in your presence","affect","the psalmist","in God's presence is fullness of joy, at his right hand pleasures forevermore - the anticipated end of the path of life","anticipated-joy","fullness-of-joy",IB,
     "v11: 'You make known to me the path of life; in your PRESENCE there is FULLNESS of joy' - the operation reaches to the destination: the interior looks to a joy made complete in God's own presence.")

for sid,sense,src,d in [
 (274664,"Preserve me",274668,"v1: 'PRESERVE me, O God' - the keeping the refuge-taking asks for."),
 (274728,"you hold my lot",274724,"v5: 'you HOLD my lot' - God's securing of the inheritance that is himself."),
 (274671,"you will not abandon",274672,"v10: 'you will not ABANDON my soul to Sheol' - God's act grounding the death-defying trust."),
 (274679,"you make known the path of life",274684,"v11: 'you make KNOWN to me the path of life' - God's guidance toward the fullness of joy."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (cup/lot/lines/pleasures imagery or label); standalone.")
r.write()
