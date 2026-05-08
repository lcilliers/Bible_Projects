# Cluster identity catalogue v1 — proposed names for review

**Date:** 2026-05-04
**Status:** PROPOSED — every entry below is a draft awaiting researcher review
**Source data:** [outputs/markdown/wa-term-anchor-20260504-clusters.md](wa-term-anchor-20260504-clusters.md)
**Machine-readable companion:** [outputs/markdown/wa-cluster-identity-v1-20260504.json](wa-cluster-identity-v1-20260504.json)

---

## Naming convention

| Field | Format |
|---|---|
| `cluster_id` | Existing — `H000`..`H054` (55 Hebrew) and `G000`..`G032` (33 Greek). Stable across reports. |
| `name` | 1–3 words, Title Case. Designed to be addressable in conversation. |
| `address_format` | `{id} {name}` — e.g. *"H028 Anger, Evil & Turning Away"* or shortened *"H028 Anger"*. |
| `description` | One sentence — captures the dominant theme + secondary themes if cluster is mixed. |
| `mixed` | **Y** = cluster spans 2+ unrelated semantic fields the name cannot fully capture; **N** = single coherent theme. |

**Author's posture for §3 review:** every name is a starting point. Where I'm uncertain (`mixed=Y`), the cluster is a better target for *recursive sub-clustering* than for a single all-encompassing name. Three clusters in particular — **H019, G003, G026** — are theological mega-clusters that deserve sub-cluster names, not single-cluster names.

## Top-line stats

| Metric | Hebrew | Greek | Total |
|---|---|---|---|
| Top-level clusters | 55 | 33 | 88 |
| `mixed=Y` (uncertain naming) | 18 | 13 | 31 |
| `mixed=N` (single-theme, name confident) | 37 | 20 | 57 |

## Standout clusters (start here)

### Cleanest (high cohesion, single morphological/semantic root) — 8 clusters

| ID | Name | Cohesion | Why clean |
|---|---|---|---|
| H013 | Atonement | 0.90 | Only kaphar/kipper/kippurim |
| H022 | Calling & Encounter | 0.74 | All qara family |
| H024 | Hearing & Obeying | 0.70 | All shama family |
| H030 | End & Completion | 0.69 | All kalah family |
| G008 | Phileō Love & Affection | 0.62 | All phil- compounds |
| G020 | Remembrance | 0.72 | All mna-/mneia- |
| G031 | Kingdom & Reign | 0.74 | All basil- compounds |
| H010 | Purity & Defilement | 0.72 | Tahor + zenut paired |

### Theological mega-clusters (need sub-cluster naming, not single-cluster) — 3 clusters

| ID | Auto-label | Why structural |
|---|---|---|
| **H019** | truth/rule/delight (T1=73, T2=107) | The Hebrew covenantal-theological core: chesed, emet, chen, tsedeq, qadosh, racham, shamar, shuv, baruch, chayah, ratson, baqash, salvation, integrity. **Naming as one cluster loses signal.** |
| **G003** | gift/sin/free (T1=33, T2=6) | NT salvation core: hamartia, charis, sōzō, metanoia, aphesis, paraptōma, katallassō. Pauline soteriology in one bag. |
| **G026** | true/clean/love (T1=32, T2=6) | NT truth/love/holiness theology: alētheia, agapaō, hagiasmos, katharos, logos, sōteria, hupakoē, telos. |

### Polar clusters (positive + negative of same axis in one cluster) — 5 clusters

These are interesting structurally — the clustering pulled opposite-pole terms together because they share verse contexts. Naming them honestly requires "X & Y" form.

| ID | Name | Polar pair |
|---|---|---|
| H016 | Justice & Injustice | tsedeq/tsadiq vs avlah/mirmah |
| H034 | Pride & Lowliness | gaon/gevah vs anavah/dakka |
| H046 | Iniquity & Forgiveness | avon vs salach/chanun |
| G014 | Weakness & Authority | astheneia vs exousia/ischuō |
| G024 | Renewal & Hardening | anakainoō vs pōroō/tufloō |

### Worst cohesion (best candidates for sub-clustering or re-clustering) — 5 clusters

| ID | Name | Cohesion |
|---|---|---|
| G032 | Mixed Virtues & Vices | 0.40 |
| H008 | Fear & Trembling | 0.41 |
| H050 | Enemy & Threat | 0.43 |
| H003 | Enmity & Aversion | 0.44 |
| G019 | Will & Purpose | 0.45 |

(H008 is large + heterogeneous but the theme really is fear/trembling — the low cohesion is a cluster-size effect, not a misclassification.)

---

## §1 Hebrew clusters (H000–H054)

Sortable by `cluster_id`. Centroid term is the cluster's mathematical centre — useful for cross-checking the name.

| ID | Name | Description | Centroid (gloss) | T1 | T2 | Cohesion | Mixed |
|---|---|---|---|---:|---:|---:|---:|
| H000 | Defects & Singletons | Catch-all of low-frequency unrelated terms (foolish, slander, perversity, defect) — heterogeneous leaf cluster. | H8400 (defect) | 9 | 0 | 0.48 | Y |
| H001 | Hope & Waiting | Awaiting/hoping in trust, with adjacent uprightness and refuge terms. | H3176H (to wait: hope) | 30 | 7 | 0.48 | Y |
| H002 | Joy & Rejoicing | Verbs and nouns of joy, gladness, singing for joy, shouting in delight. | H8055 (to rejoice) | 17 | 3 | 0.57 | N |
| H003 | Enmity & Aversion | Enmity, despising, hatred, abhorrence, sluggishness — the cluster of aversive states. | H0342 (enmity) | 23 | 0 | 0.44 | Y |
| H004 | Sin's Penalty | Small cluster: iniquity-as-punishment, sin-as-punishment, bitterness, refuse — the consequence-side of sin. | H2403I (sin: punishment) | 6 | 0 | 0.58 | N |
| H005 | Aramaic Wisdom & Authority | Aramaic terms (Daniel/Ezra): wisdom, knowledge, ruling, dominion, holy, judge, praise. | H2452 (wisdom) | 19 | 5 | 0.63 | Y |
| H006 | Forming & Intention | To form/yatsar (potter, plan, formed), with adjacent restraint, desire, sign, breaking. | H3335G (to form: formed) | 17 | 2 | 0.48 | Y |
| H007 | Pride & Haughtiness | Pride, haughtiness, height, greatness — pulling in delight/desire as adjacent affects. | H1365 (haughtiness) | 18 | 2 | 0.50 | N |
| H008 | Fear & Trembling | Large cluster of fear/trembling/dread terms (yare, pachad, charad, ragaz) plus adjacent silence, security, weariness. | H7264 (to tremble) | 65 | 11 | 0.41 | N |
| H009 | Knowledge & Wisdom | Knowledge, understanding, wisdom, counsel, prudence, with folly as paired opposite. | H1847 (knowledge) | 31 | 11 | 0.52 | N |
| H010 | Purity & Defilement | Pure/purity terms (taher, tahor, tohar) anchored against fornication. | H2892A (purity) | 7 | 3 | 0.72 | N |
| H011 | Mourning & Weeping | Mourning, weeping, sighing, tears, sorrow, with comfort/repentance as paired response. | H1058 (to weep) | 28 | 4 | 0.49 | N |
| H012 | Service & Ministry | Avad/avodah family — to serve, ministry, service-as-work, slavery, plus consecrate-prepare. | H5647H (to serve: minister) | 11 | 5 | 0.67 | N |
| H013 | Atonement | Cleanest cluster — kaphar/kipper/kippurim only (atone, cover, atonement). | H3722A (to atone) | 3 | 0 | 0.90 | N |
| H014 | Perversion & Overthrow | Overturning, overthrow, crooked, perversity, devastation; plus minor jealousy-related entries. | H4114 (overthrow) | 11 | 1 | 0.54 | N |
| H015 | Rest & Quiet | Nuach family — rest, resting place, quietness; plus chasad (be kind/shame), unblemished. | H5118 (rest) | 12 | 1 | 0.51 | Y |
| H016 | Justice & Injustice | Polar mix — injustice/treachery/deceit/wickedness clustered with righteousness/justify/blameless. Polarity inside one cluster is structurally significant. | H5766B (injustice) | 20 | 5 | 0.55 | Y |
| H017 | Terror & Dread | Terror-specific cluster (chittah, magor, mechittah, etc.) plus adjacent ruthless and bitterness. | H2847 (terror) | 18 | 1 | 0.52 | N |
| H018 | Voice & Outcry | Small cluster: qal (voice, sound), portion, rage, pain, trust — heterogeneous with voice as anchor. | H7032G (voice: sound) | 7 | 4 | 0.67 | Y |
| **H019** | **Covenantal Core (Mixed)** | Largest cluster (T1=73, T2=107). Hebrew theological/covenantal vocabulary: chesed, emet, chen, tsedeq, qadosh, racham, shamar, shuv, zakhar, chayah, baqash, baruch — plus rule, choose, ask, ruin, integrity, salvation. Too broad to name simply; recursive sub-clustering recommended before naming sub-leaves. | H2421 (to live) | 73 | 107 | 0.47 | **Y** |
| H020 | Madness & Bewilderment | Madness, bewilderment, faint, anxiety, firebrand — disorder of mind cluster. | H7697 (madness) | 14 | 0 | 0.53 | N |
| H021 | Strength & Might | Hebrew strength terms (ko'ach, oz, ezuz, etan, ammits) plus security and severe. | H5794 (strength) | 26 | 3 | 0.47 | N |
| H022 | Calling & Encounter | Qara/qara family — to call, to call out, to read, to encounter, to meet (clean morphological cluster). | H7121G (to call: call to) | 9 | 4 | 0.74 | N |
| H023 | Praise & Song | Praise/boast (halal), song/melody (zamar/mizmor), thanksgiving (yadah, todah), supplication, faithfulness, glory, wonder. | H2167 (to sing) | 27 | 2 | 0.51 | N |
| H024 | Hearing & Obeying | Shama family — hear, obey, proclaim, understand, judge — plus report, tidings, sound, guard. | H8085J (to hear: understand) | 11 | 1 | 0.70 | N |
| H025 | Aramaic Action Mix | Tiny Aramaic cluster: joy, rebellion, prophesying, willing, shut, make, wrath. Heterogeneous Aramaic verbs. | H2305 (joy) | 7 | 3 | 0.75 | Y |
| H026 | Defilement & Abomination | Tame/abomination/uncleanness/impurity (tame, niddah, toevah, shiqquts) plus guilty, common, conceal. | H2930A (to defile) | 18 | 8 | 0.57 | N |
| H027 | Pleasantness & Loveliness | Naim family — pleasant, lovely, pleasantness, musical (small cluster, single root dominance). | H5273B (musical) | 10 | 1 | 0.57 | N |
| H028 | Anger, Evil & Turning Away | Anger/wrath family (charah, charon, chemah, qatsaph, qana, zaam) merged with sur (turn aside), wickedness (rasha, raah), strife (riv), hate (sane), deception (sheqer), transgression (pesha). The 'turning toward evil' macro-cluster. | H7489A (be evil) | 46 | 23 | 0.51 | Y |
| H029 | Aramaic Strength & Bitterness | Small Aramaic cluster: strength, treacherous, crush, bitterness, willing, grief, smoothness. | H0556 (strength) | 13 | 0 | 0.58 | Y |
| H030 | End & Completion | Kalah family — to end (finish, destroy, decide, expend), consumption, perfection, limit. Clean. | H4357 (perfection) | 10 | 0 | 0.69 | N |
| H031 | Folly & Sickness | Folly (sikhlut, pash, sakhal-fool), sickness/disease, rebellion, disgrace, master/husband — disorder cluster. | H5531A (folly) | 16 | 1 | 0.49 | Y |
| H032 | Strife & Despair | Strife (matstsah/matstsut), distress (matsoq), anguish, struggle, anxious (daag), despair (ya'ash), weeping. | H4695 (strife) | 15 | 1 | 0.52 | N |
| H033 | Devising & Planning | Chashav family — to devise (design, count, devise, think), plot, plow, listen, dominion, invention. | H2803G (to devise: design) | 10 | 0 | 0.60 | N |
| H034 | Pride & Lowliness | Polar cluster — pride/height/majesty (gaon, geut, gevurah, marom) merged with humility/contrite/poor (anavah, dakka, anav). The exalted-vs-lowly axis. | H1361 (to exult) | 29 | 6 | 0.50 | Y |
| H035 | Cruelty & Harshness | Cruel (akhzar), strength, contempt, terror, scorching, vexed — harshness cluster. | H0393 (cruel) | 18 | 0 | 0.48 | N |
| H036 | Sin & Consecration (Cultic) | Cultic-system cluster — sin/sin-offering (chattat) merged with consecration/holiness (qadash, qodesh) and unblemished. The sacrificial-system semantic field. | H2403H (sin: sin offering) | 20 | 39 | 0.53 | Y |
| H037 | Support & Faltering | Tiny — support/expectation, groan/groaning, totter, sluggish. | H4937B (support) | 8 | 0 | 0.61 | N |
| H038 | Pressing & Confining | Tsur (confine, provoke, form), tsuq (press), with willing and treachery as outliers. | H6696A (to confine) | 8 | 1 | 0.63 | N |
| H039 | Peace & Well-being | Shalom family (peace, well-being, friendship, greeting, completely) plus to-keep/shamar:look-at, to-rest, to-quiet, innocence, love-as-friend. | H7965J (peace: friendship) | 16 | 0 | 0.53 | N |
| H040 | Delight & Indulgence | Anog family — to delight, dainty, luxury — plus bosom/embrace, obedience, stubbornness, pain. | H6028 (dainty) | 8 | 1 | 0.59 | N |
| H041 | Aramaic Faith & Strength | Aramaic cluster: trust, ask, gracious, strength, wise, compassion, grow, rule, wonder. | H0540 (to trust) | 14 | 4 | 0.69 | Y |
| H042 | Mixed Minor Terms II | Heterogeneous singletons — cheerful, rise, silence, shine, confidence, comfort, integrity, dishonor, boil. Like H000, a leftover/leaf cluster. | H4472 (bitterness) | 22 | 1 | 0.52 | Y |
| H043 | Lust & Fornication | Zanah/taznut (fornication), agav/agavah (lust), lover, hating, abhor, lamentation. The illicit-desire cluster. | H5691 (lust) | 16 | 5 | 0.53 | N |
| H044 | Honor & Glory | Kavod family — glory, honor, glorious, heaviness, riches — plus arrange/value (arakh), prosper, rank. | H3520A (glorious) | 14 | 1 | 0.56 | N |
| H045 | Horror & Assembly | Tiny mixed: horror, upright, destruction, assembly, proclamation, extolling. | H7318 (extolling) | 6 | 0 | 0.63 | Y |
| H046 | Iniquity & Forgiveness | Iniquity/avon (crime, guilt) merged with forgive (salach, selichah), gracious (chanun, rachum), pity (chus), supplication, pray, ransom — plus rebel, transgress, idol. The sin-and-mercy axis. | H5545 (to forgive) | 33 | 3 | 0.47 | Y |
| H047 | Pledge & Provocation | Mixed: pledge/labour (chaval), wealth, desire (chashaq), connect, provoke (marar), slander, charm, deceive, shudder, roar. | H8175A (to shudder) | 20 | 0 | 0.49 | Y |
| H048 | Strengthening & Vigor | Chazaq + chayil families — to strengthen, hold, prevail, persevere; strength as wealth/worthiness/soldiers. | H2388G (to strengthen: strengthen) | 14 | 4 | 0.63 | N |
| H049 | Languishing & Sorrow | Small mixed: languish, dismay, sorrow, illness, joy (anomaly), compassion, distress, beautify. | H1670 (dismay) | 11 | 0 | 0.52 | Y |
| H050 | Enemy & Threat | Enemy (oyev, tsar), opponent, hostile, terror, dismay, breaking, prey, tear — plus refuge, hope, master as adjacents. | H0341 (enemy) | 30 | 10 | 0.43 | Y |
| H051 | Destruction & Decay | Destruction (machshit, mashchit, chevel, chaloph), remove, slander, mourning, repose, prevail, swerve, quietness, delight — heterogeneous decay/destruction cluster. | H2256D (destruction) | 13 | 1 | 0.48 | Y |
| H052 | Aramaic Distress & Plotting | Aramaic cluster: break, displeased, hastily, dismay, strive, fear, plan, fantasies, perplexed, startled, hate, distinguish. | H2418 (to live) | 18 | 1 | 0.65 | Y |
| H053 | Shame & Reproach | Bosh/boshet/bushah (shame, ashamed) plus cherpah (reproach), kalam (humiliated), kelimmah (shame). Plus refuge, breaking, hope, outcry, pride as outliers. | H1322 (shame) | 16 | 4 | 0.54 | N |
| H054 | Distress & Anguish | Tsar/tsarah/metsuqah/tsuq family — distress, anguish, terror, hard, vex, pain, contempt — plus compassion (chemlah) and judgment. | H4691 (distress) | 16 | 2 | 0.54 | N |

## §2 Greek clusters (G000–G032)

| ID | Name | Description | Centroid (gloss) | T1 | T2 | Cohesion | Mixed |
|---|---|---|---|---:|---:|---:|---:|
| G000 | Stumbling & Mind | Stumbling block (proskomma, skandalon), be bold, weakness, abhor, discernment, reason, thoughtful, high, lazy, fervent, sound mind. Mixed thinking + stumbling. | G0662 (be bold) | 24 | 0 | 0.56 | Y |
| G001 | Boldness & Weakness | Boldness (parrēsia, tolmaō), confidence, plan, pray, dispute — mixed against weakness, dishonour. Polar mix. | G5111 (be bold) | 17 | 3 | 0.53 | Y |
| G002 | Desire & Defilement | Epithumia (desire/long for), impurity (akatharsia), corruption, defilement, callous, deceit, dishonor, idolatry, self-will, philosophy, pleasure. The 'corrupt desire' cluster. | G1939 (desire) | 26 | 2 | 0.49 | N |
| **G003** | **Sin, Grace & Salvation** | Major theological cluster — hamartia/hamartanō/hamartolos (sin/sinful), charis/charisma/charizō (grace), aphesis (forgiveness), sōzō (save), metanoia (repentance), parabasis (transgression), katallassō (reconcile), paraptōma (trespass). | G3900 (trespass) | 33 | 6 | 0.50 | **Y** |
| G004 | Justice & Righteousness | Dikaios family — just, righteousness, justify, justification, condemnation, avenge, vengeance — plus opponent, accountable. | G1344 (to justify) | 15 | 1 | 0.67 | N |
| G005 | Joy, Peace & Endurance | Chairō/chara (rejoice/joy), eirēnē (peace), elpis/elpizō (hope), eucharistia (thanksgiving), hupomonē (perseverance), parakaleō/paraklēsis (comfort/encouragement) — plus ekklēsia and the consoling cluster around it. | G5463 (to rejoice) | 38 | 11 | 0.48 | Y |
| G006 | Goodness & Mercy | Agathos (good), agathopoieō (do good), eleos (mercy), epieikēs (gentle), peaceful, brotherhood, sister, genuine, of-one's-household, propitiation, reverence-for-God, zealot. | G2317 (reverence for God) | 30 | 2 | 0.50 | Y |
| G007 | Anguish & Crying | Klaiō (weep), krazō (cry), basanismos (torment), douleia (slavery), labor — plus expire, listen, strong, plunder. | G2799 (to weep) | 12 | 0 | 0.55 | Y |
| G008 | Phileō Love & Affection | All phil- compounds — filos, fileō, filadelfia (brotherly love), filanthrōpia (benevolence), filēma (kiss), filotheos (God-loving), filarguria (love of money). Cleanest morphological cluster on the Greek side. | G5377 (God-loving) | 16 | 0 | 0.62 | N |
| G009 | Spirit-Fruit Virtues | Praotēs (gentleness), makrothumia (patience), chrēstotēs (kindness), agapē (love), tapeinofrosunē (humility), oiktirmos (compassion), hagios (holy) — broadly the fruit-of-the-Spirit cluster. | G4236 (gentleness) | 23 | 7 | 0.55 | N |
| G010 | Wisdom & Folly | Sofia/sofos (wisdom/wise), mōria/mōros (foolishness), unwise, knowing, understanding, intelligent — plus shame and natural/psychic. | G3471 (be foolish) | 14 | 0 | 0.62 | Y |
| G011 | Prayer & Struggle | Proseuchomai/proseuchē (pray/prayer), deēsis (petition), eucharisteō (thank), epipotheō (long for), profēteuō (prophesy), agōnia (struggle), peirasmos (testing/temptation), spiritual. | G1874 (to listen ro) | 29 | 3 | 0.53 | N |
| G012 | Self-Control & Sobriety | Sōfrōn/sōfronizō (self-controlled), enkratēs (self-controlled), nēfaleos (sober), hagnos (pure), hosios (sacred), semnos (noble), filagathos (lover of good), filoxenos (hospitable), prosfilēs (lovely). The disciplined-virtues cluster. | G4998 (self-controlled) | 13 | 1 | 0.58 | N |
| G013 | Shame & Boasting | Kauchaomai/kauchēma (boast/pride) merged with aischunō/aischros (be ashamed/shameful), kataischunō (dishonor), foolish, sorrowful, eagerness, repent, ignore, groan, silent. | G0150 (shameful) | 28 | 0 | 0.50 | Y |
| G014 | Weakness & Authority | Astheneia/astheneō/asthenēs (weakness/be weak/weak) merged with exousia (authority), ischuō (be strong), katakurieuō (master), proskaleō (call/summon), illness, unclean, fight. Polar weak/strong cluster. | G0769H (weakness: ill) | 26 | 11 | 0.49 | Y |
| G015 | Vices & Wickedness | NT vice catalogue — kakia (evil), ponēria/ponēros (evil/bad), eris (quarrel), hupokrisis (hypocrisy), adikia (unrighteousness), aselgeia (debauchery), blasfēmia (blasphemy), dolos (deceit), pikria (bitterness), pleonexia (greed), phthonos (envy). | G4189 (evil) | 20 | 1 | 0.63 | N |
| G016 | Mind & Anguish | Reasoning/thought (dialogizomai, dialogismos, logismos, ennoia, fronēma, suniēmi), reflection (enthumeomai), anguish (odunē, sunochē), abomination, hardening, fleshly, grieve, die-with, predetermine, seize. | G3601 (anguish) | 32 | 2 | 0.55 | Y |
| G017 | Praise & Affirmation | Eulogeō (bless/praise), ainesis (praise), humneō (praise), exomologeomai (agree), worthy, hospitable, purity, new, firstborn, foreknow, conformed, strong, hot — plus debauchery, decay, doubt, deport, distract, embitter, false-prophet, silence as outliers. | G4416 (firstborn) | 25 | 2 | 0.48 | Y |
| G018 | Idolatry & Pollution | Eidōlon family — idol, idolater, idol's-temple, sacrificed-to-idols — plus miainō/molunō (stain/defile), reject, slander, weak, gain, fainthearted. | G1493 (idol's temple) | 16 | 3 | 0.56 | N |
| G019 | Will & Purpose | Thelēma/thelō (will/desire), boulē/boulomai (plan/will), prothesis (purpose), eudokeō (delight), zēteō (seek), zēloō (be eager), oida (know), dokimazō (test) — plus disobedience, slave, contend, authority, plot. | G2307 (will/desire) | 32 | 7 | 0.45 | N |
| G020 | Remembrance | All mna-/mneia- compounds — mimnēskō (remember), mneia (remembrance), anamnēsis (remembrance), hupomimnēskō (remind). Cleanest Greek morphological cluster. | G3403 (to remember) | 9 | 1 | 0.72 | N |
| G021 | Power & Effort | Dunamis/dunamoō/endunamoō (power/empower/strengthen), energeō/energeia (active/working), kratos (power), ischus (strength), agōnizomai (struggle), hagiōsunē (holiness), self-discipline, oppress, press-on. | G4995 (self-discipline) | 24 | 1 | 0.57 | Y |
| G022 | Harm & Apostasy | Mixed wrong-doing cluster — adikeō (harm), apoballō (throw away), apokatallassō (reconcile), aporeō (perplexed), apostasia, ftheirō (destroy), hupokrinō (pretend), kataponeō (oppress), prodotēs (traitor), pantokratōr (almighty). | G0639 (be perplexed) | 16 | 0 | 0.52 | Y |
| G023 | Submission & Pressure | Hupotagē (submission), hēsuchios (quiet), haplotēs (openness), eilikrineia (sincerity), koinōnia (participation), thlipsis (pressure), kauchēsis (pride), semnotēs (dignity), authenteō (domineer). | G5292 (submission) | 13 | 2 | 0.56 | Y |
| G024 | Renewal & Hardening | Polar mix — anakainoō (renew), metamorfoō (transform), allassō (change), doxa (glory), eikōn (image) merged with pōroō (harden), tufloō (blind), katakrisis (condemnation), ekkakeō (lose heart). | G5186 (to blind) | 12 | 2 | 0.57 | Y |
| G025 | Self-Control & Reverence | Enkrateia (self-control), eulabeomai (revere), hosiotēs (holiness), hermēneuō (interpret), peacemaker, unity, foreknowledge, gentle, poor — plus enslave, conquer, cunning, quarrel. | G2059 (to interpret) | 15 | 1 | 0.56 | Y |
| **G026** | **Truth, Love & Holiness** | Major theological cluster — alētheia (truth), alēthinos/alēthēs (true), agapaō (to love), hagiasmos/hagnizō (holiness/purify), katharos/katharizō (clean), logos (word), peithō (persuade), sōteria (salvation), hupakoē (obedience), telos (goal). | G0225 (truth) | 32 | 6 | 0.48 | **Y** |
| G027 | Atonement & Grief (NT) | Hilaskomai (propitiate), penthos (grief), aischunē (shame), exaleifō (blot out), basanos (torment), epichriō (rub on/anoint), gumnazō (train), ponos (travail), saving (sōtērion), boasting (alazoneia). | G2025 (to rub on) | 15 | 2 | 0.59 | Y |
| G028 | Fear & Zeal | Fobeō/fobos (fear), tromos (trembling), foberos/emfobos/ekfobos (fearful/afraid/terrified) — plus zēlos (zeal), spoudē (diligence), epipothēsis (longing), eusplanchnos (compassionate), entrepō (cause shame). | G5401 (fear) | 18 | 4 | 0.50 | Y |
| G029 | Wrath, Calling & Mercy | Orgē/orgizō (wrath/anger), kaleō/fōneō (call), doulos/sundoulos (slave), splanchnizō (pity), aphiēmi (release/leave), kurios (lord), praise, weeping, mistreat, blind, sift, perplexed. Heterogeneous mix of authority/anger/calling/mercy. | G3710 (to anger) | 40 | 13 | 0.49 | Y |
| G030 | Faith & Mercy | Pistis/pisteuō/pistos (faith/believe/faithful), apistia (unbelief), oligopistos (little-faith), eleeō/eleēmōn (mercy/merciful), hilastērios (propitiation), aphiēmi:forgive, sōtēr (savior), hardness-of-heart, breath-of-spirit. | G4102G (faith) | 34 | 7 | 0.49 | N |
| G031 | Kingdom & Reign | All basil- compounds — basileia (kingdom), basileuō (reign), basilikos (royal), basileion (palace), basilissa (queen), sumbasileuō (reign-with). Clean. | G0933 (palace) | 7 | 1 | 0.74 | N |
| **G032** | **Mixed Virtues & Vices** | WORST cohesion (0.40). Tapeinoō (humble), metanoeō (repent), peirazō (test/tempt), hagiotēs (holiness), hupokritēs (hypocrite), huperēfanos (arrogant), eulabeia (reverence), filautos (selfish), adolos (pure), alazōn (braggart), penthos (mourn), phthoneō (envy). Recommend recursive sub-clustering before naming sub-leaves. | G5013 (to humble) | 41 | 3 | 0.40 | **Y** |

## §3 How to review / revise

1. **Read the cluster list** — flag names that misrepresent or that you'd phrase differently.
2. **For each revision** in this `.md`, edit two places:
   - The `name` cell in the table here
   - The corresponding `name` field in [`wa-cluster-identity-v1-20260504.json`](wa-cluster-identity-v1-20260504.json), and change `status` from `proposed` to `revised`
3. **For names you accept as-is**, change `status` from `proposed` to `confirmed` in the JSON.
4. **For mega-clusters (H019, G003, G026):** these are flagged as needing sub-cluster names. Recommend deferring final naming until recursive sub-clustering is run (the validation pass produced 79 H leaves and 55 G leaves — those are better naming targets).
5. When revisions are complete, run a script to bump the file to v2 and write a clean catalogue.

## §4 What this report does NOT do (yet)

- **Per-cluster drill-down pages** — the larger overview design ([wa-cluster-ecosystem-overview-design-v1-20260504.md](wa-cluster-ecosystem-overview-design-v1-20260504.md)) covers this as Option (a) per-cluster generator.
- **Sub-cluster names for the recursive leaves** — defer until you've decided which top-level clusters need recursive breakdown.
- **Bridge-pair naming** — Hebrew↔Greek crosslang bridges aren't yet matched (e.g., should H028 *Anger, Evil & Turning Away* and G029 *Wrath, Calling & Mercy* share a "wrath" tag?). Defer to ecosystem overview §D.
- **Researcher-curated short-handles** — if you want addressable short forms (e.g. `H028 = AET`), that's a separate small-table layer on top of this one.
