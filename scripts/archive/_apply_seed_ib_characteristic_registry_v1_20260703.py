"""Create + seed the inner-being CHARACTERISTIC control registry (ib_characteristic).

Fork (b) control mechanism (researcher, 2026-07-03): mark which characteristics have
SURFACED, add new ones. Designed for DISCOVERY, not summary - so it carries, per
characteristic, a working gist held OPEN, the COLOUR-RANGE (how it shifts meaning
across contexts), the JUNCTIONS (where its boundary blurs into other characteristics),
and OPEN QUESTIONS. Boundaries are expected to be unclear and to change colour
([[project_RESET_characteristics_to_movements_changeover]], [[project_inner_being_reading_questions_first]]).

Idempotent: upserts by code. Re-run to add/adjust. status: emerging|surfaced|established|thin.
"""
import sqlite3, os
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db')
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
PROV='ib-characteristic-registry-v1-20260703'

# code, name, aka/colour-range-names, family, status, books, gist(open), colour_range, junctions, open_questions
R=[
 ("fear-of-the-lord","The fear of the LORD","reverent awe · dread of anger · dread of man · hatred of evil · fearless confidence","godward","established","Psa,Pro",
  "The inner being's foundational Godward orientation; in Proverbs the explicit ROOT from which the wise faculties grow (Pro 1:7->31:30).",
  "CHANGES COLOUR sharply: (a) reverent awe / the beginning of wisdom (Ps 111:10, Pro 9:10); (b) dread of God's anger/discipline (Ps 6:1, 38); (c) the fear of MAN as a snare - a false fear dissolved by trust (Pro 29:25, Ps 56:11); (d) fear AS hatred of evil (Pro 8:13); (e) issues in fearLESSness/confidence (Pro 14:26, Ps 27:1); matures into DELIGHT (Pro 3, Ps 112:1).",
  "trust; hatred-of-evil; delight; fearlessness; the-root(formation); humility.",
  "Is 'fear' one operation across this range or several sharing a word? Where does reverent fear END and delight BEGIN? How does forgiveness GENERATE fear (Ps 130:4)?"),
 ("love-aheb","Love (aheb) and its objects","love of God/name · love of wisdom · misdirected love · love-as-covering · love of discipline · love of death","godward","established","Psa,Pro",
  "The affection/attachment operation; its object sets its valence (the love itself is always the characteristic). aheb-fix made it visible across the corpus.",
  "CHANGES COLOUR by OBJECT: love of God / his name (Ps 116:1, 5:11); love of wisdom, courted as a person (Pro 4:6, 7:4, 8:17); MISDIRECTED love - of vanity (Ps 4:2), simplicity (Pro 1:22), violence (Ps 11:5), evil (Ps 52); love-as-COVERING another's offense (Pro 10:12, 17:9); love of DISCIPLINE/knowledge (Pro 12:1); love of PURITY of heart (Pro 22:11); the extreme - 'all who hate me LOVE DEATH' (Pro 8:36).",
  "desire/appetite (love vs want?); teachability (love of discipline); relational-love/covering; the-object-forms-the-self (formation-law).",
  "Is love a distinct operation or the affective face of desire/trust? What is 'love-as-covering' (hiding another's fault) vs concealment (hiding one's own)? Can love be commanded (Ps 31:23, Pro)?"),
 ("the-heart","The heart / the inner self","seat · the true self · guarded · given · weighed · searched · hardened · divided · felt","reflexive","established","Psa,Pro",
  "The centre of the inner being - not a faculty the self HAS but, in Proverbs, the self it IS (27:19). Proverbs is intensely heart-centred.",
  "MANY COLOURS: the seat (heart/soul/spirit/flesh); the TRUE self ('the heart reflects the man', Pro 27:19); to be GUARDED, the source of life (Pro 4:23); to be GIVEN (Pro 23:26); WEIGHED/searched by God (Pro 16:2, 21:2, Ps 139); the HARDENED heart (Pro 28:14, Ps 95:8); the un-self-cleansable heart (Pro 20:9, Ps 51:10); the FELT heart (see felt-interior); the deep/opaque-yet-drawable heart (Pro 20:5, 25:3).",
  "being-known; self-mastery(ruling the heart); the-felt-interior; integrity; forgiveness(clean heart); the-seats(soul/spirit/flesh).",
  "Is 'heart' one thing or the whole interior named from its centre? How do heart/soul/spirit/flesh (the seats) differ in operation? When is the heart the ORGAN and when the SELF?"),
 ("trust-refuge","Trust / taking refuge","shelter · self-distrust · the formation-law · mis-placed trust · immovable stability","godward","established","Psa,Pro",
  "Leaning one's security on God - and being re-formed by what one leans on.",
  "COLOURS: refuge/shelter (Ps 2,5,7...); trust as SELF-DISTRUST ('lean not on your own understanding', Pro 3:5); the FORMATION-law 'you become what you trust' (Ps 115:8); MIS-placed - riches (Pro 11:28, Ps 52:7), princes (Ps 146:3), one's own mind (Pro 28:26); trust yielding IMMOVABLE stability (Ps 125:1, 112:7); trust as a deliberate VALUATION (Ps 118:8).",
  "fear-of-the-lord; the-formation-law; fearlessness; entrustment; self-reliance(its foil).",
  "Is refuge (sheltering) the same operation as trust (leaning/valuing)? Is the formation-law (become-what-you-trust) a property of trust or a law over ALL the operations?"),
 ("desire-appetite","Desire / longing / appetite","longing for God · thirst · insatiable eye · disordered craving · self-killing craving · satisfied · weaned","godward","established","Psa,Pro",
  "The inner being's wanting; its direction and satisfiability are the questions.",
  "WIDE COLOUR: longing/thirst for God met (Ps 42:1, 63:1, 107:9, 145:16); hope DEFERRED makes the heart sick / fulfilled a tree of life (Pro 13:12); the INSATIABLE eye (Pro 27:20); DISORDERED craving that tests God to ruin (Ps 106:14) or KILLS the sluggard (Pro 21:25); satisfied by God's open hand (Ps 145:16); WEANED past craving (Ps 131:2).",
  "love-aheb; hope/waiting; the-felt-interior(hope-sick heart); self-mastery(appetite-restraint); the-compulsive-will.",
  "Is desire good, neutral, or fallen by default? What is the relation of the INSATIABLE eye to the SATISFIED soul - is contentment fulfilment or renunciation (131)? Does deferral WOUND or REFINE?"),
 ("self-mastery","Self-mastery / ruling one's spirit","self-control · holding back the spirit · the walled self · slow-to-anger · appetite-restraint","reflexive","established","Psa,Pro",
  "The self governing the self; in Proverbs the SUPREME strength (16:32) and the wall that makes a self defensible (25:28).",
  "COLOURS: ruling one's SPIRIT (Pro 16:32); HOLDING BACK vs venting the spirit (Pro 29:11); self-control as the WALL of the self (Pro 25:28); slow-to-anger (Pro 14:29, 15:1); appetite-restraint (Pro 23:2); restraint of the TONGUE (Pro 13:3, 21:23, Ps 39:1); overlaps the Psalter's self-QUIETING (Ps 62, 131).",
  "self-address(the stilling register); the-felt-interior(anger/tranquil); speech(tongue-restraint); the-compulsive-will(its failure).",
  "Is self-mastery the ACT and self-address the MODE and stillness the STATE - three faces of one thing? Where is the SEAT of the governing 'I' vs the governed 'spirit'?"),
 ("being-known","Being known / searched / weighed / tested by God","known · searched · weighed · tested/refined · the invited search · the lamp within","reflexive","established","Psa,Pro",
  "The inner being's transparency to God - and, at its height, the INVITED search.",
  "COLOURS: exhaustively known (Ps 139:1-6); the INVITED search ('search me', Ps 139:23); the heart TESTED/refined as metal (Pro 17:3, Ps 66:10); WEIGHED (Pro 16:2, 21:2); the spirit as God's LAMP searching the innermost (Pro 20:27); God sees the hearts (Pro 15:11, Ps 33:15); the excuse SEEN THROUGH (Pro 24:12).",
  "the-heart(weighed/searched); integrity(assay); forgiveness(the un-cleansable heart exposed); self-examination.",
  "What turns being-known from THREAT to COMFORT (139)? Is 'testing' the same as 'searching' or a refining that CHANGES the self? Does the lamp-within (20:27) mean conscience IS God's searching?"),
 ("the-felt-interior","The felt interior / the heart's states","glad · crushed · heavy · tranquil · anxious · bitter · incommunicable · cheerful","experiential","established","Psa,Pro",
  "The inner being as a FELT thing - its states, their somatic register, their privacy. Proverbs maps this most finely.",
  "COLOURS/STATES: the incommunicable heart ('knows its own bitterness, no stranger shares its joy', Pro 14:10); glad/crushed - the crushed SPIRIT the limit of endurance (Pro 17:22, 18:14); the cheerful heart as a 'continual feast' (Pro 15:15); anxiety WEIGHS (Pro 12:25); tranquil heart = life to the flesh, envy rots the bones (Pro 14:30); the SOMATIC register (Ps 32:3, 6:6).",
  "grief; joy; rest; self-mastery(tranquil vs raging); the-heart.",
  "Is the felt interior a distinct 'characteristic' or the EXPERIENTIAL side of all of them? Why is it so much richer in Proverbs' terse couplets than expected? What of the MASK (laughter over ache, 14:13)?"),
 ("teachability","Teachability / receptivity","love of discipline · hearing · the seeking ear · the closed/hardened/unteachable heart · self-certainty","formation","established","Psa,Pro",
  "The heart's openness to correction and instruction - the diagnostic of the inner being (the reaction to reproof SORTS the heart).",
  "COLOURS: love of discipline/knowledge (Pro 12:1); hearing/inclining the ear (Pro 2, 4); the reproof that goes DEEP (Pro 17:10); the DIAGNOSTIC - scoffer hates / wise loves the reprover (Pro 9:8); its foils - self-CERTAINTY ('right in his own eyes', Pro 12:15), the HARDENED/stiff-necked heart (Pro 28:14, 29:1, Ps 95:8), self-CONCEIT (Pro 26:12).",
  "love-aheb(love of discipline); the-heart(hardened); self-examination; humility; being-known(inviting correction).",
  "Is teachability a virtue or the CONDITION of every other virtue's growth? Where is the line between healthy self-trust and self-certainty? Can the hardened heart soften, or is 29:1 final?"),
 ("humility","Humility / self-sizing / lowliness","creaturely smallness · intellectual self-emptying · refused over-reach · pride's foil · lowliness-before-honour","formation","established","Psa,Pro",
  "The self rightly measuring itself before God - and its foil, pride.",
  "COLOURS: creaturely smallness ('what is man… but a breath', Ps 8:4, 144:3); refused OVER-reach (Ps 131:1); INTELLECTUAL self-emptying (Pro 30:2-3 'too stupid to be a man'); lowliness BEFORE honour (Pro 15:33, 29:23); pride as self-DESTRUCTION (Pro 16:18); the prayer for the MIDDLE as self-knowledge (Pro 30:8-9).",
  "self-knowledge; the-fear-of-the-lord(root); teachability; being-known(self-blindness); pride(its foil).",
  "Is humility a feeling, a self-assessment, or an act (refusing over-reach)? Does it PRECEDE wisdom or FOLLOW it? Relation to the un-self-cleansable heart (20:9)?"),
 ("integrity-legibility","Integrity / the inner condition legible","truth in the inward · legible in speech · legible in gesture · the masking/concealing heart · clean hands","formation","established","Psa,Pro",
  "The self true all the way through - and the readability (or masking) of the interior.",
  "COLOURS: truth IN the inward being (Ps 51:6, 15:2); integrity in the PRIVATE sphere (Ps 101:2); legible in SPEECH (Ps 5:9, Pro 10-15) and in GESTURE (Pro 6:12-14); the MASKING/concealing heart - fair speech over an evil heart (Pro 26:23-26, Ps 28:3, 55:21); integrity that does NOT trust itself but casts on grace (Ps 26:11).",
  "speech; the-heart; forgiveness(concealment vs confession); being-known.",
  "Is integrity 'wholeness', 'truthfulness', or 'consistency inside-out'? Is the masking heart a failure OF integrity or a distinct operation (deception)? What of integrity that pleads grace (26:11)?"),
 ("speech-outflow","Speech as the outflow of the heart","legibility · restraint · concealment · life/death power · healing · penetration","speech-relational","established","Psa,Pro",
  "Speech as the heart surfacing - what is within comes out the mouth, so the lips DIAGNOSE the heart.",
  "COLOURS: legibility (the mouth reveals/conceals the heart, Pro 10:11, Ps 5:9); RESTRAINT as self-governance (Pro 10:19, 13:3); CONCEALMENT/masking (Pro 26:24); LIFE and DEATH in the tongue (Pro 18:21); HEALING/gracious words (Pro 12:18, 16:24); words that PENETRATE the hearer's inner parts (Pro 18:8).",
  "integrity-legibility; self-mastery(tongue-restraint); the-heart; the-masking-heart.",
  "Is speech a 'characteristic' or the primary EVIDENCE-channel for the others? Does speech only REVEAL the heart or also FORM it (words penetrate, 18:8)?"),
 ("entrustment","Entrustment / committing to God","committing the self · committing plans · committing the grievance · not-repaying · waiting","reflexive","surfaced","Psa,Pro",
  "Depositing the self, its plans, or its cause into God's keeping rather than holding/avenging.",
  "COLOURS: committing the SPIRIT/times (Ps 31:5,15); committing PLANS (Pro 16:3); the wronged self BECOMING PRAYER not revenge (Ps 109:4); NOT repaying, WAITING for the LORD (Pro 20:22, Ps 37); the planning heart under sovereignty (Pro 16:9, 21:1).",
  "trust; waiting; the-will-under-sovereignty; self-mastery(not-repaying).",
  "Is entrustment a distinct act or the RESOLVING move of trust? What is the relation of committing PLANS to the heart being TURNED by God (21:1) - agency and sovereignty?"),
 ("waiting-hope","Waiting / hope on the LORD","expectant watching · silent waiting · hope deferred/fulfilled · the watchman","godward","surfaced","Psa,Pro",
  "The self held expectantly toward God under delay.",
  "COLOURS: watching 'more than watchmen for the morning' (Ps 130:6); SILENT waiting (Ps 62:5); hope as the poor's posture (Ps 9:18); hope DEFERRED sickens / FULFILLED is life (Pro 13:12); fear-of-LORD -> rests SATISFIED (Pro 19:23).",
  "desire(hope); trust; entrustment; the-felt-interior(hope-sick).",
  "Is waiting a distinct movement or the intersection of hope+trust+stillness? Does Proverbs' 'hope deferred' (the WOUND of waiting) sit against the Psalter's confident waiting?"),
 ("seeking","Seeking (God's face / wisdom)","seeking the face · the one thing · seeking wisdom-as-beloved · the fixed gaze","godward","surfaced","Psa,Pro",
  "The self consolidating its attention/desire onto God, or onto wisdom as a person.",
  "COLOURS: seeking God's FACE / the 'one thing' (Ps 27:4,8); the fixed/lifted GAZE (Ps 25:15, 123); seeking WISDOM like silver, as a beloved sister/friend (Pro 2:4, 7:4, 8:17); seeking REWARDED with finding (Pro 8:17, Ps 9:10).",
  "desire; love-aheb(love of wisdom); waiting; the-fear-of-the-lord.",
  "Is seeking-God's-face and seeking-wisdom one operation with two objects? Is the 'fixed gaze' (eyes) a sub-operation of seeking or of trust?"),
 ("grief-lament","Grief / lament handled","integrity of sorrow · won't-fake-joy · deliberate remembering · unresolved lament · sorrow sown","experiential","surfaced","Psa,Pro",
  "The self voicing sorrow honestly, and handling it without faking or being destroyed.",
  "COLOURS: the self undone (Ps 6, 22); won't FAKE joy (Ps 137:2-4); sorrow SOWN reaps joy (Ps 126:5); DELIBERATE remembering against despair (Ps 143:5, 77:11); UNRESOLVED lament permitted (Ps 88); the heavy heart mis-comforted (Pro 25:20).",
  "the-felt-interior; being-heard; memory; restoration.",
  "Proverbs has little lament (a formation book, not a crisis book) - is grief therefore a Psalter-weighted characteristic? Does the felt-interior of Proverbs (heavy/crushed heart) BELONG here or separately?"),
 ("being-heard","Being heard / the cry answered","the cry from the depths · the pivot 'he has heard' · the fourfold cry · the panic-verdict overturned","experiential","surfaced","Psa",
  "The self cries from the bottom and the whole inner state inverts on being heard - largely a Psalter operation.",
  "COLOURS: the cry from the DEPTHS (Ps 130:1); the PIVOT (Ps 6:8, 22:24, 31:22); the FOURFOLD cry-and-deliverance (Ps 107); the panic-verdict overturned (Ps 31:22).",
  "grief; entrustment; trust(declared at the low point).",
  "Nearly absent in Proverbs - does being-heard belong to PRAYER (Psalms) rather than FORMATION (Proverbs)? Is the 'pivot' one operation or the meeting of cry+trust?"),
 ("restoration","Restoration / revival of the self","revival · re-creation · reversal · re-youthing","experiential","surfaced","Psa,Pro",
  "The flagging or dead-feeling self brought back / made alive.",
  "COLOURS: the soul RESTORED (Ps 23:3); RE-CREATION - a clean heart made (Ps 51:10); REVERSAL - mourning to dancing (Ps 30); the word as REVIVER (Ps 119:25); the righteous RISES again (Pro 24:16).",
  "the-felt-interior; being-heard; the-heart(clean heart); forgiveness.",
  "Is restoration a RETURN (23) or a MAKING-NEW (51)? In Proverbs it appears mainly as RESILIENCE (rising again) - same operation or different?"),
 ("joy-gladness","Joy / gladness","joy above plenty · fullness of joy · the new song · dreamlike joy · private joy · the cheerful heart","experiential","surfaced","Psa,Pro",
  "The self rejoicing - the affective signature of many operations.",
  "COLOURS: joy above plenty (Ps 4:7); fullness of joy in presence (Ps 16:11); the NEW song (Ps 33:3); DREAMLIKE joy (Ps 126:1); PRIVATE joy 'on their beds' (Ps 149:5); the CHEERFUL heart's continual feast (Pro 15:15); inmost exultation at another's wisdom (Pro 23:15).",
  "the-felt-interior; being-heard; restoration; desire(met).",
  "Is joy a characteristic in its own right or the affective FRUIT of trust/being-heard/restoration? What is the RELATIONAL joy (rejoicing in another's inner good, Pro 23:15)?"),
 ("rest-stillness","Rest / stillness / sleep / peace","fearless sleep · made rest · the stilled soul · sweet sleep · the un-anxious self","experiential","surfaced","Psa,Pro",
  "The self brought to a settledness that shows as sleep and inward stillness.",
  "COLOURS: fearless SLEEP amid danger (Ps 3:5, 4:8); rest MADE not achieved (Ps 23:2); the STILLED/quieted soul (Ps 131:2, 62:1); anxious toil vs God-given sleep (Ps 127:2); SWEET sleep of the wise (Pro 3:24); 'laughs at the time to come' (Pro 31:25).",
  "self-address(stilling); waiting(silence); trust; the-felt-interior; fearlessness.",
  "Is rest the STATE, waiting the POSTURE, self-quieting the ACT - three faces? Is sleep a proof of trust or a distinct gift?"),
 ("fearlessness","Fearlessness / courage from God","not-afraid · fear-of-man cancelled · take courage · the bold conscience · laughs at the future","godward","surfaced","Psa,Pro",
  "Courage/absence of dread DERIVED from God, not native.",
  "COLOURS: 'I will not fear, what can man do?' (Ps 56:11, 118:6); take COURAGE (Ps 27:14); the trusting heart unafraid of bad news (Ps 112:7); the clear conscience BOLD as a lion vs guilt's self-made dread (Pro 28:1); 'laughs at the time to come' (Pro 31:25).",
  "trust; fear-of-the-lord(fear-of-man its foil); rest; the-felt-interior.",
  "Is fearlessness a distinct operation or the FRUIT of trust / the flip-side of the fear-of-the-lord? Is guilt-born dread (28:1) the same faculty as the fear cancelled by trust?"),
 ("memory","Memory (self remembers; God remembers)","willed remembering · memory guarded by vow · forgetting-as-rebellion · God remembers · remember me","formation","surfaced","Psa,Pro",
  "The self governing its own remembering; resting on God's remembering.",
  "COLOURS: WILLED remembering against despair (Ps 77:11, 143:5); memory guarded by VOW (Ps 137:5); FORGETTING as the seedbed of rebellion (Ps 106:13, and evil as forgetting the covenant, Pro 2:17); GOD remembers the afflicted (Ps 9:12); 'remember me' (Ps 25:6).",
  "grief(deliberate remembering); trust(remembering God's character); forgiveness.",
  "Is memory a distinct operation or connective tissue (it serves grief, trust, fidelity)? Is 'forgetting' a failure of memory or of LOVE/fidelity (Pro 2:17)?"),
 ("forgiveness-confession","Forgiveness / confession vs concealment","the relief · the awe it generates · re-creation · confession vs concealment · the un-cleansable heart · conscience","formation","surfaced","Psa,Pro",
  "The self pardoned - and what pardon does to the interior; the confession that releases it.",
  "COLOURS: the bodily RELIEF of forgiveness (Ps 32:3-5); forgiveness that GENERATES fear/awe (Ps 130:4); RE-CREATION of a clean heart (Ps 51:10); CONFESSION vs CONCEALMENT (Pro 28:13, Ps 32); the un-self-cleansable heart (Pro 20:9); the SEARED vs tender conscience (Pro 30:20, 28:1).",
  "the-heart(clean/un-cleansable); integrity(concealment); being-known; humility.",
  "How does mercy DEEPEN fear (130:4) - the study's most counter-intuitive datum? Is the conscience (bold/seared/tender) a distinct faculty or a mode of being-known?"),
 ("self-examination","Self-examination vs self-deception","offering-to-be-tested · the way-that-seems-right · self-conceit · self-blindness · bravado","reflexive","surfaced","Psa,Pro",
  "The self scrutinising itself - and its failures (deception, conceit, blindness).",
  "COLOURS: OFFERING to be tested (Ps 26:2, 139:23); the way that SEEMS right but ends in death (Pro 14:12, 16:25); self-CONCEIT ('wise in his own eyes', Pro 26:12, 3:7); self-BLINDNESS ('pure in his own eyes', Pro 16:2); BRAVADO vs self-examination (Pro 21:29).",
  "being-known; teachability; humility; integrity.",
  "Is self-examination the same as inviting God's search, or a prior human act? Why can the self be so WRONG about itself (the way-that-seems-right) - a structural blindness?"),
 ("formation-by-relation","Formation by trust and company","you become what you trust · become like your company · iron sharpens iron · anger is caught · transmission","formation","surfaced","Psa,Pro",
  "A LAW over the inner being: the self takes the shape of what it leans on and whom it keeps near.",
  "COLOURS: 'you become what you TRUST' - dead idols deaden (Ps 115:8, 135:18); 'walks with the wise BECOMES wise' (Pro 13:20); 'iron sharpens iron' (Pro 27:17); anger is CAUGHT from company (Pro 22:24); TRANSMISSION of wisdom across generations (Pro 4:3-4).",
  "trust(the object forms the truster); teachability; wisdom-as-indwelling.",
  "Is this a 'characteristic' or a LAW governing all of them (candidate organising principle)? Does it work by imitation, attachment, or something deeper?"),
 ("wisdom-formation","Wisdom's formation of the inner being","the aims/faculties built · wisdom indwelling · wisdom as guardian · wisdom-as-beloved · the two tables","formation","surfaced","Pro",
  "Proverbs-distinctive: wisdom acquired ENTERS and RE-FORMS the inner being, becoming an internal guardian; the self is under formation.",
  "COLOURS: the AIMS/faculties wisdom builds (Pro 1:2-4); wisdom coming INTO the heart, pleasant to the soul (Pro 2:10); wisdom as an INDWELLING guardian (Pro 2:11); wisdom as a BELOVED to court (Pro 4, 7, 8); the choice of TWO TABLES - Wisdom vs Folly (Pro 9).",
  "love-aheb(love of wisdom); seeking; teachability; the-heart(reshaped).",
  "Is 'wisdom' the arena or itself an inner-being characteristic once internalised? How does an acquired thing become a GUARDIAN (agency)? Is Folly its true mirror-opposite?"),
 ("the-compulsive-will","The compulsive / captured will","evil as insomnia · addiction · self-ensnaring sin · the craving that kills · the enslaved will","reflexive","surfaced","Psa,Pro",
  "The inner being whose will is captured - by evil, appetite, or its own sin - and cannot free itself.",
  "COLOURS: evil as INSOMNIA ('cannot sleep unless they have done wrong', Pro 4:16, Ps 36:4); ADDICTION ('I must have another drink', Pro 23:35); sin as SELF-BINDING ('held in the cords of his sin', Pro 5:22, Ps 7:15); the craving that KILLS (Pro 21:25); the un-bridled self (Ps 32:9).",
  "desire(disordered); self-mastery(its failure); self-inflicted-ruin; forgiveness(the bondage broken).",
  "Is the captured will a distinct characteristic or the FAILURE-mode of self-mastery + desire? Can the enslaved will free itself, or only be freed (mercy)?"),
 ("self-toward-others","The self toward others","generosity/kindness · love-of-enemy · refused envy · the neighbour-facing heart · schadenfreude refused","speech-relational","surfaced","Psa,Pro",
  "The inner being's dispositions toward other people - which return upon the self.",
  "COLOURS: GENEROSITY/kindness that benefits the self (Pro 11:17,25); LOVE of enemy - good done (Pro 25:21, Ps 35:13); refused ENVY of the violent/sinners (Pro 3:31, 23:17, Ps 37:1, 73:3); the neighbour-facing heart (Pro 3:27, 22); the heart guarded against GLOATING (Pro 24:17, Ps 35:13).",
  "love-aheb(covering, enemy); self-mastery(the heart policed at feeling); the-felt-interior(envy).",
  "Is the disposition-toward-others a distinct characteristic or the OUTWARD face of love/humility/self-mastery? Why is even the FEELING of gloating policed (24:17)?"),
 ("self-address","Self-address / the dialogical self","rousing the soul · stilling the soul · self-interrogation · exhorting one's own heart","reflexive","established","Psa,Pro",
  "The self speaking to itself to move itself - the inner being as more than one voice.",
  "COLOURS: ROUSING ('Bless the LORD, O my soul', Ps 103:1); STILLING ('Return, O my soul, to your rest', Ps 116:7, 62:5); self-INTERROGATION ('why are you cast down?', Ps 42:5); exhorting one's OWN heart (Ps 27:14); in Proverbs the imperative to 'direct/give your heart' (Pro 23:19,26).",
  "self-mastery(the act); rest(the stilling state); the-heart(addressed).",
  "Who is the 'I' that addresses the 'soul' - are they the same self viewing itself, or distinct? Is self-address a Psalter form that Proverbs turns into COMMAND (give me your heart)?"),
]

def main():
    c=sqlite3.connect(DB); cur=c.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS ib_characteristic (
      id INTEGER PRIMARY KEY, code TEXT UNIQUE, name TEXT, aka TEXT, family TEXT,
      status TEXT, books TEXT, gist TEXT, colour_range TEXT, junctions TEXT,
      open_questions TEXT, discovery_doc TEXT, provenance TEXT, created_at TEXT, updated_at TEXT);
    ''')
    ins=upd=0
    for row in R:
        code=row[0]
        ex=cur.execute("SELECT id FROM ib_characteristic WHERE code=?",(code,)).fetchone()
        vals=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],PROV,NOW)
        if ex:
            cur.execute("""UPDATE ib_characteristic SET name=?,aka=?,family=?,status=?,books=?,gist=?,
                colour_range=?,junctions=?,open_questions=?,provenance=?,updated_at=? WHERE code=?""",vals+(code,)); upd+=1
        else:
            cur.execute("""INSERT INTO ib_characteristic (code,name,aka,family,status,books,gist,colour_range,junctions,open_questions,provenance,created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",(code,)+vals[:9]+(PROV,NOW,NOW)); ins+=1
    c.commit()
    n=cur.execute("SELECT COUNT(*) FROM ib_characteristic").fetchone()[0]
    print(f"ib_characteristic: {ins} inserted, {upd} updated; {n} total in registry")
    for r in cur.execute("SELECT code,status,books FROM ib_characteristic ORDER BY family,code"):
        print(f"  [{r[1]:11}] {r[0]:24} ({r[2]})")

if __name__=='__main__': main()
