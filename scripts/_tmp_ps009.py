#!/usr/bin/env python
"""Ps 9 (thanksgiving for judgment; the LORD a stronghold for the oppressed).
IB ops: wholehearted thanksgiving; glad exultation in the Most High; trust that
flows from knowing the name; seeking God; proclaiming his deeds; the afflicted's
cry; my own affliction pleaded; rejoicing in salvation; the poor's enduring hope.
God's judging/avenging/remembering = qualifier; the judgment-scene + net imagery
= standalone."""
import sys, os, sqlite3
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _reread_ledger_lib import Reading, IB, GOD, PER
CH=9
r = Reading("Psa", 19, CH, note="Thanksgiving + the oppressed's refuge: thanks/exult/trust/seek/proclaim + cry/affliction/hope")

r.ch(285865,"give thanks with whole heart","affect","the psalmist","the self resolves to thank the LORD with its whole heart, recounting all his wonders - undivided gratitude","wholehearted-thanks","thank-whole-heart",IB,
     "v1: 'I will GIVE THANKS to the LORD with my whole HEART; I will recount all of your wonderful deeds' - the interior gives itself entire to gratitude, nothing held back.")
r.ch(285954,"glad and exult in the Most High","affect","the psalmist","the self is glad and exults, singing praise to the name of the Most High - joy lifted to its highest object","exultation","glad-and-exult",IB,
     "v2: 'I will be GLAD and EXULT in you; I will sing praise to your name, O Most High' - distinct from the thanks-recital: this is upward-leaping joy fixed on the Most High.")
r.ch(285875,"trust flows from knowing the name","affect","those who know the name","those who know God's name put their trust in him, for he has not forsaken those who seek him - knowledge grounding reliance","knowledge-grounded-trust","know-name-trust",IB,
     "v10: 'those who KNOW your name put their TRUST in you, for you have not forsaken those who seek you' - the operation ties trust to acquaintance: to know who God is, is to rely on him.")
r.ch(285879,"seek the LORD","volition","those who seek","the self and its kind seek God, and are not forsaken - the sustained turning toward him","seeking","seek-the-LORD",IB,
     "v10: 'you have not forsaken those who SEEK you' - the interior orientation of seeking is named as the condition God honours; a directed reaching after him.")
r.ch(285880,"proclaim his deeds among peoples","volition","the psalmist","the self summons others to sing and tells among the peoples what God has done - praise turned outward and public","proclamation","tell-the-deeds",IB,
     "v11: 'SING praises to the LORD... tell among the peoples his DEEDS' - the interior gratitude will not stay private; it broadcasts God's acts to the nations.")
r.ch(285892,"the cry of the afflicted","affect","the afflicted","the afflicted cry out, and God does not forget their cry - the voiced pain of the crushed remembered","crying-out","afflicted-cry",IB,
     "v12: 'he does not forget the CRY of the AFFLICTED' - the interior of the crushed is a cry that reaches and is retained by God, over against those who forget them.")
r.ch(285897,"see my affliction","state","the psalmist","the self pleads its own affliction from those who hate it, asking to be lifted from the gates of death","personal-suffering","my-affliction",IB,
     "v13: 'see my AFFLICTION from those who hate me, O you who lift me up from the gates of death' - distinct from the general afflicted: the self brings its particular suffering, poised between death's gates and rescue.")
r.ch(285908,"rejoice in your salvation","affect","the psalmist","at the gates of Zion the self recounts God's praises and rejoices in his salvation - joy located in being saved","salvation-joy","rejoice-in-salvation",IB,
     "v14: 'that I may recount all your praises... and REJOICE in your SALVATION' - the interior's joy is grounded specifically in deliverance, praise voiced at the daughter of Zion's gates.")
r.ch(285943,"the poor's hope shall not perish","affect","the poor / needy","the needy shall not always be forgotten, nor the hope of the poor perish forever - hope that outlasts neglect","enduring-hope","hope-not-perish",IB,
     "v18: 'the needy shall not always be forgotten, and the HOPE of the POOR shall not perish forever' - the interior of the poor holds a hope the psalm insists is durable, not finally disappointed.")

for sid,sense,src,d in [
 (285889,"mindful of blood",285892,"v12: 'he who avenges blood is MINDFUL of them' - God's remembering that answers the afflicted's cry."),
 (285894,"be gracious",285897,"v13: 'Be GRACIOUS to me, O LORD' - the mercy the personal affliction begs."),
 (285899,"lift from death's gates",285897,"v13: 'you who LIFT me up from the gates of death' - the rescuing act poised against the affliction."),
 (285873,"you have not forsaken",285879,"v10: 'you have not FORSAKEN those who seek you' - God's faithfulness that rewards seeking."),
 (286003,"a stronghold for the oppressed",285875,"v9: 'The LORD is a STRONGHOLD for the oppressed' - the refuge that grounds the trust."),
]:
    r.qu(sid,sense,src,d)

conn=sqlite3.connect('database/bible_research.db');conn.row_factory=sqlite3.Row
cand={str(x['id']):x['reference'].split(':')[1] for x in conn.execute(f"SELECT id,reference FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%' AND (char_candidate=1 OR role IN ('characteristic','qualifier'))")}
sur={str(x['id']):x['surface'] for x in conn.execute(f"SELECT id,surface FROM verse_span_index WHERE reference LIKE 'Psa {CH}:%'")}
for sid,v in cand.items():
    if sid not in r.spans:
        s=sur.get(sid,'span')
        r.st(sid, s or 'span', f"v{v}: '{s}' - substrate (judgment-scene: rebuked/perished/net/pit, or God's-justice label); standalone.")
r.write()
