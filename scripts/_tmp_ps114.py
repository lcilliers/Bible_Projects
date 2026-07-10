import sys; sys.path.insert(0,'scripts')
from _reread_ledger_lib import Reading, IB, GOD, PER
r=Reading("Psa",19,114,
  note="Ps114 Exodus-theophany poem (8v). A PURE theophany-narrative: the actors are the personified SEA (looked and fled), JORDAN (turned back), the MOUNTAINS (skipped like rams), the EARTH (tremble), and God (turns the rock into a pool). Screen 0 finds NO human inner-being lexicalized - the going-out, Judah-became-his-sanctuary, and tremble-O-earth are narrative/cosmic, not human dispositions. Like Ps 93 (pure kingship hymn), it resolves to all STANDALONE (0 char, 0 qual): pure God/cosmic content with no human characteristic for a qualifier to attach to.")
for sid,sense,d in [
 (270787,"went out (yatsa)","v1: 'When Israel WENT OUT (yatsa) from Egypt' - the Exodus event, the narrative setting. Standalone."),
 (270794,"strange language (laaz)","v1: 'from a people of STRANGE LANGUAGE (laaz)' - the alien-tongued Egyptians, image. Standalone."),
 (270796,"sanctuary (qodesh)","v2: 'Judah became his SANCTUARY (qodesh)' - Judah as God's holy dwelling, covenant-status descriptor. Standalone."),
 (270799,"dominion (memshalah)","v2: 'Israel his DOMINION (memshalah)' - Israel as God's realm, covenant-status descriptor. Standalone."),
 (307585,"looked (raah)","v3: 'The sea LOOKED (raah) and fled' - the personified sea beholding God, cosmic reaction. Standalone."),
 (307586,"fled (nus)","v3: 'The sea looked and FLED (nus)' - the sea recoiling at the Exodus, cosmic image. Standalone."),
 (307588,"turned back (sabab)","v3: 'Jordan TURNED BACK (sabab)' - the river reversing at the crossing, cosmic image. Standalone."),
 (270801,"skipped (raqad)","v4: 'The mountains SKIPPED (raqad) like rams' - the mountains leaping at God's presence, cosmic image. Standalone."),
 (270802,"rams (ayil)","v4: 'skipped like RAMS (ayil)' - the leaping rams, image of the quaking mountains. Standalone."),
 (307593,"flee (nus)","v5: 'What ails you, O sea, that you FLEE (nus)?' - the sea's flight questioned, cosmic image. Standalone."),
 (307595,"turn back (sabab)","v5: 'O Jordan, that you TURN BACK (sabab)?' - the river's reversal questioned, cosmic image. Standalone."),
 (270806,"skip (raqad)","v6: 'O mountains, that you SKIP (raqad) like rams?' - the mountains' leaping questioned, cosmic image. Standalone."),
 (270807,"rams (ayil)","v6: 'that you skip like RAMS (ayil)?' - the leaping rams, image. Standalone."),
 (307597,"tremble (chul)","v7: 'TREMBLE (chul), O earth, at the presence of the Lord' - the earth called to quake before God, cosmic address (not human IB). Standalone."),
 (270810,"turns (haphak)","v8: 'who TURNS (haphak) the rock into a pool of water' - God's miracle of water from the rock, theophany act. Standalone."),
 (270811,"rock (tsur)","v8: 'turns the ROCK (tsur) into a pool of water' - the water-giving rock, image. Standalone."),
 (270812,"pool (agam)","v8: 'into a POOL (agam) of water' - the pool from the rock, image of provision. Standalone."),
 (270813,"water (mayim)","v8: 'a pool of WATER (mayim)' - the water given, image. Standalone."),
 (270814,"flint (challamish)","v8: 'the FLINT (challamish) into a spring of water' - the hard flint made to flow, image. Standalone."),
 (270815,"spring (mayan)","v8: 'into a SPRING (mayan) of water' - the spring from the flint, image. Standalone."),
 (270816,"water (mayim)","v8: 'a spring of WATER (mayim)' - the water given, image of God's provision. Standalone."),
]: r.st(sid,sense,d)
r.write()
