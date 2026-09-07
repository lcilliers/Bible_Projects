# M46 Abundance, Prosperity and Wealth — comprehensive term + verse exposure

**Generated:** 2026-05-14T11:45:45Z  
**Cluster:** `M46` (bucket=NAMED, status=Data - In Progress, version=v6)  
**Source:** `database/bible_research.db`  

**Scope of this report:** every database fact that connects to a term in this cluster, exposed by term and by verse. Items currently linked only at registry / collection level (not yet resolvable to a specific term) are listed in the appendix as candidates for future linkage. Numbered paragraphs are used throughout to make every item directly referenceable.

---

<a id="toc"></a>
## Table of contents

- [§1. Cluster summary](#s1)
- [§2. Verses by sub-group](#s2)
  - [§2.1 _(unrouted / unassigned)_](#s2-1)
- [§3. Per-term comprehensive detail](#s3)
  - [H7230 rov — abundance (`mti_id=1142`)](#t-H7230)
  - [H1952 hon — substance (`mti_id=7010`)](#t-H1952)
  - [H1878 da.shen — to prosper (`mti_id=111`)](#t-H1878)
  - [H2633 cho.sen — wealth (`mti_id=681`)](#t-H2633)
  - [H3520B ke.vud.dah — riches (`mti_id=1870`)](#t-H3520B)
- [§4. Appendix — items linked at registry or collection level](#s4)
  - [§4.1 Findings from contributor registries with no term-level link (4)](#s4-1)
  - [§4.2 SD pointers from contributor registries with no term-level link (10)](#s4-2)
  - [§4.3 Prose sections from contributor registries (0)](#s4-3)
  - [§4.4 Cluster-internal verse_context_group rows (6)](#s4-4)
  - [§4.5 Cross-cluster orphan findings/pointers](#s4-5)

---

<a id="s1"></a>
## §1. Cluster summary

1. Description: Abundance, Prosperity and Wealth
2. Bucket / Status / Version: NAMED / Data - In Progress / v6
3. Last updated: 2026-05-14T08:00:24Z
4. Terms in cluster: **5** (Hebrew 5 · Greek 0)
5. Active OWNER verses (sum across terms): 85
6. Contributor registries: 4

**Verse status summary** (85 active verses)

| Status | Count | % | Meaning |
|---|---:|---:|---|
| G | 43 | 50.6% | group-assigned (analysed) |
| SA | 25 | 29.4% | set-aside (with reason) |
| NR | 0 | 0.0% | not-relevant (is_relevant=0) |
| P | 16 | 18.8% | pending (relevant but no group yet) |
| UT | 1 | 1.2% | untouched (no verse_context row) |
| **Total** | **85** | 100% | |

**By testament:** OT 85 · NT 0

**Set-aside reasons** (25 rows):

- (1) hon = enough applied to physical phenomena (barren womb, land, fire). The insati
- (1) hon = commercial material wealth of Tyre. Commercial exchange context; no inner-
- (1) hon = commercial wealth of Tyre (Damascus trade). Same pattern as Eze 27:12; com
- (1) hon = riches sinking with Tyre. Material commercial goods lost in catastrophe; n
- (1) hon = abundant commercial wealth enriching kings. Commercial material wealth; no
- (1) rov = numerical multitude of offspring in divine promise. Sheer quantity; no inn
- (1) rov = material plenty as blessing content. Quantity of provision; no inner state
- (1) rov = adverbial quantifier of material increase (increased abundantly). Rate of
- (1) rov = numerical multitude of offspring in covenant promise. Sheer quantity; no i
- (1) rov = numerical multitude in blessing wish for descendants. Quantity of persons;
- (1) rov = quantity of years as legal-commercial price multiplier. Legal quantifier;
- (1) rov = numerical quantity of enemy forces (like locusts in number). Comparative s
- (1) rov = numerical quantity of enemy forces (locusts in abundance). Sheer quantity
- (1) rov = adverbial quantifier (plentifully declared sound knowledge). Quantifier fo
- (1) rov = many (years), temporal quantifier. Time quantity; no inner-being content.

7. Gloss list (5 entries — every distinct term currently in the cluster, disambiguated by transliteration):

abundance (rov), riches (ke.vud.dah), substance (hon), to prosper (da.shen), wealth (cho.sen)

**Patch-authoring reference table:** integer values per term for the patch's `_patch_meta.terms_covered` (mti_id) and `_patch_meta.input_versions` (md_version). Sorted by Strong's.

| Strong's | Translit | mti_id | md_version | vc_status |
|---|---|---:|---:|---|
| H1878 | da.shen | 111 | 2 | vc_completed |
| H1952 | hon | 7010 | 2 | vc_completed |
| H2633 | cho.sen | 681 | 2 | vc_completed |
| H3520B | ke.vud.dah | 1870 | 1 | not_done |
| H7230 | rov | 1142 | 2 | vc_completed |

9. Connectivity health (broken or missing links along verse → vc → vcg / sub-group → term):

| Code | Check | Count |
|---|---|---:|
| `H1` ⚠ | Active vc rows in cluster with `cluster_subgroup_id` NULL — verse not routed to any sub-group | 85 |
| `H2` ⚠ | Active vc rows with `is_relevant=1` but `group_id` NULL — relevant verse not yet in a meaning group | 17 |
| `H3` | vc.mti_term_id is not in its vcg's term set (`vcg_term`) — cross-term contamination, or vc points at a soft-deleted vcg | 0 |
| `H4` | vc.cluster_subgroup_id set but the term has no `mti_term_subgroup` link to that sub-group — orphaned verse routing | 0 |
| `H5` | Active `verse_context_group` rows with no active vc references — orphan meaning group | 0 |
| `H6` ⚠ | Cluster terms with no `mti_term_subgroup` mapping — term placed in cluster but unassigned to any sub-group | 5 |
| `H7` | Cluster terms with sub-group mapping but zero `verse_context_group` rows — sub-group placed but verses never contextually grouped | 0 |
| `H8` | vcgs whose active verses span multiple sub-groups — the same meaning is routed to different sub-groups; candidates for promotion, reassignment, or split | 0 |

_`H1` detail (showing 50 of 85):_

| vc_id | Reference | Strong's | mti_id |
|---|---|---|---|
| 64213 | Deu 31:20 | H1878 | 111 |
| 64235 | Exo 27:3 | H1878 | 111 |
| 64244 | Isa 34:6 | H1878 | 111 |
| 64245 | Isa 34:7 | H1878 | 111 |
| 64237 | Num 4:13 | H1878 | 111 |
| 533 | Pro 11:25 | H1878 | 111 |
| 532 | Pro 13:4 | H1878 | 111 |
| 64214 | Pro 15:30 | H1878 | 111 |
| 534 | Pro 28:25 | H1878 | 111 |
| 64242 | Psa 20:3 | H1878 | 111 |
| 531 | Psa 23:5 | H1878 | 111 |
| 64251 | Eze 27:12 | H1952 | 7010 |
| 64252 | Eze 27:18 | H1952 | 7010 |
| 64253 | Eze 27:27 | H1952 | 7010 |
| 64254 | Eze 27:33 | H1952 | 7010 |
| 64221 | Pro 10:15 | H1952 | 7010 |
| 52788 | Pro 11:4 | H1952 | 7010 |
| 64222 | Pro 12:27 | H1952 | 7010 |
| 64224 | Pro 13:11 | H1952 | 7010 |
| 64223 | Pro 13:7 | H1952 | 7010 |
| 52785 | Pro 18:11 | H1952 | 7010 |
| 64226 | Pro 19:14 | H1952 | 7010 |
| 64225 | Pro 19:4 | H1952 | 7010 |
| 64218 | Pro 1:13 | H1952 | 7010 |
| 64227 | Pro 24:4 | H1952 | 7010 |
| 52789 | Pro 28:22 | H1952 | 7010 |
| 64228 | Pro 28:8 | H1952 | 7010 |
| 52790 | Pro 29:3 | H1952 | 7010 |
| 64229 | Pro 30:15 | H1952 | 7010 |
| 64243 | Pro 30:16 | H1952 | 7010 |
| 52787 | Pro 3:9 | H1952 | 7010 |
| 64219 | Pro 3:9 | H1952 | 7010 |
| 64220 | Pro 8:18 | H1952 | 7010 |
| 52786 | Psa 112:3 | H1952 | 7010 |
| 52784 | Psa 119:14 | H1952 | 7010 |
| 64217 | Psa 44:12 | H1952 | 7010 |
| 52791 | Song 8:7 | H1952 | 7010 |
| 53166 | Eze 22:25 | H2633 | 681 |
| 53163 | Isa 33:6 | H2633 | 681 |
| 64250 | Jer 20:5 | H2633 | 681 |
| 53164 | Pro 15:6 | H2633 | 681 |
| 53165 | Pro 27:24 | H2633 | 681 |
| 61187 | Eze 23:41 | H3520B | 1870 |
| 61188 | Psa 45:13 | H3520B | 1870 |
| 64230 | Gen 16:10 | H7230 | 1142 |
| 64231 | Gen 27:28 | H7230 | 1142 |
| 64232 | Gen 30:30 | H7230 | 1142 |
| 64233 | Gen 32:12 | H7230 | 1142 |
| 64234 | Gen 48:16 | H7230 | 1142 |
| 38117 | Hos 10:1 | H7230 | 1142 |

_`H2` detail (showing 17 of 17):_

| vc_id | Reference | Strong's | mti_id |
|---|---|---|---|
| 64213 | Deu 31:20 | H1878 | 111 |
| 64214 | Pro 15:30 | H1878 | 111 |
| 64221 | Pro 10:15 | H1952 | 7010 |
| 64222 | Pro 12:27 | H1952 | 7010 |
| 64224 | Pro 13:11 | H1952 | 7010 |
| 64223 | Pro 13:7 | H1952 | 7010 |
| 64226 | Pro 19:14 | H1952 | 7010 |
| 64225 | Pro 19:4 | H1952 | 7010 |
| 64218 | Pro 1:13 | H1952 | 7010 |
| 64227 | Pro 24:4 | H1952 | 7010 |
| 64228 | Pro 28:8 | H1952 | 7010 |
| 64229 | Pro 30:15 | H1952 | 7010 |
| 64219 | Pro 3:9 | H1952 | 7010 |
| 64220 | Pro 8:18 | H1952 | 7010 |
| 64217 | Psa 44:12 | H1952 | 7010 |
| 64211 | Hos 9:7 | H7230 | 1142 |
| 64212 | Job 11:2 | H7230 | 1142 |

_`H6` detail (showing 5 of 5):_

| mti_id | Strong's | Translit | Gloss |
|---|---|---|---|
| 111 | H1878 | da.shen | to prosper |
| 7010 | H1952 | hon | substance |
| 681 | H2633 | cho.sen | wealth |
| 1870 | H3520B | ke.vud.dah | riches |
| 1142 | H7230 | rov | abundance |

<a id="s2"></a>
## §2. Verses by sub-group

All verses for cluster terms, grouped by the analytical sub-group the term belongs to. Within each sub-group the rows are sorted canonically (book · chapter · verse). The **Term** column shows the Strong's number and transliteration of the cluster term whose `wa_verse_records` row generated this entry; **Spans in verse** lists every term-span recorded at that verse location.

Status precedence: G = group-assigned (analysed) · SA = set-aside · NR = is_relevant=0 · P = pending in VC · UT = untouched (no VC row).

**ID columns:** `vr_id` is `wa_verse_records.id`; `mti_id` is `mti_terms.id` (also `wa_verse_records.mti_term_id` and `verse_context.mti_term_id`). Both are exposed so AI can author VCREVISE / VCNEW / VCVERSE patches directly from this report — no separate ID-resolver query needed. The `(vr_id, mti_id)` pair is the natural key for any `verse_context` operation.

<a id="s2-1"></a>
### §2.1 _(unrouted / unassigned)_

_Verses whose `verse_context.cluster_subgroup_id` is NULL, or whose term has no `mti_term_subgroup` mapping._

1. Terms (5): H1878 da.shen, H2633 cho.sen, H7230 rov, H3520B ke.vud.dah, H1952 hon
2. Verse rows (85):

| vr_id | mti_id | Reference | Term | Status | Group | Set-aside reason | Spans in verse | Verse text |
|---:|---:|---|---|---|---|---|---|---|
| 40823 | 1142 | Gen 16:10 | H7230 rov | SA |  | rov = numerical multitude of offspring in divine promise. Sheer quantity; no inner-being state named or engaged by the term. | H3808 lo (not) [cannot]; H7230 rov (abundance) [multitude]; H7235A ra.vah (to multiply) [surely]; H2233H ze.ra (seed: children) [offspring] | Gen 16:10 The angel of the Lord also said to her, “I will surely multiply your offspring so that they cannot be numbered for multitude .” |
| 40824 | 1142 | Gen 27:28 | H7230 rov | SA |  | rov = material plenty as blessing content. Quantity of provision; no inner state of the person engaged by this term. | H5414G na.tan (to give: give) [give]; H7230 rov (abundance) [plenty]; H4924A sha.man (fat) [fatness]; H4924C mash.man (fat piece) [fatness] | Gen 27:28 May God give you of the dew of heaven and of the fatness of the earth and plenty of grain and wine . |
| 40825 | 1142 | Gen 30:30 | H7230 rov | SA |  | rov = adverbial quantifier of material increase (increased abundantly). Rate of material growth; no inner-being engagement by this term. | H7230 rov (abundance) [abundantly]; H1571 gam (also) [also]; H4970 ma.tay (how) [now when]; H1288 ba.rakh (to bless) [blessed]; H4592 me.at (little) [little]; H7272 re.gel (foot) [turned] | Gen 30:30 For you had little before I came, and it has increased abundantly , and the Lord has blessed you wherever I turned . But now when shall I provide for my own household also ?” |
| 40826 | 1142 | Gen 32:12 | H7230 rov | SA |  | rov = numerical multitude of offspring in covenant promise. Sheer quantity; no inner state named by this term. | H3190 ya.tav (be good) [surely]; H7230 rov (abundance) [multitude]; H0859B t.ti (you [f.s.]) [you]; H0859E at.ten (you [f.p.]) [you]; H2233H ze.ra (seed: children) [offspring] | Gen 32:12 But you said , ‘I will surely do you good , and make your offspring as the sand of the sea , which cannot be numbered for multitude .’” |
| 40827 | 1142 | Gen 48:16 | H7230 rov | SA |  | rov = numerical multitude in blessing wish for descendants. Quantity of persons; no inner-being phenomenon. | H7230 rov (abundance) [multitude]; H1288 ba.rakh (to bless) [bless] | Gen 48:16 the angel who has redeemed me from all evil , bless the boys ; and in them let my name be carried on , and the name of my fathers Abraham and Isaac ; and let them grow into a multitude in the midst of the earth .” |
| 1130 | 111 | Exo 27:3 | H1878 da.shen | SA |  | da.shen rendered as de.shen (ashes of altar, noun). Physical ritual residue; the term here names the physical ash of offerings, not an inner-being characteristic. | H1878 da.shen (to prosper) [ashes] | Exo 27:3 You shall make pots for it to receive its ashes , and shovels and basins and forks and fire pans . You shall make all its utensils of bronze . |
| 40859 | 1142 | Lev 25:16 | H7230 rov | SA |  | rov = quantity of years as legal-commercial price multiplier. Legal quantifier; no inner state engaged by this term. | H7230 rov (abundance) [many]; H7235A ra.vah (to multiply) [increase] | Lev 25:16 If the years are many , you shall increase the price , and if the years are few , you shall reduce the price , for it is the number of the crops that he is selling to you . |
| 1131 | 111 | Num 4:13 | H1878 da.shen | SA |  | da.shen rendered as de.shen (ashes of altar, same as Exo 27:3). Physical altar ash; no inner-being content. | H1878 da.shen (to prosper) [ashes]; H0853 et ([Obj.]) [altar] | Num 4:13 And they shall take away the ashes from the altar and spread a purple cloth over it . |
| 1132 | 111 | Deu 31:20 | H1878 da.shen | P |  |  | H1878 da.shen (to prosper) [grown fat]; H5006 na.ats (to spurn) [despise]; H1285 be.rit (covenant) [covenant]; H7650 sha.va (to swear) [swore]; H5647H a.vad (to serve: minister) [serve] | Deu 31:20 For when I have brought them into the land flowing with milk and honey , which I swore to give to their fathers , and they have eaten and are full and grown fat , they will turn to other gods and serve them, and despise me and break my covenant . |
| 40854 | 1142 | Judg 6:5 | H7230 rov | SA |  | rov = numerical quantity of enemy forces (like locusts in number). Comparative size only; no inner-being content. | H1992 hem.mah (they [masc.]) [livestock]; H7230 rov (abundance) [number]; H0935G bo (to come [in]: come) [come]; H7843 sha.chat (to ruin) [laid waste] | Judg 6:5 For they would come up with their livestock and their tents ; they would come like locusts in number —both they and their camels could not be counted —so that they laid waste the land as they came in. |
| 40855 | 1142 | Judg 7:12 | H7230 rov | SA |  | rov = numerical quantity of enemy forces (locusts in abundance). Sheer quantity of personnel; no inner-being content. | H7230 rov (abundance) [abundance] | Judg 7:12 And the Midianites and the Amalekites and all the people of the East lay along the valley like locusts in abundance , and their camels were without number , as the sand that is on the seashore in abundance . |
| 40863 | 1142 | Neh 9:25 | H7230 rov | G | 1142-001 |  | H7230 rov (abundance) [abundance]; H5727 a.dan (to luxuriate) [delighted]; H8082 sha.men (rich) [rich]; H8080 sha.men (to grow fat) [became fat] | Neh 9:25 And they captured fortified cities and a rich land , and took possession of houses full of all good things , cisterns already hewn , vineyards , olive orchards and fruit trees in abundance . So they ate and were filled and became fat and delighted themselves in your great goodness . |
| 40862 | 1142 | Neh 13:22 | H7230 rov | G | 1142-001 |  | H2617A che.sed (kindness) [steadfast love]; H6942G qa.dash (to consecrate: consecate) [holy]; H7230 rov (abundance) [greatness]; H2142 za.khar (to remember) [Remember]; H1571 gam (also) [also]; H0935G bo (to come [in]: come) [come]; H2617B che.sed (shame) [steadfast love]; H2347 chus (to pity) [spare]; H8104H sha.mar (to keep: guard) [guard]; H2891 ta.her (be pure) [purify themselves] | Neh 13:22 Then I commanded the Levites that they should purify themselves and come and guard the gates , to keep the Sabbath day holy . Remember this also in my favor, O my God , and spare me according to the greatness of your steadfast love . |
| 40853 | 1142 | Job 4:14 | H7230 rov | G | 1142-001 |  | H6342 pa.chad (to dread) [shake]; H6343 pa.chad (dread) [dread]; H7230 rov (abundance) [made all]; H7461A ra.ad (trembling) [trembling]; H7122H qa.ra (to encounter: toward) [came]; H6106G e.tsem (bone) [bones] | Job 4:14 dread came upon me, and trembling , which made all my bones shake . |
| 40846 | 1142 | Job 11:2 | H7230 rov | P |  |  | H6663 tsa.deq (to justify) [judged right]; H7230 rov (abundance) [multitude] | Job 11:2 “Should a multitude of words go unanswered , and a man full of talk be judged right ? |
| 40847 | 1142 | Job 23:6 | H7230 rov | G | 1142-001 |  | H1931 hu (he/she/it) [he]; H5978 im.ma.di (with me) [with]; H7230 rov (abundance) [greatness]; H7378 riv (to contend) [contend]; H3581B ko.ach (strength) [power] | Job 23:6 Would he contend with me in the greatness of his power ? No ; he would pay attention to me . |
| 40848 | 1142 | Job 26:3 | H7230 rov | SA |  | rov = adverbial quantifier (plentifully declared sound knowledge). Quantifier for speech; no inner state engaged by the term. | H8454 tu.shiy.yah (wisdom) [sound knowledge]; H3289 ya.ats (to advise) [counseled]; H3045 ya.da (to know) [declared]; H7230 rov (abundance) [plentifully] | Job 26:3 How you have counseled him who has no wisdom , and plentifully declared sound knowledge ! |
| 40849 | 1142 | Job 32:7 | H7230 rov | SA |  | rov = many (years), temporal quantifier. Time quantity; no inner-being content. | H3045 ya.da (to know) [teach]; H7230 rov (abundance) [many] | Job 32:7 I said , ‘Let days speak , and many years teach wisdom .’ |
| 40850 | 1142 | Job 33:19 | H7230 rov | G | 1142-001 |  | H4341 makh.ov (pain) [pain]; H7230 rov (abundance) [strife]; H0386 e.tan (strong) [continual]; H6106G e.tsem (bone) [bones] | Job 33:19 “Man is also rebuked with pain on his bed and with continual strife in his bones , |
| 40851 | 1142 | Job 35:9 | H7230 rov | G | 1142-001 |  | H7230 rov (abundance) [multitude]; H2220 ze.ro.a (arm) [arm]; H2199 za.aq (to cry out) [cry out] | Job 35:9 “ Because of the multitude of oppressions people cry out ; they call for help because of the arm of the mighty . |
| 40852 | 1142 | Job 37:23 | H7230 rov | G | 1142-001 |  | H6666 tse.da.qah (righteousness) [righteousness]; H4672 ma.tsa (to find) [find]; H7230 rov (abundance) [abundant]; H7706 shad.day (Almighty [God]) [Almighty]; H4941H mish.pat (justice) [justice]; H6031B a.nah (to afflict) [violate]; H3581B ko.ach (strength) [power] | Job 37:23 The Almighty —we cannot find him; he is great in power ; justice and abundant righteousness he will not violate . |
| 1133 | 111 | Psa 20:3 | H1878 da.shen | SA |  | da.shen = God's favorable regard/acceptance of the sacrifice. The term names divine reception of the offering; inner-being content of hope for acceptance belongs to the prayer act and other elements, not to da.shen as the primary term here. | H1878 da.shen (to prosper) [favor]; H2142 za.khar (to remember) [remember] | Psa 20:3 May he remember all your offerings and regard with favor your burnt sacrifices ! Selah |
| 58191 | 111 | Psa 23:5 | H1878 da.shen | G | 111-002 |  | H8081 she.men (oil) [oil]; H1878 da.shen (to prosper) [anoint]; H6887D tsa.rar (to vex) [enemies]; H6186A a.rakh (to arrange) [prepare]; H6186B a.rakh (to value) [prepare] | Psa 23:5 You prepare a table before me in the presence of my enemies ; you anoint my head with oil ; my cup overflows . |
| 219947 | 7010 | Psa 44:12 | H1952 hon | P |  |  | H7235A ra.vah (to multiply) [high]; H5971H am (People's [Gate]) [people]; H5971I am ([Ibleam]-am) [people]; H5971L am (people: creatures) [people]; H1952 hon (substance) [trifle] | Psa 44:12 You have sold your people for a trifle , demanding no high price for them. |
| 143932 | 1870 | Psa 45:13 | H3520B ke.vud.dah | G | 1870-001 |  | H3520A ka.vod (glorious) [glorious]; H3520B ke.vud.dah (riches) [glorious]; H4865 mish.be.tsot (filigree) [interwoven] | Psa 45:13 All glorious is the princess in her chamber , with robes interwoven with gold . |
| 219945 | 7010 | Psa 112:3 | H1952 hon | G | 7010-001 |  | H6666 tse.da.qah (righteousness) [righteousness]; H1952 hon (substance) [Wealth] | Psa 112:3 Wealth and riches are in his house , and his righteousness endures forever . |
| 219946 | 7010 | Psa 119:14 | H1952 hon | G | 7010-001 |  | H7797 su.s (to rejoice) [delight]; H5715 e.dut (testimony) [testimonies]; H1952 hon (substance) [riches] | Psa 119:14 In the way of your testimonies I delight as much as in all riches . |
| 219927 | 7010 | Pro 1:13 | H1952 hon | P |  |  | H4672 ma.tsa (to find) [find]; H1952 hon (substance) [goods] | Pro 1:13 we shall find all precious goods , we shall fill our houses with plunder ; |
| 219940 | 7010 | Pro 3:9 | H1952 hon | G | 7010-001 |  | H1952 hon (substance) [wealth] | Pro 3:9 Honor the Lord with your wealth and with the firstfruits of all your produce ; |
| 219943 | 7010 | Pro 6:31 | H1952 hon | UT |  |  | H4672 ma.tsa (to find) [caught]; H1952 hon (substance) [goods] | Pro 6:31 but if he is caught , he will pay sevenfold ; he will give all the goods of his house . |
| 219944 | 7010 | Pro 8:18 | H1952 hon | P |  |  | H3519 ka.vod (glory) [honor]; H6666 tse.da.qah (righteousness) [righteousness]; H1952 hon (substance) [wealth] | Pro 8:18 Riches and honor are with me, enduring wealth and righteousness . |
| 219928 | 7010 | Pro 10:15 | H1952 hon | P |  |  | H5797 oz (strength) [strong]; H4288 me.chit.tah (terror) [ruin]; H1952 hon (substance) [wealth] | Pro 10:15 A rich man’s wealth is his strong city ; the poverty of the poor is their ruin . |
| 219929 | 7010 | Pro 11:4 | H1952 hon | G | 7010-001 |  | H6666 tse.da.qah (righteousness) [righteousness]; H1952 hon (substance) [Riches]; H4194 ma.vet (death) [death] | Pro 11:4 Riches do not profit in the day of wrath , but righteousness delivers from death . |
| 1134 | 111 | Pro 11:25 | H1878 da.shen | G | 111-001 |  | H1878 da.shen (to prosper) [enriched]; H1293 be.ra.khah (blessing) [blessing]; H5315I ne.phesh (soul: myself) [Whoever]; H1571 gam (also) [watered] | Pro 11:25 Whoever brings blessing will be enriched , and one who waters will himself be watered . |
| 219930 | 7010 | Pro 12:27 | H1952 hon | P |  |  | H1952 hon (substance) [wealth] | Pro 12:27 Whoever is slothful will not roast his game , but the diligent man will get precious wealth . |
| 1135 | 111 | Pro 13:4 | H1878 da.shen | G | 111-001 |  | H1878 da.shen (to prosper) [richly supplied]; H0183 a.vah (to desire) [craves]; H6102 a.tsel (sluggish) [sluggard]; H5315G ne.phesh (soul) [soul] | Pro 13:4 The soul of the sluggard craves and gets nothing , while the soul of the diligent is richly supplied . |
| 219932 | 7010 | Pro 13:7 | H1952 hon | P |  |  | H1952 hon (substance) [wealth] | Pro 13:7 One pretends to be rich , yet has nothing ; another pretends to be poor , yet has great wealth . |
| 219931 | 7010 | Pro 13:11 | H1952 hon | P |  |  | H3027G yad (hand) [little]; H7235A ra.vah (to multiply) [increase]; H1952 hon (substance) [Wealth] | Pro 13:11 Wealth gained hastily will dwindle , but whoever gathers little by little will increase it. |
| 12790 | 681 | Pro 15:6 | H2633 cho.sen | G | 681-001 |  | H2633 cho.sen (wealth) [treasure]; H6662 tsad.diq (righteous) [righteous]; H7563 ra.sha (wicked) [wicked] | Pro 15:6 In the house of the righteous there is much treasure , but trouble befalls the income of the wicked . |
| 1136 | 111 | Pro 15:30 | H1878 da.shen | P |  |  | H1878 da.shen (to prosper) [refreshes]; H8055 sa.mach (to rejoice) [rejoices]; H3820A lev (heart) [heart]; H2896A tov (pleasant) [good]; H6106G e.tsem (bone) [bones] | Pro 15:30 The light of the eyes rejoices the heart , and good news refreshes the bones . |
| 219933 | 7010 | Pro 18:11 | H1952 hon | G | 7010-001 |  | H5797 oz (strength) [strong]; H4906 mas.kit (figure) [imagination]; H2346G cho.mah (wall) [wall]; H1952 hon (substance) [wealth] | Pro 18:11 A rich man’s wealth is his strong city , and like a high wall in his imagination . |
| 219935 | 7010 | Pro 19:4 | H1952 hon | P |  |  | H7453 re.a (neighbor) [friends]; H1952 hon (substance) [Wealth] | Pro 19:4 Wealth brings many new friends , but a poor man is deserted by his friend . |
| 219934 | 7010 | Pro 19:14 | H1952 hon | P |  |  | H7919A sa.khal (be prudent) [prudent]; H5159 na.cha.lah (inheritance) [inherited]; H1952 hon (substance) [wealth] | Pro 19:14 House and wealth are inherited from fathers , but a prudent wife is from the Lord . |
| 219936 | 7010 | Pro 24:4 | H1952 hon | P |  |  | H5273A na.im (pleasant) [pleasant]; H5273B na.im (musical) [pleasant]; H1847 da.at (knowledge) [knowledge]; H1952 hon (substance) [riches] | Pro 24:4 by knowledge the rooms are filled with all precious and pleasant riches . |
| 12791 | 681 | Pro 27:24 | H2633 cho.sen | G | 681-001 |  | H2633 cho.sen (wealth) [riches]; H5769G o.lam (forever: enduring) [forever]; H5145H ne.zer (consecration: crown) [crown] | Pro 27:24 for riches do not last forever ; and does a crown endure to all generations ? |
| 219938 | 7010 | Pro 28:8 | H1952 hon | P |  |  | H7235A ra.vah (to multiply) [multiplies]; H2603A cha.nan (be gracious) [generous]; H2603B cha.nan (be loathsome) [generous]; H1952 hon (substance) [wealth] | Pro 28:8 Whoever multiplies his wealth by interest and profit gathers it for him who is generous to the poor . |
| 219937 | 7010 | Pro 28:22 | H1952 hon | G | 7010-001 |  | H0926 ba.hal (to dismay) [hastens]; H3045 ya.da (to know) [know]; H1952 hon (substance) [wealth] | Pro 28:22 A stingy man hastens after wealth and does not know that poverty will come upon him . |
| 1137 | 111 | Pro 28:25 | H1878 da.shen | G | 111-001 |  | H1878 da.shen (to prosper) [enriched]; H5315J ne.phesh (soul: person) [man]; H0982 ba.tach (to trust) [trusts] | Pro 28:25 A greedy man stirs up strife , but the one who trusts in the Lord will be enriched . |
| 219939 | 7010 | Pro 29:3 | H1952 hon | G | 7010-001 |  | H8055 sa.mach (to rejoice) [glad]; H2181 za.nah (to fornicate) [prostitutes]; H1952 hon (substance) [wealth] | Pro 29:3 He who loves wisdom makes his father glad , but a companion of prostitutes squanders his wealth . |
| 219941 | 7010 | Pro 30:15 | H1952 hon | P |  |  | H2007 hen.nah (they [fem.]) [never]; H1952 hon (substance) [Enough] | Pro 30:15 The leech has two daughters : Give and Give . Three things are never satisfied ; four never say , “ Enough ”: |
| 219942 | 7010 | Pro 30:16 | H1952 hon | SA |  | hon = enough applied to physical phenomena (barren womb, land, fire). The insatiability is attributed to natural phenomena rather than the inner person directly; inner-being register is not the primary face of the term in this verse. | H7356A ra.cham (womb) [womb]; H6115 o.tser (coercion) [barren]; H1952 hon (substance) [Enough] | Pro 30:16 Sheol , the barren womb , the land never satisfied with water , and the fire that never says , “ Enough .” |
| 219948 | 7010 | Song 8:7 | H1952 hon | G | 7010-001 |  | H0160 a.ha.vah (love) [love]; H1952 hon (substance) [wealth] | Song 8:7 Many waters cannot quench love , neither can floods drown it. If a man offered for love all the wealth of his house , he would be utterly despised . |
| 40832 | 1142 | Isa 1:11 | H7230 rov | G | 1142-001 |  | H2654A cha.phets (to delight in) [delight]; H3808 lo (not) [not]; H7230 rov (abundance) [multitude]; H2654B cha.phats (to sway) [delight]; H0352C a.yil (leader) [rams]; H0352D a.yil (terebinth) [rams] | Isa 1:11 “ What to me is the multitude of your sacrifices ? says the Lord ; I have had enough of burnt offerings of rams and the fat of well-fed beasts ; I do not delight in the blood of bulls , or of lambs , or of goats . |
| 40842 | 1142 | Isa 7:22 | H7230 rov | SA |  | rov = abundance of milk (material food provision). Quantity of food; no inner-being engagement by this term. | H3605 kol (all) [everyone]; H7230 rov (abundance) [abundance] | Isa 7:22 and because of the abundance of milk that they give , he will eat curds , for everyone who is left in the land will eat curds and honey . |
| 40833 | 1142 | Isa 24:22 | H7230 rov | SA |  | rov = many days (temporal quantifier before punishment). Time quantity; no inner-being content. | H7230 rov (abundance) [many]; H5462 sa.gar (to shut) [shut up]; H6485H pa.qad (to reckon: punish) [punished]; H4525 mas.ger (locksmith) [prison] | Isa 24:22 They will be gathered together as prisoners in a pit ; they will be shut up in a prison , and after many days they will be punished . |
| 12792 | 681 | Isa 33:6 | H2633 cho.sen | G | 681-001 |  | H3374 yir.ah (fear) [fear]; H2633 cho.sen (wealth) [abundance]; H0530 e.mu.nah (faithfulness) [stability]; H1847 da.at (knowledge) [knowledge]; H3444 ye.shu.ah (salvation) [salvation] | Isa 33:6 and he will be the stability of your times , abundance of salvation , wisdom , and knowledge ; the fear of the Lord is Zion’s treasure . |
| 1138 | 111 | Isa 34:6 | H1878 da.shen | SA |  | da.shen = the divine sword gorged with fat (blood of sacrificial animals in judgment). No human inner-being characteristic engaged by the term. | H1878 da.shen (to prosper) [gorged]; H3629 kil.yah (kidney) [kidneys]; H0352C a.yil (leader) [rams]; H0352D a.yil (terebinth) [rams] | Isa 34:6 The Lord has a sword ; it is sated with blood ; it is gorged with fat , with the blood of lambs and goats , with the fat of the kidneys of rams . For the Lord has a sacrifice in Bozrah , a great slaughter in the land of Edom . |
| 1139 | 111 | Isa 34:7 | H1878 da.shen | SA |  | da.shen = land gorged with blood and fat in divine judgment. Physical land; no inner-being content. | H1878 da.shen (to prosper) [gorged] | Isa 34:7 Wild oxen shall fall with them, and young steers with the mighty bulls. Their land shall drink its fill of blood , and their soil shall be gorged with fat . |
| 40834 | 1142 | Isa 37:24 | H7230 rov | G | 1142-001 |  | H4791 ma.rom (height) [heights]; H2778A cha.raph (to taunt) [mocked]; H3772G ka.rat (to cut: cut) [cut down]; H0589 a.ni (I) [gone up]; H7230 rov (abundance) [many]; H0935G bo (to come [in]: come) [come]; H0136 a.do.na (Lord [God]) [Lord]; H3027J yad (hand: by) [By]; H6967 qo.mah (height) [tallest] | Isa 37:24 By your servants you have mocked the Lord , and you have said , With my many chariots I have gone up the heights of the mountains , to the far recesses of Lebanon , to cut down its tallest cedars , its choicest cypresses , to come to its remotest height , its most fruitful forest . |
| 40835 | 1142 | Isa 40:26 | H7230 rov | G | 1142-001 |  | H4791 ma.rom (height) [high]; H0202 on (strength) [might]; H7121G qa.ra (to call: call to) [calling]; H4310 mi (who?) [who]; H7200G ra.ah (to see: see) [see]; H7230 rov (abundance) [greatness]; H8034 shem (name) [name]; H6635A tsa.va (army) [host]; H0533 am.mits (strong) [strong]; H3581B ko.ach (strength) [power] | Isa 40:26 Lift up your eyes on high and see : who created these ? He who brings out their host by number , calling them all by name ; by the greatness of his might and because he is strong in power , not one is missing . |
| 40838 | 1142 | Isa 47:9 | H7230 rov | G | 1142-001 |  | H6109 ots.mah (strength) [power]; H8537 tom (integrity) [full measure]; H0259 e.chad (one) [one]; H7230 rov (abundance) [many]; H3966 me.od (much) [great]; H3785 ke.sheph (sorcery) [sorceries] | Isa 47:9 These two things shall come to you in a moment , in one day ; the loss of children and widowhood shall come upon you in full measure , in spite of your many sorceries and the great power of your enchantments . |
| 40836 | 1142 | Isa 47:12 | H7230 rov | G | 1142-001 |  | H6206 a.rats (to tremble) [inspire terror]; H4994 na (please) [Stand fast]; H7230 rov (abundance) [many]; H0194 u.lay (perhaps) [perhaps]; H3201 ya.khol (be able) [able]; H3785 ke.sheph (sorcery) [sorceries] | Isa 47:12 Stand fast in your enchantments and your many sorceries , with which you have labored from your youth ; perhaps you may be able to succeed ; perhaps you may inspire terror . |
| 40837 | 1142 | Isa 47:13 | H7230 rov | G | 1142-001 |  | H3811 la.ah (be weary) [wearied]; H6098 e.tsah (counsel) [counsels]; H4994 na (please) [stand forth]; H3045 ya.da (to know) [known]; H7230 rov (abundance) [many] | Isa 47:13 You are wearied with your many counsels ; let them stand forth and save you, those who divide the heavens , who gaze at the stars , who at the new moons make known what shall come upon you . |
| 40839 | 1142 | Isa 57:10 | H7230 rov | G | 1142-001 |  | H2976 ya.ash (to despair) [hopeless]; H4672 ma.tsa (to find) [found]; H7230 rov (abundance) [length]; H3027H yad (hand: power) [strength]; H2416C chay.yah (living thing) [life] | Isa 57:10 You were wearied with the length of your way , but you did not say , “It is hopeless ”; you found new life for your strength , and so you were not faint . |
| 40840 | 1142 | Isa 63:1 | H7230 rov | G | 1142-001 |  | H0589 a.ni (I) [I]; H4310 mi (who?) [Who]; H6666 tse.da.qah (righteousness) [righteousness]; H7230 rov (abundance) [greatness]; H1921 ha.dar (to honor) [splendid]; H3581B ko.ach (strength) [strength] | Isa 63:1 Who is this who comes from Edom , in crimsoned garments from Bozrah , he who is splendid in his apparel , marching in the greatness of his strength ? “ It is I , speaking in righteousness , mighty to save .” |
| 40841 | 1142 | Isa 63:7 | H7230 rov | G | 1142-001 |  | H2617A che.sed (kindness) [steadfast love]; H7356B ra.cha.mim (compassion) [compassion]; H8416 te.hil.lah (praise) [praises]; H7230 rov (abundance) [abundance]; H2142 za.khar (to remember) [recount]; H2617B che.sed (shame) [steadfast love] | Isa 63:7 I will recount the steadfast love of the Lord , the praises of the Lord , according to all that the Lord has granted us, and the great goodness to the house of Israel that he has granted them according to his compassion , according to the abundance of his steadfast love . |
| 40843 | 1142 | Jer 13:22 | H7230 rov | G | 1142-001 |  | H3824 le.vav (heart) [heart]; H7230 rov (abundance) [greatness]; H5771G a.von (iniquity: crime) [iniquity]; H7122I qa.ra (to encounter: chanced) [come upon]; H4069 mad.du.a (why?) [Why] | Jer 13:22 And if you say in your heart , ‘ Why have these things come upon me?’ it is for the greatness of your iniquity that your skirts are lifted up and you suffer violence . |
| 12793 | 681 | Jer 20:5 | H2633 cho.sen | SA |  | cho.sen = wealth of the city as object of divine judgment and enemy plunder. Material wealth being transferred; no inner-being state named or engaged by the term in this verse. | H2633 cho.sen (wealth) [wealth]; H3027H yad (hand: power) [hand]; H0341 o.yev (enemy) [enemies] | Jer 20:5 Moreover, I will give all the wealth of the city , all its gains , all its prized belongings , and all the treasures of the kings of Judah into the hand of their enemies , who shall plunder them and seize them and carry them to Babylon . |
| 40844 | 1142 | Jer 30:14 | H7230 rov | G | 1142-001 |  | H1875 da.rash (to seek) [care]; H7230 rov (abundance) [great]; H5771H a.von (iniquity: guilt) [guilt]; H2403B chat.tat (sin) [sins]; H6105A a.tsom (be vast) [flagrant]; H6105B a.tsam (to shut eyes) [flagrant]; H0394 akh.za.ri (cruel) [merciless foe]; H0341 o.yev (enemy) [enemy] | Jer 30:14 All your lovers have forgotten you; they care nothing for you; for I have dealt you the blow of an enemy , the punishment of a merciless foe , because your guilt is great , because your sins are flagrant . |
| 40845 | 1142 | Jer 30:15 | H7230 rov | G | 1142-001 |  | H4341 makh.ov (pain) [pain]; H7667 she.ver (breaking) [hurt]; H7230 rov (abundance) [great]; H5771H a.von (iniquity: guilt) [guilt]; H2403B chat.tat (sin) [sins]; H2199 za.aq (to cry out) [cry out]; H6105A a.tsom (be vast) [flagrant]; H6105B a.tsam (to shut eyes) [flagrant] | Jer 30:15 Why do you cry out over your hurt ? Your pain is incurable . Because your guilt is great , because your sins are flagrant , I have done these things to you . |
| 40856 | 1142 | Lam 1:3 | H7230 rov | G | 1142-001 |  | H4712 me.tsar (terror) [distress]; H6040 o.ni (affliction) [affliction]; H4672 ma.tsa (to find) [finds]; H7230 rov (abundance) [hard]; H4494 ma.no.ach (resting) [resting place]; H5656G a.vo.dah (service) [servitude] | Lam 1:3 Judah has gone into exile because of affliction and hard servitude ; she dwells now among the nations , but finds no resting place ; her pursuers have all overtaken her in the midst of her distress . |
| 40857 | 1142 | Lam 1:5 | H7230 rov | G | 1142-001 |  | H6862C tsar (enemy) [foes]; H3013 ya.gah (to suffer) [afflicted]; H6588 pe.sha (transgression) [transgressions]; H7230 rov (abundance) [multitude]; H0341 o.yev (enemy) [enemies] | Lam 1:5 Her foes have become the head ; her enemies prosper , because the Lord has afflicted her for the multitude of her transgressions ; her children have gone away, captives before the foe . |
| 40858 | 1142 | Lam 3:32 | H7230 rov | G | 1142-001 |  | H3013 ya.gah (to suffer) [cause grief]; H2617A che.sed (kindness) [steadfast love]; H7355 ra.cham (to have compassion) [compassion]; H7230 rov (abundance) [abundance]; H2617B che.sed (shame) [steadfast love] | Lam 3:32 for , though he cause grief , he will have compassion according to the abundance of his steadfast love ; |
| 12794 | 681 | Eze 22:25 | H2633 cho.sen | G | 681-001 |  | H2633 cho.sen (wealth) [treasure]; H5315H ne.phesh (soul: life) [lives]; H7235A ra.vah (to multiply) [many]; H7580 sha.ag (to roar) [roaring]; H2963 ta.raph (to tear) [tearing]; H2964 te.reph (prey) [prey] | Eze 22:25 The conspiracy of her prophets in her midst is like a roaring lion tearing the prey ; they have devoured human lives ; they have taken treasure and precious things ; they have made many widows in her midst . |
| 143931 | 1870 | Eze 23:41 | H3520B ke.vud.dah | G | 1870-001 |  | H8081 she.men (oil) [oil]; H3520A ka.vod (glorious) [stately]; H3520B ke.vud.dah (riches) [stately]; H6186A a.rakh (to arrange) [spread]; H6186B a.rakh (to value) [spread] | Eze 23:41 You sat on a stately couch , with a table spread before it on which you had placed my incense and my oil . |
| 219923 | 7010 | Eze 27:12 | H1952 hon | SA |  | hon = commercial material wealth of Tyre. Commercial exchange context; no inner-being characteristic engaged by the term. | H1952 hon (substance) [wealth] | Eze 27:12 “ Tarshish did business with you because of your great wealth of every kind; silver , iron , tin , and lead they exchanged for your wares . |
| 219924 | 7010 | Eze 27:18 | H1952 hon | SA |  | hon = commercial wealth of Tyre (Damascus trade). Same pattern as Eze 27:12; commercial material wealth only. | H1952 hon (substance) [wealth] | Eze 27:18 Damascus did business with you for your abundant goods , because of your great wealth of every kind; wine of Helbon and wool of Sahar |
| 219925 | 7010 | Eze 27:27 | H1952 hon | SA |  | hon = riches sinking with Tyre. Material commercial goods lost in catastrophe; no inner-being content. | H2388G cha.zaq (to strengthen: strengthen) [caulkers]; H1952 hon (substance) [riches]; H2259 cho.vel (pilot) [pilots] | Eze 27:27 Your riches , your wares , your merchandise , your mariners and your pilots , your caulkers , your dealers in merchandise , and all your men of war who are in you, with all your crew that is in your midst , sink into the heart of the seas on the day of your fall . |
| 219926 | 7010 | Eze 27:33 | H1952 hon | SA |  | hon = abundant commercial wealth enriching kings. Commercial material wealth; no inner-being content. | H1952 hon (substance) [wealth] | Eze 27:33 When your wares came from the seas , you satisfied many peoples ; with your abundant wealth and merchandise you enriched the kings of the earth . |
| 40830 | 1142 | Hos 8:12 | H7230 rov | SA |  | rov = ten thousands (quantity of laws written). Quantitative amplifier for divine instruction; inner-being content of estrangement is carried by other terms in the verse, not by rov. | H7230 rov (abundance) [for him]; H3644G ke.mo (like) [strange]; H2803H cha.shav (to devise: count) [regarded] | Hos 8:12 Were I to write for him my laws by the ten thousands, they would be regarded as a strange thing. |
| 40831 | 1142 | Hos 9:7 | H7230 rov | P |  |  | H5030 na.vi (prophet) [prophet]; H4895 mas.te.mah (hatred) [hatred]; H3045 ya.da (to know) [know]; H7230 rov (abundance) [great]; H0935G bo (to come [in]: come) [come]; H5771G a.von (iniquity: crime) [iniquity]; H6486 pe.qud.dah (punishment) [punishment]; H7696 sha.ga (be mad) [mad]; H0191 e.vil (fool[ish]) [fool] | Hos 9:7 The days of punishment have come ; the days of recompense have come ; Israel shall know it. The prophet is a fool ; the man of the spirit is mad , because of your great iniquity and great hatred . |
| 40828 | 1142 | Hos 10:1 | H7230 rov | G | 1142-001 |  | H3190 ya.tav (be good) [improved]; H7230 rov (abundance) [increased]; H7235A ra.vah (to multiply) [built]; H7737B sha.vah (to set) [yields] | Hos 10:1 Israel is a luxuriant vine that yields its fruit . The more his fruit increased , the more altars he built ; as his country improved , he improved his pillars . |
| 40829 | 1142 | Hos 10:13 | H7230 rov | G | 1142-001 |  | H1368 gib.bor (mighty man) [warriors]; H7562 re.sha (wickedness) [iniquity]; H7230 rov (abundance) [multitude]; H2790A cha.rash (to plow/plot) [plowed]; H0982 ba.tach (to trust) [trusted]; H7114B qa.tsar (to reap) [reaped]; H5766B av.lah (injustice) [injustice] | Hos 10:13 You have plowed iniquity ; you have reaped injustice ; you have eaten the fruit of lies . Because you have trusted in your own way and in the multitude of your warriors , |
| 40860 | 1142 | Nah 3:3 | H7230 rov | SA |  | rov = multitude/hosts of slain. Quantity of corpses in battle description; no inner-being content. | H7230 rov (abundance) [hosts]; H3514 ko.ved (heaviness) [heaps]; H2491A cha.lal (slain: killed) [slain]; H2491B cha.lal (profaned) [slain] | Nah 3:3 Horsemen charging , flashing sword and glittering spear , hosts of slain , heaps of corpses , dead bodies without end — they stumble over the bodies ! |
| 40861 | 1142 | Nah 3:4 | H7230 rov | G | 1142-001 |  | H2896A tov (pleasant) [and]; H2580 chen (favor) [graceful]; H7230 rov (abundance) [countless]; H2183 ze.nu.nim (fornication) [whorings]; H2181 za.nah (to fornicate) [prostitute]; H1172 ba.a.lah (mistress) [of]; H3785 ke.sheph (sorcery) [charms] | Nah 3:4 And all for the countless whorings of the prostitute , graceful and of deadly charms , who betrays nations with her whorings , and peoples with her charms . |

<a id="s3"></a>
## §3. Per-term comprehensive detail

Each term gets numbered sections: identity • meaning • anchor-verse linkages • groups • findings • pointers • auxiliary data. Verses are not repeated here — they are listed by sub-group in §2. Items linked only by registry are summarised here; exhaustive lists are in the appendix §4.

---

<a id="t-H7230"></a>
### H7230 rov — abundance (`mti_id=1142`)

**Identity & meaning**

1. Strong's: `H7230` · Lang: Hebrew · Owner: OWNER
2. Registry: R152 strife · Legacy C-cluster: C18
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 152
5. Patch-authoring refs: `mti_id=1142` · `md_version=2` · `vc_status=vc_completed`

**Verses:** 41 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 2213 | 1142-001 | Term names abundance or greatness applied to inner-moral realities — the weight or magnitude of iniquity, steadfast love, pride, or spiritual failure, shaping the inner relationship between the person and God |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (2 unique)**

| Finding ID | Type | Matched anchor refs | Excerpt |
|---|---|---|---|
| OBS-062-T2-251 | OBSERVATION | Isa 47:9 | The occult-charming groups (H2267 — spell/charmer; Psa 58:5, Isa 47:9) involve the use of fellowship vocabulary in relation to non-human spiritual forces — charms are a form of joining with occult power. This is the nearest evidence of fellowship operating in relation to spiritual beings. OBS-062-024, OBS-062-035. |
| OBS-060-T2-064 | OBSERVATION | Neh 9:25 | The characteristic deepens memory in its covenantal mode: the accumulated record of divine giving across generations forms the memory-structure of Israel's inner-being identity. Each new giving adds to the memory of prior giving, deepening the narrative foundation of trust. Neh 9 (the long Levitical prayer) is itself a memory-act: reciting the history of divine giving as the basis of present covenantal renewal. Hos 2:15 invokes Exodus memory as the ground of eschatological hope — the memory of what God gave before shapes the expectation of what he will give again. The characteristic does not impair memory in any evidenced instance; it is constitutively tied to the faithfulness of remembered giving. |

**SD pointers — direct (1)**

| Pointer | Priority | Strong's ref | Description |
|---|---|---|---|
| DIM-152-SD001 | MEDIUM | H7230 | rov (H7230, abundance) in the strife registry (group 1142-001) is assigned Divine-Human Correspondence because both anchors have GOD as subject (divine weariness of ritual; divine steadfast love) while related verses carry the human moral-failure pole. This raises a programme-level question: does the biblical vocabulary of magnitude (rov, rabah, and cognates) consistently operate in divine-human correspondence mode — the greatness of divine attributes set against and corresponding to the weight of human moral condition? Session D should examine this across all registries where magnitude vocabulary appears. |

**Auxiliary data**

_Root family (1):_

1. `ROV` (Hebrew): abundance

_Related words (14):_

1. H3379G ya.ra.ve.am → Jeroboam
2. H3379H ya.ra.ve.am → Jeroboam
3. H7227A rav → many
4. H7227B rav → chief
5. H7227G rav → [Sidon] the Great
6. H7231 ra.vav → to multiply
7. H7233 re.va.vah → myriad
8. H7237 rab.bah → Rabbah
9. H7239 rib.bo → ten thousand
10. H7241 re.vi.vim → shower
11. H7245 rab.bit → Rabbith
12. H7249G rav-sa.ris → Rab-saris
13. H7249H rav-sa.ris → Rab-saris
14. H7262 rav.sha.qeh → Rabshakeh

_Data-quality flags (1):_

1. flag_id=4 · meaning field is null for H7230. STEP returned no word analysis block for this term.

---

<a id="t-H1952"></a>
### H1952 hon — substance (`mti_id=7010`)

**Identity & meaning**

1. Strong's: `H1952` · Lang: Hebrew · Owner: OWNER
2. Registry: R187 strength · Legacy C-cluster: C20
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 26
5. Patch-authoring refs: `mti_id=7010` · `md_version=2` · `vc_status=vc_completed`

**Verses:** 26 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 2933 | 7010-001 | Hon as wealth in its relation to inner-being orientation and moral condition |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Related words (2):_

1. H0202 on → strength
2. H1951 hun → be ready

_Data-quality flags (1):_

1. flag_id=4 · meaning field is null for H1952. STEP returned no word analysis block for this term.

---

<a id="t-H1878"></a>
### H1878 da.shen — to prosper (`mti_id=111`)

**Identity & meaning**

1. Strong's: `H1878` · Lang: Hebrew · Owner: OWNER
2. Registry: R006 anointing · Legacy C-cluster: C16
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 11
5. Patch-authoring refs: `mti_id=111` · `md_version=2` · `vc_status=vc_completed`

**Verses:** 11 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (2)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 50 | 111-001 | Term names the inner refreshment of the satisfied soul — the prosperity and fat-richness of the inner person whose desire is fulfilled |  |
| 51 | 111-002 | Term names the anointing that signals divine presence and favour — the saturation of the head with oil as the emblem of divine blessing upon the inner person |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `DSN` (None): 

_Related words (8):_

1. None da.shen → fat
2. None de.shen → ashes
3. None dat → law
4. H1881 dat → law
5. H1886 do.tan → Dothan
6. H1885 da.tan → Dathan
7. H1879 da.shen → fat
8. H1880 de.shen → ashes

_Data-quality flags (2):_

1. flag_id=3 · Low occurrence count: 11. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=4 · meaning field is null for H1878. STEP returned no word analysis block for this term.

---

<a id="t-H2633"></a>
### H2633 cho.sen — wealth (`mti_id=681`)

**Identity & meaning**

1. Strong's: `H2633` · Lang: Hebrew · Owner: OWNER
2. Registry: R187 strength · Legacy C-cluster: C20
3. Sub-group: —
4. Term status: extracted · Evidential: — · Occurrences: 5
5. Patch-authoring refs: `mti_id=681` · `md_version=2` · `vc_status=vc_completed`

**Verses:** 5 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 2957 | 681-001 | Term names wealth/treasure as a moral category — where the inner character of the person determines whether wealth becomes blessing or snare | Revised during Dimension Review Phase B: VCB-022 patch truncated context_description at 80 characters. Full description restored from wa-vcb-022-term-observations-v2.8-20260404.md |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `CHOSEN_ROOT` (None): 

_Related words (7):_

1. None cha.sin → mighty
2. None cha.san → to hoard
3. None cha.son → strong
4. H2634 cha.son → strong
5. H2636 chas.pas → to peel
6. H2630 cha.san → to hoard
7. H2626 cha.sin → mighty

_Data-quality flags (3):_

1. flag_id=3 · Low occurrence count: 5. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=4 · meaning field is null for H2633. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for H2633 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="t-H3520B"></a>
### H3520B ke.vud.dah — riches (`mti_id=1870`)

**Identity & meaning**

1. Strong's: `H3520B` · Lang: Hebrew · Owner: OWNER
2. Registry: R015 boastfulness · Legacy C-cluster: C09
3. Sub-group: —
4. Term status: extracted_thin · Evidential: — · Occurrences: 1
5. Patch-authoring refs: `mti_id=1870` · `md_version=1` · `vc_status=not_done`

**Verses:** 2 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 3422 | 1870-001 | Term names material richness or splendour as the setting in which inner spiritual orientation — faithfulness or its corruption toward God — is enacted or exposed |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `KAVED` (Hebrew): liver

_Related words (30):_

1. H3513G ka.ved → to honor: honour
2. H3513H ka.ved → to honor: heavy
3. H3513I ka.ved → to honor: many
4. H3513J ka.ved → to honor: dull
5. H3514 ko.ved → heaviness
6. H3515 ka.ved → heavy
7. H3516 ka.ved → liver
8. H3517 ke.ve.dut → heaviness
9. H3519 ka.vod → glory
10. H3520A ka.vod → glorious
11. H3513G ka.ved → to honor: honour
12. H3513H ka.ved → to honor: heavy
13. H3513I ka.ved → to honor: many
14. H3513J ka.ved → to honor: dull
15. H3514 ko.ved → heaviness
16. H3515 ka.ved → heavy
17. H3516 ka.ved → liver
18. H3517 ke.ve.dut → heaviness
19. H3519 ka.vod → glory
20. H3520A ka.vod → glorious
21. H3513G ka.ved → to honor: honour
22. H3513H ka.ved → to honor: heavy
23. H3513I ka.ved → to honor: many
24. H3513J ka.ved → to honor: dull
25. H3514 ko.ved → heaviness
26. H3515 ka.ved → heavy
27. H3516 ka.ved → liver
28. H3517 ke.ve.dut → heaviness
29. H3519 ka.vod → glory
30. H3520A ka.vod → glorious

_Data-quality flags (9):_

1. flag_id=3 · Only 2 confirmed verse records for H3520B. Threshold is 5.
2. flag_id=4 · meaning field is null for H3520B. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for H3520B stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 2 confirmed verse records for H3520B. Threshold is 5.
5. flag_id=4 · meaning field is null for H3520B. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for H3520B stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
7. flag_id=3 · Only 2 confirmed verse records for H3520B. Threshold is 5.
8. flag_id=4 · meaning field is null for H3520B. STEP returned no word analysis block for this term.
9. flag_id=47 · Meaning for H3520B stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

<a id="s4"></a>
## §4. Appendix — items linked at registry or collection level

<a id="s4-1"></a>
### §4.1 Findings from contributor registries with no term-level link (4)

These findings sit on a registry that contributes terms to this cluster, but their text and anchor verses don't resolve to any specific cluster term. Candidates for term-level enrichment.

| Finding ID | Type | Registry | Anchor verses | Excerpt |
|---|---|---|---|---|
| DIM-187-001 | DIMENSION_REVIEW | R187 strength | 1 Sam 15:22 | Group 7013-001 (a.yil, ram) carries a verse-level valuation in which obedience (H8085H sha.ma) and attentive listening (H7181 qashav) are declared greater than sacrifice — greater than the fat of rams (1 Sam 15:22). Neither term is an OWNER in Registry 187; their inner-being weight is present in the verse but unregistered in the programme. Session B for Registry 187 should explore: (1) what the comparative structure of 1 Sam 15:22 reveals about the hierarchy of inner-being orientations toward God — obedience and attentive listening as the higher register; (2) how this valuation relates to the strength/capacity cluster's broader understanding of inner-being agency before God; (3) the relationship between sha.ma and qashav as paired inner-being acts that together constitute the responsive orientation of the person toward God. |
| DIM-6-001 | DIMENSION_REVIEW | R006 anointing |  | Registry 6 (anointing) spans 7 dimensions across 38 groups — the widest dimensional range in C16. Session B should examine whether this breadth coheres around a unifying theme (Spirit-mediated transformation and divine endowment) or represents genuinely distinct inner-being phenomena requiring separate analytical threads. |
| DIM-6-002 | DIMENSION_REVIEW | R006 anointing |  | Multiple Transformation groups in Reg 6 have GOD as dominant subject (167-001, 179-002, 4697-001, 4701-001, 4701-002). Session B should explore the full theology of God-initiated inner transformation in the anointing vocabulary — spanning Spirit-impartation, forgiveness, restoration, eschatological renewal, and judicial dulling/hardening as distinct expressions of the same divine transforming agency. |
| DIM-15-001 | DIMENSION_REVIEW | R015 boastfulness |  | The ka.vod (glory) vocabulary in Reg 15 (boastfulness) contains its own internal corrective: divine glory (1861-001) as the proper object of inner awe, and the human act of directing glory toward God (1861-002) as the antidote to boastfulness that claims glory for itself. Session B should examine how the glory vocabulary frames the proper and improper objects of inner honour — why the same word (kavod) names both human boastfulness and divine majesty, and what this reveals about the inner-being structure of worship. |

<a id="s4-2"></a>
### §4.2 SD pointers from contributor registries with no term-level link (10)

| Pointer | Priority | Strong's ref | Description |
|---|---|---|---|
| DIM-187-SD001 | HIGH |  | Programme-level registry validation gap identified during C20 Dimension Review (2026-04-08). Root cause: STEP Bible treats suffix variants of a root (e.g. H8085G vs H8085H for sha.ma) as sub-glosses rather than as independently linked related terms. The Session A extraction pipeline follows STEP's relational architecture and consequently does not surface sub-gloss variants as candidates for independent extraction. H8085H (sha.ma — to hear/obey) was not extracted; H7181 (qashav — to attend/listen) was extracted but STEP shows its related-word set as identical to H8085G, masking the sha.ma/qashav relationship. These are foundational inner-being terms — the hearing/obeying and attending/listening cluster is central to the biblical account of the inner person's orientation toward God. Session D must initiate a backward validation sweep: for every registered term, check whether its STEP sub-gloss variants were independently assessed for extraction eligibility. Priority: terms where the H/G/I suffix pattern produces distinct semantic content. This sweep should be scoped and executed before Session D synthesis conclusions are drawn on the hearing/obeying dimension. |
| DIM-187-SD002 | MEDIUM |  | The oikos/oikia family in Reg 187 generates groups across at least seven distinct inner-being dimensions (Moral Character, Transformation, Agency/Power, Relational Disposition, Volition, Divine-Human Correspondence, Vitality/Existence). The household vocabulary functions as a structural metaphor for the inner life rather than naming a single characteristic. Session D should assess whether the household/dwelling family constitutes a distinct metaphorical register in the biblical account of the inner person. |
| DIM-187-SD003 | MEDIUM |  | The AMTS root family (am.mits, am.tsah, o.mets in Reg 187) is closely cognate with the CHAZAQ family (Reg 33/C08) in the biblical courage formula chazaq ve-amats (be strong and courageous). The split of these two roots across C08 (courage, verb forms) and C20 (strength, adjective/noun forms) is analytically significant. Session D should synthesise the full courage formula by reading the C08 and C20 groups together, addressing the verb/adjective split within the same root complex. |
| DIM-187-SD004 | MEDIUM |  | The directionally-determined pattern appears with particular density in C20 strength vocabulary. The same Hebrew root generates groups in opposite registers — divine greatness and human pride (GADAL), strength as divine gift and strength as misplaced trust (OZ, KO.ACH, CHAYIL), sure-footedness and collapse (TSAV). This pattern, established as a structural principle across earlier clusters, is most concentrated in C20. Session D should assess whether the strength/power cluster adds a specific contribution to the directionally-determined principle beyond what C08 (virtue/vice) and C09 (pride/majesty) already established. |
| DIM-068-SD003 | MEDIUM |  | C20 power cluster dimension overlap: strength (187), power (196), authority (197), might (198), dominion (199) — all share all 3 grace dimensions (Relational Disposition 9 groups, Moral Character 1, Dependence/Creatureliness 1). 2Cor 12:9 makes the structural connection explicit: power made perfect in weakness, grace as its modality. Session D should examine whether grace consistently names the relational mode through which divine power reaches the creature precisely where human power fails, and whether Dependence/Creatureliness is the inner condition that opens the person to both grace and power. |
| DIM-111-SD001 | HIGH |  | Strength/power/authority/dominion registries (Reg 187/196/197/198/199) share all 4 of mercy dimensions. Structural question: is mercy the moral direction of power toward the vulnerable? Session D to examine whether power and mercy form a structural inner-being pair. |
| DIM-103-SD026 | MEDIUM | G0025 | C20 cluster (strength/might/authority/dominion — Regs 187/198/197/199) shares all 8 dimensions with love and co-occurs in 69-105 verses. This may be a registry-breadth effect, but the co-occurrence is genuine and large. Question: does the biblical vocabulary connect love and power structurally? Is love the form that power takes in the kingdom of God, and power the form that love takes in creation? The 1Cor 13 sequence — love as greater than gifts of power and knowledge — suggests love and power are in deliberate tension in the NT. |
| DIM-064-SD019 | MEDIUM | G0859 | 19 shared verses between forgiveness (064) and strength (187) is the second-highest cooccurrence signal in this registry's corpus. The forgiveness passages frequently invoke divine power, exaltation, and authority in the same context as forgiveness: Acts 5:31 ('God exalted him at his right hand as Leader and Savior to give repentance and forgiveness of sins'), Num 14:19 ('according to the greatness of your steadfast love'). Session D question: does the programme's strength/power cluster (C20) address the relationship between divine omnipotence and the capacity to forgive at the scale Scripture describes? Is there an inner-being statement about divine power embedded in the forgiveness corpus that the C20 synthesis should address? Confirmed by 19 shared verses (strongest unexpected cooccurrence signal in this registry). |
| DIM-6-SD001 | MEDIUM |  | C16 contains a substantial concentration of GOD-dominant Agency/Power and Transformation groups across anointing, consecration, and blessing — God appointing, transforming, restoring, forgiving, and blessing as inner-being acts directed toward the human person. Session D should synthesise how God's inner-being activity toward persons is distributed across the full programme and whether C16 represents a distinct domain of divine inner-being engagement (endowment/consecration) distinguishable from other clusters. |
| DIM-068-SD016 | LOW |  | Anointing (Reg 6, C16) and blessing (Reg 194, C16) cooccurrence: 7 verses each. Grace co-occurs with both C16 registries at the same level, suggesting a possible C16-C17 connection zone. Anointing, blessing, and grace may constitute a semantic network of divine bestowal — each naming a distinct modality through which the divine disposition of favour is concretely extended to the creature. Session D should examine whether grace, anointing, and blessing share a common inner-being ground (the creature as recipient of divine favour) and what distinguishes them: grace as relational disposition freely given; blessing as the concrete content of what is given; anointing as the specific act of set-apart conferral. |

<a id="s4-3"></a>
### §4.3 Prose sections from contributor registries (0)

(none)

<a id="s4-4"></a>
### §4.4 Cluster-internal verse_context_group rows (6)

Deduplicated list of all `verse_context_group` rows that appear in this cluster (post-M47: a vcg may be linked to multiple terms via `vcg_term`; the Strong's column is a comma-joined list of all linked terms).

| Group ID | Code | Strong's (linked terms) | Description | Notes |
|---|---|---|---|---|
| 50 | 111-001 | H1878 | Term names the inner refreshment of the satisfied soul — the prosperity and fat-richness of the inner person whose desire is fulfilled |  |
| 51 | 111-002 | H1878 | Term names the anointing that signals divine presence and favour — the saturation of the head with oil as the emblem of divine blessing upon the inner person |  |
| 2213 | 1142-001 | H7230 | Term names abundance or greatness applied to inner-moral realities — the weight or magnitude of iniquity, steadfast love, pride, or spiritual failure, shaping the inner relationship between the person and God |  |
| 3422 | 1870-001 | H3520B | Term names material richness or splendour as the setting in which inner spiritual orientation — faithfulness or its corruption toward God — is enacted or exposed |  |
| 2957 | 681-001 | H2633 | Term names wealth/treasure as a moral category — where the inner character of the person determines whether wealth becomes blessing or snare | Revised during Dimension Review Phase B: VCB-022 patch truncated context_description at 80 characters. Full description restored from wa-vcb-022-term-observations-v2.8-20260404.md |
| 2933 | 7010-001 | H1952 | Hon as wealth in its relation to inner-being orientation and moral condition |  |

<a id="s4-5"></a>
### §4.5 Cross-cluster orphan findings/pointers

Findings + SD pointers that mention M-cluster vocabulary but originate from registries that do NOT contribute terms to this cluster — see [wa-cluster-m46-finding-orphans-v1-…](../../../outputs/markdown/) for the full scan.

