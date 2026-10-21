"""Extend the `characteristic` baseline (199 rows, 17 clusters) to the Ps/Pro-raised
clusters it skipped. Researcher direction (2026-07-03): the baseline was built on the
emotion/moral clusters (M01-M11, M15, M20, M26, M38, M39, M46); Psalms+Proverbs (prayer
+ wisdom) foreground the Godward-relational clusters (praise M22, trust M19, hope M18,
peace M33, faithfulness M13, memory M41, strength M23, desire M28, the seat M47, ...)
that were never characteristic-mapped. Extend, CHECKED and GROWING as we go; over-split
is fine now (consolidation deferred - 'they may be the same thing, but not now').

Fine-grained characteristics grounded in Ps/Pro (name + distinguishing definition, in
the baseline's style). Idempotent by (cluster_code, short_name). source marks provenance.
"""
import sqlite3, os
from datetime import datetime, timezone
DB=os.path.join('database','bible_research.db')
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
SRC='ps-pro-baseline-extension-v1-20260703'
NOTE='Extension from Psalms+Proverbs; checked+growing; consolidation deferred.'

# (cluster_code, short_name, definition)
C=[
 # M22 — Praise / Thanksgiving / Glory (the praising, grateful self)
 ("M22","Praise / extolling","The inner being lifting God in declared, public praise - extolling his name and greatness (Ps 145:1-3; 150). The self magnifies its object; praise is the terminus the Psalter moves toward (150:6)."),
 ("M22","Thanksgiving / gratitude","The grateful response to God's benefits - a reckoning of what has been received and a moved impulse to render something back ('what shall I render for all his benefits', Ps 116:12; 100:4; 'forget not all his benefits', 103:2)."),
 ("M22","Blessing God (self-roused)","The self blessing the LORD, mustering its whole interior to do so - 'Bless the LORD, O my soul, and all that is within me' (Ps 103:1; 104:1; 34:1). A self-address in the rousing register."),
 ("M22","The new song","Fresh praise called forth by a fresh divine act - a NEW song because God has done something new (Ps 33:3; 40:3; 96:1; 98:1)."),
 ("M22","Glorying / boasting in God","Confidence expressed as boast in the LORD rather than the self ('my soul makes its boast in the LORD', Ps 34:2; 44:8) - and its deflected form, 'not to us but to your name give glory' (115:1)."),
 ("M22","Recounting God's deeds","Declaring and rehearsing God's works as praise - telling the next generation (Ps 9:1; 78:4; 145:4). Junctions memory (M41)."),
 ("M22","Whole-hearted praise","Praise offered with the entire self engaged, undivided - 'I will give thanks with my whole heart' (Ps 9:1; 111:1; 138:1)."),
 # M19 — Trust / Refuge
 ("M19","Taking refuge / sheltering","The self fleeing into God as into a rock, tower, fortress, or shadowing wings - a spatial hiding for safety (Ps 31:1; 91:1-4; Pro 18:10)."),
 ("M19","Trust as leaning / reliance","Leaning the self's whole weight on God rather than on its own resources - 'trust in the LORD with all your heart' (Pro 3:5; Ps 37:5)."),
 ("M19","Trust as self-distrust","Trust constituted negatively - the refusal to lean on one's own understanding, riches, or mind ('do not lean on your own understanding', Pro 3:5; 28:26; Ps 44:6)."),
 ("M19","Trust as deliberate valuation","A reasoned ranking that chooses God over every human recourse - 'better to take refuge in the LORD than to trust in man' (Ps 118:8-9; 146:3)."),
 ("M19","Mis-placed trust (foil)","Trust aimed wrong, which topples the self - in riches (Pro 11:28; Ps 52:7), princes (146:3), idols that deaden their trusters (115:8), or the self."),
 ("M19","Trust yielding immovable stability","Trust that confers rock-like fixity on the self - 'those who trust in the LORD are like Mount Zion, which cannot be moved' (Ps 125:1; 112:7; 16:8)."),
 ("M19","Trust constituted from birth","Trust as original, not first chosen - the self cast on God from the womb (Ps 22:9-10; 71:5-6)."),
 # M18 — Hope / Waiting
 ("M18","Waiting on the LORD","The self held taut and expectant toward God under delay - 'my soul waits for the LORD more than watchmen for the morning' (Ps 130:5-6; 27:14; 40:1)."),
 ("M18","Silent / still waiting","Waiting held in stillness before God - 'for God alone, O my soul, wait in silence' (Ps 62:1,5)."),
 ("M18","Hope grounded in the word","Hope with a ground - expectation resting on God's promise/word rather than wish ('in his word I hope', Ps 130:5; 119:49,74,81)."),
 ("M18","Hope deferred (the sickened heart)","The wound of unmet longing - 'hope deferred makes the heart sick' (Pro 13:12). Waiting registers as a felt ache."),
 ("M18","Hope fulfilled","The granted longing as life - 'a desire fulfilled is a tree of life... sweet to the soul' (Pro 13:12,19)."),
 ("M18","Hope of the afflicted / poor","Hope as the endurance-posture of the oppressed who cannot secure their own justice (Ps 9:18; 62:5)."),
 # M33 — Peace / Stillness / Rest
 ("M33","Peace / wholeness (shalom)","Inner and relational well-being and completeness - the settled soundness God gives (Ps 4:8; 29:11; 85:8; Pro 3:17)."),
 ("M33","Stillness / being quieted","The soul brought to silence and calm - 'I have calmed and quieted my soul' (Ps 131:2; 62:1; 'be still, and know', 46:10)."),
 ("M33","Rest / repose","The settledness that reposes - led beside the waters of rest, the soul returned to its rest (Ps 23:2 menuchah; 116:7)."),
 ("M33","Fearless / sweet sleep","Sleep as the bodily proof of a self at rest in God - 'in peace I will both lie down and sleep' (Ps 3:5; 4:8; Pro 3:24)."),
 ("M33","Security / dwelling unafraid","The self dwelling safe and without dread (Ps 4:8; 16:9; Pro 1:33 'dwell secure, without dread')."),
 ("M33","Contentment","The inner good that outvalues abundance - 'better a little with the fear of the LORD than great treasure with trouble' (Pro 15:16-17); the weaned soul past craving (Ps 131:2)."),
 # M13 — Faithfulness / Fidelity
 ("M13","Faithfulness / steadfastness","The reliable, constant inner being - firmness that endures ('a faithful man who can find?', Pro 20:6; Ps 40:10)."),
 ("M13","Fidelity / loyal-love (human chesed)","Steadfast loyalty prized in a person - 'what is desired in a man is steadfast love' (Pro 19:22); loyalty kept in relationship."),
 ("M13","Keeping faith / one's word","Holding to one's oath/covenant even at cost - 'who swears to his own hurt and does not change' (Ps 15:4); its failure, 'not faithful to his covenant' (78:37)."),
 ("M13","Trustworthiness / reliability","Being one who can be relied on - the faithful envoy/messenger, the trustworthy-in-spirit who keeps a confidence (Pro 11:13; 13:17; 25:13)."),
 ("M13","Faithlessness / treachery (foil)","Covenant-breaking, the treacherous heart - unreliability that betrays (Ps 78:57; Pro 11:3,6; 25:19)."),
 # M41 — Memory / Attention
 ("M41","Willed remembering","The self deliberately recollecting God's works as a discipline against despair - 'I will remember the deeds of the LORD' (Ps 77:11; 143:5)."),
 ("M41","Memory guarded by vow","Binding oneself, on pain of self-curse, never to forget what one loves - 'if I forget you, O Jerusalem...' (Ps 137:5-6)."),
 ("M41","Forgetting (foil)","The lapse of memory as the seedbed of rebellion and infidelity - 'they soon forgot his works' (Ps 106:13); 'forget not all his benefits' (103:2); the woman who 'forgets the covenant of her God' (Pro 2:17)."),
 ("M41","Resting on God's remembering","The self's security in being held in God's memory - 'he does not forget the cry of the afflicted' (Ps 9:12); 'he remembered his covenant' (105:8; 106:45)."),
 ("M41","Attention / inclining the ear","The receptive self bending toward instruction - 'make your ear attentive... incline your heart' (Pro 2:2; 4:20; 22:17). Junctions teachability."),
 # M23 — Strength / Courage
 ("M23","Inner strength (God-given)","The self's might understood as received from God - 'you increased my strength of soul' (Ps 138:3; 18:32; 28:7 'the LORD is my strength')."),
 ("M23","Courage / taking heart","The self exhorted to summon inner courage - 'be strong, and let your heart take courage' (Ps 27:14; 31:24)."),
 ("M23","Being upheld / sustained","The self held up and carried by God - 'the LORD sustained me' (Ps 3:5; 55:22; 'your right hand upholds me', 63:8)."),
 ("M23","Fainting / failing strength (foil)","The collapse that measures the self's true strength - 'if you faint in the day of adversity, your strength is small' (Pro 24:10; 'my flesh and my heart may fail', Ps 73:26)."),
 ("M23","Boldness","The clear-conscience confidence that fears nothing - 'the righteous are bold as a lion' (Pro 28:1)."),
 # M28 — Desire / Longing / Appetite
 ("M28","Longing / thirst for God","The Godward want at the pitch of bodily need - 'my soul thirsts for God... in a dry and weary land' (Ps 42:1-2; 63:1; 143:6)."),
 ("M28","Delight","Settled desire in its restful mode - taking pleasure in the LORD and his law (Ps 1:2; 37:4; 119); wisdom prized above all desire (Pro 3:15)."),
 ("M28","Craving / disordered appetite (foil)","Desire aimed low that devours its owner - the wanton craving that tests God to ruin (Ps 106:14) or kills the sluggard (Pro 21:25)."),
 ("M28","The insatiable","Appetite with no natural floor - 'never satisfied are the eyes of man'; the leech's 'Give, Give' (Pro 27:20; 30:15-16)."),
 ("M28","Satisfied desire","The appetite answered at God's hand - 'he satisfies the longing soul'; 'you open your hand and satisfy the desire of every living thing' (Ps 107:9; 145:16)."),
 ("M28","Weaned / transcended desire","The soul content past the fretful demand - 'like a weaned child... is my soul within me' (Ps 131:2)."),
 ("M28","Consolidated desire (the one thing)","The scattered wants gathered onto a single object - 'one thing I have asked... to gaze on the beauty of the LORD' (Ps 27:4; 73:25)."),
 # M12 — Purity / Blamelessness
 ("M12","Purity of heart","The clean inner being - a heart washed and undefiled, loved as such ('who loves purity of heart', Pro 22:11; Ps 24:4; 51:10 'create in me a clean heart')."),
 ("M12","Blamelessness / integrity of walk","The whole, upright way of life held consistent inside and out (Ps 15:2; 101:2; Pro 2:7; 11:5)."),
 ("M12","Innocence / clean hands","Freedom from guilt in act and intent - 'I wash my hands in innocence' (Ps 26:6; 73:13)."),
 ("M12","The un-self-cleansable heart","The limit of self-purification - 'who can say, I have made my heart pure?' (Pro 20:9); the heart must be MADE clean (Ps 51:10). Junctions forgiveness."),
 # M30 — Keeping / Guarding
 ("M30","Guarding the heart","Keeping vigilant watch over the heart as the source of the whole life - 'keep your heart with all vigilance, for from it flow the springs of life' (Pro 4:23)."),
 ("M30","Keeping the way / commandments","Holding to God's path and word - 'I have kept your law', 'guarding it according to your word' (Ps 119:9,34; Pro 2:8)."),
 ("M30","Being kept by God","The self resting in being guarded by an unsleeping keeper (Ps 121:3-8; 91)."),
 ("M30","Guarding the gates (mouth/eyes/feet)","Keeping watch over the outlets through which the heart acts - 'set a guard over my mouth'; the eyes forward, the feet pondered (Ps 141:3; Pro 4:24-27)."),
 # M25 — Life / Vitality
 ("M25","Life / vitality","The living, animate self and its source - 'with you is the fountain of life' (Ps 36:9); wisdom/fear as 'a fountain of life' (Pro 14:27; 4:23)."),
 ("M25","Revival / being revived","The flagging or dead-feeling self brought back to life - 'he restores my soul'; 'give me life according to your word' (Ps 23:3; 71:20; 119:25)."),
 ("M25","Renewal","The self's vitality remade, not merely maintained - 'your youth is renewed like the eagle's' (Ps 103:5)."),
 ("M25","The withering / fainting self (foil)","The languishing, drying self at its lowest - 'my heart is withered like grass'; 'my spirit faints' (Ps 102:4; 143:7)."),
 # M14 — Deceit / Falsehood
 ("M14","Deceit / guile","The deceiving inner being - guile in the spirit, its absence a blessing ('in whose spirit there is no deceit', Ps 32:2; Pro 12:20)."),
 ("M14","Lying / falsehood","The lying tongue and false heart (Ps 5:6; 12:2; Pro 12:22 'lying lips are an abomination')."),
 ("M14","The double / divided heart","Duplicity - speaking with 'a double heart' (Ps 12:2); the heart that says one thing and means another (Pro 26:24-25)."),
 ("M14","Flattery","Smooth, deceiving speech that spreads a net - 'a flattering mouth works ruin' (Pro 26:28; 29:5; Ps 12:2-3)."),
 ("M14","The masking heart","Fair speech deliberately coating an evil heart - 'fervent lips with an evil heart... believe him not' (Pro 26:23-25; Ps 55:21). Junctions integrity/speech."),
 # M21 — Plea / Petition
 ("M21","Plea for mercy / supplication","The self's cry for grace and to be heard - 'hear the voice of my pleas for mercy' (Ps 28:2; 6:9; 31:22)."),
 ("M21","Petition / asking","Bringing definite requests to God - 'one thing I have asked'; 'two things I ask of you' (Ps 27:4; Pro 30:7)."),
 ("M21","Pouring out the complaint","The total unburdening of the self before God - 'pour out your heart before him'; 'I pour out my complaint before him' (Ps 62:8; 142:2)."),
 ("M21","The cry for vindication","Pleading one's cause / asking to be judged rightly (Ps 26:1; 43:1)."),
 # M47 — The seats (heart / soul / spirit / flesh / inmost)
 ("M47","Heart (leb / lebab)","The centre and core of the inner being - the true self, the source of the life, the thing guarded, given, weighed and searched (Ps 4:7; 51:10; Pro 4:23; 27:19)."),
 ("M47","Soul (nephesh)","The self / life as the seat of longing, the addressed 'O my soul', the poured-out and fainting self (Ps 42:1-2; 103:1; 116:7)."),
 ("M47","Spirit (ruach)","The animating and governing aspect - the spirit ruled and held, committed to God, and lit as 'the lamp of the LORD searching the innermost' (Ps 31:5; 51:10; Pro 16:32; 20:27)."),
 ("M47","Flesh (basar)","The frail, embodied aspect - the self as dust, the flesh that thirsts and fails and registers the heart's states (Ps 16:9; 63:1; 73:26; 103:14)."),
 ("M47","Inmost being / kidneys (kilyah)","The deepest reins/inward parts - the hidden core God tests and instructs by night (Ps 7:9; 16:7; 26:2; 139:13; Pro 23:16)."),
 # --- clusters that surfaced but overlap the baseline; captured minimally, flagged for consolidation ---
 ("M42","Crying out to God","The voiced cry that seeks a hearing - the appeal flung up from distress or the depths ('this poor man cried', Ps 34:6; the fourfold cry, 107; 'out of the depths I cry', 130:1). [Consolidation-candidate w/ M22 song, M03 groaning.]"),
 ("M24","The afflicted / brought-low self","The inner being under affliction and abasement - bowed down, humbled by suffering, its strength brought low (Ps 102 title; 119:67,71 'it is good that I was afflicted'; Pro 16:19). [Consolidation-candidate w/ M03 grief, M09 humility.]"),
 ("M16","Folly / the fool","The anti-wisdom self - the fool 'right in his own eyes', the scoffer who hates reproof, the simple who love simplicity, the self-certain heart (Pro 12:15; 1:22; 26:12). [Consolidation-candidate: foil of M15 wisdom.]"),
 ("M37","Calling on the LORD","Invoking God, turning to him by name - 'I will call on him as long as I live'; 'the LORD is near to all who call on him in truth' (Ps 116:2; 145:18). [Consolidation-candidate w/ M21 plea, M42 crying-out.]"),
]

def main():
    c=sqlite3.connect(DB); cur=c.cursor()
    ins=skip=0; seqs={}
    for cc,name,defi in C:
        ex=cur.execute("SELECT id FROM characteristic WHERE cluster_code=? AND short_name=? AND COALESCE(delete_flagged,0)=0",(cc,name)).fetchone()
        if ex: skip+=1; continue
        if cc not in seqs:
            m=cur.execute("SELECT COALESCE(MAX(char_seq),0) FROM characteristic WHERE cluster_code=?",(cc,)).fetchone()[0]
            seqs[cc]=m
        seqs[cc]+=1
        cur.execute("""INSERT INTO characteristic (cluster_code,char_seq,short_name,definition,source,version,notes,delete_flagged,created_at,last_updated_date)
            VALUES (?,?,?,?,?,?,?,0,?,?)""",(cc,seqs[cc],name,defi,SRC,'v1',NOTE,NOW,NOW)); ins+=1
    c.commit()
    tot=cur.execute("SELECT COUNT(*) FROM characteristic WHERE COALESCE(delete_flagged,0)=0").fetchone()[0]
    ncl=cur.execute("SELECT COUNT(DISTINCT cluster_code) FROM characteristic WHERE COALESCE(delete_flagged,0)=0").fetchone()[0]
    print(f"extension: {ins} inserted, {skip} already present")
    print(f"characteristic baseline now: {tot} characteristics across {ncl} clusters")

if __name__=='__main__': main()
