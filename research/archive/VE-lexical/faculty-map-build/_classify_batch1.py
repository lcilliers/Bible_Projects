# -*- coding: utf-8 -*-
"""Faculty classification for inventory slice 0..343. Decisions grounded in gloss+senses, original-language aware."""
import json

# key = Strong's; value = (faculty list, basis, confidence, taxonomy_flag)
D = {
# --- agatho- family: "do good" = moral ACT/quality, not an inner faculty itself ---
"G0014": ([], "to do good = moral act/conduct, not an inner capacity", "high", ""),
"G0015": ([], "to do good = moral act/conduct", "high", ""),
"G0016": ([], "doing good = conduct/act", "high", ""),
"G0017": ([], "doer of good = agent-descriptor of conduct", "high", ""),
"G0018": ([], "good = quality/state of things, not a faculty", "high", ""),
"G0019": ([], "goodness = moral quality/virtue-state, not an operating faculty", "high", ""),
# --- joy family ---
"G0020": (["affect"], "gladness/great joy = emotion", "high", ""),
"G0021": (["affect"], "to rejoice = emotional act", "high", ""),
"G0024": (["affect"], "indignation = emotion (anger)", "high", ""),
# --- love ---
"G0025": (["affect","volition"], "to love = affection and committed will toward the loved", "high", ""),
"G0026": (["affect","volition"], "love = affection + committed devotion", "high", ""),
# --- holiness family: states/qualities, not faculties ---
"G0038": ([], "sanctification/holiness = state/status", "high", ""),
"G0040G": ([], "holy = state/quality", "high", ""),
"G0041": ([], "holiness = state", "high", ""),
"G0042": ([], "holiness = state", "high", ""),
# --- purity family ---
"G0047": ([], "purity = state/condition", "high", ""),
"G0048": ([], "to purify = ritual/physical act of cleansing, not an inner faculty", "high", ""),
"G0049": ([], "purification = act/process", "high", ""),
# --- agnoeo: be ignorant = a cognitive condition (lack of knowing) ---
"G0050": (["cognition"], "be ignorant/unaware = the knowing faculty (in deficit)", "high", ""),
"G0053": ([], "pure/innocent = moral state/condition, not an operating faculty", "med", ""),
"G0054": ([], "purity = state", "high", ""),
# --- agon / struggle / agency candidates ---
"G0073": ([], "fight/conflict/struggle = a situation/contest, not an inner faculty", "high", ""),
"G0074": (["affect"], "agony = anguish, an emotional/distress state", "high", ""),
"G0075": (["agency","volition"], "to struggle/strive = exertion of effort toward an end", "med", "agency"),
# --- kinship/relational ---
"G0079": ([], "sister = a person/relation, not a faculty", "high", ""),
"G0081": ([], "brotherhood = a collective/relation, not an operating capacity", "med", ""),
# --- distress ---
"G0085": (["affect"], "be distressed/troubled = emotional state", "high", ""),
"G0087": (["moral_evaluation"], "impartial = even-handed in judging (assess vs standard without partiality)", "med", ""),
# --- wrong/injustice family ---
"G0091": ([], "to harm/wrong = an injurious act done to another", "high", ""),
"G0092": ([], "crime/wrongdoing/iniquity = a recorded wrong/offence (status)", "high", ""),
"G0093": (["moral_evaluation"], "unrighteousness = moral-standard category (assessed-against-standard)", "med", ""),
"G0094": (["moral_evaluation"], "unjust/unrighteous = moral-standard descriptor", "med", ""),
"G0097": ([], "pure/guileless = moral state", "high", ""),
# --- athumeo: be discouraged = loss of heart/spirit, an affect ---
"G0120": (["affect"], "be discouraged = dispiritedness, an emotion (corrected: not perception)", "high", ""),
# --- praise family: acts of worship/speech, not inner faculties ---
"G0133": ([], "praise = act of worship/speech", "high", ""),
"G0134": ([], "to praise = speech-act", "high", ""),
"G0136": ([], "praise = act", "high", ""),
# --- choose ---
"G0138": (["volition"], "to choose = act of the will", "high", ""),
"G0140": (["volition"], "to choose/select = will (affection optional; choosing is the core)", "high", ""),
# --- aisthesis / sense ---
"G0144": (["perception","cognition"], "insight/discernment = inner sensing that grasps; perception feeding cognition", "med", ""),
"G0145": (["perception"], "sense/organ of discernment = the faculty of perceiving", "med", ""),
# --- shame family ---
"G0150": (["affect","conscience"], "shameful/disgraceful = evokes shame; conscience-linked emotion", "med", ""),
"G0152": (["affect","conscience"], "shame = the painful self-awareness emotion (conscience)", "high", ""),
"G0153": (["affect","conscience"], "be ashamed = feeling shame (conscience-bound affect)", "high", ""),
# --- aitia / cause ---
"G0156": (["cognition"], "cause/reason/charge = a reasoned ground; weighing why", "med", ""),
"G0159": ([], "causer/source = an agent/origin descriptor, not a faculty", "med", ""),
# --- impurity ---
"G0167": ([], "impurity/uncleanness = state", "high", ""),
"G0169": ([], "unclean = state", "high", ""),
"G0172": ([], "innocent/naive = moral state, not an operating faculty", "med", ""),
"G0178": ([], "uncondemned = legal/status descriptor", "high", ""),
# --- akoe: hearing = perception ---
"G0189": (["perception"], "hearing = the faculty/act of perceiving by ear", "high", ""),
# --- self-control deficiency (akrasia/akrates) ---
"G0192": (["volition"], "self-indulgence = failure of volitional self-mastery", "med", ""),
"G0193": (["volition"], "intemperate/without self-control = volitional self-mastery (in deficit)", "med", ""),
# --- pride/boasting ---
"G0212": ([], "boasting/arrogance = a disposition expressed in speech/act; state, not a core faculty", "med", ""),
"G0213": ([], "braggart = a person/character descriptor", "high", ""),
# --- truth family: quality/state, the *being* truthful is not the truth-faculty ---
"G0225": ([], "truth = a quality/state of what is real (corrected: not affect)", "med", ""),
"G0226": ([], "be truthful = speaking truly, a speech-quality/act", "med", ""),
"G0227": ([], "true/real = quality/state", "high", ""),
"G0228": ([], "true = quality/state", "high", ""),
"G0236": ([], "to change/exchange = a transformation act on a thing", "high", ""),
"G0253": (["affect"], "without anxiety = absence of an emotion (affect)", "med", ""),
# --- sin family: sin = recorded offence/status; sinning = volitional act ---
"G0264": (["volition"], "to sin = willed transgression (act of the will against standard)", "med", ""),
"G0265": ([], "sin (a sin) = an offence/record, not a faculty", "high", ""),
"G0266": ([], "sin = offence/status/record (corrected: not volition)", "med", ""),
"G0268": ([], "sinful/sinner = a person/status descriptor", "high", ""),
"G0275": (["affect"], "untroubled/free from anxiety = absence of an emotion", "med", ""),
"G0278": ([], "irrevocable/without regret = property of a decision/state, not a faculty", "med", ""),
"G0315": ([], "to compel/force = coercive act upon another", "high", ""),
"G0318": (["affect"], "necessity/distress/hardship = pressing-need; here a distress affect", "low", ""),
"G0329": ([], "to rekindle/fan = a stirring act (metaphorical), physical-rooted", "med", ""),
"G0338": ([], "innocent/guiltless = legal/moral status", "med", ""),
"G0341": ([], "to renew = act of renewing/restoring", "high", ""),
"G0342": ([], "renewal = process/state", "high", ""),
"G0361": ([], "sinless = moral status descriptor", "high", ""),
# --- remembrance ---
"G0363": (["memory"], "to remind/remember = the memory faculty", "high", ""),
"G0364": (["memory"], "remembrance/reminder = memory", "high", ""),
# --- mercy family ---
"G0415": (["affect"], "merciless/ruthless = absence of compassion (affect)", "med", ""),
"G0420": (["affect","volition"], "not resentful/forbearing = enduring wrong; composed will + affect", "med", ""),
"G0425": ([], "rest/relief/ease = a state of relief, not a faculty", "med", ""),
"G0430": (["volition"], "to endure/bear with = forbearance, a sustained act of will", "med", ""),
"G0448": (["affect"], "merciless = lacking compassion (affect)", "med", ""),
# --- lawlessness ---
"G0458": (["moral_evaluation"], "lawlessness/wickedness = moral-standard category", "med", ""),
"G0462": (["moral_evaluation"], "unholy = moral-standard descriptor", "med", ""),
"G0463": (["affect","volition"], "tolerance/forbearance = patient restraint (composed will, holding back)", "low", ""),
"G0464": (["agency","volition"], "to struggle against = contending effort", "med", "agency"),
"G0467": ([], "to repay/recompense = transactional act", "high", ""),
"G0476": ([], "opponent/adversary/accuser = a person/role", "high", ""),
"G0485": ([], "dispute/hostility = a conflict situation, not an inner faculty", "med", ""),
"G0505": ([], "genuine/sincere/unhypocritical = quality of character/state", "med", ""),
# --- worthy ---
"G0514": (["moral_evaluation"], "worthy/deserving = assessed value against a standard", "med", ""),
"G0515": (["moral_evaluation","cognition"], "to deem worthy = judging/reckoning worth", "med", ""),
# --- apalgeo: become callous = loss of feeling, an affective deadening ---
"G0524": (["affect"], "become callous/past feeling = deadened affect", "high", ""),
# --- deceit family: deceit = act/quality of misleading ---
"G0539": ([], "deceit/deceitfulness = act/quality of deception, not a core faculty", "med", ""),
"G0543": ([], "disobedience = a state/pattern of refusing; here noun-state", "med", ""),
"G0544": (["volition"], "to disobey = willed refusal to comply", "med", ""),
"G0560": (["affect"], "to despair = loss of hope, an emotion", "med", ""),
# --- belief/unbelief ---
"G0569": (["volition","cognition"], "to disbelieve = withholding trust/assent (will + judgement)", "med", ""),
"G0570": (["volition","cognition"], "unbelief = withholding of trust/assent", "med", ""),
"G0571": ([], "unbelieving/faithless = a person/character descriptor", "med", ""),
"G0572": ([], "openness/generosity/sincerity = disposition-quality/state", "med", ""),
"G0573": ([], "sound/healthy = state of soundness", "high", ""),
"G0577": ([], "to throw away/cast off = physical act", "high", ""),
"G0580": ([], "loss/rejection/deprivation = an outcome/status", "high", ""),
"G0603": (["affect","perception"], "eager expectation/longing = yearning watchfulness (desire + looking)", "med", ""),
"G0604": ([], "to reconcile = act of restoring relationship (outcome-act)", "med", ""),
"G0639": (["cognition","affect"], "be perplexed = at a loss in mind (puzzled), with disquiet", "med", ""),
"G0646": ([], "apostasy/forsaking = a defection act/state", "med", ""),
"G0662": (["volition","affect"], "be bold/dare = resolute daring (will + courage-affect)", "med", ""),
"G0674": (["affect"], "to faint/lose life = swooning from emotion/shock", "low", ""),
# --- aproskopos: blameless/clear ---
"G0677": (["conscience"], "without offence/clear (conscience) = inner witness of innocence", "med", ""),
"G0679": ([], "without stumbling/falling = a kept-state", "med", ""),
"G0701": ([], "pleasing = quality of pleasing another, not an inner faculty", "med", ""),
"G0724": ([], "plunder/greed-grabbing = rapacious act/its spoil", "med", ""),
"G0726": ([], "to seize/snatch = physical act", "high", ""),
"G0746": ([], "beginning/rule/ruler = origin/authority noun", "high", ""),
"G0757": ([], "be first/begin = inception act/precedence", "high", ""),
"G0766": ([], "debauchery/sensuality = a vice-conduct/state", "med", ""),
# --- astheneia / weakness family: bodily/affective weakness; weak=state ---
"G0769G": (["affect"], "weakness (felt limitation) = experienced frailty (affective sense of weakness)", "low", ""),
"G0769H": ([], "weakness: illness = bodily state", "high", ""),
"G0770G": (["affect"], "be weak (felt) = experiencing frailty", "low", ""),
"G0770H": ([], "be weak: ill = bodily state", "high", ""),
"G0771": ([], "weakness/failing = a limitation/state", "med", ""),
"G0772G": ([], "weak = state/condition", "med", ""),
"G0772H": ([], "weak: ill = bodily state", "high", ""),
# --- wisdom-deficit family ---
"G0781": (["cognition"], "unwise = the cognitive/wisdom faculty (in deficit)", "high", ""),
"G0801": (["cognition"], "senseless/without understanding = cognition (in deficit)", "high", ""),
"G0802": ([], "untrustworthy/faithless = character-quality/status of a person", "med", ""),
"G0808": (["affect"], "indecency/shameful-exposure = that which shames; shame-affect linked", "low", ""),
"G0810": ([], "debauchery/dissipation = vice-conduct/state", "med", ""),
# --- dishonour family ---
"G0818": ([], "to dishonor/treat shamefully = an act done to another (corrected: affect was wrong)", "med", ""),
"G0819": (["affect"], "dishonour/disgrace = the shame/ignominy experienced; affect-linked status", "low", ""),
"G0824": (["moral_evaluation"], "wrong/improper = assessed-against-standard (also 'out of place')", "low", ""),
# --- self-will / self-chosen ---
"G0829": (["volition"], "self-willed = the will (asserting itself)", "high", ""),
"G0830": (["volition"], "self-chosen/of one's own accord = the will", "high", ""),
"G0831": ([], "to domineer/exercise authority = an act of dominating", "med", ""),
"G0842": ([], "self-sufficient/content = a state of sufficiency (contentment is M46)", "med", ""),
"G0843": (["conscience","moral_evaluation"], "self-condemned = inner verdict against self (conscience)", "med", ""),
# --- forgiveness/release ---
"G0859": ([], "forgiveness/release/liberty = an outcome/status, not the faculty itself", "med", ""),
"G0861": ([], "incorruptibility/immortality = a state/property", "high", ""),
"G0863G": ([], "to release: leave/divorce = act of leaving", "high", ""),
"G0863H": ([], "to release: forgive = act of remitting (outcome-act)", "med", ""),
"G0863I": ([], "to release: permit/let = act of allowing", "high", ""),
"G0865": (["affect"], "hating good/not loving good = aversion (affect)", "med", ""),
"G0866": ([], "not greedy/free from love of money = absence of a disposition", "med", ""),
# --- folly family ---
"G0877": (["cognition"], "foolishness = cognition/wisdom faculty (in deficit) (corrected: not moral_evaluation)", "med", ""),
"G0878": (["cognition"], "foolish = the cognitive faculty (in deficit)", "med", ""),
"G0880": ([], "mute/speechless/without meaning = a condition/property", "high", ""),
# --- torment family ---
"G0928G": ([], "to torture/torment = an act inflicted", "med", ""),
"G0928H": (["affect"], "to be in anguish/suffering = experiencing torment (affect)", "med", ""),
"G0929": ([], "torment = the affliction inflicted/its state", "med", ""),
"G0930": ([], "torturer/jailer = a person/role", "high", ""),
"G0931": (["affect"], "torment/pains = experienced suffering (corrected: not cognition)", "med", ""),
# --- kingdom/power family: dominion nouns, not inner faculties ---
"G0932": ([], "kingdom = realm/domain", "high", ""),
"G0933": ([], "palace = place", "high", ""),
"G0934": ([], "kingly/royal = quality", "high", ""),
"G0936": ([], "to reign = act of ruling", "high", ""),
"G0937": ([], "royal = quality", "high", ""),
"G0938G": ([], "queen = person/role", "high", ""),
# --- abomination ---
"G0946": ([], "abomination = a detestable thing/status", "high", ""),
"G0947": ([], "abominable = quality of a thing", "high", ""),
"G0948": (["affect"], "to abhor/detest = strong aversion (affect)", "med", ""),
"G0949": ([], "firm/sure/confirmed = a state of stability", "med", ""),
"G0950": ([], "to confirm/establish = act of confirming", "high", ""),
"G0951": ([], "confirmation = act/outcome", "high", ""),
"G0984": ([], "to hurt/harm = injurious act", "high", ""),
# --- blaspheme/slander ---
"G0987": ([], "to blaspheme/revile = speech-act", "high", ""),
"G0988": ([], "blasphemy/slander = speech-act/its content", "high", ""),
"G0989": ([], "blasphemous/abusive = a person/quality descriptor", "high", ""),
"G1000": ([], "a throw (stone's throw) = a measure/physical act", "high", ""),
# --- bouleuo family: counsel/plan = cognition+volition ---
"G1011": (["cognition","volition"], "to plan/resolve/take counsel = deliberation + decision", "high", ""),
"G1012": (["cognition","volition"], "plan/purpose/counsel = deliberate intent", "high", ""),
"G1013": (["volition"], "plan/will/intention = settled will", "high", ""),
"G1014": (["volition","affect"], "to will/wish/want = volition with inclination", "high", ""),
# --- gnome ---
"G1106": (["cognition","volition"], "resolution/judgment/opinion/consent = settled mind + decision", "high", ""),
"G1128": ([], "to train/exercise = disciplined act of training", "med", ""),
"G1162": ([], "petition/supplication/prayer = an act of asking", "med", ""),
# --- deilia / timidity = fear-affect ---
"G1167": (["affect"], "timidity/cowardice = fear (affect)", "high", ""),
"G1168": (["affect"], "be timid/afraid = fear (affect)", "high", ""),
"G1169": (["affect"], "timid/cowardly = fear-disposition (affect)", "high", ""),
"G1185": ([], "to entice/lure = act of enticing another", "high", ""),
"G1189": ([], "to pray/beg/beseech = act of asking", "med", ""),
"G1226": (["volition","cognition"], "to insist/affirm confidently = asserting with settled conviction", "low", ""),
# --- diaginosko: to decide/determine ---
"G1231": (["cognition","volition"], "to decide/determine = judging then resolving", "med", ""),
"G1242": (["volition"], "covenant = a binding commitment (thing-like, but rooted in pledged will)", "low", ""),
# --- diakrino ---
"G1252": (["cognition","moral_evaluation","volition"], "to discern/distinguish/doubt = weighing + judging + (waver of) will", "high", ""),
"G1253": (["cognition","moral_evaluation"], "discernment = perceiving distinctions + judging", "high", ""),
"G1256": (["cognition"], "to reason/discuss/argue = reasoning faculty", "high", ""),
"G1259": ([], "be reconciled = act of restoring relationship", "med", ""),
"G1260": (["cognition"], "to discuss/reason/question (inwardly) = reasoning (corrected: drop affect)", "med", ""),
"G1261": (["cognition"], "reasoning/thoughts/doubts = thinking faculty", "high", ""),
"G1270": (["cognition"], "thought = the cognitive product/faculty", "high", ""),
# --- dianoia: mind ---
"G1271": (["cognition"], "mind/understanding = the cognitive faculty/seat", "high", ""),
"G1280": (["cognition","affect"], "be perplexed = at a loss in mind, with disquiet", "med", ""),
"G1299": ([], "to direct/command/arrange = act of ordering/commanding", "high", ""),
"G1303": (["volition"], "to make a covenant/appoint = act of pledged disposing of one's will", "low", ""),
"G1311": ([], "to destroy/corrupt = act of ruining", "high", ""),
"G1312": ([], "decay/corruption = a process/state", "high", ""),
"G1328": ([], "interpreter = a person/role", "high", ""),
"G1329": (["cognition"], "to interpret = construing meaning (cognition)", "med", ""),
# --- dikaio- family: righteousness = moral-evaluation domain ---
"G1341": (["moral_evaluation"], "righteous judgment/justice = assessing against the standard", "high", ""),
"G1342": (["moral_evaluation"], "just/righteous = conformity-to-standard descriptor", "med", ""),
"G1343": (["moral_evaluation"], "righteousness = the standard-conformity quality/domain", "med", ""),
"G1344": (["moral_evaluation"], "to justify = render/declare righteous (a verdict-act)", "med", ""),
"G1345": (["moral_evaluation"], "righteous act/statute/regulation = standard-defined requirement", "med", ""),
"G1347": (["moral_evaluation"], "justification = verdict of righteousness", "med", ""),
"G1349": (["moral_evaluation"], "justice/penalty/condemnation = retributive judgment", "med", ""),
# --- doubt / double-mindedness ---
"G1365": (["cognition","volition"], "to doubt/waver = unsettled mind and will", "med", ""),
"G1374": (["cognition","volition"], "double-minded = a divided mind/will", "med", ""),
# --- test/approve family ---
"G1381": (["moral_evaluation","cognition"], "to test/examine/approve = assessing to judge worth/genuineness", "med", ""),
"G1382": (["moral_evaluation"], "proof/test/approval = the tried-and-assessed quality", "med", ""),
"G1383": (["moral_evaluation"], "testing/proving = assessment of genuineness", "med", ""),
"G1384": ([], "approved/tested/genuine = the resulting quality/state", "med", ""),
# --- deceit (dolos) family ---
"G1386": ([], "deceitful = quality of a person/speech", "med", ""),
"G1387": ([], "to deceive = act of deceiving", "med", ""),
"G1388": ([], "deceit/guile = act/quality of deception", "med", ""),
"G1389": ([], "to distort/adulterate = act of tampering", "high", ""),
"G1391": ([], "glory/splendor = honour/radiance status (corrected: not affect/cognition/perception)", "low", ""),
# --- slavery family: condition/role, not faculties ---
"G1396": ([], "to enslave/bring under control = act of subjugation", "high", ""),
"G1397": ([], "slavery/bondage = a condition", "high", ""),
"G1398": ([], "be a slave/serve = condition/act of serving", "high", ""),
"G1399": ([], "female slave = person/role", "high", ""),
"G1401": ([], "slave/servant = person/role", "high", ""),
"G1402": ([], "to enslave = act of subjugation", "high", ""),
# --- power/ability family: capacity-in-general, not inner-being faculty ---
"G1411": ([], "power/might = capacity/force (not an inner-being faculty per taxonomy)", "med", ""),
"G1412": ([], "to empower/strengthen = act of imparting power", "high", ""),
"G1414": ([], "be able/powerful = capacity-state", "med", ""),
"G1415": ([], "able/possible = capacity/possibility descriptor", "med", ""),
"G1426": ([], "slander/ill-report = speech-act/its content", "high", ""),
# --- gifts ---
"G1431": ([], "free gift = a thing given", "high", ""),
"G1433": ([], "to give/grant = act of giving", "high", ""),
"G1434": ([], "free gift = a thing given", "high", ""),
"G1435": ([], "gift/offering = a thing given", "high", ""),
# --- self-control (enkrateia) = volitional self-mastery ---
"G1466": (["volition"], "self-control = volitional self-mastery", "med", ""),
"G1467": (["volition"], "to exercise self-control = volitional self-mastery", "med", ""),
"G1468": (["volition"], "self-controlled/disciplined = volitional self-mastery", "med", ""),
"G1472": ([], "to rub on/anoint = physical act", "high", ""),
# --- idol family ---
"G1493": ([], "idol's temple = place", "high", ""),
"G1494": ([], "sacrificed to idols = a thing/status", "high", ""),
"G1495": ([], "idolatry = a religious practice/devotion misdirected (act/state)", "med", ""),
"G1496": ([], "idolater = person", "high", ""),
"G1497": ([], "idol = a thing", "high", ""),
# --- eiko: resemble ---
"G1503": ([], "to resemble/be like = a similarity relation, not a faculty", "med", ""),
"G1504": ([], "image/likeness = a thing/representation", "high", ""),
# --- sincerity (eilikrineia) ---
"G1505": (["conscience"], "sincerity/purity of motive = inner integrity (conscience)", "med", ""),
"G1506": ([], "pure/sincere = quality/state of a person", "med", ""),
# --- peace family: state, not a faculty (peace-as-felt = affect for the noun eirene) ---
"G1514": ([], "be at peace/live peaceably = a state/relational act", "med", ""),
"G1515": (["affect"], "peace = inner tranquillity (felt) as well as a state; affect when experienced", "low", ""),
"G1516": ([], "peaceful/peaceable = quality/disposition-state", "med", ""),
"G1517": ([], "to make peace = act of reconciling", "med", ""),
"G1518": ([], "peacemaker = a person/role", "high", ""),
# --- eisakouo: listen/heed ---
"G1522": (["perception"], "to hear/heed = perceptual attending (hearing)", "med", ""),
# --- avenge family ---
"G1556": (["moral_evaluation"], "to avenge/punish/do justice = enacting a standard-judgment", "med", ""),
"G1557": (["moral_evaluation"], "vengeance/retribution = standard-based requital", "med", ""),
"G1558": ([], "avenger = a person/role", "high", ""),
# --- ekthambeo: awe/alarm ---
"G1568": (["affect"], "be awe-struck/alarmed/amazed = emotion", "high", ""),
"G1569": (["affect"], "astonished/utterly astounded = emotion", "high", ""),
# --- ekkakeo / lose heart ---
"G1573": (["affect"], "to lose heart/grow weary = discouragement (affect) (corrected: not perception)", "high", ""),
"G1577": ([], "assembly/church = a collective/body, not a faculty", "high", ""),
"G1598": (["moral_evaluation"], "to test/tempt = putting to the test/assessing", "low", ""),
# --- fear (ekfobos) ---
"G1630": (["affect"], "terrified = fear (affect)", "high", ""),
"G1634": ([], "to expire/breathe last = death-event, physical", "high", ""),
# --- mercy/pity family ---
"G1652": (["affect"], "pitiful/pitiable = evoking pity; affect-linked descriptor", "med", ""),
"G1653": (["affect"], "to have mercy/pity = compassion (affect) (drop perception)", "high", ""),
"G1654": (["affect"], "charity/alms = mercy shown; rooted in compassion (affect)", "med", ""),
"G1655": (["affect"], "merciful = compassionate disposition (affect)", "high", ""),
"G1656": (["affect"], "mercy = compassion (affect)", "high", ""),
# --- hope ---
"G1679": (["affect","volition"], "to hope/expect = confident expectation (affective + trusting will)", "med", ""),
"G1680": (["affect","volition"], "hope = confident expectation (affect + trust-commitment)", "med", ""),
# --- fear (emfobos) ---
"G1719": (["affect"], "afraid/frightened/terror = fear (affect)", "high", ""),
"G1731": ([], "to show/demonstrate = act of displaying", "high", ""),
"G1738": (["moral_evaluation"], "just = standard-conformity descriptor", "med", ""),
"G1743": ([], "to strengthen/empower = act of imparting strength", "high", ""),
# --- energeia family: working/activity ---
"G1753": ([], "active energy/working = operation/force, not an inner-being faculty", "med", ""),
"G1754": ([], "be active/work = operating/effecting (act)", "med", ""),
"G1755": ([], "working/activity/effect = an operation/its result", "med", ""),
"G1756": ([], "effective/active = quality of efficacy", "high", ""),
# --- enthumeomai / ponder ---
"G1760": (["cognition"], "to reflect on/ponder/consider = cognition", "high", ""),
"G1761": (["cognition"], "reflection/thought/imagination = cognition", "high", ""),
"G1771": (["cognition","volition"], "thought/purpose/intent = mind + intention", "high", ""),
"G1775": ([], "unity = a relational state, not a faculty", "med", ""),
"G1783": ([], "intercession/petition/prayer = an act of asking", "med", ""),
# --- entrepo: shame/respect ---
"G1788": (["affect","conscience"], "to shame / make ashamed / regard with respect = shame-affect & conscience", "med", ""),
"G1790": (["affect"], "trembling (with fear) = fear (affect)", "high", ""),
"G1791": (["affect","conscience"], "shame = the shame emotion (conscience-linked)", "high", ""),
"G1793": ([], "to call on/intercede/appeal = an act of petitioning", "med", ""),
"G1813": ([], "to blot out/wipe away/cancel = act of erasing", "high", ""),
# --- exaporeo: despair ---
"G1820": (["affect"], "to despair utterly = despair (affect)", "high", ""),
"G1832": ([], "be permitted/lawful = a permission/status", "high", ""),
"G1840": ([], "to have power/be strong = capacity-state", "med", ""),
# --- confess/agree (exomologeo) ---
"G1843": (["volition","cognition"], "to confess/acknowledge/agree = assenting acknowledgement (will + cognition)", "med", ""),
# --- exoutheneo: despise ---
"G1848": (["affect","moral_evaluation"], "to despise/hold in contempt = contempt (affect + negative appraisal)", "med", ""),
"G1849": ([], "authority/right/power = a delegated right/status", "high", ""),
"G1850": ([], "to have/exercise authority = act of exercising power", "high", ""),
"G1864": (["agency","volition"], "to contend/struggle for = striving effort", "med", "agency"),
# --- praise (epaineo) ---
"G1867": ([], "to praise/commend = speech-act of commendation", "high", ""),
"G1868": ([], "praise/commendation = the commendation given", "high", ""),
# --- listen (epakouo / epakroaomai) ---
"G1873": (["perception"], "to hear/heed = perceptual attending", "med", ""),
"G1874": (["perception"], "to listen to = perceptual attending", "med", ""),
"G1917": ([], "plot/scheme = a contrived plan/act against someone", "med", ""),
# --- gentleness (epieikeia) ---
"G1932": ([], "gentleness/forbearance/reasonableness = a disposition-virtue (corrected: not cognition)", "med", ""),
"G1933": ([], "gentle/reasonable/forbearing = disposition-quality (corrected: not cognition)", "med", ""),
# --- seek/desire family ---
"G1934": (["affect","volition"], "to seek after = pursuing desire (longing + intentional seeking)", "med", ""),
"G1937": (["affect"], "to long for/desire = desire (affect) (drop perception)", "high", ""),
"G1938": (["affect"], "one who desires/craves = desire (affect)", "high", ""),
"G1939": (["affect"], "desire/passion/lust = desire (affect)", "high", ""),
"G1941": ([], "to call on/invoke/name = act of invoking/naming", "med", ""),
# --- forget ---
"G1950": (["memory"], "to forget/neglect = memory (failure of)", "high", ""),
# --- thought (epinoia) ---
"G1963": (["cognition"], "thought/intent/design = cognition", "high", ""),
# --- long for (epipotheo) ---
"G1971": (["affect"], "to long for = yearning (affect)", "high", ""),
"G1972": (["affect"], "longing = yearning (affect)", "high", ""),
"G1973": (["affect"], "longed for = object of yearning; affect-linked", "med", ""),
"G1974": (["affect"], "longing = yearning (affect)", "high", ""),
# --- knowing (epistemon) ---
"G1990": (["cognition"], "knowing/understanding/skilled = cognition", "high", ""),
"G2021": (["agency","volition"], "to attempt/undertake = initiating an endeavour", "low", "agency"),
"G2025": ([], "to rub on/anoint = physical act", "high", ""),
"G2026": ([], "to build up/upon (edify) = act of building (physical/metaphorical)", "med", ""),
"G2042": ([], "to provoke/irritate/stir up = act of provoking another", "med", ""),
"G2052": ([], "selfish ambition/rivalry = a self-seeking disposition/strife (state)", "med", ""),
"G2054": ([], "quarrel/strife/dissension = conflict situation", "med", ""),
# --- interpret (hermeneia) ---
"G2058": (["cognition"], "interpretation = construing meaning (cognition)", "med", ""),
"G2059": (["cognition"], "to interpret/translate = construing meaning (cognition)", "med", ""),
"G2065": ([], "to ask/request = act of asking", "high", ""),
# --- delight (eudokeo) ---
"G2106": (["affect","volition"], "to be well pleased/delight/choose = pleasure + favourable resolve", "high", ""),
"G2107": (["affect","volition"], "goodwill/good pleasure/resolve = favourable disposition + purpose", "high", ""),
# --- cheer (euthumeo) ---
"G2114": (["affect"], "be cheerful/take heart = good spirits (affect) (corrected: not perception)", "high", ""),
"G2118": (["moral_evaluation"], "uprightness/rectitude = standard-conformity", "med", ""),
# --- reverence (eulabeia) ---
"G2124": (["affect"], "reverence/godly fear = reverent awe (affect)", "med", ""),
"G2125": (["affect"], "to revere/fear reverently = reverent awe (affect)", "med", ""),
"G2126": (["affect"], "devout/reverent = reverent disposition (affect)", "med", ""),
"G2127": ([], "to bless/praise = speech-act of blessing", "high", ""),
"G2151": ([], "to show piety/worship = act of worship/piety", "med", ""),
# --- compassionate (eusplanchnos) ---
"G2155": (["affect"], "compassionate/tenderhearted = compassion (affect) (drop perception)", "high", ""),
"G2162": ([], "good report/commendable = reputation-quality", "med", ""),
# --- gladness (eufraino) ---
"G2165": (["affect"], "to rejoice/make merry/celebrate = gladness (affect)", "high", ""),
"G2167": (["affect"], "joy/gladness = emotion", "high", ""),
# --- thanks (eucharisteo) ---
"G2168": (["affect"], "to give thanks = gratitude (affect) (corrected: not blank)", "med", ""),
"G2169": (["affect"], "thankfulness/gratitude = gratitude (affect) (corrected: not perception)", "med", ""),
"G2170": (["affect"], "thankful/grateful = gratitude (affect) (corrected: not memory)", "med", ""),
# --- vow/prayer (euche) ---
"G2171": (["volition"], "a vow/prayer = pledged commitment (vow) of the will", "med", ""),
"G2174": (["affect"], "be glad/of good cheer = good spirits (affect)", "high", ""),
# --- echo: to have/be ---
"G2192": ([], "to have/hold/possess = possession/state, not an inner faculty (corrected: not cognition)", "med", ""),
"G2200": (["affect"], "hot/fervent (metaphorical zeal) = fervour (affect)", "med", ""),
"G2204": (["affect"], "be fervent/boil (with zeal) = fervour (affect) (drop perception)", "high", ""),
# --- zeal (zelos) ---
"G2205": (["affect","volition"], "zeal/jealousy = fervent emotion + driving will", "high", ""),
}

sl=json.load(open('research/VE-lexical/faculty-map-build/_slice_batch1.json',encoding='utf-8'))
out=[]
missing=[]
for x in sl:
    s=x['s']
    if s not in D:
        missing.append((x['s'],x['t'],x['g']))
        continue
    fac,basis,conf,flag=D[s]
    out.append({"s":s,"t":x['t'],"faculty":fac,"basis":basis,"confidence":conf,"taxonomy_flag":flag})

print("classified",len(out),"of",len(sl))
if missing:
    print("MISSING",len(missing))
    for m in missing: print("  ",m)
else:
    json.dump(out,open('research/VE-lexical/faculty-map-build/map-batch1.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print("written map-batch1.json")
