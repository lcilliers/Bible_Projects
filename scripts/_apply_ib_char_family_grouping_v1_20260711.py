"""Group the 877 meaning-records (ib_characteristic, book 19) into <=50 semantic
FAMILIES by similarity, writing the `family` column.

Method: an ordered, transparent keyword->family rule map (first match wins),
tested against the record NAME first, then gloss+operation as fallback. Every
assignment is auditable (the matched family is deterministic from the rules).
Errs toward leaving a meaning in 'other-uncategorised' rather than forcing it —
the residual is reported for read-back and rule refinement.

Usage:  python scripts/_apply_ib_char_family_grouping_v1_20260711.py [--live]
        (default = dry run: prints distribution + unmatched, writes nothing)
"""
import sqlite3, os, re, sys, json
from collections import Counter, defaultdict

LIVE = '--live' in sys.argv
DB = os.path.join('database','bible_research.db')
c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; cur = c.cursor()

# ordered (family, regex). First family whose regex hits the NAME wins;
# if none, the same rules are tried against gloss+operation.
RULES = [
 # --- seats / constitution ---
 ('inner-seat-heart-soul-spirit', r'\b(soul|heart|spirit|inward|inmost|bowel|kidney|reins|bosom|breast|flesh\b|my being|inner)'),
 # --- Godward positive ---
 ('trust-refuge-security',        r'\b(trust|refuge|rely|relied|lean|confidence|confiden|secur|shelter|shield me|stronghold|rock\b|fortress|take.?refuge)'),
 ('hope-waiting',                 r'\b(hope|wait|await|expect|look for|long.?for the lord)'),
 ('fear-of-god-awe',              r'\b(fear|afraid|dread|terror|tremble|trembl|awe|reveren|revere|stand in awe)'),
 ('worship-prostration-service',  r'\b(worship|bow|prostrat|kneel|homage|serv|minister|fall down before)'),
 ('praise-extol-sing',           r'\b(praise|extol|exalt|ascrib|magnif|glorif|glory\b|laud|hallelu|sing|song|melod|psalm|make music|shout for joy|shout aloud)'),
 ('thanksgiving',                 r'\b(thank|thanksgiv|give.?you.?thanks)'),
 ('blessing-benediction',        r'\b(bless|blessed|blessing)'),
 ('joy-gladness',                 r'\b(joy|glad|rejoic|exult|jubil|mirth|cheer|delight in the lord|be merry)'),
 ('faith-faithfulness-truth',     r'\b(faith|believ|faithful|truth|trustworth)'),
 ('love-devotion',                r'\b(love|beloved|cleave|clung|devot|affection)'),
 ('grace-mercy-compassion',       r'\b(grace|gracious|merc|compassion|pity|generous|loyal love|kindness)'),
 ('desire-longing-appetite',      r'\b(desire|crav|long\b|longs|longing|thirst|hunger|hungr|pant|appetite|pleasure|yearn|covet|delight|zeal|jealous|\black|\bwant|\bneed)'),
 # --- petition / communion ---
 ('prayer-petition-crying-out',   r'\b(pray|prayer|plea|plead|supplicat|cry|cries|cried|call|beseech|entreat|petition|complain|complaint|pour out|groan.*before)'),
 ('being-heard-listening',        r'\b(hear|listen|hearken|give ear|incline.*ear|answer|attend to my|regard my)'),
 # --- mind ---
 ('knowing-understanding',        r'\b(know|understand|discern|consider|perceiv|ponder|meditat|mind\b|think|thought|regard|reflect|comprehend)'),
 ('wisdom-folly-teaching',        r'\b(wise|wisdom|folly|fool|prudent|instruct|teach|learn|counsel|disciplin|understanding heart|simple\b|stupid|brutish|senseless|dull)'),
 ('memory-remembrance',           r'\b(remember|forget|mindful|recall|memory|call to mind|bring to remembrance)'),
 # --- speech ---
 ('speech-mouth-tongue',          r'\b(speak|speech|say\b|said|mouth|tongue|lips|declare|tell|utter|proclaim|talk|word of my|recount|boast in god)'),
 # --- conduct / obedience ---
 ('walk-way-conduct',             r'\b(walk|way\b|ways\b|path|go\b|goes|went|run\b|follow|step|tread|conduct|journey|wander|stray|astray|flee)'),
 ('keeping-guarding-vigilance',   r'\b(keep|guard|watch|observ|preserv|heed|attend|vigil)'),
 ('torah-obedience-word',         r'\b(obey|obedien|command|statute|\blaw\b|precept|ordinance|testimon|decree|keep your word|your word)'),
 ('righteousness-integrity',      r'\b(righteous|upright|blameless|integrity|pure|clean|innocen|honest|just\b|justice|perfect way)'),
 # --- the other side (descent / against) ---
 ('sin-guilt-iniquity',           r'\b(sin\b|sins|sinn|iniquit|transgress|guilt|guilty|trespass|wrongdoing|pollut|unclean|defile|impur)'),
 ('shame-confusion',              r'\b(shame|asham|confound|confus|disgrace|reproach|dishonou|scorn.*me|humiliat)'),
 ('confession-forgiveness',       r'\b(confess|forgiv|pardon|atone|blot out|cleanse me|wash me)'),
 ('rebellion-stubbornness',       r'\b(rebel|stubborn|stiff.?neck|obstinat|refus|spurn|reject|despis|forsake)'),
 ('wickedness-ungodliness',       r'\b(wicked|evil|ungodly|godless|worthless|vile|abomin)'),
 ('malice-enmity-persecution',    r'\b(hate|hated|hatr|enem|foe|advers|oppress|persecut|ambush|lurk|plot|scheme|devise.*evil|snare|pursue|assail|accus|oppose|curse|rise against|surround me)'),
 ('pride-arrogance-scoffing',     r'\b(pride|proud|arrogan|haughty|boast|boastful|scoff|mock|deride|derid|taunt|presumptuous|insolent|lofty|exalt themselves|exalt himself)'),
 ('deceit-falsehood',             r'\b(deceit|deceiv|lie\b|lies|lying|false|flatter|guile|treacher|hypocri|slander|betray)'),
 ('anger-wrath-vexation',         r'\b(anger|angry|wrath|rage|fury|furious|fierce|indignat|provoke|vex|fret|hot displeasure)'),
 ('violence-cruelty',             r'\b(violen|cruel|blood|destroy|devour|crush|oppression|ruthless|kill|slay|attack|conspire|contention|strife|fight|band together)'),
 # --- posture / state ---
 ('humility-lowliness-contrition',r'\b(humble|humbl|lowly|meek|contrite|broken|brokenhearted|poor\b|needy|bowed|submit|afflicted self)'),
 ('rest-stillness-peace',         r'\b(rest\b|resteth|still|quiet|peace|calm|silen|repose|be at ease|tranquil)'),
 ('strength-courage-steadfastness',r'\b(strength|strong|courage|might|power|valou|bold|firm|steadfast|establish|uphold|stand fast|not be moved|fortitude)'),
 ('faint-despair-languishing',    r'\b(faint|melt|languish|downcast|disquiet|overwhelm|despair|fail\b|weary|pine|consumed|waste away|sink|feeble|distress|troubled|anguish|dismay|afflict|suffer|wither|\bpain)'),
 ('grief-lament-sorrow',          r'\b(grief|griev|mourn|weep|wept|tears|groan|sigh|lament|sorrow|misery|woe|bitter|heavy|sad)'),
 # --- movement / turning ---
 ('turning-repentance',           r'\b(turn|return|repent|backslid|convert|come back)'),
 ('restoration-revival-satisfaction',r'\b(restor|reviv|renew|heal|satisf|refresh|redeem|rescue|deliver|save|help\b|comfort|consol|sustain me|lift me from)'),
 ('seeking-inquiring',            r'\b(seek|sought|inquir|search for you|resort|consult|require)'),
 ('lifting-bearing',              r'\b(lift|bear|bore|carry|carried|rais|sustain|uphold|support|hold up)'),
 ('will-resolve-vow-intent',      r'\b(resolv|purpose|intent|inclin|set (my|his) heart|determin|devise|plan|plot|\bwill\b|vow|pledge|dedicate|choos|choose|chose|prefer|perform|\bpay\b|fulfil|render|offer|commit my)'),
 ('being-searched-tested-by-god', r'\b(search me|try me|test|tried|proof|examine|prove|know my heart|refine)'),
 ('entrustment-committing',       r'\b(entrust|commit (my|your way)|cast (your|my)|roll (your|my)|leave it to)'),
 ('life-death-vitality',          r'\b(life|live\b|living|death|die\b|dead|grave|pit\b|sheol|perish|breath of life)'),
 ('light-darkness-inner',         r'\b(light|dark|gloom|shadow|lamp)'),
]

rows = cur.execute("SELECT id,name,instance_count,operation,lexical_gloss FROM ib_characteristic WHERE book_scope='19'").fetchall()

def classify(r):
    name = (r['name'] or '').lower()
    for fam, pat in RULES:
        if re.search(pat, name): return fam
    blob = f"{r['lexical_gloss'] or ''} || {r['operation'] or ''}".lower()
    for fam, pat in RULES:
        if re.search(pat, blob): return fam
    return 'other-uncategorised'

assign = {r['id']: classify(r) for r in rows}
fam_rec = Counter(assign.values())
fam_inst = defaultdict(int)
for r in rows: fam_inst[assign[r['id']]] += r['instance_count']

print(f"Records: {len(rows)}  |  Families: {len(fam_rec)}  (cap 50)")
print(f"{'family':40} {'recs':>5} {'inst':>6}")
for fam,_ in sorted(fam_rec.items(), key=lambda kv:-fam_inst[kv[0]]):
    print(f"  {fam:38} {fam_rec[fam]:5} {fam_inst[fam]:6}")

unм = [r for r in rows if assign[r['id']]=='other-uncategorised']
print(f"\nUNMATCHED ('other'): {len(unм)} records, {sum(r['instance_count'] for r in unм)} inst")
print("  heaviest unmatched (fix rules for these first):")
for r in sorted(unм, key=lambda r:-r['instance_count'])[:35]:
    print(f"    {r['instance_count']:>2}  {r['name'][:26]:26} | gloss={str(r['lexical_gloss'])[:30]}")

if LIVE:
    cur.executemany("UPDATE ib_characteristic SET family=? WHERE id=?",
                    [(assign[r['id']], r['id']) for r in rows])
    c.commit()
    print(f"\nLIVE: wrote family on {len(rows)} records; {len(fam_rec)} families.")
else:
    print("\n[dry run] no writes. --live to apply.")
