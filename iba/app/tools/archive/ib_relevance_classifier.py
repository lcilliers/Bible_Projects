"""
Free, local, wordlist-based first pass at Inner-Being (IB) relevance for a
standalone English lookup term (no DB lookups, no context/verse
disambiguation - that is a later, separate phase once verses are analysed;
this only asks whether the term's own meaning touches the inner being at
all).

classify_ib_relevance(term) returns one of three labels:
  - "IB related": at least one content word matches a known inner-being
    category (emotion, volition/cognition, character/moral trait, spiritual
    state). Confident yes.
  - "Not relevant": every content word matches a known non-IB category
    (concrete object/material, plant/animal, literal body part, kinship/
    social role, number, or a recognised biblical place/person name), or the
    term is a pure grammatical fragment (stopwords only, e.g. "each other",
    "for his own" - leftovers from the comma/semicolon splitting upstream).
    Confident no.
  - "Could impact IB": everything else - anything the wordlists don't
    confidently cover, plus body-part words that are also standing idiom for
    the inner being in Hebrew (heart, bowels, kidneys, ...). Default/fallback
    bucket, deliberately: a wrong "IB related"/"Not relevant" call is worse
    than an honest "not sure", since this bucket is what a human reviews.

This is a coverage heuristic, not a dictionary or an NLP model - it will
under-cover before it over-claims. Expect real review effort on the "Could
impact IB" bucket; the wordlists here are sized to clear the obvious
majority, not to be exhaustive.
"""
import re

# --- IB related: emotion, volition/cognition, character/moral trait, spiritual state ---

IB_RELATED_WORDS = {
    # emotion
    "love", "hate", "hatred", "joy", "grief", "sorrow", "sadness", "happiness",
    "delight", "pleasure", "anger", "wrath", "rage", "fury", "indignation",
    "fear", "terror", "dread", "anxiety", "worry", "distress", "anguish",
    "agony", "envy", "jealousy", "malice", "bitterness", "resentment",
    "affection", "tenderness", "compassion", "pity", "mercy", "sympathy",
    "empathy", "longing", "desire", "yearning", "hope", "despair",
    "disappointment", "shame", "guilt", "remorse", "regret", "contempt",
    "disgust", "loathing", "scorn", "disdain", "contentment", "satisfaction",
    "gladness", "cheerfulness", "gloom", "despondency", "dejection",
    "melancholy", "misery", "wretchedness", "comfort", "consolation",
    "courage", "boldness", "confidence", "timidity", "cowardice", "dismay",
    "panic", "alarm", "astonishment", "amazement", "wonder", "awe",
    "surprise", "shock", "calm", "peace", "tranquility", "serenity",
    "agitation", "turmoil", "unrest", "restlessness", "eagerness", "zeal",
    "passion", "fervor", "enthusiasm", "apathy", "indifference", "coldness",
    "warmth", "kindness", "tenderheartedness", "harshness", "cruelty",
    "gentleness", "meekness", "grudge", "spite", "vexation", "irritation",
    "annoyance", "frustration", "loneliness", "homesickness", "nostalgia",
    "excitement", "thrill", "dread", "trepidation", "apprehension",
    # volition / cognition
    "will", "desire", "intend", "intention", "purpose", "resolve",
    "determination", "decide", "decision", "choose", "choice", "believe",
    "belief", "faith", "doubt", "trust", "distrust", "suspicion", "think",
    "thought", "mind", "understanding", "wisdom", "knowledge", "discernment",
    "insight", "perception", "judgment", "reason", "reasoning",
    "imagination", "memory", "remember", "forget", "conscience",
    "consciousness", "awareness", "attention", "intent", "motive",
    "motivation", "plan", "scheme", "deliberate", "ponder", "meditate",
    "contemplate", "reflect", "consider", "conviction", "persuasion",
    "opinion", "willing", "unwilling", "reluctant", "eager", "hesitate",
    "resolve", "determine",
    # character / moral trait
    "righteous", "righteousness", "wicked", "wickedness", "evil", "good",
    "goodness", "virtue", "vice", "holy", "holiness", "sin", "sinful",
    "sinfulness", "iniquity", "transgression", "innocence", "purity",
    "impurity", "defilement", "corruption", "integrity", "honesty", "deceit",
    "deception", "lying", "falsehood", "truthfulness", "faithfulness",
    "unfaithfulness", "loyalty", "betrayal", "treachery", "humility",
    "humbleness", "pride", "arrogance", "haughtiness", "vanity", "conceit",
    "boastfulness", "modesty", "patience", "longsuffering", "forbearance",
    "temperance", "greed", "covetousness", "gluttony", "lust", "chastity",
    "generosity", "selfishness", "altruism", "benevolence", "malevolence",
    "mercilessness", "justice", "injustice", "fairness", "unfairness",
    "honor", "dishonor", "disgrace", "folly", "foolishness", "prudence",
    "imprudence", "diligence", "laziness", "sloth", "bravery", "valor",
    "obedience", "disobedience", "rebellion", "submission", "defiance",
    "stubbornness", "obstinacy", "willfulness", "docility", "gratitude",
    "ingratitude", "thankfulness", "discontent", "complaining", "murmuring",
    "hypocrisy", "sincerity", "insincerity", "cunning", "guile", "slander",
    "gossip", "flattery", "impudence", "shamelessness", "modest",
    "praise", "pure", "purity", "true", "truth", "genuine", "innocent",
    "corrupt", "understand", "perceive", "discern", "counsel", "curse",
    "bless", "blessing", "strife", "quarrel", "honour", "dishonour",
    "favour", "disfavour", "behaviour",
    # spiritual state
    "soul", "spirit", "repentance", "repent", "conversion", "salvation",
    "redemption", "sanctification", "grace", "worship", "devotion", "piety",
    "godliness", "ungodliness", "blasphemy", "reverence", "irreverence",
    "unbelief", "apostasy", "backsliding", "regeneration", "rebirth",
    "transformation", "renewal", "consecration", "dedication", "idolatry",
    "superstition", "lukewarmness", "guilty", "blessed", "cursed",
}

# --- Not relevant: concrete object/material, plant/animal, literal body part, ---
# --- kinship/social role, number, common biblical place/person name          ---

CONCRETE_OBJECT_WORDS = {
    "gold", "silver", "bronze", "brass", "iron", "stone", "wood", "wheat",
    "barley", "bread", "wine", "oil", "water", "chariot", "sword", "spear",
    "shield", "armor", "ship", "boat", "house", "tent", "altar", "temple",
    "garment", "cloak", "robe", "veil", "curtain", "table", "throne",
    "crown", "ring", "lamp", "candlestick", "basin", "pot", "jar", "vessel",
    "net", "rope", "gate", "wall", "pillar", "door", "window", "road",
    "field", "vineyard", "mountain", "valley", "river", "sea", "wilderness",
    "desert", "city", "land", "coin", "money", "silverware", "furniture",
    "money", "treasure", "gem", "jewel", "pearl", "linen", "wool", "sackcloth",
}

PLANT_ANIMAL_WORDS = {
    "lion", "bear", "wolf", "sheep", "lamb", "goat", "ox", "bull", "calf",
    "horse", "donkey", "camel", "dog", "cat", "bird", "dove", "eagle",
    "sparrow", "fish", "serpent", "snake", "locust", "ant", "bee", "fig",
    "vine", "olive", "palm", "cedar", "oak", "thorn", "thistle", "grass",
    "herb", "flower", "seed", "root", "branch", "leaf", "fruit", "wolf",
    "fox", "raven", "hawk", "owl", "stork", "swine", "pig",
}

LITERAL_BODY_PART_WORDS = {
    "hand", "foot", "arm", "leg", "head", "eye", "ear", "nose", "mouth",
    "tooth", "teeth", "hair", "finger", "toe", "knee", "shoulder", "neck",
    "back", "skin", "bone", "thigh", "cheek", "lip", "brow", "forehead",
    "jaw", "elbow", "wrist", "ankle", "heel", "nostril",
}

KINSHIP_SOCIAL_WORDS = {
    "father", "mother", "son", "daughter", "brother", "sister", "husband",
    "wife", "king", "priest", "prophet", "servant", "slave", "master",
    "judge", "elder", "prince", "nation", "people", "tribe", "family",
    "widow", "orphan", "neighbor", "stranger", "foreigner", "citizen",
}

NUMBER_WORDS = {
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety", "first", "second", "third",
    "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth",
    "many", "few", "several", "dozen", "hundred", "hundreds", "hundredth",
    "hundredfold", "thousand", "thousands", "thousandth", "thousandfold",
    "million", "millionth",
}

# units of measure / currency - like NUMBER_WORDS, these accompany a
# quantity rather than carrying inner-being content themselves
UNIT_OF_MEASURE_WORDS = {
    "cubit", "cubits", "shekel", "shekels", "talent", "talents", "mina",
    "minas", "homer", "homers", "ephah", "ephahs", "omer", "omers", "hin",
    "hins", "bath", "baths", "gerah", "gerahs", "percent", "percentage",
    "span", "handbreadth", "fathom", "fathoms", "denarius", "denarii",
    "drachma", "stadion", "stadia", "cor", "cors", "seah", "seahs",
}

# common biblical place/person names likely to surface as glosses/headwords
PROPER_NAME_WORDS = {
    "jerusalem", "judah", "judea", "israel", "egypt", "babylon", "rome",
    "galilee", "samaria", "zion", "sinai", "canaan", "moab", "edom",
    "assyria", "persia", "greece", "syria", "damascus", "bethlehem",
    "nazareth", "jericho", "capernaum", "corinth", "ephesus", "antioch",
    "athens", "philippi", "thessalonica", "abraham", "isaac", "jacob",
    "moses", "aaron", "david", "solomon", "saul", "elijah", "elisha",
    "isaiah", "jeremiah", "ezekiel", "daniel", "peter", "paul", "john",
    "james", "matthew", "mark", "luke", "mary", "joseph", "jesus", "christ",
    "adam", "eve", "noah", "cain", "abel", "sarah", "rachel", "leah",
    "joshua", "gideon", "samson", "samuel", "ruth", "esther", "job",
    "jonah", "amos", "hosea", "micah", "nazirite", "levite", "pharisee",
    "sadducee", "gentile", "hebrew", "philistine", "canaanite", "god", "lord",
    # extended batch, 2026-07-24: the Bible has thousands of minor personal/
    # place names (genealogies, tribal lists) this list will never fully
    # enumerate - see the 2+-hyphen structural rule in classify_ib_relevance
    # for compound place names this list can't keep up with either
    "abaddon", "abagtha", "abana", "abda", "abdeel", "abdi", "abdiel",
    "abdon", "abi", "abiah", "abiathar", "abib", "abida", "abidan", "abiel",
    "abiezer", "abigail", "abihail", "abihu", "abijah", "abijam", "abimael",
    "abimelech", "abinadab", "abinoam", "abiram", "abishag", "abishai",
    "abishalom", "abishua", "abital", "abiud", "abner", "abram", "achan",
    "achish", "achsah", "adah", "adaiah", "adin", "adino", "adlai", "admah",
    "adnah", "adonijah", "adoniram", "adoram", "adriel", "agag", "agrippa",
    "ahab", "ahasuerus", "ahaz", "ahaziah", "ahiam", "ahiezer", "ahijah",
    "ahikam", "ahimaaz", "ahiman", "ahimelech", "ahinoam", "ahio", "ahira",
    "ahiram", "ahishar", "ahithophel", "ahitub", "ahuzzath", "aiah", "akkub",
    "alexander", "allon", "alpheus", "amalek", "amariah", "amasa",
    "amaziah", "ammiel", "ammihud", "amminadab", "ammon", "amnon", "amok",
    "amon", "amorite", "amoz", "amram", "amraphel", "anah", "anak",
    "ananias", "anath", "anathoth", "andrew", "aner", "anna", "annas",
    "antipas", "apollos", "aquila", "arad", "aram", "ararat", "araunah",
    "archelaus", "archippus", "aretas", "argob", "ariel", "arioch",
    "aristarchus", "armageddon", "arnan", "arnon", "aroer", "artaxerxes",
    "arvad", "asa", "asahel", "asaph", "asenath", "ashdod", "asher",
    "ashkelon", "ashkenaz", "ashtaroth", "ashtoreth", "asshur", "atarah",
    "athaliah", "attalia", "augustus", "azariah", "azaz", "azazel",
    "azekah", "azgad", "aziel", "azmaveth", "azriel", "azubah", "baal",
    "baalah", "baana", "baasha", "babel", "bahurim", "balaam", "balak",
    "barabbas", "barak", "barnabas", "bartholomew", "bartimaeus", "baruch",
    "barzillai", "bashan", "bathsheba", "becher", "beeliada", "beelzebub",
    "beer", "beersheba", "bela", "belial", "belshazzar", "belteshazzar",
    "benaiah", "benjamin", "beno", "beor", "bera", "berea", "berechiah",
    "bered", "bernice", "bethany", "bethel", "bethesda", "bethphage",
    "bethsaida", "bethuel", "bezaleel", "bezek", "bichri", "bigtha",
    "bigthan", "bildad", "bilhah", "bilhan", "bithynia", "boanerges",
    "boaz", "bukki", "caesar", "caesarea", "caiaphas", "cainan", "calah",
    "caleb", "cana", "candace", "cappadocia", "carchemish", "carmel",
    "carmi", "carpus", "cephas", "chaldea", "chedorlaomer", "chemosh",
    "cherith", "chilion", "chinnereth", "chios", "chloe", "chorazin",
    "chuza", "cilicia", "claudia", "claudius", "clement", "cleopas",
    "colosse", "cornelius", "crescens", "crete", "crispus", "cush",
    "cushi", "cyprus", "cyrene", "cyrus", "dagon", "dalmatia", "damaris",
    "dan", "darius", "dathan", "debir", "deborah", "decapolis", "delilah",
    "demas", "demetrius", "derbe", "dibon", "didymus", "dinah",
    "diotrephes", "dodai", "dophkah", "dorcas", "dothan", "drusilla",
    "dumah", "ebal", "eber", "eden", "edrei", "ehud", "eker", "ekron",
    "elam", "elath", "eldad", "eleazar", "elhanan", "eli", "eliab",
    "eliada", "eliakim", "eliam", "elias", "eliashib", "eliel", "elihu",
    "elika", "elim", "elimelech", "elioenai", "eliphaz", "elishama",
    "elishua", "elizur", "elkanah", "elnathan", "elon", "elymas",
    "emmanuel", "emmaus", "enan", "endor", "enoch", "enos", "ephah",
    "epher", "ephraim", "ephron", "epaphras", "epaphroditus", "erastus",
    "esau", "esarhaddon", "esek", "eshcol", "esli", "etam", "ethan",
    "ethbaal", "eubulus", "eunice", "euphrates", "eutychus", "evi",
    "ezbon", "ezekias", "ezer", "ezra", "felix", "festus", "fortunatus",
    "gaal", "gaash", "gabbatha", "gabriel", "gad", "gadara", "gaham",
    "gaius", "galatia", "galeed", "gallim", "gallio", "gamaliel", "gareb",
    "gath", "gaza", "geba", "gebal", "gedaliah", "gehazi", "gennesaret",
    "gera", "gerar", "gershom", "gershon", "geshem", "geshur",
    "gethsemane", "gezer", "gibeah", "gibeon", "gihon", "gilboa", "gilead",
    "gilgal", "girgashite", "golan", "golgotha", "goliath", "gomer",
    "gomorrah", "goshen", "gozan", "hachilah", "hadad", "hadar",
    "hadassah", "hadoram", "hagab", "hagar", "haggai", "haggith", "ham",
    "haman", "hamath", "hamor", "hamutal", "hanamel", "hanan", "hananiah",
    "hannah", "hanun", "haran", "harbona", "harim", "havilah", "hazael",
    "hazor", "heber", "hebron", "helah", "heli", "heman", "hena",
    "hepher", "hermas", "hermes", "hermogenes", "hermon", "herod",
    "herodias", "herodion", "heshbon", "hezekiah", "hezron", "hiel",
    "hilkiah", "hinnom", "hiram", "hittite", "hivite", "hobab", "hophni",
    "hor", "horeb", "hori", "hosah", "hoshea", "huldah", "hur", "hushai",
    "hymenaeus", "ibzan", "ichabod", "iconium", "iddo", "igal", "illyricum",
    "immanuel", "iram", "isaiah", "iscariot", "ishbosheth", "ishmael",
    "israel", "issachar", "ithamar", "ittai", "izhar", "jaakan", "jabal",
    "jabbok", "jabesh", "jabin", "jachin", "jael", "jahaz", "jair",
    "jairus", "jambres", "jamin", "janna", "jannes", "japheth", "jared",
    "jashen", "jason", "javan", "jecoliah", "jeconiah", "jedidah",
    "jeduthun", "jehiel", "jehoahaz", "jehoash", "jehohanan", "jehoiachin",
    "jehoiada", "jehoiakim", "jehonadab", "jehoram", "jehoshaphat",
    "jehosheba", "jehovah", "jehu", "jehudi", "jekuthiel", "jemima",
    "jephthah", "jephunneh", "jerahmeel", "jered", "jeremoth", "jericho",
    "jeroboam", "jerubbaal", "jesse", "jethro", "jezebel", "jezreel",
    "joab", "joanna", "joash", "jochebed", "joel", "joha", "johanan",
    "jokim", "joktan", "jonadab", "jonathan", "joppa", "jorah", "joram",
    "jordan", "joses", "josiah", "jotham", "jubal", "judas", "jude",
    "julia", "julius", "junia", "justus", "kadesh", "kanah", "kedar",
    "kedesh", "keilah", "kemuel", "kenaz", "kenite", "kerioth", "keturah",
    "kezia", "kidron", "kir", "kish", "kishon", "kittim", "kohath",
    "korah", "kore", "laban", "lachish", "ladan", "lael", "laish",
    "lamech", "laodicea", "lasea", "lazarus", "lebanon", "lebbaeus",
    "lehi", "lemuel", "levi", "libnah", "libni", "libya", "linus",
    "lois", "lot", "lotan", "luke", "luz", "lycaonia", "lycia", "lydda",
    "lydia", "lysanias", "lysias", "lystra", "maacah", "maaseiah",
    "macedonia", "machir", "machpelah", "madai", "magdala", "magog",
    "mahalath", "mahanaim", "malachi", "malchiel", "malchijah", "malchus",
    "mamre", "manaen", "manasseh", "manoah", "maon", "mara", "marah",
    "mareshah", "martha", "mash", "mattan", "mattaniah", "mattatha",
    "mattathias", "matthan", "matthat", "matthias", "mede", "medad",
    "media", "megiddo", "melchi", "melchizedek", "melea", "memphis",
    "menahem", "mephibosheth", "merab", "merari", "meribah", "merom",
    "mesha", "meshach", "meshech", "meshullam", "mesopotamia", "micaiah",
    "michael", "michal", "michmash", "midian", "miletus", "milcah",
    "miriam", "mishael", "mizpah", "mizraim", "moladah", "molech",
    "mordecai", "moreh", "moriah", "mushi", "myra", "mysia", "naam",
    "naaman", "naarah", "nabal", "naboth", "nachor", "nadab", "nahash",
    "nahor", "nahshon", "nahum", "naomi", "naphtali", "narcissus",
    "nathan", "nathanael", "neapolis", "nebaioth", "nebat", "nebo",
    "nebuchadnezzar", "nebuzaradan", "necho", "nehemiah", "neriah",
    "nethanel", "nicanor", "nicodemus", "nicolas", "nicopolis", "niger",
    "nile", "nimrod", "nimshi", "nineveh", "noadiah", "nob", "nun",
    "obadiah", "obal", "obed", "og", "omar", "omri", "on", "onam", "onan",
    "onesimus", "onesiphorus", "ono", "ophir", "ophrah", "oreb", "oren",
    "orpah", "othniel", "palti", "paphos", "parmenas", "parvaim",
    "pashhur", "patara", "pathros", "patmos", "patrobas", "pekah",
    "pekahiah", "peleg", "peniel", "penuel", "perez", "perga", "pergamos",
    "pethor", "phalti", "pharaoh", "philadelphia", "philemon", "philetus",
    "philip", "philistia", "phinehas", "phlegon", "phoebe", "phoenicia",
    "phrygia", "pilate", "piram", "pisgah", "pisidia", "pithom", "pontius",
    "pontus", "potiphar", "priscilla", "prochorus", "ptolemais", "publius",
    "put", "puteoli", "quartus", "rabbah", "rabshakeh", "rachel",
    "raguel", "rahab", "ram", "rameses", "ramoth", "rapha", "reba",
    "rebekah", "rechab", "regem", "rehob", "rehoboam", "rehoboth",
    "rehum", "rekem", "remaliah", "rephaim", "rephidim", "resen", "reu",
    "reuben", "reuel", "rezin", "rezon", "rhesa", "rhoda", "rhodes",
    "riblah", "rimmon", "rissah", "rizpah", "rufus", "ruhamah", "sabta",
    "salamis", "salecah", "salem", "sallu", "salma", "salmon", "salome",
    "samgar", "samos", "sanballat", "sarah", "sardis", "sargon", "saruch",
    "sceva", "sebat", "secundus", "segub", "seir", "sela", "seleucia",
    "senaah", "sennacherib", "sergius", "seth", "shadrach", "shallum",
    "shalmaneser", "shamgar", "shammah", "shaphan", "sharon", "sheba",
    "shebna", "shechem", "shelah", "shem", "shemaiah", "sheol",
    "shephatiah", "shesh", "sheshan", "shibboleth", "shiloh", "shimea",
    "shimei", "shinar", "shishak", "shittim", "shobab", "shobal",
    "shua", "shuah", "shulammite", "shunammite", "shunem", "shur",
    "shushan", "sidon", "sihon", "silas", "silvanus", "simeon", "simon",
    "sisera", "smyrna", "socho", "sodom", "sopater", "sosthenes",
    "succoth", "susanna", "sychar", "syene", "syntyche", "syracuse",
    "taanach", "tabeal", "tabitha", "tabor", "tadmor", "talmai", "tamar",
    "tarshish", "tarsus", "tekoa", "tema", "teman", "terah", "tertius",
    "tertullus", "thaddaeus", "thebez", "theophilus", "theudas", "thomas",
    "thyatira", "tiberias", "tiberius", "tibni", "tidal", "tigris",
    "timaeus", "timna", "timon", "timotheus", "timothy", "tirhakah",
    "tirzah", "titus", "tob", "tobiah", "togarmah", "tola", "trachonitis",
    "troas", "trophimus", "tryphena", "tryphosa", "tubal", "tychicus",
    "tyrannus", "tyre", "ucal", "uel", "uphaz", "ur", "uri", "uriah",
    "uriel", "uz", "uzza", "uzzah", "uzzi", "uzziah", "uzziel", "vashti",
    "zaccai", "zacchaeus", "zacharias", "zadok", "zalmon", "zalmunna",
    "zarephath", "zattu", "zebadiah", "zebah", "zebedee", "zebul",
    "zebulun", "zechariah", "zedekiah", "zelah", "zelophehad", "zenas",
    "zephaniah", "zephath", "zerah", "zeresh", "zerubbabel", "zeruiah",
    "zibeon", "zichri", "ziklag", "zilpah", "zimran", "zimri", "zion",
    "ziph", "zipporah", "zoan", "zoar", "zobah", "zophar", "zorah",
    "zuar", "zuph",
}

# generic vocabulary: light/reporting verbs, bare physical actions, and
# neutral nouns that carry no inner-being content standing alone - the
# single biggest real coverage gap found by inspecting the "Could impact
# IB" bucket on the whole-Bible span/term reconciliation (2026-07-24): common
# words like "come", "take", "man", "nothing" were falling through to the
# uncertain default only because no wordlist covered them, not because they
# are genuinely ambiguous.
GENERIC_VERB_WORDS = {
    "come", "go", "take", "bring", "brought", "took", "went", "came",
    "gone", "put", "make", "made", "give", "gave", "given", "send", "sent",
    "say", "said", "eat", "ate", "eaten", "drink", "drank", "drunk", "see",
    "saw", "seen", "set", "leave", "left", "return", "returned", "open",
    "opened", "destroy", "destroyed", "spread", "appoint", "appointed",
    "taken", "stand", "stood", "sit", "sat", "walk", "walked", "run", "ran",
    "lie", "lay", "lain", "pass", "passed", "turn", "turned", "cut", "build",
    "built", "buy", "bought", "sell", "sold", "carry", "carried", "throw",
    "threw", "thrown", "pour", "poured", "gather", "gathered", "divide",
    "divided", "count", "counted", "measure", "measured", "fall", "fell",
    "fallen", "speak", "spoke", "spoken", "tell", "told", "keep", "kept",
    "dwell", "dwelt", "live", "lived", "command", "commanded", "offer",
    "offered", "kill", "killed", "do", "did", "done", "call", "called",
}

GENERIC_NOUN_WORDS = {
    "man", "men", "woman", "women", "people", "thing", "things", "place",
    "time", "day", "days", "way", "side", "child", "children", "food",
    "fire", "light", "rest", "end", "part", "number", "name", "word",
    "words", "sign", "work", "works", "matter", "case", "form", "kind",
    "portion", "amount", "measure", "distance", "height", "width", "length",
    "earth", "year", "years", "night", "nights", "morning", "evening",
}

QUANTIFIER_INDEFINITE_WORDS = {
    "nothing", "anything", "anyone", "everyone", "everybody", "somebody",
    "whoever", "whatever", "whichever", "none", "nobody", "something",
}

# generic descriptive adjectives - neutral size/age/quantity descriptors
# that carry no inner-being content standing alone (found via the same
# bucket inspection as GENERIC_VERB_WORDS)
GENERIC_ADJECTIVE_WORDS = {
    "great", "young", "old", "full", "little", "small", "large", "big",
    "short", "long", "new", "high", "low", "deep", "wide", "narrow",
    "broad", "whole", "entire", "total", "certain", "various", "plain",
    "common", "empty", "heavy", "light",
}

NOT_RELEVANT_WORDS = (
    CONCRETE_OBJECT_WORDS
    | PLANT_ANIMAL_WORDS
    | LITERAL_BODY_PART_WORDS
    | KINSHIP_SOCIAL_WORDS
    | NUMBER_WORDS
    | UNIT_OF_MEASURE_WORDS
    | PROPER_NAME_WORDS
    | GENERIC_VERB_WORDS
    | GENERIC_NOUN_WORDS
    | GENERIC_ADJECTIVE_WORDS
    | QUANTIFIER_INDEFINITE_WORDS
)

# body-part words that are ALSO standing Hebrew idiom for the inner being -
# deliberately excluded from NOT_RELEVANT_WORDS above so they fall through
# to the "Could impact IB" default instead of a confident "Not relevant".
BODY_PART_IDIOM_WORDS = {"heart", "bowels", "kidneys", "reins", "liver", "belly", "gut",
                          "breast", "bosom", "flesh", "blood"}

# function words - a term made up ENTIRELY of these (e.g. "each other", "for
# his own") is a pure grammatical fragment, not lexical content.
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "for", "of", "to", "in", "on",
    "at", "by", "with", "from", "that", "this", "these", "those", "each",
    "other", "is", "are", "was", "were", "be", "been", "being", "as", "if",
    "so", "than", "then", "when", "where", "which", "who", "whom", "whose",
    "what", "it", "its", "he", "she", "they", "them", "his", "her", "their",
    "our", "your", "my", "i", "you", "we", "not", "no", "do", "does", "did",
    "have", "has", "had", "will", "would", "shall", "should", "can",
    "could", "may", "might", "must", "upon", "unto", "into", "out", "up",
    "down", "over", "under", "again", "further", "once", "all", "any",
    "both", "few", "more", "most", "some", "such", "only", "own", "same",
    "too", "very", "just", "also", "even", "still", "yet", "thus", "hence",
    "therefore", "because", "since", "while", "although", "though",
    "whereas", "however", "s",
    # spatial/temporal prepositions and discourse fillers, missing from the
    # original list (found via the same "Could impact IB" bucket inspection
    # noted at GENERIC_VERB_WORDS above)
    "before", "after", "among", "between", "without", "against", "near",
    "far", "beside", "besides", "beyond", "through", "throughout", "during",
    "until", "till", "above", "below", "behind", "ahead", "away", "off",
    "along", "across", "around", "toward", "towards", "within", "amid",
    "amidst", "amongst", "together", "now", "here", "there", "surely",
    "behold", "why", "how", "about", "yea", "lo", "indeed", "verily",
    "me", "him", "us", "another", "never", "ever", "soon", "forever",
    "except", "nor", "whether", "either", "neither", "each",
}

SUFFIXES = (
    "ations", "ation", "ingly", "fully", "lessness", "ness", "ment",
    "tion", "sion", "ings", "edly", "ing", "ed", "es", "ly", "ful",
    "less", "er", "est", "s",
)


def _normalize(word):
    # curly quotes (STEP renders possessives with a Unicode right single
    # quote, e.g. "aaron’s" - some viewers show that as mojibake, but
    # it's a real character, not corruption) normalized to straight ones
    # first, so both the punctuation-strip below AND the trailing-'s strip
    # actually catch it
    word = word.lower().replace("‘", "'").replace("’", "'")
    word = word.strip(".,;:!?'\"()[]{}-")
    if word.endswith("'s"):
        word = word[:-2]
    return word


def _word_matches(word, wordset):
    if word in wordset:
        return True
    for suf in SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 3 and word[: -len(suf)] in wordset:
            return True
    return False


HYPHENATED_PLACE_NAME_PREFIXES = (
    "abel", "beth", "kiriath", "kirjath", "baal", "ramoth", "gath", "hazar",
    "hazor", "kir", "en", "beer",
)


def classify_ib_relevance(term):
    # a token with 2+ internal hyphens is almost never an ordinary English
    # lexicon gloss - it's the standard shape of a compound biblical place
    # name (e.g. "abel-beth-maacah", "kiriath-jearim", "baal-perazim") that
    # PROPER_NAME_WORDS (a bounded list, not exhaustive - the Bible has
    # thousands of minor names) will never fully enumerate. A single hyphen
    # is ambiguous on its own (real English compounds like "self-control"
    # exist) UNLESS the first segment is a recognized Hebrew place-name
    # element (e.g. "abel-shittim", "beth-shemesh") - real English lexicon
    # glosses never start with one of these.
    stripped_term = term.strip()
    if re.fullmatch(r"[A-Za-z]+(-[A-Za-z]+){2,}", stripped_term):
        return "Not relevant"
    hyphen_match = re.fullmatch(r"([A-Za-z]+)-[A-Za-z]+", stripped_term)
    if hyphen_match and hyphen_match.group(1).lower() in HYPHENATED_PLACE_NAME_PREFIXES:
        return "Not relevant"

    tokens = [_normalize(w) for w in re.split(r"[\s]+", term) if _normalize(w)]
    # drop stray non-alphabetic junk (e.g. a lone "^" left over from upstream
    # HTML/markup stripping) - it is not lexical content either way
    tokens = [t for t in tokens if re.search(r"[a-z]", t)]
    if not tokens:
        return "Not relevant"

    content_tokens = [t for t in tokens if t not in STOPWORDS]
    if not content_tokens:
        return "Not relevant"  # pure grammatical fragment

    if any(_word_matches(t, IB_RELATED_WORDS) for t in content_tokens):
        return "IB related"

    if all(
        _word_matches(t, NOT_RELEVANT_WORDS) and not _word_matches(t, BODY_PART_IDIOM_WORDS)
        for t in content_tokens
    ):
        return "Not relevant"

    return "Could impact IB"
